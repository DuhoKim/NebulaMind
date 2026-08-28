PASS_PHASE6_OPENING

As an independent fresh gate seat, I have reviewed the artifacts, executed the verification scripts, and validated the claims against the target paper and primary sources. My view is formed independently, and I confirm the findings are sound.

Here is my ruling on the specific attacks requested:

1. **AM I DOING THE THING I ACCUSE THE TARGET OF?**
No. Your exclusion of the CMB-alone rows is principled, not dataset cherry-picking. You are following the explicit diagnosis of the primary source (Planck 2018 VI), which attributes the CMB-alone closed preference to a known parameter anomaly ($A_L$) and geometric degeneracy. Breaking that degeneracy with lensing or BAO is the standard cosmological practice to measure curvature, as Planck itself states. The target paper, on the other hand, actively ignores the primary source's diagnosis to select a degenerate result. Your exclusion is structurally sound.

2. **Is the "hard prediction is a sign" reading of Eq. 27 right?**
Yes, it is a correct and fair reading. The mathematical presence of the $(\chi_*/\chi_k)^2 < 1$ factor strictly turns the value into a magnitude ceiling. Moreover, the text in Section VI explicitly walks back the magnitude if the homogeneity scale assumption is dropped ("the value of $\Omega_k$ ... could be smaller"), leaving only the sign requirement: $\Omega_k < 0$. The falsifier is indeed a sign.

3. **Is "omission" the right charge on the Planck citation?**
Yes, "omission" is precise and fair. The target paper accurately quoted the numerical value from Planck's Eq. 46b, exonerating them of misquotation. However, they entirely stripped the vital context from Section 7.3, where Planck disavows the robustness of that exact number, links it to the $A_L$ anomaly, and demonstrates that adding lensing and BAO pulls the geometry back to flat/open. Omitting the primary source's own caveats is the correct charge.

4. **Check the sign handling everywhere.**
The sign handling is accurate and mathematically sound across all artifacts. By definition, $\Omega_k \propto -k$. Therefore, $k > 0$ (positive spatial curvature, closed) requires $\Omega_k < 0$. The target model requires $\Omega_k < 0$. Current DESI+CMB data indicate negative spatial curvature ($k < 0$, open), meaning $\Omega_k > 0$. Your scripts handle this without error.

5. **Reproduce both scripts.**
Both `c1_curvature_constraints.py` (7/7) and `c2_constraint_ledger.py` (6/6) were executed and ran cleanly, exiting with code 0 and verifying all internal self-checks.

6. **What I have NOT done, and whether it is load-bearing:**
None of the omissions are load-bearing. 
- Not reading the DESI companion paper is mitigated by the fact that three independent DESI-based analyses all yield $\Omega_k > 0$. 
- Not checking ACT v1 Figure 9 is irrelevant because the target definitively mischaracterizes the ACT paper's summary conclusion regardless of the figure number. 
- Not scrutinizing the $\chi_*$ derivation is acceptable because the target paper explicitly treats it as an auxiliary, drop-able assumption, leaving the core sign prediction unaffected.

**Conclusion:**
The record's falsification condition was backwards and is now corrected. The sign handling is impeccable. The citation audit is measured, precise, and fair. The phase opening passes.
