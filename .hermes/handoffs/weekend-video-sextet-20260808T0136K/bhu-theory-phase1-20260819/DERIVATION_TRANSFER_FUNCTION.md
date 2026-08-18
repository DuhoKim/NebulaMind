# D-T — the transfer function: A = C·(ω/H)|_ta, derived (Track B step 4, the original step)

**Lana (science seat), 2026-08-19, under frozen `MODEL_SPEC.md`.** Scope label: black-hole-
universe cosmology is Duho's personal side-interest, not a NebulaMind research programme.
Novelty basis: Goru item 3 (NOT-FOUND — "no explicit analytic transfer function from global
rotation ω to a galaxy spin handedness bias magnitude exists in print"); we derive it here.
Receipts: `receipts/spherical_collapse_receipt.py` (R7),
`receipts/transfer_function_receipt.py` (R8). Pinned source: Schäfer, IJMPD 18, 173 (2009),
`sources/0808.0203.html` SHA-256 `b84bc0c5…` (Goru item 2), verbatim quotes extracted from the
saved full text tonight.

## 0. Result

  **A = C · (ω/H)|_ta**,  **C = (4√2/3π) · ξ κ_c e^{σ_λ²/2} / μ_λ**  (R8, symbolic)

  Headline **C ≈ 7.2** (ξ = 2/5, κ_c = 1, σ_λ = 0.6, μ_λ = 0.04); honest bracket
  **C ∈ [1.4, 12.8]** (R8). A is the frozen spec observable (N_cw − N_ccw)/N with hemispheres
  defined by n̂.

## 1. Ingredients, each pinned or derived

**(i) TTT angular momentum of a protohalo, and when it freezes.** Schäfer §3.1, verbatim:
> "the angular momentum grows at first order and linearly in time in Einstein-de Sitter
> universes"
and (epoch): "Tidal torquing is effective until the moment of turn-around […] After the
collapse, the halo conserves the angular momentum it has accumulated until turn-around."
So both angular-momentum components are evaluated at turnaround, and the comparison is frozen
there.

**(ii) The magnitude normalization — Schäfer Eq. (63), verbatim:**
> "λ corresponds to the ratio between the observed angular velocity of a galaxy ω and the
> angular velocity needed for rotational support ω₀: λ = ω/ω₀ = (L/(MR²))/√(GM/R³)"
i.e. **L_TTT = λ · MR² · ω₀** with ω₀ = √(GM/R³) — the review's own inertia convention (MR²,
"an estimate of the inertia of the protohalo", its §3.3).

**(iii) The λ distribution — Schäfer Eq. (65), verbatim:**
> "find λ to be approximately log-normal distributed […] with the parameters
> **0.03 ≤ μ_λ ≤ 0.05 and 0.5 ≤ σ_λ ≤ 0.7**"
(The review's separate remark that *disks* reach λ ≈ 0.5 does not enter: both L components
below are protohalo-level, and the disk inherits them proportionally — assumption T4.)

**(iv) Rotational-support rate at turnaround — derived, not cited (R7, sympy):** EdS spherical
collapse (cycloid solution) gives ρ_patch/ρ̄ = 9π²/16 at turnaround and hence
  **ω₀(ta) = √(GM/R_ta³) = √(9π²/32) · H(t_ta) = 1.666 H(t_ta)**.

**(v) The vorticity-induced component — derived.** A patch embedded in flow rotating with
angular velocity ω_ang about n̂ carries solid-body angular momentum
  **L_ω = ξ M R² ω_ang**,  ξ = 2/5 (uniform sphere; profile dependence bracketed ξ ∈ [0.2, 0.5]),
  ω_ang = κ_c ω_bound with **κ_c ∈ [1/2, 1]** the vorticity-vs-angular-velocity convention
  bracket (GR congruence vorticity equals the local rotation rate, κ_c = 1; fluid-dynamics
  vorticity ∇×v = 2Ω would give κ_c = 1/2; the Bianchi analyses' ω is taken as the congruence
  convention, headline κ_c = 1, both carried).

## 2. The sign-bias lemma (the parity-odd step, exact)

