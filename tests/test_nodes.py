"""Test the agent's steps with a fake model, fake retriever and fake tools: no LLM or server needed."""
import config
from agent import nodes
from agent.nodes import Deps
from agent.schemas import Triage, Draft

HITS = [{"chunk_id": "RBIOS:8:1", "title": "RB-IOS", "section": "8", "heading": "Time limit",
         "text": "Reply within 30 days", "url": "u"}]

class FakeRetriever:
    def search(self, q, k): return HITS

class FakeTools:
    def account_summary(self, cid): return {"account_id": "A0001", "status": "Active"}
    def recent_transactions(self, aid, days):
        return [{"txn_id": "T1", "description": "Annual card fee", "amount_inr": -999}]
    def ticket(self, tid): raise RuntimeError("Ticket K9 not found")

def fake_chat(confidence=0.9, refund=0.0, cite="RBIOS:8:1", reply="We will reply within 30 days."):
    def chat(system, user, cls):
        if cls is Triage:
            return Triage(is_complaint=True, category="Charges", product="Cards", urgency="medium",
                          search_query="card fee reversal time limit", confidence=confidence), \
                   {"input_tokens": 100, "output_tokens": 20, "latency_ms": 5}
        item = {"requirement": "Reply in 30 days", "status": "met", "citation": cite}
        return Draft(reply=reply, cited_chunk_ids=[cite], checklist=[item],
                     proposed_refund_inr=refund, confidence=confidence), \
               {"input_tokens": 900, "output_tokens": 150, "latency_ms": 9}
    return chat

def run_steps(chat, text="My card 4111 1111 1111 1111 was charged a fee twice", **extra):
    deps = Deps(chat=chat, retriever=FakeRetriever(), tools=FakeTools())
    s = {"complaint_id": "X1", "text": text, "customer_id": "C0001", "ticket_id": "K9"} | extra
    for step in (nodes.mask_node, lambda s: nodes.triage_node(s, deps), lambda s: nodes.retrieve_node(s, deps),
                 lambda s: nodes.lookup_node(s, deps), lambda s: nodes.draft_node(s, deps), nodes.check_node):
        out = step(s)
        if "usage" in out:
            out["usage"] = s.get("usage", []) + out["usage"]
        s |= out
    return s

def test_pii_is_masked_before_the_model_sees_it():
    s = run_steps(fake_chat())
    assert "4111" not in s["masked_text"] and s["pii_masked"] == 1

def test_tool_error_is_recorded_not_raised():
    s = run_steps(fake_chat())
    assert "account" in s["facts"] and "tool_error" in s["facts"]

def test_clean_case_passes_and_logs(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "EVENT_LOG", str(tmp_path / "log.csv"))
    s = run_steps(fake_chat())
    assert s["check"] == {"passed": True, "reasons": []} and nodes.route_after_check(s) == "finalise"
    final = nodes.finalise_node(s)["final"]
    assert final["status"] == "draft_ready_for_agent"
    log = (tmp_path / "log.csv").read_text().splitlines()
    assert len(log) == 2 and ",1000,170," in log[1]            # tokens summed across both steps

def test_guardrails_send_risky_drafts_to_a_human():
    s = run_steps(fake_chat(confidence=0.5, refund=9000, cite="MADEUP:1:1", reply="Call 9876543210"))
    assert nodes.route_after_check(s) == "human_review"
    assert set(s["check"]["reasons"]) == {"Low confidence", "Citation not in retrieved rules",
                                          "Personal data in reply", "Refund above limit"}

def test_reviewer_edit_replaces_reply():
    s = run_steps(fake_chat(confidence=0.5))
    upd = nodes.apply_review(s, {"action": "edit", "reviewer": "s1", "reply": "Edited reply"})
    assert upd["draft"]["reply"] == "Edited reply" and upd["review"]["reviewer"] == "s1"
