# Entry-11 deep audit — reconciliation (Tori, 2026-09-02, STEP 3, queue draw #1)

**Entry 11 — N. J. Popławski (2016), "Universe in a black hole in Einstein–Cartan gravity," ApJ 832, 96**
(arXiv 1410.3881). Tier **CONSISTENCY-ONLY**. Brief `ENTRY11_AUDIT_BRIEF_20260902.md`.

## Verdict — BOTH SEATS AGREE, tier holds; no MUST-STOP
| seat | token |
|---|---|
| codex (`ENTRY11_codex_RESULT.md`) | `AUDIT_HOLDS_CONSISTENCY_ONLY` |
| claude-seat (`ENTRY11_claude_RESULT.md`, blind, re-derived eqs. 13/20/21/26/28 and recomputed every printed number) | `AUDIT_HOLDS_CONSISTENCY_ONLY` |

## What both derived independently (Tori verified the citations and the arithmetic)
1. **The bounce is derived inside the stated background model** (Friedmann eq. with the spin term
   −αn_f² ∝ a⁻⁶ overtaking radiation ∝ a⁻⁴; T_max, τ, |H|_max, a_min all reproduce), but it rests on three
   cited-not-derived closures: the Papapetrou point-particle spin fluid (line 67), random-spin averaging
   (line 82), and s² = (ħc n_f)²/8 (lines 84–85). The author defers the beyond-point-particle treatment
   (line 361).
2. **Of the abstract's five adjectives, only "nonsingular" is derived, and only within the ansatz.** "Closed"
   is k = +1 written into the metric (line 93) and justified by citation (line 121); homogeneity/isotropy are
   the FLRW ansatz with a one-sentence assertion that the interior "becomes more" so near a bounce (line 122);
   "nearly flat" is the bounce-epoch Ω_min − 1 = 4cτ/a_i, never propagated to a present-day Ω_k.
3. **Silent input in eq. (29):** Ω_min − 1 = 5.7×10⁻³⁶ and N_max ≈ 10⁵² require a_i ≈ 1 m
   (Tori: 4cτ/a_i = 5.70×10⁻³⁶ at a_i = 0.999 m), whereas the paper's own "typical stellar" a_i = 10⁴ m
   (line 198) gives 5.7×10⁻⁴⁰. Both seats found this independently. Neither number reaches an observable.
   claude-seat also notes the exponent at line 187 (N ≈ (Ω−1)⁻³) should read −3/2 given N ≈ (ȧ/c)³ and
   Ω − 1 = c²/ȧ² (Tori: agreed). Typos, no conclusion affected.
4. **The exponential phase depends on a free constant:** K = β(κε̃)² is chosen as "the simplest form"
   (lines 298–301), β_cr ≈ 1/929 follows only after assuming Standard-Model content, and the duration goes as
   τ(β_cr − β)⁻¹ (line 348); the ≳ 23 e-fold bound is a one-bounce requirement, not a prediction.
5. **No observation-facing content:** no tilt, tensor, axis, relic density or present curvature; the
   nuclear-density remark (line 19) is a consistency statement with no threshold; the author states the
   fluctuation spectrum remains to be derived (line 364). A(a) rule: an assumed closure is not directional.

## Applied
Dated deep-audit annotation on entry 11 (tier word untouched). Queue recomputed (`b69`); next draw: entry 9.
