PASS_DERIVATION_OMEGA

Gate: KUN_P1_OMEGA_GATE (Phase 1, D-omega derivation gate per PHASE1_BRIEF.md gating protocol)
Reviewer: Miru, second reviewer. Date: 2026-08-19. Findings-only; no file other than the three
gate files written. Local files only; grep extraction only on sources; receipts rerun with
python3 (sympy 1.14.0, python 3.9.6); independent recomputes in one python call each.
Target: DERIVATION_OMEGA_EVOLUTION.md against PHASE1_BRIEF.md and frozen MODEL_SPEC.md.

## Check 1 — receipt reruns (python3, unmodified)

`python3 receipts/omega_evolution_receipt.py` (R6):
  (8.62) with Pi=0 solves to C1/a(eta)**4, dq ∝ a^-4: True          -> doc §2 (8.62 -> a^-4) CONFIRM
  matter (rho ∝ a^-3): v ∝ a^-1, omega ∝ a^-2                      -> doc n_mat = 2          CONFIRM
  radiation (rho+P ∝ a^-4): v ∝ a^0, omega ∝ a^-1                  -> doc n_rad = 1          CONFIRM
  matter-era cross-check L ∝ 1 (constant)                          -> doc §2 cross-check     CONFIRM

`python3 receipts/bound_mapping_receipt.py` (R9):
  (w/H)(z_ta) at S2: 0.5->1.293e-9, 1->1.698e-9, 2->2.256e-9, 3->2.663e-9, 5->3.300e-9,
  10->4.487e-9  -> doc §3 table (1.29/1.70/2.26/2.66/3.30/4.49 e-9) CONFIRM, all six rows.
  S1 column: A@S1/C gives 8.0e-11, 1.05e-10, 1.39e-10, 1.65e-10, 2.04e-10, 2.77e-10
  -> doc §3 S1 column CONFIRM.

## Check 2 — pinned verbatim quotes (grep extraction only on sources/)

- Malik-Wands (8.61), sources/0809.4944.html: alttext
  "{\delta q}_{i}=(\rho+P)(v_{{\rm vec}i}-S_{i})" exists immediately above tag "(8.61)".
  Character-exact with doc §1 quote. CONFIRM.
- Malik-Wands (8.62): alttext
  "{\delta q}_{i}^{\prime}+4{\cal H}\delta q_{i}=-\nabla^{2}\Pi_{i}" immediately above tag
  "(8.62)". Character-exact with doc §1 quote. CONFIRM.
- MW prose: fragments "can be supported only by divergence-free momenta, but even then",
  "8.62) shows that the vector perturbations", "redshifted away by the Hubble expansion on
  large scales unless", "driven by an anisotropic stress" all grep-present (each count 1) in
  order. Existence CONFIRM. NON-BINDING NOTE (not a repair): the source sentence opens
  "Equation (8.63) shows that vector metric perturbations ..." (grep -A2); the doc quotes from
  "vector metric perturbations" onward without a leading "[...]" ellipsis, where the same
  reviewer's regate standard treated marked elisions as fair. Fragment itself is verbatim and
  contiguous; recommend a leading "[...]" for exactness. Content claim (decay per 8.62) is
  unaffected.
- Turnaround-epoch quote, sources/0808.0203.html: "Tidal torquing is effective until the
  moment of turn-around in the spherical collapse picture, because the collapse dramatically
  reduces the lever arms. After the collapse, the halo conserves the angular momentum it has
  accumulated until turn-around." grep-verbatim, count 1. Character-exact with doc §3. CONFIRM.
- Custody: shasum -a 256 sources/0809.4944.html = 2a9d652e... (doc pin prefix MATCH);
  sources/0808.0203.html = b84bc0c5... (doc pin prefix MATCH).

## Check 3 — independent recompute (one python call, no receipt import)

ODE power bookkeeping verified numerically: with dq ∝ a^-4 and omega = v/(ax),
d ln omega / d ln a = -1.0 (radiation, rho+P ∝ a^-4) and -2.0 (matter, rho+P ∝ a^-3);
matter-era L(a=2)/L(a=1) = 1.0. Matches doc n_rad = 1, n_mat = 2. CONFIRM.
Epoch mapping (omega/H)(z) = (omega/H)_0 (1+z)^2/E(z), E^2 = 0.315(1+z)^3 + 0.685 (Phase 0 pin
S3, Omega_m = 0.315, re-greped in Phase 0 packet KUN_PHASE0_GATE.md line 36): at z = 3,
(1+z)^2/E = 3.5044, giving 2.663e-9 at S2 — doc value 2.66e-9. CONFIRM.
Doc §3 asymptotic "(1+z)^{1/2}/sqrt(Omega_m) for z >> 1" algebraically correct. CONFIRM.
Doc §3 "varies by x3.5" across the sweep: 4.487e-9/1.293e-9 = 3.47. CONFIRM.
Doc §3 flag on bound back-evolution consistency: stated as an assumption for the D-C error
budget, with direction ("cannot bridge a 5.7-order gap"). Present and honest. CONFIRM.

## Check 4 — assumptions and inflation-era honesty (brief check 5)

- Spec A7 (Pi = 0) invoked explicitly at doc §1 with the generous-direction rationale. CONFIRM.
- Inflation row (doc §2 table): "not covered by any pinned source ... n_inf in [1,2]
  parameterized per spec A6" — the inflation-era parameterization is named, ranged, and its
  non-coverage by Goru's sweep is stated. No silent exponent. CONFIRM.
- Doc §4: forward confrontation uses only bound-allowed omega(z_ta), no bounce parameters;
  the unpinned n_inf enters only the inversion. Ignorance is quarantined from the
  confrontation. CONFIRM. Spec A0-A9 not redefined anywhere in the document. CONFIRM.

## Check 5 — overclaim sweep

grep -i "prove|falsif|first-ever|first form|exclude|rule out|kill|refut|overturn" on
DERIVATION_OMEGA_EVOLUTION.md: no hits. CONFIRM.

## Verdict basis

All briefed checks pass: both receipts rerun and match every claimed number; both Malik-Wands
equations and the turnaround quote are character-exact in the pinned local sources; the
derived exponents reproduce independently; the z_ta table and sweep claims recompute exactly;
the inflation-era ignorance is parameterized and quarantined per spec A6; no overclaim
language. One non-binding presentational note (leading-ellipsis on the MW prose fragment).
No UNVERIFIED-AT-GATE items; every check completed inside the time box.

— Miru (second reviewer), 2026-08-19. Sibling gates: KUN_P1_TRANSFER_GATE.md,
KUN_P1_CONFRONT_GATE.md.
