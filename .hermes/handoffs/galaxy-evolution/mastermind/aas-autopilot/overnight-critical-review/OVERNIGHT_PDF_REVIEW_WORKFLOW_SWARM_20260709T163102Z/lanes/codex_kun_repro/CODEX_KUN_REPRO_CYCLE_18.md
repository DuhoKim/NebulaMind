# codex_kun_repro cycle 18
Started UTC: 2026-07-09T22:59:13Z
Model: gpt-5.4-mini
Provider: codex
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_18_codex_kun_repro.md

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
session id: 019f491b-4c23-7a12-ab9f-e0e3c1aa5c9e
--------
user
Kun/Codex read-only reproducibility, TeX, provenance, and no-mock-data audit.

Output marker: OVERNIGHT_CODEX_KUN_REPRO_CYCLE_18

Work mode: artifact-only, read-only lane. Do not edit files. Do not publish. Do not call or request credentials.

Critically review the 9 current candidate PDFs/manuscript TeX files and the public-linked research-topic manuscripts. Find the highest-value issues that should feed the candidate-copy PDF-writing pilot: overclaims, missing caveats, weak abstracts, confusing conclusion/limitations wording, citation role errors, stale public-vs-local mismatch, poor reader flow, figure/table/caption problems, and reproducibility risks. Give exact safe rewrite guidance where possible, but do not edit files.

Required output sections:
1. OVERNIGHT_CODEX_KUN_REPRO_CYCLE_18 status: PASS/ISSUES_FOUND/BLOCKED.
2. Files/paths actually inspected or, if not inspectable, paths used from context.
3. Ranked findings, with severity: blocker/major/minor/improvement.
4. Exact feed for PDF-writing pilot: concrete TeX-level edits or section rewrite instructions, preserving measured values and real-data boundaries.
5. Real-data/source/citation audit notes.
6. Workflow/system notes if relevant.
7. Safety ledger confirming no edits/public/db/deploy/git/cron/billing/OAuth/submission.

Run root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z
Cycle: 18
Candidate package: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers
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
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 232813,
    "pdf_sha256": "bc4111fe4ed03f898aa18c36a0e2b801158fe1d3f5ebbdd704d5abb569dd134d",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 87002,
    "pdf_sha256": "804894166a5d8392e0057edb80711ae8220f598653bcac85aa5b122453eeba4f",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 85303,
    "pdf_sha256": "f3708ce3faca849c976849e01e6787c0868dfc2508241df826032f9c04c32ed7",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 316739,
    "pdf_sha256": "aa8893b138e55acff9d25738754df53e99746e45a16d4ca6ee7743a946bc11a6",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 85100,
    "pdf_sha256": "fd9aaf5b71bc07fe0293ff4abf9e7e53a1dc990d7a092d74c40227bb889ed2cc",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 89798,
    "pdf_sha256": "7fdb3af1db8a52a8ba03da7f429489a1816aed1d27030a0f1469665a54f92e28",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 83036,
    "pdf_sha256": "ed02b48617cb79359c2684c5738f58be3c35f732086c260974c40d9b0257be11",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 214734,
    "pdf_sha256": "692c2ebfbb20e1e9cca6ea89a1508ba967c1665b947d745eb272267092b431bd",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 85471,
    "pdf_sha256": "b71e9ec2fe23a4001e027a15b6533a57a0f503f841135b6dbe74c3f400a646ec",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle

