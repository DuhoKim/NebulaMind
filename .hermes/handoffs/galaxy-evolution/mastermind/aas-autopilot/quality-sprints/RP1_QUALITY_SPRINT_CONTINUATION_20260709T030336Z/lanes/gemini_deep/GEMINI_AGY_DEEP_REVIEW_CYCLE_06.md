# gemini-agy-deep-cycle-6
Started UTC: 2026-07-09T03:37:07Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_06

## 1. Deep Research Review Summary
This review evaluates the text of the polished flagship manuscript (`rp1_flagship_polished.tex`) and the supplementary denominator/proxy atlas (`supplementary_denominator_atlas.tex`). The focus is on ensuring strict distinction between denominator/optical proxy statistics and physical causal results, correcting citation-role alignment, identifying missing observables, and proposing safer prose.

---

## 2. Issue Register and Prose Revisions

### Issue 1: Confounding of BPT Line-Ratio Classification with Accretion-Driven Physical AGN
* **Severity**: Major
* **Risky Sentence (Flagship - Abstract)**: 
  > "Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only..."
* **Risky Sentence (Flagship - Section 3)**:
  > "Each broad optical BPT galaxy is matched to the nearest star-forming control..."
* **Problem**: Referring to the matched targets simply as "BPT-selected galaxies" or "broad optical BPT AGN" in a matched comparison can lead a reader to assume physical active galactic nuclei properties (such as accretion rates or active feedback) are being matched, rather than optical line-ratio coordinates.
* **Proposed Wording**:
  > "Galaxies classified within the broad optical BPT line-ratio boundaries are matched to star-forming controls..."

### Issue 2: Environmental Quenching vs. Denominator Fractional Baseline
* **Severity**: Major
* **Risky Sentence (Supplement - Section 3.1)**:
  > "Within this selection-biased emission-line denominator, the relative 10th-neighbor index covaries with the catalog low-sSFR fraction..."
* **Problem**: The title of the subsection ("Environment baseline: SDSS density proxy for low-sSFR incidence") and the text use "low-sSFR emission-line fraction" which can easily be misread as a physical environmental quenching rate, rather than a selection-biased cohort fraction.
* **Proposed Wording**:
  > "Within this selection-biased emission-line denominator, the relative 10th-neighbor index covaries with the fraction of galaxies falling below the catalog specific star-formation rate threshold; this index is an internal relative rank within the emission-line cohort rather than a physical environmental density or halo-centric metric."

### Issue 3: Transition Mass vs. Selection Bias Peak
* **Severity**: Major
* **Risky Sentence (Supplement - Section 3.5)**:
  > "The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520. This is an optical distribution diagnostic..."
* **Problem**: A reader looking at Figure 5 (or the text) could interpret the peak as a physical transition mass where AGN feedback becomes dominant, rather than a severe selection-function bias caused by requiring $S/N \geq 3$ in all four BPT lines (which systematically excludes massive, passive galaxies).
* **Proposed Wording**:
  > "The fraction of BPT-classified emission-line galaxies peaks at 0.520 in the $11.0 \leq \log(M_\star/M_\odot) \leq 12.5$ bin. This peak is an observational artifact of our emission-line signal-to-noise requirement, which preferentially excludes quiescent massive systems, and must not be interpreted as a physical transition mass for individual galaxy evolution."

---

## 3. Citation Role Audit

The following citations are used in both manuscripts to motivate future observations. We must ensure they are not misconstrued as supporting the current SDSS-only methodology:

* **Multiphase and Outflow Kinematics**: \cite{veilleux2005, cicone2014, carniani2017, fiore2017}
  * *Audit*: These must strictly be cited to illustrate the necessity of future resolved gas kinematics. They cannot be used to support or validate the optical BPT or fiber-aperture specific star formation rates used in the present papers.
* **Radio-Mode and X-Ray Cavity Heating**: \cite{best2005, dekel2006, fabian2012, heckmanbest2014, mcnamara2007, lamassa2013}
  * *Audit*: These motivate the missing energy-injection metrics. They do not validate the optical BPT class as a proxy for mechanical feedback coupling.
* **Cosmological Simulations**: \cite{simba2019, tng2019, eagle2015}
  * *Audit*: These are cited as targets for future forward-modeling mocks. They should not be cited as confirming the physical validity of the catalog-sSFR matching offsets.

---

## 4. Missing Observables Checklist

For each supplementary topic, the following table lists the physical data missing from the current SDSS DR17 optical cache that must be integrated to draw physical conclusions:

| Topic | Missing Observables Required for Physical Interpretation |
| :--- | :--- |
| **3.1 Environment** | Group/cluster memberships, satellite/central classifications, virial halo masses, spectroscopic fiber collision corrections. |
| **3.2 Maintenance Heating** | High-resolution radio maps (jet morphology, age), X-ray cavity/cooling-flow measurements. |
| **3.3 Outflows** | Multiphase velocity profiles (CO, HI, ionized gas lines), spatial maps of outflow extension. |
| **3.4 Jets** | Jet energy coupling models, host gas density profiles. |
| **3.5 Transition Mass** | Total gas mass fractions, deep imaging for morphology, unbiased parent volume normalization. |
| **3.6 Tracer Census** | Integrated atomic and molecular gas measurements (ALMA, IRAM, Arecibo). |
| **3.7 Gas Depletion** | Measured CO-to-molecular-gas conversion factors ($\alpha_{\rm CO}$), dust-extinction-free star formation rates. |
| **3.8 Simulation Vector** | Mock catalogs run through the exact SDSS spectroscopic and emission-line selection pipelines. |

---

## 5. Ranked Integrator Actions

1. **[Blocker] Disclaim Simulation Mock Comparisons**: Revise Section 3.8 to state clearly that the target vector is a mock-observation baseline only and cannot be directly compared to raw simulation outputs.
2. **[Major] Relabel Y-Axes in Supplement Figures**: Ensure all plots in the supplement depicting "AGN fraction" or "Low-sSFR fraction" (Figures 1 through 8) explicitly label the axis as "Fraction within the BPT $S/N \geq 3$ Denominator" to prevent readers from confusing these with absolute volume-limited fractions.
3. **[Minor] Expand LINER/Retired Stellar Population Warnings**: Add a paragraph in Section 1 of the flagship paper emphasizing that retired stellar populations dominate the low-ionization BPT region, especially in high-mass bulges.

---

## 6. Safety Ledger
* **Public/Live updates**: None.
* **Database writes**: None.
* **API or Git interactions**: None.
* **Review type**: Read-only review based strictly on the provided local TeX texts.


# command_result
exit_code=0
elapsed_s=16.8
timed_out=False
finished_utc=2026-07-09T03:37:24Z
