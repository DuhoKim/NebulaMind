# STAGE TWO — CLOSED AT ITS DESIGN BOUNDARY

**Ruled by the principal, 2026-09-01, verbatim:**

> bank stage one and leave the image half

Stage two opened this afternoon to preregister the image-analysis design stage
one deliberately left unfilled. It closes today — not because the design failed,
but because a *resource* required by the frozen science does not exist in this
lane, and the honest response is to say so rather than build something that
cannot support its claim.

## Why it closes: the calibration cannot be obtained

The frozen estimator is `Â_L = β̂/(2â−1)`. The `â` is **how often a human labels
spiral handedness correctly on real objects drawn properly from the accepted
population** — it is not optional, not substitutable by machine output, and not
obtainable from known-answer synthetics alone (those estimate `ε`, the error
term that *corrects* the measurement). Every route to it was costed and closed:

| route | outcome | why |
|---|---|---|
| **One independent checker** (850 presentations, principal audits 30–50) | unavailable | no such person available to this lane |
| **Distributed panel** (nobody over ~50 decisions) | **INFEASIBLE** | 3-person majority ⇒ 1,860 decisions at the floor budget ⇒ **38 people minimum**, 51 at the inherited budget — converts one unavailable checker into 38 |
| **External labels (Galaxy Zoo)** | **NOT USABLE** | modern releases publish winding *tightness*, not *direction*; GZ1 is the only chirality release and lacks coverage of DR10.1-south, has no known-answer controls for `ε`, and its screen-relative sign has no publishable anchor to our East-of-North convention; the 8.67M-row DESI catalogue is model predictions, forbidden inside `a` |
| **Loosening the floors** | **NOT DEFENSIBLE** | the savings *delete population coverage* rather than adding noise: 9 strata × 3 bins force ≥270 real decisions before controls, so 30/50/80/120 budgets survive only by dropping strata and bins; below 120 nothing is publishable, and 120 is a restricted two-stratum upper limit — not the detection claim |

**The principal's own capacity is the binding constraint**, stated plainly by him
("i cannot see hundreads checks, only use me as very limited manner"). A small
number of his checks can legitimately *audit* the protocol; it cannot *calibrate*
the population.

## What stage two produced, preserved for a successor

Nothing here is wasted — a future effort with more hands inherits a designed,
ruled, adversarially-checked image-analysis foundation:

- **R-A (direction #31)** — image access ruled: the **NERSC coadd brick tree**,
  whole tiles pulled, cutouts cut locally, per-brick SHA-256 lists as native
  integrity anchors, ~148 GB accepted for durable self-contained provenance.
- **R-B (directions #33, #36)** — cutout geometry **ratified**: 128×128 px
  (forced by the frozen instrument, not chosen), exact celestial centering at
  `CRPIX 64.5` with no rounding, north-up/east-left with **parity strictly
  preserved** (a wrong-parity Jacobian refuses the cutout), exactly one
  deterministic bilinear reprojection, stitch-neighbours-first retaining the
  7,226 seam-exposed objects. The bilinear low-pass caveat is on the record.
- **R-C (direction #32)** — the **single blind structural probe executed and
  audited SOUND**: brick 0489m442, SHA-256 match, format contract pinned
  (two HDUs, RICE_ONE tile-compressed float32, logical 3600×3600, TAN WCS),
  companions deliberately not fetched. **The boundary held.**
- **R-D (direction #34)** — dual machine + human committees with an independent
  verifier; the *role collision* found in the frozen text (Row G forbids a
  checker holding any other role, while HC-1H names the principal, who holds two
  others) is documented for the successor to resolve.
- **R-E (direction #35)** — stage two would take its own manifest, P0′ signature
  and gate ladder, with the relocated BS-3g sweep under its freeze.

Also preserved: the reconnaissance of both access paths, the panel arithmetic,
the external-label analysis, and the loosening cost table — so no successor
repeats this search.

## What stage one banks as the contribution

Real, measured, and frozen under the principal's ed25519 signature (manifest
`d1be4a3b…`, verified three ways):

- **Stage-P exact power battery**: prefix 984/1000, final re-pass 996/1000 on
  the authenticated 49,211-object mask, every trial against its own
  20,000-permutation null through frozen v9.
- **Instrument antisymmetry**: 1000/1000 bit-exact identity, 1000/1000 byte-exact
  mirror involutions, max residual 0.0.
- **Synthetic absolute-sign anchor**: BATTERY-SIGN PASS, BATTERY-POS
  REPRODUCED-LONGO.
- **Machinery robustness**: 5,049 evaluations (99 draws × 51 γ), zero verdict
  flips, with its honest fixture-scope caveat.
- **The sampling design**: Branch B, the traversal/plan/selection receipts, the
  universe pins, nine banked Class-P candidates.
- **Thirteen pinned tools**, three blind commitments, and the full ruling record.

## Status

**STAGE TWO CLOSED. STAGE ONE IS THE DELIVERABLE.** The image-analysis half
awaits an effort with the human capacity its calibration requires. Nothing was
forced, nothing overstated, and the reason it stops is written down where the
next person will find it.
