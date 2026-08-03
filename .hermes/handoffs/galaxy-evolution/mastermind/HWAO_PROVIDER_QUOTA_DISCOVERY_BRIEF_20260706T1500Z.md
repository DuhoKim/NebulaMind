# Hwao provider quota discovery brief

Marker: HWAO_PROVIDER_QUOTA_DISCOVERY_BRIEF_20260706T1500Z

User request:
- Work with Hwao to get quota from Codex and Gemini/Antigravity.

Tori role:
- Relay/recorder/verifier.
- Execute only bounded non-secret read-only checks explicitly in this brief or later directed by Hwao/user.

Goal:
- Get non-secret quota/usage evidence for:
  1. Codex / Kun route.
  2. Gemini / Antigravity / Goru route.
- Prefer visible provider UI/TUI quota displays over generic docs.
- If numeric quota is not visible, record that plainly; do not guess.

Allowed actions:
- Read visible tmux pane status/output.
- Ask visible Codex/Kun lanes to show `/usage` or equivalent non-mutating usage view if the CLI/TUI supports it.
- Ask visible Gemini/Antigravity/Goru lanes to show `/stats`, `/usage`, tier/credit display, or equivalent non-mutating usage view if the TUI supports it.
- Inspect local non-secret config metadata only when needed to distinguish OAuth/subscription route from API-key/GCP route. Do not print tokens/secrets.
- Write receipts/reports under this mastermind handoff root.
- Update the main cockpit only after quota evidence is verified and only through stable_cockpit_guard renderer workflow.

Hard stops:
- No API keys, OAuth codes, refresh/access tokens, cookies, payment screens, billing settings, GCP project changes, Vertex/API enablement, cloud mutation, account changes, or secrets.
- No Gemini/GCP/API billing-heavy call just to discover quota.
- No DB writes, SQL, migrations, trust recompute, deploy, restart, live wiki/page_versions publish, git commit/push/merge, production write, or cross-method overwrite.
- Stop on login, 2FA, CAPTCHA, payment, API-key, GCP project, billing, or permission uncertainty.

Expected Hwao output:
- Write a concise report at:
  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_PROVIDER_QUOTA_DISCOVERY_REPORT_20260706T1500Z.md
- Include:
  - Codex evidence: exact non-secret quota/reset/usage numbers shown, command/pane/source, timestamp, or `not visible`.
  - Gemini/Antigravity evidence: exact non-secret quota/tier/credit/usage numbers shown, route source, timestamp, or `not visible`.
  - Whether each value is a provider quota, reset count, local context gauge, or unknown.
  - Whether it is safe to update the cockpit gauges.

Suggested lane instructions:
- Codex/Kun: show `/usage` or equivalent non-secret usage screen; do not run code-writing tasks.
- Gemini/Antigravity/Goru: show `/stats`, `/usage`, or equivalent Antigravity/Gemini quota/tier display if available; do not use API key/GCP billing routes.

Current caveats from prior cockpit:
- Codex/Kun previously showed `4 resets visible`, but no normalized percent.
- Gemini/Goru previously showed `Gemini 3.1 Pro (High)`, but no numeric quota.
- Tori/Hermes currently has provider gauges but those are display-only and should be corrected if Hwao obtains better evidence.
