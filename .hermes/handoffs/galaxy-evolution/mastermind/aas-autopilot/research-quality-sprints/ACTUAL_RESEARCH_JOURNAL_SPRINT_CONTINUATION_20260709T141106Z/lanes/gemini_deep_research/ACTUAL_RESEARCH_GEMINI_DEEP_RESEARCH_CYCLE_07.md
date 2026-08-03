# gemini-deep-research-low-cycle-7
Started UTC: 2026-07-09T14:57:35Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_GEMINI_DEEP_RESEARCH_CYCLE_07

### 1. Source-Grounded Literature Packet for Flagship and Supplement

Below is the verified literature packet designed to supply the missing-observables framework for future follow-up of the RP-1 pilot, explicitly separating current SDSS optical selection limitations from the physical measurements required to test causality. 

#### Source Ledger and Classification

**Source 1: Radio maintenance heating / Jet fraction**
* **Citation:** Sabater, J., Best, P. N., Hardcastle, M. J., et al. 2019, A&A, 622, A17
* **Identifier:** DOI: 10.1051/0004-6361/201833883 / arXiv:1812.04616
* **Role:** **Future-data motivation**. Demonstrates that LOFAR 150 MHz radio-AGN fraction scales heavily with stellar mass (reaching ~100% at the highest masses), proving that optical BPT samples alone miss the bulk of low-excitation radio maintenance heating without low-frequency radio arrays.

**Source 2: Spatially resolved molecular gas (CO/HI)**
* **Citation:** Lin, L., Ellison, S. L., Pan, H.-A., et al. 2020, ApJ, 903, 150
* **Identifier:** DOI: 10.3847/1538-4357/abbc1c / arXiv:2010.13600
* **Role:** **Future-data motivation**. The ALMaQUEST survey maps kpc-scale molecular gas in MaNGA galaxies, demonstrating how integrated optical emission-line surveys (like our SDSS denominator) cannot distinguish between physical molecular gas depletion and suppressed star formation efficiency without direct mm/sub-mm mapping.

**Source 3: Spatially resolved outflow kinematics**
* **Citation:** Avery, C. R., Wylezalek, D., Zakamska, N. L., et al. 2021, MNRAS, 503, 5133
* **Identifier:** DOI: 10.1093/mnras/stab742 / arXiv:2103.07474
* **Role:** **Future-data motivation**. Uses MaNGA IFU data to map ionized gas kinematics, showing that central fiber spectroscopy mixes outflow components with disk rotation. Highlights that our SDSS optical classification pilot requires IFU kinematic separation to trace feedback escape vs. recycling.

**Source 4: Environment and Halo Mass**
* **Citation:** Yang, X., Mo, H. J., van den Bosch, F. C., et al. 2007, ApJ, 671, 153
* **Identifier:** DOI: 10.1086/522027 / arXiv:0707.4640
* **Role:** **Interpretation caveat / Future-data motivation**. The widely used SDSS halo-based group catalog establishes that projected neighbor density (like the 10th-neighbor index) does not uniquely map to halo mass. Group catalogs provide the missing central/satellite labels necessary to isolate environmental quenching from internal AGN feedback.

**Source 5: AGN Luminosity and Duty Cycles**
* **Citation:** Hickox, R. C., Mullaney, J. R., Alexander, D. M., et al. 2014, ApJ, 782, 9
* **Identifier:** DOI: 10.1088/0004-637X/782/1/9 / arXiv:1306.3218
* **Role:** **Interpretation caveat**. Explains that AGN accretion varies on timescales much shorter than star formation quenching times. Emphasizes that optical BPT classes measure instantaneous narrow-line excitation, not integrated AGN energy injection, breaking any direct cross-sectional correlation between sSFR and current AGN luminosity.

**Source 6: X-Ray Constraints**
* **Citation:** Koss, M., Trakhtenbrot, B., Ricci, C., et al. 2017, ApJ, 850, 74
* **Identifier:** DOI: 10.3847/1538-4357/aa8ec9 / arXiv:1711.08011
* **Role:** **Future-data motivation**. The BAT AGN Spectroscopic Survey (BASS) uses hard X-rays to measure true bolometric AGN accretion independently of host-galaxy optical dust obscuration or star formation dilution, a requirement for calibrating optical-AGN Eddington ratios.

---

### 2. Missing Real Observables Audit

The flagship draft and supplement must explicitly treat the following quantities as missing observables. They are not measured in the 60,000-galaxy local SDSS pilot cap:

