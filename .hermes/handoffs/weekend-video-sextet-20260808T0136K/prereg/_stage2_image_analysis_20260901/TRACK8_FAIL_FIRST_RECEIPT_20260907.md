# TRACK 8 FAIL-FIRST RECEIPT (codex V27-1/2/3; Blanc 02:06: contradictions to repair, kept apart from disclosed limits) — 2026-09-07 02:06 KST

## Run 1: against BYTE-COPIES of the V27 modules (import lines renamed only), BEFORE any repair; per-test classification follows.
```
8c20a5d3370b4c91  ../track2/provenance_designs_v8.py (copy)
74518ab13a34d2ad  ../fourier_chirality/run_configurations_v12.py (copy)
0ab77f9a7fe4e27b  ../corpus_identity/build_corpus_identity_v28.py (copy)
2580370ad0c54d6a  ../beacon_v2/beacon_record_drand_v28.py (copy)
test_local_mismatch_decided_before_retrieval (test_track8_fail_first.V27_1_Precedence) ... FAIL
test_same_id_contradiction_beats_undetermined_delivery (test_track8_fail_first.V27_1_Precedence) ... FAIL
test_same_id_differently_encoded_copy_beats_verbatim_presence (test_track8_fail_first.V27_1_Precedence) ... FAIL
test_git_launch_failure_is_undetermined (test_track8_fail_first.V27_2_TriStatePropagation) ... ERROR
test_open_event_stage_is_tri_state (test_track8_fail_first.V27_2_TriStatePropagation) ... ERROR
test_names_and_count (test_track8_fail_first.V27_3_Text) ... ERROR
    self.assertEqual(P.delivery(anc, self.commit, REF, self.tmp / "not-a-repo"), "UNDETERMINED")
FileNotFoundError: [Errno 2] No such file or directory: PosixPath('/var/folders/64/71dstw0j1gd_n58lsxnhl3p80000gn/T/tmpx76iwbnm/not-a-repo')
AttributeError: module 'provenance_designs_v8' has no attribute 'validate_continuation_v8'
FileNotFoundError: [Errno 2] No such file or directory: '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/t
    o, why, prov = P.authenticate_event_live(wrong, REPO, lambda cmd: (1, "", "gh: HTTP 503: Service Unavailable"), REF, self.commit, root=self.work); self.assertEqual(o, "INCONSISTENT-INPUT", why)
AssertionError: 'UNAVAILABLE' != 'INCONSISTENT-INPUT'
    self.assertEqual(o, "FORGED", why)
AssertionError: 'UNAVAILABLE' != 'FORGED'
    o, why = P.authenticate_event(genuine, [genuine, copy], REPO, REF, self.commit, root=self.work); self.assertEqual(o, "FORGED", why)
AssertionError: 'AUTHENTIC' != 'FORGED'
Ran 6 tests in 2.098s
FAILED (failures=3, errors=3)
```

## Run 1b: codex's V27-1 cases against the V27 functions — the OLD behaviour, executed
```
V27-1(a) v7, same-id contradiction whose changed head is undeterminable in a stale clone: UNAVAILABLE — WRONG (retry declared before the contradiction was examined)
V27-1(b) v7, verbatim copy + differently encoded same-id copy: AUTHENTIC — WRONG (verbatim shortcut skipped the contradiction)
V27-1(c) v7, wrong repository + HTTP 503: UNAVAILABLE — WRONG (a locally decidable mismatch became a retry)
```

## Run 1c: codex's V27-2 complete-path cases (driver v12 COPY of v11, unrepaired) — fail-first
```
test_precheck_and_open_stage_tri_state_on_the_complete_path (test_track8_fail_first.V27_2_DriverPath) ... FAIL
    self.assertIn("IDENTITY-WITNESS-COMMIT-UNDETERMINED", str(cm.exception)); self.assertFalse(str(cm.exception).startswith("RETRY-"))          # offline: named, no retry vocabulary
AssertionError: 'IDENTITY-WITNESS-COMMIT-UNDETERMINED' not found in 'IDENTITY-WITNESS-COMMIT: the push event does not deliver the approval commit (head, commits, or before..head ancestry)'
Ran 1 test in 1.510s
FAILED (failures=1)
```

