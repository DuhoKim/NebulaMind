# TRACK 11 FAIL-FIRST RECEIPT (codex V30-1 FATAL, V30-2/3/4) — 2026-09-07 04:17 KST

## Run 1: THE FATAL REPRODUCED IN EXECUTED OUTPUT before any repair (the V20 rule), plus the V30-2/3 rows — against BYTE-COPIES of the V30 modules (import lines and the fixture's opening line renamed only)
```
f2c878f2611a840a  ../track2/provenance_designs_v11.py (copy)
4164d411144fcf6b  ../fourier_chirality/run_configurations_v15.py (copy)
test_offline_wording_and_policies (test_track11_fail_first.V30_4_Text) ... FAIL
test_every_named_refusal_has_a_class_and_ordering_is_expiry_before_unavailability (test_track11_fail_first.V30_Classification) ... ERROR
test_V30_1_null_open_event_file_never_accepts (test_track11_fail_first.V30_CompletePath) ... FAIL
test_V30_2_local_findings_beat_early_and_late_retries (test_track11_fail_first.V30_CompletePath) ... FAIL
test_V30_3_higher_findings_are_not_suppressed_and_one_snapshot_serves_all (test_track11_fail_first.V30_CompletePath) ... FAIL
    got = P.classify_refusal(f"{c}: some detail"); self.assertEqual(got[0], cls, f"{c} → {got}"); self.assertFalse(got[3], f"{c} unclassified")
AttributeError: module 'provenance_designs_v11' has no attribute 'classify_refusal'
    self.assertNotIn("offline mode, which has no retry vocabulary", r); self.assertIn("REDERIVE-RETRY", r); self.assertIn("WITNESS-FETCH-FAILED", r)
    with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
AssertionError: DataIntegrityFail not raised
    self.assertTrue(str(cm.exception).startswith("EVENT-INCONSISTENT"), str(cm.exception))
AssertionError: False is not true : WITNESS-FETCH-FAILED fatal: '/var/folders/64/71dstw0j1gd_n58lsxnhl3p80000gn/T/tmpyz87q4sf/no-such-remote.git' does not appear to be a git rep
    self.assertIn("NOT-AN-EXTENSION", str(cm.exception)); self.assertFalse(str(cm.exception).startswith("RETRY-"), str(cm.exception))
AssertionError: 'NOT-AN-EXTENSION' not found in 'RETRY-EVENTS-UNAVAILABLE: the live feed is EMPTY — no evidence either way (v3, codex V22 F); retry'
Ran 5 tests in 9.490s
FAILED (failures=4, errors=1)
```

## Run 2 (code cases): against the REPAIRED successors provenance_designs_v11 / run_configurations_v15 (staged finding collector)
```
test_V30_1_null_open_event_file_never_accepts (test_track11_fail_first.V30_CompletePath) ... ok
test_V30_2_local_findings_beat_early_and_late_retries (test_track11_fail_first.V30_CompletePath) ... ok
test_V30_3_higher_findings_are_not_suppressed_and_one_snapshot_serves_all (test_track11_fail_first.V30_CompletePath) ... ok
test_every_named_refusal_has_a_class_and_ordering_is_expiry_before_unavailability (test_track11_fail_first.V30_Classification) ... ok
Ran 4 tests in 31.169s
OK
```

## Run 2b: EVERY existing precedence test kept — tracks 8, 9 and 10 re-run against the v11/v15 successors by import alias
```
test_no_stage_retries_before_the_local_sweep_and_same_id_authentication (test_track10_fail_first.V29_1_2_CompletePaths) ... ok
test_equal_timestamps_are_not_earlier_in_either_feed_order (test_track10_fail_first.V29_4_StrictEarlier) ... ok
test_pairwise_same_winner_regardless_of_derivation_order (test_track10_fail_first.Resolver) ... ok
test_precedence_survives_the_prechecks (test_track9_fail_first.V28_1_2_CompletePaths) ... ok
test_later_distinct_delivery_does_not_invalidate_the_earliest (test_track9_fail_first.V28_3_RuleIII) ... ok
test_same_id_contradiction_beats_undetermined_delivery (test_track8_fail_first.V27_1_Precedence) ... ok
test_same_id_differently_encoded_copy_beats_verbatim_presence (test_track8_fail_first.V27_1_Precedence) ... ok
test_local_mismatch_decided_before_retrieval (test_track8_fail_first.V27_1_Precedence) ... ok
test_git_launch_failure_is_undetermined (test_track8_fail_first.V27_2_TriStatePropagation) ... ok
test_open_event_stage_is_tri_state (test_track8_fail_first.V27_2_TriStatePropagation) ... ok
test_precheck_and_open_stage_tri_state_on_the_complete_path (test_track8_fail_first.V27_2_DriverPath) ... FAIL
    self.assertTrue(str(cm.exception).startswith("EVENT-INCONSISTENT: IDENTITY-WITNESS-COMMIT"), str(cm.exception))
AssertionError: False is not true : EVENT-INCONSISTENT: the retained event positively does not deliver the approval commit to the protected ref
Ran 11 tests in 38.400s
FAILED (failures=1)
driver under test is the staged collector: True
```

## Run 2c — one wording restoration, disclosed (no logic change): the new S0 local sweep finds positive non-delivery before the conjunction's precheck, so its finding carried local_precheck's reason instead of the composed name promised since V28 (EVENT-INCONSISTENT: IDENTITY-WITNESS-COMMIT …); S0 now prefixes that name; the track-8 test was NOT changed. Re-run of the one affected test:
```
test_precheck_and_open_stage_tri_state_on_the_complete_path (test_track8_fail_first.V27_2_DriverPath) ... ok
Ran 1 test in 9.786s
OK
```

