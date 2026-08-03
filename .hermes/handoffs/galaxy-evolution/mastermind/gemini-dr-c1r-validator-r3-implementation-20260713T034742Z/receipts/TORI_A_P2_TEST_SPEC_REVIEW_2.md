# Tori A-P2 test-spec review 2 — custody/normalization correction required

The first corrections materially improved coverage. Three issues remain before Kun may certify RED:

1. **T-CUST currently hashes editable working outputs.** `validator/contract_spec_v3.json` is an A-P3 working file, not an immutable input; `fixtures/structured_capture_v3_input.json` was schema-renamed and therefore is not byte-identical to the pinned v2 source. Create exact immutable reference copies from the hash-pinned source artifacts (for example `fixtures/contract_spec_v2_reference.json` and `fixtures/structured_capture_v2_reference.json`) with no substitutions, and hash those. Also hash `fixtures/prompt_submitted.md` if it is the exact sealed prompt copy. T-CUST must be GREEN during RED and must not prevent legitimate A-P3 edits to v3 working files.
2. **D4 arXiv normalization assertion is too weak.** Merely asserting no `C7_NEAR_DUPLICATE` does not prove abs/html/pdf+version collapse. Assert that the three variants canonicalize to one URL and are detected as two duplicate rows in `C7_INTEGRITY_FAILURE` (or another exact frozen integrity representation), while producing no manual near-duplicate. Include `.pdf` suffix handling.
3. **D1 emergent positive is semantically under-shaped.** The fixture text is only `MATCHED_SELECTIONS`, so it is not a simulation–observation comparison under the frozen detector. Use comparison-bearing text such as `SIMBA matches observed data MATCHED_SELECTIONS`; then assert `C6:COMPARISON_LABEL_REVIEW` MANUAL and no `UNLABELED_COMPARISON` for that unit.

After correcting only tests/fixtures, rerun RED and rewrite the authoring receipt. Remove any temp output. Do not edit implementation or weaken any existing exact assertion.

TORI_GATE_A_P2_TEST_SPEC_REVIEW_2_REQUIRES_CORRECTION_20260713T034742Z
