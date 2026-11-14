"""Wire the steps into a LangGraph state graph with a checkpointer and a human-review pause.

mask -> triage -> retrieve -> lookup -> draft -> check --(passed)--> finalise
                                                      \\--(flagged)--> human_review -> finalise
"""
import operator, sqlite3
from typing import Annotated, Any, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt
from langgraph.checkpoint.sqlite import SqliteSaver
import config
from agent import nodes
from agent.nodes import Deps


class State(TypedDict, total=False):
    complaint_id: str
    text: str
    customer_id: str
    ticket_id: str
    masked_text: str
    pii_masked: int
    triage: dict
    hits: list
    facts: dict
    draft: dict
    check: dict
    review: dict
    final: dict
    usage: Annotated[list, operator.add]     # each step appends its token usage


def human_review(state: State, deps: Deps):
    # Pauses here. Everything above interrupt() runs again on resume, so keep it free of side effects.
    decision = interrupt({
        "complaint_id": state["complaint_id"], "reasons": state["check"]["reasons"],
        "draft": state["draft"], "triage": state["triage"],
        "options": ["approve", "edit", "reject"],
    })
    update = nodes.apply_review(state, decision)
    if decision.get("refund_token") and state["draft"]["proposed_refund_inr"] > 0:
        update["review"] = update["review"] | {"refund": deps.tools.request_refund(
            ticket_id=state["ticket_id"], amount_inr=float(state["draft"]["proposed_refund_inr"]),
            reason="Approved in supervisor review", approval_token_value=decision["refund_token"],
            approved_by=decision["reviewer"])}
    return update


def build_graph(deps: Deps, checkpointer: Any = None):
    g = StateGraph(State)
    g.add_node("mask", nodes.mask_node)
    g.add_node("triage", lambda s: nodes.triage_node(s, deps))
    g.add_node("retrieve", lambda s: nodes.retrieve_node(s, deps))
    g.add_node("lookup", lambda s: nodes.lookup_node(s, deps))
    g.add_node("draft", lambda s: nodes.draft_node(s, deps))
    g.add_node("check", nodes.check_node)
    g.add_node("human_review", lambda s: human_review(s, deps))
    g.add_node("finalise", nodes.finalise_node)
    g.add_edge(START, "mask")
    g.add_edge("mask", "triage")
    g.add_edge("triage", "retrieve")
    g.add_edge("retrieve", "lookup")
    g.add_edge("lookup", "draft")
    g.add_edge("draft", "check")
    g.add_conditional_edges("check", nodes.route_after_check, ["finalise", "human_review"])
    g.add_edge("human_review", "finalise")
    g.add_edge("finalise", END)
    if checkpointer is None:
        checkpointer = SqliteSaver(sqlite3.connect(config.CHECKPOINT_DB, check_same_thread=False))
    return g.compile(checkpointer=checkpointer)
