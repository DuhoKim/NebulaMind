# gemini-deep-research-low-cycle-33
Started UTC: 2026-07-09T18:22:40Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_GEMINI_DEEP_RESEARCH_CYCLE_33

### 1. Source-Grounded Literature Packet & Source Roles

Below is the verified literature packet to improve the interpretation and follow-up motivation in the RP-1 flagship and supplementary atlas. All sources provide checkable public identifiers.

**Source 1: Piotrowska et al. (2022)**
*   **Identifier:** DOI: 10.1093/mnras/stab3673 | arXiv:2112.07673 | MNRAS 512, 1052
*   **Role:** Interpretation caveat / Future-data motivation.
*   **Context:** Demonstrates that central velocity dispersion (a proxy for black hole mass and integrated AGN feedback history) is the primary predictive driver for quenching in central galaxies, rather than instantaneous AGN accretion states or stellar mass alone. 
*   **Usage:** Insert to reinforce the morphology/aperture caveat and mass-bin interpretation.

**Source 2: Saintonge et al. (2017) (xCOLD GASS)**
*   **Identifier:** DOI: 10.3847/1538-4365/aa97e0 | arXiv:1710.02157 | ApJS 233, 22
*   **Role:** Future-data motivation.
*   **Context:** The IRAM-30m legacy survey establishing molecular gas fractions and depletion times across the local mass-star-formation plane.
*   **Usage:** Insert as the canonical comparison sample for future CO/HI gas measurements in the supplement.

**Source 3: Ellison et al. (2021)**
*   **Identifier:** DOI: 10.1093/mnras/staa3794 | arXiv:2012.06642 | MNRAS 501, 4777
*   **Role:** Interpretation caveat.
*   **Context:** Uses MaNGA IFU data to show that spatially resolved star formation in AGN hosts can have distinct central vs. extended radial profiles, highlighting the limitation of single-fiber measurements.
*   **Usage:** Insert to bolster the aperture-fraction and central-to-global mismatch discussion in the flagship.

**Source 4: Harrison (2017)**
*   **Identifier:** DOI: 10.1038/s41550-017-0165 | arXiv:1703.06889 | Nature Astronomy 1, 0165
*   **Role:** Method support / Interpretation caveat.
*   **Context:** A review of AGN outflows highlighting that current optical emission-line classifications do not intrinsically measure multiphase outflow mass rates or direct global quenching.
*   **Usage:** Insert to support the strict boundary that the current SDSS BPT pilot is an association, not a measurement of escape/recycling feedback.

**Source 5: Heckman & Best (2014)**
*   **Identifier:** DOI: 10.1146/annurev-astro-081913-035722 | arXiv:1403.4620 | ARA&A 52, 589
*   **Role:** Interpretation caveat / Future-data motivation.
*   **Context:** Delineates the fundamental difference between radiative-mode (optical high-excitation, BPT-selected) and jet-mode (radio-selected, mechanical maintenance) AGN, and their respective host populations.
*   **Usage:** Insert into the maintenance-heating denominator section to clarify that broad BPT selection misses the primarily passive radio-jet population required for mechanical feedback tests.

---

### 2. Missing Real Observables explicitly identified

To strictly adhere to the real-data-only policy, the following physical properties are confirmed as **missing** from the current SDSS optical 60,000-galaxy cache and must not be reported as measured results:
*   **Morphology & Structural Proxies:** Central velocity dispersion ($\sigma$), concentration index ($R_{90}/R_{50}$), \texttt{fracDeV}, and bulge-to-total ratios.
*   **Multiphase Gas Masses:** Molecular gas (CO) and neutral gas (HI) limits.
*   **AGN Power & Duty Cycle:** Bolometric luminosities ($L_{\text{bol}}$), Eddington ratios, X-ray cavity energetics, and radio jet mechanical powers.
*   **Resolved Kinematics & Environment:** Spatially resolved IFU kinematics (MaNGA/SAMI outflow mapping), true halo masses, and calibrated central/satellite labels.
*   **Simulations:** Cosmological hydrodynamical comparisons (e.g., IllustrisTNG, EAGLE) passed through an SDSS-matched mock aperture.

---

### 3. Exact Safe Wording Improvements and Citation Insertions

**Target:** Flagship TeX (`rp1_flagship_polished.tex`)
*   **Location:** Section 5, Matched-control result, "Morphology and aperture caveat" paragraph.
*   **Current Text:** "...central velocity dispersion effects \citep{schawinski2010,bluck2014,belfiore2016}."
*   **Suggested Improvement:** "...central velocity dispersion effects \citep{schawinski2010,bluck2014,belfiore2016}, which recent machine-learning validations suggest is the primary predictive observable for the integrated history of AGN feedback \citep{piotrowska2022}."
*   **Current Text:** "...this is a known source of central-to-global mismatch \citep[e.g.,][]{harrison2017,ellison2021}."
*   **Suggested Improvement:** "...this is a known source of central-to-global mismatch \citep[e.g.,][]{ellison2021}, highlighting that current single-fiber excitation measurements do not directly probe galaxy-wide multiphase outflow coupling \citep{harrison2017}."

**Target:** Supplement TeX (`supplementary_denominator_atlas.tex`)
*   **Location:** Section 4.2, Maintenance-heating denominator paragraph.
*   **Current Text:** "The follow-up ingredients are X-ray cavity or cooling-luminosity measurements \citep{fabian2012}, calibrated radio jet mechanical powers \citep[e.g.,][]{best2005,hardcastle2020}, halo-selected parent catalogues, and nondetection modelling."
*   **Suggested Improvement:** "The follow-up ingredients are X-ray cavity or cooling-luminosity measurements \citep{fabian2012}, calibrated radio jet mechanical powers \citep[e.g.,][]{best2005,hardcastle2020}, and halo-selected parent catalogues. Because optical broad-line BPT selection primarily traces radiative-mode accretion rather than the mechanically dominated jet-mode population \citep{heckman2014}, radio and X-ray nondetection modeling is strictly required before inferring mechanical duty cycles."
*   **Location:** Section 4.7 (implied from abstract summary), Gas depletion optical denominator.
*   **Suggested Insertion:** When listing missing CO/HI gas data, explicitly append "\citep[e.g., the xCOLD GASS survey;][]{saintonge2017}" to formalize the missing real-data molecular baseline. 

---

### 4. No-Mock-Data Receipt and Safety Ledger

**Read-Only Safety Ledger:**
- [x] Evaluated candidate manuscripts from local `.hermes` handoff paths.
- [x] Executed internet queries solely to retrieve valid, peer-reviewed DOIs.
- [x] Generated zero synthetic dataset claims or mock sample sizes.
- [x] Prevented the invention of fake $p$-values, effect sizes, or SDSS catalog outputs.
- [x] Performed zero local file edits, system commands, Git operations, or API credential requests.
- [x] Ensured every physical concept recommended for insertion explicitly bounds the claim as "missing observable" or "association-only".


# command_result
exit_code=0
elapsed_s=39.2
timed_out=False
finished_utc=2026-07-09T18:23:19Z
