#!/usr/bin/env python3
"""Extracted-score summaries and hypothetical threshold routing.

Two audit questions: does reported confidence still separate right from wrong
under each specification, and how much review does a confidence threshold buy?
"""
from pathlib import Path
import pandas as pd

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "06_outputs" / "tables" / "current"
OUT.mkdir(parents=True, exist_ok=True)

d = pd.read_csv(REPO / "05_evidence" / "confidence_per_question.csv").dropna(subset=["top1_prob"])

print("=" * 80)
print("CONFIDENCE CALIBRATION BY SPECIFICATION")
print("=" * 80)
rows = []
for v, g in d.groupby("variant"):
    right, wrong = g[g["correct"] == 1], g[g["correct"] == 0]
    rows.append({
        "specification": v,
        "mean_confidence": round(g["top1_prob"].mean(), 4),
        "pct_above_99": round(100 * (g["top1_prob"] >= 0.99).mean(), 1),
        "conf_when_right": round(right["top1_prob"].mean(), 4),
        "conf_when_wrong": round(wrong["top1_prob"].mean(), 4),
        "separation": round(right["top1_prob"].mean() - wrong["top1_prob"].mean(), 4),
    })
cal = pd.DataFrame(rows).sort_values("separation")
print(cal.to_string(index=False))
print("\n  'separation' is how much more confident the model is when right than")
print("  when wrong. Near zero means little mean separation under this extractor; AUROC can still carry signal.")

# --- threshold curve -----------------------------------------------------
print("\n" + "=" * 80)
print("CONFIDENCE THRESHOLD — what auditing at a cutoff buys you")
print("=" * 80)
tr = []
for v, g in d.groupby("variant"):
    base = g["correct"].mean()
    for t in [0.90, 0.95, 0.99, 0.999]:
        keep = g[g["top1_prob"] >= t]
        if len(keep) < 20:
            continue
        tr.append({"specification": v, "threshold": t,
                   "coverage_pct": round(100 * len(keep) / len(g), 1),
                   "accuracy_kept": round(keep["correct"].mean(), 4),
                   "lift_pp": round(100 * (keep["correct"].mean() - base), 1),
                   "review_burden_pct": round(100 * (1 - len(keep) / len(g)), 1)})
th = pd.DataFrame(tr)
print(th[th["threshold"] == 0.99].to_string(index=False))
print("\n  At the same 0.99 cutoff, the share of outputs routed to hypothetical review")
print(f"  ranges from {th[th.threshold==0.99]['review_burden_pct'].min():.1f}% to "
      f"{th[th.threshold==0.99]['review_burden_pct'].max():.1f}% across the retained configurations under this implemented extraction rule.")

cal.to_csv(OUT / "calibration_by_specification.csv", index=False)
th.to_csv(OUT / "threshold_review_burden.csv", index=False)
print(f"\nWritten to {OUT}/")