Deterministic inventory summary:
{
  "candidate_papers": [
    {
      "slug": "01_m1_rp1_sdss_agn_sfr",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
      "title": "Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot",
      "abstract": "We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\\Delta\\log {\\rm sSFR}=-1.309$ dex; at S/N$\\geq 10$, the corresponding matched offset is $-0.744$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.",
      "tex_sha256": "4482bfaf30b330d4d0e19c4e128ef9d4d2951d37b0e86f798c15c8fb5232af18",
      "pdf_sha256": "bc4111fe4ed03f898aa18c36a0e2b801158fe1d3f5ebbdd704d5abb569dd134d",
      "pdf_bytes": 232813
    },
    {
      "slug": "02_m1_rp2_environment_quenching",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
      "title": "SDSS density proxy for environmental quenching",
      "abstract": "We use a representative 60,000-galaxy subset of the SDSS DR17 emission-line catalog to build an optical density-proxy analysis of environmental quenching. A 10th-nearest-neighbor density proxy is compared with quenched fraction (defined by specific star-formation rate $\\log(\\mathrm{sSFR}/\\mathrm{yr}^{-1}) < -11.0$) after controlling for stellar mass and redshift; using equal-count density quartiles, the high-density quartile has quenched fraction 0.230 $\\pm$ 0.003 versus 0.181 $\\pm$ 0.003 in the low-density quartile. The bootstrap high-minus-low interval is [0.041, 0.059], which excludes zero. This analysis is intentionally limited to the optical denominator and leaves the missing group and halo information for future study.",
      "tex_sha256": "da407c3c4fc931ff80f42a5c436bbef2e3bafef12fa4ab374143214118c1c805",
      "pdf_sha256": "804894166a5d8392e0057edb80711ae8220f598653bcac85aa5b122453eeba4f",
      "pdf_bytes": 87002
    },
    {
      "slug": "03_m1_rp3_maintenance_heating",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
      "title": "Optical-AGN denominator for maintenance-heating follow-up",
      "abstract": "We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to construct an optical denominator for maintenance-heating follow-up in massive galaxies. Among massive, low-sSFR hosts, the BPT-AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects, providing a proxy for the duty-cycle denominator relevant to future X-ray or radio maintenance-heating studies. This analysis remains explicitly optical and does not attempt a calorimetric heating measurement.",
      "tex_sha256": "7ec97f04b55d8cbc8079a5695dbe6e830fcf3152b71cce54462c959289313d5a",
      "pdf_sha256": "f3708ce3faca849c976849e01e6787c0868dfc2508241df826032f9c04c32ed7",
      "pdf_bytes": 85303
    },
    {
      "slug": "04_m2_p1_outflow_escape_recycling",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
      "title": "SDSS BPT-selected optical AGN denominator for outflow escape tests",
      "abstract": "We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts 4,440 BPT-selected optical AGN candidates (0.074 $\\pm$ 0.001) and records their median $\\log {\\rm sSFR} = -11.53$ as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.",
      "tex_sha256": "b3ebd1ee76b83d1bfc8c329802fb41ffb571d9dc2d7103ed8c2eebda66939185",
      "pdf_sha256": "aa8893b138e55acff9d25738754df53e99746e45a16d4ca6ee7743a946bc11a6",
      "pdf_bytes": 316739
    },
    {
      "slug": "05_m2_p2_radio_jet_environment",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf",
      "title": "Environment proxy for optical AGN in massive SDSS hosts",
      "abstract": "We build an optical denominator for radio-jet environment follow-up using a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. In massive hosts, the high-density quartile has optical AGN fraction 0.509 $\\pm$ 0.012 and the low-density quartile has 0.367 $\\pm$ 0.012, defining an environment-stratified target set for later radio or X-ray work. The result is an optical baseline only; it does not measure jet power or coupling efficiency.",
      "tex_sha256": "2fd59d9f52a195f684f08da9e5ec82df309d30078611f1b7972009ccf784635d",
      "pdf_sha256": "fd9aaf5b71bc07fe0293ff4abf9e7e53a1dc990d7a092d74c40227bb889ed2cc",
      "pdf_bytes": 85100
    },
    {
      "slug": "06_m2_p3_feedback_transition_mass",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf",
      "title": "SDSS mass transition in quenching and optical AGN incidence",
      "abstract": "We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to identify the stellar-mass regime where quenched fraction (defined by specific star-formation rate $\\log(\\mathrm{sSFR}/\\mathrm{yr}^{-1}) < -11.0$) and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, and the first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail at $\\log(M_\\star/M_\\odot)>11.0$, where the optical AGN fraction peaks at 0.520. It does not assign the transition to stellar or AGN feedback on its own.",
      "tex_sha256": "33b0d515989b37b889f2f0eea8fa5bf92963c8b3f0ea5dd8d5e113dac0e8649e",
      "pdf_sha256": "7fdb3af1db8a52a8ba03da7f429489a1816aed1d27030a0f1469665a54f92e28",
      "pdf_bytes": 89798
    },
    {
      "slug": "07_m3_p1_multiphase_census",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf",
      "title": "Common-denominator optical tracer census in SDSS",
      "abstract": "We build a common optical denominator for a multiphase outflow census from a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. Simple tracer definitions change the inferred AGN or feedback-candidate prevalence within the same denominator, spanning 0.136--0.418 within the shared selection space, so this note focuses on the optical selection baseline needed before adding ionized, neutral, molecular, or X-ray/radio tracers. This is a denominator study, not a multiphase outflow measurement.",
      "tex_sha256": "2ef209064786246ea1858d086db3f6e31d735596330aa049bcdc0a95b4871e94",
      "pdf_sha256": "ed02b48617cb79359c2684c5738f58be3c35f732086c260974c40d9b0257be11",
      "pdf_bytes": 83036
    },
    {
      "slug": "08_m3_p2_gas_depletion_efficiency",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf",
      "title": "Optical denominator for gas-fraction versus efficiency tests",
      "abstract": "We use a 6,729-galaxy downstream subset drawn from the 60,000-galaxy SDSS DR17 emission-line cache to construct an optical selection baseline and denominator for future molecular gas-fraction versus star-formation efficiency follow-up. For massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of $0.549 \\pm 0.006$ and a median log H$\\alpha$ luminosity proxy of 40.06 erg s$^{-1}$, which is offset by $-0.66$ dex relative to massiv

Candidate paper summaries:
- slug=01_m1_rp1_sdss_agn_sfr
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf
  title=Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot
  abstract=We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\Delta\log {\rm sSFR}=-1.309$ dex; at S/N$\geq 10$, the corresponding matched offset is $-0.744$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.
- slug=02_m1_rp2_environment_quenching
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf
  title=SDSS density proxy for environmental quenching
  abstract=We use a representative 60,000-galaxy subset of the SDSS DR17 emission-line catalog to build an optical density-proxy analysis of environmental quenching. A 10th-nearest-neighbor density proxy is compared with quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) after controlling for stellar mass and redshift; using equal-count density quartiles, the high-density quartile has quenched fraction 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile. The bootstrap high-minus-low interval is [0.041, 0.059], which excludes zero. This analysis is intentionally limited to the optical denominator and leaves the missing group and halo information for future study.
- slug=03_m1_rp3_maintenance_heating
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf
  title=Optical-AGN denominator for maintenance-heating follow-up
  abstract=We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to construct an optical denominator for maintenance-heating follow-up in massive galaxies. Among massive, low-sSFR hosts, the BPT-AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects, providing a proxy for the duty-cycle denominator relevant to future X-ray or radio maintenance-heating studies. This analysis remains explicitly optical and does not attempt a calorimetric heating measurement.
- slug=04_m2_p1_outflow_escape_recycling
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf
  title=SDSS BPT-selected optical AGN denominator for outflow escape tests
  abstract=We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts 4,440 BPT-selected optical AGN candidates (0.074 $\pm$ 0.001) and records their median $\log {\rm sSFR} = -11.53$ as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
- slug=05_m2_p2_radio_jet_environment
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf
  title=Environment proxy for optical AGN in massive SDSS hosts
  abstract=We build an optical denominator for radio-jet environment follow-up using a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. In massive hosts, the high-density quartile has optical AGN fraction 0.509 $\pm$ 0.012 and the low-density quartile has 0.367 $\pm$ 0.012, defining an environment-stratified target set for later radio or X-ray work. The result is an optical baseline only; it does not measure jet power or coupling efficiency.
- slug=06_m2_p3_feedback_transition_mass
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf
  title=SDSS mass transition in quenching and optical AGN incidence
  abstract=We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to identify the stellar-mass regime where quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, and the first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail at $\log(M_\star/M_\odot)>11.0$, where the optical AGN fraction peaks at 0.520. It does not assign the transition to stellar or AGN feedback on its own.
- slug=07_m3_p1_multiphase_census
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf
  title=Common-denominator optical tracer census in SDSS
  abstract=We build a common optical denominator for a multiphase outflow census from a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. Simple tracer definitions change the inferred AGN or feedback-candidate prevalence within the same denominator, spanning 0.136--0.418 within the shared selection space, so this note focuses on the optical selection baseline needed before adding ionized, neutral, molecular, or X-ray/radio tracers. This is a denominator study, not a multiphase outflow measurement.
- slug=08_m3_p2_gas_depletion_efficiency
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf
  title=Optical denominator for gas-fraction versus efficiency tests
  abstract=We use a 6,729-galaxy downstream subset drawn from the 60,000-galaxy SDSS DR17 emission-line cache to construct an optical selection baseline and denominator for future molecular gas-fraction versus star-formation efficiency follow-up. For massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of $0.549 \pm 0.006$ and a median log H$\alpha$ luminosity proxy of 40.06 erg s$^{-1}$, which is offset by $-0.66$ dex relative to massive star-forming controls. The analysis provides an empirical baseline and candidate list for future CO or dust follow-up without claiming a physical separation of gas depletion from efficiency suppression from optical data alone.
- slug=09_m3_p3_simulation_validation
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf
  title=SDSS target vector for feedback-model validation
  abstract=We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define a compact optical target vector for forward-model validation. The pilot records quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$), optical AGN incidence, and color versus mass/redshift across 15 mass-redshift cells with $n \geq 50$; across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520. It remains an empirical denominator study rather than a direct simulation comparison.

Previous feed packet for continuity:
# PDF-writing feed cycle 17

created_utc: 2026-07-09T22:43:24Z
candidate: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers`

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
- `01_m1_rp1_sdss_agn_sfr` ok=True bytes=232641 sha256=fde07eba24931f6762ef37206637e4bf21ec981cea3947cc8052edb4c21c568b
- `02_m1_rp2_environment_quenching` ok=True bytes=86155 sha256=780e3f219c09945b486002222e60d439cdfe3347ba82e7d7a8523038a522cdb0
- `03_m1_rp3_maintenance_heating` ok=True bytes=85123 sha256=5cdbfba7b58cf1520d14fa39af3ab924dea1a816f724232f52b2fbe1905269b2
- `04_m2_p1_outflow_escape_recycling` ok=True bytes=316625 sha256=f88c9eb780e7503e10d5bec31e08e20815eb9923957d73b95d31b73184d3e9f7
- `05_m2_p2_radio_jet_environment` ok=True bytes=84916 sha256=6f93669cbe7d0db5aba582de6a6f6adb2d9130c3b5e03c8821774cdeb21579f0
- `06_m2_p3_feedback_transition_mass` ok=True bytes=89223 sha256=50785f40d53876b214a97f4b29496f944d73d9c2f01f89dcd97b429556d1054c
- `07_m3_p1_multiphase_census` ok=True bytes=82862 sha256=5d2e562b4c60b4f510871c1f2e0f80e3f61503c882daa0354e24f59d64da09ae
- `08_m3_p2_gas_depletion_efficiency` ok=True bytes=214108 sha256=37b554957b19080f3363b51dbc10c827f86657e683f31a21257d278d085f7a76
- `09_m3_p3_simulation_validation` ok=True bytes=84503 sha256=df7329bb12b46309c0c4d85bc93b50156408d62ec6ed5c70a359a2be2aeb1e20

## Lane outputs to integrate

===== codex_kun_repro (gpt-5.4-mini) exit=0 =====
# codex_kun_repro cycle 17
Started UTC: 2026-07-09T22:38:05Z
Model: gpt-5.4-mini
Provider: codex
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_17_codex_kun_repro.md

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
session id: 019f4907-f1a5-7b43-904a-3ba77c03c984
--------
user
Kun/Codex read-only reproducibility, TeX, provenance, and no-mock-data audit.

Output marker: OVERNIGHT_CODEX_KUN_REPRO_CYCLE_17

Work mode: artifact-only, read-only lane. Do not edit files. Do not publish. Do not call or request credentials.

Critically review the 9 current candidate PDFs/manuscript TeX files and the public-linked research-topic manuscripts. Find the highest-value issues that should feed the candidate-copy PDF-writing pilot: overclaims, missing caveats, weak abstracts, confusing conclusion/limitations wording, citation role errors, stale public-vs-local mismatch, poor reader flow, figure/table/caption problems, and reproducibility risks. Give exact safe rewrite guidance where possible, but do not edit files.

Required output sections:
1. OVERNIGHT_CODEX_KUN_REPRO_CYCLE_17 status: PASS/ISSUES_FOUND/BLOCKED.
2. Files/paths actually inspected or, if not inspectable, paths used from context.
3. Ranked findings, with severity: blocker/major/minor/improvement.
4. Exact feed for PDF-writing pilot: concrete TeX-level edits or section rewrite instructions, preserving measured values and real-data boundaries.
5. Real-data/source/citation audit notes.
6. Workflow/system notes if relevant.
7. Safety ledger confirming no edits/public/db/deploy/git/cron/billing/OAuth/submission.

Run root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z
Cycle: 17
Candidate package: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers
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
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 232641,
    "pdf_sha256": "fde07eba24931f6762ef37206637e4bf21ec981cea3947cc8052edb4c21c568b",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 86155,
    "pdf_sha256": "780e3f219c09945b486002222e60d439cdfe3347ba82e7d7a8523038a522cdb0",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 85123,
    "pdf_sha256": "5cdbfba7b58cf1520d14fa39af3ab924dea1a816f724232f52b2fbe1905269b2",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 316625,
    "pdf_sha256": "f88c9eb780e7503e10d5bec31e08e20815eb9923957d73b95d31b73184d3e9f7",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 84916,
    "pdf_sha256": "6f93669cbe7d0db5aba582de6a6f6adb2d9130c3b5e03c8821774cdeb21579f0",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 89223,
    "pdf_sha256": "50785f40d53876b214a97f4b29496f944d73d9c2f01f89dcd97b429556d1054c",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 82862,
    "pdf_sha256": "5d2e562b4c60b4f510871c1f2e0f80e3f61503c882daa0354e24f59d64da09ae",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 214108,
    "pdf_sha256": "37b554957b19080f3363b51dbc10c827f86657e683f31a21257d278d085f7a76",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/
[TRUNCATED at 16000 chars: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/feeds/PDF_WRITING_FEED_CYCLE_17.md]


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
I’m pulling the candidate TeX and the public-linked manuscript set first so I can compare the local writeups against the publishable/public wording and look for claim drift, caveats, and citation-role issues. After that I’ll read the highest-signal sections only: abstract, intro, conclusion, limitations, captions, and any provenance/reproducibility blocks.
exec
/bin/zsh -lc "rg --files \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers\" | sed -n '1,200p'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "rg --files \"/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution\" | sed -n '1,200p'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "rg --files \"/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution\" | sed -n '1,200p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/SOURCE_COPY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/CYCLE_18_BEFORE_RECEIPT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/CYCLE_18_BEFORE_RECEIPT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf

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
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/index.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/quintet.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/manifest.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p5-2931-dedupe-spec-20260706T151025Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/quintet.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/m3-p2-same-format-draft-20260707T050500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json.backup-before-p1-spec-20260706T101547Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/manifest-20260708T014205Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-bindings-20260708T014205Z.md.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-p1-label-fix-20260708T022147Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html.backup-before-p1-spec-20260706T101547Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p5-2931-dedupe-spec-20260706T151025Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p5-2931-dedupe-spec-20260706T151025Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p1-legacy-overclaim-disposition-spec.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
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
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/index.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/lana-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/tori-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/hwao-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/goru-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/kun-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-pdf-link-20260708T214200Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p1_multiphase_census_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p2_gas_depletion_efficiency_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p3_simulation_validation_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md.backup-before-pdf-link-20260708T214200Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/goru-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/kun-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/tori-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/hwao-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/lana-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/wiki-format-preview-evidence-trust-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/page-content-evidence-trust-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-hwao-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/REVIEW_PATCH_NOTE_v2p1_20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-hwao-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-hwao-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.html

 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/source-first-paper-adjudication/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/source-first-paper-adjudication/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/debate-map-to-wiki-rebuild/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/packet-gated-paper-to-wiki-reconciliation/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/packet-gated-paper-to-wiki-reconciliation/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/packet-gated-paper-to-wiki-reconciliation/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/tori-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/hwao-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/goru-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/kun-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/lana-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/prose-evidence-trust-deepening-20260708T043427Z/cross-method-trust-legend-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/prose-evidence-trust-deepening-20260708T043427Z/cross-method-coverage-map-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/prose-evidence-trust-deepening-20260708T043427Z/manifest-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/prose-evidence-trust-deepening-20260708T043427Z/index-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/lana-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/tori-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/hwao-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/goru-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/kun-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/manifest-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-deepening-map-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/page-content-m2-v2-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-v2-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/manifest-20260708T014205Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-bindings-20260708T014205Z.md.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-p1-label-fix-20260708T022147Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-sections.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-no-go-gap-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html.backup-before-p1-spec-20260706T101547Z
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-pages.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger-summary.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p5-2931-dedupe-spec-20260706T151025Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/quintet.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json.backup-before-p1-spec-20260706T101547Z
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger-summary.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-review-checklist.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-packet.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/wiki-format-preview-evidence-trust-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/goru-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/page-content-evidence-trust-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/kun-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/tori-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/hwao-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/lana-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-hwao-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/REVIEW_PATCH_NOTE_v2p1_20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-hwao-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-hwao-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p5-2931-dedupe-spec-20260706T151025Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p1-legacy-overclaim-disposition-spec.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/quintet.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/wiki-format-preview-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/evidence-trust-map-20260708T014205Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/page-content-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-summary.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-preserved-no-go-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_pdf_link_backups_20260708T124436Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p3_simulation_validation_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p2_gas_depletion_efficiency_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/quintet.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/m3-p2-same-format-draft-20260707T050500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p1_multiphase_census_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-citation-role-mappings.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/m1_rp2_environment_quenching_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-primary-citation-anchor-registry.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/m1_rp3_maintenance_heating_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p5-2931-dedupe-spec-20260706T151025Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html.backup-before-research-topics-link-20260708T092242Z
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T094443Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T094443Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T094443Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T094443Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p3_feedback_transition_mass_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p2_radio_jet_environment_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p1_outflow_escape_recycling_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-specificity-pass-20260708T111138Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-specificity-pass-20260708T111138Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-specificity-pass-20260708T111138Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-specificity-pass-20260708T111138Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_all_pdf_link_backups_20260708T130505Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html

codex
I’ve confirmed the candidate package has the nine TeX/PDF pairs plus per-paper source-analysis JSON, and the public tree contains both the older wiki-linked manuscript pages and the PDF-linked backups. Next I’m reading the local TeX structure and the source-analysis metadata to separate wording issues from provenance issues.
exec
/bin/zsh -lc "jq '.title, .abstract, .slug' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/CYCLE_18_BEFORE_RECEIPT.json\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
null
null
null

exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/*/data/source_analysis_results.json; do echo "### $f"; jq '"'{source_count, evidence_count, citation_count, claim_count, note_count, warnings, errors}' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json
{
  "source_count": null,
  "evidence_count": null,
  "citation_count": null,
  "claim_count": null,
  "note_count": null,
  "warnings": null,
  "errors": null
}
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/data/source_analysis_results.json
{
  "source_count": null,
  "evidence_count": null,
  "citation_count": null,
  "claim_count": null,
  "note_count": null,
  "warnings": null,
  "errors": null
}
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/data/source_analysis_results.json
{
  "source_count": null,
  "evidence_count": null,
  "citation_count": null,
  "claim_count": null,
  "note_count": null,
  "warnings": null,
  "errors": null
}
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json
{
  "source_count": null,
  "evidence_count": null,
  "citation_count": null,
  "claim_count": null,
  "note_count": null,
  "warnings": null,
  "errors": null
}
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json
{
  "source_count": null,
  "evidence_count": null,
  "citation_count": null,
  "claim_count": null,
  "note_count": null,
  "warnings": null,
  "errors": null
}
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json
{
  "source_count": null,
  "evidence_count": null,
  "citation_count": null,
  "claim_count": null,
  "note_count": null,
  "warnings": null,
  "errors": null
}
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/data/source_analysis_results.json
{
  "source_count": null,
  "evidence_count": null,
  "citation_count": null,
  "claim_count": null,
  "note_count": null,
  "warnings": null,
  "errors": null
}
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json
{
  "source_count": null,
  "evidence_count": null,
  "citation_count": null,
  "claim_count": null,
  "note_count": null,
  "warnings": null,
  "errors": null
}
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/data/source_analysis_results.json
{
  "source_count": null,
  "evidence_count": null,
  "citation_count": null,
  "claim_count": null,
  "note_count": null,
  "warnings": null,
  "errors": null
}

exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/*/aastex/*_integrated.tex; do echo "### $f"; rg -n "'"\\\\begin\\{abstract\\}|\\\\end\\{abstract\\}|\\\\section\\{|\\\\subsection\\{|limitations|Conclusion|conclusion|Future work|We (present|use|measure|find|show|do not)|causal|feedback|denominator|proxy|mock|synthetic|placeholder|toy|fig:|table:|cite\" \""'$f" | sed -n '"'1,120p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|limitations|Conclusion|conclusion|Future work|We (present|use|measure|find|show|do not)|causal|feedback|denominator|proxy|mock|synthetic|placeholder|toy|fig:|table:|cite)
                          ^^
error: unrecognized escape sequence
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|limitations|Conclusion|conclusion|Future work|We (present|use|measure|find|show|do not)|causal|feedback|denominator|proxy|mock|synthetic|placeholder|toy|fig:|table:|cite)
                          ^^
error: unrecognized escape sequence
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|limitations|Conclusion|conclusion|Future work|We (present|use|measure|find|show|do not)|causal|feedback|denominator|proxy|mock|synthetic|placeholder|toy|fig:|table:|cite)
                          ^^
error: unrecognized escape sequence
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|limitations|Conclusion|conclusion|Future work|We (present|use|measure|find|show|do not)|causal|feedback|denominator|proxy|mock|synthetic|placeholder|toy|fig:|table:|cite)
                          ^^
error: unrecognized escape sequence
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|limitations|Conclusion|conclusion|Future work|We (present|use|measure|find|show|do not)|causal|feedback|denominator|proxy|mock|synthetic|placeholder|toy|fig:|table:|cite)
                          ^^
error: unrecognized escape sequence
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|limitations|Conclusion|conclusion|Future work|We (present|use|measure|find|show|do not)|causal|feedback|denominator|proxy|mock|synthetic|placeholder|toy|fig:|table:|cite)
                          ^^
error: unrecognized escape sequence
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|limitations|Conclusion|conclusion|Future work|We (present|use|measure|find|show|do not)|causal|feedback|denominator|proxy|mock|synthetic|placeholder|toy|fig:|table:|cite)
                          ^^
error: unrecognized escape sequence
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|limitations|Conclusion|conclusion|Future work|We (present|use|measure|find|show|do not)|causal|feedback|denominator|proxy|mock|synthetic|placeholder|toy|fig:|table:|cite)
                          ^^
error: unrecognized escape sequence
### /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|limitations|Conclusion|conclusion|Future work|We (present|use|measure|find|show|do not)|causal|feedback|denominator|proxy|mock|synthetic|placeholder|toy|fig:|table:|cite)
                          ^^
error: unrecognized escape sequence

codex
The first pass shows the source-analysis JSON is effectively blank metadata, so the real review has to come from the TeX/PDF content and the public-linked manuscript text. I’m now extracting abstract/conclusion/limitations blocks and a few section headings so I can flag the exact wording that should be softened or re-ordered in the PDF-writing pilot.
exec
/bin/zsh -lc "f='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex'; nl -ba \""'$f" | sed -n '"'1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "f='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex'; nl -ba \""'$f" | sed -n '"'1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS density proxy for environmental quenching}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{SDSS density proxy for environmental quenching}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a representative 60,000-galaxy subset of the SDSS DR17 emission-line catalog to build an optical density-proxy analysis of environmental quenching. A 10th-nearest-neighbor density proxy is compared with quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) after controlling for stellar mass and redshift; using equal-count density quartiles, the high-density quartile has quenched fraction 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile. The bootstrap high-minus-low interval is [0.041, 0.059], which excludes zero. This analysis is intentionally limited to the optical denominator and leaves the missing group and halo information for future study.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	Establishing environmental quenching baselines in wide-field optical surveys is useful before applying more complex group or halo metrics. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. In this note, we evaluate a local 10th-nearest-neighbor density proxy using SDSS DR17 emission-line galaxies and restrict the scope to directly measured optical properties. Group membership and halo mass remain future observational requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note uses the same public SDSS DR17 parent selection as the companion papers, but it interprets that denominator as an environmental-quenching baseline rather than a feedback or outflow sample. The capped subset contains 60,000 emission-line galaxies from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    40	\enddata
    41	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    42	\end{deluxetable*}
    43	
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{SDSS density-proxy result for environmental quenching}\label{sec:topic-result}
    55	We examine whether a nearest-neighbor density proxy adds quenched-fraction information beyond stellar mass in the SDSS emission-line sample. The result is an optical baseline rather than a full physical-feedback test.
    56	
    57	Our SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-nearest-neighbor local density proxy. Using equal-count density quartiles, the high-density quartile exhibits a quenched fraction of $0.230 \pm 0.003$ ($3,456/15,000$) compared with $0.181 \pm 0.003$ ($2,710/15,000$) in the low-density quartile. The bootstrap high-minus-low quenched-fraction difference interval is $[0.041,0.059]$, which excludes zero. A linear probability model controlling for log stellar mass and redshift yields a high-density coefficient of $0.032 \pm 0.004$, confirming that the density proxy correlates with quenching independently of the controlled host-galaxy properties.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical density-proxy diagnostic for environmental quenching. The figure summarizes the equal-count density-quartile split, where the high-density quartile reaches a quenched fraction of 0.230 $\pm$ 0.003, establishing the baseline for future group-catalog analyses.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only baseline does not include group catalogues, robust central/satellite labels, halo masses, morphology, or multi-redshift selection functions. Those data are required before the density proxy can be interpreted as a physical environmental-quenching measurement.
    69	
    70	Because the density proxy is projected on the sky, fiber-collision and redshift-space incompleteness can dilute nearest-neighbor estimates; future group-catalog work should correct those effects explicitly.
    71	
    72	Mass and environment are known separable axes in low-redshift galaxy evolution, but a real environmental-quenching analysis requires group/halo and central-satellite information beyond this nearest-neighbor proxy \citep{peng2010,baldry2006,wetzel2013,goubert2024}.
    73	
    74	
    75	\section{Data Availability}\label{sec:data-avail}
    76	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	The SDSS-only proxy shows a high-density quenched fraction of 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile, with a mass- and redshift-adjusted high-density coefficient of $0.032 \pm 0.004$. These values define an optical environmental baseline, but a full quenching interpretation still requires group catalogs, halo masses, and central/satellite labels.
    80	
    81	\acknowledgments
    82	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    83	
    84	
    85	\begin{thebibliography}{}
    86	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    87	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    88	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    89	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    90	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    91	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    92	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    93	\bibitem[Baldry et al.(2006)]{baldry2006} Baldry, I.~K., Balogh, M.~L., Bower, R.~G., et al. 2006, MNRAS, 373, 469
    94	\bibitem[Goubert et al.(2024)]{goubert2024} Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2024, arXiv:2401.12953
    95	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
    96	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
    97	\end{thebibliography}
    98	
    99	\end{document}

 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Optical-AGN denominator for maintenance-heating follow-up}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{Optical-AGN denominator for maintenance-heating follow-up}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to construct an optical denominator for maintenance-heating follow-up in massive galaxies. Among massive, low-sSFR hosts, the BPT-AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects, providing a proxy for the duty-cycle denominator relevant to future X-ray or radio maintenance-heating studies. This analysis remains explicitly optical and does not attempt a calorimetric heating measurement.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	Maintenance-heating interpretations require X-ray or radio observables, but a rigorous optical denominator is a necessary first step. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as a duty-cycle baseline for massive, low-sSFR hosts and restrict the scope to directly measured optical quantities. X-ray cavities, radio power, and hot-gas energetics remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note reuses the shared SDSS DR17 emission-line parent selection, but it treats the resulting denominator as a maintenance-heating follow-up baseline for massive, low-sSFR hosts. The capped subset contains 60,000 galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    40	\enddata
    41	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    42	\end{deluxetable*}
    43	
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for maintenance-heating follow-up}\label{sec:topic-result}
    55	Among massive, low-sSFR SDSS emission-line galaxies, we quantify the optical AGN fraction available as a denominator for X-ray and radio maintenance-heating follow-up. The result is an optical baseline rather than a calorimetric measurement.
    56	
    57	The massive galaxy subset ($\log M_\star \geq 10.8$) contains 9,298 emission-line galaxies, of which 5,695 are classified as low-sSFR based on the specific star formation rate threshold of $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$ applied in this analysis. The optical BPT AGN fraction is measured as 0.430 in the total massive subset, rising to 0.607 when restricting the sample to massive low-sSFR objects. This empirical duty-cycle baseline is intended for future X-ray or radio maintenance-heating follow-up and is not a heating measurement.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for maintenance-heating follow-up. The figure highlights that among massive, low-sSFR objects, the BPT-AGN fraction is 0.607, providing a duty-cycle denominator for future X-ray/radio studies.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.
    69	
    70	Radio-mode and hot-atmosphere studies define the future calorimetric observables--jet power, cavities, cooling luminosity, and group gas--that are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	The massive subset contains 9,298 emission-line galaxies, with 5,695 classified as low-sSFR by the pilot threshold of $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$. The BPT AGN fraction rises from 0.430 in the massive subset to 0.607 in the massive low-sSFR subset, defining an optical duty-cycle denominator for maintenance-heating follow-up rather than a direct heating result.
    78	
    79	\acknowledgments
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
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
    91	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    92	\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, Galaxies, 12(3), 24
    93	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
    94	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
    95	\bibitem[McNamara \& Nulsen(2012)]{mcnamara2012} McNamara, B.~R., \& Nulsen, P.~E.~J. 2012, New J. Phys., 14, 055023
    96	\end{thebibliography}
    97	
    98	\end{document}

exec
/bin/zsh -lc "f='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex'; nl -ba \""'$f" | sed -n '"'1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
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
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to identify the stellar-mass regime where quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, and the first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail at $\log(M_\star/M_\odot)>11.0$, where the optical AGN fraction peaks at 0.520. It does not assign the transition to stellar or AGN feedback on its own.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	The stellar-mass scale where quenched fraction and optical AGN incidence rise together is useful as an empirical transition marker, but it is not by itself a physical-feedback measurement. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as an optical transition baseline and restrict the scope to directly measured quantities. Gas fractions, baryon deficits, and halo-scale measurements remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note reuses the shared SDSS DR17 parent selection, but it interprets the outcome as a transition-mass baseline for quenching and optical AGN incidence. The capped subset contains 60,000 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    40	\enddata
    41	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    42	\end{deluxetable*}
    43	
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for feedback-transition mass}\label{sec:topic-result}
    55	We identify the stellar-mass scale at which quenched fraction and optical AGN incidence rise together in the SDSS emission-line sample. The result is an empirical optical transition vector rather than a full physical-feedback test.
    56	
    57	The first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail, defined here as $\log(M_\star/M_\odot)>11.0$, and the optical AGN fraction peaks in that same bin at 0.520. This empirical transition vector is an optical diagnostic only; gas fractions and baryon deficits are still required before assigning the trend to stellar or AGN feedback.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure shows the high-mass tail ($\log(M_\star/M_\odot)>11.0$) where the quenched fraction exceeds 0.5 and the optical AGN fraction peaks at 0.520.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.
    69	
    70	Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	The first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail, defined here as $\log(M_\star/M_\odot)>11.0$, and the optical AGN fraction peaks at 0.520 in that same bin. These values define an optical transition vector, but gas fractions, baryon deficits, and halo-scale measurements are still needed before a causal feedback interpretation.
    78	
    79	\acknowledgments
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
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
    91	\bibitem[Baldry et al.(2004)]{baldry2004} Baldry, I.~K., Glazebrook, K., Brinkmann, J., et al. 2004, ApJ, 600, 681
    92	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    93	\bibitem[Bluck et al.(2023)]{bluck2023} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108
    94	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
    95	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
    96	\bibitem[Peng et al.(2012)]{peng2012} Peng, Y.-j., Lilly, S.~J., Renzini, A., \& Carollo, M. 2012, ApJ, 757, 4
    97	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
    98	\end{thebibliography}
    99	
   100	\end{document}

exec
/bin/zsh -lc "f='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex'; nl -ba \""'$f" | sed -n '"'1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "f='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex'; nl -ba \""'$f" | sed -n '"'1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
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
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We build an optical denominator for radio-jet environment follow-up using a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. In massive hosts, the high-density quartile has optical AGN fraction 0.509 $\pm$ 0.012 and the low-density quartile has 0.367 $\pm$ 0.012, defining an environment-stratified target set for later radio or X-ray work. The result is an optical baseline only; it does not measure jet power or coupling efficiency.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	Radio-jet environment studies require radio and X-ray data, but an optical denominator is a useful starting point. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as an environment-stratified baseline for massive hosts and restrict the analysis to directly measured optical quantities. Jet power, coupling efficiency, and hot-gas structure remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note reuses the shared SDSS DR17 emission-line denominator, but it interprets the result as an environment-stratified baseline for radio-jet follow-up in massive hosts. The capped subset contains 60,000 galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    40	\enddata
    41	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    42	\end{deluxetable*}
    43	
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for radio-jet environment follow-up}\label{sec:topic-result}
    55	We examine whether a local-density proxy modulates the optical AGN fraction in massive SDSS hosts. The result is an environment-stratified optical baseline for future radio and X-ray jet-coupling work.
    56	
    57	Among massive hosts, the high-density quartile has optical AGN fraction $0.509 \pm 0.012$, while the low-density quartile has $0.367 \pm 0.012$. The bootstrap high-minus-low interval is $[0.112,0.170]$. This is an optical/environment denominator for radio-jet coupling work and does not measure jet power or coupling efficiency.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for radio-jet environment follow-up. The figure demonstrates the environment-stratified target set, with the optical AGN fraction rising to 0.509 $\pm$ 0.012 in the high-density quartile of massive hosts.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.
    69	
    70	Because the density proxy is projected on the sky, fiber-collision and redshift-space incompleteness can dilute nearest-neighbor estimates; future radio-jet follow-up should correct those effects explicitly.
    71	
    72	The radio/X-ray/group literature motivates environment-stratified follow-up, but the present result is only an optical BPT-AGN fraction versus an internal density proxy \citep{best2005,santoro2020,mcnamara2007,eckert2024}.
    73	
    74	
    75	\section{Data Availability}\label{sec:data-avail}
    76	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	Among massive hosts, the optical AGN fraction is 0.509 $\pm$ 0.012 in the high-density quartile and 0.367 $\pm$ 0.012 in the low-density quartile, with a bootstrap difference of [0.112, 0.170]. This establishes an environment-stratified optical denominator for radio-jet coupling studies, not a direct coupling measurement.
    80	
    81	\acknowledgments
    82	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    83	
    84	
    85	\begin{thebibliography}{}
    86	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    87	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    88	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    89	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    90	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    91	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    92	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    93	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    94	\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, Galaxies, 12(3), 24
    95	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
    96	\bibitem[Santoro et al.(2020)]{santoro2020} Santoro, F., Tadhunter, C., Baron, D., Morganti, R., \& Holt, J. 2020, A\&A, 644, A54
    97	\end{thebibliography}
    98	
    99	\end{document}

 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS optical AGN/sSFR matched-control pilot}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\Delta\log {\rm sSFR}=-1.309$ dex; at S/N$\geq 10$, the corresponding matched offset is $-0.744$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	While characterizing causal feedback typically requires multi-wavelength data, establishing a rigorous optical baseline is an essential first step. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present a selection-aware matched-control pilot analyzing catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. Unmeasured quantities such as molecular gas, X-ray emission, and resolved outflows remain future observational requirements rather than claims of causal feedback.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note uses a capped subset of 60,000 SDSS DR17 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    40	\enddata
    41	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    42	\end{deluxetable*}
    43	
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
    55	BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. The cached analysis table contains 39,553 star-forming galaxies, 12,234 intermediate/composite objects, 8,146 broad optical AGN, and 67 unclassified objects.
    56	
    57	The preferred estimator matches every broad optical AGN host to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. This is an association design; controls are not matched in morphology, halo mass, gas mass, aperture scale, AGN luminosity, or duty-cycle phase.
    58	
    59	Our comparison of broad BPT optical AGN hosts versus star-forming controls at S/N$\geq 3$ matches $N=8,146$ pairs, measuring a median specific star formation rate offset of $\Delta\log {\rm sSFR}=-1.309$ dex with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Applying a moderate mass-redshift caliper of $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$ retains $N=7,867$ pairs (96.6\% target coverage) and yields a median offset of $-1.318$ dex. A deterministic matching run without replacement yields $N=7,419$ matched pairs and a median offset of $-1.446$ dex, though with poorer stellar-mass balance. Raising the line-S/N threshold to 10 leaves $N=1,530$ matched pairs and reduces the median offset to $-0.744$ dex, and a narrower [N II] Seyfert-like proxy yields $N=2,114$ pairs and a median offset of $-0.763$ dex.
    60	
    61	
    62	\begin{figure*}
    63	\centering
    64	\includegraphics[width=0.73\textwidth]{../figures/fig-bpt.pdf}
    65	\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used in the RP-1 analysis. This figure documents the optical selection and classification boundary; it does not by itself identify causal AGN feedback.}
    66	\label{fig:bpt}
    67	\end{figure*}
    68	
    69	\begin{figure*}
    70	\centering
    71	\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
    72	\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset is robust within the optical emission-line subset but remains selection- and subclass-dependent.}
    73	\label{fig:offsets}
    74	\end{figure*}
    75	
    76	
    77	\section{Data Availability}\label{sec:data-avail}
    78	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    79	
    80	\section{Conclusion}\label{sec:conclusion}
    81	In the capped SDSS DR17 emission-line subset, broad BPT optical AGN hosts show a median sSFR offset of $-1.309$ dex relative to mass--redshift matched controls, with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Although the offset amplitude is highly dependent on the emission-line selection function (decreasing to $-0.744$ dex at S/N$\geq 10$), the interval remains securely negative. These measurements establish a robust optical association baseline, which will require future molecular gas or direct outflow kinematics follow-up to isolate any causal AGN quenching mechanisms.
    82	
    83	\acknowledgments
    84	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    85	
    86	
    87	\begin{thebibliography}{}
    88	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    89	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    90	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    91	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    92	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    93	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    94	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    95	
    96	\end{thebibliography}
    97	
    98	\end{document}

exec
/bin/zsh -lc "f='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex'; nl -ba \""'$f" | sed -n '"'1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
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
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We build a common optical denominator for a multiphase outflow census from a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. Simple tracer definitions change the inferred AGN or feedback-candidate prevalence within the same denominator, spanning 0.136--0.418 within the shared selection space, so this note focuses on the optical selection baseline needed before adding ionized, neutral, molecular, or X-ray/radio tracers. This is a denominator study, not a multiphase outflow measurement.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	Multiphase outflow work requires ionized, neutral, molecular, and X-ray or radio measurements, but a common optical denominator is a practical starting point. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as that baseline and restrict the manuscript to directly measured optical quantities. The missing multiphase observables remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note reuses the shared SDSS DR17 parent selection, but it interprets the result as a common denominator for a multiphase tracer census. The capped subset contains 60,000 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    40	\enddata
    41	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    42	\end{deluxetable*}
    43	
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical census of multiphase target denominators}\label{sec:topic-result}
    55	We examine how simple optical tracer definitions change the inferred AGN and feedback-candidate prevalence within one common SDSS denominator. The result is an optical baseline for later multiphase follow-up rather than a direct multiphase measurement.
    56	
    57	Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418, a factor of 3.1. That spread shows why a common-denominator census is required, while also underscoring that the present SDSS sample cannot measure molecular, neutral, or X-ray/radio outflow phases.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for the common-denominator multiphase census. The figure illustrates how varying optical tracer definitions yields AGN candidate prevalence ranging from 0.136 to 0.418 within the same denominator.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model.
    69	
    70	A real multiphase census needs independent ionized, neutral, molecular, and energetic outflow observables; the present SDSS thresholds are an optical denominator only \citep{veilleux2005,rupke2018,cicone2014,fiore2017,feruglio2015,woo2016,bae2018}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	Within the 60,000-galaxy denominator, simple tracer definitions change prevalence from 0.136 to 0.418, a factor of 3.1. That spread shows why a common-denominator census is required, while also underscoring that the present SDSS sample cannot measure molecular, neutral, or X-ray/radio outflow phases.
    78	
    79	\acknowledgments
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
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
    91	\bibitem[Bae \& Woo(2018)]{bae2018} Bae, H.-J., \& Woo, J.-H. 2018, ApJ, 853, 185
    92	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
    93	\bibitem[Feruglio et al.(2015)]{feruglio2015} Feruglio, C., Fiore, F., Carniani, S., et al. 2015, A\&A, 583, A99
    94	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
    95	\bibitem[Rupke(2018)]{rupke2018} Rupke, D.~S.~N. 2018, Galaxies, 6, 138
    96	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
    97	\bibitem[Woo et al.(2016)]{woo2016} Woo, J.-H., Bae, H.-J., Son, D., \& Karouzos, M. 2016, ApJ, 817, 108
    98	\end{thebibliography}
    99	
   100	\end{document}

exec
/bin/zsh -lc "f='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex'; nl -ba \""'$f" | sed -n '"'1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
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
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a 6,729-galaxy downstream subset drawn from the 60,000-galaxy SDSS DR17 emission-line cache to construct an optical selection baseline and denominator for future molecular gas-fraction versus star-formation efficiency follow-up. For massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of $0.549 \pm 0.006$ and a median log H$\alpha$ luminosity proxy of 40.06 erg s$^{-1}$, which is offset by $-0.66$ dex relative to massive star-forming controls. The analysis provides an empirical baseline and candidate list for future CO or dust follow-up without claiming a physical separation of gas depletion from efficiency suppression from optical data alone.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	Gas-fraction and star-formation-efficiency interpretations require CO or dust data, but the optical denominator is the necessary starting point. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as a baseline for massive quenched or transitioning galaxies and restrict the manuscript to directly measured optical quantities. Direct molecular gas masses and aperture-matched star-formation rates remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note reuses the shared SDSS DR17 parent selection, but it interprets the result as an optical denominator for gas-fraction versus efficiency follow-up. The capped subset contains 60,000 galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities, ending with the paper-specific downstream subset.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    40	Massive quenched or transitioning subset & -- & 6,729 & -- \\
    41	\enddata
    42	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies. The final row defines the specific 6,729-galaxy subset used in this optical baseline.}
    43	\end{deluxetable*}
    44	
    45	The paper-specific downstream selection retains 6,729 massive quenched or transitioning galaxies from the cached 60,000-galaxy parent, as fixed by the cached selection manifest. That branch is the denominator used for the gas-fraction versus efficiency result below, and it is a local subset rather than a separate public DR17 count query.
    46	
    47	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    48	
    49	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    50	
    51	
    52	\section{Measurements}\label{sec:measurements}
    53	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    54	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    55	
    56	
    57	\section{Optical denominator for gas-fraction versus efficiency tests}\label{sec:topic-result}
    58	We quantify how many massive quenched or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction and depletion-time follow-up. The result is an optical baseline rather than a physical gas-depletion measurement.
    59	
    60	The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is $0.549 \pm 0.006$, and the median H$\alpha$ luminosity proxy is $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$. The median H$\alpha$ luminosity proxy is approximately 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline.
    61	
    62	
    63	\begin{figure}
    64	\centering
    65	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    66	\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure isolates the 6,729 massive quenched or transitioning galaxies, revealing an optical BPT AGN fraction of $0.549 \pm 0.006$.}
    67	\label{fig:topic}
    68	\end{figure}
    69	
    70	\section{Interpretation and missing observables}\label{sec:missing}
    71	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.
    72	
    73	Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs; optical H$\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \citep{coldgass1,coldgass2,xcoldgass2017,xgass2018}.
    74	
    75	
    76	\section{Data Availability}\label{sec:data-avail}
    77	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    78	
    79	\section{Conclusion}\label{sec:conclusion}
    80	We have mapped the optical baseline for 6,729 massive quenched or transitioning galaxies in the SDSS emission-line sample. We find a BPT AGN fraction of $0.549 \pm 0.006$ and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, approximately 0.66 dex lower than star-forming counterparts. While these quantities define the target selection denominator for future CO gas-fraction versus efficiency programs, direct molecular gas masses and aperture-matched star formation rates remain required to physically distinguish depletion from low efficiency.
    81	
    82	\acknowledgments
    83	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    84	
    85	
    86	\begin{thebibliography}{}
    87	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    88	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    89	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    90	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    91	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    92	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    93	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    94	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
    95	\bibitem[Saintonge et al.(2011a)]{coldgass1} Saintonge, A., Kauffmann, G., Kramer, C., et al. 2011a, MNRAS, 415, 32
    96	\bibitem[Saintonge et al.(2011b)]{coldgass2} Saintonge, A., Kauffmann, G., Wang, J., et al. 2011b, MNRAS, 415, 61
    97	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
    98	\end{thebibliography}
    99	
   100	\end{document}

exec
/bin/zsh -lc "f='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex'; nl -ba \""'$f" | sed -n '"'1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS BPT-selected optical AGN denominator for outflow escape tests}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{SDSS BPT-selected optical AGN denominator for outflow escape tests}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts 4,440 BPT-selected optical AGN candidates (0.074 $\pm$ 0.001) and records their median $\log {\rm sSFR} = -11.53$ as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	An optical line-ratio selection can define a useful target set for future outflow work, but it cannot measure escape or recycling on its own. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as an optical baseline for massive galaxies and restrict the scope to directly measured quantities. Resolved kinematics, halo potentials, and multiphase gas remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note keeps the shared SDSS DR17 parent selection but interprets it as an outflow-escape follow-up denominator rather than a direct outflow measurement. The capped subset contains 60,000 emission-line galaxies from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    40	\enddata
    41	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    42	\end{deluxetable*}
    43	
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for outflow escape tests}\label{sec:topic-result}
    55	This note quantifies the BPT-selected optical AGN denominator needed for future resolved-kinematics tests of escape versus recycling. The result is an optical baseline rather than a direct escape-velocity measurement. ``BPT-selected optical AGN candidates'' here means the optical AGN subset counted above; it is shorthand for the denominator, not a separate kinematic or energy measurement.
    56	
    57	BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies ($0.074 \pm 0.001$). Their median $\log {\rm sSFR}$ is $-11.53$, compared with $-10.14$ for the full denominator. This optical sample defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for outflow escape-versus-recycling follow-up. The figure summarizes the 4,440-object BPT-selected denominator and the associated median $\log {\rm sSFR} = -11.53$ used for target definition.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires resolved outflow velocities, halo potentials, molecular/ionized/neutral gas phases, and CGM recycling tracers.
    69	
    70	Wind and outflow literature specifies the missing kinematic, geometric, molecular, and multiphase measurements; these sources motivate follow-up and do not turn line-ratio selection into an escape/recycling measurement \citep{veilleux2005,cicone2014,fiore2017,carniani2017,fabian2012}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074 $\pm$ 0.001), and their median $\log {\rm sSFR}$ is -11.53 compared with -10.14 for the full denominator. The optical sample therefore defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate.
    78	
    79	\acknowledgments
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
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
    91	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
    92	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
    93	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
    94	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
    95	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
    96	\end{thebibliography}
    97	
    98	\end{document}

exec
/bin/zsh -lc "f='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex'; nl -ba \""'$f" | sed -n '"'1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
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
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define a compact optical target vector for forward-model validation. The pilot records quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$), optical AGN incidence, and color versus mass/redshift across 15 mass-redshift cells with $n \geq 50$; across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520. It remains an empirical denominator study rather than a direct simulation comparison.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	Forward-model validation requires simulation mocks, but an observational target vector is a useful starting point. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as a compact optical baseline and restrict the manuscript to directly measured quantities. Mock-observation pipelines and aperture/noise modeling remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note reuses the shared SDSS DR17 parent selection, but it interprets the result as an observational target vector for later simulation validation. The capped subset contains 60,000 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    40	\enddata
    41	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    42	\end{deluxetable*}
    43	
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical target vector for simulation validation}\label{sec:topic-result}
    55	We define a compact SDSS target vector of quenched fraction, optical AGN incidence, and color versus mass/redshift for forward-model validation. The result is an observed optical baseline rather than a full physical-feedback test.
    56	
    57	We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector, so that simple Poisson counting errors remain at or below roughly 14\%; the cell grid spans mass bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 crossed with redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520. The observed target vector is useful for simulation forward modelling, but it still requires mock-observation pipelines before any model comparison can be claimed.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-model validation target vector. The figure maps quenched fractions and optical AGN incidence across 15 mass-redshift cells for simulation forward-modeling, spanning mass bins 8.0--9.5 through 11.0--12.5 and redshift bins 0.02--0.05 through 0.08--0.12.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.
    69	
    70	Simulation suites such as TNG, EAGLE, and SIMBA define the future comparison problem; the iMaNGA observational catalog provides a complementary benchmark for mock-observation work. No simulation mock has been forward-modelled or ranked in this pilot \citep{tng2019,eagle2015,simba2019,imanga2023,donnari2021,dubois2013,dubois2016}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector, spanning mass bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 across redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520. This observed target vector is useful for simulation forward modelling, but it still requires mock-observation pipelines before any model comparison can be claimed.
    78	
    79	\acknowledgments
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
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
    91	\bibitem[Dav\'e et al.(2019)]{simba2019} Dav\'e, R., Angl\'es-Alc\'azar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
    92	\bibitem[Donnari et al.(2021)]{donnari2021} Donnari, M., Pillepich, A., Nelson, D., et al. 2021, MNRAS, 506, 4760
    93	\bibitem[Dubois et al.(2013)]{dubois2013} Dubois, Y., Gavazzi, R., Peirani, S., \& Silk, J. 2013, MNRAS, 433, 3297
    94	\bibitem[Dubois et al.(2016)]{dubois2016} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, MNRAS, 463, 3948
    95	\bibitem[Nanni et al.(2023)]{imanga2023} Nanni, L., Thomas, D., Trayford, J., et al. 2023, MNRAS, 518, 2605
    96	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
    97	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
    98	\end{thebibliography}
    99	
   100	\end{document}

codex
I’ve got the local TeX structure. The next check is the public-linked manuscript layer, because this is where stale PDF links and topic-page drift usually show up even when the candidate TeX itself is clean. I’m comparing the public markdown/HTML against the local cycle-18 wording and file names rather than assuming they stayed in sync.
exec
/bin/zsh -lc 'for f in "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.md" "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.md" "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.md"; do echo "### $f"; rg -n "sdss_agn_sfr_pilot_aas|m1_rp2_environment_quenching_aas|m1_rp3_maintenance_heating_aas|m2_p1_outflow_escape_recycling_aas|m2_p2_radio_jet_environment_aas|m2_p3_feedback_transition_mass_aas|m3_p1_multiphase_census_aas|m3_p2_gas_depletion_efficiency_aas|m3_p3_simulation_validation_aas|abstract|Conclusion|Limitations|PDF|pdf|useful|causal|feedback|selection|denominator" "$f" | sed -n '"'1,220p'; done" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc 'for f in "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.md" "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.md" "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.md"; do echo "### $f"; rg -n "sdss_agn_sfr_pilot_aas|m1_rp2_environment_quenching_aas|m1_rp3_maintenance_heating_aas|m2_p1_outflow_escape_recycling_aas|m2_p2_radio_jet_environment_aas|m2_p3_feedback_transition_mass_aas|m3_p1_multiphase_census_aas|m3_p2_gas_depletion_efficiency_aas|m3_p3_simulation_validation_aas|abstract|Conclusion|Limitations|PDF|pdf|useful|causal|feedback|selection|denominator" "$f" | sed -n '"'1,220p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
### /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.md
rg: /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.md: IO error for operation on /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.md: No such file or directory (os error 2)
### /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.md
rg: /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.md: IO error for operation on /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.md: No such file or directory (os error 2)
### /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.md
rg: /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.md: IO error for operation on /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.md: No such file or directory (os error 2)

 succeeded in 0ms:
### /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.md
rg: /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.md: IO error for operation on /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.md: No such file or directory (os error 2)
### /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.md
rg: /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.md: IO error for operation on /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.md: No such file or directory (os error 2)
### /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.md
rg: /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.md: IO error for operation on /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.md: No such file or directory (os error 2)

exec
/bin/zsh -lc 'for f in "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/manifest.json" "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/manifest.json" "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json" "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json"; do echo "### $f"; jq '"'. | {generated_at, version, count:(.items|length), items:[.items[]? | {slug,title,pdf,md}] }' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
### /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/manifest.json
{
  "generated_at": null,
  "version": null,
  "count": 0,
  "items": []
}
### /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/manifest.json
{
  "generated_at": null,
  "version": null,
  "count": 0,
  "items": []
}
### /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json
{
  "generated_at": null,
  "version": null,
  "count": 0,
  "items": []
}
### /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json
{
  "generated_at": null,
  "version": null,
  "count": 0,
  "items": []
}

codex
The public tree is organized one layer deeper than the root file names suggest, so I’m switching to the exact manuscript subdirectories now. I’m checking whether those pages still point at stale PDF artifacts or if they’ve already been updated to the current candidate names.
exec
/bin/zsh -lc 'for d in "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z" "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z" "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z"; do echo "### $d"; ls "$d"; done' in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc 'for d in "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z" "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z" "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z"; do echo "### $d"; ls "$d"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
### /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z
m2_p1_outflow_escape_recycling_aas.pdf
m2_p2_radio_jet_environment_aas.pdf
m2_p3_feedback_transition_mass_aas.pdf
manifest-20260708T090359Z.json
research-topic-map-20260708T090359Z.json
research-topics-from-wiki-20260708T090359Z.html
research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
research-topics-from-wiki-20260708T090359Z.md
sdss_agn_sfr_pilot_aas.pdf
### /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z
m1_rp2_environment_quenching_aas.pdf
m1_rp3_maintenance_heating_aas.pdf
manifest-20260708T090359Z.json
research-topic-map-20260708T090359Z.json
research-topics-from-wiki-20260708T090359Z.html
research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
research-topics-from-wiki-20260708T090359Z.md
sdss_agn_sfr_pilot_aas.pdf
### /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z
m3_p1_multiphase_census_aas.pdf
m3_p2_gas_depletion_efficiency_aas.pdf
m3_p3_simulation_validation_aas.pdf
manifest-20260708T090359Z.json
research-topic-map-20260708T090359Z.json
research-topics-from-wiki-20260708T090359Z.html
research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
research-topics-from-wiki-20260708T090359Z.md
sdss_agn_sfr_pilot_aas.pdf

 succeeded in 0ms:
### /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z
m2_p1_outflow_escape_recycling_aas.pdf
m2_p2_radio_jet_environment_aas.pdf
m2_p3_feedback_transition_mass_aas.pdf
manifest-20260708T090359Z.json
research-topic-map-20260708T090359Z.json
research-topics-from-wiki-20260708T090359Z.html
research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
research-topics-from-wiki-20260708T090359Z.html.backup-before-pdf-link-20260708T214200Z
research-topics-from-wiki-20260708T090359Z.md
research-topics-from-wiki-20260708T090359Z.md.backup-before-pdf-link-20260708T214200Z
sdss_agn_sfr_pilot_aas.pdf
### /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z
m1_rp2_environment_quenching_aas.pdf
m1_rp3_maintenance_heating_aas.pdf
manifest-20260708T090359Z.json
research-topic-map-20260708T090359Z.json
research-topics-from-wiki-20260708T090359Z.html
research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
research-topics-from-wiki-20260708T090359Z.html.backup-before-pdf-link-20260708T214200Z
research-topics-from-wiki-20260708T090359Z.md
research-topics-from-wiki-20260708T090359Z.md.backup-before-pdf-link-20260708T214200Z
sdss_agn_sfr_pilot_aas.pdf
### /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z
m3_p1_multiphase_census_aas.pdf
m3_p2_gas_depletion_efficiency_aas.pdf
m3_p3_simulation_validation_aas.pdf
manifest-20260708T090359Z.json
research-topic-map-20260708T090359Z.json
research-topics-from-wiki-20260708T090359Z.html
research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
research-topics-from-wiki-20260708T090359Z.html.backup-before-pdf-link-20260708T214200Z
research-topics-from-wiki-20260708T090359Z.md
research-topics-from-wiki-20260708T090359Z.md.backup-before-pdf-link-20260708T214200Z
sdss_agn_sfr_pilot_aas.pdf

exec
/bin/zsh -lc 'for f in "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md" "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md" "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md"; do echo "### $f"; rg -n "sdss_agn_sfr_pilot_aas|m1_rp2_environment_quenching_aas|m1_rp3_maintenance_heating_aas|m2_p1_outflow_escape_recycling_aas|m2_p2_radio_jet_environment_aas|m2_p3_feedback_transition_mass_aas|m3_p1_multiphase_census_aas|m3_p2_gas_depletion_efficiency_aas|m3_p3_simulation_validation_aas|abstract|Conclusion|Limitations|pdf|PDF|causal|feedback|selection|denominator" "$f" | sed -n '"'1,220p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
### /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on outflows and feedback regimes
3:> This page presents three proposal-style research programmes on outflow fate, jet coupling, and the transition from stellar-feedback to AGN-linked regulation. The proposals are framed around measurable observables, matched denominators, and explicit decision criteria.
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- P1: [SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot (PDF)](m2_p1_outflow_escape_recycling_aas.pdf)
8:- P2: [Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot (PDF)](m2_p2_radio_jet_environment_aas.pdf)
9:- P3: [SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot (PDF)](m2_p3_feedback_transition_mass_aas.pdf)
15:**Hypothesis / objective.** A substantial fraction of AGN-driven outflowing gas remains gravitationally bound and recycles through the circumgalactic medium, limiting the permanence of feedback-driven gas removal.
18:- Quasar observations show AGN feedback acting on molecular gas reservoirs at high redshift, but such detections do not determine whether gas escapes the halo. [quasar molecular-gas reservoirs](https://arxiv.org/abs/1706.08987).
19:- Stellar-feedback work on baryon deficiency in low-mass galaxies provides a boundary condition for non-AGN removal channels that must not be confused with AGN-driven escape. [stellar feedback and baryon deficiency](https://arxiv.org/abs/2512.05584).
20:- Simulated galaxy feedback constraints highlight that gas removal, recycling, and observable baryon fractions depend on halo scale. [simulated observable feedback constraints](https://arxiv.org/abs/0901.1880).
26:**Analysis/test and decision criterion.** Compare outflow velocity distributions with halo escape velocities inferred from dynamical/halo-mass estimates, then model escaped versus bound/recycling fractions as a function of stellar mass, halo mass, and redshift. A high escaped fraction at fixed denominator supports permanent-removal feedback; a low escaped fraction supports recycling-limited regulation.
28:**Limitations and wording guardrails.** Projection, phase conversion, and uncertain halo potentials can dominate the escaped-fraction error budget.
35:- Young radio galaxies show AGN-driven outflows and provide an empirical route to estimating feedback efficiency. [young radio galaxies and feedback efficiency](https://arxiv.org/abs/2009.11175).
36:- Local M51-scale NOEMA data show how jet/AGN activity can affect molecular ISM structure at high spatial resolution, motivating a broader population test. [SWAN IV molecular ISM feedback](https://arxiv.org/abs/2604.15438).
37:- Galaxy-group feedback studies identify the group regime as a strong testbed for coupling between radio activity and hot gas. [group-scale AGN feedback](https://arxiv.org/abs/2403.17145).
45:**Limitations and wording guardrails.** Radio-to-jet-power conversions are uncertain; coupling estimates must be reported with systematic floors.
47:## P3 — Locating the transition from stellar-feedback to AGN-feedback regulation
49:**Hypothesis / objective.** There is a stellar/halo-mass regime where stellar-feedback momentum and energy budgets cease to explain gas loss or quiescence, and AGN-linked observables become necessary to reproduce the measured quenched fraction and baryon deficit.
52:- Low-mass baryon deficiency attributed to stellar feedback provides the low-mass endpoint of the transition problem. [stellar-feedback baryon deficiency](https://arxiv.org/abs/2512.05584).
54:- Simulated observable-property constraints show why feedback-regime boundaries must be tested against measured baryonic properties. [feedback constraints in simulated galaxies](https://arxiv.org/abs/0901.1880).
56:**Remaining uncertainty.** The observational crossover mass between stellar-feedback-dominated regulation and AGN-linked regulation is not cleanly measured with the same denominator and gas observables.
60:**Analysis/test and decision criterion.** Fit a broken-slope or transition model for gas fraction, baryon deficit, and quenched fraction as functions of stellar/halo mass while including AGN incidence and stellar-feedback proxies. The transition is credible only if the AGN-linked term improves predictive power above the stellar-feedback model at high mass.
62:**Limitations and wording guardrails.** Halo-mass uncertainties and selection functions can smear the transition; results should be framed as a probability surface, not a single universal mass.
### /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on AGN feedback, quenching, and environment
3:> This page presents three proposal-style research programmes on galaxy quenching and feedback. Each proposal states a falsifiable objective, the prior evidence motivating it, the unresolved measurement, the proposed survey data, the analysis test, and the wording limits that keep the conclusion appropriately bounded.
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- RP-1: [A Matched-Control SDSS DR17 Pilot Test of Specific Star Formation in Optical AGN Hosts (PDF)](sdss_agn_sfr_pilot_aas.pdf)
8:- RP-2: [SDSS density proxy for environmental quenching: an SDSS DR17 pilot (PDF)](m1_rp2_environment_quenching_aas.pdf)
9:- RP-3: [Optical-AGN denominator for maintenance-heating follow-up: an SDSS DR17 pilot (PDF)](m1_rp3_maintenance_heating_aas.pdf)
13:## RP-1 — Observational constraints on the suppression of star formation by AGN feedback
15:**Hypothesis / objective.** AGN hosts exhibit a measurable star-formation deficit relative to inactive galaxies matched in stellar mass, morphology, halo environment, and redshift only when the feedback energy budget can couple to the molecular or ionized gas reservoir.
18:- M51-scale NOEMA evidence motivates a spatially resolved test of how AGN activity perturbs the local interstellar medium, but a nearby case cannot by itself establish population-level quenching. [SWAN IV / M51 AGN feedback](https://arxiv.org/abs/2604.15438).
19:- High-redshift quasar observations directly connect AGN activity to disturbed molecular gas reservoirs, motivating a molecular-gas denominator for any causal quenching test. [quasar molecular-gas reservoir evidence](https://arxiv.org/abs/1706.08987).
20:- The local coverage record still treats the broad causal AGN-quenching statement as unsettled, so the proposal must test causality rather than restate it as established. [local coverage record for broad AGN-quenching statement](../prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-hwao-20260708T043427Z.json).
26:**Analysis/test and decision criterion.** Fit a hierarchical matched-control model in which resolved star-formation deficit, gas fraction, and depletion time are predicted by AGN power after controlling for mass, morphology, and environment. The hypothesis is supported only if the AGN coefficient remains significant and the inferred energy budget can plausibly affect the measured gas phase; otherwise the result bounds or rejects a causal interpretation.
28:**Limitations and wording guardrails.** AGN duty cycles, obscuration, and residual matching errors can mimic causal suppression; the result should be framed as a constraint on feedback coupling, not a proof of universal AGN quenching.
45:**Limitations and wording guardrails.** Group membership and halo masses are noisy, and pre-processing can be misclassified as cluster quenching; results should be reported as a transition map with uncertainty bands.
52:- Observed/simulated central-galaxy comparisons support integrated AGN feedback as relevant to quenching but do not by themselves measure a population duty cycle. [central-galaxy quenching and integrated AGN feedback](https://arxiv.org/abs/2112.07672).
53:- IllustrisTNG quenched-fraction work identifies AGN feedback, environment, and preprocessing as separable model ingredients, motivating observational tests rather than simulation restatement. [IllustrisTNG quenched fractions](https://arxiv.org/abs/2008.00005).
54:- Galaxy groups are highlighted as a sensitive regime for testing AGN feedback energetics in hot atmospheres. [galaxy groups as AGN feedback probes](https://arxiv.org/abs/2403.17145).
55:- Chaotic cold accretion and dual jet-heating models provide mechanisms for self-regulated heating that require observational duty-cycle constraints. [chaotic cold accretion](https://arxiv.org/abs/1301.3130); [dual jet/heating feedback](https://arxiv.org/abs/1108.0110).
63:**Limitations and wording guardrails.** Cavity detectability and age estimates bias toward energetic systems; nondetections must enter the model rather than be dropped.
### /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on feedback tracers and model validation
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- P1: [Common-denominator optical tracer census in SDSS: an SDSS DR17 pilot (PDF)](m3_p1_multiphase_census_aas.pdf)
8:- P2: [Optical denominator for gas-fraction versus efficiency tests: an SDSS DR17 pilot (PDF)](m3_p2_gas_depletion_efficiency_aas.pdf)
9:- P3: [SDSS target vector for feedback-model validation: an SDSS DR17 pilot (PDF)](m3_p3_simulation_validation_aas.pdf)
13:## P1 — A multiphase, common-denominator census of AGN-driven outflows
15:**Hypothesis / objective.** The inferred frequency and impact of AGN outflows depend strongly on gas phase, and a common-denominator multiphase census will change which feedback conclusions are supportable.
20:- The local evidence summary includes AGN/outflow debate anchors that should be treated as provenance, not as a complete population denominator. [Method 3 AGN evidence anchor](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#agn).
26:**Analysis/test and decision criterion.** Recompute outflow occurrence, mass-loading, and kinetic power under a common selection denominator and aperture model. The claim that AGN outflows are common or important is supportable only for phases and mass/redshift ranges where tracer-corrected occurrence remains high.
28:**Limitations and wording guardrails.** Mass conversion factors differ by phase; avoid combining phase-specific mass outflow rates without explicit conversion uncertainties.
37:- Environment/AGN comparisons against SDSS motivate separating gas supply, environment, and internal feedback rather than treating quenching as one scalar outcome. [environment and AGN quenching versus SDSS](https://arxiv.org/abs/2401.12953).
39:**Remaining uncertainty.** A quenched galaxy can have little gas or inefficient star formation in the gas it retains; those mechanisms imply different feedback and replenishment physics.
45:**Limitations and wording guardrails.** CO-to-H2 conversion, aperture mismatch, and SFR timescale indicators must be propagated into the decision criterion.
47:## P3 — Forward-modelled validation of cosmological feedback prescriptions
49:**Hypothesis / objective.** If subgrid feedback prescriptions are correct, forward-modelled mock observations from simulations should reproduce observed gas fractions, quenched fractions, outflow tracers, and morphology distributions under the same selection functions.
52:- IllustrisTNG quenched-fraction analyses explicitly tie quenching outcomes to AGN feedback, environment, and preprocessing in simulations. [IllustrisTNG quenched fractions](https://arxiv.org/abs/2008.00005).
53:- Horizon-AGN links AGN feedback to morphological diversity, making morphology a testable output rather than background context. [Horizon-AGN morphology and AGN feedback](https://arxiv.org/abs/1606.03086).
56:**Remaining uncertainty.** Simulations are often compared to derived quantities rather than to observables passed through the same survey selection, aperture, and sensitivity functions.
60:**Analysis/test and decision criterion.** Generate survey-matched mocks and compare joint distributions of gas fraction, quenched fraction, morphology, outflow incidence, and halo environment. A feedback model is constrained when residuals exceed observational uncertainties in a physically coherent subset of observables.
62:**Limitations and wording guardrails.** Different subgrid models can produce degenerate macroscopic observables; results should report which observables discriminate rather than ranking simulations globally.

exec
/bin/zsh -lc 'for f in "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md" "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md" "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md"; do echo "### $f"; rg -n "sdss_agn_sfr_pilot_aas|m1_rp2_environment_quenching_aas|m1_rp3_maintenance_heating_aas|m2_p1_outflow_escape_recycling_aas|m2_p2_radio_jet_environment_aas|m2_p3_feedback_transition_mass_aas|m3_p1_multiphase_census_aas|m3_p2_gas_depletion_efficiency_aas|m3_p3_simulation_validation_aas|abstract|Conclusion|Limitations|pdf|PDF|causal|feedback|selection|denominator" "$f" | sed -n '"'1,220p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
### /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on outflows and feedback regimes
3:> This page presents three proposal-style research programmes on outflow fate, jet coupling, and the transition from stellar-feedback to AGN-linked regulation. The proposals are framed around measurable observables, matched denominators, and explicit decision criteria.
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- P1: [SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot (PDF)](m2_p1_outflow_escape_recycling_aas.pdf)
8:- P2: [Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot (PDF)](m2_p2_radio_jet_environment_aas.pdf)
9:- P3: [SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot (PDF)](m2_p3_feedback_transition_mass_aas.pdf)
15:**Hypothesis / objective.** A substantial fraction of AGN-driven outflowing gas remains gravitationally bound and recycles through the circumgalactic medium, limiting the permanence of feedback-driven gas removal.
18:- Quasar observations show AGN feedback acting on molecular gas reservoirs at high redshift, but such detections do not determine whether gas escapes the halo. [quasar molecular-gas reservoirs](https://arxiv.org/abs/1706.08987).
19:- Stellar-feedback work on baryon deficiency in low-mass galaxies provides a boundary condition for non-AGN removal channels that must not be confused with AGN-driven escape. [stellar feedback and baryon deficiency](https://arxiv.org/abs/2512.05584).
20:- Simulated galaxy feedback constraints highlight that gas removal, recycling, and observable baryon fractions depend on halo scale. [simulated observable feedback constraints](https://arxiv.org/abs/0901.1880).
26:**Analysis/test and decision criterion.** Compare outflow velocity distributions with halo escape velocities inferred from dynamical/halo-mass estimates, then model escaped versus bound/recycling fractions as a function of stellar mass, halo mass, and redshift. A high escaped fraction at fixed denominator supports permanent-removal feedback; a low escaped fraction supports recycling-limited regulation.
28:**Limitations and wording guardrails.** Projection, phase conversion, and uncertain halo potentials can dominate the escaped-fraction error budget.
35:- Young radio galaxies show AGN-driven outflows and provide an empirical route to estimating feedback efficiency. [young radio galaxies and feedback efficiency](https://arxiv.org/abs/2009.11175).
36:- Local M51-scale NOEMA data show how jet/AGN activity can affect molecular ISM structure at high spatial resolution, motivating a broader population test. [SWAN IV molecular ISM feedback](https://arxiv.org/abs/2604.15438).
37:- Galaxy-group feedback studies identify the group regime as a strong testbed for coupling between radio activity and hot gas. [group-scale AGN feedback](https://arxiv.org/abs/2403.17145).
45:**Limitations and wording guardrails.** Radio-to-jet-power conversions are uncertain; coupling estimates must be reported with systematic floors.
47:## P3 — Locating the transition from stellar-feedback to AGN-feedback regulation
49:**Hypothesis / objective.** There is a stellar/halo-mass regime where stellar-feedback momentum and energy budgets cease to explain gas loss or quiescence, and AGN-linked observables become necessary to reproduce the measured quenched fraction and baryon deficit.
52:- Low-mass baryon deficiency attributed to stellar feedback provides the low-mass endpoint of the transition problem. [stellar-feedback baryon deficiency](https://arxiv.org/abs/2512.05584).
54:- Simulated observable-property constraints show why feedback-regime boundaries must be tested against measured baryonic properties. [feedback constraints in simulated galaxies](https://arxiv.org/abs/0901.1880).
56:**Remaining uncertainty.** The observational crossover mass between stellar-feedback-dominated regulation and AGN-linked regulation is not cleanly measured with the same denominator and gas observables.
60:**Analysis/test and decision criterion.** Fit a broken-slope or transition model for gas fraction, baryon deficit, and quenched fraction as functions of stellar/halo mass while including AGN incidence and stellar-feedback proxies. The transition is credible only if the AGN-linked term improves predictive power above the stellar-feedback model at high mass.
62:**Limitations and wording guardrails.** Halo-mass uncertainties and selection functions can smear the transition; results should be framed as a probability surface, not a single universal mass.
### /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on AGN feedback, quenching, and environment
3:> This page presents three proposal-style research programmes on galaxy quenching and feedback. Each proposal states a falsifiable objective, the prior evidence motivating it, the unresolved measurement, the proposed survey data, the analysis test, and the wording limits that keep the conclusion appropriately bounded.
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- RP-1: [A Matched-Control SDSS DR17 Pilot Test of Specific Star Formation in Optical AGN Hosts (PDF)](sdss_agn_sfr_pilot_aas.pdf)
8:- RP-2: [SDSS density proxy for environmental quenching: an SDSS DR17 pilot (PDF)](m1_rp2_environment_quenching_aas.pdf)
9:- RP-3: [Optical-AGN denominator for maintenance-heating follow-up: an SDSS DR17 pilot (PDF)](m1_rp3_maintenance_heating_aas.pdf)
13:## RP-1 — Observational constraints on the suppression of star formation by AGN feedback
15:**Hypothesis / objective.** AGN hosts exhibit a measurable star-formation deficit relative to inactive galaxies matched in stellar mass, morphology, halo environment, and redshift only when the feedback energy budget can couple to the molecular or ionized gas reservoir.
18:- M51-scale NOEMA evidence motivates a spatially resolved test of how AGN activity perturbs the local interstellar medium, but a nearby case cannot by itself establish population-level quenching. [SWAN IV / M51 AGN feedback](https://arxiv.org/abs/2604.15438).
19:- High-redshift quasar observations directly connect AGN activity to disturbed molecular gas reservoirs, motivating a molecular-gas denominator for any causal quenching test. [quasar molecular-gas reservoir evidence](https://arxiv.org/abs/1706.08987).
20:- The local coverage record still treats the broad causal AGN-quenching statement as unsettled, so the proposal must test causality rather than restate it as established. [local coverage record for broad AGN-quenching statement](../prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-hwao-20260708T043427Z.json).
26:**Analysis/test and decision criterion.** Fit a hierarchical matched-control model in which resolved star-formation deficit, gas fraction, and depletion time are predicted by AGN power after controlling for mass, morphology, and environment. The hypothesis is supported only if the AGN coefficient remains significant and the inferred energy budget can plausibly affect the measured gas phase; otherwise the result bounds or rejects a causal interpretation.
28:**Limitations and wording guardrails.** AGN duty cycles, obscuration, and residual matching errors can mimic causal suppression; the result should be framed as a constraint on feedback coupling, not a proof of universal AGN quenching.
45:**Limitations and wording guardrails.** Group membership and halo masses are noisy, and pre-processing can be misclassified as cluster quenching; results should be reported as a transition map with uncertainty bands.
52:- Observed/simulated central-galaxy comparisons support integrated AGN feedback as relevant to quenching but do not by themselves measure a population duty cycle. [central-galaxy quenching and integrated AGN feedback](https://arxiv.org/abs/2112.07672).
53:- IllustrisTNG quenched-fraction work identifies AGN feedback, environment, and preprocessing as separable model ingredients, motivating observational tests rather than simulation restatement. [IllustrisTNG quenched fractions](https://arxiv.org/abs/2008.00005).
54:- Galaxy groups are highlighted as a sensitive regime for testing AGN feedback energetics in hot atmospheres. [galaxy groups as AGN feedback probes](https://arxiv.org/abs/2403.17145).
55:- Chaotic cold accretion and dual jet-heating models provide mechanisms for self-regulated heating that require observational duty-cycle constraints. [chaotic cold accretion](https://arxiv.org/abs/1301.3130); [dual jet/heating feedback](https://arxiv.org/abs/1108.0110).
63:**Limitations and wording guardrails.** Cavity detectability and age estimates bias toward energetic systems; nondetections must enter the model rather than be dropped.
### /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on feedback tracers and model validation
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- P1: [Common-denominator optical tracer census in SDSS: an SDSS DR17 pilot (PDF)](m3_p1_multiphase_census_aas.pdf)
8:- P2: [Optical denominator for gas-fraction versus efficiency tests: an SDSS DR17 pilot (PDF)](m3_p2_gas_depletion_efficiency_aas.pdf)
9:- P3: [SDSS target vector for feedback-model validation: an SDSS DR17 pilot (PDF)](m3_p3_simulation_validation_aas.pdf)
13:## P1 — A multiphase, common-denominator census of AGN-driven outflows
15:**Hypothesis / objective.** The inferred frequency and impact of AGN outflows depend strongly on gas phase, and a common-denominator multiphase census will change which feedback conclusions are supportable.
20:- The local evidence summary includes AGN/outflow debate anchors that should be treated as provenance, not as a complete population denominator. [Method 3 AGN evidence anchor](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#agn).
26:**Analysis/test and decision criterion.** Recompute outflow occurrence, mass-loading, and kinetic power under a common selection denominator and aperture model. The claim that AGN outflows are common or important is supportable only for phases and mass/redshift ranges where tracer-corrected occurrence remains high.
28:**Limitations and wording guardrails.** Mass conversion factors differ by phase; avoid combining phase-specific mass outflow rates without explicit conversion uncertainties.
37:- Environment/AGN comparisons against SDSS motivate separating gas supply, environment, and internal feedback rather than treating quenching as one scalar outcome. [environment and AGN quenching versus SDSS](https://arxiv.org/abs/2401.12953).
39:**Remaining uncertainty.** A quenched galaxy can have little gas or inefficient star formation in the gas it retains; those mechanisms imply different feedback and replenishment physics.
45:**Limitations and wording guardrails.** CO-to-H2 conversion, aperture mismatch, and SFR timescale indicators must be propagated into the decision criterion.
47:## P3 — Forward-modelled validation of cosmological feedback prescriptions
49:**Hypothesis / objective.** If subgrid feedback prescriptions are correct, forward-modelled mock observations from simulations should reproduce observed gas fractions, quenched fractions, outflow tracers, and morphology distributions under the same selection functions.
52:- IllustrisTNG quenched-fraction analyses explicitly tie quenching outcomes to AGN feedback, environment, and preprocessing in simulations. [IllustrisTNG quenched fractions](https://arxiv.org/abs/2008.00005).
53:- Horizon-AGN links AGN feedback to morphological diversity, making morphology a testable output rather than background context. [Horizon-AGN morphology and AGN feedback](https://arxiv.org/abs/1606.03086).
56:**Remaining uncertainty.** Simulations are often compared to derived quantities rather than to observables passed through the same survey selection, aperture, and sensitivity functions.
60:**Analysis/test and decision criterion.** Generate survey-matched mocks and compare joint distributions of gas fraction, quenched fraction, morphology, outflow incidence, and halo environment. A feedback model is constrained when residuals exceed observational uncertainties in a physically coherent subset of observables.
62:**Limitations and wording guardrails.** Different subgrid models can produce degenerate macroscopic observables; results should report which observables discriminate rather than ranking simulations globally.

codex
I’ve confirmed the public manuscripts still use the older proposal-style naming and PDF aliases, while the local candidate package is on the integrated cycle-18 file names. I’m now checking the provenance artifacts and the diff between cycle 17 and 18 so I can separate genuine content issues from routine file-renaming drift.
exec
/bin/zsh -lc "jq '{source_copy:.source_copy, generated_at, cycle, papers:[.papers[]? | {slug, tex_sha256, pdf_sha256, pdf_bytes}]}' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/SOURCE_COPY.json\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "source_copy": null,
  "generated_at": null,
  "cycle": 18,
  "papers": []
}

exec
/bin/zsh -lc "jq '.' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/CYCLE_18_BEFORE_RECEIPT.json\" | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "all_ok": true,
  "created_utc": "2026-07-09T22:58:41Z",
  "label": "before",
  "results": [
    {
      "fatal_markers": [],
      "header": "%PDF",
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.overnight.compile.log",
      "ok": true,
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
      "pdf_bytes": 232813,
      "pdf_sha256": "bc4111fe4ed03f898aa18c36a0e2b801158fe1d3f5ebbdd704d5abb569dd134d",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex"
    },
    {
      "fatal_markers": [],
      "header": "%PDF",
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.overnight.compile.log",
      "ok": true,
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
      "pdf_bytes": 87002,
      "pdf_sha256": "804894166a5d8392e0057edb80711ae8220f598653bcac85aa5b122453eeba4f",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex"
    },
    {
      "fatal_markers": [],
      "header": "%PDF",
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.overnight.compile.log",
      "ok": true,
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
      "pdf_bytes": 85303,
      "pdf_sha256": "f3708ce3faca849c976849e01e6787c0868dfc2508241df826032f9c04c32ed7",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex"
    },
    {
      "fatal_markers": [],
      "header": "%PDF",
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.overnight.compile.log",
      "ok": true,
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
      "pdf_bytes": 316739,
      "pdf_sha256": "aa8893b138e55acff9d25738754df53e99746e45a16d4ca6ee7743a946bc11a6",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex"
    },
    {
      "fatal_markers": [],
      "header": "%PDF",
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.overnight.compile.log",
      "ok": true,
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf",
      "pdf_bytes": 85100,
      "pdf_sha256": "fd9aaf5b71bc07fe0293ff4abf9e7e53a1dc990d7a092d74c40227bb889ed2cc",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex"
    },
    {
      "fatal_markers": [],
      "header": "%PDF",
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.overnight.compile.log",
      "ok": true,
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf",
      "pdf_bytes": 89798,
      "pdf_sha256": "7fdb3af1db8a52a8ba03da7f429489a1816aed1d27030a0f1469665a54f92e28",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex"
    },
    {
      "fatal_markers": [],
      "header": "%PDF",
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.overnight.compile.log",
      "ok": true,
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf",
      "pdf_bytes": 83036,
      "pdf_sha256": "ed02b48617cb79359c2684c5738f58be3c35f732086c260974c40d9b0257be11",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex"
    },
    {
      "fatal_markers": [],
      "header": "%PDF",
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.overnight.compile.log",
      "ok": true,
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf",
      "pdf_bytes": 214734,
      "pdf_sha256": "692c2ebfbb20e1e9cca6ea89a1508ba967c1665b947d745eb272267092b431bd",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex"
    },
    {
      "fatal_markers": [],
      "header": "%PDF",
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.overnight.compile.log",
      "ok": true,
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf",
      "pdf_bytes": 85471,
      "pdf_sha256": "b71e9ec2fe23a4001e027a15b6533a57a0f503f841135b6dbe74c3f400a646ec",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex"
    }
  ]
}

exec
/bin/zsh -lc "diff -u \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex\" | sed -n '1,220p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/*/aastex/*_integrated.tex; do echo "### $(basename "$f")"; rg -n "Dubois|Dubrois|citet|citep|citeauthor|figure|table|caption|label|ref'"\\{|eqref\\{|appendix|limitations|missing|future-data|causal|model comparison|selection dependent|representativeness\" \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
### m1_rp1_sdss_agn_sfr_integrated.tex
15:We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\Delta\log {\rm sSFR}=-1.309$ dex; at S/N$\geq 10$, the corresponding matched offset is $-0.744$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.
21:\section{Introduction}\label{sec:introduction}
22:While characterizing causal feedback typically requires multi-wavelength data, establishing a rigorous optical baseline is an essential first step. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present a selection-aware matched-control pilot analyzing catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. Unmeasured quantities such as molecular gas, X-ray emission, and resolved outflows remain future observational requirements rather than claims of causal feedback.
25:\section{Data and Sample Selection}\label{sec:shared-selection}
28:\begin{deluxetable*}{lrrr}
29:\tabletypesize{\scriptsize}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
31:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
41:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
42:\end{deluxetable*}
44:The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
46:Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
55:BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. The cached analysis table contains 39,553 star-forming galaxies, 12,234 intermediate/composite objects, 8,146 broad optical AGN, and 67 unclassified objects.
62:\begin{figure*}
64:\includegraphics[width=0.73\textwidth]{../figures/fig-bpt.pdf}
65:\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used in the RP-1 analysis. This figure documents the optical selection and classification boundary; it does not by itself identify causal AGN feedback.}
66:\label{fig:bpt}
67:\end{figure*}
69:\begin{figure*}
71:\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
72:\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset is robust within the optical emission-line subset but remains selection- and subclass-dependent.}
73:\label{fig:offsets}
74:\end{figure*}
77:\section{Data Availability}\label{sec:data-avail}
80:\section{Conclusion}\label{sec:conclusion}
81:In the capped SDSS DR17 emission-line subset, broad BPT optical AGN hosts show a median sSFR offset of $-1.309$ dex relative to mass--redshift matched controls, with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Although the offset amplitude is highly dependent on the emission-line selection function (decreasing to $-0.744$ dex at S/N$\geq 10$), the interval remains securely negative. These measurements establish a robust optical association baseline, which will require future molecular gas or direct outflow kinematics follow-up to isolate any causal AGN quenching mechanisms.
### m1_rp2_environment_quenching_integrated.tex
15:We use a representative 60,000-galaxy subset of the SDSS DR17 emission-line catalog to build an optical density-proxy analysis of environmental quenching. A 10th-nearest-neighbor density proxy is compared with quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) after controlling for stellar mass and redshift; using equal-count density quartiles, the high-density quartile has quenched fraction 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile. The bootstrap high-minus-low interval is [0.041, 0.059], which excludes zero. This analysis is intentionally limited to the optical denominator and leaves the missing group and halo information for future study.
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
28:\begin{deluxetable*}{lrrr}
29:\tabletypesize{\scriptsize}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
31:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
41:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
42:\end{deluxetable*}
44:The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
46:Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{SDSS density-proxy result for environmental quenching}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
63:\caption{SDSS DR17 optical density-proxy diagnostic for environmental quenching. The figure summarizes the equal-count density-quartile split, where the high-density quartile reaches a quenched fraction of 0.230 $\pm$ 0.003, establishing the baseline for future group-catalog analyses.}
64:\label{fig:topic}
65:\end{figure}
67:\section{Interpretation and missing observables}\label{sec:missing}
68:This SDSS-only baseline does not include group catalogues, robust central/satellite labels, halo masses, morphology, or multi-redshift selection functions. Those data are required before the density proxy can be interpreted as a physical environmental-quenching measurement.
72:Mass and environment are known separable axes in low-redshift galaxy evolution, but a real environmental-quenching analysis requires group/halo and central-satellite information beyond this nearest-neighbor proxy \citep{peng2010,baldry2006,wetzel2013,goubert2024}.
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}
79:The SDSS-only proxy shows a high-density quenched fraction of 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile, with a mass- and redshift-adjusted high-density coefficient of $0.032 \pm 0.004$. These values define an optical environmental baseline, but a full quenching interpretation still requires group catalogs, halo masses, and central/satellite labels.
### m1_rp3_maintenance_heating_integrated.tex
21:\section{Introduction}\label{sec:introduction}
22:Maintenance-heating interpretations require X-ray or radio observables, but a rigorous optical denominator is a necessary first step. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as a duty-cycle baseline for massive, low-sSFR hosts and restrict the scope to directly measured optical quantities. X-ray cavities, radio power, and hot-gas energetics remain future-data requirements.
25:\section{Data and Sample Selection}\label{sec:shared-selection}
28:\begin{deluxetable*}{lrrr}
29:\tabletypesize{\scriptsize}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
31:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
41:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
42:\end{deluxetable*}
44:The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
46:Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Optical denominator for maintenance-heating follow-up}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for maintenance-heating follow-up. The figure highlights that among massive, low-sSFR objects, the BPT-AGN fraction is 0.607, providing a duty-cycle denominator for future X-ray/radio studies.}
64:\label{fig:topic}
65:\end{figure}
67:\section{Interpretation and missing observables}\label{sec:missing}
70:Radio-mode and hot-atmosphere studies define the future calorimetric observables--jet power, cavities, cooling luminosity, and group gas--that are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}.
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
### m2_p1_outflow_escape_recycling_integrated.tex
21:\section{Introduction}\label{sec:introduction}
22:An optical line-ratio selection can define a useful target set for future outflow work, but it cannot measure escape or recycling on its own. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as an optical baseline for massive galaxies and restrict the scope to directly measured quantities. Resolved kinematics, halo potentials, and multiphase gas remain future-data requirements.
25:\section{Data and Sample Selection}\label{sec:shared-selection}
28:\begin{deluxetable*}{lrrr}
29:\tabletypesize{\scriptsize}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
31:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
41:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
42:\end{deluxetable*}
44:The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
46:Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Optical denominator for outflow escape tests}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for outflow escape-versus-recycling follow-up. The figure summarizes the 4,440-object BPT-selected denominator and the associated median $\log {\rm sSFR} = -11.53$ used for target definition.}
64:\label{fig:topic}
65:\end{figure}
67:\section{Interpretation and missing observables}\label{sec:missing}
70:Wind and outflow literature specifies the missing kinematic, geometric, molecular, and multiphase measurements; these sources motivate follow-up and do not turn line-ratio selection into an escape/recycling measurement \citep{veilleux2005,cicone2014,fiore2017,carniani2017,fabian2012}.
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
### m2_p2_radio_jet_environment_integrated.tex
21:\section{Introduction}\label{sec:introduction}
22:Radio-jet environment studies require radio and X-ray data, but an optical denominator is a useful starting point. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as an environment-stratified baseline for massive hosts and restrict the analysis to directly measured optical quantities. Jet power, coupling efficiency, and hot-gas structure remain future-data requirements.
25:\section{Data and Sample Selection}\label{sec:shared-selection}
28:\begin{deluxetable*}{lrrr}
29:\tabletypesize{\scriptsize}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
31:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
41:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
42:\end{deluxetable*}
44:The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
46:Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Optical denominator for radio-jet environment follow-up}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for radio-jet environment follow-up. The figure demonstrates the environment-stratified target set, with the optical AGN fraction rising to 0.509 $\pm$ 0.012 in the high-density quartile of massive hosts.}
64:\label{fig:topic}
65:\end{figure}
67:\section{Interpretation and missing observables}\label{sec:missing}
72:The radio/X-ray/group literature motivates environment-stratified follow-up, but the present result is only an optical BPT-AGN fraction versus an internal density proxy \citep{best2005,santoro2020,mcnamara2007,eckert2024}.
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}
### m2_p3_feedback_transition_mass_integrated.tex
21:\section{Introduction}\label{sec:introduction}
22:The stellar-mass scale where quenched fraction and optical AGN incidence rise together is useful as an empirical transition marker, but it is not by itself a physical-feedback measurement. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as an optical transition baseline and restrict the scope to directly measured quantities. Gas fractions, baryon deficits, and halo-scale measurements remain future-data requirements.
25:\section{Data and Sample Selection}\label{sec:shared-selection}
28:\begin{deluxetable*}{lrrr}
29:\tabletypesize{\scriptsize}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
31:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
41:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
42:\end{deluxetable*}
44:The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
46:Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Optical denominator for feedback-transition mass}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure shows the high-mass tail ($\log(M_\star/M_\odot)>11.0$) where the quenched fraction exceeds 0.5 and the optical AGN fraction peaks at 0.520.}
64:\label{fig:topic}
65:\end{figure}
67:\section{Interpretation and missing observables}\label{sec:missing}
70:Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
77:The first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail, defined here as $\log(M_\star/M_\odot)>11.0$, and the optical AGN fraction peaks at 0.520 in that same bin. These values define an optical transition vector, but gas fractions, baryon deficits, and halo-scale measurements are still needed before a causal feedback interpretation.
### m3_p1_multiphase_census_integrated.tex
21:\section{Introduction}\label{sec:introduction}
22:Multiphase outflow work requires ionized, neutral, molecular, and X-ray or radio measurements, but a common optical denominator is a practical starting point. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as that baseline and restrict the manuscript to directly measured optical quantities. The missing multiphase observables remain future-data requirements.
25:\section{Data and Sample Selection}\label{sec:shared-selection}
28:\begin{deluxetable*}{lrrr}
29:\tabletypesize{\scriptsize}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
31:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
41:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
42:\end{deluxetable*}
44:The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
46:Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Optical census of multiphase target denominators}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for the common-denominator multiphase census. The figure illustrates how varying optical tracer definitions yields AGN candidate prevalence ranging from 0.136 to 0.418 within the same denominator.}
64:\label{fig:topic}
65:\end{figure}
67:\section{Interpretation and missing observables}\label{sec:missing}
70:A real multiphase census needs independent ionized, neutral, molecular, and energetic outflow observables; the present SDSS thresholds are an optical denominator only \citep{veilleux2005,rupke2018,cicone2014,fiore2017,feruglio2015,woo2016,bae2018}.
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
### m3_p2_gas_depletion_efficiency_integrated.tex
21:\section{Introduction}\label{sec:introduction}
22:Gas-fraction and star-formation-efficiency interpretations require CO or dust data, but the optical denominator is the necessary starting point. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as a baseline for massive quenched or transitioning galaxies and restrict the manuscript to directly measured optical quantities. Direct molecular gas masses and aperture-matched star-formation rates remain future-data requirements.
25:\section{Data and Sample Selection}\label{sec:shared-selection}
28:\begin{deluxetable*}{lrrr}
29:\tabletypesize{\scriptsize}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities, ending with the paper-specific downstream subset.\label{tab:selection-cascade}}
31:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
42:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies. The final row defines the specific 6,729-galaxy subset used in this optical baseline.}
43:\end{deluxetable*}
47:The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
49:Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
52:\section{Measurements}\label{sec:measurements}
53:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
57:\section{Optical denominator for gas-fraction versus efficiency tests}\label{sec:topic-result}
63:\begin{figure}
65:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
66:\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure isolates the 6,729 massive quenched or transitioning galaxies, revealing an optical BPT AGN fraction of $0.549 \pm 0.006$.}
67:\label{fig:topic}
68:\end{figure}
70:\section{Interpretation and missing observables}\label{sec:missing}
71:This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.
73:Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs; optical H$\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \citep{coldgass1,coldgass2,xcoldgass2017,xgass2018}.
76:\section{Data Availability}\label{sec:data-avail}
79:\section{Conclusion}\label{sec:conclusion}
### m3_p3_simulation_validation_integrated.tex
21:\section{Introduction}\label{sec:introduction}
22:Forward-model validation requires simulation mocks, but an observational target vector is a useful starting point. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as a compact optical baseline and restrict the manuscript to directly measured quantities. Mock-observation pipelines and aperture/noise modeling remain future-data requirements.
25:\section{Data and Sample Selection}\label{sec:shared-selection}
28:\begin{deluxetable*}{lrrr}
29:\tabletypesize{\scriptsize}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
31:\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
41:\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
42:\end{deluxetable*}
44:The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
46:Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Optical target vector for simulation validation}\label{sec:topic-result}
57:We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector, so that simple Poisson counting errors remain at or below roughly 14\%; the cell grid spans mass bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 crossed with redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520. The observed target vector is useful for simulation forward modelling, but it still requires mock-observation pipelines before any model comparison can be claimed.
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-model validation target vector. The figure maps quenched fractions and optical AGN incidence across 15 mass-redshift cells for simulation forward-modeling, spanning mass bins 8.0--9.5 through 11.0--12.5 and redshift bins 0.02--0.05 through 0.08--0.12.}
64:\label{fig:topic}
65:\end{figure}
67:\section{Interpretation and missing observables}\label{sec:missing}
70:Simulation suites such as TNG, EAGLE, and SIMBA define the future comparison problem; the iMaNGA observational catalog provides a complementary benchmark for mock-observation work. No simulation mock has been forward-modelled or ranked in this pilot \citep{tng2019,eagle2015,simba2019,imanga2023,donnari2021,dubois2013,dubois2016}.
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
77:We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector, spanning mass bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 across redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520. This observed target vector is useful for simulation forward modelling, but it still requires mock-observation pipelines before any model comparison can be claimed.
93:\bibitem[Dubois et al.(2013)]{dubois2013} Dubois, Y., Gavazzi, R., Peirani, S., \& Silk, J. 2013, MNRAS, 433, 3297
94:\bibitem[Dubois et al.(2016)]{dubois2016} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, MNRAS, 463, 3948

codex
I’ve found one likely wording issue already: paper 1 uses “broad optical AGN,” which can be read as broad-line AGN even though the analysis is BPT-classified optical AGN. I’m checking the compile logs next for table/figure/citation warnings so I can separate semantic issues from actual TeX/layout problems.
exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/*/aastex/*.overnight.compile.log; do echo "### $(basename "$f")"; rg -n "Warning|Overfull|Underfull|Undefined|Citation|Reference|multiply|float|Table|Figure" "$f" | sed -n '"'1,120p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
### m1_rp1_sdss_agn_sfr_integrated.overnight.compile.log
3:warning: m1_rp1_sdss_agn_sfr_integrated.tex:83: Overfull \hbox (4.48347pt too wide) in paragraph at lines 83--83
4:warning: m1_rp1_sdss_agn_sfr_integrated.tex:83: Overfull \hbox (7.25346pt too wide) in paragraph at lines 83--83
7:warning: m1_rp1_sdss_agn_sfr_integrated.tex:83: Overfull \hbox (4.48347pt too wide) in paragraph at lines 83--83
8:warning: m1_rp1_sdss_agn_sfr_integrated.tex:83: Overfull \hbox (7.25346pt too wide) in paragraph at lines 83--83
### m1_rp2_environment_quenching_integrated.overnight.compile.log
3:warning: m1_rp2_environment_quenching_integrated.tex:58: Underfull \hbox (badness 1303) in paragraph at lines 57--58
4:warning: m1_rp2_environment_quenching_integrated.tex:81: Overfull \hbox (4.48347pt too wide) in paragraph at lines 81--81
5:warning: m1_rp2_environment_quenching_integrated.tex:81: Overfull \hbox (7.25346pt too wide) in paragraph at lines 81--81
8:warning: m1_rp2_environment_quenching_integrated.tex:58: Underfull \hbox (badness 1303) in paragraph at lines 57--58
9:warning: m1_rp2_environment_quenching_integrated.tex:81: Overfull \hbox (4.48347pt too wide) in paragraph at lines 81--81
10:warning: m1_rp2_environment_quenching_integrated.tex:81: Overfull \hbox (7.25346pt too wide) in paragraph at lines 81--81
### m1_rp3_maintenance_heating_integrated.overnight.compile.log
3:warning: m1_rp3_maintenance_heating_integrated.tex:69: Underfull \hbox (badness 1874) in paragraph at lines 68--69
4:warning: m1_rp3_maintenance_heating_integrated.tex:79: Overfull \hbox (4.48347pt too wide) in paragraph at lines 79--79
5:warning: m1_rp3_maintenance_heating_integrated.tex:79: Overfull \hbox (7.25346pt too wide) in paragraph at lines 79--79
8:warning: m1_rp3_maintenance_heating_integrated.tex:69: Underfull \hbox (badness 1874) in paragraph at lines 68--69
9:warning: m1_rp3_maintenance_heating_integrated.tex:79: Overfull \hbox (4.48347pt too wide) in paragraph at lines 79--79
10:warning: m1_rp3_maintenance_heating_integrated.tex:79: Overfull \hbox (7.25346pt too wide) in paragraph at lines 79--79
### m2_p1_outflow_escape_recycling_integrated.overnight.compile.log
3:warning: m2_p1_outflow_escape_recycling_integrated.tex:79: Overfull \hbox (4.48347pt too wide) in paragraph at lines 79--79
4:warning: m2_p1_outflow_escape_recycling_integrated.tex:79: Overfull \hbox (7.25346pt too wide) in paragraph at lines 79--79
7:warning: m2_p1_outflow_escape_recycling_integrated.tex:79: Overfull \hbox (4.48347pt too wide) in paragraph at lines 79--79
8:warning: m2_p1_outflow_escape_recycling_integrated.tex:79: Overfull \hbox (7.25346pt too wide) in paragraph at lines 79--79
### m2_p2_radio_jet_environment_integrated.overnight.compile.log
3:warning: m2_p2_radio_jet_environment_integrated.tex:73: Underfull \hbox (badness 10000) in paragraph at lines 72--73
4:warning: m2_p2_radio_jet_environment_integrated.tex:81: Overfull \hbox (4.48347pt too wide) in paragraph at lines 81--81
5:warning: m2_p2_radio_jet_environment_integrated.tex:81: Overfull \hbox (7.25346pt too wide) in paragraph at lines 81--81
8:warning: m2_p2_radio_jet_environment_integrated.tex:73: Underfull \hbox (badness 10000) in paragraph at lines 72--73
9:warning: m2_p2_radio_jet_environment_integrated.tex:81: Overfull \hbox (4.48347pt too wide) in paragraph at lines 81--81
10:warning: m2_p2_radio_jet_environment_integrated.tex:81: Overfull \hbox (7.25346pt too wide) in paragraph at lines 81--81
### m2_p3_feedback_transition_mass_integrated.overnight.compile.log
3:warning: m2_p3_feedback_transition_mass_integrated.tex:58: Underfull \hbox (badness 2134) in paragraph at lines 57--58
4:warning: m2_p3_feedback_transition_mass_integrated.tex:78: Underfull \hbox (badness 2134) in paragraph at lines 77--78
5:warning: m2_p3_feedback_transition_mass_integrated.tex:79: Overfull \hbox (4.48347pt too wide) in paragraph at lines 79--79
6:warning: m2_p3_feedback_transition_mass_integrated.tex:79: Overfull \hbox (7.25346pt too wide) in paragraph at lines 79--79
9:warning: m2_p3_feedback_transition_mass_integrated.tex:58: Underfull \hbox (badness 2134) in paragraph at lines 57--58
10:warning: m2_p3_feedback_transition_mass_integrated.tex:78: Underfull \hbox (badness 2134) in paragraph at lines 77--78
11:warning: m2_p3_feedback_transition_mass_integrated.tex:79: Overfull \hbox (4.48347pt too wide) in paragraph at lines 79--79
12:warning: m2_p3_feedback_transition_mass_integrated.tex:79: Overfull \hbox (7.25346pt too wide) in paragraph at lines 79--79
### m3_p1_multiphase_census_integrated.overnight.compile.log
3:warning: m3_p1_multiphase_census_integrated.tex:79: Overfull \hbox (4.48347pt too wide) in paragraph at lines 79--79
4:warning: m3_p1_multiphase_census_integrated.tex:79: Overfull \hbox (7.25346pt too wide) in paragraph at lines 79--79
7:warning: m3_p1_multiphase_census_integrated.tex:79: Overfull \hbox (4.48347pt too wide) in paragraph at lines 79--79
8:warning: m3_p1_multiphase_census_integrated.tex:79: Overfull \hbox (7.25346pt too wide) in paragraph at lines 79--79
### m3_p2_gas_depletion_efficiency_integrated.overnight.compile.log
3:warning: m3_p2_gas_depletion_efficiency_integrated.tex:82: Overfull \hbox (4.48347pt too wide) in paragraph at lines 82--82
4:warning: m3_p2_gas_depletion_efficiency_integrated.tex:82: Overfull \hbox (7.25346pt too wide) in paragraph at lines 82--82
7:warning: m3_p2_gas_depletion_efficiency_integrated.tex:82: Overfull \hbox (4.48347pt too wide) in paragraph at lines 82--82
8:warning: m3_p2_gas_depletion_efficiency_integrated.tex:82: Overfull \hbox (7.25346pt too wide) in paragraph at lines 82--82
### m3_p3_simulation_validation_integrated.overnight.compile.log
3:warning: m3_p3_simulation_validation_integrated.tex:56: Underfull \hbox (badness 1546) in paragraph at lines 55--56
4:warning: m3_p3_simulation_validation_integrated.tex:71: Underfull \hbox (badness 1028) in paragraph at lines 70--71
5:warning: m3_p3_simulation_validation_integrated.tex:79: Overfull \hbox (4.48347pt too wide) in paragraph at lines 79--79
6:warning: m3_p3_simulation_validation_integrated.tex:79: Overfull \hbox (7.25346pt too wide) in paragraph at lines 79--79
9:warning: m3_p3_simulation_validation_integrated.tex:56: Underfull \hbox (badness 1546) in paragraph at lines 55--56
10:warning: m3_p3_simulation_validation_integrated.tex:71: Underfull \hbox (badness 1028) in paragraph at lines 70--71
11:warning: m3_p3_simulation_validation_integrated.tex:79: Overfull \hbox (4.48347pt too wide) in paragraph at lines 79--79
12:warning: m3_p3_simulation_validation_integrated.tex:79: Overfull \hbox (7.25346pt too wide) in paragraph at lines 79--79

exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/*/aastex/*_integrated.tex; do echo "### $(basename "$f")"; rg -n "broad optical AGN|broad BPT|BPT AGN|BPT-selected optical AGN|feedback coupling|causal AGN|validation|future proposal|future-data requirements|available upon reasonable request|publicly available through the SDSS data releases" "$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
### m1_rp1_sdss_agn_sfr_integrated.tex
15:We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\Delta\log {\rm sSFR}=-1.309$ dex; at S/N$\geq 10$, the corresponding matched offset is $-0.744$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.
55:BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. The cached analysis table contains 39,553 star-forming galaxies, 12,234 intermediate/composite objects, 8,146 broad optical AGN, and 67 unclassified objects.
57:The preferred estimator matches every broad optical AGN host to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. This is an association design; controls are not matched in morphology, halo mass, gas mass, aperture scale, AGN luminosity, or duty-cycle phase.
59:Our comparison of broad BPT optical AGN hosts versus star-forming controls at S/N$\geq 3$ matches $N=8,146$ pairs, measuring a median specific star formation rate offset of $\Delta\log {\rm sSFR}=-1.309$ dex with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Applying a moderate mass-redshift caliper of $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$ retains $N=7,867$ pairs (96.6\% target coverage) and yields a median offset of $-1.318$ dex. A deterministic matching run without replacement yields $N=7,419$ matched pairs and a median offset of $-1.446$ dex, though with poorer stellar-mass balance. Raising the line-S/N threshold to 10 leaves $N=1,530$ matched pairs and reduces the median offset to $-0.744$ dex, and a narrower [N II] Seyfert-like proxy yields $N=2,114$ pairs and a median offset of $-0.763$ dex.
65:\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used in the RP-1 analysis. This figure documents the optical selection and classification boundary; it does not by itself identify causal AGN feedback.}
72:\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset is robust within the optical emission-line subset but remains selection- and subclass-dependent.}
78:The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
81:In the capped SDSS DR17 emission-line subset, broad BPT optical AGN hosts show a median sSFR offset of $-1.309$ dex relative to mass--redshift matched controls, with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Although the offset amplitude is highly dependent on the emission-line selection function (decreasing to $-0.744$ dex at S/N$\geq 10$), the interval remains securely negative. These measurements establish a robust optical association baseline, which will require future molecular gas or direct outflow kinematics follow-up to isolate any causal AGN quenching mechanisms.
### m1_rp2_environment_quenching_integrated.tex
76:The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
### m1_rp3_maintenance_heating_integrated.tex
22:Maintenance-heating interpretations require X-ray or radio observables, but a rigorous optical denominator is a necessary first step. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as a duty-cycle baseline for massive, low-sSFR hosts and restrict the scope to directly measured optical quantities. X-ray cavities, radio power, and hot-gas energetics remain future-data requirements.
57:The massive galaxy subset ($\log M_\star \geq 10.8$) contains 9,298 emission-line galaxies, of which 5,695 are classified as low-sSFR based on the specific star formation rate threshold of $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$ applied in this analysis. The optical BPT AGN fraction is measured as 0.430 in the total massive subset, rising to 0.607 when restricting the sample to massive low-sSFR objects. This empirical duty-cycle baseline is intended for future X-ray or radio maintenance-heating follow-up and is not a heating measurement.
74:The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
77:The massive subset contains 9,298 emission-line galaxies, with 5,695 classified as low-sSFR by the pilot threshold of $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$. The BPT AGN fraction rises from 0.430 in the massive subset to 0.607 in the massive low-sSFR subset, defining an optical duty-cycle denominator for maintenance-heating follow-up rather than a direct heating result.
### m2_p1_outflow_escape_recycling_integrated.tex
4:\shorttitle{SDSS BPT-selected optical AGN denominator for outflow escape tests}
8:\title{SDSS BPT-selected optical AGN denominator for outflow escape tests}
15:We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts 4,440 BPT-selected optical AGN candidates (0.074 $\pm$ 0.001) and records their median $\log {\rm sSFR} = -11.53$ as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
22:An optical line-ratio selection can define a useful target set for future outflow work, but it cannot measure escape or recycling on its own. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as an optical baseline for massive galaxies and restrict the scope to directly measured quantities. Resolved kinematics, halo potentials, and multiphase gas remain future-data requirements.
55:This note quantifies the BPT-selected optical AGN denominator needed for future resolved-kinematics tests of escape versus recycling. The result is an optical baseline rather than a direct escape-velocity measurement. ``BPT-selected optical AGN candidates'' here means the optical AGN subset counted above; it is shorthand for the denominator, not a separate kinematic or energy measurement.
57:BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies ($0.074 \pm 0.001$). Their median $\log {\rm sSFR}$ is $-11.53$, compared with $-10.14$ for the full denominator. This optical sample defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate.
74:The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
77:BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074 $\pm$ 0.001), and their median $\log {\rm sSFR}$ is -11.53 compared with -10.14 for the full denominator. The optical sample therefore defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate.
### m2_p2_radio_jet_environment_integrated.tex
22:Radio-jet environment studies require radio and X-ray data, but an optical denominator is a useful starting point. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as an environment-stratified baseline for massive hosts and restrict the analysis to directly measured optical quantities. Jet power, coupling efficiency, and hot-gas structure remain future-data requirements.
76:The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
### m2_p3_feedback_transition_mass_integrated.tex
22:The stellar-mass scale where quenched fraction and optical AGN incidence rise together is useful as an empirical transition marker, but it is not by itself a physical-feedback measurement. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as an optical transition baseline and restrict the scope to directly measured quantities. Gas fractions, baryon deficits, and halo-scale measurements remain future-data requirements.
74:The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
### m3_p1_multiphase_census_integrated.tex
22:Multiphase outflow work requires ionized, neutral, molecular, and X-ray or radio measurements, but a common optical denominator is a practical starting point. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as that baseline and restrict the manuscript to directly measured optical quantities. The missing multiphase observables remain future-data requirements.
74:The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
### m3_p2_gas_depletion_efficiency_integrated.tex
15:We use a 6,729-galaxy downstream subset drawn from the 60,000-galaxy SDSS DR17 emission-line cache to construct an optical selection baseline and denominator for future molecular gas-fraction versus star-formation efficiency follow-up. For massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of $0.549 \pm 0.006$ and a median log H$\alpha$ luminosity proxy of 40.06 erg s$^{-1}$, which is offset by $-0.66$ dex relative to massive star-forming controls. The analysis provides an empirical baseline and candidate list for future CO or dust follow-up without claiming a physical separation of gas depletion from efficiency suppression from optical data alone.
22:Gas-fraction and star-formation-efficiency interpretations require CO or dust data, but the optical denominator is the necessary starting point. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as a baseline for massive quenched or transitioning galaxies and restrict the manuscript to directly measured optical quantities. Direct molecular gas masses and aperture-matched star-formation rates remain future-data requirements.
60:The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is $0.549 \pm 0.006$, and the median H$\alpha$ luminosity proxy is $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$. The median H$\alpha$ luminosity proxy is approximately 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline.
66:\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure isolates the 6,729 massive quenched or transitioning galaxies, revealing an optical BPT AGN fraction of $0.549 \pm 0.006$.}
77:The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
80:We have mapped the optical baseline for 6,729 massive quenched or transitioning galaxies in the SDSS emission-line sample. We find a BPT AGN fraction of $0.549 \pm 0.006$ and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, approximately 0.66 dex lower than star-forming counterparts. While these quantities define the target selection denominator for future CO gas-fraction versus efficiency programs, direct molecular gas masses and aperture-matched star formation rates remain required to physically distinguish depletion from low efficiency.
### m3_p3_simulation_validation_integrated.tex
4:\shorttitle{SDSS target vector for feedback-model validation}
8:\title{SDSS target vector for feedback-model validation}
15:We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define a compact optical target vector for forward-model validation. The pilot records quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$), optical AGN incidence, and color versus mass/redshift across 15 mass-redshift cells with $n \geq 50$; across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520. It remains an empirical denominator study rather than a direct simulation comparison.
22:Forward-model validation requires simulation mocks, but an observational target vector is a useful starting point. Here, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. Here we present the SDSS DR17 emission-line sample as a compact optical baseline and restrict the manuscript to directly measured quantities. Mock-observation pipelines and aperture/noise modeling remain future-data requirements.
26:This note reuses the shared SDSS DR17 parent selection, but it interprets the result as an observational target vector for later simulation validation. The capped subset contains 60,000 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
54:\section{Optical target vector for simulation validation}\label{sec:topic-result}
55:We define a compact SDSS target vector of quenched fraction, optical AGN incidence, and color versus mass/redshift for forward-model validation. The result is an observed optical baseline rather than a full physical-feedback test.
57:We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector, so that simple Poisson counting errors remain at or below roughly 14\%; the cell grid spans mass bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 crossed with redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520. The observed target vector is useful for simulation forward modelling, but it still requires mock-observation pipelines before any model comparison can be claimed.
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-model validation target vector. The figure maps quenched fractions and optical AGN incidence across 15 mass-redshift cells for simulation forward-modeling, spanning mass bins 8.0--9.5 through 11.0--12.5 and redshift bins 0.02--0.05 through 0.08--0.12.}
74:The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
77:We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector, spanning mass bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 across redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520. This observed target vector is useful for simulation forward modelling, but it still requires mock-observation pipelines before any model comparison can be claimed.

exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/*/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/*/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md; do [ -f "$f" ] || continue; echo "### $(basename $(dirname "$f")) / $(basename "$f")"; rg -n "PDF|pdf|proposal|pilot|causal|validation|denominator|molecular|halo|group|cavity|quenching|outflow|feedback" "$f" | sed -n '"'1,80p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
### research-topics-from-wiki-20260708T090359Z / research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on feedback tracers and model validation
3:> This page presents three proposal-style research programmes on multiphase outflows, molecular-gas depletion versus efficiency, and forward-modelled simulation validation. Duplicate themes are consolidated so each proposal targets a distinct physical uncertainty.
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- P1: [Common-denominator optical tracer census in SDSS: an SDSS DR17 pilot (PDF)](m3_p1_multiphase_census_aas.pdf)
8:- P2: [Optical denominator for gas-fraction versus efficiency tests: an SDSS DR17 pilot (PDF)](m3_p2_gas_depletion_efficiency_aas.pdf)
9:- P3: [SDSS target vector for feedback-model validation: an SDSS DR17 pilot (PDF)](m3_p3_simulation_validation_aas.pdf)
11:3 proposal-style research programmes.
13:## P1 — A multiphase, common-denominator census of AGN-driven outflows
15:**Hypothesis / objective.** The inferred frequency and impact of AGN outflows depend strongly on gas phase, and a common-denominator multiphase census will change which feedback conclusions are supportable.
18:- High-redshift quasar molecular-gas work provides one tracer of AGN impact on cold reservoirs, but it cannot represent all gas phases. [molecular gas reservoirs in quasars](https://arxiv.org/abs/1706.08987).
19:- Young radio-galaxy outflow studies provide a complementary radio/ionized-gas efficiency perspective. [young radio-galaxy outflows](https://arxiv.org/abs/2009.11175).
20:- The local evidence summary includes AGN/outflow debate anchors that should be treated as provenance, not as a complete population denominator. [Method 3 AGN evidence anchor](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#agn).
22:**Remaining uncertainty.** Different tracers select different temperature/density phases and apertures, so current outflow rates may not be comparable or population-representative.
24:**Survey/data plan.** Parent AGN sample selected before outflow detection; MUSE/MaNGA ionized gas, ALMA CO molecular gas, HI/Na D or UV absorption for neutral gas, and JWST/NIRSpec at higher redshift; matched inactive controls.
26:**Analysis/test and decision criterion.** Recompute outflow occurrence, mass-loading, and kinetic power under a common selection denominator and aperture model. The claim that AGN outflows are common or important is supportable only for phases and mass/redshift ranges where tracer-corrected occurrence remains high.
28:**Limitations and wording guardrails.** Mass conversion factors differ by phase; avoid combining phase-specific mass outflow rates without explicit conversion uncertainties.
30:## P2 — Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies
32:**Hypothesis / objective.** In quenched or transitioning galaxies, low star formation is driven primarily by reduced molecular-gas fraction in some regimes and by reduced star-formation efficiency in others.
36:- Molecular-gas reservoir observations in quasars show that AGN can coincide with disturbed cold gas, but they do not alone distinguish depletion from suppressed efficiency. [quasar molecular-gas reservoir evidence](https://arxiv.org/abs/1706.08987).
37:- Environment/AGN comparisons against SDSS motivate separating gas supply, environment, and internal feedback rather than treating quenching as one scalar outcome. [environment and AGN quenching versus SDSS](https://arxiv.org/abs/2401.12953).
39:**Remaining uncertainty.** A quenched galaxy can have little gas or inefficient star formation in the gas it retains; those mechanisms imply different feedback and replenishment physics.
41:**Survey/data plan.** ALMA CO for molecular gas mass, dust continuum as a cross-check, Hα/UV/IR SFR indicators, optical morphology and stellar population ages, environment labels, and matched star-forming/transition/quiescent controls.
47:## P3 — Forward-modelled validation of cosmological feedback prescriptions
49:**Hypothesis / objective.** If subgrid feedback prescriptions are correct, forward-modelled mock observations from simulations should reproduce observed gas fractions, quenched fractions, outflow tracers, and morphology distributions under the same selection functions.
52:- IllustrisTNG quenched-fraction analyses explicitly tie quenching outcomes to AGN feedback, environment, and preprocessing in simulations. [IllustrisTNG quenched fractions](https://arxiv.org/abs/2008.00005).
53:- Horizon-AGN links AGN feedback to morphological diversity, making morphology a testable output rather than background context. [Horizon-AGN morphology and AGN feedback](https://arxiv.org/abs/1606.03086).
54:- Hydrodynamic quenching simulations motivate observationally matched validation, not direct import of simulation conclusions. [AGN-driven quenching simulation implications](https://arxiv.org/abs/1301.3092).
58:**Survey/data plan.** IllustrisTNG/Horizon-AGN/EAGLE-like public simulation outputs; synthetic MaNGA/MUSE/ALMA/X-ray/radio observables; real comparison samples from SDSS/MaNGA, ALMA follow-up, and group catalogues.
60:**Analysis/test and decision criterion.** Generate survey-matched mocks and compare joint distributions of gas fraction, quenched fraction, morphology, outflow incidence, and halo environment. A feedback model is constrained when residuals exceed observational uncertainties in a physically coherent subset of observables.
66:- Corpus-rebalancing work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.
70:These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.
### research-topics-from-wiki-20260708T090359Z / research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on AGN feedback, quenching, and environment
3:> This page presents three proposal-style research programmes on galaxy quenching and feedback. Each proposal states a falsifiable objective, the prior evidence motivating it, the unresolved measurement, the proposed survey data, the analysis test, and the wording limits that keep the conclusion appropriately bounded.
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- RP-1: [A Matched-Control SDSS DR17 Pilot Test of Specific Star Formation in Optical AGN Hosts (PDF)](sdss_agn_sfr_pilot_aas.pdf)
8:- RP-2: [SDSS density proxy for environmental quenching: an SDSS DR17 pilot (PDF)](m1_rp2_environment_quenching_aas.pdf)
9:- RP-3: [Optical-AGN denominator for maintenance-heating follow-up: an SDSS DR17 pilot (PDF)](m1_rp3_maintenance_heating_aas.pdf)
11:3 proposal-style research programmes.
13:## RP-1 — Observational constraints on the suppression of star formation by AGN feedback
15:**Hypothesis / objective.** AGN hosts exhibit a measurable star-formation deficit relative to inactive galaxies matched in stellar mass, morphology, halo environment, and redshift only when the feedback energy budget can couple to the molecular or ionized gas reservoir.
18:- M51-scale NOEMA evidence motivates a spatially resolved test of how AGN activity perturbs the local interstellar medium, but a nearby case cannot by itself establish population-level quenching. [SWAN IV / M51 AGN feedback](https://arxiv.org/abs/2604.15438).
19:- High-redshift quasar observations directly connect AGN activity to disturbed molecular gas reservoirs, motivating a molecular-gas denominator for any causal quenching test. [quasar molecular-gas reservoir evidence](https://arxiv.org/abs/1706.08987).
20:- The local coverage record still treats the broad causal AGN-quenching statement as unsettled, so the proposal must test causality rather than restate it as established. [local coverage record for broad AGN-quenching statement](../prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-hwao-20260708T043427Z.json).
22:**Remaining uncertainty.** The unresolved issue is not whether AGN and quiescence coexist, but whether AGN power predicts a deficit in star formation after matching on the covariates that also correlate with quenching.
24:**Survey/data plan.** Parent sample: MaNGA or MUSE IFU AGN hosts and inactive controls matched in stellar mass, morphology, halo mass/environment, and redshift; ALMA CO for molecular gas mass and depletion time; Chandra/XMM/eROSITA for radiative and mechanical AGN power proxies; VLA/LOFAR for radio-mode duty cycle.
26:**Analysis/test and decision criterion.** Fit a hierarchical matched-control model in which resolved star-formation deficit, gas fraction, and depletion time are predicted by AGN power after controlling for mass, morphology, and environment. The hypothesis is supported only if the AGN coefficient remains significant and the inferred energy budget can plausibly affect the measured gas phase; otherwise the result bounds or rejects a causal interpretation.
28:**Limitations and wording guardrails.** AGN duty cycles, obscuration, and residual matching errors can mimic causal suppression; the result should be framed as a constraint on feedback coupling, not a proof of universal AGN quenching.
30:## RP-2 — Separating internal and environmental quenching across stellar mass, halo mass, and redshift
32:**Hypothesis / objective.** Environmental quenching contributes an excess quenched fraction at fixed stellar mass below a halo- and redshift-dependent transition, whereas internal/AGN-linked channels dominate at higher stellar or halo mass.
35:- Local simulations compared to SDSS explicitly frame quenching as a joint environment-plus-AGN problem rather than a single-channel process. [environment and AGN quenching versus SDSS](https://arxiv.org/abs/2401.12953).
36:- Euclid Q1 results motivate a morphology/environment sequence in which dense environments can quench before bulge formation, while field evolution may follow a different order. [Euclid Q1 quenching sequence](https://arxiv.org/abs/2511.02964).
39:**Remaining uncertainty.** The main unknown is the transition surface in stellar mass, halo mass, satellite/central status, and redshift where environmental effects become separable from internal mass-linked quenching.
41:**Survey/data plan.** Low redshift: SDSS, GAMA, ALFALFA/FASHI HI, and group catalogues for stellar mass, halo proxy, central/satellite status, and quenched fraction. Intermediate/high redshift: COSMOS/CANDELS/JWST fields for SFR and morphology; Euclid and DESI for larger-scale environment and redshift completeness.
43:**Analysis/test and decision criterion.** Estimate quenched-fraction excess in a multivariate model with stellar mass, halo/environment, central/satellite label, morphology, and redshift. A credible environmental channel requires an excess that persists at fixed stellar mass and halo proxy with controlled central/satellite classification.
45:**Limitations and wording guardrails.** Group membership and halo masses are noisy, and pre-processing can be misclassified as cluster quenching; results should be reported as a transition map with uncertainty bands.
47:## RP-3 — Empirical duty-cycle constraints on AGN maintenance heating in massive halos
49:**Hypothesis / objective.** For massive central galaxies and groups, the time-averaged mechanical power from radio-mode AGN balances hot-halo cooling often enough to maintain low star-formation rates.
52:- Observed/simulated central-galaxy comparisons support integrated AGN feedback as relevant to quenching but do not by themselves measure a population duty cycle. [central-galaxy quenching and integrated AGN feedback](https://arxiv.org/abs/2112.07672).
53:- IllustrisTNG quenched-fraction work identifies AGN feedback, environment, and preprocessing as separable model ingredients, motivating observational tests rather than simulation restatement. [IllustrisTNG quenched fractions](https://arxiv.org/abs/2008.00005).
54:- Galaxy groups are highlighted as a sensitive regime for testing AGN feedback energetics in hot atmospheres. [galaxy groups as AGN feedback probes](https://arxiv.org/abs/2403.17145).
55:- Chaotic cold accretion and dual jet-heating models provide mechanisms for self-regulated heating that require observational duty-cycle constraints. [chaotic cold accretion](https://arxiv.org/abs/1301.3130); [dual jet/heating feedback](https://arxiv.org/abs/1108.0110).
59:**Survey/data plan.** Chandra cavity measurements and XMM/eROSITA thermodynamics for cooling luminosity; VLA/LOFAR radio data for jet age and duty-cycle indicators; group/cluster catalogues selected by halo mass rather than cavity visibility.
61:**Analysis/test and decision criterion.** Compute cavity enthalpy and buoyancy/age-based jet power, compare to X-ray cooling luminosity, and model censoring for systems without detectable cavities. Maintenance heating is supported only if the time-averaged heating-to-cooling distribution is centered near unity for the relevant halo-mass range.
67:- Evidence-gap ranking and acceptance-threshold work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.
71:These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.
### research-topics-from-wiki-20260708T090359Z / research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on outflows and feedback regimes
3:> This page presents three proposal-style research programmes on outflow fate, jet coupling, and the transition from stellar-feedback to AGN-linked regulation. The proposals are framed around measurable observables, matched denominators, and explicit decision criteria.
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- P1: [SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot (PDF)](m2_p1_outflow_escape_recycling_aas.pdf)
8:- P2: [Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot (PDF)](m2_p2_radio_jet_environment_aas.pdf)
9:- P3: [SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot (PDF)](m2_p3_feedback_transition_mass_aas.pdf)
11:3 proposal-style research programmes.
13:## P1 — Escape versus recycling: the fate of AGN-driven multiphase outflows
15:**Hypothesis / objective.** A substantial fraction of AGN-driven outflowing gas remains gravitationally bound and recycles through the circumgalactic medium, limiting the permanence of feedback-driven gas removal.
18:- Quasar observations show AGN feedback acting on molecular gas reservoirs at high redshift, but such detections do not determine whether gas escapes the halo. [quasar molecular-gas reservoirs](https://arxiv.org/abs/1706.08987).
19:- Stellar-feedback work on baryon deficiency in low-mass galaxies provides a boundary condition for non-AGN removal channels that must not be confused with AGN-driven escape. [stellar feedback and baryon deficiency](https://arxiv.org/abs/2512.05584).
20:- Simulated galaxy feedback constraints highlight that gas removal, recycling, and observable baryon fractions depend on halo scale. [simulated observable feedback constraints](https://arxiv.org/abs/0901.1880).
22:**Remaining uncertainty.** The escaped fraction of multiphase outflows is unmeasured across a representative mass/redshift sample; an outflow detection is not equivalent to permanent quenching.
24:**Survey/data plan.** AGN hosts and inactive controls spanning stellar mass and redshift; MUSE/MaNGA ionized-gas kinematics, ALMA CO and [C II] for cold gas, JWST/NIRSpec for z>2 outflow tracers, and CGM absorption where available to track recycling.
26:**Analysis/test and decision criterion.** Compare outflow velocity distributions with halo escape velocities inferred from dynamical/halo-mass estimates, then model escaped versus bound/recycling fractions as a function of stellar mass, halo mass, and redshift. A high escaped fraction at fixed denominator supports permanent-removal feedback; a low escaped fraction supports recycling-limited regulation.
28:**Limitations and wording guardrails.** Projection, phase conversion, and uncertain halo potentials can dominate the escaped-fraction error budget.
35:- Young radio galaxies show AGN-driven outflows and provide an empirical route to estimating feedback efficiency. [young radio galaxies and feedback efficiency](https://arxiv.org/abs/2009.11175).
36:- Local M51-scale NOEMA data show how jet/AGN activity can affect molecular ISM structure at high spatial resolution, motivating a broader population test. [SWAN IV molecular ISM feedback](https://arxiv.org/abs/2604.15438).
37:- Galaxy-group feedback studies identify the group regime as a strong testbed for coupling between radio activity and hot gas. [group-scale AGN feedback](https://arxiv.org/abs/2403.17145).
41:**Survey/data plan.** VLA/LOFAR/MeerKAT for jet morphology and radio spectral ages; Chandra for cavities/shocks/hot gas; MUSE/MaNGA for ionized-gas shock diagnostics; ALMA CO for molecular disturbances; environment from group catalogues.
47:## P3 — Locating the transition from stellar-feedback to AGN-feedback regulation
49:**Hypothesis / objective.** There is a stellar/halo-mass regime where stellar-feedback momentum and energy budgets cease to explain gas loss or quiescence, and AGN-linked observables become necessary to reproduce the measured quenched fraction and baryon deficit.
52:- Low-mass baryon deficiency attributed to stellar feedback provides the low-mass endpoint of the transition problem. [stellar-feedback baryon deficiency](https://arxiv.org/abs/2512.05584).
53:- High-redshift environmental-quenching simulations emphasize that quenching mechanisms vary with mass and redshift, not only with local observables. [high-redshift environmental quenching simulations](https://arxiv.org/abs/2605.03008).
54:- Simulated observable-property constraints show why feedback-regime boundaries must be tested against measured baryonic properties. [feedback constraints in simulated galaxies](https://arxiv.org/abs/0901.1880).
56:**Remaining uncertainty.** The observational crossover mass between stellar-feedback-dominated regulation and AGN-linked regulation is not cleanly measured with the same denominator and gas observables.
58:**Survey/data plan.** DESI/GAMA/COSMOS parent samples with stellar mass and halo proxy; ALFALFA/FASHI HI and ALMA CO gas fractions; optical/IR SFRs; X-ray/radio AGN indicators; JWST for high-redshift extension.
60:**Analysis/test and decision criterion.** Fit a broken-slope or transition model for gas fraction, baryon deficit, and quenched fraction as functions of stellar/halo mass while including AGN incidence and stellar-feedback proxies. The transition is credible only if the AGN-linked term improves predictive power above the stellar-feedback model at high mass.
66:- Evidence-traceability work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.
70:These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.
### research-topics-from-wiki-20260708T090359Z / research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on feedback tracers and model validation
3:> This page presents three proposal-style research programmes on multiphase outflows, molecular-gas depletion versus efficiency, and forward-modelled simulation validation. Duplicate themes are consolidated so each proposal targets a distinct physical uncertainty.
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- P1: [Common-denominator optical tracer census in SDSS: an SDSS DR17 pilot (PDF)](m3_p1_multiphase_census_aas.pdf)
8:- P2: [Optical denominator for gas-fraction versus efficiency tests: an SDSS DR17 pilot (PDF)](m3_p2_gas_depletion_efficiency_aas.pdf)
9:- P3: [SDSS target vector for feedback-model validation: an SDSS DR17 pilot (PDF)](m3_p3_simulation_validation_aas.pdf)
11:3 proposal-style research programmes.
13:## P1 — A multiphase, common-denominator census of AGN-driven outflows
15:**Hypothesis / objective.** The inferred frequency and impact of AGN outflows depend strongly on gas phase, and a common-denominator multiphase census will change which feedback conclusions are supportable.
18:- High-redshift quasar molecular-gas work provides one tracer of AGN impact on cold reservoirs, but it cannot represent all gas phases. [molecular gas reservoirs in quasars](https://arxiv.org/abs/1706.08987).
19:- Young radio-galaxy outflow studies provide a complementary radio/ionized-gas efficiency perspective. [young radio-galaxy outflows](https://arxiv.org/abs/2009.11175).
20:- The local evidence summary includes AGN/outflow debate anchors that should be treated as provenance, not as a complete population denominator. [Method 3 AGN evidence anchor](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#agn).
22:**Remaining uncertainty.** Different tracers select different temperature/density phases and apertures, so current outflow rates may not be comparable or population-representative.
24:**Survey/data plan.** Parent AGN sample selected before outflow detection; MUSE/MaNGA ionized gas, ALMA CO molecular gas, HI/Na D or UV absorption for neutral gas, and JWST/NIRSpec at higher redshift; matched inactive controls.
26:**Analysis/test and decision criterion.** Recompute outflow occurrence, mass-loading, and kinetic power under a common selection denominator and aperture model. The claim that AGN outflows are common or important is supportable only for phases and mass/redshift ranges where tracer-corrected occurrence remains high.
28:**Limitations and wording guardrails.** Mass conversion factors differ by phase; avoid combining phase-specific mass outflow rates without explicit conversion uncertainties.
30:## P2 — Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies
32:**Hypothesis / objective.** In quenched or transitioning galaxies, low star formation is driven primarily by reduced molecular-gas fraction in some regimes and by reduced star-formation efficiency in others.
36:- Molecular-gas reservoir observations in quasars show that AGN can coincide with disturbed cold gas, but they do not alone distinguish depletion from suppressed efficiency. [quasar molecular-gas reservoir evidence](https://arxiv.org/abs/1706.08987).
37:- Environment/AGN comparisons against SDSS motivate separating gas supply, environment, and internal feedback rather than treating quenching as one scalar outcome. [environment and AGN quenching versus SDSS](https://arxiv.org/abs/2401.12953).
39:**Remaining uncertainty.** A quenched galaxy can have little gas or inefficient star formation in the gas it retains; those mechanisms imply different feedback and replenishment physics.
41:**Survey/data plan.** ALMA CO for molecular gas mass, dust continuum as a cross-check, Hα/UV/IR SFR indicators, optical morphology and stellar population ages, environment labels, and matched star-forming/transition/quiescent controls.
47:## P3 — Forward-modelled validation of cosmological feedback prescriptions
49:**Hypothesis / objective.** If subgrid feedback prescriptions are correct, forward-modelled mock observations from simulations should reproduce observed gas fractions, quenched fractions, outflow tracers, and morphology distributions under the same selection functions.
52:- IllustrisTNG quenched-fraction analyses explicitly tie quenching outcomes to AGN feedback, environment, and preprocessing in simulations. [IllustrisTNG quenched fractions](https://arxiv.org/abs/2008.00005).
53:- Horizon-AGN links AGN feedback to morphological diversity, making morphology a testable output rather than background context. [Horizon-AGN morphology and AGN feedback](https://arxiv.org/abs/1606.03086).
54:- Hydrodynamic quenching simulations motivate observationally matched validation, not direct import of simulation conclusions. [AGN-driven quenching simulation implications](https://arxiv.org/abs/1301.3092).
58:**Survey/data plan.** IllustrisTNG/Horizon-AGN/EAGLE-like public simulation outputs; synthetic MaNGA/MUSE/ALMA/X-ray/radio observables; real comparison samples from SDSS/MaNGA, ALMA follow-up, and group catalogues.
60:**Analysis/test and decision criterion.** Generate survey-matched mocks and compare joint distributions of gas fraction, quenched fraction, morphology, outflow incidence, and halo environment. A feedback model is constrained when residuals exceed observational uncertainties in a physically coherent subset of observables.
66:- Corpus-rebalancing work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.
70:These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.
### research-topics-from-wiki-20260708T090359Z / research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on AGN feedback, quenching, and environment
3:> This page presents three proposal-style research programmes on galaxy quenching and feedback. Each proposal states a falsifiable objective, the prior evidence motivating it, the unresolved measurement, the proposed survey data, the analysis test, and the wording limits that keep the conclusion appropriately bounded.
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- RP-1: [A Matched-Control SDSS DR17 Pilot Test of Specific Star Formation in Optical AGN Hosts (PDF)](sdss_agn_sfr_pilot_aas.pdf)
8:- RP-2: [SDSS density proxy for environmental quenching: an SDSS DR17 pilot (PDF)](m1_rp2_environment_quenching_aas.pdf)
9:- RP-3: [Optical-AGN denominator for maintenance-heating follow-up: an SDSS DR17 pilot (PDF)](m1_rp3_maintenance_heating_aas.pdf)
11:3 proposal-style research programmes.
13:## RP-1 — Observational constraints on the suppression of star formation by AGN feedback
15:**Hypothesis / objective.** AGN hosts exhibit a measurable star-formation deficit relative to inactive galaxies matched in stellar mass, morphology, halo environment, and redshift only when the feedback energy budget can couple to the molecular or ionized gas reservoir.
18:- M51-scale NOEMA evidence motivates a spatially resolved test of how AGN activity perturbs the local interstellar medium, but a nearby case cannot by itself establish population-level quenching. [SWAN IV / M51 AGN feedback](https://arxiv.org/abs/2604.15438).
19:- High-redshift quasar observations directly connect AGN activity to disturbed molecular gas reservoirs, motivating a molecular-gas denominator for any causal quenching test. [quasar molecular-gas reservoir evidence](https://arxiv.org/abs/1706.08987).
20:- The local coverage record still treats the broad causal AGN-quenching statement as unsettled, so the proposal must test causality rather than restate it as established. [local coverage record for broad AGN-quenching statement](../prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-hwao-20260708T043427Z.json).
22:**Remaining uncertainty.** The unresolved issue is not whether AGN and quiescence coexist, but whether AGN power predicts a deficit in star formation after matching on the covariates that also correlate with quenching.
24:**Survey/data plan.** Parent sample: MaNGA or MUSE IFU AGN hosts and inactive controls matched in stellar mass, morphology, halo mass/environment, and redshift; ALMA CO for molecular gas mass and depletion time; Chandra/XMM/eROSITA for radiative and mechanical AGN power proxies; VLA/LOFAR for radio-mode duty cycle.
26:**Analysis/test and decision criterion.** Fit a hierarchical matched-control model in which resolved star-formation deficit, gas fraction, and depletion time are predicted by AGN power after controlling for mass, morphology, and environment. The hypothesis is supported only if the AGN coefficient remains significant and the inferred energy budget can plausibly affect the measured gas phase; otherwise the result bounds or rejects a causal interpretation.
28:**Limitations and wording guardrails.** AGN duty cycles, obscuration, and residual matching errors can mimic causal suppression; the result should be framed as a constraint on feedback coupling, not a proof of universal AGN quenching.
30:## RP-2 — Separating internal and environmental quenching across stellar mass, halo mass, and redshift
32:**Hypothesis / objective.** Environmental quenching contributes an excess quenched fraction at fixed stellar mass below a halo- and redshift-dependent transition, whereas internal/AGN-linked channels dominate at higher stellar or halo mass.
35:- Local simulations compared to SDSS explicitly frame quenching as a joint environment-plus-AGN problem rather than a single-channel process. [environment and AGN quenching versus SDSS](https://arxiv.org/abs/2401.12953).
36:- Euclid Q1 results motivate a morphology/environment sequence in which dense environments can quench before bulge formation, while field evolution may follow a different order. [Euclid Q1 quenching sequence](https://arxiv.org/abs/2511.02964).
39:**Remaining uncertainty.** The main unknown is the transition surface in stellar mass, halo mass, satellite/central status, and redshift where environmental effects become separable from internal mass-linked quenching.
41:**Survey/data plan.** Low redshift: SDSS, GAMA, ALFALFA/FASHI HI, and group catalogues for stellar mass, halo proxy, central/satellite status, and quenched fraction. Intermediate/high redshift: COSMOS/CANDELS/JWST fields for SFR and morphology; Euclid and DESI for larger-scale environment and redshift completeness.
43:**Analysis/test and decision criterion.** Estimate quenched-fraction excess in a multivariate model with stellar mass, halo/environment, central/satellite label, morphology, and redshift. A credible environmental channel requires an excess that persists at fixed stellar mass and halo proxy with controlled central/satellite classification.
45:**Limitations and wording guardrails.** Group membership and halo masses are noisy, and pre-processing can be misclassified as cluster quenching; results should be reported as a transition map with uncertainty bands.
47:## RP-3 — Empirical duty-cycle constraints on AGN maintenance heating in massive halos
49:**Hypothesis / objective.** For massive central galaxies and groups, the time-averaged mechanical power from radio-mode AGN balances hot-halo cooling often enough to maintain low star-formation rates.
52:- Observed/simulated central-galaxy comparisons support integrated AGN feedback as relevant to quenching but do not by themselves measure a population duty cycle. [central-galaxy quenching and integrated AGN feedback](https://arxiv.org/abs/2112.07672).
53:- IllustrisTNG quenched-fraction work identifies AGN feedback, environment, and preprocessing as separable model ingredients, motivating observational tests rather than simulation restatement. [IllustrisTNG quenched fractions](https://arxiv.org/abs/2008.00005).
54:- Galaxy groups are highlighted as a sensitive regime for testing AGN feedback energetics in hot atmospheres. [galaxy groups as AGN feedback probes](https://arxiv.org/abs/2403.17145).
55:- Chaotic cold accretion and dual jet-heating models provide mechanisms for self-regulated heating that require observational duty-cycle constraints. [chaotic cold accretion](https://arxiv.org/abs/1301.3130); [dual jet/heating feedback](https://arxiv.org/abs/1108.0110).
59:**Survey/data plan.** Chandra cavity measurements and XMM/eROSITA thermodynamics for cooling luminosity; VLA/LOFAR radio data for jet age and duty-cycle indicators; group/cluster catalogues selected by halo mass rather than cavity visibility.
61:**Analysis/test and decision criterion.** Compute cavity enthalpy and buoyancy/age-based jet power, compare to X-ray cooling luminosity, and model censoring for systems without detectable cavities. Maintenance heating is supported only if the time-averaged heating-to-cooling distribution is centered near unity for the relevant halo-mass range.
67:- Evidence-gap ranking and acceptance-threshold work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.
71:These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.
### research-topics-from-wiki-20260708T090359Z / research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on outflows and feedback regimes
3:> This page presents three proposal-style research programmes on outflow fate, jet coupling, and the transition from stellar-feedback to AGN-linked regulation. The proposals are framed around measurable observables, matched denominators, and explicit decision criteria.
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- P1: [SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot (PDF)](m2_p1_outflow_escape_recycling_aas.pdf)
8:- P2: [Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot (PDF)](m2_p2_radio_jet_environment_aas.pdf)
9:- P3: [SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot (PDF)](m2_p3_feedback_transition_mass_aas.pdf)
11:3 proposal-style research programmes.
13:## P1 — Escape versus recycling: the fate of AGN-driven multiphase outflows
15:**Hypothesis / objective.** A substantial fraction of AGN-driven outflowing gas remains gravitationally bound and recycles through the circumgalactic medium, limiting the permanence of feedback-driven gas removal.
18:- Quasar observations show AGN feedback acting on molecular gas reservoirs at high redshift, but such detections do not determine whether gas escapes the halo. [quasar molecular-gas reservoirs](https://arxiv.org/abs/1706.08987).
19:- Stellar-feedback work on baryon deficiency in low-mass galaxies provides a boundary condition for non-AGN removal channels that must not be confused with AGN-driven escape. [stellar feedback and baryon deficiency](https://arxiv.org/abs/2512.05584).
20:- Simulated galaxy feedback constraints highlight that gas removal, recycling, and observable baryon fractions depend on halo scale. [simulated observable feedback constraints](https://arxiv.org/abs/0901.1880).
22:**Remaining uncertainty.** The escaped fraction of multiphase outflows is unmeasured across a representative mass/redshift sample; an outflow detection is not equivalent to permanent quenching.
24:**Survey/data plan.** AGN hosts and inactive controls spanning stellar mass and redshift; MUSE/MaNGA ionized-gas kinematics, ALMA CO and [C II] for cold gas, JWST/NIRSpec for z>2 outflow tracers, and CGM absorption where available to track recycling.
26:**Analysis/test and decision criterion.** Compare outflow velocity distributions with halo escape velocities inferred from dynamical/halo-mass estimates, then model escaped versus bound/recycling fractions as a function of stellar mass, halo mass, and redshift. A high escaped fraction at fixed denominator supports permanent-removal feedback; a low escaped fraction supports recycling-limited regulation.
28:**Limitations and wording guardrails.** Projection, phase conversion, and uncertain halo potentials can dominate the escaped-fraction error budget.
35:- Young radio galaxies show AGN-driven outflows and provide an empirical route to estimating feedback efficiency. [young radio galaxies and feedback efficiency](https://arxiv.org/abs/2009.11175).
36:- Local M51-scale NOEMA data show how jet/AGN activity can affect molecular ISM structure at high spatial resolution, motivating a broader population test. [SWAN IV molecular ISM feedback](https://arxiv.org/abs/2604.15438).
37:- Galaxy-group feedback studies identify the group regime as a strong testbed for coupling between radio activity and hot gas. [group-scale AGN feedback](https://arxiv.org/abs/2403.17145).
41:**Survey/data plan.** VLA/LOFAR/MeerKAT for jet morphology and radio spectral ages; Chandra for cavities/shocks/hot gas; MUSE/MaNGA for ionized-gas shock diagnostics; ALMA CO for molecular disturbances; environment from group catalogues.
47:## P3 — Locating the transition from stellar-feedback to AGN-feedback regulation
49:**Hypothesis / objective.** There is a stellar/halo-mass regime where stellar-feedback momentum and energy budgets cease to explain gas loss or quiescence, and AGN-linked observables become necessary to reproduce the measured quenched fraction and baryon deficit.
52:- Low-mass baryon deficiency attributed to stellar feedback provides the low-mass endpoint of the transition problem. [stellar-feedback baryon deficiency](https://arxiv.org/abs/2512.05584).
53:- High-redshift environmental-quenching simulations emphasize that quenching mechanisms vary with mass and redshift, not only with local observables. [high-redshift environmental quenching simulations](https://arxiv.org/abs/2605.03008).
54:- Simulated observable-property constraints show why feedback-regime boundaries must be tested against measured baryonic properties. [feedback constraints in simulated galaxies](https://arxiv.org/abs/0901.1880).
56:**Remaining uncertainty.** The observational crossover mass between stellar-feedback-dominated regulation and AGN-linked regulation is not cleanly measured with the same denominator and gas observables.
58:**Survey/data plan.** DESI/GAMA/COSMOS parent samples with stellar mass and halo proxy; ALFALFA/FASHI HI and ALMA CO gas fractions; optical/IR SFRs; X-ray/radio AGN indicators; JWST for high-redshift extension.
60:**Analysis/test and decision criterion.** Fit a broken-slope or transition model for gas fraction, baryon deficit, and quenched fraction as functions of stellar/halo mass while including AGN incidence and stellar-feedback proxies. The transition is credible only if the AGN-linked term improves predictive power above the stellar-feedback model at high mass.
66:- Evidence-traceability work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.
70:These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.

codex
**1. OVERNIGHT_CODEX_KUN_REPRO_CYCLE_18 status:** `ISSUES_FOUND`

**2. Files/paths actually inspected**
- Cycle-18 candidate TeX files:
  - [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
  - [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
  - [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
  - [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
  - [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
  - [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
  - [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
  - [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
  - [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)
- Cycle-18 compile receipts and provenance artifacts:
  - [CYCLE_18_BEFORE_RECEIPT.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/CYCLE_18_BEFORE_RECEIPT.json)
  - [SOURCE_COPY.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/SOURCE_COPY.json)
  - All nine [*.overnight.compile.log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.overnight.compile.log) logs and the other eight sibling logs
  - All nine [data/source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json) files
- Public-linked research-topic manuscripts:
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
- Same public-linked manuscript paths in the live mirror under [NebulaMind-origin-main-live](/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/)

**3. Ranked findings**
- **Major:** The provenance ledger is effectively empty. Every `data/source_analysis_results.json` I inspected is all `null`, and `SOURCE_COPY.json` / `CYCLE_18_BEFORE_RECEIPT.json` do not carry usable source-trace metadata. This is the biggest reproducibility gap because it weakens the no-mock-data and source-to-claim audit even though the TeX itself compiles.
- **Major:** The public-linked research-topic manuscripts are stale relative to the current cycle-18 candidate package. The public pages still use old proposal-style framing and old PDF aliases such as `sdss_agn_sfr_pilot_aas.pdf`, `m1_rp2_environment_quenching_aas.pdf`, and `m3_p3_simulation_validation_aas.pdf`, while the local candidates are the integrated cycle-18 TeX/PDFs. The public prose also remains more causal/proposal-like than the current conservative pilot manuscripts.
- **Major:** [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex#L15) has a unit/log inconsistency in the abstract: `median log H$\alpha$ luminosity proxy of 40.06 erg s$^{-1}$`. That should be rewritten as a dimensionally correct logarithmic quantity.
- **Major:** [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex#L15) uses `broad optical AGN` / `broad BPT optical AGN`, which is easy to misread as broad-line AGN. The analysis is BPT-classified optical AGN, so the terminology should be tightened.
- **Minor:** [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex#L57) and [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex#L55) still lean on mildly causal verbs (`confirming`, `modulates`). The science is already framed as association-only, so those verbs should be softened to `associated with` / `in this model`.
- **Minor:** The compile logs show only layout warnings, not fatal errors, but there are repeated underfull/overfull `\hbox` messages around result/conclusion and acknowledgments, especially in papers 2, 3, 5, 6, and 9. This is a readability and polishing issue, not a science issue.

**4. Exact feed for PDF-writing pilot**
- **Paper 1:** Replace every `broad optical AGN` / `broad BPT optical AGN` with `BPT-classified optical AGN` or `BPT-selected optical AGN`. Keep all sample counts and offsets unchanged. Suggested sentence for the abstract: `We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in BPT-classified optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog.`
- **Paper 2:** Rewrite the result sentence to keep the measured values but remove the causal gloss. Suggested replacement for the key result paragraph: `Using equal-count density quartiles, the high-density quartile has quenched fraction 0.230 \pm 0.003 versus 0.181 \pm 0.003 in the low-density quartile. In this linear probability model, the high-density coefficient is 0.032 \pm 0.004 after controlling for stellar mass and redshift.` Also change `modulates` to `is associated with` in the topic-result lead sentence.
- **Paper 3:** Keep the current measured fractions, but if you want cleaner flow, shorten the repeated qualifier `massive, low-sSFR` once per section and avoid repeating the full threshold more than necessary. No science change needed.
- **Paper 4:** Keep the current denominator and 4,440 count, but make the follow-up language explicitly future-facing. Suggested cleanup: `This note quantifies the BPT-selected optical AGN denominator needed for future resolved-kinematics tests of escape versus recycling.` That preserves the real-data boundary.
- **Paper 5:** Rewrite the lead sentence from `We examine whether a local-density proxy modulates the optical AGN fraction...` to `We examine whether a local-density proxy is associated with the optical AGN fraction...`. Keep the fractions `0.509 \pm 0.012` and `0.367 \pm 0.012` unchanged.
- **Paper 6:** Keep the transition-mass numbers unchanged, but make the result and conclusion read as an empirical trend, not a physical assignment. If you want one extra safety sentence, add: `This is an optical transition vector only; gas fractions, baryon deficits, and halo-scale measurements are still required before any causal feedback interpretation.`
- **Paper 7:** No blocker-level rewrite needed. The common-denominator framing is already conservative. If anything, trim repetition in the intro and conclusion to reduce layout warnings.
- **Paper 8:** Fix the Hα unit/log sentence everywhere it appears. Safe version for the abstract: `For massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of $0.549 \pm 0.006$ and a median $\log(L_{\mathrm{H}\alpha}/\mathrm{erg~s}^{-1}) = 40.06$, which is 0.66 dex lower than the massive star-forming control median.` Mirror the same wording in the body and conclusion.
- **Paper 9:** Keep the current target-vector numbers, but consider a small title/lead cleanup if you want to avoid overpromising: `SDSS target vector for future feedback-model validation`. The current body already stays honest by saying no simulation mock has been forward-modelled or ranked.
- **All papers:** Add or keep one explicit no-mock-data sentence in the methods/data-availability block: `No mock, synthetic, placeholder, or toy data were used in any quantitative claim in this manuscript.` This is a clean provenance guardrail for the pilot.
- **All papers:** If you keep the current data-availability wording, tighten it to make the exact local artifacts explicit: `The SDSS DR17 parent data are public; the exact capped subset, selection manifest, and local query snapshot used for this manuscript are retained in the project handoff for reproducibility.`

**5. Real-data/source/citation audit notes**
- I did not find evidence of mock/synthetic/placeholder data being used as numerical evidence in the cycle-18 TeX files.
- All numeric claims I checked are either SDSS public counts, cached subset counts, or derived quantities from the local cached table.
- The local TeX citation usage is mostly sane: `\citep` is used for data-release and literature context, not as a substitute for results.
- The biggest audit weakness is not a bad citation inside the TeX; it is the empty machine-readable provenance layer in `source_analysis_results.json`.
- The public-linked research-topic pages use external arXiv links as provenance/motivation anchors. Those should not be confused with manuscript citations in the local PDFs.
- The public-linked pages are also more proposal-like than the local cycle-18 manuscripts, so they should be treated as archived guidance unless they are explicitly synchronized.

**6. Workflow/system notes**
- All nine candidate PDFs compiled successfully; there were no fatal markers.
- The only TeX-quality issues in the compile logs were underfull/overfull `\hbox` warnings, concentrated in dense result paragraphs and acknowledgments.
- The cycle-18 local candidate package is more conservative than the public research-topic pages, which still look like archived proposal material.
- The blank provenance JSON suggests the workflow is not emitting a usable source audit record for the candidate-copy pilot, even though the TeX content itself is careful.
- The public and live trees appear to expose the older research-topic pages and PDF aliases rather than a cycle-18 synchronized landing page.

**7. Safety ledger**
- No file edits were made.
- No public PDFs were replaced or published.
- No DB, SQL, `/api/pages`, page_versions, wiki publish, or trust recompute actions were taken.
- No deploy/restart actions were taken.
- No git commit, push, merge, rebase, or history rewrite was taken.
- No cron changes were taken.
- No billing, cloud, OAuth, API-key, account, credential, token, or cookie access was taken.
- No external manuscript submission was made.
tokens used
140,734
**1. OVERNIGHT_CODEX_KUN_REPRO_CYCLE_18 status:** `ISSUES_FOUND`

**2. Files/paths actually inspected**
- Cycle-18 candidate TeX files:
  - [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
  - [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
  - [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
  - [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
  - [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
  - [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
  - [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
  - [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
  - [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)
- Cycle-18 compile receipts and provenance artifacts:
  - [CYCLE_18_BEFORE_RECEIPT.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/CYCLE_18_BEFORE_RECEIPT.json)
  - [SOURCE_COPY.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/SOURCE_COPY.json)
  - All nine [*.overnight.compile.log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.overnight.compile.log) logs and the other eight sibling logs
  - All nine [data/source_analysis_results.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json) files
- Public-linked research-topic manuscripts:
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
- Same public-linked manuscript paths in the live mirror under [NebulaMind-origin-main-live](/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/)

**3. Ranked findings**
- **Major:** The provenance ledger is effectively empty. Every `data/source_analysis_results.json` I inspected is all `null`, and `SOURCE_COPY.json` / `CYCLE_18_BEFORE_RECEIPT.json` do not carry usable source-trace metadata. This is the biggest reproducibility gap because it weakens the no-mock-data and source-to-claim audit even though the TeX itself compiles.
- **Major:** The public-linked research-topic manuscripts are stale relative to the current cycle-18 candidate package. The public pages still use old proposal-style framing and old PDF aliases such as `sdss_agn_sfr_pilot_aas.pdf`, `m1_rp2_environment_quenching_aas.pdf`, and `m3_p3_simulation_validation_aas.pdf`, while the local candidates are the integrated cycle-18 TeX/PDFs. The public prose also remains more causal/proposal-like than the current conservative pilot manuscripts.
- **Major:** [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex#L15) has a unit/log inconsistency in the abstract: `median log H$\alpha$ luminosity proxy of 40.06 erg s$^{-1}$`. That should be rewritten as a dimensionally correct logarithmic quantity.
- **Major:** [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_18_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex#L15) uses `broad optical AGN` / `broad BPT optical AGN`, which is easy to misread as broad-line AGN. The analysis is BPT-classified optical AGN, so the terminology should be tightened.
- **Minor:** [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_18_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex#L57) and [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_18_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex#L55) still lean on mildly causal verbs (`confirming`, `modulates`). The science is already framed as association-only, so those verbs should be softened to `associated with` / `in this model`.
- **Minor:** The compile logs show only layout warnings, not fatal errors, but there are repeated underfull/overfull `\hbox` messages around result/conclusion and acknowledgments, especially in papers 2, 3, 5, 6, and 9. This is a readability and polishing issue, not a science issue.

**4. Exact feed for PDF-writing pilot**
- **Paper 1:** Replace every `broad optical AGN` / `broad BPT optical AGN` with `BPT-classified optical AGN` or `BPT-selected optical AGN`. Keep all sample counts and offsets unchanged. Suggested sentence for the abstract: `We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in BPT-classified optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog.`
- **Paper 2:** Rewrite the result sentence to keep the measured values but remove the causal gloss. Suggested replacement for the key result paragraph: `Using equal-count density quartiles, the high-density quartile has quenched fraction 0.230 \pm 0.003 versus 0.181 \pm 0.003 in the low-density quartile. In this linear probability model, the high-density coefficient is 0.032 \pm 0.004 after controlling for stellar mass and redshift.` Also change `modulates` to `is associated with` in the topic-result lead sentence.
- **Paper 3:** Keep the current measured fractions, but if you want cleaner flow, shorten the repeated qualifier `massive, low-sSFR` once per section and avoid repeating the full threshold more than necessary. No science change needed.
- **Paper 4:** Keep the current denominator and 4,440 count, but make the follow-up language explicitly future-facing. Suggested cleanup: `This note quantifies the BPT-selected optical AGN denominator needed for future resolved-kinematics tests of escape versus recycling.` That preserves the real-data boundary.
- **Paper 5:** Rewrite the lead sentence from `We examine whether a local-density proxy modulates the optical AGN fraction...` to `We examine whether a local-density proxy is associated with the optical AGN fraction...`. Keep the fractions `0.509 \pm 0.012` and `0.367 \pm 0.012` unchanged.
- **Paper 6:** Keep the transition-mass numbers unchanged, but make the result and conclusion read as an empirical trend, not a physical assignment. If you want one extra safety sentence, add: `This is an optical transition vector only; gas fractions, baryon deficits, and halo-scale measurements are still required before any causal feedback interpretation.`
- **Paper 7:** No blocker-level rewrite needed. The common-denominator framing is already conservative. If anything, trim repetition in the intro and conclusion to reduce layout warnings.
- **Paper 8:** Fix the Hα unit/log sentence everywhere it appears. Safe version for the abstract: `For massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of $0.549 \pm 0.006$ and a median $\log(L_{\mathrm{H}\alpha}/\mathrm{erg~s}^{-1}) = 40.06$, which is 0.66 dex lower than the massive star-forming control median.` Mirror the same wording in the body and conclusion.
- **Paper 9:** Keep the current target-vector numbers, but consider a small title/lead cleanup if you want to avoid overpromising: `SDSS target vector for future feedback-model validation`. The current body already stays honest by saying no simulation mock has been forward-modelled or ranked.
- **All papers:** Add or keep one explicit no-mock-data sentence in the methods/data-availability block: `No mock, synthetic, placeholder, or toy data were used in any quantitative claim in this manuscript.` This is a clean provenance guardrail for the pilot.
- **All papers:** If you keep the current data-availability wording, tighten it to make the exact local artifacts explicit: `The SDSS DR17 parent data are public; the exact capped subset, selection manifest, and local query snapshot used for this manuscript are retained in the project handoff for reproducibility.`

**5. Real-data/source/citation audit notes**
- I did not find evidence of mock/synthetic/placeholder data being used as numerical evidence in the cycle-18 TeX files.
- All numeric claims I checked are either SDSS public counts, cached subset counts, or derived quantities from the local cached table.
- The local TeX citation usage is mostly sane: `\citep` is used for data-release and literature context, not as a substitute for results.
- The biggest audit weakness is not a bad citation inside the TeX; it is the empty machine-readable provenance layer in `source_analysis_results.json`.
- The public-linked research-topic pages use external arXiv links as provenance/motivation anchors. Those should not be confused with manuscript citations in the local PDFs.
- The public-linked pages are also more proposal-like than the local cycle-18 manuscripts, so they should be treated as archived guidance unless they are explicitly synchronized.

**6. Workflow/system notes**
- All nine candidate PDFs compiled successfully; there were no fatal markers.
- The only TeX-quality issues in the compile logs were underfull/overfull `\hbox` warnings, concentrated in dense result paragraphs and acknowledgments.
- The cycle-18 local candidate package is more conservative than the public research-topic pages, which still look like archived proposal material.
- The blank provenance JSON suggests the workflow is not emitting a usable source audit record for the candidate-copy pilot, even though the TeX content itself is careful.
- The public and live trees appear to expose the older research-topic pages and PDF aliases rather than a cycle-18 synchronized landing page.

**7. Safety ledger**
- No file edits were made.
- No public PDFs were replaced or published.
- No DB, SQL, `/api/pages`, page_versions, wiki publish, or trust recompute actions were taken.
- No deploy/restart actions were taken.
- No git commit, push, merge, rebase, or history rewrite was taken.
- No cron changes were taken.
- No billing, cloud, OAuth, API-key, account, credential, token, or cookie access was taken.
- No external manuscript submission was made.


# command_result
exit_code=0
elapsed_s=364.0
timed_out=False
finished_utc=2026-07-09T23:05:17Z
