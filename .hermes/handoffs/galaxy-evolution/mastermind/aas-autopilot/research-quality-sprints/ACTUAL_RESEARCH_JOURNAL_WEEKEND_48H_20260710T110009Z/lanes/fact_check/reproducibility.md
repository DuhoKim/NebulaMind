# Reproducibility & Overclaim Referee Report

## 1. Integrity Check and Provenance Verification
All numeric values and statistics mentioned in the flagship and supplement manuscripts have been cross-checked against the raw measurements in the provenance-tracked JSON files under the `cycle_12_package` run metadata.
- **Flagship paper invariants**: 
  - Median matched-control $\Delta\log\text{sSFR}$ of $-1.309$ dex (95% bootstrap CI $[-1.334, -1.283]$ dex) traces exactly to the `matched_delta_log_sSFR_median_dex` and `matched_delta_log_sSFR_median_ci95_bootstrap` fields in [analysis_results.json](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json).
  - Sample breakdown: 39,553 star-forming, 12,234 intermediate, 8,146 AGN, and 67 unclassified galaxies match the `bpt_counts` field.
  - Euclidean matching separation diagnostics (0.0045 dex in $\log M_\star$ and 0.00021 in $z$) match the median delta parameters.
- **Supplement paper invariants**:
  - The relative neighbor-count baseline (high quartile low-sSFR fraction of 0.230; low quartile of 0.181; boostrap delta interval $[0.041, 0.059]$; regression coefficient of $0.032 \pm 0.004$) matches [m1_rp2_environment_quenching/analysis_results.json](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp2_environment_quenching/analysis_results.json).
  - Massive subset properties (9,298 massive hosts, 5,695 low-sSFR, BPT fractions of 0.430 and 0.607) match [m1_rp3_maintenance_heating/analysis_results.json](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp3_maintenance_heating/analysis_results.json).
  - Outflow demographics (4,440/60,000 AGN, median $\log\text{sSFR}$ of $-11.53$ vs. $-10.14$) match [m2_p1_outflow_escape_recycling/analysis_results.json](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p1_outflow_escape_recycling/analysis_results.json).
  - Environment-stratified massive host BPT fractions (0.509 vs 0.367; delta $[0.112, 0.170]$) match [m2_p2_radio_jet_environment/analysis_results.json](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p2_radio_jet_environment/analysis_results.json).
  - All 15 cells in Table 4 (simulation target vector) match the values in [m3_p3_simulation_validation/analysis_results.json](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/analysis_results.json).

*Integrity Blockers:* None.

---

## 2. Overclaim and Boundary Assessment
Both documents strictly respect the causal boundary:
- They state that the results are purely association-only.
- They define the fiber-aperture degeneracies and selection constraints (sequential `specObjID` bias and the $S/N \geq 3$ thresholding that discards weak emitters).
- The supplement clearly separates its local optical measurements from the missing physical dimensions (gas masses, radio jet power, X-ray cooling, halo catalogs) needed for physical mechanisms.

---

## 3. Section-Level Improvement Recommendations

### Flagship Paper ([rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_12_package/flagship_rp1/aastex/rp1_flagship_polished.tex))
* **Section 1 (Question and claim boundary)**: Expand on the selection effect of the 3-arcsec fiber aperture by referencing how the fraction of the total light sampled by the fiber varies across the redshift range ($0.02 < z < 0.12$).
* **Section 5 (Matched-control result)**: Introduce a short paragraph explaining the bootstrap resampling implementation details (e.g., number of bootstrap trials, typical variation of standard errors) to bolster the statistical description.

### Supplement Paper ([supplementary_denominator_atlas.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_12_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex))
* **Section 5.1 (Relative neighbor-count baseline)**: Quantify the angular projection effect by estimating the physical transverse distance corresponding to the 55-arcsec fiber-collision limit at the median redshift of the sample.
* **Section 5.7 (Low-sSFR optical denominator)**: Outline the systematic errors introduced by dust correction assumptions (specifically the Charlot & Fall 2000 Balmer decrement) in BPT-classified AGN hosts where non-stellar ionization makes standard H$\alpha$/H$\beta$ conversion factors more uncertain.

---

## 4. Literature Suggestions
To improve the context of the missing observables, the following papers are proposed:
* **For Fiber-Collision & Clustering Corrections**:
  - *Zehavi et al. (2011)*: Galaxy clustering studies in SDSS DR7 detailing fiber-collision corrections. (ADS Bibcode: `2011ApJ...736...59Z`, DOI: `10.1088/0004-637X/736/1/59`).
* **For Gas Mass/Depletion Systematics in AGN**:
  - *Saintonge et al. (2012)*: COLD GASS results on molecular gas fractions and their relation to stellar mass and SFR. (ADS Bibcode: `2012MNRAS.422.2285S`, DOI: `10.1111/j.1365-2966.2012.20777.x`).
* **For LINER Post-AGB Contamination**:
  - *Yan & Blanton (2012)*: Detailing the spatial distribution and post-AGB stellar origin of LINER-like emission. (ADS Bibcode: `2012ApJ...747...61Y`, DOI: `10.1088/0004-637X/747/1/61`).

---

JOURNAL_LEVEL_PASS: YES
