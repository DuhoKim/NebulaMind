# gemini_deep_pdf_critic cycle 8
Started UTC: 2026-07-09T19:16:17Z
Model: Gemini 3.1 Pro (High)
Provider: agy
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_08_gemini_deep_pdf_critic.md

### 1. OVERNIGHT_GEMINI_DEEP_PDF_CRITIC_CYCLE_08 status
**ISSUES_FOUND**

### 2. Files/paths actually inspected
**Candidate TeX source files inspected:**
- `/.../cycle_08_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex`
- `/.../cycle_08_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
- `/.../cycle_08_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex`
- `/.../cycle_08_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex`
- `/.../cycle_08_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex`
- `/.../cycle_08_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex`
- `/.../cycle_08_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex`
- `/.../cycle_08_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`
- `/.../cycle_08_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex`

**Public-linked research-topic manuscripts inspected:**
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md`
- Related `index.html` within the public wiki root.

### 3. Ranked findings, with severity

**1. [MAJOR] Stale public-vs-local mismatch in missing-observables phrasing (Papers 04-09)**  
Papers 04 through 09 consistently refer readers to a non-existent public destination. In Section 5 (`\section{Interpretation and missing observables}`), the boilerplate phrasing explicitly states:  
> `"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page."`  
However, the public-linked `research-topics-from-wiki` page only contains the M1-tier proposals (`RP-1`, `RP-2`, and `RP-3`). The proposals for M2 and M3 do not exist on the public wiki yet, creating a broken referential loop for readers of these new PDFs.  
*(Note: Paper 03 also contains this string, which is technically valid since RP-3 exists, but for uniformity, it should be cleaned up).*

**2. [MINOR] Title text mismatch between wiki links and generated PDFs**  
The public wiki hardcodes proposal titles (e.g., `"A Matched-Control SDSS DR17 Pilot Test of Specific Star Formation in Optical AGN Hosts"`) that differ slightly from the finalized `\title{}` compiled in the TeX source (e.g., `"Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot"`). This causes a reader-flow mismatch when clicking from the wiki.

**3. [IMPROVEMENT] Incomplete research-topic integration**  
The public wiki infrastructure needs an update sequence to ingest and generate proposal sections for the 6 newly piloted M2 and M3 topic tracks.

### 4. Exact feed for PDF-writing pilot

To safely decouple the local PDFs from the stale wiki link without changing measured values or real-data boundaries, issue the following exact TeX rewrite instruction for **Papers 03, 04, 05, 06, 07, 08, and 09**:

**Target Section:** `\section{Interpretation and missing observables}\label{sec:missing}`  
**Current Text:** `SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.`  
**Required Rewrite:** `SDSS-only pilot; full proposal requires additional survey data.`

*(The sentence immediately following this string in each respective paper already explicitly lists the exact required survey data, meaning no information is lost by removing the pointer to the missing research-topic page.)*

### 5. Real-data/source/citation audit notes
- **Mock data:** Passed. None found. 
- **Citations:** Passed. All cited works (`saintonge`, `catinella`, `dubois`, `mcnamara`, etc.) are real and accurately reflect standard literature.
- **Typo check:** Passed. The previous cycle's correction of `Dubrois` to `Dubois` in Paper 09 was successfully integrated.
- **Data boundaries:** Passed. Every paper explicitly limits itself to being an optical baseline/denominator and avoids broad causal claims.

### 6. Workflow/system notes
**Wiki-to-PDF synchronization:** The document pipeline is currently out-of-sync. The PDF generation loop has produced 9 valid candidate papers, but the static public wiki report generator stopped after integrating the first 3. The workflow orchestrator needs a step to either pull the 6 new M2/M3 papers into the wiki generation loop or decouple the PDF writing from expecting an updated wiki page. Additionally, wiki link text should be dynamically pulled from the `\title{}` tag of the finalized PDFs.

### 7. Safety ledger
- **Public-linked PDFs replaced:** 0
- **Public/live roots touched:** 0
- **DB/API/wiki/trust writes:** 0
- **Deploy/restart:** 0
- **Git commit/push/merge/rebase/history rewrite:** 0
- **Cron changes:** 0
- **Billing/cloud/OAuth/account changes:** 0
- **External manuscript submission:** 0
- **Candidate files edited:** 0 (read-only inspection performed)


# command_result
exit_code=0
elapsed_s=140.1
timed_out=False
finished_utc=2026-07-09T19:18:38Z
