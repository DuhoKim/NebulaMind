# gemini-deep-research-low-cycle-26
Started UTC: 2026-07-09T17:27:01Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_GEMINI_DEEP_RESEARCH_CYCLE_26

### 1. Source-Grounded Literature Packet

Below is the verified, read-only literature packet to motivate the missing observables and support interpretation caveats in the RP-1 flagship and supplement. All sources include checkable identifiers.

**Source 1: Hardcastle & Croston (2020)**
*   **Title:** Radio galaxies and feedback from AGN jets
*   **Journal:** New Astronomy Reviews, Volume 88, 101539
*   **Public Identifier:** DOI: 10.1016/j.newar.2020.101539 / arXiv:2003.06137
*   **Classification:** Future-data motivation
*   **Application:** Required to motivate the radio and X-ray follow-up parameters (jet mechanical power, cavity energetics, hot-gas density) in the "Maintenance-heating denominator" and "Radio-jet environment baseline" sections. 

**Source 2: Heckman & Best (2014)**
*   **Title:** The Coevolution of Galaxies and Supermassive Black Holes: Insights from Surveys of the Contemporary Universe
*   **Journal:** Annual Review of Astronomy and Astrophysics, Vol. 52, pp. 589-660
*   **Public Identifier:** DOI: 10.1146/annurev-astro-081913-035722 / ADS: 2014ARA&A..52..589H
*   **Classification:** Interpretation caveat / Future-data motivation
*   **Application:** Establishes the distinction between radiative (quasar) and kinetic (radio) modes. Critical caveat for the flagship: BPT excitation captures optical (radiative-like) properties, but maintenance heating requires radio/kinetic evidence.

**Source 3: Saintonge et al. (2017)**
*   **Title:** xCOLD GASS: The Complete IRAM 30 m Legacy Survey of Molecular Gas for Galaxy Evolution Studies
*   **Journal:** The Astrophysical Journal Supplement Series, 233, 22
*   **Public Identifier:** DOI: 10.3847/1538-4365/aa97e0 / arXiv:1710.04227
*   **Classification:** Future-data motivation
*   **Application:** Motivates the "Low-sSFR optical denominator: baseline for future CO/HI gas measurements" by establishing the actual molecular gas masses and depletion times required to separate starvation from efficiency suppression.

**Source 4: Bundy et al. (2015)**
*   **Title:** Overview of the SDSS-IV MaNGA Survey: Mapping nearby Galaxies at Apache Point Observatory
*   **Journal:** The Astrophysical Journal, 798, 7
*   **Public Identifier:** DOI: 10.1088/0004-637X/798/1/7 / ADS: 2015ApJ...798....7B
*   **Classification:** Interpretation caveat / Future-data motivation
*   **Application:** Addresses the "Morphology and aperture caveat." Explains how central 3-arcsec fiber measurements systematically misrepresent global sSFR, requiring resolved IFU mapping to overcome aperture biases.

**Source 5: Harrison et al. (2018)**
*   **Title:** AGN outflows and feedback twenty years on
*   **Journal:** Nature Astronomy, Vol. 2, pp. 198-205
*   **Public Identifier:** DOI: 10.1038/s41550-018-0403-6 / arXiv:1802.10306
*   **Classification:** Interpretation caveat
*   **Application:** Highlights that observing an optical excitation or an outflow does not guarantee that gas is escaping the halo; supports the "High-excitation broad optical BPT-selected baseline" missing observables (resolved velocities, halo potentials).

---

### 2. Missing Real Observables & Role in Manuscript

As enforced by the REAL-DATA-ONLY policy, these physical properties are **not measured in the current RP-1 pilot**. They are missing observables that must be explicitly acknowledged as required future work for any causal or physical-mechanism tests.

