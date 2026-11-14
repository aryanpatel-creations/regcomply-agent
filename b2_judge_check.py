"""Is the LLM judge trustworthy? Label 20 answers yourself and measure agreement.

  python b2_judge_check.py sample hybrid_300w   -> writes eval/judge_check.csv (fill my_label: 1 or 0)
  python b2_judge_check.py score                  -> agreement between you and the judge
"""
import json, random, sys
import pandas as pd

if sys.argv[1] == "sample":
    rows = [json.loads(l) for l in open(f"eval/runs/{sys.argv[2]}.jsonl") if '"supported"' in l]
    sample = random.Random(1).sample(rows, min(20, len(rows)))
    pd.DataFrame([{"id": r["id"], "answer": r["answer"], "judge": int(r["supported"]), "my_label": ""}
                  for r in sample]).to_csv("eval/judge_check.csv", index=False)
    print("Open eval/judge_check.csv, read each answer against its sources, and fill my_label")
else:
    df = pd.read_csv("eval/judge_check.csv").dropna(subset=["my_label"])
    agree = (df["judge"] == df["my_label"]).mean()
    print(f"Agreement on {len(df)} answers: {agree:.0%}")
    print(pd.crosstab(df["my_label"], df["judge"], rownames=["you"], colnames=["judge"]))
    if agree < 0.8:
        print("Below 80%: improve the judge prompt or use a bigger judge model before trusting its numbers.")
