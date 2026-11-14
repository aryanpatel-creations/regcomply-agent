# Environment Specification (Milestone M0)

**Date Recorded**: 14 November 2026  
**Project Path**: `c:\Users\aryan\Desktop\project 2 genai`  
**Milestone**: M0 - Setup Check  

---

## 1. Hardware Specifications

| Component | Detected Specification |
|---|---|
| **Operating System** | Microsoft Windows 11 Home Single Language (Build 10.0.26300) |
| **Shell** | PowerShell |
| **System Memory (RAM)** | 16 GB visible (~15.79 GiB / 16,555,320 KB) |
| **GPU / Video Processor** | Intel(R) Iris(R) Xe Graphics (Integrated, ~2.1 GB shared memory) |
| **Discrete GPU** | None (NVIDIA GPU absent; CPU/iGPU execution) |

---

## 2. Software & Runtime Stack

| Component | Version / Setting |
|---|---|
| **Python** | 3.11.9 (64-bit) |
| **Virtual Environment** | `.venv` at project root |
| **Package Manager** | `uv` (v0.11.8) / `pip` (v26.1) |
| **Lockfile** | `requirements.lock` (72 pinned dependencies) |
| **Test Suite** | `pytest` v9.2.0 |
| **Orchestration Framework** | `langgraph` v1.2.22 |
| **Checkpoint Storage** | `langgraph-checkpoint-sqlite` v3.1.3 |
| **Tool Protocol** | Official MCP Python SDK v2 (`mcp` v2.3.0) |
| **Web Service** | `fastapi` v0.162.7, `uvicorn` v0.54.0 |

---

## 3. Model Configuration (.env)

| Parameter | Configuration Value |
|---|---|
| `LLM_PROVIDER` | `ollama` (local laptop execution) |
| `OLLAMA_URL` | `http://localhost:11434` |
| `CHAT_MODEL` | `llama3.2:3b` (primary local model; measured 12.81 tokens/s on Intel CPU; `qwen3.5:9b` also pulled) |
| `EMBED_MODEL` | `nomic-embed-text` (verified 768-dim vectors, ~2s per batch) |
| `RETRIEVER` | `hybrid` |
| `MCP_URL` | `http://localhost:8001/mcp` |
| `APPROVAL_SECRET` | 256-bit secure hex key |

*Token Evaluation Benchmark*:
- Chat Model (`llama3.2:3b`): **12.81 tokens/s** (Ollama on Intel Iris Xe / CPU).
- Embedding Model (`nomic-embed-text`): **768-dimensional embeddings** generated in ~2.0s.

---

## 4. Test Suite Baseline

- **Executed**: `.venv\Scripts\pytest.exe -v` (14 Nov 2026)
- **Outcome**: **36 passed in 2.25s** (100% green across chunking, graph orchestration, MCP tools, node guardrails, PII masking, and hybrid retrieval).
