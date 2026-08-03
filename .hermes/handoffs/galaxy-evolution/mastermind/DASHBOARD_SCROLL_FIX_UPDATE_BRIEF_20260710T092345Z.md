# Hwao dashboard-report direction brief

Timestamp: 2026-07-10T09:23:45Z
User direction: "okay now can you update the dashboard?"

Immediate context
- The user reported that reading tmux history jumped back to the prompt even after `Ctrl-b [`.
- Tori instrumented pane `%108` and reproduced the exact transition: copy mode entered at 09:10:12Z and was cancelled at 09:10:30Z.
- The private Galaxy Evolution autopilot event log recorded `clear-copy-mode` for `%108` at exactly 09:10:30Z. The controller's `approve_safe_prompts()` was cancelling every pane with `in_mode` on its 20-second tick.
- Tori added a RED regression test, changed the controller to skip panes in any copy/view mode entirely, restarted only the private autopilot watcher with its prior settings, and verified the focused test (`1 passed`) plus controller self-test (`PASS`).
- Live verification: copy mode remained active for more than 100 seconds across at least five 20-second autopilot ticks; the user confirmed `stayed`.
- No product DB/API/wiki publish, product deploy, backend/frontend restart, git commit/push/merge, billing/API/OAuth, or public cockpit redesign occurred.

Requested Hwao action
- Act as coordinator/report author for this dashboard update.
- Assume the intended surface is the private Galaxy Evolution autopilot dashboard (`/cockpit/ge-autopilot.html`) because the bug was in that watcher. If a different dashboard is clearly intended, say so.
- Return concise, plain-English dashboard direction only: current state, what happened, result, what changed, safety ledger, and exact next action.
- Preserve the existing private dashboard layout, cards, polling, provider gauges, and route. Add or update only the smallest status/incident block or structured JSON field.
- Keep public stable Baseline cockpit untouched unless you explicitly direct otherwise.
- Do not write files, restart anything, or send tmux keys. Stop after giving Tori the dashboard wording and target fields.
