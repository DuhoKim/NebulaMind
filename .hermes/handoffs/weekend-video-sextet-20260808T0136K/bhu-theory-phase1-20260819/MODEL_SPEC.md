# MODEL_SPEC — the strict base model (Track B steps 1–2, frozen before derivation)

**Lana (science seat), 2026-08-19, overnight lane per `PHASE1_BRIEF.md`.** Scope label:
black-hole-universe cosmology is Duho's personal side-interest, not a NebulaMind research
programme. This spec freezes what "the strict model" means; the derivation documents
(`DERIVATION_ω_EVOLUTION.md`, `DERIVATION_TRANSFER_FUNCTION.md`,
`CONFRONTATION_AND_INVERSION.md`) may not redefine anything herein. Where this spec cites a
"standard" formula, the derivation step that uses it must pin it to a fetched primary source
before use (Goru's `GORU_INGREDIENTS.md` feeds this); the spec itself introduces no numbers
beyond already-pinned Phase 0 values. Everything the literature does not supply is a **named
parameter**, never a silent assumption (brief: "a named unknown beats a silent assumption").

## 0. Notation (fixed; avoids the source paper's M/m collision — Track A §2.1)

| Symbol | Meaning |
|---|---|
| M_p | parent black hole mass |
| a★ ∈ [0, 1) | parent dimensionless spin; J_p = a★ G M_p²/c |
| Ω_H | parent horizon angular velocity |
| a(t), a₀ | scale factor of the baby universe; today |
| a_b | scale factor at the bounce (patch-normalized) |
| ω(a) | vorticity (global rotation rate) of the baby universe's matter |
| ω_i | initial vorticity on the post-bounce patch, ω(a_b) |
| ε ∈ [0, 1] | angular-momentum inheritance efficiency through the bounce (A4) |
| Z_x | expansion factors: Z_inf (bounce→end of torsion inflation), Z_rad, Z_mat |
| z_spin | protogalactic spin-acquisition redshift (defined in §4) |
| A | full-sky handedness asymmetry, A = (N_cw − N_ccw)/N (§4 definition frozen) |
| n_era | vorticity decay exponent per era: ω ∝ a^(−n_era) — **to be derived, not assumed** |

## 1. Model definition (Track B step 1)

**M1 — Parent.** A Kerr black hole (M_p, a★) in a parent universe. The only parent properties
the model admits as inheritable are the conserved charges of the collapsing interior: mass and
angular momentum (electric charge set to zero by assumption A0 below).

**M2 — Birth realization.** Torsion bounce of the Popławski/ECSK class inside the horizon
(pinned in the Phase 0 packet: Phys. Lett. B 694, 181; ApJ 832, 96): the collapsing fermionic
matter reaches Cartan-scale density, bounces, and undergoes a finite torsion-driven
quasi-exponential expansion. An agnostic-bounce variant (any nonsingular bounce inside the
horizon) is carried in parallel: every result must state whether it depends on the ECSK
realization or only on "some bounce happened" (tag [ECSK] vs [BOUNCE-AGNOSTIC]).

**M3 — Post-bounce patch.** A closed FRW patch carrying a homogeneous vector-mode
(vorticity) perturbation ω about a fixed axis n̂ inherited from J_p. This is the ONE live
physical object Track A's audit leaves standing (its §3): no Gödel ingredient, no global
rotating frame, no centrifugal dark energy. Rotation enters as a vorticity perturbation on
FLRW, full stop.

**Matching assumptions, enumerated (the honesty core of the spec):**

- **A0** — parent charge Q = 0; realistic astrophysical holes. [BOUNCE-AGNOSTIC; benign]
- **A1** — a single connected closed FRW patch forms interior to the horizon after the bounce.
  Source: ECSK bounce papers (pinned above) assert this for their models. [ECSK; the
  agnostic variant simply postulates it] Confidence: model-dependent, medium.
- **A2** — the patch's matter is the bounced interior matter; no exterior accretion after the
  bounce alters its net angular momentum direction. Confidence: assumption of convenience,
  medium-low; stated, not defended — a later accretion phase would only *add* angular momentum
  along axes uncorrelated with n̂, diluting the signal, so A2 is generous to the model.
- **A3** — the axis survives: the bounce and torsion-inflation phase preserve the *direction*
  n̂ of the net angular momentum (rotational symmetry about n̂ is not broken by the bounce
  dynamics). Confidence: plausible by symmetry, medium; no source computes it.
- **A4 — THE PARAMETERIZED IGNORANCE.** No published matching condition exists for how much
  specific angular momentum crosses an ECSK (or any) bounce: the Phase 0 packet records no
  amplitude anywhere in the family literature, and Track A found none in the v2 full text
  (its row 2: no perturbed metric is ever written). Goru's ingredient sweep must confirm or
  refute this absence; until a source supplies the matching, it is parameterized:
  **ω_i = ε · ω_ref(a_b)**, ε ∈ [0, 1], where ω_ref(a_b) is the pre-bounce interior's
  rotation rate at the bounce scale (A5). ε = 1 means perfect inheritance; ε = 0 means the
  bounce erases rotation. Every downstream result must display its ε dependence explicitly.
- **A5** — the pre-bounce reference rotation is set by the parent's horizon scale:
  ω_ref(bounce) is anchored to Ω_H(M_p, a★) blueshifted/adiabatically mapped to the bounce
  patch — the precise mapping is a derivation task (D-ω step 1, below), with the standard Kerr
  Ω_H formula to be source-pinned there. If the mapping proves underdetermined, its unknown
  factor is absorbed into ε (which is why ε multiplies ω_ref rather than standing alone).
- **A6** — post-bounce history: torsion inflation (expansion factor Z_inf, model-dependent,
  [ECSK]) → radiation era (Z_rad) → matter era (Z_mat to z_spin, then to today). Total
  a₀/a_b = Z_inf·Z_rad·Z_mat. The Z's are parameters chained to the bounce energy scale;
  D-ω must state which are source-pinnable ([ECSK] papers quote e-fold counts) and which
  remain free.
- **A7** — vorticity evolves passively (no vorticity sources after the bounce: no primordial
  magnetic fields, no anisotropic stress regeneration). Generous to the model in the same
  sense as A2 — sources would decohere, not amplify, the axis. Confidence: standard, high.
- **A8** — the baby universe's observed flatness is compatible with the closed patch (the
  patch inflated: |Ω_K| today below observational bounds); the model makes no closure claim
  the data don't (contra the source paper's T 168 claim — Track A row 8).
