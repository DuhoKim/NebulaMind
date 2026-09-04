ACCESS_SHA=45cd18da4014a90275549646c85959b1ee6c8ee9b2de256605a718014a2f784e
GATE=PREREG_UNSOUND

1. LINE TRACING: The cited lines do not contain what is claimed. L134 defines the mass equation, L138 is irrelevant, and L143 explicitly states "More generally, M could be a function of time." L252 and L262-263 also do not mandate a strictly constant mass.
2. THE DRAFT REPAIR: The draft repair was not applied verbatim. While C2 requires exact search terms and quoted text, the failure condition reverted to "without that search fails" instead of the required "without those quotes fails".
3. THE RIGIDITY PREMISE: The premise is assumed rather than shown. The cited lines explicitly allow M to evolve over time, meaning the lane is assuming its own answer to force a constant `r_S`. This makes the whole design circular.
4. OUTCOME CLASSES: The classes are exhaustive and mutually exclusive. The precedence rule for Class 4 successfully prevents a shared falsifier (predicting `w=-1` alongside ΛCDM) from being reported as uniquely discriminating against this model.
5. CONTROLS: C5 (live-harness) and C5b (no-cross-lane-access) are exact named codes and highly mechanical. C5 requires the execution and printing of specific shell/Python environment variables, and C5b forces a halt on an explicit boundary condition.
6. THE DATA BOUNDARY: The stop condition is tight. It strictly limits access to published constraints and enforces a halt with escalation to the principal if those are insufficient, expressly forbidding drift into Hwao's lane.
7. CIRCULARITY: Verified. Limb A handles the theoretical question without data, and data is only introduced in Limb B if Limb A holds.
8. RE-RUN: Verified. The document states it does not re-run K4 or Program A, distinguishing its focus on background expansion history from the perturbation logic in those programs.

Repairs:
1.
- Quoted sentence: `Its own equations hold the enclosed mass **constant** (**L134**, **L138**, **L143**), so \`r_S\` is constant and \`Λ\` is exactly constant — equation of state \`w = −1\`, with no evolution available.`
- Defect: The premise is assumed rather than shown, rendering the design circular. The cited lines do not establish a constant mass; L143 expressly notes M could be a function of time.
- EXACT replacement wording: `We must test whether its equations hold the enclosed mass **constant**. If \`r_S\` is constant, \`Λ\` is exactly constant — equation of state \`w = −1\`, with no evolution available.`
2.
- Quoted sentence: `evolve, and **print the exact search terms used and quote the resulting text.** A rigidity claim asserted without that search fails.`
- Defect: The gate's previous repair was not applied verbatim. The condition "without that search fails" is not mechanical and was explicitly rejected in the draft gate in favor of "without those quotes fails".
- EXACT replacement wording: `evolve, and **print the exact search terms used and quote the resulting text.** A rigidity claim asserted without those quotes fails.`

Answers to 9 and 10:
9. HONESTY: Declaring the expected outcome in advance is good practice. It establishes honesty by preventing a shared falsifier from being spuriously claimed as a novel discovery later, while the objective controls ensure this expectation does not force the execution.
10. VERDICT / STALL: The design can reach a guaranteed verdict without stalling. The stall guard (Section 11) places a hard 120-second timeout on symbolic operations and forces a clean fallback to algebraic or numerical arguments if exceeded.

R3B_PREREG_GATE_COMPLETE
