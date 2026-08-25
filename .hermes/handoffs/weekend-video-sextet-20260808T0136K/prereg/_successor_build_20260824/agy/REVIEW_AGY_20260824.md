# Requirement Coverage

1. **Req 1 (No contiguous BRICKID):** Implemented in §2. Draft: "Bricks are ranked by |cosθ| DESCENDING and accepted in that order. Contiguous-BRICKID selection is banned."
2. **Req 2 (Stopping rule on leverage):** Implemented in §2. Draft: "stop when accepted-sample L = N·Var(cosθ) ≥ L_min".
3. **Req 3 (Footprint-aware normalisation):** Implemented in §3. Draft: "the amplitude comparison to A_L uses E[cos²θ]". (See Finding 3 for math mismatch).
4. **Req 4 (Project monopole out):** Implemented in §3. Draft: "Â_c = Σ(s_i − s̄)(c_i − c̄) / Σ(c_i − c̄)²".
5. **Req 5 (Derive sigma from footprint):** Asserted in §3. Draft: "analytic check Var(Â_c) = Var(s)·Var(c)/(N−1)". (See Finding 1 for blocker: assertion is mathematically impossible).
6. **Req 6 (Power gate Var(cosθ) input):** Implemented in §4. Draft: "Named inputs... accepted-sample Var(cosθ)".
7. **Req 7 (Fix sidedness seam):** Asserted in §3. Draft: "Sidedness, declared once, here: one-sided at Longo's oriented sign". (See Finding 7 for testability issue).

# Findings

1. **Severity: BLOCKER** (Req 5 / internal math consistency)
   - **Quote:** "analytic check Var(Â_c) = Var(s)·Var(c)/(N−1)" (§3)
   - **Why it fails:** Algebraic error. The variance of the centred estimator `Â_c` is `Var(s) / ((N−1)·Var(c))`. Multiplying by `Var(c)` instead of dividing artificially shrinks the variance (since Var(c) < 1). This mathematical loophole guarantees a false pass at the power gate because the variance is grossly underestimated.
   - **Minimal repair:** Change to `Var(Â_c) = Var(s) / ((N−1)·Var(c))`

2. **Severity: BLOCKER** (Internal consistency / Quotation fidelity)
   - **Quote:** "EXCLUDED-AT-AMPLITUDE: p ≥ 0.001 region per V3's exclusion arithmetic" and "No third real-sky path exists." (§5)
   - **Why it fails:** V3 F-6 defines REJECTED explicitly as `p > 0.05 AND (|Â_c| + 3·σ_ours) < 0.0408`. Draft §5 incorrectly claims the V3 arithmetic covers the entire `p ≥ 0.001` region and asserts no third path exists, deliberately omitting V3's INCONCLUSIVE gap (0.001 ≤ p ≤ 0.05). It cannot be incorporated by reference while redefining its boundaries.
   - **Minimal repair:** Restate the full V3 exclusion rule explicitly (`p > 0.05 AND (|Â_c| + 3·σ_ours) < 0.0408`) and restore the INCONCLUSIVE region for the gap.

3. **Severity: MAJOR** (Req 3 / internal math consistency)
   - **Quote:** "the amplitude comparison to A_L uses E[cos²θ] evaluated on the accepted sample." (§3)
   - **Why it fails:** The defined estimator `Â_c` divides by `Σ(c_i − c̄)²`, which is proportional to `Var(cosθ)`. If the sample isn't perfectly symmetric around the equator (`c̄ != 0`), `E[cos²θ]` will diverge from `Var(cosθ)`, creating a normalisation mismatch between the text procedure and the estimator.
   - **Minimal repair:** Change "uses E[cos²θ]" to "uses Var(cosθ)".

4. **Severity: MAJOR** (Quotation fidelity)
   - **Quote:** "Cut-6 exactly as frozen in V3, carried by quotation at freeze (incl. flux_r > 0, dered_mag_r < 17.7, and the frozen z cut on z_phot_median)." (§2)
   - **Why it fails:** V3 does not contain a cut on `z_phot_median` (it only mentions Longo's z < 0.085 in passing context). Claiming it is "frozen in V3" is a false quotation.
   - **Minimal repair:** Remove "and the frozen z cut on z_phot_median" from the V3 quotation parentheses, and introduce the photo-z cut as a new successor requirement.

5. **Severity: MAJOR** (Loophole)
   - **Quote:** "requirement power ≥ 0.95." (§4)
   - **Why it fails:** It omits the alpha level. The laziest compliant reading allows evaluating power at an absurd threshold (e.g., p < 0.5), bypassing the gate's intent. V3 F-6 specified `p < 0.001`.
   - **Minimal repair:** Change to "requirement power ≥ 0.95 at p < 0.001".

6. **Severity: MAJOR** (Blind-double integrity)
   - **Quote:** "Selection numbers (accepted N, Var(cosθ), L) are produced by two implementations... Freeze requires their agreement on the real catalog input" (§6)
   - **Why it fails:** `Var(cosθ)` and `L` are floating-point values. Without a specified tolerance, standard floating-point divergence between two independent implementations will permanently block the freeze or allow arbitrary subjective overrides.
   - **Minimal repair:** Specify a numeric tolerance (e.g., "agreement to 1e-7 relative").

7. **Severity: MINOR** (Req 7 / Loophole)
   - **Quote:** "The harness must implement exactly this sentence; BS-7 is the identity receipt between this line and the harness's self-reported test." (§3)
   - **Why it fails:** A Python harness cannot meaningfully "implement" a natural language sentence as a statistical test. The laziest compliance is the code merely printing the sentence as a string.
   - **Minimal repair:** Define the explicit mathematical test the harness must run (e.g., `Â_c > 0`).

8. **Severity: MINOR** (Internal consistency)
   - **Quote:** "synthetic absolute-sign anchor run before any real image (BS-5 receipt)" (§3) vs "BS-4 | synthetic absolute-sign anchor rerun" and "BS-5 | power-gate receipt" (§7).
   - **Why it fails:** Slot mismatch between the body text (§3) and the binding slot table (§7).
   - **Minimal repair:** In §3, change "(BS-5 receipt)" to "(BS-4 receipt)".

REPAIR-FIRST
