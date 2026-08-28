# Decision 2 exact-diff preflight — stale provider cards stay visible

- Marker: `TORI_COCKPIT_USAGE_LIMIT_DECISION_2_STALE_VISIBILITY_PREFLIGHT_20260810T1807K`
- State: `PREPARED_ONLY_NOT_EXECUTED`
- Authority: Duho approval of Decision 2 from `HWAO_USAGE_MONITOR_APPROVAL_FRAME_20260810T1740K.md`
- Authority SHA-256: `bf081384503a090a1c6ddbf39ae14e07898b215d39d2181c5998194460bd3bc2`
- Active execution phrase: `NO ACTIVE EXECUTION PHRASE`
- Runtime/source patch applied: **NO**
- Test/build executed: **NO**
- Renderer/watcher restarted: **NO**

## Scope correction

This is the authoritative scoped Decision 2 preflight.

The earlier broad draft `TORI_COCKPIT_USAGE_LIMIT_DECISION_2_EXACT_DIFF_PREFLIGHT_20260810T1759K.md` remains historical but is **not Decision 2 execution authority** because it also described headline-value and Moonshot-deduplication changes. Duho/Hwao explicitly require those restoration-exposed defects to remain separate.

Decision 2 does one thing:

> When the provider monitor stops or its wrapper feed becomes stale, provider cards remain visible as `STALE HISTORICAL OBSERVATION` or `UNAVAILABLE / UNKNOWN`; current percentages are removed and old values move into explicitly historical copy.

A stopped monitor must read as `we stopped reading this`, never as `this pool does not exist`.

## Bound source and exact target

- Source: `tools/render_ge_autopilot_dashboard_v2.py`
- Bound SHA-256: `a246d502b0af1a494460b10a43bb4aa9692f3cf2dba855ecd2c9a6f24bceead4`
- Function: `build_public_usage_snapshot()` at lines 1393-1480
- Exact stale branch: lines 1417-1445
- Card normalizer available for reuse: `public_gauge_card()` at lines 1075-1113
- Generated HTML is not a patch target.
- Approved monitor `tools/live_provider_usage_monitor.py` is not a patch target.
- `tools/moonshot_balance_usage.py` is not a Decision 2 patch target.

## Current failing behavior

The renderer first builds six retained public provider cards, appends private Kimi, Flow, and YouTube cards, and therefore has nine records in `cards`.

When `observed_age > 3600`, it returns only:

- private Kimi
- Flow
- YouTube

The six provider cards disappear. The branch says `stale-source-hidden`, sets exact sources to zero, and records a hidden count, but the user cannot see which pools stopped reporting.

## Exact proposed source behavior

### A. Historicalize retained provider cards

Add one private helper beside `public_gauge_card()`, conceptually `historicalize_usage_card(card, observed_at, age_seconds)`.

For every public provider card when the wrapper is stale:

- preserve `name`, `kind`, `source`, detail provenance, and every sub-meter row;
- set top-level `classification` to `STALE HISTORICAL OBSERVATION` when an old observation/value exists;
- set top-level `classification` to `UNAVAILABLE / UNKNOWN` when no prior reading exists;
- set `observed_at_utc` and `age_seconds` from the card's own source timestamp where present, otherwise from the stale wrapper timestamp;
- set `percent` to `None`;
- move the former `percent_label`/`activity` reading into `historical_value_label` or copy prefixed exactly `Last observed — ...`;
- set current `percent_label` to `Current percentage unavailable — provider feed stale`;
- set `status` to `Stale historical observation` or `Unavailable / unknown`;
- set `big` to `Stale` or `Unknown` for this stale branch only;
- change current-looking tone/status styling to warning/unknown styling.

For every sub-gauge:

- preserve `label`;
- set `percent` to `None`;
- move the former measured label to `historical_value_label` or `Last observed — ...`;
- use `not observed` for fields that were already unknown;
- do not create `0%` from a missing field.

### B. Return all records instead of three

Replace the stale branch's current `cards: [kimi_card, flow_credit_card(), youtube_api_quota_card()]` with:

- all six historicalized/unknown retained provider cards;
- the existing private Kimi card unchanged by Decision 2;
- the existing Flow card unchanged by Decision 2;
- the existing YouTube card unchanged by Decision 2.

Expected Decision 2 stale-branch card count: **9**, preserving current card membership. Moonshot deduplication is a separate defect and therefore intentionally not performed by this patch.

### C. Expose the outage explicitly

In the returned snapshot:

- `cache_state`: `stale-source-visible`
- `provider_monitor_status`: `STALE_PROVIDER_FEED_CARDS_VISIBLE`
- `exact_limit_percent_sources`: `0`
- remove `provider_gauge_count_hidden_as_stale`
- add counts equivalent to:
  - `provider_gauge_count_visible_as_stale`
  - `provider_meter_count_unknown`
  - `provider_meter_count_planning_envelope`
- notes must say the provider feed age and that last observations are historical, not current routing headroom.

Do not advance any provider/card observation timestamp during rendering.

### D. Preserve category boundaries

