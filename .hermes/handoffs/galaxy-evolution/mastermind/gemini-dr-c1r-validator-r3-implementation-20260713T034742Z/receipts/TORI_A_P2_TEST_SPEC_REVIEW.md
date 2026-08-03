# Tori A-P2 test-spec review — correction required before Kun RED receipt

Status: RED is genuine, but the test packet does not yet satisfy all frozen assertions. Do not open A-P3.

Required corrections, tests/fixtures only:

1. **T-CUST is not implemented.** `RED_TEST_INDEX.md` claims immutable-input hashes, but the integration test contains no SHA-256 assertions. Add exact hash checks for the sealed body/HTML/spec and the v2 capture/result inputs pinned in `KUN_INPUT_CUSTODY_RECEIPT.md`.
2. **Manual multiset is not exact.** The integration test asserts only `len==82` plus a code subset. Compare the full order-independent `Counter[(clause,code,status,tuple(source_refs))]` against the 73 immutable v2 manual identities + eight D3 row reviews at `[table_row_14..21,2]` + one C7 near-duplicate. Do not accept extra/missing identities that happen to total 82.
3. **D1 sealed refs are not exact.** Assert the nine exact `MISSING_CALIBRATION_TARGET_PREFIX` refs: `[table_row_4..11,1]` plus `[table_row_11,2]`. Add positive checks for no-observation-reference and `NONE_FOUND`/`NONE_FOUND.` exemption, and retained emergent-token MANUAL behavior.
4. **D5 capture schema is not directly asserted.** On the real merged HTML, assert all four captured gap lines have required non-empty `parent_path`, all share the same value, and the validator emits exactly one finding. Keep the synthetic four-parent positive. A separate Node test is optional; the integration test may carry these capture assertions.
5. **D2 positive matrix is incomplete.** Add: a non-numeric word `fraction`/`incidence` yields neither qualifier finding; an observational numeric fraction with a complete real four-field tuple yields MANUAL and no FAIL.
6. **D3 exact refs/guard.** Assert the eight new row reviews are exactly `[table_row_14..21,2]`; keep `EMPTY_CITATION_CELL` hard-fail and add missing-citation-cell shape if distinct from empty.
7. **D4 normalization fixture.** Exercise arXiv `abs|html|pdf` plus version normalization and assert it does not produce `C7_NEAR_DUPLICATE`; retain the article/article-abstract manual fixture. Integration already asserts sealed 12/9/46/0 counts.
8. Delete `tests/pytest_output.txt` if present; the receipt itself is the durable test output.

After corrections, rerun the new tests once. They must remain genuinely RED for missing r3 behavior. Rewrite `GORU_RED_AUTHORING_RECEIPT.md` with the exact current failing test list and the same final marker. No validator/capture/baseline edits.

TORI_GATE_A_P2_TEST_SPEC_REVIEW_REQUIRES_CORRECTION_20260713T034742Z
