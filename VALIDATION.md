# Local release validation

Validation date: 3 November 2026. Runtime: CPython 3.9.6 with the exact versions in `requirements.txt`. No model/API calls or external fits are performed.

## Verified results

- 16 frozen experimental CSV targets match regenerated values, with numeric tolerance 1e-10.
- 6,000 raw repeat answers reparse and match their saved labels; per-question prompts are identical across the five repeats.
- The 1,199-case four-way grouping is 717/215/76/191. Agreement selection retains 908 cases, with 717 matching CAP.
- The matched AI–AI/AI–CAP comparison uses 28 AI pairs and eight CAP comparisons on that same population.
- The 28 exact McNemar comparisons reproduce six unadjusted findings and none after Holm or Benjamini–Hochberg adjustment. The fixed-seed bootstrap reproduces 889/1,000 time-scope wins and 74 anchor wins.
- Documentary exports reproduce 37 units (19 UK/18 EU), 4,375 coding placements (2,057 UK/2,318 EU), 395 subthemes and 71 shared themes. Passage IDs and shortened-quote links are checked against frozen thematic inputs.
- The Table 2 counts, documentary placement totals, repeated-run table and all Table A11 F1 values/ranges are cross-checked. F1 ranges are calculated from unrounded counts, not differences between rounded cells.
- All six chart PDFs and all 22 numbered paper-asset PDFs reproduce their frozen searchable text and numbers. The frozen qualitative table text is not re-inferred by the build.
- Seven tests independently check input alignment, item partitioning, raw repeats, documentary scope/counts, the recorded historical vendor example, excluded working-file types and searchable assets.

## Anonymity and source checks

The preparation audit scans release text, filenames and extracted PDF text/metadata for the known author identifiers, local usernames/paths and credential patterns. It excludes ignored caches and Git internals. No matches were found. Public third-party names and institutional issuers in source material are retained with attribution.

The package has independent anonymous Git attribution and no configured remote. It does not include the working manuscript, private Git history, source workbooks' author properties/comments, personal research notes or agent/session logs. The release process did not modify the source inputs or manuscript. The released table cells and final documentary findings were checked against the current saved manuscript. `SHA256SUMS` records the released file state.

## Reproduction protocol

Run `make all` from a complete checkout at a different filesystem path. It rebuilds every supplied analysis, verifies the frozen targets, runs the tests and checks the file manifest. The setup instructions identify the tested dependency versions; a successful run does not establish applicability to untested model versions or actual deployment outcomes.

The complete policy source bank is intentionally not redistributed. Source hashes and public pointers support locating the analysed documents. Coding and thematic judgments are frozen inputs, not independently re-adjudicated by this verifier. Historical records and unavailable historical raw responses remain distinguished in `docs/PROVENANCE.md`.

## Clean-checkout acceptance

An independent local Git clone at a different filesystem path completed `make all`: all analyses and asset renderers ran, all 16 frozen CSV comparisons and paper-level checks passed, all seven tests passed, and all 237 file checksums matched after reproduction. Its tracked working tree remained clean. Original numerical inputs were checked unchanged by release preparation. All 16 table cell sets, eight final documentary findings and 22 current paper PDFs match the current saved manuscript and exports. The six regenerated chart PDFs were visually inspected.

The final validation-report addition and its checksum were checked against the validated tree; analysis code and inputs were unchanged. The artifact has independent history rooted in an anonymous commit. Hosting and mirror availability are verified separately from these local reproduction checks.
