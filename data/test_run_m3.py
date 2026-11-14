import sys
sys.path.insert(0, ".")
import json, sqlite3
import config
from llm import chat_json
from retrieval import load_retriever
from agent.graph import build_graph
from agent.nodes import Deps
from agent.tools import BankTools
from langgraph.types import Command
from langgraph.checkpoint.sqlite import SqliteSaver

# Initialize dependencies with in-process tools for local testing
deps = Deps(chat=chat_json, retriever=load_retriever("hybrid"), tools=BankTools("inprocess"))
conn = sqlite3.connect("data/checkpoints.db", check_same_thread=False)
graph = build_graph(deps, checkpointer=SqliteSaver(conn))

print("=================================================================")
print("=== Case 1: Clear Fee Complaint (Expect: Finalised directly) ===")
print("=================================================================")
c1 = {
    "complaint_id": "fee_001",
    "text": "Please clarify the Rs 150 annual debit card fee charged to my savings account and provide the relevant card schedule of charges.",
}
res1 = graph.invoke(c1, {"configurable": {"thread_id": "fee_001"}})
if "__interrupt__" in res1:
    print("Case 1 Paused for review:", res1["__interrupt__"][0].value["reasons"])
else:
    print("Case 1 Status:", res1["final"]["status"])
    print("  Reasons flagged:", res1["final"]["reasons"])
    print("  Citations:", res1["final"]["citations"])
    print("  Checklist:", res1["final"]["checklist"])
    print("  Reply snippet:", res1["final"]["reply"][:140].strip())

print("\n=================================================================")
print("=== Case 2: Fraud Complaint (Expect: Pause at human_review) ===")
print("=================================================================")
c2 = {
    "complaint_id": "fraud_002",
    "text": "Someone made an unauthorized debit of Rs 15000 from my card yesterday without my knowledge. I reported this immediately within 24 hours. Please refund my money.",
}
res2 = graph.invoke(c2, {"configurable": {"thread_id": "fraud_002"}})
if "__interrupt__" in res2:
    print("Case 2 Paused for review (EXPECTED):", res2["__interrupt__"][0].value["reasons"])
    print("Resuming Case 2 with supervisor approval...")
    resume_decision = {"action": "approve", "reviewer": "Aryan Patel (Supervisor)"}
    res2_resumed = graph.invoke(Command(resume=resume_decision), {"configurable": {"thread_id": "fraud_002"}})
    print("Case 2 Final Status after Resume:", res2_resumed["final"]["status"])
    print("Case 2 Event ID:", res2_resumed["final"]["event_id"])
else:
    print("Case 2 Finished directly:", res2["final"]["status"])

print("\n=================================================================")
print("=== Case 3: Non-Complaint Query (Expect: Pause at human_review) ===")
print("=================================================================")
c3 = {
    "complaint_id": "query_003",
    "text": "Can you please tell me the working hours for the branch and whether locker facilities are available?",
}
res3 = graph.invoke(c3, {"configurable": {"thread_id": "query_003"}})
if "__interrupt__" in res3:
    print("Case 3 Paused for review (EXPECTED):", res3["__interrupt__"][0].value["reasons"])
    print("Resuming Case 3 with supervisor edit...")
    edit_decision = {
        "action": "edit",
        "reviewer": "Aryan Patel (Supervisor)",
        "reply": "Our branches operate from 10:00 AM to 4:00 PM Monday through Friday. Lockers are subject to branch availability.",
    }
    res3_resumed = graph.invoke(Command(resume=edit_decision), {"configurable": {"thread_id": "query_003"}})
    print("Case 3 Final Status after Resume:", res3_resumed["final"]["status"])
    print("Case 3 Edited Reply:", res3_resumed["final"]["reply"][:100].strip())
else:
    print("Case 3 Finished directly:", res3["final"]["status"])
