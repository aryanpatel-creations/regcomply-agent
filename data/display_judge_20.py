import pandas as pd
import json

df = pd.read_csv('eval/judge_check.csv')
qmap = {json.loads(l)['id']: json.loads(l) for l in open('eval/golden.jsonl', encoding='utf-8')}

for idx, r in df.iterrows():
    qid = r['id']
    q = qmap.get(qid, {})
    judge_label = "1 (Supported)" if r['judge'] == 1 else "0 (Unsupported)"
    print(f"[{idx+1:02d}/20] ID: {qid} | Judge: {judge_label}")
    print(f"  Question:  {q.get('question')}")
    print(f"  AI Answer: {r['answer']}")
    print(f"  Reference: {q.get('reference')}")
    print(f"  RBI Quote: {q.get('quote')}\n")
