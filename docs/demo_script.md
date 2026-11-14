# RegComply Agent: 3-Minute Video Demo Script

**Speaker**: Aryan Patel, MBA (Business Analytics) | GenAI Solutions Consultant  
**Target Audience**: Big 4 Consulting Partners & Senior Directors (EY GDS, Deloitte USI, PwC AC, KPMG)  
**Total Target Duration**: 3 minutes (180 seconds)  

---

## Storyboard & Script Breakdown

### Section 1: The Problem & The Consulting Opportunity (0:00 – 0:20)
* **Visual**: Show slide or title page: *"RegComply Agent: Automated Banking Complaint Handling & Regulatory Compliance"*.
* **Spoken Script**:
  > *"Hello, I'm Aryan Patel. At Indian commercial banks like our case study Kestrel Bank, frontline complaint agents handle over 23,000 grievances a month. Every response must comply with strict, binding Reserve Bank of India circulars covering unauthorized electronic transactions, card billing, and customer service. Agents spend 15 minutes per complaint manually digging through circulars and core-banking systems, risking regulatory fines and customer churn. I scoped this opportunity like a consultant, and built the solution like an engineer: the RegComply Agent."*

---

### Section 2: Architecture & Safe Design Principles (0:20 – 0:50)
* **Visual**: Show the Architecture Diagram (from README.md / draw.io). Point cursor to sequential stages: Masking $\rightarrow$ Triage $\rightarrow$ Hybrid Retrieval $\rightarrow$ MCP Tools $\rightarrow$ Guardrails $\rightarrow$ Human Review.
* **Spoken Script**:
  > *"The architecture enforces three non-negotiable enterprise banking principles:*  
  > *First, **Privacy First**: all customer names, phone numbers, and account digits are masked before touching any model or index.*  
  > *Second, **Grounded Regulatory RAG**: we use Reciprocal Rank Fusion hybrid search over indexed RBI circulars, requiring verbatim clause citations.*  
  > *Third, **Humans in Control**: built with LangGraph checkpointers, the agent never communicates with customers autonomously. Routine complaints generate a pre-approved draft for frontline agents, while high-risk grievances or refunds trigger a state pause that strictly requires human supervisor approval."*

---

### Section 3: Live Swagger Demo — Direct Pass vs Guardrail Pause (0:50 – 1:40)
* **Visual**: Switch to browser showing Swagger UI at `http://localhost:8000/docs`.

#### Step 1: Submit a Clean Fee Complaint
* **Action**: Expand `POST /complaints`, paste `demo_fee_02` (Rs 500 fee dispute), click **Execute**.
* **Spoken Script**:
  > *"Let's test a routine inquiry in Swagger UI. A customer disputes a ₹500 maintenance fee. Within seconds, the agent classifies the grievance, pulls real RBI circular clauses on minimum balance penal charges, and returns `status: draft_ready_for_agent`. Look at the compliance checklist: every item is verified as `met` or `check`, and citations are validated. No supervisor time is wasted."*

#### Step 2: Submit a High-Risk Fraud Complaint
* **Action**: In `POST /complaints`, paste `demo_fraud_02` (Rs 15,000 unauthorized transaction), click **Execute**.
* **Spoken Script**:
  > *"Now, watch what happens when a customer reports a ₹15,000 unauthorized transaction. Instead of auto-approving, our deterministic code guardrail catches that the refund exceeds our ₹5,000 threshold and involves a sensitive fraud category. The workflow halts immediately with `status: waiting_for_review`. LangGraph serializes state into SQLite, preventing any side effects."*

---

### Section 4: Human Review Resume & Cryptographic Gated Refund (1:40 – 2:15)
* **Visual**: Scroll to `POST /reviews/{cid}`.

#### Step 1: Supervisor Approval & State Resumption
* **Action**: Enter `cid: demo_fraud_02`, paste approval payload with `approve_refund: true`, click **Execute**.
* **Spoken Script**:
  > *"As supervisor, I review the draft and click approve. The API server mints an HMAC-SHA256 approval token bound cryptographically to this specific ticket and amount. LangGraph resumes from the exact checkpoint, transitions to `approved_by_supervisor`, and calls our core-banking MCP tool."*

#### Step 2: Show Automated Security Tests Passing
* **Action**: Switch to terminal showing `pytest tests/test_mcp.py -v`.
* **Spoken Script**:
  > *"Our MCP Python SDK v2 tool server enforces the principle of least privilege. In our test suite, read-only tools return account facts, while write tools strictly reject requests without a valid server token. Tampering with the amount or replaying tokens is mathematically blocked."*

---

### Section 5: Evaluation Harness & Executive Dashboard (2:15 – 2:45)
* **Visual**: Switch to `docs/evaluation_report.md` metrics table or Power BI dashboard.
* **Spoken Script**:
  > *"To ensure executive credibility, we measured the system across 100 verified questions with a strict 70/30 dev/test split. Section-aware chunking beat naive windowing by 12.5 percentage points, while hybrid search achieved 79.5% multi-clause recall. We also validated our LLM Judge against 20 human-audited answers, achieving 95% agreement. In our event log, direct cost on open-weight models is zero, and enterprise cloud cost is just ₹0.33 per complaint."*

---

### Section 6: Next Steps for Enterprise Production (2:45 – 3:00)
* **Visual**: Return to slide or camera.
* **Spoken Script**:
  > *"In a full production rollout, we would connect the MCP server to Finacle core APIs, integrate dual-control approval for refunds above ₹25,000, and scale out on Azure Container Apps. The RegComply Agent demonstrates how generative AI can transform bank operations safely, measurably, and cost-effectively. Thank you."*
