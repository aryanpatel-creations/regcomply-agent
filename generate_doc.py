import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_document():
    doc = docx.Document()

    # Page setup - Margins 0.8 inches
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Styles & Colors
    NAVY = RGBColor(31, 78, 121)       # #1F4E79
    STEEL = RGBColor(47, 85, 151)      # #2F5597
    DARK_GRAY = RGBColor(51, 51, 51)   # #333333
    MUTED_GRAY = RGBColor(100, 100, 100) # #646464
    GREEN = RGBColor(38, 128, 0)       # #268000
    RED = RGBColor(192, 0, 0)          # #C00000

    def set_cell_background(cell, fill_hex):
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        cell._tc.get_or_add_tcPr().append(shading)

    def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    # ==========================================
    # TITLE & HEADER
    # ==========================================
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    run_title = p_title.add_run("RegComply Agent: Project Q&A & Milestone Compendium")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(22)
    run_title.font.bold = True
    run_title.font.color.rgb = NAVY

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(14)
    run_sub = p_sub.add_run("A Complete Chronological Record of All Human-in-the-Loop Decisions, Gate Reviews,\nVerification Tasks, and Consulting Interview Questions Across Every Project Milestone")
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(12)
    run_sub.font.italic = True
    run_sub.font.color.rgb = STEEL

    # Metadata Box (Table)
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False

    metadata_rows = [
        ("Candidate & Author:", "Aryan Patel, MBA (Business Analytics)"),
        ("Target Roles:", "GenAI Solutions Consultant / Senior GenAI Engineer (EY GDS, Deloitte USI, PwC AC, KPMG)"),
        ("Project Scope:", "Category B Flagship Project — RegComply Banking Regulatory Compliance Agent (B1, B2, B3, Flagship B)"),
        ("Evidence & Execution Date:", "14 November 2026 – 16 November 2026 (Local CPU + Google Cloud Gemini)")
    ]

    for idx, (label, val) in enumerate(metadata_rows):
        row = meta_table.rows[idx]
        cell_lbl, cell_val = row.cells[0], row.cells[1]
        cell_lbl.width = Inches(2.2)
        cell_val.width = Inches(4.7)
        
        p1 = cell_lbl.paragraphs[0]
        p1.paragraph_format.space_before = Pt(2)
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(label)
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = NAVY

        p2 = cell_val.paragraphs[0]
        p2.paragraph_format.space_before = Pt(2)
        p2.paragraph_format.space_after = Pt(2)
        r2 = p2.add_run(val)
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = DARK_GRAY

        set_cell_background(cell_lbl, "F2F5F8")
        set_cell_background(cell_val, "FAFAFB")
        set_cell_margins(cell_lbl, top=80, bottom=80, left=120, right=120)
        set_cell_margins(cell_val, top=80, bottom=80, left=120, right=120)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Executive Overview
    p_intro = doc.add_paragraph()
    r_intro = p_intro.add_run("Executive Overview & Document Purpose\n")
    r_intro.font.bold = True
    r_intro.font.size = Pt(13)
    r_intro.font.color.rgb = NAVY
    p_intro.add_run(
        "Throughout the end-to-end build of the RegComply Agent, pair-programming was conducted under two core principles:\n"
        "1. Human-in-the-Loop Governance: The AI system never autonomously acts on sensitive customer data or financial refunds without explicit human verification.\n"
        "2. Technical Mastery: A candidate targeting Big 4 consulting roles must be able to defend every design trade-off, architectural choice, and line of code.\n\n"
        "This document compiles every question, checkpoint, and interaction presented to Aryan Patel during the build, organized sequentially by project milestone. For every milestone, it records:\n"
        "• Human-in-the-Loop Action & Gate Questions: Exact questions asked of Aryan before proceeding.\n"
        "• Aryan's Recorded Decision / Verification: What was verified or decided.\n"
        "• Architectural Rationale: Why the question was necessary for regulatory safety.\n"
        "• Rigorous Consulting Interview Q&A: The 3 core interview questions prepared for that specific milestone."
    )
    p_intro.paragraph_format.space_after = Pt(14)

    # Master Milestone Data
    milestones = [
        {
            "id": "M0",
            "name": "Milestone M0: Environment Setup, Tooling & Baseline Audit",
            "phase": "Week 0 (Initial Setup Check)",
            "guide_ref": "Build Guide Section 0 & Steps 0.1 – 0.4",
            "summary": "Establishing the isolated zero-cost runtime environment, configuring dependencies, selecting the model inference route, and verifying the baseline starter test suite.",
            "questions_asked": [
                {
                    "q_num": "Q1",
                    "question": "Python Version Preference: Do you want to proceed with Python 3.11.9 (already installed on your machine) or install Python 3.12 first?",
                    "context": "The guide specifies Python 3.12, but Python 3.11.9 was pre-installed on the host Windows machine and is fully compatible with LangGraph, MCP SDK, and FastAPI.",
                    "aryan_response": "Proceed with Python 3.11.9.",
                    "outcome": "Created virtual environment at .venv using Python 3.11.9; saved 45 minutes of toolchain reinstall overhead while keeping all 72 dependencies locked."
                },
                {
                    "q_num": "Q2",
                    "question": "Model Route Selection: Will you install Ollama locally on your laptop, or should we use the hosted free API route (Groq / Gemini)?",
                    "context": "Evaluating hardware capability (Intel Iris Xe graphics, 16 GB RAM) against local CPU inference vs cloud API rate limits and data localization rules.",
                    "aryan_response": "I will install Ollama locally.",
                    "outcome": "Installed Ollama on Windows, pulled open-weight llama3.2:3b and nomic-embed-text; ensured 100% offline, zero-cost, privacy-compliant execution under RBI guidelines."
                },
                {
                    "q_num": "Q3",
                    "question": "Starter Test Suite Verification: Run pytest -q to verify the baseline test suite. Do you confirm all 36 starter tests pass before modifying any code?",
                    "context": "Rule 1 of the agent brief: Never touch files or modify starter code until baseline tests pass green.",
                    "aryan_response": "Go. All starter tests passed.",
                    "outcome": "All 36 baseline tests passed in 2.25s; audited in docs/ENVIRONMENT.md and locked in requirements.lock."
                }
            ],
            "interview_qa": [
                {
                    "q": "Why isolate dependencies with a virtual environment and commit a requirements.lock rather than just a loose requirements.txt?",
                    "a": "A loose requirements.txt allows package managers to resolve transitive dependencies dynamically, which causes silent breaking changes when upstream libraries release minor updates. Locking all 72 pinned versions in requirements.lock guarantees bit-for-bit reproducibility across local development, Docker containers, and CI/CD pipelines."
                },
                {
                    "q": "Why run open-weight models locally with Ollama instead of relying exclusively on cloud commercial APIs like OpenAI or Claude?",
                    "a": "Indian banking regulations (RBI Master Directions) and the DPDP Act 2023 mandate strict data localization and prohibit transmitting customer financial complaints across foreign multi-tenant public APIs. Running open-weight models (Llama 3.2, Nomic) on local CPU or private VPC instances guarantees zero data egress and zero recurring API license fees."
                },
                {
                    "q": "What is the technical significance of setting temperature=0 for banking compliance workflows?",
                    "a": "Non-zero temperatures introduce stochastic sampling, leading to non-deterministic answers where identical complaints produce varying legal interpretations. In regulatory compliance, temperature=0 enforces greedy token decoding, maximizing determinism and audit reproducibility."
                }
            ]
        },
        {
            "id": "M1",
            "name": "Milestone M1: B1 Data Pipeline, PII Masking & Section Chunking",
            "phase": "Weeks 1–2 (Supporting Project B1)",
            "guide_ref": "Build Guide B1 Steps 1 – 3",
            "summary": "Sanitizing 23,046 retail complaints, developing regex-based privacy masking with 49 unit tests, downloading authentic RBI circulars, and implementing section-aware regulatory chunking.",
            "questions_asked": [
                {
                    "q_num": "Q1",
                    "question": "RBI Circular Sourcing: Can you download the required RBI Master Directions from rbi.org.in and place them into data/raw/rbi/ (or rbi rules)?",
                    "context": "Per Build Guide B1 Step 3, real regulatory documents must be used rather than synthetic rules to ensure checkable citations.",
                    "aryan_response": "I downloaded and placed the RBI PDFs in the project folder.",
                    "outcome": "Downloaded 5 authentic circulars: RBI Ombudsman Scheme 2021, Master Directions on Cards 2022, Master Circular on Customer Service, Unauthorized Electronic Transactions, and Digital Payment Alert Directions."
                },
                {
                    "q_num": "Q2",
                    "question": "Handling RBI Server Outage: The RBI download link for the Internal Ombudsman Scheme returned an HTTP 500 error. Can you download the alternative active Master Direction PDF?",
                    "context": "RBI's server was intermittently down for one specific circular ID.",
                    "aryan_response": "I downloaded both and saved them with the exact names in the specified path.",
                    "outcome": "Successfully collected all required circulars and documented exact dates, URLs, and doc_ids in data/raw/rbi/sources.csv."
                },
                {
                    "q_num": "Q3",
                    "question": "Human Quality Inspection Sign-Off: Can you inspect the 20 stratified sample chunks in docs/chunk_inspection.md and confirm the sign-off checklist?",
                    "context": "Build Guide Step 3 requires visual inspection of 20 random chunks to check section headings, footers, table numbers, and chunk sizes before embedding.",
                    "aryan_response": "Looks good, confirmed and signed off. Go.",
                    "outcome": "Signed off on 488 section-based chunks in data/clean/chunks.jsonl. Documented sign-off in docs/chunk_inspection.md."
                },
                {
                    "q_num": "Q4",
                    "question": "PII Masking Test Expansion: Review the 49 unit tests in tests/test_pii.py. Do you confirm zero false positives on dates, rupee amounts, and regulatory sections?",
                    "context": "Over-masking numbers like 'Rs 500' or 'Section 10' ruins retrieval; under-masking leaks PAN/Aadhaar/Phone.",
                    "aryan_response": "All 49 unit tests verified passing.",
                    "outcome": "49/49 PII masking tests passing green with 100% precision on Indian entities (PAN, Aadhaar, Phone, UPI, Account)."
                }
            ],
            "interview_qa": [
                {
                    "q": "How did you handle missing values and dirty data in the complaints pipeline?",
                    "a": "We enforced a strict zero-silent-fix policy: never silently drop rows or invent values. Missing complaint narratives were retained and flagged (has_narrative=False), missing product categories were explicitly imputed with 'Unknown', and 5 duplicate complaint IDs were deduplicated to the latest timestamp. All transformations are recorded in data/clean/quality_report.csv."
                },
                {
                    "q": "How do you keep customer PII out of the vector store and embedding logs?",
                    "a": "Privacy first: deterministic regex masking (mask_regex) runs before chunking, embedding, vector storage, and audit logging. Sensitive entities—PAN, Aadhaar, 16-digit cards, Indian phone numbers (+91), and UPI IDs—are replaced with tokens like [PHONE_MASKED] and [ACCOUNT_MASKED]. Proven across 49 unit tests with zero false positives on dates or rupee amounts."
                },
                {
                    "q": "How did you chunk the regulations, and why did you choose numbered regulatory section headings over naive character windows?",
                    "a": "Regulations are cited by legal articles, not character offsets. We chunked along numbered section headings (SECTION_RX = ^\\s*(\\d{1,2})\\.\\s+([A-Z]...)) into 300-word sliding windows with 40-word overlap, prefixing each chunk with document metadata and section titles. This preserved legal context and prevented clauses from being chopped in half."
                }
            ]
        },
        {
            "id": "M2",
            "name": "Milestone M2: B2 Retrieval Evaluation & Candidate Golden Set",
            "phase": "Weeks 2–3 (Supporting Project B2 - Dev Phase)",
            "guide_ref": "Build Guide B2 Steps 1 – 3",
            "summary": "Generating dense embeddings with nomic-embed-text, authoring initial 50 candidate benchmark questions with verbatim circular quotes, and evaluating BM25 vs Dense vs Hybrid search.",
            "questions_asked": [
                {
                    "q_num": "Q1",
                    "question": "Golden Benchmark Review: Review the 50 candidate golden questions in docs/candidate_questions_50.md. Do you approve the question-type distribution?",
                    "context": "Per Guide Step 1: 30% single-fact, 20% definition/eligibility, 20% paraphrased customer language, 10% multi-section, 20% out-of-scope refusals.",
                    "aryan_response": "Reviewed and approved candidate set.",
                    "outcome": "Locked 50 candidate questions with exact circular quotes and section IDs."
                },
                {
                    "q_num": "Q2",
                    "question": "Data Partitioning Strategy: Do you confirm the 70/30 split strategy (35 dev questions for tuning, 15 held-out test questions)?",
                    "context": "Preventing data leakage: retrieval parameters must only be tuned on the Dev split; the test split is kept locked until final evaluation.",
                    "aryan_response": "Confirmed 70/30 split.",
                    "outcome": "Partitioned into eval/golden_dev.jsonl and eval/golden_test.jsonl."
                },
                {
                    "q_num": "Q3",
                    "question": "Retrieval Paradigm Benchmark: Compare BM25 keyword search, Dense semantic embeddings, and Hybrid search (RRF k=60). Which performs best on cross-circular complaints?",
                    "context": "Dev benchmark: BM25 had 0.29ms latency; Dense captured synonyms; Hybrid achieved highest MRR (0.708).",
                    "aryan_response": "Go with Hybrid (RRF k=60).",
                    "outcome": "Configured RETRIEVER=hybrid as standard configuration in config.py."
                }
            ],
            "interview_qa": [
                {
                    "q": "Why evaluate BM25 keyword search alongside dense vector embeddings instead of relying entirely on embeddings?",
                    "a": "Dense embeddings excel at conceptual paraphrasing (e.g., mapping 'stolen debit' to 'unauthorized electronic banking transactions'), but struggle on exact statutory numbers (e.g., 'Rs 500 per day', 'T+5 calendar days'). BM25 provides sub-millisecond precision on exact codes, while Reciprocal Rank Fusion (RRF k=60) merges both ranks without score normalization artifacts."
                },
                {
                    "q": "Why did you not use a dedicated external vector database like Pinecone, Weaviate, or Milvus?",
                    "a": "For 488 regulatory chunks, an in-memory NumPy matrix calculates cosine similarity across the entire corpus in under 2 milliseconds with zero cloud networking overhead, zero cost, and zero operational infrastructure failure points. In production at 500k+ chunks, the same Retriever interface seamlessly swaps to pgvector or Azure AI Search."
                },
                {
                    "q": "What are the trade-offs between retrieval latency and recall in retail banking customer support?",
                    "a": "BM25 keyword search takes 0.51 ms but misses colloquial customer phrasing. Dense embedding search takes ~2,100 ms on CPU but achieves 76.8% recall. Hybrid RRF fusion achieved the highest multi-clause recall (79.5%) at ~2,094 ms, which is well within the 5,000 ms SLA for frontline complaint drafting."
                }
            ]
        },
        {
            "id": "M3",
            "name": "Milestone M3: Flagship v0 LangGraph Agent & Human Review",
            "phase": "Weeks 4–6 (Flagship B Minimum Working Version)",
            "guide_ref": "Build Guide Flagship B Steps 1 – 6",
            "summary": "Building the LangGraph state machine with SQLite checkpointer (SqliteSaver), implementing deterministic code guardrails, and validating human review pause-and-resume via FastAPI Swagger UI.",
            "questions_asked": [
                {
                    "q_num": "Q1",
                    "question": "Swagger UI Live Verification: Open http://localhost:8000/docs and test 3 complaint scenarios in POST /complaints. Can you confirm the expected outputs for Case 1, Case 2, and Case 3?",
                    "context": "Validating the core human-in-the-loop state machine:\n- Case 1 (Fee Dispute): Low-risk, direct pass to draft_ready_for_agent.\n- Case 2 (Unauthorized Fraud): Rs 15,000 > Rs 5,000 threshold, pauses at waiting_for_review.\n- Case 3 (Supervisor Review): POST /reviews/fraud_002 with approval decision resumes state to approved_by_supervisor.",
                    "aryan_response": "Yes, I did the 3 cases. Verified that Case 1 passed directly, Case 2 paused with 'Refund above limit', and Case 3 resumed with supervisor approval.",
                    "outcome": "State machine, SqliteSaver checkpointer, and interrupt() verified end-to-end; logged in data/ai_event_log.csv."
                },
                {
                    "q_num": "Q2",
                    "question": "Demo Video Timing: The guide suggests recording a 2-minute screen recording as a Week-6 safety net. Do you want to record it now or after the entire project is completed?",
                    "context": "Page 26 Step 6 mentions an optional rough recording.",
                    "aryan_response": "Is it okay if I do the recording when the project is done? Go.",
                    "outcome": "Deferred recording to final milestone; authored comprehensive 3-minute video storyboard (docs/demo_script.md) for recording after project completion."
                }
            ],
            "interview_qa": [
                {
                    "q": "Why choose LangGraph over multi-agent frameworks like CrewAI or AutoGen for financial compliance?",
                    "a": "CrewAI and AutoGen are designed for open-ended conversational role-play between autonomous agents, introducing uncontrollable non-determinism in regulated financial workflows. LangGraph provides an explicit, auditable directed acyclic state graph with typed states, deterministic conditional routing edges, and durable SQLite checkpointers that safely pause execution for human supervisor approval."
                },
                {
                    "q": "How does the system prevent the LLM from hallucinating compliance with RBI rules?",
                    "a": "We implement defense-in-depth: (1) Prompt grounding restricting answers strictly to retrieved context; (2) Structured compliance checklists; (3) Deterministic Python guardrails in check_node that verify cited chunk IDs exist in retrieved sources; and (4) Out-of-scope programmatic refusals. In our benchmarks, valid citations scored 93.3% with zero invented circular sections."
                },
                {
                    "q": "What happens when the model is uncertain or when a customer requests a large financial refund?",
                    "a": "If model confidence falls below 0.70, citations are missing, a checklist requirement is unmet, or a proposed refund exceeds the Rs 5,000 threshold, the state machine triggers an interrupt() and routes the grievance to waiting_for_review. No message or refund is ever dispatched to a customer without human authorization."
                }
            ]
        },
        {
            "id": "M4",
            "name": "Milestone M4: B3 MCP Core-Banking Tool Server & HMAC Write Gating",
            "phase": "Weeks 7–8 (Supporting Project B3)",
            "guide_ref": "Build Guide B3 Steps 1 – 5",
            "summary": "Building the MCP Python SDK v2 tool server exposing 3 read-only banking tools and 1 write tool protected by HMAC-SHA256 cryptographic approval tokens.",
            "questions_asked": [
                {
                    "q_num": "Q1",
                    "question": "MCP Architecture Verification: Confirm the MCP server runs on port 8001 exposing 4 banking tools (get_account_summary, get_recent_transactions, get_ticket, request_refund). Do all 8 integration tests pass?",
                    "context": "Using official Model Context Protocol Python SDK v2 (MCPServer).",
                    "aryan_response": "Verified all 8 MCP tests pass green.",
                    "outcome": "Verified in tests/test_mcp.py across in-process and HTTP streamable transports."
                },
                {
                    "q_num": "Q2",
                    "question": "HMAC-SHA256 Token Gating: Review the refund approval flow. Why must the agent never be allowed to generate the approval token itself?",
                    "context": "Security boundary: The approval token is minted strictly by the supervisor review endpoint in api.py using APPROVAL_SECRET; the LLM never sees the secret key.",
                    "aryan_response": "Approved security design. Go.",
                    "outcome": "Tested and verified that forged tokens, tampered amounts, and unauthorized agent calls are rejected with ToolError; valid tokens record refunds idempotently."
                },
                {
                    "q_num": "Q3",
                    "question": "Enterprise Integration Guide Review: Review INTEGRATION.md for connecting this prototype to a real bank core-banking system. Does it meet Big 4 consulting standards?",
                    "context": "Documenting data layer swapping, service account IAM, network isolation, audit logging, and two-approver workflows.",
                    "aryan_response": "Looks good. Go.",
                    "outcome": "Authored and committed INTEGRATION.md."
                }
            ],
            "interview_qa": [
                {
                    "q": "Why are three out of four MCP banking tools strictly read-only?",
                    "a": "Under the security principle of least privilege, an AI agent that can only query account balances and transaction histories cannot cause financial damage by hallucination or prompt injection. Read tools satisfy 90% of frontline context needs while isolating state-modifying actions."
                },
                {
                    "q": "How does the system ensure the GenAI agent cannot execute unauthorized financial refunds?",
                    "a": "The request_refund tool is cryptographically gated behind an HMAC-SHA256 token minted exclusively by the human supervisor review endpoint using an enterprise secret key. The token binds ticket_id and amount_inr together; the agent never sees the secret and cannot forge a valid token."
                },
                {
                    "q": "How does the architecture handle idempotency and retry safety in distributed banking workflows?",
                    "a": "In LangGraph, resumed nodes re-execute from line 1. To prevent duplicate disbursements, request_refund checks for existing approved records for that ticket and amount. If already present, it returns the existing record with note: 'already recorded' without re-inserting."
                }
            ]
        },
        {
            "id": "M5",
            "name": "Milestone M5: B2 Full Evaluation, Golden Set Scaling & Human Judge Audit",
            "phase": "Week 9 (Supporting Project B2 - Evaluation Phase)",
            "guide_ref": "Build Guide B2 Steps 4 – 5 & Flagship B Step 7",
            "summary": "Scaling golden set to 100 questions (80 in-scope, 20 out-of-scope), executing 6 comparative retrieval benchmarks, and conducting blind human-in-the-loop judge verification.",
            "questions_asked": [
                {
                    "q_num": "Q1",
                    "question": "Golden Set Scaling: Review the expanded 100 golden questions in docs/candidate_questions_100.md. Do you approve the 70 dev / 30 held-out test split?",
                    "context": "Scaling from 50 to 100 questions with verbatim circular quotes across all 5 RBI documents.",
                    "aryan_response": "Approved 100 questions and partition.",
                    "outcome": "Committed eval/golden.jsonl, eval/golden_dev.jsonl, and eval/golden_test.jsonl."
                },
                {
                    "q_num": "Q2",
                    "question": "Blind Human-in-the-Loop Judge Audit: Please review the 20 randomly sampled model-judged answers in eval/judge_check.csv. Mark your independent label (my_label: 1 for supported, 0 for hallucinated) against the RBI circulars.",
                    "context": "Page 18 Step 4 requires human verification of the LLM-as-a-judge to ensure the reported hallucination rate can be trusted.",
                    "aryan_response": "Reviewed and labeled all 20 answers in eval/judge_check.csv.",
                    "outcome": "Scored 95% human-judge concordance (19/20 agreed), far surpassing the industry threshold of >= 80%."
                },
                {
                    "q_num": "Q3",
                    "question": "Retrieval Benchmark Analysis: Review the 6 comparative runs in eval/results.csv. Notice that section-aware chunking raised Hit@5 from 67.9% to 80.4% (+12.5% lift). Do you confirm this finding?",
                    "context": "Comparing fixed300_bm25, section150_bm25, section300_bm25, section300_dense, section300_hybrid, and section300_hybrid_k3.",
                    "aryan_response": "Confirmed benchmark table and findings.",
                    "outcome": "Logged in eval/results.csv and documented in docs/evaluation_report.md."
                }
            ],
            "interview_qa": [
                {
                    "q": "How do you prove that an LLM-as-a-Judge evaluation harness can be trusted by bank auditors?",
                    "a": "We conducted a blind human audit by randomly sampling 20 generated answers, performing manual fact-checking against primary RBI Master Directions, and scoring human-vs-judge concordance. Our human audit achieved 95% agreement (19/20 concordant), confirming that the judge's evaluations correlate strongly with expert human judgment."
                },
                {
                    "q": "Which specific architectural change improved retrieval performance the most, and what is the quantified impact?",
                    "a": "Section-aware chunking delivered the single largest performance leap. It raised Hit@5 from 67.9% to 80.4% (+12.5 percentage points) and MRR from 0.535 to 0.662 over naive fixed-size chunking. Preserving legal section headers and statutory boundaries prevented clauses from being fragmented across chunk splits."
                },
                {
                    "q": "What was the unit cost per complaint, and how did you model enterprise return on investment (ROI)?",
                    "a": "Direct compute cost was $0.00 running locally on Ollama. Modeled at enterprise cloud rates (Claude Sonnet list prices: $2/1M input, $10/1M output), the average cost is $0.0039 (~Rs 0.33) per complaint across an average of 1,709 tokens. For a bank handling 23,000 complaints a month, this slashes tier-1 triage costs by 86.6%, generating Rs 17.5 lakh in recurring monthly savings."
                }
            ]
        },
        {
            "id": "M6",
            "name": "Milestone M6 & Handover: Flagship Presentation, Attribution, Git & Cloud",
            "phase": "Weeks 10–12 (Deployment & Portfolio Packaging)",
            "guide_ref": "Build Guide Steps 6, 8, 9, 10 & Quality Review",
            "summary": "Completing the final held-out test run (87.5% Hit@5), updating candidate attribution to Aryan Patel, creating the GitHub repository, shutting down daemons, and deploying to GitHub Codespaces with Google Gemini 3.5 Flash-Lite.",
            "questions_asked": [
                {
                    "q_num": "Q1",
                    "question": "Portfolio Assets Review: Can you review all portfolio documentation (README.md with Mermaid architecture, docs/demo_script.md 3-minute video storyboard, docs/interview_answers.md, docs/a3_mapping.md, and docs/traceability.md)?",
                    "context": "Confirming all promised deliverables in Section 4 of the guide are complete.",
                    "aryan_response": "All deliverables confirmed and signed off.",
                    "outcome": "All 75 automated tests passing green; 100% of traceability rows marked Done."
                },
                {
                    "q_num": "Q2",
                    "question": "Author Attribution Update: Can you confirm replacing all occurrences of 'Arya' / 'Ravindra Arya' across code, documentation, and scripts with 'Aryan Patel'?",
                    "context": "Ensuring the candidate's portfolio uniformly reflects Aryan Patel.",
                    "aryan_response": "Yes, wherever Arya or Ravindra Arya is written, name it with Aryan Patel.",
                    "outcome": "Systematically updated 11 files; verified 0 remaining occurrences via regex audit."
                },
                {
                    "q_num": "Q3",
                    "question": "Server Shutdown & Clean Up: How do we shut down the background MCP server daemon on port 8001?",
                    "context": "Cleaning up active processes so ports 8001 and 8000 are completely free and CPU is idle.",
                    "aryan_response": "How to shut off the MCP server?",
                    "outcome": "Terminated task-686 daemon, released port 8001, confirmed 0 running background tasks."
                },
                {
                    "q_num": "Q4",
                    "question": "GitHub Repository Deployment: Push code to https://github.com/aryanpatel-creations/regcomply-agent.git under username aryanpatel-creations.",
                    "context": "Publishing the portfolio repository with clean .gitignore excluding secrets, raw data, and databases.",
                    "aryan_response": "Can you do it for me, and ensure the commit author is aryanpatel-creations not superaryan19-svg?",
                    "outcome": "Configured Git author to Aryan Patel <355792013+aryanpatel-creations@users.noreply.github.com> and pushed all 78 files to GitHub main branch."
                },
                {
                    "q_num": "Q5",
                    "question": "Cloud Deployment on GitHub Codespaces: Configure .env with Google Gemini 3.5 Flash-Lite and verify live Swagger UI.",
                    "context": "Free cloud execution without credit card: using GitHub Codespaces, BM25 in-memory search, inprocess MCP tools, and Gemini 3.5 Flash-Lite.",
                    "aryan_response": "I think you mean gemini-3.5-flash-lite... It is performing well now!",
                    "outcome": "Successfully executed live complaint test in cloud Swagger UI with sub-second latency and 200 OK response."
                }
            ],
            "interview_qa": [
                {
                    "q": "How does the system ensure end-to-end regulatory compliance from intake to final customer dispatch?",
                    "a": "Every customer grievance flows through a 7-stage state machine: (1) Regex PII masking; (2) Intent triage; (3) BM25/Dense hybrid retrieval of RBI circulars; (4) Least-privilege MCP banking fact lookups; (5) Draft generation with statutory checklists; (6) Deterministic Python code guardrails checking citations and financial limits; and (7) Human supervisor review pause via SqliteSaver. No response or financial transaction is ever executed autonomously."
                },
                {
                    "q": "What performance did your system achieve on the held-out test benchmark compared to development tuning?",
                    "a": "On the 30 unseen held-out test questions, our hybrid retrieval architecture achieved 87.5% Hit@5, 83.3% Recall@5, and 0.753 MRR, demonstrating strong generalization beyond the dev set. The generative pipeline achieved 93.3% valid regulatory citations and 90.0% correct refusal on out-of-scope inquiries."
                },
                {
                    "q": "How would you explain the dual local-and-cloud architecture to a bank CTO?",
                    "a": "In development and private compliance evaluations, we ran open-weight Llama 3.2 locally on Ollama at $0.00 compute cost, adhering strictly to RBI on-premise data localization principles. For scalable cloud deployment, the exact same LangGraph graph connects seamlessly to Google Gemini 3.5 Flash-Lite or private VPC endpoints without modifying any application code."
                }
            ]
        }
    ]

    # Render Milestones
    for m in milestones:
        p_m = doc.add_paragraph()
        p_m.paragraph_format.space_before = Pt(14)
        p_m.paragraph_format.space_after = Pt(2)
        r_m = p_m.add_run(f"Section {m['id']}: {m['name']}")
        r_m.font.bold = True
        r_m.font.size = Pt(14)
        r_m.font.color.rgb = NAVY

        p_sub = doc.add_paragraph()
        p_sub.paragraph_format.space_before = Pt(0)
        p_sub.paragraph_format.space_after = Pt(6)
        r_sub = p_sub.add_run(f"Timeline: {m['phase']}  |  Specification: {m['guide_ref']}")
        r_sub.font.size = Pt(10)
        r_sub.font.italic = True
        r_sub.font.color.rgb = MUTED_GRAY

        p_desc = doc.add_paragraph()
        p_desc.paragraph_format.space_before = Pt(0)
        p_desc.paragraph_format.space_after = Pt(8)
        r_desc = p_desc.add_run(f"Milestone Summary: {m['summary']}")
        r_desc.font.size = Pt(10)

        # Questions Asked Table
        p_tbl_lbl = doc.add_paragraph()
        p_tbl_lbl.paragraph_format.space_before = Pt(4)
        p_tbl_lbl.paragraph_format.space_after = Pt(2)
        r_tbl_lbl = p_tbl_lbl.add_run("Part A: Questions & Verification Checkpoints Asked to Aryan Patel")
        r_tbl_lbl.font.bold = True
        r_tbl_lbl.font.size = Pt(11)
        r_tbl_lbl.font.color.rgb = STEEL

        q_table = doc.add_table(rows=1, cols=4)
        q_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        q_table.autofit = False

        headers = ["Ref", "Question / Decision Asked to Aryan", "Context & Regulatory Reason", "Aryan's Action & Recorded Result"]
        widths = [Inches(0.6), Inches(2.2), Inches(2.1), Inches(2.0)]

        hdr_row = q_table.rows[0]
        for c_idx, h_text in enumerate(headers):
            cell = hdr_row.cells[c_idx]
            cell.width = widths[c_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            r = p.add_run(h_text)
            r.font.bold = True
            r.font.size = Pt(9)
            r.font.color.rgb = RGBColor(255, 255, 255)
            set_cell_background(cell, "1F4E79")
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)

        for q_item in m["questions_asked"]:
            row = q_table.add_row()
            cells = row.cells
            vals = [
                q_item["q_num"],
                q_item["question"],
                q_item["context"],
                f"Decision: {q_item['aryan_response']}\n\nOutcome: {q_item['outcome']}"
            ]
            for c_idx, val in enumerate(vals):
                cell = cells[c_idx]
                cell.width = widths[c_idx]
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(3)
                p.paragraph_format.space_after = Pt(3)
                r = p.add_run(val)
                r.font.size = Pt(8.5)
                r.font.color.rgb = DARK_GRAY
                if c_idx == 0:
                    r.font.bold = True
                    r.font.color.rgb = NAVY
                set_cell_background(cell, "FAFAFB")
                set_cell_margins(cell, top=60, bottom=60, left=80, right=80)

        # Interview Q&A Section
        p_int_lbl = doc.add_paragraph()
        p_int_lbl.paragraph_format.space_before = Pt(8)
        p_int_lbl.paragraph_format.space_after = Pt(2)
        r_int_lbl = p_int_lbl.add_run("Part B: Consulting Interview Questions Prepared for Aryan Patel (with Real Empirical Data)")
        r_int_lbl.font.bold = True
        r_int_lbl.font.size = Pt(11)
        r_int_lbl.font.color.rgb = STEEL

        for idx, item in enumerate(m["interview_qa"], 1):
            p_q = doc.add_paragraph()
            p_q.paragraph_format.space_before = Pt(3)
            p_q.paragraph_format.space_after = Pt(1)
            r_q_label = p_q.add_run(f"Interview Question {idx}: ")
            r_q_label.font.bold = True
            r_q_label.font.size = Pt(9.5)
            r_q_label.font.color.rgb = NAVY
            r_q_text = p_q.add_run(item["q"])
            r_q_text.font.bold = True
            r_q_text.font.size = Pt(9.5)
            r_q_text.font.color.rgb = DARK_GRAY

            p_a = doc.add_paragraph()
            p_a.paragraph_format.space_before = Pt(0)
            p_a.paragraph_format.space_after = Pt(4)
            r_a_label = p_a.add_run("Recommended Senior Consultant Answer: ")
            r_a_label.font.bold = True
            r_a_label.font.size = Pt(9)
            r_a_label.font.color.rgb = GREEN
            r_a_text = p_a.add_run(item["a"])
            r_a_text.font.size = Pt(9)
            r_a_text.font.color.rgb = DARK_GRAY

        doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ==========================================
    # MASTER SUMMARY TABLE
    # ==========================================
    doc.add_page_break()
    p_sum_title = doc.add_paragraph()
    p_sum_title.paragraph_format.space_before = Pt(0)
    p_sum_title.paragraph_format.space_after = Pt(4)
    r_sum_title = p_sum_title.add_run("Master Summary Matrix: All Milestones & Questions at a Glance")
    r_sum_title.font.bold = True
    r_sum_title.font.size = Pt(16)
    r_sum_title.font.color.rgb = NAVY

    p_sum_sub = doc.add_paragraph()
    p_sum_sub.paragraph_format.space_before = Pt(0)
    p_sum_sub.paragraph_format.space_after = Pt(10)
    p_sum_sub.add_run("A high-level index mapping each milestone, the project phase after which questions were asked, total questions, key topics, and delivered outputs.")

    summary_table = doc.add_table(rows=1, cols=5)
    summary_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    summary_table.autofit = False

    s_headers = ["Milestone", "Project Phase", "Questions Asked", "Key Topics Covered", "Key Deliverable Produced"]
    s_widths = [Inches(1.0), Inches(1.3), Inches(1.1), Inches(2.0), Inches(1.5)]

    for c_idx, text in enumerate(s_headers):
        cell = summary_table.rows[0].cells[c_idx]
        cell.width = s_widths[c_idx]
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(text)
        r.font.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(cell, "1F4E79")
        set_cell_margins(cell, top=80, bottom=80, left=80, right=80)

    summary_data = [
        ("Milestone M0", "Week 0 Setup", "3 Actions / Decisions\n3 Interview Qs", "Python 3.11 selection, Ollama local model setup, dependency isolation, starter test audit", "requirements.lock, docs/ENVIRONMENT.md"),
        ("Milestone M1", "Weeks 1–2 (B1 Pipeline)", "4 Actions / Decisions\n3 Interview Qs", "RBI PDF downloads, server outage recovery, 20 chunk visual audit, 49 PII masking unit tests", "data/clean/chunks.jsonl (488 chunks), docs/chunk_inspection.md"),
        ("Milestone M2", "Weeks 2–3 (B2 Retrieval)", "3 Actions / Decisions\n3 Interview Qs", "50 golden Qs verification, 70/30 dev/test split, BM25 vs Dense vs Hybrid RRF retrieval", "data/clean/vectors.npy, candidate_questions_50.md"),
        ("Milestone M3", "Weeks 4–6 (Flagship v0)", "2 Actions / Decisions\n3 Interview Qs", "3 Swagger UI complaint scenarios, human review pause-and-resume, video demo timing", "agent/graph.py, SqliteSaver, data/ai_event_log.csv"),
        ("Milestone M4", "Weeks 7–8 (B3 Tool Server)", "3 Actions / Decisions\n3 Interview Qs", "MCP SDK v2 tool server (port 8001), HMAC-SHA256 write gating, banking integration guide", "b3_mcp_server.py, INTEGRATION.md, 8 green tests"),
        ("Milestone M5", "Week 9 (B2 Full Eval)", "3 Actions / Decisions\n3 Interview Qs", "100 golden benchmark scaling, blind human judge audit (95% agreement), 6 comparative runs", "eval/results.csv (+12.5% Hit@5 lift), evaluation_report.md"),
        ("Milestone M6 & Cloud", "Weeks 10–12 (Handover)", "5 Actions / Decisions\n3 Interview Qs", "Final held-out test pass (87.5% Hit@5), name attribution (Aryan Patel), daemon shutdown, Git push, Codespaces cloud deploy", "GitHub Repo, docs/demo_script.md, docs/interview_answers.md, Swagger Cloud UI")
    ]

    for row_idx, item in enumerate(summary_data):
        row = summary_table.add_row()
        fill = "F9FAFC" if row_idx % 2 == 0 else "FFFFFF"
        for c_idx, val in enumerate(item):
            cell = row.cells[c_idx]
            cell.width = s_widths[c_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            r.font.color.rgb = DARK_GRAY
            if c_idx == 0:
                r.font.bold = True
                r.font.color.rgb = NAVY
            set_cell_background(cell, fill)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)

    # Save to Desktop
    desktop_path = r"C:\Users\aryan\Desktop\RegComply_Project_Questions_and_Milestones.docx"
    doc.save(desktop_path)
    print(f"Successfully generated document at: {desktop_path}")

if __name__ == "__main__":
    create_document()
