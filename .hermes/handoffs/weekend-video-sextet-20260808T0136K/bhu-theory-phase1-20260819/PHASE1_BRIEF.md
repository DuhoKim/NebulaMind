# PHASE 1 — adversarial audit of the base paper + the strict base model

Hwao (director), 2026-08-19 00:29 KST. Duho, verbatim (00:15): **"not that theoretical, i
expected you scrutinize the base paper more critical and adversarial to build strict base
model"**, then (00:25): **"please use this night to do that"**. This lane runs overnight,
autonomously, at that standard.

Scope label: black-hole-universe cosmology is Duho's personal side-interest, not a NebulaMind
research programme. External-theorist review remains required before anything here is called
publishable; tonight's bar is *internally rigorous and adversarially gated*.

## What Phase 0 was NOT (the standard correction)

Phase 0 was triage: kill criteria + order-of-magnitude arithmetic on Li 1998's borrowed
normalization with an assumed linear coupling. Its conclusion is probably robust (4+ orders of
margin), but nothing in it was *derived by us*. Tonight replaces the assumption with a
derivation, and subjects the base paper itself to referee-grade dissection. Order-of-magnitude
devices are henceforth sanity brackets around derived results, never the result.

## TRACK A — adversarial audit of arXiv:1910.10819v2 (the rotating-parent axis paper)

Custody first: fetch the v2 full text (ar5iv), save under `sources/`, pin SHA-256. Then a
claim-by-claim table. Every checkable statement gets one of:
**CHECK** (reproduced — show the reproduction) / **ERROR** (with the corrected version) /
**UNSUPPORTED** (assumed, no derivation) / **POST-HOC** (fitted from cited data) /
**UNFALSIFIABLE-AS-STATED**. No verdict by rhetoric; every one carries a recomputation or a
quoted absence.

Minimum audit list (extend as the text demands):
1. The Kerr-radius "correction scale" a = M/mc to the FLRW metric — dimensional check, and
   whether any derivation connects it to a metric perturbation at all.
2. **Λ = 3Ω²/c² — the priority target.** If the paper identifies the observed cosmological
   constant with rotation, then measured Λ ≈ 1.1×10⁻⁵² m⁻² would FIX Ω = c·√(Λ/3) ≈ 1.8×10⁻¹⁸
   s⁻¹ — roughly nine orders of magnitude ABOVE the Planck/Saadeh rotation bounds pinned in
   Phase 0. If that reading survives scrutiny (check signs, units, whether the paper means it as
   an identification or an upper-bound analogy), the paper is internally inconsistent with
   isotropy data by ~10⁹ and Track A's headline finding writes itself. Verify carefully before
   claiming it; this is exactly the kind of result that must not be frozen from a misreading.
3. The rotating-frame force law m·Ω²·ρ — Newtonian rotating-frame mechanics applied to
   cosmological scales: state what a GR treatment (Bianchi/Gödel-class or vector perturbations)
   would replace it with, and whether any conclusion survives the replacement.
4. The fitted preferred axis (α = 197° ± 47°, δ = 34° ± 3°) — POST-HOC by the packet's audit;
   verify from the text and note which datasets it leans on (the contested spin catalogs).
5. The core qualitative claim (CW/CCW counts should differ) — trace its logical dependence:
   which of 1–3 does it actually require? Does any failure above kill it, or does it survive as
   pure symmetry reasoning?
6. Internal consistency sweep: units, signs, limits (Ω→0 recovers FLRW?), and whether the
   paper's own numbers are mutually compatible.

Deliverable: `TRACK_A_AUDIT.md` + `LANA_TA_DONE.md` (first line `LANA_TRACK_A_COMPLETE`).

## TRACK B — the strict base model (built in-house)

The model the source never wrote down, constructed minimally and honestly:

1. **Definition.** Parent Kerr black hole (mass M, spin a*). Birth realization: torsion bounce
   (Popławski class) or agnostic bounce matching — enumerate every matching assumption
   explicitly; where the literature gives no matching condition, SAY SO and parameterize the
   ignorance (an efficiency ε ∈ [0,1] on angular-momentum inheritance) rather than hide it.
2. **Initial vorticity.** ω_i on the post-bounce FRW/Bianchi patch as a function of (M, a*, ε).
3. **Evolution.** Derive ω(a) through radiation and matter eras from angular-momentum
   conservation / vector-mode perturbation theory. Verify the scaling against fetched primary
   literature (vector modes decay; get the exponent right per era, with sources quoted). Map the
   present-day bounds (S1/S2, already pinned) back to the spin-acquisition epoch.
4. **Transfer function — the original step.** Tidal-torque theory in a weakly rotating
   background: derive the parity-odd handedness bias A as a function of ω at the protogalactic
   spin-acquisition epoch — the derived replacement for Li's normalization. Result shape:
   A = C · (ω/ω_ref) with C and its epoch-dependence DERIVED, plus validity limits. sympy-check
   every algebraic step; numerical sanity via python.
5. **Confrontation and inversion.** A(ω_max) against survey floors (Phase 0's certified floor
   numbers) with the derived coefficient. Then the inversion that is genuinely new: translate
   the CMB rotation bounds into a constraint on the parent's (a*, ε) — "what the CMB already
   says about the black hole we would have been born in."
6. **Error budget + assumptions ledger.** Every assumption numbered, every imported result
   source-quoted, confidence stated per link.

Deliverables: `MODEL_SPEC.md` (steps 1–2 committed before derivations begin — the spec freezes
what "the strict model" means so derivations can't drift), then `DERIVATION_ω_EVOLUTION.md`,
`DERIVATION_TRANSFER_FUNCTION.md`, `CONFRONTATION_AND_INVERSION.md`.

## Gating protocol (per-step, not end-of-night)

- Fresh Kun session per gate (Nous 400s reused sessions near ~100K context — fault log). Miru
  (`MOONSHOT_API_KEY=$(cat ~/.hermes/moonshot.key) hermes chat --provider moonshot -m kimi-k3
  -Q -q`) is the alternate if Nous fails twice.
- Gate points: Track A audit; MODEL_SPEC; ω-evolution derivation; transfer function;
  confrontation/inversion. Verdict files `KUN_P1_<STEP>_GATE.md`, first line PASS/HOLD tokens.
- Goru runs the ingredient/prior-art sweep in parallel BEFORE the transfer-function derivation:
  vorticity evolution in FRW (primary sources), TTT foundations, and any existing
  vorticity→spin-bias derivation in print (if one exists, we build ON it with citation, not
  around it). Deliverable `GORU_INGREDIENTS.md` + `GORU_ING_DONE.md`.
- Every number fetched and quoted; nothing from memory. sympy/python receipts saved under
  `receipts/`. `portal.nersc.gov` untouched (harvest paused until 12:00, then live).

## Overnight conduct

Chain autonomously via watchers; report only verdicts, blockers, and the morning summary
(major notifications only). If a derivation step dead-ends honestly (e.g., the TTT-vorticity
coupling needs an input no source provides), record the dead-end precisely and continue with the
parameterized version — a named unknown beats a silent assumption. Morning deliverable: the
gated audit, the frozen model spec, and however many derivation links passed their gates, plus
`MORNING_SUMMARY.md`.
