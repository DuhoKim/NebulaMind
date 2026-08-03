I will list the contents of the candidate root directory to understand the files we need to inspect.
I will list the contents of the `provenance`, `flagship_rp1`, and `supplementary_denominator_atlas` subdirectories to find the documents and data custody information.
I will now list the contents of `flagship_rp1` and `supplementary_denominator_atlas`.
I will list the files in `flagship_rp1/aastex` and `supplementary_denominator_atlas`.
I will list the contents of `supplementary_denominator_atlas`.
I will list the files in `supplementary_denominator_atlas/aastex`.
I will view the `REAL_DATA_SOURCE_CUSTODY.json` file to understand the real source paths, hashes, and row counts.
I will view the primary pilot's analysis results to understand the underlying statistical metrics.
I will view the manifest for the remaining topic pilots.
I will view the topic pilot analysis results to gather the exact values and stats.
I will view the next set of topic pilot results.
I will view the next set of topic pilot results (p1, p2, p3).
I will view the next two topic pilot results (p2, p3).
I will view the next topic pilot results (p3).
I will view the remaining three topic pilot results (p1, p2, p3).
I will view the final two topic pilot results (p2, p3).
I will view the simulation validation topic pilot results.
I will view the flagship manuscript to verify the text, values, and citation accuracy.
I will view the supplementary manuscript to verify its text and citations.
An audit of the candidate package against the real data provenance inventories and source metrics has been conducted. 

### 1. Provenance Verification & Numeric Invariant Audit

All count and median statistics in both the flagship paper and the supplementary denominator atlas were cross-checked with the custody-backed analysis outputs:
* **Total cache size**: 60,000 galaxies (verified).
* **BPT classification counts**: 39,553 star-forming, 12,234 intermediate/composite, 8,146 broad BPT AGN, and 67 unclassified galaxies (verified).
* **Preferred matched pairs**: 8,146 pairs (verified).
* **Median $\Delta\log\text{sSFR}$ offset**: $-1.309$ dex (verified; value in JSON is $-1.308887$).
* **Matched coordinate offsets**: Median absolute separations of $0.0045$ dex in $\log M_\star$ and $0.00021$ in redshift (verified; values in JSON are $0.00446$ and $0.000211$).
* **Supplement Section 5.1 (Relative neighbor-count)**: Quartile quenched counts $3,456/15,000$ (high-density) and $2,710/15,000$ (low-density), bootstrap difference interval $[0.041, 0.059]$, and LPM high-density coefficient $0.032 \pm 0.004$ (verified).
* **Supplement Section 5.2 (Maintenance heating)**: $9,298$ massive galaxies, $5,695$ massive low-sSFR, massive BPT AGN fraction $0.430$, and low-sSFR massive BPT AGN fraction $0.607$ (verified).
* **Supplement Section 5.3 (High-excitation baseline)**: $4,440/60,000$ high-excitation AGN, median sSFR of $-11.53$ vs. $-10.14$ (verified).
* **Supplement Section 5.4 (Radio-jet environment)**: High-density massive AGN fraction $0.509$, low-density $0.367$, and difference interval $[0.112, 0.170]$ (verified).
* **Supplement Section 5.5 (Mass bins)**: Peak BPT fraction in $11.0\text{--}12.5$ bin is $0.520$, and quenched fraction is $0.729$ (verified).
* **Supplement Section 5.6 (Tracer census)**: Prevalence ranges $0.136$ to $0.418$, ratio $3.1$ (verified).
* **Supplement Section 5.7 (Gas depletion)**: $6,729$ transition/quenched galaxies, BPT AGN fraction $0.549$, median $\log L_{\text{H}\alpha}$ proxy of $40.061$, and offset of $-0.66$ dex (verified).
* **Supplement Section 5.8 (Simulation target vector)**: All 15 mass-redshift cells' counts, fractions, and colors in Table 4 match the JSON target vector within rounding limits (verified).

---

### 2. Integrity Blockers (Numerical Discrepancies)

* **Bootstrap sSFR confidence interval upper bound mismatch**: 
  Throughout the flagship paper [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex) (specifically in the Abstract, Section 1, Section 5, Table 1, Figure 2 caption, and Section 7), the bootstrap 95% confidence interval for the median $\Delta\log\text{sSFR}$ of the matched pairs is reported as `[-1.334,-1.283]` dex.
  However, the source results file `SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json` defines `matched_delta_log_sSFR_median_ci95_bootstrap` as `[-1.3341385500000003, -1.2821399375]`. The upper bound of $-1.2821...$ mathematically rounds to **$-1.282$**, not $-1.283$. This numerical mismatch is an integrity blocker.

---

### 3. Journal-Quality Blockers (Citations & Structure)

* **Unused bibliography items in Flagship**:
  The bibliography in `rp1_flagship_polished.tex` contains four references that are never cited in the body:
  * `ellison2021` (Ellison et al. 2021, MNRAS, 501, 4777)
  * `harrison2017` (Harrison 2017, Nature Astronomy, 1, 0165)
  * `strateva2001` (Strateva et al. 2001, AJ, 122, 1861)
  * `mendel2014` (Mendel et al. 2014, ApJS, 210, 3)
* **Unused bibliography items in Supplement**:
  The bibliography in [supplementary_denominator_atlas.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex) contains two references that are never cited in the body:
  * `cidfernandes2011` (Cid Fernandes et al. 2011, MNRAS, 413, 1687)
  * `mcnamara2007` (McNamara & Nulsen 2007, ARA&A, 45, 117)

---

### 4. Concrete Section-Level Improvements

* **Flagship Abstract, Sections 1, 5, 7 & Table 1**: Change all instances of `[-1.334,-1.283]` to `[-1.334,-1.282]` to enforce correct mathematical rounding.
* **Flagship Bibliography**: Remove the entries for `ellison2021`, `harrison2017`, `strateva2001`, and `mendel2014` to clean up unused references.
* **Supplement Bibliography**: Remove the entries for `cidfernandes2011` and `mcnamara2007` to resolve unused references.

JOURNAL_LEVEL_PASS: NO
