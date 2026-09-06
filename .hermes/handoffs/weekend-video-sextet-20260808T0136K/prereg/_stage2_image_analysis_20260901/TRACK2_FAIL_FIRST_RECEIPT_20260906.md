# TRACK 2 FAIL-FIRST RECEIPT — 2026-09-06 21:05 KST

## Run 1: the tests against a BYTE-COPY of provenance_designs.py (the module codex probed, 6ff0f7dc…) renamed provenance_designs_v2.py, BEFORE any repair
```
6ff0f7dcb4c7a417  provenance_designs_v2.py (copy of 6ff0f7dc…)
test_error_handling_each_failure_takes_its_path (test_track2_fail_first.Events) ... ERROR
test_expired_event_and_independent_receipt_path (test_track2_fail_first.Events) ... ERROR
test_retrieval_and_pagination_execute (test_track2_fail_first.Events) ... ERROR
test_codex_counterexample_1_unpushed_append (test_track2_fail_first.History) ... ERROR
test_codex_counterexample_2_local_reset_and_replacement (test_track2_fail_first.History) ... ERROR
test_deleted_suffix_and_rebuild_with_remote_consulted (test_track2_fail_first.History) ... ERROR
test_honest_continuation_pushed_each_entry (test_track2_fail_first.History) ... ERROR
test_stale_expected_head_unavailable_remote_and_unpublished_open_commit (test_track2_fail_first.History) ... ERROR
AttributeError: module 'provenance_designs_v2' has no attribute 'EventsUnavailable'
AttributeError: module 'provenance_designs_v2' has no attribute 'authenticate_event_live'
AttributeError: module 'provenance_designs_v2' has no attribute 'retrieve_events'
AttributeError: module 'provenance_designs_v2' has no attribute 'validate_continuation_v2'
AttributeError: module 'provenance_designs_v2' has no attribute 'validate_continuation_v2'
AttributeError: module 'provenance_designs_v2' has no attribute 'validate_continuation_v2'
AttributeError: module 'provenance_designs_v2' has no attribute 'validate_continuation_v2'
AttributeError: module 'provenance_designs_v2' has no attribute 'validate_continuation_v2'
Ran 8 tests in 1.625s
FAILED (errors=8)
```

## Run 1b: codex's two counterexamples reproduced against the OLD validate_continuation (the probed module), executed
```
baseline: True
counterexample 1 (unpushed ACCEPT appended, remote unchanged): old validator says True — WRONG
counterexample 2 (client reset to history-open, RETRY replaced by ACCEPT, remote unchanged): old validator says True — WRONG
remote head unchanged throughout: True
```

## Run 2: the SAME tests against the REPAIRED provenance_designs_v2 — 21:07 KST
```
74b33dfcd7f5abaa  provenance_designs_v2.py (repaired)
test_error_handling_each_failure_takes_its_path (test_track2_fail_first.Events) ... ok
test_expired_event_and_independent_receipt_path (test_track2_fail_first.Events) ... ok
test_retrieval_and_pagination_execute (test_track2_fail_first.Events) ... ok
test_codex_counterexample_1_unpushed_append (test_track2_fail_first.History) ... ok
test_codex_counterexample_2_local_reset_and_replacement (test_track2_fail_first.History) ... ok
test_deleted_suffix_and_rebuild_with_remote_consulted (test_track2_fail_first.History) ... ok
test_honest_continuation_pushed_each_entry (test_track2_fail_first.History) ... ok
test_stale_expected_head_unavailable_remote_and_unpublished_open_commit (test_track2_fail_first.History) ... ok
Ran 8 tests in 3.023s
OK
```
