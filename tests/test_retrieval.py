import numpy as np
from retrieval import BM25, Retriever, rrf, tokenize
from b2_eval import retrieval_metrics

CHUNKS = [
    {"chunk_id": "D:8:1", "doc_id": "D", "section": "8", "text": "The bank shall reply to a complaint within thirty days of receipt."},
    {"chunk_id": "D:10:1", "doc_id": "D", "section": "10", "text": "The ombudsman may award compensation for consequential loss."},
    {"chunk_id": "D:2:1", "doc_id": "D", "section": "2", "text": "A complaint means an expression of dissatisfaction."},
]

def test_tokenize_drops_stopwords():
    assert tokenize("The bank SHALL reply") == ["bank", "reply"]

def test_bm25_ranks_the_right_section_first():
    s = BM25([c["text"] for c in CHUNKS]).scores("how many days to reply")
    assert int(np.argmax(s)) == 0

def test_rrf_rewards_agreement():
    assert rrf([[0, 1, 2], [1, 0, 2]])[:2] in ([0, 1], [1, 0])
    assert rrf([[2, 0], [2, 1]])[0] == 2

def test_hybrid_search_with_fake_embeddings():
    vocab = ["reply", "days", "compensation", "loss", "dissatisfaction"]
    emb = lambda texts: [[t.lower().count(w) + 0.01 for w in vocab] for t in texts]
    r = Retriever(CHUNKS, "hybrid", np.array(emb([c["text"] for c in CHUNKS])), emb)
    hits = r.search("compensation for loss", k=2)
    assert hits[0]["chunk_id"] == "D:10:1" and hits[0]["rank"] == 1

def test_metrics():
    hits = [{"doc_id": "D", "section": "2"}, {"doc_id": "D", "section": "8"}]
    m = retrieval_metrics(hits, ["D:8"])
    assert m == {"hit": 1, "recall": 1.0, "rr": 0.5}
    assert retrieval_metrics(hits, ["D:10"])["hit"] == 0
