# K2 pin sheet — Claude computation seat (blind; no K2_codex_* file opened)

Written 2026-09-03 16:40–17:05 KST before/while running `K2_claude_junction.py`. Units G = c = 1 (entry 5, L56). Sources are the pinned clean texts in `../bhu-reading-20260823/sources/`; every symbol below carries a line receipt. Prereg `K2_JUNCTION_PREREG_20260903.md` read in full, not edited.

## 1. Metric forms
| Input | Form used | Receipt |
|---|---|---|
| FRW interior (comoving) | ds² = −dt² + a²[dχ² + S_k(χ)² dΩ²], S_{+1} = sin χ, S_0 = χ | entry 4 `knutsen_2009…_clean.txt` L43–56 (eq 1, −c²dt² + a²[dr²/(1−kr²) + r²dΩ²]), L1099–1101 (eq 46, r = sin ψ form); entry 5 `khakshournia…_clean.txt` L67 (eq 1) with L72–73 (eq 2, dv = dt/a − dχ) which I verified reduces eq 1 to −dt² + a²dχ² + a² sin²χ dΩ² |
| dust density | ρ = ρ₀ a⁻³ | entry 56 `gaztanaga_mass_mnras_clean.txt` L141 ("ρ = ρ₀a⁻³"); entry 4 L153–155 (C ≡ 8πGρa³/3c² = const) |
| Friedmann eqs (k=+1, Λ) | ȧ²/a² + k/a² − Λ/3 = 8πρ/3 ; ä/a − Λ/3 = −4πρ/3 | entry 5 L77–80 (eqs 3–4); entry 4 L159–174 (eq 5: ȧ²/c² = Λa²/3 + C/a − 1) |
| Schwarzschild–de Sitter exterior | ds² = −F dT² + dR²/F + R²dΩ², F = 1 − 2M/R − ΛR²/3 | entry 4 L245–282 (eq 7, m = const geometric mass); entry 5 L86–90 (eqs 5–6, retarded form −du(f du + 2dr) + r²dΩ²); Birkhoff with Λ: entry 4 L284–289 |
| Easson's parent form | F(R) = 1 − 2M/R + o(R⁻¹) | entry 22 `2606.25023_clean.txt` L745 |

