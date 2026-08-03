# gemini-deep-research-low-cycle-18
Started UTC: 2026-07-09T16:31:08Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_GEMINI_DEEP_RESEARCH_CYCLE_18

### 1. Source-Grounded Literature and Source Packet

Here is the source-grounded literature packet for improving the RP-1 flagship and supplement, focused on aperture constraints, morphological degeneracies, and multiwavelength follow-up motivation.

**Source 1:**
- **Citation:** Kewley, L. J., Jansen, R. A., & Geller, M. J. (2005), "Aperture Effects on Star Formation Rate Estimates and AGN Activity", *PASP*, 117, 227.
- **Identifier:** DOI: 10.1086/428303 / arXiv:astro-ph/0501100
- **Classified Role:** *Interpretation caveat*. Defines the physical limits of 3-arcsec fiber spectroscopy at low redshift, strongly cautioning against extrapolating central-fiber catalog sSFR to global galaxy star formation without spatially resolved controls.

**Source 2:**
- **Citation:** Belfiore, F., et al. (2016), "SDSS IV MaNGA - spatially resolved diagnostic diagrams: a proof that many galaxies are LIERs", *MNRAS*, 461, 3111.
- **Identifier:** DOI: 10.1093/mnras/stw1234 / arXiv:1602.05532
- **Classified Role:** *Interpretation caveat*. Proves that many broad optical BPT-selected LINER-like targets in local SDSS catalogs are driven by spatially extended retired stellar populations (hot post-AGB stars), not central black-hole accretion, heavily caveatting the single-fiber BPT selection.

**Source 3:**
- **Citation:** Bluck, A. F. L., et al. (2014), "Bulge mass is king: the dominant role of the bulge in determining the fraction of passive galaxies in the Sloan Digital Sky Survey", *MNRAS*, 441, 599.
- **Identifier:** DOI: 10.1093/mnras/stu504 / arXiv:1403.5269
- **Classified Role:** *Interpretation caveat*. Reinforces the mass-morphology degeneracy, establishing that bulge mass or central density strongly correlates with quenched status. Without morphological matching, the BPT-associated sSFR offset is degenerate with this structural quenching track.

**Source 4:**
- **Citation:** Heckman, T. M., & Best, P. N. (2014), "The Coevolution of Galaxies and Supermassive Black Holes: Insights from Surveys of the Contemporary Universe", *ARA&A*, 52, 589.
- **Identifier:** DOI: 10.1146/annurev-astro-081913-035710 / arXiv:1403.4620
- **Classified Role:** *Future-data motivation*. Summarizes the duty-cycle phase mapping, emphasizing that optical excitation only probes "radiative mode" AGN, and multiwavelength radio/X-ray follow-up is necessary to constrain the maintenance mode and temporal feedback cycles.

**Source 5:**
- **Citation:** Saintonge, A., et al. (2017), "xCOLD GASS: The Complete IRAM 30 m Legacy Survey of Molecular Gas for Galaxy Evolution Studies", *ApJS*, 233, 22.
- **Identifier:** DOI: 10.3847/1538-4365/aa97e0 / arXiv:1710.04227
- **Classified Role:** *Future-data motivation*. Serves as the benchmark for bulk molecular gas ($M_{\rm H_2}$) depletion measurements, essential for testing if the low sSFR in BPT-selected hosts results from gas removal or suppressed star-formation efficiency.

---

### 2. Missing Real Observables

The following physical properties are entirely missing from the current 60,000-galaxy pilot cache and are identified strictly as published comparison data/motivations for future tests. They are not measured results in the present SDSS optical denominator:

