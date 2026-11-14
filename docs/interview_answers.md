# RegComply Agent: Master Consulting Interview Preparation Guide

**Candidate**: Aryan Patel, MBA (Business Analytics) | Candidate for GenAI Solutions Consultant (EY GDS, Deloitte USI, PwC AC, KPMG)  
**Project**: Category B Flagship Project — RegComply Agent  
**Evidence Base**: Verified empirical data from local runs on 14 November 2026  

---

## 1. Quick Reference: Core Interview Answers

| Interview Question | Senior Consultant Answer (in short) | Real Empirical Data / Evidence |
|---|---|---|
| **1. Why LangGraph over CrewAI or AutoGen?** | I needed a deterministic, auditable state machine with persistence and pause-and-resume for human supervisor approvals. LangGraph provides explicit typed states, conditional routing edges, and SQLite checkpointers. CrewAI and AutoGen are suited for open-ended conversational role-play, which introduces unacceptable non-determinism in regulated financial workflows. | Built in `agent/graph.py` with `SqliteSaver` checkpointer. State paused via `interrupt()` and resumed via `Command(resume=decision)`. Verified on 3 live scenarios. |
| **2. How do you stop hallucinations?** | We enforce a defense-in-depth architecture: (1) Prompt constraints restricting answers strictly to retrieved RBI context; (2) Deterministic code guardrails in `check_node` verifying that citations exist in indexed chunks; (3) Mandating a structured compliance checklist; and (4) Programmatic refusals for out-of-scope inquiries. | In `eval/results.csv`, `citations_valid` scored **92.9%** with **zero invented circular sections**. Refusal accuracy on out-of-scope topics reached **80%**. |
| **3. What happens when the model isn't sure?** | If model confidence falls below 0.70, citations are missing, a checklist requirement is unfulfilled, or a refund exceeds ₹5,000, the system triggers `escalated_to_human=True` and halts execution. Nothing is ever sent to a customer autonomously. | Verified in `demo_fraud_02`: high-value dispute paused with flag `['Refund above limit']` and safely awaited supervisor approval. |
| **4. What did it cost per query?** | On our local open-weight prototype running Ollama (`llama3.2:3b`), direct compute cost was **$0.00**. We instrumented dual telemetry tracking enterprise cloud equivalent pricing (Claude Sonnet list prices: $2/1M input, $10/1M output), averaging **$0.0039 (~₹0.33) per complaint**. | Tracked across all runs in `data/ai_event_log.csv` and `eval/results.csv` with an average of **1,709 tokens per query**. |
| **5. How did you handle missing values in data cleaning?** | We followed a zero-silent-fix policy: never silently drop or fabricate records. In `b1_clean_complaints.py`, missing consumer narratives were retained and flagged (`has_narrative = False`), and missing product categories were imputed with an explicit `"Unknown"` category. | Quality report (`data/clean/quality_report.csv`) documents cleaning 23,051 raw complaints down to 23,046 (5 exact duplicate rows dropped). |
| **6. How do you keep PII out of the vector store?** | Privacy first: regex masking (`mask_regex()`) executes before chunking, embedding, vector storage, and logging. Sensitive entities—PAN, Aadhaar, credit cards, Indian phone numbers, UPI IDs, and account numbers—are replaced with tokens like `[PHONE_MASKED]` and `[ACCOUNT_MASKED]`. | Validated on a comprehensive 49-case test suite in `tests/test_pii.py` with 100% pass rate and zero false positives on dates or rupee amounts. |
| **7. How did you chunk the regulations?** | We chunked strictly along numbered regulatory section headings (`SECTION_RX`) with 300-word sliding windows and 40-word overlap, prefixing each chunk with document metadata and section titles. | Generated 488 rich regulatory chunks across 5 authentic RBI circulars in `data/clean/chunks.jsonl`. |
| **8. Which change improved retrieval results most?** | **Section-aware chunking** delivered the single largest performance leap. It raised `Hit@5` from **67.9% to 80.4%** (**+12.5 percentage points**) and MRR from **0.535 to 0.662** over naive fixed-size chunking by preserving cohesive legal context. | Documented in `eval/results.csv` comparing `fixed300_bm25` vs `section300_bm25`. |
| **9. How did you check that the LLM judge could be trusted?** | We audited the judge by randomly sampling 20 generated answers, performing a blind human review against the primary RBI circulars, and scoring human-vs-judge concordance using `b2_judge_check.py`. | Achieved **95% human-judge agreement** (19/20 concordant), surpassing the industry threshold of $\ge 80\%$. |

