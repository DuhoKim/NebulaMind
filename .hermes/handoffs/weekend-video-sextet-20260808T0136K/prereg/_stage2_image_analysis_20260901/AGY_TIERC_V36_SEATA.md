ACCESS_SHA=017045d95f7b1fe551e36879f2409d9f1ac77b5ddcb123984d965fb7c7a71ef4

AUTHORSHIP: My engine (Gemini 3.1 Pro / Antigravity) did not author anything reviewed here, to the best of my knowledge. No finding depends on code it wrote.

1. [MINOR] DOES THE CODE DO WHAT §8.9a/§8.9b/§8.9d/§8.12 NOW SAY, and nothing else?
Yes, it does exactly what the clauses say. I read `pixel_rejection_v2.py` line by line:
- Five rejecting bits are explicitly set (`1, 3, 6, 10, 13`).
- `MEDIUM` (11) is excluded from the rejection mask, carried, and its count is tracked via `medium_count()`.
- Source pixels with `nexp-r == 0` are evaluated on the source grid, included in the boolean rejection mask via `zero_exposure_mask()`, replaced by the lower median of accepted pixels (with unexposed pixels correctly excluded from that median), and flagged on output.
- Non-integer, mismatched shape, and negative exposure counts immediately raise explicit `ValueError`s.
- The 16-pixel floor for replacement remains unchanged (`MIN_ACCEPTED = 16`).
Regarding §8.9a pins, I verified the hashes of all pinned files and they match exactly:
- `pixel_rejection_v2.py`: `0655370958b7fd65dd2324d41b0a05aa31dd0e8a50f01317e63bf663bb9f6cde`
- `test_pixel_rejection_v2.py`: `85aaba182dd0ffe5f4d6f4bb429ec390e0cf9223ba1faf0f2c2f39b0a5d8ead8`
- `pixel_rejection.py`: `8f66bc1c61173648f11386eb17f2d5afd3c3f1a338aee5bf3e11fe9aad950818`

2. [MINOR] DOES THE FIXTURE FAIL ON THE OLD BEHAVIOUR?
Yes. The fixture explicitly imports the V35 module (`pixel_rejection.py`) as `V1` and runs it on identical synthetic input planes alongside the new V2 module. A reviewer swapping V2 for V35 would see failures because the fixture explicitly asserts differences on the old behavior:
- `test_medium_is_carried_not_replaced__old_module_replaces_it` asserts `old_cleaned[3, 3] != img[3, 3]` and that `11` is in `V1.REJECT_BITS`.
- `test_zero_exposure_rejects_and_flags__old_module_ignores_nexp` asserts that under V1, `old_n == 0` and the unexposed pixel survives untouched (`old_cleaned[5, 1] == img[5, 1]`).

3. [MINOR] SCOPE: is any clause beyond the five named changed?
No. A full diff between V35 and V36 confirms that exactly those five clauses (§8.9a, §8.9b, §8.9d, §8.12, §8.15b) were changed, alongside expected updates to the header block, signature block, and the register block. A strict grep confirms that no other clause still asserts the six-bit set or the all-or-nothing coverage rule (the mention in V36 §8.12 explicitly records its removal). The regenerated register agrees exactly with the clause text (verified by `--audit` returning exit code 0).

4. [MINOR] §17.6 FORM:
The form strictly adheres to §17.6 requirements:
- The new version is properly identified as V36.
- The disclosed diff is explicitly named in the header (`MINI_PREREG_V36_CHANGE_RECORD_20260906.md` with `V35_TO_V36.diff`).
- The signature block is blanked (empty UTC).
- The preimage digest perfectly matches the file digest (`017045d95f7b1fe551e36879f2409d9f1ac77b5ddcb123984d965fb7c7a71ef4`).
- The approval-procedure paragraph accurately describes what will run (Codex-conversation approval and Blanc's recomputation) and explicitly bounds what it proves (verifying bytes on disk, not who spoke).

5. [MINOR] Is the relaxation bounded exactly as V15 §6 requires? Is anything aspirational?
Yes, the relaxation is bounded exactly as required by Option A V15 §6. The maximum flagged pixel limit `F ≤ 819` and the core protected radius `r_T = 23` are wholly unchanged and appropriately continue to govern zero-exposure pixels. Nothing in the text is aspirational or unexecuted; every modified clause accurately maps to the already-written, functioning, and tested module.

6. [MINOR] What is still missing for SIGNABLE, as clause text; or state that nothing is.
Nothing is missing. The document conforms exactly to its stated purpose and constraints, implementing the pipeline correctly to precisely match the Option A requirements.

VERDICT: SIGNABLE
