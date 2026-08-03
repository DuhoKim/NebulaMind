# HWAO_DASHBOARD_DIRECTION — overnight C1r report → private dashboard content

Scope: content direction only, per `HWAO_DASHBOARD_BRIEF.md`. Hwao edits nothing live: no renderer, generated dashboard, public cockpit, product code, DB, deploy/restart, git, cron, browser, or network action. Tori performs the bounded renderer update, validation, backup, private-watcher refresh if needed, and route verification. Target surface: private tailnet dashboard only (`/cockpit/ge-autopilot.html` via `tools/render_ge_autopilot_dashboard_v2.py`); the public rich Baseline cockpit stays untouched.

## 1. Headline + actual result (plain English)

**Headline:** "C1r Deep Research canary stays rejected — but most of the 54 failures were ours, not Gemini's."

**Actual result:** The overnight root-cause investigation (sealed packet `gemini-dr-revised-canary-20260712T045317Z`, report `HWAO_ROOT_CAUSE.md` + `TORI_ROOT_CAUSE_CORRECTED.md`, convergent) found the capture extractor ignored Gemini's `source-footnote` / `data-turn-source-index` citation chips. 108 chips existed in the rendered DOM at per-unit granularity. Corrected accounting of the 54 reported failures: **41 capture-caused, 4 validator false positives, 8 genuine model violations, 1 mixed/genuine C7 finding with inflated evidence** — plus **6 additional Section-2 citation defects the validator missed**. Real residual defects: Section-2 result-cell citations, unlabeled comparisons, and ledger hygiene (12 truly orphaned sources, 9 duplicate rows, 46 blank short-name fields). **C1r remains FAIL_CLOSED: no retro-acceptance, no retry.** Scientific/source-level review remains unresolved; all URLs stay quarantined.

## 2. Replacement overnight cards (replace stale `GE_AUTOPILOT_OVERNIGHT_REPORT_20260712` panel)

| # | Card title | Status | Detail (one line) |
|---|---|---|---|
| 1 | C1r Deep Research canary | **FAIL_CLOSED (unchanged)** | Rejected 2026-07-12T07:22Z; no retry, no retro-acceptance; sealed packet immutable |
| 2 | Root cause | **DIAGNOSED** | Extractor read only `a[href]`; Gemini cited via source-footnote chips (108 in DOM) — 41/54 findings capture-caused |
| 3 | Corrected accounting | **RE-ADJUDICATED** | 41 capture / 4 validator FP / 8 genuine / 1 mixed C7 (evidence inflated); +6 Section-2 citation defects validator missed |
| 4 | Genuine model defects | **CONFIRMED, BOUNDED** | Section-2 result-cell citations (8), 6 unlabeled comparisons, ledger: 12 orphans · 9 duplicate rows · 46 blank short names |
| 5 | Next safe work | **QUEUED — OFFLINE ONLY** | Chip-aware capture → validator TDD → offline re-adjudication of sealed capture; new live canary HELD |
| 6 | Science review | **UNRESOLVED** | No source-level/semantic verification performed; all cited URLs remain QUARANTINED_PENDING_LOCAL_CHECK |

## 3. Exact next action and held work

**Next action (only):** Tori applies this content to the private dashboard via the bounded renderer update, with validation, backup, private-watcher refresh if needed, and route verification (dashboard + status JSON HTTP 200).
**Queued after that (offline, new packet, in order):** chip-aware capture upgrade → validator TDD (RED = sealed C1r capture, GREEN = realistic fixture) → offline re-adjudication of the sealed capture.
**Held:** any new live Gemini run or retry (requires a fresh, separate Duho approval in a new packet); contract r3 finalization until after offline re-adjudication; any public Baseline cockpit change; any provider-account/quota action.

## 4. Current safety boundary

Investigation was offline/local-only: no browser, Gemini, network, DB, deploy, git, cron, provider-account, or public Baseline action occurred, and none is authorized by this directive. Sealed packets remain immutable. The dashboard update is content-only on the existing private tailnet surface; the public cockpit guard must keep passing. Fail-closed posture stands everywhere.

## 5. Approval phrase

**None warranted (default holds).** Nothing is armed, nothing needs an active approval phrase on the dashboard. Any future live canary gets its own fresh Duho approval in its own packet — not via a standing phrase.

## 6. Unique dashboard marker to publish

`GE_AUTOPILOT_OVERNIGHT_REPORT_20260713T004424Z_DR_C1R_ROOT_CAUSE`

(Replaces the stale `GE_AUTOPILOT_OVERNIGHT_REPORT_20260712` marker; unique per this directive's timestamp.)

HWAO_OVERNIGHT_DASHBOARD_DIRECTION_DONE_20260713T004424Z
