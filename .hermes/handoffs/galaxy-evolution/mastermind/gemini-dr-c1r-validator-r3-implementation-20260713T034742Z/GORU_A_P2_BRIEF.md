# Goru A-P2 brief — author frozen RED tests only

A-P1 is countersigned. Read:

- coordination `HWAO_PARALLEL_PLAN.md` and `ROLE_TABLE.md`;
- Gate A `design/LANA_R3_RED_PIN.md` and `design/HWAO_R3_RED_PIN_COUNTERSIGN.md`;
- Gate A custody receipt and approval boundaries;
- packet-local `validator/validator_v3.py`, `capture/structured_capture_v3.js`, baseline tests, and fixtures.

Tori has already copied v2 behavior into packet-local v3 working files and confirmed the baseline suites are GREEN: 8 Python tests and 1 Node suite. The only pre-RED code delta is the mechanical schema rename `NM_GEMINI_RENDERED_DOM_V2`→`V3`; no r3 behavior is implemented.

Write only Gate A `tests/` and `fixtures/`:

- new r3 RED tests covering D5 → D4 → D2 → D1 → D3 in that order;
- positive and negative fixtures for every D item;
- full sealed-capture T-INT multiset assertion for exactly 19 deterministic FAIL and 82 MANUAL, exact identities/refs, removed eight C4 failures absent, unchanged pass classes, overall FAIL;
- determinism assertion and immutable-input custody assertion;
- `tests/RED_TEST_INDEX.md` mapping each assertion to the frozen pin.

Binding expectations:

1. D5: `gap_line.parent_path` required; merged four-GAP paragraph produces exactly one `C2:GAP_MULTIPLE_PER_PARAGRAPH`; four paragraphs produce none.
2. D4: exact 12 orphan, 9 duplicate rows, 46 blanks, 0 inline-only inside `C7_INTEGRITY_FAILURE`; exact +1 MANUAL `C7_NEAR_DUPLICATE` for 14↔29; arXiv abs/html/pdf variants auto-merge.
3. D2: sealed SIMBA `~10%` remains `MISSING_QUALIFIER`; `MODEL_PARAMETER`/`NOT_APPLICABLE` full tuple becomes manual semantic review, not fail; non-numeric fraction words do not trigger.
4. D1: frozen negation-blind detector and exact 9 missing-prefix refs; prefix/no-observation/sentinel positives; emergent comparison behavior retained.
5. D3: eight S2 result failures become eight manual row reviews anchored to full `table_row_14..21,2`; empty/missing Citation cell is hard `C4:EMPTY_CITATION_CELL`; no broader relaxation.
6. Use full actual IDs (`table_row_N`), not the `trN` shorthand in prose tables.
7. Tests may be order-independent but must not weaken exact multisets.

Run the new test commands once to confirm genuine RED. Do not edit `validator/`, `capture/`, runner code, contract spec, or baseline tests. Do not make tests pass. Record exact failing tests in `tests/GORU_RED_AUTHORING_RECEIPT.md`, ending with `GORU_GATE_A_RED_TESTS_WRITTEN_20260713T034742Z`.

No network/live/browser/DB/dashboard/deploy/cron/git action. Delete any temporary helper before completion.
