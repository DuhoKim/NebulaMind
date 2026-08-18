HOLD_GORU_ITEMS12_NO_CITATIONS

Gate: KUN_P1_MODELSPEC_GATE (Phase 1, MODEL_SPEC freeze gate per PHASE1_BRIEF.md gating protocol)
Reviewer: Miru, second reviewer (documented alternate seat; Kun's session cancelled — read loop).
Date: 2026-08-19. Findings-only; nothing outside this file and its sibling gate file was edited.
No web fetches performed; all checks against the local files MODEL_SPEC.md and GORU_INGREDIENTS.md.

## Part 1 — MODEL_SPEC.md: ALL SPEC-SIDE CHECKS PASS
- A0-A9 present: all ten matching assumptions enumerated in section 1 (A0 parent Q=0; A1 closed
  FRW patch; A2 no post-bounce net-J accretion; A3 axis direction survives; A4 inheritance
  amplitude parameterized; A5 omega_ref anchored to Omega_H; A6 Z_inf*Z_rad*Z_mat history;
  A7 passive vorticity; A8 flatness compatible; A9 LambdaCDM + vorticity) and mirrored in the
  section 5 ledger. CONFIRM.
- epsilon in [0,1] defined: section 0 notation table ("epsilon in [0, 1] | angular-momentum
  inheritance efficiency through the bounce (A4)") and A4 itself ("omega_i = epsilon *
  omega_ref(a_b), epsilon in [0, 1]"), with endpoint semantics stated (1 = perfect inheritance,
  0 = bounce erases rotation). CONFIRM.
- omega_i = epsilon * Omega_H * f_b with symbols fixed: section 2 freezes verbatim
  "omega_i = epsilon * Omega_H(M_p, a_star) * f_b(bounce mapping) [A4, A5]"; every factor is
  fixed in the section 0 notation table (epsilon, Omega_H, M_p, a_star) or defined in section 2
  (f_b, including the f_b = 1 fallback with the residual absorbed into epsilon). CONFIRM.
- Decay exponents deferred-with-pinning: notation table marks n_era "to be derived, not
  assumed"; section 2 states the spec "deliberately does NOT commit to n_era values" and
  requires each exponent "derived ... and pinned to a fetched primary source", explicitly
  disowning the audit-device n = 2 used in receipt R5. CONFIRM.
- Observable frozen: section 4 freezes A = (N_cw - N_ccw)/N with the hemisphere convention
  tied to n-hat, the z_spin evaluation rule (omega/H at spin acquisition, not today), and the
  S1/S2 bound values with the S2-headline convention. CONFIRM.
- Inversion targets frozen: section 3 D-C freezes the inversion S1/S2 -> allowed omega_0 ->
  constraint contours in (a_star * epsilon, M_p, {Z}), with both survey-floor comparisons
  (sigma_A = 3.2e-3 design; 7.1e-7 sample-complete) and the Phase 0 bracket demoted to sanity
  band. CONFIRM.

## Part 2 — GORU_INGREDIENTS.md: ITEMS 1-2 FAIL THE CITATION REQUIREMENT
- Items 1-2 (vorticity decay ∝ a^-2; TTT L ∝ a^2 dD/dt): carry NO citations. Neither item
  names an author, year, title, venue, or arXiv/DOI identifier. Item 1 cites only the generic
  label "standard cosmological perturbation theory"; item 2 cites only "TTT" and
  "Einstein-de Sitter universe". There is nothing to "accept without re-fetching" — the
  citation titles the gate instruction allows me to accept are absent, not unverified.
  (This is recorded as a straight FAIL of the briefed check, not UNVERIFIED-AT-GATE: verifying
  absence required no fetch, only reading the delivered file.)
- Items 3-4 (novelty checks): DO state search coverage — item 3 lists four explicit search
  terms ("rotating universe galaxy spin", "vorticity chirality galaxies", "parity-odd spin
  correlations primordial vorticity", "Li 1998 global rotation galaxy spin bias") and item 4
  lists two ("constraint CMB rotation bounds primordial angular momentum parent", "CMB rotation
  parent black hole spin"), each with a NOT-FOUND verdict. PASS for items 3-4.

## Why this binds the model-spec gate
MODEL_SPEC.md's own preamble requires that every "standard" formula "be pin[ned] to a fetched
primary source before use" and names GORU_INGREDIENTS.md as the feed for those pins. The two
un-cited items are exactly the load-bearing imports of the next two derivations: the a^-2
vector-mode decay law (D-omega, which the spec refuses to commit to until source-pinned) and
the L ∝ a^2 dD/dt growth relation (D-T, the transfer-function step). Letting the derivations
start on un-pinned ingredients would reproduce, one level down, the silent-assumption failure
the brief's overnight-conduct clause exists to prevent. The block is procedural, not
scientific: both scalings are plausibly standard, but the gate brief requires the citations to
be present in the ingredients file.

## To clear this HOLD
Goru (or Lana) adds primary-source citations (title plus identifier) to GORU_INGREDIENTS.md
items 1 and 2; re-gate is then a re-read of that file only — Part 1 above stands.

— Miru (second reviewer), 2026-08-19. Sibling gate: KUN_P1_TRACKA_GATE.md (PASS_TRACKA_AUDIT).
