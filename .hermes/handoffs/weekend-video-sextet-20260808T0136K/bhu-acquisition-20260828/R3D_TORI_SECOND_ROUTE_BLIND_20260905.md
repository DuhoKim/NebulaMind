# R3D — Tori's independent second route, written BLIND (no seat report read) — SEALED BY COMMIT TIME + HASH

**Written 2026-09-05 12:36:16 KST by Tori. Seat status at writing: codex run seat RUNNING since 12:30 KST, no report file exists; kimi not yet dispatched.**

Purpose (§7 "independent second route", Duho's 09-03 "both" rule): a reading of the four manifest sources by the lane
owner, done and committed BEFORE any seat's run report is opened, so the seats' results can be checked against a
route that could not have been shaped by them. This is NOT a filing. It files no class and moves no token. It is a
list of what the sources print, with line numbers, and what a check-sheet reader must verify.

Sources read in full (bytes verified against §2a before reading): entry 18 (355 raw lines), entry 19 (1333 raw
lines), entry 20 (754 raw lines), entry 55 (1856 raw lines; LaTeX duplicates stripped for reading). Line numbers
below are `cat -n` numbers of the raw files.

## A. Printed relations binding size to mass, or bounding the mass — what I found

### Entry 18 — Dymnikova 1992, GRG 24, 235 (`dymnikova_1992_grg24_235_vor_clean.txt`)
- L94-95, eq (6): `r_g = 2GM/c²` — the Schwarzschild radius bound to the mass. **A printed size–mass relation.**
- L126-127, eq (9): `r0² = 3c⁴/(8πG ε0)` — the core scale bound to the interior vacuum density ε0.
- L148, eq (13): `r*³ = r0² r_g` — the characteristic radius bound to r0 and r_g, hence to M and ε0.
- L146, eq (12): `R_g(r) = r_g(1 − exp(−r³/r*³))` — the mass function.
- L187, eq (17): two horizons `r+ ≈ r_g[1 − O(exp(−r_g²/r0²))]`, `r− ≈ r0[1 − O(r0/4r_g)]` — asymptotic forms valid for
  r_g ≫ r0; **no condition for horizon existence is printed as an inequality on M.**
- L318, eq (23): `m_in = M(1 − exp(−r_g²/r0²))`.
- L177-183, L301-304: "several solar masses", "GUT energy ~10¹⁵ GeV", "M ~ 10 M☉", "Planckian energy" — **worked
  examples, stated conditionally ("If … then"), not relations fixing ε0.**
- **No lower bound on M is printed.** ε0 is a free parameter of the solution; nothing in the paper fixes it.

### Entry 19 — Dymnikova 2019, Universe 5, 111 (`dymnikova_2019_universe_clean.txt`)
- L33-35: `r_g = 2GM`, `r0 = √(3/Λ)`.
- L216, eq (2): `R_g(r) = 2GM(r)`; L222-228, eq (3): `M(r) = 4π∫ρ x² dx`; L234-250, eq (4): `M = 4π∫₀^∞ ρ x² dx < ∞`,
  `R_g(r→∞) = r_g`, `R_g(r→0) = r³/r0²`, `r0² = 3c²/(8πGρ0)` — ρ0 "the vacuum density at r = 0" (L252).
- L253: the profile `ρ(r) = ρ0 exp(−r³/r0² r_g)`.
- **L277-279: "Within the range of masses M ≥ M_crit, where M_crit corresponds to the double horizon, the de
  Sitter–Schwarzschild geometry (2) describes a regular black hole with the de Sitter interior … For M > M_crit
  spacetime has two horizons."** — **THE ONE PRINTED MASS BOUND in the Dymnikova sources.** M_crit is named, not
  given: no formula, no value, in this paper. By eq (4) it can only depend on ρ0 (and G, c), and ρ0 is free.
- The rest of the paper (Sec. 3, L593-1147) is quantum birth of universes: Wheeler–DeWitt, tunnelling factors
  `D1 = exp(−(2/3)(r0/l_Pl)² ...)` (L883-887) etc. — no further mass bound; "GUT scale E_GUT ~ 10¹⁵ GeV" (L892) is a
  numerical example.

### Entry 20 — Bronnikov, Melnikov & Dehnen 2007, GRG 39, 973 (`gr-qc_0611022_clean.txt`)
- L146-148, eq (2): Bardeen's `A(ρ) = 1 − Mρ²/(ρ²+q²)^{3/2}`, "two horizons exist provided q² < (16/27) M²" — **a
  printed size–mass inequality, for the Bardeen metric (type 1 regular BH), not the Dymnikova branch.** Expected
  census disposition: WRONG_BRANCH, demonstrable from L143-146 ("Bardeen's work … a particular BH configuration").
- L335-336: asymptotic flatness `2bc = −πρ0`, Schwarzschild mass `m = ρ0/3` (black-universe example, eq (11)-(16)).
- L343-348: horizon radius "depends on both parameters m and b = min r(ρ) and cannot be smaller than b"; throat in
  R region if `3πm < 2b`, at the horizon if `3πm = 2b`, in T region if `3πm > 2b` — **size–mass relations for the
  black-universe branch; they bound nothing below** (L337-341: ρ0 = m = 0 is the Ellis wormhole; ρ0 < 0 gives m < 0).
- The Global Structure Theorem (L233-253) constrains horizon count, not mass.

### Entry 55 — Alesci, Bahrami & Pranzetti 2020, PRD 102, 066010 (`2007.06664_clean.txt`)
- L303-316, eqs (14)-(16): Kretschmann `K = 3e^{−3τ/Gm}/(4(Gm)⁴)` (as printed), `τ* ~ (Gm/3) log[3ℓ_P⁴/(4G⁴m⁴)]`,
  **`R_c(τ*) ~ (Gm)^{1/3} ℓ_P^{2/3}`** — a size (the radius where curvature turns Planckian) bound to the mass.
- L549-551, eq (29): `A(R) = 4πR² = 8πγℓ_P² Σ j̃ ≃ 4πγℓ_P² j_x N²` — area bound to spin numbers.
- L565-573, eq (31): `α = 2π√(γ j_x) ℓ_P`, `β = 4√(8πγ j) ℓ_P/j_x`; L584-586, eq (32): `j = γ j_x`.
- L841-843, eq (47): `ℓ := 2Gm/ξ`; L859-861, eq (49): `λ = 3/(N0² ℓ²)`; L996-1003, eq (59): λ in terms of ξ, β, γ, j;
  L1094-1096, eq (67): **`λ = 0.06/(ℓ_P² j)`** (for γ₂ᵈˢ ≈ 0.274).
- **L1099-1100: "the restriction that 1 ≪ j ≪ Gm/ℓ_P"** — a printed inequality on the mass (validity of the
  semiclassical regime): m ≫ j ℓ_P/G, with j ≫ 1. **Bounds the mass from below, with no coefficient and a free j.**
- L1105-1118, eqs (68)-(69): bounce radius `R_b(m,j) ~ (Gm)^{1/3}(ℓ_P² j)^{1/3}`; "upper bound on j of order ~10⁶"
  argued, not derived.
- L1126-1135, eqs (70)-(71): `j̄ ~ j_i N_i² ~ G²m²/ℓ_P²`, **`λ̄ ~ c⁴/(G²m²)`** — the emergent cosmological constant bound
  to the mass (proposed rescaling, "sketch", L1137). L1140-1144: inserting "the observed mass … m ≃ 1.46 × 10⁵³ kg"
  (Planck 2018) — **a value outside §2b; ADDED if used.**
- Table 1 (L946-967): tuned parameters ξ ∈ {0.957, 0.974}, γ ∈ {0.227, 0.274}, ν = 1.802, δ, δ_x ∝ 1/β².
- **No lower bound on m is printed other than the regime condition L1099.**

## B. What this route expects the protocol to do with that — stated as expectations, not results
1. **Limb A is satisfied, not exited:** a printed relation binding size to mass exists in every source (entry 18
   eq (6), (9), (13); entry 19 eq (4); entry 20 eq (2) and L347; entry 55 eq (16), (69), (71)). Class 3
   (`DYM_NO_SIZE_MASS_RELATION`) should NOT be filed. **A seat filing class 3 has missed eq (6) of entry 18** — check.
2. **The only printed mass bounds are (a) entry 19 L277 `M ≥ M_crit` with M_crit unspecified and, by eq (4), a
   function of the free ρ0; (b) entry 55 L1099 `Gm/ℓ_P ≫ j ≫ 1`, a regime condition with free j and no coefficient.**
   Neither fixes a number.
3. **Completion-free reading:** with ρ0 (ε0) free, the allowed mass set is (0, ∞) — every M > 0 is a regular black
   hole for some ρ0 — so it **permits masses approaching zero: Z.** A seat that reads "M ≥ M_crit(ρ0)" at FIXED ρ0
   as a positive floor is filing a floor that depends on a parameter it chose: that is what C6 condition 3 (free
   normalisation ρ0) and condition 4 (fixity of ρ0) exist to catch, and §2b forbids introducing ρ_Planck or ρ_GUT
   as "standard".
4. **The four completion kinds** (Euclidean volume, uniform interior, order-unity coefficient, GR exterior) — none
   of them fixes ρ0; a "uniform interior" completion (ρ = ρ0 inside r0) does not choose ρ0's value. So I expect no
   admissible reading in P, hence **class 4 `DYM_NO_POSITIVE_FLOOR`** (P empty, Z non-empty, I empty) — **OR** class 2
   if a seat legitimately counts a ρ0-conditional floor as P. **A split between 4 and 2 is the plausible split**, and
   §9's third-seat rule handles it. Either way C6 is then either NOT_RUN (class 4) or expected to FAIL on condition
   3 (class 2) — but the failure must be exhibited, not assumed.
5. **What would surprise this route:** class 1 (a completion-free, ρ0-independent positive floor). If a seat files
   it, the check-sheet reader must find the printed relation that fixes ρ0 (or ε0, or j) without a chosen value —
   I found none.

## C. Check-sheet anchors (the lines a human must verify)
| claim | file | lines | what to look at |
|---|---|---|---|
| size–mass relation is printed | entry 18 | 94-95 | `r_g = 2GM/c²`, eq (6) |
| core scale ↔ density | entry 18 | 126-127 | eq (9) |
| the ONE printed mass bound | entry 19 | 277-279 | "M ≥ M_crit … double horizon"; no formula for M_crit anywhere in the file |
| ρ0 is a free parameter | entry 19 | 252 | "ρ0 is the vacuum density at r = 0" — defined, never fixed |
| Bardeen inequality is another branch | entry 20 | 143-148 | "Bardeen's work … q² < (16/27)M²" |
| regime bound, free j | entry 55 | 1099-1100 | "1 ≪ j ≪ Gm/ℓ_P" |
| λ–mass relation is a sketch with an outside value | entry 55 | 1131-1144 | eq (71), "m ≃ 1.46 × 10⁵³ kg" |

Nothing here is a verdict. The verdict is the seats', reconciled under §9, and Duho's to read.
