# Claim-to-evidence map

This map records what the artifact establishes. It is not a claim of complete historical raw-response recovery or observed deployed impact.

| Paper result | Producer / released evidence | Verification and boundary |
| --- | --- | --- |
| Similar aggregate performance; two configurations each 822/1,200 but 181 different labels | `analysis/recompute_retained_findings.py`; retained labels and audit | Direct retained-label recomputation; CAP agreement is a reference measure |
| Four groups: 717 / 215 / 76 / 191 on 1,199 complete questions | Same producer; Table 2 | The changing-label count is 215+76, counted once per question; no configuration-level rates are added |
| 291/1,199 = 24.27% receive at least two labels across the eight configurations | Same producer | Specific configuration set and population; not a universal model instability rate |
| AI–AI agreement exceeds AI–CAP agreement on matched cases | `analysis/compare_retained_agreement.py` | 28 configuration pairs and eight CAP comparisons, all on the same 1,199 questions; not independent confirmation or general human-versus-AI ability |
| Agreement filtering: anchor 835/1,199 → 717/908 | `analysis/recompute_retained_findings.py` | Selection changes the evaluation population; the classifier does not improve |
| Later-repeat pair counts 32/31/32/33/38/34/35/32/32/35; mean 334/12,000 = 2.783333% | Same producer, raw repeat JSONL/CSV; Table A10 | All 6,000 raw answers are reparsed; later timing and unpinned model alias remain |
| Seven alternatives change 5.00%–11.58% relative to the anchor | Same producer | Descriptive paired comparison; not an isolation of configuration effects from drift |
| 28 paired accuracy tests; six unadjusted, none after Holm/BH | `analysis/build_metrics.py` | Exact McNemar on matched items; multiple comparisons are explicit |
| Time-scope first in 889/1,000 bootstrap samples; anchor in 74 | `analysis/recompute_bootstrap.py` | Fixed seed and retained complete cohort; no claim of an optimal setup |
| Same five prominent topics, varying shares/order | `analysis/topic_shares_reweighted.py` | Post-stratified full-period shares; no annual-leader or downstream-decision inference |
| Score separation/AUROC and 0.99 hypothetical routing (anchor 36%, chain-of-thought below 1%) | `analysis/recompute_calibration.py`, `analysis/recompute_auroc.py`, figures | Implemented extracted score, not validated final-answer calibration or measured reviewer effectiveness |
| Per-category F1 and error destinations | `analysis/recompute_per_category.py`; Table A11 / appendix figures | Direct eight-configuration label calculations, distinct from semantic validity |
| MP examples: 5 Law/Crime + 3 Social Welfare; 7 Housing + 1 Public Lands | `analysis/compare_retained_agreement.py` | Exact question-level labels; possible implications for representation, not observed responses |
| Historical Immigration example | Historical vendor CSV, row 6265 marked `recorded_disagreement` | Specific recorded label, not an imputed case; excluded from principal eight-configuration calculations |
| Historical 17-configuration 682/291/90/137 and subset sensitivity | Frozen recovered summary; `analysis/recompute_inclusion_robustness.py` | Recomputed from recovery records where possible; no complete original raw-answer matrix claimed |
| 37 documents: 19 UK / 18 EU; 4,375 placements | `analysis/build_documentary.py`; source catalogue and worksheet exports | Placements can repeat a passage in different cells; not unique-passage or human agreement counts |
| 395 subthemes / 71 shared themes | Same producer; frozen thematic output and grouping | Verifies mapping and IDs; does not recreate the interpretive judgement |
| F1–F8, legal comparisons and implications | `documentary/final_findings.json`; frozen current table cells; source pointers | Authored/checked qualitative findings, not mechanically inferred or a test of implementation/compliance |
| Historical API call/cost table | Frozen Table A13 | Accounting record; this offline artifact makes no API calls and does not independently reconstruct all historical expenditure |

The distinct patterns of stability and disagreement can direct investigation of competing interpretations, model behaviour, human reference labels and coding rules. That is a reasoned implication, not a measured intervention on reviewer performance.
