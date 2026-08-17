# Decision — stay on DR10.1. DR11 not pursued.

**Duho decided 2026-08-17.** This supersedes `DR11_MIGRATION_DECISION_20260816.md` and closes
`DR11_MIGRATION_HOLD_20260816.md`. Both are retained, not deleted.

## Why

`ls_dr11.photo_z` was initially read as a NOIRLab Astro Data Lab ingestion lag. It is not.
Checked directly at NERSC:

    DR10  south/sweep/   10.0/  10.1/  10.0-extra/  10.1-extra/  10.1-photo-z/  10.1-lightcurves/
    DR11  south/sweep/   11.0/  11.0-extra/  11.0-lightcurves/

`11.0-extra/` holds `-ex.fits` column sweeps, not photo-z. **DR11 photo-z does not exist anywhere
yet** — not in Data Lab, not as sweep products. The Legacy Surveys team has not produced it.

So the wait is not a deployment queue measured in weeks; it is an unproduced data product with no
published schedule. Cut 3 (`0 <= z_phot_median < 0.15`) removes 99.2% of the sample and cannot be
applied without it.

## The workaround that was considered and rejected

Positionally cross-matching DR11 `tractor_s` to DR10 `photo_z` is **self-defeating, not merely
imperfect**. DR10 photo-z covers only DR10's footprint, so the match yields redshifts exactly where
they already existed and none in the new sky. The entire case for DR11 was +48% area
(15,342 → 22,731 deg²). A cross-match gains zero galaxies while adding match ambiguity — strictly
worse than staying on DR10.1.

Computing photo-z independently was also rejected: a new estimator with its own systematics inside
a preregistered measurement is a research project requiring its own validation and gate, not a
workaround.

## What this buys

**The frozen preregistration stands unchanged.** No successor prereg, no re-freeze, no
re-derivation of the parent set, the 208,407 count, the feasibility chain, or the BRICKID keyspace.
Everything frozen was frozen against DR10.1.

`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` (`b06901c8a0f3a057`, mode 444) remains
operative and requires no amendment.

## What this costs, stated plainly

The +48% area is forgone. **Treat this as a commitment rather than a deferral.** K-8 bars a
parameter change after a real-sky statistic has been computed, so once the run begins, switching to
DR11 would void it. Revisiting is only clean while no statistic exists — which is true today and
will not be true later.

If DR11 photo-z is published *before* the run starts, reopening is legitimate and would be a fresh
decision under the same integrity condition recorded in `DR11_MIGRATION_DECISION_20260816.md`:
outcome-independent reasons only, frozen cuts carried verbatim.

## What is still open on DR10.1

1. **R3 — per-brick checksum freshness.** Unresolved. The Nov-2022 bulk pass predates the Sept-2023
   in-place replacements by ten months; the top-level `.sha256sum` refreshed Dec 2023 is a
   counter-signal. Blocks manifest approval per
   `MANIFEST_GATE_REQUIREMENTS_20260816.md`.
2. **Route selection.** Route A (Globus/NERSC DTN) requires a linked `nersc.gov` identity — measured,
   not assumed. Route B (public HTTPS) is viable but currently forbidden by the frozen route
   binding, so it needs a successor binding and a new freeze (memo §6). Note the asymmetry: **route
   A needs no amendment at all**, so obtaining NERSC access remains the cheapest path in process
   terms even though it is the harder one administratively.
3. R1 (margin-brick r-band coverage) and R2 (absent-by-coverage vs missing-unexpectedly), unchanged.

## Unaffected

Every gate stands. All eight are release-independent — they test code and synthetic geometry, not a
data release. The adapter remains byte-identical at `267b2a93` through seven of them.

## Boundary

Directory listings only. Zero data bytes fetched, no endpoint activated, no transfer, no count
computed. K-8 untripped.