*   **Radio / X-ray:** Missing jet mechanical powers, large-scale morphology, X-ray cavities, and hot-halo cooling rates. Needed for maintenance heating. (Motivation: Hardcastle & Croston 2020).
*   **CO/HI (Molecular/Neutral Gas):** Missing total cold-gas mass and depletion timescales. Needed to differentiate between gas-fraction depletion and suppressed star-formation efficiency. (Motivation: Saintonge et al. 2017).
*   **Morphology / Aperture:** Missing structural proxies (e.g., bulge-to-total ratio) and IFU/resolved spatial kinematics. Currently, the 3-arcsec fiber introduces central-to-global mismatches. (Motivation: Bundy et al. 2015).
*   **Environment / Halo:** Missing robust central/satellite catalogs, dark matter halo mass matching, and corrections for SDSS 55-arcsec fiber collisions. The 10th-neighbor index is only a local proxy. 
*   **Outflow / Kinematics:** Missing resolved escape velocities, multiphase gas accounting, and CGM recycling tracers. (Motivation: Harrison et al. 2018).
*   **AGN Luminosity / Duty Cycle:** Missing bolometric proxies and Eddington ratios. Optical BPT classification is an excitation state, not an absolute power measurement. (Motivation: Heckman & Best 2014).
*   **Simulations:** Missing forward-modeled comparisons passed through the exact SDSS mock selection function.

---

### 3. Safe Wording Improvements and Citation Insertions

**Target: Flagship TeX (`rp1_flagship_polished.tex`) - Section: Morphology and aperture caveat**
*   *Current phrasing:* "...single-fiber measurements cannot separate galaxy-wide changes from purely central gradients, so spatially resolved integral-field spectroscopy is required to resolve the aperture-morphology degeneracy \citep{penny2018,cheung2016}."
*   *Improved insertion:* "...single-fiber measurements cannot separate galaxy-wide changes from purely central gradients, so spatially resolved integral-field spectroscopy is required to resolve the aperture-morphology degeneracy \citep{penny2018,cheung2016,bundy2015}. In particular, relying on central 3-arcsec fibers can misclassify extended disk star-formation, requiring mapping via surveys like MaNGA to derive total SFRs."

**Target: Supplement TeX (`supplementary_denominator_atlas.tex`) - Section: Maintenance-heating denominator**
*   *Current phrasing:* "The follow-up ingredients are X-ray cavity or cooling-luminosity measurements \citep{fabian2012}, calibrated radio jet mechanical powers \citep[e.g.,][]{best2005,hardcastle2020}, halo-selected parent catalogues, and nondetection modelling."
*   *Improved insertion:* "The follow-up ingredients are X-ray cavity or cooling-luminosity measurements \citep{fabian2012}, calibrated radio jet mechanical powers and large-scale jet mapping \citep[e.g.,][]{heckman2014,hardcastle2020}, halo-selected parent catalogues, and nondetection modelling. Without directly resolving kinetic jet power and hot halo environments, the local BPT classification remains purely a radiative/optical parameterization."

**Target: Supplement TeX (`supplementary_denominator_atlas.tex`) - Section: Low-sSFR optical denominator: baseline for future CO/HI gas measurements**
*   *Current phrasing:* "SDSS optical data alone cannot distinguish bulk molecular-gas depletion from localized reductions in star-formation efficiency or measure total cold-gas mass \citep{tacconi2018}..."
*   *Improved insertion:* "SDSS optical data alone cannot distinguish bulk molecular-gas depletion from localized reductions in star-formation efficiency or measure total cold-gas mass \citep{tacconi2018,saintonge2017}. Definitive tests of quenching modes require direct observations of $t_{\text{dep}}$ and $M_{\text{gas}}$ from submillimeter and radio surveys."

---

### 4. No-Mock-Data Receipt and Safety Ledger

*   **Mock Data Status:** NO mock data, placeholder metrics, or synthetic numeric figures were created. All reported sample sizes (60,000 computational cap, 8,146 matched pairs) strictly reflect the existing text.
*   **Literature Integrity:** All recommended citations are verified existing papers with public DOIs/arXiv IDs. They are positioned purely to identify missing future observables, not to falsely validate the present optical measurements.
*   **File System Operations:** Zero files were modified, created, or deleted. 
*   **External Commits:** No commits, pushes, API calls, or external submissions were executed. Operated in strict read-only analytical mode.
*   **Result Status:** The manuscript remains a local SDSS optical baseline and matched-control association pilot. Physical feedback, gas mass, and kinematic parameters remain explicitly listed as "missing real observables."


# command_result
exit_code=0
elapsed_s=51.2
timed_out=False
finished_utc=2026-07-09T17:27:52Z
