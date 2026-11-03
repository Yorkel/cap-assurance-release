#!/usr/bin/env python3
"""Publication figures, generated from the deposited tables.

Figures use retained inputs and regenerated result tables; numerical equivalence is tested by the release verifier.

Palette is Okabe-Ito, which is colour-vision-deficiency safe. Identity is never
carried by colour alone: every series is also directly labelled or legended.
"""
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
import textwrap

import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parent.parent
T = REPO / "06_outputs" / "tables" / "current"
OUT = REPO / "06_outputs" / "figures"


# Okabe-Ito, minus yellow (poor on white)
BLUE, VERM, GREEN, SKY = "#0072B2", "#D55E00", "#009E73", "#56B4E9"
PURPLE, ORANGE, GREY = "#CC79A7", "#E69F00", "#888888"
INK, MUTED = "#1a1a1a", "#666666"

mpl.rcParams.update({
    "font.family": "serif", "font.size": 9,
    "axes.edgecolor": "#cccccc", "axes.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.labelcolor": INK, "text.color": INK,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "xtick.major.width": 0.8, "ytick.major.width": 0.8,
    "grid.color": "#e8e8e8", "grid.linewidth": 0.6,
    "figure.dpi": 150, "savefig.bbox": "tight", "savefig.pad_inches": 0.02,
})
LABEL = {
    "anchor": "Reference", "L2_C_drop_bundle": "Descriptions only",
    "L2_C_drop_fewshot": "No few-shot examples", "L2_F_reasoning": "Reasoning and label",
    "L2_F_cot": "Chain-of-thought", "L2_D_time": "Time scope",
    "L2_D_speaker": "Speaker scope", "L3_freetext": "Free-text output",
    "L1_claude_reconstructed": "Vendor swap*", "L1_claude": "Vendor swap*",
}
def save(fig, name):
    # PDF for typesetting; PNG at 300 dpi so it holds up placed in Word
    fig.savefig(OUT / f"{name}.pdf", metadata={"CreationDate": None, "ModDate": None})
    fig.savefig(OUT / f"{name}.png", dpi=300)
    plt.close(fig)
    print(f"  {name}.pdf / .png")

# ---------------------------------------------------------------- Figure 1
def fig1():
    import json
    data = pd.read_csv(T / "retained_configuration_accuracy.csv")
    data = data[data.variant != "anchor"].copy()
    data["rate"] = data.n_changed_anchor / data.n_paired_anchor * 100
    data = data.sort_values("rate")
    audit = json.loads((T / "retained_findings_audit.json").read_text())
    repeated = audit["repeats"]
    floor = repeated["mean_pair_disagreement"] * 100
    pair_rates = [n / 1200 * 100 for n in repeated["pair_disagreements"]]
    fig, ax = plt.subplots(figsize=(7.1, 4.3))
    y = np.arange(len(data))
    ax.axvspan(min(pair_rates), max(pair_rates), color="#dddddd", zorder=0)
    ax.barh(y, data.rate, color=BLUE, height=.62, zorder=2)
    ax.axvline(floor, color=INK, linewidth=1.3, label=f"Later repeat mean: {floor:.2f}%")
    ax.set_yticks(y); ax.set_yticklabels(data.variant.map(LABEL))
    for pos, value in enumerate(data.rate):
        ax.text(value + .12, pos, f"{value:.2f}%", va="center", fontsize=8)
    ax.set_xlim(0, 13); ax.set_xlabel("Paired labels differing from the anchor (%)")
    ax.set_title("Seven retained alternatives compared with later unchanged repeats", loc="left", fontsize=10, pad=10)
    ax.legend(loc="lower right", frameon=False, fontsize=8)
    ax.grid(axis="x", zorder=0); ax.set_axisbelow(True)
    fig.text(.02, .015, "Shading: range across repeat pairs, not a confidence interval. Runs occurred in different periods.", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, .05, 1, 1))
    save(fig, "fig1_floor_vs_configurations")


def fig2():
    data = pd.read_csv(REPO / "05_evidence/confidence_per_question.csv")
    rows = [{"variant": v, "share": 100 * g.top1_prob.lt(.99).mean()}
            for v, g in data.groupby("variant")]
    routing = pd.DataFrame(rows).sort_values("share")
    fig, ax = plt.subplots(figsize=(7.1, 4.4))
    y = np.arange(len(routing))
    ax.barh(y, routing.share, color=BLUE, height=.62)
    ax.set_yticks(y); ax.set_yticklabels(routing.variant.map(LABEL))
    for pos, value in enumerate(routing.share):
        ax.text(value + .5, pos, f"{value:.2f}%", va="center", fontsize=8)
    ax.set_xlim(0, 47); ax.set_xlabel("Outputs routed to hypothetical review at a 0.99 cutoff (%)")
    ax.set_title("Review routing under the implemented score-extraction procedure", loc="left", fontsize=10, pad=10)
    ax.grid(axis="x"); ax.set_axisbelow(True)
    fig.text(.02, .015, "The score need not describe the final answer. Reviewer decisions and effectiveness were not measured.", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, .05, 1, 1))
    save(fig, "fig2_confidence_collapse")


