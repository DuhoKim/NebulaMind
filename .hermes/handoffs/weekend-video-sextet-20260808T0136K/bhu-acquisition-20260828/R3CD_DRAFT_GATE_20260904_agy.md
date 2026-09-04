ACCESS_SHA=7f6bb74c4fbb7575b66ea2df8ca22a2be214bcd743ccb5fcfafbd1d6990630ca
GATE_C=PREREG_SOUND_WITH_REPAIRS
GATE_D=PREREG_SOUND_WITH_REPAIRS

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

Answers to 7 and 8:

7. The breaker conditions are not fully operational as written, and two seats would likely apply them differently. Specifically, Condition 5 is not decidable because determining if a number is shared with "any standard model predicting it for unrelated reasons" requires unbounded, subjective knowledge of all possible standard models. (Condition 1 is also subjective at the boundary between a "scale" and a "magnitude").

8. R3C is worth its stated cost because establishing whether the central shape/magnitude pattern holds universally across the remaining 48 corpus rows is critical to the lane's final synthesis. R3D is worth its stated cost because the regular-core metric is the most likely candidate to break the pattern, and securing the claim requires explicitly testing this branch.

R3CD_DRAFT_GATE_COMPLETE
