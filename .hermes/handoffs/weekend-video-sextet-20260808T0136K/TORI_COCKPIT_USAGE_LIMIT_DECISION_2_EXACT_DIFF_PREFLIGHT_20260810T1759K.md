# Decision 2 exact-diff preflight — usage-limit coverage and Moonshot wallet resolution

- Marker: `TORI_COCKPIT_USAGE_LIMIT_DECISION_2_EXACT_DIFF_PREFLIGHT_20260810T1759K`
- State: `PREPARED_ONLY_NOT_EXECUTED`
- Amended: 2026-08-10 18:04 KST with Duho's same-endpoint/headline trace
- Authority chain:
  - `DUHO_COCKPIT_USAGE_LIMIT_COVERAGE_CORRECTION_20260810T1727K`
  - `TORI_COCKPIT_USAGE_LIMIT_COVERAGE_INVENTORY_20260810T1733K`
  - `HWAO_USAGE_MONITOR_APPROVAL_FRAME_20260810T1740K`, Decision 2
  - Duho's authoritative Moonshot correction received 2026-08-10: `"$33.3 is the available balance."`
  - Duho's same-endpoint trace: the live and stale cards both read `api.moonshot.ai/v1/users/me/balance`; the duplicate is one wallet observed five days apart, not two budgets.
- Runtime/source patch applied: **NO**
- Tests/build run: **NO**
- Deploy/restart/public write/Git action: **NO**
- Active execution phrase: `NO ACTIVE EXECUTION PHRASE`

## Decision 2 result required

The private renderer must keep every operational usage pool visible through collector outages. Each meter must be one of exactly:

- `FRESH LIVE METER`
- `STALE HISTORICAL OBSERVATION`
- `UNAVAILABLE / UNKNOWN`
- `PLANNING ENVELOPE`

A fresh wrapper timestamp must not freshen an inherited card. A missing value must not become zero. Stale cards remain visible, but stale percentages cannot count as current routing headroom.

This preflight also resolves Moonshot/Kimi to **one wallet and one current budget**, not two cards or two apparent budgets.

## Bound current source

- Primary renderer: `tools/render_ge_autopilot_dashboard_v2.py`
- Bound SHA-256: `a246d502b0af1a494460b10a43bb4aa9692f3cf2dba855ecd2c9a6f24bceead4`
- Current private status path: `/Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json`
- Current private renderer: PID 31235, 20-second render loop; restart is not part of this preflight.
- Approved provider monitor is already a separate Decision 1 input. Decision 2 must not add another provider/account/browser call.

Secondary source proposed for semantic correction:

- `tools/moonshot_balance_usage.py`
- Current function: `fetch_gauge()`
- Purpose: stop percent-of-local-peak from masquerading as an exact provider quota percentage while retaining the real dollar balance.

Focused tests proposed:

- Extend `tools/tests/test_provider_usage_quota_parsing.py`, bound SHA-256 `b68d0d32b3c886118c60ffe77f178186cf9116bb25b78ee12665ef3fa354f00d`, for Moonshot classification semantics.
- Add a focused private-renderer usage-snapshot test for stale visibility, per-card age, deduplication, headline values, and meter separation.

No generated HTML is a patch target.

## Authoritative Moonshot resolution — operationally material

Canonical pool identity:

- `pool_id`: `moonshot_kun_kimi_k3_wallet`
- Provider/product: Moonshot direct-key wallet used by Kun's Kimi K3 lane
- Current authoritative classification: `FRESH LIVE METER`
- Live observation used for this correction: `2026-08-10T08:47:22Z`
- Available: **$33.30**
- Cash: **$33.30**
- Voucher: **$0.00**
- Pricing metadata: **$3 per million input tokens; $15 per million output tokens**
- Peak observed: **$94.66**

The peak comparison is a `PLANNING ENVELOPE`, not provider-reported quota. Current dollars equal 35.18% of the local peak; the local peak therefore implies 64.82% consumed. Neither number may count as an exact provider quota source.

### Superseded observation that must be resolved, not silently dropped

- Old amount: **$80.41442** available/cash, voucher $0.00
- Classification: `STALE HISTORICAL OBSERVATION`
- Original observation: `2026-08-05T09:32:53Z` / 2026-08-05 18:32:53 KST
- At the traced live observation `2026-08-10T08:47:22Z`, it was **4d 23h 14m 29s old**.
- It overstated current available cash by **$47.11442**, or **141.48% above the real balance**; it was **2.4148×** the real balance.
- The real $33.30 is only **41.41%** of the stale displayed $80.41.
- Because both cards were rendered as separate budgets, their apparent combined headroom was **$113.71442**, or **3.4148×** the real wallet. This is the board-level "roughly triple" failure; the stale headline alone was 2.4148× the real balance.

### What fed the stale $80.41 card

