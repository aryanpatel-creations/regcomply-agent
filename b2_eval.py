"""RAG evaluation harness.

  python b2_eval.py --name bm25_300w --retriever bm25 --retrieval-only     (fast, no model calls)
  python b2_eval.py --name hybrid_300w --retriever hybrid                  (full run with answers + judge)

Golden set (eval/golden.jsonl), one question per line:
{"id": "q001", "question": "...", "in_scope": true, "gold_sections": ["RBIOS2026:10"], "reference": "..."}
"""
import argparse, csv, json, os, statistics, time
from pydantic import BaseModel, Field
import config
from retrieval import load_retriever

ANSWER_SYSTEM = ("You answer questions about RBI rules for bank complaint staff. Use ONLY the context. "
                 "Cite the chunk_id of every passage you use. If the context does not answer the question, "
                 "set refused=true and say you cannot find it in the rules.")
JUDGE_SYSTEM = ("You check whether an answer is fully supported by the context. "
                "If the facts in the answer are directly confirmed by the context, set fully_supported=true and unsupported_claims=[]. "
                "Only list claims in unsupported_claims if they are NOT mentioned or are contradicted by the context. Be fair and accurate.")


class Answer(BaseModel):
    answer: str
    cited_chunk_ids: list[str] = Field(default_factory=list)
    refused: bool = False

class Judgement(BaseModel):
    fully_supported: bool = Field(description="True if the answer is supported by the context, False if it contains ungrounded claims")
    unsupported_claims: list[str] = Field(default_factory=list, description="List of ungrounded or contradictory claims, empty if fully supported")


def section_key(chunk: dict) -> str:
    return f'{chunk["doc_id"]}:{chunk["section"]}'          # match at section level, not chunk level


def retrieval_metrics(hits: list[dict], gold: list[str]) -> dict:
    found = [section_key(h) for h in hits]
    first = next((i + 1 for i, s in enumerate(found) if s in gold), None)
    return {"hit": int(first is not None),
            "recall": len(set(found) & set(gold)) / len(gold),
            "rr": 1 / first if first else 0.0}


def context_block(hits: list[dict]) -> str:
    return "\n\n".join(f'[{h["chunk_id"]}] {h["text"]}' for h in hits)


def run(name: str, mode: str, k: int, retrieval_only: bool, golden: str = "eval/golden.jsonl") -> dict:
    from llm import chat_json                                  # imported here so retrieval-only needs no model
    retriever = load_retriever(mode)
    os.makedirs("eval/runs", exist_ok=True)
    out_path = f"eval/runs/{name}.jsonl"
    existing_ids = set()
    rows = []
    if os.path.exists(out_path):
        for l in open(out_path, encoding="utf-8"):
            if l.strip():
                item = json.loads(l)
                rows.append(item)
                existing_ids.add(item["id"])
        if existing_ids:
            print(f"Resuming run '{name}': loaded {len(existing_ids)} completed questions.")

    for line in open(golden, encoding="utf-8"):
        q = json.loads(line)
        if q["id"] in existing_ids:
            continue
        t0 = time.perf_counter()
        hits = retriever.search(q["question"], k=k)
        row = {"id": q["id"], "in_scope": q["in_scope"], "retrieval_ms": int(1000 * (time.perf_counter() - t0))}
        if q["in_scope"]:
            row |= retrieval_metrics(hits, q["gold_sections"])
        if not retrieval_only:
            prompt = f"Context:\n{context_block(hits)}\n\nQuestion: {q['question']}"
            ans, use = chat_json(ANSWER_SYSTEM, prompt, Answer)
            retrieved_ids = {h["chunk_id"] for h in hits}
            row |= {"refused": ans.refused,
                    "correct_refusal": ans.refused == (not q["in_scope"]),
                    "citations_valid": set(ans.cited_chunk_ids) <= retrieved_ids,
                    "answer_ms": use["latency_ms"],
                    "in_tokens": use["input_tokens"], "out_tokens": use["output_tokens"]}
            if q["in_scope"] and not ans.refused:
                judge_prompt = f"Context:\n{context_block(hits)}\n\nQuestion: {q['question']}\n\nAnswer:\n{ans.answer}"
                verdict, _ = chat_json(JUDGE_SYSTEM, judge_prompt, Judgement)
                row["supported"] = verdict.fully_supported
            row["answer"] = ans.answer
        rows.append(row)
        with open(out_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"[{len(rows)}] {q['id']}: in_scope={q['in_scope']} answer_ms={row.get('answer_ms')} supported={row.get('supported')}", flush=True)

    return summarise(name, mode, k, rows)


def mean(rows, key):
    vals = [float(r[key]) for r in rows if key in r]
    return round(statistics.mean(vals), 3) if vals else None


def summarise(name, mode, k, rows) -> dict:
    inscope = [r for r in rows if r["in_scope"]]
    answered = [r for r in inscope if "supported" in r]
    summary = {"run": name, "retriever": mode, "k": k, "questions": len(rows),
               f"hit@{k}": mean(inscope, "hit"), f"recall@{k}": mean(inscope, "recall"),
               "mrr": mean(inscope, "rr"),
               "correct_refusal": mean(rows, "correct_refusal"), "citations_valid": mean(rows, "citations_valid"),
               "hallucination_rate": round(1 - mean(answered, "supported"), 3) if answered else None,
               "retrieval_ms": mean(rows, "retrieval_ms"), "answer_ms": mean(rows, "answer_ms"),
               "tokens_per_q": (mean(rows, "in_tokens") or 0) + (mean(rows, "out_tokens") or 0) or None,
               # $0 on a free model; this is what the same tokens would cost at Claude Sonnet 5.5 list prices (A2)
               "cost_if_paid_usd": round(((mean(rows, "in_tokens") or 0) * 2
                                          + (mean(rows, "out_tokens") or 0) * 10) / 1e6, 5)}
    new = not os.path.exists("eval/results.csv")
    with open("eval/results.csv", "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(summary))
        if new:
            w.writeheader()
        w.writerow(summary)
    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--retriever", default=config.RETRIEVER, choices=["bm25", "dense", "hybrid"])
    ap.add_argument("--k", type=int, default=config.TOP_K)
    ap.add_argument("--retrieval-only", action="store_true")
    ap.add_argument("--golden", default="eval/golden.jsonl")
    a = ap.parse_args()
    print(json.dumps(run(a.name, a.retriever, a.k, a.retrieval_only, golden=a.golden), indent=2))
