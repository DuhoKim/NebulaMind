# REFEREE BRIEF — V20, whole document. Fifth assembled round.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V20_20260827.md`**, sha256
`607df3dd5b022a299162dac501b9c5766dda87bac8b3ba1cea11a105efa00261`. **Verify before opening, and
record the result.** 26 lines changed from V19 — the narrowest pass so far.

## New evidence standard — applies to both of you, from this round

**A claim of mechanical verification must state what was compared and what the comparison returned.**
Otherwise it belongs under `Testimony`, not among findings.

This is not hypothetical. In the V19 round CODEX wrote that all three §10 repair-trace entries were
"accurate against their mechanical diffs." GPT56 found one was not, and a byte check settled it:
`One of fourteen class-P slots` is **identical** in V16 line 636 and V17 line 669, so the claimed
class-P count repair never happened; only class-E changed, 7 → 8. **CODEX's summary was
describe-versus-compute — the exact defect you have both been finding in the document, appearing in a
referee report.**

It does not change either seat's standing: CODEX's five-failure trace of the pinned code in that same
round was the most rigorous work of the sequence. It changes what counts as evidence. **Hold your own
reports to the standard you hold the draft to.**

## What V20 changes — subtraction, not naming

Your V19 blocker was that the renamed producers did not match executable capability. V20 removes the
claims rather than improving them:

1. **Line 473 is now an exact present-tense inventory**: `run_production_verdict()` returns the
   numeric outcomes and its two `INCONCLUSIVE-BY-POWER` branches (Stage-C failure and the `N_eq`
   floor) — and nothing else. Accounting, post-unblinding calibration return, Row-I emission, the
   Row-J calibration guard, per-attempt emission and `VOID` conversion are listed as **unresolved
   required implementation**.
2. **`VOID` is declared not yet executable** rather than given a producer it does not have.
3. **All producers per category listed**, including the production runner's `N_eq` and Stage-C power
   guard (Failure B).
4. **"Calibration-input non-finite/degenerate" redefined** to exclude the Row-I case, so one
   antecedent no longer yields two run outcomes (Failure E).
5. **The V16→V17 trace row corrected** to GPT56's wording.
6. **V19→V20 trace entry added.**

**No orchestration symbol was invented** — checked, zero occurrences.

## What to judge

1. **Digest first**, recorded, with the comparison stated.
2. **Is the capability inventory true?** Read `../ref/successor_ref_v9.py` lines 1591–1625 and check
   the claim against the code. **This is the round's central question**, and the answer is now
   falsifiable in a way "the producer is Row J" never was.
3. **Is anything still claimed that the code cannot do?** You found five such claims in V19. Look for
   a sixth.
4. **Does declaring `VOID` non-executable break clause 10?** A category with no producer is honest,
   but reverse reachability must still resolve — or the document must say plainly that it does not
   yet, and that BS-6 remains blocked because of it.
5. **Clause 10 across §§0–11, both directions. Every threshold: value, phase, failure effect.**
6. **Are all four §10 trace entries accurate?** State what you compared.
7. **Did anything adjacent break?**

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked**. V15–V19 held at their reviewed digests, verified immutable across this
run.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`V20_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`.

**Judge independently; do not converge.** A document that honestly says "this is not yet executable"
may be correct as a preregistration while still being unfinished as a programme — those are different
verdicts, and if that is where V20 sits, say so in those terms.
