# REPAIR BRIEF — V26. The independence argument was wrong. Replace it with what is actually true.

Base: `../PREREG_SUCCESSOR_DRAFT_V25_20260827.md`, sha256
`50f2e53256cc79707f2a4dfbf737740e6101742deb39365498737c904aa0f59b`. **Verify before starting.**
Read `V25_WHOLE_REVIEW_GPT56.md` and `V25_WHOLE_REVIEW_CODEX.md` in full first.

**Write `../PREREG_SUCCESSOR_DRAFT_V26_20260827.md`.** Do not edit V25. **Do not touch V15–V24.**

## Blocker 1 (CRITICAL, both seats) — temporal precedence is not independence

**The argument I gave you for V25 was wrong.** I said these columns were measured before the study
existed, therefore independent of handedness, therefore no blindness construction needed. Both seats
refuted it identically. CODEX:

> Chronology establishes only that this study's later instrument output did not cause those earlier
> catalogue values. It does not establish statistical independence, conditional independence, or
> reflection invariance. A pre-existing variable may correlate with a later outcome through sky
> position, galaxy morphology, observing strategy, or measurement difficulty. **The receipt itself
> establishes substantial correlations with the tested axis.**

That last sentence is the sharpest part: `gates/BS2A_QUALITY_CUT_RECEIPT_20260828.md` reports
`corr(psfsize_r, cos θ) = +0.3659`. **The Longo hypothesis is that handedness correlates with position
on that axis** — so a cut on `psfsize_r` may cut on handedness *through position*, which is the
circularity the whole design exists to avoid.

**Repair — write the narrow claim, which is true and useful:** the predicate is **outcome-blind with
respect to this study's unobserved χ** — its columns and absolute thresholds were fixed **without
reading χ and before any image byte**, so it cannot be tuned post hoc. **Delete every claim of
independence from handedness.** Do not infer independence from time order anywhere in the document.

**And state the open question rather than resolving it by assertion:** whether the predicate is
independent of handedness *conditional on position* — the property the dipole estimator actually
needs — is **not established**. Either preregister a check for it, or record it as a **stated
assumption with its risk**. Do not claim it.

## Blocker 2 (CRITICAL, both seats) — the predicate is applied at P8 but its population is claimed at P5

§4 and BS-5f print `N = 49,211` and `N_eq = 110,983` for the **P5** mask, while §2.7 line 382 has Row
P applying the predicate at **P8**, post-unblinding. The document reports a population that does not
exist until three phases later.

**Repair (CODEX's, take it):** define a **distinct closed catalogue-quality exclusion reason** with
authenticated evidence fields, and **apply the frozen predicate before BS-2f** so the **P3 sealed mask
genuinely holds 49,211 rows** while the **65,060-row parent identity stays unchanged**. Update Rows
C2/E/F, the terminal-state vocabulary, BS-2f, and Clause-10 phases and effects to match. **Keep
post-unblinding instrument-confidence handling separate** — it is a different thing at a different
time.

## Blocker 3 (HIGH, CODEX) — Stage-P evidence is from the old population

§2.6 and the adoption chain present the 995/1000 Stage-P result as standing for a geometry that has
changed. **It was computed on 65,060.** Either mark it superseded pending a rerun on the actual
post-quality mask, or state plainly that BS-5p cannot be filled until that rerun exists.

## Blocker 4 (HIGH, both) — BS-2a must NOT be FILLED

The §7 row flipped to `FILLED` and the rest of the document did not follow. CODEX states the rule:
**"A DESIGN slot declared gated as text and code cannot be FILLED while its required code/schema/
digest remains deferred."**

**Repair: walk BS-2a back.** The design exists and is recorded; the code, schema and digest do not.
Mark it **DESIGN, defined, UNFILLED**, and reconcile every status statement and count across the
preamble, fold record, §7 and §11. **One of fifteen class-P slots is filled, not two.** Say so.

## Blocker 5 (HIGH, both) — the findings mapping and its enforcement

`tools/prereg_trace.py` no longer truncates the changed-section list — CODEX found it dropping
sections silently, and it now emits all of them. Two things remain for the document:

- **Define the coverage contract** in prose and checker: predecessor-only in-band, plus an external
  pinned artifact for the current transition, or another non-self-referential design.
- **Populate or explicitly exempt the historical mappings under a stated rule** — V1→V15 currently
  cite nothing.
- **The V24→V25 mapping must cite only findings the delta demonstrably answers.** Check it.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V26_20260827.md`, complete, single write, titled **V26**.

Do not read `/Users/duhokim/NebulaMindData/`. No image byte is authorised.

**Where a claim cannot be supported, write the narrower true one and name what is missing.** That has
been the only move that has worked in this lane.
