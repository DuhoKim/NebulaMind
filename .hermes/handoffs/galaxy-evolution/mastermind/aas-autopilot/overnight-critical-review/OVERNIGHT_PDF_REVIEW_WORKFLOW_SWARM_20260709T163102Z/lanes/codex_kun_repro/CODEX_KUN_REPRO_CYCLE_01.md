# codex_kun_repro cycle 1
Started UTC: 2026-07-09T16:31:47Z
Model: gpt-5.4-mini
Provider: codex
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_01_codex_kun_repro.md

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
session id: 019f47b8-96e8-7ae1-b6d2-d4917282eb5a
--------
user
Kun/Codex read-only reproducibility, TeX, provenance, and no-mock-data audit.

Output marker: OVERNIGHT_CODEX_KUN_REPRO_CYCLE_01

Work mode: artifact-only, read-only lane. Do not edit files. Do not publish. Do not call or request credentials.

Critically review the 9 current candidate PDFs/manuscript TeX files and the public-linked research-topic manuscripts. Find the highest-value issues that should feed the candidate-copy PDF-writing pilot: overclaims, missing caveats, weak abstracts, confusing conclusion/limitations wording, citation role errors, stale public-vs-local mismatch, poor reader flow, figure/table/caption problems, and reproducibility risks. Give exact safe rewrite guidance where possible, but do not edit files.

Required output sections:
1. OVERNIGHT_CODEX_KUN_REPRO_CYCLE_01 status: PASS/ISSUES_FOUND/BLOCKED.
2. Files/paths actually inspected or, if not inspectable, paths used from context.
3. Ranked findings, with severity: blocker/major/minor/improvement.
4. Exact feed for PDF-writing pilot: concrete TeX-level edits or section rewrite instructions, preserving measured values and real-data boundaries.
5. Real-data/source/citation audit notes.
6. Workflow/system notes if relevant.
7. Safety ledger confirming no edits/public/db/deploy/git/cron/billing/OAuth/submission.

