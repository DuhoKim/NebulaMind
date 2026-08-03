# Clean final MacBook lid-protected observer — setup (Studio-side done; MacBook-side to install)

Scope: MacBook-side mosh-backed reconnect wrapper + dedicated iTerm profile + one read-only `ge-mastermind` observer + dedupe legacy observers + resilience verification. No repo/DB/deploy/git changes.

## Studio-side (DONE by Hwao-director on the Studio)
- **Deduped legacy observers:** detached 3 stale read-only tmux clients (`ttys033`@13:33, `ttys034`@14:04, `ttys035`@14:05). `ge-mastermind` now has **1 client** (the active read-write control `ttys003`, 265×68). Session persisted (attached=1, 3 windows: Directors / rp1-quality-4h / wiki-quality-4h).
- **mosh present on Studio:** `/opt/homebrew/bin/mosh-server` (mosh 1.4.0). One mosh-server running (backs the live connection; not an orphan).
- **Resilience (Studio side):** the tmux session lives on the Studio and survives every client disconnect — verified (detaching all observers did not affect the session or the mesh). So a closed lid / dropped link never loses state; the observer just re-attaches.

## MacBook-side: (1) mosh reconnect wrapper  →  save as `~/bin/ge-observe` and `chmod +x`
```zsh
#!/bin/zsh
# ge-observe — lid-protected READ-ONLY observer of the Studio ge-mastermind tmux session.
# mosh survives network changes / sleep-wake; this loop re-attaches if the link drops.
set -u
STUDIO_HOST="${GE_STUDIO_HOST:-duho-macstudio.taila27502.ts.net}"   # tailnet name (roams anywhere); or LAN IP / Duhoui-MacStudio.local
STUDIO_USER="${GE_STUDIO_USER:-duhokim}"
SESSION="${GE_SESSION:-ge-mastermind}"
print -P "%F{cyan}[observer]%f READ-ONLY ${SESSION} @ ${STUDIO_USER}@${STUDIO_HOST} (mosh, auto-reconnect). Prefix(Ctrl-b)+d to leave."
while true; do
  mosh --predict=experimental "${STUDIO_USER}@${STUDIO_HOST}" -- tmux attach-session -r -t "${SESSION}"
  rc=$?
  [ $rc -eq 0 ] && { print -P "%F{green}[observer]%f detached cleanly."; break; }
  print -P "%F{yellow}[observer]%f link dropped (rc=$rc); reconnecting in 3s — Ctrl-C to stop."
  sleep 3
done
```
- `tmux attach-session -r` = **read-only** (the observer cannot send keystrokes — cannot fight the keyboard/UC or disturb the board).
- If your mosh build rejects `-- tmux …`, drop the `--` (`mosh host tmux attach-session -r -t ge-mastermind`), or `mosh` in plain and run the attach manually.
- Set `GE_STUDIO_HOST` to the tailnet name for lid-protected roaming, or the LAN IP `168.188.91.189` / `Duhoui-MacStudio.local` on the same network.

## MacBook-side: (2) dedicated iTerm2 profile
iTerm2 → Settings → Profiles → **+** (new):
- **Name:** `GE Mastermind Observer (read-only)`; give it a distinct **badge/color** so it's unmistakable.
- **General → Command:** `Command` → `/Users/<you>/bin/ge-observe` (runs the wrapper instead of a login shell).
- **Session → After a session ends:** `No Action` isn't needed — the wrapper's loop keeps it alive; set **"Prompt before closing"** to *No* so a wake-up reconnect is seamless.
- **Terminal:** leave scrollback generous; the read-only attach won't resize the active control client if you keep this window ≥ the Directors window size.
- (Optional) Keys → make it obvious it's observe-only; the tmux `-r` already blocks input.

## Lid-protected behavior
- **Default (recommended):** closing the lid sleeps the MacBook; the Studio session keeps running; on wake, mosh + the loop **re-attach automatically** — no state lost.
- **Keep observing with the lid closed:** run the wrapper under `caffeinate -s ge-observe` (prevents sleep on AC power). True clamshell-with-lid-shut also needs external power; deeper `pmset` clamshell tweaks need sudo (out of scope here).

## Resilience verification (MacBook side, for you to confirm)
1. Start the observer (iTerm profile) → confirm you see the Directors window, and typing does nothing (read-only).
2. Toggle Wi-Fi off/on (or close+reopen lid) → the loop should reconnect within a few seconds and resume the same view.
3. On the Studio, `tmux list-clients` should then show your one read-only observer + the control client — no legacy duplicates.

## Note (separate, still open)
This observer is read-only by design, so it won't affect the earlier **VNC/Remote-Management exposure** (root `:5900`/`:3283` still listening) — that still needs the MacBook SSH+sudo close-out from the prior relay.
