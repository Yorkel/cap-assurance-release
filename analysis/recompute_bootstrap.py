#!/usr/bin/env python3
"""Bootstrap: how often does each specification win on aggregate accuracy?

Resamples questions with replacement and records the winner each time. The
original run reported the anchor winning 507/1000; this recomputes it over the
8 specifications that retain item-level data.
"""
from pathlib import Path
import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "06_outputs" / "tables" / "current"
OUT.mkdir(parents=True, exist_ok=True)
RNG = np.random.default_rng(2026)
N_BOOT = 1000

d = pd.read_csv(REPO / "05_evidence" / "confidence_per_question.csv")
corr = d.pivot_table(index="question_id", columns="variant", values="correct", aggfunc="first").dropna()
M = corr.to_numpy()
names = list(corr.columns)
n = len(M)

wins = np.zeros(len(names), dtype=int)
for _ in range(N_BOOT):
    idx = RNG.integers(0, n, n)
    means = M[idx].mean(axis=0)
    wins[means.argmax()] += 1

res = pd.DataFrame({"specification": names, "wins": wins,
                    "win_rate": wins / N_BOOT}).sort_values("wins", ascending=False)
print("=" * 62)
print(f"BOOTSTRAP WINNER STABILITY — {N_BOOT} resamples, {len(names)} specifications")
print("=" * 62)
print(res.to_string(index=False))
top = res.iloc[0]
print(f"\n  Most frequent winner: {top['specification']} at {100*top['win_rate']:.1f}%")
print(f"  The anchor wins {100*float(res[res.specification=='anchor']['win_rate'].iloc[0]):.1f}% of resamples.")
if top["win_rate"] > 0.5:
    print(f"  -> {top['specification']} dominates: it is not a tie between these 8.")
    print("     Note the original 17-specification bootstrap reported the anchor")
    print("     winning 507/1000; that included the 9 specifications without")
    print("     item-level data, which cannot be resampled here.")
else:
    print("  -> the ranking is unstable under resampling; no specification is reliably best.")
res.to_csv(OUT / "bootstrap_winner_stability.csv", index=False)
print(f"\nWritten to {OUT}/")
