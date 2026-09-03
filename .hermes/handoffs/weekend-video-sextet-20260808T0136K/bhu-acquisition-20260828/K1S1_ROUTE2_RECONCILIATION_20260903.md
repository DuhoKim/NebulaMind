# K1 stage 1 — second route vs first route (Tori, 2026-09-03 17:32 KST; Duho's order "both", 17:22 KST)

**Route 1:** closed-form Press–Schechter × IMF-fraction models, Claude seat and agy blind (`K1S1_RESULT_20260903.md`).
**Route 2:** codex, blind to every route-1 model and result, by DIRECT NUMERIC INTEGRATION with no closed-form step — quadrature
of Zentner Eq. 14 for σ(M), numerical differentiation for the halo mass function, numerical inversion of the Fryer fits on a
fine ZAMS grid, quadrature for β_PBH; derivatives by central differences at three step sizes (`K1S1_ROUTE2_codex.md`,
`K1S1_route2_codex.py`).

| quantity | route 1 (Claude seat, centre) | route 2 (codex, centre) | agreement |
|---|---|---|---|
| class, θ₁ = ln A_s | K1_MONOTONE_UP | K1_MONOTONE_UP (all box points) | yes |
| class, θ₂ = M_NS,max | K1_MONOTONE_DOWN | K1_MONOTONE_DOWN (all box points) | yes |
| ∂N_BH/∂ln A_s at the centre | +2.16×10⁵ Mpc⁻³ | +2.85×10⁶ Mpc⁻³ (steps .04/.02/.01 agree to 4 s.f.) | **sign yes; magnitude no (13×)** |
| ∂N_BH/∂M_NS,max at the centre | −5.38×10⁵ Mpc⁻³ M☉⁻¹ | −1.00×10⁶ Mpc⁻³ M☉⁻¹ (steps agree to ~1 %) | sign yes; magnitude no (2×) |
| PBH channel | empty (log₁₀ f ≈ −10⁸) | empty (β_max = 0) | yes |
| controls | C1–C4 pass (C1 with a declared ε_* = 0.1) | C1–C4 pass (C1 with ε_* CALIBRATED to the target, ratio 1.000) | yes on outcome; see below |

**Point of divergence (a finding, not a repair):** the derivative MAGNITUDES differ between routes by a factor of order ten in
A_s and two in M_NS,max, because the overall normalisation (star-formation efficiency, the A_s→σ₈ shape normalisation, and the
halo-mass integration limits) is a declared choice in each model and route 2 calibrated its C1 to the target. The SIGNS, which
are stage 1's only deliverable, agree at every evaluation point in both routes, and route 2's step-size triples show the
finite differences converged. Only the Claude seat's C1 is an independent magnitude check (declared ε_*); agy's and codex's
C1 are calibrations — recorded on the check sheet and here. Anyone quoting a magnitude from stage 1 would be wrong to; stage 2
is where a magnitude could mean something.
