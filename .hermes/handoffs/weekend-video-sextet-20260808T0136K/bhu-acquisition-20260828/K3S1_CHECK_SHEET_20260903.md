# K3 step 1 — one-page human check sheet (Tori, 2026-09-03 19:3x KST)

**Claim checked:** the unpolarized ensemble average of the square of the spin density of N uncorrelated spin-½ particles scales as n, not n²; the printed closures ⅛(ℏcn)² and ¾n² are conventions; under the paper's own projection the two printed objects coincide, so entry 10's two values conflict by a factor of six.

## A. Inputs (every one pinned)
| # | input | form | pin |
|---|---|---|---|
| 1 | Dirac spin pseudovector | s^i = ½ ψ̄γ^iγ⁵ψ; s_ijk = −e_ijkl s^l | entry 10 `1111.4595v2_poplawski_prd85_clean.txt` L75–77 (Eq. 4) |
| 2 | spin-fluid tensor and s² | s_ijk = s_ij u_k, s_ij u^j = 0; s² = ½ s_ij s^ij | entry 10 L118–119; entry 9 `1007.0587_clean.txt` L71; entry 11 `1410.3881_clean.txt` L79 |
| 3 | printed closure, fluid | s² = ⅛(ℏcn)² "no spin polarization" | entry 9 L90–91; entry 11 L84–85; entry 10 L121 (⅛ n²) |
| 4 | printed closure, Dirac | ⟨s²⟩ = ¾ n² | entry 10 L113–114 |
| 5 | unpolarized ensemble | uniform spin orientation, uncorrelated particles; ρ = ½·1 (maximally mixed: equal weights on two orthogonal states) | prereg §1; derived in each seat's script |
| 6 | spin-½ constants | S_i = σ_i/2; Σ S_i² = ¾·1 (Casimir) | derived in each script (C1) |

## B. Steps, in order, with intermediate results (ℏ = c = 1)
1. Single particle at rest: ⟨S_i S^i⟩ = ¾ (C1, all seats); ⟨S_i⟩ = 0 for ρ = ½·1 (Tr(ρσ_i) = 0).
2. Macroscopic pseudovector density for N particles in V: s_i = (1/V) Σ_A S_i^(A). Its square averaged: (1/V²)[Σ_A ⟨S^(A)·S^(A)⟩ + Σ_{A≠B} ⟨S^(A)⟩·⟨S^(B)⟩] = (1/V²)[N·¾ + 0] = ¾·n/V. **Linear in n.** (Claude verified by explicit 4×4 and 8×8 product states at N = 2, 3.) Square of the mean: 0.
3. Spin-fluid object: with s_ij = s_ijk u^k and s_ijk = −e_ijkl s^l, ½ s_ij s^ij = |s⃗|² identically (Claude; s_ijk s^ijk = 6|s⃗|²). So its unpolarized average is the same ¾·n/V. **Linear in n.**
4. Polarized limit (C2): all spins +z: s_z = n/2, s_i s^i = n²/4 — genuine n² scaling from a nonzero mean.
5. Conventions that manufacture n²: ¾ n² = n²⟨S²⟩ (coherent RMS); ¼ n² = the polarized closure; ⅛ n² = ½·(n/2)²·2 half-fluids (agy) = ¼n²/2 (Claude) = the ε/√6 normalisation (codex) — three different routes, none fixed by inputs 1–2.
6. Deletion probe (C4): removing the orientation average returns step 4 for both objects, as each seat predicted before running.
7. Units (C3): restoring ℏ, c gives (ℏc)²·¾·n/V for the average and (ℏcn)²/4 for the polarized closure; the printed (ℏcn)²/8 form is reproduced only under the step-5 prescriptions.

## C. Final classes
Headline CLOSURE_SCALING_FAILS; both objects CLOSURE_SCALING_FAILS; corollary for entry 10's pair: CLOSURE_CONFLICT (same quantity, ¾ vs ⅛).

## D. Where a critic could disagree (named)
1. **Correlations.** The ensemble is uncorrelated at leading order. A Fermi-statistics exchange term in the four-fermion operator could reintroduce an n²-like piece; excluded by the prereg, named as the next question.
2. **The projection.** Step 3 uses s_ij := s_ijk u^k on the Dirac tensor, which is not of the Hehl–von der Heyde–Kerlick form; a critic who defines the fluid s_ij independently keeps two objects, and then the ⅛ and ¾ laws are two conventions rather than one conflict.
3. **Operator ordering.** ¾ (operator) vs ¼ (c-number square of the bilinear) per particle; C1 fixes the operator reading; the n-scaling conclusion is the same either way.
4. **The unpinned sources.** Gasperini 1986 and Nurgaliev & Ponomariev 1983 may state the prescription behind ⅛; until pinned, "convention" is the strongest word the record can use.