- **A9** — structure formation is standard ΛCDM apart from the vorticity perturbation; the
  handedness bias enters only through the spin-acquisition physics of §4.

## 2. Initial vorticity (Track B step 2)

Frozen functional form, with every factor labeled:

  **ω_i = ε · Ω_H(M_p, a★) · f_b(bounce mapping)**   [A4, A5]

- Ω_H(M_p, a★): standard Kerr horizon angular velocity — source-pin at derivation time.
  Scaling note for design purposes only (to be verified in D-ω): Ω_H ∝ a★ c³/(G M_p) up to an
  O(1) function of a★, so ω_i is *larger* for smaller parents at fixed a★.
- f_b: the kinematic factor from mapping the horizon-scale rotation onto the bounce patch
  (D-ω step 1 derives it or proves it underdetermined; in the latter case f_b ≡ 1 and the
  uncertainty lives in ε — one knob, not two hidden ones).
- Present-day value (D-ω target): **ω₀ = ω_i · Π_eras (a_b/a₀)^{n_era}**, with each n_era
  derived from vector-mode perturbation theory / angular-momentum conservation and pinned to a
  fetched primary source (brief Track B step 3: "vector modes decay; get the exponent right
  per era, with sources quoted"). This spec deliberately does NOT commit to n_era values —
  Track A receipt R5 used n = 2 (matter/rigid) as an audit device against the paper's own
  premise; the strict model derives its exponents.

## 3. Derivation targets this spec freezes (for the later documents)

- **D-ω (`DERIVATION_ω_EVOLUTION.md`):** (1) the Ω_H → ω_i mapping (or its underdetermination,
  → f_b ≡ 1); (2) n_era per era with primary sources; (3) the inversion ω₀ ↔ ω(z_spin);
  (4) map S1/S2 present-day bounds back to ω(z_spin) — the allowed vorticity at spin
  acquisition.
- **D-T (`DERIVATION_TRANSFER_FUNCTION.md`) — the original step:** tidal-torque theory on an
  FLRW background carrying homogeneous vorticity ω(z_spin) about n̂: derive the parity-odd
  bias of protogalactic angular momenta toward n̂ and hence
  **A = C(z_spin, window) · (ω/H)|_{z_spin}**, with the coefficient C *derived* (not
  Li-normalized), its epoch and mass-window dependence stated, and validity limits declared
  (perturbative in ω/H; breaks if C would exceed O(1)). Every algebraic step sympy-checked
  into `receipts/`. If the TTT-vorticity coupling requires an input no source provides, the
  dead-end is recorded precisely and the missing input becomes a named parameter (brief,
  overnight conduct).
- **D-C (`CONFRONTATION_AND_INVERSION.md`):** A(ω_max) with the derived C against the Phase 0
  certified survey floors (N = 10⁵ design: σ_A = 1/√N ≈ 3.2×10⁻³; all-sky N = 2×10¹²:
  σ_A ≈ 7.1×10⁻⁷ — pinned numbers, Kun-certified 2026-08-18); then the genuinely new
  inversion: S1/S2 → allowed ω₀ → constraint contours in (a★·ε, M_p, {Z}) — "what the CMB
  already says about the black hole we would have been born in." Both the design-floor and
  the sample-complete comparisons are reported; Phase 0's order-of-magnitude bracket serves
  as the sanity band around the derived result, never as the result.

## 4. Frozen observable definitions

- **A (handedness asymmetry):** A = (N_cw − N_ccw)/N over a full-sky spiral sample, where
  "cw" is defined by the sign of the galaxy spin projection onto n̂ (hemisphere convention
  fixed by n̂, not by the observer's north); for a survey covering solid angle W, D-T must
  state the W-dependence of the observable bias (a dipole-like statistic, not a monopole).
- **z_spin:** the epoch window over which protogalactic angular momentum is acquired in TTT
  (to be pinned to the TTT literature in D-T; the spec fixes only that A is evaluated with
  ω/H at that epoch, not today — the epoch mapping is D-ω task 3).
- **Bounds:** S1 (σ_V/H)₀ < 4.7×10⁻¹¹ (95% CI), S2 (ω/H)₀ < 7.6×10⁻¹⁰ (95% CL) — Phase 0
  pins, re-verified at Kun's Phase 0 gate; S2 (looser) is the generous headline choice,
  S1 reported alongside, same convention as the closure note.

## 5. Assumptions ledger (summary)

| # | Content | Tag | Status |
|---|---|---|---|
| A0 | Q = 0 parent | agnostic | benign |
| A1 | closed FRW patch forms | ECSK | source-asserted, medium |
| A2 | no post-bounce net-J accretion | both | convenience, generous direction, medium-low |
| A3 | axis direction survives bounce | both | symmetry-plausible, uncomputed, medium |
| A4 | J-inheritance amplitude unknown → ε | both | **parameterized ignorance (the honest core)** |
| A5 | ω_ref anchored to Ω_H | both | derivation task; residual → ε |
| A6 | Z_inf·Z_rad·Z_mat history | ECSK for Z_inf | partially pinnable |
| A7 | passive vorticity evolution | both | standard, high; generous direction |
| A8 | flatness compatible | both | observational, high |
| A9 | ΛCDM structure formation + vorticity | both | standard, high |

**What this model is NOT (inherited from Track A):** it contains no rotating global frame, no
centrifugal dark energy (Track A rows 16–20 killed that sector), no Kerr-radius metric
correction (row 2, unsupported), and no closed-universe claim (row 8). It is the minimal
honest formalization of the single surviving claim: a bounded, axis-carrying cosmological
vorticity that may bias galaxy handedness.

— Lana, Track B spec, 2026-08-19. Frozen as of this commit; Kun gates
(`KUN_P1_MODELSPEC_GATE.md`) before any derivation document cites it.
