# Kmux-style tmux + iTerm2 Comparison Plan

> **For Hermes:** Execute this plan only after explicit user approval for each side-effect gate. Do not migrate or modify active NebulaMind tmux boards by default.

**Goal:** Pursue options 2+3: keep tmux as the live substrate, borrow kmux/iTerm2-style observability improvements, and compare iTerm2 tmux control-mode in a disposable macOS sandbox.

**Architecture:** Treat tmux as the persistent source of truth. Add read-only/status-producing helper scripts and optional tmux bindings around the existing board; compare iTerm2 only against a separate tmux socket/session so active sessions are never touched.

**Tech Stack:** macOS, Homebrew tmux 3.6b, optional iTerm2 cask, tmux control mode (`tmux -CC`), Python/shell helpers.

---

## Current facts from inspection

- Correct Linux/KDE kmux is `futpib/kmux`: a Konsole fork that maps tmux control-mode windows/panes onto native Konsole tabs/splits.
- It is not directly usable on this Mac as a Homebrew package.
- Local tmux exists: `/opt/homebrew/bin/tmux`, version `tmux 3.6b`.
- iTerm2 is not installed.
- Homebrew cask is available: `iterm2` version `3.6.11`, app artifact `iTerm.app`, requirement macOS >= 12.
- Active tmux clients are normal clients, not control-mode clients:
  - `/dev/ttys044`, `ge-mastermind`, control `0`
  - `/dev/ttys003`, `ge-mastermind`, control `0`
  - `/dev/ttys002`, `goru-agy`, control `0`
- Current `~/.tmux.conf` already contains several kmux-like safety/UX pieces:
  - mouse on
  - set-clipboard on
  - copy-command pbcopy
  - history-limit 50000
  - window-size smallest
  - pane-border-status top
  - pane-border-format showing `@mesh_role` and pane id
  - prefix+u copies cockpit URL
  - prefix+e copies execution phrase
  - prefix+m toggles mouse/selection mode
  - prefix+p copies active pane recent scrollback
  - prefix+P copies active pane visible screen

## Non-negotiable guardrails

- Do not migrate active NebulaMind boards to kmux or iTerm2 control mode without a separate approval.
- Do not kill, restart, resize, split, attach, detach, or send keys into active board panes as part of evaluation.
- Do not change public cockpit, DB, deploy state, git history, or cron jobs.
- Any iTerm2 test must use a separate tmux socket, e.g. `tmux -L iterm-sandbox`, not the default active tmux server.
- Any tmux config change must be backed up and reload-tested before use.

---

## Track 2: Borrow kmux-style ideas while staying on tmux

### Task 2.1: Add a read-only board snapshot helper

**Objective:** Produce one structured JSON snapshot of all tmux sessions/windows/panes for dashboards and status inspection.

**Files:**
- Create: `tools/tmux_board_snapshot.py`
- Output target: `.hermes/tmux-board-status.json` or `/tmp/tmux-board-status.json`

**Implementation shape:**
- Run only read-only tmux commands:
  - `tmux list-sessions`
  - `tmux list-windows -a`
  - `tmux list-panes -a`
  - `tmux list-clients`
- Include for each pane:
  - session/window/pane target
  - active/dead flags
  - current command
  - current path
  - title
  - `@mesh_role`
  - pane id
  - tty
  - dimensions
- Include top-level warnings:
  - dead panes
  - empty `@mesh_role` on known board panes
  - non-control clients vs control clients
  - smallest-client width/height constraints

**Verification:**

```bash
python3 tools/tmux_board_snapshot.py --output /tmp/tmux-board-status.json
python3 -m json.tool /tmp/tmux-board-status.json >/dev/null
python3 - <<'PY'
import json
p='/tmp/tmux-board-status.json'
d=json.load(open(p))
assert 'sessions' in d
assert 'panes' in d
print(len(d['sessions']), len(d['panes']))
PY
```

Expected: valid JSON and nonzero session/pane counts.

### Task 2.2: Add a copy-safe board summary helper

**Objective:** Make one command that gives the user a readable board inventory without dragging across panes.

