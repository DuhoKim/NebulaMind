# Mirror test — design. The blinding question has a proof, not an argument.

**Duho's instruction, relayed 2026-08-28: go with the mirror test.** Design below; three questions
Blanc raised, and the one thing not to build on.

## Q1 — whose classifications. ANSWERED: automated.

`BS-3` is **instrument identity: weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity**,
and the frozen `SLOT_SCHEMA` at `successor_ref_v9.py:198` already reads:

    "BS-3": ("weights_sha256", "tau", "antisymmetry_receipt")

**The classifier is an automated weighted instrument, not volunteers.** It can be re-run on mirrored
input reproducibly and cheaply, and **the receipt already has a home in the frozen schema** — BS-3's
third field, currently unfilled. The mirror test needs no new slot.

## Q3 — is it permitted pre-unblinding. ANSWERED BY CONSTRUCTION.

Blanc: *"it reads them to characterise the classifier rather than to estimate the signal, which seems
different in kind — but that is a freeze question."* Right to flag it, and "different in kind" is too
weak to gate on. Here is the stronger statement.

Define, per object, with `M` the mirror operation:

    d(g) = χ(g) + χ(Mg)

For a perfectly antisymmetric instrument `χ(Mg) = −χ(g)`, so `d = 0`. **Any departure from zero is
instrument bias, measured directly.**

And `d` is **mirror-invariant by construction**:

    d(Mg) = χ(Mg) + χ(MMg) = χ(Mg) + χ(g) = d(g)

**`d` is parity-EVEN. The dipole is parity-ODD. A parity-even statistic cannot carry a parity-odd
signal.** So `⟨d⟩` — including stratified by position — is structurally incapable of leaking the
result, whatever the labels underneath it say.

That is a proof about the statistic, not a policy about intent, and it is the form a freeze gate can
accept. **It still needs an explicit ruling** — the instrument outputs are χ-bearing under V29 §6.1
scope, and a producer computing `d` touches them even though what it emits cannot carry the signal.
The clean construction is a **sealed-side producer that emits only `⟨d⟩` per bin and the count**, with
per-object χ never leaving the store. That is Row D's shape, not a new actor.

## Q2 — a global amplitude is insufficient. AGREED, and the design requires stratification.

Blanc is right that "the classifier prefers S over Z by x%" does not settle position dependence.
**Stratify `⟨d⟩` in `cos θ` bins**, the same 8 equal-count bins the parity test used, and report per
bin with its standard error.

**And there is a cheaper, stronger version.** Instrument bias is a property of *image quality*, not of
sky position — position dependence is **induced** through the seeing/position correlation we measured,
`corr(psfsize_r, cos θ) = +0.3659`. So:

1. measure `⟨d⟩` as a function of **`psfsize_r`** (and `flux_ivar_r`), which needs images but **not
   this study's footprint** — any comparable DR10 cutouts will do;
2. propagate through the **known, already-measured** `psfsize_r`–`cos θ` relation to predict
   `⟨d⟩(cos θ)`.

This decouples the instrument characterisation from the sealed sample entirely, and it makes the
prediction falsifiable against step 1's direct stratification when images are available.

## The blocker, stated

**The mirror test needs cutouts, and BS-6 — the first image byte — is blocked.** Nothing here can run
today. What can be done now is exactly what has been done: fix the design, prove the blinding
property, and identify that BS-3's `antisymmetry_receipt` is its home.

**The seeing-stratified variant above is the one that could run first**, on non-sample images, without
BS-6 — if the gate accepts that characterising the instrument on unrelated cutouts is not a study
fetch. That is a question for the principal, not an assumption for me.

## NOT to be built on — flagged at Blanc's instruction

Blanc's recollection that **Galaxy Zoo ran mirrored-subset experiments on GZ1 and found a real
handedness bias** would supply a published amplitude instead of a commissioned measurement. **Blanc
has not verified it against any paper and explicitly asked that it be treated as a lead.**

**It is recorded here as unverified and nothing in this design depends on it.** Today alone this lane
corrected a falsification condition, a tier, and a limb assignment, each because the record said
something the source did not. If the published amplitude is wanted, it needs a citation checked
against the paper — and even then it would be a comparison, not a substitute: **a GZ1 bias measured on
GZ1 images with GZ1 volunteers does not characterise this instrument.**

## What this changes

Nothing frozen. No threshold, no receipt, no slot. It fills in the method behind BS-3's existing
`antisymmetry_receipt` field and establishes that the test is blind by construction rather than by
permission.
