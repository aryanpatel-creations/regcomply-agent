"""Three retrievers you can compare in B2: BM25 (keywords), dense (embeddings), hybrid (both)."""
import json, math, re
from collections import Counter
import numpy as np
import config

TOKEN = re.compile(r"[a-z0-9]+")
STOP = set("the a an of to in and or for on by with is are be shall may any its this that as at from".split())

def tokenize(text: str) -> list[str]:
    return [t for t in TOKEN.findall(text.lower()) if t not in STOP]


class BM25:
    """Classic BM25 in ~25 lines, so you can explain every part in an interview."""
    def __init__(self, docs: list[str], k1: float = 1.5, b: float = 0.75):
        self.k1, self.b = k1, b
        self.tf = [Counter(tokenize(d)) for d in docs]
        self.len = [sum(t.values()) for t in self.tf]
        self.avg = sum(self.len) / len(self.len)
        df = Counter(w for t in self.tf for w in t)
        n = len(docs)
        self.idf = {w: math.log(1 + (n - f + 0.5) / (f + 0.5)) for w, f in df.items()}

    def scores(self, query: str) -> np.ndarray:
        q = tokenize(query)
        out = np.zeros(len(self.tf))
        for i, (tf, dl) in enumerate(zip(self.tf, self.len)):
            for w in q:
                if w in tf:
                    f = tf[w]
                    norm = self.k1 * (1 - self.b + self.b * dl / self.avg)   # longer chunks count less
                    out[i] += self.idf[w] * f * (self.k1 + 1) / (f + norm)
        return out


class Dense:
    """Cosine similarity over pre-computed embeddings. No vector database needed below ~50k chunks."""
    def __init__(self, vectors: np.ndarray, embed_fn):
        self.m = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)
        self.embed_fn = embed_fn

    def scores(self, query: str) -> np.ndarray:
        q = np.array(self.embed_fn([query])[0])
        return self.m @ (q / np.linalg.norm(q))


def rrf(rankings: list[list[int]], k: int = 60) -> list[int]:
    """Reciprocal rank fusion: merge ranked lists without needing comparable scores."""
    score = Counter()
    for ranking in rankings:
        for rank, idx in enumerate(ranking):
            score[idx] += 1 / (k + rank + 1)
    return [idx for idx, _ in score.most_common()]


class Retriever:
    def __init__(self, chunks: list[dict], mode: str = "hybrid", vectors=None, embed_fn=None):
        self.chunks, self.mode = chunks, mode
        self.bm25 = BM25([c["text"] for c in chunks])
        self.dense = Dense(vectors, embed_fn) if mode in ("dense", "hybrid") else None

    def search(self, query: str, k: int = 5, pool: int = 20) -> list[dict]:
        ranks = []
        if self.mode in ("bm25", "hybrid"):
            ranks.append(list(np.argsort(-self.bm25.scores(query))[:pool]))
        if self.mode in ("dense", "hybrid"):
            ranks.append(list(np.argsort(-self.dense.scores(query))[:pool]))
        order = rrf(ranks) if len(ranks) > 1 else ranks[0]
        return [self.chunks[i] | {"rank": r + 1} for r, i in enumerate(order[:k])]


def load_retriever(mode: str = config.RETRIEVER) -> Retriever:
    chunks = [json.loads(line) for line in open(config.CHUNKS_PATH, encoding="utf-8")]
    if mode == "bm25":
        return Retriever(chunks, "bm25")
    from llm import embed
    query_embed = lambda qs: embed(["search_query: " + q for q in qs])   # nomic task prefix
    return Retriever(chunks, mode, np.load(config.VECTORS_PATH), query_embed)
