"""Mask personal data BEFORE any text is embedded, logged or sent to a model.

Layer 1 (always on): regular expressions for Indian and common identifiers.
Layer 2 (optional): Microsoft Presidio for names and locations.
"""
import re

# Order matters: the most specific patterns run first.
PATTERNS = [
    ("EMAIL",   r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b"),
    ("PAN",     r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"),
    ("IFSC",    r"\b[A-Z]{4}0[A-Z0-9]{6}\b"),
    ("CARD",    r"\b(?:\d{4}[ -]?){3}\d{4}\b"),
    ("AADHAAR", r"\b[2-9]\d{3}[ -]?\d{4}[ -]?\d{4}\b"),
    ("PHONE",   r"(?:\+91[ -]?\b|\b0?)[6-9]\d{9}\b"),
    ("ACCOUNT", r"\b\d{9,18}\b"),
    ("UPI",     r"\b[\w.-]{2,}@(?:ok\w+|ybl|paytm|upi|ibl|axl)\b"),
]
COMPILED = [(label, re.compile(rx)) for label, rx in PATTERNS]


def mask_regex(text: str) -> tuple[str, dict]:
    """Replace each match with <LABEL>. Returns masked text and counts per label."""
    counts = {}
    for label, rx in COMPILED:
        text, n = rx.subn(f"<{label}>", text)
        if n:
            counts[label] = counts.get(label, 0) + n
    # CFPB already masks private details as XXXX; standardise that too
    text, n = re.subn(r"\bX{2,}(?:/X{2,})*\b", "<REDACTED>", text)
    if n:
        counts["REDACTED"] = n
    return text, counts


_presidio = None

def mask(text: str, use_presidio: bool = False) -> tuple[str, dict]:
    """Regex first; then, if installed and switched on, Presidio for PERSON and LOCATION."""
    text, counts = mask_regex(text)
    if not use_presidio:
        return text, counts
    global _presidio
    if _presidio is None:
        from presidio_analyzer import AnalyzerEngine
        from presidio_anonymizer import AnonymizerEngine
        _presidio = (AnalyzerEngine(), AnonymizerEngine())
    analyzer, anonymizer = _presidio
    results = analyzer.analyze(text=text, language="en", entities=["PERSON", "LOCATION"])
    for r in results:
        counts[r.entity_type] = counts.get(r.entity_type, 0) + 1
    return anonymizer.anonymize(text=text, analyzer_results=results).text, counts