Run root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z
Cycle: 1
Candidate package: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers
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
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 229280,
    "pdf_sha256": "8caf3de48100fcc87872773fe204be990bb53e6b7c1be5469978fd367367761d",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 81992,
    "pdf_sha256": "29301b0be0d530a6270b1534fc4005941b009237adeccc948778eb14869ee7ed",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 82318,
    "pdf_sha256": "7ee05cfc35151cc4264145a3807f4fd699d8284cb20b9f612faa8c39d2a6f796",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 311269,
    "pdf_sha256": "96c85d8647f032cb04761b9a258181b61afae95427a9fc0980b82fb35bf85d41",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 82542,
    "pdf_sha256": "a27a7386f1ef5274b6286e36e6e87867a768bf7910e758e6ceb3edcdfd58ddd2",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 82247,
    "pdf_sha256": "b8e39f7c061f4d6eb20b85879f7f82a7457304c010dd3fd052d472d250f5372e",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 82716,
    "pdf_sha256": "79a1357534963a4ae1d7ca87a82bef881e9a55aef0008765e3574cc6219b639d",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 204987,
    "pdf_sha256": "ac0542525fef5ae14f92a9a4edc315e80f3917156078333092ce0678e3b12335",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.overnight.compile.log"
  },
  {
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex",
    "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf",
    "ok": true,
    "returncode": 0,
    "pdf_bytes": 82996,
    "pdf_sha256": "04abcb27018973bad28cc937071c83031812186f13ce0343b4d17304e30cfb7b",
    "header": "%PDF",
    "fatal_markers": [],
    "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle

Deterministic inventory summary:
{
  "candidate_papers": [
    {
      "slug": "01_m1_rp1_sdss_agn_sfr",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
      "title": "Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot",
      "abstract": "We integrate the strongest Galaxy Evolution pilot into a selection-aware short-paper draft: a matched-control comparison of catalog specific star formation in broad BPT optical AGN hosts and star-forming controls in SDSS DR17. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a flagship short-paper draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "tex_sha256": "69409b90a0479f23a84991da03dc514daec083c93145505a4b4d2dd8ca58e51b",
      "pdf_sha256": "8caf3de48100fcc87872773fe204be990bb53e6b7c1be5469978fd367367761d",
      "pdf_bytes": 229280
    },
    {
      "slug": "02_m1_rp2_environment_quenching",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
      "title": "SDSS density proxy for environmental quenching: selection-aware SDSS optical proxy integration",
      "abstract": "We integrate the active proposal 'Separating internal and environmental quenching across stellar mass, halo mass, and redshift' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "tex_sha256": "6f879108b0889194069d7f56cfa194433db87cb751ec50a51e758652f06c2de2",
      "pdf_sha256": "29301b0be0d530a6270b1534fc4005941b009237adeccc948778eb14869ee7ed",
      "pdf_bytes": 81992
    },
    {
      "slug": "03_m1_rp3_maintenance_heating",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
      "title": "Optical-AGN denominator for maintenance-heating follow-up: selection-aware SDSS optical proxy integration",
      "abstract": "We integrate the active proposal 'Empirical duty-cycle constraints on AGN maintenance heating in massive halos' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "tex_sha256": "0cab9f8bd9614a68ed067043f211be6f4d0372ca97c8d41004b3c9fb49da9583",
      "pdf_sha256": "7ee05cfc35151cc4264145a3807f4fd699d8284cb20b9f612faa8c39d2a6f796",
      "pdf_bytes": 82318
    },
    {
      "slug": "04_m2_p1_outflow_escape_recycling",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
      "title": "SDSS high-excitation AGN denominator for outflow escape tests: selection-aware SDSS optical proxy integration",
      "abstract": "We integrate the active proposal 'Escape versus recycling: the fate of AGN-driven multiphase outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "tex_sha256": "53136bb1594ca816064601098db5378e48d276d2ed27561911c7560201d2c90f",
      "pdf_sha256": "96c85d8647f032cb04761b9a258181b61afae95427a9fc0980b82fb35bf85d41",
      "pdf_bytes": 311269
    },
    {
      "slug": "05_m2_p2_radio_jet_environment",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf",
      "title": "Environment proxy for optical AGN in massive SDSS hosts: selection-aware SDSS optical proxy integration",
      "abstract": "We integrate the active proposal 'Environmental dependence of radio-jet coupling efficiency in galaxy gas' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "tex_sha256": "560b68a8e59f35d9195c18216618a5491d3683cb13120c06ce10a27ad2b23e4e",
      "pdf_sha256": "a27a7386f1ef5274b6286e36e6e87867a768bf7910e758e6ceb3edcdfd58ddd2",
      "pdf_bytes": 82542
    },
    {
      "slug": "06_m2_p3_feedback_transition_mass",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf",
      "title": "SDSS mass transition in quenching and optical AGN incidence: selection-aware SDSS optical proxy integration",
      "abstract": "We integrate the active proposal 'Locating the transition from stellar-feedback to AGN-feedback regulation' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "tex_sha256": "b7916767462d58a17c5aa36371e5857d802fa6c685ffddb23f326dcd817495b3",
      "pdf_sha256": "b8e39f7c061f4d6eb20b85879f7f82a7457304c010dd3fd052d472d250f5372e",
      "pdf_bytes": 82247
    },
    {
      "slug": "07_m3_p1_multiphase_census",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf",
      "title": "Common-denominator optical tracer census in SDSS: selection-aware SDSS optical proxy integration",
      "abstract": "We integrate the active proposal 'A multiphase, common-denominator census of AGN-driven outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.",
      "tex_sha256": "24c8adf2a69c03a0c942f1c10c9ee873d1cd2450d4e63e0c8449954995063204",
      "pdf_sha256": "79a1357534963a4ae1d7ca87a82bef881e9a55aef0008765e3574cc6219b639d",
      "pdf_bytes": 82716
    },
    {
      "slug": "08_m3_p2_gas_depletion_efficiency",
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T

Candidate paper summaries:
- slug=01_m1_rp1_sdss_agn_sfr
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf
  title=Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot
  abstract=We integrate the strongest Galaxy Evolution pilot into a selection-aware short-paper draft: a matched-control comparison of catalog specific star formation in broad BPT optical AGN hosts and star-forming controls in SDSS DR17. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a flagship short-paper draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- slug=02_m1_rp2_environment_quenching
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf
  title=SDSS density proxy for environmental quenching: selection-aware SDSS optical proxy integration
  abstract=We integrate the active proposal 'Separating internal and environmental quenching across stellar mass, halo mass, and redshift' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- slug=03_m1_rp3_maintenance_heating
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf
  title=Optical-AGN denominator for maintenance-heating follow-up: selection-aware SDSS optical proxy integration
  abstract=We integrate the active proposal 'Empirical duty-cycle constraints on AGN maintenance heating in massive halos' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- slug=04_m2_p1_outflow_escape_recycling
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf
  title=SDSS high-excitation AGN denominator for outflow escape tests: selection-aware SDSS optical proxy integration
  abstract=We integrate the active proposal 'Escape versus recycling: the fate of AGN-driven multiphase outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- slug=05_m2_p2_radio_jet_environment
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf
  title=Environment proxy for optical AGN in massive SDSS hosts: selection-aware SDSS optical proxy integration
  abstract=We integrate the active proposal 'Environmental dependence of radio-jet coupling efficiency in galaxy gas' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- slug=06_m2_p3_feedback_transition_mass
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf
  title=SDSS mass transition in quenching and optical AGN incidence: selection-aware SDSS optical proxy integration
  abstract=We integrate the active proposal 'Locating the transition from stellar-feedback to AGN-feedback regulation' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- slug=07_m3_p1_multiphase_census
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf
  title=Common-denominator optical tracer census in SDSS: selection-aware SDSS optical proxy integration
  abstract=We integrate the active proposal 'A multiphase, common-denominator census of AGN-driven outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- slug=08_m3_p2_gas_depletion_efficiency
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf
  title=Optical denominator for gas-fraction versus efficiency tests: selection-aware SDSS optical proxy integration
  abstract=We integrate the active proposal 'Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
- slug=09_m3_p3_simulation_validation
  tex=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
  pdf=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf
  title=SDSS target vector for feedback-model validation: selection-aware SDSS optical proxy integration
  abstract=We integrate the active proposal 'Forward-modelled validation of cosmological feedback prescriptions' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.

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
I’m inspecting the nine candidate TeX sources plus the public-linked manuscript copies to look for overclaiming, caveat gaps, flow issues, citation-role problems, and any reproducibility mismatches. First step is to map the exact files present and pull the key sections that drive the review.
exec
/bin/zsh -c "rg --files \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers\" | sed -n '1,120p'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -c "rg --files \"/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution\" | sed -n '1,120p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/CYCLE_01_BEFORE_RECEIPT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/CYCLE_01_BEFORE_RECEIPT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/SOURCE_COPY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf

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
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-preserved-no-go-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger-summary.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-review-checklist.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-packet.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-summary.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-no-go-gap-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger-summary.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-sections.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/manifest.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/index.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-pages.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/quintet.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-v2-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-citation-role-mappings.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-primary-citation-anchor-registry.jsonl
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/page-content-m2-v2-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/manifest-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-deepening-map-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/quintet.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/wiki-format-preview-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/evidence-trust-map-20260708T014205Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/manifest.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/page-content-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/index.html
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
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/manifest.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/m3-p2-same-format-draft-20260707T050500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/goru-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/kun-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/tori-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/hwao-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/lana-dmw.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/lana-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/tori-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/hwao-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/goru-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/kun-pgr.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.json
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p2-2929-route-spec-20260706T144637Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json.backup-before-p1-spec-20260706T101547Z
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.json
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
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/wiki-format-preview-evidence-trust-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/page-content-evidence-trust-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md

exec
/bin/zsh -c "rg --files \"/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution\" | sed -n '1,120p'" in /Users/duhokim/NebulaMind/NebulaMind
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
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-primary-citation-anchor-registry.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-summary.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-citation-role-mappings.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-preserved-no-go-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-review-checklist.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/quintet.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-packet.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger-summary.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-pages.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger-summary.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-no-go-gap-ledger.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-sections.jsonl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/page-content-20260707T064500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/page-content-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/evidence-trust-map-20260708T014205Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/wiki-format-preview-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p1_outflow_escape_recycling_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p2_radio_jet_environment_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html.backup-before-embedded-pdf-link-20260708T124436Z-dataurl
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p3_feedback_transition_mass_aas.pdf
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/quintet.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/m3-p2-same-format-draft-20260707T050500Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/tori-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/hwao-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/goru-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/kun-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/lana-sfa.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/source-first-paper-adjudication/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/source-first-paper-adjudication/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/hwao-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/lana-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/tori-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/page-content-m2-v2-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-v2-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-deepening-map-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/packet-gated-paper-to-wiki-reconciliation/manifest.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/packet-gated-paper-to-wiki-reconciliation/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/packet-gated-paper-to-wiki-reconciliation/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/goru-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/kun-dmw.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/wiki-format-preview-evidence-trust-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/page-content-evidence-trust-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/manifest-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p4-trust-level-route-consistency-guard-spec-20260706T150328Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_backup_before_mirror_20260708T013540Z/debate-map-to-wiki-rebuild/wiki-page.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/lana-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/tori-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/hwao-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/goru-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/briefs/kun-pgr.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.json
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.md
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p3-2572-2573-primacy-wording-spec-20260706T145409Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-20260708T014205Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/wiki-format-preview-20260707T064500Z.html
/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/manifest-20260708T014205Z.json

codex
I have the file map. Next I’m pulling the manuscript sections that usually hide the highest-value problems: abstracts, conclusions/limitations, figure captions, and any reviewer-facing caveat language or citation-role mapping.
exec
/bin/zsh -c "sed -n '1,220p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "card_id": "p2",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p2_radio_jet_environment/figures/m2_p2_radio_jet_environment_figure1.pdf",
  "full_proposal_requires": "radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.",
  "high_density_massive_agn": {
    "fraction": 0.5085836909871244,
    "k": 948,
    "n": 1864,
    "se": 0.011579319665266517
  },
  "high_minus_low_ci": [
    0.11189880364416133,
    0.1702164814837969
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "low_density_massive_agn": {
    "fraction": 0.3667152221412964,
    "k": 1007,
    "n": 2746,
    "se": 0.009196312633686535
  },
  "massive_rows": 9298,
  "method": "source-first-paper-adjudication",
  "pilot_question": "Does a local-density proxy modulate the optical AGN fraction in massive SDSS hosts, motivating environment-stratified radio/X-ray jet-coupling follow-up?",
  "proposal_title": "Environmental dependence of radio-jet coupling efficiency in galaxy gas",
  "result_bullets": [
    "Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.",
    "The bootstrap high-minus-low interval is [0.112, 0.170].",
    "This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "Environment proxy for optical AGN in massive SDSS hosts",
  "slug": "m2_p2_radio_jet_environment",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
}
exec
/bin/zsh -c 'for f in "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers"/*/aastex/*_integrated.tex; do echo "==== $f"; rg -n "'"\\\\begin\\{abstract\\}|\\\\section\\{(Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability)\\}|\\\\caption\\{|\\\\label\\{|\\\\cite\\{|overclaim|limitation|caveat|selection-aware|denominator/proxy|association-only|not a completed|not a causal|future work\" \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 exited 2 in 0ms:
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\section\{(Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability)\}|\caption\{|\label\{|\cite\{|overclaim|limitation|caveat|selection-aware|denominator/proxy|association-only|not a completed|not a causal|future work)
                                                                                                                                  ^^
error: unrecognized escape sequence
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\section\{(Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability)\}|\caption\{|\label\{|\cite\{|overclaim|limitation|caveat|selection-aware|denominator/proxy|association-only|not a completed|not a causal|future work)
                                                                                                                                  ^^
error: unrecognized escape sequence
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\section\{(Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability)\}|\caption\{|\label\{|\cite\{|overclaim|limitation|caveat|selection-aware|denominator/proxy|association-only|not a completed|not a causal|future work)
                                                                                                                                  ^^
error: unrecognized escape sequence
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\section\{(Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability)\}|\caption\{|\label\{|\cite\{|overclaim|limitation|caveat|selection-aware|denominator/proxy|association-only|not a completed|not a causal|future work)
                                                                                                                                  ^^
error: unrecognized escape sequence
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\section\{(Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability)\}|\caption\{|\label\{|\cite\{|overclaim|limitation|caveat|selection-aware|denominator/proxy|association-only|not a completed|not a causal|future work)
                                                                                                                                  ^^
error: unrecognized escape sequence
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\section\{(Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability)\}|\caption\{|\label\{|\cite\{|overclaim|limitation|caveat|selection-aware|denominator/proxy|association-only|not a completed|not a causal|future work)
                                                                                                                                  ^^
error: unrecognized escape sequence
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\section\{(Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability)\}|\caption\{|\label\{|\cite\{|overclaim|limitation|caveat|selection-aware|denominator/proxy|association-only|not a completed|not a causal|future work)
                                                                                                                                  ^^
error: unrecognized escape sequence
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\section\{(Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability)\}|\caption\{|\label\{|\cite\{|overclaim|limitation|caveat|selection-aware|denominator/proxy|association-only|not a completed|not a causal|future work)
                                                                                                                                  ^^
error: unrecognized escape sequence
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\section\{(Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability)\}|\caption\{|\label\{|\cite\{|overclaim|limitation|caveat|selection-aware|denominator/proxy|association-only|not a completed|not a causal|future work)
                                                                                                                                  ^^
error: unrecognized escape sequence

exec
/bin/zsh -c "sed -n '1,220p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/SOURCE_COPY.json\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers",
  "cycle": 1,
  "copied_utc": "2026-07-09T16:31:02Z",
  "paper_dirs": [
    "01_m1_rp1_sdss_agn_sfr",
    "02_m1_rp2_environment_quenching",
    "03_m1_rp3_maintenance_heating",
    "04_m2_p1_outflow_escape_recycling",
    "05_m2_p2_radio_jet_environment",
    "06_m2_p3_feedback_transition_mass",
    "07_m3_p1_multiphase_census",
    "08_m3_p2_gas_depletion_efficiency",
    "09_m3_p3_simulation_validation"
  ]
}
exec
/bin/zsh -c "sed -n '1,220p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/FINAL_POST_FIX_HANDOFF.md\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
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
I’ve confirmed the candidate package and the public wiki/PDF roots are present. I’m now comparing manuscript-level wording against the source-analysis artifacts so I can separate true manuscript issues from already-guarded pilot framing.
exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/*/aastex/*_integrated.tex; do echo "==== $(basename "$f")"; rg -n -C 2 "'"\\\\begin\\{abstract\\}|\\\\end\\{abstract\\}|\\\\section\\{|\\\\subsection\\{|\\\\caption\\{|\\\\cite\\{|\\\\citep\\{|\\\\citet\\{|Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability|Acknowledgments|Acknowledgements\" \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 exited 2 in 0ms:
==== m1_rp1_sdss_agn_sfr_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\cite\{|\citep\{|\citet\{|Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability|Acknowledgments|Acknowledgements)
                          ^^
error: unrecognized escape sequence
==== m1_rp2_environment_quenching_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\cite\{|\citep\{|\citet\{|Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability|Acknowledgments|Acknowledgements)
                          ^^
error: unrecognized escape sequence
==== m1_rp3_maintenance_heating_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\cite\{|\citep\{|\citet\{|Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability|Acknowledgments|Acknowledgements)
                          ^^
error: unrecognized escape sequence
==== m2_p1_outflow_escape_recycling_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\cite\{|\citep\{|\citet\{|Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability|Acknowledgments|Acknowledgements)
                          ^^
error: unrecognized escape sequence
==== m2_p2_radio_jet_environment_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\cite\{|\citep\{|\citet\{|Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability|Acknowledgments|Acknowledgements)
                          ^^
error: unrecognized escape sequence
==== m2_p3_feedback_transition_mass_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\cite\{|\citep\{|\citet\{|Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability|Acknowledgments|Acknowledgements)
                          ^^
error: unrecognized escape sequence
==== m3_p1_multiphase_census_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\cite\{|\citep\{|\citet\{|Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability|Acknowledgments|Acknowledgements)
                          ^^
error: unrecognized escape sequence
==== m3_p2_gas_depletion_efficiency_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\cite\{|\citep\{|\citet\{|Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability|Acknowledgments|Acknowledgements)
                          ^^
error: unrecognized escape sequence
==== m3_p3_simulation_validation_integrated.tex
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\section\{|\subsection\{|\caption\{|\cite\{|\citep\{|\citet\{|Conclusion|Conclusions|Summary|Discussion|Limitations|Data availability|Code availability|Acknowledgments|Acknowledgements)
                          ^^
error: unrecognized escape sequence

exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/*/data/source_analysis_results.json; do echo "==== $(basename $(dirname "$f"))"; jq -r '"'{short_title, proposal_title, pilot_question, interpretation_guard, result_bullets, full_proposal_requires, sample_rows, massive_rows, high_density_massive_agn, low_density_massive_agn, high_minus_low_ci} | @json' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== data
{"short_title":null,"proposal_title":null,"pilot_question":null,"interpretation_guard":null,"result_bullets":null,"full_proposal_requires":null,"sample_rows":null,"massive_rows":null,"high_density_massive_agn":null,"low_density_massive_agn":null,"high_minus_low_ci":null}
==== data
{"short_title":"SDSS density proxy for environmental quenching","proposal_title":"Separating internal and environmental quenching across stellar mass, halo mass, and redshift","pilot_question":"Does a nearest-neighbour density proxy add quenched-fraction information beyond stellar mass in the SDSS emission-line sample?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy.","The high-density quartile has quenched fraction 0.230 (3,456/15,000); the low-density quartile has 0.181 (2,710/15,000).","The bootstrap high-minus-low quenched-fraction interval is [0.041, 0.059].","A linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004."],"full_proposal_requires":"group catalogues, robust central/satellite labels, halo masses, morphology, and multi-redshift selection functions.","sample_rows":60000,"massive_rows":null,"high_density_massive_agn":null,"low_density_massive_agn":null,"high_minus_low_ci":[0.04059666666666669,0.059135]}
==== data
{"short_title":"Optical-AGN denominator for maintenance-heating follow-up","proposal_title":"Empirical duty-cycle constraints on AGN maintenance heating in massive halos","pilot_question":"Among massive, low-sSFR SDSS emission-line galaxies, what optical AGN fraction is available as a denominator for X-ray/radio maintenance-heating follow-up?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["The massive subset (logM >= 10.8) contains 9,298 emission-line galaxies; 5,695 are low-sSFR by the pilot threshold.","The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.","This provides an optical duty-cycle denominator for X-ray/radio maintenance-heating follow-up, not a heating-to-cooling measurement."],"full_proposal_requires":"X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.","sample_rows":60000,"massive_rows":9298,"high_density_massive_agn":null,"low_density_massive_agn":null,"high_minus_low_ci":null}
==== data
{"short_title":"SDSS high-excitation AGN denominator for outflow escape tests","proposal_title":"Escape versus recycling: the fate of AGN-driven multiphase outflows","pilot_question":"How large is the SDSS high-excitation optical-AGN denominator that would need resolved kinematics to test escape versus recycling?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074).","Their median log sSFR is -11.53, compared with -10.14 for the full denominator.","SDSS does not measure escape velocity or multiphase outflow velocities here; the pilot supplies a denominator for resolved follow-up rather than an escape/recycling result."],"full_proposal_requires":"resolved outflow velocities, halo potentials, molecular/ionized/neutral gas phases, and CGM recycling tracers.","sample_rows":60000,"massive_rows":null,"high_density_massive_agn":null,"low_density_massive_agn":null,"high_minus_low_ci":null}
==== data
{"short_title":"Environment proxy for optical AGN in massive SDSS hosts","proposal_title":"Environmental dependence of radio-jet coupling efficiency in galaxy gas","pilot_question":"Does a local-density proxy modulate the optical AGN fraction in massive SDSS hosts, motivating environment-stratified radio/X-ray jet-coupling follow-up?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.","The bootstrap high-minus-low interval is [0.112, 0.170].","This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency."],"full_proposal_requires":"radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.","sample_rows":60000,"massive_rows":9298,"high_density_massive_agn":{"fraction":0.5085836909871244,"k":948,"n":1864,"se":0.011579319665266517},"low_density_massive_agn":{"fraction":0.3667152221412964,"k":1007,"n":2746,"se":0.009196312633686535},"high_minus_low_ci":[0.11189880364416133,0.1702164814837969]}
==== data
{"short_title":"SDSS mass transition in quenching and optical AGN incidence","proposal_title":"Locating the transition from stellar-feedback to AGN-feedback regulation","pilot_question":"At what stellar-mass scale do quenched fraction and optical AGN incidence rise in the same SDSS denominator?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["The first stellar-mass bin with quenched fraction above 0.5 is 11.0-12.5.","The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520.","The result is an optical transition diagnostic; gas fractions and baryon deficits are needed before assigning the transition to stellar or AGN feedback."],"full_proposal_requires":"gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.","sample_rows":60000,"massive_rows":null,"high_density_massive_agn":null,"low_density_massive_agn":null,"high_minus_low_ci":null}
==== data
{"short_title":"Common-denominator optical tracer census in SDSS","proposal_title":"A multiphase, common-denominator census of AGN-driven outflows","pilot_question":"How strongly do simple optical tracer definitions change the inferred AGN/feedback-candidate prevalence in one common SDSS denominator?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.","The widest-to-narrowest prevalence ratio is 3.1, before adding molecular, neutral, or X-ray/radio phases.","This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates."],"full_proposal_requires":"ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model.","sample_rows":60000,"massive_rows":null,"high_density_massive_agn":null,"low_density_massive_agn":null,"high_minus_low_ci":null}
==== data
{"short_title":"Optical denominator for gas-fraction versus efficiency tests","proposal_title":"Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies","pilot_question":"How many massive quenched or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction/depletion-time follow-up?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample.","Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.","The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies.","SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline."],"full_proposal_requires":"CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.","sample_rows":60000,"massive_rows":null,"high_density_massive_agn":null,"low_density_massive_agn":null,"high_minus_low_ci":null}
==== data
{"short_title":"SDSS target vector for feedback-model validation","proposal_title":"Forward-modelled validation of cosmological feedback prescriptions","pilot_question":"What compact SDSS target vector of quenched fraction, optical AGN incidence, and colour versus mass/redshift can be used for forward-model validation?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["The pilot writes 15 mass-redshift cells with n >= 50 as a compact validation vector.","Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.","The output is an observed target vector for simulation forward modelling, not a direct simulation comparison."],"full_proposal_requires":"simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.","sample_rows":60000,"massive_rows":null,"high_density_massive_agn":null,"low_density_massive_agn":null,"high_minus_low_ci":null}

exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/*.md /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/*.md; do [ -f "$f" ] || continue; echo "==== $f"; rg -n "sdss_agn_sfr_pilot|m2_p1_outflow_escape_recycling|m2_p2_radio_jet_environment|m2_p3_feedback_transition_mass|m3_p1_multiphase_census|m3_p2_gas_depletion_efficiency|m3_p3_simulation_validation|proposal|pilot|association|proxy|denominator|selection-aware" "$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on outflows and feedback regimes
3:> This page presents three proposal-style research programmes on outflow fate, jet coupling, and the transition from stellar-feedback to AGN-linked regulation. The proposals are framed around measurable observables, matched denominators, and explicit decision criteria.
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- P1: [SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot (PDF)](m2_p1_outflow_escape_recycling_aas.pdf)
8:- P2: [Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot (PDF)](m2_p2_radio_jet_environment_aas.pdf)
9:- P3: [SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot (PDF)](m2_p3_feedback_transition_mass_aas.pdf)
11:3 proposal-style research programmes.
26:**Analysis/test and decision criterion.** Compare outflow velocity distributions with halo escape velocities inferred from dynamical/halo-mass estimates, then model escaped versus bound/recycling fractions as a function of stellar mass, halo mass, and redshift. A high escaped fraction at fixed denominator supports permanent-removal feedback; a low escaped fraction supports recycling-limited regulation.
56:**Remaining uncertainty.** The observational crossover mass between stellar-feedback-dominated regulation and AGN-linked regulation is not cleanly measured with the same denominator and gas observables.
58:**Survey/data plan.** DESI/GAMA/COSMOS parent samples with stellar mass and halo proxy; ALFALFA/FASHI HI and ALMA CO gas fractions; optical/IR SFRs; X-ray/radio AGN indicators; JWST for high-redshift extension.
66:- Evidence-traceability work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.
70:These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.
==== /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
1:# Galaxy Evolution — Research proposals on outflows and feedback regimes
3:> This page presents three proposal-style research programmes on outflow fate, jet coupling, and the transition from stellar-feedback to AGN-linked regulation. The proposals are framed around measurable observables, matched denominators, and explicit decision criteria.
5:**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
7:- P1: [SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot (PDF)](m2_p1_outflow_escape_recycling_aas.pdf)
8:- P2: [Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot (PDF)](m2_p2_radio_jet_environment_aas.pdf)
9:- P3: [SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot (PDF)](m2_p3_feedback_transition_mass_aas.pdf)
11:3 proposal-style research programmes.
26:**Analysis/test and decision criterion.** Compare outflow velocity distributions with halo escape velocities inferred from dynamical/halo-mass estimates, then model escaped versus bound/recycling fractions as a function of stellar mass, halo mass, and redshift. A high escaped fraction at fixed denominator supports permanent-removal feedback; a low escaped fraction supports recycling-limited regulation.
56:**Remaining uncertainty.** The observational crossover mass between stellar-feedback-dominated regulation and AGN-linked regulation is not cleanly measured with the same denominator and gas observables.
58:**Survey/data plan.** DESI/GAMA/COSMOS parent samples with stellar mass and halo proxy; ALFALFA/FASHI HI and ALMA CO gas fractions; optical/IR SFRs; X-ray/radio AGN indicators; JWST for high-redshift extension.
66:- Evidence-traceability work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.
70:These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.

codex
The source-analysis JSON shows the pilot numbers and the required interpretation guard are already real-data constrained. I’m now checking whether the TeX actually preserves those boundaries, especially in the abstract, conclusion, and any figure-caption phrasing that could drift into causal language.
exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/*/aastex/*_integrated.tex; do echo "==== $(basename "$f")"; sed -n '"'1,120p' \""'$f" | sed -n '"'/\\\\begin{abstract}/, /\\\\end{abstract}/p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== m1_rp1_sdss_agn_sfr_integrated.tex
\begin{abstract}
We integrate the strongest Galaxy Evolution pilot into a selection-aware short-paper draft: a matched-control comparison of catalog specific star formation in broad BPT optical AGN hosts and star-forming controls in SDSS DR17. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a flagship short-paper draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}
==== m1_rp2_environment_quenching_integrated.tex
\begin{abstract}
We integrate the active proposal 'Separating internal and environmental quenching across stellar mass, halo mass, and redshift' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}
==== m1_rp3_maintenance_heating_integrated.tex
\begin{abstract}
We integrate the active proposal 'Empirical duty-cycle constraints on AGN maintenance heating in massive halos' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}
==== m2_p1_outflow_escape_recycling_integrated.tex
\begin{abstract}
We integrate the active proposal 'Escape versus recycling: the fate of AGN-driven multiphase outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}
==== m2_p2_radio_jet_environment_integrated.tex
\begin{abstract}
We integrate the active proposal 'Environmental dependence of radio-jet coupling efficiency in galaxy gas' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}
==== m2_p3_feedback_transition_mass_integrated.tex
\begin{abstract}
We integrate the active proposal 'Locating the transition from stellar-feedback to AGN-feedback regulation' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}
==== m3_p1_multiphase_census_integrated.tex
\begin{abstract}
We integrate the active proposal 'A multiphase, common-denominator census of AGN-driven outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}
==== m3_p2_gas_depletion_efficiency_integrated.tex
\begin{abstract}
We integrate the active proposal 'Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}
==== m3_p3_simulation_validation_integrated.tex
\begin{abstract}
We integrate the active proposal 'Forward-modelled validation of cosmological feedback prescriptions' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
\end{abstract}

exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/*/aastex/*_integrated.tex; do echo "==== $(basename "$f")"; rg -n -F -e '"'\\begin{abstract}' -e '\\end{abstract}' -e '\\section{' -e '\\subsection{' -e '\\caption{' -e '\\cite{' -e '\\citep{' -e '\\citet{' -e 'Conclusion' -e 'Conclusions' -e 'Summary' -e 'Discussion' -e 'Limitations' -e 'Data availability' -e 'Code availability' -e 'Acknowledgments' -e 'Acknowledgements' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== m1_rp1_sdss_agn_sfr_integrated.tex
12:\begin{abstract}
14:\end{abstract}
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
49:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
52:\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
53:BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. The cached analysis table contains 39,553 star-forming galaxies, 12,234 intermediate/composite objects, 8,146 broad optical AGN, and 67 unclassified objects.
69:\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used by the flagship RP-1 integration. This figure verifies the measured line-ratio denominator and broad optical classification; it does not by itself identify causal AGN feedback.}
76:\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset is robust within the optical emission-line subset but remains selection- and subclass-dependent.}
81:\section{Reproducibility and safety}\label{sec:repro}
84:\section{Conclusion}\label{sec:conclusion}
==== m1_rp2_environment_quenching_integrated.tex
12:\begin{abstract}
14:\end{abstract}
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
49:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
66:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for packet-gated-paper-to-wiki-reconciliation rp-2. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
70:\section{Interpretation and missing observables}\label{sec:missing}
73:Mass and environment are known separable axes in low-redshift galaxy evolution, but a real environmental-quenching analysis requires group/halo and central-satellite information beyond this nearest-neighbour proxy \citep{peng2010,baldry2006,wetzel2013,goubert2024}.
76:\section{Reproducibility and safety}\label{sec:repro}
79:\section{Conclusion}\label{sec:conclusion}
==== m1_rp3_maintenance_heating_integrated.tex
12:\begin{abstract}
14:\end{abstract}
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
49:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
65:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for packet-gated-paper-to-wiki-reconciliation rp-3. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
69:\section{Interpretation and missing observables}\label{sec:missing}
72:Radio-mode and hot-atmosphere studies define the future calorimetric observables--jet power, cavities, cooling luminosity, and group gas--that are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}.
75:\section{Reproducibility and safety}\label{sec:repro}
78:\section{Conclusion}\label{sec:conclusion}
==== m2_p1_outflow_escape_recycling_integrated.tex
12:\begin{abstract}
14:\end{abstract}
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
49:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
65:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for source-first-paper-adjudication p1. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
69:\section{Interpretation and missing observables}\label{sec:missing}
72:Wind and outflow literature specifies the missing kinematic, geometric, molecular, and multiphase measurements; these sources motivate follow-up and do not turn line-ratio selection into an escape/recycling measurement \citep{veilleux2005,cicone2014,fiore2017,carniani2017,fabian2012}.
75:\section{Reproducibility and safety}\label{sec:repro}
78:\section{Conclusion}\label{sec:conclusion}
==== m2_p2_radio_jet_environment_integrated.tex
12:\begin{abstract}
14:\end{abstract}
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
49:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
65:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for source-first-paper-adjudication p2. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
69:\section{Interpretation and missing observables}\label{sec:missing}
72:The radio/X-ray/group literature motivates environment-stratified follow-up, but the present result is only an optical BPT-AGN fraction versus an internal density proxy \citep{best2005,santoro2020,mcnamara2007,eckert2024}.
75:\section{Reproducibility and safety}\label{sec:repro}
78:\section{Conclusion}\label{sec:conclusion}
==== m2_p3_feedback_transition_mass_integrated.tex
12:\begin{abstract}
14:\end{abstract}
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
49:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
65:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for source-first-paper-adjudication p3. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
69:\section{Interpretation and missing observables}\label{sec:missing}
72:Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.
75:\section{Reproducibility and safety}\label{sec:repro}
78:\section{Conclusion}\label{sec:conclusion}
==== m3_p1_multiphase_census_integrated.tex
12:\begin{abstract}
14:\end{abstract}
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
49:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
65:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for debate-map-to-wiki-rebuild p1. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
69:\section{Interpretation and missing observables}\label{sec:missing}
72:A real multiphase census needs independent ionized, neutral, molecular, and energetic outflow observables; the present SDSS thresholds are an optical denominator only \citep{veilleux2005,rupke2018,cicone2014,fiore2017,feruglio2015,woo2016,bae2018}.
75:\section{Reproducibility and safety}\label{sec:repro}
78:\section{Conclusion}\label{sec:conclusion}
==== m3_p2_gas_depletion_efficiency_integrated.tex
12:\begin{abstract}
14:\end{abstract}
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
49:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
66:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for debate-map-to-wiki-rebuild p2. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
70:\section{Interpretation and missing observables}\label{sec:missing}
73:Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs; optical H$\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \citep{coldgass1,coldgass2,xcoldgass2017,xgass2018}.
76:\section{Reproducibility and safety}\label{sec:repro}
79:\section{Conclusion}\label{sec:conclusion}
==== m3_p3_simulation_validation_integrated.tex
12:\begin{abstract}
14:\end{abstract}
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
49:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
65:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for debate-map-to-wiki-rebuild p3. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
69:\section{Interpretation and missing observables}\label{sec:missing}
72:Simulation suites and mock-observation methods define the future comparison problem; no simulation mock has been forward-modelled or ranked in this pilot \citep{tng2019,eagle2015,simba2019,imanga2023,donnari2021,dubois2013,dubois2016}.
75:\section{Reproducibility and safety}\label{sec:repro}
78:\section{Conclusion}\label{sec:conclusion}

exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/*/aastex/*_integrated.tex; do echo "==== $(basename "$f")"; tail -n 120 "$f" | rg -n -F -e '"'\\section{' -e '\\subsection{' -e '\\caption{' -e '\\bibliography{' -e '\\begin{thebibliography}' -e 'Conclusion' -e 'Limitations' -e 'Data availability' -e 'Code availability'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== m1_rp1_sdss_agn_sfr_integrated.tex
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
69:\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used by the flagship RP-1 integration. This figure verifies the measured line-ratio denominator and broad optical classification; it does not by itself identify causal AGN feedback.}
76:\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset is robust within the optical emission-line subset but remains selection- and subclass-dependent.}
81:\section{Reproducibility and safety}\label{sec:repro}
84:\section{Conclusion}\label{sec:conclusion}
88:\begin{thebibliography}{}
==== m1_rp2_environment_quenching_integrated.tex
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
66:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for packet-gated-paper-to-wiki-reconciliation rp-2. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
70:\section{Interpretation and missing observables}\label{sec:missing}
76:\section{Reproducibility and safety}\label{sec:repro}
79:\section{Conclusion}\label{sec:conclusion}
83:\begin{thebibliography}{}
==== m1_rp3_maintenance_heating_integrated.tex
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
65:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for packet-gated-paper-to-wiki-reconciliation rp-3. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
69:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Reproducibility and safety}\label{sec:repro}
78:\section{Conclusion}\label{sec:conclusion}
82:\begin{thebibliography}{}
==== m2_p1_outflow_escape_recycling_integrated.tex
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
65:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for source-first-paper-adjudication p1. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
69:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Reproducibility and safety}\label{sec:repro}
78:\section{Conclusion}\label{sec:conclusion}
82:\begin{thebibliography}{}
==== m2_p2_radio_jet_environment_integrated.tex
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
65:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for source-first-paper-adjudication p2. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
69:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Reproducibility and safety}\label{sec:repro}
78:\section{Conclusion}\label{sec:conclusion}
82:\begin{thebibliography}{}
==== m2_p3_feedback_transition_mass_integrated.tex
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
65:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for source-first-paper-adjudication p3. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
69:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Reproducibility and safety}\label{sec:repro}
78:\section{Conclusion}\label{sec:conclusion}
82:\begin{thebibliography}{}
==== m3_p1_multiphase_census_integrated.tex
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
65:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for debate-map-to-wiki-rebuild p1. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
69:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Reproducibility and safety}\label{sec:repro}
78:\section{Conclusion}\label{sec:conclusion}
82:\begin{thebibliography}{}
==== m3_p2_gas_depletion_efficiency_integrated.tex
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
66:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for debate-map-to-wiki-rebuild p2. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
70:\section{Interpretation and missing observables}\label{sec:missing}
76:\section{Reproducibility and safety}\label{sec:repro}
79:\section{Conclusion}\label{sec:conclusion}
83:\begin{thebibliography}{}
==== m3_p3_simulation_validation_integrated.tex
18:\section{Purpose and claim contract}\label{sec:purpose}
24:\section{Shared parent sample and selection function}\label{sec:shared-selection}
48:\section{Measurements}\label{sec:measurements}
52:\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
65:\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for debate-map-to-wiki-rebuild p3. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
69:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Reproducibility and safety}\label{sec:repro}
78:\section{Conclusion}\label{sec:conclusion}
82:\begin{thebibliography}{}

exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex; do echo "==== $f"; [ -f "$f" ] && nl -ba "$f" | sed -n '"'1,120p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709D163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Environment proxy for optical AGN in massive SDSS hosts}
     5	\shortauthors{NebulaMind local integration}
     6	\begin{document}
     7	
     8	\title{Environment proxy for optical AGN in massive SDSS hosts: selection-aware SDSS optical proxy integration}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Local reproducible integration run; public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We integrate the active proposal 'Environmental dependence of radio-jet coupling efficiency in galaxy gas' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Purpose and claim contract}\label{sec:purpose}
    19	This draft preserves the active proposal title, 'Environmental dependence of radio-jet coupling efficiency in galaxy gas', but narrows the supported claim to the cached SDSS optical measurement named in the results. The unmeasured physical observables remain future-data requirements.
    20	
    21	The claim contract is intentionally conservative. Quantities measured here are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. Citations are used by role: SDSS/BPT/catalog sources support the actual method, while radio, X-ray, molecular-gas, wind, and simulation sources only motivate future observables unless those data are present in the analysis.
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
    36	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
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
    65	\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for source-first-paper-adjudication p2. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
    66	\label{fig:topic}
    67	\end{figure}
    68	
    69	\section{Interpretation and missing observables}\label{sec:missing}
    70	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.
    71	
    72	The radio/X-ray/group literature motivates environment-stratified follow-up, but the present result is only an optical BPT-AGN fraction versus an internal density proxy \citep{best2005,santoro2020,mcnamara2007,eckert2024}.
    73	
    74	
    75	\section{Reproducibility and safety}\label{sec:repro}
    76	This manuscript was generated by local integration run \texttt{INTEGRATED\_9\_PAPERS\_20260709T012051Z}. Inputs are the original RP-1 SDSS query/run directory, the eight-topic SDSS remaining-topic manifest, the overnight shared selection-function packet, the cached-versus-public representativeness packet, Goru robustness outputs, and literature/source placement packets. The output is a local draft PDF and manifest entry only. No public-linked PDF was replaced.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
    80	
    81	
    82	\begin{thebibliography}{}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    88	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    89	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    90	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    91	
    92	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    93	\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, arXiv:2403.17145
    94	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
    95	\bibitem[Santoro et al.(2020)]{santoro2020} Santoro, F., Tadhunter, C., Baron, D., Morganti, R., \& Holt, J. 2020, A\&A, 644, A54
    96	\end{thebibliography}
    97	
    98	\end{document}
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS mass transition in quenching and optical AGN incidence}
     5	\shortauthors{NebulaMind local integration}
     6	\begin{document}
     7	
     8	\title{SDSS mass transition in quenching and optical AGN incidence: selection-aware SDSS optical proxy integration}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Local reproducible integration run; public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We integrate the active proposal 'Locating the transition from stellar-feedback to AGN-feedback regulation' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Purpose and claim contract}\label{sec:purpose}
    19	This draft preserves the active proposal title, 'Locating the transition from stellar-feedback to AGN-feedback regulation', but narrows the supported claim to the cached SDSS optical measurement named in the results. The unmeasured physical observables remain future-data requirements.
    20	
    21	The claim contract is intentionally conservative. Quantities measured here are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. Citations are used by role: SDSS/BPT/catalog sources support the actual method, while radio, X-ray, molecular-gas, wind, and simulation sources only motivate future observables unless those data are present in the analysis.
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
    36	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
    53	The consolidated proposal question is: At what stellar-mass scale do quenched fraction and optical AGN incidence rise in the same SDSS denominator? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.
    54	
    55	\begin{itemize}
    56	\item The first stellar-mass bin with quenched fraction above 0.5 is 11.0-12.5.
    57	\item The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520.
    58	\item The result is an optical transition diagnostic; gas fractions and baryon deficits are needed before assigning the transition to stellar or AGN feedback.
    59	\end{itemize}
    60	
    61	
    62	\begin{figure}
    63	\centering
    64	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    65	\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for source-first-paper-adjudication p3. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
    66	\label{fig:topic}
    67	\end{figure}
    68	
    69	\section{Interpretation and missing observables}\label{sec:missing}
    70	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.
    71	
    72	Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.
    73	
    74	
    75	\section{Reproducibility and safety}\label{sec:repro}
    76	This manuscript was generated by local integration run \texttt{INTEGRATED\_9\_PAPERS\_20260709T012051Z}. Inputs are the original RP-1 SDSS query/run directory, the eight-topic SDSS remaining-topic manifest, the overnight shared selection-function packet, the cached-versus-public representativeness packet, Goru robustness outputs, and literature/source placement packets. The output is a local draft PDF and manifest entry only. No public-linked PDF was replaced.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
    80	
    81	
    82	\begin{thebibliography}{}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    88	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    89	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    90	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    91	
    92	\bibitem[Baldry et al.(2004)]{baldry2004} Baldry, I.~K., Glazebrook, K., Brinkmann, J., et al. 2004, ApJ, 600, 681
    93	\bibitem[Bluck et al.(2023)]{bluck2023} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108
    94	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
    95	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
    96	\bibitem[Peng et al.(2012)]{peng2012} Peng, Y.-j., Lilly, S.~J., Renzini, A., \& Carollo, M. 2012, ApJ, 757, 4
    97	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
    98	\end{thebibliography}
    99	
   100	\end{document}

exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex; do echo "==== $f"; nl -ba "$f" | sed -n '"'1,120p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS optical AGN/sSFR matched-control pilot}
     5	\shortauthors{NebulaMind local integration}
     6	\begin{document}
     7	
     8	\title{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Local reproducible integration run; public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We integrate the strongest Galaxy Evolution pilot into a selection-aware short-paper draft: a matched-control comparison of catalog specific star formation in broad BPT optical AGN hosts and star-forming controls in SDSS DR17. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a flagship short-paper draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Purpose and claim contract}\label{sec:purpose}
    19	This is the flagship local integration draft. It tests an optical-classification-associated catalog-sSFR offset, not causal AGN feedback, gas depletion, or halo maintenance heating.
    20	
    21	The claim contract is intentionally conservative. Quantities measured here are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. Citations are used by role: SDSS/BPT/catalog sources support the actual method, while radio, X-ray, molecular-gas, wind, and simulation sources only motivate future observables unless those data are present in the analysis.
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
    36	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
    53	BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. The cached analysis table contains 39,553 star-forming galaxies, 12,234 intermediate/composite objects, 8,146 broad optical AGN, and 67 unclassified objects.
    54	
    55	The preferred estimator matches every broad optical AGN host to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. This is an association design; controls are not matched in morphology, halo mass, gas mass, aperture scale, AGN luminosity, or duty-cycle phase.
    56	
    57	\begin{itemize}
    58	\item Broad BPT optical AGN vs. star-forming controls at S/N$\geq3$: $N=8,146$ matched pairs, median $\Delta\log {\rm sSFR}=-1.309$ dex with 95\% bootstrap interval $[-1.334,-1.283]$ dex.
    59	\item Moderate mass-redshift caliper $|\Delta\log M_\star|\leq0.05$, $|\Delta z|\leq0.002$: $N=7,867$ retained pairs (96.6\% target coverage), median offset -1.318 dex.
    60	\item A deterministic no-replacement diagnostic uses $N=7,419$ pairs and gives median offset -1.446 dex, but with visibly poorer mass balance; it is a stress test, not the preferred estimator.
    61	\item Raising the line-S/N threshold to 10 leaves $N=1,530$ matched pairs and reduces the median offset to -0.744 dex, showing sensitivity to the emission-line selection function.
    62	\item A narrower [N II] Seyfert-like proxy gives $N=2,114$ pairs and median offset -0.763 dex, reinforcing that subclass definitions change the effect size.
    63	\end{itemize}
    64	
    65	
    66	\begin{figure*}
    67	\centering
    68	\includegraphics[width=0.73\textwidth]{../figures/fig-bpt.pdf}
    69	\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used by the flagship RP-1 integration. This figure verifies the measured line-ratio denominator and broad optical classification; it does not by itself identify causal AGN feedback.}
    70	\label{fig:bpt}
    71	\end{figure*}
    72	
    73	\begin{figure*}
    74	\centering
    75	\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
    76	\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset is robust within the optical emission-line subset but remains selection- and subclass-dependent.}
    77	\label{fig:offsets}
    78	\end{figure*}
    79	
    80	
    81	\section{Reproducibility and safety}\label{sec:repro}
    82	This manuscript was generated by local integration run \texttt{INTEGRATED\_9\_PAPERS\_20260709T012051Z}. Inputs are the original RP-1 SDSS query/run directory, the eight-topic SDSS remaining-topic manifest, the overnight shared selection-function packet, the cached-versus-public representativeness packet, Goru robustness outputs, and literature/source placement packets. The output is a local draft PDF and manifest entry only. No public-linked PDF was replaced.
    83	
    84	\section{Conclusion}\label{sec:conclusion}
    85	The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
    86	
    87	
    88	\begin{thebibliography}{}
    89	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    90	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    91	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    92	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    93	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    94	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    95	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    96	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    97	
    98	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
    99	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   100	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   101	\end{thebibliography}
   102	
   103	\end{document}
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS density proxy for environmental quenching}
     5	\shortauthors{NebulaMind local integration}
     6	\begin{document}
     7	
     8	\title{SDSS density proxy for environmental quenching: selection-aware SDSS optical proxy integration}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Local reproducible integration run; public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We integrate the active proposal 'Separating internal and environmental quenching across stellar mass, halo mass, and redshift' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Purpose and claim contract}\label{sec:purpose}
    19	This draft preserves the active proposal title, 'Separating internal and environmental quenching across stellar mass, halo mass, and redshift', but narrows the supported claim to the cached SDSS optical measurement named in the results. The unmeasured physical observables remain future-data requirements.
    20	
    21	The claim contract is intentionally conservative. Quantities measured here are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. Citations are used by role: SDSS/BPT/catalog sources support the actual method, while radio, X-ray, molecular-gas, wind, and simulation sources only motivate future observables unless those data are present in the analysis.
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
    36	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
    53	The consolidated proposal question is: Does a nearest-neighbour density proxy add quenched-fraction information beyond stellar mass in the SDSS emission-line sample? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.
    54	
    55	\begin{itemize}
    56	\item The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy.
    57	\item The high-density quartile has quenched fraction 0.230 (3,456/15,000); the low-density quartile has 0.181 (2,710/15,000).
    58	\item The bootstrap high-minus-low quenched-fraction interval is [0.041, 0.059].
    59	\item A linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004.
    60	\end{itemize}
    61	
    62	
    63	\begin{figure}
    64	\centering
    65	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    66	\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for packet-gated-paper-to-wiki-reconciliation rp-2. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
    67	\label{fig:topic}
    68	\end{figure}
    69	
    70	\section{Interpretation and missing observables}\label{sec:missing}
    71	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: group catalogues, robust central/satellite labels, halo masses, morphology, and multi-redshift selection functions.
    72	
    73	Mass and environment are known separable axes in low-redshift galaxy evolution, but a real environmental-quenching analysis requires group/halo and central-satellite information beyond this nearest-neighbour proxy \citep{peng2010,baldry2006,wetzel2013,goubert2024}.
    74	
    75	
    76	\section{Reproducibility and safety}\label{sec:repro}
    77	This manuscript was generated by local integration run \texttt{INTEGRATED\_9\_PAPERS\_20260709T012051Z}. Inputs are the original RP-1 SDSS query/run directory, the eight-topic SDSS remaining-topic manifest, the overnight shared selection-function packet, the cached-versus-public representativeness packet, Goru robustness outputs, and literature/source placement packets. The output is a local draft PDF and manifest entry only. No public-linked PDF was replaced.
    78	
    79	\section{Conclusion}\label{sec:conclusion}
    80	The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
    81	
    82	
    83	\begin{thebibliography}{}
    84	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    85	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    86	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    87	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    88	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	
    93	\bibitem[Baldry et al.(2006)]{baldry2006} Baldry, I.~K., Balogh, M.~L., Bower, R.~G., et al. 2006, MNRAS, 373, 469
    94	\bibitem[Goubert et al.(2024)]{goubert2024} Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2024, arXiv:2401.12953
    95	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
    96	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
    97	\end{thebibliography}
    98	
    99	\end{document}
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Optical-AGN denominator for maintenance-heating follow-up}
     5	\shortauthors{NebulaMind local integration}
     6	\begin{document}
     7	
     8	\title{Optical-AGN denominator for maintenance-heating follow-up: selection-aware SDSS optical proxy integration}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Local reproducible integration run; public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We integrate the active proposal 'Empirical duty-cycle constraints on AGN maintenance heating in massive halos' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Purpose and claim contract}\label{sec:purpose}
    19	This draft preserves the active proposal title, 'Empirical duty-cycle constraints on AGN maintenance heating in massive halos', but narrows the supported claim to the cached SDSS optical measurement named in the results. The unmeasured physical observables remain future-data requirements.
    20	
    21	The claim contract is intentionally conservative. Quantities measured here are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. Citations are used by role: SDSS/BPT/catalog sources support the actual method, while radio, X-ray, molecular-gas, wind, and simulation sources only motivate future observables unless those data are present in the analysis.
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
    36	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
    53	The consolidated proposal question is: Among massive, low-sSFR SDSS emission-line galaxies, what optical AGN fraction is available as a denominator for X-ray/radio maintenance-heating follow-up? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.
    54	
    55	\begin{itemize}
    56	\item The massive subset (logM >= 10.8) contains 9,298 emission-line galaxies; 5,695 are low-sSFR by the pilot threshold.
    57	\item The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.
    58	\item This provides an optical duty-cycle denominator for X-ray/radio maintenance-heating follow-up, not a heating-to-cooling measurement.
    59	\end{itemize}
    60	
    61	
    62	\begin{figure}
    63	\centering
    64	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    65	\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for packet-gated-paper-to-wiki-reconciliation rp-3. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
    66	\label{fig:topic}
    67	\end{figure}
    68	
    69	\section{Interpretation and missing observables}\label{sec:missing}
    70	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.
    71	
    72	Radio-mode and hot-atmosphere studies define the future calorimetric observables--jet power, cavities, cooling luminosity, and group gas--that are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}.
    73	
    74	
    75	\section{Reproducibility and safety}\label{sec:repro}
    76	This manuscript was generated by local integration run \texttt{INTEGRATED\_9\_PAPERS\_20260709T012051Z}. Inputs are the original RP-1 SDSS query/run directory, the eight-topic SDSS remaining-topic manifest, the overnight shared selection-function packet, the cached-versus-public representativeness packet, Goru robustness outputs, and literature/source placement packets. The output is a local draft PDF and manifest entry only. No public-linked PDF was replaced.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
    80	
    81	
    82	\begin{thebibliography}{}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    88	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    89	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    90	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    91	
    92	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    93	\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, arXiv:2403.17145
    94	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
    95	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
    96	\bibitem[McNamara \& Nulsen(2012)]{mcnamara2012} McNamara, B.~R., \& Nulsen, P.~E.~J. 2012, New J. Phys., 14, 055023
    97	\end{thebibliography}
    98	
    99	\end{document}

exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex; do echo "==== $f"; nl -ba "$f" | sed -n '"'1,120p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Common-denominator optical tracer census in SDSS}
     5	\shortauthors{NebulaMind local integration}
     6	\begin{document}
     7	
     8	\title{Common-denominator optical tracer census in SDSS: selection-aware SDSS optical proxy integration}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Local reproducible integration run; public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We integrate the active proposal 'A multiphase, common-denominator census of AGN-driven outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Purpose and claim contract}\label{sec:purpose}
    19	This draft preserves the active proposal title, 'A multiphase, common-denominator census of AGN-driven outflows', but narrows the supported claim to the cached SDSS optical measurement named in the results. The unmeasured physical observables remain future-data requirements.
    20	
    21	The claim contract is intentionally conservative. Quantities measured here are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. Citations are used by role: SDSS/BPT/catalog sources support the actual method, while radio, X-ray, molecular-gas, wind, and simulation sources only motivate future observables unless those data are present in the analysis.
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
    36	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
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
    65	\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for debate-map-to-wiki-rebuild p1. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
    66	\label{fig:topic}
    67	\end{figure}
    68	
    69	\section{Interpretation and missing observables}\label{sec:missing}
    70	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model.
    71	
    72	A real multiphase census needs independent ionized, neutral, molecular, and energetic outflow observables; the present SDSS thresholds are an optical denominator only \citep{veilleux2005,rupke2018,cicone2014,fiore2017,feruglio2015,woo2016,bae2018}.
    73	
    74	
    75	\section{Reproducibility and safety}\label{sec:repro}
    76	This manuscript was generated by local integration run \texttt{INTEGRATED\_9\_PAPERS\_20260709T012051Z}. Inputs are the original RP-1 SDSS query/run directory, the eight-topic SDSS remaining-topic manifest, the overnight shared selection-function packet, the cached-versus-public representativeness packet, Goru robustness outputs, and literature/source placement packets. The output is a local draft PDF and manifest entry only. No public-linked PDF was replaced.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
    80	
    81	
    82	\begin{thebibliography}{}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    88	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    89	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    90	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    91	
    92	\bibitem[Bae \& Woo(2018)]{bae2018} Bae, H.-J., \& Woo, J.-H. 2018, ApJ, 853, 185
    93	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
    94	\bibitem[Feruglio et al.(2015)]{feruglio2015} Feruglio, C., Fiore, F., Carniani, S., et al. 2015, A\&A, 583, A99
    95	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
    96	\bibitem[Rupke(2018)]{rupke2018} Rupke, D.~S.~N. 2018, Galaxies, 6, 138
    97	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
    98	\bibitem[Woo et al.(2016)]{woo2016} Woo, J.-H., Bae, H.-J., Son, D., \& Karouzos, M. 2016, ApJ, 817, 108
    99	\end{thebibliography}
   100	
   101	\end{document}
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Optical denominator for gas-fraction versus efficiency tests}
     5	\shortauthors{NebulaMind local integration}
     6	\begin{document}
     7	
     8	\title{Optical denominator for gas-fraction versus efficiency tests: selection-aware SDSS optical proxy integration}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Local reproducible integration run; public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We integrate the active proposal 'Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Purpose and claim contract}\label{sec:purpose}
    19	This draft preserves the active proposal title, 'Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies', but narrows the supported claim to the cached SDSS optical measurement named in the results. The unmeasured physical observables remain future-data requirements.
    20	
    21	The claim contract is intentionally conservative. Quantities measured here are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. Citations are used by role: SDSS/BPT/catalog sources support the actual method, while radio, X-ray, molecular-gas, wind, and simulation sources only motivate future observables unless those data are present in the analysis.
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
    36	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
    53	The consolidated proposal question is: How many massive quenched or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction/depletion-time follow-up? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.
    54	
    55	\begin{itemize}
    56	\item The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample.
    57	\item Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.
    58	\item The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies.
    59	\item SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline.
    60	\end{itemize}
    61	
    62	
    63	\begin{figure}
    64	\centering
    65	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    66	\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for debate-map-to-wiki-rebuild p2. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
    67	\label{fig:topic}
    68	\end{figure}
    69	
    70	\section{Interpretation and missing observables}\label{sec:missing}
    71	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.
    72	
    73	Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs; optical H$\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \citep{coldgass1,coldgass2,xcoldgass2017,xgass2018}.
    74	
    75	
    76	\section{Reproducibility and safety}\label{sec:repro}
    77	This manuscript was generated by local integration run \texttt{INTEGRATED\_9\_PAPERS\_20260709T012051Z}. Inputs are the original RP-1 SDSS query/run directory, the eight-topic SDSS remaining-topic manifest, the overnight shared selection-function packet, the cached-versus-public representativeness packet, Goru robustness outputs, and literature/source placement packets. The output is a local draft PDF and manifest entry only. No public-linked PDF was replaced.
    78	
    79	\section{Conclusion}\label{sec:conclusion}
    80	The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
    81	
    82	
    83	\begin{thebibliography}{}
    84	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    85	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    86	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    87	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    88	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	
    93	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
    94	\bibitem[Saintonge et al.(2011a)]{coldgass1} Saintonge, A., Kauffmann, G., Kramer, C., et al. 2011a, MNRAS, 415, 32
    95	\bibitem[Saintonge et al.(2011b)]{coldgass2} Saintonge, A., Kauffmann, G., Wang, J., et al. 2011b, MNRAS, 415, 61
    96	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
    97	\end{thebibliography}
    98	
    99	\end{document}
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS target vector for feedback-model validation}
     5	\shortauthors{NebulaMind local integration}
     6	\begin{document}
     7	
     8	\title{SDSS target vector for feedback-model validation: selection-aware SDSS optical proxy integration}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Local reproducible integration run; public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We integrate the active proposal 'Forward-modelled validation of cosmological feedback prescriptions' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Purpose and claim contract}\label{sec:purpose}
    19	This draft preserves the active proposal title, 'Forward-modelled validation of cosmological feedback prescriptions', but narrows the supported claim to the cached SDSS optical measurement named in the results. The unmeasured physical observables remain future-data requirements.
    20	
    21	The claim contract is intentionally conservative. Quantities measured here are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. Citations are used by role: SDSS/BPT/catalog sources support the actual method, while radio, X-ray, molecular-gas, wind, and simulation sources only motivate future observables unless those data are present in the analysis.
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
    36	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
    53	The consolidated proposal question is: What compact SDSS target vector of quenched fraction, optical AGN incidence, and colour versus mass/redshift can be used for forward-model validation? The integrated manuscript deliberately demotes the claim to the directly measured SDSS quantity. It is not a full physical-feedback test.
    54	
    55	\begin{itemize}
    56	\item The pilot writes 15 mass-redshift cells with n >= 50 as a compact validation vector.
    57	\item Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.
    58	\item The output is an observed target vector for simulation forward modelling, not a direct simulation comparison.
    59	\end{itemize}
    60	
    61	
    62	\begin{figure}
    63	\centering
    64	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    65	\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for debate-map-to-wiki-rebuild p3. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
    66	\label{fig:topic}
    67	\end{figure}
    68	
    69	\section{Interpretation and missing observables}\label{sec:missing}
    70	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.
    71	
    72	Simulation suites and mock-observation methods define the future comparison problem; no simulation mock has been forward-modelled or ranked in this pilot \citep{tng2019,eagle2015,simba2019,imanga2023,donnari2021,dubois2013,dubois2016}.
    73	
    74	
    75	\section{Reproducibility and safety}\label{sec:repro}
    76	This manuscript was generated by local integration run \texttt{INTEGRATED\_9\_PAPERS\_20260709T012051Z}. Inputs are the original RP-1 SDSS query/run directory, the eight-topic SDSS remaining-topic manifest, the overnight shared selection-function packet, the cached-versus-public representativeness packet, Goru robustness outputs, and literature/source placement packets. The output is a local draft PDF and manifest entry only. No public-linked PDF was replaced.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
    80	
    81	
    82	\begin{thebibliography}{}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    88	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    89	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    90	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    91	
    92	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
    93	\bibitem[Donnari et al.(2021)]{donnari2021} Donnari, M., Pillepich, A., Nelson, D., et al. 2021, MNRAS, 506, 4760
    94	\bibitem[Dubois et al.(2013)]{dubois2013} Dubois, Y., Gavazzi, R., Peirani, S., \& Silk, J. 2013, MNRAS, 433, 3297
    95	\bibitem[Dubois et al.(2016)]{dubois2016} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, MNRAS, 463, 3948
    96	\bibitem[Nanni et al.(2023)]{imanga2023} Nanni, L., Thomas, D., Trayford, J., et al. 2023, MNRAS, 518, 2605
    97	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
    98	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
    99	\end{thebibliography}
   100	
   101	\end{document}

codex
I’ve got the manuscript skeletons. One thing already stands out: the topic papers 2–9 all reuse a generic conclusion paragraph that still names RP-1, which is a reader-flow and coherence problem even if the science is guarded correctly. I’m verifying the remaining paper-specific sections and the public-linked pages to separate template residue from actual claim drift.
exec
/bin/zsh -c "f='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex'; echo \"==== "'$f"; nl -ba "$f" | sed -n '"'1,120p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS high-excitation AGN denominator for outflow escape tests}
     5	\shortauthors{NebulaMind local integration}
     6	\begin{document}
     7	
     8	\title{SDSS high-excitation AGN denominator for outflow escape tests: selection-aware SDSS optical proxy integration}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Local reproducible integration run; public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We integrate the active proposal 'Escape versus recycling: the fate of AGN-driven multiphase outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    17	
    18	\section{Purpose and claim contract}\label{sec:purpose}
    19	This draft preserves the active proposal title, 'Escape versus recycling: the fate of AGN-driven multiphase outflows', but narrows the supported claim to the cached SDSS optical measurement named in the results. The unmeasured physical observables remain future-data requirements.
    20	
    21	The claim contract is intentionally conservative. Quantities measured here are conditional on optical emission-line selection, catalog stellar-mass/sSFR estimates, and the cached SDSS DR17 subset. Citations are used by role: SDSS/BPT/catalog sources support the actual method, while radio, X-ray, molecular-gas, wind, and simulation sources only motivate future observables unless those data are present in the analysis.
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
    36	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    37	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    38	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    39	\enddata
    40	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    41	\end{deluxetable*}
    42	
    43	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this integration is conditional on the four-line emission-line selection.
    44	
    45	Cached-versus-public marginal checks found no redshift, stellar-mass, or sSFR bin with a cached-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    46	
    47	
    48	\section{Measurements}\label{sec:measurements}
    49	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    50	
    51	
    52	\section{Topic-specific optical denominator or proxy result}\label{sec:topic-result}
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
    65	\caption{Topic-specific SDSS DR17 optical denominator/proxy diagnostic for source-first-paper-adjudication p1. The caption is intentionally narrow: this figure summarizes the cached optical result used for target definition or denominator design, not the unmeasured multi-survey physical claim.}
    66	\label{fig:topic}
    67	\end{figure}
    68	
    69	\section{Interpretation and missing observables}\label{sec:missing}
    70	SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: resolved outflow velocities, halo potentials, molecular/ionized/neutral gas phases, and CGM recycling tracers.
    71	
    72	Wind and outflow literature specifies the missing kinematic, geometric, molecular, and multiphase measurements; these sources motivate follow-up and do not turn line-ratio selection into an escape/recycling measurement \citep{veilleux2005,cicone2014,fiore2017,carniani2017,fabian2012}.
    73	
    74	
    75	\section{Reproducibility and safety}\label{sec:repro}
    76	This manuscript was generated by local integration run \texttt{INTEGRATED\_9\_PAPERS\_20260709T012051Z}. Inputs are the original RP-1 SDSS query/run directory, the eight-topic SDSS remaining-topic manifest, the overnight shared selection-function packet, the cached-versus-public representativeness packet, Goru robustness outputs, and literature/source placement packets. The output is a local draft PDF and manifest entry only. No public-linked PDF was replaced.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
    80	
    81	
    82	\begin{thebibliography}{}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    88	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    89	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    90	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    91	
    92	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
    93	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
    94	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
    95	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
    96	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
    97	\end{thebibliography}
    98	
    99	\end{document}

exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md; do echo "==== $f"; nl -ba "$f" | sed -n '"'1,120p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
     1	# Galaxy Evolution — Research proposals on outflows and feedback regimes
     2	
     3	> This page presents three proposal-style research programmes on outflow fate, jet coupling, and the transition from stellar-feedback to AGN-linked regulation. The proposals are framed around measurable observables, matched denominators, and explicit decision criteria.
     4	
     5	**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
     6	
     7	- P1: [SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot (PDF)](m2_p1_outflow_escape_recycling_aas.pdf)
     8	- P2: [Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot (PDF)](m2_p2_radio_jet_environment_aas.pdf)
     9	- P3: [SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot (PDF)](m2_p3_feedback_transition_mass_aas.pdf)
    10	
    11	3 proposal-style research programmes.
    12	
    13	## P1 — Escape versus recycling: the fate of AGN-driven multiphase outflows
    14	
    15	**Hypothesis / objective.** A substantial fraction of AGN-driven outflowing gas remains gravitationally bound and recycles through the circumgalactic medium, limiting the permanence of feedback-driven gas removal.
    16	
    17	**Prior evidence and constraints.**
    18	- Quasar observations show AGN feedback acting on molecular gas reservoirs at high redshift, but such detections do not determine whether gas escapes the halo. [quasar molecular-gas reservoirs](https://arxiv.org/abs/1706.08987).
    19	- Stellar-feedback work on baryon deficiency in low-mass galaxies provides a boundary condition for non-AGN removal channels that must not be confused with AGN-driven escape. [stellar feedback and baryon deficiency](https://arxiv.org/abs/2512.05584).
    20	- Simulated galaxy feedback constraints highlight that gas removal, recycling, and observable baryon fractions depend on halo scale. [simulated observable feedback constraints](https://arxiv.org/abs/0901.1880).
    21	
    22	**Remaining uncertainty.** The escaped fraction of multiphase outflows is unmeasured across a representative mass/redshift sample; an outflow detection is not equivalent to permanent quenching.
    23	
    24	**Survey/data plan.** AGN hosts and inactive controls spanning stellar mass and redshift; MUSE/MaNGA ionized-gas kinematics, ALMA CO and [C II] for cold gas, JWST/NIRSpec for z>2 outflow tracers, and CGM absorption where available to track recycling.
    25	
    26	**Analysis/test and decision criterion.** Compare outflow velocity distributions with halo escape velocities inferred from dynamical/halo-mass estimates, then model escaped versus bound/recycling fractions as a function of stellar mass, halo mass, and redshift. A high escaped fraction at fixed denominator supports permanent-removal feedback; a low escaped fraction supports recycling-limited regulation.
    27	
    28	**Limitations and wording guardrails.** Projection, phase conversion, and uncertain halo potentials can dominate the escaped-fraction error budget.
    29	
    30	## P2 — Environmental dependence of radio-jet coupling efficiency in galaxy gas
    31	
    32	**Hypothesis / objective.** The fraction of radio-jet mechanical power deposited into the multiphase interstellar or circumgalactic medium varies systematically with ambient gas density and host environment.
    33	
    34	**Prior evidence and constraints.**
    35	- Young radio galaxies show AGN-driven outflows and provide an empirical route to estimating feedback efficiency. [young radio galaxies and feedback efficiency](https://arxiv.org/abs/2009.11175).
    36	- Local M51-scale NOEMA data show how jet/AGN activity can affect molecular ISM structure at high spatial resolution, motivating a broader population test. [SWAN IV molecular ISM feedback](https://arxiv.org/abs/2604.15438).
    37	- Galaxy-group feedback studies identify the group regime as a strong testbed for coupling between radio activity and hot gas. [group-scale AGN feedback](https://arxiv.org/abs/2403.17145).
    38	
    39	**Remaining uncertainty.** Radio luminosity is not a direct coupling-efficiency measurement; the key unknown is the distribution of deposited energy relative to jet power across host gas conditions.
    40	
    41	**Survey/data plan.** VLA/LOFAR/MeerKAT for jet morphology and radio spectral ages; Chandra for cavities/shocks/hot gas; MUSE/MaNGA for ionized-gas shock diagnostics; ALMA CO for molecular disturbances; environment from group catalogues.
    42	
    43	**Analysis/test and decision criterion.** Estimate jet power and gas work/thermal response in the same apertures, then regress coupling efficiency on gas density, environment, and jet age. A robust environmental dependence requires efficiency differences larger than radio-power calibration uncertainties.
    44	
    45	**Limitations and wording guardrails.** Radio-to-jet-power conversions are uncertain; coupling estimates must be reported with systematic floors.
    46	
    47	## P3 — Locating the transition from stellar-feedback to AGN-feedback regulation
    48	
    49	**Hypothesis / objective.** There is a stellar/halo-mass regime where stellar-feedback momentum and energy budgets cease to explain gas loss or quiescence, and AGN-linked observables become necessary to reproduce the measured quenched fraction and baryon deficit.
    50	
    51	**Prior evidence and constraints.**
    52	- Low-mass baryon deficiency attributed to stellar feedback provides the low-mass endpoint of the transition problem. [stellar-feedback baryon deficiency](https://arxiv.org/abs/2512.05584).
    53	- High-redshift environmental-quenching simulations emphasize that quenching mechanisms vary with mass and redshift, not only with local observables. [high-redshift environmental quenching simulations](https://arxiv.org/abs/2605.03008).
    54	- Simulated observable-property constraints show why feedback-regime boundaries must be tested against measured baryonic properties. [feedback constraints in simulated galaxies](https://arxiv.org/abs/0901.1880).
    55	
    56	**Remaining uncertainty.** The observational crossover mass between stellar-feedback-dominated regulation and AGN-linked regulation is not cleanly measured with the same denominator and gas observables.
    57	
    58	**Survey/data plan.** DESI/GAMA/COSMOS parent samples with stellar mass and halo proxy; ALFALFA/FASHI HI and ALMA CO gas fractions; optical/IR SFRs; X-ray/radio AGN indicators; JWST for high-redshift extension.
    59	
    60	**Analysis/test and decision criterion.** Fit a broken-slope or transition model for gas fraction, baryon deficit, and quenched fraction as functions of stellar/halo mass while including AGN incidence and stellar-feedback proxies. The transition is credible only if the AGN-linked term improves predictive power above the stellar-feedback model at high mass.
    61	
    62	**Limitations and wording guardrails.** Halo-mass uncertainties and selection functions can smear the transition; results should be framed as a probability surface, not a single universal mass.
    63	
    64	## Methodological note
    65	
    66	- Evidence-traceability work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.
    67	
    68	## Scope note
    69	
    70	These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.
    71	
    72	<!-- AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z · professional Gemini-assisted RT revision · docs-static no-apply -->
==== /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md
     1	# Galaxy Evolution — Research proposals on outflows and feedback regimes
     2	
     3	> This page presents three proposal-style research programmes on outflow fate, jet coupling, and the transition from stellar-feedback to AGN-linked regulation. The proposals are framed around measurable observables, matched denominators, and explicit decision criteria.
     4	
     5	**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for each proposal:
     6	
     7	- P1: [SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot (PDF)](m2_p1_outflow_escape_recycling_aas.pdf)
     8	- P2: [Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot (PDF)](m2_p2_radio_jet_environment_aas.pdf)
     9	- P3: [SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot (PDF)](m2_p3_feedback_transition_mass_aas.pdf)
    10	
    11	3 proposal-style research programmes.
    12	
    13	## P1 — Escape versus recycling: the fate of AGN-driven multiphase outflows
    14	
    15	**Hypothesis / objective.** A substantial fraction of AGN-driven outflowing gas remains gravitationally bound and recycles through the circumgalactic medium, limiting the permanence of feedback-driven gas removal.
    16	
    17	**Prior evidence and constraints.**
    18	- Quasar observations show AGN feedback acting on molecular gas reservoirs at high redshift, but such detections do not determine whether gas escapes the halo. [quasar molecular-gas reservoirs](https://arxiv.org/abs/1706.08987).
    19	- Stellar-feedback work on baryon deficiency in low-mass galaxies provides a boundary condition for non-AGN removal channels that must not be confused with AGN-driven escape. [stellar feedback and baryon deficiency](https://arxiv.org/abs/2512.05584).
    20	- Simulated galaxy feedback constraints highlight that gas removal, recycling, and observable baryon fractions depend on halo scale. [simulated observable feedback constraints](https://arxiv.org/abs/0901.1880).
    21	
    22	**Remaining uncertainty.** The escaped fraction of multiphase outflows is unmeasured across a representative mass/redshift sample; an outflow detection is not equivalent to permanent quenching.
    23	
    24	**Survey/data plan.** AGN hosts and inactive controls spanning stellar mass and redshift; MUSE/MaNGA ionized-gas kinematics, ALMA CO and [C II] for cold gas, JWST/NIRSpec for z>2 outflow tracers, and CGM absorption where available to track recycling.
    25	
    26	**Analysis/test and decision criterion.** Compare outflow velocity distributions with halo escape velocities inferred from dynamical/halo-mass estimates, then model escaped versus bound/recycling fractions as a function of stellar mass, halo mass, and redshift. A high escaped fraction at fixed denominator supports permanent-removal feedback; a low escaped fraction supports recycling-limited regulation.
    27	
    28	**Limitations and wording guardrails.** Projection, phase conversion, and uncertain halo potentials can dominate the escaped-fraction error budget.
    29	
    30	## P2 — Environmental dependence of radio-jet coupling efficiency in galaxy gas
    31	
    32	**Hypothesis / objective.** The fraction of radio-jet mechanical power deposited into the multiphase interstellar or circumgalactic medium varies systematically with ambient gas density and host environment.
    33	
    34	**Prior evidence and constraints.**
    35	- Young radio galaxies show AGN-driven outflows and provide an empirical route to estimating feedback efficiency. [young radio galaxies and feedback efficiency](https://arxiv.org/abs/2009.11175).
    36	- Local M51-scale NOEMA data show how jet/AGN activity can affect molecular ISM structure at high spatial resolution, motivating a broader population test. [SWAN IV molecular ISM feedback](https://arxiv.org/abs/2604.15438).
    37	- Galaxy-group feedback studies identify the group regime as a strong testbed for coupling between radio activity and hot gas. [group-scale AGN feedback](https://arxiv.org/abs/2403.17145).
    38	
    39	**Remaining uncertainty.** Radio luminosity is not a direct coupling-efficiency measurement; the key unknown is the distribution of deposited energy relative to jet power across host gas conditions.
    40	
    41	**Survey/data plan.** VLA/LOFAR/MeerKAT for jet morphology and radio spectral ages; Chandra for cavities/shocks/hot gas; MUSE/MaNGA for ionized-gas shock diagnostics; ALMA CO for molecular disturbances; environment from group catalogues.
    42	
    43	**Analysis/test and decision criterion.** Estimate jet power and gas work/thermal response in the same apertures, then regress coupling efficiency on gas density, environment, and jet age. A robust environmental dependence requires efficiency differences larger than radio-power calibration uncertainties.
    44	
    45	**Limitations and wording guardrails.** Radio-to-jet-power conversions are uncertain; coupling estimates must be reported with systematic floors.
    46	
    47	## P3 — Locating the transition from stellar-feedback to AGN-feedback regulation
    48	
    49	**Hypothesis / objective.** There is a stellar/halo-mass regime where stellar-feedback momentum and energy budgets cease to explain gas loss or quiescence, and AGN-linked observables become necessary to reproduce the measured quenched fraction and baryon deficit.
    50	
    51	**Prior evidence and constraints.**
    52	- Low-mass baryon deficiency attributed to stellar feedback provides the low-mass endpoint of the transition problem. [stellar-feedback baryon deficiency](https://arxiv.org/abs/2512.05584).
    53	- High-redshift environmental-quenching simulations emphasize that quenching mechanisms vary with mass and redshift, not only with local observables. [high-redshift environmental quenching simulations](https://arxiv.org/abs/2605.03008).
    54	- Simulated observable-property constraints show why feedback-regime boundaries must be tested against measured baryonic properties. [feedback constraints in simulated galaxies](https://arxiv.org/abs/0901.1880).
    55	
    56	**Remaining uncertainty.** The observational crossover mass between stellar-feedback-dominated regulation and AGN-linked regulation is not cleanly measured with the same denominator and gas observables.
    57	
    58	**Survey/data plan.** DESI/GAMA/COSMOS parent samples with stellar mass and halo proxy; ALFALFA/FASHI HI and ALMA CO gas fractions; optical/IR SFRs; X-ray/radio AGN indicators; JWST for high-redshift extension.
    59	
    60	**Analysis/test and decision criterion.** Fit a broken-slope or transition model for gas fraction, baryon deficit, and quenched fraction as functions of stellar/halo mass while including AGN incidence and stellar-feedback proxies. The transition is credible only if the AGN-linked term improves predictive power above the stellar-feedback model at high mass.
    61	
    62	**Limitations and wording guardrails.** Halo-mass uncertainties and selection functions can smear the transition; results should be framed as a probability surface, not a single universal mass.
    63	
    64	## Methodological note
    65	
    66	- Evidence-traceability work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.
    67	
    68	## Scope note
    69	
    70	These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.
    71	
    72	<!-- AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z · professional Gemini-assisted RT revision · docs-static no-apply -->

exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/*.md /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/briefs/*.md; do echo "==== $(basename "$f")"; rg -n "claim|caveat|conclusion|limitations|citation|proxy|denominator|pilot|not|should|must|selection|public|local" "$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== goru-sfa.md
13:Task: checks paths, counts, citation/source coverage, markers, and no-go rows.
15:Method rule: Begin from the papers themselves, adjudicate source positions first, then allow claims and prose only after source roles are accepted or accepted-limited.
17:First step: Build a source-position ledger for the target papers and decide which positions can support a public wiki sentence.
==== hwao-sfa.md
15:Method rule: Begin from the papers themselves, adjudicate source positions first, then allow claims and prose only after source roles are accepted or accepted-limited.
17:First step: Build a source-position ledger for the target papers and decide which positions can support a public wiki sentence.
==== kun-sfa.md
13:Task: checks whether another agent can reproduce the method from files and briefs.
15:Method rule: Begin from the papers themselves, adjudicate source positions first, then allow claims and prose only after source roles are accepted or accepted-limited.
17:First step: Build a source-position ledger for the target papers and decide which positions can support a public wiki sentence.
==== lana-sfa.md
15:  and say whether it can support a public wiki sentence.
==== tori-sfa.md
13:Task: records instructions, updates public surfaces, verifies files/routes, and keeps safety ledgers.
15:Method rule: Begin from the papers themselves, adjudicate source positions first, then allow claims and prose only after source roles are accepted or accepted-limited.
17:First step: Build a source-position ledger for the target papers and decide which positions can support a public wiki sentence.
==== goru-dmw.md
13:Task: checks paths, counts, citation/source coverage, markers, and no-go rows.
17:First step: Map the strongest settled/debated/challenged positions, then draft a sentence plan before binding citations or claim chips.
==== hwao-dmw.md
17:First step: Map the strongest settled/debated/challenged positions, then draft a sentence plan before binding citations or claim chips.
==== kun-dmw.md
13:Task: checks whether another agent can reproduce the method from files and briefs.
17:First step: Map the strongest settled/debated/challenged positions, then draft a sentence plan before binding citations or claim chips.
==== lana-dmw.md
13:Task: checks semantic accuracy, reader-facing clarity, and overclaim risk.
17:First step: Map the strongest settled/debated/challenged positions, then draft a sentence plan before binding citations or claim chips.
==== tori-dmw.md
13:Task: records instructions, updates public surfaces, verifies files/routes, and keeps safety ledgers.
17:First step: Map the strongest settled/debated/challenged positions, then draft a sentence plan before binding citations or claim chips.

codex
I’ve confirmed a concrete coherence issue: every non-RP-1 paper still closes by talking about RP-1. That is not a science error, but it is exactly the sort of stale template artifact that hurts reader flow and should be fixed before the PDF-writing pilot. I’m checking the paper-specific numeric claims against the source-analysis receipts now to see whether any result wording or caption framing needs tighter guarding.
exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/*/data/source_analysis_results.json; do echo "==== $(basename $(dirname "$f"))"; jq -r '"'{short_title, proposal_title, pilot_question, interpretation_guard, result_bullets} | @json' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== data
{"short_title":null,"proposal_title":null,"pilot_question":null,"interpretation_guard":null,"result_bullets":null}
==== data
{"short_title":"SDSS density proxy for environmental quenching","proposal_title":"Separating internal and environmental quenching across stellar mass, halo mass, and redshift","pilot_question":"Does a nearest-neighbour density proxy add quenched-fraction information beyond stellar mass in the SDSS emission-line sample?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy.","The high-density quartile has quenched fraction 0.230 (3,456/15,000); the low-density quartile has 0.181 (2,710/15,000).","The bootstrap high-minus-low quenched-fraction interval is [0.041, 0.059].","A linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004."]}
==== data
{"short_title":"Optical-AGN denominator for maintenance-heating follow-up","proposal_title":"Empirical duty-cycle constraints on AGN maintenance heating in massive halos","pilot_question":"Among massive, low-sSFR SDSS emission-line galaxies, what optical AGN fraction is available as a denominator for X-ray/radio maintenance-heating follow-up?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["The massive subset (logM >= 10.8) contains 9,298 emission-line galaxies; 5,695 are low-sSFR by the pilot threshold.","The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.","This provides an optical duty-cycle denominator for X-ray/radio maintenance-heating follow-up, not a heating-to-cooling measurement."]}
==== data
{"short_title":"SDSS high-excitation AGN denominator for outflow escape tests","proposal_title":"Escape versus recycling: the fate of AGN-driven multiphase outflows","pilot_question":"How large is the SDSS high-excitation optical-AGN denominator that would need resolved kinematics to test escape versus recycling?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074).","Their median log sSFR is -11.53, compared with -10.14 for the full denominator.","SDSS does not measure escape velocity or multiphase outflow velocities here; the pilot supplies a denominator for resolved follow-up rather than an escape/recycling result."]}
==== data
{"short_title":"Environment proxy for optical AGN in massive SDSS hosts","proposal_title":"Environmental dependence of radio-jet coupling efficiency in galaxy gas","pilot_question":"Does a local-density proxy modulate the optical AGN fraction in massive SDSS hosts, motivating environment-stratified radio/X-ray jet-coupling follow-up?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.","The bootstrap high-minus-low interval is [0.112, 0.170].","This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency."]}
==== data
{"short_title":"SDSS mass transition in quenching and optical AGN incidence","proposal_title":"Locating the transition from stellar-feedback to AGN-feedback regulation","pilot_question":"At what stellar-mass scale do quenched fraction and optical AGN incidence rise in the same SDSS denominator?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["The first stellar-mass bin with quenched fraction above 0.5 is 11.0-12.5.","The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520.","The result is an optical transition diagnostic; gas fractions and baryon deficits are needed before assigning the transition to stellar or AGN feedback."]}
==== data
{"short_title":"Common-denominator optical tracer census in SDSS","proposal_title":"A multiphase, common-denominator census of AGN-driven outflows","pilot_question":"How strongly do simple optical tracer definitions change the inferred AGN/feedback-candidate prevalence in one common SDSS denominator?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.","The widest-to-narrowest prevalence ratio is 3.1, before adding molecular, neutral, or X-ray/radio phases.","This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates."]}
==== data
{"short_title":"Optical denominator for gas-fraction versus efficiency tests","proposal_title":"Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies","pilot_question":"How many massive quenched or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction/depletion-time follow-up?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample.","Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.","The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies.","SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline."]}
==== data
{"short_title":"SDSS target vector for feedback-model validation","proposal_title":"Forward-modelled validation of cosmological feedback prescriptions","pilot_question":"What compact SDSS target vector of quenched fraction, optical AGN incidence, and colour versus mass/redshift can be used for forward-model validation?","interpretation_guard":"SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.","result_bullets":["The pilot writes 15 mass-redshift cells with n >= 50 as a compact validation vector.","Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.","The output is an observed target vector for simulation forward modelling, not a direct simulation comparison."]}

exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/*/aastex/*_integrated.tex; do echo "==== $(basename "$f")"; rg -n -F "guarded SDSS optical proxy/denominator draft" "$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/*/aastex/*_integrated.tex; do echo "==== $(basename "$f")"; rg -n -F "For RP-1" "$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== m1_rp1_sdss_agn_sfr_integrated.tex
==== m1_rp2_environment_quenching_integrated.tex
13:We integrate the active proposal 'Separating internal and environmental quenching across stellar mass, halo mass, and redshift' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m1_rp3_maintenance_heating_integrated.tex
13:We integrate the active proposal 'Empirical duty-cycle constraints on AGN maintenance heating in massive halos' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m2_p1_outflow_escape_recycling_integrated.tex
13:We integrate the active proposal 'Escape versus recycling: the fate of AGN-driven multiphase outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m2_p2_radio_jet_environment_integrated.tex
13:We integrate the active proposal 'Environmental dependence of radio-jet coupling efficiency in galaxy gas' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m2_p3_feedback_transition_mass_integrated.tex
13:We integrate the active proposal 'Locating the transition from stellar-feedback to AGN-feedback regulation' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m3_p1_multiphase_census_integrated.tex
13:We integrate the active proposal 'A multiphase, common-denominator census of AGN-driven outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m3_p2_gas_depletion_efficiency_integrated.tex
13:We integrate the active proposal 'Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m3_p3_simulation_validation_integrated.tex
13:We integrate the active proposal 'Forward-modelled validation of cosmological feedback prescriptions' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.

 succeeded in 0ms:
==== m1_rp1_sdss_agn_sfr_integrated.tex
85:The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
==== m1_rp2_environment_quenching_integrated.tex
80:The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
==== m1_rp3_maintenance_heating_integrated.tex
79:The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
==== m2_p1_outflow_escape_recycling_integrated.tex
79:The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
==== m2_p2_radio_jet_environment_integrated.tex
79:The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
==== m2_p3_feedback_transition_mass_integrated.tex
79:The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
==== m3_p1_multiphase_census_integrated.tex
79:The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
==== m3_p2_gas_depletion_efficiency_integrated.tex
80:The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.
==== m3_p3_simulation_validation_integrated.tex
79:The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers.

codex
The manuscripts all compile cleanly, so the remaining value is in soft failures: stale template sentences, weak abstracts, and any LaTeX warnings that could still degrade the PDF experience. I’m checking the compile logs for unresolved refs, overfull boxes, or citation noise before I finalize the review.
exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/*/figures/fig-topic.pdf /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf; do echo "==== $f"; file "$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/figures/fig-topic.pdf: PDF document, version 1.4, 1 pages
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf: PDF document, version 1.4, 1 pages
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf: PDF document, version 1.4, 1 pages
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/figures/fig-topic.pdf: PDF document, version 1.4, 1 pages
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/figures/fig-topic.pdf: PDF document, version 1.4, 1 pages
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/figures/fig-topic.pdf: PDF document, version 1.4, 1 pages
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/figures/fig-topic.pdf: PDF document, version 1.4, 1 pages
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/figures/fig-topic.pdf: PDF document, version 1.4, 1 pages
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf: PDF document, version 1.4, 1 pages
==== /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf: PDF document, version 1.4, 1 pages

exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/*/aastex/*.overnight.compile.log; do echo "==== $(basename "$f")"; rg -n "Warning|Undefined|Overfull|Underfull|LaTeX Error|Citation|Reference" "$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== m1_rp1_sdss_agn_sfr_integrated.overnight.compile.log
3:warning: m1_rp1_sdss_agn_sfr_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
4:warning: m1_rp1_sdss_agn_sfr_integrated.tex:83: Underfull \hbox (badness 2626) in paragraph at lines 82--83
5:warning: m1_rp1_sdss_agn_sfr_integrated.tex:83: Underfull \hbox (badness 1019) in paragraph at lines 82--83
6:warning: m1_rp1_sdss_agn_sfr_integrated.tex:86: Underfull \hbox (badness 1789) in paragraph at lines 85--86
9:warning: m1_rp1_sdss_agn_sfr_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
10:warning: m1_rp1_sdss_agn_sfr_integrated.tex:83: Underfull \hbox (badness 2626) in paragraph at lines 82--83
11:warning: m1_rp1_sdss_agn_sfr_integrated.tex:83: Underfull \hbox (badness 1019) in paragraph at lines 82--83
12:warning: m1_rp1_sdss_agn_sfr_integrated.tex:86: Underfull \hbox (badness 1789) in paragraph at lines 85--86
==== m1_rp2_environment_quenching_integrated.overnight.compile.log
3:warning: m1_rp2_environment_quenching_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
4:warning: m1_rp2_environment_quenching_integrated.tex:57: Underfull \hbox (badness 1337) in paragraph at lines 56--57
5:warning: m1_rp2_environment_quenching_integrated.tex:66: Underfull \hbox (badness 4291) in paragraph at lines 66--66
6:warning: m1_rp2_environment_quenching_integrated.tex:74: Underfull \hbox (badness 2189) in paragraph at lines 73--74
7:warning: m1_rp2_environment_quenching_integrated.tex:78: Underfull \hbox (badness 2626) in paragraph at lines 77--78
8:warning: m1_rp2_environment_quenching_integrated.tex:78: Underfull \hbox (badness 1019) in paragraph at lines 77--78
9:warning: m1_rp2_environment_quenching_integrated.tex:81: Underfull \hbox (badness 1789) in paragraph at lines 80--81
12:warning: m1_rp2_environment_quenching_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
13:warning: m1_rp2_environment_quenching_integrated.tex:57: Underfull \hbox (badness 1337) in paragraph at lines 56--57
14:warning: m1_rp2_environment_quenching_integrated.tex:66: Underfull \hbox (badness 4291) in paragraph at lines 66--66
15:warning: m1_rp2_environment_quenching_integrated.tex:74: Underfull \hbox (badness 2189) in paragraph at lines 73--74
16:warning: m1_rp2_environment_quenching_integrated.tex:78: Underfull \hbox (badness 2626) in paragraph at lines 77--78
17:warning: m1_rp2_environment_quenching_integrated.tex:78: Underfull \hbox (badness 1019) in paragraph at lines 77--78
18:warning: m1_rp2_environment_quenching_integrated.tex:81: Underfull \hbox (badness 1789) in paragraph at lines 80--81
==== m1_rp3_maintenance_heating_integrated.overnight.compile.log
3:warning: m1_rp3_maintenance_heating_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
4:warning: m1_rp3_maintenance_heating_integrated.tex:65: Underfull \hbox (badness 4291) in paragraph at lines 65--65
5:warning: m1_rp3_maintenance_heating_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
6:warning: m1_rp3_maintenance_heating_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
7:warning: m1_rp3_maintenance_heating_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
10:warning: m1_rp3_maintenance_heating_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
11:warning: m1_rp3_maintenance_heating_integrated.tex:65: Underfull \hbox (badness 4291) in paragraph at lines 65--65
12:warning: m1_rp3_maintenance_heating_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
13:warning: m1_rp3_maintenance_heating_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
14:warning: m1_rp3_maintenance_heating_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
17:warning: m1_rp3_maintenance_heating_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
18:warning: m1_rp3_maintenance_heating_integrated.tex:65: Underfull \hbox (badness 4291) in paragraph at lines 65--65
19:warning: m1_rp3_maintenance_heating_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
20:warning: m1_rp3_maintenance_heating_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
21:warning: m1_rp3_maintenance_heating_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
==== m2_p1_outflow_escape_recycling_integrated.overnight.compile.log
3:warning: m2_p1_outflow_escape_recycling_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
4:warning: m2_p1_outflow_escape_recycling_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
5:warning: m2_p1_outflow_escape_recycling_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
6:warning: m2_p1_outflow_escape_recycling_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
9:warning: m2_p1_outflow_escape_recycling_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
10:warning: m2_p1_outflow_escape_recycling_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
11:warning: m2_p1_outflow_escape_recycling_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
12:warning: m2_p1_outflow_escape_recycling_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
15:warning: m2_p1_outflow_escape_recycling_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
16:warning: m2_p1_outflow_escape_recycling_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
17:warning: m2_p1_outflow_escape_recycling_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
18:warning: m2_p1_outflow_escape_recycling_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
==== m2_p2_radio_jet_environment_integrated.overnight.compile.log
3:warning: m2_p2_radio_jet_environment_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
4:warning: m2_p2_radio_jet_environment_integrated.tex:73: Underfull \hbox (badness 10000) in paragraph at lines 72--73
5:warning: m2_p2_radio_jet_environment_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
6:warning: m2_p2_radio_jet_environment_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
7:warning: m2_p2_radio_jet_environment_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
10:warning: m2_p2_radio_jet_environment_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
11:warning: m2_p2_radio_jet_environment_integrated.tex:73: Underfull \hbox (badness 10000) in paragraph at lines 72--73
12:warning: m2_p2_radio_jet_environment_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
13:warning: m2_p2_radio_jet_environment_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
14:warning: m2_p2_radio_jet_environment_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
17:warning: m2_p2_radio_jet_environment_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
18:warning: m2_p2_radio_jet_environment_integrated.tex:73: Underfull \hbox (badness 10000) in paragraph at lines 72--73
19:warning: m2_p2_radio_jet_environment_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
20:warning: m2_p2_radio_jet_environment_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
21:warning: m2_p2_radio_jet_environment_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
==== m2_p3_feedback_transition_mass_integrated.overnight.compile.log
3:warning: m2_p3_feedback_transition_mass_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
4:warning: m2_p3_feedback_transition_mass_integrated.tex:54: Underfull \hbox (badness 1009) in paragraph at lines 53--54
5:warning: m2_p3_feedback_transition_mass_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
6:warning: m2_p3_feedback_transition_mass_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
7:warning: m2_p3_feedback_transition_mass_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
10:warning: m2_p3_feedback_transition_mass_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
11:warning: m2_p3_feedback_transition_mass_integrated.tex:54: Underfull \hbox (badness 1009) in paragraph at lines 53--54
12:warning: m2_p3_feedback_transition_mass_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
13:warning: m2_p3_feedback_transition_mass_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
14:warning: m2_p3_feedback_transition_mass_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
15:warning: m2_p3_feedback_transition_mass_integrated.tex:85: Overfull \vbox (2.51009pt too high) has occurred while \output is active
16:warning: m2_p3_feedback_transition_mass_integrated.tex:86: Overfull \vbox (2.51009pt too high) has occurred while \output is active
19:warning: m2_p3_feedback_transition_mass_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
20:warning: m2_p3_feedback_transition_mass_integrated.tex:54: Underfull \hbox (badness 1009) in paragraph at lines 53--54
21:warning: m2_p3_feedback_transition_mass_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
22:warning: m2_p3_feedback_transition_mass_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
23:warning: m2_p3_feedback_transition_mass_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
24:warning: m2_p3_feedback_transition_mass_integrated.tex:85: Overfull \vbox (2.51009pt too high) has occurred while \output is active
25:warning: m2_p3_feedback_transition_mass_integrated.tex:86: Overfull \vbox (2.51009pt too high) has occurred while \output is active
==== m3_p1_multiphase_census_integrated.overnight.compile.log
3:warning: m3_p1_multiphase_census_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
4:warning: m3_p1_multiphase_census_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
5:warning: m3_p1_multiphase_census_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
6:warning: m3_p1_multiphase_census_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
9:warning: m3_p1_multiphase_census_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
10:warning: m3_p1_multiphase_census_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
11:warning: m3_p1_multiphase_census_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
12:warning: m3_p1_multiphase_census_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
15:warning: m3_p1_multiphase_census_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
16:warning: m3_p1_multiphase_census_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
17:warning: m3_p1_multiphase_census_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
18:warning: m3_p1_multiphase_census_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
==== m3_p2_gas_depletion_efficiency_integrated.overnight.compile.log
3:warning: m3_p2_gas_depletion_efficiency_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
4:warning: m3_p2_gas_depletion_efficiency_integrated.tex:57: Underfull \hbox (badness 2057) in paragraph at lines 56--57
5:warning: m3_p2_gas_depletion_efficiency_integrated.tex:78: Underfull \hbox (badness 2626) in paragraph at lines 77--78
6:warning: m3_p2_gas_depletion_efficiency_integrated.tex:78: Underfull \hbox (badness 1019) in paragraph at lines 77--78
7:warning: m3_p2_gas_depletion_efficiency_integrated.tex:81: Underfull \hbox (badness 1789) in paragraph at lines 80--81
10:warning: m3_p2_gas_depletion_efficiency_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
11:warning: m3_p2_gas_depletion_efficiency_integrated.tex:57: Underfull \hbox (badness 2057) in paragraph at lines 56--57
12:warning: m3_p2_gas_depletion_efficiency_integrated.tex:78: Underfull \hbox (badness 2626) in paragraph at lines 77--78
13:warning: m3_p2_gas_depletion_efficiency_integrated.tex:78: Underfull \hbox (badness 1019) in paragraph at lines 77--78
14:warning: m3_p2_gas_depletion_efficiency_integrated.tex:81: Underfull \hbox (badness 1789) in paragraph at lines 80--81
17:warning: m3_p2_gas_depletion_efficiency_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
18:warning: m3_p2_gas_depletion_efficiency_integrated.tex:57: Underfull \hbox (badness 2057) in paragraph at lines 56--57
19:warning: m3_p2_gas_depletion_efficiency_integrated.tex:78: Underfull \hbox (badness 2626) in paragraph at lines 77--78
20:warning: m3_p2_gas_depletion_efficiency_integrated.tex:78: Underfull \hbox (badness 1019) in paragraph at lines 77--78
21:warning: m3_p2_gas_depletion_efficiency_integrated.tex:81: Underfull \hbox (badness 1789) in paragraph at lines 80--81
==== m3_p3_simulation_validation_integrated.overnight.compile.log
3:warning: m3_p3_simulation_validation_integrated.tex:20: Underfull \hbox (badness 4543) in paragraph at lines 19--20
4:warning: m3_p3_simulation_validation_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
5:warning: m3_p3_simulation_validation_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
6:warning: m3_p3_simulation_validation_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
7:warning: m3_p3_simulation_validation_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
10:warning: m3_p3_simulation_validation_integrated.tex:20: Underfull \hbox (badness 4543) in paragraph at lines 19--20
11:warning: m3_p3_simulation_validation_integrated.tex:22: Underfull \hbox (badness 2050) in paragraph at lines 21--22
12:warning: m3_p3_simulation_validation_integrated.tex:77: Underfull \hbox (badness 2626) in paragraph at lines 76--77
13:warning: m3_p3_simulation_validation_integrated.tex:77: Underfull \hbox (badness 1019) in paragraph at lines 76--77
14:warning: m3_p3_simulation_validation_integrated.tex:80: Underfull \hbox (badness 1789) in paragraph at lines 79--80
15:warning: m3_p3_simulation_validation_integrated.tex:85: Overfull \vbox (2.2901pt too high) has occurred while \output is active
16:warning: m3_p3_simulation_validation_integrated.tex:86: Overfull \vbox (2.2901pt too high) has occurred while \output is active

exec
/bin/zsh -c 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/*/aastex/*_integrated.tex; do echo "==== $(basename "$f")"; rg -n -F "No public page, live root, database, deployment, git, or external submission action is part of this run." "$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
==== m1_rp1_sdss_agn_sfr_integrated.tex
13:We integrate the strongest Galaxy Evolution pilot into a selection-aware short-paper draft: a matched-control comparison of catalog specific star formation in broad BPT optical AGN hosts and star-forming controls in SDSS DR17. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a flagship short-paper draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m1_rp2_environment_quenching_integrated.tex
13:We integrate the active proposal 'Separating internal and environmental quenching across stellar mass, halo mass, and redshift' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m1_rp3_maintenance_heating_integrated.tex
13:We integrate the active proposal 'Empirical duty-cycle constraints on AGN maintenance heating in massive halos' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m2_p1_outflow_escape_recycling_integrated.tex
13:We integrate the active proposal 'Escape versus recycling: the fate of AGN-driven multiphase outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m2_p2_radio_jet_environment_integrated.tex
13:We integrate the active proposal 'Environmental dependence of radio-jet coupling efficiency in galaxy gas' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m2_p3_feedback_transition_mass_integrated.tex
13:We integrate the active proposal 'Locating the transition from stellar-feedback to AGN-feedback regulation' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m3_p1_multiphase_census_integrated.tex
13:We integrate the active proposal 'A multiphase, common-denominator census of AGN-driven outflows' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m3_p2_gas_depletion_efficiency_integrated.tex
13:We integrate the active proposal 'Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.
==== m3_p3_simulation_validation_integrated.tex
13:We integrate the active proposal 'Forward-modelled validation of cosmological feedback prescriptions' as a guarded SDSS DR17 optical denominator/proxy draft rather than as a completed physical-feedback paper. This local-only integration folds the overnight selection-function, cached-versus-public representativeness, literature-placement, and reproducibility outputs into the manuscript before interpreting the topic-specific measurement. The resulting status is a guarded SDSS optical proxy/denominator draft. No public page, live root, database, deployment, git, or external submission action is part of this run.

codex
OVERNIGHT_CODEX_KUN_REPRO_CYCLE_01 status: ISSUES_FOUND

Files/paths actually inspected
- Candidate TeX files:
  - [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
  - [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
  - [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
  - [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
  - [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
  - [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
  - [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
  - [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
  - [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)
- Supporting candidate artifacts:
  - The corresponding `data/source_analysis_results.json` files under each paper directory.
  - The corresponding `aastex/*.overnight.compile.log` files under each paper directory.
- Public-linked research-topic manuscripts:
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
- Supporting public/live briefs and ledgers under `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/` and `.../debate-map-to-wiki-rebuild/`.

Ranked findings

1. Major: Workflow labels are leaking into figure captions in papers 2-9.
- The captions contain internal process names such as `packet-gated-paper-to-wiki-reconciliation`, `source-first-paper-adjudication`, and `debate-map-to-wiki-rebuild`, which are not publication-facing language.
- Examples:
  - [m1_rp2_environment_quenching_integrated.tex#L66](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex#L66)
  - [m1_rp3_maintenance_heating_integrated.tex#L65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex#L65)
  - [m2_p1_outflow_escape_recycling_integrated.tex#L65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex#L65)
  - [m2_p2_radio_jet_environment_integrated.tex#L65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex#L65)
  - [m2_p3_feedback_transition_mass_integrated.tex#L65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex#L65)
  - [m3_p1_multiphase_census_integrated.tex#L65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex#L65)
  - [m3_p2_gas_depletion_efficiency_integrated.tex#L66](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex#L66)
  - [m3_p3_simulation_validation_integrated.tex#L65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex#L65)
- Safe rewrite guidance:
  - Replace each caption with a self-contained scientific caption that names the measured quantity, sample size, and limitation.
  - Keep the measured values; remove the workflow tag.
  - Example pattern: `SDSS-only environment proxy in massive hosts. High-density quartile: 0.509; low-density quartile: 0.367; bootstrap difference [0.112, 0.170]. This is a denominator for follow-up, not a coupling-efficiency measurement.`

2. Major: Conclusions in papers 2-9 are copy-pasted and incorrectly refer back to RP-1.
- Every non-RP1 conclusion ends with a sentence about the RP-1 association draft and “the other active topics,” which is confusing in a standalone manuscript.
- Examples:
  - [m1_rp2_environment_quenching_integrated.tex#L80](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex#L80)
  - [m2_p1_outflow_escape_recycling_integrated.tex#L79](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex#L79)
  - [m3_p3_simulation_validation_integrated.tex#L78](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex#L78)
- Safe rewrite guidance:
  - Replace the entire final paragraph in each non-RP1 paper with a paper-specific conclusion.
  - Keep the actual result, then the limitation, then the follow-up requirement.
  - Example pattern for a non-RP1 paper: `This manuscript isolates [measured SDSS quantity] in the SDSS emission-line sample, but the result remains a proxy because [missing observables].`
  - Do not mention RP-1 or “the other active topics” inside the paper-specific conclusion.

3. Minor: Abstracts are too generic and meta-heavy for publication.
- The abstract text mostly says the manuscript was integrated, not what was measured.
- That makes the PDFs read like workflow receipts rather than short papers.
- Safe rewrite guidance:
  - Put the measured SDSS result in sentence 1.
  - Put the boundary condition in sentence 2.
  - Keep provenance to one short clause or move it to a reproducibility note.
- Example template:
  - `Using the cached 60,000-row SDSS DR17 emission-line subset, [measured quantity] is [numeric result]. This is an SDSS-only proxy result and does not measure [causal physical claim].`
- Strong examples of result-specific text already available in the source-analysis receipts and should be surfaced in the abstract:
  - Paper 2: high-density quartile quenched fraction 0.230 vs low-density 0.181, bootstrap interval [0.041, 0.059].
  - Paper 4: 4,440 high-excitation AGN candidates of 60,000 (0.074), median log sSFR -11.53 vs -10.14.
  - Paper 6: first stellar-mass bin with quenched fraction above 0.5 is 11.0-12.5; optical AGN fraction peaks there at 0.520.
  - Paper 9: 15 mass-redshift cells with n >= 50; quenched fractions span 0.005-0.729 and optical AGN fractions 0.003-0.520.

4. Minor: RP-1 has one precision bug in the representativeness sentence, and several manuscripts still use internal-scope wording in the body.
- In RP-1, “largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR” is mathematically sloppy because absolute differences are not negative.
- In the non-RP1 papers, `All nine integrated drafts use the same public-data backbone...` and `SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.` make the manuscripts less self-contained.
- Safe rewrite guidance:
  - RP-1 [m1_rp1_sdss_agn_sfr_integrated.tex#L45](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex#L45): change to `The largest signed differences were 2.03 percentage points in redshift, 1.63 percentage points in stellar mass, and 0.58 percentage points in sSFR.`
  - Replace “All nine integrated drafts...” with a single self-contained sentence about this manuscript’s cached SDSS DR17 subset.
  - Replace “research-topic page” with the actual missing observables, listed inline.

Exact feed for PDF-writing pilot
- Paper 1 abstract should surface the real result and preserve the selection boundary.
  - Suggested rewrite: `Using the 60,000-row SDSS DR17 emission-line subset, broad BPT AGN hosts matched in stellar mass and redshift show a median catalog sSFR offset of -1.309 dex relative to star-forming controls (95% bootstrap interval [-1.334,-1.283]). This is an association result within an emission-line-selected SDSS sample, not causal AGN feedback evidence.`
- Paper 1 conclusion should stop after the RP-1 result and remove suite-level spillover.
  - Suggested rewrite: `The strongest result is an association-only short-paper draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass-redshift matched star-forming controls, with sensitivity to selection and subclass definitions.`
- Paper 2 caption should be rewritten around the actual result, not the workflow tag.
  - Suggested rewrite: `SDSS-only environment proxy in massive hosts. High-density quartile quenched fraction is 0.230 (3,456/15,000); low-density quartile is 0.181 (2,710/15,000); bootstrap high-minus-low interval is [0.041, 0.059]. This is a proxy for follow-up, not a halo-based environmental-quenching measurement.`
- Paper 3 caption should be rewritten around the actual result, not the workflow tag.
  - Suggested rewrite: `SDSS-only maintenance-heating denominator in massive, low-sSFR hosts. The massive subset contains 9,298 emission-line galaxies; 5,695 are low-sSFR; the optical BPT AGN fraction is 0.430 in the massive subset and 0.607 in the low-sSFR subset. This is a duty-cycle denominator, not a heating-to-cooling measurement.`
- Paper 4 caption should say the escape/recycling denominator, not the internal label.
  - Suggested rewrite: `SDSS-only outflow-follow-up denominator. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074), and their median log sSFR is -11.53 versus -10.14 for the full denominator. This does not measure escape velocity or multiphase outflow speed.`
- Paper 5 caption should mirror the environment result and its limitation.
  - Suggested rewrite: `SDSS-only optical AGN environment proxy in massive hosts. High-density quartile optical AGN fraction is 0.509; low-density quartile is 0.367; bootstrap high-minus-low interval is [0.112, 0.170]. This is an environment proxy for radio/X-ray follow-up, not a jet-coupling measurement.`
- Paper 6 caption should be the mass-transition diagnostic.
  - Suggested rewrite: `SDSS-only optical transition diagnostic. The first stellar-mass bin with quenched fraction above 0.5 is 11.0-12.5, and optical AGN fraction peaks there at 0.520. This is a transition diagnostic only; it does not assign the transition to stellar or AGN feedback.`
- Paper 7 caption should emphasize denominator sensitivity.
  - Suggested rewrite: `SDSS-only common-denominator optical tracer census. Simple optical tracer definitions produce prevalence from 0.136 to 0.418 within the same 60,000-galaxy denominator, a factor of 3.1. This shows denominator sensitivity, not multiphase outflow rates.`
- Paper 8 caption should stay explicit about the CO follow-up boundary.
  - Suggested rewrite: `SDSS-only CO follow-up denominator. The massive transition/quenched denominator contains 6,729 galaxies; optical BPT AGN fraction is 0.549; median log H-alpha proxy is 40.06, which is 0.66 dex below massive star-forming emission-line galaxies. This is not a molecular-gas depletion measurement.`
- Paper 9 caption should stay explicit about forward-model targets only.
  - Suggested rewrite: `SDSS-only target vector for forward modeling. The pilot writes 15 mass-redshift cells with n >= 50; quenched fractions span 0.005-0.729 and optical AGN fractions span 0.003-0.520. This is an observed target vector, not a direct simulation comparison.`
- Reproducibility sections should be shortened for publication-facing text.
  - Keep one sentence of provenance.
  - Move run IDs, packet names, and workflow tags out of the visible manuscript body or into a local-only appendix if the pilot requires them.

Real-data/source/citation audit notes
- No mock, synthetic, placeholder, or toy data were accepted in the reviewed manuscripts.
- The main quantitative claims match the `source_analysis_results.json` receipts:
  - Paper 2: 60,000-row emission-line denominator; high-density 0.230 vs low-density 0.181; CI [0.041, 0.059].
  - Paper 4: 4,440 high-excitation AGN candidates out of 60,000; median log sSFR -11.53 vs -10.14.
  - Paper 5: high-density 0.509 vs low-density 0.367; CI [0.112, 0.170].
  - Paper 6: first quenched-fraction bin above 0.5 is 11.0-12.5; optical AGN fraction peaks at 0.520.
  - Paper 7: prevalence range 0.136 to 0.418.
  - Paper 8: 6,729 massive transition/quenched galaxies; BPT AGN fraction 0.549; median H-alpha proxy 40.06.
  - Paper 9: 15 mass-redshift cells with n >= 50; quenched fractions 0.005-0.729; optical AGN fractions 0.003-0.520.
- Citation-role separation is broadly correct:
  - SDSS/BPT/catalog citations are used for the method.
  - Radio, X-ray, molecular-gas, wind, and simulation citations are correctly reserved for missing-observable motivation.
- No unresolved references or citation errors showed up in the compile logs.
- One wording bug exists in RP-1’s representativeness sentence: “absolute differences” should not carry negative signs.
- Public/live research-topic markdown is identical across the two roots I inspected, so I did not find a stale public-vs-local divergence inside that page itself.
- The scope mismatch is instead between the public-linked 3-proposal hub and the local 9-paper integrated candidate set, which is expected context but should not be conflated.

Workflow/system notes
- The compile receipts were clean enough to proceed; warnings were cosmetic rather than fatal.
- I saw underfull `\hbox` warnings across several papers.
- I saw small overfull `\vbox` warnings in [m2_p3_feedback_transition_mass_integrated.tex#L85](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex#L85) and [m3_p3_simulation_validation_integrated.tex#L85](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex#L85); if the PDF page bottoms look crowded, a small bibliography reflow is the likely fix.
- The dominant workflow issue is prose hygiene, not data integrity.

Safety ledger
- Edits: 0
- Public/live root changes: 0
- Database/API/wiki writes: 0
- Deploy/restart: 0
- Git commit/push/merge/rebase/history rewrite: 0
- Cron changes: 0
- Billing/cloud/OAuth/account changes: 0
- External submission: 0
- Credential/token/cookie reads: 0
tokens used
119,613
OVERNIGHT_CODEX_KUN_REPRO_CYCLE_01 status: ISSUES_FOUND

Files/paths actually inspected
- Candidate TeX files:
  - [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
  - [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
  - [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
  - [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
  - [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
  - [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
  - [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
  - [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
  - [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)
- Supporting candidate artifacts:
  - The corresponding `data/source_analysis_results.json` files under each paper directory.
  - The corresponding `aastex/*.overnight.compile.log` files under each paper directory.
- Public-linked research-topic manuscripts:
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
  - [research-topics-from-wiki-20260708T090359Z.md](/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md)
- Supporting public/live briefs and ledgers under `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/` and `.../debate-map-to-wiki-rebuild/`.

Ranked findings

1. Major: Workflow labels are leaking into figure captions in papers 2-9.
- The captions contain internal process names such as `packet-gated-paper-to-wiki-reconciliation`, `source-first-paper-adjudication`, and `debate-map-to-wiki-rebuild`, which are not publication-facing language.
- Examples:
  - [m1_rp2_environment_quenching_integrated.tex#L66](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex#L66)
  - [m1_rp3_maintenance_heating_integrated.tex#L65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex#L65)
  - [m2_p1_outflow_escape_recycling_integrated.tex#L65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex#L65)
  - [m2_p2_radio_jet_environment_integrated.tex#L65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex#L65)
  - [m2_p3_feedback_transition_mass_integrated.tex#L65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex#L65)
  - [m3_p1_multiphase_census_integrated.tex#L65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex#L65)
  - [m3_p2_gas_depletion_efficiency_integrated.tex#L66](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex#L66)
  - [m3_p3_simulation_validation_integrated.tex#L65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex#L65)
- Safe rewrite guidance:
  - Replace each caption with a self-contained scientific caption that names the measured quantity, sample size, and limitation.
  - Keep the measured values; remove the workflow tag.
  - Example pattern: `SDSS-only environment proxy in massive hosts. High-density quartile: 0.509; low-density quartile: 0.367; bootstrap difference [0.112, 0.170]. This is a denominator for follow-up, not a coupling-efficiency measurement.`

2. Major: Conclusions in papers 2-9 are copy-pasted and incorrectly refer back to RP-1.
- Every non-RP1 conclusion ends with a sentence about the RP-1 association draft and “the other active topics,” which is confusing in a standalone manuscript.
- Examples:
  - [m1_rp2_environment_quenching_integrated.tex#L80](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex#L80)
  - [m2_p1_outflow_escape_recycling_integrated.tex#L79](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex#L79)
  - [m3_p3_simulation_validation_integrated.tex#L78](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex#L78)
- Safe rewrite guidance:
  - Replace the entire final paragraph in each non-RP1 paper with a paper-specific conclusion.
  - Keep the actual result, then the limitation, then the follow-up requirement.
  - Example pattern for a non-RP1 paper: `This manuscript isolates [measured SDSS quantity] in the SDSS emission-line sample, but the result remains a proxy because [missing observables].`
  - Do not mention RP-1 or “the other active topics” inside the paper-specific conclusion.

3. Minor: Abstracts are too generic and meta-heavy for publication.
- The abstract text mostly says the manuscript was integrated, not what was measured.
- That makes the PDFs read like workflow receipts rather than short papers.
- Safe rewrite guidance:
  - Put the measured SDSS result in sentence 1.
  - Put the boundary condition in sentence 2.
  - Keep provenance to one short clause or move it to a reproducibility note.
- Example template:
  - `Using the cached 60,000-row SDSS DR17 emission-line subset, [measured quantity] is [numeric result]. This is an SDSS-only proxy result and does not measure [causal physical claim].`
- Strong examples of result-specific text already available in the source-analysis receipts and should be surfaced in the abstract:
  - Paper 2: high-density quartile quenched fraction 0.230 vs low-density 0.181, bootstrap interval [0.041, 0.059].
  - Paper 4: 4,440 high-excitation AGN candidates of 60,000 (0.074), median log sSFR -11.53 vs -10.14.
  - Paper 6: first stellar-mass bin with quenched fraction above 0.5 is 11.0-12.5; optical AGN fraction peaks there at 0.520.
  - Paper 9: 15 mass-redshift cells with n >= 50; quenched fractions span 0.005-0.729 and optical AGN fractions 0.003-0.520.

4. Minor: RP-1 has one precision bug in the representativeness sentence, and several manuscripts still use internal-scope wording in the body.
- In RP-1, “largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR” is mathematically sloppy because absolute differences are not negative.
- In the non-RP1 papers, `All nine integrated drafts use the same public-data backbone...` and `SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.` make the manuscripts less self-contained.
- Safe rewrite guidance:
  - RP-1 [m1_rp1_sdss_agn_sfr_integrated.tex#L45](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex#L45): change to `The largest signed differences were 2.03 percentage points in redshift, 1.63 percentage points in stellar mass, and 0.58 percentage points in sSFR.`
  - Replace “All nine integrated drafts...” with a single self-contained sentence about this manuscript’s cached SDSS DR17 subset.
  - Replace “research-topic page” with the actual missing observables, listed inline.

Exact feed for PDF-writing pilot
- Paper 1 abstract should surface the real result and preserve the selection boundary.
  - Suggested rewrite: `Using the 60,000-row SDSS DR17 emission-line subset, broad BPT AGN hosts matched in stellar mass and redshift show a median catalog sSFR offset of -1.309 dex relative to star-forming controls (95% bootstrap interval [-1.334,-1.283]). This is an association result within an emission-line-selected SDSS sample, not causal AGN feedback evidence.`
- Paper 1 conclusion should stop after the RP-1 result and remove suite-level spillover.
  - Suggested rewrite: `The strongest result is an association-only short-paper draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass-redshift matched star-forming controls, with sensitivity to selection and subclass definitions.`
- Paper 2 caption should be rewritten around the actual result, not the workflow tag.
  - Suggested rewrite: `SDSS-only environment proxy in massive hosts. High-density quartile quenched fraction is 0.230 (3,456/15,000); low-density quartile is 0.181 (2,710/15,000); bootstrap high-minus-low interval is [0.041, 0.059]. This is a proxy for follow-up, not a halo-based environmental-quenching measurement.`
- Paper 3 caption should be rewritten around the actual result, not the workflow tag.
  - Suggested rewrite: `SDSS-only maintenance-heating denominator in massive, low-sSFR hosts. The massive subset contains 9,298 emission-line galaxies; 5,695 are low-sSFR; the optical BPT AGN fraction is 0.430 in the massive subset and 0.607 in the low-sSFR subset. This is a duty-cycle denominator, not a heating-to-cooling measurement.`
- Paper 4 caption should say the escape/recycling denominator, not the internal label.
  - Suggested rewrite: `SDSS-only outflow-follow-up denominator. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074), and their median log sSFR is -11.53 versus -10.14 for the full denominator. This does not measure escape velocity or multiphase outflow speed.`
- Paper 5 caption should mirror the environment result and its limitation.
  - Suggested rewrite: `SDSS-only optical AGN environment proxy in massive hosts. High-density quartile optical AGN fraction is 0.509; low-density quartile is 0.367; bootstrap high-minus-low interval is [0.112, 0.170]. This is an environment proxy for radio/X-ray follow-up, not a jet-coupling measurement.`
- Paper 6 caption should be the mass-transition diagnostic.
  - Suggested rewrite: `SDSS-only optical transition diagnostic. The first stellar-mass bin with quenched fraction above 0.5 is 11.0-12.5, and optical AGN fraction peaks there at 0.520. This is a transition diagnostic only; it does not assign the transition to stellar or AGN feedback.`
- Paper 7 caption should emphasize denominator sensitivity.
  - Suggested rewrite: `SDSS-only common-denominator optical tracer census. Simple optical tracer definitions produce prevalence from 0.136 to 0.418 within the same 60,000-galaxy denominator, a factor of 3.1. This shows denominator sensitivity, not multiphase outflow rates.`
- Paper 8 caption should stay explicit about the CO follow-up boundary.
  - Suggested rewrite: `SDSS-only CO follow-up denominator. The massive transition/quenched denominator contains 6,729 galaxies; optical BPT AGN fraction is 0.549; median log H-alpha proxy is 40.06, which is 0.66 dex below massive star-forming emission-line galaxies. This is not a molecular-gas depletion measurement.`
- Paper 9 caption should stay explicit about forward-model targets only.
  - Suggested rewrite: `SDSS-only target vector for forward modeling. The pilot writes 15 mass-redshift cells with n >= 50; quenched fractions span 0.005-0.729 and optical AGN fractions span 0.003-0.520. This is an observed target vector, not a direct simulation comparison.`
- Reproducibility sections should be shortened for publication-facing text.
  - Keep one sentence of provenance.
  - Move run IDs, packet names, and workflow tags out of the visible manuscript body or into a local-only appendix if the pilot requires them.

Real-data/source/citation audit notes
- No mock, synthetic, placeholder, or toy data were accepted in the reviewed manuscripts.
- The main quantitative claims match the `source_analysis_results.json` receipts:
  - Paper 2: 60,000-row emission-line denominator; high-density 0.230 vs low-density 0.181; CI [0.041, 0.059].
  - Paper 4: 4,440 high-excitation AGN candidates out of 60,000; median log sSFR -11.53 vs -10.14.
  - Paper 5: high-density 0.509 vs low-density 0.367; CI [0.112, 0.170].
  - Paper 6: first quenched-fraction bin above 0.5 is 11.0-12.5; optical AGN fraction peaks at 0.520.
  - Paper 7: prevalence range 0.136 to 0.418.
  - Paper 8: 6,729 massive transition/quenched galaxies; BPT AGN fraction 0.549; median H-alpha proxy 40.06.
  - Paper 9: 15 mass-redshift cells with n >= 50; quenched fractions 0.005-0.729; optical AGN fractions 0.003-0.520.
- Citation-role separation is broadly correct:
  - SDSS/BPT/catalog citations are used for the method.
  - Radio, X-ray, molecular-gas, wind, and simulation citations are correctly reserved for missing-observable motivation.
- No unresolved references or citation errors showed up in the compile logs.
- One wording bug exists in RP-1’s representativeness sentence: “absolute differences” should not carry negative signs.
- Public/live research-topic markdown is identical across the two roots I inspected, so I did not find a stale public-vs-local divergence inside that page itself.
- The scope mismatch is instead between the public-linked 3-proposal hub and the local 9-paper integrated candidate set, which is expected context but should not be conflated.

Workflow/system notes
- The compile receipts were clean enough to proceed; warnings were cosmetic rather than fatal.
- I saw underfull `\hbox` warnings across several papers.
- I saw small overfull `\vbox` warnings in [m2_p3_feedback_transition_mass_integrated.tex#L85](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex#L85) and [m3_p3_simulation_validation_integrated.tex#L85](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex#L85); if the PDF page bottoms look crowded, a small bibliography reflow is the likely fix.
- The dominant workflow issue is prose hygiene, not data integrity.

Safety ledger
- Edits: 0
- Public/live root changes: 0
- Database/API/wiki writes: 0
- Deploy/restart: 0
- Git commit/push/merge/rebase/history rewrite: 0
- Cron changes: 0
- Billing/cloud/OAuth/account changes: 0
- External submission: 0
- Credential/token/cookie reads: 0


# command_result
exit_code=0
elapsed_s=401.4
timed_out=False
finished_utc=2026-07-09T16:38:28Z
