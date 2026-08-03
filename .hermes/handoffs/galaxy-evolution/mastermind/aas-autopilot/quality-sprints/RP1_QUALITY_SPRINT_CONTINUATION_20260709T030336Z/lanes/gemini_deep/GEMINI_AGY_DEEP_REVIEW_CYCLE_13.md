# gemini-agy-deep-cycle-13
Started UTC: 2026-07-09T04:22:46Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_13

### 1. Overview of the Deep Review
As a skeptical deep research reviewer, the candidate package has been analyzed solely based on the provided text of the local flagship paper and its supplementary atlas. The manuscript shows strong progress in positioning the results as selection-aware and association-only. However, there remain several critical risks where a reader could mistake statistical denominator adjustments or proxies for physical feedback, physical environments, or causal transitions.

---

### 2. Issue Log & Proposed Replacements

#### Issue 1: Conflating Optical Excitation with Physical Inflow/Outflow (Kinematics)
* **Severity**: Major
* **Location**: Flagship Abstract, Supplementary Section 3.3
* **Risky Sentence**: 
  > *"An accompanying supplement details the structural and multiwavelength observables required to convert these optical baselines into physical feedback tests."* (Flagship Abstract)
  > *"We isolate the outflow-kinematics denominator that resolved kinematics would need to test escape versus recycling."* (Supplement Section 3.3)
* **Critique**: The term "outflow-kinematics denominator" in Section 3.3 of the Supplement riskily suggests that the sample itself contains outflow signatures or kinematics, whereas it is merely an emission-line-selected sample of high-excitation optical AGN. Calling it "outflow-kinematics" instead of "high-excitation optical AGN" can mislead readers into thinking some kinematic selection has occurred.
* **Safer Replacement**:
  > *"An accompanying supplement details the structural and multiwavelength observables required to translate these statistical optical baselines into physical feedback or kinematic tests."*
  > *"We isolate the high-excitation optical AGN candidate sample to serve as a denominator for future resolved kinematic follow-up."*

#### Issue 2: Weak Caveat on 10th-Neighbor Index and Physical Environment
* **Severity**: Major
* **Location**: Supplement Section 3.1
* **Risky Sentence**:
  > *"Environment baseline: SDSS 10th-neighbor index for low-sSFR incidence"*
  > *"We establish an internal environmental baseline within the emission-line denominator that can later be joined to group catalogs and halo masses."*
* **Critique**: The 10th-neighbor index calculated *within* a selection-limited (four-line S/N $\geq 3$ optical emission line) capped cache is highly unphysical. It does not measure the actual spatial density of the Universe or the parent galaxy distribution; it only measures the density of other highly active emission-line galaxies within a capped subset. This is a severe proxy hazard.
* **Safer Replacement**:
  > *"Baseline of catalog-centric neighbor counts within the emission-line subset for future environmental follow-up"*
  > *"We establish a relative local spatial density baseline within this specific emission-line denominator, which should not be confused with physical local environmental density or halo density until matched to volume-complete catalogs."*

#### Issue 3: Mistaking Denominator Mass Concentration for a Physical Transition Mass
* **Severity**: Major
* **Location**: Supplement Section 3.5
* **Risky Sentence**:
  > *"We identify the mass bin where a future gas-inclusive study should look for an apparent incidence change."*
  > *"The first stellar-mass bin with low-sSFR fraction above 0.5 is $\log(M_\star/M_\odot) \in [11.0,12.5]$"*
* **Critique**: A reader may easily mistake the high incidence of low-sSFR or optical AGN in the $\log(M_\star/M_\odot) \in [11.0, 12.5]$ bin as a physical transition mass signature (e.g., halo quenching or AGN feedback turn-on). However, this concentration is heavily sculpted by the S/N $\geq 3$ selection function, which systematically drops the most quiescent passive galaxies at lower masses and restricts the sample to active/hybrid emitters.
* **Safer Replacement**:
  > *"We identify the stellar-mass ranges where selection effects concentrate hybrid emission-line galaxies, defining a baseline for future gas-inclusive matches."*
  > *"Within this selection-skewed emission-line denominator, the subset with low catalog-sSFR resides predominantly in the $\log(M_\star/M_\odot) \in [11.0,12.5]$ range; this is a selection consequence rather than a physical transition-mass boundary."*

#### Issue 4: Misleading Title/Heading for "Gas-depletion denominator"
* **Severity**: Minor
* **Location**: Supplement Section 3.7
* **Risky Sentence**:
  > *"Gas-depletion denominator: optical baseline for CO/HI follow-up"*
