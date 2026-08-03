# Hwao private autopilot dashboard — design receipt

Marker: HWAO_PRIVATE_AUTOPILOT_DASHBOARD_DESIGN_20260707T085122Z
Brief followed: HWAO_PRIVATE_AUTOPILOT_DASHBOARD_DESIGN_BRIEF_20260707T085122Z
Author: Hwao-director (pane %107), design collaboration with Goru (mechanical verification, §6).
Written: 2026-07-07 (~17:55 KST), designed against the real `autopilot-status.json` snapshot observed at ts 17:53.
Class: **design receipt only** — private, tailnet-only, static HTML/JSON. No build, no mutation performed here.

Implementation target (for the later build step, not built now):
- File: `/Users/duhokim/HermesOps/cockpit/ge-autopilot.html` (NEW file — must not edit `baseline-*.html` or the public NebulaMind cockpit)
- URL: `https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html`
- Data: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot-status.json`

Design is bound to the actual JSON schema: `ts`, `phase`, `targets`, `hard_gates_closed[]`, `blockers[]`, `panes[]{role, master_role, mesh_role, target, active, dead, in_mode, current_command, title, tail, size, classification{permission_prompt, safe_to_approve, read_onlyish, forbidden_pattern, referenced_paths[]{path, allowed}}}`, `repo`, `state_path`, `status_path`. Every UI element below maps to one of these — nothing invented.

---

## 1. Recommended layout sections (top → bottom)

1. **Status hero bar** (sticky, full-width). Left: `phase` + repo short name. Center: one large **board-state pill** (§2 rollup). Right: **freshness** — parsed `ts` rendered as "updated 12s ago", turning amber when the snapshot is stale (§6). This is the room-glance line.
2. **Hard-gates strip** — the 8 `hard_gates_closed[]` rendered as small locked-🔒 chips under the hero, always visible. If the array is missing any expected gate, that chip renders red (escalation), else all green-locked.
3. **"Needs you" blockers panel** — derived from `blockers[]`, shown ONLY when non-empty; sorted NEEDS-YOU first, then SAFE. Each row: `role` · `pane_id` · one-line `reason` · a classification badge (§2). Empty state collapses to a single green "No blockers — board running clean" line so the panel never adds noise.
4. **Directors band** — the two director panes (`master_role` ∈ {Hwao-director, Tori-director}, `target` `ge-mastermind:Directors`). Wider, emphasized (§5).
5. **Method lanes M1 / M2 / M3** — three equal-weight columns (desktop) / stacked cards (MacBook portrait), grouped by `target` (`mesh-ge-m1-packet`, `mesh-ge-m2-source`, `mesh-ge-m3-debate`). Each lane: a header chip for the method's Hwao coordinator + member chips for Goru/Kun/Lana/Tori, plus the lane's current step/verdict if present in `targets`/`phase`.
6. **Standalone/helper bucket** (small, collapsible) — any pane whose `target`/`mesh_role` isn't a director or a numbered mesh (e.g., standalone Goru/Lana lanes).
7. **Safety footer** — the persistent read-only-mirror statement (§4) + `state_path`/`status_path`/`ts` provenance line.

## 2. Plain-English status model

Per-pane state (derived, not a raw field — computed from the JSON so the label is honest):

| Label | Derivation from `panes[]` | Color |
|---|---|---|
| **WORKING** | `active` true and no `classification.permission_prompt` | blue (soft pulse) |
| **IDLE / DONE** | not active, `dead` false, no prompt | slate-gray |
| **BLOCKED · SAFE** | `permission_prompt` true AND `safe_to_approve` true AND `read_onlyish` true AND no `forbidden_pattern` AND every `referenced_paths[].allowed` true | amber |
| **BLOCKED · NEEDS YOU** | `permission_prompt` true AND (`safe_to_approve` false OR `forbidden_pattern` set OR any `referenced_paths[].allowed` false) | red |
| **DEAD** | `dead` true | dark-red, struck |

Board rollup (the hero pill), in plain words:
- **RUNNING CLEAN** — zero `blockers[]`, or only BLOCKED·SAFE items (a director can clear those in docs/static scope). Green.
- **NEEDS YOU · N** — N = count of BLOCKED·NEEDS-YOU. Red; N is the number the user actually cares about.
- **STALE** — if `ts` age exceeds the freshness threshold, the pill is overlaid with a "data stale — monitor may be paused" ribbon regardless of counts (never show a confident "clean" over old data).

Plain-English guarantee shown near the pill: *"Green means the autopilot is working and nothing needs you. Amber means a safe docs/static prompt a director can approve. Red means something is waiting on your decision."*

## 3. What the user should see first from the MacBook

Above the fold, legible across a room, in one glance answer three questions in this order:
1. **Does anything need me?** → the hero **board-state pill** (RUNNING CLEAN / NEEDS YOU · N). If red, the "Needs you" panel (§1.3) is the only thing that should draw the eye.
2. **Are the rails still shut?** → the **hard-gates strip** — all-🔒 green = safe to walk away.
3. **Is this data even current?** → the **freshness** stamp next to the pill.

Everything else (per-method lane detail, pane tails) is deliberately below the fold — reachable by scroll, never competing with the three answers above. Default view opens collapsed to lanes-summary; a pane's `tail` is revealed on click, not shown by default (keeps the board calm).

## 4. Safety language (exact phrasings to render)

- Persistent header badge: **"PRIVATE TAILNET MIRROR · READ-ONLY · this page takes no actions."**
- Hard-gates strip caption: **"Hard gates closed — no DB · no live wiki/publish · no deploy · no git · no cockpit/global · no cloud/billing/OAuth · no browser · no cron."** (mirrors `hard_gates_closed[]` verbatim).
- BLOCKED·SAFE badge tooltip: **"Docs/static, in-scope — a director can approve this without you."**
- BLOCKED·NEEDS-YOU badge tooltip: **"Hard-gate-adjacent or out-of-scope — your decision. The autopilot will not proceed on its own."**
- Footer: **"This dashboard is a read-only mirror of a JSON snapshot. It has no control surface: it cannot publish, write to the DB, deploy, run git, edit the cockpit, or take any board action. To act, use the actual panes."**
- Tone rule: never render a control-looking button. Links are informational (open a path/receipt), never actions. No "approve", "run", "publish" affordances anywhere.

## 5. Visual hierarchy — Directors, Method 1, Method 2, Method 3

Top-down weight, so the eye lands where steering happens then where work happens:
- **Directors band (tier 1)** — full-width, largest role chips, subtle accent border. Hwao-director and Tori-director side by side; Hwao-director leads (left). They set direction, so they sit above the methods.
- **Method lanes (tier 2)** — three equal columns, no method visually privileged over another (they are independent, competing approaches). Column header = method name + its Hwao coordinator chip (emphasized within the lane). Below it, the quintet members Goru → Kun → Lana → Tori as smaller uniform chips (consistent order across all three lanes for scan-ability).
- **Within a pane chip** — role name (bold) · state dot (color from §2) · one-line focus (from `title`, truncated). Blocked panes escalate visually: amber/red left-border and they float to the top of their lane so a stuck pane is never buried.
- **Standalone bucket (tier 3)** — de-emphasized, collapsed by default.
- Color discipline: exactly one accent hue for "attention" (red = needs-you) so red is rare and meaningful; amber for safe-approve; green/blue/gray for healthy states. Dark theme (home-lit MacBook viewing), high-contrast text, no decorative gradients competing with the status colors.

## 6. What Goru should verify mechanically (build-time conformance checklist)

Goru runs these read-only mechanical checks on the built `ge-autopilot.html` before it's considered ready:
1. **Self-contained / no external calls** — page has zero requests to any non-tailnet host: no CDN, web font, analytics, or remote asset; all CSS/JS inline. Only network activity is fetching the local `autopilot-status.json`.
2. **Pane completeness** — number of pane chips rendered == `len(panes)`; no pane silently dropped; DEAD panes still shown (struck), not hidden.
3. **Correct grouping** — panes bucket into Directors / M1 / M2 / M3 / standalone strictly by `target`/`master_role`/`mesh_role`; no pane double-counted or mis-lane'd.
4. **Blocker classification parity** — every `blockers[]` entry appears in the "Needs you" panel; each SAFE vs NEEDS-YOU badge exactly matches the §2 derivation from `safe_to_approve`/`forbidden_pattern`/`referenced_paths[].allowed` (spot-check ≥1 of each).
5. **Hard-gates integrity** — all 8 `hard_gates_closed[]` render as closed chips; if the array is short/changed, the missing gate escalates (red), never silently omitted.
6. **Freshness honesty** — `ts` parsed to an age; stale threshold triggers the STALE ribbon; a missing/malformed/empty JSON yields a clear "no data / monitor paused" state, not a blank page or a JS crash.
7. **No action surface** — DOM contains no form/POST/mutation control; grep the built file for `fetch(...POST`, `<form`, `<button` bound to anything beyond expand/collapse; links are informational only.
8. **Path scoping** — the file lives at `HermesOps/cockpit/ge-autopilot.html`; it does not modify `baseline-*.html`, `copy-execution-phrase.html`, the public NebulaMind cockpit, or any shared/global surface; the JSON fetch path resolves under the tailnet server root (see assumptions).
9. **MacBook render** — responsive down to a laptop viewport; the three §3 answers are above the fold without horizontal scroll; dark-theme contrast passes legibility.

## Data + implementation assumptions (flag for the builder — NOT built or decided here)

- **JSON reachability:** the web root (`HermesOps/cockpit`) differs from the JSON path (`NebulaMind/.hermes/...`). The build step must make the snapshot fetchable from the tailnet server (served path, symlink, or a benign read-only copy into the cockpit root). This is a docs/static plumbing choice for the builder; Goru §6.8 verifies whichever path resolves. No cron/daemon is implied — refresh is client-side.
- **Refresh:** client-side `setInterval` re-fetch of the JSON every ~15–30 s (read-only poll); no server push, no websocket.
- **Snapshot producer:** this dashboard only *reads* `autopilot-status.json`; whatever process writes that snapshot is out of scope for this design.

## Hard boundaries honored (this receipt)

Design-only. No DB/API write, no live wiki publish, no deploy/restart, no git, no public cockpit replacement, no baseline cockpit edit, no cloud/API/billing/OAuth/secrets, no cron. Read-only inspection of the JSON schema + web-root listing, and this one mastermind-local design receipt write.

## Safety ledger
Zero live wiki/`page_versions`/`/api/pages` · DB/SQL/trust · deploy/restart · git · cockpit/global/shared-parent/baseline edit · cloud/GCP/Gemini/billing/OAuth/token/secrets · browser · cron · route/config action. Writes: 1 (this design receipt).

HWAO_PRIVATE_AUTOPILOT_DASHBOARD_DESIGN_20260707T085122Z
