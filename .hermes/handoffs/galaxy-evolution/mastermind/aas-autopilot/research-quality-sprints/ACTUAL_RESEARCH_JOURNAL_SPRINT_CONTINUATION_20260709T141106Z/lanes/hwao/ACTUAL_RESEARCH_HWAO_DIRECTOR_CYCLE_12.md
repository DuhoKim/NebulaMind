# hwao-agy-low-cycle-12
Started UTC: 2026-07-09T15:42:04Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_12

### Publication-Readiness Verdict
**Verdict: Not Ready for External Submission (Internal Pilot Status)**
Neither the RP-1 Flagship nor the Supplementary Atlas is ready for external journal submission in their current state. Both drafts rely on an arbitrary 60,000-galaxy "computational pilot cap" sequentially selected by `specObjID`, which introduces unquantified survey-plate and sky-coverage biases. While the manuscripts explicitly and transparently caveat this limitation, reporting an arbitrary cache limit as the primary sample for an SDSS study is not acceptable for a final journal publication when the full 249,917 S/N $\geq 3$ parent sample exists. Furthermore, the lack of morphology and aperture-fraction controls in the matching process leaves the central 3-arcsec fiber bias highly degenerate with the bulge-to-disk ratio, meaning the observed -1.309 dex sSFR offset cannot be isolated from standard structural correlations. The papers represent excellent, rigorously caveated observational baselines and workflow validations, but must remain internal until the sample cap is removed or the missing structural controls are added.

### Top 12 Concrete Quality Improvements (Ranked by Scientific Value)
1. **Remove the 60,000-Galaxy Cache Cap:** Expand the analysis to the full 249,917-galaxy strict four-line S/N $\geq 3$ parent sample to eliminate arbitrary plate targeting and sky-coverage biases.
2. **Incorporate Morphology Controls:** Add a bulge-to-total ratio or structural morphology proxy to the matching criteria to break the degeneracy between the 3-arcsec fiber aperture effect and true sSFR suppression.
3. **Control for Fiber Aperture Fraction:** Match controls on redshift and physical fiber coverage to mitigate the systematic under-sampling of extended star-forming disks at low redshift.
4. **Disaggregate Seyfert and LINER/Retired Populations:** Elevate the Seyfert-like Kewley et al. (2006) cut from a sensitivity check to a primary parallel analysis track to distinguish true accretion-driven AGN from hot post-AGB retired stellar populations.
5. **Integrate Existing SDSS Group Catalogs:** Cross-match with public SDSS group catalogs to add central/satellite labels and halo mass estimates, upgrading the 10th-neighbor index to a physical environmental metric.
6. **Apply Fiber-Collision Corrections:** Implement a spectroscopic fiber-collision correction at the 55-arcsec scale to resolve the systematic undercounting of close neighbors in dense environments for the neighbor-rank baseline.
7. **Add $D_n(4000)$ or EW(H$\alpha$) Diagnostics:** Use available spectral indices to explicitly quantify and control for the fraction of broad BPT targets that are retired galaxies rather than active galactic nuclei.
8. **Adopt the Moderate Caliper by Default:** Switch the primary matched-control result from the unrestricted nearest-neighbor match to the moderate caliper ($|\Delta\log M_\star| \leq 0.05$ and $|\Delta z| \leq 0.002$) to guarantee strict pairing balance.
9. **Environment-Matched Controls:** Include the local environmental density proxy (e.g., the 10th-neighbor index) directly in the matching vector to ensure the sSFR offset is not purely density-driven.
10. **Include AGN Luminosity Proxies:** Utilize [O III] $\lambda 5007$ luminosity or existing MPA-JHU AGN proxies to evaluate if the sSFR offset scales with proxy accretion power.
11. **Refine the Dust Correction for H$\alpha$:** Explicitly validate the Balmer decrement dust-attenuation correction applied to the H$\alpha$ luminosity proxy used in the gas-depletion baseline.
12. **Model the Redshift Selection Function:** Apply a rigorous $V_{\rm max}$ or multi-redshift volume correction within the $0.02 < z < 0.12$ slice to test for evolutionary or mass-incompleteness biases across the window.

### What Can Be Improved Now Using Real Local SDSS Data Already Inventoried
*   Applying the moderate mass-redshift caliper ($|\Delta\log M_\star| \leq 0.05$, $|\Delta z| \leq 0.002$) as the primary matching threshold rather than a sensitivity variant.
*   Reporting the Seyfert-like Kewley et al. (2006) subset as a primary matched-control track alongside the broad BPT track, as the data is already computed (yielding the -0.763 dex offset).
*   Using the existing `galSpecExtra` and `galSpecInfo` catalogs to investigate $D_n(4000)$ and EW(H$\alpha$) distributions for the currently retained sample.
*   Upgrading the neighbor-count baseline with the already inventoried public data to verify relative density distributions within the cached sample.

### What Requires New Real Data (Must NOT Be Written As A Result Yet)
*   **Causal Feedback Claims:** Any assertion that the AGN is physically quenching star formation (requires time-domain modeling, outflow rates, and total gas mass).
*   **Total Gas Mass / Depletion Times:** Determining if the sSFR offset is due to missing gas or suppressed efficiency (requires ALMA CO or HI data).
*   **Resolved Kinematics:** Claims about outflow escape versus recycling (requires IFU data like MaNGA to measure resolved velocities and halo potentials).
*   **Radio-Mode / Jet Coupling:** Assertions about maintenance heating energetics (requires VLA/LOFAR radio morphology and Chandra/XMM X-ray cavity data).
*   **Global sSFR Suppression:** Claims that the *entire* galaxy is quenched, rather than just the central 1.2–6.5 kpc covered by the fiber (requires spatially resolved IFU spectroscopy).

### Exact Guidance for the Integrator: Safe Wording/Citation Changes Only
*   **Preserve Pilot Caveats:** Do not soften or remove the warnings regarding the 60,000-galaxy cache cap, the non-random `specObjID` selection, or the resulting sky-coverage bias.
*   **Enforce "Association-Only" Language:** Ensure all verbs describing the matched-control result state "is associated with" rather than "causes," "quenches," "suppresses," or "drives."
*   **Maintain Denominator Boundaries:** Ensure that the Supplementary Atlas strictly describes its entries as "optical denominators" or "target vectors" for future work, explicitly listing the radio, X-ray, CO/HI, and IFU references as *missing observables*.
*   **Morphology Caveats:** Ensure the limitation regarding the 3-arcsec fiber and the lack of morphology controls remains prominent in the abstract and conclusion of the flagship.

### No-Mock-Data Receipt and Safety Ledger
*   **Mock/Synthetic Data Generated:** 0
*   **Invented Numbers/Citations/URLs:** 0
*   **File/Database/Git/Live Root Mutations:** 0 (Strict read-only review mode maintained).
*   **Data Provenance:** All quoted values (-1.309 dex, -0.763 dex, 60,000 cap, 249,917 parent, etc.) were sourced directly from the provided read-only text context.
*   **Boundary Enforcement:** Association-only boundary explicitly preserved and strongly defended in the triage plan.


# command_result
exit_code=0
elapsed_s=36.6
timed_out=False
finished_utc=2026-07-09T15:42:41Z
