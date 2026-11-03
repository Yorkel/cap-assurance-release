#!/usr/bin/env python3
"""Per-category F1 across specifications, and where wrong labels go.

Recovers the two analyses whose source CSVs were lost: the per-category
delta-F1 matrix (figure 4) and rare-category absorption (figure 5).
"""
from pathlib import Path
import pandas as pd

def f1_score(y_true, y_pred, labels, average=None, zero_division=0):
    """Per-class F1 without sklearn."""
    import collections
    yt, yp = list(y_true), list(y_pred)
    out = []
    for c in labels:
        tp = sum(1 for a, b in zip(yt, yp) if a == c and b == c)
        fp = sum(1 for a, b in zip(yt, yp) if a != c and b == c)
        fn = sum(1 for a, b in zip(yt, yp) if a == c and b != c)
        prec = tp / (tp + fp) if tp + fp else 0.0
        rec = tp / (tp + fn) if tp + fn else 0.0
        out.append(2 * prec * rec / (prec + rec) if prec + rec else 0.0)
    return out


REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "06_outputs" / "tables" / "current"
OUT.mkdir(parents=True, exist_ok=True)
ANCHOR = "anchor"

d = pd.read_csv(REPO / "05_evidence" / "confidence_per_question.csv").dropna(subset=["predicted_label"])
names = pd.read_csv(REPO / "01_data" / "category_names.csv")
NAME = dict(zip(names.gold_code, names.gold_name))
cats = sorted(d["gold"].unique())

rows = {}
for v, g in d.groupby("variant"):
    f1 = f1_score(g["gold"], g["predicted_label"], labels=cats, average=None, zero_division=0)
    rows[v] = dict(zip(cats, f1))
F = pd.DataFrame(rows).T
F.columns = [NAME.get(c, c) for c in F.columns]

delta = (F - F.loc[ANCHOR]).drop(index=ANCHOR)
spread = (F.max() - F.min()).sort_values(ascending=False)

print("=" * 76)
print("PER-CATEGORY F1 — how much each topic moves across specifications")
print("=" * 76)
out = pd.DataFrame({"anchor_f1": F.loc[ANCHOR].round(3), "min": F.min().round(3),
                    "max": F.max().round(3), "spread_pp": (spread * 100).round(1)})
out = out.sort_values("spread_pp", ascending=False)
print(out.head(12).to_string())
print(f"\n  Largest single-category swing: {spread.max()*100:.1f} pp ({spread.idxmax()})")
print(f"  Categories moving more than 5 pp: {int((spread > 0.05).sum())} of {len(spread)}")

print("\n" + "=" * 76)
print("WHERE WRONG LABELS GO — the worst categories")
print("=" * 76)
abs_rows = []
for gold in cats:
    sub = d[(d["gold"] == gold) & (d["predicted_label"] != d["gold"])]
    if len(sub) == 0:
        continue
    dest = sub["predicted_label"].value_counts(normalize=True)
    tot = len(d[d["gold"] == gold])
    for dcode, share in dest.head(3).items():
        abs_rows.append({"gold_category": NAME.get(gold, gold),
                         "error_rate_pct": round(100 * len(sub) / tot, 1),
                         "absorbed_into": NAME.get(dcode, dcode),
                         "share_of_errors_pct": round(100 * share, 1)})
A = pd.DataFrame(abs_rows)
worst = A.sort_values("error_rate_pct", ascending=False)["gold_category"].unique()[:4]
print(A[A["gold_category"].isin(worst)].to_string(index=False))

F.round(4).to_csv(OUT / "per_category_f1_by_specification.csv")
delta.round(4).to_csv(OUT / "per_category_delta_f1_vs_anchor.csv")
A.to_csv(OUT / "category_absorption.csv", index=False)
print(f"\nWritten to {OUT}/")
