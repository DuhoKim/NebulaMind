# P6 blind double — CONFIRMED the physics, CAUGHT a real error of mine, NOT yet numerically
# reconciled (2026-08-26)

Third double briefed with the decisive question left open: *what does a crossing sight line
terminate on, and does anything arrive from beyond?*

## It reached my central result independently — and derived it better

gpt1, unprompted: **"radiation from beyond the TOV horizon reaches the shock with zero strength"**,
quantified as g < 4.26×10⁻⁶ with residual intensity weight below 3.3×10⁻²². Its derivation is
sharper than mine: near the horizon |B| ∝ x (x = N−1), so the frequency ratio g ∝ √x, and **by
Liouville invariance the bolometric weight is g⁴ ∝ x²**. It also concluded independently that
**"B is essential"** for depth weighting.

So P6's overturning of P5's transmitted-background term stands on two derivations.

## It caught a fourth-power error in mine

My P6 summed **temperature** ratios linearly and weighted the incoming beam by a single power
of Z. Transfer is bolometric: **intensities add, not temperatures**, and Liouville weights the
beam by g⁴. Corrected (intensities summed with Z⁴, then T = I^(1/4)):

| w | c₁ before | c₁ after | bound before | bound after |
|---|---|---|---|---|
| 0.2456 | 3.441 | **0.517** | 3.95e-4 | **2.63e-3** |
| 0.010 | 2.257 | 3.103 | 6.01e-4 | 4.37e-4 |

The error made the crossing sky far darker than it is and tightened the bound by ~6×. **The
"exclusion tightens by 3–6×" claim in P6_RECEIPT.md is WITHDRAWN.**

## The brightness story, corrected

My receipt said flatly "the crossing sky is DARK". The seat's phrasing is right and mine was
the thin-end case mistaken for the whole: **dim at low opacity, comparable at intermediate,
brighter in the opaque limit**, saturating at the Doppler-boosted shock photosphere. My own
corrected monopole now shows exactly that — −0.535 at the junction closure, **+0.828** at
w = 0.01. I had reported the trend from one end of it.

## Numerically NOT yet reconciled

At the junction closure: mine c₁ = 0.517, bound 2.63e-3; theirs a₁ = 0.627, bound 2.16e-3 —
about 20%. Their opaque limit (a₁ = 0.61524, bound 2.2065e-3) reproduces P5's vacuum case to
five digits, which is a meaningful internal consistency on their side. The residual gap is most
likely the source term: I use the energy-budget radiation ceiling T_rad, they use the local
shock source with an explicit opacity parameter λ. **Not reconciled, so P6's numbers are NOT
confirmed.**

## Where the bound now stands

Mine post-correction: 4.4×10⁻⁴ to 4.1×10⁻³ (one part in 245 to 2286). Theirs: ~1.9×10⁻³ to
2.2×10⁻³. P5's single-screen: 2.2×10⁻³ to 5.5×10⁻³. **All three overlap around one part in a
few hundred to a few thousand** — the exclusion survives every treatment; only its exact
strength is unsettled.
