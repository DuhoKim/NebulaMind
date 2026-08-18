HOLD_CONFRONT_SWEEP_FIGURES_MISLABELED

Gate: KUN_P1_CONFRONT_GATE (Phase 1, D-C confrontation/inversion gate per PHASE1_BRIEF.md
gating protocol)
Reviewer: Miru, second reviewer. Date: 2026-08-19. Findings-only; no file other than the three
gate files written. Local files only; grep extraction only on sources; receipts rerun with
python3 (python 3.9.6); independent recomputes in one python call each.
Target: CONFRONTATION_AND_INVERSION.md against PHASE1_BRIEF.md and frozen MODEL_SPEC.md.

Every headline number, both receipts, the strengthens-not-overturns claim, the assumptions
display, and the overclaim sweep PASS (Checks 1-5 below). The gate HOLDs on three mislabeled
sweep figures in §1 and §3(b) — all conservative-direction, none touching a conclusion —
plus two UNVERIFIED-AT-GATE items recorded with reasons (Check 6). Numbered repairs at the end.

## Check 1 — receipt reruns (python3, unmodified): ALL CONFIRM

`python3 receipts/bound_mapping_receipt.py` (R9):
  fiducial z_ta=3, S2, headline C: A = 1.91e-8        -> doc §1 table 1.9e-8        CONFIRM
  z=1: 1.221e-8 [2.3e-9,2.2e-8]; z=10: 3.226e-8 [6.1e-9,5.7e-8]
                                                     -> doc §1 table rows          CONFIRM
  5.0e+05x short (5.7 orders) vs 9.5e-3 design floor -> doc "5x10^5 (5.7 orders)"   CONFIRM
  significance 0.027 sigma all-sky                   -> doc "0.027 sigma"           CONFIRM
  strict/generous = 0.037 vs 5.2e-7 edge             -> doc "0.037", "0.04x"        CONFIRM
  N for 3 sigma = 2.45e16 = 1.2e4 universes          -> doc "2.5e16", "12,000"      CONFIRM
`python3 receipts/inversion_receipt.py` (R10):
  omega_max,0 (S2) = 1.660e-27 s^-1                  -> doc §3 "1.66e-27"           CONFIRM
  10 Msun, a*=0.7: D_min = 2.496e30, ln D = 70.0     -> doc "D > 2.5e30 (ln > 70)"  CONFIRM
  1e9 Msun, a*=0.7: D_min = 2.496e22                 -> doc "D > 2.5e22"            CONFIRM
  Z_mat^2 = 1.16e7                                   -> doc "1.2e7"                 CONFIRM
  early factors 2.16e23 / 2.16e15                    -> doc "2.2e23 / 2.2e15"       CONFIRM
  N_inf > 26.9 / 17.7 e-folds                        -> doc "27 / 18 e-folds"       CONFIRM

## Check 2 — independent recomputes (one python call each, no receipt import): ALL CONFIRM

(a) A at S2, fiducial z_ta=3: (1+z)^2/E(z) = 3.5044 (Omega_m = 0.315); omega/H = 2.663e-9;
    A = 7.1858 x 2.663e-9 = 1.914e-8 -> doc 1.9e-8. CONFIRM.
(b) Floor figures: gap 9.5e-3/1.914e-8 = 4.96e5 = 5.70 orders; 1.914e-8/7.07e-7 = 0.0271
    sigma; N = 9/A^2 = 2.46e16 = 1.23e4 observable universes; strict/generous 0.0368.
    All CONFIRM.
(c) D thresholds with independent constants (G, c, Msun, H0 = 67.4 km/s/Mpc):
    Omega_H(10 Msun, 0.7) = 4.144e3 s^-1 -> D_min = 2.496e30; Omega_H(1e9 Msun, 0.7) =
    4.144e-5 s^-1 -> D_min = 2.496e22; early factors 2.16e23 / 2.16e15; N_inf 26.9 / 17.7.
    All CONFIRM.
(d) Error-budget brackets (doc §4): C x[0.19, 1.8] recomputes to [0.189, 1.777]; z_ta
    x[0.49, 1.7] recomputes to [0.486, 1.685]; "S1 16x tighter" = 16.17. All CONFIRM.

## Check 3 — strengthens-not-overturns (brief check 4): CONFIRM, provenance verified locally

- Phase 0's declared bracket exists in the Phase 0 packet (sibling directory, local):
  ../bhu-theory-phase0-20260818/LANA_PHASE0_SCOPING.md line 118: "A in [~1e-12, ~5e-7]";
  restated in BHU_ROTATION_HANDEDNESS_CLOSURE_20260818.md line 106; Kun-certified edge
  5.24e-7 (KUN_PHASE0_GATE.md line 70). Doc's "5.2e-7 generous edge" matches the certified
  value. CONFIRM.
- Strict A = 1.9e-8 lies inside [1e-12, 5e-7]; the full (z_ta, C) sweep [1.76e-9, 5.74e-8]
  also lies inside. Nothing overturned; the derived result lands 0.037x the generous edge
  ("1.4 orders below the generous edge": log10(1/0.0368) = 1.43). CONFIRM.
- Phase 0's "18 universes short" figure exists (LANA_PHASE0_SCOPING.md line 127:
  3.6e13 / 2e12 = 18). CONFIRM.
