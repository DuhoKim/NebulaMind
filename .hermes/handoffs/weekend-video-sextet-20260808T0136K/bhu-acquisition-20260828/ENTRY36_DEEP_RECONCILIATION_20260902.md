# Entry-36 deep audit — reconciliation (Tori, 2026-09-02, STEP 3, queue draw #19)

**Entry 36 — J. Smoller & B. Temple (2000), "Cosmology with a shock-wave," CMP 210, 275–308** (astro-ph/9812063).
Tier **CONSISTENCY-ONLY**. Brief `ENTRY36_AUDIT_BRIEF_20260902.md`.

## Verdict — BOTH SEATS AGREE, tier holds; the 2026-08-28 blind flag is ADJUDICATED and does not survive
| seat | token |
|---|---|
| codex (`ENTRY36_codex_DEEP_RESULT.md`, full 3,797-line read) | `AUDIT_HOLDS_CONSISTENCY_ONLY` |
| claude-seat (`ENTRY36_claude_DEEP_RESULT.md`, blind; re-derived (7.24)–(7.33)) | `AUDIT_HOLDS_CONSISTENCY_ONLY` |

## What both derived independently (Tori verified the citations)
1. **H₀ and T₀ are inputs, not outputs:** with R₀ = 1, Q₀ = H₀² (5.6) and α = âT₀⁴/3, β = H₀² − âT₀⁴ (7.13–7.14,
   lines 3138–3183) normalise a standard flat FRW interior; "accounts for the observed Hubble constant and CMB
   temperature" means the FRW side is fitted to them.
2. **The "predicted" present shock position is a one-parameter family, not a number:** indexed by the free start
   epoch R* (plus a free initial position inside a window). At the paper's own fiducial R* = 2.7/4000, eqs.
   (7.37)–(7.38) give 0.019–0.029 H₀⁻¹ (≈ 100–160 Mpc for h₀ = 0.55); at R* = 1, anything from 0 to 0.87 H₀⁻¹.
   So "comparable to the Hubble length" (lines 14, 312) is set by the knob, contradicting line 103's "no adjustable
   parameters other than H₀ and T₀" against the paper's own lines 161–166 and Figure 2.
3. **No observable:** no observer position, no signature (temperature edge, density jump, anisotropy); the paper
   itself: "nothing quantitative could be said … And to a large extent this must be true" (lines 302–306); the
   closing questions about other explosions are questions (lines 318–333). Flag fails under A(a).
4. **Internal slips recorded (claude-seat):** (7.34)–(7.36) print R*² where the derivation gives R*; (8.6)'s
   118 h₀H₀⁻¹ is inconsistent with (7.26) (≈ 346; only the β = 0 comparison case affected); (7.29) reads "2.2/4000"
   for 2.7/4000. The one R*-independent derived statement — the present shock lies within ≈ 0.87 H₀⁻¹ of the centre —
   is a bound inside the construction with no observable attached; noted, not promoted.

## Applied
Dated deep-audit annotation on entry 36 (tier word untouched; BLIND-FLAGGED note marked ADJUDICATED). Queue recomputed.
