# DECLARATION — the run is VOID on a disclosed design defect

Hwao, 2026-08-21 18:31 KST. **Draft. Not effective until gated and accepted by Duho.** Supersedes
`DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md`, which was **REFUTED** and is retained
byte-for-byte as `..._REFUTED.md`.

## What this document is, and is not

It is **not** a preregistered outcome. It does not claim INCONCLUSIVE-BY-POWER, INCONCLUSIVE,
REPRODUCED-LONGO, or REJECTED-AT-LONGO-AMPLITUDE. It does not claim that section 5's gate was
executed or that it failed.

It says one thing: **the frozen design cannot certify the property its power gate exists to
certify, we established that from geometry alone, and we are therefore not proceeding.**

## Why the previous attempt was wrong, in its own words

`GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md` refuted the earlier declaration on three
independent grounds, all correct:

1. **It failed a different gate than HC-6 froze.** HC-6 names the pinned harness and
   *"the same analytical method"* — uniform-sphere, two-sided. The declaration substituted
   accepted-position geometry, an SSE bound, and a one-sided critical value. Better science; not
   the frozen operation.
2. **Refusing the literal reading after discovering it can PASS is post-freeze discretion** —
   exactly what preregistration removes. The gate's disposal of my defence is the part worth
   preserving: *preregistration discipline does not contain a "conservative outcome" exception,*
   and a biased actor might equally prefer to avoid a costly or disconfirming run. **Direction of
   choice is irrelevant to whether the frozen procedure was followed.**
3. **"No run" contradicted letting acquisition continue through real-sky chi.** That was an
   internal contradiction, and mine.

This document takes none of those three steps. It makes no claim on the frozen decision regions,
so it needs no reading of HC-6 at all.

## The defect, stated

The frozen power gate evaluates a uniform-sphere calculation (`spike/sim_power.py`:
`costheta = np.random.uniform(-1, 1, N)`, `mean(cos^2) = 1/3`) and never inspects the footprint
it is certifying. The measured parent — 208,407 dered Cut-5 rows, BRICKID 1..121000 — has
`Var(cos theta) = 0.057985` about Longo's frozen axis, against a full-sky `1/3`.

Consequently the frozen gate **can report PASS on a footprint with 5.7486 times less leverage than
the sphere it assumes.** A gate that cannot fail for the reason it exists is not a gate. That is a
defect in the frozen design, discovered after freezing, and no reading of the text repairs it —
which is precisely why this is a void and not an outcome.

Supporting, twice-gated and never refuted: `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md`
(Revision 3; Revisions 1 and 2 retained). Both gates returned HOLD, not PASS, and Revision 3's
current bytes have not themselves been gated — stated here because the refuted draft wrongly
claimed they had.

## Custody, demonstrated rather than asserted

`CHI_CUSTODY_RECEIPT_20260821.md`: no aggregate, tertile, or summary over real-sky chi exists as
an artifact, and no code path computes one. Exactly one individual chi value is public, by
design, as a provenance card. The blind, as
`K8_CROSSING_AUTHORIZATION_20260820.md` condition 1 defines it, is intact. The receipt states its
own limits, including that it is a snapshot and cannot prove nobody read values on screen.

## What is NOT claimed

- **Nothing about Longo.** Void is not rejection. An instrument that could not reach the
  preregistered power cannot reject the amplitude it could not detect.
- **Nothing about the sky.** The canonical boundary sentence stands.
- **Nothing about black-hole-universe cosmology**, in either direction. Duho's 2026-08-21
  confirmation places this lane inside the BHU programme as scope and motivation; it does not
  license an inference from any outcome here to any BHU model.
- **Not a fault of the instrument's mechanics.** The classifier weights, tau, the bit-exact
  antisymmetry receipts, the committee, and the hand-check harness are untouched by this evidence.
  But — correcting the refuted draft's over-claim — **the statistical estimator and power protocol
  ARE impeached**: F-1's `3 * D_hat` does not transfer to this footprint, F-4 and F-7 inherit the
  same `1/3`, and `sim_power.py` is two-sided where F-3 is one-sided. The defect is the
  mismatch between footprint and frozen statistical machinery, not the footprint alone.

## What continues, and why this is consistent

Acquisition continues to completion. **This creates no contradiction, because this document
declares no preregistered outcome and therefore triggers no "no run" clause.** The run is void;
finishing the acquisition simply preserves a complete, verified, receipted sample that a successor
can use without re-fetching 0.7 TB. The verdict estimator is still built and hash-frozen per
`VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md`, and will not be run on real chi under this
preregistration.

Successor design: `SUCCESSOR_SCOPE_20260821.md`.

## The cause, recorded

The parent was fixed by a stopping rule that took contiguous BRICKIDs until 200,000 galaxies
accumulated. Legacy brick IDs run south-to-north, so a contiguous prefix is a polar cap by
construction. The figure of merit for a fixed-axis dipole test is `N * Var(cos theta)`; the rule
maximised `N` while structurally minimising `Var(cos theta)`.

*(Two ancillary claims the refuting gate placed on HOLD as unestablished by its assigned inputs —
the 0.7 TB figure and the "worst available geometry" characterisation — are not relied on here.
The stopping-rule causation above is stated as this lane's own reading of
`TORI_PARENT_ROW_COUNT_20260812.md`, and a gate is free to reject it without disturbing anything
else in this document.)*

## What this requires from Duho

Voiding a frozen preregistration is not a step any seat may take alone. This document requests
that decision; it does not make it.