- **Morphology / Central Velocity Dispersion:** Required to break the degeneracy between AGN feedback and standard structural/bulge quenching.
- **Radio / X-ray:** Required to map maintenance-heating jet powers, hot gas halos, and cavity energetics.
- **CO / HI (Multiphase Gas):** Required to measure actual gas fractions, depletion timescales, and distinguish cold gas removal from suppressed efficiency.
- **Resolved Outflow Kinematics:** Required to separate escaped gas from recycling fountain flows, replacing the simple optical excitation proxies.
- **Environment / Halo Mass:** Required to place satellites and centrals into their proper context and account for environmental stripping versus internal feedback.
- **AGN Luminosity / Duty Cycle:** Required to measure actual bolometric accretion power rather than relying on binary BPT emission-line ratios.
- **Simulations (Forward Models):** Require applying the exact SDSS optical S/N$\geq3$ pipeline logic to synthetic lightcones; currently entirely absent from the analysis cache.

---

### 3. Exact Safe Wording Improvements and Citation Insertion

**A. Flagship Improvement (Morphology Caveat)**
*Target Location:* Section 4, "Morphology and aperture caveat."
*Current:* "Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology or aperture fraction, the observed sSFR offset is highly degenerate with the known mass--morphology relation..."
*Suggested Replacement:*
"Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology or aperture fraction \citep{kewley2005}, the observed sSFR offset is highly degenerate with the known mass--morphology relation \citep{bluck2014}. Without spatially resolved data, it remains undetermined whether the offset reflects galaxy-wide quenching or extended retired stellar populations mimicking LINER-like emission \citep{belfiore2016}."

**B. Supplement Improvement (Maintenance Heating)**
*Target Location:* Section 4.2, "Maintenance-heating denominator"
*Current:* "The follow-up ingredients are X-ray cavity or cooling-luminosity measurements \citep{fabian2012}, radio jet powers \citep[e.g.,][]{best2005,hardcastle2020}, halo-selected parent catalogues, and nondetection modelling."
*Suggested Replacement:*
"The follow-up ingredients are X-ray cavity or cooling-luminosity measurements \citep{fabian2012}, radio jet powers, robust empirical constraints on AGN duty cycles \citep{heckmanbest2014}, halo-selected parent catalogues, and nondetection modelling. These properties are completely unconstrained by the present SDSS optical sample and require future cross-matches to real radio and X-ray observations."

**C. Supplement Improvement (Gas Depletion)**
*Target Location:* Section 4.7, "Low-sSFR optical denominator"
*Current:* "The follow-up ingredients are CO or dust-based molecular gas masses \citep[e.g., xCOLD GASS;][]{xcoldgass2017}, atomic hydrogen masses \citep[e.g., xGASS;]["
*Suggested Completion / Replacement:*
"The follow-up ingredients are CO-based molecular gas masses \citep[e.g., xCOLD GASS;][]{saintonge2017}, atomic hydrogen masses, spatially matched aperture SFRs, and independent environmental labels. Cold-gas data are not measured here; these literature benchmarks only serve to define the multiwavelength follow-up requirements."

---

### 4. No-Mock-Data Receipt and Safety Ledger

**Data Safety Checklist:**
- [x] Evaluated purely on the reported SDSS DR17 real-data denominators (60,000-row cached counts).
- [x] No synthetic numerical values, simulated sample sizes, or fake physical observables were inserted.
- [x] Missing observables were explicitly isolated as "future-data motivation" and not claimed as measurements in the flagship or supplement.
- [x] All suggested citations (Kewley 2005, Belfiore 2016, Bluck 2014, Heckman & Best 2014, Saintonge 2017) are real, highly cited literature benchmarks equipped with DOIs and correctly mapped to their roles as caveats and motivations.

**Operational Safety Checklist:**
- [x] Read-only operation executed.
- [x] Zero file modifications were made to the candidate packages or integration roots.
- [x] No `git`, public page edits, database updates, or deployment commands were invoked.
- [x] No `mock`, `placeholder`, or `synthetic` strings were integrated into any proposed TeX output.


# command_result
exit_code=0
elapsed_s=38.0
timed_out=False
finished_utc=2026-07-09T16:31:46Z
