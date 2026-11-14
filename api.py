"""FastAPI service. Open http://localhost:8000/docs to try it (free built-in UI for your demo).

uvicorn api:app --port 8000
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Literal
from langgraph.types import Command
import config
from llm import chat_json
from retrieval import load_retriever
from agent.graph import build_graph
from agent.nodes import Deps
from agent.tools import BankTools
from b3_mcp_server import approval_token
import os, b3_mock_bank

if not os.path.exists(config.BANK_DB):           # cloud hosts start with an empty disk
    b3_mock_bank.build()

app = FastAPI(title="RegComply Agent", version="0.1")
graph = build_graph(Deps(chat=chat_json, retriever=load_retriever(), tools=BankTools()))


class ComplaintIn(BaseModel):
    complaint_id: str
    text: str
    customer_id: str | None = None
    ticket_id: str | None = None


class ReviewIn(BaseModel):
    action: Literal["approve", "edit", "reject"]
    reviewer: str
    reply: str | None = None
    approve_refund: bool = False


def thread(cid: str) -> dict:
    return {"configurable": {"thread_id": cid}}      # one thread per complaint


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


@app.get("/health")
def health():
    return {"status": "ok", "model": config.CHAT_MODEL, "retriever": config.RETRIEVER}


@app.post("/complaints")
def submit(c: ComplaintIn):                          # plain def: FastAPI runs it in a worker thread
    result = graph.invoke(c.model_dump(exclude_none=True), thread(c.complaint_id))
    if "__interrupt__" in result:
        return {"status": "waiting_for_review", "review_request": result["__interrupt__"][0].value}
    return result["final"]


@app.get("/complaints/{cid}")
def status(cid: str):
    snap = graph.get_state(thread(cid))
    if not snap.values:
        raise HTTPException(404, "Unknown complaint")
    return {"next": list(snap.next), "final": snap.values.get("final"),
            "check": snap.values.get("check"), "draft": snap.values.get("draft")}


@app.post("/reviews/{cid}")
def review(cid: str, r: ReviewIn):
    snap = graph.get_state(thread(cid))
    if "human_review" not in snap.next:
        raise HTTPException(409, "This complaint is not waiting for review")
    if r.action == "edit" and not r.reply:
        raise HTTPException(422, "An edit needs the new reply text")
    decision = r.model_dump(exclude={"approve_refund"})
    draft = snap.values["draft"]
    wants_refund = r.approve_refund and r.action != "reject" and draft["proposed_refund_inr"] > 0
    if wants_refund and snap.values.get("ticket_id"):
        # The token is created here, by the server, only after a named human approves.
        decision["refund_token"] = approval_token(snap.values["ticket_id"], float(draft["proposed_refund_inr"]))
    result = graph.invoke(Command(resume=decision), thread(cid))
    return result["final"]