def fig3():
    shares = pd.read_csv(T / "topic_shares_reweighted.csv", index_col=0)
    variants = [v for v in LABEL if v in shares.index and not v.startswith("L1_")]
    shares = shares.loc[variants]
    fig, ax = plt.subplots(figsize=(7.1, 4.7))
    y = np.arange(len(shares))
    ax.barh(y - .17, shares["20.0"], height=.32, color=BLUE, label="Government Operations")
    ax.barh(y + .17, shares["19.0"], height=.32, color=VERM, label="International Affairs")
    ax.set_yticks(y); ax.set_yticklabels([LABEL[v] for v in variants])
    ax.invert_yaxis(); ax.set_xlabel("Post-stratified topic share (%)")
    ax.set_xlim(0, 21); ax.legend(loc="lower left", bbox_to_anchor=(0, 1.01), ncol=2, frameon=False, fontsize=8)
    ax.set_title("Estimated topic shares across the retained configurations", loc="left", fontsize=10, pad=34)
    ax.grid(axis="x"); ax.set_axisbelow(True)
    fig.text(.02, .015, "Descriptive estimates without uncertainty intervals. The same five topics remain most prominent.", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, .05, 1, 1))
    # Retain the established output path so links remain valid; the content now
    # shows full-period shares rather than unsupported annual-leader claims.
    save(fig, "fig3_leading_topic_by_year")


# ------------------------------------------------------- Figure A1
def figA1():
    f = pd.read_csv(T / "per_category_f1_by_specification.csv", index_col=0)
    f = f.loc[[i for i in f.index if i in LABEL]]
    lo, hi, med = f.min(), f.max(), f.median()
    order = (hi - lo).sort_values().index
    lo, hi, med = lo[order], hi[order], med[order]

    fig, ax = plt.subplots(figsize=(6.4, 5.4))
    y = np.arange(len(order))
    ax.hlines(y, lo, hi, color=SKY, lw=4.5, zorder=2)
    ax.scatter(med, y, s=26, color=BLUE, zorder=3, label="median")
    for yi, (a, b) in enumerate(zip(lo, hi)):
        ax.text(b + 0.012, yi, f"{(b - a):.2f}", va="center",
                fontsize=6.8, color=MUTED)
    ax.set_yticks(y)
    ax.set_yticklabels(order, fontsize=7.8)
    ax.set_xlabel("Per-category F1 across the eight configurations")
    ax.set_xlim(0, 1.06)
    ax.xaxis.grid(True)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=7.6, loc="lower right")
    ax.set_title("Per-category F1 range across the eight configurations\n"
                 "(bar = minimum to maximum; number = its width; dot = median)",
                 loc="left", fontsize=9.5, pad=8)
    save(fig, "figA1_per_category_f1_spread")


# ------------------------------------------------------- Figure A2
def figA2():
    a = pd.read_csv(T / "category_absorption.csv")
    top = (a.sort_values("share_of_errors_pct", ascending=False)
             .groupby("gold_category", as_index=False).first())
    top = top.sort_values("error_rate_pct")
    y = np.arange(len(top))

    fig, (ax, tx) = plt.subplots(
        1, 2, figsize=(7.0, 5.4), sharey=True,
        gridspec_kw=dict(width_ratios=[2.0, 1.25], wspace=0.02))

    ax.barh(y, top["error_rate_pct"], height=0.6, color=VERM, zorder=2)
    for yi, r in zip(y, top["error_rate_pct"]):
        inside = r > 12
        ax.text(r - 1.5 if inside else r + 1.5, yi, f"{r:.1f}%",
                va="center", ha="right" if inside else "left", fontsize=7.6,
                color="white" if inside else INK)
    ax.set_yticks(y)
    ax.set_yticklabels(top["gold_category"], fontsize=7.8)
    ax.set_xlabel("Classification outputs disagreeing with CAP,\n"
                  "pooled across eight configurations (%)")
    ax.set_xlim(0, 100)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.xaxis.grid(True)
    ax.set_axisbelow(True)

    # destinations live in their own column, so the quantitative axis stops
    # at 100% instead of being stretched to make room for text
    for yi, (dest, sh) in enumerate(zip(top["absorbed_into"],
                                        top["share_of_errors_pct"])):
        tx.text(0.02, yi, f"\u2192 {dest}", va="center", ha="left",
                fontsize=7.4, color=INK)
        tx.text(0.98, yi, f"{sh:.1f}%", va="center", ha="right",
                fontsize=7.4, color=MUTED)
    tx.set_xlim(0, 1)
    tx.set_xticks([])
    tx.tick_params(length=0)
    for s in tx.spines.values():
        s.set_visible(False)
    tx.set_title("Largest destination, and the\nshare of the errors it takes",
                 loc="left", fontsize=8, color=INK, pad=7)

    ax.set_title("Where errors go", loc="left", fontsize=9.8, pad=7)
    fig.text(0.045, -0.055, "Culture is omitted: all its outputs agree with CAP "
             "across these configurations (recall 1.00).",
             fontsize=7.0, color=MUTED)
    save(fig, "figA2_error_absorption")


