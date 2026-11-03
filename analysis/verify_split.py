#!/usr/bin/env python3
"""Read-only reconstruction of the sample from the supplied source-row order.

The reduced source CSV preserves original row order, including duplicates.
Its original identifiers are the one-based row numbers, assigned BEFORE
deduplication. No data are written and no model is called.
"""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent


def reconstruct_sample(root=ROOT):
    data = pd.read_csv(root / '01_data/uk_pmqs.csv')
    data.insert(0, 'id', range(1, len(data) + 1))
    data = data.drop_duplicates(['date', 'question', 'majortopic']).reset_index(drop=True)
    data['majortopic'] = data.majortopic.astype(int)
    selection = json.loads((root / '01_data/splits/category_selection.json').read_text())
    parts = [data[data.majortopic.eq(int(code))].sample(
        n=info['target_n'], random_state=42, replace=False
    ) for code, info in selection['categories'].items()]
    return pd.concat(parts).sample(frac=1, random_state=42).reset_index(drop=True)


def verify_sample(root=ROOT):
    actual = reconstruct_sample(root)
    saved = pd.read_csv(root / '01_data/splits/sst_main.csv')
    evidence = pd.read_csv(root / '05_evidence/three_bucket_classification.csv')
    assert len(actual) == len(saved) == len(evidence) == 1200
    assert actual.id.is_unique and saved.id.is_unique and evidence.question_id.is_unique
    # Check ordered IDs, reference labels and source text against the sample.
    pd.testing.assert_frame_equal(actual[['id', 'majortopic', 'date', 'question']],
                                  saved[['id', 'majortopic', 'date', 'question']],
                                  check_dtype=False)
    expected = evidence.set_index('question_id').gold_code.sort_index()
    pd.testing.assert_series_equal(actual.set_index('id').majortopic.sort_index(),
                                   expected, check_names=False, check_dtype=False)
    return len(actual)


if __name__ == '__main__':
    print(f'Exact sample reconstruction: {verify_sample():,} identifiers and CAP labels match; source dates/text match.')
