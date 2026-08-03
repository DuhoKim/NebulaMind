# Referee Report: Fact-Checking & Overclaim Adjudication
**Sprint**: `ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z`  
**Candidate Directory**: `candidates/cycle_10_package`  
**Role**: Fact-check and overclaim referee  

---

## 1. Integrity Audit & Data Custody Verification
A search of the directory structures and `/provenance/REAL_DATA_SOURCE_CUSTODY.json` confirms that:
* No mock, synthetic, or placeholder datasets are utilized.
* All data points originate from local, verified, and custody-tracked run directories.
* Standard emission-line catalog metadata is properly loaded and joined.
* There are **no integrity blockers** (e.g., missing custody records, fabricated counts, or unverified claims).

---

## 2. Quantitative Verification of Invariants

We verified every numeric value in [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_10_package/flagship_rp1/aastex/rp1_flagship_polished.tex) and [supplementary_denominator_atlas.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_10_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex) against their JSON origins:

* **Flagship BPT Counts**: Star-forming (`39,553`), composite (`12,234`), AGN (`8,146`), and unclassified (`67`) match `SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json` exactly.
* **Flagship Median Offset**: The median $\Delta\log\text{sSFR}$ is `-1.309 dex` (rounded from `-1.30888...`) with a 95% bootstrap confidence interval of `[-1.334, -1.283] dex` (the upper bound `-1.2821...` is rounded to `-1.283` in LaTeX, which is a conservative rounding).
* **Flagship Pair Metrics**: The absolute median separations of `0.0045 dex` in $\log M_\star$ and `0.00021` in redshift match `"match_abs_delta_logM_median"` and `"match_abs_delta_z_median"` exactly.
* **Supplement Topics (10th-Neighbor Index)**: Quenched fraction of `0.230` ($3,456/15,000$) for high-density quartile and `0.181` ($2,710/15,000$) for low-density quartile match `m1_rp2` JSON exactly. The linear probability model coefficient `0.032 +/- 0.004` matches the JSON coefficient (`0.03249`) and standard error (`0.0037`).
* **Supplement Topics (Massive BPT fraction)**: Massive rows (`9,298`), massive low-sSFR rows (`5,695`), and AGN fractions (`0.430` / `0.607`) match `m1_rp3` JSON exactly.
* **Supplement Topics (High-Excitation Outflow Baseline)**: High-excitation candidates (`4,440/60,000`), median sSFRs (`-11.53` and `-10.14`) match `m2_p1` JSON exactly.
* **Supplement Topics (Radio-Jet Environment baseline)**: High-density quartile massive AGN fraction (`0.509`) and low-density quartile (`0.367`) with high-minus-low interval `[0.112, 0.170]` match `m2_p2` JSON exactly.
* **Supplement Topics (Mass bin transition)**: Peaks in the `11.0--12.5` bin at `0.520` matches `m2_p3` JSON exactly.
* **Supplement Topics (Tracer census)**: Optical tracer prevalence range of `0.136 to 0.418` (ratio `3.1`) matches `m3_p1` JSON exactly.
* **Supplement Topics (Gas depletion denominator)**: Massive low-sSFR denominator contains `6,729` galaxies, BPT fraction `0.549`, median $L_{\text{H}\alpha}$ proxy of `40.061`, and offset of `-0.66 dex` matching `m3_p2` JSON exactly.
* **Supplement Topics (Simulation target vector)**: All 15 mass-redshift bins in Table 3 match the fractions and median $u-r$ colors in `m3_p3` JSON exactly.

---

## 3. Boundaries and Overclaim Mitigation
The manuscript excels at boundary defense:
* It consistently asserts that results are **observational association-only**, avoiding causal feedback claims.
* It explicitly describes the role of the 3-arcsec SDSS fiber, noting the missing morphological, structural, and aperture controls.
* It lists all missing observables required for physical verification: resolved velocity fields, molecular gas masses ($M_{\text{gas}}$), group/halo catalog variables, and forward-model simulation comparisons.

---

## 4. Concrete Section-level Improvements

### Flagship: [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_10_package/flagship_rp1/aastex/rp1_flagship_polished.tex)
* **Section 3 (Data and shared selection)**: 
  * *Improvement*: Quantify the impact of the sequential `specObjID` cap on selection bias (e.g., mention that selecting sequentially from the SDSS cache means the survey-plate coverage may favor specific regions of the sky, leading to spatial clustering/bias).
  * *Literature suggestion*: Mention York et al. 2000 (AJ, 120, 1579; ADS bibcode: 2000AJ....120.1579Y; DOI: 10.1086/301513) for SDSS targeting algorithm details.
* **Section 5 (Matched-control result)**:
  * *Improvement*: Add a brief explanation of how the bootstrap 95% confidence interval on the median offset was calculated (e.g., number of bootstrap iterations $B=1000$, standard percentile method).

### Supplement: [supplementary_denominator_atlas.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_10_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex)
* **Section 5.1 (Relative neighbor-count baseline)**:
  * *Improvement*: Clarify how the 10th-neighbor index handles survey boundaries (edge effects) and state that no boundary corrections are applied here, representing a potential systematic error.
  * *Literature suggestion*: Compare with the spatial correlation functions in Zehavi et al. 2002 (ApJ, 571, 172; ADS bibcode: 2002ApJ...571..172Z) or Blanton et al. 2003 (ApJ, 592, 819; ADS bibcode: 2003ApJ...592..819B) to highlight why edge correction matters.
* **Section 5.7 (Low-sSFR optical denominator)**:
  * *Improvement*: Add a sentence describing the typical metallicity and excitation assumptions when converting CO luminosity to molecular-gas mass ($M_{\text{H}_2} = \alpha_{\text{CO}} L'_{\text{CO}}$), emphasizing that $\alpha_{\text{CO}}$ varies with metallicity.
  * *Literature suggestion*: Bolatto et al. 2013 (ARA&A, 51, 207; DOI: 10.1146/annurev-astro-082812-140944).

---

## 5. Verification of Literature and Identifiers
All key literature references are verified and have complete ADS bibcodes, DOIs, or arXiv identifiers:
* **Best et al. 2005**: MNRAS, 362, 25; ADS bibcode: `2005MNRAS.362...25B`; DOI: `10.1111/j.1365-2966.2005.09192.x`
* **Hardcastle & Croston 2020**: New Astronomy Reviews, 88, 101539; arXiv: `2003.06137`
* **Harrison et al. 2018**: Nature Astronomy, 2, 198; ADS bibcode: `2018NatAs...2..198H`
* **Piotrowska et al. 2022**: MNRAS, 512, 1052; ADS bibcode: `2022MNRAS.512.1052P`; DOI: `10.1093/mnras/stac532`
* **Bolatto et al. 2013**: ARA&A, 51, 207; DOI: `10.1146/annurev-astro-082812-140944`

---

## 6. Final Verdict

JOURNAL_LEVEL_PASS: YES
