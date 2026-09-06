# TRACK 4 FAIL-FIRST RECEIPT (codex V23 M1/M2/M3/M6) — 2026-09-06 23:38 KST

## Run 1: against BYTE-COPIES of the V23 modules (import lines renamed only), BEFORE any repair. AttributeError/TypeError = MISSING-INTERFACE; an assertion mismatch = BEHAVIOURAL.
```
fd0b3a47ca54347f  ../track2/provenance_designs_v4.py (copy)
e45cc4ea3be04994  ../beacon_v2/beacon_record_drand_v24.py (copy)
0308c180746aa4ee  ../corpus_identity/build_corpus_identity_v24.py (copy)
bdfefe6680044d4e  ../fourier_chirality/run_configurations_v8.py (copy)
test_M1_one_push_per_commit_validates_and_ordering_is_checked (test_track4_fail_first.M1_PerEntryAcknowledgment) ... ERROR
test_M1_single_entry_commits_pushed_together_are_refused (test_track4_fail_first.M1_PerEntryAcknowledgment) ... ERROR
test_M2_collector_cli_publishes_outer_error_and_reconciles_on_restart (test_track4_fail_first.M2_ProducerRecovery) ... FAIL
test_M2_publish_entry_retries_an_existing_pending_commit (test_track4_fail_first.M2_ProducerRecovery) ... ERROR
test_M2_reconcile_before_operating_and_error_entries_published (test_track4_fail_first.M2_ProducerRecovery) ... ERROR
test_M3_residual_stated_exactly (test_track4_fail_first.M3_M6_Text) ... FAIL
test_M6_text_sweep (test_track4_fail_first.M3_M6_Text) ... FAIL
    ok, why, info = P.validate_continuation_v4(work, log.name, str(bare), REF, evs[0], feed(evs), REPO); self.assertTrue(ok, why); self.assertEqual(info["publications"], 3)
AttributeError: module 'provenance_designs_v4' has no attribute 'validate_continuation_v4'
AttributeError: module 'provenance_designs_v4' has no attribute 'validate_continuation_v4'
    c = P.publish_entry(work, log.name, str(bare), REF, "retry"); self.assertEqual(c, pending, "the existing pending commit is pushed, not re-committed"); self.assertEqual(git(bare, "rev-parse", REF),
    st = P.reconcile_pending(work, log.name, str(bare), REF); self.assertEqual(st["published"], 1); self.assertEqual(git(bare, "rev-parse", REF), git(work, "rev-parse", "HEAD"))
AttributeError: module 'provenance_designs_v4' has no attribute 'reconcile_pending'
    self.assertIn("collector-error", remote_blob.decode(), "the outer error entry must be PUBLISHED, not left local")
AssertionError: 'collector-error' not found in '{"approval_record_sha256":"7b0d411eda44c3ada044ab4c5de6856979eb9ba99774b4a483761b4c784b76b5","prev_sha256":"00000000000000000000000000000000000000000000
    t = p.read_text(encoding="utf-8"); self.assertNotIn("cannot hide a CLOSED witness state", t, p.name); self.assertIn("absence-based", t, p.name)
    for bad in ("about 90 days", "NOT wired", "would do it themselves", "one network read per driver run"): self.assertNotIn(bad, t2, bad)
AssertionError: 'about 90 days' unexpectedly found in '# TRACK 2 — RECOMMENDED, UNADOPTED DESIGNS for the two provenance boundaries (Blanc\'s order 20:45 KST; codex\'s note 20:43) — REVISED 21:07 KST 
Ran 7 tests in 2.012s
FAILED (failures=3, errors=4)
```

## Run 1b: codex's M1 case against the V23 validator (validate_continuation_v3), executed — the OLD behaviour
```
v3 on four single-entry commits delivered by ONE late push: True | entries_per_commit [1, 1, 1, 1] — WRONG (codex V23 M1)
```

## Run 2: the SAME tests against the REPAIRED successors, the V24 staged text and the revised design document — 23:46 KST (no edit to the test file between runs)
```
ddcfa7227c3510a2  ../track2/provenance_designs_v4.py (repaired)
5bffe90ca404bec1  ../beacon_v2/beacon_record_drand_v24.py (repaired)
1e8498532bcd9e87  ../corpus_identity/build_corpus_identity_v24.py (repaired)
4d1fb393716e25ed  ../fourier_chirality/run_configurations_v8.py (repaired)
test file f101e956ab92ae28  (identical to run 1)
test_M1_one_push_per_commit_validates_and_ordering_is_checked (test_track4_fail_first.M1_PerEntryAcknowledgment) ... ok
test_M1_single_entry_commits_pushed_together_are_refused (test_track4_fail_first.M1_PerEntryAcknowledgment) ... ok
test_M2_collector_cli_publishes_outer_error_and_reconciles_on_restart (test_track4_fail_first.M2_ProducerRecovery) ... ok
test_M2_publish_entry_retries_an_existing_pending_commit (test_track4_fail_first.M2_ProducerRecovery) ... ok
test_M2_reconcile_before_operating_and_error_entries_published (test_track4_fail_first.M2_ProducerRecovery) ... ok
test_M3_residual_stated_exactly (test_track4_fail_first.M3_M6_Text) ... ok
test_M6_text_sweep (test_track4_fail_first.M3_M6_Text) ... ok
Ran 7 tests in 4.942s
OK
```
