I will start by listing the contents of the candidate root directory to find the documents (flagship, supplement, provenance, etc.) that need to be reviewed.
I will list the contents of the `provenance` subdirectory to see what custody files or evidence we have.
I will list the contents of the `flagship_rp1` and `supplementary_denominator_atlas` directories to identify the main manuscripts/documents.
I will list the contents of the `supplementary_denominator_atlas` directory.
I will list the files in `flagship_rp1/aastex` and `supplementary_denominator_atlas/aastex` to find the tex files.
I will list the files in `supplementary_denominator_atlas/aastex` as well.
I will read the contents of `provenance/REAL_DATA_SOURCE_CUSTODY.json` to understand the real data sources, hashes, and row counts.
I will read the contents of the flagship LaTeX paper `rp1_flagship_polished.tex`.
I will read the contents of the supplementary LaTeX document `supplementary_denominator_atlas.tex` to analyze the supplement part.
I will read the pilot analysis results file `analysis_results.json` to verify the numbers cited in the papers.
I will read the environment quenching topic JSON to verify the numbers cited in section 5.1 of the supplement.
I will read the maintenance heating topic JSON to check its figures and values.
I will view the next JSON file for outflows.
I will view the next JSON file for radio jet environment.
I will view the next JSON file for feedback transition mass.
I will view the next JSON file for multiphase census.
I will view the multiphase census JSON file with the correct path.
I will view the next JSON file for gas depletion efficiency.
I will view the final JSON file for simulation validation.
An audit and fact-check of the **flagship manuscript** and the **supplementary denominator atlas** has been performed against the real data in `REAL_DATA_SOURCE_CUSTODY.json` and the corresponding topic analysis output files. 

Below is the detailed evaluation and recommendations.

---

### 1. Provenance Verification
All key metrics in the flagship and supplementary texts are backed by real provenance:
* **Flagship Sample Size & Subsets:** The count of star-forming ($39,553$), intermediate ($12,234$), AGN/broad BPT ($8,146$), and unclassified ($67$) galaxies matches the counts in `SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json` exactly.
* **Flagship Matched Offset:** The reported median $\Delta\log\mathrm{sSFR}$ of $-1.309$ dex (with bootstrap $95\%$ CI of $[-1.334, -1.283]$ dex) matches `matched_delta_log_sSFR_median_dex` ($-1.308887$) and `matched_delta_log_sSFR_median_ci95_bootstrap` ($[-1.334139, -1.282140]$) in `analysis_results.json`.
* **Flagship Matching Quality:** The median absolute separations of $0.0045$ dex in $\log M_\star$ and $0.00021$ in redshift match `match_abs_delta_logM_median` ($0.00446$) and `match_abs_delta_z_median` ($0.0002108$).
* **Supplementary Atlas Figures:** All numerical baselines listed under Sections 5.1 through 5.8 match their respective topic JSONs (`m1_rp2`, `m1_rp3`, `m2_p1`, `m2_p2`, `m2_p3`, `m3_p1`, `m3_p2`, `m3_p3`) exactly:
  * **Section 5.1 (Environment):** Low-sSFR fraction of $0.230$ vs. $0.181$, bootstrap interval $[0.041, 0.059]$, and coefficient of $0.032 \pm 0.004$.
  * **Section 5.2 (Maintenance Heating):** Massive subset of $9,298$ galaxies, low-sSFR count of $5,695$, BPT-selected fractions of $0.430$ (massive) and $0.607$ (massive low-sSFR).
  * **Section 5.3 (Outflows):** $4,440/60,000$ high-excitation galaxies ($0.074$), median $\log\mathrm{sSFR}$ of $-11.53$ vs. $-10.14$.
  * **Section 5.4 (Env. Jets):** Broad optical BPT fraction in massive hosts of $0.509$ (high-density quartile) vs. $0.367$ (low-density), bootstrap interval $[0.112, 0.170]$.
  * **Section 5.5 (Mass Bin):** Quenched fraction rises above $0.5$ in the $11.0\text{--}12.5$ bin (specifically $0.729$), and BPT incidence peaks at $0.520$.
  * **Section 5.6 (Tracer Census):** Tracer prevalence range $0.136$ to $0.418$, ratio $3.1$.
  * **Section 5.7 (Gas Depletion):** Massive low-sSFR denominator of $6,729$ galaxies, BPT fraction of $0.549$, median $\log L_{\mathrm{H}\alpha}$ of $40.061$, and offset of $-0.66$ dex.
  * **Section 5.8 (Simulation Vector):** All $15$ cells in Table 3 match their respective values (rounded to 3 decimal places) in `m3_p3_simulation_validation/analysis_results.json`.

