# Hwao brief — overnight Deep Research report + private dashboard update

User direction: "overnight report and update the dashboard"

Target surface: existing private tailnet dashboard only:
- `https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html`
- renderer: `tools/render_ge_autopilot_dashboard_v2.py`

Verified current state:
- dashboard and status JSON return HTTP 200;
- renderer watcher and shared usage monitor are both running;
- current overnight panel is stale (`GE_AUTOPILOT_OVERNIGHT_REPORT_20260712`) and contains no Deep Research outcome;
- public rich Baseline cockpit guard passes and must remain untouched.

Please coordinate the content decision and write one short directive report:
`HWAO_DASHBOARD_DIRECTION.md`
in this directory, ending with exactly:
`HWAO_OVERNIGHT_DASHBOARD_DIRECTION_DONE_20260713T004424Z`

Directive must specify:
1. plain-English headline and actual result for the C1r Deep Research overnight investigation;
2. compact card titles/statuses/details to replace the stale overnight cards;
3. exact next action and held work;
4. current safety boundary;
5. whether an active approval phrase is warranted (default: none);
6. the unique dashboard marker to publish.

Facts that must not be distorted:
- C1r remains `FAIL_CLOSED`; no retro-acceptance and no retry;
- corrected accounting: 41 capture-caused findings, 4 validator false positives, 8 genuine model violations, 1 mixed/genuine C7 finding with inflated evidence, plus 6 additional Section-2 citation defects missed by the validator;
- primary root cause: extractor ignored Gemini `source-footnote` / `data-turn-source-index` citation chips;
- 108 chips existed; 12 ledger sources were truly orphaned; 9 duplicate rows; 46 blank short-name fields;
- next safe work is chip-aware capture + validator TDD + offline re-adjudication before any new live canary;
- scientific/source-level review remains unresolved;
- no browser, Gemini, network, DB, deploy, git, cron, provider-account, or public Baseline action occurred in the investigation.

Scope: content direction only. Do not edit the renderer, generated private dashboard files, public cockpit, product code, DB, deploy/restart, git, or live services. Tori will perform the bounded renderer update, validation, backup, private-watcher refresh if needed, and route verification.
