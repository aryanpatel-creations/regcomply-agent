import json

chunks = [json.loads(l) for l in open('data/clean/chunks.jsonl', encoding='utf-8')]

def search(doc, term):
    res = [c for c in chunks if c['doc_id'] == doc and term.lower() in c['text'].lower()]
    print(f"=== {doc} : '{term}' ({len(res)} matches) ===")
    for c in res[:3]:
        idx = c['text'].lower().find(term.lower())
        snippet = c['text'][max(0, idx-40):min(len(c['text']), idx+160)].replace('\n', ' ')
        print(f"  Sec {c['section']} ({c['heading']}) [{c['chunk_id']}]:\n    ...{snippet}...\n")

terms = [
    ('MD_DIGISEC', 'factor'),
    ('MD_DIGISEC', 'session'),
    ('MD_DIGISEC', 'alert'),
    ('MD_DIGISEC', 'cooling'),
    ('MD_DIGISEC', 'international'),
    ('MD_DIGISEC', 'timeout'),
    ('MD_DIGISEC', 'velocity'),
    ('MD_DIGISEC', 'two factor'),
    ('MC_CUSTSERV', 'passbook'),
    ('MC_CUSTSERV', 'cheque'),
    ('MC_CUSTSERV', 'doorstep'),
    ('MC_CUSTSERV', 'inoperative'),
    ('MC_CUSTSERV', 'reconciliation'),
    ('MC_CUSTSERV', 'sms'),
    ('MD_CARDS', 'closure'),
    ('MD_CARDS', 'billing cycle'),
    ('MD_CARDS', 'unsolicited'),
    ('MD_CARDS', 'telemarketing'),
    ('MD_CARDS', 'insurance'),
    ('CIR_UNAUTH', 'burden of proof'),
    ('CIR_UNAUTH', 'shadow'),
    ('CIR_UNAUTH', 'third party'),
    ('RBIOS2021', 'reject'),
    ('RBIOS2021', 'non-maintainable'),
]

for doc, term in terms:
    search(doc, term)
