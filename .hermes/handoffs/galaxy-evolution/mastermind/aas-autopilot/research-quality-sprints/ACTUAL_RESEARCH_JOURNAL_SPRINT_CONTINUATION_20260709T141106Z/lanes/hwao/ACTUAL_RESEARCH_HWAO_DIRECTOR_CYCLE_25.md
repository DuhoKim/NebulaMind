# hwao-agy-low-cycle-25
Started UTC: 2026-07-09T17:21:48Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_25

**Publication-Readiness Verdict**
Both the RP-1 flagship draft and the supplementary denominator/proxy atlas are **NOT READY** for publication as physical or causal claims, but they are approaching readiness as **association-only methodology pilots**. The text correctly restricts its claims to the optical emission-line denominator, but the presence of a non-random 60,000-galaxy `specObjID` computational cap introduces severe survey-plate and sky-coverage biases. Until the matching explicitly controls for structural proxies (which are available in the local SDSS data), the headline -1.309 dex sSFR offset remains indistinguishably degenerate with the standard mass-morphology relation. They cannot be submitted to an external journal until the structural controls are implemented and the sample selection is properly randomized or complete.

**Top 12 Concrete Quality Improvements (Ranked by Scientific Value)**
1. **Implement Structural Matching**: Incorporate `fracDeV` or concentration index (from the already-joined `PhotoObj` table) into the Euclidean nearest-neighbor match to break the mass-morphology degeneracy. 
2. **Aperture-Fraction Control**: Add a control for the 3-arcsec fiber aperture fraction (using photometric sizes vs fiber radius) to account for extended disk star formation systematically missed in the central fiber.
3. **Remove `specObjID` Sequential Cap Bias**: Replace the non-random 60,000-galaxy sequential cache cap with a purely random subsample of the 249,917-galaxy parent to eliminate survey-plate and sky-coverage clustering bias.
4. **Spectroscopic Fiber-Collision Correction**: Calculate and apply a 55-arcsec fiber-collision weight correction to the 10th-neighbor index, which is currently systematically biased in dense environments.
5. **Formalize Seyfert/LINER Separation**: Elevate the Kewley et al. (2006) high-excitation (Seyfert-like) cut from a supplemental robustness check to a primary parallel analysis track to isolate actual accretion-driven excitation from retired/post-AGB stellar populations.
6. **Marginal Distribution Table**: Add a table explicitly quantifying the marginal distribution differences (in mass, redshift, and sSFR bins) between the 60,000-galaxy cache and the 249,917-galaxy parent to prove the cap's relative neutrality.
7. **Incorporate Existing SDSS Group Catalogs**: If local volume-complete group catalogs (e.g., Yang et al.) are available in the cached inventory, use them to assign basic central/satellite labels instead of relying solely on the raw 10th-neighbor index.
8. **Stricter Matching Caliper Test**: Introduce an extremely strict matching caliper (e.g., $|\Delta\log M_\star|\leq0.02$, $|\Delta z|\leq0.001$) to explicitly verify that the Euclidean match with replacement is not artificially inflating the control pool distance.
9. **Clarify H$\alpha$ Luminosity Proxy Assumptions**: Explicitly document the model assumptions behind the `galSpecExtra` aperture-corrected H$\alpha$ luminosity proxy, noting that it assumes line emission tracks the broadband light profile.
10. **Include Unclassified Objects in Baselines**: Ensure the 67 unclassified BPT objects are systematically accounted for in the broader denominator tables before they are excluded from the control match.
11. **Standardize Subset Terminology**: Ensure "broad optical BPT-selected galaxies" is rigorously distinguished from "Seyfert-like proxies" across all 8 supplementary atlas sections to avoid terminology drift.
12. **Abstract Disclaimer**: Front-load the abstract of the flagship paper with an explicit statement that the -1.309 dex offset is highly degenerate with bulge prominence. 

**What Can Be Improved NOW Using Real Local SDSS Data Already Inventoried**
We have `PhotoObj` and `galSpecExtra` fully joined in the cache. This means we can immediately implement:
* **Structural proxies**: We can extract `fracDeV` and concentration indices to control for morphology.
* **Aperture controls**: We can compute the ratio of the 3-arcsec fiber to the total photometric radius.
* **Randomized capping**: We can randomize the 60k draw from the 249,917 parent instead of sorting by `specObjID`.
* **Sub-classification**: We can fully compute the Kewley (2006) demarcations to filter out the low-ionization retired/LINER branch.

**What Requires New Real Data (Must NOT Be Written as a Result Yet)**
We absolutely must not write conclusions regarding causal physical feedback or quenching mechanisms. The following require external data currently missing from our analysis:
* **Gas Depletion / Star Formation Efficiency**: Requires CO/HI mass measurements (e.g., ALMA, IRAM, xCOLD GASS).
* **Maintenance Heating / Radio Jets**: Requires X-ray cavity/cooling measurements (Chandra/XMM) and calibrated radio jet morphology/powers (FIRST/NVSS/LOFAR).
* **Outflow Escape vs. Recycling**: Requires spatially resolved IFU kinematics (MaNGA/SAMI) and CGM multiphase tracers.
* **True Environmental Quenching**: Requires calibrated dark-matter halo masses and definitive central/satellite designations, not just a 10th-neighbor proxy.

**Exact Guidance for the Integrator (Safe Wording/Citation Changes Only)**
* **DO NOT** edit code, rerun the pipeline, or touch database states.
* **DO** edit the TeX draft to explicitly state: "The 60,000-galaxy cap is a sequential computational limit and is not a volume-complete or randomized sample."
* **DO** prefix the -1.309 dex offset claim with the phrase: "Without controlling for structural morphology or aperture fraction..."
* **DO** ensure the word "association" replaces any accidental use of "cause," "drives," "regulates," or "quenches" when discussing the BPT match.
* **DO** maintain the separation between the SDSS/BPT citations (which validate the observed data) and the multiwavelength/simulation citations (which strictly motivate missing follow-up observables).

**No-Mock-Data Receipt and Safety Ledger**
* **MOCK DATA CHECK**: CLEAN. No synthetic values, mock samples, or hallucinated citations were generated. All counts (e.g., 249,917 parent; 60,000 cache cap; 8,146 matched pairs; 67 unclassified; -1.309 dex offset) are extracted verbatim from the provided real-data TeX excerpts.
* **ACTION CHECK**: CLEAN. Read-only limits strictly observed. No git commits, database writes, external network requests, or file modifications were executed.
* **CITATION CHECK**: CLEAN. No URLs, DOIs, arXiv IDs, or ADS bibcodes were invented. Standard literature (Kauffmann 2003, Kewley 2006) was referenced exactly as provided in the context.


# command_result
exit_code=0
elapsed_s=39.8
timed_out=False
finished_utc=2026-07-09T17:22:28Z