**Files:**
- Create: `tools/tmux_board_summary.py`
- Optional output target: `/Users/duhokim/HermesOps/tmux-copies/latest-board-summary.txt`

**Implementation shape:**
- Consume the JSON from Task 2.1.
- Print one compact line per pane:
  `session:window.pane | role | command | title | active/dead | path`
- Optionally write the same text to clipboard using `pbcopy` only when invoked with `--copy`.

**Verification:**

```bash
python3 tools/tmux_board_snapshot.py --output /tmp/tmux-board-status.json
python3 tools/tmux_board_summary.py /tmp/tmux-board-status.json | sed -n '1,40p'
```

Expected: lines include `ge-mastermind`, `mesh-ge-m1-packet`, `mesh-ge-m2-source`, and `mesh-ge-m3-debate` when those sessions are alive.

### Task 2.3: Optional tmux binding for board summary

**Objective:** Give the user a prefix key to copy board status without pane selection pain.

**Files:**
- Modify only after approval: `/Users/duhokim/.tmux.conf`
- Backup first: `/Users/duhokim/.tmux.conf.bak-YYYYMMDDTHHMMSSZ`

**Candidate binding:**

```tmux
# Copy current board summary to clipboard and file.
# Use: tmux prefix + B
bind-key B run-shell 'cd /Users/duhokim/NebulaMind/NebulaMind && python3 tools/tmux_board_snapshot.py --output /tmp/tmux-board-status.json && python3 tools/tmux_board_summary.py --copy /tmp/tmux-board-status.json && tmux display-message "Copied board summary to clipboard"'
```

**Verification:**

```bash
tmux source-file /Users/duhokim/.tmux.conf
tmux list-keys | grep 'bind-key B run-shell'
```

Expected: binding exists. Manual user test: prefix+B copies a board summary.

### Task 2.4: Optional pane-role hardening

**Objective:** Fill missing `@mesh_role` metadata for long-lived board panes so pane borders are more useful.

**Risk:** This mutates tmux pane options. It is visible but low-risk. Requires approval.

**Candidate read-only preflight:**

```bash
tmux list-panes -a -F '#{session_name}:#{window_index}.#{pane_index}|role=#{@mesh_role}|title=#{pane_title}|cmd=#{pane_current_command}'
```

**Candidate mutation after approval:**

Use exact pane targets only after re-reading current pane list. Examples from the inspection, not commands to run blindly:

```bash
tmux set-option -pt ge-mastermind:0.0 @mesh_role Hwao-director
tmux set-option -pt ge-mastermind:0.1 @mesh_role Goru-director
tmux set-option -pt ge-mastermind:0.2 @mesh_role Tori-director
```

**Verification:**

```bash
tmux list-panes -a -F '#{session_name}:#{window_index}.#{pane_index}|role=#{@mesh_role}|title=#{pane_title}' | grep ge-mastermind
```

Expected: director panes show role names in the pane-border format.

---

## Track 3: Compare iTerm2 tmux control mode safely on macOS

### Task 3.1: Install iTerm2 only with explicit approval

**Objective:** Add the macOS terminal that supports native tmux control-mode integration.

**Gate:** Requires explicit user approval because it installs a GUI app.

**Command after approval:**

```bash
brew install --cask iterm2
```

**Verification:**

```bash
mdfind 'kMDItemCFBundleIdentifier == "com.googlecode.iterm2"'
python3 - <<'PY'
import os, plistlib
for p in ['/Applications/iTerm.app', os.path.expanduser('~/Applications/iTerm.app')]:
    info=os.path.join(p,'Contents','Info.plist')
    if os.path.exists(info):
        d=plistlib.load(open(info,'rb'))
        print(p, d.get('CFBundleIdentifier'), d.get('CFBundleShortVersionString'))
PY
```

Expected: `com.googlecode.iterm2` found.

### Task 3.2: Create a separate tmux sandbox socket

**Objective:** Ensure the iTerm2 comparison cannot attach to or disturb active NebulaMind sessions.

**Command:**