## Run 2 (code cases only; the V27-3 text case waits for the V28 text): against the REPAIRED successors provenance_designs_v8 / run_configurations_v12
```
test_local_mismatch_decided_before_retrieval (test_track8_fail_first.V27_1_Precedence) ... ok
test_same_id_contradiction_beats_undetermined_delivery (test_track8_fail_first.V27_1_Precedence) ... ok
test_same_id_differently_encoded_copy_beats_verbatim_presence (test_track8_fail_first.V27_1_Precedence) ... ok
test_git_launch_failure_is_undetermined (test_track8_fail_first.V27_2_TriStatePropagation) ... ok
test_open_event_stage_is_tri_state (test_track8_fail_first.V27_2_TriStatePropagation) ... FAIL
test_precheck_and_open_stage_tri_state_on_the_complete_path (test_track8_fail_first.V27_2_DriverPath) ... FAIL
    else: self.assertTrue(why.startswith("EVIDENCE-") or ok, why)                                            # (objects present after fetch: the validator fetches the ref; then the event authenticates or is otherwise EVIDENCE-*)
AssertionError: False is not true : HISTORY-PUBLICATION-BATCH: the feed shows history commit 18dc31ccfa4a (entry 0) delivered inside a push that carried other commits (open-anc; proven by head/commits/before..head ancestry) — not an acknowledged publication of its own; terminal
    self.assertTrue(str(cm.exception).startswith("HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT"), str(cm.exception))
AssertionError: False is not true : EVENT-NOT-EARLIEST: an earlier qualifying event exists in the live feed; the retained one is not the earliest (an input inconsistency, not 'different bytes')
Ran 6 tests in 9.644s
FAILED (failures=2)
```

## Run 2b — two TEST-CONSTRUCTION corrections, disclosed (no code change between run 2 and 2b): (1) the standalone open-event case had withheld an object the validator's own fetch restores, so its 'undetermined' event became a proven batch — rewritten with a `before` no clone holds (UNDETERMINED after any fetch) and a positive non-delivery case (before = head = the open commit's grandparent); (2) driver case (d) had used the open commit's parent, which is the approval commit itself, so the event qualified for the approval stage (EVENT-NOT-EARLIEST) — moved to the grandparent.
```
test_local_mismatch_decided_before_retrieval (test_track8_fail_first.V27_1_Precedence) ... ok
test_same_id_contradiction_beats_undetermined_delivery (test_track8_fail_first.V27_1_Precedence) ... ok
test_same_id_differently_encoded_copy_beats_verbatim_presence (test_track8_fail_first.V27_1_Precedence) ... ok
test_git_launch_failure_is_undetermined (test_track8_fail_first.V27_2_TriStatePropagation) ... ok
test_open_event_stage_is_tri_state (test_track8_fail_first.V27_2_TriStatePropagation) ... ok
test_precheck_and_open_stage_tri_state_on_the_complete_path (test_track8_fail_first.V27_2_DriverPath) ... ok
Ran 6 tests in 9.721s
OK
```

## Run 2c — the corrected open-event / driver cases against the UNREPAIRED bytes (a byte-copy of v7 as provenance_designs_v8 and of v11 as run_configurations_v12 under `_tmp_v28_unrepaired/`, import lines renamed only), so the corrected tests are shown to fail-first too. (A first attempt of this block resolved the repaired module and lacked the BLS site-packages — a harness error, removed; this is the re-run.)
```
test_open_event_stage_is_tri_state (test_track8_fail_first.V27_2_TriStatePropagation) ... ERROR
test_precheck_and_open_stage_tri_state_on_the_complete_path (test_track8_fail_first.V27_2_DriverPath) ... FAIL
AttributeError: module 'provenance_designs_v8' has no attribute 'validate_continuation_v8'
    self.assertIn("IDENTITY-WITNESS-COMMIT-UNDETERMINED", str(cm.exception)); self.assertFalse(str(cm.exception).startswith("RETRY-"))          # offline: named, no retry vocabulary
AssertionError: 'IDENTITY-WITNESS-COMMIT-UNDETERMINED' not found in 'IDENTITY-WITNESS-COMMIT: the push event does not deliver the approval commit (head, commits, or before..head ancestry)'
Ran 2 tests in 1.997s
FAILED (failures=1, errors=1)
unrepaired P loaded from: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_tmp_v28_unrepaired/track2/provenance_designs_v8.py
unrepaired driver loaded from: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_tmp_v28_unrepaired/fourier_chirality/run_configurations_v12.py
```

## Run 3 — text: the V28-specific text test (written against V28) FAIL-FIRST against the V27 text, then against V28; the track-8 V27-3 assertions against V28 + the corrected design document. Disclosed: the V27-3 case first asserted '18 suites' (codex's count of the V27 logs); the V28 candidate executes 20 suites and states 20 — the expectation was corrected to the V28 statement before this run (the test digest pinned in the V28 text is the corrected file's).
```
[test_track8_text_v28 vs V27 text]
AssertionError: 'DRAFT V28 — STAGED CANDIDATE' not found in '# OPTION (A) — INSTRUMENT SELECTION RULE, DRAFT V27 — STAGED CANDIDATE (NOT GATED, NOT ADOPTED, NOT APPROVED) — DRAND-ONLY SAMPLING AMENDME
Ran 1 test in 0.001s
FAILED (failures=1)
[test_track8_text_v28 vs V28 text]
Ran 1 test in 0.001s
OK
[V27_3_Text vs V27 text (fail-first) / vs V28 text + design doc rev 8]
Ran 1 test in 0.001s
FAILED (failures=1)
Ran 1 test in 0.001s
OK
```

