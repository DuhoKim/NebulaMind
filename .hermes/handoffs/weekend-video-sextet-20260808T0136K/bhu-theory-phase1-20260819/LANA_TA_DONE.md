LANA_TRACK_A_COMPLETE

Lana, 2026-08-19 00:39 KST. Deliverables: `TRACK_A_AUDIT.md` (SHA-256 `ed3da496…`) +
`MODEL_SPEC.md` (SHA-256 `6d409813…`), with `sources/` custody and `receipts/` (5 scripts, all
run, all passing).

- **Custody:** arXiv:1910.10819v2 full text fetched from ar5iv 00:31 KST;
  `sources/ar5iv_1910.10819v2.html` pinned `49632249…`, tag-stripped text `71d66161…` (v2
  confirmed by the axis/clockwise material). One new external fetch: the DES paper the source
  itself cites (arXiv:2503.06712 abstract; w = −0.948 +0.028/−0.027 quoted verbatim). All other
  numbers from Phase 0 pins. portal.nersc.gov untouched.
- **Audit result: 23 verdict rows.** CHECK ×8 (all of Eqs. 1–6 reproduce by sympy; spherical
  trig and axis arithmetic reproduce; Kerr radius is dimensionally a length), ERROR ×4,
  UNSUPPORTED ×6, POST-HOC ×3, UNFALSIFIABLE ×1, out-of-scope ×1.
- **Headline 1 (the priority target, verified before claimed):** the paper's own sentence
  "H=(Λ/3)^{1/2}c would thus be equal to Ω" commits it to identification; observed Λ then fixes
  (Ω/H)₀ = 0.828 — **1.09×10⁹ over the Planck Bianchi bound, 1.76×10¹⁰ over Saadeh** (receipt
  lambda_omega_check.py). Converse horn: bound-compliant rotation supplies < 8.5×10⁻¹⁹ of
  observed Λ. The dilemma has no third reading in the text.
- **Headline 2 (new, independent):** the paper's own angular-momentum-conservation premise
  fixes Ω ∝ a⁻² ⇒ rotational dark energy has w = +1/3 — vs the DES value the paper cites as
  support, w = −0.948 ± 0.028: **Δw ≈ 1.28, ~46σ**, and w = +1/3 cannot accelerate at all
  (receipt w_eos_check.py).
- **Headline 3:** the same centrifugal force is used axisymmetrically (bulk-flow section) and
  isotropically (dark-energy section) with a one-sentence unsupported conversion between them.
- **Survivor:** the qualitative CW/CCW claim only, as symmetry reasoning, dependent on none of
  the failed sectors — Phase 0's closure is strengthened, not weakened.
- **MODEL_SPEC.md frozen** (Track B steps 1–2): notation fixed, matching assumptions A0–A9
  enumerated, the angular-momentum inheritance parameterized as ε ∈ [0,1] with the absence of
  any published matching condition stated (Goru's sweep to confirm), ω_i = ε·Ω_H·f_b frozen,
  decay exponents explicitly deferred to derivation with source-pinning required, observable A
  and confrontation/inversion targets frozen.

Next per the brief's gating protocol: fresh Kun session gates Track A
(`KUN_P1_TRACKA_GATE.md`) and the spec (`KUN_P1_MODELSPEC_GATE.md`); Goru's
`GORU_INGREDIENTS.md` feeds the ω-evolution and transfer-function derivations.
