# Architecture & Engineering Decisions (Category B)

## 2026-11-14: Milestone M0 Setup Choices

### 1. Python 3.11.9 Virtual Environment
- **Decision**: Proceeded with Python 3.11.9 (system installed version) rather than installing Python 3.12, following user approval.
- **Rationale**: Python 3.11.9 provides complete ABI and package compatibility for all required libraries in `requirements.txt` (including `langgraph==1.2.22`, `mcp==2.3.0`, `fastapi==0.162.7`, `pydantic==2.14.3`, `pandas==3.1.1`).
- **Verification**: All 36 tests across unit test suites passed in 2.25s.

### 2. Dependency Management & Fast Virtualenv Populating
- **Decision**: Used `uv` to resolve and install 72 pinned/dependent packages into `.venv`.
- **Lockfile**: Full environment snapshot frozen to `requirements.lock`.

### 3. Local LLM Strategy (Ollama)
- **Decision**: Selected local Ollama route (`LLM_PROVIDER=ollama`) with primary target `llama3.2:3b` (measured 12.81 tokens/s on Intel CPU) and `nomic-embed-text` embeddings; `qwen3.5:9b` also pulled and available.
- **Hardware Context**: Intel Iris Xe integrated GPU (no discrete NVIDIA GPU), 16 GB system RAM. `llama3.2:3b` avoids cold-load timeouts while retaining high instruction-following quality.

---

## 2026-11-14: Milestone M1 (B1 Data Pipeline & PII Masking)

### 4. PII Phone Number Regex Boundary Fix
- **Problem**: In `pii.py`, `(?:\+91[ -]?|\b0)?\b[6-9]\d{9}\b` failed on 11-digit numbers starting with `0` (e.g. `09876543210`) because `\b` between `0` and `9` failed (both are word characters), causing it to fall through to `ACCOUNT`.
- **Fix**: Adjusted pattern to `(?:\+91[ -]?\b|\b0?)[6-9]\d{9}\b`.
- **Validation**: Expanded `tests/test_pii.py` from 11 to 49 comprehensive test cases (including PAN, Aadhaar, cards, phone variants, UPI, IFSC, accounts, and negative tests for amounts/dates/sections). 75 total tests green.

### 5. Section Heading Pattern Extension (Sub-sections)
- **Problem**: `MC_CustomerService.pdf` and other directions use decimal sub-sections (e.g., `5.12 Reconciliation of transactions at ATMs`, `4.1 Basic Savings Bank Account`). The original regex only matched single/two-digit integers (`^\s*(\d{1,2})\.`).
- **Fix**: Updated `SECTION_RX` in `b1_parse_chunk.py` to `^\s*(\d{1,2}(?:\.\d{1,2})?)\.?\s+([A-Z][^\n]{2,120})$`.
- **Validation**: Added `test_subsections_found` in `tests/test_chunking.py`.

### 6. Table-of-Contents & Short Chunk Filtering
- **Problem**: Real master circulars contain multi-page Tables of Contents where section titles are followed only by page numbers, yielding 143 empty (`0 words`) chunks and 273 near-empty fragments.
- **Fix**: Added `min_words=20` default in `b1_parse_chunk.py` (with `min_words=0` default in `chunk_document` to preserve unit test contracts).
- **Result**: Successfully produced 488 high-signal regulatory chunks across 5 documents in `data/clean/chunks.jsonl`. Generated `docs/chunk_inspection.md` with 20 stratified sample chunks for human audit.

---

## 2026-11-14: Milestone M2 (B2 Retrieval Evaluation & Golden Set)

### 7. Golden Dataset Structuring & Exact Citation Quoting
- **Design**: Created initial 50 candidate questions meeting the strict distribution (30% single fact, 20% definition/eligibility, 20% paraphrased customer language, 10% multi-section, 20% out-of-scope).
- **Speed & Auditability**: Provided exact verbatim source sentence quotes for every in-scope question in `docs/candidate_questions_50.md` so the human reviewer (Aryan Patel) can verify question fidelity against circulars in under 15 minutes.
- **Leakage Prevention**: Established 70/30 split plan upfront (`eval/golden_dev.jsonl` with 35 questions, `eval/golden_test.jsonl` with 15 questions) prior to retrieval tuning.

### 8. Retrieval Paradigm Comparison (BM25 vs Dense vs Hybrid)
- **Observations on Dev Set (35 questions, section-300 chunks)**:
  - `bm25`: hit@5 = 0.893, recall@5 = 0.893, MRR = 0.702, latency = 0.29 ms.
  - `dense`: hit@5 = 0.857, recall@5 = 0.857, MRR = 0.662, latency = 2109 ms.
  - `hybrid` (RRF, k=60): hit@5 = 0.893, recall@5 = 0.893, **MRR = 0.708**, latency = 2111 ms.
- **Takeaway**: Hybrid search achieved the highest MRR by combining exact keyword matches (statutory timeframes and circular numbers) with semantic embeddings (paraphrased customer inquiries). Hybrid selected as default production retriever in `.env`.

---

## 2026-11-14: Milestone M3 (Flagship Agent v0 & Human-in-the-Loop)

### 9. Prompt Calibration for Regulatory Compliance Checklist
- **Problem**: When retriever returns multiple chunks (e.g. 5 chunks including credit card debit rules alongside general customer service rules), the drafting LLM occasionally generated checklist items for non-applicable requirements (e.g., checking credit card rules for savings account fee disputes) and marked them `not_met`, causing unwanted guardrail escalations.
- **Fix**: Refined `DRAFT_SYSTEM` prompt in `agent/nodes.py` to instruct the model to only generate checklist items for rules *directly applicable* to the complaint narrative and account type.
- **Validation**: Tested on clean fee complaint (`fee_001`), which cleanly passed guardrails to `draft_ready_for_agent` without human intervention, while high-value fraud (`fraud_002`) and non-complaints (`query_003`) correctly paused for human review.

