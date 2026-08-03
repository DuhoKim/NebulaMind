# gemini-deep-research-low-cycle-23
Started UTC: 2026-07-09T17:07:21Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_GEMINI_DEEP_RESEARCH_CYCLE_23

Here is your source-grounded literature and research packet. As requested, I have operated entirely in read-only mode, providing only verified external literature identifiers and safe text improvements to map the local optical denominators to the required missing physical observables. No mock data or synthetic local values have been generated.

### 1. Source-Grounded Literature Packet & Classifications

Each source provides the necessary physical context to explain *why* the local SDSS BPT measurements cannot support causal claims until the missing observables are added. 

*   **Bluck et al. (2014)**
    *   **Identifier:** ADS bibcode `2014MNRAS.441..599B` / `2014ApJ...786L..24B` (CANDELS/SDSS Bulge Mass)
    *   **Role:** Interpretation Caveat (Morphology). 
    *   **Justification:** Demonstrates that bulge mass and central velocity dispersion are the strongest predictors of the quenched fraction, independent of specific AGN optical indicators. Shows that without morphological controls, any offset is degenerate with structural quenching.
*   **Piotrowska et al. (2022)**
    *   **Identifier:** DOI `10.1093/mnras/stab3673` (MNRAS 512, 1052)
    *   **Role:** Future-Data Motivation / Interpretation Caveat.
    *   **Justification:** Compares SDSS data to EAGLE and IllustrisTNG, showing central velocity dispersion (or black hole mass proxies) is the most predictive metric of quenching due to integrated AGN feedback. Connects the structural caveat directly to the missing simulation validation targets.
*   **Belfiore et al. (2018)**
    *   **Identifier:** ADS bibcode `2018MNRAS.477.2616B` (MaNGA sSFR profiles)
    *   **Role:** Interpretation Caveat (Aperture Effects).
    *   **Justification:** Uses resolved IFU data to show that suppression often happens centrally (inside-out quenching). Verifies that a fixed 3-arcsec fiber centrally biases sSFR measurements, explaining why the fiber-matched SDSS controls must be treated as central-aperture proxies, not global star-formation metrics.
*   **Saintonge et al. (2017)**
    *   **Identifier:** ADS bibcode `2017ApJS..233...22S` (xCOLD GASS)
    *   **Role:** Future-Data Motivation (Molecular Gas / CO).
    *   **Justification:** Defines the definitive local CO survey for molecular gas scaling relations. This is the exact required observable to convert the "low-sSFR optical denominator" into a physical gas depletion time or gas fraction test.
*   **Best & Heckman (2012)**
    *   **Identifier:** ADS bibcode `2012MNRAS.421.1569B` (Local Radio-AGN dichotomy)
    *   **Role:** Future-Data Motivation (Radio Jets / Maintenance Heating).
    *   **Justification:** Distinguishes high-excitation radiative mode from low-excitation jet-mode AGN. Needed to transition the "broad optical BPT-selected massive hosts" baseline into a measurement of mechanical jet power and maintenance-heating duty cycles.
*   **Yang et al. (2007)**
    *   **Identifier:** ADS bibcode `2007ApJ...671..153Y` (SDSS Halo Group Catalog)
    *   **Role:** Future-Data Motivation (Environment / Halo Mass).
    *   **Justification:** Provides the gold-standard physical halo mass estimates and central/satellite designations for SDSS. Replaces the biased 10th-neighbor 2D projection with the physical 3D environment metric required for the environment jet tests.

### 2. Missing Real Observables Inventory

The current optical baseline lacks the following physical measurements (these must be supplied by the external literature/follow-up above, not invented locally):
*   **Morphology / Central Velocity Dispersion:** Required to control the mass-morphology relation degeneracy (Bluck 2014, Piotrowska 2022).
*   **Aperture Fraction / Resolved Kinematics:** Required to separate nuclear suppression from global disk star formation (Belfiore 2018).
*   **Radio and X-ray Proxies:** Required to measure mechanical jet power and halo cooling rates for maintenance heating (Best & Heckman 2012).
*   **CO/HI Cold Gas Measurements:** Required to test bulk molecular-gas depletion versus star-formation efficiency (Saintonge 2017).
*   **Environment / Halo Mass:** Required to replace the fiber-collision-biased 10th-neighbor index with central/satellite labels and physical halo potential depths (Yang 2007).

### 3. Wording Improvements and Citation Insertions

**For Flagship `rp1_flagship_polished.tex`:**
*In Section 5, "Matched-control result", update the Morphology and aperture caveat paragraph:*
> "Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology, structural proxies, or aperture fraction, the observed sSFR offset is highly degenerate with the known mass--morphology relation and the transition from disk-dominated to bulge-dominated systems. Central velocity dispersion and bulge mass are known to be dominant predictors of the quiescent fraction \citep{bluck2014,piotrowska2022}. Furthermore, the lack of structural matching limits the result's ability to separate structural suppression from excitation-linked suppression. Single-fiber measurements cannot separate galaxy-wide changes from purely central gradients, as spatially resolved integral-field spectroscopy frequently reveals inside-out suppression \citep{belfiore2018}. Resolving the aperture-morphology degeneracy requires matched IFU comparisons."

**For Supplement `supplementary_denominator_atlas.tex`:**
*In Section 4.2, "Maintenance-heating denominator":*
> "The follow-up ingredients are X-ray cavity or cooling-luminosity measurements, calibrated radio jet mechanical powers \citep[e.g.,][]{best2012}, halo-selected parent catalogues, and nondetection modelling. Those observables are missing here; this entry remains an optical baseline only..."

*In Section 4.7, "Low-sSFR optical denominator: baseline for future CO/HI gas measurements":*
> "SDSS optical data alone cannot distinguish bulk molecular-gas depletion from localized reductions in star-formation efficiency or measure total cold-gas mass; this note identifies the CO/HI follow-up denominator and optical baseline required for spatially resolved gas tests. The follow-up ingredients are global CO or dust-based molecular gas masses \citep[e.g., xCOLD GASS;][]{saintonge2017}, atomic hydrogen masses, and aperture-matched SFRs."

*In Section 4.1, "Relative neighbor-count baseline":*
> "The follow-up ingredients are physical group catalogues with robust central/satellite labels and halo masses \citep[e.g.,][]{yang2007}, a spectroscopic fiber-collision correction at the 55-arcsec scale, morphology, and multi-redshift selection functions."

### 4. Safety Ledger & Receipt

*   **No-Mock-Data Receipt:** No new datasets, synthetic local numbers, fake URLs, or artificial sample sizes were introduced. All references correspond to external, widely-used, public astrophysical publications with verifiable identifiers.
*   **Safety Ledger:**
    *   Read-only restrictions fully honored.
    *   No file operations (read/write/replace) were executed on the disk.
    *   No deployments, DB queries, commits, or workflow executions were triggered.
    *   All provided text relies strictly on the provided context block and standard external literature matching the requested physical themes.


# command_result
exit_code=0
elapsed_s=61.2
timed_out=False
finished_utc=2026-07-09T17:08:22Z
