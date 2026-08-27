# SECTION 6 REVIEW R12 — CODEX

## Verdict

R12 correctly reseats the protocol-deviation `VOID` branch in Row J and completes the locked Stage-C FAIL partition. Clause 10 holds in both directions for that repaired partition. The draft is nevertheless not clear because it moves a frozen, already-computable calibration failure past unblinding, contrary to its cited source and the brief's fail-closed constraint.

## Digest verification

- Pinned digest in `runner_s6r12_round.log` line 5: `6339d940842fecad772034eb942600444afbf495a6da392aff6dec5e21d79dd7`.
- Independently computed before opening the subject: `6339d940842fecad772034eb942600444afbf495a6da392aff6dec5e21d79dd7`.
- Result: **MATCH**.

## Numbered findings

1. **BLOCKING — Row P / Clause 10 / Part 2 item 4 / Part 3 C2: the calibration lower-bound failure is delayed until after unblinding even though the frozen rule requires a pre-unblinding halt.**
   - **Evidence:** Row P places the `a_LB_b < 0.85` decision at P8, after unblinding. The cited frozen source, `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` lines 566–567, says that any `a_LB_b < 0.85` yields `INCONCLUSIVE-BY-CALIBRATION, pre-unblinding halt`. The aggregate needed for that decision already exists in BS-8f at P4. `../ref/successor_ref_v9.py` line 81 independently confirms the numeric floor `A_FLOOR = 0.85`.
   - **Why it fails:** This is not merely a placement preference. The draft permits BS-5f, BS-L, and unblinding to occur after a frozen calibration failure that the governing text says must halt before unblinding. That weakens the fail-closed calibration rule expressly protected by the review brief. It also makes the Part 3 claim that the threshold is “carried from the frozen record” incomplete: the number is carried, but its required phase and stopping effect are not.
   - **Smallest sufficient repair:** Evaluate `a_LB_b < 0.85` immediately after BS-8f and before BS-L (in Row I, Row J before Stage C, or a separately named pre-lock gate), emit `INCONCLUSIVE-BY-CALIBRATION`, and halt. Require BS-L/`verify_lock()` to bind the complementary calibration PASS. Remove the Row P low-bound branch, or state there only that Row P binds the already-verified pre-unblinding calibration PASS; keep Row P's distinct post-unblinding removal/applicability branch.

2. **MINOR — Part 5 item 16 attributes the lawful-trial-count guarantee to the wrong code lines.**
   - **Evidence:** Part 5 item 16 says “the frozen code at lines 1275-1276 admits no lawful state where the count differs without a breach.” Lines 1275–1276 only implement `if refuted or nonconservative: return succ, False, audit`. The count-dependent return is line 1277, which returns `None` when `n_trials != N_TRIALS`. The no-deviation legality rule is supplied by Row J's new pre-run verification, not by lines 1275–1276.
   - **Why it fails:** The normative Row J mechanism is sound, but the repair map misdescribes what the cited code proves. That is a whole-document consistency defect in a passage labelled `REPAIR`.
   - **Smallest sufficient repair:** Attribute the no-deviation rule to Row J, and cite lines 1275–1277 only for the implementation's self-verification/count return partition.

## Clause 10 — both directions over the table

### Every branch reaches exactly one stated outcome

- **Row J, protocol verification:** any `N_TRIALS != 1_000` or frozen implementation/protocol-digest deviation is checked before execution or BS-5f issuance and terminates `VOID` through Row J's void column.
- **Row J, locked execution:** with the protocol verified, FAIL is exactly `(passing trials < 962) OR refuted OR nonconservative`; it emits `INCONCLUSIVE-BY-POWER` and halts. The complement—at least 962 passing trials, no `refuted`, and no `nonconservative`—is PASS and is the sole route to BS-5f → BS-L.
- **Row P:** the exact-parent precedence gives one per-attempt terminal state. Missing, duplicate, extra, and malformed records have distinct unconditional `INCONCLUSIVE-BY-*` refusals. Absence, non-finiteness, or low confidence produces a removal, and the ordered adequacy tree maps any removal to `INCONCLUSIVE-BY-CALIBRATION` without a Stage-C rerun. No-removal then reaches the calibration-accuracy branch. Its outcome is unique, but Finding 1 shows that it is seated in the wrong phase.
- **Remaining table rows:** normal emissions advance along the stated phase line; listed forbidden/deviation conditions terminate through the table's `what voids the run` column or an explicit refusal/halt. I found no additional R12-created orphan or double outcome.

