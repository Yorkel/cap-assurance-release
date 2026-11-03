#!/usr/bin/env python3
"""
Post-stratified version of the topic-share test.

The study sample is stratified to near-equal category sizes, so ranks sit
near-tied and reshuffle under any perturbation. This reweights each question
by (natural CAP share / sample share) for its gold category, recovering the
topic distribution Parliament actually produces, and asks whether the
specification effect survives.
"""

from pathlib import Path

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "06_outputs" / "tables" / "current"

# --- natural distribution from the full cleaned corpus -------------------
corpus = pd.read_csv(REPO / "01_data" / "uk_pmqs.csv")
corpus = corpus.drop_duplicates(
    subset=["date", "question", "majortopic"], keep="first"
).reset_index(drop=True)
corpus["majortopic"] = corpus["majortopic"].astype(int)
natural = corpus["majortopic"].value_counts(normalize=True)

df = pd.read_csv(REPO / "05_evidence" / "confidence_per_question.csv")
variants = list(dict.fromkeys(df["variant"]))
anchor = "anchor"

sample = df[df["variant"] == anchor]["gold"].value_counts(normalize=True)
weights = (natural / sample).dropna()
df["w"] = df["gold"].map(weights)
df = df.dropna(subset=["w"])

print("=" * 74)
print("NATURAL vs STRATIFIED CATEGORY DISTRIBUTION")
print("=" * 74)
comp = pd.DataFrame(
    {"natural_%": natural * 100, "sample_%": sample * 100}
).dropna().sort_values("natural_%", ascending=False)
print(comp.round(2).head(8).to_string())
print(f"\n  natural  range: {natural.min()*100:.2f}% – {natural.max()*100:.2f}%")
print(f"  sample   range: {sample.min()*100:.2f}% – {sample.max()*100:.2f}%")
print("  -> in the real corpus, topics are far from tied.")

# --- weighted topic shares ------------------------------------------------
rows = {}
for v in variants:
    sub = df[df["variant"] == v]
    rows[v] = sub.groupby("predicted_label")["w"].sum() / sub["w"].sum() * 100
shares = pd.DataFrame(rows).T.fillna(0).reindex(variants)
ranks = shares.rank(axis=1, ascending=False, method="min").astype(int)

out = []
for v in variants:
    if v == anchor:
        continue
    sd = (shares.loc[v] - shares.loc[anchor]).abs()
    rd = (ranks.loc[v] - ranks.loc[anchor]).abs()
    top10_a = set(ranks.loc[anchor].nsmallest(10).index)
    out.append(
        {
            "variant": v,
            "max_share_shift_pp": round(sd.max(), 2),
            "mean_share_shift_pp": round(sd.mean(), 2),
            "topics_changing_rank": int((rd > 0).sum()),
            "max_rank_move": int(rd.max()),
            "top10_changes": len(top10_a ^ set(ranks.loc[v].nsmallest(10).index)) // 2,
            "top5_changes": len(
                set(ranks.loc[anchor].nsmallest(5).index)
                ^ set(ranks.loc[v].nsmallest(5).index)
            )
            // 2,
        }
    )
res = pd.DataFrame(out).sort_values("max_share_shift_pp", ascending=False)

print("\n" + "=" * 74)
print("REWEIGHTED: SPECIFICATION EFFECT ON THE REAL ISSUE MAP")
print("=" * 74)
print(res.to_string(index=False))

print("\n" + "=" * 74)
print("TOP 8 TOPICS BY SHARE, EACH SPECIFICATION (%)")
print("=" * 74)
top = shares.loc[anchor].nlargest(8).index
print(shares[top].round(2).to_string())

spread = (ranks.max() - ranks.min())
print("\n" + "=" * 74)
print("VERDICT (reweighted)")
print("=" * 74)
print(f"  largest share shift vs anchor : {res['max_share_shift_pp'].max():.2f} pp")
print(f"  ranks not stable              : {int((spread>0).sum())} of {len(shares.columns)}")
print(f"  top-5 membership changes      : {res['top5_changes'].max()}")
print(f"  top-10 membership changes     : {res['top10_changes'].max()}")
print()
print("Descriptive full-period shares and ordering; no annual or downstream-impact inference.")

shares.to_csv(OUT / "topic_shares_reweighted.csv")
res.to_csv(OUT / "topic_share_stability_reweighted.csv", index=False)
print(f"\nWritten to {OUT}/")
