# Tori-director receipt — tmux usability repair

Marker: TORI_TMUX_USABILITY_REPAIR_20260707T123740Z
Author: Tori-director
Scope: local tmux usability only. No board/method work dispatched.

## User issue

Visible tmux panels looked flaky: some session layouts were larger than the visible terminal, so text/panes extended beyond the screen, and mouse/trackpad scrollback was unreliable in TUI panes.

## Diagnosis

Observed before repair:
- `mouse on` was already set, but only vi copy-mode wheel bindings existed while global `mode-keys` was `emacs`.
- Multiple board sessions were attached from clients with different sizes, but some windows were still sized around `238x72`, larger than visible clients such as `189x57`, `210x61`, `196x59`, and `182x53`.
- That mismatch explains panes/text going beyond the visible terminal boundary.

## Changes applied

Patched `/Users/duhokim/.tmux.conf`:
- Kept `set -g mouse on`.
- Kept `set -g history-limit 50000`.
- Added `set -g window-size smallest` so board windows do not exceed the smallest attached client.
- Added `setw -g mode-keys vi` so copy-mode behavior matches the existing wheel bindings.
- Added wheel bindings for both `copy-mode` and `copy-mode-vi`.

Runtime repair:
- Sourced `/Users/duhokim/.tmux.conf` into the running tmux server.
- Re-applied `mouse on`, `window-size smallest`, and `mode-keys vi` at runtime.
- Reflowed existing windows with `tmux resize-window -a`.

## Verification

Runtime options now show:
- `mouse on`
- `window-size smallest`
- `mode-keys vi`
- `history-limit 50000`

Wheel bindings now exist in:
- `root WheelUpPane` / `root WheelDownPane`
- `copy-mode WheelUpPane` / `copy-mode WheelDownPane`
- `copy-mode-vi WheelUpPane` / `copy-mode-vi WheelDownPane`

Window sizes now fit current attached clients instead of old oversized layouts, for example:
- `ge-mastermind:0` resized from `238x72` to `189x56`.
- `mesh-ge-m1-packet:0` resized from `238x72` to `210x59`.
- `mesh-ge-m2-source:0` resized from `238x72` to `196x58`.
- `mesh-ge-m3-debate:0` resized from `238x72` to `182x52`.

Director pane proportions were then nudged inside `ge-mastermind:0` so Hwao/Goru are not unusably narrow while Tori remains the widest pane: `%107=50x55`, `%109=45x55`, `%108=92x55`.

Autopilot status after the repair remained fresh and clean:
- phase `phase1-bounded-controller`
- blockers `0`

## Operator note

Trackpad/mouse wheel-up should now enter tmux scrollback instead of being swallowed by Claude/agy/Codex TUIs. If raw text selection is needed, use `tmux prefix + m` to toggle mouse off temporarily; turn it back on for scrolling.

Caveat: `window-size smallest` can make nested/live-view tmux clients shrink a source session to the embedded pane size. If a specific helper lane becomes too narrow, detach the nested live-view client or switch that specific session back to latest/manual sizing.

## Safety ledger

Local tmux configuration and runtime layout repair only. No DB/SQL. No `/api/pages`. No `page_versions`. No live wiki publish. No product deploy/restart. No git commit/push/merge. No public NebulaMind cockpit/Baseline edit. No cloud/GCP/Gemini/billing/OAuth/secrets. No browser automation. No cron. No new method dispatch.

TORI_TMUX_USABILITY_REPAIR_20260707T123740Z
