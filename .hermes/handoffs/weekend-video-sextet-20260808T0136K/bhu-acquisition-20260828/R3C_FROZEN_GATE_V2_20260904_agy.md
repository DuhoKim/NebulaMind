ACCESS_SHA=ece4c6d97eecebb404aeb7749468412655625e6129be45512bc0327f0d4dbce7
GATE_C=PREREG_UNSOUND
GATE_D=PREREG_UNSOUND

Repairs for Draft C:

1. Quoted sentence: "A second seat re-screens the **excluded** rows looking for a wrongly-excluded candidate. A census that only checks its survivors is not a census. `C6_EXCLUSIONS_RECHECKED=PASS`."
   Defect: The control is not mechanical and can be waved through without proof.
   EXACT replacement: "A second seat re-screens the **excluded** rows looking for a wrongly-excluded candidate, **printing an independent list of exclusions for automated diffing against the first seat's**. A census that only checks its survivors is not a census. `C6_EXCLUSIONS_RECHECKED=PASS`."
2. Quoted sentence: "No row may be excluded because the pattern predicts it will fail; each exclusion must cite the row's own content."
   Defect: The prohibition against circularity is merely stated, not mechanically enforced.
   EXACT replacement: "No row may be excluded because the pattern predicts it will fail; **to make this mechanical, every exclusion must quote the exact source text and line number, and a script must verify these citations contain no reference to the pattern.**"
3. Quoted sentence: "Paper HOLD."
   Defect: Fails to mandate the standing fairness wording for negative findings.
   EXACT replacement: "Paper HOLD; **the record's wording for any negative finding must be "unreproduced from the stated inputs," not "error."**"

Repairs for Draft D:

1. Quoted sentence: "C3 — deletion probe, K6's corrected form: delete the **source-pinned field equations**; if a unique floor survives on an injected relation alone, that relation is circular and no derived-floor class may be filed. `C3_DELETION_PROBE=PASS`."
   Defect: The control is not mechanical; a seat could claim it passed without printing the failed state.
   EXACT replacement: "C3 — deletion probe, K6's corrected form: delete the **source-pinned field equations**; if a unique floor survives on an injected relation alone, that relation is circular and no derived-floor class may be filed. **The harness must print the execution output of the deleted state to prove the probe was run.** `C3_DELETION_PROBE=PASS`."

Explicit Checks:
1. Are the draft gate's four repairs actually present in the frozen texts? Draft C Repair 2 is NOT present (the required script verification and exact line numbers were omitted). The other three are present verbatim or better.
2. CIRCULARITY IN R3C: The loophole is that R3C allows exclusions to quote the "specific phrase in that row's own claim cell." Since the claim cells are in the warrant table authored by this lane, a seat can exclude a row by quoting the lane's own summaries instead of the paper's original text. Without script verification, human judgement still decides if the exclusion relies on the pattern.
4. OUTCOME CLASSES: In R3C, class 3 (nothing survives screening) is explicitly distinct and cannot be reported as equivalent to class 2 ("held trivially, which is weaker"). However, neither set of outcome classes is fully exhaustive because they lack classes for hard stops.
5. CONTROLS: Section 9's inherited discipline is mechanical, not decorative. It mandates executable outputs (shasum, LIVE python/sympy versions, printing captured timeouts, and ACCESS_SHA validations) that a wrapper can verify, quarantining the report if missing.
6. Re-run closed K1-K6/Programs: Neither re-runs closed K1-K6 branches. R3D specifically targets a new branch (Dymnikova regular-core).
7. FAIRNESS: The standing fairness wording ("unreproduced from the stated inputs", not "error") is present verbatim in both.

Answers to 3 and 8:

3. Carrying an undecidable condition and reporting it separately is NOT an acceptable resolution. It leaves the falsifier undecidable in practice because the core binary question (is there a counterexample?) cannot be concluded if the defining condition cannot be evaluated. 
8. Both can stall or fail to reach a verdict:
   - R3C Failure Mode: Section 5 rule 3 states "A sampled exclusion the third seat cannot reproduce fails the census and the run stops." There is no outcome class defined for this event, so it stalls without a verdict.
   - R3D Failure Mode: Section 7 states "limb A confirms that first and reports BLOCKED if not." There is no outcome class for `BLOCKED` (Class 3 is `DYM_NO_SIZE_MASS_RELATION`), so the run fails to reach a verdict.

R3CD_FROZEN_GATE_COMPLETE
