"""Draw a seeded, stratified sample of grants as unlabelled eval cases (eval/cases.jsonl)."""
import json
import sqlite3
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent
df = pd.read_sql("SELECT * FROM grants WHERE amount > 0", sqlite3.connect(HERE.parent / "data" / "grants.sqlite"))
df["dlen"] = df["description"].fillna("").str.len()
df = df[(df["dlen"] >= 40) & (df["dlen"] <= 600)]
parts = [g.sample(3, random_state=7) for _, g in df.groupby("funder")]
cases = pd.concat(parts).reset_index(drop=True)
with open(HERE / "cases.jsonl", "w", encoding="utf-8") as f:
    for i, r in cases.iterrows():
        rec = {"id": i + 1, **{k: r[k] for k in ["grant_id", "funder", "recipient", "amount", "award_date", "title", "description"]},
               "label": {"theme": None, "beneficiary": None, "funding_type": None, "outcome_stated": None, "impact_case_score": None}}
        f.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
        print(f"#{rec['id']} [{r['funder'][:12]}] £{r['amount']:,.0f} {r['award_date']} | {r['recipient']}\n   {r['title']}\n   {r['description'][:420]}\n")
