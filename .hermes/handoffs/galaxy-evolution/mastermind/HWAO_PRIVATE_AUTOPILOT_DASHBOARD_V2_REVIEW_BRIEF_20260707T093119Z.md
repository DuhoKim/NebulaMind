# Hwao private autopilot dashboard V2 review brief

Marker: `HWAO_PRIVATE_AUTOPILOT_DASHBOARD_V2_REVIEW_BRIEF_20260707T093119Z`
User request: "can you upgrade the dashboard?"
Scope: private tailnet-only `/Users/duhokim/HermesOps/cockpit/ge-autopilot.html`; do not touch public NebulaMind cockpit/Baseline.

## Requested Hwao role

Review the upgraded dashboard design direction, not implementation. The builder/Tori will implement and verify.

## V2 upgrade goals

1. Preserve the V1 safety frame:
   - private tailnet mirror;
   - read-only browser page;
   - no DB/API/live publish/deploy/git/cloud/secrets/cron/browser action surface;
   - no public NebulaMind cockpit/Baseline replacement.
2. Make the dashboard easier to read from a MacBook at home:
   - bigger hero answer: does anything need me?
   - clearer freshness/staleness state;
   - visible director/method lane map;
   - plain-English next action if blocked vs clean;
   - no need to navigate Goru's TUI.
3. Add richer observability:
   - role/lane summaries;
   - latest autopilot event ticks/actions/blockers from local JSONL log;
   - per-lane status counts;
   - safety policy legend.
4. Avoid control-looking UI:
   - no approve/run/publish/execute buttons;
   - informational links/text only;
   - any browser JS only fetches local JSON and updates DOM.

## Expected receipt

Write a concise design receipt at:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_PRIVATE_AUTOPILOT_DASHBOARD_V2_REVIEW_20260707T093119Z.md`

Include PASS or PATCHES with exact requested changes. Stop after writing the receipt.
