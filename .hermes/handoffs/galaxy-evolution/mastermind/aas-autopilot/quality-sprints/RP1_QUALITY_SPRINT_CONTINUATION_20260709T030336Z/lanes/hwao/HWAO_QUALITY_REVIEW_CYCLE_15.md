# hwao-agy-cycle-15
Started UTC: 2026-07-09T04:35:55Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

HWAO_QUALITY_REVIEW_CYCLE_15

## Publication-Readiness Verdict

**RP-1 Flagship:** NOT READY FOR PUBLIC RELEASE. While the scientific guardrails (association-only, aperture caveats, pilot cap limitations) are excellently stated, the reliance on a non-random, fixed-size 60,000-row cap ordered by `specObjID` introduces unquantified sky-coverage and survey-plate biases. It is a strong local proof-of-concept, but it requires a few more clarifications regarding the exact nature of the control pool and the matching process before it is robust enough for public scrutiny.

**Supplementary Atlas:** NOT READY FOR PUBLIC RELEASE. It successfully corrals the 8 preliminary studies into safe denominators, avoiding false causal claims. However, it still reads somewhat like 8 truncated papers stitched together. It needs minor structural polish to function purely as a "follow-up baseline atlas" without confusing readers about its intent.

## Top 10 Concrete Improvements (Ranked by Effect on Scientific Quality)

### Must fix before public
1. **Clarify the 60k Cap Bias (RP-1 & Supp):** Explicitly state that selecting the first 60,000 objects by `specObjID` introduces a sky-distribution/survey-plate bias (since SDSS IDs are tied to plates/MJD). The integrator must add a sentence in Section 2 clarifying that this is not a random draw from the parent.
2. **Define Star-Forming Controls (RP-1):** In Section 3, explicitly define what constitutes the "star-forming control" pool. Is it everything below the Kauffmann (2003) line? State it clearly so the matching pool is reproducible.
3. **Clarify "Positive Errors" (RP-1 Table 1):** The phrase "positive errors" in the selection cascade table is slightly ambiguous. Update the wording to explicitly mean "valid flux variance/error measurements (e.g., `ivar > 0`)".
4. **Clarify the Seyfert/LINER split in abstract (RP-1):** The abstract mentions that narrower Seyfert-like definitions reduce the offset, but should briefly clarify *why* (e.g., "removing LINER-like retired galaxies"). 

### Nice local polish
5. **Move Bootstrap Definition (RP-1):** In the abstract and Section 4, explicitly state that the `[-1.334, -1.283] dex` interval is a 95% confidence interval on the median offset.
6. **Harmonize Atlas Subsections (Supp):** Ensure all 8 subsections in the supplement begin with the exact same framing sentence structure to drive home that these are parallel baselines of the *same* denominator, not sequential discoveries.
7. **Refine Table 2 (Supp):** In the atlas summary table, rename the "Role" column to something like "Future Follow-up Domain" to completely stamp out any implication that these are completed studies.

### Needs new data
8. **Morphological Matching:** The 3-arcsec fiber bias cannot be resolved without incorporating structural data (e.g., bulge-to-total mass ratios or Sérsic indices from Simard et al. or Mendel et al.). Matching on morphology is the only way to separate AGN feedback from simple bulge-driven star formation suppression.
9. **Global SFRs:** The catalog sSFR is aperture-corrected, but relying on global UV+IR SFRs (e.g., from GALEX/WISE) is required to truly confirm that the global star formation is suppressed, rather than just the nuclear region.
10. **Halo Mass & Environment:** Group catalog matching (central vs. satellite, halo mass) is required to rule out environmental quenching as the primary driver of the observed offset.

## Safe Changes for the Integrator

The integrator is authorized to make the following exact wording/section changes to the `.tex` files:
- **RP-1 Section 2 & Supp Section 2:** Add a sentence clarifying that the 60,000 `specObjID` cap introduces a spatial/survey-plate bias and is not a random sampling of the parent volume.
- **RP-1 Section 3:** Add one sentence explicitly defining the star-forming control pool (e.g., "objects falling below the Kauffmann et al. 2003 demarcation").
- **RP-1 & Supp Tables 1/2:** Change "positive errors" to "valid flux measurements (inverse variance $> 0$)".
- **RP-1 Abstract & Section 4:** Add "95\% confidence interval" when mentioning the bootstrap interval.
- **Supp Table 2:** Rename the "Role" column header to "Future Follow-up Domain".

**DO NOT** change any numeric results. **DO NOT** alter the core claim boundary (it must remain an association-only, fixed-size pilot study). **DO NOT** run new SQL queries or change the data table.

## Safety Ledger
- No files were edited or overwritten.
- No public APIs, databases, or wikis were touched.
- No git commits, pushes, or deployments were executed.
- Review performed strictly on the provided local `.tex` and markdown package text.
- No external manuscript submissions were initiated.


# command_result
exit_code=0
elapsed_s=29.1
timed_out=False
finished_utc=2026-07-09T04:36:24Z
