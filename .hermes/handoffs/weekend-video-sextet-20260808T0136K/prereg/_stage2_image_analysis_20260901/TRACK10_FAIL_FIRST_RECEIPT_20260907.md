# TRACK 10 FAIL-FIRST RECEIPT (codex V29-1/2/3/4 — contradictions, repaired; Blanc 02:06 categories) — 2026-09-07 03:20 KST

## Run 1: against BYTE-COPIES of the V29 modules (import lines and the fixture's opening line renamed only), BEFORE any repair
```
cbebc41767149caa  ../track2/provenance_designs_v10.py (copy)
3a783d7080102e55  ../fourier_chirality/run_configurations_v14.py (copy)
test_no_stage_retries_before_the_local_sweep_and_same_id_authentication (test_track10_fail_first.V29_1_2_CompletePaths) ... FAIL
test_labels_and_placeholders (test_track10_fail_first.V29_3_Text) ... FAIL
test_equal_timestamps_are_not_earlier_in_either_feed_order (test_track10_fail_first.V29_4_StrictEarlier) ... FAIL
    self.assertTrue(str(cm.exception).startswith("EVENT-INCONSISTENT"), str(cm.exception))
AssertionError: False is not true : REDERIVE-RETRY: fewer than 2 distinct pinned relays verify for round 6441924 (or verified values disagree); retry later
    self.assertEqual(re.findall(r"`\\[0-9]`", r), [], "literal backreference tokens where digests belong")
AssertionError: Lists differ: ['`\\2`', '`\\1`', '`\\2`', '`\\1`'] != []
    o, why = P.authenticate_event(genuine, order, REPO, REF, commit, root=tmp); self.assertEqual(o, "AUTHENTIC", why)
AssertionError: 'NOT-EARLIEST' != 'AUTHENTIC'
Ran 3 tests in 2.068s
FAILED (failures=3)
```

## Run 1b: the resolver's own pairwise test (Blanc 03:20, item 4), against the UNREPAIRED v10 copy — no resolver exists there
```
test_pairwise_same_winner_regardless_of_derivation_order (test_track10_fail_first.Resolver) ... ERROR
AttributeError: module 'provenance_designs_v10' has no attribute 'PRECEDENCE'
Ran 1 test in 0.000s
FAILED (errors=1)
```

## Run 2 (code cases): against the REPAIRED successors provenance_designs_v10 / run_configurations_v14 (ONE resolver, four contributing stages). (Two earlier runs of this block executed before the driver edit had applied — the edit script had aborted on a guard and then been mis-indented; harness errors, removed; the driver edit is now applied in full, `_tmp_v30_driver_edit.py`.)
```
test_no_stage_retries_before_the_local_sweep_and_same_id_authentication (test_track10_fail_first.V29_1_2_CompletePaths) ... ok
test_equal_timestamps_are_not_earlier_in_either_feed_order (test_track10_fail_first.V29_4_StrictEarlier) ... ok
test_pairwise_same_winner_regardless_of_derivation_order (test_track10_fail_first.Resolver) ... ok
Ran 3 tests in 13.768s
OK
```

## Run 2b: every EXISTING precedence test kept (Blanc item 4) — tracks 8 and 9 re-run against the v10/v14 successors by import alias, plus the v14 driver fixture (23)
```
test_precedence_survives_the_prechecks (test_track9_fail_first.V28_1_2_CompletePaths) ... ok
test_later_distinct_delivery_does_not_invalidate_the_earliest (test_track9_fail_first.V28_3_RuleIII) ... ok
test_same_id_contradiction_beats_undetermined_delivery (test_track8_fail_first.V27_1_Precedence) ... ok
test_same_id_differently_encoded_copy_beats_verbatim_presence (test_track8_fail_first.V27_1_Precedence) ... ok
test_local_mismatch_decided_before_retrieval (test_track8_fail_first.V27_1_Precedence) ... ok
test_git_launch_failure_is_undetermined (test_track8_fail_first.V27_2_TriStatePropagation) ... ok
test_open_event_stage_is_tri_state (test_track8_fail_first.V27_2_TriStatePropagation) ... ok
test_precheck_and_open_stage_tri_state_on_the_complete_path (test_track8_fail_first.V27_2_DriverPath) ... ok
Ran 8 tests in 29.331s
OK
driver under test has composed_resolver: True
Ran 23 tests in 114.561s
OK
```

## Run 3 — text: the V30-specific text test FAIL-FIRST against V29, then V30; track 10's V29-3 text case against V29 (fail-first) and V30
```
[test_track10_text_v30 vs V29]
Ran 1 test in 0.001s
FAILED (failures=1)
[test_track10_text_v30 vs V30]
Ran 1 test in 0.001s
OK
[V29_3_Text vs V29]
Ran 1 test in 0.001s
FAILED (failures=1)
[V29_3_Text vs V30]
Ran 1 test in 0.001s
OK
```

## Run 4 — the complete aggregate on the V30 candidate (`_tmp_v30_all_suites_aggregate_RUN1.txt`): 141 tests in 24 suites, every block OK, warning-strict; attribution: track 5 → V25, track-6 text → V26, track-7 text → V27, track 8 + the V28-specific text → V28, the V29-specific text → V29, track 9's fail-first (its V28-3 text case holds against V30 as well, so it ran against V30) and the version-agnostic tests + track 10 + the V30-specific test → V30.

