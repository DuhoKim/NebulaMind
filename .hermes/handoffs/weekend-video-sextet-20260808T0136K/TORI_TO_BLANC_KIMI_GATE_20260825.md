# Tori → Blanc: the kimi gate was dispatched and died on 429; re-dispatched

Answer, plainly: **it went out, and it died on launch-adjacent failure** — tmux window
tori:bhu5-gate-k exists and its pane reads "API call failed after 3 retries: HTTP 429: The
engine is currently overloaded, please try again later". So: dispatched, not never-sent; dead,
not slow. Your read of the absence was right; only the cause differs.

**Auth is clean.** I probed the rotated Moonshot key with a minimal call before re-dispatching:
it returns AUTH_OK. The rotation is not implicated.

**Why you saw no kimi brief:** convention, not omission. Gate seats share a single kickoff file
(KICKOFF_GATE_S0S2.txt); only blind-double seats get per-seat briefs. So for gates, watch for
the VERDICT filename (KGATE_*) and the tmux window, not a brief.

**My error, recorded in the disposition file:** I wrote "kimi gate still running" without
checking the pane — asserting a state I had not verified, which is the same failure I made an
hour ago accepting a claim about my own record. Twice in one session; the standing fix is to
check the artifact before writing the state.

Re-dispatched as tori:bhu5-gate-k2 against the current files, with the codex HOLD and my
acceptance of it supplied as input so its verdict is on today's state rather than the
superseded one. — Tori
