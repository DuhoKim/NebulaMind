# K2 — one-page human check sheet (Tori, 2026-09-03 17:25 KST; Duho's order "both", 17:22 KST)

**Claim checked:** a pressureless spherical FRW interior joins a Schwarzschild(–de Sitter) exterior WITHOUT a shell iff the boundary
is comoving (then it is the Oppenheimer–Snyder match); Pathria's horizon identification as a null junction needs a shell that
fails the dominant energy condition. Files: `K2_JUNCTION_PREREG_20260903.md` (frozen), `K2_codex_junction.py`, `K2_claude_junction.py`,
`K2_RESULT_20260903.md`. Sources under `bhu-reading-20260823/sources/`.

## A. Inputs (every one pinned)
| # | input | value / form | pin |
|---|---|---|---|
| 1 | interior metric | ds² = −dτ² + a²[dχ² + S_k(χ)²dΩ²] with S_k = sin χ (k=+1) or χ (k=0) — the angular gauge used in every step below; the sources print the equivalent r-gauge a²[dr²/(1−kr²) + r²dΩ²] with r = S_k(χ); dust ρ ∝ a⁻³ | entry 22 `2606.25023_clean.txt` L316–320; entry 56 `gaztanaga_mass_mnras_clean.txt` L141 |
| 2 | exterior metric | ds² = −F dT² + F⁻¹dR² + R²dΩ², F = 1 − 2GM/R − ΛR²/3 | entry 4 `knutsen_2009_gravcosmol15_273_clean.txt` L238–283 |
| 3 | smooth (Darmois–Israel) condition | induced metric and extrinsic curvature K_ab continuous; a shell ⇔ [K_ab] ≠ 0 | entry 4 L603–642, L695–70x |
| 4 | null junction (Barrabès–Israel) | transverse curvature K_ab = e^μ_a e^ν_b ∇_μ N_ν; jump ⇒ surface stress | entry 5 `khakshournia_2010_note_pathria_arxiv1412.0105_clean.txt` L49–55, L137–168 |
| 5 | mass relation | M = (4π/3) ρ R³ on the boundary | entry 1 `pathria_1972_…_clean.txt` L308–329 (μ = 4πGρR³/3c²); entry 5 L88–92; entry 56 L143 |
| 6 | Pathria's boundary | r_b = 1, i.e. the maximum-expansion sphere χ = π/2 of the closed model | entry 1 L67–71, L394–409; entry 4 (r_b = 1) |
| 7 | Λ range | 0 ≤ Λ ≤ Λ_c | entry 5 L29–41 |
| 8 | placements B1/B2/B3 and classes | prereg §1, §3 | `K2_JUNCTION_PREREG_20260903.md` |

## B. Steps, in order, with the intermediate results
1. Areal radius on the boundary: R = a S_k(χ), S_k = sin χ (k=+1) or χ (k=0). Outward normal from FRW to the exterior.
2. **B1 (comoving χ = χ*):** interior angular curvature K⁻_θθ = R C_k with C_k ≡ √(1 − k S_k²); exterior K⁺_θθ = R √(Ṙ² + F).
   With input 5 and the Friedmann equation, Ṙ² + F = C_k² exactly (Λ cancels term by term). ⇒ [K_θθ] = 0; also [K_ss] = 0.
   ⇒ **S_ab = 0: smooth.** k=0: expands forever (entry 56's cell). k=+1: recollapses (C_k² < 1). *(Control C1 prints exactly this.)*
3. **B2 (null junction at the horizon at maximum expansion, k=+1):** ȧ = 0 there, F(R_b) = 0. Barrabès–Israel jump: [K_uu] = −2πρa,
   angular jumps 0 ⇒ surface energy μ = 0, pressure p = ρa/4 (input 4, reproduced by both seats; *control C2*). Energy
   conditions: WEC (μ ≥ 0, μ+p ≥ 0) holds; DEC (μ ≥ |p|) FAILS since μ = 0 < p. ⇒ **J_SHELL_UNPHYSICAL.** Λ-independent.
4. **B2, k=0:** flat dust with Λ ≥ 0 has H² = 8πGρ/3 + Λ/3 > 0, never a maximum expansion ⇒ no such surface ⇒ **J_NONE** (vacuous).
5. **B3 (general timelike χ*(τ)):** [K_θθ] = 0 ⇔ M equals the Misner–Sharp dust mass inside the boundary; Birkhoff makes M constant
   in time ⇒ the boundary encloses fixed dust ⇒ comoving. So a no-shell B3 boundary IS a B1 boundary ⇒ **J_SMOOTH_EXPANDING** (the
   third seat verified this equation; a shelled non-comoving boundary has trajectory-dependent S_ab, reported, not classed).
6. **Extra row:** the comoving surface χ* = π/2 followed in time: smooth, M = C/2, exterior side T = const with F(R_b) = −ȧ², so
   R_max = R_s is derived; expanding phase inside the white-hole region; recollapse (*control C3*: with Knutsen's hypothesis
   F > 0 this forces ȧ = 0, his static sphere).
7. **Deletion probe (C4):** removing the energy-condition test flips exactly the two B2 k=+1 cells and nothing else.

## C. Final classes
Entry 56's cell (B1, k=0, Λ=0): **J_SMOOTH_EXPANDING**. Pathria's cell (B2, k=+1, 0≤Λ≤Λ_c): **J_SHELL_UNPHYSICAL**. No cell undetermined.

*(Kimi arithmetic re-check 17:30 KST: all steps recompute clean; the gauge notation of input 1 was clarified above in answer to its one issue.)*

## D. Where a critic could disagree (named)
1. **Dust.** Any interior pressure changes step 2 (Ṙ² + F ≠ C_k² in general); the theorem is for p = 0 only.
2. **What "B2" means.** Read as the comoving surface through maximum expansion it is smooth (step 6); read as a null junction ON
   the horizon it is a DEC-violating shell (step 3). The prereg fixed the second reading; both are reported.
3. **The physicality criterion.** "Unphysical" = violates the dominant energy condition; a critic who accepts DEC violation for a
   null shell (p > 0, μ = 0) keeps a J_SHELL_EXPANDING reading — this is exactly what C4 flips.
4. **The mass prescription at the null surface.** Khakshournia freezes M = (4π/3)ρr³ on Σ; the Claude seat records a 0/0 in the
   null generator's parameter at χ = π/2 under that prescription; the class does not depend on it.
5. **Spherical symmetry and a single Λ** on both sides are assumed throughout (prereg §1).