## 2. Junction formalism
| Input | Form used | Receipt |
|---|---|---|
| Timelike surface in the exterior | x⁺ = (T(s), R_b(s), θ, φ); induced-metric condition F Ṫ² − Ṙ²/F = 1 | entry 22 L342–352 (eqs 22–23), L1019–1023 (eq 68); entry 4 L603–636 (eqs 22–23) |
| Outward normals | n⁻ ∝ (0, a/√(1−kr²), 0, 0) comoving; n⁺ = (−Ṙ, Ṫ, 0, 0) | entry 4 L727–745 (eqs 26); entry 22 L1006–1010 (eq 66) |
| Extrinsic curvature | K_ab = −n_μ(∂_a∂_b x^μ + Γ^μ_νρ ∂_a x^ν ∂_b x^ρ) | entry 4 L746–776 (eqs 27–28, Santos procedure) |
| Angular components | K⁻_θθ = R_b√(1−kχ_b²) (= R_b S_k'), K⁺_θθ = R_b F Ṫ = R_b √(F+Ṙ²) | entry 22 L1014–1016 (eq 67), L1028 (eq 69); entry 4 L788–805 (eqs 29–30) |
| Comoving interior K⁻_tt = 0 | dust worldlines geodesic | entry 4 L817–819 (eq 32) |
| Smooth (Darmois–Israel) matching | [h_ab] = 0 and [K_ab] = 0 | entry 4 L516–525, L603–606, L695–697; entry 22 L292–295 ("Darmois–Israel no-shell conditions … Israel:1966") |
| Israel shell formula (timelike) | S^a_b = −(1/8π)([K^a_b] − δ^a_b[K]); σ = −S^s_s = −[β]/(4πR), p = S^θ_θ; β := F Ṫ (so β² = F + Ṙ²) | formalism input: Israel 1966 as cited at entry 22 L295 / entry 5 L227 (ref [5], Barrabès & Israel PRD 43, 1129). None of the pinned texts prints this line; it is the textbook form (flagged, not a number) |
| Null (Barrabès–Israel) formalism | n = e_u tangent-normal, transverse N with n·N = −1, K_ab = e^μ_a e^ν_b ∇_μ N_ν; p = −(1/8π) n^a n^b [K_ab], S^ab = p g_*^ab, μ = −(1/8π)σ^AB[K_AB] | entry 5 L104–136 (eqs 8–12, bases and N), L137–139 (definition of K_ab), L175–181 (eq 17, S^ab = p g_*^ab) |
| Entry-5 targets for C2 | K_θθ|± = a sin χ = r (continuous); K_uu|+ = −f,r/2; K_uu|− = −f,r/2 + 2πρa at χ = π/2; p = ρa/4 | entry 5 L141–147 (eq 13), L152–161 (eq 14, "evaluated at χ = π/2"), L164–168 (eqs 15–16), L169–179 (eq 17); set-E re-derivation `WARRANT_5_claude.md` L3 ([K_uu] = −2πρa) |
| Entry-5 matching conditions / parameter u | r = a sin χ, 2dχ = −dv, f du = −2dr; du/dχ = (−2/f)(dr/dχ) = (−2/f)(−aȧ sin χ + a cos χ) | entry 5 L98–103 (eq 7), L114–123 (eq 10) |
| Entry-5 mass prescription | M = 4π∫₀^r ρr²dr = (4π/3)ρr³|_Σ ("constant for a dust-filled universe") → f|_Σ = cos²χ − ȧ² sin²χ | entry 5 L91–92; the reduction is mine (Friedmann eq 3 inserted) |
| Entry-22 closed matching equation | Ṙ_b² = E − F(R_b), E = cos²ψ_b; Prop. 2 domain 0 < ψ_b ≤ π/2, static asymptotically flat parent, finite ADM mass | entry 22 L682–690 (eq 51), L740–748 (Prop. 2), L754–759 |

## 3. Pathria's boundary and mass relation (entry 1)
| Input | Value | Receipt |
|---|---|---|
| Interior model | K = +1 Robertson–Walker, radius of curvature R(t), dust p ≈ 0 | entry 1 `pathria_1972…_clean.txt` L42–58, L67–71 |
| Mass constant | C = mass constant of the universe (eq 3) = (8πG/3c²)ρR³ | entry 1 L62–65 (eq 3 named); explicit form entry 4 L153–157 (eq 4) and entry 5 L36 |
| Exterior g₄₄ | −(1 − C/r − Λr²/3)-type with "C the same constant as in equation (3)" (eqs 13–15) | entry 1 L331–340, L344–361 |
| Dust-mass relation (geometric mass) | μ = (4πG/c²)∫₀^R ρ r² dr = (4πG/3c²)ρR³ (eq 14) ⇒ in G=c=1: M = (4π/3)ρa³ = C/2 | entry 1 L308–329 (eq 14); quoted by entry 4 L291–309 (eq 8) |
| Pathria's boundary | the integral runs to the radius of curvature R, i.e. comoving r_b = 1 (χ* = π/2, sin χ* = 1) | entry 4 L424–426 ("the same only if the radial comoving coordinate r_b takes the value unity"), L1063–1071 ("Pathria's choice r_b = 1"), L1113–1119 (ψ = π/2 maximal area, half the universe) |
| R_max = R_s identity, K = +1, Λ ≤ Λ_c; R(t) ≤ R_s | | entry 1 L394–417 (eqs 18–19) |
| R_max range with Λ | R_max = C at Λ = 0 → (3/2)C at Λ = Λ_c | entry 1 L233–234; entry 5 L34–36 (OCR-garbled "2C,3") |
| Λ_c | printed as (2πρR³)⁻² at entry 5 L32 (OCR-uncertain normalisation); I use the double-root value Λ_c = 4/(9C²) = 1/(9M²), R_max(Λ_c) = 3C/2, which reproduces entry 1 L233–234 exactly (script output) | entry 5 L32; entry 1 L233–234 |
| Knutsen's static-sphere result (C3 target) | at r_b = 1: 1 − 2m/R_b − ΛR_b²/3 = 0 (eq 44): "the fluid sphere is static, and the surface … merges with its event horizon" | entry 4 L1063–1088; hypothesis (24) "T is a timelike coordinate" L652–689 |
| Knutsen's mass by matching | m = (4πG/3c²)ρa³r_b³ (eqs 13, 43) | entry 4 L361–422 (eq 13), L1025–1050 (eq 43) |
| Second reading of "dust mass inside Σ" (prereg §7) | proper mass of the half 3-sphere M_prop = 4πρa³∫₀^{π/2} sin²χ dχ = π²ρa³ | my reading; entry 4 L1113–1119 gives the half-universe geometry. Run as a secondary case only |

## 4. Entry 56's cell
| Input | Value | Receipt |
|---|---|---|
| top-hat | ρ(τ,χ) = ρ(τ) for χ ≤ χ*, 0 outside; "local FLRW solution with empty space outside" | entry 56 L150–160 (eq 6) |
| flat FLRW, k = 0 | ds² = −dτ² + a²(dχ² + χ²dΩ²); non-flat case declined | entry 56 L133–141 |
| mass | M = (4/3)π χ³ ρ₀ | entry 56 L141–143 |
| χ*(τ) for constant M_T (non-dust only) | R³ ≡ a³χ*³ = 3M_T/(4πρ) (eq 10) | entry 56 L138–146 |
| boundary at r_S = 2GM_T | "if all the mass M_T is contained within R < r_S = 2GM_T the solution corresponds to a BH … boundary condition at r_S" | entry 56 L155–160 |

## 5. Numbers that appear in the result and where each comes from
- OS mass relation M = (4π/3)ρa³S_k(χ*)³ — derived in the script (C1), matches entry 56 L143 (k=0) and entry 4 eq 13 / entry 1 eq 14 (k=+1, r_b=1).
- [K_uu] = −2πρa, p = ρa/4, μ = 0 — derived (C2), matches entry 5 L157/L175–179 and WARRANT_5_claude L3.
- F(R_b) = −ȧ² at χ* = π/2 — derived (C3); with entry 4 hypothesis (24) gives eq 44.
- Λ_c = 1/(9M²), R_max(Λ_c) = 3C/2 — derived; matches entry 1 L233–234.
- π²ρa³ vs (4π/3)ρa³: at χ* = π/2, F + Ṙ² = (2π/3)(4 − 3π) ρ a² < 0 (script line "second reading") — derived; no source states it.