1. Cache file: `/Users/duhokim/HermesOps/private-state/kimi-direct-balance.json`
2. Cache marker: `KIMI_DIRECT_BALANCE_CACHE_V1`
3. Private renderer constant: `KIMI_BALANCE_CACHE_PATH` at `tools/render_ge_autopilot_dashboard_v2.py:66-72`
4. Card path: `kimi_direct_balance_card()` at `tools/render_ge_autopilot_dashboard_v2.py:1213-1235`
5. Refresh path: `_fetch_kimi_direct_balance()` at `tools/render_ge_autopilot_dashboard_v2.py:1176-1210`
6. Endpoint: `https://api.moonshot.ai/v1/users/me/balance`
7. Credential selectors in that private refresh path: in-memory `MOONSHOT_API_KEY`, `KIMI_API_KEY`, or `KIMI_CODING_API_KEY`; no value is emitted.
8. Current private-path result: the private renderer reports `Last read-only balance · refresh unavailable`. That is not a truthful capability statement for this wallet: the approved live path refreshed the identical endpoint minutes ago. It describes only the private duplicate path's failure to refresh, but the card presents it as a wallet/source limitation. Once canonicalized, this false status must disappear.

The fresh $33.30 card is fed by the approved provider monitor through `tools/moonshot_balance_usage.py:49-88`, using the same official endpoint. Duho has resolved the identity question: these are observations of **one wallet**, not separate budgets.

### Exact Moonshot disposition

- Keep exactly one card named `Moonshot / Kun (Kimi K3)`.
- Select the authoritative fresh monitor observation for the canonical card: $33.30 / $33.30 / $0.00.
- Do not average $33.30 and $80.41.
- Do not sum them.
- Do not render `Kimi / Moonshot direct API` as a second card or second budget. The canonical live card is the only Moonshot wallet card.
- Preserve the $80.41 record under the canonical card as an explicitly labelled `STALE HISTORICAL OBSERVATION`, with original timestamp and age, or in a structured `historical_observations` field.
- If retained, the historical record must never populate `big`, `percent`, current totals, or routing headroom.
- Replace the false `refresh unavailable` self-description with `Historical observation superseded by newer official reading` on the history row, or omit a status string from the historical row entirely.
- If the fresh monitor later becomes unavailable, retain one Moonshot card and fail closed to `STALE HISTORICAL OBSERVATION` or `UNAVAILABLE / UNKNOWN`; never resurrect $80.41 as a current live balance.
- The private cache refresh code may remain as a fallback candidate source, but every candidate must bind to the same `pool_id`; candidate readings are reconciled by timestamp/authority, never appended as separate cards.
- A same-pool contradiction at comparable timestamps must become `UNAVAILABLE / UNKNOWN` with a visible conflict note rather than choose the larger balance.

Expected unique-card effect: the nine current card records become **eight unique budget/product cards** after the duplicate Kimi/Moonshot wallet representation is canonicalized. No underlying cash/voucher meter is lost.

## Exact renderer changes proposed

### 1. Add explicit classification/provenance

At `public_gauge_card()` (`tools/render_ge_autopilot_dashboard_v2.py:1075-1113`) and private card constructors, emit:

- `pool_id`
- `classification`
- `observed_at_utc`
- `age_seconds`
- `current_value_known`
- `source_name`
- `refresh_gate`
- `historical_value_label` when applicable
- `denominator_source`

Do not infer classification from a numeric `percent`.

### 2. Preserve stale-branch visibility

Replace the stale branch at `tools/render_ge_autopilot_dashboard_v2.py:1417-1445`:

- Current behavior: build all cards, then return only private Kimi, Flow, and YouTube.
- Proposed behavior: return every unique operational provider/product card.
- Public-source cards are labelled `STALE HISTORICAL OBSERVATION` or `UNAVAILABLE / UNKNOWN` per their own source time.
- Remove current percentages from routing/headline use when stale; retain old values only in historical copy with timestamp and age.
- Replace `stale-source-hidden` with a visible stale/unknown state such as `stale-source-visible`.
- Replace `provider_gauge_count_hidden_as_stale` with explicit counts for visible stale, unknown, planning, and fresh meters.

### 3. Apply freshness per card, not per wrapper

The current fresh branch at `tools/render_ge_autopilot_dashboard_v2.py:1446-1479` trusts the wrapper observation time. Instead:

- Extract or carry each gauge's original observation timestamp from `source_label`/structured provenance.
- Classify Codex and Antigravity by those original timestamps even when the approved monitor writes a fresh wrapper.
- A collector pass may be fresh while inherited pane observations remain stale.
- `exact_limit_percent_sources` counts only fresh provider-authoritative percentages.
- Exclude local Moonshot percent-of-peak, stale Codex, stale Antigravity, planning envelopes, and nulls.

### 4. Fix the five currently empty headline values

`public_gauge_card()` leaves `big: null` on exactly these current cards:

1. `Claude / Fable / Lana`
2. `Gemini app / consumer`
3. `Moonshot / Kun (Kimi K3)`
4. `Antigravity / Gemini`
5. `Codex`

The shared structural cause is one code path: `public_gauge_card()` at `tools/render_ge_autopilot_dashboard_v2.py:1098-1105` copies `gauge.get("big")`, but the live public gauges do not populate `big`. Its only fallback runs when `pct is None` and the label starts with `available`; it therefore does not populate any of these five live-path records.

