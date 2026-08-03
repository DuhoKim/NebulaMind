# Lana A-P1 brief — exact r3 RED pin

P0 is GREEN. Read the coordination `HWAO_PARALLEL_PLAN.md` and Gate A custody receipt, then derive `design/LANA_R3_RED_PIN.md` only. Do not write tests or code.

Inputs of record:

- `../gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z/design/CONTRACT_R3_DRAFT.md` (§D1–D6 and standalone r3);
- repaired `validator_result_v2.json` and `structured_capture_v2.json`;
- sealed body/HTML/spec;
- repaired v2 validator/capture/tests.

Required pin:

1. Exact expected Gate-A RED test families for D5→D4→D2→D1→D3, with positive and negative fixtures and exact codes/statuses.
2. Exact predicted v3 deterministic/manual finding multiset on the sealed pre-r3 capture, with every new/retained/removed code count and source_refs.
3. Cell-by-cell list for all expected-new D1 missing typed-prefix findings, including any rows/roles that are exempt because the text is not a calibration-target description.
4. Exact D5 merged-paragraph detection expectation using the capture's available provenance; say whether capture v3 needs an additional parent/paragraph field.
5. Exact D4 per-row/per-index output: 12 orphan, 9 duplicate, 46 blank-short-name, near-duplicate 14↔29 manual; note any normalization deltas.
6. D2 sealed SIMBA result and positive `MODEL_PARAMETER` fixture.
7. D3 removal of the eight Result-cell failures, preserved row-citation manual-review behavior, and exact `EMPTY_CITATION_CELL` hard-fail behavior.
8. Exact integration acceptance rule, order-independent multiset representation, and how manual review entries are counted without claiming science.
9. Explicit diagnostic disclaimer: pre-r3 body, no retro-acceptance, C1r remains FAIL_CLOSED.
10. End marker `LANA_GATE_A_R3_RED_PIN_DONE_20260713T034742Z`.

If any count cannot be pinned from the local artifacts, STOP and name the missing fact rather than estimate. No network/live/browser/git/DB/dashboard action.
