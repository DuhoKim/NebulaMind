# DESIGN BRIEF — BS-2a, second attempt. Independence can be temporal instead of argued.

BS-2a has been REFUSED by all three seats since 2026-08-27. The reason has never changed: the only
confidence quantity in the frozen record is `abs(χ_net)`, frozen at
`YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md` line 82 as *"Accept object x iff |χ_net(x)| > τ"* —
and that quantity **is** handedness amplitude, so the inherited acceptance rule selects on the
measured effect. Mirror-evenness was tried as a screening criterion and failed, because `abs(χ_net)`
is itself mirror-even.

**This brief exists because the frozen record already contains a working solution to the same
problem, applied at a different time, and nobody has noticed.**

## The observation

`acquire/positions_query.adql` — the ADQL that selected the 65,060-object sample — filters on:

    brick_primary = 1
    maskbits = 0
    type <> 'PSF'
    flux_r > 0
    z_phot_median in [0, 0.15)
    dered_mag_r < 17.7
    shape_r > 1.5
    shape_e1^2 + shape_e2^2 < 0.1836734693877551

**Every one of these is a quality cut. Every one is classifier-independent. Every one is
parity-even.** And note `shape_e1^2 + shape_e2^2` rather than `shape_e2` alone: under the mirror
operation that flips handedness, `shape_e1` is invariant while **`shape_e2` changes sign**, so the
sum of squares is parity-invariant where the raw component is not. Whoever wrote that line already
solved the problem this brief is about.

**The independence is not argued. It is temporal.** These cuts were evaluated before any cutout
existed. A quantity computed before the image exists cannot depend on the image's handedness, and no
capability allowlist, hermetic worker or blindness fixture is needed to establish it.

## The question to answer

**Can the study's quality filtering be moved entirely upstream — to catalogue quantities evaluated
before the first image byte — leaving post-cutout acceptance integrity-only?**

If yes, BS-2a becomes fillable: the acceptance rule stops touching handedness because it stops
touching the classifier's output at all.

## What you must establish

**1. Does acceptance still need a post-cutout quality cut at all?** §2.7's reason (d) and its
confidence threshold have been deleted from the current draft; reason (c) is refused. If the
surviving predicates are integrity-only — cutout present, correct frozen tensor shape — then
acceptance already excludes nothing on the measured quantity. **Say plainly whether BS-2a is still
refused, or whether the deletions resolved it.** That is a real possible answer and nobody has asked
it since reason (d) was removed.

**2. If integrity-only acceptance costs power, what upstream cut recovers it?** This is the honest
risk: a cutout can be present, correctly shaped and finite while being unmeasurable — low
signal-to-noise, poor seeing, few exposures, heavily blended. Accepting such objects does not bias
the sign; it **dilutes accuracy `a`, and BS-5f's power depends on `a`.** Name candidate DR10 tractor
columns — for example `flux_ivar_r` (signal-to-noise), `psfsize_r` (seeing), `nobs_r` (exposures),
`fracflux_r`, `fracmasked_r`, `fracin_r`. **Verify each exists in the DR10 tractor schema before
relying on it; do not assume from my list.**

**3. Prove parity-evenness by computation, not assertion.** For every candidate quantity, state the
mirror operation and show the quantity is invariant under it. Where a component is not invariant —
`shape_e2` is the worked example — state the invariant combination instead. **Specify a fixture: the
quantity computed on a cutout and on its mirror must be equal**, which a gate can run and fail.

**4. Price the cost honestly.** The sample is frozen at 65,060 objects with `plan_digest aaeaa9f3…`,
and the closure, geometry and Stage-P power receipts were all computed on that population. **Any
additional filter changes N and invalidates those receipts.** State what would have to be recomputed,
and whether the leverage geometry — Var(cosθ)=0.756, the two-ended distribution the successor exists
to obtain — survives the cut. **If a proposed cut destroys the geometry that justifies the successor,
it is not a solution and you must say so.**

**5. Say if the answer is no.** If no admissible upstream quantity protects power without destroying
the sample, **say that plainly.** This lane has repeatedly found that a stated impossibility is a
result: BS-2a refused rather than composed, reason (c) refused rather than invented, a missing
threshold declared missing rather than fabricated. **A fifth refusal, argued from the data, is more
useful than a sixth design that a referee will find circular.**

## Deliverable

`BS2A_DESIGN_V2.md` in this directory: the finding for each of 1–5; the proposed acceptance rule if
one exists, or the argued refusal if not; the parity fixture specification; and the recomputation
cost. Cite every column and every frozen value by file and line.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. **Nothing is
authorised to fetch** — this is design against the catalogue schema and the frozen receipts, not
against data.
