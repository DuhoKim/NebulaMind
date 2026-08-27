# REFEREE BRIEF — §6 sixth pass. The channel was closed by removal. Test whether it stayed closed.

Subject: **`SECTION6_DRAFT_AGY_R6B.md`**, sha256
`f9743e836ff791906c94726991a7db43f04ef1a82baaaf4b9e0bea60c2c3d566`.
Author: the agy seat. You are not its author. Do not referee your own text.

## What your R5 reports caused

You both returned NOT CLEAR and converged independently on the C2 checksum. Duho's ruling took your
framing and allowed exactly two routes: **(a)** C2 exports no checksum before the lock, or **(b)**
attempt identity is given a closed form so the channel has provably finite outcome-free content. He
added that if closing it costs a capability the pipeline relies on, the capability goes — *a
narrower row you can prove beats a wider one you have to promise about.*

**R6b took route (a) and paid the price openly.** No checksum is exported. All cutout digests stay
inside the sealed boundary. The projection now carries only enumerated authenticated predicate bits
— `parent_attempt_present`, `byte_integrity_pass`, `canonical_shape_pass` — each meant to be
mechanically recomputable by a separately pinned verifier, with every legal value fixed. Part 3
names the cost: nobody can verify image byte hashes against a public manifest without re-running
the sealed verifier.

**It also refused rather than repaired your second finding.** You both showed a pre-inference writer
cannot report instrument presence or finiteness. R6b did not invent a supervisor to paper over it.
It **dropped §2.7 reason (c)** from the pre-lock structural exclusion predicates entirely and marked
the finding `REPAIR (by REFUSAL)`.

## The three questions this round turns on

**1. Did removing the checksum actually close the channel, or narrow it?** Three bits per object
across 65,060 objects is not zero capacity. Ask what a hostile C2 implementation can still encode:
in the choice of which bit fails, in `canonical_shape_pass` where shape is derived from pixels, in
the ordering or timing of projections, in the stage-completion artifact's contents. The exact-parent
closure rule is meant to kill the missingness channel — verify that it does, and that nothing else
in the row admits an omission, a duplicate, or a caller-chosen value.

**2. Is dropping reason (c) safe, or does it move the problem?** This is the question I most want
answered and the one the draft is thinnest on. If instrument output can be absent or non-finite and
no pre-lock predicate excludes it, what reaches the estimator? Does the accepted mask now contain
objects with no usable measurement? Does BS-5f's power calculation still describe the sample that
will actually be analysed? A refusal that silently relocates the defect into the estimator is worse
than the predicate it removed.

**3. Do the enforcement mechanisms exist or are they still promises?** R6b answers your third
finding with a hermetic worker profile, runtime attestation, row B refusing D until C2's
exact-parent stage-completion artifact verifies, and BS-2a gate fixtures that rerun the real
producer under transformed cutouts and must fail. Judge whether those are specified tightly enough
that a gate could actually fail an implementation, or whether they are the same promise in stronger
words.

## Disclosed defect — do not spend findings on it

**§6.2 and §6.3 are placeholders**, written as parenthetical notes saying "carried unchanged from
R5" rather than as drop-in text. That is a known assembly gap, not a hidden one. The text must be
reconstituted from R5 before any document edit. Report it if you think it hides something; do not
spend a finding establishing that it is incomplete.

Also disclosed: an earlier R6 emptied six clause bodies to bare headings, and R6b restored them from
R5. Clause 5's example changed — R5 named the committee explicitly, R6b names BS-L issuance. The
general rule still covers row G. **Check that the restoration is faithful and that the three
protected properties survive with actual clause bodies**: the universal ban (clause 1), the
committee completing G→H→I without voiding the run (clause 5 plus rows G/H/I), and the BS-5f → BS-L
→ unblinding chain (clause 3).

## Standing constraint

**BS-2a is REFUSED by all three seats.** R6b marks it REFUSED/UNFILLED in its own clause 2 and row
C2, and states rows C2 and E cannot run until BS-2a is redesigned without a handedness quantity. So
the draft describes a pipeline it admits cannot presently execute. Say whether that is the honest
position or whether it makes §6 unreviewable.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch; the 148 GB ceiling is
planning only. No deadline is attached to this round.

## Verdict

Write `SECTION6_REVIEW_R6B_<YOURSEAT>.md` here. Numbered findings, each with severity, the row,
clause or sentence at issue, why it fails, and the smallest sufficient repair. Anything asserted but
not verified against a file goes under `Testimony`. Final line exactly `**CLEAR**` or
`**NOT CLEAR**` with the blocking findings named.

**Renaming a finding counts as refusing it** — and so does emptying a clause. If R6b has narrowed a
channel while calling it closed, say so in those words.
