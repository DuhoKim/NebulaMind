# DR11 PHOTO-Z RE-MEASUREMENT — 2026-08-25 17:16 KST

Requested by Duho via Blanc: re-measure whether the DR11 photo-z product exists now. Same
method and same boundary as `DR11_PHOTOZ_STATUS_POSTK8_20260821.md` — HTTPS directory
listings at NERSC, metadata only, **zero data bytes, no statistic, nothing frozen touched.**

## Result: DR11 photo-z STILL DOES NOT EXIST (measured 2026-08-25 17:16 KST)

Sweep directory listings, verbatim:

    DR10  south/sweep/   10.0/  10.0-extra/  10.0-lightcurves/  10.1/  10.1-extra/
                         10.1-lightcurves/  10.1-photo-z/
    DR11  south/sweep/   11.0/  11.0-extra/  11.0-lightcurves/

DR10 is the positive control: `10.1-photo-z/` is present and is the product Branch B's
predicate 5 joins against, so the method demonstrably detects a photo-z directory when one
exists. DR11's sweep listing has no photo-z entry.

Corroboration, same boundary:

- `dr11/south/` lists: `coadd/`, `dr11-south-depth-summary.fits.gz`, `dr11-south-depth.fits.gz`,
  `external/`, `legacysurvey_dr11_south.sha256sum`, `logs/`, `metrics/`, `randoms/`,
  `survey-bricks-dr11-south.fits.gz`, `sweep/`, `tractor-i/`, `tractor/` — no photo-z.
- `dr11/` top level contains no entry matching "photo".
- `GET dr11/south/sweep/11.0-photo-z/` returns **HTTP 404**.

Unchanged since the 2026-08-24 status line in the V9 draft (§2.1) and since the 2026-08-21
measurement. Rongpu Zhou's product was described by Dustin Lang on 2026-08-19 as "ready in
2 weeks, optimistically by the end of this week"; six days on, it has not been published.

## What this does and does not mean

**Does not resolve BS-1.** The release choice-point resolves by its own frozen rule
(`resolve_branch()`): Branch A only if the photo-z product exists at resolution, Branch B
otherwise, and the rule refuses to close for Branch B before 2026-09-05 precisely so a
late-landing product is not missed. This measurement is an input to that rule, not a
substitute for it. No branch is selected, nothing is frozen.

**Context that changed the stakes.** `real/REAL_GEOMETRY_RESULT_20260825.md` measured Stage P
at **997/1000 on Branch B (DR10) geometry**, so DR11 is now *upside* — more area, the DR10.1
sub-blob fix — rather than a requirement. The study does not depend on it landing.

## Boundary

HTTPS directory listings and one HEAD-equivalent GET returning 404. No catalog rows, no image
bytes, no χ, no statistic, no frozen artifact touched.
