"""All settings in one place. Values come from a .env file or environment variables."""
import os
from dotenv import load_dotenv

load_dotenv()

# "ollama" = free, runs on your laptop.  "openai_compat" = a free hosted API (Groq or Gemini).
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
CHAT_MODEL = os.getenv("CHAT_MODEL", "qwen3.5:9b")           # use llama3.2:3b on an 8 GB laptop
EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.groq.com/openai/v1")
API_KEY = os.getenv("API_KEY", "")                           # never write the key in code
JSON_MODE = os.getenv("JSON_MODE", "schema")                  # schema | object | prompt

RETRIEVER = os.getenv("RETRIEVER", "hybrid")                  # hybrid | bm25 | dense
TOP_K = int(os.getenv("TOP_K", "5"))
CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", "0.7"))
REFUND_LIMIT_INR = int(os.getenv("REFUND_LIMIT_INR", "5000"))

DATA_DIR = os.getenv("DATA_DIR", "data")
CHUNKS_PATH = os.path.join(DATA_DIR, "clean", "chunks.jsonl")
VECTORS_PATH = os.path.join(DATA_DIR, "clean", "vectors.npy")
BANK_DB = os.getenv("BANK_DB", os.path.join(DATA_DIR, "mock_bank.db"))
CHECKPOINT_DB = os.getenv("CHECKPOINT_DB", os.path.join(DATA_DIR, "checkpoints.db"))
EVENT_LOG = os.getenv("EVENT_LOG", os.path.join(DATA_DIR, "ai_event_log.csv"))
MCP_URL = os.getenv("MCP_URL", "http://localhost:8001/mcp")
APPROVAL_SECRET = os.getenv("APPROVAL_SECRET", "change-me-in-.env")