Model: each protohalo's total L = L_T + L_ω n̂, where L_T is the TTT component with isotropic
direction (exact in the absence of vorticity: no preferred direction exists) and magnitude
L_T = λ MR² ω₀ drawn from (iii); L_ω is coherent along n̂. The observable counts spins by the
sign of L·n̂.

For fixed magnitude L_T: Y ≡ L_T·n̂ = L_T cosθ with cosθ uniform on [−1, 1], so Y is uniform on
[−L_T, L_T], and

  A = P(Y > −L_ω) − P(Y < −L_ω) = 1 − 2F_Y(−L_ω) = **L_ω/L_T**  — *exact* for L_ω ≤ L_T (R8a,
  sympy; no small-signal truncation was needed — linearity is exact under the uniform-cosθ law).

Averaging over the log-normal magnitude distribution (R8b, sympy: ⟨1/λ⟩ = e^{σ_λ²/2}/μ_λ):

  A = L_ω ⟨1/L_T⟩ = (ξ κ_c / (e^{−σ_λ²/2} μ_λ)) · (ω/ω₀)|_ta.

With (iv), ω₀ = 1.666 H_ta:

  **A = [4√2 ξ κ_c e^{σ_λ²/2} / (3π μ_λ)] · (ω/H)|_ta ≡ C (ω/H)|_ta.**   (R8c)

## 3. Coefficient, epoch dependence, uncertainty

- **C = 7.2 headline; C ∈ [1.4, 12.8]** from the labeled brackets (ξ, κ_c, μ_λ, σ_λ — R8c).
  The epoch dependence of A is carried entirely by (ω/H)(z_ta) (D-ω §3): C itself is
  epoch-independent in EdS because both ω₀ ∝ H_ta and the collapse geometry are self-similar;
  at z_ta ≲ 1 where Ω_m(z) < 1 the EdS collapse numbers shift at the tens-of-percent level —
  inside the bracket.
- **Direction of un-modeled effects — all reduce A.** Post-turnaround mergers and nonlinear
  torques randomize spin directions (decoherence); misidentification noise in any real
  classifier dilutes A further; the L_TTT growth "quasi-linearly until shell crossing"
  (Schäfer §6.1) means L_T is if anything *larger* than the turnaround value used. The derived
  A is therefore an **upper bound within the model**, which is the conservative direction for
  a closure test.

## 4. Validity limits (stated per the brief)

1. Linear response: exact for L_ω ≤ L_T; at the bound-allowed ω, L_ω/L_T ~ 10⁻⁸ — deep inside.
2. Isotropic-TTT assumption: exact at zeroth order in ω; the first correction (tidal-vorticity
   cross term) is O(ω/H) relative and cannot compete with the retained term.
3. EdS collapse used at z_ta ≥ 1 (Ω_m(z) ≈ 1 there); z_ta sweep in D-ω covers the residual.
4. Tidal randomization dominates (A → below the derived value) whenever post-turnaround merger
   spin-flips are common — N-body-calibrated decoherence would only lower A; not modeled,
   direction stated.
5. Convention and profile factors carried as brackets, not chosen silently (ξ, κ_c).

## 5. Assumptions ledger (extends MODEL_SPEC A0–A9)

| # | Content | Status |
|---|---|---|
| T1 | TTT direction isotropic in absence of vorticity | exact by symmetry |
| T2 | vorticity enters as coherent solid-body L_ω = ξMR²κ_cω | derived; ξ, κ_c bracketed |
| T3 | magnitudes: Schäfer Eq. 63/65 normalization and distribution | pinned verbatim |
| T4 | disk inherits halo L components proportionally (ratio preserved) | assumption, stated; standard j_disk ∝ j_halo reasoning |
| T5 | both components frozen at turnaround | pinned (Schäfer §3.3 quote) |

**The dead-end check the brief required:** no genuinely underivable input appeared —
the one place a source gap existed (vorticity through the bounce) belongs to the inversion
chain (D-ω §2, n_inf), not to this transfer function, and it is parameterized there.

— Lana, D-T, 2026-08-19. Gate: `KUN_P1_TRANSFER_GATE.md` expected.
