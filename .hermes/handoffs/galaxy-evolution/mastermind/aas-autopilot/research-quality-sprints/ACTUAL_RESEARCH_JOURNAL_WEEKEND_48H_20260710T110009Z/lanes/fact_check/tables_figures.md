# Fact-Checking and Overclaim Review

We have completed a comprehensive review of the flagship manuscript and supplementary atlas under the **tables/figures** phase for the sprint `ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z`.

---

## 1. Number and Statistical Verification

All numbers, row counts, statistical intervals, and decimal values in the LaTeX files were cross-referenced against the raw run outputs and the custody index (`provenance/REAL_DATA_SOURCE_CUSTODY.json`). 

### Flagship Verification (`rp1_flagship_polished.tex`) vs. `SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json`:
* **Matched Pairs**: The paper lists **8,146 pairs**, which matches `matched_pairs: 8146` exactly.
* **Median $\Delta\log\text{sSFR}$**: The paper reports **-1.309 dex**. The raw JSON contains `-1.3088869999999995`, which rounds exactly to **-1.309**.
* **95% Confidence Interval**: The paper reports **[-1.334, -1.283] dex**. The raw bootstrap CI in the JSON is `[-1.33413855, -1.2821399375]`, which rounds exactly to **[-1.334, -1.283]**.
* **BPT Class Denominator Counts**: The paper lists **39,553 star-forming, 12,234 intermediate/composite, 8,146 broad optical BPT-selected, and 67 unclassified** galaxies. This matches `bpt_counts` in the JSON exactly.
* **Matched Separations**: The paper lists median absolute separations of **0.0045 dex in $\log M_\star$** and **0.00021 in redshift**. These match `match_abs_delta_logM_median: 0.00446` and `match_abs_delta_z_median: 0.00021079` exactly.

### Supplement Verification (`supplementary_denominator_atlas.tex`) vs. `SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/`:
* **Relative Neighbor-Count (m1_rp2)**: 
  * High-density quartile quenched fraction: **0.230** (3,456/15,000) vs. JSON `fraction: 0.2304, k: 3456, n: 15000` (Matches).
  * Low-density quartile quenched fraction: **0.181** (2,710/15,000) vs. JSON `fraction: 0.18067, k: 2710, n: 15000` (Matches).
  * CI: **[0.041, 0.059]** vs. JSON `[0.04059, 0.05913]` (Matches).
  * LPM high-density coefficient: **0.032 +/- 0.004** vs. JSON coeff `0.03249`, se `0.003707` (Matches).
* **Maintenance Heating (m1_rp3)**:
  * Massive subset ($M_\star \ge 10.8$): **9,298** galaxies with **5,695** low-sSFR (Matches JSON `massive_rows` and `massive_quenched_rows`).
  * BPT fractions: **0.430** in massive and **0.607** in massive low-sSFR vs. JSON `0.42987` and `0.60737` (Matches).
* **Outflow Kinematics (m2_p1)**:
  * High-excitation candidates: **4,440 of 60,000** (0.074) (Matches JSON).
  * Median $\log\text{sSFR}$: **-11.53** vs. **-10.14** for full denominator (Matches JSON `median_log_sSFR_high_excitation: -11.532` and `median_log_sSFR_all: -10.1405`).
* **Radio-Jet Environment (m2_p2)**:
  * High-density quartile broad BPT: **0.509** (948/1864) vs. JSON `fraction: 0.50858, k: 948, n: 1864` (Matches).
  * Low-density quartile broad BPT: **0.367** (1007/2746) vs. JSON `fraction: 0.36671, k: 1007, n: 2746` (Matches).
  * CI: **[0.112, 0.170]** vs. JSON `[0.11189, 0.17021]` (Matches).
* **Stellar-Mass Selection (m2_p3)**:
  * Peak AGN fraction in $[11.0, 12.5]$ bin: **0.520** vs. JSON `0.520208` (Matches).
* **Tracer Census (m3_p1)**:
  * Prevalence range: **0.136** to **0.418** with widest-to-narrowest ratio **3.1** (Matches JSON).
* **Gas Depletion (m3_p2)**:
  * Massive low-sSFR denominator: **6,729** galaxies (Matches JSON `massive_transition_quenched_rows`).
  * Broad BPT fraction: **0.549** vs. JSON `0.54866` (Matches).
  * Median $L_{\text{H}\alpha}$: **40.061** (Matches JSON `median_log_lha_denominator`).
  * Offset vs. massive SF: **-0.66 dex** vs. JSON `-0.65858` (Matches).
* **Simulation Vector Table (m3_p3)**:
  * All 15 cells in Table 3 of the supplement match the target vector array in the JSON file exactly (e.g., cell 1: $N=6,201$, low-sSFR fraction = 0.006, broad BPT fraction = 0.003).

No numerical inconsistencies or synthetic data were found.

---

## 2. Integrity Blockers
* **None**. 
* There are no synthetic, mock, or placeholder values in either the flagship or the supplement.
* All reported statistics map directly to local custody-tracked assets.
* Overclaims are strictly guarded against via robust "association-only" language, clear fiber-collision/aperture limitations, and explicit lists of missing multiwavelength observables.

---

## 3. Journal-Quality Blockers & Recommended Section-Level Improvements

While the papers are in exceptional shape, minor additions of real literature identifiers can help polish the future-work sections:

### Flagship Section-Level Improvements:
* **Section 2 (Missing Observables for Future Causal Inference)**:
  To strengthen the catalog-comparison discussion, cite the Yang et al. group catalog framework:
  * *Literature suggestion*: Yang, X., Mo, H. J., van den Bosch, F. C., et al. 2007, ApJ, 671, 153 (ADS Bibcode: `2007ApJ...671..153Y`).
* **Section 5 (Matched-Control Result)**:
  Make the bootstrap confidence interval context more precise by citing standard resampling guides:
  * *Literature suggestion*: Efron, B., & Tibshirani, R. J. 1993, *An Introduction to the Bootstrap*, Chapman & Hall (ISBN: `978-0412042317`).

### Supplement Section-Level Improvements:
* **Section 5.1 (Relative neighbor-count baseline)**:
  In the fiber-collision warning paragraph, explicitly reference the SDSS spectroscopic tiling strategy:
  * *Literature suggestion*: Blanton, M. R., Lin, H., Lupton, R. H., et al. 2003, ApJ, 592, 819 (ADS Bibcode: `2003ApJ...592..819B`).

---

## Verdict

JOURNAL_LEVEL_PASS: YES