# ------------------------------------------------------- Figure A3
def figA3():
    th = pd.read_csv(T / "threshold_review_burden.csv")
    d = th[th["threshold"] == 0.99].copy()
    d = d[d["specification"].isin(LABEL)]
    d["lab"] = d["specification"].map(LABEL)
    d = d.sort_values("lift_pp")
    openended = {"L2_F_cot", "L2_F_reasoning", "L3_freetext"}
    cols = [VERM if s in openended else BLUE for s in d["specification"]]
    y = np.arange(len(d))

    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.3), sharey=True)

    ax = axes[0]
    ax.barh(y, d["lift_pp"], height=0.62, color=cols, zorder=2)
    for yi, v in zip(y, d["lift_pp"]):
        ax.text(v + 0.3, yi, f"{v:.1f}", va="center", fontsize=8, color=INK)
    ax.set_yticks(y)
    ax.set_yticklabels(d["lab"], fontsize=8.4)
    ax.set_xlabel("Retained-subset accuracy\ngain (pp)")
    ax.set_xlim(0, 17.5)
    ax.xaxis.grid(True)
    ax.set_axisbelow(True)
    ax.set_title("Retained outputs", loc="left", fontsize=9.4, pad=7)

    ax = axes[1]
    ax.barh(y, d["review_burden_pct"], height=0.62, color=cols, zorder=2)
    for yi, v in zip(y, d["review_burden_pct"]):
        ax.text(v + 0.8, yi, f"{v:.1f}%", va="center", fontsize=8, color=INK)
    ax.set_xlabel("Outputs routed to\nhypothetical review (%)")
    ax.set_xlim(0, 52)
    ax.xaxis.grid(True)
    ax.set_axisbelow(True)
    ax.set_title("Hypothetical review share", loc="left", fontsize=9.4, pad=7)

    fig.subplots_adjust(wspace=0.10)
    fig.suptitle("At a 0.99 extracted-score cutoff, open-ended outputs (orange)"
                 "\nhave smaller retained-subset gains and "
                 "hypothetical review shares",
                 x=0.045, ha="left", fontsize=9.8, y=1.06)
    fig.text(0.045, -0.24, "The grouping of the three open-ended "
             "configurations and the other five also holds\nat 0.999, "
             "0.95 and 0.90.\nExtracted scores need not refer to the final answer; no reviewer outcomes are measured.",
             fontsize=7.2, color=MUTED)
    save(fig, "figA3_threshold_curves_all")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate paper figures from saved analysis outputs.")
    parser.add_argument("--data-root", type=Path, default=REPO)
    parser.add_argument("--tables-dir", type=Path)
    parser.add_argument("--output-dir", type=Path, default=OUT)
    parser.add_argument("--main-only", action="store_true")
    args = parser.parse_args()
    REPO = args.data_root
    T = args.tables_dir or REPO / "06_outputs/tables/current"
    OUT = args.output_dir
    OUT.mkdir(parents=True, exist_ok=True)
    print("Writing figures:")
    fig1(); fig2(); fig3()
    import hashlib, json
    main_names = ["fig1_floor_vs_configurations", "fig2_confidence_collapse", "fig3_leading_topic_by_year"]
    source_paths = {"06_outputs/tables/current/" + name: T / name for name in [
        "retained_configuration_accuracy.csv", "retained_findings_audit.json", "topic_shares_reweighted.csv"]}
    source_paths["05_evidence/confidence_per_question.csv"] = REPO / "05_evidence/confidence_per_question.csv"
    manifest = {
        "producer": "04_analysis/make_figures.py",
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "input_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in source_paths.items()},
        "output_sha256": {name + "." + ext: hashlib.sha256((OUT / (name + "." + ext)).read_bytes()).hexdigest()
                          for name in main_names for ext in ["pdf", "png"]},
        "roles": {main_names[0]: "Seven retained alternatives versus later repeats; descriptive comparison",
                  main_names[1]: "Hypothetical review routing under the extracted-score rule",
                  main_names[2]: "Full-period weighted topic shares; replaces annual-leader graphic"},
        "weighted_share_producer": "04_analysis/topic_shares_reweighted.py",
        "note": "Established output filenames retained for path continuity; titles and roles above describe current content."
    }
    (OUT / "retained_main_figure_provenance.json").write_text(json.dumps(manifest, indent=2) + "\n")
    if not args.main_only:
        print("Appendix:")
        figA1(); figA2(); figA3()
