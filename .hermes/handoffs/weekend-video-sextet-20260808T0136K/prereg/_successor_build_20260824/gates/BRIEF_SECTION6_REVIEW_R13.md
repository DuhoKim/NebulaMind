# REFEREE BRIEF — §6 thirteenth pass. The calibration halt moved to where it binds.

Subject: **`SECTION6_DRAFT_AGY_R13.md`**. Its sha256 is pinned in `runner_s6r13_round.log` after the
drafting seat exited, confirmed stable across two reads. **Verify the file you open matches it and
record the result.**

## Where the round stands

**GPT56 returned CLEAR on R12** — no blocking finding, the first clear verdict on §6 in twelve
rounds. **CODEX returned NOT CLEAR with one blocking finding, and it has been treated as blocking.**
A freeze cannot rest on whichever seat was more lenient.

CODEX was right. R12 placed the `a_LB_b < 0.85` decision at P8, after unblinding, while V15 lines
566–567 require `INCONCLUSIVE-BY-CALIBRATION` and a **pre-unblinding halt** — with the deciding
aggregate already present in BS-8f at P4. As written, BS-5f, BS-L and unblinding itself could proceed
past a frozen calibration failure that should have stopped the run before anyone looked.

## What R13 changes

1. **`a_LB_b < 0.85` is evaluated after BS-8f and before BS-L**, emitting
   `INCONCLUSIVE-BY-CALIBRATION` and halting, pre-unblinding. The draft states which row or gate owns
   it.
2. **`verify_lock()` binds the complementary calibration PASS.**
3. **Row P's low-bound branch is removed** (or reduced to binding the already-verified PASS), while
   **Row P's distinct post-unblinding removal/applicability branch is kept** — those are different
   things and must stay different.
4. **Part 5 item 16's citation is corrected.** It credited lines 1275–1276 with a count guarantee;
   those lines implement `if refuted or nonconservative: return succ, False, audit`, and the
   count-dependent `None` return is line 1277. The no-deviation rule comes from Row J.

Everything GPT56 credited in R12 stays: the Row J protocol seating before Stage-C execution and BS-5f
issuance, the binding into BS-5f, the exhausted PASS/FAIL partition, no Stage-C FAIL branch in Row P.

## What to judge

1. **Verify the digest first**, record it, and treat a mismatch as outranking content.
2. **Does the calibration decision now actually execute before BS-L?** Not merely described as
   earlier — check the phase ordering, that the deciding aggregate exists when it runs, and that
   `verify_lock()` genuinely cannot pass without the calibration PASS bound.
3. **Clause 10 in both directions.** Moving a decision earlier can orphan what depended on it later,
   exactly as R11's deletion orphaned the VOID branch and R12's late placement broke the halt. This
   test has caught something in five consecutive rounds. Assume it will again.
4. **Did removing Row P's low-bound branch damage the post-unblinding applicability branch?** They
   were adjacent; confirm the surviving one is intact and still reachable.
5. **Check the corrected citation against lines 1275–1277 yourself.** A repair to a citation can be
   wrong in the same way the original was.
6. **The three-part threshold test, applied everywhere.** CODEX's finding named it: a threshold has a
   value, a phase it binds at, and a failure effect. R8 fabricated a value; R12 carried a value
   without its phase or effect. **Sweep every threshold in the draft for all three parts, not just
   the number.** No numeric sweep would have caught R12's defect, and four clean numeric sweeps did
   not.

## Not in scope

The attrition-intolerance design question is with the principal. Findings 1, 2, 2b and 3 stay
UNRESOLVED pending BS-2a; BS-2a is REFUSED; rows C2 and E cannot run; BS-6 and the first image byte
stay blocked. Do not accept a draft that weakens the fail-closed calibration rule.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`SECTION6_REVIEW_R13_<YOURSEAT>.md`. Numbered findings with severity, row/clause, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`.

One seat has now cleared this section once. **If it is sound, say so; if it is not, say what is
wrong.** Do not weight your verdict by what the other seat said last round — you are not being asked
to agree, and a split has already proved more useful than a consensus would have been.
