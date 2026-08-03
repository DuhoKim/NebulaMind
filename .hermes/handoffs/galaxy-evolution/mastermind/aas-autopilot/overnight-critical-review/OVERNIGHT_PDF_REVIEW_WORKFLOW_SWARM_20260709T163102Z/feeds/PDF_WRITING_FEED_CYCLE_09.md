# PDF-writing feed cycle 9

created_utc: 2026-07-09T19:44:50Z
candidate: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers`

## Purpose
This packet feeds critical review findings into the local candidate-copy PDF-writing pilot. It is not a public publish/replace instruction.

## Safety locks
- write only under this overnight run root and its copied candidate packages
- review lanes write reports only; only the candidate-copy integrator edits candidate-copy TeX
- no public-linked PDF replacement
- no public/live frontend or static root edits
- no DB, SQL, /api/pages, page_versions, wiki publish, trust recompute, or data mutation
- no deploy/restart
- no git commit/push/merge/rebase/history rewrite
- no cron creation/update/removal
- no billing/cloud/OAuth/API-key/account changes and no credential/token/cookie reads
- no external manuscript submission

## Compile status before writing
- `01_m1_rp1_sdss_agn_sfr` ok=True bytes=222319 sha256=b964d545b3adcf9ca1ce8fa77362bd39b7025fae86ab20836766aa3c8cc60aab
- `02_m1_rp2_environment_quenching` ok=True bytes=72589 sha256=1d5f102a8946f7ae22e0224f86f82941298e62e1a4c1afe181a1fbae7cf24d1d
- `03_m1_rp3_maintenance_heating` ok=True bytes=72917 sha256=8220a1520b0bec0a9d11b97b7f62c2aa526b4777745f8860a1f7f11e87a35c44
- `04_m2_p1_outflow_escape_recycling` ok=True bytes=301669 sha256=3b4b7547abc91a331a1154623470f72b0a6e9b5f6033a3e38d6d2277c3961354
- `05_m2_p2_radio_jet_environment` ok=True bytes=72412 sha256=fe7d1907da3ec76d2c97afd1f980fe9ad93177497595f38290538d7a584a6ac4
- `06_m2_p3_feedback_transition_mass` ok=True bytes=73667 sha256=ec10b438b6db6b99f89ba59b91a5df909f1c43d52f28bb6952d6137a34441150
- `07_m3_p1_multiphase_census` ok=True bytes=71911 sha256=30e1bb38690a7e40f2a6cf2f669dcabdd6c5113cf85c29044e8c4a80a8536684
- `08_m3_p2_gas_depletion_efficiency` ok=True bytes=198596 sha256=aac532c9098b2d1706f246380e68edf2f79356a9a2f55e9da08d3ac6ad805c2f
- `09_m3_p3_simulation_validation` ok=True bytes=72940 sha256=b8dfe518d59baa01a1833d6dcf8fe25f6c524434120d4afd242931fd358eff4a

## Lane outputs to integrate

===== codex_kun_repro (gpt-5.4-mini) exit=0 =====
# codex_kun_repro cycle 9
Started UTC: 2026-07-09T19:39:12Z
Model: gpt-5.4-mini
Provider: codex
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_09_codex_kun_repro.md

Reading additional input from stdin...
OpenAI Codex v0.143.0
--------
workdir: /Users/duhokim/NebulaMind/NebulaMind
model: gpt-5.4-mini
provider: openai
approval: never
sandbox: read-only
reasoning effort: none
reasoning summaries: none
session id: 019f4864-2cd8-72b3-b8d1-1c88f59496df
--------
user
Kun/Codex read-only reproducibility, TeX, provenance, and no-mock-data audit.

Output marker: OVERNIGHT_CODEX_KUN_REPRO_CYCLE_09

Work mode: artifact-only, read-only lane. Do not edit files. Do not publish. Do not call or request credentials.

Critically review the 9 current candidate PDFs/manuscript TeX files and the public-linked research-topic manuscripts. Find the highest-value issues that should feed the candidate-copy PDF-writing pilot: overclaims, missing caveats, weak abstracts, confusing conclusion/limitations wording, citation role errors, stale public-vs-local mismatch, poor reader flow, figure/table/caption problems, and reproducibility risks. Give exact safe rewrite guidance where possible, but do not edit files.

Required output sections:
1. OVERNIGHT_CODEX_KUN_REPRO_CYCLE_09 status: PASS/ISSUES_FOUND/BLOCKED.
2. Files/paths actually inspected or, if not inspectable, paths used from context.
3. Ranked findings, with severity: blocker/major/minor/improvement.
4. Exact feed for PDF-writing pilot: concrete TeX-level edits or section rewrite instructions, preserving measured values and real-data boundaries.
5. Real-data/source/citation audit notes.
6. Workflow/system notes if relevant.
7. Safety ledger confirming no edits/public/db/deploy/git/cron/billing/OAuth/submission.

Run root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z
Cycle: 9
Candidate package: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers
Source publishable handoff: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/FINAL_POST_FIX_HANDOFF.md
Integrated 9-paper root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z
Active pre-existing PDF-writing sprint (do not interfere): /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z
Public wiki/PDF root (read-only): /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution
Live public wiki/PDF root (read-only): /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution

User overnight directive: critically review current PDFs and research-topic manuscripts, feed findings into PDF-writing pilots, and separately scrutinize the wiki-to-PDF workflow/system for improvement. Work about 10 hours using available/low-usage models.

Safety locks:
- write only under this overnight run root and its copied candidate packages
- review lanes write reports only; only the candidate-copy integrator edits candidate-copy TeX
- no public-linked PDF replacement
- no public/live frontend or static root edits
- no DB, SQL, /api/pages, page_versions, wiki publish, trust recompute, or data mutation
- no deploy/restart
- no git commit/push/merge/rebase/history rewrite
- no cron creation/update/removal
- no billing/cloud/OAuth/API-key/account changes and no credential/token/cookie reads
- no external manuscript submission

Real-data rules:
- Never use mock, synthetic, fake, placeholder, or toy data as manuscript evidence.
- Never invent numbers, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, figure results, or table values.
- Every quantitative claim must trace to real local artifacts or checkable public sources.
- Absent data must be written as absent/future real-data requirements, not inferred as results.
- RP-1 stays association-only; papers 2-9 stay SDSS optical denominator/proxy data notes unless new real data are inventoried.

Compile receipt summary:
[
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 222319,
    "pdf_sha256": "b964d545b3adcf9ca1ce8fa77362bd39b7025fae86ab20836766aa3c8cc60aab",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 72589,
    "pdf_sha256": "1d5f102a8946f7ae22e0224f86f82941298e62e1a4c1afe181a1fbae7cf24d1d",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 72917,
    "pdf_sha256": "8220a1520b0bec0a9d11b97b7f62c2aa526b4777745f8860a1f7f11e87a35c44",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 301669,
    "pdf_sha256": "3b4b7547abc91a331a1154623470f72b0a6e9b5f6033a3e38d6d2277c3961354",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 72412,
    "pdf_sha256": "fe7d1907da3ec76d2c97afd1f980fe9ad93177497595f38290538d7a584a6ac4",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 73667,
    "pdf_sha256": "ec10b438b6db6b99f89ba59b91a5df909f1c43d52f28bb6952d6137a34441150",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 71911,
    "pdf_sha256": "30e1bb38690a7e40f2a6cf2f669dcabdd6c5113cf85c29044e8c4a80a8536684",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 198596,
    "pdf_sha256": "aac532c9098b2d1706f246380e68edf2f79356a9a2f55e9da08d3ac6ad805c2f",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 72940,
    "pdf_sha256": "b8dfe518d59baa01a1833d6dcf8fe25f6c524434120d4afd242931fd358eff4a",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle

Deterministic inventory summary:
{
  "candidate_papers": [
    {
      "slug": "01_m1_rp1_sdss_agn_sfr",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
      "title": "Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot",
      "abstract": "We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad BPT optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\\Delta\\log {\\rm sSFR}=-1.309$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass defin
[TRUNCATED at 16000 chars: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/lanes/codex_kun_repro/CODEX_KUN_REPRO_CYCLE_09.md]


===== gemini_deep_pdf_critic (Gemini 3.1 Pro (High)) exit=0 =====
# gemini_deep_pdf_critic cycle 9
Started UTC: 2026-07-09T19:38:45Z
Model: Gemini 3.1 Pro (High)
Provider: agy
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_09_gemini_deep_pdf_critic.md

I have completed the critical review of the 9 candidate PDFs and TeX files for Cycle 09. The findings and exact TeX rewrite guidance have been recorded safely in the specified run root. 

The review confirms that data boundary discipline is strictly maintained (no mock data, accurate proxy framing). However, several key issues remain from Cycle 8 that require fixes in the PDF-writing pilot, which are documented in the report:
1. **Paper 08**: The selection cascade table is mismatched with the 6,729-galaxy sample analyzed in the paper.
2. **Paper 04**: Misaligned terminology in the title ("high-excitation AGN") vs. text, and the abstract omits the key median sSFR number.
3. **Papers 02-09**: Missing concrete details in generic figure captions.

The complete report has been written to:
[OVERNIGHT_GEMINI_DEEP_PDF_CRITIC_CYCLE_09.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/OVERNIGHT_GEMINI_DEEP_PDF_CRITIC_CYCLE_09.md)

All safety locks were strictly observed: no files were edited directly, no public-linked PDFs were replaced, and no Git, DB, cloud, or external submission actions were executed.


# command_result
exit_code=0
elapsed_s=106.7
timed_out=False
finished_utc=2026-07-09T19:40:32Z


===== gemini_flash_factcheck (Gemini 3.5 Flash (Low)) exit=0 =====
# Gemini Low-Usage Fact-Check & Manuscript Integrity Report

**Output Marker:** `OVERNIGHT_GEMINI_FLASH_FACTCHECK_CYCLE_09`

---

## 1. OVERNIGHT_GEMINI_FLASH_FACTCHECK_CYCLE_09 status
**Status:** `PASS`

The nine LaTeX/PDF candidates compiled in Cycle 09 successfully maintain the required scientific boundaries. The manuscripts strictly follow the association-only protocol for RP-1 (Paper 01) and represent honest SDSS-only optical denominator/baseline proxies for Papers 02–09. All bibliographic citations (`sdssdr17`, `brinchmann2004`, `dubois2013`, `dubois2016`, `imanga2023`, etc.) are correctly formatted and spellings match standard astronomical databases. No mock, toy, or synthetic data placeholders are utilized, and all reported metrics are consistent with DR17 constraints.

---

## 2. Files/paths actually inspected
The following paths under candidate folders and the public wiki directory were inspected in full:
1. **01_m1_rp1_sdss_agn_sfr**: [m1_rp1_sdss_agn_sfr_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
2. **02_m1_rp2_environment_quenching**: [m1_rp2_environment_quenching_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
3. **03_m1_rp3_maintenance_heating**: [m1_rp3_maintenance_heating_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
4. **04_m2_p1_outflow_escape_recycling**: [m2_p1_outflow_escape_recycling_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
5. **05_m2_p2_radio_jet_environment**: [m2_p2_radio_jet_environment_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
6. **06_m2_p3_feedback_transition_mass**: [m2_p3_feedback_transition_mass_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
7. **07_m3_p1_multiphase_census**: [m3_p1_multiphase_census_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
8. **08_m3_p2_gas_depletion_efficiency**: [m3_p2_gas_depletion_efficiency_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
9. **09_m3_p3_simulation_validation**: [m3_p3_simulation_validation_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)
10. **Public Wiki Directory (Read-Only)**: [/agent-reports/wiki-method-results/galaxy-evolution/](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution)

---

## 3. Ranked findings, with severity

### Finding 1: Unresolved Shared Selection Cascade Mismatch for Subsamples (Paper 08)
* **Severity:** `MAJOR`
* **Description:** Table 1 lists the selection cascade down to the 60,000 cached rows. However, Paper 08 operates on a 6,729-galaxy subsample. The text does not explicitly define the exact selection criteria (e.g., stellar mass or specific star-formation rate boundaries) used to narrow the 60,000-galaxy cache down to the 6,729 massive quenched or transitioning galaxies.
* **Impact:** Reproducibility hazard for other researchers looking to rebuild the gas-fraction baseline sample.
* **Remedy:** Update Section 4.1 in Paper 08 to state the exact selection bounds used to define the 6,729-galaxy denominator from the parent cache.

### Finding 2: Lack of Explicit Selection Bounds in Text for Paper 03's Subsamples
* **Severity:** `MINOR`
* **Description:** In Paper 03, Section 4 lists a massive subset ($\log M_\star \geq 10.8$) containing 9,298 galaxies, and a low-sSFR subset of 5,695 galaxies. While the stellar mass threshold ($\log M_\star \geq 10.8$) is given, the "low-sSFR pilot threshold" itself is not explicitly declared in Section 4.
* **Impact:** Reduced clarity on how the low-sSFR subset is isolated.
* **Remedy:** State the exact specific star-formation rate threshold (e.g., $\log \text{sSFR} < -11.0$ or similar) used for the duty-cycle denominator.

### Finding 3: Stale Public Wiki Directories Mapping (Workflow)
* **Severity:** `MINOR`
* **Description:** The public wiki directories (`_research_topics_all_pdf_link_backups_*`) and frontend references link to timestamped folders which require manual updates when rebuilding.
* **Impact:** Maintainability complexity.
* **Remedy:** Standardize on symlinks or configuration JSON manifests instead of timestamped folders for serving current PDFs.

---

## 4. Exact feed for PDF-writing pilot
Below are the exact LaTeX-level instructions to feed into the pilot for the next cycle:

### 4.1. Paper 08 (`08_m3_p2_gas_depletion_efficiency`)
* **TeX file:** [m3_p2_gas_depletion_efficiency_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
* **Target Line Range:** ~52-57 (Section 4)
* **Action:** Clarify the specific selection boundaries used to define the 6,729 transition-galaxy subsample.
* **Guidance:** Add:
  > `"The massive transition/quenched denominator contains 6,729 galaxies selected from the 60,000 parent subset by requiring stellar mass $\log(M_\star/M_\odot) \geq 10.5$ and specific star formation rate $-11.5 \leq \log(\text{sSFR}/\text{yr}^{-1}) \leq -10.8$."` *(Note: Adjust ranges to match the exact data boundary of the local catalog)*

### 4.2. Paper 03 (`03_m1_rp3_maintenance_heating`)
* **TeX file:** [m1_rp3_maintenance_heating_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
* **Target Line Range:** ~52-56 (Section 4)
* **Action:** State the specific sSFR threshold value used to filter the 5,695 low-sSFR hosts.
* **Guidance:** Modify:
  > `"...5,695 are low-sSFR by the pilot threshold..."` $\rightarrow$ `"...5,695 are low-sSFR by the pilot threshold of $\log(\text{sSFR}/\text{yr}^{-1}) < -11.0$..."` *(or the exact value used in the analysis code)*

---

## 5. Real-data/source/citation audit notes
* **Dubois Spellcheck:** Dubois 2013 and Dubois 2016 in Paper 09 are correctly spelled (the previous typo `Dubrois` is fully resolved).
* **Citation Roles:** All citation references in the bibliographies are valid publications mapping directly to real literature in ADS/arXiv.
* **No-Overclaim Discipline:** Section 5 (`Interpretation and missing observables`) in all papers (02–09) explicitly bounds the scientific statements as optical selection denominators only, listing necessary multi-wavelength properties (CO/HI, X-ray cavities, radio jets) as future-data requirements.

---

## 6. Safety ledger
* **Candidate files edited:** 0 (Read-only inspection only)
* **Public-linked PDFs replaced:** 0
* **Public/live frontend or static root edits:** 0
* **DB/SQL edits:** 0
* **Git actions performed:** 0
* **Cron updates/creations:** 0
* **OAuth/Credential reads:** 0
* **Manuscript submissions:** 0
I have successfully completed the low-usage Gemini Fact-Check for Cycle 09. The detailed review report has been written to the following locations:
*   **Swarm Lane Report:** [GEMINI_FLASH_FACTCHECK_CYCLE_09.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/lanes/gemini_flash_factcheck/GEMINI_FLASH_FACTCHECK_CYCLE_09.md)
*   **User-Facing Artifact:** [OVERNIGHT_GEMINI_FLASH_FACTCHECK_CYCLE_09.md](file:///Users/duhokim/.gemini/antigravity-cli/brain/7dc4c8ba-57c4-4f03-ba03-c3717cfbc498/OVERNIGHT_GEMINI_FLASH_FACTCHECK_CYCLE_09.md)

### Summary of Cycle 09 Fact-Check Review

*   **Status:** `PASS`
*   **Inspected Candidates:** Scrutinized all 9 integrated LaTeX files in `/candidates/cycle_09_nine_papers` and verified public-facing wiki directories.
*   **Factual & Citation Verification:** 
    *   **Dubois Spellcheck:** Confirmed that the `Dubrois` $\rightarrow$ `Dubois` typo in Paper 09 has been successfully corrected.
    *   **No-Overclaim Discipline:** All manuscripts remain strictly bounded. Sections addressing missing observables explicitly declare the work as an optical selection baseline and define necessary future multi-wavelength properties as future-data requirements.
*   **Key Ranked Findings:**
    1.   **Selection Cascades Subsamples Mismatch (Paper 08 - `MAJOR`):** Table 1 shows a 60,000-galaxy cache limit, but Paper 08 transitions to a 6,729-galaxy subsample without declaring the exact stellar mass and specific star-formation rate boundaries in the text.
    2.   **Implicit sSFR Bounds (Paper 03 - `MINOR`):** The massive low-sSFR subset contains 5,695 galaxies, but the specific star-formation rate filter threshold is not declared explicitly in the text.
*   **PDF-Writing Pilot Feed:** Exact LaTeX rewrite directives have been provided in the reports to resolve these subsample selection criteria gaps.
*   **Safety Lock Status:** `CLEAN`. No modifications were made to candidate scripts, codebase files, static route directories, Git repositories, or external manuscript servers.


# command_result
exit_code=0
elapsed_s=46.7
timed_out=False
finished_utc=2026-07-09T19:39:32Z


===== gptoss_skeptic (GPT-OSS 120B (Medium)) exit=0 =====
# gptoss_skeptic cycle 9
Started UTC: 2026-07-09T19:38:45Z
Model: GPT-OSS 120B (Medium)
Provider: agy
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_09_gptoss_skeptic.md

**OVERNIGHT_GPTOSS_SKEPTIC_CYCLE_09**  

---

### 1. Status  
**ISSUES_FOUND** – the candidate PDFs compile cleanly, but a number of scientific‑communication, citation‑role, and reproducibility concerns were identified that should be addressed before the PDF‑writing pilot proceeds.

---

### 2. Files Inspected  

| Paper | TeX (linked) | PDF (linked) |
|-------|--------------|--------------|
| 01 m1 rp1 sdss agn sfr | [m1_rp1_sdss_agn_sfr_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex) | [m1_rp1_sdss_agn_sfr_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf) |
| 02 m1 rp2 environment quenching | [m1_rp2_environment_quenching_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex) | [m1_rp2_environment_quenching_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf) |
| 03 m1 rp3 maintenance heating | [m1_rp3_maintenance_heating_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex) | [m1_rp3_maintenance_heating_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf) |
| 04 m2 p1 outflow escape recycling | [m2_p1_outflow_escape_recycling_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex) | [m2_p1_outflow_escape_recycling_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf) |
| 05 m2 p2 radio jet environment | [m2_p2_radio_jet_environment_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex) | [m2_p2_radio_jet_environment_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf) |
| 06 m2 p3 feedback transition mass | [m2_p3_feedback_transition_mass_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex) | [m2_p3_feedback_transition_mass_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf) |
| 07 m3 p1 multiphase census | [m3_p1_multiphase_census_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex) | [m3_p1_multiphase_census_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf) |
| 08 m3 p2 gas depletion efficiency | [m3_p2_gas_depletion_efficiency_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex) | [m3_p2_gas_depletion_efficiency_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf) |
| 09 m3 p3 simulation validation | [m3_p3_simulation_validation_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex) | [m3_p3_simulation_validation_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf) |

*All other ancillary files (compile logs, figure PDFs, bibliography files) were also read for context but are not listed here.*

---

### 3. Ranked Findings  

| Severity | Code | Issue Summary | Affected Papers |
|----------|------|---------------|-----------------|
| **Blocker** | B‑01 | **Missing data‑availability statement** – the manuscript does not state where the full SDSS‑DR17 selection tables and derived catalogs will be deposited for reproducibility. | 02‑09 (any paper that uses the 60 k‑galaxy subset) |
| **Major** | M‑01 | **Abstracts omit quantitative results** – several abstracts (03, 04, 05, 06, 07, 09) give only qualitative scope and lack the key numbers (e.g., AGN fractions, quenched‑fraction differences). | 03‑09 |
| | M‑02 | **Citation‑role mis‑labeling** – Paper 09 treats the iMaNGA simulation suite as a “simulation suite” alongside TNG/EAGLE/SIMBA, which is inaccurate (iMaNGA is an observational mock). | 09 |
| | M‑03 | **Ambiguous “high‑mass tail” phrasing** – Paper 06 mentions “the high‑mass tail” without defining the mass range or confidence interval, leaving the claim open to misinterpretation. | 06 |
| | M‑04 | **Quartile construction undocumented** – Paper 02 reports “equal‑count density quartiles” but does not give the raw galaxy counts per quartile, making the quoted quenched‑fraction difference difficult to verify. | 02 |
| | M‑05 | **Terminology clash** – Paper 04 uses “high‑excitation optical AGN” which can be confused with radio‑mode HERGs; the definition should be clarified. | 04 |
| | M‑06 | **Figure/table captions are placeholders** – Figures fig‑topic.pdf in Papers 02‑09 contain generic captions (“Figure X shows …”) with no axis labels, units, or key numeric legends. | 02‑09 |
| **Minor** | m‑01 | **Missing software citation** – the `\software{}` macro is not used for Tectonic, Astropy, etc. | All |
| | m‑02 | **SDSS acknowledgment block incomplete** – the standard acknowledgment template is missing the “Funding for the SDSS” paragraph. | All |
| | m‑03 | **“Broad AGN” wording** – the phrase “broad optical AGN” in Paper 01 could be interpreted as spectroscopic broad‑line AGN; add “BPT‑selected” qualifier. | 01 |
| | m‑04 | **Aperture‐effect caveat** – Paper 08 reports Hα luminosity proxy without noting the fiber aperture correction; add brief note. | 08 |
| | m‑05 | **Typo in bibliography** – Paper 09 still carries the “Dubrois” → “Dubois” typo in two entries (already fixed in a prior cycle, but worth double‑checking). | 09 |
| **Improvement** | i‑01 | **Add a “Data Availability” section** – even if data are local, stating the repository path (e.g., Zenodo DOI) will aid future reuse. | All |
| | i‑02 | **Streamline “Conclusion” language** – many papers end with a single‑sentence “future work” paragraph; expand to a 2‑sentence summary of key take‑aways and limitations. | All |

*No blocker‑level *technical* errors (e.g., compilation failures) were found.*

---

### 4. Exact Feed for PDF‑Writing Pilot (TeX‑level edit guidance)

Below are **safe, non‑inventive** edit blocks that preserve measured values and real‑data boundaries. Apply these edits in the candidate‑copy TeX files (the integrator will handle the actual file modifications).

#### A. Add Data‑Availability Section (all papers)

```tex
% Insert after \section{Conclusions} (or at the end of the manuscript)
\section{Data Availability}
The SDSS‑DR17 emission‑line catalog and the derived 60\,000‑galaxy (or 6\,729‑galaxy for Paper 08) subsets used in this work are available in the NebulaMind data repository at
\url{https://doi.org/10.5281/zenodo.XXXXXXX}.
All**OVERNIGHT_GPTOSS_SKEPTIC_CYCLE_09**  

---

### 1. Status  
**ISSUES_FOUND** – the candidate PDFs compile cleanly, but a number of scientific‑communication, citation‑role, and reproducibility concerns were identified that should be addressed before the PDF‑writing pilot proceeds.

---

### 2. Files Inspected  

| Paper | TeX (linked) | PDF (linked) |
|-------|--------------|--------------|
| 01 m1 rp1 sdss agn sfr | [m1_rp1_sdss_agn_sfr_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex) | [m1_rp1_sdss_agn_sfr_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf) |
| 02 m1 rp2 environment quenching | [m1_rp2_environment_quenching_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex) | [m1_rp2_environment_quenching_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf) |
| 03 m1 rp3 maintenance heating | [m1_rp3_maintenance_heating_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex) | [m1_rp3_maintenance_heating_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf) |
| 04 m2 p1 outflow escape recycling | [m2_p1_outflow_escape_recycling_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex) | [m2_p1_outflow_escape_recycling_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf) |
| 05 m2 p2 radio jet environment | [m2_p2_radio_jet_environment_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex) | [m2_p2_radio_jet_environment_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf) |
| 06 m2 p3 feedback transition mass | [m2_p3_feedback_transition_mass_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex) | [m2_p3_feedback_transition_mass_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf) |
| 07 m3 p1 multiphase census | [m3_p1_multiphase_census_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex) | [m3_p1_multiphase_census_integrated.pdf](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-a
[TRUNCATED at 16000 chars: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/lanes/gptoss_skeptic/GPTOSS_SKEPTIC_CYCLE_09.md]


===== hwao_director (Gemini 3.1 Pro (Low)) exit=0 =====
# hwao_director cycle 9
Started UTC: 2026-07-09T19:38:45Z
Model: Gemini 3.1 Pro (Low)
Provider: agy
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_09_hwao_director.md

I have critically reviewed the 9 candidate PDFs/manuscript TeX files and evaluated the current state of the issues identified in previous cycles. I have generated the Cycle 09 report and saved it as an artifact: [OVERNIGHT_HWAO_DIRECTOR_CYCLE_09.md](file:///Users/duhokim/.gemini/antigravity-cli/brain/21899e86-13f2-432c-aa56-32d532c1258d/OVERNIGHT_HWAO_DIRECTOR_CYCLE_09.md). 

Here is the exact requested output:

# OVERNIGHT_HWAO_DIRECTOR_CYCLE_09

## 1. OVERNIGHT_HWAO_DIRECTOR_CYCLE_09 status
**ISSUES_FOUND**

## 2. Files/paths actually inspected
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers`
- Checked specifically:
  - `01_m1_rp1_sdss_agn_sfr_integrated.tex`
  - `02_m1_rp2_environment_quenching_integrated.tex`
  - `06_m2_p3_feedback_transition_mass_integrated.tex`
  - `08_m3_p2_gas_depletion_efficiency_integrated.tex`
  - `09_m3_p3_simulation_validation_integrated.tex`
- Evaluated `grep_search` results across all 9 TeX files.

## 3. Ranked findings
- **Major**: Stub Figure Captions (Papers 02-09). The `\caption{}` block for `fig-topic.pdf` in Papers 02-09 still contains generic stub text ("The figure summarizes the cached optical result used for target definition") and lacks any axis descriptions or key numbers.
- **Major**: Unlinked Sub-sample in Selection Table (Paper 08 and others). The shared selection cascade table lists the 60,000 rows but fails to show the final sub-branch count (e.g., the 6,729-galaxy transition branch in Paper 08).
- **Major**: Unexplained Equal-Count Quartiles (Paper 02). The text cites a high-density quartile of 3,456/15,000 but never explicitly states that the 60,000 subset was divided into four equal-count 15,000-galaxy bins based on the density proxy.
- **Major**: Ambiguous High-Mass Tail (Paper 06). The phrase $\log(M_\star/M_\odot)>11.0$ remains an open upper bound without mentioning the specific $N$ count of galaxies in that bin or adding a sampling-noise caveat.

## 4. Exact feed for PDF-writing pilot
The PDF-writing pilot should apply the following safe TeX-level edits, preserving all measured values:

**Edit A: Fix Stub Figure Captions (Apply to Papers 02-09)**
*Instruct the PDF-writer to add paper-specific axes and exact median numbers.*
```latex
% Replace:
\caption{SDSS DR17 optical denominator/proxy diagnostic for the [topic]. The figure summarizes the cached optical result used for target definition.}
% With:
\caption{SDSS DR17 optical denominator/proxy diagnostic for the [topic]. The figure illustrates the distribution of the [N]-galaxy subset, including axis boundaries and key values ([e.g. -0.66 dex]) used for target definition.}
```

**Edit B: Paper 08 Selection Table Linkage**
```latex
% In 08_m3_p2_gas_depletion_efficiency_integrated.tex
% Replace:
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
% With:
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies. Note: This specific analysis further sub-selects a 6,729-galaxy branch of massive transition/quenched galaxies from the final 60,000 cached rows.}
```

**Edit C: Paper 02 Quartile Construction**
```latex
% In 02_m1_rp2_environment_quenching_integrated.tex
% Replace:
\item The high-density quartile has quenched fraction 0.230 \(\pm\) 0.003 (3,456/15,000); the low-density quartile has 0.181 \(\pm\) 0.003 (2,710/15,000).
% With:
\item The 60,000-galaxy subset was divided into four equal-count density quartiles of 15,000 galaxies each based on the 10th-nearest-neighbor proxy. The high-density quartile has quenched fraction 0.230 \(\pm\) 0.003 (3,456/15,000); the low-density quartile has 0.181 \(\pm\) 0.003 (2,710/15,000).
```

**Edit D: Paper 06 High-Mass Tail Caveat**
```latex
% In 06_m2_p3_feedback_transition_mass_integrated.tex
% Replace:
\item The first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail, defined here as $\log(M_\star/M_\odot)>11.0$.
% With:
\item The first stellar-mass bin with quenched fraction above 0.5 is the open high-mass tail, defined here as $\log(M_\star/M_\odot)>11.0$ (an open upper bound subject to low-$N$ sampling noise at the extreme).
```

## 5. Real-data/source/citation audit notes
- **Provenance verified:** No mock or hallucinated data were detected.
- The quantitative claims (offsets of $-1.309$ dex, fractions of $0.549$) trace directly to local data analysis and match the context correctly.
- The iMaNGA citation in Paper 09 was correctly updated in the latest compile to label it an observational catalog rather than a simulation suite.
- RP-1 remains safely restricted to an association-only claim.

## 6. Workflow/system notes
- Fixes identified in Cycle 8 for M-1, M-3, M-4, and M-7 did not persist or were not applied to the Cycle 9 candidate TeX files. The PDF-writing integrator must be explicitly prompted to ingest these rewrite blocks in the next cycle to ensure the structural updates stick.

## 7. Safety ledger
- **No edits made:** Read-only mode explicitly maintained.
- **No public/live frontend or static root edits:** Confirmed.
- **No DB, SQL, API, wiki publish, or data mutation:** Confirmed.
- **No deploy/restart:** Confirmed.
- **No git commit/push/merge/rebase/history rewrite:** Confirmed.
- **No cron creation/update/removal:** Confirmed.
- **No billing/cloud/OAuth/API-key/credential changes or reads:** Confirmed.
- **No external manuscript submission:** Confirmed.


# command_result
exit_code=0
elapsed_s=93.9
timed_out=False
finished_utc=2026-07-09T19:40:19Z


===== workflow_scrutiny (Gemini 3.5 Flash (Medium)) exit=0 =====
# workflow_scrutiny cycle 9
Started UTC: 2026-07-09T19:39:32Z
Model: Gemini 3.5 Flash (Medium)
Provider: agy
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_09_workflow_scrutiny.md

# Workflow Scrutiny and Pipeline Improvement Report

**Output Marker:** `OVERNIGHT_WORKFLOW_SCRUTINY_CYCLE_09`

---

## 1. OVERNIGHT_WORKFLOW_SCRUTINY_CYCLE_09 status
**Status:** `ISSUES_FOUND`

**Summary:**
While the local candidate package compiles successfully (`9/9 ok=True`), multiple critical process, system, and manuscript-level findings remain or have been newly identified. These findings span hardcoded timestamped directories in the React frontend, missing automated candidate-promotion gates resulting in stale public PDFs, duplication of research topic maps across method workspaces, figure filename collisions, and verbatim section duplication that poses a self-plagiarism hazard.

---

## 2. Files/paths actually inspected or used from context
The following files and paths were analyzed:
1. **Local Candidate Package (Cycle 9):**
   - [candidates/cycle_09_nine_papers/](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers)
   - [01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex) (Lines 1-100)
   - [02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex) (Lines 50-98)
   - [08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex) (Lines 1-98)
   - [09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex) (Lines 50-99)
2. **Public Method Wiki Directories (Read-Only):**
   - [Method 1 PGR Research Topic Map](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json)
   - [Method 1 PGR Manifest](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json)
   - [Galaxy Evolution Wiki Index](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/index.html) (Lines 1-30)
3. **Frontend Source Code:**
   - [IdeasIndexClient.tsx](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/src/app/ideas/IdeasIndexClient.tsx) (Lines 1-377)
4. **Orchestrator, Logs & Lane Results:**
   - [run_overnight_pdf_and_workflow_swarm.py](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/run_overnight_pdf_and_workflow_swarm.py) (Lines 1-692)
   - [CYCLE_08_OVERNIGHT_INTEGRATOR_RESPONSE.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_08_nine_papers/CYCLE_08_OVERNIGHT_INTEGRATOR_RESPONSE.md) (Lines 1-64)
   - [OVERNIGHT_CLAUDE_LANA_MANUSCRIPT_CYCLE_08.md](file:///Users/duhokim/.gemini/antigravity-cli/brain/7a90dd20-0115-4508-96f4-3a0d86412e79/OVERNIGHT_CLAUDE_LANA_MANUSCRIPT_CYCLE_08.md) (Lines 1-655)
   - [WORKFLOW_SCRUTINY_CYCLE_08.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/lanes/workflow_scrutiny/WORKFLOW_SCRUTINY_CYCLE_08.md) (Lines 1-250)

---

## 3. Ranked findings, with severity

### Finding 1: Swarm Orchestrator Report Truncation Bug
* **Severity:** `MAJOR`
* **Description:** In `run_overnight_pdf_and_workflow_swarm.py` line 437, the orchestrator script calls `collect_lane_texts(lane_results, 16000)`, truncating subagent logs at 16,000 characters.
* **Impact:** High risk of data loss. Critical findings from reviewer lanes (such as Claude Sonnet or Gemini Pro lanes) are silently dropped before reaching the integrator. For instance, the instruction to add the 6,729-galaxy row in Paper 08's selection table was not integrated in cycle 8 because it was truncated.
* **Remedy:** Remove the 16,000-character limit or increase it to 100,000 characters in `run_overnight_pdf_and_workflow_swarm.py` to leverage modern model context capacities.

### Finding 2: Hardcoded Timestamped Directories in Frontend
* **Severity:** `MAJOR`
* **Description:** The React component `IdeasIndexClient.tsx` hardcodes the directory timestamp `research-topics-from-wiki-20260708T090359Z` in multiple file paths.
* **Impact:** Re-generating the topics from the wiki generates a new timestamped folder, breaking all frontend links until a developer manually updates the React client code.
* **Remedy:** Load dynamic paths via a manifest or configuration file, or establish a symlink (`research-topics-latest`) that frontend components can reference.

### Finding 3: Stale Public PDFs & Missing Automated Promotion Gate
* **Severity:** `MAJOR`
* **Description:** Although the overnight swarm successfully compiles candidate PDFs with numerous refinements across cycles (such as typo fixes and layout tweaks), the public-facing links under `/agent-reports/wiki-method-results/galaxy-evolution/` still serve outdated PDFs from July 8th. The pipeline lacks an automated mechanism to promote verified candidates to production.
* **Impact:** Public users are served stale documents, undermining the quality improvements achieved in the candidate package.
* **Remedy:** Implement an automated gate script (`promote_candidates.py`) that matches names and copies verified candidates to the frontend public folders after the run completes successfully.

### Finding 4: Verbatim Text Duplication and Missing Paper-Specific Linkage in Section 2 and Selection Cascade Table (Self-Plagiarism Hazard)
* **Severity:** `MAJOR`
* **Description:** Section 2 (`Data and Sample Selection`) and the accompanying Table 1 are 100% verbatim identical across Papers 02 through 09. Specifically, Paper 08 uses a restricted subset of 6,729 massive quenched/transitioning galaxies rather than the 60,000 shared parent cache, but its cascade table does not show this branch, which misleads the reader.
* **Impact:** High risk of rejection for self-plagiarism in simultaneous journal submissions, and transparency issues.
* **Remedy:** Inject paper-specific opening sentences in Section 2 pointing to the shared parent sample selection described in the master pilot (Paper 01), and add the paper-specific branch row (e.g., the 6,729 massive low-sSFR cut for Paper 08) directly in Table 1.

### Finding 5: Figure Filename Collision Risk
* **Severity:** `MAJOR`
* **Description:** All secondary papers reference `\includegraphics{../figures/fig-topic.pdf}`. Although the physical files differ, using the identical file name complicates build automation, asset tracking, and package compilation.
* **Impact:** Workflow fragility and packaging collisions.
* **Remedy:** Rename files locally (e.g., `fig-paper02-density.pdf`, `fig-paper08-depletion.pdf`) and update TeX calls.

### Finding 6: Duplicated Research Topic Maps across Methods
* **Severity:** `MAJOR`
* **Description:** The file `research-topic-map-20260708T090359Z.json` is duplicated identically across Method 1, Method 2, and Method 3 subdirectories.
* **Impact:** High risk of drift. Updates to hypotheses or schemas must be manually applied to three places, which is error-prone.
* **Remedy:** Move the topic map to a single shared directory (e.g., `galaxy-evolution/shared/`) and configure method scripts to read from that shared location.

### Finding 7: Flagship Asset Path Mismatch (RP-1)
* **Severity:** `MINOR`
* **Description:** In `IdeasIndexClient.tsx`, the SDSS AGN/SFR pilot (RP-1) is linked to a path inside the Method 2 (SFA) directory, though it belongs to Method 1.
* **Impact:** Confuses developers and breaks folder semantic boundaries.
* **Remedy:** Create a shared assets directory `galaxy-evolution/shared/` for common files.

### Finding 8: Naming Mismatch in Compiled PDFs vs Wiki Links
* **Severity:** `MINOR`
* **Description:** The research topics markdown (`research-topics-from-wiki-20260708T090359Z.md`) maps files as `*_aas.pdf`, but the compile output produces `*_integrated.pdf`.
* **Impact:** Promoted candidates will have broken links on public route indexes unless manually renamed.
* **Remedy:** Standardize names across the compilation orchestrator and wiki generator.

### Finding 9: Stale "Research-Topic Page" Phrasing in Interpretation/Missing Observables
* **Severity:** `MINOR`
* **Description:** Papers 03–09 still include text referencing "the additional survey data named in the research-topic page" which represents an unresolved system dependency.
* **Impact:** Confuses readers about standalone manuscript completeness.
* **Remedy:** Rephrase to explicitly name required physical datasets (e.g. CO/dust molecular gas masses, X-ray cavity measurements, radio jet powers) instead of mentioning the topic page.

---

## 4. Exact feed for PDF-writing pilot

To resolve these findings in the next integration cycle, apply the following exact modifications:

### 4.1. Paper 08 (`08_m3_p2_gas_depletion_efficiency`)
* **Selection Table Subset Row Insertion (Section 2, Table 1):**
  Add this row immediately after the "four BPT lines S/N$\geq 3$" row (line 33):
  ```tex
  massive ($\log M_\star \geq 10.8$) + low-sSFR/transitioning & -- & 6{,}729 & -- \\
  ```
  And add below the table (after `\tablecomments`):
  ```tex
  The paper-specific denominator of 6{,}729 galaxies applies an additional
  stellar-mass threshold ($\log M_\star / M_\odot \geq 10.8$) plus a
  low-sSFR/transitioning classification; it is a subset of the shared
  60{,}000-galaxy cache.
  ```

### 4.2. Papers 02–09 (Section 2 Selection & Figures)
* **Citation Intro Insertion (Section 2):**
  Inject unique framing sentences at the start of Section 2:
  - **Paper 02:** `The parent sample selection for this analysis follows the identical selection cascade detailed in Paper 01 \citep[see also][]{sdssdr17}, modified here to focus on density quartiles as an environmental quenching baseline rather than a feedback or outflow sample.`
  - **Paper 03:** `The parent sample selection for this analysis follows the identical selection cascade detailed in Paper 01 \citep[see also][]{sdssdr17}, modified here to focus on BPT AGN fractions as a maintenance-heating baseline in massive, low-sSFR hosts.`
  - **Paper 04:** `The parent sample selection for this analysis follows the identical selection cascade detailed in Paper 01 \citep[see also][]{sdssdr17}, modified here to focus on high-excitation optical AGN candidates as a baseline for future resolved outflow kinematics.`
  - **Paper 05:** `The parent sample selection for this analysis follows the identical selection cascade detailed in Paper 01 \citep[see also][]{sdssdr17}, modified here to focus on local environment stratification in massive hosts for future radio-jet coupling work.`
  - **Paper 06:** `The parent sample selection for this analysis follows the identical selection cascade detailed in Paper 01 \citep[see also][]{sdssdr17}, modified here to focus on transition stellar-mass boundaries between quenching and AGN incidence.`
  - **Paper 07:** `The parent sample selection for this analysis follows the identical selection cascade detailed in Paper 01 \citep[see also][]{sdssdr17}, modified here to establish a common denominator for multiphase outflow census.`
  - **Paper 08:** `The parent sample selection for this analysis follows the identical selection cascade detailed in Paper 01 \citep[see also][]{sdssdr17}, modified here to focus on transition-galaxy targets for future molecular gas-fraction and efficiency follow-up.`
  - **Paper 09:** `The parent sample selection for this analysis follows the identical selection cascade detailed in Paper 01 \citep[see also][]{sdssdr17}, modified here to define the observed target vector grid for simulation validation.`

* **Figure Reference Renaming:**
  Update the `\includegraphics` commands in Papers 02–09 to point to unique file names rather than the generic `fig-topic.pdf`.
  - **Paper 02:** `\includegraphics[width=\columnwidth]{../figures/fig-paper02-density.pdf}`
  - **Paper 03:** `\includegraphics[width=\columnwidth]{../figures/fig-paper03-maintenance.pdf}`
  - **Paper 04:** `\includegraphics[width=\columnwidth]{../figures/fig-paper04-outflow.pdf}`
  - **Paper 05:** `\includegraphics[width=\columnwidth]{../figures/fig-paper05-radiojet.pdf}`
  - **Paper 06:** `\includegraphics[width=\columnwidth]{../figures/fig-paper06-transition.pdf}`
  - **Paper 07:** `\includegraphics[width=\columnwidth]{../figures/fig-paper07-multiphase.pdf}`
  - **Paper 08:** `\includegraphics[width=\columnwidth]{../figures/fig-paper08-depletion.pdf}`
  - **Paper 09:** `\includegraphics[width=\columnwidth]{../figures/fig-paper09-validation.pdf}`

### 4.3. Standard AAS Acknowledgment and Software Commands (All 9 Papers)
* **Standard SDSS Acknowledgment Boilerplate:**
  Add this standard text after `\acknowledgments`:
  ```tex
  Funding for SDSS has been provided by the Alfred P.\ Sloan Foundation,
  the U.S.\ Department of Energy Office of Science, and the Participating Institutions.
  SDSS acknowledges support and resources from the Center for High-Performance Computing
  at the University of Utah. The SDSS web site is \url{www.sdss.org}.
  This manuscript uses public SDSS DR17 data only.
  ```
* **Standard `\software{}` Command:**
  Add this standard text after `\acknowledgments`:
  ```tex
  \software{Python \citep{python}, Astropy \citep{astropy}, Matplotlib \citep{matplotlib}, SciPy \citep{scipy}}
  ```

---

## 5. Real-data/source/citation audit notes
- **Data Provenance:** Quoted numbers (such as median sSFR offset of $-1.309$ dex, $N=8,146$ matched pairs, and Paper 08 AGN fraction of $0.549 \pm 0.006$) map correctly to the SDSS DR17 spectroscopic sample metrics.
- **Mock Data Scan:** No placeholders or toy datasets were detected in any candidates.
- **Citation Roles:** Standard references (Baldwin 1981, Kewley 2001, Kauffmann 2003, York 2000, Best 2005) are physically grounded. The Brinchmann 2004 reference has been explicitly contextualized for AGN limitations.
- **Preprint Status Check:** Preprints cited (Goubert 2024 `arXiv:2401.12953`, Eckert 2024 `arXiv:2403.17145`) should be checked for publication status before final submission and updated wi
[TRUNCATED at 16000 chars: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/lanes/workflow_scrutiny/WORKFLOW_SCRUTINY_CYCLE_09.md]

