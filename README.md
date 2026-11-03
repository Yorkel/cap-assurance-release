# AI assurance: anonymous review artifact

Code, frozen inputs and analytical materials accompanying a study of AI-produced information in public services. The package connects a topic-classification experiment with analysis of UK/EU assurance requirements. It is prepared for anonymous review, with independent Git history and anonymous contributor metadata.

## What is reproduced

- Read-only reconstruction of all 1,200 sampled identifiers and CAP reference labels from source-row order (`analysis/verify_split.py`), with source dates and text checked against the deposited sample.
- Eight retained GPT-4o configurations on 1,200 questions, with 1,199 complete cases; accuracy, matched-item variation, four-way CAP-agreement grouping, agreement filtering, pairwise AI–AI/AI–CAP comparison, paired tests, bootstrap rankings, category effects and full-period weighted topic shares.
- Five later unchanged repeats: 6,000 raw answers, prompt consistency, saved-label reconciliation and pairwise disagreement.
- Extracted-score discrimination and **hypothetical** threshold routing. These scores are not validated final-answer probabilities or observed human-review outcomes.
- Documentary counts: 37 units (19 UK/18 EU), 4,375 placements, 395 subthemes and 71 shared themes. The coding and interpretations are frozen analytical inputs, not newly generated or independently re-adjudicated by this build.
- The six charts and 22 numbered paper assets (16 tables and six figures). The manuscript table cells are frozen authored inputs; the verifier cross-checks numerical claims against recomputation. Legal interpretations are not inferred automatically from counts.

Historical 17-configuration summaries and the reconstructed vendor comparison are clearly separate from the principal eight-configuration results. See [evidence boundaries](docs/PROVENANCE.md), [claim map](docs/CLAIM_MAP.md) and [data sources and rights](DATA_SOURCES.md).

## Setup

Tested using CPython 3.9.6 and the exact dependency versions in `requirements.txt`.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
make all
```

Installing dependencies may use the network. **Reproduction itself is offline:** no API key, model download or paid experiment is needed. Tests read the supplied data. The AUROC bootstrap is the longest step.

Separate commands:

```sh
make reproduce   # rebuild experimental/documentary outputs and figures
make verify      # compare against frozen targets and paper-level assertions
make test        # independent data/provenance/interface checks
make checksums   # verify the supplied SHA256 manifest
```

The commands work from a checkout at any filesystem path; `make -C PATH all` also works. To choose a Python executable, use `make PYTHON=/path/to/python all`.

## Layout

| Path | Contents |
| --- | --- |
| `01_data/`, `02_specs/` | CAP inputs, sample, codebook and exact rendered prompts |
| `05_evidence/` | Retained labels/probability fields, raw later repeats and historical summaries |
| `analysis/` | Offline analyses and figure/table rendering |
| `documentary/` | Selected coding-sheet exports, coding frame, source catalogue, frozen themes and final findings |
| `expected/` | Frozen experimental numerical targets and six chart PDFs |
| `paper_tables/` | Frozen current manuscript table cells and captions |
| `paper_assets/` | Frozen 22 numbered PDF targets |
| `06_outputs/` | Rebuilt tables, audits, charts and paper-asset PDFs |
| `tools/`, `tests/` | Reproduction, verification, checksums and tests |

The complete policy-document bank and author-bearing Word files are not included. Source pointers and hashes identify the analysed texts. Some documentary units comprise several source files: the 54 source records are **not** 54 documentary units. AI-assisted thematic files are intermediate interpretation records; `documentary/final_findings.json` preserves the final findings used by the current draft.

The table PDFs are review/reference assets. They do not replace accessible native tables in the final typeset manuscript.

## Review anonymity

The package has independent Git history with anonymous attribution and no working-repository history, local usernames, author profiles, manuscript comments or session logs. Public names within parliamentary source material, policy documents and data-source attribution are retained as scientific source content. Use the anonymous mirror URL when referring to this artifact in an anonymous submission.

## Licensing and citation

The [MIT licence](LICENSE) covers original artifact code only. Upstream CAP data/codebook terms and third-party text rights remain separate; see `DATA_SOURCES.md`. Anonymous citation metadata is in `CITATION.cff`. Author identification and publication identifiers can be added after anonymous review.