## Per-test classification (written against the SUCCESSORS; run 1 against byte-copies of the V29 modules)
| test | kind | run 1 (V29 copies) | run 2 (repaired, ONE resolver) | codex / Blanc |
|---|---|---|---|---|
| V29_1_2 no stage retries before the local sweep and same-id authentication — codex's seven V29 rows on the COMPLETE path (unverifiable seed bodies + undetermined approval + wrong repository → EVENT-INCONSISTENT; + genuine same-id contradiction → EVENT-FORGED; genuine approval → REDERIVE-RETRY; open event wrong repository with ls-remote down / approval feed 503 → OPEN-EVENT-INCONSISTENT-INPUT; open same-id contradiction with ls-remote down → OPEN-EVENT-FORGED; genuine open event with ls-remote down → RETRY-REMOTE-UNAVAILABLE) | complete-path, behavioural | FAIL at the first row (`REDERIVE-RETRY: fewer than 2 distinct pinned relays verify…`, codex's exact V29-1 output); the later rows were not reached by the lane's run 1 — codex's dispatched V29 report (seat B, category 2) executed each on the V29 bytes | ok | V29-1, V29-2; Blanc 03:20 |
| V29_4 equal timestamps are not earlier in either feed order; strictly earlier → NOT-EARLIEST; the clause in the module header | behavioural + text | FAIL (NOT-EARLIEST on the reversed order) | ok | V29-4 |
| Resolver: pairwise same winner regardless of derivation order (21 class pairs, both orders; within-class fixed sequence; classify_history) | resolver's own | run 1b: ERROR (no resolver, no PRECEDENCE) | ok | Blanc 03:20 items 1–4 |
| V29_3 labels and placeholders (no literal backreference tokens; the four digests written out; driver v14 / builder v30 / verdict v30 labels; V29-1..4, resolver, exhibit names) | text | FAIL (four `\1`/`\2` tokens found; stale labels) | ok vs V30 | V29-3 |

Run 2b: every existing precedence test of tracks 8 and 9 (8 tests) re-run against the v10/v14 successors — OK; the v14 driver fixture (23) — OK. No test expectation was changed in track 10; the two harness errors (the driver edit not yet applied when a run-2 block was first executed) are disclosed in place.

## Digests
```
f2c878f2611a840a1bf8865a02023621b54ccf5ffb8a0b0b008a983586b0d8d3  _optionA_dev/track2/provenance_designs_v10.py
264a3897e335bb5bc9f83fc63ac7d3cabef7815f9f563e97a02d93ad8800b22a  _optionA_dev/fourier_chirality/run_configurations_v14.py
fbaf17c0d828f666c7f9228532042b0bdbb861b0d41fb13632540251fa2af240  _optionA_dev/fourier_chirality/test_run_configurations_v14.py
aec5834cd6e944c4911ff9f5c614e12d4d87970c513a022bb84b6915c447064f  _optionA_dev/corpus_identity/build_corpus_identity_v30.py
2a3eeb0e5e50b2b9fe408369984c342861fe650a443d01649b95d55dc1d56224  _optionA_dev/corpus_identity/test_build_corpus_identity_v30.py
43f7c1f7b9335425849aefab420ea0e727f5db63749a7fc8b7145222525c0111  _optionA_dev/beacon_v2/beacon_record_drand_v30.py
985f1784c5e4bf1a09561147a47a39540faeda37d0cdda3977c40efa7317178b  _optionA_dev/beacon_v2/test_beacon_record_drand_v30.py
3deb4802d3dd89c9ec121789df9d1aced80d17b950f3e8a06274836ba5dbf896  _optionA_dev/track1/coherent_attacks_v30.py
8206328178624949068c9fee2fa0652fc6ece625a68ce8f75a2926ed49fc1aa7  _optionA_dev/track10/test_track10_fail_first.py
e57fcb8191017c47fa500b7e94bb8d2fa1d25545e65be005bb4fabef217738e7  _optionA_dev/track10/test_track10_text_v30.py
d44bc2860e167842b6e561221dfc678d22d552b39d4f5f36ef575368ec8f65f8  _optionA_dev/track10/exhibit_precedence_pairs.py
98881c7ecba0ac3bb718983f8534aaa55d325efeb4314d72b31b64b95af2abb9  OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V30_20260907.md
c9f1a3507720fca2e9ee0b73ed8ff6c1b21b8df8ccff249f4f5565bc550ce561  V30_CANDIDATE_ATTACK_INSPECTION_20260907.md
30e01423ef40f058697b05bbe16d1b58d14f3ce4f5b1c6eff5f75dd1832dcd6e  V30_PRECEDENCE_EXHIBIT_20260907.md
b9daa35e13dc313c4f7db80fe4bf427edbc55891cfb83e0582b89637be4fe7ae  LIMITS_VS_CONTRADICTIONS_20260907.md
```

Closed 2026-09-07 03:39 KST. Nothing gated, adopted, signed or drawn.
