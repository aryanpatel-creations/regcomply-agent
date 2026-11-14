from b1_parse_chunk import split_sections, chunk_document

DOC = ("Title page text\n1. Short title\nThese directions apply.\n"
       "8. Time limit for reply\n" + "Reply within thirty days. " * 120 + "\n10. Compensation\nUp to a limit.\n")
META = {"doc_id": "T", "title": "Test", "issued": "2026", "url": "u"}

def test_sections_found():
    assert [s["section"] for s in split_sections(DOC)] == ["0", "1", "8", "10"]

def test_subsections_found():
    doc_sub = "Preamble\n1. General provisions\nText here.\n1.1 Sub-clause heading\nDetails.\n"
    assert [s["section"] for s in split_sections(doc_sub)] == ["0", "1", "1.1"]

def test_long_section_is_split_with_overlap():
    parts = [c for c in chunk_document(DOC, META) if c["section"] == "8"]
    assert len(parts) == 2 and parts[0]["n_words"] == 300

def test_section_mode_prefixes_heading_fixed_mode_does_not():
    assert chunk_document(DOC, META)[1]["text"].startswith("Test - Section 1: Short title.")
    fixed = chunk_document(DOC, META, mode="fixed")
    assert not fixed[0]["text"].startswith("Test") and len(fixed) >= 2

def test_ids_are_unique():
    for mode in ("section", "fixed"):
        ids = [c["chunk_id"] for c in chunk_document(DOC, META, mode)]
        assert len(ids) == len(set(ids))