* **Critique**: The phrase "Gas-depletion denominator" implies that gas depletion is measured or used as a denominator. In reality, the denominator consists of massive, low-sSFR optical emission-line galaxies.
* **Safer Replacement**:
  > *"Low-sSFR optical denominator: baseline for future CO/HI gas measurements"*

---

### 3. Citation Role Integrity Analysis

The following citations are flagged for potential role confusion where they may be read as supporting the current SDSS-only methodology rather than acting strictly as motivation for missing future data:

1. **`\citep{piotrowska2022}` (Supplement Section 3.7 & Flagship Section 6)**:
   * *Current Role*: Cited alongside `xcoldgass2017` and `xgass2018` as a requirement for future gas-fraction/depletion-time tests.
   * *Reviewer Guidance*: Correctly positioned as motivation for future multi-parameter analyses. However, care must be taken that the reader does not assume the current matching scheme (stellar mass and redshift only) is validated by the multi-parameter random forest methodology of Piotrowska et al. (2022), which specifically highlights the dominant role of central velocity dispersion/black hole mass over stellar mass. 
   * *Remedy*: Add a note clarifying that the matching in this work is deliberately simpler than the physical regression parameters discussed in Piotrowska et al. (2022).

2. **`\citep{peng2010,wetzel2013,dekel2006}` (Supplement Section 3.1 & 3.5)**:
   * *Current Role*: Cited as motivation/context for environmental and transition-mass tests.
   * *Reviewer Guidance*: These are physical-model and volume-complete statistical papers. Using them in Section 3.1 and 3.5 could lead readers to think the uncorrected 10th-neighbor index in a capped cache behaves similarly to the corrected environments of Peng et al. (2010) or the halo models of Wetzel et al. (2013).
   * *Remedy*: Explicitly state: *"These works rely on volume-complete or halo-calibrated metrics, whereas our 10th-neighbor rank is strictly relative to the active emission-line cache."*

---

### 4. Missing-Data Checklist & Observable Flags

The manuscript lacks, and must explicitly list, the following observations to validate any physical feedback claims:

* **Radio Observables**: Missing resolved radio jet power, morphology (core vs. lobe), and radio duty-cycle calculations to test maintenance heating or environment coupling.
* **X-ray Observables**: Missing hot gas cooling rates, cavity energetics, or X-ray AGN bolometric corrections to establish heating-cooling balance.
* **CO/HI Observables**: Missing molecular gas masses ($M_{\text{H}_2}$ via CO or dust) and neutral gas masses ($M_{\text{HI}}$) to verify whether low sSFR corresponds to gas depletion or low star formation efficiency.
* **Resolved Outflows**: Missing spectroscopic kinematics showing high-velocity gas components (e.g., [O III] asymmetric blue wings) or spatial outflow extent to test gas ejection.
* **Halo/Group Data**: Missing group catalog memberships, satellite vs. central designations, and halo mass estimations to control for environmental quenching.
* **Morphology**: Missing bulge-to-disk decomposition, concentration indices, or Sersic profiles to control for the 3-arcsec fiber aperture mismatch.
* **Simulation Mocks**: Missing synthetic SDSS observations generated by applying the exact S/N and fiber-aperture selection cuts to simulated galaxy populations.

---

### 5. Ranked Integrator Actions

For the next iteration of the manuscript suite, the integrator should prioritize actions in this order:

1. **Aperture & Morphology Warning (Blocker)**: Elevate the 3-arcsec fiber aperture warning in the Flagship and Supplement. Clearly state that because BPT galaxies are typically more bulge-dominated than star-forming controls, the fiber-centered offset of -1.309 dex is likely an upper limit inflated by aperture mismatch rather than global quenching.
2. **Rename Supplementary Section Headings (Major)**: Update titles from "Outflow-kinematics denominator" to "High-excitation optical AGN baseline", and "Environment baseline" to "Relative neighbor-count baseline" to prevent proxy confusion.
3. **Selection-Cut Bias Disclaimer in Mass Trends (Major)**: Add an explicit warning in Supplement Section 3.5 that the $\log(M_\star/M_\odot) \in [11.0,12.5]$ concentration is a selection artifact of the four-line S/N requirement.
4. **Citation Context Clarifications (Minor)**: Append disclaimers to environmental and physical feedback citations (`peng2010`, `piotrowska2022`) to highlight the statistical limitations of the current matched-control comparison.

---

### 6. Safety Ledger

* **Read-only review**: Yes, no files edited or created.
* **Git operations**: None.
* **External APIs / Cloud / Billing**: None.
* **Public updates / replacement / publishing**: None. All actions remained strictly local.


# command_result
exit_code=0
elapsed_s=16.9
timed_out=False
finished_utc=2026-07-09T04:23:03Z
