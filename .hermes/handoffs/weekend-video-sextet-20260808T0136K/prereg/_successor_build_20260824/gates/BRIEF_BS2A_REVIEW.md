# REFEREE BRIEF — BS-2a, the acceptance design. Written by a seat, not by me.

`BS2A_DESIGN_DRAFT_GPT.md` (871 lines) proposes the rule deciding **which measured galaxies count
as analysis rows**. A gpt seat wrote it. I have not edited it.

## Why this one matters more than its size suggests

The sample is 65,060 galaxies. Some measurements will fail — a missing cutout, a non-finite
instrument output, a confidence below threshold. The rule that decides which failures are
excluded is exercised **after image inference exists**, and it moves both the signs and the
geometry. Two of you found the original hole independently: the preregistration closed the
*vocabulary* of exclusion reasons without binding the *truth* of one, so a conforming operator
could mark an unwanted object `EXCLUDED / low confidence`, a wanted one `ACCEPTED`, and satisfy
the partition, the closed list and every digest.

**This design must be settled before the first image byte**, because after that every choice in
it is outcome-adjacent. Duho's instruction was to fix it before the images, not alongside them.

## Start here, because you proved it an hour ago

You have just refereed §6 R4 and both found, independently, that its "sign-blind" acceptance
projection is not blind by construction:

- GPT56: *"A field-name prohibition does not stop either field from carrying outcome
  information"* — cutout checksums are χ-bearing verification oracles, and the confidence quantity
  is undefined and written by the outcome-bearing instrument process.
- CODEX: it *"removes named sign fields but is produced after inference by the same process that
  sees the sign and retains several writable per-object channels."*

**That finding lands directly on this draft.** Its §R5 claims a defined confidence quantity and a
single threshold home. Judge it against what you just established: **can the confidence quantity,
as defined here, encode or correlate with handedness?** Can any other per-object field the
acceptance path reads do so? A definition that names a field without constraining what may
produce it repeats the defect one level down.

## What to decide

1. **Is the partition real?** All 65,060 IDs, exactly one terminal status each, no remainder, no
   duplicates — and is the accounting verifiable rather than asserted?
2. **Is every predicate a function of evidence alone**, recomputed rather than replayed from an
   operator's label? Does production refuse a status that disagrees with its evidence, and what
   raises?
3. **Is the confidence quantity defined, and is it incapable of carrying an outcome?** See above.
   This is the question I most want answered.
4. **Does the threshold have exactly one home?** It was previously in two places at once.
5. **Are the exclusion reasons the right closed list**, or does it admit a reason that can see
   handedness, or omit one that must exist?
6. **Would the fixtures actually demonstrate any of this**, or only exercise it?
7. **What does it leave to be decided after images exist?** Anything on that list is a defect,
   because that is the whole point of the slot.

## The rule the drafter was given, and the hazard in it

Findings must be REPAIR — naming the artifact, its fields, its producer, its verifier and what
fails if absent — or REFUSE, with what would have to exist first. Bare "Accepted" was banned.
**The hazard, demonstrated today:** that rule makes nominal repairs harder to write and not
impossible, and CODEX found four in the last §6 draft. **Test the mechanisms, not the labels.**

## Verdict

Write `BS2A_REVIEW_<YOURSEAT>.md` here. Numbered findings, severity, the clause or field at
issue, why it fails as a promise, smallest sufficient repair. Final line exactly `**CLEAR**` or
`**NOT CLEAR**`. Unverified assertions under `Testimony`.
