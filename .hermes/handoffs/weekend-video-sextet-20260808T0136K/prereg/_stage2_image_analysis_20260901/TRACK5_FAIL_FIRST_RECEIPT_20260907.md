# TRACK 5 FAIL-FIRST RECEIPT (codex V24 N1/N2/N3/N5; N4 by a correction note) — 2026-09-07 00:17 KST

## Run 1: against BYTE-COPIES of the V24 modules (import lines renamed only), BEFORE any repair. Per-test classification follows the run (missing-interface vs behavioural), not unittest's error/failure categories.
```
ddcfa7227c3510a2  ../track2/provenance_designs_v5.py (copy)
b83c41e7c75c5255  ../fourier_chirality/run_configurations_v9.py (copy)
2fa6c8eec05760dc  ../corpus_identity/build_corpus_identity_v25.py (copy)
9309d593a3546053  ../beacon_v2/beacon_record_drand_v25.py (copy)
test_N1_residual_is_the_covenant (test_track5_fail_first.N1_N5_Text) ... FAIL
test_N5_labels_and_sweep (test_track5_fail_first.N1_N5_Text) ... FAIL
test_N2a_empty_second_feed_is_retry_not_batch (test_track5_fail_first.N2_Dispositions) ... ERROR
test_N2b_missing_middle_event_is_incomplete_evidence_not_batch (test_track5_fail_first.N2_Dispositions) ... ERROR
test_N2c_multi_commit_delivery_is_batch (test_track5_fail_first.N2_Dispositions) ... ERROR
test_N3_unrelated_unpublished_commit_refused_before_publishing (test_track5_fail_first.N3_ProducerPrecondition) ... FAIL
AttributeError: module 'provenance_designs_v5' has no attribute 'validate_continuation_v5'
AttributeError: module 'provenance_designs_v5' has no attribute 'validate_continuation_v5'
AttributeError: module 'provenance_designs_v5' has no attribute 'validate_continuation_v5'
    t = p.read_text(encoding="utf-8"); self.assertIn("between later publications", t, p.name); self.assertIn("does not authenticate when", t, p.name)
    self.assertIn("3c. V25", r); self.assertNotIn("3c. V22", r); self.assertIn("coherent_attacks_v25.py", r); self.assertNotIn("`coherent_attacks.py` and add", r)
    with self.assertRaises(SystemExit) as cm: P.publish_entry(work, log.name, str(bare), REF, "entry 1")
AssertionError: SystemExit not raised
Ran 6 tests in 2.167s
FAILED (failures=3, errors=3)
```

## Run 1 classification (per test, from the output above)
- N2a/N2b/N2c: `validate_continuation_v5` does not exist in the copy → MISSING-INTERFACE (3 unittest errors); their OLD BEHAVIOUR is established in run 1b below by executing `validate_continuation_v4` on the same fixtures.
- N3: BEHAVIOURAL — the copy's `publish_entry` exists and PUBLISHED the entry together with the unrelated commit (SystemExit not raised); run 1b shows the same.
- N1/N5: text assertions against the V24 text/design/driver — BEHAVIOURAL (the text is what it is). Totals: 3 missing-interface, 3 behavioural.

## Run 1b: the same fixtures against the V24 functions (validate_continuation_v4, v4 publish_entry) — the OLD behaviour, executed
```
N2a v4, empty second feed: False HISTORY-PUBLICATION-BATCH — WRONG (should be retry)
N2b v4, one middle event missing: False HISTORY-PUBLICATION-BATCH — WRONG (no evidence of a batch)
N3 v4, unrelated commit rides along: PUBLISHED d8c562c89a58 — WRONG (the validator will refuse it: before != parent)
```

## Run 2: the SAME tests against the REPAIRED successors, the V25 staged text, the revised design document and questions file — 00:22 KST (test file identical to run 1; two earlier run-2 attempts — one before the V25 text existed, one before a case-only wording fix in the questions file — were stripped and are not counted; the fix added the lowercase phrase 'every history commit' the test looks for)
```
c265097167d81948  ../track2/provenance_designs_v5.py (repaired)
71c8a53b3f2ef2c3  ../fourier_chirality/run_configurations_v9.py (repaired)
c0e9000d8ef7b4ec  ../corpus_identity/build_corpus_identity_v25.py (repaired)
639427be5b058a9e  ../beacon_v2/beacon_record_drand_v25.py (repaired)
test file 0f0ce4780581026d
test_N1_residual_is_the_covenant (test_track5_fail_first.N1_N5_Text) ... ok
test_N5_labels_and_sweep (test_track5_fail_first.N1_N5_Text) ... ok
test_N2a_empty_second_feed_is_retry_not_batch (test_track5_fail_first.N2_Dispositions) ... ok
test_N2b_missing_middle_event_is_incomplete_evidence_not_batch (test_track5_fail_first.N2_Dispositions) ... ok
test_N2c_multi_commit_delivery_is_batch (test_track5_fail_first.N2_Dispositions) ... ok
test_N3_unrelated_unpublished_commit_refused_before_publishing (test_track5_fail_first.N3_ProducerPrecondition) ... ok
Ran 6 tests in 2.827s
OK
    exit status: 0
```
