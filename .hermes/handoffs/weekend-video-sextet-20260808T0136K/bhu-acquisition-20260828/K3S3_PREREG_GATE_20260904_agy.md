ACCESS_SHA=26aaca948236038f1ffd70da442432e58151ccc70538f88f657960c8a7a51aff
GATE=PREREG_SOUND_WITH_REPAIRS

1.
Quoted sentence: "- **If that ratio is not small at the bounce** — which is what "the spin term causes the bounce" means — then perturbation theory in the four-fermion term fails exactly where the answer matters. **File `K3S3_NOT_PERTURBATIVE` and stop.** No Hartree–Fock machinery is written, no expensive half is run."
Defect: The exit condition is left to taste; "not small" is not operationalised with a numerical threshold.
Exact replacement wording: "- **If that ratio's magnitude is ≥ 0.1 at the bounce** — which is what "the spin term causes the bounce" means — then perturbation theory in the four-fermion term fails exactly where the answer matters. **File `K3S3_NOT_PERTURBATIVE` and stop.** No Hartree–Fock machinery is written, no expensive half is run."

2.
Quoted sentence: "3. **K3S3_SIGN_REVERSED_OR_ZERO** — the self-consistent coefficient is positive or exactly zero. Report it, and report whether it approaches either printed value; step 2's sign statement is then withdrawn **by amendment**, and the record says so plainly."
Defect: A coefficient that changes sign depending on the physical regime (e.g., density) falls into a gap between classes 2 and 3.
Exact replacement wording: "3. **K3S3_SIGN_REVERSED_OR_ZERO** — the self-consistent coefficient is positive, exactly zero, or changes sign depending on the regime. Report it, and report whether it approaches either printed value; step 2's sign statement is then withdrawn **by amendment**, and the record says so plainly."

3.
Quoted sentence: "5. **K3S3_PRESCRIPTION_DEPENDENT** — the answer depends on the truncation, ordering or coarse-graining in a way the sources do not fix. **INCONCLUSIVE**; state the residual freedom exactly."
Defect: Fails to declare precedence over classes 1-3. A prescription-dependent result that remains negative could simultaneously trigger classes 2 and 5.
Exact replacement wording: "5. **K3S3_PRESCRIPTION_DEPENDENT** — the answer depends on the truncation, ordering or coarse-graining in a way the sources do not fix. **INCONCLUSIVE**; state the residual freedom exactly. This class takes precedence over classes 1, 2, and 3."

4.
Quoted sentence: "**If limb A exits, C1/C2/C3/C6 belong to the half never reached and are recorded `NOT RUN`, never as passes** — the discipline K4 established."
Defect: Fails to include C5 and C7, which also belong to the unreached expensive half and would falsely be claimable as passes if limb A exits.
Exact replacement wording: "**If limb A exits, C1/C2/C3/C5/C6/C7 belong to the half never reached and are recorded `NOT RUN`, never as passes** — the discipline K4 established."

Justification:
- Numeral tracing is strict and accurate; line numbers in entry 10 are flawless (accounting for the 3/8 typo in the source text extraction) and the K3S2 coefficients match perfectly.
- C1 is not circular. Using the predecessor's free-field result as the non-interacting limit to control the new Hartree-Fock code is a valid software check, not a circular physical input.
- The recorded objection is honest, placed correctly at the top, and does not read as a hedge or criticism; it neutrally registers the lane's prior stance before executing the principal's explicit override.

Answer to Criterion 8: 
Effectively no. Limb A checks if the spin term is small compared to the ordinary energy density at the bounce. However, the bounce is defined *by construction* as the point where these two quantities balance (i.e. the ratio is exactly 1). Therefore, the dimensionless parameter will always evaluate to order 1 at the bounce, limb A will always fail the "small" test, and the study is mathematically guaranteed to exit with the inconclusive `K3S3_NOT_PERTURBATIVE` class. It can never reach the expensive half. The lane should be aware of this before proceeding.

K3S3_PREREG_GATE_COMPLETE
