# Duho correction — private cockpit still lacks many usage limits

- Marker: `DUHO_COCKPIT_USAGE_LIMIT_COVERAGE_CORRECTION_20260810T1727K`
- Recorded: 2026-08-10 17:27 KST
- User feedback, verbatim: `so Hwao worked on the cockpit dashboard, but still, it lacks many usage limits`
- Target: private Tailnet dashboard `https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html`.

## Immediate interpretation

The current quota/usage area is not complete merely because existing cards are fresh. Treat this as a coverage defect: inventory the actual served cards and all active or operationally relevant provider/product limit pools, then identify each missing pool and why it is absent.

Do not manufacture percentages, collapse distinct meters, or relabel context-window use as provider quota. For each pool, distinguish fresh live meter, stale historical observation, unavailable/unknown meter, and planning envelope. State the billing/subscription source clearly.

## Gate for this turn

Hwao coordinates. Tori performs read-only source/process/served-JSON inventory first. No generated-HTML hand edit, watcher restart, public monitor write, account/billing/API/credits/OAuth page access, browser capture, provider call, DB/wiki/deploy/Git/cron/config/secret action is authorized by this correction alone. Hwao should issue an exact-diff coverage order after the inventory identifies the missing limits and their sanctioned data sources.
