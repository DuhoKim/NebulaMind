# Actual-data-only journal-paper quality sprint

Marker: `ACTUAL_RESEARCH_JOURNAL_SPRINT_20260709T131026Z`
Start UTC: 2026-07-09T13:16:29Z
Target end UTC: 2026-07-09T21:16:29Z
Start KST: 2026-07-09 22:16:29 KST

## User directive
Relaunch the autopilots that worked on actual research and journal-paper writing; enhance paper quality using low-usage provider lanes such as Gemini/Gemini-web/deep-research style. For research, never use mock data; use real data only.

## Source package
Primary candidate source: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/final_guardrail_cleanup_package`
Integrated nine-paper context: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z`
Overnight lane artifacts: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708`

## Lane roles
- Hwao/Fable director lane: Gemini 3.1 Pro Low via AGY; publication triage and paper-by-paper priority.
- Gemini deep-research lane: Gemini 3.1 Pro Low via AGY; web/deep-research-style literature/source gap work with URLs/DOIs/arXiv/ADS only.
- Gemini source fact-check lane: Gemini 3.5 Flash Low via AGY; citation-role and overclaim checks.
- Kun/Codex lane: gpt-5.4-mini read-only reproducibility, TeX, and data-provenance audit.
- Goru mechanical lane: local Python real-data inventory, hashes, row counts, no-mock scan, compile receipts.
- Tori integrator lane: candidate-copy-only TeX integration; no public/live/git/DB/deploy side effects.

## Real-data-only policy
- Never use mock, synthetic, fake, placeholder, or toy data.
- Do not invent numeric values, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, or figure results.
- New quantitative claims must be traceable to the real local SDSS artifacts inventoried by this sprint or to a cited public source with URL/DOI/arXiv/ADS metadata.
- If a value is not present in the local real-data inventory or a cited public source, write 'not measured here' or 'needs real data'.
- Literature-only sources may motivate future work; they do not become measured NebulaMind results.
- The RP-1 flagship remains an optical SDSS/BPT association pilot unless real additional observables are supplied.

## Safety locks
- write only under this sprint directory and candidate copies
- no public pages, public PDF replacement, or live/static root edits
- no product DB, SQL, /api/pages, page_versions, wiki publish, trust recompute, or data mutation
- no deploy/restart
- no git commit/push/merge/rebase/history rewrite
- no cron creation/update
- no billing/cloud/OAuth/API-key/account changes and no credential/token/cookie reads
- no external manuscript submission
