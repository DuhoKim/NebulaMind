# Lana — scientific audit of the var(cos θ) approach (BS-1 blocker)

**Lana (science / claim-boundary seat), 2026-08-14.** Audit on paper, per Hwao; nothing here runs
against the service. Assigned questions: **(3)** is the brick-centre route the same number, and
**(4)** what is the footprint-adequacy check actually for. Framing checked rather than assumed.

---

## 0. Verdict up front

**The number Kun's BS-1 requires is obtainable today, locally, without the service scheduling a
single further job — because the per-row trigonometry that has failed three times was never
necessary.** cos θ is a function of *position*, and position is quantised by the survey into bricks
whose centres we already have in a frozen static product; only the *counts* live in the object
table, and counts are precisely the query shape that demonstrably succeeds on this service (the
55-partition counting sweep). The object-table COS/SIN query shipped the geometry to the scheduler
when the geometry should have stayed home. Three graded routes below compute the **same statistic**
— with a provable, negligible discretisation error — and differ only in the weights' granularity.
The frozen requirement itself (Q4) is scientifically right and should not be weakened; only its
computation route was wrong. If even a static file download is currently unauthorized, Tier 2 runs
from artifacts we already hold plus one file, and the honest blocker statement narrows to "one
~file-sized GET awaiting authorization" — not "fourteen hours of queue."

## 1. Q4 — what the check is FOR, precisely

The preregistered estimator is D̂(n̂_L) = mean(sign(χᵢ)·cos θᵢ). Its statistical anatomy:

- **Power.** Under a true asymmetry A along n̂_L (sign probability (1 + A·cos θ)/2), E[D̂] =
  A·⟨cos²θ⟩ and Var_null[D̂] = ⟨cos²θ⟩/N, so detection SNR = A·√(N·⟨cos²θ⟩). The quantity that buys
  power is the **second moment** of cos θ over the *analysed population*.
- **Monopole separation.** A global sign offset M leaks into D̂ through ⟨cos θ⟩: E[D̂] ⊃ M·⟨cos θ⟩.
  After orthogonalising the dipole regressor against the monopole (which is what the analysis and
  the permutation null effectively do, since permutations preserve positions), the per-object
  leverage of the dipole is exactly **var(cos θ) = ⟨cos²θ⟩ − ⟨cos θ⟩²**.

So the frozen statistic is the right one, for the right reason: **var(cos θ) is the
monopole-orthogonal leverage of the dipole test**, and since ⟨cos²θ⟩ ≥ var(cos θ), the var ≥ 0.15
requirement is *conservative* for raw power as well (full-sky uniform value: 1/3; the threshold
demands ~45% of that). Answer to Q4's alternative: a footprint-geometry statistic that ignores
where the objects actually are would satisfy neither role exactly — the estimand is over the
analysed population — **but §2 shows the population quantity decomposes onto footprint geometry
plus counts, so the dichotomy in Q4 is false: the object statistic IS a footprint statistic with
weights.** The requirement stands unmodified; ⟨cos θ⟩ should be reported alongside it (it is the
monopole-leakage coefficient and costs nothing extra).

## 2. Q3 — the brick-centre route: same statistic, with a provable error bound

**The decomposition.** By the law of total variance over bricks b with Cut-6 counts n_b and
brick-centre values c_b = cos θ(centre_b):

  Var_objects(cos θ) = Σ(n_b/N)·var_within-b + Var_weighted-centres(c_b)

**The within-brick term is negligible, provably.** A brick is 0.25° × 0.25°; its half-diagonal is
0.177° = 3.09×10⁻³ rad. cos θ is 1-Lipschitz along great-circle angle, so no object in a brick can
differ from its centre value by more than 3.09×10⁻³, giving var_within ≤ (3.09×10⁻³)² ≈
**9.5×10⁻⁶ — five orders of magnitude below the 0.15 threshold.** Hwao's hypothesis is therefore
**not a different statistic**: count-weighted variance over brick centres equals the object
variance to better than 10⁻⁵ absolute. It could only "not satisfy Kun's requirement" if the true
value sat within 10⁻⁵ of 0.15, which is no margin at all by any standard.

**Three tiers, by weight granularity — what each licenses:**

