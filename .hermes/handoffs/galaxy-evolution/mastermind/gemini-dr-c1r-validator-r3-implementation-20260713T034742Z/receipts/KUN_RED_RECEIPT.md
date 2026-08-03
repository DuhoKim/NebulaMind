# Kun Gate A RED Receipt

Packet: `gemini-dr-c1r-validator-r3-implementation-20260713T034742Z`
Phase: A-P2 independent RED runner.
Decision: GREEN-to-open-A-P3.

Scope honored: no edits to tests, fixtures, validator, capture, spec, or runners. No network, live, browser, DB, dashboard, deploy, cron, or git action. Runtime temp was confined to `receipts/_kun_red_tmp` and removed before finish.

## Inputs Read

- `design/LANA_R3_RED_PIN.md`
- `design/HWAO_R3_RED_PIN_COUNTERSIGN.md`
- `receipts/KUN_INPUT_CUSTODY_RECEIPT.md`
- `receipts/TORI_A_P2_TEST_SPEC_REVIEW.md`
- `receipts/TORI_A_P2_TEST_SPEC_REVIEW_2.md`
- current `tests/`, `fixtures/`, `capture/`, `validator/`

## Commands And Results

Baseline Python:

```text
env TMPDIR=receipts/_kun_red_tmp PYTHONDONTWRITEBYTECODE=1 PYTEST_ADDOPTS='--cache-clear -p no:cacheprovider --assert=plain --basetemp=receipts/_kun_red_tmp/pytest' /Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python -B -m pytest -q tests/test_validator_v3_baseline.py tests/test_integration_v3_baseline.py
```

Result: exit `0`; `8 passed in 0.24s`.

Baseline Node capture:

```text
env TMPDIR=receipts/_kun_red_tmp node tests/test_capture_v3_baseline.mjs
```

Result: exit `0`; `T1-T6 capture RED/GREEN contract passed`.

R3 RED Python:

```text
env TMPDIR=receipts/_kun_red_tmp PYTHONDONTWRITEBYTECODE=1 PYTEST_ADDOPTS='--cache-clear -p no:cacheprovider --assert=plain --basetemp=receipts/_kun_red_tmp/pytest_red' /Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python -B -m pytest -q tests/test_validator_v3_r3_red.py tests/test_integration_v3_r3_red.py
```

Result: exit `1`; collected `6`; `5 failed, 1 passed in 0.26s`.

Actual current v3 integration multiset extraction:

```text
env TMPDIR=receipts/_kun_red_tmp PYTHONDONTWRITEBYTECODE=1 /Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python -B - <integration summary script>
```

Result: exit `0`; current output is still v2-shaped: `17` FAIL, `73` MANUAL, `4` PASS.

Cleanup:

```text
rm -rf receipts/_kun_red_tmp
```

Result: exit `0`.

## RED Failure List

Expected RED failures, all due to missing r3 behavior in packet-local v3 working code:

1. `tests/test_validator_v3_r3_red.py::test_d5_gap_multiple_per_paragraph`
   - expected `C2:GAP_MULTIPLE_PER_PARAGRAPH` exactly once for four GAP lines sharing one `parent_path`
   - actual: no such finding
2. `tests/test_validator_v3_r3_red.py::test_d4_ledger_integrity`
   - expected arXiv `abs|html|pdf` plus version normalization to collapse three variants, yielding two duplicate rows in `C7_INTEGRITY_FAILURE`, with no `C7_NEAR_DUPLICATE`
   - actual: duplicate row count was `1`, not `2`
3. `tests/test_validator_v3_r3_red.py::test_d1_missing_calibration_target_prefix`
   - expected `C6:MISSING_CALIBRATION_TARGET_PREFIX` for unprefixed calibration-target description
   - actual: no such finding
4. `tests/test_validator_v3_r3_red.py::test_d3_cited_cell_claim_review`
   - expected `C4:EMPTY_CITATION_CELL` hard failure for empty or missing dedicated S2 Citation cell
   - actual: no such finding
5. `tests/test_integration_v3_r3_red.py::test_t14_exact_mechanical_residue_r3_and_t15_determinism`
   - expected frozen r3 T-INT multiset: exact `19` deterministic FAIL, exact `82` MANUAL, removed `C4:UNCITED_CELL_CLAIM`, D5 parent-path schema, D1 exact refs, D3 exact row reviews, deterministic double-run
   - actual current integration remains v2-shaped: `C4:UNCITED_CELL_CLAIM` ×8 still present, `C2:GAP_MULTIPLE_PER_PARAGRAPH` absent, `C6:MISSING_CALIBRATION_TARGET_PREFIX` absent, total `17` FAIL / `73` MANUAL

Expected pass in RED:

- `tests/test_validator_v3_r3_red.py::test_d2_missing_qualifier`
  - passed because v2 already retained the D2 numeric-fraction behavior and the added positive/negative D2 fixture family is satisfied.