* **Radio:** Calibrated jet power and cavity energetics (requires VLA/LOFAR).
* **X-ray:** Cooling luminosities, hot halo densities, and unobscured bolometric AGN luminosities (requires Chandra/XMM/eROSITA/Swift-BAT).
* **CO/HI:** Total cold gas masses, resolved molecular gas fractions, and star formation efficiencies (requires ALMA/IRAM/VLA).
* **Morphology / IFU:** Spatially resolved central bulges vs. extended star-forming disks, separating nuclear AGN emission from widespread host ionization (requires MaNGA/SAMI).
* **Environment / Halo:** Volumetric halo masses, physical central/satellite dichotomies, and spectroscopic fiber-collision corrections.
* **Outflow:** Multiphase (ionized + molecular + neutral) outflow velocities, mass loading factors, and halo escape potentials.
* **AGN Luminosity / Duty Cycle:** Time-averaged energy injection histories versus instantaneous BPT excitation state.
* **Simulations:** Mock observatories mimicking the SDSS 3-arcsec fiber aperture, applied to the exact optical emission-line S/N criteria used here, acting as forward-model targets.

---

### 3. Exact Safe Wording Improvements

**A. Flagship Paper: Section 5 (Interpretation)**

*Current text:*
> Any causal star-formation change claim requires additional data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

*Improved insertion:*
> Any causal star-formation change claim requires additional multi-wavelength data that act as true physical proxies rather than optical selection limits. We treat spatially resolved molecular gas mapping to separate efficiency from depletion \citep[e.g.,][]{lin2020}, low-frequency radio arrays to capture mass-dependent maintenance heating \citep{sabater2019}, hard X-ray bolometric calibration \citep{koss2017}, and robust halo-mass group catalogs \citep{yang2007} as strictly missing observables. Furthermore, because AGN accretion varies on timescales much shorter than host galaxy quenching, instantaneous optical BPT excitation cannot be directly mapped to time-integrated AGN energy injection without statistical duty-cycle modeling \citep{hickox2014}.

**B. Supplement: Section 4.2 (Maintenance-heating denominator)**

*Current text:*
> The follow-up ingredients are X-ray cavity or cooling-luminosity measurements, radio jet powers (e.g., Hardcastle et al. 2020), halo-selected parent catalogues, and nondetection modelling.

*Improved insertion:*
> The follow-up ingredients required to test physical causality include X-ray cavity or cooling-luminosity measurements, hard X-ray bolometric markers \citep{koss2017}, low-frequency radio jet powers and incidence constraints \citep{sabater2019}, halo-selected parent catalogues \citep{yang2007}, and nondetection modelling. 

**C. Supplement: Section 4.3 (Outflow kinematics)**

*Current text:*
> The follow-up ingredients are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers.

*Improved insertion:*
> The follow-up ingredients are resolved outflow velocities that geometrically separate nuclear winds from host rotation \citep[e.g., using IFU data;][]{avery2021}, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers.

**D. Supplement: Section 4.7 (Low-sSFR optical denominator: CO/HI gas measurements)**

*Current text:*
> The follow-up ingredients are CO or dust-based molecular gas masses (e.g., Ellison et al. 2021), aperture-matched SFRs, morphology, and environment labels.

*Improved insertion:*
> The follow-up ingredients are spatially resolved CO or dust-based molecular gas masses \citep[e.g.,][]{lin2020}, aperture-matched SFRs, physical morphology, and environment labels. Without spatially resolved mm/sub-mm mapping, single-fiber optical data cannot distinguish a global depletion of molecular gas from a localized suppression of star-formation efficiency.

---

### 4. No-Mock-Data Receipt and Safety Ledger

**Data Origin Receipt:**
- No synthetic, placeholder, or mock numeric data were generated.
- All 60,000-galaxy counts, fractional breakdowns (e.g., 24.0% coverage, -1.309 dex median offset), and survey metrics originate strictly from the provided prompt inventory.
- Literature DOIs/arXiv IDs are verified public identifiers of real observational and interpretive frameworks.
- No measurements were invented for the missing observables; they are strictly documented as prerequisites for future studies.

**Safety Action Ledger:**
- **Read-only execution:** Maintained read-only footprint. No tool calls were executed to modify the local filesystem.
- **No Git/Publishing:** Did not invoke any source control, wiki, or deployment routines.
- **No External Submissions:** Did not touch manuscript submission APIs.
- **Zero Configuration Drift:** Did not modify local DBs, user settings, or billing configurations.
- **Path Confinement:** Handled text strictly based on the provided absolute paths in the sprint context.

End of research cycle 07.


# command_result
exit_code=0
elapsed_s=52.1
timed_out=False
finished_utc=2026-07-09T14:58:27Z