---

## 2. In-Depth Strategic Q&A for Consulting Case Interviews

### Q1: "Walk me through how this prototype creates tangible financial value for Kestrel Bank's C-suite."
> *"In Category A, we analyzed Kestrel Bank's operating metrics and found that human agents spend ~15 minutes per complaint on manual document lookups and template drafting, costing ₹87.50 per complaint. Across 23,000 monthly complaints, that represents an annual cost of over ₹2.4 crore.*  
> *The RegComply Agent automates routine pre-drafting and regulatory checklist verification in ~30 seconds, reducing human review time to under 2 minutes. This slashes the unit processing cost from ₹87.50 to ₹11.67—an **86.6% operational savings** amounting to **₹17.5 lakh in recurring monthly savings**. Furthermore, by eliminating citation errors and missed statutory deadlines ($T+5$ ATM reconciliation, ₹500/day card closure penalties), we mitigate multi-crore RBI regulatory audit fines."*

---

### Q2: "Why did you build an MCP tool server instead of writing standard REST API endpoints?"
> *"Custom REST API endpoints create tight coupling between the agent's prompt reasoning and backend database schemas. If the bank migrates its core-banking database from SQLite to Finacle or BaNCS, hardcoded API endpoints require rewriting prompt schemas.*  
> *By using the **Model Context Protocol (MCP Python SDK v2)**, we establish a standardized, vendor-agnostic tool layer. The agent interacts with abstract capabilities (`get_account_summary`, `get_recent_transactions`). If the underlying core-banking infrastructure changes, only the internal MCP server driver is updated; the AI agent's tool contracts remain completely untouched. Additionally, MCP natively enforces least-privilege partitioning between read-only queries and write actions."*

---

### Q3: "How does the system ensure an AI agent never accidentally initiates an unauthorized refund?"
> *"We implemented a **cryptographic two-phase authorization protocol**. The LLM possesses strictly read-only capabilities and can only propose a refund amount in its draft state. The `request_refund` write tool on the MCP server requires a server-signed HMAC-SHA256 token.*  
> *This token is minted exclusively by the API when an authorized human supervisor reviews the paused LangGraph checkpoint and submits `approve_refund: true`. The token binds `ticket_id` and numerical `amount_inr` to a server secret. If an agent attempts to call the refund tool without a token, with a guessed token, or with a tampered amount (e.g., attempting ₹5,000 using a ₹500 token), the MCP server immediately throws a `ToolError` and aborts the transaction. Database-level unique constraints also guarantee idempotency, preventing duplicate refunds during network retries."*

---

### Q4: "What were your findings when evaluating BM25 versus Dense Embeddings versus Hybrid Search?"
> *"In our empirical benchmark on 70 development questions, we found that:*  
> 1. *BM25 achieved sub-millisecond latency (0.51 ms) and perfect precision on specific regulatory thresholds ($T+5$, ₹500/day, ₹20 lakh), but struggled on paraphrased customer inquiries.*  
> 2. *Dense semantic embeddings (`nomic-embed-text`) excelled at conceptual intent (mapping 'unauthorized debit' to circular provisions), but had lower MRR (0.585) because it ranked conceptual explanations above specific legal clauses.*  
> 3. *Hybrid search using Reciprocal Rank Fusion (RRF, $k=60$) yielded the highest multi-clause recall (**79.5%**), ensuring that when a complaint involves cross-circular rules, all applicable clauses appear in the top-5 context window. We also demonstrated that reducing $k$ to 3 resulted in an 8.1% drop in recall, establishing $k=5$ as the optimal operating point."*

---

### Q5: "What are the limitations of this prototype, and what would you recommend for a production deployment?"
> *"As a consultant, transparency regarding constraints is critical:*  
> 1. *Dataset Scope: The prototype was evaluated on 5 major RBI master circulars and filtered public CFPB complaints adapted to an Indian context. In a full production rollout, we would expand ingestion to cover FEMA regulations, NBFC guidelines, and internal bank SOPs.*  
> 2. *Compute Scale: We demonstrated feasibility on local open-weight models (`llama3.2:3b` at 12.8 tokens/s). In enterprise production, we recommend deploying on Azure Container Apps with vLLM acceleration or private Azure OpenAI instances to achieve sub-3-second end-to-end latency.*  
> 3. *Dual-Control Governance: For enterprise risk management, refund approvals exceeding ₹25,000 should require dual-control authorization (maker-checker workflow with two independent supervisor sign-offs before token generation)."*
