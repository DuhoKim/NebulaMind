J_SMOOTH_EXPANDING — entry 56's cell (B1, k=0, Λ=0): the comoving Oppenheimer–Snyder matching, M = (4π/3)ρ₀χ*³ (entry 56 L143), [K_ab] = 0, expands forever; it lies OUTSIDE Easson's Prop. 2 domain (flat daughter, not closed), so Prop. 2 is neither confirmed nor refuted by it.
J_SMOOTH_EXPANDING — Pathria's cell (B2, k=+1, 0≤Λ≤Λ_c), on the surface Pathria names (comoving χ* = π/2 = Knutsen's r_b = 1): smooth with M = C/2 = (4π/3)ρa³, for every 0≤Λ≤Λ_c; the exterior side is the T = const surface with F(R_b) = −ȧ², i.e. the boundary is inside the white-hole region while expanding, on the bifurcation sphere at maximum expansion (R_max = R_s exactly — Pathria's identity is the matching condition), inside the black hole while contracting; it recollapses (Easson Prop. 2 endpoint ψ_b = π/2, simple outer zero at R = R_s: CONFIRMED, not refuted). The entry-5 reading of the same cell — gluing along the null horizon — is J_SHELL_UNPHYSICAL (null shell μ = 0, p = ρa/4 > 0: WEC/NEC hold, DEC fails), and it is not an expanding realization (Σ is the turnaround itself).

# K2 RESULT — Claude computation seat (blind double)
Claude seat, 2026-09-03 17:06 KST. Script `K2_claude_junction.py` (sha256 04339b12d9bb94b2e642d190becdd773e039521b5c8c8207434ab46324c42e55), its full printout `K2_claude_junction.out` (sha256 1d49030d01d88ebd828a0d061fca31627cd8099047221f1f5c9afecba5687f79), pins `K2_claude_pins.md`. Pure sympy 1.14.0, no web, no data, no K2_codex_* file opened. Prereg followed as frozen; controls run before any class; all four passed.

## Full table (placement × k × Λ)
| placement | k | Λ | class | basis |
|---|---|---|---|---|
| B1 comoving χ = χ* | +1 | 0 | J_SMOOTH_EXPANDING | OS matching, M = (4π/3)ρ₀ sin³χ*, β₊ = β₋ = cos χ*, [K^s_s] = 0; expands then recollapses (a_max finite) |
| B1 | +1 | 0<Λ≤Λ_c | J_SMOOTH_EXPANDING | same identity, Λ cancels exactly (script: β₊² − β₋² = 0, R̈ + F'/2 = 0 for general Λ) |
| B1 | 0 | 0 | J_SMOOTH_EXPANDING | entry 56's cell; M = (4π/3)ρ₀χ*³; expands forever |
| B1 | 0 | 0<Λ≤Λ_c | J_SMOOTH_EXPANDING | same; the surface later crosses the SdS cosmological horizon, still smooth |
| B2 χ = π/2 ↔ horizon (timelike, Pathria/Knutsen r_b = 1) | +1 | 0 | J_SMOOTH_EXPANDING | M = C/2; F(R_b) = −ȧ²; R_max = R_s = 2M; both K_ab ≡ 0 (χ = π/2 and T = const are totally geodesic) |
| B2 | +1 | 0<Λ≤Λ_c | J_SMOOTH_EXPANDING | same with F = 1 − C/R − ΛR²/3; R_max = smaller positive root = R_BH; Λ_c = 1/(9M²), R_max(Λ_c) = 3C/2 |
| B2 | 0 | 0 | J_NONE (vacuous) | no maximum-expansion surface for k = 0 (S_0' = 1 never vanishes); the placement does not exist |
| B2 | 0 | 0<Λ≤Λ_c | J_NONE (vacuous) | same |
| B3 general χ = X(t) | +1 | 0 | J_SMOOTH_EXPANDING | theorem: [K^θ_θ] = 0 ⇔ M = (4π/3)ρ₀S_k(X(t))³ for ANY X(t) (Ẋ drops out); M constant ⇒ Ẋ = 0 ⇒ the smooth members are exactly B1 |
| B3 | +1 | 0<Λ≤Λ_c | J_SMOOTH_EXPANDING | same |
| B3 | 0 | 0 | J_SMOOTH_EXPANDING | same |
| B3 | 0 | 0<Λ≤Λ_c | J_SMOOTH_EXPANDING | same |
| B2-null (entry 5: glue along the null horizon) | +1 | 0 | J_SHELL_UNPHYSICAL | [K_θθ] = 0, [K_uu] = −2πρa ≠ 0; μ = 0, p = ρa/4; DEC fails; not expanding on Σ |
| B2-null | +1 | 0<Λ≤Λ_c | J_SHELL_UNPHYSICAL | [K_uu] Λ-independent (∂_Λ[K_uu] = 0) |
| B2-null | 0 | any | J_NONE (vacuous) | no such surface |

No cell is J_UNDETERMINED: every class is fixed by an explicit smooth solution or a closed-form S_ab.

## Control outcomes (printed values, from `K2_claude_junction.out`)
- **C1 PASS** (B1, k=+1, Λ=0): `[K^θ_θ]=0 ⇔ F+Ṙ² = cos²χ* ⇔ M = 4πρ₀ sin³(χ*)/3`; with that M, `R̈ + F'(R_b)/2 = 0` so `[K^s_s]=0`; `F + Ṙ² = cos²(χ*)`. k=0 check: `M = 4πχ³ρ₀/3` (entry 56 L143). Λ-general: `β₊² − β₋² = 0`, `R̈ + F'/2 = 0` for both k.
- **C2 PASS** (entry-5 null junction, Barrabès–Israel, Khakshournia's prescription M = (4π/3)ρr³|_Σ pointwise, χ = π/2): exterior `K_uu|+ = −f,r/2`, `K_θθ|+ = r`; interior `K_θθ|− = a sin χ`, `K_uu|− = (Λa³ + 2πρ₀)/(3a²)`, so `K_uu|− − (−f,r/2) = 2πρ₀/a² = 2πρa`; `[K_uu] = −2πρ₀/a² = −2πρa`; `p = −[K_uu]/8π = ρ₀/(4a²) = ρa/4`; `μ = 0`; `∂_Λ[K_uu] = 0`. Caveat recorded (not a failure): with M frozen along Σ the parameter u is singular at the point χ = π/2 (f = 0 = dr/dχ there), so the value is tied to the paper's own prescription.
- **C3 PASS** (smooth timelike matching at r_b = 1): `β₋ = cos(π/2) = 0 ⇒ F(R_b) + Ṙ² = 2(−3M + 4πρ₀)/(3a) = 0 ⇔ M = 4πρ₀/3` (Pathria eq 14, Knutsen eq 8), then `F(R_b) = −ȧ²`; under Knutsen's hypothesis (24) (T timelike ⇔ F > 0) the only solution is ȧ = 0, F(R_b) = 0: the static sphere on its horizon = Knutsen eq (44). Direct exterior computation at Ṫ = T̈ = 0: `K_ss = 0, K_θθ = 0` (no division by β).
- **C4 PASS** (deletion probe, exact failure set): removing the energy-condition test changes exactly `[('B2-null', 1, '0<Lam<=Lam_c'), ('B2-null', 1, 'Lam=0')]`: `J_SHELL_UNPHYSICAL → J_SHELL_EXPANDING`; all 14 other cells unchanged. Asserted equal to the expected set.

## Key symbolic expressions
- Exterior (surface (T(s),R(s)), n⁺ = (−Ṙ, Ṫ, 0, 0)): `K^θ_θ⁺ = Ṫ F(R_b)/R_b = β₊/R_b`, `K^s_s⁺ · β₊ = R̈ + F'/2` with `β₊ := FṪ`, `β₊² = F + Ṙ²` (constraint F Ṫ² − Ṙ²/F = 1).
- Interior, general surface χ = X(t), γ⁻² = 1 − a²Ẋ²: `K^θ_θ⁻ = γ(aȧẊ + S_k'/S_k)/a`, `K^s_s⁻ = γ³(aẌ − a²ȧẊ³ + 2ȧẊ)`, `β₋ = γ(aȧẊS_k + S_k')`, `u·n = −γaẊ`.
- Israel shell (B1, exterior mass M = M_OS + m): `β₊² − β₋² = −2m/R_b`; `σ = −(β₊ − β₋)/(4πR_b)`, `p = (1/8π)([β]/R_b + (R̈ + F'/2)/β₊)`; σ > 0 ⇔ m > 0; no real embedding if m > R_bβ₋²/2. Full closed forms for σ, p (both k) are printed in the .out (lines "B1, k=…").
- B3 identity: `F + Ṙ² − β₋² = −(Λa³S³ + 6M − 3aȧ²S³ − 3a k S³)/(3aS)`, S = S_k(X(t)) — Ẋ-free, hence `[K^θ_θ] = 0 ⇔ M = (4π/3)ρ₀S_k(X)³`.
- Null shell: `S^ab = p g_*^ab`, `μ = 0`, `p = ρa/4`; WEC (μ ≥ 0, p ≥ 0) True; DEC (μ ≥ 0, p = 0) False; NEC True.
- Λ_c: double root of 1 − C/R − ΛR²/3: `Λ_c = 4/(9C²) = 1/(9M²)`, `R_max(Λ_c) = 3C/2` (entry 1 L233–234 reproduced).
- Second reading of the mass relation (§7, proper dust mass π²ρa³ of the half 3-sphere): at χ* = π/2, `F + Ṙ² = 2πρ₀(4 − 3π)/(3a) < 0` ⇒ no real embedding, smooth or shelled (J_NONE under that reading; Pathria's own eq 14 is the (4π/3)ρR³ reading, which is the one filed).

## Derivation summary (≤200 words)
For a comoving boundary the angular junction condition equates the exterior mass with the Misner–Sharp dust mass inside the surface, M = (4π/3)ρa³S_k(χ*)³, and then the ss-condition R̈ + F'/2 = 0 holds identically by the Friedmann equations, Λ cancelling — the Oppenheimer–Snyder matching exists for every (k, Λ) cell, so B1 is J_SMOOTH_EXPANDING everywhere, including entry 56's flat cell. For a general timelike surface χ = X(t) the same angular condition is Ẋ-free and again fixes M to the instantaneous Misner–Sharp mass; Birkhoff constancy of M forces Ẋ = 0, so no-shell junctions are exactly the comoving ones (B3 inherits B1's class; a non-comoving surface always carries a shell with u·n ≠ 0). At Pathria's surface χ* = π/2 the interior β₋ vanishes, forcing F(R_b) = −ȧ²: the junction is smooth (both K_ab vanish identically) with the boundary on the exterior T = const surface inside the horizon, touching the bifurcation sphere at maximum expansion — R_max = R_s is derived, not assumed, for all Λ ≤ Λ_c; Knutsen's static conclusion is the F > 0 restriction (his eq 24), Khakshournia's null shell is a different (horizon) gluing whose pressure-only shell violates DEC. Entries 4, 5, 22 stand as controls; Pathria's "universe inside a black hole" is the white-hole/black-hole halves of the χ* = π/2 OS model.

## Boundaries
Pure theory; dust only (entry 56's time-dependent χ* for non-dust fluids is outside the prereg — for dust the comoving mass is already constant, and a non-comoving edge would need a shell by the B3 theorem). The Israel timelike-shell formula and the Codazzi/Birkhoff facts are textbook inputs, flagged in the pins; every number is otherwise derived in the committed script. Paper HOLD respected; tiers untouched; nothing outward.