- Certified floors re-verified in the Phase 0 packet: sigma_A(N=1e5) = 3.16e-3, 3-sigma
  9.5e-3; sigma_A(2e12) = 7.07e-7; S1 = 4.7e-11, S2 = 7.6e-10, Omega_m = 0.315, 2e12
  galaxies (KUN_PHASE0_GATE.md lines 36, 74, 79; KUN_CLOSURE_GATE.md lines 45, 48, 80).
  All CONFIRM.

## Check 4 — assumptions and honesty (brief check 5): CONFIRM

- n_inf in [1,2], Z_rad, Z_inf unpinned appear in the §4 error budget as named parameters
  "displayed in D_min form, not hidden" (spec A6); f_b absorbed in epsilon per spec A5;
  z_eq = 3400 flagged "standard value, not load-bearing". Inflation-era ignorance is
  parameterized and quarantined to the inversion, exactly as spec A6 requires. CONFIRM.
- The one imported formula (Kerr Omega_H) is openly self-flagged in the doc for
  source-pinning at this gate — declared, not silent. See Check 6 item U1.

## Check 5 — overclaim sweep (brief check 6): CONFIRM, no violation

grep -i "prove|falsif|first-ever|first form|exclude|rule out|kill|refut|overturn":
- "Nothing is overturned" / "sample-complete kill deepens" — kill refers to the Phase 0
  detection-route closure, not to any parent model. In-bounds.
- "Goru item 4: first formulation" — matches GORU_INGREDIENTS.md item 4's own wording
  ("We will be the first to formulate the inversion"). Goru-backed novelty wording. In-bounds.
- "any future model that pins its dilution below D_min ... is already excluded by Planck.
  That is a falsifiable statement about model space" — a conditional threshold statement
  about hypothetical future models, i.e. exactly the dilution threshold the kickoff permits;
  §3's honest reading explicitly says the bound does NOT meaningfully constrain (a*, epsilon)
  for plausible histories. No existing parent is claimed excluded; "falsifiable" is
  meta-language, not "falsified". In-bounds.
No "proves", no "falsified", no "first-ever" anywhere in the document.

## Check 6 — FAIL items and UNVERIFIED-AT-GATE

F1 (§1): "5.2-6.4 orders across the full (z_ta, C) sweep" — mislabeled. Independent recompute
  of the full sweep (z_ta in [0.5, 10], C in [1.36, 12.78], S2): the shortfall is 5.22-6.73
  orders. The 6.4 figure is the TOP OF THE FIDUCIAL-z C-BRACKET (5.45-6.42), not the full
  sweep. Conservative direction (understates the gap); conclusion unaffected; factually
  mislabeled as "full sweep".
F2 (§1): "(bracket 0.005-0.08 sigma)" — mixed provenance. 0.005 is the fiducial-z C-bracket
  bottom (0.0051); 0.08 is the FULL-SWEEP top corner (0.081). Consistent pairings are:
  fiducial C-bracket 0.005-0.048; full sweep 0.0025-0.08. As printed, the two endpoints come
  from two different sweeps. Conservative/mixed; conclusion unaffected.
F3 (§3(b)): "binding (below 1) for D ~< 1e30 (stellar) / 1e23 (supermassive)" — the R10
  converse recomputes the crossovers at 6.1e30 (stellar) and 6.1e22 (supermassive). The
  stellar "~< 1e30" understates the binding reach by ~0.8 dex (supermassive is acceptable at
  order-of-magnitude). Conservative direction for the doc's point (constraint is weak);
  precision repair.
U1 UNVERIFIED-AT-GATE: the Kerr Omega_H formula carries no fetched primary-source pin (the
  doc itself flags it: "flagged for source-pinning at Kun's gate — the only imported formula
  in this document"). Constraint: local files only; no fetched Kerr source exists in this
  directory, and the gate may not fetch. Mitigating: the formula is exercised numerically in
  R10 and independently in Check 2(c); it is the standard horizon form
  a*c^3/(2GM(1+sqrt(1-a^2))), dimensionally correct. Declared openly — not a silent
  assumption. Not held on this; recorded per the kickoff's UNVERIFIED-AT-GATE rule.
U2 UNVERIFIED-AT-GATE: "ECSK torsion-bounce inflation is generically quoted at tens of
  e-folds" — a literature characterization with no fetched pin in this directory. Hedged
  ("generically"), qualitative, and the doc's own confidence line marks the inversion's
  numeric bite "low ... which is itself the finding". Not load-bearing for any quantitative
  number (the D_min values stand alone). Recorded, not held.

## Numbered repairs to clear this HOLD (all one-line text edits in D-C; no number changes)

1. §1: replace "5.2-6.4 orders across the full (z_ta, C) sweep" with the recomputed full-sweep
   figure "5.2-6.7 orders across the full (z_ta, C) sweep" (or re-scope the sentence to the
   fiducial z_ta = 3 C-bracket, "5.4-6.4 orders").
2. §1: make the sigma bracket single-sweep-consistent — either "(bracket 0.005-0.048 sigma
   across the C bracket at fiducial z_ta = 3)" or "(bracket 0.0025-0.08 sigma across the
   full (z_ta, C) sweep)".
3. §3(b): tighten the stellar binding threshold to the recomputed crossover, "binding for
   D ~< 6e30 (stellar)" (supermassive "~< 1e23" may stand).

Regate scope after repair: the three sentences only; Checks 1-5 stand as passed and are not
re-litigated (same convention as KUN_P1_MODELSPEC_REGATE.md).

— Miru (second reviewer), 2026-08-19. Sibling gates: KUN_P1_OMEGA_GATE.md (PASS),
KUN_P1_TRANSFER_GATE.md (PASS).
