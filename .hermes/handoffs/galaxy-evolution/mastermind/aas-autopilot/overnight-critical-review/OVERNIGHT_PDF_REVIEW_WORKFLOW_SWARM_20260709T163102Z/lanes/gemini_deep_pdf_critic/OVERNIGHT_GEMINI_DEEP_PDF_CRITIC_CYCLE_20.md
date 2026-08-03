# OVERNIGHT_GEMINI_DEEP_PDF_CRITIC_CYCLE_20 Report

## 1. Status
OVERNIGHT_GEMINI_DEEP_PDF_CRITIC_CYCLE_20 status: ISSUES_FOUND

## 2. Files/paths inspected
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex`

## 3. Ranked findings
- **Major (Flow/Logic Error)**: In Paper 03 (`03_m1_rp3_maintenance_heating_integrated.tex`), the abstract states: "Among massive, low-sSFR hosts, the BPT-AGN fraction is 0.430 (3,997/9,298) in the massive subset and 0.607 (3,459/5,695) among massive low-sSFR objects..." The opening clause incorrectly scopes the entire sentence, contradicting the first reported fraction (which applies to the total massive subset, not just the low-sSFR hosts). This confuses the baseline description.
- **Minor (Formatting/Style)**: Papers 02 through 09 use Sentence case for their article titles and section headers (e.g., `\title{SDSS density proxy for environmental quenching}`). Standard AAS journal style (ApJ/AJ) requires Title Case for article titles and top-level section headings.
- **Minor (Citation Style Error)**: Papers 01, 02, 03, 04, 05, 07, 08, and 09 cite Kauffmann et al. 2003 as `Kauffmann et al.(2003a)` (and print "2003a" in the bibliography and text) even though there is no `2003b` cited in those documents. Only Paper 06 cites both 2003a and 2003b, making the "a" valid only for Paper 06.

## 4. Exact feed for PDF-writing pilot

### Fix 1: Paper 03 Abstract Logical Scope (Major)
**Target:** `03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex`
**Find:**
```latex
We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to construct an optical denominator for maintenance-heating follow-up in massive galaxies. Among massive, low-sSFR hosts, the BPT-AGN fraction is 0.430 (3,997/9,298) in the massive subset and 0.607 (3,459/5,695) among massive low-sSFR objects, providing a proxy for the duty-cycle denominator relevant to future X-ray or radio maintenance-heating studies.
```
**Replace:**
```latex
We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to construct an optical denominator for maintenance-heating follow-up in massive galaxies. The BPT-AGN fraction is 0.430 (3,997/9,298) in the massive subset and 0.607 (3,459/5,695) among massive low-sSFR objects, providing a proxy for the duty-cycle denominator relevant to future X-ray or radio maintenance-heating studies.
```

### Fix 2: Orphaned "(2003a)" Citation (Minor)
**Targets:** `01`, `02`, `03`, `04`, `05`, `07`, `08`, `09` (all except `06`).
**Find:**
```latex
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
```
**Replace:**
```latex
\bibitem[Kauffmann et al.(2003)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003, MNRAS, 346, 1055
```

### Fix 3: AAS Title Case Correction (Minor)
Apply Title Case adjustments to `\title{}` lines in the respective `.tex` files:
- Paper 02: `\title{SDSS Density Proxy for Environmental Quenching}`
- Paper 03: `\title{Optical-AGN Denominator for Maintenance-Heating Follow-up}`
- Paper 04: `\title{SDSS BPT-Selected Optical AGN Denominator for Outflow Escape Tests}`
- Paper 05: `\title{Environment Proxy for Optical AGN in Massive SDSS Hosts}`
- Paper 06: `\title{SDSS Mass Transition in Quenching and Optical AGN Incidence}`
- Paper 07: `\title{Common-Denominator Optical Tracer Census in SDSS}`
- Paper 08: `\title{Optical Denominator for Gas-Fraction versus Efficiency Tests}`
- Paper 09: `\title{SDSS Target Vector for Feedback-Model Validation}`
*Note: We recommend updating Section headers to Title Case natively in the text generation pipeline.*

## 5. Real-data/source/citation audit notes
- All 9 abstracts successfully maintain the "optical denominator/proxy" scope and cleanly decouple association metrics from explicit causal/calorimetric claims.
- Reference DOIs and ADS matches for all cited works (e.g., Dubois, Saintonge, Catinella, Veilleux) remain valid.
- The 0.074 fraction and median offsets strictly correspond to the real SDSS count totals (e.g., 4440/60000) verified in the previous cycles. 

## 6. Workflow/system notes
The system pipeline appears to be injecting titles directly from Markdown `#` headers (which canonically use sentence case) into the AAS TeX templates. Upgrading the export logic to apply a Title Case filter when mapping markdown fields to `\title{}` and `\section{}` will improve stylistic compliance with ApJ/AJ automatically.

## 7. Safety ledger
- No files edited.
- No public-linked PDF replaced.
- No public/live frontend or static root edits made.
- No DB, SQL, /api/pages, page_versions, wiki publish, trust recompute, or data mutation made.
- No deploy/restart executed.
- No git commit/push/merge/rebase/history rewrite.
- No cron creation/update/removal.
- No billing/cloud/OAuth/API-key/account changes; no credential/token/cookie reads.
- No external manuscript submission.
