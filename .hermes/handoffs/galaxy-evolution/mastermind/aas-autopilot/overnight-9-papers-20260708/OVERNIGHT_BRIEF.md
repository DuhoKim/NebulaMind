# Overnight 9-paper autopilot brief

Marker: `OVERNIGHT_9_PAPERS_AUTOPILOT_20260708T132404Z`

User request:

> work on the 9 papers overnight using all your autopilots. do not finish in a short time. work until tomorrow morning.

Local time when scheduled: 2026-07-08 22:24:04 KST.
Default morning target: 2026-07-09 08:00 KST.
Morning rollup target: 2026-07-09 08:05 KST.

## Scope

Work on the 9 active Galaxy Evolution AAS-style pilot papers, improving their scientific/reproducibility quality over multiple overnight passes. The 9 are the active consolidated proposal-card papers already linked on the public research-topic pages:

1. M1 RP-1 — SDSS AGN/sSFR matched-control pilot.
2. M1 RP-2 — SDSS density proxy for environmental quenching.
3. M1 RP-3 — optical-AGN denominator for maintenance-heating follow-up.
4. M2 P1 — high-excitation optical AGN denominator for outflow escape/recycling tests.
5. M2 P2 — environment proxy for optical AGN in massive hosts.
6. M2 P3 — mass transition in quenching and optical AGN incidence.
7. M3 P1 — common-denominator optical tracer census.
8. M3 P2 — optical denominator for gas-fraction versus efficiency tests.
9. M3 P3 — SDSS target vector for feedback-model validation.

Important correction: these 9 cover the active consolidated pages, not every historical candidate topic from pre-reduction backups. Overnight work should preserve that distinction and may create notes mapping omitted historical candidate topics to future extensions, but should not pretend the current 9 exhaust the historical topic universe.

## Inputs

Repo root:

`/Users/duhokim/NebulaMind/NebulaMind`

Autopilot root:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot`

First paper run:

`runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/`

Remaining 8-paper batch run:

`runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/`

Existing batch manifest:

`runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/ALL_REMAINING_TOPIC_PILOTS_MANIFEST.json`

Existing public-link verification packet:

`ALL_TOPICS_AAS_PDF_LINK_PUBLIC_VERIFY_20260708T130505Z.md`

Overnight work root:

`overnight-9-papers-20260708/`

## Allowed actions

- Read public web/arXiv/Semantic Scholar/SDSS resources.
- Read local backup/topic/source/manuscript files.
- Run local Python analysis scripts.
- Write local artifacts under the overnight work root and/or a new local manuscript-improvement run under the aas-autopilot root.
- Generate figures, tables, JSON summaries, AASTeX source, compiled PDFs, verification logs, and handoff notes.
- Recompile local PDFs and record hashes.

## Prohibited without fresh explicit user approval

- NebulaMind/product DB writes or SQL.
- `/api/pages`, `page_versions`, live wiki publish, trust recompute.
- Public/live frontend page changes or public mirroring.
- Deploy/restart.
- Git commit/push/merge/rebase.
- Creating additional cron jobs from inside a cron run.
- Billing/cloud/OAuth/API-key setup or changes.
- External journal/arXiv/manuscript submission.

## Overnight worker expectations

Each scheduled tick should do one real bounded phase and write a tick report. Do not just say work is done because the current PDFs compile. Choose the next useful improvement from this backlog:

1. Build a paper-by-paper quality inventory: missing sections, weak claims, proxy limits, figures/tables, bibliography gaps.
2. Add or verify literature/source anchors with arXiv/Semantic Scholar/public pages; record URLs and exact relevance.
3. Add robustness analyses from the cached SDSS sample: S/N cuts, redshift/mass bins, density-proxy variants, BPT class sensitivity, bootstrap intervals, table outputs.
4. Improve AASTeX manuscripts with honest scope guards, clearer methods, reproducibility tables, and topic-specific result tables.
5. Recompile modified PDFs and verify hashes.
6. Map omitted historical candidate topics from backups to the 9 active consolidated papers and list future extra-paper candidates.
7. Prepare a morning handoff with what changed, what is stronger, what remains proxy-only, and next high-value data extensions.

Every tick must update:

- `OVERNIGHT_LEDGER.md`
- `ticks/TICK_<UTC_TIMESTAMP>.md`

If a tick changes manuscripts/PDFs, also update a local manifest with PDF paths, sizes, SHA256, compile status, and source paths.

## Reporting style

Plain English. Distinguish actual data from proposal/future data. Never invent survey results, citations, or source metadata. If a claim remains proxy-only, say so.

## Safety line for final/morning packet

No DB/API/page_versions/wiki publish/deploy/restart/git/cron/billing/OAuth changes were performed unless explicitly recorded with separate approval.
