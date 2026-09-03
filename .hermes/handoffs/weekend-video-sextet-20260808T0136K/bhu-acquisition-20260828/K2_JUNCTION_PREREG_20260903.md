# K2 pre-registration — does the closed-FRW interior join its exterior without a shell? A junction-classification theorem at the Pathria/Gaztañaga boundary (entries 1, 4, 5, 22, 56)

**Tori, 2026-09-03 16:26 KST. Ordered by Duho ("a", relay via Blanc 16:24 KST) on the round-2 topic packet. Written and committed BEFORE any
derivation. Gated by a fresh seat via `nm_referee_dispatch.sh` (agy, ACCESS PROVEN, `K2_PREREG_GATE_agy.md`: PREREG_SOUND_WITH_REPAIRS, six repairs applied 16:34 KST). Paper HOLD; nothing outward; tiers untouched.**

## 0. Why this exists
Three obstruction papers and one construction paper leave the same door open. Entry 4 (Knutsen 2009): smooth matching of an
FLRW interior to a vacuum exterior at Pathria's boundary forces a static sphere — "shell-bearing junctions not excluded"
(`BHU_CORPUS_SYNTHESIS_20260902.md` L114–116; surviving narrowed no-go per `ENTRY4_THIRD_SEAT_ADJUDICATION.md`, ruling
DOMAIN_NARROWER). Entry 5 (Khakshournia 2010): at the maximum-expansion surface identified with the horizon the null junction
is not smooth, [K_uu] ≠ 0, so it carries a pressure-only null shell p = ρa/4; "shell-bearing realizations … not excluded"
(synthesis L117–121; source `khakshournia_2010_note_pathria_arxiv1412.0105_clean.txt` L49–55, L137–140). Entry 22 (Easson
2026), Proposition 2: no-shell closed daughters with nondegenerate matching 0<ψ_b≤π/2 to a static asymptotically flat
finite-ADM parent cannot extend to arbitrarily large scale factor — they recollapse; shells are outside the result (source
`2606.25023_clean.txt` L740–748; domain narrowed to this limb by Duho 09-03 14:33). Entry 56 (Gaztañaga 2023): a finite
top-hat, ρ(τ,χ)=ρ(τ) for χ≤χ*, 0 outside, "local FLRW solution with empty space outside", a boundary at r_S = 2GM_T
(source `gaztanaga_mass_mnras_clean.txt` L147–160; the non-flat case declined at L138–141); its boundary closure is a
borrowed input (`WARRANT_TABLE_20260903.md` row 56, `W_DIRECTION_ASSUMED`, ruled (a) 16:11). Nobody has classified the
junctions. This study does, and either exhibits an expanding realization or proves none exists.

