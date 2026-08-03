# hwao-agy-cycle-7
Started UTC: 2026-07-09T02:50:38Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

HWAO_QUALITY_REVIEW_CYCLE_07

**Publication-Readiness Verdict**
- **RP-1 Flagship:** The manuscript is highly disciplined and successfully maintains the required association-only boundary. It accurately reflects the limitations of the cached data and correctly interprets the sensitivity of the result to LINER-like contamination. However, before any public release, the abstract must more prominently feature the offset reduction seen with stricter cuts, as this severely qualifies the primary -1.309 dex offset. Currently **Not Ready for Public Release (Local Polish Required)**.
- **Supplementary Atlas:** The supplement does an excellent job of packaging the 8 distinct denominators without overclaiming. The guardrails are strong and explicit. **Ready for Local Use (Minor Polish Recommended)**.

---

### Top 10 Prioritized Quality Improvements

**Category A: Must Fix Before Public (Crucial Caveats)**
These changes ensure the manuscript cannot be misquoted by readers skimming for feedback validation.

1. **RP-1 Abstract - Include the Seyfert-Proxy Offset Reduction:** The abstract quotes the -1.309 dex offset but does not mention that stricter line-S/N and Seyfert-like cuts reduce this offset to roughly half (-0.763 dex). This reduction must be in the abstract to prevent the -1.309 dex figure from being cited out of context as a pure AGN effect.
2. **RP-1 Section 2 - Define the "Cap" Mechanism:** The text repeatedly mentions a "non-random, capped 60,000-row emission-line cache." The paper must state exactly *how* it was capped (e.g., "capped by an arbitrary database row limit during pilot query execution" or similar) so the selection bias is transparent.
3. **Supplement Section 3.8 - Emphasize Selection-Function Matching for Mocks:** Make it explicitly clear in the text that any simulation validation using this target vector *must* pass the simulated galaxies through the exact same optical S/N and fiber-aperture selection function, otherwise the comparison is invalid.

**Category B: Nice Local Polish (Safe Wording/Section Changes)**
These are safe instructions for the integrator to improve readability and internal consistency. 

4. **RP-1 & Supplement - Standardize Terminology:** Unify the terms "cached denominator", "pilot cache", "capped 60,000-row cache", and "60,000-galaxy sample". Pick one standard phrase (e.g., "capped 60k-row pilot cache") and use it consistently across both PDFs. 
5. **RP-1 Section 5 - Clarify LINER Contamination Implications:** Strengthen the wording in the interpretation. Explicitly state: "Because the Seyfert-like proxy halves the sSFR offset, a significant fraction of the broad-BPT association is driven by retired galaxies with LINER-like emission rather than active black-hole accretion."
6. **Supplement Section 3.1 - Contextualize the Density Proxy:** Briefly mention in the text how a 10th-neighbor proxy typically behaves (e.g., whether it traces local environment or larger halo scale) to help readers understand why it is not a substitute for robust central/satellite labels.
7. **RP-1 Section 1 - Explicit List of Missing Observables:** Move or mirror the list of missing observables from Section 6 (Conclusion) into Section 1 (Question and claim boundary). This sets the stage immediately that the paper will not address these physical drivers.
8. **Supplement Abstract - Reinforce the "Atlas" Nature:** Add a concluding sentence: "This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables."

**Category C: Needs New Data (Acknowledge Only, Do Not Claim)**
These represent the physical boundary the current text correctly avoids crossing.

9. **Direct Gas Mass Measurements:** Resolving whether the observed sSFR offset is driven by gas depletion or reduced star-formation efficiency requires targeted CO/HI or dust-continuum follow-up. 
10. **Radio/X-Ray Energetics:** Testing maintenance heating or jet-environment coupling requires calibrated radio jet powers and X-ray cavity/cooling measurements, which cannot be inferred from the optical duty-cycle denominators provided.

---

### Instructions for the Integrator

**Safe to Change:**
- You may update the RP-1 abstract to include the -0.763 dex Seyfert-like proxy offset.
- You may add explanatory text regarding the nature of the 60,000-row cap.
- You may standardize terminology regarding the "pilot cache" across both `.tex` files.
- You may strengthen caveats emphasizing LINER contamination and the necessity of applying optical selection functions to simulation mocks.

**DO NOT Change (Unsafe):**
- Do not alter the core matched-pair counts (8,146) or the median $\Delta\log {\rm sSFR}$ results (-1.309 dex, -0.763 dex).
- Do not remove the "association only" language. 
- Do not introduce claims that the observed sSFR drop is causally linked to AGN feedback, heating, or outflows. 
- Do not attempt to extrapolate the 24.0% cached fraction to a volume-limited population density.

---

### Safety Ledger
- **Status:** Read-only review completed.
- **File modifications:** 0 files modified.
- **System actions:** No database writes, API calls, or external submissions performed.
- **Public exposure:** Zero. Package remains strictly local. No git commits or deployments executed.


# command_result
exit_code=0
elapsed_s=30.9
timed_out=False
finished_utc=2026-07-09T02:51:08Z