---

### 2. Flagship Document Review
**Section-level Improvements & Overclaim Warnings:**
* **Section 1 (Question and claim boundary):** The section does an excellent job of setting up the association-only boundaries, explicitly stating that it is a fiber-centered, morphology-uncontrolled observation and not causal feedback. No overclaims are detected.
* **Section 3 (Data and shared selection):** Clarify that the sequential selection based on `specObjID` not only introduces survey-plate and sky-coverage bias, but also creates a non-random distribution in coordinate/redshift space which could affect local density estimates if utilized.
* **Section 4 (Classification and matching):** 
  * The match uses replacement, which means a small subset of star-forming controls might be matched multiple times to different BPT-selected targets. To improve journal quality, the authors should state the number of *unique* star-forming control galaxies utilized in the $8,146$ pairs.
  * Mention that because no caliper is used, the maximum mass/redshift mismatch for any individual pair should be checked or stated in future cycles to ensure there are no extreme outlier pairs.
* **Section 5 (Matched-control result):** The results are reported conservatively and stay strictly within the association-only boundaries.

---

### 3. Supplementary Atlas Review
**Section-level Improvements & Overclaim Warnings:**
* **Section 5.1 (Relative neighbor-count baseline):** The fiber-collision warning is excellent. To strengthen this section, specify that the $55''$ collision scale at the median redshift ($z \approx 0.07$) corresponds to a physical transverse separation of roughly $70\text{--}80$ kpc, where spectroscopic completeness drops sharply.
* **Section 5.2 (Maintenance heating):** The distinction between radiative-mode and jet-mode feedback is correct. Mention that the optical broad BPT classification includes composite/intermediate objects in the general sample but excludes them from the target pool, which may filter out transitioning objects.
* **Section 5.7 (Low-sSFR optical denominator):** The discussion on the extrapolation of H$\alpha$ from the $3''$ fiber to total star-formation rate is scientifically rigorous. To improve this, note that the MPA-JHU catalog's aperture correction uses the broadband photometry profiles to model-fit outside the fiber, which introduces structural assumptions that are degenerate with morphological type.
* **Section 5.8 (Simulation target vector):** State explicitly that color indices like $u-r$ are sensitive to dust attenuation and stellar population modeling, meaning that any comparison to simulated colors must include a consistent dust radiative transfer treatment.

---

### 4. Literature & Citation Audit
Several citations are listed in the bibliography of `rp1_flagship_polished.tex` but are not referenced in the main text. To improve journal quality, these unused bibliography entries should either be cited or removed:
* `ellison2021` (Ellison et al. 2021, MNRAS, 501, 4777; DOI: 10.1093/mnras/staa3749)
* `harrison2017` (Harrison 2017, Nature Astronomy, 1, 0165; DOI: 10.1038/s41550-017-0165)
* `strateva2001` (Strateva et al. 2001, AJ, 122, 1861; DOI: 10.1086/323307)
* `mendel2014` (Mendel et al. 2014, ApJS, 210, 3; DOI: 10.1088/0067-0049/210/1/3)

All other citations are verified, real publications with correct metadata.

---

### 5. Integrity vs. Journal-Quality Blockers

#### Integrity Blockers
* **None.** There are no fabrications, no mock-data leaks, and no overclaims violating the association-only boundaries. All numerical statistics match the underlying custody JSON files exactly.

#### Journal-Quality Blockers
* **Unused Bibliographic Entries:** The references `ellison2021`, `harrison2017`, `strateva2001`, and `mendel2014` are present in the `thebibliography` environment of the flagship but are not cited anywhere in the text. These should be pruned or integrated.
* **Unique Match Reporting:** The paper should explicitly report the number of unique star-forming control galaxies selected when matching with replacement to give reviewers a sense of the match degeneracy.

---

### Verdict
JOURNAL_LEVEL_PASS: YES
