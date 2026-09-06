# TRACK 3 FAIL-FIRST RECEIPT (codex V22 A–F) — 2026-09-06 21:57 KST

## Run 1: against BYTE-COPIES of the V22 modules (import lines renamed only), BEFORE any repair. A result that is an AttributeError is MISSING-INTERFACE evidence (the function did not exist); a False/True mismatch is BEHAVIOURAL evidence.
```
0ec04b3943b5dfba  ../track2/provenance_designs_v3.py (copy)
6d23c534636a9cdd  ../fourier_chirality/run_configurations_v7.py (copy)
b3bb92293b72d649  ../corpus_identity/build_corpus_identity_v23.py (copy)
df034ed5931b198e  ../beacon_v2/beacon_record_drand_v23.py (copy)
test_A_late_first_publication_of_a_rebuilt_history_is_refused (test_track3_fail_first.A_HistoryOpenAnchor) ... ERROR
test_A_open_commit_event_must_be_authentic_and_open_blob_genesis_only (test_track3_fail_first.A_HistoryOpenAnchor) ... ERROR
test_B_collector_cli_publishes_each_entry_when_asked (test_track3_fail_first.B_ProducerBoundary) ... usage: python3 -m unittest [-h] {collect,verify} ...
test_B_publish_entry_acknowledges_before_returning_and_refuses_batches (test_track3_fail_first.B_ProducerBoundary) ... ERROR
test_B_validator_requires_one_entry_per_acknowledged_commit (test_track3_fail_first.B_ProducerBoundary) ... ERROR
test_C_ancestry_delivered_push_is_authentic_in_composed_mode (test_track3_fail_first.C_OnePredicate) ... ERROR
test_D_control_failure_appends_a_named_entry (test_track3_fail_first.D_ControlFailureLogged) ... ERROR
test_E_render_end_must_be_the_last_relevant_record (test_track3_fail_first.E_RenderEndLast) ... FAIL
test_F_empty_feed_is_not_forged_and_every_failure_kind_is_exercised (test_track3_fail_first.F_FeedSemantics) ... FAIL
test_F_questions_text_states_30_days_and_option_B_not_implemented (test_track3_fail_first.F_FeedSemantics) ... FAIL
AttributeError: module 'provenance_designs_v3' has no attribute 'validate_continuation_v3'
    ok, why, info = P.validate_continuation_v3(work, log.name, str(bare), REF, open_event=ev_for(oc), runner=feed(live), repo=REPO); self.assertTrue(ok, why); self.assertEqual(info["entries_per_commit"], [1, 1, 1])
AttributeError: module 'provenance_designs_v3' has no attribute 'validate_continuation_v3'
    oc = P.publish_entry(work, log.name, str(bare), REF, "history-open"); self.assertEqual(git(bare, "rev-parse", REF), oc)
AttributeError: module 'provenance_designs_v3' has no attribute 'publish_entry'
AttributeError: module 'provenance_designs_v3' has no attribute 'validate_continuation_v3'
    self.assertEqual(P.authenticate_event(anc, [anc], REPO, REF, commit, root=work)[0], "AUTHENTIC")
TypeError: authenticate_event() got an unexpected keyword argument 'root'
    with self.assertRaises(rc.DataIntegrityFail) as cm: rc.reconcile_sentinels(rows, rj)
AssertionError: DataIntegrityFail not raised
    self.assertEqual(P.authenticate_event_live(e, REPO, feed([]), REF, "a" * 40)[0], "UNAVAILABLE")          # empty feed: no evidence either way → RETRY, never FORGED
AssertionError: 'FORGED' != 'UNAVAILABLE'
    q = Path(os.environ["QUESTIONS_TEXT"]).read_text(); self.assertNotIn("90 days", q); self.assertIn("30 days", q); self.assertIn("NOT IMPLEMENTED", q)
AssertionError: '90 days' unexpectedly found in '# TRACK 2 EVENT-RECEIPT PATH — the delegated witness workflow (recommended default) and the ONE step that is Duho\'s — 2026-09-06 21:18 KST\n\nWritten after Blanc\'s 21:14
Ran 10 tests in 2.820s
FAILED (failures=3, errors=7)
```

## Run 2: the SAME tests against the REPAIRED successors and the corrected questions text — 22:05 KST (one edit to the test file between runs: the D case lifts the exhibit-round exclusion inside the fixture, as every fixture on the real round does; nothing else)
```
fd0b3a47ca54347f  ../track2/provenance_designs_v3.py (repaired)
e5fcbb9fc9ef89af  ../fourier_chirality/run_configurations_v7.py (repaired)
49a13f4c46526c43  ../corpus_identity/build_corpus_identity_v23.py (repaired)
0257981d9a138bb5  ../beacon_v2/beacon_record_drand_v23.py (repaired)
test_A_late_first_publication_of_a_rebuilt_history_is_refused (test_track3_fail_first.A_HistoryOpenAnchor) ... ok
test_A_open_commit_event_must_be_authentic_and_open_blob_genesis_only (test_track3_fail_first.A_HistoryOpenAnchor) ... ok
test_B_collector_cli_publishes_each_entry_when_asked (test_track3_fail_first.B_ProducerBoundary) ... ok
test_B_publish_entry_acknowledges_before_returning_and_refuses_batches (test_track3_fail_first.B_ProducerBoundary) ... ok
test_B_validator_requires_one_entry_per_acknowledged_commit (test_track3_fail_first.B_ProducerBoundary) ... ok
test_C_ancestry_delivered_push_is_authentic_in_composed_mode (test_track3_fail_first.C_OnePredicate) ... ok
test_D_control_failure_appends_a_named_entry (test_track3_fail_first.D_ControlFailureLogged) ... ok
test_E_render_end_must_be_the_last_relevant_record (test_track3_fail_first.E_RenderEndLast) ... ok
test_F_empty_feed_is_not_forged_and_every_failure_kind_is_exercised (test_track3_fail_first.F_FeedSemantics) ... ok
test_F_questions_text_states_30_days_and_option_B_not_implemented (test_track3_fail_first.F_FeedSemantics) ... ok
Ran 10 tests in 7.046s
OK
```
