# gemini-deep-research-low-cycle-14
Started UTC: 2026-07-09T15:56:42Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_GEMINI_DEEP_RESEARCH_CYCLE_14

Here is the source-grounded literature and research packet designed to support and motivate the required missing observables for the RP-1 flagship and supplement, strictly following the read-only and no-mock-data rules. 

### 1. Source-Grounded Literature Packet & Role Classification

Below is a curated set of verified literature sources mapping to the missing physical observables needed to elevate the current association-only pilot to a physical feedback test. 

**Source 1:**
- **Identifier:** DOI: 10.1146/annurev-astro-081913-035722 | ADS: 2014ARA&A..52..589H | arXiv:1403.4620 
- **Reference:** Heckman, T. M., & Best, P. N. (2014). The Coevolution of Galaxies and Supermassive Black Holes: Insights from Surveys of the Contemporary Universe. *Annual Review of Astronomy and Astrophysics*, 52, 589-639.
- **Role Classification:** **Future-data motivation** (Radio/X-ray, AGN Luminosity/Duty Cycle).
- **Justification:** Essential baseline for interpreting optical BPT AGN vs. radio-mode/maintenance heating. Defines why optical emission lines (radiative mode) do not directly trace the mechanical jet power (jet mode) required for maintenance heating.

**Source 2:**
- **Identifier:** DOI: 10.3847/1538-4365/aa97e0 | ADS: 2017ApJS..233...22S | arXiv:1710.04227
- **Reference:** Saintonge, A., Catinella, B., Tacconi, L. J., et al. (2017). xCOLD GASS: The Complete IRAM 30 m Legacy Survey of Molecular Gas in Massive Galaxies. *The Astrophysical Journal Supplement Series*, 233(1), 22.
- **Role Classification:** **Future-data motivation** (CO/HI, gas fractions).
- **Justification:** Provides the gold-standard molecular gas (CO) depletion reference in the local universe. Required to move from optical catalog sSFR offsets to actual molecular gas depletion times and gas fraction tests.

**Source 3:**
- **Identifier:** DOI: 10.1086/522027 | ADS: 2007ApJ...671.153Y | arXiv:0707.4640
- **Reference:** Yang, X., Mo, H. J., van den Bosch, F. C., et al. (2007). Galaxy Groups in the SDSS DR4. I. The Catalog and Basic Properties. *The Astrophysical Journal*, 671(1), 153-170.
- **Role Classification:** **Actual method support / Future-data motivation** (Environment/Halo).
- **Justification:** Provides the standard framework for moving from projected neighbor-counts (the 10th-neighbor index in this pilot) to physical halo masses and central/satellite categorizations.

**Source 4:**
- **Identifier:** DOI: 10.1093/mnras/stu504 | ADS: 2014MNRAS.441..599B | arXiv:1403.5269
- **Reference:** Bluck, A. F. L., Mendel, J. T., Ellison, S. L., et al. (2014). Bulge mass is king: the dominant role of the bulge in determining the fraction of passive galaxies in the Sloan Digital Sky Survey. *Monthly Notices of the Royal Astronomical Society*, 441(1), 599-629.
- **Role Classification:** **Interpretation caveat** (Morphology).
- **Justification:** Demonstrates that bulge mass/morphology correlates strongly with quenching. Since the current RP-1 pilot does not match on morphology, this reference establishes why the observed sSFR offset is highly degenerate with the bulge-to-disk ratio in central fibers.

**Source 5:**
- **Identifier:** DOI: 10.1093/mnras/stu515 | ADS: 2014MNRAS.441.3306H | arXiv:1403.3086
- **Reference:** Harrison, C. M., Alexander, D. M., Mullaney, J. R., & Swinbank, A. M. (2014). Kiloparsec-scale outflows are prevalent among luminous AGN: outflows and feedback in the context of the overall AGN population. *Monthly Notices of the Royal Astronomical Society*, 441(4), 3306-3321.
- **Role Classification:** **Future-data motivation** (Outflow/Kinematics).
- **Justification:** Shows that IFU kinematics are required to measure resolved outflow velocities, differentiating between localized gas disturbance and true escape/recycling.

---

