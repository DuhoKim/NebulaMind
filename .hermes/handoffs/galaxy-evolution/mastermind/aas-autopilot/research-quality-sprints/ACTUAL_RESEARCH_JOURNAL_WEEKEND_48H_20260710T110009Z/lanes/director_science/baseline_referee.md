**Review: Baseline Sprint ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H**
**Role: Director / Science Referee**

I have inspected the candidate package, including the `REAL_DATA_SOURCE_CUSTODY.json` file. The provenance is intact, mapping the 60,000-galaxy cache, the 8,146 matched pairs, and the resulting exact numeric invariants (e.g., the -1.309 dex median sSFR offset) to real local data artifacts (`analysis_sample_bpt.csv`, `matched_agn_sf_pairs.csv`, etc.). There is no mock, synthetic, or invented data in the empirical results. The manuscripts successfully maintain strict association-only boundaries, avoiding unsupported causal claims.

However, to elevate this from a safe baseline to a journal-ready submission, several improvements are required.

### Integrity Blockers
*   **None.** The candidate successfully adheres to all safety locks and real-data rules. The results are strictly traced to the provenance receipt, and the language respects the association-only, selection-limited nature of the denominator.

### Journal-Quality Blockers & Section-Level Improvements

**1. Flagship Manuscript (`rp1_flagship_polished.tex`)**
*   **Abstract & Section 1 (Question and claim boundary):** The prose is excessively defensive. While it is excellent that you explicitly state what the paper *does not* do (e.g., "morphology-uncontrolled", "non-volume-complete"), the repetition of these exact phrases makes the text read like a legal disclaimer rather than a scientific paper. *Improvement:* Condense the limitations into a single dedicated paragraph in the introduction or methodology section, allowing the abstract to flow more naturally while retaining the strict association-only boundary.
*   **Section 4 (Classification and matching):** You mention that variance-normalized Euclidean distance matching was used with replacement, but you must justify *why* no maximum mass-redshift caliper was imposed. A brief sentence explaining the trade-off (e.g., retaining all 8,146 targets at the cost of potential localized mismatch) is needed for reproducibility and peer review.
*   **Bibliography:** The bibliography lacks standard digital identifiers. You must add ADS bibcodes or DOIs to every reference to meet journal standards.

**2. Supplementary Atlas (`supplementary_denominator_atlas.tex`)**
*   **Section 5.1 & 5.4 (Environment baselines):** The 10th-neighbor index is well-caveated regarding fiber collisions. However, you should add a brief sentence comparing this simple metric to standard SDSS group catalogs (e.g., the Yang et al. catalog) to ground the reader in why this is only a proxy.
*   **Section 5.7 (Low-sSFR optical denominator):** When discussing the H-alpha luminosity proxy and its limitations regarding total cold-gas mass, explicitly mention the need for CO-to-H2 conversion factor calibrations (e.g., metallicity dependence) as a missing observable for future follow-up. 
*   **Bibliography:** Like the flagship, the supplement bibliography must be updated with ADS bibcodes or DOIs.

### Literature Suggestions (with real source identifiers)
To address the bibliography issues and enrich the follow-up discussions, integrate the following identifiers and references:
*   **For IFU/MaNGA context (Flagship Sec 5 & Supp Sec 5.3):**
    *   Bundy et al. 2015, ApJ, 798, 7. ADS Bibcode: `2015ApJ...798....7B`
*   **For molecular/neutral gas depletion (Supp Sec 5.7):**
    *   Saintonge et al. 2017 (xCOLD GASS), ApJS, 233, 22. ADS Bibcode: `2017ApJS..233...22S`
    *   Catinella et al. 2018 (xGASS), MNRAS, 476, 875. ADS Bibcode: `2018MNRAS.476..875C`
*   **For environment and halo catalogs (Supp Sec 5.1):**
    *   Yang et al. 2007, ApJ, 671, 153. ADS Bibcode: `2007ApJ...671..153Y`
    *   Zehavi et al. 2002, ApJ, 571, 172. ADS Bibcode: `2002ApJ...571..172Z`
*   **For BPT classifications (Flagship Sec 4):**
    *   Kauffmann et al. 2003, MNRAS, 346, 1055. ADS Bibcode: `2003MNRAS.346.1055K`

Please address the repetitive prose and bibliography identifiers in the next cycle.

JOURNAL_LEVEL_PASS: NO
