"""Embed every chunk once and save the vectors (run again whenever chunks change)."""
import json
import numpy as np
import config
from llm import embed

chunks = [json.loads(line) for line in open(config.CHUNKS_PATH, encoding="utf-8")]
# nomic-embed-text expects a task prefix on documents and queries
vectors = embed(["search_document: " + c["text"] for c in chunks])
np.save(config.VECTORS_PATH, np.array(vectors, dtype=np.float32))
print(f"Saved {len(vectors)} vectors of size {len(vectors[0])} to {config.VECTORS_PATH}")