- Tori/Hermes context-window use remains filtered from provider quota.
- The public Flow planning card remains filtered; the private Flow credit card remains separate.
- Every provider/model/window sub-meter stays distinct.
- No fixed denominator is invented for purchased wallets.
- Static allowances and derived call counts remain `PLANNING ENVELOPE`, not measured utilization.

## RED test packet required before later apply

A later executable exact-diff packet must add a focused test module for the private renderer. RED assertions:

1. A fixture with six retained provider cards and a wrapper age above one hour returns nine visible cards, not three.
2. The six provider names remain present in the same order:
   - Claude / Fable / Lana
   - Gemini app / consumer
   - Hermes / Nous credits
   - Moonshot / Kun (Kimi K3)
   - Antigravity / Gemini
   - Codex
3. Every stale provider card has top-level `percent is None`.
4. Every stale provider sub-gauge has `percent is None`.
5. Prior numeric/text readings survive only in historical fields/copy prefixed `Last observed`.
6. Previously unknown fields remain unknown and do not become 0% or $0.00.
7. `cache_state == "stale-source-visible"`.
8. `provider_monitor_status == "STALE_PROVIDER_FEED_CARDS_VISIBLE"`.
9. `exact_limit_percent_sources == 0`.
10. `provider_gauge_count_hidden_as_stale` is absent.
11. Context-window/Tori analytics remain absent from quota cards.
12. Fresh-branch fixtures remain unchanged by Decision 2.
13. No provider/account/network helper is invoked by snapshot rendering.

## GREEN patch scope for a later exact approval

Allowed only after a separate apply approval:

- `tools/render_ge_autopilot_dashboard_v2.py`
- one focused renderer test file under `tools/tests/`

Not part of Decision 2:

- `tools/live_provider_usage_monitor.py`
- `tools/moonshot_balance_usage.py`
- generated `ge-autopilot.html`
- public status/cockpit files
- provider/account/OAuth/browser sources
- watcher or renderer restart
- deploy
- Git commit/push/merge
- cron/config/secret action
- DB/wiki/product mutation

## Apply/activation sequence — not authorized now

1. Recheck the bound source hash and dirty-tree state.
2. Validate split RED-test and GREEN-source patches with non-mutating `git apply --check`.
3. Apply/run RED only after test execution approval; require the old three-card behavior to fail the visibility assertions.
4. Apply GREEN; rerun focused and adjacent renderer tests.
5. Stop at `VERIFIED_IN_WORKTREE_NOT_DEPLOYED`.
6. A private-renderer restart is a separate activation gate.
7. Public cockpit/status publication remains a separate gate.

Rollback must reverse only the focused source/test hunks. It must not reset unrelated pre-existing worktree changes.

## Separate restoration-exposed defect A — five empty live headlines

Classification: `SEPARATE_DECISION_REQUIRED_NOT_IN_DECISION_2`

Affected live-path records:

- Claude / Fable / Lana
- Gemini app / consumer
- Moonshot / Kun (Kimi K3)
- Antigravity / Gemini
- Codex

Verified common structural cause: `public_gauge_card()` copies `gauge.get("big")`, while these public gauges do not supply `big`; its limited fallback does not run for numeric percentages.

Recommendation to Duho:

- Prepare a separate headline exact-diff packet.
- Use one classification-aware renderer headline helper for the shared blank-field defect.
- Fresh percentage cards show the provider percentage; stale cards show `Stale`; unknown cards show `Unknown`.
- Moonshot needs a wallet-specific dollar headline, not percent-of-peak.
- Do not include this hunk in Decision 2 merely because it touches the same function.

## Separate restoration-exposed defect B — one Moonshot wallet, contradictory cards

Classification: `SEPARATE_DECISION_REQUIRED_NOT_IN_DECISION_2`

Both cards use `https://api.moonshot.ai/v1/users/me/balance`.

Current/stale determination from timestamp evidence plus Duho's authoritative balance resolution:

- `Moonshot / Kun (Kimi K3)`: `FRESH LIVE METER`, $33.30 available, cash $33.30, voucher $0.00.
- `Kimi / Moonshot direct API`: `STALE HISTORICAL OBSERVATION`, $80.41 observed `2026-08-05T09:32:53Z`, approximately five days old at restoration.

Do not average, sum, reconcile numerically, or silently drop the conflict.

Recommendation to Duho:

- Prepare a separate canonical-wallet exact-diff packet.
- Render one current Moonshot/Kun card fed by the approved live path.
- If retained, attach $80.41 only as explicitly historical data with timestamp/age; never as a second card, current headline, total, or routing balance.
- Remove the false wallet-level self-description `refresh unavailable`; the identical endpoint is demonstrably refreshing through the approved live path.
- Keep percent-of-peak as `PLANNING ENVELOPE`, not exact provider quota.

Neither separate recommendation is authorized for source apply by Decision 2.

## Safety receipt

This artifact is a preflight only. It performs no source/test application, account/billing/OAuth-page access, browser capture, new provider call, generated-HTML/public write, monitor/renderer restart, deploy, Git, cron, config, secret, DB, wiki, or product mutation.
