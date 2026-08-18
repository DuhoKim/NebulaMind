# Morning summary — Phase 1 overnight (assembled 2026-08-19 03:01 KST)

Everything below is gated. Chain: Track A audit (PASS_TRACKA_AUDIT) → MODEL_SPEC
(PASS_MODELSPEC, after a citations repair) → ω-evolution (PASS_DERIVATION_OMEGA) →
transfer function (PASS_DERIVATION_TRANSFER) → confrontation/inversion (PASS_CONFRONTATION,
after three one-line label repairs). Gates by Miru after Kun's Nous sessions proved unreliable
(one 400 at ~100K context, one read-loop — both in the fault log); every gate reran the receipts.

## Track A — the base paper does not survive adversarial audit

arXiv:1910.10819v2, full text pinned. 23 verdict rows: 8 CHECK, 4 ERROR, 6 UNSUPPORTED,
3 POST-HOC, 1 UNFALSIFIABLE, 1 out-of-scope.

1. **The Λ-identification dilemma.** The paper's own sentence commits Λ = 3Ω²/c² as an
   identification; observed Λ then fixes (Ω/H)₀ = 0.828 — 1.09×10⁹ over the Planck Bianchi
   bound, 1.76×10¹⁰ over Saadeh. Converse horn: allowed rotation supplies < 10⁻¹⁸ of Λ.
   No third reading exists in the text.
2. **The w = +1/3 contradiction (new).** The paper's own angular-momentum-conservation premise
   forces Ω ∝ a⁻², making its "rotational dark energy" behave as w = +1/3 — which cannot
   accelerate, and sits ~46σ from the DES w = −0.948 the paper itself cites as support.
3. Centrifugal force used axisymmetrically in one section and isotropically in another, with an
   unsupported one-sentence conversion.
- **Survivor:** only the bare qualitative CW/CCW symmetry claim, which depends on none of the
  failed sectors.

## Track B — the strict model, built and gated

- **MODEL_SPEC** frozen: parent Kerr (M_p, a★), ε ∈ [0,1] inheritance, ω_i = ε·Ω_H·f_b,
  A0–A9 assumptions enumerated, decay exponents derivation-pinned.
- **ω(a) derived** (not assumed): a⁻¹ (radiation), a⁻² (matter/Λ), from Malik–Wands (8.62),
  sympy-solved; inflation parameterized (no pinned source exists); z_ta swept [0.5, 10].
- **The transfer function — first in print (Goru novelty check: NOT-FOUND):**
  A = C·(ω/H)|_ta with **C = (4√2/3π)·ξκ_c·e^{σ²/2}/μ_λ ≈ 7.2, bracket [1.4, 12.8]** —
  the derived replacement for Phase 0's borrowed Li-1998 linearity.
- **Strict confrontation:** A = 1.9×10⁻⁸ at the generous bound (fiducial z_ta = 3; ≤ 5.7×10⁻⁸
  across the full sweep) → **0.027σ all-sky; 3σ needs ~2.5×10¹⁶ galaxies ≈ 12,000 observable
  universes.** Phase 0's closure is **strengthened** (strict result = 0.04× its generous edge,
  inside the declared bracket). Nothing overturned.
- **The inversion — also first (NOT-FOUND in print):** the CMB rotation bound translated to the
  parent: post-bounce spin dilution must exceed **2.5×10³⁰ (stellar parent) / 2.5×10²²
  (supermassive)** — a real but weak constraint, easily satisfied by plausible bounce
  histories, and stated exactly that honestly.

## Standing caveats

External-theorist review still required before any publication claim; two UNVERIFIED-AT-GATE
items are recorded in the confrontation doc's error budget; inflation-era behavior is
parameterized, not derived. The spin-parity measurement is untouched by all of this.

## Overnight fault log additions

Nous kimi-k3: 400s a reused session near ~100K context; separately, a fresh session entered a
one-line-per-read crawl loop on a large fetched file (cancelled at 262K context). Standing
rules now: one gate per session; grep extraction only; time-boxed checks; Miru is the reliable
gate route tonight (five clean gates).