## 1. Objects, every symbol bound
- **Interior:** FRW dust, ds² = −dτ² + a(τ)²[dχ² + S_k(χ)² dΩ²], k ∈ {+1, 0} (the metric form is a textbook object; its receipt is pinned at step 1); ρ(τ) = ρ₀ a⁻³ (entry 56 L141: "matter-dominated
  universe with ρ = ρ₀a⁻³"). Λ ≥ 0 allowed as a parameter (entry 5's range 0 ≤ Λ ≤ Λ_c, synthesis L117).
- **Exterior:** Schwarzschild–de Sitter with the same Λ: F(R) = 1 − 2GM/R − ΛR²/3 (textbook form, receipt pinned at step 1; Λ=0 gives Schwarzschild, entry 56's case).
- **Boundary Σ:** three candidate placements, all computed. (B1) comoving timelike surface χ = χ* = const (entry 56's top-hat
  edge; entry 22's "comoving no-shell" matching surface ψ_b). (B2) the maximum-expansion surface χ = π/2 of the k=+1 interior
  identified with the exterior horizon F(R)=0 — Pathria's identification, entry 5's null junction. (B3) a general timelike
  surface χ = χ*(τ) (entry 56 L150–153 needs χ* a function of time to keep M_T constant).
- **Junction formalism:** Israel (timelike/spacelike) and Barrabès–Israel (null), as entry 5 uses (source L49–55). Surface
  stress-energy S_ab from the jump [K_ab]; "no shell" ⇔ [K_ab] = 0 with the induced metrics matching.
- **Mass relation:** the Pathria dust-mass relation as stated in entry 1's source (to be quoted with a line receipt at step 1;
  the prereg fixes only that the exterior M equals the interior dust mass inside Σ).

## 2. The question, exactly
For each placement B1–B3, k ∈ {+1, 0}, Λ ≥ 0: does an EXPANDING (ȧ > 0 on Σ) solution exist with (i) no shell, or (ii) a
shell whose S_ab satisfies the weak and dominant energy conditions? Report the full classification, not a single case.

## 3. Outcome classes — declared now
- **J_SMOOTH_EXPANDING:** an expanding no-shell junction exists in some (placement, k, Λ) cell. If it is the comoving
  Oppenheimer–Snyder-type matching at B1, say so explicitly and state whether it lies inside Easson's Prop. 2 domain (then it
  recollapses and Prop. 2 is confirmed, not refuted).
- **J_SHELL_EXPANDING:** expanding realizations exist only with a shell; report S_ab, its sign, and which energy conditions it
  meets. A shell violating the dominant energy condition in every expanding cell is reported as J_SHELL_UNPHYSICAL.
- **J_NONE:** no expanding realization in any cell, smooth or shelled with an energy-condition-respecting S_ab — a theorem
  with stated hypotheses (this owns what entries 4, 5, 22 leave open).
- **J_UNDETERMINED:** the classification depends on a shell equation of state the energy conditions do not fix → INCONCLUSIVE
  (state the residual freedom exactly).
Each cell of the (placement × k × Λ) table gets one class; the headline is the class of the cell entry 56 actually uses (B1,
k=0, Λ=0) and of Pathria's cell (B2, k=+1, 0≤Λ≤Λ_c).

## 4. What counts as a verdict either way
A closed-form S_ab per cell (symbolic) with the energy-condition inequalities evaluated, OR an explicit expanding no-shell
solution with its matched first and second fundamental forms displayed. A verdict that rests on a numerical example must
be reproduced symbolically or reported as J_UNDETERMINED.

## 5. Controls (must pass before any class is filed)
- **C1 positive control:** at B1 with k=+1, Λ=0, the computation must reproduce the textbook Oppenheimer–Snyder smooth
  matching (the dust-mass relation of the form M ∝ ρa³S_k(χ*)³, entry 56 states it at source L143, "M = 4/3 π χ³ ρ₀"; the textbook form is pinned at step 1). Failure = the pipeline is wrong, stop.
- **C2 entry-5 control:** at B2 the null-junction jump must reproduce Khakshournia's [K_uu] and the pressure p = ρa/4
  (independently re-derived 09-03 by the set-E seat: [K_uu] = −2πρa, `WARRANT_5_claude.md`). Failure = the pipeline is wrong, stop; no class is filed.
- **C3 entry-4 control:** the smooth timelike matching at Pathria's boundary r_b = 1 (Pathria's own coordinate value, receipt pinned at step 1 from entry 1's source) must reproduce the static-sphere result. Failure = the pipeline is wrong, stop; no class is filed.
- **C4 deletion probe:** remove the energy-condition test and confirm the class of at least one cell changes (the control
  asserts an exact failure, per `reference_controls_assert_exact_failure_set`).

## 6. Seat plan, blind double, cost
- Two seats compute the full table independently (codex and the Claude seat; computer algebra, each its own script committed
  with its result; results written only when complete). A split on any cell → third seat via `nm_referee_dispatch.sh`.
- Tori verifies one equation per placement by hand or sympy before filing.
- Cost (seat planning estimates, not corpus results): three to eight seat-days (a planning estimate, not a corpus number); no data; no compute beyond a laptop.

## 7. What would make it INCONCLUSIVE
J_UNDETERMINED in the headline cells; or C1–C3 failing after two independent attempts; or the Pathria mass relation quoted at
step 1 admitting more than one reading (then both are run and reported).

## 8. Non-circularity
No CMB statistic, no observed value, enters. Inputs are the metrics and the junction formalism. The known results (OS matching,
entries 4, 5, 22) are CONTROLS, not conclusions.
