# Hwao private autopilot dashboard V2 — design-direction review receipt

Marker: HWAO_PRIVATE_AUTOPILOT_DASHBOARD_V2_REVIEW_20260707T093119Z
Brief followed: HWAO_PRIVATE_AUTOPILOT_DASHBOARD_V2_REVIEW_BRIEF_20260707T093119Z
Reviews: V2 dashboard (marker `GE_AUTOPILOT_PRIVATE_DASHBOARD_V2`), live at `https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html`
Author: Hwao-director (pane %107). Written 2026-07-07 (KST evening).
Basis: operator-verified facts supplied with the review request + the V1 design receipt (`HWAO_PRIVATE_AUTOPILOT_DASHBOARD_DESIGN_20260707T085122Z`) + the known `autopilot-status.json` schema. **Direction review only** — I ran no tools and did not inspect the live page; mechanical/implementation verification remains the builder/Tori's job.

---

## VERDICT: PASS

The V2 direction is approved. On the operator-verified facts it preserves the V1 safety frame in full, adds the requested observability, and does so without introducing any control surface. Nothing in the direction needs to change to ship. Three non-blocking confirm-items (below) are things the builder/Tori should eyeball on the live page; each carries an exact patch to apply *only if* it turns out absent.

## Goal-by-goal conformance (against the brief's four V2 goals)

| # | Goal | Verified facts | Result |
|---|---|---|---|
| 1 | Preserve V1 safety frame — private tailnet mirror, read-only, no action surface, no public cockpit/Baseline replacement | private tailnet-only, read-only; no button/form/POST/external CDN; no public NebulaMind cockpit/Baseline changed | **PASS** |
| 2 | Easier to read from MacBook — bigger "does anything need me?" hero; clearer freshness/staleness; visible director/method lane map; plain-English next action; no need to open Goru's TUI | room-glance answer; directors/method cards; lane summaries; latest autopilot events; provenance | **PASS** (see confirm-items C1–C2) |
| 3 | Richer observability — role/lane summaries; latest autopilot events from local JSONL; per-lane status counts; safety policy legend | lane summaries; latest autopilot events; safety policy legend | **PASS** (see confirm-item C3) |
| 4 | Avoid control-looking UI — no approve/run/publish/execute buttons; informational only; JS only fetches local JSON + updates DOM | no button/form/POST; no external CDN | **PASS** |

## Safety frame — explicitly confirmed (the non-negotiable V1 carry-over)

- **Read-only, no action surface:** no button / form / POST / external CDN → the page cannot publish, write DB, deploy, run git, edit the cockpit, or take any board action. Confirmed.
- **Private tailnet-only:** served on the tailnet host; not a public surface. Confirmed.
- **No public cockpit/Baseline touched:** the V2 lives at `cockpit/ge-autopilot.html`; the public NebulaMind cockpit and `baseline-*.html` are unchanged. Confirmed.
- **Marker present** locally and over tailnet (`GE_AUTOPILOT_PRIVATE_DASHBOARD_V2`) → the live page and the local artifact are the same reviewed thing. Confirmed.
- **Self-contained JS:** local-JSON fetch + DOM update only, no external calls — matches the V1 "no CDN/analytics/remote asset" rule. Confirmed.

This is the part that mattered most, and it is clean: the upgrade added observability without adding capability. Good.

## Conditional patches — apply ONLY if the live page lacks the item (non-blocking)

These are the three goal sub-points not explicitly named in the verified-facts list. If present on the live page, ignore; if absent, apply exactly:

- **C1 — Freshness must be a STATE, not just a timestamp.** "Provenance" should include an explicit **STALE** treatment: when the snapshot `ts` age exceeds the threshold, show a visible "data stale — monitor may be paused" ribbon and never render a confident "nothing needs you" over old data. (Carry-over of the V1 freshness-honesty rule.)
- **C2 — Room-glance hero must give the plain-English NEXT ACTION for the blocked case.** Not just "does anything need me?" but, when blockers exist, one line naming what to do — e.g., "N item(s) waiting on you — open pane %xx" — vs the clean-state line "Nothing needs you — autopilot running." Keep it informational text (no action control).
- **C3 — Lane summaries must include per-lane status COUNTS.** Each of Directors / M1 / M2 / M3 shows a small tally (e.g., working / idle / blocked) so the user reads lane health at a glance without expanding, satisfying goal 3's "per-lane status counts."

All three are text/derived-state refinements consistent with the read-only frame — none introduces a control surface, external call, or public-cockpit dependency. They do not change the PASS.

## Scope note
This review judges the design direction on operator-verified facts. The exact mechanical checks on the built file (self-contained/no external requests, no form/POST in the DOM, pane/lane completeness vs `autopilot-status.json`, hard-gates integrity, staleness handling, path scoping away from Baseline/public cockpit) remain the builder/Tori's implementation-verification pass — see the V1 receipt §6 checklist, which applies unchanged to V2.

## Safety ledger (this receipt)
No tools run. Zero live wiki/`page_versions`/`/api/pages` · DB/SQL/trust · deploy/restart · git · cockpit/global/shared-parent/Baseline edit · cloud/GCP/Gemini/billing/OAuth/token/secrets · browser · cron · route/config action. Writes: 1 (this review receipt).

HWAO_PRIVATE_AUTOPILOT_DASHBOARD_V2_REVIEW_20260707T093119Z
