# OVERNIGHT_HWAO_DIRECTOR_CYCLE_07

## 1. Status
**ISSUES_FOUND**

## 2. Files/paths actually inspected
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_07_nine_papers/*/*.tex` (all 9 manuscripts)

## 3. Ranked findings, with severity
- **M-1 (major)**: Paper 01 `m1_rp1_sdss_agn_sfr_integrated.tex` — Bootstrap CI upper bound in text is still `−1.283` when it should be `−1.282`.
- **M-2 (major)**: Papers 02–09 — Section 2 ("Data and Sample Selection") contains a 350-word shared-selection block that is verbatim identical across all 8 papers, risking journal self-plagiarism flags.
- **M-3 (major)**: Paper 06 `m2_p3_feedback_transition_mass_integrated.tex` — The mass bin `\log(M_\star/M_\odot)=11.0$--$12.5` is implausibly wide (1.5 dex) and should be rewritten to clarify it as an open high-mass tail.
- **M-4 (major)**: Papers 02–09 — Generic figure filename `fig-topic.pdf` with near-identical, uninformative captions. Needs more specificity per paper.
- **m-1 (minor)**: All 9 papers — `\affiliation{Public SDSS DR17 data only}` is a non-standard usage of the affiliation field; data provenance should be moved to an Acknowledgments section.
- **m-2 (minor)**: Paper 04 `m2_p1_outflow_escape_recycling_integrated.tex` — The term "high-excitation optical AGN" is used in the title and abstract but never explicitly defined in the selection criterion.
- **i-1 (improvement)**: All 9 papers — Missing `\acknowledgments` section which is required by the SDSS data-use policy.

## 4. Exact feed for PDF-writing pilot
- **Paper 01**: In `m1_rp1_sdss_agn_sfr_integrated.tex`, replace `[-1.334,-1.283]` with `[-1.334,-1.282]`.
- **Papers 02–09**: Rewrite `\section{Data and Sample Selection}` in each paper to uniquely summarize the selection process in the context of the specific paper's objective, avoiding verbatim copy-paste.
- **Paper 06**: In `m2_p3_feedback_transition_mass_integrated.tex`, replace `\log(M_\star/M_\odot)=11.0$--$12.5` with `\log(M_\star/M_\odot) > 11.0` or explicitly state it is the high-mass tail.
- **All Papers**: Remove `\affiliation{Public SDSS DR17 data only}`. Add an `\acknowledgments` section before the bibliography containing: `We thank the SDSS collaboration. Funding for the Sloan Digital Sky Survey IV has been provided by the Alfred P. Sloan Foundation, the U.S. Department of Energy Office of Science, and the Participating Institutions.`
- **Paper 04**: Add a sentence in Section 4 defining "high-excitation optical AGN".

## 5. Real-data/source/citation audit notes
All 9 papers correctly maintain their baseline optical-denominator framing. No causal feedback overclaims or mock/synthetic data were found.

## 6. Workflow/system notes
The wiki-to-PDF pipeline is generating identical text blocks (Section 2) and identical figure names/captions across multiple papers. The generator needs an update to inject paper-specific context into these shared templates.

## 7. Safety ledger
- Edits made: 0
- Public/live roots touched: 0
- DB/API/wiki/trust writes: 0
- Deploy/restart: 0
- Git commit/push/merge/rebase: 0
- Cron changes: 0
- Billing/cloud/OAuth/account changes: 0
- External manuscript submission: 0
