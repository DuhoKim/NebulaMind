# PIN IMMUTABILITY RULE (adopted 2026-09-06 23:00 KST after the third pin drift of 2026-09-06; Blanc's order 22:58 KST)

1. A file becomes PINNED the moment its digest is stated to a dispatched review: in a rule/candidate text, a brief, a pin sheet, or a sandbox digest list (COPIED_DIGESTS.txt).
2. A pinned file is IMMUTABLE at its path until the review's verdicts are filed in the lane. No edit, no "staged"/"draft" exception; test files, fixtures and inspection scripts included.
3. Any change to pinned bytes goes to a NEW filename (successor: v(N+1), _v2, …). The predecessor stays at its path or, if the path must carry the successor, under an archived name with its digest recorded.
4. The sandbox digest list of a review is the authority on what its reviewers read. A verdict is labelled with the digests it was rendered on; a later re-pin never rewrites an earlier text.
5. Before dispatch: verify every stated digest against the bytes in the sandbox (already done by the wrapper for the target; extend to the pin set). After the verdicts: never retro-edit a pinned text to match drifted bytes — record the drift (old digest, new digest, what changed, whether any verdict depended on it).
Breach today (M5): history_v2.py, test_track1_fail_first.py, coherent_attacks.py, test_track2_fail_first.py edited in place after the V22 review; recorded in PIN_DRIFT_RECORD_V22_M5_20260906.md; V22 bytes restored under _optionA_dev/_archive_v22_pins/.
