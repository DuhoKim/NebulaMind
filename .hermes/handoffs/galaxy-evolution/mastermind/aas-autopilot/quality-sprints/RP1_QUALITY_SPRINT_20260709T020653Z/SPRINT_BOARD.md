# RP-1 four-hour local quality sprint

Marker: `RP1_QUALITY_SPRINT_20260709T020653Z`

Start UTC: 2026-07-09T02:11:24Z
Target end UTC: 2026-07-09T06:11:24Z
Start KST: 2026-07-09 11:11:24 KST
Duration: about 4 hours

## User directive

Let the autopilots that worked on the Galaxy Evolution papers keep working on the two-PDF package to increase quality, following Gemini/deep-research-style and/or Hwao review results, while leveraging low-usage models.

## Source package

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`

Inputs:

- polished RP-1 flagship paper
- supplementary denominator/proxy atlas
- package audit and final handoff

## Lane roles

- Hwao-style director lane: AGY/Antigravity `Gemini 3.1 Pro (Low)`, publication/readiness triage.
- Gemini/Goru deep-review-style lane: AGY/Antigravity `Gemini 3.5 Flash (Low)`, science guardrails, missing observables, citation-role critique.
- Codex/Kun lane: Codex `gpt-5.4-mini`, read-only reproducibility/prose/TeX critique and candidate-only integration edits.
- Goru mechanical lane: local Python checks for phrases, figures, PDFs, logs, and unchanged numeric invariants.
- Tori integrator lane: this orchestrator copies the package into cycle-local candidate directories, applies only local candidate edits, compiles, audits, and writes receipts.

## Single-writer rule

Reviewer lanes write reports only. The integrator lane may edit only candidate copies under this sprint directory. The original decision package and public-linked artifacts are not edited.

## Safety locks

- no public pages or live roots
- no public PDF replacement
- no database, SQL, /api/pages, page_versions, wiki publish, or trust recompute
- no deploy/restart
- no git commit/push/merge/rebase
- no cron creation/update
- no billing/cloud/OAuth/API-key/account changes
- no external manuscript submission
- no credential/token/cookie reads
