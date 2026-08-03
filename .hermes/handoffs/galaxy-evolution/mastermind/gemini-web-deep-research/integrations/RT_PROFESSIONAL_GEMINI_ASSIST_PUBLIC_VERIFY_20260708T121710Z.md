# Public verification — Gemini-assisted professional RT revision

Marker: `RT_PROFESSIONAL_GEMINI_ASSIST_PUBLIC_VERIFY_20260708T121710Z`
Revision marker: `AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z`

## User request

Use Gemini Deep Research / Gemini-web help to revise the current Galaxy Evolution research-topic pages because the previous pages did not read like professional-level research proposals.

## What actually happened

- Prepared a Gemini-web Deep Research prompt packet for the 18 prior cards.
- Attempted supervised browser/Gemini-web execution through computer use.
- Browser GUI path was blocked: `computer_use` returned 0x0 captures for screen/Chrome/Safari even though `hermes computer-use doctor` was green.
- No login, payment, API/GCP/billing/OAuth/token/cookie/profile screen was clicked or handled.
- Used the authenticated Gemini/Antigravity lane as a labeled advisory fallback, not as a verified Gemini-web Deep Research transcript.
- Verified retained source links through local artifacts and arXiv/public HTTP metadata before using them in page text.

## Revision outcome

The visible RT pages were rewritten from process-heavy topic cards into proposal-style research programmes:

- 3 main proposal cards per method, not 6 mixed science/meta cards.
- Meta/process cards were demoted to a short methodological note.
- Visible internal terms were removed from the page body.
- Each proposal now has:
  - Hypothesis / objective
  - Prior evidence and constraints
  - Remaining uncertainty
  - Survey/data plan
  - Analysis/test and decision criterion
  - Limitations and wording guardrails

## Public URLs verified

M1:
https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html

M2:
https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html

M3:
https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html

## Verification summary

Working root strict verification: PASS.
Live root static verification: PASS.
Public URL verification: PASS.

Per method public checks:

- M1: HTTP 200; 3 proposal cards; 3 `Survey/data plan` sections; 3 `Analysis/test and decision criterion` sections; 3 `Prior evidence and constraints` sections; marker present; 1 local evidence link checked; 0 broken local links; no visible internal agent/process terms.
- M2: HTTP 200; 3 proposal cards; 3 `Survey/data plan` sections; 3 `Analysis/test and decision criterion` sections; 3 `Prior evidence and constraints` sections; marker present; 0 broken local links; no visible internal agent/process terms.
- M3: HTTP 200; 3 proposal cards; 3 `Survey/data plan` sections; 3 `Analysis/test and decision criterion` sections; 3 `Prior evidence and constraints` sections; marker present; 2 local evidence-anchor links checked; 0 broken local links; no visible internal agent/process terms.

Static source safety in working + live roots:

- 0 source `<script>`
- 0 `fetch`
- 0 XMLHttpRequest
- 0 WebSocket
- 0 inline event handlers
- 0 forms
- 0 product `<!--claim:` comments
- 0 product `<!--cite:` comments

## Backups

Live static backups:
`/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/_research_topics_professional_gemini_backups_20260708T121710Z/`

Working static backups:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z`

## Safety boundary

No DB writes. No SQL. No `/api/pages`. No page_versions/live wiki publish. No trust recompute. No deploy/restart. No git commit/push/merge. No cron. No browser-login/payment/API/GCP/OAuth/token handling.

RT_PROFESSIONAL_GEMINI_ASSIST_PUBLIC_VERIFY_20260708T121710Z
