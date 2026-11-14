import json

questions = [json.loads(l) for l in open('eval/golden.jsonl', encoding='utf-8')]

md = [
    '# Complete Golden Test Set (100 Questions) for Aryan Patel\'s Verification\n\n',
    '**Milestone**: M5 (B2 Full RAG Evaluation Harness)  \n',
    '**Source Documents**: 5 Downloaded RBI Regulatory Circulars (`data/clean/chunks.jsonl`)  \n',
    '**Total Questions**: 100 (80 In-Scope, 20 Out-of-Scope)  \n',
    '**Dataset Partitions**: 70 Dev Questions (`eval/golden_dev.jsonl`), 30 Held-Out Test Questions (`eval/golden_test.jsonl`)  \n\n',
    '---\n\n',
    '## Breakdown by Category\n',
    '- **Single Fact** (statutory amounts, turnaround times, penalties): 30 questions\n',
    '- **Definition or Eligibility** (BSBD accounts, card issuance criteria, liability tiers): 20 questions\n',
    '- **Paraphrased / Customer Complaint Language** (realistic retail complaint phrasing): 20 questions\n',
    '- **Needs Two Sections / Multi-Circular** (cross-clause or cross-document rules): 10 questions\n',
    '- **Out of Scope** (wholesale, corporate lending, IBC, crypto, SGB, FDI): 20 questions\n\n',
    '---\n\n',
    '## Questions Directory\n\n'
]

for q in questions:
    qid = q["id"]
    question = q["question"]
    in_scope = str(q["in_scope"]).lower()
    md.append(f'### Question `{qid}`\n')
    md.append(f'- **Question**: **"{question}"**\n')
    md.append(f'- **In Scope**: `{in_scope}`\n')
    if q["in_scope"]:
        gold = ", ".join(q["gold_sections"])
        quote = q.get("quote", "")
        ref = q["reference"]
        md.append(f'- **Gold Section(s)**: `{gold}`\n')
        md.append(f'- **Exact Source Quote**: *"{quote}"*\n')
        md.append(f'- **Reference Answer**: {ref}\n\n')
    else:
        reason = q.get("quote", "Outside retail complaint handling")
        ref = q["reference"]
        md.append(f'- **Reason Out of Scope**: *{reason}*\n')
        md.append(f'- **Reference Refusal**: {ref}\n\n')

with open('docs/candidate_questions_100.md', 'w', encoding='utf-8') as f:
    f.writelines(md)

print('Saved docs/candidate_questions_100.md successfully!')
