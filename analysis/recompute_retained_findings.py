#!/usr/bin/env python3
"""Reproduce the principal retained-label results without APIs or reconstruction.

Run with the project environment. Outputs default to 06_outputs/tables/current;
--output-dir permits a separate validation run. The eight-configuration cohort
is the intersection of valid labels, so filtering uses the same denominator
before and after selection. Historical 17-configuration outputs are untouched.
"""
import argparse
import hashlib
import itertools
import json
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = {
    "anchor", "L2_C_drop_bundle", "L2_C_drop_fewshot", "L2_F_reasoning",
    "L2_F_cot", "L2_D_time", "L2_D_speaker", "L3_freetext",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def category_f1(frame, code):
    tp = int((frame.anchor.eq(code) & frame.gold.eq(code)).sum())
    fp = int((frame.anchor.eq(code) & frame.gold.ne(code)).sum())
    fn = int((frame.anchor.ne(code) & frame.gold.eq(code)).sum())
    denominator = 2 * tp + fp + fn
    return 2 * tp / denominator if denominator else float("nan")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path,
                        default=ROOT / "06_outputs/tables/current")
    out = parser.parse_args().output_dir
    labels_path = ROOT / "05_evidence/confidence_per_question.csv"
    sample_path = ROOT / "01_data/splits/sst_main.csv"
    labels = pd.read_csv(labels_path)
    sample = pd.read_csv(sample_path).set_index("id")
    gold = sample.majortopic
    assert gold.index.is_unique and len(gold) == 1200
    assert set(labels.variant) == EXPECTED
    assert not labels.duplicated(["variant", "question_id"]).any()
    assert labels.predicted_label.notna().all()
    assert labels.question_id.isin(gold.index).all()
    assert labels.gold.eq(labels.question_id.map(gold)).all()
    assert labels.predicted_label.eq(labels.gold).eq(labels.correct).all()
    wide = labels.pivot(index="question_id", columns="variant",
                        values="predicted_label").sort_index()
    complete = wide.dropna().astype(int)
    reference = gold.reindex(complete.index)
    correctness = complete.eq(reference, axis=0)
    unanimous = complete.nunique(axis=1).eq(1)
    buckets = pd.Series("", index=complete.index, name="bucket")
    buckets.loc[correctness.all(axis=1)] = "CAP-agreeing in all eight"
    buckets.loc[correctness.any(axis=1) & ~correctness.all(axis=1)] = "CAP-agreeing in some only"
    buckets.loc[~correctness.any(axis=1) & ~unanimous] = "CAP-disagreeing throughout, different labels"
    buckets.loc[~correctness.any(axis=1) & unanimous] = "CAP-disagreeing throughout, same label"
    assert buckets.ne("").all()
    order = ["CAP-agreeing in all eight", "CAP-agreeing in some only",
             "CAP-disagreeing throughout, different labels",
             "CAP-disagreeing throughout, same label"]
    counts = buckets.value_counts().reindex(order, fill_value=0)
    bucket_table = counts.rename_axis("bucket").rename("n").reset_index()
    bucket_table["denominator"] = len(complete)
    bucket_table["pct"] = bucket_table.n / len(complete) * 100
    filtered = []
    accuracy = []
    for variant in sorted(EXPECTED):
        before = correctness[variant]
        after = before.loc[unanimous]
        filtered.append({"variant": variant, "n_complete": len(before),
                         "correct_complete": int(before.sum()),
                         "accuracy_complete": float(before.mean()),
                         "n_unanimous": len(after), "correct_unanimous": int(after.sum()),
                         "accuracy_unanimous": float(after.mean()),
                         "increase_pp": float((after.mean() - before.mean()) * 100)})
        valid = labels[labels.variant.eq(variant)]
        paired = wide[["anchor", variant]].dropna() if variant != "anchor" else None
        accuracy.append({"variant": variant, "n_valid": len(valid),
                         "n_correct": int(valid.correct.sum()),
                         "accuracy": float(valid.correct.mean()),
                         "n_paired_anchor": len(paired) if paired is not None else len(valid),
                         "n_changed_anchor": int(paired.iloc[:, 0].ne(paired.iloc[:, 1]).sum())
                         if paired is not None else 0})
    anchor = pd.DataFrame({"anchor": complete.anchor, "gold": reference})
    selected = anchor.loc[unanimous]
    categories = []
    for code, group in anchor.groupby("gold"):
        retained = selected[selected.gold.eq(code)]
        before, after = category_f1(anchor, code), category_f1(selected, code)
        categories.append({"gold_code": int(code), "n_complete": len(group),
                           "n_unanimous": len(retained),
                           "excluded_pct": (1 - len(retained) / len(group)) * 100,
                           "anchor_f1_complete": before, "anchor_f1_unanimous": after,
                           "f1_increase_pp": (after - before) * 100})
    text = sample.question.astype(str)
    length = text.str.split().str.len()
    masks = {
        "All complete cases": pd.Series(True, index=sample.index),
        "Exclude official engagements": ~text.str.contains("official engagements", case=False),
        "Exclude Culture, Foreign Trade and Public Lands": ~gold.isin([23, 18, 21]),
        "Exclude shortest length quartile": length.gt(length.quantile(.25)),
        "Exclude longest length quartile": length.lt(length.quantile(.75)),
        "1997-2002": sample.year.le(2002),
        "2003-2008": sample.year.ge(2003),
    }
    robustness = []
    for name, mask in masks.items():
        ids = complete.index.intersection(sample.index[mask])
        correct = correctness.loc[ids]
        n_varying = int(complete.loc[ids].nunique(axis=1).gt(1).sum())
        acc = correct.mean()
        robustness.append({"subset": name, "n_complete": len(ids),
                           "n_varying_labels": n_varying,
                           "varying_labels_pct": n_varying / len(ids) * 100,
                           "accuracy_min": float(acc.min()), "accuracy_max": float(acc.max())})
    inputs = [labels_path, sample_path]
    repeats = {}
    prompts = {}
    raw_matches = 0
    fenced = 0
    for csv_path in sorted((ROOT / "05_evidence/raw/25_repeated_anchor").glob("REPEAT_*.csv")):
        rows = pd.read_csv(csv_path)
        assert len(rows) == len(sample) and rows.question_id.is_unique
        assert rows.parse_success.all() and set(rows.question_id) == set(sample.index)
        repeats[csv_path.stem] = rows.set_index("question_id").label
        jsonl_path = csv_path.with_suffix(".jsonl")
        seen = set()
        for line in jsonl_path.read_text().splitlines():
            record = json.loads(line)
            qid = record["question_id"]
            assert qid not in seen
            seen.add(qid)
            raw = record["raw_response"].strip()
            if raw.startswith("```"):
                fenced += 1
                raw = re.sub(r"^```(?:json)?\s*", "", raw)
                raw = re.sub(r"\s*```\s*$", "", raw)
            label = int(json.loads(raw)["label"])
            assert label == record["label"] == repeats[csv_path.stem].loc[qid]
            prompt = (record["system"], record["user"])
            assert prompts.setdefault(qid, prompt) == prompt
            raw_matches += 1
        assert seen == set(sample.index)
        inputs.extend([csv_path, jsonl_path])
    assert len(repeats) == 5
    reruns = pd.DataFrame(repeats)
    pair_counts = [int(reruns[a].ne(reruns[b]).sum())
                   for a, b in itertools.combinations(reruns.columns, 2)]
    pair = wide[["L2_C_drop_bundle", "L2_F_cot"]].dropna()
    audit = {
        "producer": str(Path(__file__).relative_to(ROOT)), "producer_sha256": digest(Path(__file__)),
        "input_sha256": {str(p.relative_to(ROOT)): digest(p) for p in inputs},
        "n_label_rows": len(labels), "n_questions": len(sample),
        "n_configurations": len(EXPECTED), "n_complete": len(complete),
        "missing_question_ids": [int(i) for i in wide.index[wide.isna().any(axis=1)]],
        "n_varying_labels": int((~unanimous).sum()),
        "equal_accuracy_pair": {"variants": list(pair.columns), "n": len(pair),
                                "correct": [int(pair[v].eq(gold.reindex(pair.index)).sum()) for v in pair],
                                "different_labels": int(pair.iloc[:, 0].ne(pair.iloc[:, 1]).sum())},
        "repeats": {"n_raw_answers_matched": raw_matches, "n_code_fences": fenced,
                    "pair_disagreements": pair_counts, "comparison_denominator": len(reruns) * len(pair_counts),
                    "mean_pair_disagreement": sum(pair_counts) / (len(reruns) * len(pair_counts)),
                    "n_questions_changing": int(reruns.nunique(axis=1).gt(1).sum())},
        "scope": "Recorded labels and raw later repeats; no inferred Claude labels or 17-configuration bucket summary used.",
    }
    outputs = {
        "retained_configuration_accuracy.csv": pd.DataFrame(accuracy),
        "retained_configuration_buckets.csv": bucket_table,
        "retained_agreement_filtering.csv": pd.DataFrame(filtered),
        "retained_agreement_filtering_by_category.csv": pd.DataFrame(categories),
        "retained_inclusion_robustness.csv": pd.DataFrame(robustness),
    }
    out.mkdir(parents=True, exist_ok=True)
    for name, frame in outputs.items():
        frame.to_csv(out / name, index=False)
    (out / "retained_findings_audit.json").write_text(json.dumps(audit, indent=2) + "\n")
    print(bucket_table.to_string(index=False))
    print(pd.DataFrame(filtered).to_string(index=False))
    print(f"Validated {raw_matches} raw repeat answers; wrote {len(outputs)} tables and audit JSON to {out}")


if __name__ == "__main__":
    main()
