# Fresh-process handoff — Deep Research computer-use recovery

Parent packet: `gemini-dr-content-expert-gate-20260713T160239Z`
Role: fresh Tori execution process; sole browser owner after this handoff
Status: packet remains NOT ARMED

## Why this process exists

The parent Hermes process completed Hwao/Goru/Tori local preflight but its `computer_use` bridge returned zero apps and `0x0` captures. `hermes computer-use doctor` was fully GREEN. The user explicitly asked Tori to resume without closing the current window. This detached tmux process is the fresh-process recovery; do not create another browser owner.

## Read before acting

Read, in order:

1. `USER_DIRECTION_AND_BOUNDARIES.md`
2. `HWAO_ONE_CANARY_PLAN.md`
3. `HWAO_PREFLIGHT_CORRECTION.md`
4. `preflight/GORU_PREFLIGHT.md`
5. `preflight/TORI_PREFLIGHT_RECEIPT.md`
6. `preflight/TORI_COMPUTER_USE_DIAGNOSTIC.md`
7. `prompt/GE_COMPARABILITY_CANARY.md` and its `.sha256`

## Exact execution scope

1. Retry `computer_use list_apps`, Google Chrome capture, and screen capture from this fresh process.
2. If captures remain empty, keep NOT_ARMED, write `preflight/TORI_FRESH_PROCESS_DIAGNOSTIC.md`, and stop. Do not use an isolated managed browser, API, alternate profile, login workaround, or unpinned fallback.
3. If captures work, proceed exactly under Hwao's single-browser-owner plan:
   - one authenticated Gemini tab/conversation;
   - verify Deep Research mode, highest available model, and any max-thinking control;
   - verify current quota/usage and every hard stop;
   - pin exact tab identity and write pre-submit metadata/screenshots;
   - verify frozen prompt hash `4d57fd71b49e74760cc1be1acc6fb50ce1e777b4c43907612830b346b471f42a` and composer equality;
   - replace NOT_ARMED with one ARMED marker only after every check is GREEN;
   - submit once and start once; no retry, no duplicate tab, no follow-up steering except the one plan-permitted neutral continue on visible truncation;
   - capture and validate exactly as Hwao specified.
4. On verification wall, unusual traffic, CAPTCHA, login, billing/upsell, quota ≥80%, wrong mode/model, uncertain tab, or any doubt: stop fail-closed and record the blocker.
5. No DB, wiki/product/trust mutation, publication, dashboard edit, git write, deploy/restart, cron, billing/OAuth/account action, quarantine release, or prose application.

The user's fresh direction is sufficient for this bounded resume; do not ask for another scope approval unless a hard stop occurs.

Write all receipts only inside this packet. End your final pane response with standalone `TORI_FRESH_PROCESS_DR_RESUME_DONE` or `TORI_FRESH_PROCESS_DR_RESUME_BLOCKED`.