## Run 3 — text: the V31-specific text test FAIL-FIRST against V30, then V31; track 11's V30-4 text case against V30 (fail-first) and V31. Disclosed: (1) the V30-4 case was scoped to the CURRENT text (the newest version paragraph and §3c) before this run, since historical paragraphs keep their wording verbatim; (2) a first generation of the V31 text had applied the §3c resolver rewrite to the historical V30 paragraph instead of §3c — the V31-specific test caught it (no 'S0' in §3c); the edit script was anchored to §3c and the text regenerated from V30; the earlier run of this block is removed. The test digests pinned in V31 are the final files'.
```
[test_track11_text_v31 vs V30]
Ran 1 test in 0.001s
FAILED (failures=1)
[test_track11_text_v31 vs V31]
Ran 1 test in 0.001s
OK
[V30_4_Text vs V30]
Ran 1 test in 0.001s
FAILED (failures=1)
[V30_4_Text vs V31]
Ran 1 test in 0.000s
OK
```

## Run 4 — the complete aggregate on the V31 candidate (`_tmp_v31_all_suites_aggregate_RUN1.txt`): 147 tests in 26 suites, OK blocks 26; attribution: track 5 → V25, track-6 text → V26, track-7 text → V27, track 8 + the V28 text → V28, the V29 text → V29, track 10 (its text case asserts the V30 labels) + the V30 text → V30, version-agnostic tests + track 9 + track 11 + the V31 text → V31.

## Per-test classification (written against the SUCCESSORS; run 1 against byte-copies of the V30 modules)
| test | kind | run 1 (V30 copies) | run 2 (repaired) | codex |
|---|---|---|---|---|
| V30_1 a null / non-object open-event file never accepts; the rewrite + null stays refused | FATAL reproduction, behavioural | FAIL — `DataIntegrityFail not raised`: the null open file LOADED (the FATAL, in executed output) | ok (HISTORY-OPEN-EVENT-INVALID; the rewrite + null refused) | V30-1 |
| V30_2 wrong approval repository + failed witness fetch → EVENT-INCONSISTENT; one tuning id missing + HTTP 503 → IDENTITY-tuning_objids-SIZE-OR-TYPE | complete-path, behavioural | FAIL (WITNESS-FETCH-FAILED, codex's exact output) | ok | V30-2 |
| V30_3 a rewrite with an empty feed → HISTORY-NOT-AN-EXTENSION; undetermined approval + newer feed + remote down → EVENT-EXPIRED-NO-RECEIPT-PATH; one retrieval per invocation | complete-path, behavioural | FAIL (RETRY-EVENTS-UNAVAILABLE on the empty feed) | ok | V30-3 |
| V30_Classification every named refusal of codex's inventory classified; unknown codes flagged; malformed input class 0 / I/O class 5; EXPIRED before UNAVAILABLE | table + predicate | ERROR (no classify_refusal) | ok | V30-2/3 |
| V30_4 text (current-text scope) | text | FAIL vs V30 | ok vs V31 | V30-4 |

Run 2b: every existing precedence test of tracks 8–10 (11 tests) re-run against v11/v15 — OK after one disclosed wording restoration in S0 (no test changed, no logic changed); run 2c re-ran the affected test. Test-side corrections: the V30-4 case scoped to the current text (disclosed at run 3). Harness errors: none in this track.

## Digests
```
4d4a2a439765d394007746ac82d54838348bd127832d41dd571946e4d5a446ab  _optionA_dev/track2/provenance_designs_v11.py
a9ffae72071fbd5d0f7f0e337ec825307a494f3ae26d5d6d4b91d647bcb2ebe1  _optionA_dev/fourier_chirality/run_configurations_v15.py
3f7d5d07e2d0319a440c4229e91e916ce01bdb9810e9f1b45138d8d1ac2b53ec  _optionA_dev/fourier_chirality/test_run_configurations_v15.py
883ca5e9d0856dd78485e1d21cf92e1e023af129046faf74defac90d8af5bf25  _optionA_dev/corpus_identity/build_corpus_identity_v31.py
4a001d9b740f994484e78348caac08e045a502e2e90597a48b137174d1b7565c  _optionA_dev/corpus_identity/test_build_corpus_identity_v31.py
90a8059f472a4a3bbe76dab485cc680566ebc8487024f0d85a82f68d2c3e30a2  _optionA_dev/beacon_v2/beacon_record_drand_v31.py
f5cb4df48a489c9a2dd069920c9b5b02015312fbdd058b07059c24847d9e979d  _optionA_dev/beacon_v2/test_beacon_record_drand_v31.py
c9b6847417c8f8bccc32dfee9953a9f5876305c69c7d1d2b634680d0fb65d566  _optionA_dev/track1/coherent_attacks_v31.py
ae61a5ee0251c8e98c9b6825b604430f3da3a10e22d5e48c624f0a066d8888fb  _optionA_dev/track11/test_track11_fail_first.py
dcc2a63f0b3dce1eea3354946b991ac927a9db01a8f0f5d480feb4a298d8f820  _optionA_dev/track11/test_track11_text_v31.py
f94b45e626ec95f1d2a60da783eb23c70f02394bbbe2be7389583013dd00cc49  OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V31_20260907.md
52c8b0e3c40651b1806c5f3db81fc0bdf436951d73b922c5ff9d99daa082a286  V31_CANDIDATE_ATTACK_INSPECTION_20260907.md
c698fd1a7131d85fe417c6298600849ac409c2aa71bb237858ca55d79d4719b6  LIMITS_VS_CONTRADICTIONS_20260907.md
```

Closed 2026-09-07 04:30 KST. Nothing gated, adopted, signed or drawn.
