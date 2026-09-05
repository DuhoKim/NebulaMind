# C4 GR benchmark

Relations used: the source-pinned metric/mass function, its exponential profile, and the asymptotic Schwarzschild mass identity (C2 L01, L04-L08, L10).

Stated-limit algebra:

`M(r)=4π∫₀ʳρ(x)x²dx → 4π∫₀∞ρ(x)x²dx=M` as `r→∞` (entry 19 L00222-L00245).

Therefore `R_g(r)=2GM(r)/c² → 2GM/c²=r_g`, and

`g_tt=1-R_g(r)/r → 1-r_g/r = 1-2GM/(c²r)`;

`g_rr=-[1-R_g(r)/r]⁻¹ → -[1-2GM/(c²r)]⁻¹`, while the angular term remains `-r²dΩ²`. This equals the Schwarzschild exterior form. Entry 18 L00152-L00154 independently states that for large radius the exact solution “practically coincides with the Schwarzschild solution.”

Premise list for this limit:

1. Entry 19 L00218: printed `R_g(r)=2GM(r)` (with the source's unit convention; restored `c²` fixed by entry 18 equation (6)).
2. Entry 19 L00222-L00245: printed enclosed-mass integral, finite total mass, and `R_g(r→∞)=r_g`.
3. Entry 18 L00095-L00100: printed `r_g=2GM/c²` and distant-observer mass definition.

No interior premise (`r₀`, `ρ₀`, de Sitter limit, pressure law, or regularity condition) enters the exterior-limit algebra.

C4_GR_BENCHMARK=PASS