- **Tier 1 — unweighted brick-centre variance (geometry only).** Computable entirely locally from
  the frozen brick-summary product (662,174 rows; a *static file*, not a compute job), restricted
  to the survey footprint. **Licenses:** a footprint-adequacy statement and a strong prior on the
  answer. **Does not license:** BS-1's letter, which is over the selected population — density
  weighting can shift the value, and the shift is not cleanly boundable without counts. Use as
  sanity, not as the receipt.
- **Tier 2 — partition-weighted decomposition (computable from what we already hold).** We hold
  certified per-partition Cut-6 counts (67 numbers) from the counting sweep. Compute, locally:
  within-partition unweighted brick-centre variance + between-partition count-weighted variance,
  by the same total-variance identity at partition level. Residual error = the within-partition
  covariance of density with cos θ — second-order, and boundable by recomputing under extreme
  density tilts within each partition (report the bracket). **Licenses:** the BS-1 number with a
  quantified error bracket. **Rule I attach: if Tier 2's value clears 0.15 with margin ≥ 2× its
  bracket, BS-1 is satisfiable on this route; if it sits inside the bracket of 0.15, escalate to
  Tier 3 — do not argue the margin.**
- **Tier 3 — exact per-brick weights (the letter, no trigonometry shipped).** One aggregation per
  partition of the form `SELECT brick, COUNT(*) ... GROUP BY brick` under the frozen Cut-6
  predicates — **the same no-trig query shape as the sweep that ran 55+ partitions to completion**
  — returning n_b; all geometry then local. Error collapses to the ≤ 10⁻⁵ within-brick term.
  This is the confirmation route when/if the scheduler behaves; it is not needed to unblock if
  Tier 2 clears with margin.

**What none of the tiers licenses:** the accepted-sample (post-classifier) variance — abstention
correlates with depth and could re-tilt weights. BS-1 as stated by Hwao is over the frozen dered
Cut-6 population (832,393), so this is not a BS-1 gap; it is already covered by the prereg's
sensitivity-map machinery (CB-7) downstream. Noted so nobody stretches this receipt later.

## 3. The recommended path, concretely

1. **Authorize one static acquisition** (if not already held in Tori's evidence): the current
   post-Dec-2023 `survey-bricks-dr10-south.fits.gz`, already a frozen bound product with a frozen
   URL. This is a file GET — the operation class that has answered in ~0.5 s throughout — not a
   compute job. Custody: sha-pin on receipt, per standing rules.
2. **Tier 2 locally, same day:** brick centres → cos θ against Longo's axis
   ((RA, Dec) = (216.9844°, +32.0606°), already frozen in Tori's binding); 67 certified counts as
   weights; report var, ⟨cos θ⟩, ⟨cos²θ⟩, the tilt bracket, and the margin rule verdict.
3. **Tier 3 when convenient** as the letter-perfect confirmation — and as a matter of standing
   practice: **never ship trigonometry to the service again.** Fetch counts; compute geometry
   where it is exact, free, and cannot sit PENDING.
4. If even step 1 is blocked, the stated blocker is: *"BS-1 waits on one authorized static file
   download"* — which is a very different sentence from "the service will not run our jobs," and
   Duho should hear it in that form.

## 4. Side-answer to Q1 (one paragraph, since it interacts with the science)

Whether per-row COS/SIN forces a scan class the scheduler deprioritises is a service-internals
question we cannot settle from outside — but the audit renders it moot: the successful sweep and
the failing attempts differ exactly by the trigonometry, and §2 shows the trigonometry never needed
to be in the query. The cheapest formulation that gets the same number is "no formulation": counts
by brick (or the counts we already hold), trig at home. If Goru's policy audit (Q2) finds we are
deprioritised as an account, the same conclusion holds with more force.

## 5. Bottom line for Duho

Three attempts failed because the job asked the service to do geometry it never needed to do. The
statistic Kun froze is the right one and stays; the same number is computable to a provable
10⁻⁵-class accuracy from brick centres plus counts — most of which we already hold — with one
static file download as the only external dependency. A fourth attempt of the old shape is not
warranted under any outcome of this audit.

— Lana, 2026-08-14. Audit on paper; nothing run against the service; no acquisition performed.
