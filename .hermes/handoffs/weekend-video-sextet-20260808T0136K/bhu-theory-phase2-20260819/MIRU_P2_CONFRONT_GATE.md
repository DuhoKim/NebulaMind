PASS_P2_CONFRONT

# kimi — Phase 2, Track B step-3 gate: the confrontation (second reviewer, fresh one-shot)

Working dir: the bhu-theory-phase2-20260819 lane. Inputs read: PHASE2_BRIEF.md, all three
prior gates (MIRU_P2_STAGE1_GATE.md, MIRU_P2_BOUNCE_GATE.md, MIRU_P2_INHERIT_GATE.md),
KICKOFF_CSEAT_B3_CONFRONT.txt (six binding requirements), P2_CONFRONTATION.md, B3_DONE.md,
P2_DERIVATION_INHERITANCE.md, and the Phase 1 confrontation/receipts where cited. Findings
only; nothing edited; this is the one file written.

## Check 1 — receipts rerun: CONFIRM

`python3 receipts/p2b3_bbn_confront.py` (exit 0): |eps_S/eps_R|(10 MeV) = 1.81e-44
(coherent) / 3.02e-45 (incoherent) vs bound 30 -> margins 1.7e45 / 9.9e45, CONSISTENT.
That is the Omega_S bracket sitting 45.2-46.0 orders under the pinned BBN bound; the
doc's "44-46 orders" and the table's "margin 10^45-10^46" bracket it, low end stated
conservatively. CONFIRM.

`python3 receipts/p2b3_stack.py` (exit 0): Stack A (D >= Z_mat^2 alone): A <= 6.0e-12 (I,
C-bracket top 1.1e-11) / 5.4e-11 (II, top 9.6e-11); vs all-sky 1-sigma floor 8.5e-6 /
7.6e-5. Stack B: A <= 6.3e-77 (I) / 5.7e-76 (II) at 10 Msun; 1e9 Msun supermassive
omega_0 <= 2.66e-85. Gate-corrected slivers recomputed in-receipt: 5.1e-13 (I) /
2.9e-13 (II matched-input, per inherit-gate nit N2). Every headline number reproduced.
CONFIRM.

## Check 2 — the new pin: CONFIRM

- Pin exists: sources/ar5iv_1006.4166.html; one shasum invocation:
  `f99cd41924258887be309706fe2dc4fd58de34f666b983fafe83a885f781fe22` — byte-identical to
  the hash recorded in P2_CONFRONTATION.md section 2. MATCH.
- Verbatim quote grep-extracted from the pinned text: "Models that lead to a cosmological
  stiff fluid component, with a density [rho_S] that scales as [a^-6] ... have been
  proposed recently in a variety of contexts" (abstract; math in MathML) and
  "we obtain the bound \rho_{S10}/\rho_{R10}<30" (Eq. 9 region, alttext confirmed twice),
  with the 4He + WMAP7 eta = 6.2e-10 provenance in the surrounding sentence as the doc
  states. VERBATIM CONFIRMED.
- DOI live-verified against api.crossref.org (the only host fetched at this gate):
  10.1103/PhysRevD.82.083501 -> Physical Review D, volume 82, published 2010-10-01,
  title "Big bang nucleosynthesis with a stiff fluid", authors Dutta, Scherrer.
  Journal/volume/year match the citation. CONFIRM.
