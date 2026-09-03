# K3S1 pin sheet — seat claude (route 1, blind)
Stamped 2026-09-03 19:30 KST. Prereg K3S1_SPIN_CLOSURE_PREREG_20260903.md sha256[:16]=9ff4b0f41796fa84 (read in full, not edited).
Script K3S1_claude_spin.py sha256[:16]=5e753763511c9b52; its full stdout K3S1_claude_spin.log sha256[:16]=2d5ebca0233f00f5. Every constant below is
either quoted from a pinned source with a line number or reproduced by executed algebra in the script (tag in brackets).

## A. Objects, with receipts (sources under ../bhu-reading-20260823/sources/)
| object | receipt | pinned as |
|---|---|---|
| Dirac spin pseudovector s^i = ½ ψ̄γ^iγ⁵ψ; s_ijk = −e_ijkl s^l; units c=ℏ=1 | 1111.4595v2_poplawski_prd85_clean.txt L69-70 (units), L72-77 (eq. 4) | script §4 [s^mu]: s^μ = (0, n̂/2) for a rest spinor |
| s_i u^i = 0 ⇒ s^0 = 0 in the comoving frame; "s is the spatial spin pseudovector" | 1111.4595v2 L111-113 | script §4 [s^0] verified |
| C_Dirac: "The average value of its square is ⟨s²⟩ = ¾ n², n the fermion number density" | 1111.4595v2 L113-114 | comparison target only (PRINTED["DIRAC"]) |
| Spin-fluid (HHK) approximation s_ijk = s_ij u_k, s_ij u^j = 0 | 1111.4595v2 L118-119 | script §7 [transverse], [HHK_form] |
| C_fluid (entry 10 form): "s² = ½ s_ik s^ik = ⅛ n² [8, 9]" | 1111.4595v2 L120-121 | comparison target only (PRINTED["FLUID"]) |
| s² = ½ s_ij s^ij > 0 "the square of the spin density" (eq. 9) | 1007.0587_clean.txt L71-73 | script §7 [fluid_sq] |
| C_fluid (entry 9 form): s² = ⅛(ℏcn)² "for a fluid consisting of fermions with no spin polarization" (eq. 13) | 1007.0587 L88-91 | C3 form target |
| s² = ½ s_ij s^ij > 0 (eq. 7); random orientation kills the gradient term | 1410.3881_clean.txt L79-82 | script §7 |
| C_fluid (entry 11 form): s² = ⅛(ℏc n_f)² (eq. 8), cited to Gas; NuPo | 1410.3881 L83-85 | C3 form target |
| Signature: ϵ = cΠ_i u^i, u^0 = 1, u^α = 0 (comoving), so (+,−,−,−) | 1007.0587 L70, L78-79; 1111.4595v2 L110-111 | script eta = diag(+1,−1,−1,−1) |

## B. Deferred textbook constants, each pinned by a receipted derivation in the script
| constant | derivation in script | printed value |
|---|---|---|
| spin-½ Casimir | §1 [Casimir]: S_k = σ_k/2, su(2) algebra verified, S·S = diag(¾,¾) | 3/4 = s(s+1), s=½ |
| single-particle rest spinor | §3: χ = (cos θ/2, e^{iφ} sin θ/2), ψ = (χ,0); (γ⁰p₀−m)ψ=0 at rest; ψ†ψ = 1; χ†Sχ = n̂/2; n̂·S χ = ½χ | [Dirac_eq], [norm], [spin_expect], [eigen] |
| Σ^k ≡ γ⁰γ^kγ⁵ = γ⁵γ⁰γ^k = diag(σ_k,σ_k) | §2 [Sigma] | verified k=1,2,3 |
| polarized limit, all spins +z | C2: Σ_a s_z = N/2; c-number square N²/4; operator square N²/4 + N/2 = S_tot(S_tot+1), S_tot = N/2; explicit N=2 → 2, N=3 → 15/4 | s_z = n/2, s² = n²/4 (+ n/2 under P1) |
| maximally mixed spin-½ state | §5 [rho_avg],[rho_mixed]: sphere average of \|χ⟩⟨χ\| = ½·1 = ½(\|↑⟩⟨↑\|+\|↓⟩⟨↓\|); Tr(ρS_iS_j) = ¼δ_ij; Tr(ρS·S) = ¾ | ρ = ½·1 |
| unpolarized moments | §5: ⟨n̂_i⟩ = 0, ⟨n̂_i n̂_j⟩ = δ_ij/3 by ∫dΩ/4π | [<n_i>], [<n_i n_j>] |
| units dressing | C3 [dim]: κ(ℏcn)² with κ = 8πG/c⁴ converts to joule/m³ (sympy.physics.units) | (ℏcn)² form |

## C. Derived numbers (all from executed algebra; N particles in volume V, n = N/V; tags in the log)
| quantity | P1 operator-ordered | P2 c-number | tag |
|---|---|---|---|
| single particle \|s\|² (= −s_i s^i) | 3/4 | 1/4 | [P1_single],[P2_single] |
| ⟨(Σ_a S_a)²⟩ unpolarized | 3N/4 | N/4 | [unpol_P1],[unpol_P2] (explicit N=2: 3/2, N=3: 9/4) |
| \|⟨Σ_a S_a⟩\|² unpolarized | 0 | 0 | [square_of_mean] |
| density square ⟨s²⟩, s = (1/V)Σ_a S_a | (3/4) n/V | (1/4) n/V | [density_P1] |
| leading power of n (V=1) | 1 | 1 | [scaling_P1],[scaling_P2] |
| ½ s_ij s^ij with s_ij := s_ijk u^k | = \|s\|² = −s_i s^i, every orientation | same | [IDENTITY],[fluid_N=2_P2] |
| s_ijk s^ijk (full Dirac tensor) | 6\|s\|² | | [full_Dirac_sq] |
| coherent-RMS convention (N·√¾)² | 3N²/4 | | [convention_coherent_P1] |
| coherent-expectation convention (N·½)² | N²/4 | | [convention_coherent_P2] |
| half of that, ½(N/2)² | N²/8 | | [convention_half_coherent_P2] |
