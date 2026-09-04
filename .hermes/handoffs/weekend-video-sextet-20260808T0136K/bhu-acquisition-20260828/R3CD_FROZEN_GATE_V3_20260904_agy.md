ACCESS_SHA=5c7480b7c17c020a20e635de0e9c8970a94f2291571c9740244084a2a4c27a78
GATE_C=PREREG_UNSOUND
GATE_D=PREREG_SOUND_WITH_REPAIRS

Repairs for Draft C:
1. Quoted sentence: "A second seat re-screens the **excluded** rows looking for a wrongly-excluded candidate. A census that only checks its survivors is not a census. `C6_EXCLUSIONS_RECHECKED=PASS`."
   Defect: The control is not mechanical and can be waved through without proof.
   EXACT replacement: "A second seat re-screens the **excluded** rows looking for a wrongly-excluded candidate, **printing an independent list of exclusions for automated diffing against the first seat's**. A census that only checks its survivors is not a census. `C6_EXCLUSIONS_RECHECKED=PASS`."
   Status: Present verbatim/better.

2. Quoted sentence: "No row may be excluded because the pattern predicts it will fail; each exclusion must cite the row's own content."
   Defect: The prohibition against circularity is merely stated, not mechanically enforced.
   EXACT replacement: "No row may be excluded because the pattern predicts it will fail; **to make this mechanical, every exclusion must quote the exact source text and line number, and a script must verify these citations contain no reference to the pattern.**"
   Status: NOT PRESENT VERBATIM. (Answers check 1 & 2). R3C substitutes a 3-point list. Crucially, the requirement that "a script must verify these citations contain no reference to the pattern" is absent. This leaves a circularity loophole: a seat can mechanically quote an irrelevant sentence from the source to pass the verification script, while still quietly basing their exclusion decision on the pattern itself.

3. Quoted sentence: "Paper HOLD."
   Defect: Fails to mandate the standing fairness wording for negative findings.
   EXACT replacement: "Paper HOLD; **the record's wording for any negative finding must be "unreproduced from the stated inputs," not "error."**"
   Status: Present verbatim.

Repairs for Draft D:
1. Quoted sentence: "C3 — deletion probe, K6's corrected form: delete the **source-pinned field equations**; if a unique floor survives on an injected relation alone, that relation is circular and no derived-floor class may be filed. `C3_DELETION_PROBE=PASS`."
   Defect: The control is not mechanical; a seat could claim it passed without printing the failed state.
   EXACT replacement: "C3 — deletion probe, K6's corrected form: delete the **source-pinned field equations**; if a unique floor survives on an injected relation alone, that relation is circular and no derived-floor class may be filed. **The harness must print the execution output of the deleted state to prove the probe was run.** `C3_DELETION_PROBE=PASS`."
   Status: Present verbatim/better.

Explicit Checks 4, 5, 6, 7:
4. Outcome classes are exhaustive, mutually exclusive, and have inconclusive routes reachable (Class 4 in R3C, Class 2 in R3D). R3C Class 3 is explicitly marked weaker than Class 2 and cannot be reported as equivalent.
5. Controls use exact named codes and NOT RUN discipline. Section 9 inherited discipline is highly mechanical, containing strict operational failures (quarantining if no ACCESS_SHA, SYMBOLIC_TIMEOUT fallbacks, C5 harness failure).
6. Neither re-runs closed K1-K6 items. R3C runs a new census; R3D explicitly tests a new branch (Dymnikova) and forbids assuming K6's outcome.
7. Fairness wording ("unreproduced from the stated inputs", not "error") is explicitly standing in both texts.

Answers to 3 and 8:
3. The premise that R3C carried the condition-5 warning is factually incorrect. R3C Section 8 explicitly REPAIRED it by replacing the subjective phrasing with two exact named comparators (ΛCDM and the stripped BHU model). This numerical test makes the falsifier fully decidable. If stripping the BHU element leaves no defined model, it is recorded as NOT APPLICABLE and strictly falls back to conditions 1-4, which is also decidable.
8. Yes, both can stall or fail to reach a verdict. R3C fails to reach a verdict if the third seat's re-derivation cannot reproduce a sampled exclusion (`CENSUS_AUDIT_FAILED`, which voids the census). R3D explicitly stalls if a source cannot be read (`DYM_SOURCE_BLOCKED` - "The study waits; this is not a scientific verdict").

R3CD_FROZEN_GATE_COMPLETE
