"""Runs the real LangGraph flow with fake model/retriever/tools. Skipped if LangGraph is not installed."""
import pytest
pytest.importorskip("langgraph")
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command
import config
from agent.graph import build_graph
from agent.nodes import Deps
from tests.test_nodes import fake_chat, FakeRetriever, FakeTools

def graph(chat):
    return build_graph(Deps(chat=chat, retriever=FakeRetriever(), tools=FakeTools()), InMemorySaver())

def test_clean_case_runs_to_the_end(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "EVENT_LOG", str(tmp_path / "log.csv"))
    cfg = {"configurable": {"thread_id": "t1"}}
    complaint = {"complaint_id": "t1", "text": "Fee charged twice", "customer_id": "C0001"}
    out = graph(fake_chat()).invoke(complaint, cfg)
    assert out["final"]["status"] == "draft_ready_for_agent"

def test_risky_case_pauses_then_resumes_after_edit(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "EVENT_LOG", str(tmp_path / "log.csv"))
    g, cfg = graph(fake_chat(confidence=0.5)), {"configurable": {"thread_id": "t2"}}
    out = g.invoke({"complaint_id": "t2", "text": "Fee charged twice", "customer_id": "C0001"}, cfg)
    assert "__interrupt__" in out and g.get_state(cfg).next == ("human_review",)
    out = g.invoke(Command(resume={"action": "edit", "reviewer": "s1", "reply": "Edited reply"}), cfg)
    assert out["final"]["status"] == "approved_by_supervisor" and out["final"]["reply"] == "Edited reply"
