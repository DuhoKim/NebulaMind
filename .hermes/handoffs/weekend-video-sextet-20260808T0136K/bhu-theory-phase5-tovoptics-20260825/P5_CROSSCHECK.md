# P5 blind double — CONFIRMED, and exactly (2026-08-26)

Second double briefed with the open items left open. gpt1 was asked to decide for itself
whether the exterior's emission is Doppler-shifted, whether the anisotropy survives opacity,
and which radius normalises the offset — none of it supplied.

## It reached the structural result independently

Its own words: the exterior's thermal emission **"is Doppler shifted at crossing"** — isotropic
in the exterior fluid's rest frame, not in the observer's — which is precisely the error I had
found in my own P2 while building the joint argument. And: **"Opacity weakens but does not
erase the anisotropy … The coefficient saturates … rather than approaching zero. Therefore
opacity cannot hide an arbitrary offset."**

That is the phase's central claim, reached from the physics rather than from my text.

## The numbers agree to the digit, under the gate's own conversion factor

The seat chose r_*(η_obs) = 2.000 as its normaliser; I use r_*(η_crossing) = 1.4366 per the
gate's B1 ruling. The B1 conversion factor is 1.392165, and applying it:

| quantity | mine (crossing-normalised) | × 1.392165 | gpt1 (observer-normalised) |
|---|---|---|---|
| saturated dipole coefficient | 0.2461 | 0.34263 | **0.34258957** |
| saturated offset bound | 5.5166e-3 | 7.680e-3 → ÷ | **3.96261e-3** = 5.5166e-3 / 1.392165 |

Both quantities map through the *same* factor the gate derived independently in B1. **The two
implementations are the same computation in two reporting conventions.** Per B1 the
crossing-normalised figures are the ones to quote.

## What the seat added that I did not have

A physical argument for which opaque endpoint is meaningful: a pure absorber (λ = 0) leaves the
normalised pattern intact — attenuation is common and divides out — **but its absolute
intensity vanishes**, so it cannot be identified with the measured 2.7255 K monopole at all.
The LTE/source-dominated endpoint is therefore the physically admissible opaque limit, not
merely the conservative one. That sharpens my treatment, which carried both endpoints without
distinguishing them on physical grounds.

## Disposition

**P5's joint exclusion is CONFIRMED by blind double.** Across the full opacity range, thin
through saturated, the observer must sit within one part in 453 to one part in 181 of the
crossing radius. The exclusion does not depend on resolving the opacity.

Process note: the seat wrote its completion marker as GPT1_P2B_DONE.md rather than
GPT1_P5_DONE.md, because I generated its brief by substituting "P2b" and the marker line spelled
it "P2B". My error in brief generation, not the seat's; the work itself is complete and
correctly scoped to P5.

## Verification-arithmetic correction (same day)

My first verification print applied the B1 factor as a multiplication to BOTH quantities and
reported the bound as a mismatch. That was an error in the check, not in the finding: a
coefficient scales UP with a larger normaliser (a given fraction is a larger physical offset),
while a bound scales DOWN, being its inverse. Applied correctly:

- coefficient: 0.246100 × 1.392165 = 0.342612 vs 0.34258957 — **MATCH**
- bound: 0.0055166 ÷ 1.392165 = 0.00396261 vs 0.00396261 — **MATCH**

Both map through the single B1 factor, as the receipt body already stated. The erroneous print
is left in the commit history rather than amended away.
