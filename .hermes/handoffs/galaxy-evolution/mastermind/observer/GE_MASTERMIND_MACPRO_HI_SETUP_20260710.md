# Mac Pro (Intel) — mirror the `hi` features (mosh interactive ge-mastermind + one-client lock + reconnect + iTerm profile)

Mirrors the MacBook `hi` setup, adapted for **Intel Homebrew** (`/usr/local`). Local config only — no repo/DB/deploy/git.
Faithful to the Studio source `~/.local/bin/install-tori-mosh-aliases` (its `__tori_mosh_client` already falls back to `/usr/local/bin/mosh`, and the Studio-side `/opt/homebrew/bin/{tmux,mosh-server}` paths are the *remote* paths, unchanged).

## Prereqs on the Mac Pro
1. **Intel Homebrew mosh:** `brew install mosh` → installs to `/usr/local/bin/mosh` (auto-detected by the block below).
2. **ssh `studio` host** in `~/.ssh/config` (same as the MacBook), e.g.:
   ```
   Host studio
     HostName duho-macstudio.taila27502.ts.net   # tailnet (roams); or LAN IP 168.188.91.189 / Duhoui-MacStudio.local
     User duhokim
     ServerAliveInterval 15
     ServerAliveCountMax 40
     TCPKeepAlive yes
   ```

## (1) Shell block — paste into `~/.zshrc` on the Mac Pro, then `source ~/.zshrc`
Self-contained (base `h/hm` family + the new `hi` ge-mastermind interactive/lock/reconnect). Intel client mosh auto-detected; Studio remote paths kept.
```zsh
# >>> tori-numbered-mosh-lanes + hi >>>
: ${__hermes_studio_host:=studio}
: ${__hermes_studio_tmux:=/opt/homebrew/bin/tmux}          # remote (Studio, Apple Silicon) — do NOT change to /usr/local
: ${__hermes_studio_hermes:=/Users/duhokim/.local/bin/hermes}
: ${__hermes_studio_mosh_server:=/opt/homebrew/bin/mosh-server}   # remote (Studio) mosh-server

__tori_safe_term() { case "${TERM:-xterm-256color}" in xterm-ghostty|dumb|unknown) printf '%s' 'xterm-256color';; *) printf '%s' "$TERM";; esac; }
__tori_mosh_client() {
  command -v mosh >/dev/null 2>&1 && { command -v mosh; return 0; }
  [ -x /usr/local/bin/mosh ]  && { printf '%s\n' /usr/local/bin/mosh;  return 0; }   # Intel Homebrew
  [ -x /opt/homebrew/bin/mosh ] && { printf '%s\n' /opt/homebrew/bin/mosh; return 0; }
  return 1
}
__hermes_mosh() {  # $1 = tmux subcommand string (e.g. "attach-session -d -t ge-mastermind")
  local mb; mb="$(__tori_mosh_client)" || { echo 'mosh not installed. Intel macOS: brew install mosh (-> /usr/local/bin/mosh).' >&2; return 127; }
  TERM="$(__tori_safe_term)" MOSH_TITLE_NOPREFIX=1 \
    "$mb" --server="$__hermes_studio_mosh_server" \
      --ssh="ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=40 -o TCPKeepAlive=yes" \
      -- "$__hermes_studio_host" "$__hermes_studio_tmux" ${=1}
}

# base lanes (same as MacBook): hm -> hermes-main over mosh; h -> same over ssh
hm() { __hermes_mosh "new-session -A -s hermes-main $__hermes_studio_hermes"; }
h()  { ssh -tt "$__hermes_studio_host" "$__hermes_studio_tmux new-session -A -s hermes-main $__hermes_studio_hermes"; }

# hi -> INTERACTIVE ge-mastermind attach, ONE-CLIENT LOCK (-d detaches other clients), auto-reconnect
hi() {
  echo "[hi] interactive ge-mastermind @ $__hermes_studio_host (mosh; one-client lock; auto-reconnect). Ctrl-b d to leave." >&2
  while true; do
    __hermes_mosh "attach-session -d -t ge-mastermind"
    local rc=$?
    [ $rc -eq 0 ] && { echo '[hi] detached cleanly.' >&2; break; }
    echo "[hi] link dropped (rc=$rc); reconnecting in 3s — Ctrl-C to stop." >&2
    sleep 3
  done
}
# <<< tori-numbered-mosh-lanes + hi <<<
```
- `attach-session -d -t ge-mastermind`: **interactive** (read-write control) + **`-d` = one-client lock** — attaching detaches any other client, so the Mac Pro becomes the sole control client (prevents the stale-duplicate build-up we just cleaned up).
- The reconnect `while` loop re-moshes if the link drops (network change / sleep-wake); mosh itself already survives roaming.

## (2) Dedicated iTerm2 profile (Mac Pro)
iTerm2 → Settings → Profiles → **+**:
- **Name:** `GE Mastermind — hi (Mac Pro control)`; distinct badge/color.
- **General → Command → `Command`:** `/bin/zsh -ic hi` (loads your zshrc so the `hi` function exists, then runs it). Alternatively `Login shell` and just type `hi`.
- **Session → "Prompt before closing": No** (seamless wake-up reconnect).
- Generous scrollback.

## Resilience verification (run on the Mac Pro)
1. `source ~/.zshrc && hi` → you should land in `ge-mastermind` (Directors window), interactive.
2. Because of `-d`, other clients get detached — from the Studio `tmux list-clients` should show your Mac Pro as the one client on ge-mastermind.
3. Toggle Wi-Fi / close+reopen lid → the loop reconnects within a few seconds to the same session.

## One-client-lock caveat (important)
`hi` uses `-d`, so **whenever the Mac Pro runs `hi` it detaches the MacBook (and any other) client** from ge-mastermind — that's the "one-client lock." If you want the MacBook read-only observer *and* the Mac Pro control up at the same time, drop `-d` on the Mac Pro (`attach-session -t ge-mastermind`) so they coexist — but then it's no longer a single-client lock. Pick per how you want the two machines to share the session.

## From the Studio (me), for reference
The base `~/.local/bin/install-tori-mosh-aliases` is Intel-portable already; this doc's block is the self-contained equivalent + the `hi`/ge-mastermind/lock/reconnect additions, so you can just paste it on the Mac Pro without copying the script. I can't reach the Mac Pro from the Studio to install it for you.
