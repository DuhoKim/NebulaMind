# Couple-hour LaTeX + publishability repair board

Run ID: `LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z`
Run root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z`
Started UTC: 2026-07-09T23:54:47Z
Target end UTC: 2026-07-10T01:54:47Z
Source candidate: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_19_nine_papers`
Source note: latest completed overnight candidate cycle 19: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_19_nine_papers/CYCLE_19_AFTER_RECEIPT.json

## Mission
Run autonomous pilots for about two hours to fix real LaTeX/log problems and improve AAS-style publishability in local candidate copies only.

## Lanes
- hwao_publishability_director: agy / Gemini 3.1 Pro (Low) — Hwao/Fable director: triage why the papers still feel not publishable; prioritize exact blockers for the writer.
- gemini_latex_layout_critic: agy / Gemini 3.5 Flash (Low) — Goru/Gemini TeX critic: focus on LaTeX errors, warnings, overfull/underfull boxes, broken citations/references, figure/table layout, and exact safe TeX fixes.
- gemini_publishability_critic: agy / Gemini 3.1 Pro (High) — Gemini Deep manuscript critic: strict AAS-style publishability review and exact rewrite instructions, preserving real-data boundaries.
- gptoss_skeptic: agy / GPT-OSS 120B (Medium) — Low-usage skeptic: adversarial scan for remaining non-publishable structure, weak abstracts, unsupported claims, and reader-confusing language.
- codex_kun_tex_repro: codex / gpt-5.4-mini — Kun/Codex read-only TeX/reproducibility audit: inspect candidate TeX and strict compile audit; report exact blockers; no edits.

## Safety locks
- write only under this repair run root and copied candidate packages
- review lanes write reports only; only the candidate-copy integrator edits candidate-copy TeX
- no public-linked PDF replacement or public/live static root edits
- no DB, SQL, /api/pages, page_versions, wiki publish, trust recompute, or data mutation
- no deploy/restart
- no git commit/push/merge/rebase/history rewrite
- no cron creation/update/removal
- no billing/cloud/OAuth/API-key/account changes and no credential/token/cookie reads
- no external manuscript submission

## Real-data rules
- Never use mock, synthetic, fake, placeholder, or toy data as manuscript evidence.
- Never invent numbers, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, figure results, or table values.
- Every quantitative claim must trace to real local artifacts or checkable public sources already in the package.
- Absent data must be written as absent/future real-data requirements, not inferred as results.
- RP-1 stays association-only; papers 2-9 stay SDSS optical denominator/proxy notes unless new real data are inventoried.
