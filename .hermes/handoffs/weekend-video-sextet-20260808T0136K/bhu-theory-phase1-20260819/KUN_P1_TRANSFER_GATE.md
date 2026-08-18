PASS_DERIVATION_TRANSFER

Gate: KUN_P1_TRANSFER_GATE (Phase 1, D-T transfer-function gate per PHASE1_BRIEF.md gating
protocol)
Reviewer: Miru, second reviewer. Date: 2026-08-19. Findings-only; no file other than the three
gate files written. Local files only; grep extraction only on sources; receipts rerun with
python3 (sympy 1.14.0, python 3.9.6); independent recomputes in one python call each.
Target: DERIVATION_TRANSFER_FUNCTION.md against PHASE1_BRIEF.md and frozen MODEL_SPEC.md.

## Check 1 — receipt reruns (python3, unmodified)

`python3 receipts/spherical_collapse_receipt.py` (R7):
  rho_patch/rho_bar at turnaround = 9 pi^2/16 = 5.5517; equals 9 pi^2/16: True
  (GM/R_ta^3)/H_ta^2 = 9 pi^2/32 = 2.7758; sqrt = 1.66608; equals 9 pi^2/32: True
  -> doc ingredient (iv): omega_0(ta) = sqrt(9 pi^2/32) H = 1.666 H_ta. CONFIRM, symbolic.

`python3 receipts/transfer_function_receipt.py` (R8):
  (a) A = mu/L (exact for mu <= L)          -> doc §2 sign-bias lemma. CONFIRM, symbolic.
  (b) <1/lambda> = exp(s^2/2)/mu_l: True    -> doc §2 log-normal average. CONFIRM, symbolic.
  (c) C = 4*sqrt(2)*kappa*xi*exp(s^2/2)/(3*pi*mu_l) — symbolically identical to the doc §0
      frozen form C = (4 sqrt(2)/3 pi) xi kappa_c e^{sigma^2/2} / mu_lambda. CONFIRM.
  headline C = 7.18583 (xi=2/5, kappa=1, sigma=0.6, mu=0.04)  -> doc "C approx 7.2". CONFIRM.
  bracket [1.36026, 12.78070]                                 -> doc "[1.4, 12.8]". CONFIRM
      at stated rounding (1.36 -> 1.4 at 1 dp; the downstream receipt R9 carries the precise
      1.36/12.78, so no precision is lost in the chain).

## Check 2 — pinned verbatim quotes (grep extraction only on sources/0808.0203.html)

- Ingredient (i) EdS growth: "angular momentum grows at first order and linearly in time in
  Einstein-de Sitter universes" grep-verbatim, count 1. CONFIRM.
- Ingredient (i) epoch: turnaround quote ("Tidal torquing is effective until the moment of
  turn-around ... accumulated until turn-around.") grep-verbatim, count 1. CONFIRM.
- Ingredient (ii) Schafer Eq. (63): "corresponds to the ratio between the observed angular
  velocity of a galaxy omega and the angular velocity needed for rotational support omega_0"
  grep-verbatim (count 1), and the equation alttext
  "\lambda=\frac{\omega}{\omega_{0}}=\frac{L/(MR^{2})}{\sqrt{GM/R^{3}}}" exists exactly.
  Text + equation both character-exact with the doc quote. CONFIRM.
- Ingredient (iii) Schafer Eq. (65): "find lambda to be approximately log-normal distributed"
  (count 1) and the ranges "0.03\leq\mu_{\lambda}\leq 0.05" and "0.5\leq\sigma_{\lambda}\leq
  0.7" both grep-present; the doc's "[...]" marks the elided clause. CONFIRM.
- Ingredient (ii) inertia convention: "an estimate of the inertia of the protohalo"
  grep-verbatim, count 1. CONFIRM.
- §3 supporting quote: "linear growth with cosmic time until turn-around, and continues
  quasi-linearly until shell crossing" grep-verbatim (the doc's quoted fragment "quasi-
  linearly until shell crossing" is contiguous). CONFIRM.
- Custody: shasum -a 256 sources/0808.0203.html = b84bc0c5... (doc pin prefix MATCH).

## Check 3 — independent recompute (one python call, no receipt import)

C(xi, kappa, sigma, mu) = (4 sqrt(2)/(3 pi)) xi kappa exp(sigma^2/2)/mu:
  headline (2/5, 1, 0.6, 0.04) = 7.1858        -> doc 7.2            CONFIRM
  low  (0.2, 0.5, 0.5, 0.05)  = 1.3603         -> doc bracket 1.4    CONFIRM (stated rounding)
  high (0.5, 1.0, 0.7, 0.03)  = 12.7807        -> doc bracket 12.8   CONFIRM
Assembly identity: 4 sqrt(2)/(3 pi) = 0.600211 = 1/sqrt(9 pi^2/32) = 1/1.66608 — the R7
collapse factor and the R8 C-form are mutually consistent (C carries 1/omega_0 correctly).
CONFIRM.
Validity-limit figure (doc §4 item 1): L_omega/L_T = (xi kappa/lambda)(omega/omega_0) at the
bound-allowed omega (z_ta = 3, S2) = (0.4/0.04)(2.663e-9/1.666) = 1.6e-8 ~ 1e-8 — "deep
inside" the exact-linear regime. CONFIRM.

## Check 4 — assumptions ledger and spec compliance (brief check 5)

- T1-T5 ledger present (doc §5), each row carrying a status ("exact by symmetry", "derived;
  bracketed", "pinned verbatim", "assumption, stated", "pinned"). CONFIRM.
- Ledger header explicitly "extends MODEL_SPEC A0-A9"; nothing in the spec is redefined.
  CONFIRM.
- Epoch and mass-window dependence stated (§3: C epoch-independent in EdS, tens-of-percent
  shift at z_ta <~ 1 inside the bracket); validity limits stated (§4, five items, including
  the perturbative bound and the decoherence direction). Per the frozen spec D-T target.
  CONFIRM.
- Brief-mandated dead-end check answered in writing (§5): the one source gap (vorticity
  through the bounce) is assigned to the inversion chain where it is parameterized, not to
  this transfer function. CONFIRM.
- Novelty basis matches Goru item 3 verbatim ("no explicit analytic transfer function from
  global rotation omega to a galaxy spin handedness bias magnitude exists in print").
  CONFIRM against GORU_INGREDIENTS.md.

## Check 5 — overclaim sweep

grep -i "prove|falsif|first-ever|first form|exclude|rule out|kill|refut|overturn" on
DERIVATION_TRANSFER_FUNCTION.md: no hits. CONFIRM.

## Verdict basis

All briefed checks pass: both receipts rerun and match (symbolic collapse numbers, exact
sign-bias lemma, exact log-normal average, symbolic C identical to the doc's frozen form);
every Schafer quote (Eq. 63 text + equation, Eq. 65 + parameter ranges, EdS growth, inertia,
turnaround, shell-crossing) is character-exact in the pinned local source; the headline 7.2
and bracket [1.4, 12.8] reproduce independently; the T1-T5 ledger, validity limits, and the
dead-end statement satisfy the frozen spec; no overclaim language. One non-binding note: the
printed bracket low end 1.4 is a 1-dp rounding of 1.36; the precise value is carried in R9.
No UNVERIFIED-AT-GATE items; every check completed inside the time box.

— Miru (second reviewer), 2026-08-19. Sibling gates: KUN_P1_OMEGA_GATE.md,
KUN_P1_CONFRONT_GATE.md.
