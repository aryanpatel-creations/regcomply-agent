import pandas as pd
import json

df = pd.read_csv('eval/judge_check.csv')
qmap = {json.loads(l)['id']: json.loads(l) for l in open('eval/golden.jsonl', encoding='utf-8')}

print('| # | Question ID | Question | AI Model Answer | Judge Verdict | Suggested Label |')
print('|---|---|---|---|---|---|')
for idx, r in df.iterrows():
    qid = r['id']
    q = qmap.get(qid, {})
    j = "1 (Supported)" if r['judge'] == 1 else "0 (Unsupported)"
    ans = str(r['answer']).replace('\n', ' ').strip()
    if len(ans) > 75:
        ans = ans[:72] + '...'
    q_text = str(q.get('question', '')).replace('\n', ' ').strip()
    if len(q_text) > 55:
        q_text = q_text[:52] + '...'
    print(f"| {idx+1} | `{qid}` | {q_text} | {ans} | **{j}** | `{r['judge']}` |")