### Every stated outcome is reachable

- `VOID` is reachable through a protocol/digest deviation in Row J and through the table's other enumerated void conditions.
- `INCONCLUSIVE-BY-POWER` is reachable through either fewer than 962 passing trials or a `refuted`/`nonconservative` self-verification result.
- Row P's missing/duplicate/orphan/malformed refusals are each reachable through the corresponding exact-parent join state; its exclusion states are reachable through absent, non-finite, or low-confidence records; `INCONCLUSIVE-BY-CALIBRATION` is reachable through any removal and, as currently written, through `a_LB_b < 0.85`.
- The successful result/disclosure path is reachable through verified protocol, locked Stage-C PASS, verified BS-L, unblinding, an accepted-finite exact-parent partition with no removal, calibration PASS, BS-7f, and BS-V.

## Stage-C source check and numeric sweep

- `../ref/successor_ref_v9.py` line 77: `N_TRIALS = 1_000` — matches Row J and Parts 3/5.
- Line 78: `CP_PASS_X = 962` — matches the stated `< 962` FAIL / `>= 962` PASS partition.
- Lines 1275–1276: any nonempty `refuted` or `nonconservative` result returns `False` regardless of passing-trial count — R12 now includes both in Row J's FAIL branch.
- Line 1277: with the verified trial count, the remaining return is `succ >= CP_PASS_X`; therefore the two named FAIL classes exhaust the locked FAIL space and their complement is PASS.
- Line 81 and V15 lines 566–567: calibration floor is `0.85`; the number matches, but the frozen pre-unblinding timing does not (Finding 1).
- V15 lines 570–573: post-first-real-χ changes to binding rules or thresholds void the run; R12 correctly cites this anti-amendment rule, but it does not cure Finding 1's predeclared timing regression.

## Failed attacks

- I tried to reproduce the R11 orphan by following a protocol/digest deviation: it now terminates `VOID` in Row J before Stage C or BS-5f.
- I tried to find a locked Stage-C FAIL not covered by Row J. Under verified `N_TRIALS = 1_000`, the code leaves none: count failure and self-verification failure exhaust FAIL.
- I tried to route a Stage-C FAIL into Row P. BS-L requires verified BS-5f PASS, so that branch remains unreachable and is correctly absent from Row P.
- I tried to find a new double consequence for missing/duplicate/extra/malformed records. They remain absent from Row P's void column and retain one named refusal each.

## Testimony

- The draft states that BS-2a is `REFUSED / UNFILLED`, that Rows C2 and E cannot run, and that BS-6/the first image byte remain blocked. I did not independently verify external gate state; these assertions remain testimony for this prose review.
- The draft states that the predecessor archive contains 208,405 measurements. I did not inspect `/Users/duhokim/NebulaMindData/` and performed no fetch, as required by the brief; that count remains testimony here.
- I reviewed prose and the named local reference lines. I did not execute Stage C or inspect χ-bearing data.

## Evidence ledger

Content read:
- `BRIEF_SECTION6_REVIEW_R12.md`
- `runner_s6r12_round.log`
- `SECTION6_DRAFT_AGY_R12.md`
- `SECTION6_DRAFT_AGY_R11.md` only through a no-index R11→R12 diff used to isolate the current delta
- `../ref/successor_ref_v9.py` lines 73–92 and 1268–1297, including required lines 1275–1276
- `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` lines 560–579

Checks run:
- `shasum -a 256 SECTION6_DRAFT_AGY_R12.md`
- `git diff --no-index -- SECTION6_DRAFT_AGY_R11.md SECTION6_DRAFT_AGY_R12.md`
- Exact extraction of the full Row P table line for review
- Whole-document outcome-token search for `VOID`, `INCONCLUSIVE`, `PASS`, `FAIL`, `EXCLUDED`, refusal, halt, and blocked paths

No content under `/Users/duhokim/NebulaMindData/` was read, and no network fetch was performed.

**NOT CLEAR**