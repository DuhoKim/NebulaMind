# P8 receipt — the thick-limit test, and what it actually isolated
(2026-08-27. p8_thick_limit.py. The headline verdict the script first printed is WITHDRAWN as
under-resolved; what survives is a precise diagnosis.)

## First: the verdict I did not ship

The script printed **NOT NESTED**, on the strength of runs at opacity multipliers K = 10³ and
10⁴. Before reporting it I checked whether my own grid could resolve those runs. It cannot:

| K | emitting skin depth | grid cells | |
|---|---|---|---|
| 1 | 1.24 | 2370 | resolved |
| 10 | 0.124 | 237 | resolved |
| 100 | 0.0124 | 23.7 | resolved |
| 10³ | 1.24e-3 | **2.37** | UNDER-RESOLVED |
| 10⁴ | 1.24e-4 | **0.24** | UNDER-RESOLVED |

As opacity rises the emission concentrates into a skin just outside the junction; above
K ≈ 100 that skin is thinner than my grid spacing and the integral is sampling noise. **The
NOT-NESTED verdict rested on those two rows and is withdrawn.** The script's own check would
have passed it through — I caught it by asking whether the numbers could be resolved, not by
the check.

## What the RESOLVED runs show

| K | τ at w = 0.08 | null location |
|---|---|---|
| 1 | 0.38 | 0.0408 |
| 10 | 3.8 | 0.0870 |
| 100 | 37.7 | 0.268 |

The null **migrates monotonically upward** with opacity and does not converge toward the seat's
0.0815 — it passes near it at K = 10 (6.7% away) and keeps going. So even within the resolved
range, the two models do not meet.

## The diagnosis — it is the source's EPOCH-variation, not opacity at all

Working out my own thick limit analytically: as K → ∞ the emitting skin collapses onto the
junction, where the depth-redshift is unity, so my emergent temperature tends to the junction
source, which in my construction is the **blackbody value at that epoch**, ∝ ρ̄(η)^(1/4).

Theirs carries the source **adiabatically** from a single normalisation, ∝ ρ̄(η)^(w/(1+w)).

**These agree only at w = 1/3.** Everywhere else they differ, and that — not opacity, not depth,
not the transfer — is why the nulls sit in different places. The models were never going to
nest, and the thick-limit test located the reason rather than settling the question.

## The physics question this leaves, stated for adjudication

Different crossing directions look at the boundary at different epochs. Is the exterior's
temperature at those different epochs:

- **(a)** set locally at each epoch by its own energy density (my blackbody anchoring), or
- **(b)** inherited adiabatically along a shared history (their carried normalisation)?

The adiabatic law governs one fluid element evolving. Different crossing epochs sample the
boundary at different times — but inside the horizon the areal radius IS a time coordinate, so
whether those are "the same element later" or "different elements" is exactly the question, and
I do not think it is settled by anything pinned. **I am not deciding it myself**; it goes to the
gate with both constructions named.

## Status

- Thick-limit nesting: **NOT ANSWERED** (test under-resolved above K = 100; withdrawn).
- Why the nulls differ: **ANSWERED** — competing source-temperature laws across crossing epochs,
  identical only at w = 1/3.
- The null's existence: unaffected, still confirmed in both treatments.
- The null's location: still not quotable, and now for an identified reason.

---

# REPAIR, 2026-08-27 — three reporting defects fixed, and my own resolution bound tightened

REGATE4 required-repair 4. The gate's finding: "exit 1, 1/3 checks. Roots existed only at
K=1,10,100; K>=1000 returned `nan`. The script then mislabeled the last finite K=100 root as
'K=1e5' in its convergence detail." All accepted. Three defects, all now fixed in the script.

**(a) The mislabel.** The convergence line printed `finite[-1]` — the last *finite* root, which
was K=1e2 — under a hard-coded label reading `K=1e5`. Every label now carries the K that
actually produced the number, read from the run.

**(b) Bracket truncation, not an absent root.** The search ran on [0.02, 0.30] while the root
was migrating right: 0.0408 → 0.0870 → 0.2681. At K=1e3 the root sits at **w = 0.4777**,
outside the old bracket, and was reported as `nan` — that is, as an absence. It is not an
absence. The bracket is widened. (At K=1e4 and 1e5 there is genuinely no sign change anywhere
in (0.02, 0.99) — but see (c) before treating that as physics.)

**(c) Silent under-resolution, now a computed gate.** This receipt already withdrew the
NOT-NESTED verdict as under-resolved, on a skin-depth-versus-grid-spacing argument that put the
limit at K ≈ 100. **That bound was too generous and I am tightening it against myself.** The
correct criterion is that the grid resolve the τ~1 layer, max per-cell Δτ ≤ 1 — and it must be
evaluated where the root-finder actually *evaluates*, which includes the low-w floor of its own
bracket, not a mid-band probe:

| w | K_MAX (largest resolved multiplier) |
|---|---|
| **0.02 (the search floor)** | **18.42** |
| 0.05 | 111.5 |
| 0.08 | 282.4 |
| 0.2456 | 2935 |
| 0.95 | 5704 |

Gating at w=0.08 would have admitted K=1e2, whose bracket runs down to w=0.02 where this grid
resolves only K ≤ 18.4 — brentq would be reading grid noise at its own left endpoint. **So the
K=100 row, which this receipt previously listed as resolved and which REGATE4 quoted as the
last finite root, is withdrawn too.** Only K=1 and K=10 survive.

Corroboration that the unresolved rows are noise and not physics: the coefficient flips sign
discontinuously across the whole w range between K=1e3 (+0.259 at w=0.03) and K=1e4 (−1.526 at
the same w). That is a grid artefact, not a transition.

**What the script now reports.** Beyond the resolved range it prints UNRESOLVED and declines to
claim anything — reporting "no root" there would be a physics claim this grid cannot support.

| K | τ at w=0.08 | null w | ratio to their 0.0815 | status |
|---|---|---|---|---|
| 1 | 0.377 | 0.0407786 | 0.5004 | resolved |
| 10 | 3.768 | 0.0870001 | 1.0675 | resolved |
| ≥100 | — | — | — | UNRESOLVED, not reported |

**Revised finding.** At the thickest *properly resolved* opacity, K=10, my null is 0.0870001
against the seat's 0.0815000 — **6.75% apart**, not the 228.92% the delivered script reported
from its unresolved K=1e2 row. Still NOT NESTED at the 2% test, and still moving away rather
than toward. But the honest gap is 6.75%, and the earlier figure should not be quoted.

**Scope, stated so it cannot be over-read.** The true asymptotic thick limit is **not tested
here**. Testing it needs a grid resolving the photosphere at K ≫ 18.4, which this one does not.

**Standing conditionality (REGATE4 repair 4).** The script now carries a header banner: it
executes p6's prefix and inherits the blackbody junction anchor with the adiabatic depth law
T ∝ ρ̄^[w/(1+w)]. Every null here is a property of **that assumed source map**, not of the
pinned solution, and REGATE4 withdrew null existence as a model-level claim outright.

**Run record.** `python3 p8_thick_limit.py` → exit 1, **2/3 checks**. The remaining FAIL is the
NOT-NESTED result itself — a genuine negative finding, correctly labelled, not a defect.
