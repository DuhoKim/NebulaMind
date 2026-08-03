# gemini-agy-deep-cycle-17
Started UTC: 2026-07-09T04:49:11Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_17

# Astronomy Manuscript Quality Sprint Deep Review Report
**Cycle**: 17  
**Candidate Root**: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_17_package`  
**Review Type**: Skeptical Deep Research Review (Read-only)

---

## 1. Identified Issues & Proposed Wording Replacements

### Issue 1: Lack of Morphology/Aperture Matching and Aperture Bias
* **Severity**: **Blocker**
* **Risk**: The manuscript compares broad-BPT targets to star-forming controls matched only in stellar mass and redshift. Since broad-BPT hosts (which include bulge-dominated and passive/retired galaxies) are structurally different from disk-dominated star-forming galaxies, a 3-arcsec fiber preferentially samples the central bulge (low sSFR region) in targets and the disk (high sSFR region) in controls. This aperture/morphology mismatch could entirely simulate the observed $\Delta\log\text{sSFR}$ offset of $-1.309$ dex, rather than any physical feedback.
* **Risky Sentence (Abstract)**: 
  > *"Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, and the sample is not matched in morphology or aperture fraction."*
* **Safer Replacement**: 
  > *"Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only. Because the sample is not matched in morphology or aperture fraction, the 3-arcsec fiber preferentially samples the quiescent bulges of BPT hosts compared to the active disks of star-forming controls; this aperture bias and structural mismatch may account for the entirety of the observed catalog-sSFR offset."*

---

### Issue 2: Fixed-Size pilot-query Cap Survey-Plate/Sky-Coverage Bias
* **Severity**: **Major**
* **Risk**: The 60,000-galaxy pilot cap selected sequentially by `specObjID` is not a random sample. Since `specObjID` correlates with Survey Plate and MJD (Modified Julian Date), this cap introduces strong spatial sky-coverage and instrumental biases. The manuscript mentions this but needs to explicitly warn that standard statistical uncertainty estimators (like bootstrap confidence intervals) assume independent, identically distributed draws and are therefore artificially narrow here.
* **Risky Sentence (Section 2)**: 
  > *"The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex."*
* **Safer Replacement**: 
  > *"The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex. Due to spatial sky-coverage and plate biases introduced by the sequential `specObjID` selection cap, standard bootstrap intervals (here $[-1.334, -1.283]$ dex) underestimate the true systematic survey-level uncertainty."*

---

### Issue 3: Mistaking Denominator/Proxy Notes for Physical Quenching
* **Severity**: **Major**
* **Risk**: A reader might interpret the "Maintenance-heating denominator" or the "Tracer-threshold census" as physical measurements of feedback efficiency or mass-dependent transition physics.
* **Risky Sentence (Supplement Section 3.5)**: 
  > *"The first stellar-mass bin with low-sSFR fraction above 0.5 is $\log(M_\star/M_\odot) \in [11.0,12.5]$, and the optical AGN fraction peaks in the 11.0--12.5 bin at 0.520. This is an optical distribution diagnostic..."*
* **Safer Replacement**: 
  > *"The apparent peaking of the low-sSFR fraction above 0.5 at $\log(M_\star/M_\odot) \in [11.0,12.5]$ in the emission-line denominator is a selection artifact. Truly passive, massive galaxies are excluded by the four-line S/N $\geq 3$ threshold, leaving an unrepresentative sample. This peak is a sample-selection diagnostic and must not be interpreted as a physical feedback transition mass."*

---

### Issue 4: Citation Role Ambiguity for Future-Data Motivation
* **Severity**: **Minor**
* **Risk**: Highlighting citations in lists at the end of sections without reiterating that they do not support the current data can lead readers to assume the cited works validate the current SDSS-only methodology.
* **Risky Sentence (Supplement Section 1)**: 
  > *"Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables..."*
* **Safer Replacement**: 
  > *"Citations to SDSS/BPT/catalog papers provide methodological framework for the optical sample definition. Conversely, citations to radio, X-ray, CO/HI, outflow, and simulation papers are included exclusively as future-data motivation; they do not validate or cross-correlate with the optical observations presented in this work."*

---

## 2. Missing-Data Claims & Observables Tracker

The following claims/sections in the local package require missing physical observables to support their inferences:

| Document / Section | Claimed/Implied Physical Result | Required Missing Observables / Mocks |
| :--- | :--- | :--- |
| **Flagship / Section 4 & 5** | Quenching / sSFR suppression | Global morphology catalogs, spatially resolved star formation maps (to correct for 3" fiber aperture bias). |
| **Supplement / Section 3.1** | Environmental quenching | Group catalogs, central/satellite labels, halo masses, spectroscopic fiber-collision correction at the $55$-arcsec scale. |
| **Supplement / Section 3.2** | Maintenance heating | X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogs. |
| **Supplement / Section 3.3** | Outflow escape & recycling | Resolved outflow velocities, deep halo potentials, multiphase gas mass measurements (ionized, neutral, molecular). |
| **Supplement / Section 3.6** | Multiphase gas census | Combined HI/CO gas-mass measurements, common aperture-matched tracer models. |
| **Supplement / Section 3.8** | Simulation validation | Mock catalogs processed through the exact SDSS S/N selection function and fiber aperture limits. |

---

## 3. Ranked Integrator Actions

For the next iteration of the manuscript (to be executed by the autopilot or editors), the following prose actions are ranked in order of priority:

1. **[Blocker Action]** Revise the Flagship Abstract and Discussion to elevate the morphologic/aperture mismatch from a caveat to a primary alternative explanation for the $-1.3$ dex offset.
2. **[Major Action]** Add explicit warnings regarding the sequential `specObjID` query cap in both the Flagship and Supplement, explaining the survey-plate and sky-coverage biases.
3. **[Major Action]** Rename Section 3.5 of the Supplement from *"Stellar-mass selection diagnostic"* to *"Stellar-mass Selection Artifact"* to prevent readers from mistaking the distribution peak for a physical feedback boundary.
4. **[Minor Action]** Audit the bibliography to ensure that physical feedback models/observations (e.g., *Saintonge et al. 2017*, *Cicone et al. 2014*) are explicitly labeled in-text as "future follow-up targets" rather than method references.

---

## 4. Safety Ledger

* **Live system updates**: None.
* **File writes/edits**: None (Read-only review mode).
* **Database/API calls**: None.
* **Public/git publishing**: None.
* **Local sandbox compliance**: Fully adhered to. All analysis is strictly restricted to the provided local package snapshot paths.


# command_result
exit_code=0
elapsed_s=16.7
timed_out=False
finished_utc=2026-07-09T04:49:27Z
