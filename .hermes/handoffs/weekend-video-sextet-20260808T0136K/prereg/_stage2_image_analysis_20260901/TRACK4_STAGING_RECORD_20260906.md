# TRACK 4 — STAGED REPAIRS OF CODEX'S V23 FINDINGS M1/M2/M3/M6 (NOT GATED, NOT ADOPTED) — 2026-09-06 23:50 KST

Under the standing preparation notes and Blanc's 22:58 order ("M1, M2, M3: repair in the next preparation round"). Successor files only (PIN_IMMUTABILITY_RULE): provenance_designs_v4, beacon_record_drand_v24, build_corpus_identity_v24, run_configurations_v8 (+ test_run_configurations_v8, test_build_corpus_identity_v24, test_beacon_record_drand_v24, track4/test_track4_fail_first.py, track1/coherent_attacks_v24.py). Fail-first: `TRACK4_FAIL_FIRST_RECEIPT_20260906.md` — run 1 against byte-copies of the V23 modules: 7 of 7 fail (4 MISSING-INTERFACE, 3 behavioural), run 1b executes codex's late-push case on the V23 validator (True — wrong), run 2 after repair: 7 OK with the test file byte-identical to run 1.

| codex V23 | repair (staged) | evidence |
|---|---|---|
| M1 per-entry commits ≠ per-entry acknowledgment | `validate_continuation_v4`: every history commit needs its OWN PushEvent in the live feed delivering exactly it (head = commit, before = parent), server-timed in the recorded order; HISTORY-PUBLICATION-BATCH / HISTORY-PUBLICATION-ORDER | tests M1 ×2; inspection rows 9c, 9l |
| M2 error entries unpublished; restart without reconciliation; retry re-commits | collector v24 publishes outer refusal/error entries; `reconcile_pending` before any collector/builder operation (PUBLISH-BATCH / PENDING-PUSH refuse); `publish_entry` pushes an existing pending commit | tests M2 ×3 (incl. the collector CLI crashing after genesis, then restarting) |
| M3 "cannot hide CLOSED" overclaimed | residual restated exactly in provenance_designs_v4, the design doc and the V24 text | test M3 (text) |
| M6 text remnants | design doc: window, "wired", "would do it themselves", network reads; V24 text: builder attribution + stage list, historical verifier cite, §9/§10 labels; driver comment | test M6 (text) |
| M4 (Blanc 22:58) | questions file: Option A′ partly built / not built for the history-open event; C the only working option; Q1 un-presented | done before this round |
| M5 (Blanc 22:58) | PIN_DRIFT_RECORD_V22_M5 + PIN_IMMUTABILITY_RULE; V22 bytes archived | done before this round |

Suites on the V24 candidate (warning-strict): 13 suites, 107 tests OK (see the V24 text §3c). V24 staged text `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V24_20260906.md` digest `f3987cbe0d31b7c5eb5a72c7018c624175d60cd8b4c3e374335cb6f19c3d2992`; diff `V23_TO_V24.diff`. Not dispatched for review — Blanc decides. Nothing adopted; no beacon read, draw, fetch, render, pixel.
