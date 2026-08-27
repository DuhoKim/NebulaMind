# REFEREE BRIEF — §6 ninth pass. Both branches terminate. Is anything still open?

Subject: **`SECTION6_DRAFT_AGY_R9C.md`**. Its sha256 is printed by the dispatcher into
`runner_s6rev9c_round.log` at send time; verify the file you read matches it.

## What you found last round, and what happened

Both of you returned NOT CLEAR on R8b and named the same defect in different words: a defined branch
that ends nowhere. GPT56 — Row P emits `INCONCLUSIVE-BY-POWER` on a failed rerun and *then* introduces
a gap with no terminal consequence. CODEX — the "inapplicable" Stage-C branch has no terminal
consequence and invites a forbidden post-unblinding threshold, conflicting with V15 lines 570–573.

**That gap was my instruction, not the seat's invention.** I told the drafter a stated gap was an
acceptable output. CODEX is right that it is not: the branch is reached after unblinding, where the
void rule forbids defining a threshold, so the gap could never lawfully be filled. Candor is not a
terminal state.

Three changes since:

1. **The inapplicable 962/1,000 case now emits `INCONCLUSIVE-BY-POWER` unconditionally**, with the
   text stating the consequence is fixed before any real χ is read and citing V15 570–573 as why.
2. **Non-committee attrition fails closed to `INCONCLUSIVE-BY-CALIBRATION`**, and states the reason:
   the applicability predicate does not exist in the frozen record. The seat named the missing
   quantity rather than composing one.
3. **A new clause 10 — branch termination** — requiring every branch of every row to terminate in
   one stated outcome, and stating why: an unterminated branch is where the meaning gets chosen
   after the data is visible, which is the failure this preregistration exists to prevent. A
   consequence that depends on a judgement made later is not a termination.

## What to judge

**1. Is any branch still open?** Apply clause 10 to the whole table as a test, not just to row P.
Walk every row's consequence column and every predicate in §6 and ask whether each path reaches one
stated outcome with no discretion at the point of use. This is the round's main question, and clause
10 gives you a rule to test the document against — including against itself.

**2. Are the two new terminal consequences the right ones?** `INCONCLUSIVE-BY-POWER` for the
inapplicable criterion, and fail-closed `INCONCLUSIVE-BY-CALIBRATION` for non-committee attrition.
Both were chosen over voiding the run. Say if voiding is the honest state instead.

**3. Does fail-closed-on-missing-predicate have a cost nobody has priced?** If any non-committee
attrition forces `INCONCLUSIVE-BY-CALIBRATION`, and attrition is near-certain at 65,060 objects,
does this study now always terminate inconclusive? If so that is a finding about the design, not the
prose, and I want it named plainly.

**4. Verify the numbers again.** You both confirmed `a_LB_b < 0.85` and 962/1,000 against the pinned
files last round and swept for further composed values. Re-check that nothing drifted, and sweep
again — a fabricated threshold survived one full round undetected two passes ago.

**5. Confirm the diff is confined.** R9→R9b→R9c should show clause 10 being added and then rewritten,
plus the row P consequences, plus metadata. Nothing else should have moved. Say so if it did.

## Standing state

Findings 1, 2, 2b and 3 remain **UNRESOLVED**, pending the BS-2a design artifact — that scope has not
moved and this pass did not attempt it. BS-2a is REFUSED by all three seats; rows C2 and E cannot
run; BS-6 and the first image byte stay blocked.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`SECTION6_REVIEW_R9C_<YOURSEAT>.md`. Numbered findings, severity, row/clause, why it fails, smallest
sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**` or
`**NOT CLEAR**`.

**If §6 is now sound as prose and the remaining work is genuinely the BS-2a mechanism, say so
explicitly.** Nine rounds have each been strictly narrower than the last. I will act on a clear
statement either way, and I would rather have a tenth finding than a courtesy pass.