- Sign caveat: stated at section 2 where the bound is used ("the bound is derived for a
  *positive* stiff component; the torsion term is *negative*...") and applicability is
  argued on magnitude grounds ("At 44+ orders below the bound's magnitude, the
  distinction is academic ... the row's CONSISTENT verdict is a magnitude statement"),
  not assumed. At a 10^45 margin the magnitude argument is sound — any expansion-rate
  perturbation of either sign at 10^-44 relative size is invisible to BBN. CONFIRM.

## Check 3 — confrontation table audit: CONFIRM

Eight rows present (lines 36-43), enumerating exactly the kickoff requirement-1 list:
Omega_S bracket; both treatments' bounce states; eps_max with M^(-2/3) scaling; the
polarization sliver; the frozen-ratio shear result; the M->size channel; the mandated
stack. Each row carries a derived value (or an explicit "a condition, not an amplitude" /
state-named dash where the quantity is not a number), a pinned bound or an explicit
UNTESTABLE / CONSISTENCY-ONLY / NOT-AN-OBSERVABLE / CONDITION status, the treatment fork
where a fork exists (rows 1-5, 8; rows 6-7 are treatment-independent statements — the
frozen-ratio theorem is exponent-level and the M->size map comes from the exact interior,
so no fork applies), and V-markers per row (row 6 explicitly "V2-independent").
Zero UNCONFRONTED-NO-PINNED-BOUND rows, as required.

Bound-citation sweep (grep): every bound cited in the doc resolves to a pin — the
Dutta & Scherrer pin (verified above) or Phase 0/1 pins named with paths. Spot-verified
at the cited paths (two required, four done):
- S2 rotation bound omega_max,0 = 1.66e-27 s^-1:
  ../bhu-theory-phase1-20260819/CONFRONTATION_AND_INVERSION.md line 49. EXISTS.
- Floors sigma_A = 3.16e-3 (design; 3-sigma 9.5e-3) and 7.07e-7 (all-sky, N = 2e12),
  C = 7.19 [1.36, 12.78]: phase1 receipts/bound_mapping_receipt.py lines 6-11; receipt
  rerun reproduces fiducial A = 1.91e-08, matching the doc's "Phase 1's generous-bound
  signal ... was A ~ 1.9e-8". EXISTS.
- Omega_H(10 Msun, 0.7) = 4.144e3 s^-1 and (1+z)^2/E(z) = 3.5044 at z_ta = 3 (doc's
  "mapping factor 3.50"): phase1 KUN_P1_CONFRONT_GATE.md lines 35/41-42 and
  KUN_P1_OMEGA_GATE.md line 54, both gate-passed artifacts. EXISTS.
CONFIRM.

## Check 4 — headline audit: CONFIRM, with nit N1

The headline paragraph is FIRST (section 0, before the table), and states plainly: "No
finite-amplitude signature of the Poplawski chain survives at observable magnitude." It
names conditions V1 (Planck regime), V2 (undischarged averaging), and the underived
production-step heuristic behind the axis-memory UNDETERMINED. Softening scan of the doc
and B3_DONE.md (grep: could be / detectable / potentially / might be / within reach /
future observ / prospect / marginal / in principle observ): ZERO hits. No sentence
anywhere claims more than the headline; the two "structural escapes" named in section 7
are framed as what would settle open caveats, not as survivals. No quiet upgrades found
to quote.

N1 (non-blocking): the headline does not name "Reading 1", and the string "Reading"
appears NOWHERE in P2_CONFRONTATION.md — yet row 4's eps_max and both stacks inherit
B2's Reading-1 conditionality (P2_DERIVATION_INHERITANCE.md section 2.2: the ceiling
applies if the homogeneous bounce is demanded of a rotating parent; under Reading 2 the
rotating-parent scenario is UNDERIVED entirely). A2/A7 is named in section 4's Stack-B
premise but not in the headline paragraph. Direction-of-effect check: this cuts AGAINST
survival — under Reading 2 there is even less signal, so no number, row, or verdict
changes, and the omission is conservative. Recorded as a nit per this lane's discipline;
PHASE2_SUMMARY.md should restate the Reading-1 conditionality in one sentence so the
phase headline's chain of conditions is self-contained.

## Check 5 — stack logic attack: CONFIRM

Stack A generosity, inequality by inequality (receipt p2b3_stack.py docstring + code):
D >= Z_mat^2 alone takes the SMALLEST allowed dilution (largest omega_0); dropping
Z_rad, Z_inf >= 1 slackens further toward survival; eps_max applied as the roof on the
(eps f_b) product per the B2 A5 row; z_eq = 3400 flagged as a standard-value assumption;
C-bracket tops (1.1e-11 / 9.6e-11) reported alongside the headline-C values so the full
envelope is visible — even the tops sit 10^-4 of the floor. Every inequality slackens
toward survival. GENUINELY GENEROUS.

Stack B premise: J_b <= xi M c R_b is verbatim the B2-derived ceiling
(P2_DERIVATION_INHERITANCE.md line 81, v_rot < c self-consistency of the homogeneous
bounce); post-bounce angular-momentum conservation with NO dilution is the
survival-maximal extreme and is named as spec rows A2/A7 in section 4 — the premise is
the one the B1/B2 lane derived and named, not a new invention. The I_today choice
(closed 3-sphere at critical density) is argued conservative (Hubble-volume-only inertia
would raise omega_0). CONFIRM.

Noise-floor comparison: the "10^-5 of the floor" claim uses the sample-complete all-sky
counting floor sigma_A = 7.07e-7 (N = 2e12 galaxies), pinned to Phase 0/1
(bound_mapping_receipt.py, "Phase 0 certified" floors) with the N assumption explicit in
the pin. This is the strongest admissible floor ("there are no more galaxies than all of
them"); a named-instrument figure could only be weaker. PINNED, ASSUMPTION EXPLICIT.

## Check 6 — requirements sweep, quoted evidence: CONFIRM

1. Eight rows, fork + V-markers per row: quoted/audited in Check 3. KEPT.
2. Gate-1 condition 1 closed as a named, pinned, Crossref-verified publication with
   verbatim quotes; excluded Goru quotes stated excluded (section 2: "The excluded Goru
   quotes remain excluded"). CLOSED.
3. Stack quantified with receipts, both forms, gate-corrected slivers (5.1e-13 /
   2.9e-13) used, not the doc-rounded ones: Check 1 rerun. KEPT.
4. Frozen-ratio kept as a condition: section 5 — "Axis memory: UNDETERMINED, in both
   directions. This is a condition on any future claim, not a number: it neither adds an
   amplitude to row 8 nor rescues one, and this document does not convert it." KEPT.
5. Headline first, plain, unsoftened, V-markers traveling (section 6 per-row marker
   summary): KEPT, modulo nit N1 above.
6. No new observables: line 45-46 — "No new observables were invented at this step
   (requirement 6); rows 1-8 exhaust the derived quantities of steps 1-2 plus the
   mandated stack." Fetches: host grep of the doc yields only ar5iv.org and
   api.crossref.org (plus the "portal.nersc.gov untouched" disclaimer sentence); this
   gate's own single fetch was api.crossref.org only. Writes: lane dir only. KEPT.

## Nits recorded (non-blocking; neither touches a number or verdict)

N1: "Reading 1" conditionality on the eps_max ceiling (and hence on both stacks' quoted
magnitudes) is not restated anywhere in P2_CONFRONTATION.md, and A2/A7 is named in
section 4 but not in the headline paragraph. Conservative direction (Reading 2 forbids
more); PHASE2_SUMMARY.md should carry the one-sentence restatement.

N2: B3_DONE.md states Stack B as "A <= 6x10^-77 (I)"; the receipt computes 6.3e-77 — the
DONE file rounds the bound tighter than computed (5% overstatement of the ceiling's
tightness). P2_CONFRONTATION.md itself says 6.3e-77 / <= 1e-76 correctly. Cosmetic, in
the handoff file only; direction immaterial at 70 orders.

## UNVERIFIED-AT-GATE

None. All six checks completed inside the time box; one network fetch total
(api.crossref.org, permitted).

## Gate decision

PASS_P2_CONFRONT. The headline survives an adversarial read: both receipts reproduce
every number on rerun; the one new pin hashes byte-identical, quotes verbatim, and
Crossref-matches its citation with the sign caveat argued where used; all eight rows are
confronted with pinned bounds or explicit statuses and zero unpinned citations; the
stacks are genuinely generous in the survival direction and rest on the B2-derived
premise; the frozen-ratio condition is never converted to a number. Two conservative-
direction nits recorded for the summary to absorb. The phase headline — no
finite-amplitude signature survives at observable magnitude — is gated for Duho.

— kimi, second reviewer, Track B step-3 gate, Phase 2, 2026-08-19. One file written.
api.crossref.org the only host fetched. portal.nersc.gov untouched.
