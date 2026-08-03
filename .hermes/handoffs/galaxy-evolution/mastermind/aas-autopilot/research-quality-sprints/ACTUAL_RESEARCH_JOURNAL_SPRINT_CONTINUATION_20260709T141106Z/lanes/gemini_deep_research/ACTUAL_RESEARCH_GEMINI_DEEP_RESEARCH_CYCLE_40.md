# gemini-deep-research-low-cycle-40
Started UTC: 2026-07-09T19:19:10Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_GEMINI_DEEP_RESEARCH_CYCLE_40

### 1. Source-Grounded Literature Packet

Below is the verified literature packet to improve the RP-1 flagship and supplement, focusing on interpretation caveats regarding BPT classification, aperture/morphology degeneracy, and multi-wavelength completeness.

*   **Belfiore, F., et al. (2016), MNRAS 461, 3111. arXiv:1602.05944.** 
    *   **Identifier:** arXiv:1602.05944 / ADS: 2016MNRAS.461.3111B
    *   **Role:** Interpretation caveat.
    *   **Context:** Proves via SDSS-IV MaNGA spatially resolved IFU data that many galaxies classified globally or centrally as LINERs in standard SDSS single-fiber spectroscopy are extended "LIERs" (Low-Ionization Emission-line Regions). Their emission is driven by evolved stellar populations (e.g., post-AGB stars) rather than accretion onto a central supermassive black hole.

*   **Stasińska, G., et al. (2008), MNRAS 391, L29. arXiv:0809.1327.**
    *   **Identifier:** arXiv:0809.1327 / ADS: 2008MNRAS.391L..29S
    *   **Role:** Interpretation caveat.
    *   **Context:** Demonstrates that retired galaxies can produce optical emission line ratios that mimic LINERs on the BPT diagram via Hot Low-Mass Evolved Stars (HOLMES). It establishes that BPT classification alone cannot confirm active accretion without controlling for equivalent widths and stellar population age.

*   **Heckman, T. M., & Best, P. N. (2014), ARA&A 52, 589. arXiv:1403.4620.**
    *   **Identifier:** arXiv:1403.4620 / ADS: 2014ARA&A..52..589H
    *   **Role:** Future-data motivation.
    *   **Context:** Defines the phenomenological split between radiative-mode (often optical BPT-selected) and jet-mode (often radio-selected, low optical excitation) AGN. Emphasizes that optical broad BPT selection primarily traces radiative modes and fails to construct a complete census of mechanical feedback or maintenance-heating duty cycles without X-ray and radio integrations.

*   **Agostino, C. J., & Salim, S. (2019), ApJ 876, 12. arXiv:1904.05359.**
    *   **Identifier:** arXiv:1904.05359 / ADS: 2019ApJ...876...12A
    *   **Role:** Interpretation caveat / Future-data motivation.
    *   **Context:** Evaluates the completeness of optical BPT classification against X-ray-selected AGN in the local universe. Finds significant mismatches, especially in quiescent galaxies where BPT diagnostics may only identify a fraction (~50-70%) of true X-ray-selected AGNs due to host galaxy dilution and optically dull/XBONG phenomena.

---

### 2. Missing Real Observables

The current SDSS DR17 backbone establishes an optical denominator, but causal tests of feedback, maintenance heating, and gas depletion require the following missing observables. *Do not write them as measured results unless real data are integrated.*

*   **Morphology / Aperture Fraction:** MaNGA or SAMI IFU data to resolve central AGN from extended LIER/post-AGB emission, and `fracDeV` or $R_{90}/R_{50}$ from complete photometric joins to control for bulge prominence.
*   **Radio / X-ray:** Required for testing maintenance-heating hypotheses. X-ray cavities, cooling luminosities, and calibrated radio jet mechanical powers. Optical emission strictly misses optically dull X-ray AGN and jet-mode maintenance heating events.
*   **CO / HI Gas Masses:** Needed to distinguish between suppressed star-formation efficiency (long depletion times) and genuine molecular gas depletion (low gas fractions). Optical sSFR acts as a tracer, not a phase-separated gas measurement.
*   **Environment / Halo Mass:** Central/satellite labels from group catalogs (e.g., Yang or Tinker) and formal halo mass estimates. The current 10th-neighbor proxy is projection-biased and severely impacted by the SDSS 55-arcsec fiber collision limit in dense clusters.
*   **Resolved Outflow Kinematics:** Required to separate non-circular gas motions from host rotation to measure true outflow velocity, multiphase escape fractions, and mass-loading factors.
*   **Simulation Comparisons:** Required as forward-modeled benchmark target vectors (e.g., IllustrisTNG, EAGLE mock observations passed through the identical SDSS S/N$\ge3$ fiber selection function).

---

### 3. Exact Safe Wording Improvements & Citation Insertion Suggestions

**For the RP-1 Flagship TeX:**
*   *In Section 1 (Question and claim boundary), after the sentence:* "...as well as low-ionization nuclear emission-line region (LINER)-like ionization, can contaminate broad low-ionization classes and mimic active-nucleus signatures \citep{cidfernandes2011,stasinska2008,stasinska2015}."
*   *Suggested Insertion:* "Integral-field studies explicitly demonstrate that much of this LINER-like emission is extended on kiloparsec scales and ionized by evolved stellar populations (LIERs) rather than a central AGN \citep{belfiore2016}."

*   *In Section 5 (Matched-control result), under "Morphology and aperture caveat", after:* "...single-fiber measurements cannot separate galaxy-wide changes from purely central gradients, so spatially resolved integral-field spectroscopy is required to resolve the aperture-morphology degeneracy \citep{penny2018,cheung2016,bundy2015}."
*   *Suggested Insertion:* "Furthermore, relying exclusively on optical BPT selection systematically misses optically dull or X-ray-bright but optically quiescent AGN \citep{agostino2019}, meaning our baseline does not represent a complete multi-wavelength AGN census."

**For the Supplement TeX:**
*   *In Section 4.2 (Maintenance-heating denominator), after:* "Optical broad BPT selection primarily traces the radiative-mode denominator, so it cannot isolate the mechanically dominated jet-mode population without contemporaneous X-ray and radio measurements \citep{heckmanbest2014}."
*   *Suggested Insertion:* "Because many massive, low-sSFR hosts harbour genuine X-ray or radio active nuclei that fall inside the optical BPT star-forming or composite regions due to dilution \citep{agostino2019}, this optical fraction remains a strict lower bound on the true multi-wavelength duty cycle."

---

### 4. No-Mock-Data Receipt and Safety Ledger

**Data Verification Ledger:**
*   **Mock data generated:** None.
*   **Synthetic values invented:** None.
*   **Citations verified:** Yes (arXiv:1602.05944, arXiv:0809.1327, arXiv:1403.4620, arXiv:1904.05359).
*   **Missing observables acknowledged:** Yes, explicitly listed as unmeasured requirements.

**Safety Action Ledger:**
*   **Files edited:** 0 (Read-only policy enforced).
*   **Commands run:** 0 mutating commands (Only safe `search_web` used).
*   **Git / External operations:** 0.
*   **Database / API interactions:** 0.

The requested deep-research synthesis is complete and strictly adheres to the read-only and no-mock-data policies.


# command_result
exit_code=0
elapsed_s=54.9
timed_out=False
finished_utc=2026-07-09T19:20:05Z