```bash
tmux -L iterm-sandbox new-session -d -s iterm-sandbox -c /Users/duhokim/NebulaMind/NebulaMind
tmux -L iterm-sandbox split-window -h -t iterm-sandbox:0
tmux -L iterm-sandbox send-keys -t iterm-sandbox:0.0 'printf "left sandbox pane\\n"; pwd' Enter
tmux -L iterm-sandbox send-keys -t iterm-sandbox:0.1 'printf "right sandbox pane\\n"; pwd' Enter
tmux -L iterm-sandbox list-panes -a -F '#{session_name}:#{window_index}.#{pane_index}|#{pane_current_command}|#{pane_current_path}|#{pane_width}x#{pane_height}'
```

**Verification:**

```bash
tmux -L iterm-sandbox list-sessions
# and separately:
tmux list-sessions | grep -v iterm-sandbox || true
```

Expected: sandbox session exists only on the `iterm-sandbox` socket; default active sessions are unchanged.

### Task 3.3: Attach iTerm2 to the sandbox with tmux control mode

**Objective:** Test native tabs/splits while preserving tmux persistence.

**Manual command to run inside iTerm2:**

```bash
/opt/homebrew/bin/tmux -L iterm-sandbox -CC attach -t iterm-sandbox
```

**Expected behavior from iTerm2 docs:**
- iTerm2 opens native windows/tabs/panes for tmux windows/panes.
- iTerm2 split/resize/close actions send tmux commands.
- Detach via Shell > tmux > Detach or press escape in the tmux-mode menu.

**Verification from regular Terminal:**

```bash
tmux -L iterm-sandbox list-clients -F '#{client_tty}|session=#{client_session}|control=#{client_control_mode}|width=#{client_width}|height=#{client_height}'
tmux -L iterm-sandbox list-panes -a -F '#{session_name}:#{window_index}.#{pane_index}|#{pane_width}x#{pane_height}|#{pane_title}'
```

Expected: at least one client has `control=1` while iTerm2 is attached.

### Task 3.4: Compare against current board needs

**Checklist:**
- Can the user select/copy a single pane without dragging across columns?
- Do native iTerm2 split panes map cleanly to tmux panes?
- Does `tmux capture-pane` still work from the normal shell?
- Does `tmux send-keys` still work to sandbox panes?
- Does pane resize behave better than current Terminal/tmux with multiple attached clients?
- Does iTerm2 make board observability better enough to justify optional observer use?
- Does it interfere with Hermes/tmux automation assumptions?

**Pass condition:** iTerm2 is useful as an optional observer for humans without replacing tmux as the automation substrate.

**Fail condition:** control-mode changes pane addressing/capture/resize behavior enough to make Tori/Hwao/Goru automation less reliable.

### Task 3.5: Clean up sandbox

**Command:**

```bash
tmux -L iterm-sandbox kill-server
```

**Verification:**

```bash
tmux -L iterm-sandbox list-sessions 2>&1 | sed -n '1,20p'
tmux list-sessions | sed -n '1,80p'
```

Expected: sandbox server gone; default active sessions still present.

---

## Decision rule after 2+3

- Keep the current tmux boards as canonical unless the sandbox proves a better path.
- Prefer Track 2 improvements immediately because they preserve existing automation and solve the user’s copy/visibility pain directly.
- Treat Track 3 as a human-observer experiment, not a migration, until `tmux capture-pane`, `tmux send-keys`, pane roles, and board status JSON all work reliably with control-mode clients.
- Do not use Linux/KDE `futpib/kmux` for this Mac board unless a separate Linux/KDE sandbox is approved.

## Proposed next approval prompt

If the user wants execution now, ask for one of these explicit approvals:

1. `approve track2 helper scripts only` — create `tools/tmux_board_snapshot.py` and `tools/tmux_board_summary.py`, no tmux config changes.
2. `approve track2 tmux binding` — after scripts pass, back up and patch `/Users/duhokim/.tmux.conf` with prefix+B.
3. `approve install iTerm2 sandbox` — install iTerm2 via Homebrew cask and test only `tmux -L iterm-sandbox`.
