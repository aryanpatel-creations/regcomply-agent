# Deliverables Traceability Matrix (Category B)

Mapping promised deliverables to source files, tests, and completion statuses.

| Project | Promised Deliverable | Guide Reference | File / Evidence | Status |
|---|---|---|---|---|
| **M0** | **Environment & Test Suite Baseline** | Guide Sec 0 | `docs/ENVIRONMENT.md`, `requirements.lock`, `.env` | **Done** |
| **B1** | Cleaning script with flags (never silent fixes) | B1 Step 2 | `b1_clean_complaints.py`, `data/clean/complaints_clean.csv` | **Done** |
| **B1** | Data-quality report | B1 Step 2 | `data/clean/quality_report.csv` | **Done** |
| **B1** | Section-based chunks with metadata | B1 Step 3 | `b1_parse_chunk.py`, `data/clean/chunks.jsonl` (488 chunks) | **Done** |
| **B1** | PII masking step with a test set (>=40 tests) | B1 Step 1 | `pii.py`, `tests/test_pii.py` (49 tests, 75 total tests green) | **Done** |
| **B1** | Chunk inspection report (20 samples) | B1 Step 3 | `docs/chunk_inspection.md` | **Done & Signed Off** |
| **B2** | Golden test set: 100 questions (incl. quotes & 70/30 split) | B2 Step 1 | `eval/golden.jsonl`, `docs/candidate_questions_100.md` | **Done (100 Qs verified)** |
| **B2** | Vector Index (`nomic-embed-text`) | B2 Step 2 | `b2_build_index.py`, `data/clean/vectors.npy` | **Done (488 vectors)** |
| **B2** | Retrieval evaluation on Dev Set (BM25 vs Dense vs Hybrid) | B2 Step 3 | `b2_eval.py`, `eval/results.csv` | **Done (6 runs recorded)** |
| **B2** | 3 chunking methods; keyword vs hybrid search | B2 Step 5 | `eval/results.csv` (section300, fixed300, section150) | **Done (6 runs recorded)** |
| **B2** | Full answer evaluation & LLM judge check | B2 Steps 3–5 | `b2_eval.py`, `eval/judge_check.csv` | **Done (95% Judge Agreement)** |
| **B2** | Results table with latency & cost per query | B2 Steps 3, 5 | `eval/results.csv` (`answer_ms`, `cost_if_paid_usd`) | **Done (Full metrics recorded)** |
| **B3** | MCP server with read-only tools | B3 Step 2 | `b3_mcp_server.py` | **Done (Live HTTP on port 8001)** |
| **B3** | Write tool gated behind approval token | B3 Step 2 | `request_refund` + token logic in `b3_mcp_server.py` | **Done (HMAC token verified)** |
| **B3** | MCP tool tests | B3 Step 3 | `tests/test_mcp.py` | **Passing (8 tests green)** |
| **B3** | Short integration guide | B3 Step 5 | `INTEGRATION.md` | **Done** |
| **Flagship B** | LangGraph flow with SQLite checkpointer | FB Steps 1–4 | `agent/graph.py`, `agent/nodes.py`, `SqliteSaver` | **Done (Verified on 3 complaints)** |
| **Flagship B** | FastAPI service (`/docs`) | FB Step 5 | `api.py` | **Done (Verified via TestClient & /docs)** |
| **Flagship B** | Docker image & Compose | FB Step 6 | `Dockerfile`, `docker-compose.yml` | **Done (Compose syntax verified)** |
| **Flagship B** | Evaluation report from B2 | FB Step 7 | `docs/evaluation_report.md` | **Done** |
| **Flagship B** | Architecture diagram & 3-minute demo script | FB Step 10 | `README.md`, `docs/demo_script.md` | **Done** |
| **Flagship B** | Power BI A3 Fact Table Mapping | FB Step 8 | `docs/a3_mapping.md` | **Done** |
| **Portfolio** | Interview preparation document | Sec 4 / 35 | `docs/interview_answers.md` | **Done (9 core questions + case Qs)** |
| **Portfolio** | Architecture & Decisions log | Guide Sec 0 | `docs/DECISIONS.md` | **Done (16 decisions logged)** |
