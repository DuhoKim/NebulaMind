ACCESS_SHA=7a5ad550f3044bbd0584b09e51595989deb121d2b20093bc50b36a8ef77f066c
THIRD_SEAT_LIMB2=LIMB2_UNDETERMINED
THIRD_SEAT_K4_CLASS=K4_UNDETERMINED

1. "No incoming radiation" and "regularity at infinity" are ADDITIONAL physical assumptions, not consequences of the Darmois conditions. The Darmois conditions are strictly local, applying only to the matching hypersurface $\Sigma$. For $\ell \ge 2$, the exterior vacuum perturbations are governed by the Zerilli equation, which requires boundary conditions at spatial/null infinity to form a uniquely solvable boundary-value problem. Without imposing these conditions externally, the Darmois conditions alone do not uniquely fix the exterior response.

2. All three seats explicitly agree that the junction is NEITHER F1 NOR F2. 
- Claude prints: "FINDING_NOT_F1=True", "FINDING_NOT_F2=True", and "CONSEQUENCE=limb 2 does NOT fire".
- Codex prints: "F1_COMPARISON=NO", "F2_COMPARISON=NO".
- Route 2 prints: "Because the Darmois conditions alone do not close the system for l >= 2, this does not reduce to either F1 or F2."
Since they all agree, limb 2 does not fire regardless of how the split resolves.

3. `LIMB2_UNDETERMINED` is correct. Because the Darmois junction alone does not close as a boundary condition on the interior (as it leaves free Cauchy data for the exterior), it cannot uniquely fix the interior evolution without an added assumption. Therefore, as instructed by the test framework, `LIMB2_UNDETERMINED` is correct even though the comparison to F1 and F2 is negative.

4. K4 should file `K4_UNDETERMINED`. The exact freedom is: for every multipole $\ell \ge 2$ and azimuthal number $m$ ($-\ell \le m \le \ell$), the exterior Zerilli field retains one free function of time (representing incoming even-parity gravitational radiation from past null infinity, or equivalently two real Cauchy data functions left unconstrained by the junction). These functions are completely free subject only to reality and finite-energy/regularity constraints.

5. No, this outcome does not require touching the Planck data at all. Filing `K4_UNDETERMINED` means the problem is inconclusive because the junction fails to uniquely constrain the interior modes without a manufactured boundary condition. Without a unique prediction for the $C_\ell$ modification, there is nothing to score on the Planck map, and the study stops a priori.

6. There is NO CLASS GAP for this outcome. The Claude seat's concern about a missing class assumed the junction formed a closed problem that resulted in "no modification" without being an F1/F2 condition. However, because the problem is genuinely undetermined, it perfectly fits the already declared `K4_UNDETERMINED` class. The prereg's class list is exhaustive for this physical outcome, and no amendment is owed.

K4_THIRD_SEAT_COMPLETE
