"""Clean complaints, flag problems (never silently fix them), mask PII, write a quality report.

Input: the filtered file from Category A, Step 4 (bank_complaints_24m.csv) with narratives joined.
"""
import pandas as pd
from pii import mask_regex

RAW = "data/raw/bank_complaints_24m.csv"
OUT, REPORT = "data/clean/complaints_clean.csv", "data/clean/quality_report.csv"

PRODUCT_GROUPS = {               # many CFPB product names -> 3 standard groups
    "credit card": "Cards", "prepaid card": "Cards",
    "checking": "Accounts", "savings": "Accounts",
    "money transfer": "Payments", "virtual currency": "Payments",
}

def product_group(p: str) -> str:
    p = str(p).lower()
    return next((g for key, g in PRODUCT_GROUPS.items() if key in p), "Other")

def profile(df: pd.DataFrame, stage: str) -> dict:
    return {"stage": stage, "rows": len(df),
            "duplicate_ids": int(df["Complaint ID"].duplicated().sum()),
            "missing_issue_pct": round(100 * df["Issue"].isna().mean(), 2),
            "missing_narrative_pct": round(100 * df["Consumer complaint narrative"].isna().mean(), 2),
            "products": df["Product"].nunique()}

def main():
    df = pd.read_csv(RAW, dtype=str)
    report = [profile(df, "before")]

    df = df.drop_duplicates(subset="Complaint ID", keep="last")
    for col in ["Date received", "Date sent to company"]:
        df[col] = pd.to_datetime(df[col], format="mixed", errors="coerce")

    # Flags: keep the row, mark the problem, let the reviewer decide
    lag = (df["Date sent to company"] - df["Date received"]).dt.days
    df["flag_bad_dates"] = lag.isna() | (lag < 0)
    df["flag_missing_issue"] = df["Issue"].isna()
    narrative = df["Consumer complaint narrative"].fillna("").str.strip()
    df["flag_short_narrative"] = narrative.str.len().between(1, 49)

    # Standardise categories
    df["product_group"] = df["Product"].map(product_group)
    df["Issue"] = df["Issue"].fillna("Unknown").str.strip()

    # Mask PII in the text BEFORE it goes anywhere else
    masked = narrative.map(mask_regex)
    df["narrative_masked"] = masked.map(lambda t: t[0])
    df["pii_items_masked"] = masked.map(lambda t: sum(t[1].values()))
    df = df.drop(columns=["Consumer complaint narrative"])      # the raw text never leaves this step

    masked_view = df.assign(**{"Consumer complaint narrative": df["narrative_masked"].replace("", None)})
    after = profile(masked_view, "after")
    after.update({"flag_bad_dates": int(df["flag_bad_dates"].sum()),
                  "flag_missing_issue": int(df["flag_missing_issue"].sum()),
                  "flag_short_narrative": int(df["flag_short_narrative"].sum()),
                  "pii_items_masked": int(df["pii_items_masked"].sum()),
                  "product_groups": df["product_group"].nunique()})
    report.append(after)

    df.to_csv(OUT, index=False)
    pd.DataFrame(report).to_csv(REPORT, index=False)
    print(pd.DataFrame(report).T)

if __name__ == "__main__":
    main()
