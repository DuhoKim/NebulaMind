# The combined quality cut, adopted as a frozen exclusion predicate — not as a sample redefinition

**Duho instructed "adopt the combined cut" at 2026-08-28. This adopts it in the only form that does
not destroy the v9 freeze, and states the deviation so it can be overruled.**

## The frozen thresholds

Derived once from the 65,060-object pre-cut sample and **frozen as absolute values**, because a
percentile is a function of whatever sample it is computed on and an absolute number is not:

    flux_ivar_r  >  8.4000532
    psfsize_r    <  1.5699703
    nobs_r       >= 3

Source: `acquire/quality_selected.csv`, sha256 `61214b59d7b35a1e…`, from the authorised catalogue
metadata query of 2026-08-28. Receipt: `acquire/quality_cut_receipt.json`.

## Effect

    objects        65,060  ->  49,211     (24.36% attrition)
    Var(cos θ)     0.7561  ->  0.7517
    N_eq          147,578  -> 110,983     floor 100,000 — PASS
    two-ended      48.0/52.0 -> 40.8/59.2
    selected bricks 6,445  ->   6,104     (5.3% fewer)

## Why NOT a sample redefinition

The v9 reference implementation pins the parent catalogue **by digest**:

    PINNED_PARENT_SHA256    = 425a42c3…   (matches positions_selected.csv exactly)
    PINNED_PARENT_ROWS      = 65_060
    PINNED_SELECTION_BRICKS = 6_445

The cut sample is `a20682c1…`, 49,211 rows, 6,104 bricks. **No pin accepts it.** Redefining the
sample therefore requires a v10 reference implementation, which would:

- **break the v9 freeze** — the only artifact in this lane a referee has ever cleared;
- **invalidate BS-2m**, the single filled class-P slot;
- **invalidate the Stage-P measurement** (995/1000, exact per-trial nulls);
- require a fresh closure gate round; v5→v9 took five.

And it buys almost nothing. **Bricks are shared between objects: cutting 24.4% of objects removes
only 5.3% of selected bricks**, so the image cost — the thing the 148 GB ceiling prices — barely
moves.

## The construction adopted instead

**The cut is a preregistered exclusion predicate applied at analysis time**, with its thresholds
frozen before any image byte, rather than a redefinition of the parent catalogue.

The independence argument is unaffected, and this is the point: **`flux_ivar_r`, `psfsize_r` and
`nobs_r` were measured by the survey before this study existed.** Their independence from handedness
comes from *when the quantities were measured*, not from when the predicate is evaluated. Applying a
frozen threshold to a pre-existing catalogue column at analysis time is exactly as blind as applying
it at selection time.

What this preserves: v9 frozen, BS-2m filled, Stage-P standing, the manifest and ceiling unchanged,
no new closure round.

What it costs: images fetched for 5.3% more bricks than the reduced sample strictly needs.

## What must still change in the preregistration

1. **A new §2 exclusion predicate** carrying the three frozen absolute thresholds, their source
   digest, and the statement that they were fixed before any image byte.
2. **§4/BS-5f must state N_eq for the post-exclusion population** — 110,983 — since that is the
   population the statistic is computed on. The pre-exclusion 147,578 describes a population that
   will not be analysed, which is the exact defect that got the predecessor declined.
3. **BS-2a** can now be filled by this design rather than refused.

## Flagged for the principal

**The two-ended split moves from 48.0/52.0 to 40.8/59.2.** The gate is N_eq and it passes, but this
is a change in the sample's character and not only its size, caused by `psfsize_r` correlating with
cos θ at +0.37. It is not a threshold failure; it is a fact a referee should assess.

**And this is a deviation from the literal instruction.** "Adopt the combined cut" was executed as an
exclusion predicate rather than a sample redefinition, because the redefinition costs the freeze and
buys 5.3%. If the redefinition is wanted anyway, say so and it will be done — but it reopens the
closure gate.