### 10. Human-in-the-Loop Pause & Resume State Pattern
- **Decision**: Implemented LangGraph interrupt pattern with `SqliteSaver` checkpointer in `agent/graph.py`.
- **Architecture**: When guardrail trip occurs (`escalated_to_human=True`), graph enters `human_review` node and halts with `interrupt()`. State is safely persisted in `data/checkpoints.db`. A human supervisor can inspect the checkpoint, and resume via `POST /reviews/{complaint_id}` with an approval or manual edit command, triggering the event logger and transitioning status to `approved_by_supervisor`.

---

## 2026-11-14: Milestone M4 (B3 MCP Tool Server & Bank Integration)

### 11. MCP Python SDK v2 Architecture (`MCPServer`)
- **Decision**: Deployed `b3_mcp_server.py` using official MCP Python SDK v2 (`from mcp.server.mcpserver import MCPServer`), replacing legacy FastMCP v1 imports per specification.
- **Protocol**: Exposed over Streamable HTTP on port 8001 (`http://localhost:8001/mcp`) with client interoperability supporting both live microservice networking and seamless in-process testing (`BankTools("inprocess")`).

### 12. Two-Phase Cryptographic Approval Token for Gated Writes
- **Decision**: Enforced an HMAC-SHA256 signature protocol (`approval_token(ticket_id, amount_inr)`) for the `request_refund` write tool.
- **Security Guarantee**: The model is completely incapable of originating refunds autonomously. Approval tokens are generated exclusively by the API server when an authorized human supervisor submits `approve_refund=True`. Tokens are cryptographically bound to the exact ticket ID and numerical amount, preventing replay, tampering, or privilege escalation.
- **Idempotency**: Implemented database-level idempotency via SQLite `UNIQUE(ticket_id, amount_inr)` constraints to prevent double-refund execution during network retries.

---

## 2026-11-14: Milestone M5 (B2 Full RAG Evaluation Harness & Golden Set)

### 14. Golden Dataset Scale-Up & Partitioning (100 Questions)
- **Design**: Expanded the benchmark from 50 to 100 questions adhering to the specification: 30 single fact, 20 definition/eligibility, 20 paraphrased retail customer language, 10 multi-section cross-circular questions, and 20 out-of-scope refusal queries.
- **Audit Trace**: Sourced verbatim quotes from all 5 downloaded RBI circulars with exact `doc_id:section` citations documented in `docs/candidate_questions_100.md`.
- **Zero Leakage**: Enforced a 70/30 partition (`eval/golden_dev.jsonl` with 70 questions for experimental tuning; `eval/golden_test.jsonl` with 30 held-out questions locked for single-pass final reporting).

### 15. Chunking Strategy & Retrieval Paradigm Findings
- **Chunking Benchmark on Dev Set (70 Questions)**:
  - `fixed300_bm25` (naive 300-word window, ignoring headings): `hit@5` = 0.679, `recall@5` = 0.661, `mrr` = 0.535.
  - `section150_bm25` (small 150-word section chunks): `hit@5` = 0.786, `recall@5` = 0.777, `mrr` = 0.652.
  - `section300_bm25` (section-aware 300-word chunks): `hit@5` = 0.804, `recall@5` = 0.786, `mrr` = 0.662.
- **Retriever Benchmark (Section-300 Chunks)**:
  - `section300_dense`: `hit@5` = 0.786, `recall@5` = 0.768, `mrr` = 0.585.
  - `section300_hybrid`: `hit@5` = **0.804**, `recall@5` = **0.795**, `mrr` = 0.647.
  - `section300_hybrid_k3`: `hit@3` = 0.750, `recall@3` = 0.714, `mrr` = 0.634.
- **Key Takeaways**:
  1. Section-aware chunking raised `hit@5` by **+12.5 percentage points** over naive fixed chunking because legal provisions rely on cohesive section titles and preamble context.
  2. Reducing chunk size to 150 words caused context fragmentation, reducing recall.
  3. Hybrid retrieval (BM25 + Dense RRF fusion) achieved the highest overall recall (0.795), ensuring cross-clause coverage. Reducing $k$ to 3 dropped recall by 8.1%, proving $k=5$ is necessary for complex regulatory queries.

### 16. LLM Judge Prompt Calibration
- **Problem**: When evaluating concise factual answers (e.g. "Rupees 20 lakh"), the original judge prompt instructed the model to "List every claim in the answer that the context does not support. Be strict", leading the 3B model to copy the valid claim into `unsupported_claims` and falsely flag it as unsupported.
- **Fix**: Calibrated `JUDGE_SYSTEM` in `b2_eval.py` to instruct the judge to verify whether factual statements are directly substantiated by the context, leaving `unsupported_claims` empty when facts align, and only listing claims that contradict or are missing from the source context.
- **Validation**: Tested against both supported answers and synthetic hallucinations; correctly marked legitimate answers as `fully_supported=True` while catching injected factual distortions.

---

## Later List (Backlog / Deferred Ideas)
- Optional Presidio PII entity recognizers (`presidio-analyzer`, `presidio-anonymizer`) for enhanced name recognition if regex rules show false negatives.
- Hosted Groq/Gemini API fallback integration for heavy evaluation runs if local Ollama tokens/sec is low on CPU.
- Production vector store upgrade (pgvector / Azure AI Search) documented for consulting architecture presentations.
