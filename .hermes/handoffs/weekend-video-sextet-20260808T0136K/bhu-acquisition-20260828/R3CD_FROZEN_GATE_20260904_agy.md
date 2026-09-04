ACCESS_SHA=acdaa07593873cf53dc6aca3d9f2885a0deec98d784e1f021d1ea75bc526bf0c
GATE_C=PREREG_UNSOUND
GATE_D=PREREG_SOUND

1. Are the draft gate's four repairs actually present in the frozen texts?
- Draft C Repair 1 (Quoted sentence: "A second seat re-screens the excluded rows looking for a wrongly-excluded candidate. A census that only checks its survivors is not a census. `C6_EXCLUSIONS_RECHECKED=PASS`.", Defect: The control is not mechanical and can be waved through without proof., EXACT replacement: "A second seat re-screens the excluded rows looking for a wrongly-excluded candidate, printing an independent list of exclusions for automated diffing against the first seat's. A census that only checks its survivors is not a census. `C6_EXCLUSIONS_RECHECKED=PASS`."): Present and improved in R3C (added list reporting rules).
- Draft C Repair 2 (Quoted sentence: "No row may be excluded because the pattern predicts it will fail; each exclusion must cite the row's own content.", Defect: The prohibition against circularity is merely stated, not mechanically enforced., EXACT replacement: "No row may be excluded because the pattern predicts it will fail; to make this mechanical, every exclusion must quote the exact source text and line number, and a script must verify these citations contain no reference to the pattern."): NOT PRESENT VERBATIM OR BETTER. The text drops the requirement that "a script must verify these citations contain no reference to the pattern", replacing it with "...and a seat whose exclusion carries no quotation fails C2."
- Draft C Repair 3 (Quoted sentence: "Paper HOLD.", Defect: Fails to mandate the standing fairness wording for negative findings., EXACT replacement: "Paper HOLD; the record's wording for any negative finding must be "unreproduced from the stated inputs," not "error.""): Present verbatim in R3C.
- Draft D Repair 1 (Quoted sentence: "C3 — deletion probe, K6's corrected form: delete the source-pinned field equations; if a unique floor survives on an injected relation alone, that relation is circular and no derived-floor class may be filed. `C3_DELETION_PROBE=PASS`.", Defect: The control is not mechanical; a seat could claim it passed without printing the failed state., EXACT replacement: "C3 — deletion probe, K6's corrected form: delete the source-pinned field equations; if a unique floor survives on an injected relation alone, that relation is circular and no derived-floor class may be filed. The harness must print the execution output of the deleted state to prove the probe was run. `C3_DELETION_PROBE=PASS`."): Present and equivalent/better in R3D.

2. CIRCULARITY IN R3C
Loophole: Because the mechanical script verification of the citation text was dropped (Repair 2), the mechanical check only verifies the *presence* of a quotation. A seat can append any source quotation to satisfy C2 mechanically, while their actual reasoning for exclusion relies informally on the pattern.

3. R3C's condition-5 warning
Carrying the warning with an instruction to report condition 5 separately is not an acceptable resolution; it leaves the falsifier undecidable in practice. Separating an undecidable condition just yields a separate undecidable outcome, as the unbounded knowledge of all standard models is still required. 

4. OUTCOME CLASSES
Exhaustive, mutually exclusive, and an inconclusive route is reachable for both. In R3C, class 3 explicitly states it must hold "trivially, which is weaker than class 2," so it cannot be reported as equivalent.

5. CONTROLS
Exact named codes and NOT RUN discipline are present. Section 9's inherited discipline is mechanical, not decorative, as it mandates exact terminal commands (`shasum`, `python3 --version`) and sets strict timeout rules that cannot be transcribed.

6. Re-runs
Neither re-runs anything closed by K1-K6 or Programs A/C. R3D explores the Dymnikova regular-core branch (entries 18-20, 55), explicitly distinct from K6's ECKS target (entry 51). R3C runs a new hypothesis search over the full corpus.

7. FAIRNESS
The standing wording "unreproduced from the stated inputs," not "error," is present in both texts.

8. Can either stall or fail to reach a verdict?
Yes. Failure modes include:
- Inconclusive findings (R3C Class 4, R3D Class 2).
- Failing controls in both seats after two attempts (Class 5 for both).
- Symbolic timeouts hitting the 120-second stall guard, preventing a verdict.

R3CD_FROZEN_GATE_COMPLETE
