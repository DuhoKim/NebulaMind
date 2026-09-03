ACCESS_SHA=76e15005585d84ebab98ba792892e48152e7ff21233da449d5c69c9a25dd097f

F1. SEVERITY: FATAL
CLAUSE: Truthful statement of machine facts / Hiding FAILED outcome
EVIDENCE:
Command: `grep -E "5049|5,049|0.864|draw 94|-0.10" PREREG_SUCCESSOR_DRAFT_V137_20260903.md`
Output: (Empty / No matches found)
The human direction requires the draft to state truthfully the machine facts of the fresh sweep: determinism (two runs, identical receipt digest 19ffcbab...), 0 of 5049 cells INCONCLUSIVE-BY-CALIBRATION, min a_lb 0.864, sigma_gamma 0.0479, and crucially that the invariance receipt is FAILED because one cell (draw 94, gamma = -0.10) changes the decision relative to the baseline. The draft mentions the digest and sigma_gamma but completely omits the determinism, cell counts, min a_lb, and the exact failing cell counterexample. By omitting the actual cause of the failure, the draft softens and hides the FAILED outcome.
REPAIR: Add the exact machine facts (determinism, 0 of 5049 cells inconclusive, min a_lb 0.864, failing cell draw 94 at gamma = -0.10) to the BS-3g rows in §7 and §11 of the draft to truthfully reflect the invariance receipt's failure without softening the outcome.

Checks performed successfully without findings:
- Check 2: `python3 ../../../../../tools/prereg_trace.py --check PREREG_SUCCESSOR_DRAFT_V137_20260903.md .`
Output:
prereg trace check — PREREG_SUCCESSOR_DRAFT_V137_20260903.md
  136 computed transition(s); 0 problem(s)
- Check 3: `shasum -a 256 -c P0_PACKAGE_MANIFEST_20260831.txt` returned OK for all 30 files (no FATAL non-OK).
- Check 4: The preamble correctly names V136 as predecessor, specifies the chat signature mechanism via Blanc relay, signature lines are blanked, and V135/V136 records in §10 are unaltered.
- Check 5: `ref/gain_counterfactual_path.py` and `ref/DRAW_MECHANICS_COMMIT_20260830.md` were confirmed byte-for-byte untouched against the P0 manifest.

SEAT: AGY
VERSION: V137H-REFEREE-V1
VERDICT: NOT-SIGNABLE
COUNT: 1
