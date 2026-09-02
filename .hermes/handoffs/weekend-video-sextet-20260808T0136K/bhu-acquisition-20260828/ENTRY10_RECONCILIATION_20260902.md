# Entry-10 deep audit — reconciliation (Tori, 2026-09-02, STEP 3, queue draw #4)

**Entry 10 — N. J. Popławski (2012), "Nonsingular, big-bounce cosmology from spinor-torsion coupling," PRD 85,
107502** (arXiv 1111.4595). Tier **CONSISTENCY-ONLY**. Brief `ENTRY10_AUDIT_BRIEF_20260902.md`.

## Verdict — BOTH SEATS AGREE, tier holds; no MUST-STOP
| seat | token |
|---|---|
| codex (`ENTRY10_codex_RESULT.md`) | `AUDIT_HOLDS_CONSISTENCY_ONLY` |
| claude-seat (`ENTRY10_claude_RESULT.md`, blind) | `AUDIT_HOLDS_CONSISTENCY_ONLY` |

## What both derived independently (Tori verified citations and recomputed the numbers)
1. **Mechanism:** the Dirac-specific axial-torsion source is reproduced (Kerlick / Hehl–Datta credited); the paper
   explicitly rejects the Weyssenhoff spin-fluid closure entry 9 used and instead averages the Dirac stress tensor as
   a perfect fluid with ⟨s²⟩ = (3/4)n² (line 113, asserted without citation), giving ρ̃ = −p̃ = −αn², α = 9κ/16.
   Closed FLRW with k = 1 is assumed "as in [16]" (lines 134–137); ultrarelativistic kinetic equilibrium with fixed
   degrees of freedom is assumed.
2. **The cusp is an artefact of the reduced system, not a solution of the full equations:** ȧ jumps from −v to +v at
   a_cr (lines 287–290), which makes ä a δ-function while the second Friedmann equation's right-hand side is
   bounded — an unsourced impulse violating the paper's own eq. (12) (claude-seat; codex: "not established in a
   distributional sense"). No regulariser, no matching, no perturbation treatment; the "nonsingular with respect to
   curvature" claim is not established by the displayed cusp.
3. **Numbers:** T_cr = 0.78 m_P and a_cr = 5.9×10⁻⁴ m reproduce from the stated inputs (Tori: 0.785 m_P,
   5.86×10⁻⁴ m). **v_ant = 8.9×10³⁴ and Ω(T_cr) − 1 = 1.3×10⁻⁷⁰ (eqs. 30–31) do NOT** — consistent recomputation
   gives v_ant ≈ 2.8×10³¹ and Ω − 1 ≈ 1.3×10⁻⁶². The two seats proposed different origins; Tori's check favours
   claude-seat's: printed/recomputed v_ant = 3,225 ≈ 1 + z_eq = 3,201 (a_r → a_0 substitution), and the Ω ratio
   ~10⁸ ≈ π²(1+z_eq)² fits using 1/v_ant² for eq. (25)'s 1/v². codex's kelvin-for-eV hypothesis gives ~10⁴, a
   worse fit. Recorded as the best explanation, not a certainty. Either way the numbers carry no observational
   threshold; a_0 itself encodes Ω₀ − 1, so "explains flatness" feeds in what it explains.
4. **Observation-facing content:** none derived — curvature sign assumed (A(a)); no relic, tilt, tensor or
   likelihood; the low-density GR-recovery statement (lines 53–56) is consistency. Not PROSPECT (matching across
   the cusp undefined, so no route).

## Applied
Dated deep-audit annotation on entry 10 (tier word untouched). Queue recomputed; next draw: entry 52.
Seat note: from draw #5 the second blind seat is kimi (single-source briefs are within its context), claude-seat
reserved for splits — cost discipline (Claude burn watch).
