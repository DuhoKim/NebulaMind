# Question for Tori (relay from Duho, via Fable/Claude-Code session)

Duho asks: **on the Mac Studio (`Duhoui-MacStudio.local`), what did you turn off in the Sharing settings?**

Answer from receipts only. If you have no record of an action, say so plainly rather than inferring it.

## For each service, state: OFF or ON, when (UTC), why, and the receipt path

1. **Screen Sharing** — `com.apple.screensharing`, TCP 5900
2. **Remote Login / sshd** — TCP 22
3. **Remote Management / ARD** — TCP 3283

## Observed state on the Studio right now (2026-07-10, verified by Fable)

- `sshd` **LISTENING** on `*:22`, `PasswordAuthentication no`, 0 failed auths in 24h
- TCP `5900` **closed**; `com.apple.screensharing` => `disabled` at launchd
- TCP `3283` **closed**
- Firewall enabled, block-all off; Mac is **not** MDM-enrolled

So on the Studio, Remote Login appears never to have been disabled, and Screen Sharing / ARD are off.

## The specific contradiction to resolve

`.hermes/handoffs/galaxy-evolution/mastermind/observer/GE_MASTERMIND_OBSERVER_SETUP_20260710.md`, line 50, says:

> This observer is read-only by design, so it won't affect the earlier **VNC/Remote-Management exposure** (root `:5900`/`:3283` still listening) — that still needs the MacBook SSH+sudo close-out from the prior relay.

Please confirm:

- **Which host** does that exposure refer to — the MacBook, the Studio, or both?
- Was there ever a `:5900`/`:3283` exposure **on the Studio**, and did you close it?
- Is the MacBook close-out **still outstanding**?
- Where is the receipt for the original finding? Nothing in-repo records it; only this downstream reference survives.

## Context you should know

Your session `20260710_202749_df8d81` was terminated at 23:11:40 UTC because I (Fable) sent a long free-text string into your pane with `tmux send-keys` **without the `-l` literal flag**. tmux parsed it as ~97 key-name arguments and hermes shut down. That was my error, not yours, and not a security event. Goru restarted you. The 48h research sprint (pids 2126, 45665) was unaffected and kept running.
