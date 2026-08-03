I have completed a thorough fact-check and overclaim review of the cycle 22 research package (`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_22_package`). 

Below is the structured referee report evaluating the flagship paper and the supplementary denominator atlas against the real data inventory in `provenance/REAL_DATA_SOURCE_CUSTODY.json` and the corresponding source JSON/CSV tables.

---

### I. Invariant & Numeric Integrity Audit
Every numeric claim in both manuscripts was cross-referenced line-by-line with the source artifacts.

*   **Flagship Paper (`flagship_rp1/aastex/rp1_flagship_polished.tex`):**
    *   **BPT Excitation Counts (Line 38):** The text reports 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 AGN/broad BPT-selected targets, and 67 unclassified objects. These perfectly match `bpt_counts` in `SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json`.
    *   **Matched Pairs & sSFR Offsets (Lines 13, 38, 49, 56):** The paper reports 8,146 matched pairs with a median $\Delta\log\text{sSFR}$ of $-1.309$ dex (bootstrap 95% CI: $[-1.334, -1.283]$ dex). These align with `matched_pairs`, `matched_delta_log_sSFR_median_dex` ($-1.308887$), and `matched_delta_log_sSFR_median_ci95_bootstrap` ($-1.334139$ to $-1.282140$) in the source pilot JSON.
    *   **Matching Quality (Line 38):** The reported median absolute distance offsets of $0.0045$ dex in $\log M_\star$ and $0.00021$ in redshift exactly match `match_abs_delta_logM_median` ($0.004460$) and `match_abs_delta_z_median` ($0.000211$) from the custody JSON.

*   **Supplementary Atlas (`supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`):**
    *   **Section 5.1 (Environment):** Low-sSFR fraction in the high-density quartile is 0.230 (3,456/15,000) and in the low-density quartile is 0.181 (2,710/15,000). Linear probability model (LPM) coefficient is $0.032 \pm 0.004$. These match `m1_rp2.../analysis_results.json` exactly.
    *   **Section 5.2 (Maintenance Heating):** 9,298 massive emission-line galaxies ($\log M_\star \ge 10.8$), 5,695 low-sSFR. AGN fraction is 0.430 in the massive sample and 0.607 in the low-sSFR massive sample. These match `m1_rp3.../analysis_results.json` (`massive_agn_fraction.fraction` = 0.4299, `massive_quenched_agn_fraction.fraction` = 0.6074).
    *   **Section 5.3 (Outflow Kinematics):** 4,440 of 60,000 high-excitation candidates. Median $\log\text{sSFR}$ is $-11.53$ vs. $-10.14$. These match `m2_p1.../analysis_results.json` exactly.
    *   **Section 5.4 (Radio-Jet Environment):** Massive host high-density quartile AGN fraction is 0.509; low-density quartile is 0.367. The bootstrap difference is $[0.112, 0.170]$. These match `m2_p2.../analysis_results.json`.
    *   **Section 5.5 (Mass Bin):** Peak AGN fraction in the $11.0-12.5$ mass bin is 0.520. Quenched fraction in the $11.0-12.5$ bin is 0.729. These match `m2_p3.../analysis_results.json`.
    *   **Section 5.6 (Tracer Census):** Range of 0.136 to 0.418 (BPT AGN fraction 0.136; red+emission fraction 0.418). These match `m3_p1.../analysis_results.json` exactly.
    *   **Section 5.7 (Gas Depletion):** Massive low-sSFR denominator contains 6,729 galaxies; BPT AGN fraction is 0.549. Median $\log(L_{\text{H}\alpha}/\text{erg s}^{-1}) = 40.061$. Offset vs massive star-forming galaxies is $-0.66$ dex. These match `m3_p2.../analysis_results.json`.
    *   **Section 5.8 (Simulation Target Vector):** The values in Table 4 for low-sSFR fraction, AGN fraction, and $u-r$ colour across the 15 bins are perfectly consistent with the raw numbers in `m3_p3.../analysis_results.json`.

---

### II. Claim Boundary & Overclaim Review
*   **Flagship Paper:** The paper is exceptionally clean of causal overclaims. It explicitly highlights that the measured offset is fiber-centered, morphology-uncontrolled, and strictly association-only. It clearly labels excitation as optical BPT-selected rather than asserting it is black-hole accretion power. It references Cid Fernandes et al. (2011) and Belfiore et al. (2016) to warn about retired stellar population contamination.
*   **Supplementary Atlas:** The supplement strictly adheres to framing the numbers as optical selection baselines and denominators. Each section features a clear list of "missing observables" (X-ray, radio, resolved kinematics, molecular gas, halo-matched grouping) required for follow-up. 
*   **Integrity Blockers:** None found. No mock or synthetic data are present; all data trace directly to actual files and row counts in the custody log.
*   **Literature Provenance:** All literature recommendations (e.g., Cid Fernandes et al. 2010/2011, Salim et al. 2007/2012, Belfiore et al. 2016) contain standard publication tags (ADS, DOI, or arXiv identifiers).

---

### III. Verdict

JOURNAL_LEVEL_PASS: YES
