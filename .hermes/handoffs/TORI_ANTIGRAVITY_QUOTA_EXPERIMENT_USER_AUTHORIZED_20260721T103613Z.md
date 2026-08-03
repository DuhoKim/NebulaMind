# Tori relay: user-authorized Antigravity quota experiment

Recorded: 2026-07-21T10:36:13Z

User direction: "you can waste some, go ahead with your experiments"

Tori interpretation and bounded plan:

1. Preserve the current `/usage` baseline for Gemini weekly/5h and Claude-GPT weekly/5h.
2. Send one no-tools exact-token request through the authenticated AGY/Garu pane using Gemini 3.1 Pro (High).
3. Observe `/usage` through the existing safe monitor immediately and after backend settlement.
4. Send at most one no-tools request through the Claude/GPT pool only if needed to distinguish pool behavior.
5. Stop on any quota error, account/login/verification prompt, billing/overage surface, unexpected tool loop, or target drift.

Closed surfaces: no files beyond this relay/experiment receipt, no browser, no API/GCP/billing change, no DB, no deploy/restart, no git write, no cron, no publication.

Hwao relay note: canonical and alternate Hwao panes contained unsubmitted user drafts at dispatch time, so Tori did not overwrite or submit them. The user explicitly directed Tori to conduct this bounded experiment.

Marker: `TORI_ANTIGRAVITY_QUOTA_EXPERIMENT_USER_AUTHORIZED_20260721T103613Z`

## Verified results

- Baseline at `2026-07-21T10:35:15Z`: Gemini weekly/5h and Claude-GPT weekly/5h all displayed `Quota available`.
- QP1 used Gemini 3.1 Pro (High), no tools, and returned the exact requested token `QUOTA_PROBE_GEMINI_OK`.
- Immediate post-QP1 `/usage`: Gemini weekly `100.00%` remaining with a 163h23m reset; Gemini five-hour `99.97%` remaining with a 4h59m reset.
- QP2 used Claude Sonnet 4.6 (Thinking), no tools, and returned `QUOTA_PROBE_CLAUDE_OK`.
- Immediate post-QP2 `/usage`: Claude-GPT weekly `99.94%` remaining with a 167h59m reset; Claude-GPT five-hour `99.70%` remaining with a 4h59m reset.
- AGY 1.1.2 and 1.1.5 showed the same backend values. The temporary 1.1.5 probe session was removed after capture.
- The existing monitor propagated numeric state at `2026-07-21T10:40:31Z`, proving the qualitative state transitions after first use.

Conclusion: `Quota available` is the full/untouched bucket state in this observed account. The first charged request activates the precise percentage and reset clock for that model group.

The experiment also exposed a parser defect: the precise bar regex omitted the literal `%`, so the monitor fell back to Antigravity's rounded text line. A focused TDD fix now preserves the precise bar values and shows two decimals for nonzero usage below 0.1%. Verification: 14 focused quota/pane tests pass; the broader provider set has 74 passes and four unrelated pre-existing Gemini-consumer staleness-window failures; the renderer set has seven passes and one unrelated pre-existing stale overnight-marker failure.

## Runtime activation

The user separately approved the provider-monitor restart. Pre-restart PID `8988` was backed up and replaced only in tmux pane `%266` by PID `24001`, preserving `--watch --interval 60 --slash-interval 300`. No other process or renderer was restarted.

Live verification at `2026-07-21T10:49:01Z` showed Gemini five-hour `0.03% used · 99.97% remaining`, Claude-GPT weekly `0.06% used · 99.94% remaining`, and Claude-GPT five-hour `0.3% used · 99.7% remaining`. Both public cockpit mirrors remained byte-identical, retained all protected rich markers and `NO ACTIVE EXECUTION PHRASE`, and the served dashboard JSON returned HTTP 200 with the new readings.

Backup: `/Users/duhokim/HermesOps/backups/provider-usage-monitor-precision-restart-20260721T104845Z`
