# REFEREE BRIEF — §6 eleventh pass. Custody fixed. Two content repairs. Read the pinned digest.

Subject: **`SECTION6_DRAFT_AGY_R11.md`**. Its sha256 is printed in `runner_s6rev11_round.log`
**after the drafting seat exited** and after the digest was confirmed stable across two reads.
**Verify the file you open matches that digest, and say so in your report.**

## Your first blocker last round was upheld

You both blocked on artifact identity before reviewing content, and you were right. My dispatcher
hashed R10B while the seat was still writing it, so the log pinned `4e36683e` — which is R10's
content, because the seat built R10B by copying R10 and editing in place. The same mistake produced
the log's "changed lines: 0". One fact, stated twice, both times wrong.

Resolution, recorded in `CUSTODY_NOTE_R10B_PIN_MISMATCH_20260827.md`: the two digests are **not** two
drafts; `ef35a8b1` is the R10B of record and nothing is discarded. **Your content findings stand** —
both of you printed the digest you actually opened, and it was the finished artifact.

Dispatcher now: hashes only after the seat exits, requires the digest stable across two reads five
seconds apart, and **aborts on a zero-line diff** as well as an oversized one. A repair pass that
produces an identical file is a failed pass.

## What R11 changes — two repairs only

**1. The unreachable Stage-C power branch is deleted from Row P.** You both showed it cannot be
reached: Row P requires a verified BS-L, `verify_lock()` checks BS-5f's PASS, Row J forbids
continuing after a Stage-C FAIL, and V15 421–425 halts pre-unblinding on FAIL — so Row P can only
inherit a PASS. The `< 962/1,000 → INCONCLUSIVE-BY-POWER` decision is **kept where it executes**, at
pre-unblinding Row J / BS-5f. The adequacy receipt may bind the locked PASS and protocol digest but
must not branch on a FAIL that BS-L excludes.

**2. Part 3 C1 and Part 5 finding 5 are conformed** to the frozen no-rerun rule. C1 no longer claims
the design relies on "recomputing power"; Part 5 no longer says the receipt binds a "re-evaluated
Stage-C result."

**Your R10B power-inapplicability repair was judged substantively correct by both of you and is
unchanged.** So are all R10 repairs, the twenty rows, the ten clauses, and the thresholds.

## What to judge

1. **Verify the digest first** and record it. If it does not match the log, stop and say so — that is
   a finding, and it is the check I most need you to keep making.
2. **Apply clause 10 in both directions.** Every path must reach exactly one stated outcome, and
   every stated outcome must be reachable. That test has caught something in three consecutive
   rounds. Deleting a branch can orphan another.
3. **Is the `< 962` decision now correctly seated at Row J?** Confirm it still exists and executes
   there, and that removing it from Row P did not remove it from the study.
4. **Whole-document consistency on no-rerun.** Row P, Part 2, Part 3 C1, Part 5, R3 must all agree.
5. **Sweep the numbers again.** Three clean sweeps do not retire the class.

## Not in scope

The attrition-intolerance design question is with the principal. Do not accept a draft that weakens
the fail-closed calibration rule to escape it. Findings 1, 2, 2b and 3 stay UNRESOLVED pending BS-2a;
BS-2a is REFUSED; rows C2 and E cannot run; BS-6 and the first image byte stay blocked.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`SECTION6_REVIEW_R11_<YOURSEAT>.md`. Numbered findings with severity, row/clause, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`.

**If §6 is now sound as prose and the remainder is genuinely the BS-2a mechanism, say so plainly.**
Eleven rounds have each been narrower than the last. I would rather have a twelfth finding than a
courtesy pass — but if the section is done, that is the useful answer and I will act on it.
