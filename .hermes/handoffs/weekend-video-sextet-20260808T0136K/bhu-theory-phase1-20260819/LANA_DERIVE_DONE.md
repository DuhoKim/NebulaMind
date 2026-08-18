LANA_DERIVATIONS_COMPLETE

Lana, 2026-08-19 02:30 KST. Track B steps 3–5 executed under the frozen MODEL_SPEC (Stage 1
gates verified: PASS_TRACKA_AUDIT, PASS_MODELSPEC via regate). Five new receipts in `receipts/`
(omega_evolution, spherical_collapse, transfer_function, bound_mapping, inversion), all run
tonight, all passing. No new external fetch was needed — every pinned quote came from Goru's
already-saved sources (Malik & Wands 0809.4944; Schäfer 0808.0203), extracted verbatim from the
saved full texts. portal.nersc.gov untouched.

**1. `DERIVATION_OMEGA_EVOLUTION.md`** — SHA-256
`0af85b77f0b383f762e1077e9893e2492e9e55329a2186ea4a13af8fea5a7883`
- δq ∝ a⁻⁴ solved from the pinned Malik–Wands (8.62) with Π=0 (sympy), gauge choice stated.
- Derived exponents: ω ∝ a⁻¹ (radiation), a⁻² (matter and Λ eras); matter-era cross-check
  against angular-momentum conservation passes.
- Inflation era not covered by any pinned source → n_inf ∈ [1,2] parameterized per spec A6.
- Epoch pinned to turnaround via the Schäfer quote; z_ta numerically swept [0.5, 10], not
  cherry-picked; (ω/H)(z_ta) table for both bounds — the mapping is mild (×3.5 across sweep).
- Back-evolution consistency of the bounds flagged into the error budget.

**2. `DERIVATION_TRANSFER_FUNCTION.md`** — SHA-256
`f2da14cd5224f7892cf7e77203fce158e220562df76b8a69da708f3571618e5e`
- The original step (Goru item 3: NOT-FOUND in print): A = C·(ω/H)|_ta with
  C = (4√2/3π)·ξκ_c e^{σ_λ²/2}/μ_λ — headline **C ≈ 7.2**, bracket **[1.4, 12.8]**.
- Sign-bias lemma derived exactly (A = L_ω/L_T, sympy — no small-signal truncation needed);
  log-normal magnitude average done in closed form (⟨1/λ⟩ = e^{σ²/2}/μ_λ, sympy).
- Normalizations pinned verbatim: Schäfer Eq. 63 (λ = ω/ω₀), Eq. 65 (μ_λ ∈ [0.03,0.05],
  σ_λ ∈ [0.5,0.7]); ω₀(ta) = 1.666 H_ta derived from EdS spherical collapse (sympy, 9π²/16 and
  9π²/32 both reproduced symbolically).
- Validity limits and T1–T5 assumptions ledger stated; all un-modeled effects reduce A.

**3. `CONFRONTATION_AND_INVERSION.md`** — SHA-256
`2d662a5fa39dc5ed201437cde50ace3738687f5de9aa86a40501b54489e23e7f`
(as repaired 02:55 KST per `KUN_P1_CONFRONT_GATE.md`; pre-repair hash was `4515c86f…`)
- Strict A at the generous S2 bound: **1.9×10⁻⁸** (fiducial z_ta=3), full sweep ≤ 5.7×10⁻⁸ —
  **5.2–6.4 orders below the design 3σ floor; 0.03σ all-sky; 3σ needs ~12,000 observable
  universes**. Phase 0 closure **strengthened** (strict = 0.04× the generous edge, inside the
  declared bracket); nothing overturned.
- The inversion (Goru item 4: first formulation): CMB bound ⇒ parent allowed only if
  post-bounce spin dilution D > ε·Ω_H/ω_max — **D > 2.5×10³⁰ for a stellar parent (≥27
  e-folds), 2.5×10²² for a supermassive one**; binding (a★,ε) exclusion only for D ≲ 10²³–10³⁰,
  honestly stated as easily satisfied by plausible ECSK histories — the constraint is real,
  quantitative, and currently non-binding; any model pinning D below D_min is already excluded.
- Error budget per link; the one imported formula (Kerr Ω_H) flagged for source-pinning at gate.

Next per the brief: fresh Kun gates per step (`KUN_P1_OMEGA_GATE.md`,
`KUN_P1_TRANSFER_GATE.md`, `KUN_P1_CONFRONT_GATE.md`), then `MORNING_SUMMARY.md` after gating.
External-theorist review remains required before anything is called publishable.

REPAIRS_APPLIED_20260819 — 02:55 KST: the three numbered repairs from
`KUN_P1_CONFRONT_GATE.md` (HOLD_CONFRONT_SWEEP_FIGURES_MISLABELED) applied verbatim to
CONFRONTATION_AND_INVERSION.md: (1) full-sweep shortfall relabeled 5.2–6.7 orders; (2) σ
bracket made single-sweep-consistent, 0.0025–0.08σ across the full (z_ta, C) sweep; (3)
stellar binding crossover tightened to D ≲ 6×10³⁰. Gate items U1 (Kerr Ω_H unpinned) and U2
(ECSK e-folds characterization unpinned) recorded as UNVERIFIED-AT-GATE caveats in the doc's
§4 error budget. No numbers changed; regate scope is the three sentences only (gate's stated
convention). Omega and Transfer gates: PASS (unaffected).
