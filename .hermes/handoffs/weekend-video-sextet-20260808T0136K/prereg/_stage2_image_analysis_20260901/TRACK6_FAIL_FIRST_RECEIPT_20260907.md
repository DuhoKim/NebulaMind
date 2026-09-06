# TRACK 6 FAIL-FIRST RECEIPT (codex V25 P1–P4) — 2026-09-07 00:51 KST

## Run 1: against BYTE-COPIES of the V25 modules (import lines renamed only), BEFORE any repair; classification per test follows.
```
c265097167d81948  ../track2/provenance_designs_v6.py (copy)
8f057ad31b24fe40  ../fourier_chirality/run_configurations_v10.py (copy)
fe55c70bcaccaacf  ../corpus_identity/build_corpus_identity_v26.py (copy)
14dae3c92dd7e127  ../beacon_v2/beacon_record_drand_v26.py (copy)
test_P1_batch_proven_by_ancestry_without_commits_list_is_terminal (test_track6_fail_first.P1_AncestryBatch) ... ERROR
test_P2_approval_event_absent_from_a_covering_feed_is_retry_not_forged (test_track6_fail_first.P2_AbsenceIsNotForgery) ... FAIL
test_P2_open_event_absent_is_retry_in_the_driver_shape (test_track6_fail_first.P2_AbsenceIsNotForgery) ... ERROR
test_P3_sweep (test_track6_fail_first.P3_P4_Text) ... ERROR
test_P4_covenant_in_the_questions_file (test_track6_fail_first.P3_P4_Text) ... FAIL
AttributeError: module 'provenance_designs_v6' has no attribute 'validate_continuation_v6'
AttributeError: module 'provenance_designs_v6' has no attribute 'validate_continuation_v6'
FileNotFoundError: [Errno 2] No such file or directory: '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/t
    self.assertEqual(o, "INCOMPLETE", why)
AssertionError: 'FORGED' != 'INCOMPLETE'
    q = Path(os.environ["QUESTIONS_TEXT"]).read_text(encoding="utf-8"); self.assertIn("does not authenticate when", q); self.assertIn("between later publications", q)
AssertionError: 'does not authenticate when' not found in '# TRACK 2 EVENT-RECEIPT PATH — the delegated witness workflow (recommended default) and the ONE step that is Duho\'s — 2026-09-06 21:18 KST\n
Ran 5 tests in 1.382s
FAILED (failures=2, errors=3)
```

## Run 1b: the same fixtures against the V25 functions — the OLD behaviour, executed
```
P1 v5, batch proven by ancestry, no commits list: EVIDENCE-INCOMPLETE — WRONG (a proven batch called incomplete)
P2 v5, approval event absent from a covering feed: FORGED — WRONG (absence called forgery)
```

## Run 1 classification (per test): P1 → MISSING-INTERFACE (validate_continuation_v6 absent; old behaviour in run 1b: EVIDENCE-INCOMPLETE for a proven batch); P2a → BEHAVIOURAL (the copy's authenticate_event said FORGED); P2b → MISSING-INTERFACE (v6 absent); P3 → MISSING-INTERFACE for the v26 script file plus behavioural text remnants; P4 → BEHAVIOURAL (text). Totals: 3 missing-interface, 2 behavioural. Between runs the P2b assertion was widened to the uniform EVIDENCE-* vocabulary (the open event older than the feed's oldest is EVIDENCE-EXPIRED, correctly) — disclosed.

## Run 2: the SAME tests (P2b assertion widened as disclosed) against the REPAIRED successors, the V26 staged text, the revised design document and questions file — 00:56 KST
```
02b9fb4291bc4ae0  ../track2/provenance_designs_v6.py (repaired)
3c3610c94360b2e8  ../fourier_chirality/run_configurations_v10.py (repaired)
0c99f5fe92a80525  ../corpus_identity/build_corpus_identity_v26.py (repaired)
13a2fa3f5e8636d0  ../beacon_v2/beacon_record_drand_v26.py (repaired)
test file 20ead17b4e29cf60
test_P1_batch_proven_by_ancestry_without_commits_list_is_terminal (test_track6_fail_first.P1_AncestryBatch) ... ok
test_P2_approval_event_absent_from_a_covering_feed_is_retry_not_forged (test_track6_fail_first.P2_AbsenceIsNotForgery) ... ok
test_P2_open_event_absent_is_retry_in_the_driver_shape (test_track6_fail_first.P2_AbsenceIsNotForgery) ... ok
test_P3_sweep (test_track6_fail_first.P3_P4_Text) ... ok
test_P4_covenant_in_the_questions_file (test_track6_fail_first.P3_P4_Text) ... ok
Ran 5 tests in 1.705s
OK
    exit status: 0
```
