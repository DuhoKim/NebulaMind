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
