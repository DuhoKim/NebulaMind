# gemini-deep-research-low-cycle-37
Started UTC: 2026-07-09T18:56:27Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_GEMINI_DEEP_RESEARCH_CYCLE_37

### 1. Source-Grounded Literature Packet for RP-1 Flagship and Supplement

Below is the verified literature packet containing real, public sources to support the missing observable follow-ups and interpretation caveats in the RP-1 flagship and supplementary atlas.

*   **Source 1:** Piotrowska, J. M., Bluck, A. F. L., et al., 2022, MNRAS, 512, 1052. (DOI: 10.1093/mnras/stac535, arXiv:2112.07661)
    *   **Role:** Interpretation caveat / Future-data motivation.
    *   **Context:** Demonstrates that central velocity dispersion ($\sigma_c$) and bulge prominence are the primary predictive proxies for central galaxy quenching, heavily degenerating with AGN selection in optical fibers.
*   **Source 2:** Saintonge, A., Catinella, B., et al. (xCOLD GASS), 2017, ApJS, 233, 22. (DOI: 10.3847/1538-4365/aa97e0, arXiv:1710.04229)
    *   **Role:** Future-data motivation.
    *   **Context:** Provides the necessary $M_{\text{mol}}$ / SFR baseline to test global molecular gas depletion; crucial for motivating CO/HI follow-up since AGN effects on global scales often wash out compared to inactive mass-matched controls.
*   **Source 3:** Harrison, C. M., Costa, T., et al., 2018, Nature Astronomy, 2, 198. (DOI: 10.1038/s41550-018-0403-6, arXiv:1802.10306)
    *   **Role:** Future-data motivation / Interpretation caveat.
    *   **Context:** IFU kinematics are required to separate non-circular outflow motions from galaxy rotation and to determine if high-excitation outflows actually exceed the halo escape fraction.
*   **Source 4:** Heckman, T. M., & Best, P. N., 2014, ARA&A, 52, 589. (DOI: 10.1146/annurev-astro-081913-035722, arXiv:1403.4620)
    *   **Role:** Actual method support / Future-data motivation.
    *   **Context:** Establishes the fundamental separation between radiative-mode (optical BPT) and jet-mode (radio/X-ray maintenance) accretion, dictating that optical BPT selection cannot independently measure mechanical duty cycles without X-ray/radio data.
*   **Source 5:** Bluck, A. F. L., Mendel, J. T., et al., 2014, MNRAS, 441, 599. (DOI: 10.1093/mnras/stu500, arXiv:1403.5269)
    *   **Role:** Interpretation caveat.
    *   **Context:** Confirms that bulge mass is the tightest correlator with passive fractions in the local SDSS volume, requiring structural controls when comparing BPT-selected samples.

---

### 2. Missing Real Observables

Consistent with the fixed 60,000-galaxy optical SDSS selection, the following required observables are strictly missing from the current data inventory. They must be treated as future follow-up targets, not measured results:
*   **Morphology / Structure:** Central velocity dispersion ($\sigma_c$), bulge fraction, Sérsic index, concentration index, and aperture-fraction corrections.
*   **Gas Measurements (CO/HI):** Molecular and neutral gas masses, gas depletion timescales ($t_{\rm depl}$), and dust continuum estimates.
*   **Resolved Outflow Kinematics:** IFU velocity maps, $W_{80}$ line widths, and spatially resolved multiphase (ionized/molecular/neutral) CGM outflow components.
*   **Radio and X-ray Data:** Radio jet morphology, mechanical cavity energetics, X-ray cooling luminosities, and hot-gas densities.
*   **Environment / Halos:** Verified central/satellite labels, volume-complete halo masses, and group catalog matching (beyond the fiber-collided 10th-neighbor index).
*   **Simulations:** Forward-modeled mock catalogs matching the exact SDSS optical selection function and fiber aperture.

---

### 3. Exact Safe Wording and Citation Insertion Suggestions

**For the Flagship (rp1_flagship_polished.tex):**
*   *Location:* End of the "Morphology and aperture caveat" paragraph (Section 5).
*   *Current Text:* "...spatially resolved integral-field spectroscopy is required to resolve the aperture-morphology degeneracy \citep{penny2018,cheung2016,bundy2015}."
*   *Suggested Insertion:* "...spatially resolved integral-field spectroscopy is required to resolve the aperture-morphology degeneracy \citep{penny2018,cheung2016,bundy2015}. Furthermore, because central velocity dispersion and bulge mass act as primary structural predictors for quenching in local samples \citep{bluck2014, piotrowska2022}, the lack of structural controls means the optical BPT signature cannot currently be decoupled from the inside-out growth of the host bulge."

**For the Supplement (supplementary_denominator_atlas.tex - Maintenance Heating):**
*   *Location:* Section 4.2 (Maintenance-heating denominator).
*   *Current Text:* "...calibrated radio jet mechanical powers \citep[e.g.,][]{best2005,hardcastle2020}, halo-selected parent catalogues, and nondetection modelling."
*   *Suggested Insertion:* "...calibrated radio jet mechanical powers \citep[e.g.,][]{best2005,hardcastle2020}, halo-selected parent catalogues, and nondetection modelling. Optical broad BPT selection primarily traces radiative-mode accretion; thus, separating it from mechanically dominated jet-mode feedback requires strictly contemporaneous X-ray and radio measurements \citep{heckmanbest2014}."

**For the Supplement (supplementary_denominator_atlas.tex - High-excitation Baseline):**
*   *Location:* Section 4.3 (High-excitation broad optical BPT-selected baseline).
*   *Current Text:* "The follow-up ingredients are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers."
*   *Suggested Insertion:* "The follow-up ingredients are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers. Without IFU kinematics to decouple non-circular outflow components from host rotation \citep{harrison2018}, optical excitation alone cannot determine whether gas effectively exceeds the halo escape velocity."

**For the Supplement (supplementary_denominator_atlas.tex - Gas Depletion Baseline):**
*   *Location:* Section 4.7 (Low-sSFR optical denominator: baseline for future CO/HI).
*   *Suggested Insertion:* (Add to the missing follow-up list at the end of the section): "Direct CO(1-0) measurements from surveys like xCOLD GASS \citep{saintonge2017} are missing here and are required to test whether global molecular gas depletion timescales actively differ in these BPT-selected hosts."

---

### 4. No-Mock-Data Receipt and Safety Ledger

*   **Mock Data Status:** NO mock data, synthetic values, fake placeholder measurements, or toy arrays were generated.
*   **Verification:** All URLs/DOIs/Bibcodes provided correspond to highly cited, verifiable, published literature in astrophysics.
*   **Data Isolation:** All new citations are categorized strictly as interpretation caveats or motivations for future data. No new quantitative results were forced into the SDSS DR17 60,000-galaxy cache.
*   **Read-Only Safety:** No file edits, `git` commands, DB mutations, or deployments were executed. The filesystem and candidates remain strictly untouched.
*   **Sprint Compliance:** This packet meets the cycle 37 REAL-DATA-ONLY policy by sourcing valid external literature to define missing observables without fabricating integration data.


# command_result
exit_code=0
elapsed_s=47.4
timed_out=False
finished_utc=2026-07-09T18:57:15Z