One classification-aware headline helper in `public_gauge_card()` covers the blank-`big` defect for all five cards. Moonshot also needs its separate wallet-specific semantic hunk because its headline must be `$33.30`, not the local `64.8% of peak used`, and its private duplicate must be removed.

Proposed dynamic headline policy:

- Fresh provider percentage: render the measured percentage, e.g. `1%`.
- Fresh dollar wallet: render the amount, so Moonshot shows `$33.30`, not `64.8%`.
- Stale observation: render `Stale`.
- Unavailable meter: render `Unknown`.
- Planning envelope: render an allowance label, never a live percent.

No card may fall through to the current JavaScript `—%` placeholder when the state is known to be stale, unknown, dollar balance, or planning envelope.

### 5. Keep every meter separate

Remove the blanket 5-hour suppression at `tools/render_ge_autopilot_dashboard_v2.py:1079-1085`. Preserve as distinct meters:

- Claude account five-hour, Fable weekly, all-model weekly, Opus weekly unknown, Sonnet weekly unknown
- Gemini app current-window and weekly
- Nous monthly plan and purchased top-up
- Moonshot available/cash/voucher; peak comparison separately labelled planning
- Antigravity Gemini weekly/five-hour and Antigravity Claude/GPT weekly/five-hour
- Codex main weekly/five-hour and Spark weekly/five-hour
- Flow monthly and daily bonus
- YouTube one shared daily unit pool; upload/search counts remain derived planning envelopes, not separate budgets

Tori/Hermes context-window use remains excluded from provider quota.

### 6. Stop identity rewriting

Remove the unconditional `gpt-5.5` → `gpt-5.6` rewrite at `tools/render_ge_autopilot_dashboard_v2.py:1049-1055`. Preserve the source-reported model identity; a new model label requires a new observation.

### 7. Correct Moonshot source semantics

In `tools/moonshot_balance_usage.py:67-87`:

- Retain fresh available/cash/voucher dollars and peak metadata.
- Emit `big: "$33.30"` dynamically from the fresh `available_balance` value so the live path supplies the authoritative headline directly.
- Do not expose percent-of-peak as `fill_pct` or any field counted as provider quota.
- Emit the peak comparison as `PLANNING ENVELOPE` metadata/sub-gauge.
- Preserve no-fixed-denominator semantics for the wallet.

## RED assertions required before a later source apply

1. With a source wrapper older than one hour, all unique operational cards remain present; none disappear.
2. Stale cards have `percent is None`, visible stale status, original observation time, and age.
3. A fresh wrapper containing day-old Codex/Antigravity observations does not classify those meters as fresh.
4. Exactly one Moonshot/Kimi wallet card exists.
5. Canonical Moonshot values equal $33.30 available, $33.30 cash, $0.00 voucher when the approved monitor supplies that reading.
6. The old $80.41442 observation appears only as historical data with `2026-08-05T09:32:53Z` and never enters totals/headlines.
7. The historical row does not claim `refresh unavailable`; it says it was superseded by a newer official reading or carries no capability-status assertion.
8. Moonshot percent-of-peak is not counted in exact provider percentages.
9. One shared classification-aware renderer helper populates meaningful `big` headlines for Claude, Gemini app, Moonshot, Antigravity, and Codex; Moonshot's value comes from fresh dollars, while stale Antigravity/Codex resolve to `Stale` rather than promoting old percentages.
10. Five-hour/current-window meters remain present.
11. Null meters stay null/unknown; no absent value becomes 0% or $0.00.
12. Source-reported model names are not rewritten.
13. Context-window/local-token analytics remain outside quota counts.
14. Current nine records canonicalize to eight unique cards because the same Moonshot wallet is no longer duplicated.

## GREEN scope for a later explicit apply

Allowed only after a separate exact approval:

- `tools/render_ge_autopilot_dashboard_v2.py`
- `tools/moonshot_balance_usage.py`
- focused tests under `tools/tests/`

Not allowed by Decision 2 apply alone:

- generated `ge-autopilot.html` hand edit
- provider/account/OAuth/browser call beyond the separately approved monitor
- public monitor write outside its approved loop
- renderer or watcher restart
- deploy
- DB/wiki/product mutation
- Git commit/push/merge
- cron/config/secret change

## Apply and activation gates

1. Recheck bound source hashes and dirty-tree scope.
2. Apply test-only RED diff; run only after test execution is explicitly approved.
3. Apply minimal source GREEN diff; rerun focused tests.
4. Stop with `VERIFIED_IN_WORKTREE_NOT_DEPLOYED`.
5. A later private-renderer restart is a separate activation approval.
6. Public cockpit/status publication remains a separate gate.

## Rollback preflight

The future exact packet must provide split test/source patches and reverse-check commands. Rollback affects only the scoped source/test hunks; it must not reset unrelated pre-existing worktree changes.

## Safety receipt

This preflight records Duho's current wallet authority and proposed exact-diff behavior only. It performs no account/billing/OAuth-page access, browser capture, new provider call, deploy, Git, cron, config, secret, watcher, renderer, public cockpit, DB, or wiki action.
