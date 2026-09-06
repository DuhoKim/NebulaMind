# TRACK 1 FAIL-FIRST RECEIPT — 2026-09-06 20:46 KST

## Run 1: the tests against BYTE-COPIES of the V21 modules (beacon_record_drand_v22 = v21, build_corpus_identity_v22 = v21, history_v2 = history, run_configurations_v6 = v5), BEFORE any repair
```
b1c627e2e3b5a5dd  ../beacon_v2/beacon_record_drand_v22.py (copy: only the import lines renamed)
49ca7d98b99c965b  ../corpus_identity/build_corpus_identity_v22.py (copy: only the import lines renamed)
8ac7a81cc9ee5c25  ../corpus_identity/history_v2.py (copy: only the import lines renamed)
0f3d03ee5408791b  ../fourier_chirality/run_configurations_v6.py (copy: only the import lines renamed)
test_C2_driver_reproduces_W4_first_approval_is_final (test_track1_fail_first.T) ... FAIL
test_C3_closed_is_terminal_in_history_and_driver (test_track1_fail_first.T) ... FAIL
test_C3_genesis_takes_the_lock_before_testing_existence (test_track1_fail_first.T) ... FAIL
test_C4a_builder_missing_args_is_logged (test_track1_fail_first.T) ... FAIL
test_C4b_builder_output_failure_after_validation_is_logged (test_track1_fail_first.T) ... ERROR
test_C4c_collector_argparse_failure_is_disclosed (test_track1_fail_first.T) ... FAIL
test_C5_round_6441904_excluded_by_name (test_track1_fail_first.T) ... FAIL
test_C6_uppercase_hex_signature_is_the_same_value (test_track1_fail_first.T) ... FAIL
test_C7_C8_C10_rule_text_consistent (test_track1_fail_first.T) ... FAIL
test_C9_sentinel_journal_must_be_complete (test_track1_fail_first.T) ... FAIL
FileExistsError: [Errno 17] File exists: '/var/folders/64/71dstw0j1gd_n58lsxnhl3p80000gn/T/tmprj2edw9f/outfile'
AssertionError: DataIntegrityFail not raised
AssertionError: DataIntegrityFail not raised
AssertionError: SystemExit not raised
AssertionError: False is not true : the refusal must be disclosed beside the history
AssertionError: False is not true : argparse failure must reach the sidecar named by --log
AssertionError: 6441904 not found in (6440756, 6441924)
AssertionError: 'REFUSE-CONFLICTING-VALID-SIGNATURES' != 'ACCEPT-DRAND'
AssertionError: DataIntegrityFail not raised
Ran 10 tests in 10.906s
FAILED (failures=9, errors=1)
```

## Run 2: the SAME tests against the REPAIRED successors and the V22 staged text — 20:59 KST
```
df034ed5931b198e  ../beacon_v2/beacon_record_drand_v22.py (repaired)
6c830c1ba62316ee  ../corpus_identity/build_corpus_identity_v22.py (repaired)
ce3d8c1cee3f9734  ../corpus_identity/history_v2.py (repaired)
9cc941a6b0919dfb  ../fourier_chirality/run_configurations_v6.py (repaired)
test file f2772a6cbe3081df  (one edit between runs: the C2 case's second record name V21_T_second → V22_T_second, to match the successor glob; nothing else)
test_C2_driver_reproduces_W4_first_approval_is_final (test_track1_fail_first.T) ... ok
test_C3_closed_is_terminal_in_history_and_driver (test_track1_fail_first.T) ... ok
test_C3_genesis_takes_the_lock_before_testing_existence (test_track1_fail_first.T) ... ok
test_C4a_builder_missing_args_is_logged (test_track1_fail_first.T) ... ok
test_C4b_builder_output_failure_after_validation_is_logged (test_track1_fail_first.T) ... ok
test_C4c_collector_argparse_failure_is_disclosed (test_track1_fail_first.T) ... ok
test_C5_round_6441904_excluded_by_name (test_track1_fail_first.T) ... ok
test_C6_uppercase_hex_signature_is_the_same_value (test_track1_fail_first.T) ... ok
test_C7_C8_C10_rule_text_consistent (test_track1_fail_first.T) ... ok
test_C9_sentinel_journal_must_be_complete (test_track1_fail_first.T) ... ok
Ran 10 tests in 8.913s
OK
```
