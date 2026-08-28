# The BS-2a refusal rests on an uncomputed claim. Here is the computation.

`BS2A_DESIGN_V2.md` concludes: *"There is no admissible upstream quantity that protects power without
destroying the frozen sample… we have no guarantee that the specific leverage geometry — Var(cosθ) =
0.756 — survives the cut."*

**"No guarantee" is not a finding. Whether the geometry survives attrition is computable from
`acquire/positions_selected.csv`, which holds RA and Dec for all 65,060 objects.** It was not
computed. This is the describe-versus-compute law applied to a refusal.

## Method

Longo axis (l,b) = (52, 68.5) from `ref/successor_ref_v9.py` line 71, converted to equatorial
(RA 216.98°, Dec +32.06°). Unit vectors from catalogue RA/Dec; cosθ = û · axis.

## Result 1 — the baseline reproduces the frozen value

    Var(cos θ) = 0.7561        frozen record: 0.756
    mean cos θ = −0.0165       two-ended split: 48.0% / 52.0%

An independent recomputation of the number the successor exists to obtain.

## Result 2 — random attrition does not move it

40 random subsets per row:

    keep 95%   Var = 0.7561 ± 0.0002
    keep 90%   Var = 0.7561 ± 0.0003
    keep 80%   Var = 0.7561 ± 0.0003
    keep 70%   Var = 0.7560 ± 0.0005
    keep 50%   Var = 0.7562 ± 0.0008
    keep 30%   Var = 0.7560 ± 0.0011

**Var is a property of the distribution's shape, not its size.** Removing half the sample leaves it
unchanged to four decimals, against a threshold of **0.15**.

## Result 3 — even a maximally hostile cut leaves large margin

Dropping the objects with the most extreme |cos θ| is the worst possible correlation between a cut
and position along the tested axis:

    drop 10% most extreme   Var = 0.7291
    drop 20% most extreme   Var = 0.6970
    drop 30% most extreme   Var = 0.6623

**The adversarial worst case at 30% attrition still leaves Var = 0.662 — 4.4× the 0.15 threshold.**

## What this means for BS-2a

**The stated obstacle does not exist.** An upstream quality cut on `flux_ivar_r`, `psfsize_r` or
`nobs_r` — all three confirmed present in the DR10 tractor schema at
`_tori_parent_row_count_evidence/schema_result.csv` — threatens the leverage geometry only if it is
strongly correlated with position along the Longo axis, and even then not at realistic attrition
rates.

Two claims in the refusal stand and are worth keeping:

1. **BS-2a's original cause is resolved.** With §2.7 reason (d) deleted and reason (c) refused,
   acceptance is integrity-only and excludes nothing on the measured quantity. The refusal has been
   carried forward as a status after its premise was removed.
2. **Any cut changes N and invalidates the closure, geometry and Stage-P receipts.** True, and a real
   cost — but a recomputation cost, not an impossibility.

## What is still not computed, and why

The decisive number — **how much attrition a given `flux_ivar_r` threshold actually causes, and
whether that attrition correlates with cos θ** — requires those columns, which are not in the local
CSV. It needs a **catalogue metadata query**, not an image fetch. Nothing is authorised to fetch, and
the distinction between a metadata query and the 148 GB image ceiling is a decision for the principal.

## The defect in the fixture, separately

`BS2A_DESIGN_V2.md` §3 proposes asserting `metadata(img).flux_ivar_r == metadata(M(img)).flux_ivar_r`.
**That test is vacuous**: catalogue metadata is keyed by object, not derived from pixels, so it is
trivially equal for an image and its mirror regardless of any property of the quantity. It is the
same shape as the vacuous probes the closure suite produced three times — a test that cannot fail.
A real parity fixture must recompute the quantity **from the mirrored pixels**, which is only
meaningful for pixel-derived quantities, not catalogue columns. For catalogue columns the
independence argument is temporal and needs no fixture at all.
