# codex_kun_repro cycle 6
Started UTC: 2026-07-09T18:35:01Z
Model: gpt-5.4-mini
Provider: codex
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_06_codex_kun_repro.md

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
session id: 019f4829-688f-7cd1-939a-6c76cb1b4acf
--------
user
Kun/Codex read-only reproducibility, TeX, provenance, and no-mock-data audit.

Output marker: OVERNIGHT_CODEX_KUN_REPRO_CYCLE_06

Work mode: artifact-only, read-only lane. Do not edit files. Do not publish. Do not call or request credentials.

Critically review the 9 current candidate PDFs/manuscript TeX files and the public-linked research-topic manuscripts. Find the highest-value issues that should feed the candidate-copy PDF-writing pilot: overclaims, missing caveats, weak abstracts, confusing conclusion/limitations wording, citation role errors, stale public-vs-local mismatch, poor reader flow, figure/table/caption problems, and reproducibility risks. Give exact safe rewrite guidance where possible, but do not edit files.

Required output sections:
1. OVERNIGHT_CODEX_KUN_REPRO_CYCLE_06 status: PASS/ISSUES_FOUND/BLOCKED.
2. Files/paths actually inspected or, if not inspectable, paths used from context.
3. Ranked findings, with severity: blocker/major/minor/improvement.
4. Exact feed for PDF-writing pilot: concrete TeX-level edits or section rewrite instructions, preserving measured values and real-data boundaries.
5. Real-data/source/citation audit notes.
6. Workflow/system notes if relevant.
7. Safety ledger confirming no edits/public/db/deploy/git/cron/billing/OAuth/submission.

Run root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z
Cycle: 6
Candidate package: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers
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
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 227902,
    "pdf_sha256": "ff25d074ad2a0514ce86a33e5f61ebc61b86ba2ccdff0ca58b9fa49caac5ba3d",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 81690,
    "pdf_sha256": "f26d4eb9e5d4ee8b6c403f278c63fa530d786bdddb17ddaef76c1ac6acf6afd8",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 82272,
    "pdf_sha256": "825fd3981536c4dcf018b858945c35c2ca8868dc70e8537349220998c116ba35",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 310589,
    "pdf_sha256": "a4eba5d8ac71e576f4dc8536eb7cfe5bec08082e2fa86515eeb785b5ecf76919",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 81507,
    "pdf_sha256": "8bd52806af3bfdea9303a14c4ad72a80462f3c3c44331854508713515af4ef77",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 81086,
    "pdf_sha256": "d664109336e4612c07bccae7b691dab3288a5b4fa4b8127c50bad9fc3a320081",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 81468,
    "pdf_sha256": "9b48e5545c92fb4cd2a8b52dfce01547c1192f2fe18b9d7b84587a5ae88e94e2",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 206641,
    "pdf_sha256": "acaa0ac340beed75db3ae5b3a2070cbfd60311837d556fa405aa98e8cb9f7b4d",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 82290,
    "pdf_sha256": "b1ebacd23e28dc18fa4c8e4fb0388ac1fcc5792c647eadd7e89b6c59b0635206",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle

