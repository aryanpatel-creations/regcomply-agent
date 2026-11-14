"""Turn RBI PDFs into section-based chunks with metadata, saved as JSON Lines.

Usage:  python b1_parse_chunk.py data/raw/rbi --mode section --max-words 300
        --mode fixed ignores headings (the baseline to beat in B2)
Each PDF needs an entry in data/raw/rbi/sources.csv: file,doc_id,title,issued,url
"""
import argparse, csv, json, re
from collections import Counter
from pathlib import Path
from pypdf import PdfReader
from pii import mask_regex
import config

# A section heading looks like "10. Compensation" or "5.12 Reconciliation" at the start of a line.
SECTION_RX = re.compile(r"^\s*(\d{1,2}(?:\.\d{1,2})?)\.?\s+([A-Z][^\n]{2,120})$", re.M)
MAX_WORDS, OVERLAP_WORDS = 300, 40


def pdf_text(path: Path) -> str:
    pages = [p.extract_text() or "" for p in PdfReader(path).pages]
    text = "\n".join(pages)
    text = re.sub(r"[ \t]+", " ", text)                         # squeeze spaces
    text = re.sub(r"\n\s*Page \d+ of \d+\s*\n", "\n", text)     # drop page footers
    return text


def split_sections(text: str) -> list[dict]:
    heads = list(SECTION_RX.finditer(text))
    if not heads:                                              # no numbered headings found
        return [{"section": "0", "heading": "Full text", "body": text.strip()}]
    out = []
    preamble = text[: heads[0].start()].strip()
    if preamble:
        out.append({"section": "0", "heading": "Preamble", "body": preamble})
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        out.append({"section": h.group(1), "heading": h.group(2).strip(),
                    "body": text[h.end():end].strip()})
    return out


def window(words: list) -> list[list]:
    """Split a long list into overlapping windows of MAX_WORDS items."""
    if len(words) <= MAX_WORDS:
        return [words]
    step = MAX_WORDS - OVERLAP_WORDS
    return [words[i:i + MAX_WORDS] for i in range(0, len(words) - OVERLAP_WORDS, step)]


def units(text: str, mode: str):
    """Yield (section, heading, part, words). 'section' respects headings; 'fixed' does not."""
    secs = split_sections(text)
    if mode == "section":
        for sec in secs:
            for part, words in enumerate(window(sec["body"].split()), start=1):
                yield sec["section"], sec["heading"], part, words
        return
    tagged = [(w, s["section"], s["heading"]) for s in secs for w in s["body"].split()]
    for part, win in enumerate(window(tagged), start=1):
        section, heading = Counter((t[1], t[2]) for t in win).most_common(1)[0][0]   # majority section
        yield section, heading, part, [t[0] for t in win]


def chunk_document(text: str, meta: dict, mode: str = "section", min_words: int = 0) -> list[dict]:
    chunks = []
    for section, heading, part, words in units(text, mode):
        if len(words) < min_words:
            continue
        body, pii_counts = mask_regex(" ".join(words))
        # In section mode the title and heading are repeated inside the text, so they are searchable
        prefix = f'{meta["title"]} - Section {section}: {heading}. ' if mode == "section" else ""
        chunks.append({
            "chunk_id": f'{meta["doc_id"]}:{section}:{part}',
            "doc_id": meta["doc_id"], "title": meta["title"], "issued": meta["issued"], "url": meta["url"],
            "section": section, "heading": heading, "text": prefix + body,
            "n_words": len(words), "pii_masked": sum(pii_counts.values()),
        })
    return chunks


def main(folder: str, mode: str, min_words: int = 20):
    folder = Path(folder)
    with open(folder / "sources.csv", newline="", encoding="utf-8") as f:
        sources = {row["file"]: row for row in csv.DictReader(f)}
    all_chunks = []
    for pdf in sorted(folder.glob("*.pdf")):
        meta = sources.get(pdf.name)
        if meta is None:
            print(f"SKIPPED {pdf.name}: add it to sources.csv"); continue
        chunks = chunk_document(pdf_text(pdf), meta, mode, min_words=min_words)
        print(f"{pdf.name}: {len(chunks)} chunks")
        all_chunks += chunks
    Path(config.CHUNKS_PATH).parent.mkdir(parents=True, exist_ok=True)
    with open(config.CHUNKS_PATH, "w", encoding="utf-8") as f:
        for c in all_chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"Saved {len(all_chunks)} chunks to {config.CHUNKS_PATH}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", nargs="?", default="data/raw/rbi")
    ap.add_argument("--mode", choices=["section", "fixed"], default="section")
    ap.add_argument("--max-words", type=int, default=MAX_WORDS)
    ap.add_argument("--min-words", type=int, default=20)
    a = ap.parse_args()
    MAX_WORDS = a.max_words
    OVERLAP_WORDS = max(10, MAX_WORDS // 8)
    main(a.folder, a.mode, a.min_words)
