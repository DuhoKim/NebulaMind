# Overnight PDF review + workflow scrutiny swarm

Run ID: `OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z`
Run root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z`
Start UTC: 2026-07-09T16:31:02Z
Target end UTC: 2026-07-10T02:31:02Z
Start KST: 2026-07-10 01:31:02 KST
Target end KST: 2026-07-10 11:31:02 KST

## User directive
Critically review current PDFs and research-topic manuscripts, feed review output into PDF-writing pilots, and have another autopilot scrutinize the wiki-to-PDF/current workflow system for improvements. Work overnight for about 10 hours and use available/low-usage models.

## Inputs
- Local publishable candidate: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/candidates/cycle_01_nine_papers`
- Publishability handoff: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/publishability-loops/PUBLISHABLE_9_PDFS_DEEP_RESEARCH_LOOP_20260709T162008Z/FINAL_POST_FIX_HANDOFF.md`
- Integrated 9-paper root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z`
- Active existing sprint (left running, not interfered with): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z`
- Public-linked PDFs root (read-only): `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution`
- Live public PDFs root (read-only): `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution`

## Lanes
- `hwao_director` — Gemini 3.1 Pro (Low) — Hwao/Fable director: prioritize paper-quality work, decide what should feed writer pilots, and keep scope honest.
- `gemini_deep_pdf_critic` — Gemini 3.1 Pro (High) — Gemini Deep Research critic: strict astronomy/AAS-style review of all 9 PDFs and research-topic manuscripts.
- `gemini_flash_factcheck` — Gemini 3.5 Flash (Low) — Goru/Gemini low-usage fact-check: citation display, source-role, no-overclaim, and missing-observable scan.
- `gptoss_skeptic` — GPT-OSS 120B (Medium) — Low-usage local/open model skeptic: adversarial read for unclear logic, structure, and workflow risk.
- `claude_lana_manuscript` — Claude Sonnet 4.6 (Thinking) — Lana-style manuscript reviewer: polish priorities, journal-readiness, reader experience, and exact safe rewrites.
- `codex_kun_repro` — gpt-5.4-mini — Kun/Codex read-only reproducibility, TeX, provenance, and no-mock-data audit.
- `workflow_scrutiny` — Gemini 3.5 Flash (Medium) — Independent workflow auditor: scrutinize wiki -> topics -> manuscript/PDF -> public-link pipeline and propose system improvements.

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

## Real-data rules
- Never use mock, synthetic, fake, placeholder, or toy data as manuscript evidence.
- Never invent numbers, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, figure results, or table values.
- Every quantitative claim must trace to real local artifacts or checkable public sources.
- Absent data must be written as absent/future real-data requirements, not inferred as results.
- RP-1 stays association-only; papers 2-9 stay SDSS optical denominator/proxy data notes unless new real data are inventoried.
