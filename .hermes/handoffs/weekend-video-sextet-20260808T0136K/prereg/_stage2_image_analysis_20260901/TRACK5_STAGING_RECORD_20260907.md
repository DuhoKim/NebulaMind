# TRACK 5 — STAGED ANSWERS TO CODEX'S V24 FINDINGS N1–N5 (NOT GATED, NOT ADOPTED) — 2026-09-07 00:27 KST

Standing preparation after the V24 review split. Successor files only (PIN_IMMUTABILITY_RULE): provenance_designs_v5, beacon_record_drand_v25, build_corpus_identity_v25, run_configurations_v9 (+ tests v9/v25/v25, track5/test_track5_fail_first.py, track1/coherent_attacks_v25.py). Fail-first: `TRACK5_FAIL_FIRST_RECEIPT_20260907.md` — run 1 against byte-copies of the V24 modules: 6 of 6 fail, classified per test (3 missing-interface: N2a/b/c; 3 behavioural: N3, N1, N5); run 1b executes the V24 functions on the same fixtures (empty second feed → BATCH, missing middle event → BATCH, unrelated commit → PUBLISHED — the old behaviour); run 2 after repair: 6 OK, exit 0, test file identical.

| codex V24 | answer (staged) | evidence |
|---|---|---|
| N1 chronology of unpublished work/decisions (structural) | NOT a repair: THE COVENANT in codex's clause shape replaces the residual in provenance_designs_v5, the design doc and the V25 text §3c | test N1 (text) |
| N2 live contract + dispositions | `validate_continuation_v5`: EVIDENCE-UNAVAILABLE (empty/unavailable per-entry retrieval) and EVIDENCE-INCOMPLETE (no own event, no proof of batching) = RETRY; HISTORY-PUBLICATION-BATCH only when the feed proves a multi-commit delivery; driver v9 prefixes RETRY-; the questions file states the FULL contract (approval + open + every history commit) and the dispositions; Option A′ marked not built for the per-commit events either | tests N2a/b/c; rows 9m/9n |
| N3 producer precondition; §7 names | `publish_entry` refuses PUBLISH-UNRELATED-COMMITS; §7 names the v25 collector/builder | test N3; row 9o |
| N4 receipt classification | `TRACK_RECEIPTS_CLASSIFICATION_CORRECTION_20260907.md` beside the pinned receipts (tracks 3/4 corrected; tracks 1/2 confirmed) | test N5 asserts the note exists |
| N5 labels / sweep / sandbox omission | §3c self-label V25, §9 names the v25 script, driver comments swept, stronger text assertions; the next sandbox includes the historical `_tmp_*_COPIED_DIGESTS.txt` lists | test N5 |

Suites on the V25 candidate (warning-strict, variables passed separately): 14 suites, 113 tests OK. V25 staged text `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V25_20260907.md` digest `d29aabac28d6d7de32e8b33b5ec4082c5c758a0ebf9913455f7b8b9cd642e1a3`; diff `V24_TO_V25.diff`. Nothing adopted; no beacon read, draw, fetch, render, pixel.