## Run 4 — the complete aggregate on the V28 candidate (`_tmp_v28_all_suites_aggregate_RUN1.txt`): 132 tests in 20 suites, every block OK, warning-strict; text attribution: track 5 → V25, track-6 text → V26, track-7 text → V27, version-agnostic tests + the V28-specific test → V28.

## Per-test classification (written against the SUCCESSORS; run 1/1b/1c/2c against the V27 bytes or byte-copies)
| test | kind | run 1 (V27 copies) | run 2b (repaired) | codex clause |
|---|---|---|---|---|
| V27_1 same-id contradiction beats undetermined delivery | behavioural | FAIL (UNAVAILABLE) | ok (FORGED) | V27-1 first probe |
| V27_1 differently encoded same-id copy beats verbatim presence | behavioural | FAIL (AUTHENTIC) | ok (FORGED) | V27-1 defensive probe |
| V27_1 local mismatch decided before retrieval (wrong repo / positive non-delivery under HTTP 503; undetermined + 503 stays UNAVAILABLE) | behavioural | FAIL (UNAVAILABLE) | ok | V27-1 second |
| V27_2 git launch failure is UNDETERMINED (not a repo; patched OSError) | behavioural | ERROR (OSError raised) | ok | V27-2 'process-launch exceptions' |
| V27_2 open-event stage is tri-state (standalone validator) | missing interface | ERROR (no validate_continuation_v8); run 2c on the v7 bytes: ERROR | ok (EVIDENCE-UNAVAILABLE / OPEN-EVENT-INCONSISTENT-INPUT) | V27-2 P:282 |
| V27_2 precheck + open stage on the COMPLETE path (driver v12, four cases a–d) | complete-path | run 1c: FAIL (IDENTITY-WITNESS-COMMIT); run 2c on the v11 bytes: FAIL | ok | V27-2 D:247 / D:343 |
| V27_3 names and count (driver lineage, helper docstrings, inspection header, design row 9b, §9, suite count, categories kept apart) | text | ERROR (no coherent_attacks_v28) / FAIL vs V27 text | ok vs V28 | V27-3 |

Test-expectation corrections made between runs, all disclosed above: two test constructions (run 2b) and one stale suite-count expectation (run 3). No code was changed to satisfy a test after run 2; the two run-2 failures were test-side.

## Digests
```
fd5b7eb5f3ce8efcce0105f54d3b7acbfc8e3e57e880a39647995851cec3126e  _optionA_dev/track2/provenance_designs_v8.py
ad01d6a9a294c0cda32ec45c3f722e7336b34ee03871989c323fc7cdb556cd7a  _optionA_dev/fourier_chirality/run_configurations_v12.py
45436198dbb5539144143cf807c8763f23c8cd39ad104c4bdb794e923cbe4d57  _optionA_dev/fourier_chirality/test_run_configurations_v12.py
0ab77f9a7fe4e27b28856aa1ba693f5223d711fb22a342e332d65dcae86decb1  _optionA_dev/corpus_identity/build_corpus_identity_v28.py
fd581106fae0475112337d3b7677c95d805f73a4bd9db7bb9f87268baf4f5691  _optionA_dev/corpus_identity/test_build_corpus_identity_v28.py
2580370ad0c54d6a9cd9cf7771c3f25ecad8306803078a815966cecc090dd55d  _optionA_dev/beacon_v2/beacon_record_drand_v28.py
a8289e0e9de89cd8657f7c4ddd58898a69c1e0e74dfa34bade406a62a7ab23a3  _optionA_dev/beacon_v2/test_beacon_record_drand_v28.py
7823d819d21d49f2016ff8a49d7fa32f3ce3a0c7fbf9d15b6e604f2c82ff0f1e  _optionA_dev/track1/coherent_attacks_v28.py
05710cb371138a34825c53aa9c80e9370be935a5a428201c4366329eaa4cc494  _optionA_dev/track8/test_track8_fail_first.py
4f1dc05521aec6588a70a5df5286b479c670f6824d1c40a65ca4bdca2db1f81e  _optionA_dev/track8/test_track8_text_v28.py
c9e65f1bfc2bdac10716760670c85866d20c1ec0ca1d9aebdfa5b83842804fc2  OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V28_20260907.md
9e1e55fe334c045b27b24458ebd160d041d12a247a611a6f62159f34a6339ded  V28_CANDIDATE_ATTACK_INSPECTION_20260907.md
b90b0ae41327dba132b780d497769bf7b9c48f6ddca1b9af39e813590a75f844  LIMITS_VS_CONTRADICTIONS_20260907.md
e58c2d1e1130402fe448c0e54cb1328796141956d4bc66f19890ef9e816c769d  TRACK2_PROVENANCE_DESIGNS_UNADOPTED_20260906.md
```

Closed 2026-09-07 02:24 KST. Nothing gated, adopted, signed or drawn.
