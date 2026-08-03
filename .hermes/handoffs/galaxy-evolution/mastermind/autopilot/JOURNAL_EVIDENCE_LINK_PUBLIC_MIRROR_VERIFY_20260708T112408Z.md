# Public mirror verification — research topics journal-quality evidence-link pass

Marker: `AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z`
Applied by: Tori/Hermes
UTC applied: 2026-07-08T11:44:12Z
Public host verified: `https://nebulamind.net`

## Status: COMPLETE

The journal-quality/evidence-linked research-topic pages have been mirrored from the working repo static root into the live frontend static root and verified publicly.

## Files copied / changed

Live frontend root:
`/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/`

Per method, the following static files were copied from the working root to the matching live root:
- `manifest-20260708T090359Z.json`
- `research-topic-map-20260708T090359Z.json`
- `research-topics-from-wiki-20260708T090359Z.html`
- `research-topics-from-wiki-20260708T090359Z.md`

Backups of the previous live research-topic directories:
`/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/_research_topics_journal_evidence_backups_20260708T114412Z/`

Additional public-link repair:
- Method 2 markdown marker was added to both working and live roots because the HTML had the marker but the markdown did not.
- Method 3 prior-evidence links were repointed from a newly copied `.md#sN` target, which returned 404 from the already-running static server, to the already-served Method 3 evidence HTML anchors:
  `../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#...`
- This avoided a frontend restart.

## File-level verification

Working root and live root both passed:

| Method | cards | JSON count | marker in HTML/MD | prior-evidence links/card | broken local links | source static-safety | product claim/cite comments | formal-tone scan |
|---|---:|---:|---|---|---:|---|---:|---|
| M1 | 6 | 6 | yes/yes | 8, 13, 8, 2, 1, 1 | 0 | pass | 0 | pass |
| M2 | 6 | 6 | yes/yes | 5, 4, 5, 4, 3, 3 | 0 | pass | 0 | pass |
| M3 | 6 | 6 | yes/yes | 4, 2, 3, 2, 1, 4 | 0 | pass | 0 | pass |

Source static-safety means: 0 `<script>`, `fetch`, XHR, WebSocket, inline event handlers, and `<form>` in the local/static HTML artifacts.

## Public HTTP verification

All public pages returned HTTP 200 with the journal marker and visible prior-evidence sections:

- M1: `https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`
  - HTTP 200
  - marker present
  - prior-evidence text present
  - visible href count: 40
  - local evidence links checked: 2
  - broken local evidence links: 0

- M2: `https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`
  - HTTP 200
  - marker present
  - prior-evidence text present
  - visible href count: 33
  - local evidence links checked: 11
  - broken local evidence links: 0

- M3: `https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`
  - HTTP 200
  - marker present
  - prior-evidence text present
  - visible href count: 26
  - local evidence links checked: 8
  - broken local evidence links: 0

Note: public responses include a serving-layer `<script>` tag, but the source artifacts themselves are static-safe. This is the expected distinction described in the public-cockpit/static-report workflow.

## Safety ledger

Done:
- static file copy to existing live frontend public directories
- backup before overwrite
- public HTTP/content verification
- public local-evidence-link verification

Not done:
- no backend/API restart
- no frontend restart
- no DB writes
- no `/api/pages`
- no page_versions or live wiki publish
- no trust recompute
- no deploy
- no git commit/push/merge
- no browser automation
- no cron