## Custody / T-CUST

T-CUST reference hashes are GREEN during RED and are not the cause of failure:

- `fixtures/prompt_submitted.md`: `fffac44fbf6e9abe3afb1f8f34f3a9e3e7688991f319c4927459fb29ac00e1ef`
- `fixtures/body.md`: `8a130c5a6fc1b1f5d534888d3fb20806230b8b4c7737cb00f9bfb18ad0d6bc00`
- `fixtures/rendered_body.html`: `78ed129c47daf9300d9ed319aa1ffe95bbb0d1810a223733afaf48c4372f2bbc`
- `fixtures/contract_spec_v2_reference.json`: `1b10b4538162e1f786e3e36b639448cbe0d4252282d236c88495272398062338`
- `fixtures/structured_capture_v2_reference.json`: `e26819dbc90a040ecc228639fbee3e2a68f8942fa9d26b9458aee71bbc65e3e9`
- `fixtures/validator_result_v2_reference.json`: `ad4d035b291f6d64ad47f510811cc05826d822f449cf3d181974be2ce2473d52`

Current working code hashes recorded for A-P3 comparison:

- `capture/structured_capture_v3.js`: `ef7c5b4b235c8cfd0b605b4315cefbfa362323af0f3f6b4b395cfe0eae5581dd`
- `capture/run_capture_v3.mjs`: `de90da08a3572efe262029103bfe1861ef733fdf54f8859dadcb35f6d5a6216f`
- `validator/validator_v3.py`: `ba4889ca35938f65a834b05ec838837c99174870904250c7ff35d17c5768a5d5`
- `validator/run_validator_v3.py`: `aee75f95510a607edb681d426323def1187913be89999bafeb59f2af62100b1b`
- `validator/contract_spec_v3.json`: `1b10b4538162e1f786e3e36b639448cbe0d4252282d236c88495272398062338`

No implementation files were edited by this Kun run. Goru A-P2 authoring artifacts are tests/fixtures/spec-review receipts; current code remains pre-A-P3 working code.

## Test Shape Audit

Shape checks verified by direct inspection / `rg`:

- T-INT asserts exact deterministic FAIL count `19`.
- T-INT asserts exact manual multiset sum `82`.
- T-INT asserts `C4:UNCITED_CELL_CLAIM` absent.
- T-INT asserts exact D1 refs: `[table_row_4..11,1]` plus `[table_row_11,2]`.
- T-INT asserts all four captured `gap_line` blocks have required non-empty shared `parent_path`.
- D5 unit fixture asserts one shared parent produces exactly one `GAP_MULTIPLE_PER_PARAGRAPH`; four distinct parents produce none.
- D4 fixture asserts arXiv `abs|html|pdf` plus version normalization produces duplicate-row evidence and no manual near-duplicate; article/article-abstract produces `C7_NEAR_DUPLICATE`.
- D3 fixture asserts empty and missing S2 Citation cells hard-fail with `EMPTY_CITATION_CELL`, and populated Citation cell removes `UNCITED_CELL_CLAIM` while adding exact row review.
- D2 fixture includes negative SIMBA `~10%`, `MODEL_PARAMETER` positive, non-numeric fraction/incidence no-finding, and observational numeric fraction with complete real tuple.
- Deterministic double-run is asserted by byte equality of two capture outputs and stable validator JSON serialization.

## Test File Hashes

- `tests/test_validator_v3_r3_red.py`: `a639b45b6a7fbc0349865252968e11e98dadd1ace2988bd7d465c413a5a227f1`
- `tests/test_integration_v3_r3_red.py`: `9eec1cf3a434fffe043434816a5d5950895aca91853da717672b15ab844caaa8`
- `tests/test_validator_v3_baseline.py`: `facdb31211c13b8d9799be4e68c4851f1b9bd72e44de477694a0fa05269cef75`
- `tests/test_integration_v3_baseline.py`: `fe6bd084e1b625dfe57d42579316b36db3fe67f79d395810550088238e30ba9c`
- `tests/test_capture_v3_baseline.mjs`: `864b7f98f96c3b9fe87639c6928dff7cac08004120b7d9481804eac2216292e9`
- `tests/RED_TEST_INDEX.md`: `a7ba90cbfd64e24425ed596eaa3be6ea97f61f18861692e8bfe46731c7e2584c`
- `tests/GORU_RED_AUTHORING_RECEIPT.md`: `cb2e29dbfb30649eb10613acadc679e690d1db54273f89f689795d5073b61f50`

## Decision

A-P2 RED runner decision: GREEN-to-open-A-P3.

Reason: baseline v3 compatibility is GREEN, T-CUST is GREEN, RED failures are exactly in the missing r3 behavior families, D2 already passes as expected, and the corrected test shapes cover the frozen A-P1 pin and Tori spec reviews.

KUN_GATE_A_RED_RECEIPT_DONE_20260713T034742Z
