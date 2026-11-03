#!/usr/bin/env python3
"""Inclusion-criteria robustness: do the headline results survive different
defensible choices about which questions to include?

The cherry-picking defence. Every subset below is a choice another researcher
could reasonably have made. If the findings move, the corpus choice is itself
a specification.
"""
from pathlib import Path
import pandas as pd

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "06_outputs" / "tables" / "current"
OUT.mkdir(parents=True, exist_ok=True)

main = pd.read_csv(REPO / "01_data" / "splits" / "sst_main.csv")
buckets = pd.read_csv(REPO / "05_evidence" / "three_bucket_classification.csv")
conf = pd.read_csv(REPO / "05_evidence" / "confidence_per_question.csv")
d = main.merge(buckets, left_on="id", right_on="question_id")
d["qlen"] = d["question"].astype(str).str.split().str.len()
d["engagements"] = d["question"].astype(str).str.contains("official engagements", case=False, na=False)

EXCLUDED_TOPICS = ["Culture", "Foreign Trade", "Public Lands"]
subsets = {
    "ALL (as published)":        d,
    "drop procedural 'official engagements'": d[~d["engagements"]],
    "drop Culture, Foreign Trade and Public Lands": d[~d["gold_name"].isin(EXCLUDED_TOPICS)],
    "drop shortest quartile":     d[d["qlen"] > d["qlen"].quantile(0.25)],
    "drop longest quartile":      d[d["qlen"] < d["qlen"].quantile(0.75)],
    "exclude validation subset":  d[~d["is_validation"]] if "is_validation" in d else d,
    "1997-2002 only":             d[d["year"] <= 2002],
    "2003-2008 only":             d[d["year"] >= 2003],
}

rows = []
for name, s in subsets.items():
    if len(s) < 100:
        continue
    n = len(s)
    b1 = (s["bucket"] == "B1_always_right").mean() * 100
    cont = s["bucket"].isin(["B2_sometimes_right", "B3_divergent_wrong"]).mean() * 100
    b4 = (s["bucket"] == "B3_unanimous_wrong").mean() * 100
    ids = set(s["id"])
    c = conf[conf["question_id"].isin(ids)]
    acc = c.groupby("variant")["correct"].mean()
    rows.append({"subset": name, "n": n,
                 "always_right_pct": round(b1, 1),
                 "contingent_pct": round(cont, 1),
                 "always_wrong_pct": round(b4, 1),
                 "acc_min": round(acc.min(), 4), "acc_max": round(acc.max(), 4),
                 "acc_spread_pp": round(100 * (acc.max() - acc.min()), 2)})
r = pd.DataFrame(rows)

print("=" * 96)
print("INCLUSION-CRITERIA ROBUSTNESS — do the findings survive other reasonable corpora?")
print("=" * 96)
print(r.to_string(index=False))

base = r.iloc[0]
print(f"\n  Published: {base['contingent_pct']}% specification-contingent, "
      f"accuracy spread {base['acc_spread_pp']} pp")
print(f"  Across all {len(r)} subsets: contingent ranges "
      f"{r['contingent_pct'].min()}-{r['contingent_pct'].max()}%, "
      f"spread ranges {r['acc_spread_pp'].min()}-{r['acc_spread_pp'].max()} pp")
worst = r.loc[r["contingent_pct"].idxmax()]
print(f"  Most contingent subset: {worst['subset']} at {worst['contingent_pct']}%")
if r["contingent_pct"].max() - r["contingent_pct"].min() < 10:
    print("\n  -> The core finding is stable across inclusion choices.")
else:
    print("\n  -> The corpus choice materially changes the result; report it as a specification.")

r.to_csv(OUT / "inclusion_criteria_robustness.csv", index=False)
print(f"\nWritten to {OUT}/")
