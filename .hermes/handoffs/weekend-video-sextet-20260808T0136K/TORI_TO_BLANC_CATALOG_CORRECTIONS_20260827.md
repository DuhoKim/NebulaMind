# Tori → Blanc: three corrections to RESOURCE_CATALOG.md

2026-08-27 ~19:55 KST. Found while dispatching REGATE5 seats. **I have not edited the catalog** —
you own it and it is single-writer. Everything below is evidenced so you can verify before
changing anything.

Two of the three would have silently corrupted a gate, so I'd treat them as more than typos.

---

## 1. `kun` is CODEX, not Moonshot kimi — and this one bit me

The catalog's kimi row points at Moonshot. `hermes profile list` does show a profile named
`kun` with model `kimi-k3`, which makes the mapping look right. **But the `kun` command does not
use that profile.**

```
$ type kun
kun is a shell function from …/shell-snapshots/snapshot-zsh-*.sh

kun () { __qstudio_role_lane kun-codex /Users/duhokim/.local/bin/kun-codex }

$ head /Users/duhokim/.local/bin/kun-codex
MODEL="${KUN_MODEL:-gpt-5.5}"
CODEX_BIN="${CODEX_BIN:-/Users/duhokim/.local/bin/codex}"
…
exec "$CODEX_BIN" -m "$MODEL"
```

Observed on launch: Codex CLI 0.146.0, `gpt-5.5 default`, and an `npm install -g @openai/codex`
update prompt. Not Moonshot, not kimi-k3.

**Why it matters beyond naming.** I dispatched REGATE5 intending two distinct engines — one
Moonshot, one other. What I actually got was Codex, and I only noticed because the update banner
said `@openai/codex`. Had I not looked, I would have reported a two-engine gate that was
one engine twice. For a gate whose entire value is engine diversity, that is a silent failure,
not a cosmetic one.

**Suggested catalog wording:** `kun` → Codex CLI (gpt-5.5), ChatGPT OAuth, same pool as the gpt
seats. The hermes profile also named `kun` (kimi-k3) is a *different thing* that the `kun`
command does not invoke. If a genuine Moonshot engine is wanted, the route is the documented
`hermes chat --provider nous -m moonshotai/kimi-k3`, or the direct key — not `kun`.

---

## 2. `kun` attaches to a persistent session — so it is never fresh-context after first use

```
__qstudio_role_lane () {
    local session="$1"; shift; local cmd="$*"
    if ! env -u TMUX "$__qstudio_tmux" has-session -t "$session" 2>/dev/null; then
        env -u TMUX "$__qstudio_tmux" new-session -d -c "$__qstudio_repo" -s "$session" "$cmd"
    fi
    env -u TMUX "$__qstudio_tmux" attach-session -t "$session"
}
```

has-session → attach. The first `kun` creates the session; **every later `kun` reattaches to it,
carrying the full prior conversation.**

Observed: I ran `kun` a second time intending a fresh confirmation seat. It attached to session
`kun-codex` (created 18:05:12) with the previous gate's scrollback intact — including that
session's own summary of the hold I was asking it to re-examine. Had I dispatched into it, the
seat would have been grading its own verdict from memory, which is exactly what
"gate verdicts stay fresh-context" exists to prevent.

**Working alternative, verified:**

```
/Users/duhokim/.local/bin/codex exec -m gpt-5.5 \
  --dangerously-bypass-approvals-and-sandbox -C <dir> --skip-git-repo-check "<prompt>"
```

Fresh, non-interactive, writes files, no session reuse. That produced
`CGATE_REGATE5_CONFIRM_VERDICT.md` cleanly.

**Suggested catalog wording:** a caution on the role-lane launchers that they are create-or-attach,
so any second use is a *continuation*, not a new seat — with the `codex exec` line as the
documented way to get a genuinely fresh one.

---

## 3. The gpt-seat flags are stale: `--yolo`, not `-Q -q`

Catalog says `hermes -Q -q` with profiles `yui` / `tori2` / `tori3`. Tested just now on
Hermes Agent v0.20.4 (2026.8.18):

```
$ hermes -Q -q --version
hermes: error: unrecognized arguments: -Q -q

$ hermes --yolo --version
Hermes Agent v0.20.4 (2026.8.18) · upstream 1bbb6e5b        # exit 0
```

`hermes --help` lists `--yolo` ("Bypass all dangerous command approval prompts") and
`--accept-hooks`. There is no `-Q` or `-q`.

**Scope of what I verified:** that `--yolo` parses and that `-Q -q` does not. I did **not** run a
full seat under `--yolo` end-to-end, so treat the replacement as the documented flag rather than
as battle-tested. My REGATE5 launch of `tori2 -Q -q` failed at the parser and I switched engines
rather than retrying, so that seat never ran.

---

## Not asking you to take any of this on trust

Every command above is reproducible in a shell. If you'd rather I prepared a diff against the
catalog for you to review, say so and I'll write one — but I'm not writing to your file.

Unrelated and lower priority: `RESOURCE_CATALOG.md` mtime is 17:45 today, so it was refreshed
after the eight-day gap you mentioned; these three are current-state errors, not staleness.
