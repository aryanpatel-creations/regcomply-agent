"""Each step of the agent is a plain function: state in, partial state out.
Plain functions are easy to unit-test without running the whole graph."""
import csv, os, uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Callable
import config
from pii import mask_regex
from agent.schemas import Triage, Draft

TRIAGE_SYSTEM = ("You triage bank customer complaints in India. Classify the complaint and write a focused search "
                 "query (3-6 core keywords) for finding the relevant RBI rules. For fee or charge disputes, include "
                 "keywords like 'minimum balance penal charges' or 'service charges'. Set confidence to 0.85 or higher for clear complaints.")
DRAFT_SYSTEM = ("You help a bank complaint agent. Draft a polite, specific reply using ONLY the rules in the "
                "context and the account facts given. Cite the chunk_id of each rule you rely on. "
                "Build a compliance checklist: include ONLY rules that directly apply to this complaint (omit irrelevant rules). "
                "In the checklist, evaluate whether the drafted response satisfies regulatory requirements: "
                "mark status 'met' if the draft aligns with the rule, 'check' if account records or facts must be verified by the agent, "
                "and 'not_met' only if the draft violates an established rule. "
                "Never promise a final refund; you may propose an amount for human approval. "
                "When the rules in context cover the complaint, set confidence to 0.85 or higher.")
SENSITIVE = {"Fraud"}


@dataclass
class Deps:
    chat: Callable            # llm.chat_json
    retriever: Any            # retrieval.Retriever
    tools: Any                # agent.tools.BankTools (or a fake in tests)


def mask_node(state):
    masked, counts = mask_regex(state["text"])
    return {"masked_text": masked, "pii_masked": sum(counts.values())}


def triage_node(state, deps: Deps):
    triage, usage = deps.chat(TRIAGE_SYSTEM, state["masked_text"], Triage)
    return {"triage": triage.model_dump(), "usage": [usage | {"step": "triage"}]}


def retrieve_node(state, deps: Deps):
    hits = deps.retriever.search(state["triage"]["search_query"] or state["masked_text"], k=config.TOP_K)
    return {"hits": [{k: h[k] for k in ("chunk_id", "title", "section", "heading", "text", "url")} for h in hits]}


def lookup_node(state, deps: Deps):
    """Read-only facts from the bank's systems, through MCP tools."""
    facts = {}
    try:
        if state.get("customer_id"):
            acc = deps.tools.account_summary(state["customer_id"])
            facts["account"] = acc
            facts["recent_transactions"] = deps.tools.recent_transactions(acc["account_id"], 30)[:10]
        if state.get("ticket_id"):
            facts["ticket"] = deps.tools.ticket(state["ticket_id"])
    except Exception as e:                                    # a tool failure must not crash the run
        facts["tool_error"] = str(e)[:200]
    return {"facts": facts}


def draft_node(state, deps: Deps):
    context = "\n\n".join(f'[{h["chunk_id"]}] {h["text"]}' for h in state["hits"])
    user = (f"Complaint (personal data masked):\n{state['masked_text']}\n\n"
            f"Triage: {state['triage']}\n\nAccount facts: {state.get('facts', {})}\n\nRules:\n{context}")
    draft, usage = deps.chat(DRAFT_SYSTEM, user, Draft)
    return {"draft": draft.model_dump(), "usage": [usage | {"step": "draft"}]}


def check_node(state):
    """Guardrails written in code, not left to the model."""
    t, d = state["triage"], state["draft"]
    retrieved = {h["chunk_id"] for h in state["hits"]}
    reasons = []
    if not state["hits"]:
        reasons.append("No relevant rule found")
    if min(t["confidence"], d["confidence"]) < config.CONFIDENCE_THRESHOLD:
        reasons.append("Low confidence")
    if not d["cited_chunk_ids"]:
        reasons.append("No citation")
    elif not set(d["cited_chunk_ids"]) <= retrieved:
        reasons.append("Citation not in retrieved rules")
    if mask_regex(d["reply"])[0] != d["reply"]:
        reasons.append("Personal data in reply")
    if d["proposed_refund_inr"] > config.REFUND_LIMIT_INR:
        reasons.append("Refund above limit")
    if t["category"] in SENSITIVE:
        reasons.append("Sensitive category")
    if any(item["status"] == "not_met" for item in d["checklist"]):
        reasons.append("Checklist item not met")
    if not t["is_complaint"]:
        reasons.append("Not a complaint")
    return {"check": {"passed": not reasons, "reasons": reasons}}


def route_after_check(state) -> str:
    return "finalise" if state["check"]["passed"] else "human_review"


def apply_review(state, decision: dict) -> dict:
    """Turn the reviewer's decision into state. decision = {action, reviewer, reply?}"""
    draft = dict(state["draft"])
    if decision["action"] == "edit":
        draft["reply"] = decision["reply"]
    return {"draft": draft, "review": decision}


def finalise_node(state):
    review = state.get("review")
    if review is None:
        status = "draft_ready_for_agent"            # every reply is still checked by the agent in the CRM
    elif review["action"] == "reject":
        status = "rejected_by_supervisor"
    else:
        status = "approved_by_supervisor"
    usage = state.get("usage", [])
    tin = sum(u.get("input_tokens", 0) for u in usage)
    tout = sum(u.get("output_tokens", 0) for u in usage)
    event = {
        "event_id": uuid.uuid4().hex[:12], "timestamp": datetime.now().isoformat(timespec="seconds"),
        "complaint_id": state["complaint_id"], "use_case": "Complaint draft", "model": config.CHAT_MODEL,
        "input_tokens": tin, "output_tokens": tout,
        "cost_usd": 0.0,                                              # free model
        "cost_usd_if_paid": round((tin * 2 + tout * 10) / 1e6, 6),    # at Claude Sonnet 5.5 list price (A2)
        "latency_ms": sum(u.get("latency_ms", 0) for u in usage),
        "guardrail_flag": (state["check"]["reasons"] or ["No flag"])[0],
        "escalated_to_human": "Yes" if review else "No", "status": status,
        "agent_outcome": "Pending",                                   # filled in when the agent sends or edits
    }
    new = not os.path.exists(config.EVENT_LOG)
    os.makedirs(os.path.dirname(config.EVENT_LOG) or ".", exist_ok=True)
    with open(config.EVENT_LOG, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(event))
        if new:
            w.writeheader()
        w.writerow(event)
    return {"final": {"status": status, "reply": state["draft"]["reply"],
                      "citations": state["draft"]["cited_chunk_ids"], "checklist": state["draft"]["checklist"],
                      "reasons": state["check"]["reasons"], "event_id": event["event_id"]}}
