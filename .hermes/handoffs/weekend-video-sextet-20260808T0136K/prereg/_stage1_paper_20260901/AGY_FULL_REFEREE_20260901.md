# AGY FULL REFEREE REPORT

## 1. SEAM DEFECTS
- **Contradiction:** Section 6 claims that "every stage of the pre-image machinery... was executed and passed." This directly contradicts Section 4.1 (which details a Stage-P planner reporting "status: FAIL, and a blocked plan") and Section 5 / Section 7 (which detail two go-live attempts voided by post-hoc verification and robustness rehearsals that failed to discharge edges).
- **Terminology Drift:** The human annotators are referred to inconsistently across sections. Section 6 uses "checker", "panelist", and "calibrated observer", while Section 7 switches to "human calibration resource" and "people". The "gain-gradient counterfactual" (Sections 1 and 4) is suddenly referred to as the "gamma grid" in Section 4.3 without unification.
- **Gaps:** Section 1 fails to execute a strict instruction from the brief: it must quote Longo 2011's own figures for dipole amplitude, uncertainty, and significance. The section only qualitatively describes a "dipolar fit". 

## 2. OVERCLAIM ACROSS THE WHOLE
- The paper overclaims its success in aggregate by allowing Section 6 to declare that "every stage... passed", erasing the friction, debt, and voided attempts clearly laid out in Sections 5 and 7.
- **Fatal Leverage Overclaim:** The Abstract and Section 2 cite the pre-cut selection leverage `Var(cos theta) = 0.754664` to describe the paper's "selected geometry". They completely fail to quote the post-cut leverage `0.7517` corresponding to the actual 49,211 mask that was executed. Presenting the higher leverage figure of a pre-cut sample as the geometry of the paper—without providing the post-cut figure of the actual sample—is a major aggregate overclaim. 
- Section 7 claims the methods "eliminate the silent convention flips", which is slightly overzealous given the surrounding caveats.

## 3. NUMBERS
- **N_eq / Var(cos theta) Violation:** As noted above, the Abstract and Section 2 use the pre-cut `0.754664` variance, while the post-cut `0.7517` figure (the actual 49,211 mask) is completely missing. Using a pre-cut figure to describe the analysed sample is a major finding.
- **Unverified Numbers in Section 6:** Section 6 flagrantly violates the "No section may use a number absent from this table" rule. It introduces `850` (objects), `51` (panelists at inherited budget), `8.67-million-row` (DESI catalogue), and `120` (total decisions). None of these exist in `VERIFIED_NUMBERS_20260901.md`.

## 4. RASTI CONFORMANCE
- **Abstract ≤ 250 words, one paragraph:** PASS. The abstract is ~188 words and formatting is correct.
- **Conclusions must be the LAST numbered section:** FAIL. There is no Conclusions section. The last section is currently Section 8.
- **Unnumbered Acknowledgements / Data Availability / Conflict of Interest / References:** FAIL. Data Availability is incorrectly numbered as Section 8, and the other three sections are completely missing. 
- **3–6 keywords present:** FAIL. No keywords are included anywhere in the draft.

## 5. PRIMARY-SOURCE VERIFICATION
- **Longo 2011:** FAIL on instructions (direction is correct regarding the dipole, but the mandate to quote the reported amplitude, uncertainty, and significance was entirely ignored).
- **Land et al. 2008:** PASS (Correctly describes the null result and the mirrored-image bias mechanism).
- **Shamir 2012:** PASS (Correctly describes machine-classified positives).

## 6. THE CONTRIBUTION QUESTION
Is this research or a project report? The assembled draft reverts to a project report. The lack of a conclusion, the injection of unverified numbers in Section 6, the outright contradiction masking pipeline failures, and the scientific overclaim of omitting the actual sample's leverage metric (`0.7517`) in favor of the pre-cut metric render the current text unacceptable as a finished research paper.

SEAT: AGY
VERSION: FULL-REFEREE-V1
VERDICT: REJECT
COUNT: 11
F-lines: NONE
