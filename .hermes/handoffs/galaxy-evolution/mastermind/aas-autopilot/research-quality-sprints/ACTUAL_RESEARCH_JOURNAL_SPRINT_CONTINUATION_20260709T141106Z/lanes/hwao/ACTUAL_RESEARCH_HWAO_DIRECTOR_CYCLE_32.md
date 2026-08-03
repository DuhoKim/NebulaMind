# hwao-agy-low-cycle-32
Started UTC: 2026-07-09T18:16:23Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_32

Here is the paper-quality triage plan for cycle 32, working strictly in read-only review mode with no mock data and no unauthorized system edits.

### 1. Publication-Readiness Verdict
*   **RP-1 Flagship (`rp1_flagship_polished.tex`)**: *Not yet ready for external submission, but structurally sound as a guarded pilot.* The manuscript successfully maintains the strict association-only boundary, clearly disclaiming causal feedback inferences. However, its presentation needs refinement to ensure the lack of morphological/aperture control is not just stated, but critically contextualized within the limitations of the fixed 60,000-galaxy cache.
*   **Supplementary Denominator Atlas (`supplementary_denominator_atlas.tex`)**: *Functionally ready as an internal follow-up checklist, but requires structural polishing for journal alignment.* The atlas successfully aggregates eight distinct proposals into a single, selection-biased optical baseline. It effectively serves as a ledger of missing observables.

### 2. Top 12 Concrete Quality Improvements (Ranked by Scientific Value)
1.  **Contextualize the Mass-Morphology Degeneracy**: Explicitly clarify in the flagship discussion how the missing `fracDeV` and $R_{90}/R_{50}$ parameters (omitted from the 60k cache) prevent breaking the degeneracy between excitation-linked quenching and passive bulge-dominated populations.
2.  **Clarify the S/N Selection Function Bias**: Enhance the explanation of how the $S/N \geq 3$ BPT requirement actively filters out low-equivalent-width passive galaxies, thus artificially skewing the denominator's representativeness of the full quenched population.
3.  **Refine LINER vs. Seyfert Distinctions**: Strengthen the flagship's discussion of why the $\Delta\log {\rm sSFR}$ offset drops from -1.309 dex to -0.763 dex when applying the stricter Kewley et al. (2006) demarcation (removing retired/LINER-like bulges).
4.  **Aperture Effect Caveats**: Expand the explanation of how the fixed 3-arcsec SDSS fiber (subtending 1.2–6.5 kpc at $0.02<z<0.12$) systematically underestimates extended disk star formation, especially in matched controls.
5.  **Fiber-Collision Bias Explication**: In the atlas, add a deeper methodological disclaimer about how the 55-arcsec fiber-collision limit specifically suppresses close-pair neighbor counts, skewing the 10th-neighbor index in dense group environments.
6.  **Unify Terminology**: Ensure "broad optical BPT-selected galaxies" is used consistently across both the flagship and the atlas when referring to the inclusive emission-line class, reserving "Seyfert-like" only for the specific high-excitation subset.
7.  **Match Quality Transparency**: Recommend adding descriptive text (not new data) detailing the variance-normalized Euclidean matching distributions (e.g., reinforcing the median absolute separations of 0.0045 dex in $\log M_\star$ and 0.00021 in $z$).
8.  **Explicit Cross-Referencing**: Add clear directional pointers in the flagship abstract and conclusion pointing readers directly to the Supplementary Atlas for the inventory of missing multiwavelength observables.
9.  **Atlas Section Parity**: Standardize the structure of the eight atlas subsections so that every subsection explicitly ends with the identical "This entry remains an optical baseline only..." disclaimer format.
10. **Refine Subclass Sensitivity Context**: In the flagship's Table 2, expand the "Interpretation" column for the greedy no-replacement stress test (-1.446 dex) to explain why the poorer balance drives the offset lower.
11. **Strengthen the Non-Volume-Complete Disclaimer**: Reiterate in the atlas introduction that the sequential `specObjID` selection precludes derivation of absolute volume densities or luminosity functions.
12. **Methodological Citation Verification**: Ensure that the citations for the `galSpecExtra` catalog estimators (`lgm_tot_p50` and `specsfr_tot_p50`) are fully integrated into the methodology sections without suggesting new data derivations.

### 3. What Can Be Improved Now Using Real Local SDSS Data Already Inventoried
*   **Wording and Framing**: We can tighten the language around the mass--redshift Euclidean matching, clarifying the replacement strategy and the caliper sensitivity bounds.
*   **Contextualizing Cached Data**: We can explicitly document that while `PhotoObj` was joined, the structural parameters were not cached, framing this not as an oversight but as a defined boundary of the current sprint's selection limits.
*   **Literature Placement**: We can safely integrate existing citations (e.g., Kewley, Kauffmann, Stasińska, Schawinski) to explain the physical differences between the -1.309 dex (broad BPT) and -0.763 dex (Seyfert-like) offsets.

### 4. What Requires New Real Data (MUST NOT Be Written as a Result Yet)
*   **Morphological matching**: Cannot claim to isolate AGN feedback from bulge-mass correlations without `$R_{90}/R_{50}$` or `fracDeV`.
*   **Aperture corrections**: Cannot claim global galaxy quenching rates without resolved IFU data (e.g., MaNGA) to model the outer disk star formation.
*   **Physical environment density**: Cannot map the 10th-neighbor index to physical halo mass or central/satellite designations without group catalogs.
*   **Gas depletion times**: Cannot claim molecular gas depletion or heating efficiencies without ALMA/IRAM CO/HI measurements and X-ray/radio cavity energetics.
*   **Kinematic escape fractions**: Cannot determine outflow escape versus recycling without resolved multiphase velocity profiles.

### 5. Exact Guidance for the Integrator (Safe Wording/Citation Changes Only)
*   **Integrator Directive**: You are authorized *only* to apply wording improvements, structural reorganizations, and citation placements. 
*   **Prohibited Actions**: Do not compute new medians, standard deviations, or subset counts. Do not extrapolate the cached 60,000-galaxy fractions to the 249,917-galaxy parent. 
*   **Tone**: Ensure the tone remains hyper-cautious. When describing the matched offset (-1.309 dex), always pair it with the phrase "within this morphology-uncontrolled optical denominator."
*   **Citations**: Use only the literature already provided in the context (e.g., `cidfernandes2011`, `kewley2006`, `bluck2014`). Do not invent ADS bibcodes or DOIs.

### 6. No-Mock-Data Receipt and Safety Ledger
*   **Mock Data Status**: NO mock, synthetic, toy, or placeholder data has been used or proposed.
*   **Data Provenance**: All quantitative values cited (-1.309 dex offset, 60,000 cached rows, 249,917 parent rows, 8,146 matched pairs, etc.) are strictly sourced from the provided cycle 32 context and the local SDSS real-data inventory.
*   **System Interactions**: NO files were edited, NO public pages deployed, NO databases mutated, NO git histories rewritten, and NO external submissions initiated. Operations remained 100% read-only and analytical.


# command_result
exit_code=0
elapsed_s=33.2
timed_out=False
finished_utc=2026-07-09T18:16:56Z
