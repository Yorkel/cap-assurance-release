#!/usr/bin/env python3
"""Per-specification AUROC: can reported confidence tell right from wrong?

AUROC is the probability that a randomly chosen correct item is given higher
confidence than a randomly chosen incorrect one. 0.5 is a coin flip - the
confidence signal carries no information about correctness.

Reported so the collapse is directly comparable to the selective-prediction and
calibration literature, which trades in AUROC rather than in review burden.
"""
from pathlib import Path
import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "06_outputs" / "tables" / "current"
OUT.mkdir(parents=True, exist_ok=True)

d = pd.read_csv(REPO / "05_evidence" / "confidence_per_question.csv").dropna(subset=["top1_prob"])

def auroc(scores, labels):
    """Mann-Whitney U form, with ties at 0.5 credit."""
    pos = np.asarray(scores)[np.asarray(labels) == 1]
    neg = np.asarray(scores)[np.asarray(labels) == 0]
    if len(pos) == 0 or len(neg) == 0:
        return np.nan
    order = np.argsort(np.concatenate([pos, neg]), kind="mergesort")
    ranks = np.empty(len(order), float)
    ranks[order] = np.arange(1, len(order) + 1)
    both = np.concatenate([pos, neg])
    # average ranks over ties
    s = pd.Series(both)
    ranks = s.rank(method="average").to_numpy()
    return (ranks[:len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg))

def boot_ci(scores, labels, n=2000, seed=2026):
    rng = np.random.default_rng(seed)
    s, l = np.asarray(scores), np.asarray(labels)
    vals = []
    for _ in range(n):
        i = rng.integers(0, len(s), len(s))
        v = auroc(s[i], l[i])
        if not np.isnan(v):
            vals.append(v)
    return np.percentile(vals, [2.5, 97.5])

rows = []
for v, g in d.groupby("variant"):
    a_top1 = auroc(g["top1_prob"], g["correct"])
    a_margin = auroc(g["margin"], g["correct"]) if "margin" in g else np.nan
    lo, hi = boot_ci(g["top1_prob"].to_numpy(), g["correct"].to_numpy())
    rows.append({
        "specification": v, "n": len(g),
        "auroc_top1_prob": round(a_top1, 4),
        "ci_low": round(lo, 4), "ci_high": round(hi, 4),
        "auroc_margin": round(a_margin, 4),
        "pct_conf_above_99": round(100 * (g["top1_prob"] >= 0.99).mean(), 1),
        "accuracy": round(g["correct"].mean(), 4),
    })
r = pd.DataFrame(rows).sort_values("auroc_top1_prob", ascending=False)

print("=" * 88)
print("PER-SPECIFICATION AUROC — does confidence separate correct from incorrect?")
print("=" * 88)
print(r.to_string(index=False))
print("\n  AUROC 0.5 = confidence carries no information about correctness.")
print(f"  Range across specifications: {r['auroc_top1_prob'].min():.4f} - {r['auroc_top1_prob'].max():.4f}")
chance = r[r["ci_low"] <= 0.5]
if len(chance):
    print(f"\n  Specifications whose 95% CI includes 0.5 (indistinguishable from chance):")
    for _, x in chance.iterrows():
        print(f"    {x['specification']:<20} AUROC {x['auroc_top1_prob']:.4f} "
              f"[{x['ci_low']:.4f}, {x['ci_high']:.4f}]")
r.to_csv(OUT / "auroc_by_specification.csv", index=False)
print(f"\nWritten to {OUT}/auroc_by_specification.csv")
