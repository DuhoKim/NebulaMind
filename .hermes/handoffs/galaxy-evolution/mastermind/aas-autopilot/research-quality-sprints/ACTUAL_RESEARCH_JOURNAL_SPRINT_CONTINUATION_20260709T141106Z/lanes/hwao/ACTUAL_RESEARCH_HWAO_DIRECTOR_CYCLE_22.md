# hwao-agy-low-cycle-22
Started UTC: 2026-07-09T17:00:43Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_22

### 1. Publication-Readiness Verdict
**Flagship RP-1 (Optical AGN Hosts and Catalog sSFR):** **Not Ready.** The manuscript is scientifically honest about its limitations, maintaining a strict association-only boundary. However, the reliance on a 60,000-galaxy "computational pilot cap" selected sequentially by `specObjID` introduces unquantifiable survey-plate and sky-coverage biases. A computational cache limit is not a publishable scientific selection function. To be publication-ready, the analysis must either be run on the full 249,917-galaxy parent sample or use a statistically rigorous, randomized, and physically motivated subsampling method. Additionally, the lack of morphological/structural control (which is available in SDSS data) leaves the result highly degenerate with the mass-morphology relation.

**Supplementary Denominator/Proxy Atlas:** **Not Ready.** The supplement is highly fragmented and currently reads as a collection of incomplete proposals rather than a cohesive atlas. Since it shares the identical 60k computational cap limitation, it suffers from the same fatal selection bias. It should be reframed and condensed into a "Future Work and Missing Observables" section within the flagship, or formalized as a data release paper only after the sample cap is resolved.

### 2. Top 12 Concrete Quality Improvements (Ranked by Scientific Value)
1. **Remove the 60k Cache Cap:** Execute the analysis on the full 249,917 strict four-line S/N $\geq 3$ parent sample to eliminate the arbitrary `specObjID` sorting bias.
2. **Implement Structural/Morphological Matching:** Add SDSS structural proxies (e.g., `fracDeV`, concentration index) to the matching algorithm alongside mass and redshift to break the mass-morphology degeneracy.
3. **Explicit Seyfert vs. LINER Separation:** Separate Seyferts and LINERs in the primary analysis and all figures, rather than just as a tabular sensitivity check, as they represent distinct physical populations (accretion vs. retired stellar populations).
4. **Empirical Aperture Correction:** Use available SDSS photometric data (fiber vs. model/total magnitudes) to estimate and control for the aperture fraction in the sSFR comparisons.
5. **Consolidate the Supplement:** Merge the 8 supplementary notes into a single, cohesive "Requirements for Causal Inference" discussion section in the flagship paper.
6. **Refine the Matching Caliper:** Justify the maximum mass-redshift caliper physically rather than using an arbitrary $\Delta\log M_\star \leq 0.05$ threshold.
7. **Quantify the `specObjID` Bias:** If the 60k cap cannot be lifted, explicitly measure and plot the redshift, mass, and spatial distribution of the capped sample against the parent to fully quantify the introduced bias.
8. **Clarify Unclassified Objects:** Explicitly state the properties of the 67 unclassified objects and justify their retention in the denominator counts while being excluded from matching.
9. **Formal Statistical Testing:** Provide formal non-parametric statistical tests (e.g., Kolmogorov-Smirnov or Anderson-Darling tests) comparing the sSFR distributions of the target and control samples, beyond just the median offset intervals.
10. **Address Fiber Collision Biases:** Explicitly quantify the fraction of the sample affected by the 55-arcsec fiber collision limit, especially in the context of the 10th-neighbor index proxy.
11. **Contextualize with Volume-Complete Literature:** Compare the sample's mass and redshift distributions to known volume-complete SDSS samples from the literature to anchor the selection biases.
12. **Improve Figure 1 (BPT Diagram):** Add contours for the parent population (or the star-forming controls) behind the scatter points to better illustrate the relative densities of the matched populations.

### 3. Improvements Possible Now (Using Real Local SDSS Data)
- **Structural Matching:** SDSS `PhotoObj` provides `fracDeV`, radii, and concentration indices. These can be integrated into the matching algorithm immediately.
- **Seyfert/LINER Splitting:** The pipeline already contains the Kewley et al. (2006) demarcations. You can split the broad BPT classification into Seyfert and LINER sub-populations for the primary analysis.
- **Aperture Proxy:** You can utilize the ratio of fiber magnitudes to total model magnitudes (already in SDSS photometry) as an aperture control.
- **Sample Expansion:** If local compute allows, the workflow can be re-run on the full 249,917 sample to remove the `specObjID` cache bias.

### 4. Requires New Real Data (Must NOT Be Written As Results)
- **Causal Mechanisms of Quenching:** Do not claim AGN feedback causes the lower sSFR.
- **Bolometric Luminosity / Eddington Ratios:** Do not estimate these without real X-ray or bolometric correction data.
- **Gas Mass / Depletion Times:** Do not claim molecular gas depletion or changes in star-formation efficiency without actual CO (e.g., xCOLD GASS) or HI (e.g., xGASS) measurements.
- **Outflow Kinematics:** Do not discuss escape fractions or outflow velocities without spatially resolved IFU data (e.g., MaNGA).
- **Physical Environmental Density:** Do not convert the 10th-neighbor index into a physical halo mass, 3D density, or central/satellite designation without an external group catalog.
- **Maintenance Heating:** Do not estimate radio jet power or X-ray cavity energetics.

### 5. Exact Guidance for the Integrator (Safe Wording/Citation Changes)
- **Wording Change:** Replace instances of "60,000-galaxy computational pilot cap" with a clear warning: "This analysis is currently restricted to a 60,000-galaxy cache limited by local workflow constraints, selected sequentially by `specObjID`. This introduces unquantified survey-plate biases, and absolute fractions must not be interpreted as volume-representative."
- **Wording Change:** In the Abstract and Conclusion, explicitly state: "Because morphology and structural proxies available in SDSS were not controlled in this iteration, the observed sSFR offset remains highly degenerate with the mass-morphology relation."
- **Structural Move:** Move the contents of the *Supplementary SDSS Denominator and Proxy Atlas* into a new section in the flagship titled: "Section 7: Missing Observables and Requirements for Future Causal Inference."
- **No Citation Inventions:** Ensure all citations strictly reference the provided SDSS/BPT/catalog literature. Do not invent DOIs, ADS bibcodes, or arXiv IDs for the missing multi-wavelength surveys.

### 6. No-Mock-Data Receipt and Safety Ledger
- **Read-Only Compliance:** Verified. No files were edited, created, or deleted. No git, DB, API, or live roots were touched.
- **No Mock Data:** Verified. No synthetic, fake, or placeholder data were proposed or utilized.
- **No Fabricated Numbers:** Verified. All numbers, sample sizes, and fractions reflect the exact values provided in the prompt's `REAL-DATA INVENTORY COUNTS` and integrated draft excerpts.
- **Association-Only Boundary:** Verified. The plan explicitly forbids causal claims regarding feedback, quenching, or heating, maintaining the strict optical-association boundary of the existing data.


# command_result
exit_code=0
elapsed_s=35.6
timed_out=False
finished_utc=2026-07-09T17:01:19Z