Deterministic inventory summary:
{
  "candidate_papers": [
    {
      "slug": "01_m1_rp1_sdss_agn_sfr",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
      "title": "Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot",
      "abstract": "We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad BPT optical AGN hosts and star-forming controls from the cached SDSS DR17 emission-line subset. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\\Delta\\log {\\rm sSFR}=-1.309$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.",
      "tex_sha256": "25faefa03decafeeb44b0b914d6d24b9d29cb24501756d2d63ac3ad0a0571a86",
      "pdf_sha256": "ff25d074ad2a0514ce86a33e5f61ebc61b86ba2ccdff0ca58b9fa49caac5ba3d",
      "pdf_bytes": 227902
    },
    {
      "slug": "02_m1_rp2_environment_quenching",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
      "title": "SDSS density proxy for environmental quenching",
      "abstract": "We use the cached SDSS DR17 emission-line subset to build an optical density-proxy analysis of environmental quenching across a 60,000-galaxy sample. A 10th-nearest-neighbor density proxy is compared with quenched fraction after controlling for stellar mass and redshift; the high-density quartile has quenched fraction 0.230 versus 0.181 in the low-density quartile. This analysis is intentionally limited to the optical denominator and treats the missing group and halo information as a future-data requirement.",
      "tex_sha256": "61ef52161a3f2b74280102823061c1c1f8f40aa14db38296764356130844f4fe",
      "pdf_sha256": "f26d4eb9e5d4ee8b6c403f278c63fa530d786bdddb17ddaef76c1ac6acf6afd8",
      "pdf_bytes": 81690
    },
    {
      "slug": "03_m1_rp3_maintenance_heating",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
      "title": "Optical-AGN denominator for maintenance-heating follow-up",
      "abstract": "We use the cached SDSS DR17 emission-line subset to construct an optical denominator for maintenance-heating follow-up in massive galaxies. Among massive, low-sSFR hosts, we measure the available BPT-AGN fraction as a proxy for the duty-cycle denominator relevant to future X-ray or radio maintenance-heating studies. This analysis remains explicitly optical and does not attempt a calorimetric heating measurement.",
      "tex_sha256": "e0390aa08ad366da58551460a972fd18555439c82bd0459f53fcf12d351e3ec3",
      "pdf_sha256": "825fd3981536c4dcf018b858945c35c2ca8868dc70e8537349220998c116ba35",
      "pdf_bytes": 82272
    },
    {
      "slug": "04_m2_p1_outflow_escape_recycling",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
      "title": "SDSS high-excitation AGN denominator for outflow escape tests",
      "abstract": "We use the cached SDSS DR17 emission-line subset to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts high-excitation optical AGN candidates and records their median sSFR as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.",
      "tex_sha256": "266219b60d41afd6ad85d47aecf59e8d9e136cc7d34cd440214bb6aeb5d1928f",
      "pdf_sha256": "a4eba5d8ac71e576f4dc8536eb7cfe5bec08082e2fa86515eeb785b5ecf76919",
      "pdf_bytes": 310589
    },
    {
      "slug": "05_m2_p2_radio_jet_environment",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf",
      "title": "Environment proxy for optical AGN in massive SDSS hosts",
      "abstract": "We build an optical denominator for radio-jet environment follow-up using the cached SDSS DR17 emission-line subset. In massive hosts, we compare the high- and low-density quartiles of the optical AGN fraction to identify an environment-stratified target set for later radio or X-ray work. The result is an optical baseline only; it does not measure jet power or coupling efficiency.",
      "tex_sha256": "9fd41c1e8e9915969054177daf5252fd35e46a307574dbdc027bd6080914bf84",
      "pdf_sha256": "8bd52806af3bfdea9303a14c4ad72a80462f3c3c44331854508713515af4ef77",
      "pdf_bytes": 81507
    },
    {
      "slug": "06_m2_p3_feedback_transition_mass",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf",
      "title": "SDSS mass transition in quenching and optical AGN incidence",
      "abstract": "We use the cached SDSS DR17 emission-line subset to identify the stellar-mass regime where quenched fraction and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, but it does not assign the transition to stellar or AGN feedback on its own.",
      "tex_sha256": "1c4427ffc7141fa7e51d2b14c91a605b86d76d3e9c2c04aa52e65c418869be30",
      "pdf_sha256": "d664109336e4612c07bccae7b691dab3288a5b4fa4b8127c50bad9fc3a320081",
      "pdf_bytes": 81086
    },
    {
      "slug": "07_m3_p1_multiphase_census",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf",
      "title": "Common-denominator optical tracer census in SDSS",
      "abstract": "We build a common optical denominator for a multiphase outflow census from the cached SDSS DR17 emission-line subset. Simple tracer definitions change the inferred AGN or feedback-candidate prevalence within the same denominator, so the draft focuses on the optical selection baseline needed before adding ionized, neutral, molecular, or X-ray/radio tracers. This is a denominator study, not a multiphase outflow measurement.",
      "tex_sha256": "1e5fb63d3581a0d4b4a68ec77b239a2258a6c49654d663b85f1d4e8a563400a1",
      "pdf_sha256": "9b48e5545c92fb4cd2a8b52dfce01547c1192f2fe18b9d7b84587a5ae88e94e2",
      "pdf_bytes": 81468
    },
    {
      "slug": "08_m3_p2_gas_depletion_efficiency",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf",
      "title": "Optical denominator for gas-fraction versus efficiency tests",
      "abstract": "We use the cached SDSS DR17 emission-line subset to construct an optical selection baseline and denominator for future molecular gas-fraction versus star-formation efficiency follow-up. For a sample of 6,729 massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of 0.549 and a median log H$\\alpha$ luminosity proxy of 40.06 erg s$^{-1}$, which is offset by $-0.66$ dex relative to massive star-forming controls. The analysis provides the empirical baseline necessary to identify targets for CO or dust follow-up without claiming a physical separation of gas depletion from efficiency suppression from optical data alone.",
      "tex_sha256": "7b010e7c1cb077e6b2aaa10eca1d628d2bb04ce393fd43e4389329e60e8bd158",
      "pdf_sha256": "acaa0ac340beed75db3ae5b3a2070cbfd60311837d556fa405aa98e8cb9f7b4d",
      "pdf_bytes": 206641
    },
    {
      "slug": "09_m3_p3_simulation_validation",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OV

Candidate paper summaries:
- slug=01_m1_rp1_sdss_agn_sfr
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf
  title=Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot
  abstract=We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad BPT optical AGN hosts and star-forming controls from the cached SDSS DR17 emission-line subset. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\Delta\log {\rm sSFR}=-1.309$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.
- slug=02_m1_rp2_environment_quenching
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf
  title=SDSS density proxy for environmental quenching
  abstract=We use the cached SDSS DR17 emission-line subset to build an optical density-proxy analysis of environmental quenching across a 60,000-galaxy sample. A 10th-nearest-neighbor density proxy is compared with quenched fraction after controlling for stellar mass and redshift; the high-density quartile has quenched fraction 0.230 versus 0.181 in the low-density quartile. This analysis is intentionally limited to the optical denominator and treats the missing group and halo information as a future-data requirement.
- slug=03_m1_rp3_maintenance_heating
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf
  title=Optical-AGN denominator for maintenance-heating follow-up
  abstract=We use the cached SDSS DR17 emission-line subset to construct an optical denominator for maintenance-heating follow-up in massive galaxies. Among massive, low-sSFR hosts, we measure the available BPT-AGN fraction as a proxy for the duty-cycle denominator relevant to future X-ray or radio maintenance-heating studies. This analysis remains explicitly optical and does not attempt a calorimetric heating measurement.
- slug=04_m2_p1_outflow_escape_recycling
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf
  title=SDSS high-excitation AGN denominator for outflow escape tests
  abstract=We use the cached SDSS DR17 emission-line subset to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts high-excitation optical AGN candidates and records their median sSFR as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
- slug=05_m2_p2_radio_jet_environment
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf
  title=Environment proxy for optical AGN in massive SDSS hosts
  abstract=We build an optical denominator for radio-jet environment follow-up using the cached SDSS DR17 emission-line subset. In massive hosts, we compare the high- and low-density quartiles of the optical AGN fraction to identify an environment-stratified target set for later radio or X-ray work. The result is an optical baseline only; it does not measure jet power or coupling efficiency.
- slug=06_m2_p3_feedback_transition_mass
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf
  title=SDSS mass transition in quenching and optical AGN incidence
  abstract=We use the cached SDSS DR17 emission-line subset to identify the stellar-mass regime where quenched fraction and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, but it does not assign the transition to stellar or AGN feedback on its own.
- slug=07_m3_p1_multiphase_census
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf
  title=Common-denominator optical tracer census in SDSS
  abstract=We build a common optical denominator for a multiphase outflow census from the cached SDSS DR17 emission-line subset. Simple tracer definitions change the inferred AGN or feedback-candidate prevalence within the same denominator, so the draft focuses on the optical selection baseline needed before adding ionized, neutral, molecular, or X-ray/radio tracers. This is a denominator study, not a multiphase outflow measurement.
- slug=08_m3_p2_gas_depletion_efficiency
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf
  title=Optical denominator for gas-fraction versus efficiency tests
  abstract=We use the cached SDSS DR17 emission-line subset to construct an optical selection baseline and denominator for future molecular gas-fraction versus star-formation efficiency follow-up. For a sample of 6,729 massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of 0.549 and a median log H$\alpha$ luminosity proxy of 40.06 erg s$^{-1}$, which is offset by $-0.66$ dex relative to massive star-forming controls. The analysis provides the empirical baseline necessary to identify targets for CO or dust follow-up without claiming a physical separation of gas depletion from efficiency suppression from optical data alone.
- slug=09_m3_p3_simulation_validation
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf
  title=SDSS target vector for feedback-model validation
  abstract=We use the cached SDSS DR17 emission-line subset to define a compact optical target vector for forward-model validation. The pilot records quenched fraction, optical AGN incidence, and color versus mass/redshift across cells with sufficient counts, providing an observed target vector for later simulation work. It remains an empirical denominator study rather than a direct simulation comparison.

Previous feed packet for continuity:
# PDF-writing feed cycle 5

created_utc: 2026-07-09T18:10:56Z
candidate: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers`

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
- `01_m1_rp1_sdss_agn_sfr` ok=True bytes=227653 sha256=8c2f674ea63066cdb9882b932aa3dff2ec2380b9da21cf7445eecc6cf99a07e2
- `02_m1_rp2_environment_quenching` ok=True bytes=80674 sha256=ab5c10c2b7b0c5f8bbff11b5a2d402b9143b659532e79209943ecf424daafb89
- `03_m1_rp3_maintenance_heating` ok=True bytes=81937 sha256=2ffeb3c8025a64bb3c7d07f287442cccc41ee20eae2bf6bb78a447972d6ed58e
- `04_m2_p1_outflow_escape_recycling` ok=True bytes=308088 sha256=ebab0559ed81b4cf566d47acefb8c5fee4d73e81ff0dd9ccb4de027e2fbd5d97
- `05_m2_p2_radio_jet_environment` ok=True bytes=80805 sha256=cb42f5cbddefe9fbaa765a10a932dfe51e3a27000b9c6b01be95d6e378440839
- `06_m2_p3_feedback_transition_mass` ok=True bytes=79766 sha256=5be63185892e62b5fb0952fa9dfaea28d031cdf87accd1fa501b12e4f0d9aed3
- `07_m3_p1_multiphase_census` ok=True bytes=80527 sha256=85167cfcf54de71f2591571760b91360662c5ff398c73158b16ba5383b226066
- `08_m3_p2_gas_depletion_efficiency` ok=True bytes=205857 sha256=52ab9fe8220ceb86b8598bc59d68d3f26b8184b91ae9db74983c8876798190ad
- `09_m3_p3_simulation_validation` ok=True bytes=81647 sha256=78c80d7107ed1c0cbaae0903ad8d525f7218e13eafb71457e9857aa5acc4919d

## Lane outputs to integrate

===== codex_kun_repro (gpt-5.4-mini) exit=0 =====
# codex_kun_repro cycle 5
Started UTC: 2026-07-09T18:06:48Z
Model: gpt-5.4-mini
Provider: codex
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_05_codex_kun_repro.md

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
session id: 019f480f-95ac-7221-a541-f3d0073dd906
--------
user
Kun/Codex read-only reproducibility, TeX, provenance, and no-mock-data audit.

Output marker: OVERNIGHT_CODEX_KUN_REPRO_CYCLE_05

Work mode: artifact-only, read-only lane. Do not edit files. Do not publish. Do not call or request credentials.

Critically review the 9 current candidate PDFs/manuscript TeX files and the public-linked research-topic manuscripts. Find the highest-value issues that should feed the candidate-copy PDF-writing pilot: overclaims, missing caveats, weak abstracts, confusing conclusion/limitations wording, citation role errors, stale public-vs-local mismatch, poor reader flow, figure/table/caption problems, and reproducibility risks. Give exact safe rewrite guidance where possible, but do not edit files.

Required output sections:
1. OVERNIGHT_CODEX_KUN_REPRO_CYCLE_05 status: PASS/ISSUES_FOUND/BLOCKED.
2. Files/paths actually inspected or, if not inspectable, paths used from context.
3. Ranked findings, with severity: blocker/major/minor/improvement.
4. Exact feed for PDF-writing pilot: concrete TeX-level edits or section rewrite instructions, preserving measured values and real-data boundaries.
5. Real-data/source/citation audit notes.
6. Workflow/system notes if relevant.
7. Safety ledger confirming no edits/public/db/deploy/git/cron/billing/OAuth/submission.

Run root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z
Cycle: 5
Candidate package: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers
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
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 227653,
    "pdf_sha256": "8c2f674ea63066cdb9882b932aa3dff2ec2380b9da21cf7445eecc6cf99a07e2",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 80674,
    "pdf_sha256": "ab5c10c2b7b0c5f8bbff11b5a2d402b9143b659532e79209943ecf424daafb89",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 81937,
    "pdf_sha256": "2ffeb3c8025a64bb3c7d07f287442cccc41ee20eae2bf6bb78a447972d6ed58e",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 308088,
    "pdf_sha256": "ebab0559ed81b4cf566d47acefb8c5fee4d73e81ff0dd9ccb4de027e2fbd5d97",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 80805,
    "pdf_sha256": "cb42f5cbddefe9fbaa765a10a932dfe51e3a27000b9c6b01be95d6e378440839",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 79766,
    "pdf_sha256": "5be63185892e62b5fb0952fa9dfaea28d031cdf87accd1fa501b12e4f0d9aed3",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 80527,
    "pdf_sha256": "85167cfcf54de71f2591571760b91360662c5ff398c73158b16ba5383b226066",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 205857,
    "pdf_sha256": "52ab9fe8220ceb86b8598bc59d68d3f26b8184b91ae9db74983c8876798190ad",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/Neb
[TRUNCATED at 16000 chars: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/feeds/PDF_WRITING_FEED_CYCLE_05.md]


Relevant handoff excerpts:
# Final post-fix handoff: 9 publishable Galaxy Evolution PDFs

Run ID: `PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z`

## Result

Gemini Deep Research final verdict: `DEEP_RESEARCH_PASS: YES`.

The 9 local candidate PDFs are publishable under the conservative NebulaMind/AAS-style standard:

- RP-1 remains an association-only flagship short paper.
- Papers 2-9 remain honest SDSS optical denominator/proxy data notes, not causal feedback papers.
- No blocker, major, or minor issues remain after the final typo fix.
- No mock, synthetic, fake, placeholder, or toy data were accepted.
- No invented values or citations were accepted.

## What happened

1. Copied the integrated 9-paper source package into a local candidate package.
2. Compiled all 9 PDFs with Tectonic.
3. Ran Gemini Deep Research publication-gate review.
4. Gemini returned `DEEP_RESEARCH_PASS: YES` and identified one minor typo in Paper 09: `Dubrois` should be `Dubois` in two bibliography display labels.
5. Patched only the local candidate TeX file for Paper 09.
6. Recompiled all 9 PDFs.
7. Re-ran Gemini Deep Research final review.
8. Gemini returned `DEEP_RESEARCH_PASS: YES` with no blocker, major, or minor issues remaining.

## Candidate root

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers`

## Final review receipts

- First Deep Research review: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/lanes/gemini_deep_research/PUBLISHABLE_9PDF_GEMINI_DEEP_RESEARCH_CYCLE_01.md`
- Final post-fix Deep Research review: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/lanes/gemini_deep_research/FINAL_GEMINI_DEEP_RESEARCH_POST_MINOR_FIX.md`
- Final compile receipt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers/FINAL_POST_MINOR_FIX_COMPILE_RECEIPT.json`

## Final PDFs

1. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf`
2. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf`
3. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf`
4. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf`
5. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf`
6. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf`
7. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf`
8. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf`
9. `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf`

## Safety ledger

- Public-linked PDFs replaced: 0
- Public/live roots touched: 0
- DB/API/wiki/trust writes: 0
- Deploy/restart: 0
- Git commit/push/merge/rebase: 0
- Cron changes: 0
- Billing/cloud/OAuth/account changes: 0
- External manuscript submission: 0

These are local publishable candidates only. Promotion to public-linked PDFs remains a separate explicit approval gate.


codex
I’m tracing the 9 candidate TeX/PDFs against the public-linked manuscript set and the prior handoff so I can isolate only the highest-value risks for the PDF-writing pilot. First pass is inventory plus targeted reads for abstract/conclusion/caption/citation sections, then I’ll rank issues and extract concrete rewrite instructions without touching files.
exec
/bin/zsh -lc "rg --files /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers | sed -n '1,220p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/SOURCE_COPY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/CYCLE_06_BEFORE_RECEIPT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/CYCLE_06_BEFORE_RECEIPT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf

exec
/bin/zsh -lc "rg --files /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution | sed -n '1,220p'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "rg --files /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution | sed -n '1,220p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/prose-evidence-trust-deepening-20260708T043427Z/cross-method-trust-legend-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/prose-evidence-trust-deepening-20260708T043427Z/cross-method-coverage-map-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/prose-evidence-trust-deepening-20260708T043427Z/manifest-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/prose-evidence-trust-deepening-20260708T043427Z/index-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/tori-sfa.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/hwao-sfa.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/goru-sfa.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/kun-sfa.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/lana-sfa.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/manifest-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-deepening-map-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/page-content-m2-v2-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-v2-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/manifest.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-sections.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-no-go-gap-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-pages.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger-summary.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/quintet.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger-summary.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-review-checklist.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-packet.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/wiki-format-preview-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/evidence-trust-map-20260708T014205Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/manifest.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/page-content-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-summary.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-preserved-no-go-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-pdf-link-20260708T214200Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p1_outflow_escape_recycling_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md.backup-before-pdf-link-20260708T214200Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p2_radio_jet_environment_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p3_feedback_transition_mass_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-primary-citation-anchor-registry.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-citation-role-mappings.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/index.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/goru-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/kun-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/tori-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/hwao-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/lana-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/lana-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/tori-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/hwao-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/goru-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/kun-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/m3-p2-same-format-draft-20260707T050500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/manifest.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/manifest-20260708T014205Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-bindings-20260708T014205Z.md.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-p1-label-fix-20260708T022147Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html.backup-before-p1-spec-20260706T101547Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p5-2931-dedupe-spec-20260706T151025Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json.backup-before-p1-spec-20260706T101547Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-hwao-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/REVIEW_PATCH_NOTE_v2p1_20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-hwao-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-hwao-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p5-2931-dedupe-spec-20260706T151025Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p1-legacy-overclaim-disposition-spec.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p5-2931-dedupe-spec-20260706T151025Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/quintet.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/m1_rp2_environment_quenching_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-pdf-link-20260708T214200Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md.backup-before-pdf-link-20260708T214200Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/m1_rp3_maintenance_heating_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/quintet.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-pdf-link-20260708T214200Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/wiki-format-preview-evidence-trust-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/page-content-evidence-trust-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p1_multiphase_census_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p2_gas_depletion_efficiency_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p3_simulation_validation_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md.backup-before-pdf-link-20260708T214200Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/index.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html

 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/prose-evidence-trust-deepening-20260708T043427Z/cross-method-trust-legend-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/prose-evidence-trust-deepening-20260708T043427Z/cross-method-coverage-map-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/prose-evidence-trust-deepening-20260708T043427Z/manifest-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/prose-evidence-trust-deepening-20260708T043427Z/index-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/source-first-paper-adjudication/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/goru-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/source-first-paper-adjudication/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/tori-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/hwao-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/goru-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/kun-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/lana-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/kun-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/tori-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/hwao-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/lana-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-packet.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/debate-map-to-wiki-rebuild/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/lana-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/tori-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/hwao-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/goru-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/kun-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p5-2931-dedupe-spec-20260706T151025Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json.backup-before-p1-spec-20260706T101547Z
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/m3-p2-same-format-draft-20260707T050500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/quintet.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-citation-role-mappings.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/page-content-evidence-trust-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/wiki-format-preview-evidence-trust-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-preserved-no-go-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-summary.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/quintet.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger-summary.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-review-checklist.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-no-go-gap-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-pages.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger-summary.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-sections.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/m1_rp2_environment_quenching_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/m1_rp3_maintenance_heating_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/manifest-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-deepening-map-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/page-content-m2-v2-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-v2-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/packet-gated-paper-to-wiki-reconciliation/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/packet-gated-paper-to-wiki-reconciliation/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/packet-gated-paper-to-wiki-reconciliation/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-primary-citation-anchor-registry.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/wiki-format-preview-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/evidence-trust-map-20260708T014205Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/page-content-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html.backup-before-p1-spec-20260706T101547Z
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p5-2931-dedupe-spec-20260706T151025Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html.backup-before-research-topics-link-20260708T092242Z
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/quintet.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p5-2931-dedupe-spec-20260706T151025Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p1-legacy-overclaim-disposition-spec.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-hwao-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/REVIEW_PATCH_NOTE_v2p1_20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-hwao-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-hwao-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p1_multiphase_census_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p2_gas_depletion_efficiency_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p3_simulation_validation_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p3_feedback_transition_mass_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T094443Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T094443Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T094443Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T094443Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p1_outflow_escape_recycling_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p2_radio_jet_environment_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-p1-label-fix-20260708T022147Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-bindings-20260708T014205Z.md.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/manifest-20260708T014205Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-specificity-pass-20260708T111138Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-specificity-pass-20260708T111138Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-specificity-pass-20260708T111138Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-specificity-pass-20260708T111138Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json

codex
I have the inventory. Next I’m reading the manuscript bodies directly, focusing on abstract, intro, conclusion, figure/table captions, and citation anchors so I can separate genuine publication risks from already-accepted wording. I’ll cross-check the candidate copy against the public-linked manuscript text where that helps surface stale mismatches.
exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/*.md; do echo "===== $(basename "$f")"; sed -n '"'1,120p' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
===== research-topics-from-wiki-20260708T090359Z.md
# Galaxy Evolution — Research proposals on outflows and feedback regimes

> This page presents three proposal-style research programmes on outflow fate, jet coupling, and the transition from stellar-feedback to AGN-linked regulation. The proposals are framed around measurable observables, matched denominators, and explicit decision criteria.

**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:

- P1: [SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot (PDF)](m2_p1_outflow_escape_recycling_aas.pdf)
- P2: [Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot (PDF)](m2_p2_radio_jet_environment_aas.pdf)
- P3: [SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot (PDF)](m2_p3_feedback_transition_mass_aas.pdf)

3 proposal-style research programmes.

## P1 — Escape versus recycling: the fate of AGN-driven multiphase outflows

**Hypothesis / objective.** A substantial fraction of AGN-driven outflowing gas remains gravitationally bound and recycles through the circumgalactic medium, limiting the permanence of feedback-driven gas removal.

**Prior evidence and constraints.**
- Quasar observations show AGN feedback acting on molecular gas reservoirs at high redshift, but such detections do not determine whether gas escapes the halo. [quasar molecular-gas reservoirs](https://arxiv.org/abs/1706.08987).
- Stellar-feedback work on baryon deficiency in low-mass galaxies provides a boundary condition for non-AGN removal channels that must not be confused with AGN-driven escape. [stellar feedback and baryon deficiency](https://arxiv.org/abs/2512.05584).
- Simulated galaxy feedback constraints highlight that gas removal, recycling, and observable baryon fractions depend on halo scale. [simulated observable feedback constraints](https://arxiv.org/abs/0901.1880).

**Remaining uncertainty.** The escaped fraction of multiphase outflows is unmeasured across a representative mass/redshift sample; an outflow detection is not equivalent to permanent quenching.

**Survey/data plan.** AGN hosts and inactive controls spanning stellar mass and redshift; MUSE/MaNGA ionized-gas kinematics, ALMA CO and [C II] for cold gas, JWST/NIRSpec for z>2 outflow tracers, and CGM absorption where available to track recycling.

**Analysis/test and decision criterion.** Compare outflow velocity distributions with halo escape velocities inferred from dynamical/halo-mass estimates, then model escaped versus bound/recycling fractions as a function of stellar mass, halo mass, and redshift. A high escaped fraction at fixed denominator supports permanent-removal feedback; a low escaped fraction supports recycling-limited regulation.

**Limitations and wording guardrails.** Projection, phase conversion, and uncertain halo potentials can dominate the escaped-fraction error budget.

## P2 — Environmental dependence of radio-jet coupling efficiency in galaxy gas

**Hypothesis / objective.** The fraction of radio-jet mechanical power deposited into the multiphase interstellar or circumgalactic medium varies systematically with ambient gas density and host environment.

**Prior evidence and constraints.**
- Young radio galaxies show AGN-driven outflows and provide an empirical route to estimating feedback efficiency. [young radio galaxies and feedback efficiency](https://arxiv.org/abs/2009.11175).
- Local M51-scale NOEMA data show how jet/AGN activity can affect molecular ISM structure at high spatial resolution, motivating a broader population test. [SWAN IV molecular ISM feedback](https://arxiv.org/abs/2604.15438).
- Galaxy-group feedback studies identify the group regime as a strong testbed for coupling between radio activity and hot gas. [group-scale AGN feedback](https://arxiv.org/abs/2403.17145).

**Remaining uncertainty.** Radio luminosity is not a direct coupling-efficiency measurement; the key unknown is the distribution of deposited energy relative to jet power across host gas conditions.

**Survey/data plan.** VLA/LOFAR/MeerKAT for jet morphology and radio spectral ages; Chandra for cavities/shocks/hot gas; MUSE/MaNGA for ionized-gas shock diagnostics; ALMA CO for molecular disturbances; environment from group catalogues.

**Analysis/test and decision criterion.** Estimate jet power and gas work/thermal response in the same apertures, then regress coupling efficiency on gas density, environment, and jet age. A robust environmental dependence requires efficiency differences larger than radio-power calibration uncertainties.

**Limitations and wording guardrails.** Radio-to-jet-power conversions are uncertain; coupling estimates must be reported with systematic floors.

## P3 — Locating the transition from stellar-feedback to AGN-feedback regulation

**Hypothesis / objective.** There is a stellar/halo-mass regime where stellar-feedback momentum and energy budgets cease to explain gas loss or quiescence, and AGN-linked observables become necessary to reproduce the measured quenched fraction and baryon deficit.

**Prior evidence and constraints.**
- Low-mass baryon deficiency attributed to stellar feedback provides the low-mass endpoint of the transition problem. [stellar-feedback baryon deficiency](https://arxiv.org/abs/2512.05584).
- High-redshift environmental-quenching simulations emphasize that quenching mechanisms vary with mass and redshift, not only with local observables. [high-redshift environmental quenching simulations](https://arxiv.org/abs/2605.03008).
- Simulated observable-property constraints show why feedback-regime boundaries must be tested against measured baryonic properties. [feedback constraints in simulated galaxies](https://arxiv.org/abs/0901.1880).

**Remaining uncertainty.** The observational crossover mass between stellar-feedback-dominated regulation and AGN-linked regulation is not cleanly measured with the same denominator and gas observables.

**Survey/data plan.** DESI/GAMA/COSMOS parent samples with stellar mass and halo proxy; ALFALFA/FASHI HI and ALMA CO gas fractions; optical/IR SFRs; X-ray/radio AGN indicators; JWST for high-redshift extension.

**Analysis/test and decision criterion.** Fit a broken-slope or transition model for gas fraction, baryon deficit, and quenched fraction as functions of stellar/halo mass while including AGN incidence and stellar-feedback proxies. The transition is credible only if the AGN-linked term improves predictive power above the stellar-feedback model at high mass.

**Limitations and wording guardrails.** Halo-mass uncertainties and selection functions can smear the transition; results should be framed as a probability surface, not a single universal mass.

## Methodological note

- Evidence-traceability work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.

## Scope note

These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.

<!-- AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z · professional Gemini-assisted RT revision · docs-static no-apply -->

exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/*/aastex/*_integrated.tex; do echo "===== $f"; rg -n "''^('"\\\\begin\\{abstract\\}|\\\\end\\{abstract\\}|\\\\section\\{|\\\\subsection\\{|\\\\caption\\{|\\\\label\\{|\\\\cite[t|p|alp|author|year]?\\{)\" \""'$f" | sed -n '"'1,120p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
rg: regex parse error:
    (?:^(\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\label\{|\cite[t|p|alp|author|year]?\{))
                            ^^
error: unrecognized escape sequence
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
rg: regex parse error:
    (?:^(\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\label\{|\cite[t|p|alp|author|year]?\{))
                            ^^
error: unrecognized escape sequence
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
rg: regex parse error:
    (?:^(\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\label\{|\cite[t|p|alp|author|year]?\{))
                            ^^
error: unrecognized escape sequence
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
rg: regex parse error:
    (?:^(\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\label\{|\cite[t|p|alp|author|year]?\{))
                            ^^
error: unrecognized escape sequence
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
rg: regex parse error:
    (?:^(\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\label\{|\cite[t|p|alp|author|year]?\{))
                            ^^
error: unrecognized escape sequence
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
rg: regex parse error:
    (?:^(\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\label\{|\cite[t|p|alp|author|year]?\{))
                            ^^
error: unrecognized escape sequence
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
rg: regex parse error:
    (?:^(\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\label\{|\cite[t|p|alp|author|year]?\{))
                            ^^
error: unrecognized escape sequence
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
rg: regex parse error:
    (?:^(\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\label\{|\cite[t|p|alp|author|year]?\{))
                            ^^
error: unrecognized escape sequence
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
rg: regex parse error:
    (?:^(\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\label\{|\cite[t|p|alp|author|year]?\{))
                            ^^
error: unrecognized escape sequence

exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/*.md; do echo "===== $(basename "$f")"; sed -n '"'1,120p' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
===== research-topics-from-wiki-20260708T090359Z.md
# Galaxy Evolution — Research proposals on outflows and feedback regimes

> This page presents three proposal-style research programmes on outflow fate, jet coupling, and the transition from stellar-feedback to AGN-linked regulation. The proposals are framed around measurable observables, matched denominators, and explicit decision criteria.

**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:

- P1: [SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot (PDF)](m2_p1_outflow_escape_recycling_aas.pdf)
- P2: [Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot (PDF)](m2_p2_radio_jet_environment_aas.pdf)
- P3: [SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot (PDF)](m2_p3_feedback_transition_mass_aas.pdf)

3 proposal-style research programmes.

## P1 — Escape versus recycling: the fate of AGN-driven multiphase outflows

**Hypothesis / objective.** A substantial fraction of AGN-driven outflowing gas remains gravitationally bound and recycles through the circumgalactic medium, limiting the permanence of feedback-driven gas removal.

**Prior evidence and constraints.**
- Quasar observations show AGN feedback acting on molecular gas reservoirs at high redshift, but such detections do not determine whether gas escapes the halo. [quasar molecular-gas reservoirs](https://arxiv.org/abs/1706.08987).
- Stellar-feedback work on baryon deficiency in low-mass galaxies provides a boundary condition for non-AGN removal channels that must not be confused with AGN-driven escape. [stellar feedback and baryon deficiency](https://arxiv.org/abs/2512.05584).
- Simulated galaxy feedback constraints highlight that gas removal, recycling, and observable baryon fractions depend on halo scale. [simulated observable feedback constraints](https://arxiv.org/abs/0901.1880).

**Remaining uncertainty.** The escaped fraction of multiphase outflows is unmeasured across a representative mass/redshift sample; an outflow detection is not equivalent to permanent quenching.

**Survey/data plan.** AGN hosts and inactive controls spanning stellar mass and redshift; MUSE/MaNGA ionized-gas kinematics, ALMA CO and [C II] for cold gas, JWST/NIRSpec for z>2 outflow tracers, and CGM absorption where available to track recycling.

**Analysis/test and decision criterion.** Compare outflow velocity distributions with halo escape velocities inferred from dynamical/halo-mass estimates, then model escaped versus bound/recycling fractions as a function of stellar mass, halo mass, and redshift. A high escaped fraction at fixed denominator supports permanent-removal feedback; a low escaped fraction supports recycling-limited regulation.

**Limitations and wording guardrails.** Projection, phase conversion, and uncertain halo potentials can dominate the escaped-fraction error budget.

## P2 — Environmental dependence of radio-jet coupling efficiency in galaxy gas

**Hypothesis / objective.** The fraction of radio-jet mechanical power deposited into the multiphase interstellar or circumgalactic medium varies systematically with ambient gas density and host environment.

**Prior evidence and constraints.**
- Young radio galaxies show AGN-driven outflows and provide an empirical route to estimating feedback efficiency. [young radio galaxies and feedback efficiency](https://arxiv.org/abs/2009.11175).
- Local M51-scale NOEMA data show how jet/AGN activity can affect molecular ISM structure at high spatial resolution, motivating a broader population test. [SWAN IV molecular ISM feedback](https://arxiv.org/abs/2604.15438).
- Galaxy-group feedback studies identify the group regime as a strong testbed for coupling between radio activity and hot gas. [group-scale AGN feedback](https://arxiv.org/abs/2403.17145).

**Remaining uncertainty.** Radio luminosity is not a direct coupling-efficiency measurement; the key unknown is the distribution of deposited energy relative to jet power across host gas conditions.

**Survey/data plan.** VLA/LOFAR/MeerKAT for jet morphology and radio spectral ages; Chandra for cavities/shocks/hot gas; MUSE/MaNGA for ionized-gas shock diagnostics; ALMA CO for molecular disturbances; environment from group catalogues.

**Analysis/test and decision criterion.** Estimate jet power and gas work/thermal response in the same apertures, then regress coupling efficiency on gas density, environment, and jet age. A robust environmental dependence requires efficiency differences larger than radio-power calibration uncertainties.

**Limitations and wording guardrails.** Radio-to-jet-power conversions are uncertain; coupling estimates must be reported with systematic floors.

## P3 — Locating the transition from stellar-feedback to AGN-feedback regulation

**Hypothesis / objective.** There is a stellar/halo-mass regime where stellar-feedback momentum and energy budgets cease to explain gas loss or quiescence, and AGN-linked observables become necessary to reproduce the measured quenched fraction and baryon deficit.

**Prior evidence and constraints.**
- Low-mass baryon deficiency attributed to stellar feedback provides the low-mass endpoint of the transition problem. [stellar-feedback baryon deficiency](https://arxiv.org/abs/2512.05584).
- High-redshift environmental-quenching simulations emphasize that quenching mechanisms vary with mass and redshift, not only with local observables. [high-redshift environmental quenching simulations](https://arxiv.org/abs/2605.03008).
- Simulated observable-property constraints show why feedback-regime boundaries must be tested against measured baryonic properties. [feedback constraints in simulated galaxies](https://arxiv.org/abs/0901.1880).

**Remaining uncertainty.** The observational crossover mass between stellar-feedback-dominated regulation and AGN-linked regulation is not cleanly measured with the same denominator and gas observables.

**Survey/data plan.** DESI/GAMA/COSMOS parent samples with stellar mass and halo proxy; ALFALFA/FASHI HI and ALMA CO gas fractions; optical/IR SFRs; X-ray/radio AGN indicators; JWST for high-redshift extension.

**Analysis/test and decision criterion.** Fit a broken-slope or transition model for gas fraction, baryon deficit, and quenched fraction as functions of stellar/halo mass while including AGN incidence and stellar-feedback proxies. The transition is credible only if the AGN-linked term improves predictive power above the stellar-feedback model at high mass.

**Limitations and wording guardrails.** Halo-mass uncertainties and selection functions can smear the transition; results should be framed as a probability surface, not a single universal mass.

## Methodological note

- Evidence-traceability work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.

## Scope note

These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.

<!-- AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z · professional Gemini-assisted RT revision · docs-static no-apply -->

codex
I’ve confirmed the public-linked proposal text is stable across the mirrored roots, so the value now is in the manuscript-level wording and provenance boundaries rather than a large local-vs-live drift. I’m pulling the data-provenance JSON next because the strongest audit findings will come from whether each numeric claim is actually backed by the cached SDSS-derived artifacts.
exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_06_nine_papers/*/data/source_analysis_results.json; do echo "$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 exited 1 in 0ms:
zsh:1: no matches found: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_06_nine_papers/*/data/source_analysis_results.json

exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/*/data/source_analysis_results.json; do echo "===== $f"; jq '"'keys' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json
[
  "analysis_rows",
  "bpt_counts",
  "data_release",
  "files",
  "group_medians",
  "match_abs_delta_logM_median",
  "match_abs_delta_z_median",
  "match_distance_scaled_median",
  "matched_delta_log_sSFR_mean_ci95_bootstrap",
  "matched_delta_log_sSFR_mean_dex",
  "matched_delta_log_sSFR_median_ci95_bootstrap",
  "matched_delta_log_sSFR_median_dex",
  "matched_pairs",
  "ols_adjusted_for_logM_z",
  "query_top_n",
  "raw_rows",
  "revision_marker",
  "run_id",
  "safety"
]
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/data/source_analysis_results.json
[
  "card_id",
  "figure_pdf",
  "full_proposal_requires",
  "high_density_quenched",
  "high_minus_low_ci",
  "interpretation_guard",
  "low_density_quenched",
  "lpm_high_density_coeff",
  "lpm_high_density_se",
  "method",
  "pilot_question",
  "proposal_title",
  "result_bullets",
  "run_id",
  "sample_rows",
  "short_title",
  "slug",
  "source_sample"
]
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/data/source_analysis_results.json
[
  "card_id",
  "figure_pdf",
  "full_proposal_requires",
  "interpretation_guard",
  "massive_agn_fraction",
  "massive_quenched_agn_fraction",
  "massive_quenched_rows",
  "massive_rows",
  "method",
  "pilot_question",
  "proposal_title",
  "result_bullets",
  "run_id",
  "sample_rows",
  "short_title",
  "slug",
  "source_sample"
]
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json
[
  "card_id",
  "figure_pdf",
  "full_proposal_requires",
  "high_excitation_agn",
  "interpretation_guard",
  "median_log_sSFR_all",
  "median_log_sSFR_high_excitation",
  "method",
  "pilot_question",
  "proposal_title",
  "result_bullets",
  "run_id",
  "sample_rows",
  "short_title",
  "slug",
  "source_sample"
]
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json
[
  "card_id",
  "figure_pdf",
  "full_proposal_requires",
  "high_density_massive_agn",
  "high_minus_low_ci",
  "interpretation_guard",
  "low_density_massive_agn",
  "massive_rows",
  "method",
  "pilot_question",
  "proposal_title",
  "result_bullets",
  "run_id",
  "sample_rows",
  "short_title",
  "slug",
  "source_sample"
]
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json
[
  "agn_fraction_by_mass",
  "card_id",
  "figure_pdf",
  "full_proposal_requires",
  "interpretation_guard",
  "mass_bin_labels",
  "method",
  "peak_agn_fraction",
  "peak_agn_mass_bin",
  "pilot_question",
  "proposal_title",
  "quenched_fraction_by_mass",
  "result_bullets",
  "run_id",
  "sample_rows",
  "short_title",
  "slug",
  "source_sample",
  "transition_mass_bin_quenched_fraction_gt_0p5"
]
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/data/source_analysis_results.json
[
  "card_id",
  "figure_pdf",
  "full_proposal_requires",
  "interpretation_guard",
  "method",
  "pilot_question",
  "prevalence_ratio_widest_to_narrowest",
  "proposal_title",
  "result_bullets",
  "run_id",
  "sample_rows",
  "short_title",
  "slug",
  "source_sample",
  "tracer_prevalence"
]
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json
[
  "agn_fraction_in_denominator",
  "card_id",
  "figure_pdf",
  "full_proposal_requires",
  "interpretation_guard",
  "massive_transition_quenched_rows",
  "median_log_lha_denominator",
  "median_log_lha_offset_vs_massive_sf",
  "method",
  "pilot_question",
  "proposal_title",
  "result_bullets",
  "run_id",
  "sample_rows",
  "short_title",
  "slug",
  "source_sample"
]
===== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/data/source_analysis_results.json
[
  "agn_fraction_range",
  "card_id",
  "figure_pdf",
  "full_proposal_requires",
  "interpretation_guard",
  "method",
  "pilot_question",
  "proposal_title",
  "quenched_fraction_range",
  "result_bullets",
  "run_id",
  "sample_rows",
  "short_title",
  "slug",
  "source_sample",
  "target_vector_cells"
]

exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/*/data/source_analysis_results.json; do echo "===== $(basename $(dirname $(dirname "$f")))"; jq '"'{sample_size, matched_controls, selection, metrics, notes}' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
===== 01_m1_rp1_sdss_agn_sfr
{
  "sample_size": null,
  "matched_controls": null,
  "selection": null,
  "metrics": null,
  "notes": null
}
===== 02_m1_rp2_environment_quenching
{
  "sample_size": null,
  "matched_controls": null,
  "selection": null,
  "metrics": null,
  "notes": null
}
===== 03_m1_rp3_maintenance_heating
{
  "sample_size": null,
  "matched_controls": null,
  "selection": null,
  "metrics": null,
  "notes": null
}
===== 04_m2_p1_outflow_escape_recycling
{
  "sample_size": null,
  "matched_controls": null,
  "selection": null,
  "metrics": null,
  "notes": null
}
===== 05_m2_p2_radio_jet_environment
{
  "sample_size": null,
  "matched_controls": null,
  "selection": null,
  "metrics": null,
  "notes": null
}
===== 06_m2_p3_feedback_transition_mass
{
  "sample_size": null,
  "matched_controls": null,
  "selection": null,
  "metrics": null,
  "notes": null
}
===== 07_m3_p1_multiphase_census
{
  "sample_size": null,
  "matched_controls": null,
  "selection": null,
  "metrics": null,
  "notes": null
}
===== 08_m3_p2_gas_depletion_efficiency
{
  "sample_size": null,
  "matched_controls": null,
  "selection": null,
  "metrics": null,
  "notes": null
}
===== 09_m3_p3_simulation_validation
{
  "sample_size": null,
  "matched_controls": null,
  "selection": null,
  "metrics": null,
  "notes": null
}

codex
I’ve got the structural inventory; now I’m extracting the numeric provenance fields so I can verify that every headline number in the abstracts and discussion is actually traceable to the candidate’s cached-analysis JSON. After that I’ll isolate only the papers where wording still risks implying causality, simulation validation, or physical measurements the data do not support.
exec
/bin/zsh -lc "jq '{matched_pairs,raw_rows,analysis_rows,matched_delta_log_sSFR_median_dex,matched_delta_log_sSFR_mean_dex,match_abs_delta_logM_median,match_abs_delta_z_median,match_distance_scaled_median,bpt_counts,group_medians,ols_adjusted_for_logM_z}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "matched_pairs": 8146,
  "raw_rows": 60000,
  "analysis_rows": 60000,
  "matched_delta_log_sSFR_median_dex": -1.3088869999999995,
  "matched_delta_log_sSFR_mean_dex": -1.201557615885097,
  "match_abs_delta_logM_median": 0.0044599999999999085,
  "match_abs_delta_z_median": 0.00021079499999999973,
  "match_distance_scaled_median": 0.013706693336996863,
  "bpt_counts": {
    "agn": 8146,
    "intermediate": 12234,
    "star-forming": 39553,
    "unclassified": 67
  },
  "group_medians": {
    "agn": {
      "median_logM": 10.79099,
      "median_log_sSFR": -11.769829999999999,
      "median_u_minus_r": 2.7576649999999994,
      "median_z": 0.075976265,
      "n": 8146
    },
    "intermediate": {
      "median_logM": 10.62895,
      "median_log_sSFR": -10.8564,
      "median_u_minus_r": 2.5431500000000007,
      "median_z": 0.079609505,
      "n": 12234
    },
    "star-forming": {
      "median_logM": 10.01737,
      "median_log_sSFR": -9.909236,
      "median_u_minus_r": 1.814429999999998,
      "median_z": 0.06887668,
      "n": 39553
    },
    "unclassified": {
      "median_logM": 10.87501,
      "median_log_sSFR": -12.06685,
      "median_u_minus_r": 2.8580700000000014,
      "median_z": 0.08311625,
      "n": 67
    }
  },
  "ols_adjusted_for_logM_z": {
    "coef_is_agn_ci95": [
      -1.2103153323534461,
      -1.1873688115826728
    ],
    "coef_is_agn_log_sSFR_dex": -1.1988420719680595,
    "coef_is_agn_se": 0.005853704278258507,
    "coef_logM": -0.6590074792789541,
    "coef_z": 6.926838817644406,
    "n_regression": 47699
  }
}

exec
/bin/zsh -lc "jq '{sample_rows,source_sample,massive_rows,massive_quenched_rows,massive_agn_fraction,massive_quenched_agn_fraction,result_bullets,interpretation_guard}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "jq '{sample_rows,source_sample,high_excitation_agn,median_log_sSFR_all,median_log_sSFR_high_excitation,result_bullets,interpretation_guard}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "sample_rows": 60000,
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "high_excitation_agn": {
    "fraction": 0.074,
    "k": 4440,
    "n": 60000,
    "se": 0.0010686751923136733
  },
  "median_log_sSFR_all": -10.140585,
  "median_log_sSFR_high_excitation": -11.53205,
  "result_bullets": [
    "High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074).",
    "Their median log sSFR is -11.53, compared with -10.14 for the full denominator.",
    "SDSS does not measure escape velocity or multiphase outflow velocities here; the pilot supplies a denominator for resolved follow-up rather than an escape/recycling result."
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page."
}

 succeeded in 0ms:
{
  "sample_rows": 60000,
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "massive_rows": 9298,
  "massive_quenched_rows": 5695,
  "massive_agn_fraction": {
    "fraction": 0.4298773929877393,
    "k": 3997,
    "n": 9298,
    "se": 0.005134068554795429
  },
  "massive_quenched_agn_fraction": {
    "fraction": 0.6073748902546093,
    "k": 3459,
    "n": 5695,
    "se": 0.006470987903713825
  },
  "result_bullets": [
    "The massive subset (logM >= 10.8) contains 9,298 emission-line galaxies; 5,695 are low-sSFR by the pilot threshold.",
    "The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.",
    "This provides an optical duty-cycle denominator for X-ray/radio maintenance-heating follow-up, not a heating-to-cooling measurement."
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page."
}

exec
/bin/zsh -lc "jq '{sample_rows,source_sample,high_density_quenched,low_density_quenched,high_minus_low_ci,lpm_high_density_coeff,lpm_high_density_se,result_bullets,interpretation_guard}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "sample_rows": 60000,
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "high_density_quenched": {
    "fraction": 0.2304,
    "k": 3456,
    "n": 15000,
    "se": 0.003438176260752203
  },
  "low_density_quenched": {
    "fraction": 0.18066666666666667,
    "k": 2710,
    "n": 15000,
    "se": 0.0031414033193486656
  },
  "high_minus_low_ci": [
    0.04059666666666669,
    0.059135
  ],
  "lpm_high_density_coeff": 0.03249480778035638,
  "lpm_high_density_se": 0.003707733046841099,
  "result_bullets": [
    "The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy.",
    "The high-density quartile has quenched fraction 0.230 (3,456/15,000); the low-density quartile has 0.181 (2,710/15,000).",
    "The bootstrap high-minus-low quenched-fraction interval is [0.041, 0.059].",
    "A linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004."
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page."
}

exec
/bin/zsh -lc "jq '{sample_rows,source_sample,high_density_massive_agn,low_density_massive_agn,high_minus_low_ci,result_bullets,interpretation_guard}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "jq '{sample_rows,source_sample,agn_fraction_by_mass,quenched_fraction_by_mass,mass_bin_labels,peak_agn_fraction,peak_agn_mass_bin,transition_mass_bin_quenched_fraction_gt_0p5,result_bullets,interpretation_guard}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "sample_rows": 60000,
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "agn_fraction_by_mass": [
    0.0027030347708563705,
    0.013751792795072977,
    0.07734113712374582,
    0.2602886157135222,
    0.5202082816761716
  ],
  "quenched_fraction_by_mass": [
    0.005283204324855633,
    0.025816249050873197,
    0.1311663879598662,
    0.39254112476987946,
    0.7292338209769402
  ],
  "mass_bin_labels": [
    "8.0-9.5",
    "9.5-10.0",
    "10.0-10.5",
    "10.5-11.0",
    "11.0-12.5"
  ],
  "peak_agn_fraction": 0.5202082816761716,
  "peak_agn_mass_bin": "11.0-12.5",
  "transition_mass_bin_quenched_fraction_gt_0p5": "11.0-12.5",
  "result_bullets": [
    "The first stellar-mass bin with quenched fraction above 0.5 is 11.0-12.5.",
    "The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520.",
    "The result is an optical transition diagnostic; gas fractions and baryon deficits are needed before assigning the transition to stellar or AGN feedback."
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page."
}

 succeeded in 0ms:
{
  "sample_rows": 60000,
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "high_density_massive_agn": {
    "fraction": 0.5085836909871244,
    "k": 948,
    "n": 1864,
    "se": 0.011579319665266517
  },
  "low_density_massive_agn": {
    "fraction": 0.3667152221412964,
    "k": 1007,
    "n": 2746,
    "se": 0.009196312633686535
  },
  "high_minus_low_ci": [
    0.11189880364416133,
    0.1702164814837969
  ],
  "result_bullets": [
    "Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.",
    "The bootstrap high-minus-low interval is [0.112, 0.170].",
    "This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency."
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page."
}

exec
/bin/zsh -lc "jq '{sample_rows,source_sample,target_vector_cells,quenched_fraction_range,agn_fraction_range,result_bullets,interpretation_guard}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "sample_rows": 60000,
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "target_vector_cells": [
    {
      "agn_fraction": 0.002902757619738752,
      "mass_bin": "8.0-9.5",
      "median_u_minus_r": 1.5324300000000015,
      "n": 6201,
      "quenched_fraction": 0.006450572488308337,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.0006105006105006105,
      "mass_bin": "8.0-9.5",
      "median_u_minus_r": 1.378694999999999,
      "n": 1638,
      "quenched_fraction": 0.0006105006105006105,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.01,
      "mass_bin": "8.0-9.5",
      "median_u_minus_r": 1.0446000000000009,
      "n": 300,
      "quenched_fraction": 0.006666666666666667,
      "z_bin": "0.08-0.12"
    },
    {
      "agn_fraction": 0.030219018574993067,
      "mass_bin": "9.5-10.0",
      "median_u_minus_r": 1.8540899999999991,
      "n": 3607,
      "quenched_fraction": 0.06099251455503188,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.008417230566100017,
      "mass_bin": "9.5-10.0",
      "median_u_minus_r": 1.6964299999999994,
      "n": 6059,
      "quenched_fraction": 0.013038455190625516,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.0013717421124828531,
      "mass_bin": "9.5-10.0",
      "median_u_minus_r": 1.5156199999999984,
      "n": 2187,
      "quenched_fraction": 0.003200731595793324,
      "z_bin": "0.08-0.12"
    },
    {
      "agn_fraction": 0.15361242403781228,
      "mass_bin": "10.0-10.5",
      "median_u_minus_r": 2.2637100000000006,
      "n": 2962,
      "quenched_fraction": 0.25557056043214044,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.09022556390977443,
      "mass_bin": "10.0-10.5",
      "median_u_minus_r": 2.119389999999999,
      "n": 7581,
      "quenched_fraction": 0.160928637382931,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.03968346328406843,
      "mass_bin": "10.0-10.5",
      "median_u_minus_r": 1.9204700000000017,
      "n": 8593,
      "quenched_fraction": 0.06202723146747353,
      "z_bin": "0.08-0.12"
    },
    {
      "agn_fraction": 0.42955145118733506,
      "mass_bin": "10.5-11.0",
      "median_u_minus_r": 2.6227300000000007,
      "n": 1895,
      "quenched_fraction": 0.5810026385224274,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.2968719260279363,
      "mass_bin": "10.5-11.0",
      "median_u_minus_r": 2.5802999999999994,
      "n": 5083,
      "quenched_fraction": 0.45130828251032856,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.2089037622959132,
      "mass_bin": "10.5-11.0",
      "median_u_minus_r": 2.45496,
      "n": 9861,
      "quenched_fraction": 0.3260318426123111,
      "z_bin": "0.08-0.12"
    },
    {
      "agn_fraction": 0.6102564102564103,
      "mass_bin": "11.0-12.5",
      "median_u_minus_r": 2.83066,
      "n": 390,
      "quenched_fraction": 0.8564102564102564,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.5629691409507923,
      "mass_bin": "11.0-12.5",
      "median_u_minus_r": 2.850570000000001,
      "n": 1199,
      "quenched_fraction": 0.804837364470392,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.484860883797054,
      "mass_bin": "11.0-12.5",
      "median_u_minus_r": 2.8379250000000003,
      "n": 2444,
      "quenched_fraction": 0.6718494271685761,
      "z_bin": "0.08-0.12"
    }
  ],
  "quenched_fraction_range": [
    0.005283204324855633,
    0.7292338209769402
  ],
  "agn_fraction_range": [
    0.0027030347708563705,
    0.5202082816761716
  ],
  "result_bullets": [
    "The pilot writes 15 mass-redshift cells with n >= 50 as a compact validation vector.",
    "Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.",
    "The output is an observed target vector for simulation forward modelling, not a direct simulation comparison."
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page."
}

exec
/bin/zsh -lc "jq '{sample_rows,source_sample,tracer_prevalence,prevalence_ratio_widest_to_narrowest,result_bullets,interpretation_guard}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "sample_rows": 60000,
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "tracer_prevalence": {
    "BPT AGN": {
      "fraction": 0.13576666666666667,
      "k": 8146,
      "n": 60000,
      "se": 0.0013984162404239596
    },
    "high [NII]/Ha": {
      "fraction": 0.19161666666666666,
      "k": 11497,
      "n": 60000,
      "se": 0.0016067551136904373
    },
    "high [OIII]/Hb": {
      "fraction": 0.31698333333333334,
      "k": 19019,
      "n": 60000,
      "se": 0.0018995828477248288
    },
    "low-sSFR+emission": {
      "fraction": 0.20683333333333334,
      "k": 12410,
      "n": 60000,
      "se": 0.0016535482331215075
    },
    "red+emission": {
      "fraction": 0.4182666666666667,
      "k": 25096,
      "n": 60000,
      "se": 0.002013784423344193
    }
  },
  "prevalence_ratio_widest_to_narrowest": 3.080775840903511,
  "result_bullets": [
    "Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.",
    "The widest-to-narrowest prevalence ratio is 3.1, before adding molecular, neutral, or X-ray/radio phases.",
    "This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates."
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page."
}

exec
/bin/zsh -lc "jq '{sample_rows,source_sample,agn_fraction_in_denominator,median_log_lha_denominator,median_log_lha_offset_vs_massive_sf,massive_transition_quenched_rows,result_bullets,interpretation_guard}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "sample_rows": 60000,
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "agn_fraction_in_denominator": {
    "fraction": 0.5486699360974885,
    "k": 3692,
    "n": 6729,
    "se": 0.006066349807598532
  },
  "median_log_lha_denominator": 40.06117405071403,
  "median_log_lha_offset_vs_massive_sf": -0.6585859816891073,
  "massive_transition_quenched_rows": 6729,
  "result_bullets": [
    "The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample.",
    "Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.",
    "The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies.",
    "SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline."
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page."
}

exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/*/aastex/*_integrated.tex; do echo "===== $(basename "$f")"; sed -n '"'1,120p' \""'$f" | sed -n '"'1,120p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
===== m1_rp1_sdss_agn_sfr_integrated.tex
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS optical AGN/sSFR matched-control pilot}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad BPT optical AGN hosts and star-forming controls from the cached SDSS DR17 emission-line subset. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\Delta\log {\rm sSFR}=-1.309$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Introduction}\label{sec:purpose}
This analysis is the flagship local integration. It tests an optical-classification-associated catalog-sSFR offset, not causal AGN feedback, gas depletion, or halo maintenance heating.

This analysis preserves the active proposal title, 'Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.

All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.


\section{Shared parent sample and selection function}\label{sec:shared-selection}
All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.

Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.


\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. The cached analysis table contains 39,553 star-forming galaxies, 12,234 intermediate/composite objects, 8,146 broad optical AGN, and 67 unclassified objects.

The preferred estimator matches every broad optical AGN host to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. This is an association design; controls are not matched in morphology, halo mass, gas mass, aperture scale, AGN luminosity, or duty-cycle phase.

\begin{itemize}
\item Broad BPT optical AGN vs. star-forming controls at S/N$\geq 3$: $N=8,146$ matched pairs, median $\Delta\log {\rm sSFR}=-1.309$ dex with 95\% bootstrap interval $[-1.334,-1.283]$ dex.
\item Moderate mass-redshift caliper $|\Delta\log M_\star|\leq0.05$, $|\Delta z|\leq0.002$: $N=7,867$ retained pairs (96.6\% target coverage), median offset -1.318 dex.
\item A deterministic no-replacement diagnostic uses $N=7,419$ pairs and gives median offset -1.446 dex, but with visibly poorer mass balance; it is a stress test, not the preferred estimator.
\item Raising the line-S/N threshold to 10 leaves $N=1,530$ matched pairs and reduces the median offset to -0.744 dex, showing sensitivity to the emission-line selection function.
\item A narrower [N II] Seyfert-like proxy gives $N=2,114$ pairs and median offset -0.763 dex, reinforcing that subclass definitions change the effect size.
\end{itemize}


\begin{figure*}
\centering
\includegraphics[width=0.73\textwidth]{../figures/fig-bpt.pdf}
\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used in the RP-1 analysis. This figure documents the optical selection and classification boundary; it does not by itself identify causal AGN feedback.}
\label{fig:bpt}
\end{figure*}

\begin{figure*}
\centering
\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset is robust within the optical emission-line subset but remains selection- and subclass-dependent.}
\label{fig:offsets}
\end{figure*}


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.

\section{Conclusion}\label{sec:conclusion}
In the cached SDSS DR17 emission-line subset, broad BPT optical AGN hosts show a median sSFR offset of $-1.309$ dex relative to mass--redshift matched controls. The offset remains large but decreases to $-0.744$ dex at S/N$\geq 10$, so the result should be read as a selection-dependent optical association rather than evidence for causal AGN quenching.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579

\end{thebibliography}

\end{document}
===== m1_rp2_environment_quenching_integrated.tex
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS density proxy for environmental quenching}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{SDSS density proxy for environmental quenching}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We use the cached SDSS DR17 emission-line subset to build an optical density-proxy analysis of environmental quenching across a 60,000-galaxy sample. A 10th-nearest-neighbor density proxy is compared with quenched fraction after controlling for stellar mass and redshift; the high-density quartile has quenched fraction 0.230 versus 0.181 in the low-density quartile. This analysis is intentionally limited to the optical denominator and treats the missing group and halo information as a future-data requirement.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Introduction}\label{sec:purpose}
This analysis preserves the active proposal title, 'Separating internal and environmental quenching across stellar mass, halo mass, and redshift', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.

All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.


\section{Shared parent sample and selection function}\label{sec:shared-selection}
All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.

Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.


\section{SDSS density-proxy result for environmental quenching}\label{sec:topic-result}
The consolidated proposal question is: Does a nearest-neighbour density proxy add quenched-fraction information beyond stellar mass in the SDSS emission-line sample? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.

\begin{itemize}
\item The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy.
\item The high-density quartile has quenched fraction 0.230 (3,456/15,000); the low-density quartile has 0.181 (2,710/15,000).
\item The bootstrap high-minus-low quenched-fraction interval is [0.041, 0.059].
\item A linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of $0.032 \pm 0.004$.
\end{itemize}


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical density-proxy diagnostic for environmental quenching. The figure summarizes the cached optical result used as a denominator for future group-catalog analyses.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: group catalogues, robust central/satellite labels, halo masses, morphology, and multi-redshift selection functions.

Mass and environment are known separable axes in low-redshift galaxy evolution, but a real environmental-quenching analysis requires group/halo and central-satellite information beyond this nearest-neighbour proxy \citep{peng2010,baldry2006,wetzel2013,goubert2024}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.

\section{Conclusion}\label{sec:conclusion}
The SDSS-only proxy shows a high-density quenched fraction of 0.230 versus 0.181 in the low-density quartile, with a mass- and redshift-adjusted high-density coefficient of $0.032 \pm 0.004$. These values define an optical environmental baseline, but a full quenching interpretation still requires group catalogs, halo masses, and central/satellite labels.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\bibitem[Baldry et al.(2006)]{baldry2006} Baldry, I.~K., Balogh, M.~L., Bower, R.~G., et al. 2006, MNRAS, 373, 469
\bibitem[Goubert et al.(2024)]{goubert2024} Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2024, arXiv:2401.12953
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\end{thebibliography}

\end{document}
===== m1_rp3_maintenance_heating_integrated.tex
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Optical-AGN denominator for maintenance-heating follow-up}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{Optical-AGN denominator for maintenance-heating follow-up}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We use the cached SDSS DR17 emission-line subset to construct an optical denominator for maintenance-heating follow-up in massive galaxies. Among massive, low-sSFR hosts, we measure the available BPT-AGN fraction as a proxy for the duty-cycle denominator relevant to future X-ray or radio maintenance-heating studies. This analysis remains explicitly optical and does not attempt a calorimetric heating measurement.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Introduction}\label{sec:purpose}
This analysis preserves the active proposal title, 'Empirical duty-cycle constraints on AGN maintenance heating in massive halos', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.

All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.


\section{Shared parent sample and selection function}\label{sec:shared-selection}
All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.

Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.


\section{Optical denominator for maintenance-heating follow-up}\label{sec:topic-result}
The consolidated proposal question is: Among massive, low-sSFR SDSS emission-line galaxies, what optical AGN fraction is available as a denominator for X-ray/radio maintenance-heating follow-up? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.

\begin{itemize}
\item The massive subset ($\log M_\star \geq 10.8$) contains 9,298 emission-line galaxies; 5,695 are low-sSFR by the pilot threshold.
\item The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.
\item This provides an optical duty-cycle denominator for X-ray/radio maintenance-heating follow-up, not a heating-to-cooling measurement.
\end{itemize}


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for maintenance-heating follow-up. The figure summarizes the cached optical result used for target definition or denominator design.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.

Radio-mode and hot-atmosphere studies define the future calorimetric observables--jet power, cavities, cooling luminosity, and group gas--that are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.

\section{Conclusion}\label{sec:conclusion}
The massive subset contains 9,298 emission-line galaxies, with 5,695 classified as low-sSFR. The BPT AGN fraction rises from 0.430 in the massive subset to 0.607 in the massive low-sSFR subset, defining an optical duty-cycle denominator for maintenance-heating follow-up rather than a direct heating result.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, arXiv:2403.17145
\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[McNamara \& Nulsen(2012)]{mcnamara2012} McNamara, B.~R., \& Nulsen, P.~E.~J. 2012, New J. Phys., 14, 055023
\end{thebibliography}

\end{document}
===== m2_p1_outflow_escape_recycling_integrated.tex
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS high-excitation AGN denominator for outflow escape tests}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{SDSS high-excitation AGN denominator for outflow escape tests}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We use the cached SDSS DR17 emission-line subset to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts high-excitation optical AGN candidates and records their median sSFR as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Introduction}\label{sec:purpose}
This analysis preserves the active proposal title, 'Escape versus recycling: the fate of AGN-driven multiphase outflows', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.

All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.


\section{Shared parent sample and selection function}\label{sec:shared-selection}
All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.

Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.


\section{Optical denominator for outflow escape tests}\label{sec:topic-result}
The consolidated proposal question is: How large is the SDSS high-excitation optical-AGN denominator that would need resolved kinematics to test escape versus recycling? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.

\begin{itemize}
\item High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074).
\item Their median log sSFR is -11.53, compared with -10.14 for the full denominator.
\item SDSS does not measure escape velocity or multiphase outflow velocities here; the pilot supplies a denominator for resolved follow-up rather than an escape/recycling result.
\end{itemize}


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for outflow escape-versus-recycling follow-up. The figure summarizes the cached optical result used for target definition.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: resolved outflow velocities, halo potentials, molecular/ionized/neutral gas phases, and CGM recycling tracers.

Wind and outflow literature specifies the missing kinematic, geometric, molecular, and multiphase measurements; these sources motivate follow-up and do not turn line-ratio selection into an escape/recycling measurement \citep{veilleux2005,cicone2014,fiore2017,carniani2017,fabian2012}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.

\section{Conclusion}\label{sec:conclusion}
High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies, and their median log sSFR is -11.53 compared with -10.14 for the full denominator. The optical sample therefore defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\end{thebibliography}

\end{document}
===== m2_p2_radio_jet_environment_integrated.tex
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Environment proxy for optical AGN in massive SDSS hosts}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{Environment proxy for optical AGN in massive SDSS hosts}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We build an optical denominator for radio-jet environment follow-up using the cached SDSS DR17 emission-line subset. In massive hosts, we compare the high- and low-density quartiles of the optical AGN fraction to identify an environment-stratified target set for later radio or X-ray work. The result is an optical baseline only; it does not measure jet power or coupling efficiency.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Introduction}\label{sec:purpose}
This analysis preserves the active proposal title, 'Environmental dependence of radio-jet coupling efficiency in galaxy gas', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.

All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.


\section{Shared parent sample and selection function}\label{sec:shared-selection}
All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.

Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.


\section{Optical denominator for radio-jet environment follow-up}\label{sec:topic-result}
The consolidated proposal question is: Does a local-density proxy modulate the optical AGN fraction in massive SDSS hosts, motivating environment-stratified radio/X-ray jet-coupling follow-up? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.

\begin{itemize}
\item Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.
\item The bootstrap high-minus-low interval is [0.112, 0.170].
\item This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency.
\end{itemize}


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for radio-jet environment follow-up. The figure summarizes the cached optical result used for target definition.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.

The radio/X-ray/group literature motivates environment-stratified follow-up, but the present result is only an optical BPT-AGN fraction versus an internal density proxy \citep{best2005,santoro2020,mcnamara2007,eckert2024}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.

\section{Conclusion}\label{sec:conclusion}
Among massive hosts, the optical AGN fraction is 0.509 in the high-density quartile and 0.367 in the low-density quartile, with a bootstrap difference of [0.112, 0.170]. This establishes an environment-stratified optical denominator for radio-jet coupling studies, not a direct coupling measurement.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, arXiv:2403.17145
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Santoro et al.(2020)]{santoro2020} Santoro, F., Tadhunter, C., Baron, D., Morganti, R., \& Holt, J. 2020, A\&A, 644, A54
\end{thebibliography}

\end{document}
===== m2_p3_feedback_transition_mass_integrated.tex
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS mass transition in quenching and optical AGN incidence}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{SDSS mass transition in quenching and optical AGN incidence}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We use the cached SDSS DR17 emission-line subset to identify the stellar-mass regime where quenched fraction and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, but it does not assign the transition to stellar or AGN feedback on its own.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Introduction}\label{sec:purpose}
This analysis preserves the active proposal title, 'Locating the transition from stellar-feedback to AGN-feedback regulation', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.

All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.


\section{Shared parent sample and selection function}\label{sec:shared-selection}
All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.

Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.


\section{Optical denominator for feedback-transition mass}\label{sec:topic-result}
The consolidated proposal question is: At what stellar-mass scale do quenched fraction and optical AGN incidence rise in the same SDSS denominator? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.

\begin{itemize}
\item The first stellar-mass bin with quenched fraction above 0.5 is 11.0--12.5.
\item The optical AGN fraction peaks in the 11.0--12.5 bin at 0.520.
\item The result is an optical transition diagnostic; gas fractions and baryon deficits are needed before assigning the transition to stellar or AGN feedback.
\end{itemize}


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure summarizes the cached optical result used for target definition.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.

Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.

\section{Conclusion}\label{sec:conclusion}
The first stellar-mass bin with quenched fraction above 0.5 is 11.0--12.5, and the optical AGN fraction peaks at 0.520 in that same bin. These values define an optical transition vector, but gas fractions, baryon deficits, and halo-scale measurements are still needed before a causal feedback interpretation.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\bibitem[Baldry et al.(2004)]{baldry2004} Baldry, I.~K., Glazebrook, K., Brinkmann, J., et al. 2004, ApJ, 600, 681
\bibitem[Bluck et al.(2023)]{bluck2023} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108
\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Peng et al.(2012)]{peng2012} Peng, Y.-j., Lilly, S.~J., Renzini, A., \& Carollo, M. 2012, ApJ, 757, 4
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
\end{thebibliography}

\end{document}
===== m3_p1_multiphase_census_integrated.tex
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Common-denominator optical tracer census in SDSS}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{Common-denominator optical tracer census in SDSS}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We build a common optical denominator for a multiphase outflow census from the cached SDSS DR17 emission-line subset. Simple tracer definitions change the inferred AGN or feedback-candidate prevalence within the same denominator, so the draft focuses on the optical selection baseline needed before adding ionized, neutral, molecular, or X-ray/radio tracers. This is a denominator study, not a multiphase outflow measurement.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Introduction}\label{sec:purpose}
This analysis preserves the active proposal title, 'A multiphase, common-denominator census of AGN-driven outflows', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.

All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.


\section{Shared parent sample and selection function}\label{sec:shared-selection}
All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.

Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.


\section{Optical census of multiphase target denominators}\label{sec:topic-result}
The consolidated proposal question is: How strongly do simple optical tracer definitions change the inferred AGN/feedback-candidate prevalence in one common SDSS denominator? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.

\begin{itemize}
\item Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.
\item The widest-to-narrowest prevalence ratio is 3.1, before adding molecular, neutral, or X-ray/radio phases.
\item This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates.
\end{itemize}


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for the common-denominator multiphase census. The figure summarizes the cached optical result used for target definition.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model.

A real multiphase census needs independent ionized, neutral, molecular, and energetic outflow observables; the present SDSS thresholds are an optical denominator only \citep{veilleux2005,rupke2018,cicone2014,fiore2017,feruglio2015,woo2016,bae2018}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.

\section{Conclusion}\label{sec:conclusion}
Within the 60,000-galaxy denominator, simple tracer definitions change prevalence from 0.136 to 0.418, a factor of 3.1. That spread shows why a common-denominator census is required, while also underscoring that the present SDSS sample cannot measure molecular, neutral, or X-ray/radio outflow phases.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\bibitem[Bae \& Woo(2018)]{bae2018} Bae, H.-J., \& Woo, J.-H. 2018, ApJ, 853, 185
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Feruglio et al.(2015)]{feruglio2015} Feruglio, C., Fiore, F., Carniani, S., et al. 2015, A\&A, 583, A99
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Rupke(2018)]{rupke2018} Rupke, D.~S.~N. 2018, Galaxies, 6, 138
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Woo et al.(2016)]{woo2016} Woo, J.-H., Bae, H.-J., Son, D., \& Karouzos, M. 2016, ApJ, 817, 108
\end{thebibliography}

\end{document}
===== m3_p2_gas_depletion_efficiency_integrated.tex
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Optical denominator for gas-fraction versus efficiency tests}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{Optical denominator for gas-fraction versus efficiency tests}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We use the cached SDSS DR17 emission-line subset to construct an optical selection baseline and denominator for future molecular gas-fraction versus star-formation efficiency follow-up. For a sample of 6,729 massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of 0.549 and a median log H$\alpha$ luminosity proxy of 40.06 erg s$^{-1}$, which is offset by $-0.66$ dex relative to massive star-forming controls. The analysis provides the empirical baseline necessary to identify targets for CO or dust follow-up without claiming a physical separation of gas depletion from efficiency suppression from optical data alone.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Introduction}\label{sec:purpose}
This analysis preserves the active proposal title, 'Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.

All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.


\section{Shared parent sample and selection function}\label{sec:shared-selection}
All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.

Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.


\section{Optical denominator for gas-fraction versus efficiency tests}\label{sec:topic-result}
The consolidated proposal question is: How many massive quenched or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction/depletion-time follow-up? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.

\begin{itemize}
\item The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample.
\item Its optical BPT AGN fraction is 0.549; the median H$\alpha$ luminosity proxy is $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$.
\item The median H$\alpha$ luminosity proxy is approximately 0.66 dex lower than massive star-forming emission-line galaxies.
\item SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline.
\end{itemize}


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure summarizes the cached optical result used for target definition.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.

Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs; optical H$\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \citep{coldgass1,coldgass2,xcoldgass2017,xgass2018}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.

\section{Conclusion}\label{sec:conclusion}
We have mapped the optical baseline for 6,729 massive quenched or transitioning galaxies in the SDSS emission-line sample. We find a high BPT AGN fraction of 0.549 and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, approximately 0.66 dex lower than star-forming counterparts. While these quantities define the target selection denominator for future CO gas-fraction versus efficiency programs, direct molecular gas masses and aperture-matched star formation rates remain required to physically distinguish depletion from low efficiency.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
\bibitem[Saintonge et al.(2011a)]{coldgass1} Saintonge, A., Kauffmann, G., Kramer, C., et al. 2011a, MNRAS, 415, 32
\bibitem[Saintonge et al.(2011b)]{coldgass2} Saintonge, A., Kauffmann, G., Wang, J., et al. 2011b, MNRAS, 415, 61
\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
\end{thebibliography}

\end{document}
===== m3_p3_simulation_validation_integrated.tex
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS target vector for feedback-model validation}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{SDSS target vector for feedback-model validation}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We use the cached SDSS DR17 emission-line subset to define a compact optical target vector for forward-model validation. The pilot records quenched fraction, optical AGN incidence, and color versus mass/redshift across cells with sufficient counts, providing an observed target vector for later simulation work. It remains an empirical denominator study rather than a direct simulation comparison.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}

\section{Introduction}\label{sec:purpose}
This analysis preserves the active proposal title, 'Forward-modelled validation of cosmological feedback prescriptions', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.

All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.


\section{Shared parent sample and selection function}\label{sec:shared-selection}
All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.

Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.


\section{Optical target vector for simulation validation}\label{sec:topic-result}
The consolidated proposal question is: What compact SDSS target vector of quenched fraction, optical AGN incidence, and colour versus mass/redshift can be used for forward-model validation? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.

\begin{itemize}
\item The pilot writes 15 mass-redshift cells with $n \geq 50$ as a compact validation vector.
\item Across mass bins, quenched fractions span 0.005--0.729; optical AGN fractions span 0.003--0.520.
\item The output is an observed target vector for simulation forward modelling, not a direct simulation comparison.
\end{itemize}


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-model validation target vector. The figure summarizes the cached optical result used for target definition.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.

Simulation suites and mock-observation methods define the future comparison problem; no simulation mock has been forward-modelled or ranked in this pilot \citep{tng2019,eagle2015,simba2019,imanga2023,donnari2021,dubois2013,dubois2016}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.

\section{Conclusion}\label{sec:conclusion}
The pilot writes 15 mass-redshift cells with $n \geq 50$ as a compact validation vector, with quenched fractions spanning 0.005--0.729 and optical AGN fractions spanning 0.003--0.520. This observed target vector is useful for simulation forward modelling, but it still requires mock-observation pipelines before any model comparison can be claimed.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\bibitem[Dav\'e et al.(2019)]{simba2019} Dav\'e, R., Angl\'es-Alc\'azar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
\bibitem[Donnari et al.(2021)]{donnari2021} Donnari, M., Pillepich, A., Nelson, D., et al. 2021, MNRAS, 506, 4760
\bibitem[Dubois et al.(2013)]{dubois2013} Dubois, Y., Gavazzi, R., Peirani, S., \& Silk, J. 2013, MNRAS, 433, 3297
\bibitem[Dubois et al.(2016)]{dubois2016} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, MNRAS, 463, 3948
\bibitem[Nanni et al.(2023)]{imanga2023} Nanni, L., Thomas, D., Trayford, J., et al. 2023, MNRAS, 518, 2605
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
\end{thebibliography}

\end{document}

exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/*/aastex/*_integrated.tex; do echo "===== $(basename "$f")"; rg -n -F '"'\\begin{abstract}' \""'$f"; rg -n -F '"'\\end{abstract}' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
===== m1_rp1_sdss_agn_sfr_integrated.tex
12:\begin{abstract}
14:\end{abstract}
===== m1_rp2_environment_quenching_integrated.tex
12:\begin{abstract}
14:\end{abstract}
===== m1_rp3_maintenance_heating_integrated.tex
12:\begin{abstract}
14:\end{abstract}
===== m2_p1_outflow_escape_recycling_integrated.tex
12:\begin{abstract}
14:\end{abstract}
===== m2_p2_radio_jet_environment_integrated.tex
12:\begin{abstract}
14:\end{abstract}
===== m2_p3_feedback_transition_mass_integrated.tex
12:\begin{abstract}
14:\end{abstract}
===== m3_p1_multiphase_census_integrated.tex
12:\begin{abstract}
14:\end{abstract}
===== m3_p2_gas_depletion_efficiency_integrated.tex
12:\begin{abstract}
14:\end{abstract}
===== m3_p3_simulation_validation_integrated.tex
12:\begin{abstract}
14:\end{abstract}

exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/*/aastex/*_integrated.tex; do echo "===== $(basename "$f")"; rg -n -F '"'\\section{' \""'$f"; rg -n -F '"'\\subsection{' \""'$f"; rg -n -F '"'\\caption{' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
===== m1_rp1_sdss_agn_sfr_integrated.tex
18:\section{Introduction}\label{sec:purpose}
26:\section{Shared parent sample and selection function}\label{sec:shared-selection}
50:\section{Measurements}\label{sec:measurements}
54:\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
83:\section{Data Availability}\label{sec:data-avail}
86:\section{Conclusion}\label{sec:conclusion}
71:\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used in the RP-1 analysis. This figure documents the optical selection and classification boundary; it does not by itself identify causal AGN feedback.}
78:\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset is robust within the optical emission-line subset but remains selection- and subclass-dependent.}
===== m1_rp2_environment_quenching_integrated.tex
18:\section{Introduction}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{SDSS density-proxy result for environmental quenching}\label{sec:topic-result}
70:\section{Interpretation and missing observables}\label{sec:missing}
76:\section{Data Availability}\label{sec:data-avail}
79:\section{Conclusion}\label{sec:conclusion}
66:\caption{SDSS DR17 optical density-proxy diagnostic for environmental quenching. The figure summarizes the cached optical result used as a denominator for future group-catalog analyses.}
===== m1_rp3_maintenance_heating_integrated.tex
18:\section{Introduction}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Optical denominator for maintenance-heating follow-up}\label{sec:topic-result}
69:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}
65:\caption{SDSS DR17 optical denominator/proxy diagnostic for maintenance-heating follow-up. The figure summarizes the cached optical result used for target definition or denominator design.}
===== m2_p1_outflow_escape_recycling_integrated.tex
18:\section{Introduction}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Optical denominator for outflow escape tests}\label{sec:topic-result}
69:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}
65:\caption{SDSS DR17 optical denominator/proxy diagnostic for outflow escape-versus-recycling follow-up. The figure summarizes the cached optical result used for target definition.}
===== m2_p2_radio_jet_environment_integrated.tex
18:\section{Introduction}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Optical denominator for radio-jet environment follow-up}\label{sec:topic-result}
69:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}
65:\caption{SDSS DR17 optical denominator/proxy diagnostic for radio-jet environment follow-up. The figure summarizes the cached optical result used for target definition.}
===== m2_p3_feedback_transition_mass_integrated.tex
18:\section{Introduction}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Optical denominator for feedback-transition mass}\label{sec:topic-result}
69:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}
65:\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure summarizes the cached optical result used for target definition.}
===== m3_p1_multiphase_census_integrated.tex
18:\section{Introduction}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Optical census of multiphase target denominators}\label{sec:topic-result}
69:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}
65:\caption{SDSS DR17 optical denominator/proxy diagnostic for the common-denominator multiphase census. The figure summarizes the cached optical result used for target definition.}
===== m3_p2_gas_depletion_efficiency_integrated.tex
18:\section{Introduction}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Optical denominator for gas-fraction versus efficiency tests}\label{sec:topic-result}
70:\section{Interpretation and missing observables}\label{sec:missing}
76:\section{Data Availability}\label{sec:data-avail}
79:\section{Conclusion}\label{sec:conclusion}
66:\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure summarizes the cached optical result used for target definition.}
===== m3_p3_simulation_validation_integrated.tex
18:\section{Introduction}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Optical target vector for simulation validation}\label{sec:topic-result}
69:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}
65:\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-model validation target vector. The figure summarizes the cached optical result used for target definition.}

codex
I have enough to see the overall structure and the strongest candidate risk: some papers are clean denominator notes, but a few still carry proposal-style phrasing that can read like a physical claim if the reader only skims the abstract or conclusion. I’m now reading the remaining papers in full line-numbered form so I can name the exact sections that need tightening, especially where the wording could overstate what the SDSS-only baseline actually shows.
exec
/bin/zsh -lc "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex | sed -n '1,160p'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex | sed -n '1,140p'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex | sed -n '1,140p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Optical denominator for gas-fraction versus efficiency tests}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{Optical denominator for gas-fraction versus efficiency tests}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We use the cached SDSS DR17 emission-line subset to construct an optical selection baseline and denominator for future molecular gas-fraction versus star-formation efficiency follow-up. For a sample of 6,729 massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of 0.549 and a median log H$\alpha$ luminosity proxy of 40.06 erg s$^{-1}$, which is offset by $-0.66$ dex relative to massive star-forming controls. The analysis provides the empirical baseline necessary to identify targets for CO or dust follow-up without claiming a physical separation of gas depletion from efficiency suppression from optical data alone.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Introduction}\label{sec:purpose}
    19	This analysis preserves the active proposal title, 'Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.
    20	
    21	All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.
    22	
    23	
    24	\section{Shared parent sample and selection function}\label{sec:shared-selection}
    25	All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
    26	
    27	\begin{deluxetable*}{lrrr}
    28	\tabletypesize{\scriptsize}
    29	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    30	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    31	\startdata
    32	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    33	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    34	plus galSpecLine join & 416,554 & -- & 0.831 \\
    35	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    36	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Optical denominator for gas-fraction versus efficiency tests}\label{sec:topic-result}
    53	The consolidated proposal question is: How many massive quenched or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction/depletion-time follow-up? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.
    54	
    55	\begin{itemize}
    56	\item The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample.
    57	\item Its optical BPT AGN fraction is 0.549; the median H$\alpha$ luminosity proxy is $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$.
    58	\item The median H$\alpha$ luminosity proxy is approximately 0.66 dex lower than massive star-forming emission-line galaxies.
    59	\item SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline.
    60	\end{itemize}
    61	
    62	
    63	\begin{figure}
    64	\centering
    65	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    66	\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure summarizes the cached optical result used for target definition.}
    67	\label{fig:topic}
    68	\end{figure}
    69	
    70	\section{Interpretation and missing observables}\label{sec:missing}
    71	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.
    72	
    73	Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs; optical H$\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \citep{coldgass1,coldgass2,xcoldgass2017,xgass2018}.
    74	
    75	
    76	\section{Data Availability}\label{sec:data-avail}
    77	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.
    78	
    79	\section{Conclusion}\label{sec:conclusion}
    80	We have mapped the optical baseline for 6,729 massive quenched or transitioning galaxies in the SDSS emission-line sample. We find a high BPT AGN fraction of 0.549 and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, approximately 0.66 dex lower than star-forming counterparts. While these quantities define the target selection denominator for future CO gas-fraction versus efficiency programs, direct molecular gas masses and aperture-matched star formation rates remain required to physically distinguish depletion from low efficiency.
    81	
    82	
    83	\begin{thebibliography}{}
    84	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    85	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    86	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    87	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    88	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    89	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    90	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    91	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
    92	\bibitem[Saintonge et al.(2011a)]{coldgass1} Saintonge, A., Kauffmann, G., Kramer, C., et al. 2011a, MNRAS, 415, 32
    93	\bibitem[Saintonge et al.(2011b)]{coldgass2} Saintonge, A., Kauffmann, G., Wang, J., et al. 2011b, MNRAS, 415, 61
    94	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
    95	\end{thebibliography}
    96	
    97	\end{document}

 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS high-excitation AGN denominator for outflow escape tests}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{SDSS high-excitation AGN denominator for outflow escape tests}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We use the cached SDSS DR17 emission-line subset to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts high-excitation optical AGN candidates and records their median sSFR as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Introduction}\label{sec:purpose}
    19	This analysis preserves the active proposal title, 'Escape versus recycling: the fate of AGN-driven multiphase outflows', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.
    20	
    21	All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.
    22	
    23	
    24	\section{Shared parent sample and selection function}\label{sec:shared-selection}
    25	All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
    26	
    27	\begin{deluxetable*}{lrrr}
    28	\tabletypesize{\scriptsize}
    29	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    30	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    31	\startdata
    32	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    33	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    34	plus galSpecLine join & 416,554 & -- & 0.831 \\
    35	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    36	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Optical denominator for outflow escape tests}\label{sec:topic-result}
    53	The consolidated proposal question is: How large is the SDSS high-excitation optical-AGN denominator that would need resolved kinematics to test escape versus recycling? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.
    54	
    55	\begin{itemize}
    56	\item High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074).
    57	\item Their median log sSFR is -11.53, compared with -10.14 for the full denominator.
    58	\item SDSS does not measure escape velocity or multiphase outflow velocities here; the pilot supplies a denominator for resolved follow-up rather than an escape/recycling result.
    59	\end{itemize}
    60	
    61	
    62	\begin{figure}
    63	\centering
    64	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    65	\caption{SDSS DR17 optical denominator/proxy diagnostic for outflow escape-versus-recycling follow-up. The figure summarizes the cached optical result used for target definition.}
    66	\label{fig:topic}
    67	\end{figure}
    68	
    69	\section{Interpretation and missing observables}\label{sec:missing}
    70	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: resolved outflow velocities, halo potentials, molecular/ionized/neutral gas phases, and CGM recycling tracers.
    71	
    72	Wind and outflow literature specifies the missing kinematic, geometric, molecular, and multiphase measurements; these sources motivate follow-up and do not turn line-ratio selection into an escape/recycling measurement \citep{veilleux2005,cicone2014,fiore2017,carniani2017,fabian2012}.
    73	
    74	
    75	\section{Data Availability}\label{sec:data-avail}
    76	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies, and their median log sSFR is -11.53 compared with -10.14 for the full denominator. The optical sample therefore defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate.
    80	
    81	
    82	\begin{thebibliography}{}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    88	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    89	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    90	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
    91	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
    92	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
    93	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
    94	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
    95	\end{thebibliography}
    96	
    97	\end{document}

 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS mass transition in quenching and optical AGN incidence}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{SDSS mass transition in quenching and optical AGN incidence}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We use the cached SDSS DR17 emission-line subset to identify the stellar-mass regime where quenched fraction and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, but it does not assign the transition to stellar or AGN feedback on its own.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Introduction}\label{sec:purpose}
    19	This analysis preserves the active proposal title, 'Locating the transition from stellar-feedback to AGN-feedback regulation', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.
    20	
    21	All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.
    22	
    23	
    24	\section{Shared parent sample and selection function}\label{sec:shared-selection}
    25	All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
    26	
    27	\begin{deluxetable*}{lrrr}
    28	\tabletypesize{\scriptsize}
    29	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    30	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    31	\startdata
    32	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    33	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    34	plus galSpecLine join & 416,554 & -- & 0.831 \\
    35	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    36	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Optical denominator for feedback-transition mass}\label{sec:topic-result}
    53	The consolidated proposal question is: At what stellar-mass scale do quenched fraction and optical AGN incidence rise in the same SDSS denominator? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.
    54	
    55	\begin{itemize}
    56	\item The first stellar-mass bin with quenched fraction above 0.5 is 11.0--12.5.
    57	\item The optical AGN fraction peaks in the 11.0--12.5 bin at 0.520.
    58	\item The result is an optical transition diagnostic; gas fractions and baryon deficits are needed before assigning the transition to stellar or AGN feedback.
    59	\end{itemize}
    60	
    61	
    62	\begin{figure}
    63	\centering
    64	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    65	\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure summarizes the cached optical result used for target definition.}
    66	\label{fig:topic}
    67	\end{figure}
    68	
    69	\section{Interpretation and missing observables}\label{sec:missing}
    70	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.
    71	
    72	Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.
    73	
    74	
    75	\section{Data Availability}\label{sec:data-avail}
    76	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	The first stellar-mass bin with quenched fraction above 0.5 is 11.0--12.5, and the optical AGN fraction peaks at 0.520 in that same bin. These values define an optical transition vector, but gas fractions, baryon deficits, and halo-scale measurements are still needed before a causal feedback interpretation.
    80	
    81	
    82	\begin{thebibliography}{}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    88	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    89	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    90	\bibitem[Baldry et al.(2004)]{baldry2004} Baldry, I.~K., Glazebrook, K., Brinkmann, J., et al. 2004, ApJ, 600, 681
    91	\bibitem[Bluck et al.(2023)]{bluck2023} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108
    92	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
    93	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
    94	\bibitem[Peng et al.(2012)]{peng2012} Peng, Y.-j., Lilly, S.~J., Renzini, A., \& Carollo, M. 2012, ApJ, 757, 4
    95	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
    96	\end{thebibliography}
    97	
    98	\end{document}

exec
/bin/zsh -lc "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex | sed -n '1,140p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Common-denominator optical tracer census in SDSS}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{Common-denominator optical tracer census in SDSS}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We build a common optical denominator for a multiphase outflow census from the cached SDSS DR17 emission-line subset. Simple tracer definitions change the inferred AGN or feedback-candidate prevalence within the same denominator, so the draft focuses on the optical selection baseline needed before adding ionized, neutral, molecular, or X-ray/radio tracers. This is a denominator study, not a multiphase outflow measurement.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Introduction}\label{sec:purpose}
    19	This analysis preserves the active proposal title, 'A multiphase, common-denominator census of AGN-driven outflows', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.
    20	
    21	All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.
    22	
    23	
    24	\section{Shared parent sample and selection function}\label{sec:shared-selection}
    25	All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
    26	
    27	\begin{deluxetable*}{lrrr}
    28	\tabletypesize{\scriptsize}
    29	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    30	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    31	\startdata
    32	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    33	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    34	plus galSpecLine join & 416,554 & -- & 0.831 \\
    35	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    36	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Optical census of multiphase target denominators}\label{sec:topic-result}
    53	The consolidated proposal question is: How strongly do simple optical tracer definitions change the inferred AGN/feedback-candidate prevalence in one common SDSS denominator? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.
    54	
    55	\begin{itemize}
    56	\item Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.
    57	\item The widest-to-narrowest prevalence ratio is 3.1, before adding molecular, neutral, or X-ray/radio phases.
    58	\item This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates.
    59	\end{itemize}
    60	
    61	
    62	\begin{figure}
    63	\centering
    64	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    65	\caption{SDSS DR17 optical denominator/proxy diagnostic for the common-denominator multiphase census. The figure summarizes the cached optical result used for target definition.}
    66	\label{fig:topic}
    67	\end{figure}
    68	
    69	\section{Interpretation and missing observables}\label{sec:missing}
    70	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model.
    71	
    72	A real multiphase census needs independent ionized, neutral, molecular, and energetic outflow observables; the present SDSS thresholds are an optical denominator only \citep{veilleux2005,rupke2018,cicone2014,fiore2017,feruglio2015,woo2016,bae2018}.
    73	
    74	
    75	\section{Data Availability}\label{sec:data-avail}
    76	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	Within the 60,000-galaxy denominator, simple tracer definitions change prevalence from 0.136 to 0.418, a factor of 3.1. That spread shows why a common-denominator census is required, while also underscoring that the present SDSS sample cannot measure molecular, neutral, or X-ray/radio outflow phases.
    80	
    81	
    82	\begin{thebibliography}{}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    88	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    89	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    90	\bibitem[Bae \& Woo(2018)]{bae2018} Bae, H.-J., \& Woo, J.-H. 2018, ApJ, 853, 185
    91	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
    92	\bibitem[Feruglio et al.(2015)]{feruglio2015} Feruglio, C., Fiore, F., Carniani, S., et al. 2015, A\&A, 583, A99
    93	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
    94	\bibitem[Rupke(2018)]{rupke2018} Rupke, D.~S.~N. 2018, Galaxies, 6, 138
    95	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
    96	\bibitem[Woo et al.(2016)]{woo2016} Woo, J.-H., Bae, H.-J., Son, D., \& Karouzos, M. 2016, ApJ, 817, 108
    97	\end{thebibliography}
    98	
    99	\end{document}

exec
/bin/zsh -lc "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex | sed -n '1,140p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS target vector for feedback-model validation}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{SDSS target vector for feedback-model validation}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We use the cached SDSS DR17 emission-line subset to define a compact optical target vector for forward-model validation. The pilot records quenched fraction, optical AGN incidence, and color versus mass/redshift across cells with sufficient counts, providing an observed target vector for later simulation work. It remains an empirical denominator study rather than a direct simulation comparison.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Introduction}\label{sec:purpose}
    19	This analysis preserves the active proposal title, 'Forward-modelled validation of cosmological feedback prescriptions', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.
    20	
    21	All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.
    22	
    23	
    24	\section{Shared parent sample and selection function}\label{sec:shared-selection}
    25	All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
    26	
    27	\begin{deluxetable*}{lrrr}
    28	\tabletypesize{\scriptsize}
    29	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    30	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    31	\startdata
    32	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    33	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    34	plus galSpecLine join & 416,554 & -- & 0.831 \\
    35	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    36	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Optical target vector for simulation validation}\label{sec:topic-result}
    53	The consolidated proposal question is: What compact SDSS target vector of quenched fraction, optical AGN incidence, and colour versus mass/redshift can be used for forward-model validation? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.
    54	
    55	\begin{itemize}
    56	\item The pilot writes 15 mass-redshift cells with $n \geq 50$ as a compact validation vector.
    57	\item Across mass bins, quenched fractions span 0.005--0.729; optical AGN fractions span 0.003--0.520.
    58	\item The output is an observed target vector for simulation forward modelling, not a direct simulation comparison.
    59	\end{itemize}
    60	
    61	
    62	\begin{figure}
    63	\centering
    64	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    65	\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-model validation target vector. The figure summarizes the cached optical result used for target definition.}
    66	\label{fig:topic}
    67	\end{figure}
    68	
    69	\section{Interpretation and missing observables}\label{sec:missing}
    70	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.
    71	
    72	Simulation suites and mock-observation methods define the future comparison problem; no simulation mock has been forward-modelled or ranked in this pilot \citep{tng2019,eagle2015,simba2019,imanga2023,donnari2021,dubois2013,dubois2016}.
    73	
    74	
    75	\section{Data Availability}\label{sec:data-avail}
    76	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	The pilot writes 15 mass-redshift cells with $n \geq 50$ as a compact validation vector, with quenched fractions spanning 0.005--0.729 and optical AGN fractions spanning 0.003--0.520. This observed target vector is useful for simulation forward modelling, but it still requires mock-observation pipelines before any model comparison can be claimed.
    80	
    81	
    82	\begin{thebibliography}{}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    88	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    89	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    90	\bibitem[Dav\'e et al.(2019)]{simba2019} Dav\'e, R., Angl\'es-Alc\'azar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
    91	\bibitem[Donnari et al.(2021)]{donnari2021} Donnari, M., Pillepich, A., Nelson, D., et al. 2021, MNRAS, 506, 4760
    92	\bibitem[Dubois et al.(2013)]{dubois2013} Dubois, Y., Gavazzi, R., Peirani, S., \& Silk, J. 2013, MNRAS, 433, 3297
    93	\bibitem[Dubois et al.(2016)]{dubois2016} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, MNRAS, 463, 3948
    94	\bibitem[Nanni et al.(2023)]{imanga2023} Nanni, L., Thomas, D., Trayford, J., et al. 2023, MNRAS, 518, 2605
    95	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
    96	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
    97	\end{thebibliography}
    98	
    99	\end{document}

exec
/bin/zsh -lc "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex | sed -n '1,140p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Environment proxy for optical AGN in massive SDSS hosts}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{Environment proxy for optical AGN in massive SDSS hosts}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We build an optical denominator for radio-jet environment follow-up using the cached SDSS DR17 emission-line subset. In massive hosts, we compare the high- and low-density quartiles of the optical AGN fraction to identify an environment-stratified target set for later radio or X-ray work. The result is an optical baseline only; it does not measure jet power or coupling efficiency.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Introduction}\label{sec:purpose}
    19	This analysis preserves the active proposal title, 'Environmental dependence of radio-jet coupling efficiency in galaxy gas', but narrows the manuscript to the directly measured SDSS optical quantities reported below. The unmeasured physical observables remain future-data requirements.
    20	
    21	All quantitative statements are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. SDSS/BPT/catalog citations support the optical method; radio, X-ray, molecular-gas, wind, and simulation citations motivate future observables only unless those data are actually used here.
    22	
    23	
    24	\section{Shared parent sample and selection function}\label{sec:shared-selection}
    25	All nine integrated drafts use the same public-data backbone unless explicitly noted. The row-level table is the cached SDSS DR17 emission-line subset from the first pilot: 60,000 rows selected from public SDSS spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The strict public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the cached table covers 24.0\% of that strict parent. The cache is a capped subset ordered by \texttt{specObjID}, not a random or population-complete parent sample.
    26	
    27	\begin{deluxetable*}{lrrr}
    28	\tabletypesize{\scriptsize}
    29	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    30	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    31	\startdata
    32	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    33	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    34	plus galSpecLine join & 416,554 & -- & 0.831 \\
    35	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    36	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Optical denominator for radio-jet environment follow-up}\label{sec:topic-result}
    53	The consolidated proposal question is: Does a local-density proxy modulate the optical AGN fraction in massive SDSS hosts, motivating environment-stratified radio/X-ray jet-coupling follow-up? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.
    54	
    55	\begin{itemize}
    56	\item Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.
    57	\item The bootstrap high-minus-low interval is [0.112, 0.170].
    58	\item This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency.
    59	\end{itemize}
    60	
    61	
    62	\begin{figure}
    63	\centering
    64	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    65	\caption{SDSS DR17 optical denominator/proxy diagnostic for radio-jet environment follow-up. The figure summarizes the cached optical result used for target definition.}
    66	\label{fig:topic}
    67	\end{figure}
    68	
    69	\section{Interpretation and missing observables}\label{sec:missing}
    70	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.
    71	
    72	The radio/X-ray/group literature motivates environment-stratified follow-up, but the present result is only an optical BPT-AGN fraction versus an internal density proxy \citep{best2005,santoro2020,mcnamara2007,eckert2024}.
    73	
    74	
    75	\section{Data Availability}\label{sec:data-avail}
    76	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. The analysis-specific cached subset and local manifest are internal project artifacts used to preserve reproducibility for this candidate copy.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	Among massive hosts, the optical AGN fraction is 0.509 in the high-density quartile and 0.367 in the low-density quartile, with a bootstrap difference of [0.112, 0.170]. This establishes an environment-stratified optical denominator for radio-jet coupling studies, not a direct coupling measurement.
    80	
    81	
    82	\begin{thebibliography}{}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    88	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    89	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    90	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    91	\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, arXiv:2403.17145
    92	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
    93	\bibitem[Santoro et al.(2020)]{santoro2020} Santoro, F., Tadhunter, C., Baron, D., Morganti, R., \& Holt, J. 2020, A\&A, 644, A54
    94	\end{thebibliography}
    95	
    96	\end{document}

codex
I’ve now read the full candidate TeX for the riskier papers. I’m doing one final consistency pass across the mirrored public/life copies of the research-topic manuscript so I can say whether there is a true stale mismatch or just parallel copies that are intentionally identical.
exec
/bin/zsh -lc 'sha256sum /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
d28723882b4504923293dbbb9a7776970417cbf108d8f2a51064da55b3cf0eb4  /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
d28723882b4504923293dbbb9a7776970417cbf108d8f2a51064da55b3cf0eb4  /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md

exec
/bin/zsh -lc 'sha256sum /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md' in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc 'sha256sum /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
657367652e295a210b46aea9f527896b9ce4c03ba683a84b21c1518b5dbe7e01  /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html
657367652e295a210b46aea9f527896b9ce4c03ba683a84b21c1518b5dbe7e01  /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html

 succeeded in 0ms:
a5120dced76e19fa19c6a59232c8442de14033713aa3cc1cebbee137f214d082  /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
a5120dced76e19fa19c6a59232c8442de14033713aa3cc1cebbee137f214d082  /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md

exec
/bin/zsh -lc 'sha256sum /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
4f8e7fb0f272837b9b075f028cfb20ee89849e83383de104353fd529289abb56  /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
4f8e7fb0f272837b9b075f028cfb20ee89849e83383de104353fd529289abb56  /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md

codex
**OVERNIGHT_CODEX_KUN_REPRO_CYCLE_06 status: ISSUES_FOUND**

**Files/paths actually inspected**
- Candidate TeX files, all 9:
  - [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
  - [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
  - [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
  - [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
  - [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
  - [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
  - [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
  - [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
  - [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)
- Candidate provenance JSONs, all 9:
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/data/source_analysis_results.json)
- Public-linked manuscript copies checked for stale drift:
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [index.html](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html)
  - [index.html](/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)

**Ranked findings**
1. **Major**: [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex#L12) still risks reading like a simulation-comparison paper even though it explicitly says no direct comparison was done. The title, abstract, and conclusion should keep the focus on an observed SDSS target vector, not “validation” as a completed act. Safe fix: keep the measured values, but rewrite every skim-surface sentence to say “observed target vector for later validation” and “no simulation mock/comparison in this pilot.”
2. **Major**: [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex#L12) has a notation/units problem in the abstract and conclusion. “median log H-alpha luminosity proxy of 40.06 erg s^-1” is dimensionally awkward and easier to misread than the body text. Safe fix: use the explicit form already present in the body, `median log(L_Hα / erg s^-1) = 40.06`, and keep the comparison boundary explicit as “relative to massive star-forming emission-line controls.”
3. **Major**: [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex#L12) is still a little too close to an “escape test” claim in its title and topic section. The manuscript is honest, but the wording can be skimmed as more physical than it is. Safe fix: prefer “denominator for outflow escape-versus-recycling tests” everywhere, and keep the result sentence limited to “4,440 high-excitation optical AGN candidates of 60,000; median sSFR -11.53,” with the follow-up requirement pushed to the missing-observables section.
4. **Minor**: [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex#L12) uses “measures a median Δlog sSFR” in the abstract, which is slightly too active for an association-only paper. Safe fix: change to “finds a median matched-pair offset” or “reports a median matched-pair Δlog sSFR” so the causal boundary is obvious at first glance.
5. **Improvement**: The figure captions in papers 02-09 are still boilerplate and not result-rich. They often say only that the figure “summarizes the cached optical result used for target definition,” which makes skimmers work too hard. Safe fix: replace each with a variable-specific caption that names the plotted quantities, sample size, and caveat, for example “SDSS DR17 density-proxy diagnostic showing high-density and low-density quartile quenched fractions in the 60,000-galaxy cached denominator.” Preserve every numeric value from the source-analysis JSON, do not introduce new numbers.

**Exact feed for PDF-writing pilot**
- [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex#L12): change the abstract’s second sentence to “The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and finds a median matched-pair Δlog sSFR of -1.309 dex.” Keep the third sentence’s association-only guardrail. In the conclusion, keep “selection-dependent optical association rather than evidence for causal AGN quenching.”
- [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex#L12): make the abstract and conclusion explicit that the 0.230 versus 0.181 comparison is an optical density-proxy baseline, not a full environmental-quenching result. In the figure caption, name the 10th-nearest-neighbor proxy and the quartile comparison instead of “cached optical result.”
- [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex#L12): keep the denominator framing, but tighten the abstract so it says the paper measures the available BPT-AGN fraction in massive low-sSFR hosts and does not make a heating claim. If you keep “duty-cycle denominator,” add “optical-only” in the same sentence.
- [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex#L12): rewrite the abstract’s middle sentence to “The analysis counts 4,440 high-excitation optical AGN candidates and records their median sSFR as a proxy for where resolved kinematics and multiphase-gas follow-up should focus.” Keep “not an escape-velocity measurement” verbatim. In the conclusion, say “follow-up denominator” rather than “escape/recycling work” if you want maximum skimming safety.
- [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex#L12): keep the result values, but phrase the abstract as an optical environment-stratified denominator for later radio/X-ray work, not as an implied coupling study. Caption should name the high- and low-density quartile AGN fractions and the bootstrap interval.
- [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex#L12): keep the transition-bin numbers exactly as-is, but add “optical transition diagnostic” near the result sentence and keep the causal interpretation only in the missing-observables section.
- [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex#L12): the abstract and conclusion are sound, but the figure caption should name the prevalence range and the “widest-to-narrowest” ratio explicitly so the figure is self-explanatory.
- [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex#L12): change the abstract and conclusion to use the explicit log-luminosity notation already used in the body, and add “same denominator” or “massive star-forming emission-line controls” to the offset sentence.
- [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex#L12): keep the 15-cell, `n >= 50`, 0.005-0.729, and 0.003-0.520 values unchanged, but rewrite the abstract and conclusion to say “observed target vector for later forward-model validation” and “not a direct simulation comparison.” That is the safest wording for the pilot.

**Real-data/source/citation audit notes**
- Every headline number I checked traces to `source_analysis_results.json` and matches the TeX:
  - RP-1: 8,146 matched pairs, median matched-pair offset -1.308887 dex.
  - RP-2: 60,000 rows, high-density quenched fraction 0.2304, low-density 0.1807.
  - RP-3: 9,298 massive rows, 5,695 quenched, BPT AGN fractions 0.4299 and 0.6074.
  - P1: 4,440 high-excitation AGN of 60,000, median sSFR -11.53205.
  - P2: high-density massive AGN fraction 0.5086, low-density 0.3667, bootstrap interval [0.1119, 0.1702].
  - P3: transition bin 11.0-12.5, peak AGN fraction 0.5202, quenched-fraction threshold crossed there.
  - P4: prevalence 0.136 to 0.418, ratio 3.0808.
  - P5: 6,729-row denominator, AGN fraction 0.5487, median H-alpha proxy 40.0612, offset -0.6586 dex.
  - P6: 15 mass-redshift cells with `n >= 50`, quenched fraction range 0.0053-0.7292, AGN fraction range 0.0027-0.5202.
- No invented numbers, citations, or URLs were introduced in the inspected files.
- Citation roles are mostly correct. The future-observables citations in the “missing observables” sections are used as motivation, not as evidence for the SDSS-only result. Keep them quarantined there.
- Public/live mirrored research-topic manuscripts are byte-identical on checksum for the inspected pairs, so I did not find a stale public-vs-local mismatch in those copies.

**Workflow/system notes**
- The read-only candidate TeX and the mirrored public/live research-topic manuscripts are synchronized for the inspected artifacts.
- The main provenance gap is not text drift, it is version traceability across candidate-copy TeX, public-linked manuscript pages, and the cached analysis JSON. A hash manifest tying the PDF-writing pilot output back to the exact candidate-copy TeX would make future audits cheaper.
- I did not touch the public/live roots, did not replace any PDFs, and did not attempt any publish path.

**Safety ledger**
- No file edits: yes.
- No public replacement or publish: yes.
- No DB, SQL, wiki mutation, or page-version writes: yes.
- No deploy or restart: yes.
- No git commit, push, merge, rebase, or history rewrite: yes.
- No cron changes: yes.
- No billing, cloud, OAuth, API-key, account, credential, token, or cookie access: yes.
- No external manuscript submission: yes.
tokens used
118,799
**OVERNIGHT_CODEX_KUN_REPRO_CYCLE_06 status: ISSUES_FOUND**

**Files/paths actually inspected**
- Candidate TeX files, all 9:
  - [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
  - [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
  - [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
  - [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
  - [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
  - [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
  - [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
  - [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
  - [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)
- Candidate provenance JSONs, all 9:
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json)
  - [source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/data/source_analysis_results.json)
- Public-linked manuscript copies checked for stale drift:
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [index.html](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html)
  - [index.html](/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)

**Ranked findings**
1. **Major**: [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex#L12) still risks reading like a simulation-comparison paper even though it explicitly says no direct comparison was done. The title, abstract, and conclusion should keep the focus on an observed SDSS target vector, not “validation” as a completed act. Safe fix: keep the measured values, but rewrite every skim-surface sentence to say “observed target vector for later validation” and “no simulation mock/comparison in this pilot.”
2. **Major**: [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex#L12) has a notation/units problem in the abstract and conclusion. “median log H-alpha luminosity proxy of 40.06 erg s^-1” is dimensionally awkward and easier to misread than the body text. Safe fix: use the explicit form already present in the body, `median log(L_Hα / erg s^-1) = 40.06`, and keep the comparison boundary explicit as “relative to massive star-forming emission-line controls.”
3. **Major**: [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex#L12) is still a little too close to an “escape test” claim in its title and topic section. The manuscript is honest, but the wording can be skimmed as more physical than it is. Safe fix: prefer “denominator for outflow escape-versus-recycling tests” everywhere, and keep the result sentence limited to “4,440 high-excitation optical AGN candidates of 60,000; median sSFR -11.53,” with the follow-up requirement pushed to the missing-observables section.
4. **Minor**: [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex#L12) uses “measures a median Δlog sSFR” in the abstract, which is slightly too active for an association-only paper. Safe fix: change to “finds a median matched-pair offset” or “reports a median matched-pair Δlog sSFR” so the causal boundary is obvious at first glance.
5. **Improvement**: The figure captions in papers 02-09 are still boilerplate and not result-rich. They often say only that the figure “summarizes the cached optical result used for target definition,” which makes skimmers work too hard. Safe fix: replace each with a variable-specific caption that names the plotted quantities, sample size, and caveat, for example “SDSS DR17 density-proxy diagnostic showing high-density and low-density quartile quenched fractions in the 60,000-galaxy cached denominator.” Preserve every numeric value from the source-analysis JSON, do not introduce new numbers.

**Exact feed for PDF-writing pilot**
- [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex#L12): change the abstract’s second sentence to “The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and finds a median matched-pair Δlog sSFR of -1.309 dex.” Keep the third sentence’s association-only guardrail. In the conclusion, keep “selection-dependent optical association rather than evidence for causal AGN quenching.”
- [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex#L12): make the abstract and conclusion explicit that the 0.230 versus 0.181 comparison is an optical density-proxy baseline, not a full environmental-quenching result. In the figure caption, name the 10th-nearest-neighbor proxy and the quartile comparison instead of “cached optical result.”
- [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex#L12): keep the denominator framing, but tighten the abstract so it says the paper measures the available BPT-AGN fraction in massive low-sSFR hosts and does not make a heating claim. If you keep “duty-cycle denominator,” add “optical-only” in the same sentence.
- [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex#L12): rewrite the abstract’s middle sentence to “The analysis counts 4,440 high-excitation optical AGN candidates and records their median sSFR as a proxy for where resolved kinematics and multiphase-gas follow-up should focus.” Keep “not an escape-velocity measurement” verbatim. In the conclusion, say “follow-up denominator” rather than “escape/recycling work” if you want maximum skimming safety.
- [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_06_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex#L12): keep the result values, but phrase the abstract as an optical environment-stratified denominator for later radio/X-ray work, not as an implied coupling study. Caption should name the high- and low-density quartile AGN fractions and the bootstrap interval.
- [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex#L12): keep the transition-bin numbers exactly as-is, but add “optical transition diagnostic” near the result sentence and keep the causal interpretation only in the missing-observables section.
- [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex#L12): the abstract and conclusion are sound, but the figure caption should name the prevalence range and the “widest-to-narrowest” ratio explicitly so the figure is self-explanatory.
- [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_06_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex#L12): change the abstract and conclusion to use the explicit log-luminosity notation already used in the body, and add “same denominator” or “massive star-forming emission-line controls” to the offset sentence.
- [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_06_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex#L12): keep the 15-cell, `n >= 50`, 0.005-0.729, and 0.003-0.520 values unchanged, but rewrite the abstract and conclusion to say “observed target vector for later forward-model validation” and “not a direct simulation comparison.” That is the safest wording for the pilot.

**Real-data/source/citation audit notes**
- Every headline number I checked traces to `source_analysis_results.json` and matches the TeX:
  - RP-1: 8,146 matched pairs, median matched-pair offset -1.308887 dex.
  - RP-2: 60,000 rows, high-density quenched fraction 0.2304, low-density 0.1807.
  - RP-3: 9,298 massive rows, 5,695 quenched, BPT AGN fractions 0.4299 and 0.6074.
  - P1: 4,440 high-excitation AGN of 60,000, median sSFR -11.53205.
  - P2: high-density massive AGN fraction 0.5086, low-density 0.3667, bootstrap interval [0.1119, 0.1702].
  - P3: transition bin 11.0-12.5, peak AGN fraction 0.5202, quenched-fraction threshold crossed there.
  - P4: prevalence 0.136 to 0.418, ratio 3.0808.
  - P5: 6,729-row denominator, AGN fraction 0.5487, median H-alpha proxy 40.0612, offset -0.6586 dex.
  - P6: 15 mass-redshift cells with `n >= 50`, quenched fraction range 0.0053-0.7292, AGN fraction range 0.0027-0.5202.
- No invented numbers, citations, or URLs were introduced in the inspected files.
- Citation roles are mostly correct. The future-observables citations in the “missing observables” sections are used as motivation, not as evidence for the SDSS-only result. Keep them quarantined there.
- Public/live mirrored research-topic manuscripts are byte-identical on checksum for the inspected pairs, so I did not find a stale public-vs-local mismatch in those copies.

**Workflow/system notes**
- The read-only candidate TeX and the mirrored public/live research-topic manuscripts are synchronized for the inspected artifacts.
- The main provenance gap is not text drift, it is version traceability across candidate-copy TeX, public-linked manuscript pages, and the cached analysis JSON. A hash manifest tying the PDF-writing pilot output back to the exact candidate-copy TeX would make future audits cheaper.
- I did not touch the public/live roots, did not replace any PDFs, and did not attempt any publish path.

**Safety ledger**
- No file edits: yes.
- No public replacement or publish: yes.
- No DB, SQL, wiki mutation, or page-version writes: yes.
- No deploy or restart: yes.
- No git commit, push, merge, rebase, or history rewrite: yes.
- No cron changes: yes.
- No billing, cloud, OAuth, API-key, account, credential, token, or cookie access: yes.
- No external manuscript submission: yes.


# command_result
exit_code=0
elapsed_s=337.6
timed_out=False
finished_utc=2026-07-09T18:40:38Z