### 2. Missing Real Observables Identification
The pilot is currently restricted to SDSS catalog parameters. The following observables remain explicitly **missing** from the integration and are identified as published comparison data/motivations only. They are not measured results in the NebulaMind sprint:
*   **Radio / X-ray:** Jet mechanical power, 1.4 GHz core/lobe luminosities, X-ray cavity energetics, and hot halo gas densities.
*   **CO / HI:** Molecular (CO) and neutral (HI) gas masses, yielding actual $M_{\rm gas}$ and depletion times ($\tau_{\rm dep}$) instead of optical proxy associations.
*   **Morphology:** Bulge-to-total ($B/T$) mass ratios, S\'ersic indices, and central velocity dispersions ($\sigma$) for structural matching.
*   **Environment / Halo:** Group catalog membership, physical halo mass ($M_h$), and central vs. satellite designations (replacing the uncalibrated 10th-neighbor rank).
*   **Outflow:** Spatially resolved velocity maps, broad-line kinematic components ($W_{80}$, $v_{05}$), and multiphase mass outflow rates.
*   **AGN Luminosity / Duty Cycle:** Bolometric luminosities ($L_{\rm bol}$), Eddington ratios ($\lambda_{\rm Edd}$), and hard X-ray constraints.
*   **Simulations:** Mock observable lightcones from forward-modeled suites (e.g., EAGLE, IllustrisTNG, SIMBA) passed through the exact SDSS optical fiber selection function.

---

### 3. Exact Safe Wording Improvements & Citation Insertions

**For Flagship `rp1_flagship_polished.tex`:**
*Location: Section 4, "Morphology and aperture caveat."*
*Improvement:* Strengthen the morphological degeneracy warning by citing the established structural quenching literature directly.
*Suggested Text Insertion:*
> "Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology or aperture fraction, the observed sSFR offset is highly degenerate with the known mass--morphology relation. Specifically, central fiber measurements are heavily biased by the transition from disk-dominated to bulge-dominated systems, where bulge prominence acts as a dominant predictor of passive fractions \citep[e.g.,][]{bluck2014}. Single-fiber measurements cannot separate galaxy-wide changes from purely central gradients..."

*Location: Section 5, "Interpretation"*
*Improvement:* Clarify the missing AGN luminosity dimension.
*Suggested Text Insertion:*
> "...The central-kiloparsec aperture restriction is one reason this remains a local association rather than a galaxy-wide star-formation measurement. Furthermore, optical excitation alone does not trace the bolometric accretion rate or mechanical jet power \citep{heckmanbest2014}. Any causal star-formation change claim requires additional real data, including morphology and aperture controls, Seyfert/LINER separation, calibrated AGN luminosity or Eddington proxy, gas mass, physical environment, and time-domain/duty-cycle modelling."

**For Supplement `supplementary_denominator_atlas.tex`:**
*Location: Section 4.1, "Relative neighbor-count baseline"*
*Improvement:* Clearly distinguish the 10th-neighbor index from physical group catalogs.
*Suggested Text Insertion:*
> "...The follow-up ingredients are group catalogues \citep[e.g.,][]{yang2007}, robust central/satellite labels, halo masses, a spectroscopic fiber-collision correction at the 55-arcsec scale, morphology, and multi-redshift selection functions. Within this selection-biased emission-line sample, the 10th-neighbor statistic is only a relative local rank, not a physical volume density and not a substitute for central/satellite labels or a volume-complete halo-density measurement."

*Location: Section 4.7, "Low-sSFR optical denominator: baseline for future CO/HI gas measurements"*
*Improvement:* Ground the required follow-up in established cold-gas legacy surveys.
*Suggested Text Insertion:*
> "...SDSS optical data alone cannot distinguish bulk molecular-gas depletion from localized reductions in star-formation efficiency or measure total cold-gas mass \citep{tacconi2018}; this note identifies the CO/HI follow-up denominator and optical baseline required for spatially resolved gas tests. The follow-up ingredients are CO or dust-based molecular gas masses \citep[e.g.,][]{xcoldgass2017}, aperture-matched SFRs, morphology, and environment labels..."

*(Note: Add the corresponding BibTeX entries for `yang2007`, `xcoldgass2017`, `heckmanbest2014`, and `bluck2014` to the manuscript's `.bib` file / bibliography environment if not already present.)*

---

### 4. No-Mock-Data Receipt and Safety Ledger

**Receipt of Observational Integrity:**
*   **Zero Mock Data Generated:** No synthetic numbers, fake sample sizes, or interpolated statistical outputs were created. 
*   **Zero Fictitious Identifiers:** All provided literature references contain real DOIs, arXiv IDs, and ADS Bibcodes representing published, peer-reviewed astrophysical literature.
*   **Boundary Enforcement:** Explicitly maintained the boundary between the currently measured SDSS association pilot (capped at 60,000 specObjIDs) and the missing physical follow-up metrics. Literature sources are designated as future-data motivations only.

**Safety Ledger:**
*   **File Status:** READ-ONLY mode confirmed. No edits were made to `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/.../rp1_flagship_polished.tex` or the supplementary atlas.
*   **Execution Status:** No Git operations (commit/push/rebase) executed.
*   **Environment Status:** No deployment, database mutations, API writes, or cron scheduling actions performed.
*   **External Comm Status:** No external submission or public-facing deployment initiated. All analysis remains isolated in the local research sprint context.


# command_result
exit_code=0
elapsed_s=41.8
timed_out=False
finished_utc=2026-07-09T15:57:24Z
