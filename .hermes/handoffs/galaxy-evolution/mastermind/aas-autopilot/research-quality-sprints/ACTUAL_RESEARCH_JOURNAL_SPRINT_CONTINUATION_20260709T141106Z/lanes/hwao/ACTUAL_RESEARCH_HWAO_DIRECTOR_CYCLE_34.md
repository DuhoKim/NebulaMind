# hwao-agy-low-cycle-34
Started UTC: 2026-07-09T18:31:17Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_34

### Publication-Readiness Verdict
**RP-1 Flagship & Supplementary Atlas:** Both manuscripts are fundamentally sound as an **association-only pilot study** and an **observational baseline atlas**, respectively. They are remarkably disciplined in explicitly defining their selection biases, aperture limitations, and missing observables. However, they are **not ready** to be published as papers testing causal physical mechanisms (e.g., AGN feedback, quenching, or outflow escape) due to the uncontrolled structural morphology and the reliance on fiber-centered optical data alone. As methodological and baseline papers, they are close to readiness, provided the narrative strictly remains within the stated association boundaries.

### Top 12 Concrete Quality Improvements (Ranked by Scientific Value)

**What can be improved NOW using real local SDSS data already inventoried or publicly available:**
1. **Re-integrate Structural Morphology (`PhotoObj`):** The most critical flaw is the lack of morphology control. Since `PhotoObj` was used in the catalog backbone, re-run the cache pipeline to retain $R_{90}/R_{50}$ (concentration index) and `fracDeV`. This allows separating bulge-driven mass-morphology effects from genuine AGN-host excitation offsets.
2. **Include Aperture Coverage Fraction:** Calculate the physical fraction of each galaxy covered by the 3-arcsec fiber using the redshift and photometric sizes. This provides a direct flag for systems highly susceptible to central-to-global mismatch.
3. **Expand Matching Parameters:** Upgrade the matched-control algorithm to include the concentration index and aperture coverage fraction alongside stellar mass and redshift.
4. **Formalize Seyfert vs. LINER-like Stratification:** Instead of treating the Seyfert-like Kewley demarcation merely as a sensitivity check, establish it as a parallel primary track to explicitly isolate true AGN from post-AGB/retired LINER-like bulges.
5. **Quantify the Passive Galaxy Loss:** Calculate the exact demographic shift caused by the strict 4-line S/N $\geq 3$ cut. Provide a comparison of the $M_\star$-sSFR plane before and after this cut to explicitly show the bias against quiescent hosts.
6. **Audit the 67 Unclassified Objects:** Briefly verify the properties of the 67 unclassified objects to ensure they are simply low-S/N or masked data rather than a structurally distinct sub-population.

**What requires NEW real data (Must NOT be written as a result yet):**
7. **Bolometric AGN Power & Accretion Rates:** Requires cross-matching with X-ray (e.g., eROSITA, Chandra) or radio catalogs to measure actual AGN luminosity, rather than relying on optical excitation classes.
8. **Resolved Spatial Gradients & Kinematics:** Requires IFU data (e.g., SDSS-IV MaNGA) to resolve central versus extended disk star formation, breaking the 3-arcsec aperture bias, and to measure true outflow velocities.
9. **Direct Cold Gas Measurements:** Requires ALMA or IRAM CO/HI observations to separate true molecular gas depletion from mere suppression of star-formation efficiency.
10. **Robust Halo Mass & Central/Satellite Labels:** Requires integration with formal group/cluster catalogs (e.g., Tinker or Yang catalogs) to replace the highly biased, fiber-collision-affected 10th-neighbor index.
11. **Spectroscopic Fiber-Collision Corrections:** Requires statistical forward modeling or overlapping multi-pass survey data to correct the projected-neighbor statistics in dense environments.
12. **Forward-Modeled Cosmological Simulations:** Requires passing simulated galaxies (e.g., IllustrisTNG, EAGLE) through the exact SDSS target selection, fiber aperture, and S/N cuts to compare theoretical feedback models against this empirical baseline.

### Exact Guidance for the Integrator (Safe Wording/Citation Changes Only)
- **Morphology Caveat:** Strengthen the wording in the abstract and conclusion to state that the observed -1.309 dex sSFR offset is currently indistinguishable from a morphology/bulge-fraction effect.
- **Neighbor-Index Warning:** Ensure the text aggressively flags that the 10th-neighbor index is explicitly biased by the SDSS 55-arcsec fiber collision limit and *cannot* be read as physical density.
- **BPT Class Clarification:** Double-check that all references to the primary sample use "broad optical BPT-selected" and never accidentally shorten it to "AGN", given the known LINER/retired contamination.
- **No Results Alteration:** Do not change any numbers (e.g., 60,000, 8,146, -1.309 dex, -0.763 dex). Do not invent mock morphology distributions. If the `PhotoObj` re-cache is not performed in this cycle, the morphology control must remain strictly in the "missing observables" section.

### No-Mock-Data Receipt and Safety Ledger
- **Mock/Synthetic Data:** ZERO mock, fake, placeholder, or toy data proposed or generated.
- **Invented Values:** ZERO values invented. All numerical values, sample sizes (e.g., 249,917 public parent; 60,000 subset; 24.0% coverage), and statistical outputs are cited precisely from the provided manuscript context.
- **Read-Only Verification:** Strict adherence to read-only mode. No files were edited, no public pages deployed, no databases mutated, and no Git history touched.
- **Association Boundary:** Maintained intact. The plan explicitly prohibits causal physical claims without the integration of new, real multiwavelength/IFU observables.


# command_result
exit_code=0
elapsed_s=31.0
timed_out=False
finished_utc=2026-07-09T18:31:48Z
