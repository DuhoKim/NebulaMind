# REFEREE BRIEF — V16, the whole document. First time either of you has seen it assembled.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V16_20260827.md`**, sha256
`1b9b9486736bf734c8cb4ac8cedf54870fd179587e3e1455273ec4724132a0da`.
**Verify it before you open it, and record the result.**

## Why this round is different

Every review either of you has done tonight judged **§6 in isolation**, against a base document
neither of you had read end to end. Fifteen rounds of that produced a section both of you now largely
credit. **But a folded section's real defects live in the seam, not the section** — and V16 is the
first artifact where the section and the document it changed can be checked against each other.

The conforming edits are no longer a *list*. They are *applied*. Check them as applied.

## What V16 is

V15 with §6 replaced by `SECTION6_DRAFT_AGY_R15.md` (`d2c388a4…`, whose Part 1 is byte-identical to
the R14 §6 body you both credited), plus that section's conforming edits to §2.5, §2.7, §4, §5, §7,
§10 and a new §11 code-side inventory. The fold record is in the banner and at the end of §6.

Since your R15 reports, two things changed:

1. **GPT56's HIGH blocker is closed at document-contract level.** §11 now requires the canonical
   unblinding-receipt schema and its exact authenticated fields — BS-L identity and checkpoint,
   complete extending chain segment, terminal unsealing events, final post-unblinding checkpoint,
   destination, one-use ceremony identity and replay state — bound into the pinned implementation and
   schema digest, with `verify_unblinding_receipt()` required to authenticate exactly those.
   **Implementation remains UNRESOLVED.** *"A verifier name does not define its accepted bytes"* was
   the finding; check whether the bytes are now defined.
2. **CODEX's LOW note** on the stale Part 5 status label does not apply — Parts 3–5 were drafting
   apparatus and were deliberately not carried into the preregistration.

A `prereg_lint.py` finding against V16 turned out to be **a false positive in the linter, not a defect
in the document**: it matched the fold record quoting V15's stale class-P list and reported it as a
live assertion. BS-2f correctly sits in class E. The linter is fixed and V16 lints clean. **Do not
take that on trust — check BS-2f's class yourself.**

## What to judge

**1. The seams, as applied.** For each conforming edit §11 and the fold record claim: find it in the
document and confirm it landed where it belongs and says what it should. §7's counts and DESIGN
inventory; §5's guard surface; §2.5's producer-checksum narrowing; §2.7's exclusion reasons after
reason (c) was refused; §10's repair trace; §4's Stage-C definition against Row J's seating.

**2. Contradiction across the whole document.** §6 now asserts things §2, §4, §5 and §7 must agree
with. Fifteen rounds found the same failure repeatedly — a repair in one place leaving another
asserting the old behaviour. **This is the first round where you can check the whole surface. Assume
there is at least one.**

**3. Clause 10 against the entire document**, both directions, not just §6's table. Every branch
anywhere in V16 must terminate in one stated outcome, and every stated outcome must be reachable.

**4. Every threshold: value, phase, failure effect.** One was fabricated tonight and caught by a
numeric sweep; another carried the right value with the wrong phase and no sweep would have found it.
**Check all three parts for every threshold in the document, not only in §6.**

**5. Is the fold record accurate?** It states what was folded, under whose instruction, at what time,
against what referee state, and what remains open. **Verify each claim.** A record that overstates its
own standing is worse than no record.

**6. Does the document overclaim?** It is a preregistration with most class-P slots unfilled, BS-2a
refused, and the first image byte blocked. Does it read as more finished than it is?

## Standing state — carried, not closed

Findings 1, 2, 2b and 3 **UNRESOLVED** pending the refused BS-2a design. **BS-2a REFUSED by all three
seats.** Rows C2 and E cannot run. **BS-6 and the first image byte remain blocked.** `verify_lock()`
and the unblinding-receipt schema are required work, **not implemented**. Any single post-unblinding
removal emits `INCONCLUSIVE-BY-CALIBRATION`; no attrition rate exists in the frozen record.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`V16_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`.

You have split on every round tonight and the split has been worth more than agreement each time —
one of you cleared §6 twice while the other found a defect that would have let a run be unblinded
after a mandatory halt. **Judge independently. Do not converge.**
