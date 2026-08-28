# Moonshot/Kimi wallet canonicalisation exact-diff preflight

- Marker: `TORI_MOONSHOT_WALLET_CANONICALISATION_PREFLIGHT_20260810T1913K`
- State: `PREPARED_ONLY_NOT_APPLIED`
- Authority: Duho verbatim `approve both`, interpreted as permission to author/open this packet only
- Apply authority: **NOT GRANTED**
- User-acceptance label: **not asserted**
- Active execution phrase: `NO ACTIVE EXECUTION PHRASE`

A later apply requires a new exact phrase such as:

`APPROVE APPLY TORI_MOONSHOT_WALLET_CANONICALISATION_PREFLIGHT_20260810T1913K`

This phrase is proposed locally for a future decision; it is not active and has not been supplied.

## Problem statement

The private dashboard renders two cards as if they are separate budgets even though both read:

`https://api.moonshot.ai/v1/users/me/balance`

They are one Moonshot wallet observed at different times.

### Authoritative live observation

- card: `Moonshot / Kun (Kimi K3)`
- classification: `FRESH LIVE METER`
- latest locally observed source line during packet authoring: endpoint fetched `2026-08-10T10:07:45Z`
- available: `$33.30`
- cash: `$33.30`
- voucher: `$0.00`
- current `big`: `None`
- current `percent`: `64.8`, derived from local peak rather than provider quota
- status: `Live official balance endpoint (key never emitted)`
- peak observed: `$94.66`
- pricing metadata: `$3/M` input, `$15/M` output, `$0.30/M` cache hit

Duho has authoritatively resolved `$33.30` as the available balance.

### Superseded private-cache observation

- card: `Kimi / Moonshot direct API`
- classification: `STALE HISTORICAL OBSERVATION`
- observed: `2026-08-05T09:32:53Z`
- available/cash: `$80.41442`
- voucher: `$0.00`
- cache: `/Users/duhokim/HermesOps/private-state/kimi-direct-balance.json`
- cache SHA-256: `5ce04fff004052fd1c5c899ee4af19c7cc7d3b3747c89580aecfe699ffb3509f`
- age at 2026-08-10 19:13 KST: approximately `5d 0h 40m`
- current `big`: `$80.41`
- status: `Last read-only balance · refresh unavailable`

The stale status is a false wallet-level self-description: the approved live path is refreshing the identical endpoint. It describes only the duplicate private path's failure, not a provider capability limit.

## Required result

Render exactly one canonical wallet card:

- `pool_id`: `moonshot_kun_kimi_k3_wallet`
- name: `Moonshot / Kun (Kimi K3)`
- current source: approved `tools/live_provider_usage_monitor.py` path through `tools/moonshot_balance_usage.py`
- `big`: live available dollars, currently `$33.30`
- available/cash/voucher retained as separate structured values
- no fixed-denominator percentage invented
- local percent-of-peak retained only as `PLANNING ENVELOPE`

The `$80.41442` cache may be retained only under `historical_observations` with:

- `classification: STALE HISTORICAL OBSERVATION`
- original timestamp
- dynamic age
- exact old available/cash/voucher values
- status `Historical observation superseded by newer official reading`

It must never be:

- a second card
- a current headline
- a routing balance
- added to or averaged with the live amount
- promoted to current when the approved live source is unavailable
- silently deleted without a historical disposition

If the approved live source is unavailable, the one canonical card becomes `UNAVAILABLE / UNKNOWN`; old cache data remains explicitly historical.

## Bound current sources

1. `tools/render_ge_autopilot_dashboard_v2.py`
   - bound SHA-256 after Decision 2 source apply: `1c46d1890c2559b6ffcc3696f5961d3ef3a05031bba3f37f3d1503c598053168`
   - `public_gauge_card()`: lines 1075-1113
   - private cache/card path: `_read_kimi_balance_cache()`, `_fetch_kimi_direct_balance()`, `kimi_direct_balance_card()`
   - `build_public_usage_snapshot()`: lines 1495-1599
2. `tools/moonshot_balance_usage.py`
   - bound SHA-256: `54cb169f0cd33689483a8fc0ba4dd012854f7bbf621b6c2ca4b0961678253ec1`
   - `fetch_gauge()`: lines 49-88
3. New focused wallet tests under `tools/tests/`

Decision 2's new stale-visibility behavior must remain intact.

## Exact GREEN design — not applied

### A. Make the approved live gauge authoritative and structured

In `tools/moonshot_balance_usage.py`:

- add constant `POOL_ID = "moonshot_kun_kimi_k3_wallet"`;
- emit `pool_id`, `classification`, `observed_at_utc`, and `current_value_known`;
- emit `available_balance_usd`, `cash_balance_usd`, and `voucher_balance_usd` as distinct fields;
- emit `big` from live `available_balance`, e.g. `$33.30`;
- set provider-quota `fill_pct` to `None` because the wallet has no fixed denominator;
- move percent-of-peak into a nested `planning_envelopes` entry classified `PLANNING ENVELOPE`;
- retain peak/pricing metadata in detail;
- if cash/voucher fields are absent, preserve them as unknown instead of defaulting missing values to `$0.00`.

### B. Preserve structured fields through the private normalizer

In `public_gauge_card()`:

- carry `pool_id`, `classification`, `observed_at_utc`, structured dollar fields, `planning_envelopes`, and `historical_observations` through to private JSON;
- use provider-supplied live `big` when present;
- do not derive a Moonshot headline from percent-of-peak.

### C. Canonicalise before appending private supplements

In `build_public_usage_snapshot()`:

- find the public live card by `pool_id`, with exact-name fallback only for migration;
- do not call or append `kimi_direct_balance_card()` when the canonical public Moonshot card exists;
- read the old private cache locally without invoking `_fetch_kimi_direct_balance()`;
- attach an older cache record only as `historical_observations`;
- return one Moonshot card in both fresh and stale wrapper branches;
- update provider/card count from nine records to eight unique product/budget cards;
- remove notes claiming the private Kimi wallet is a separate supplement.

If the public card is absent, create one `UNAVAILABLE / UNKNOWN` canonical Moonshot card and attach the cache only as history. Do not turn the cache into current balance.

### D. False-status removal

The historical row must say:

`Historical observation superseded by newer official reading`

It must not say:

`refresh unavailable`

No provider/account capability assertion may be inferred from one duplicate local path's credential/runtime state.

## RED test packet required before any later apply

1. Approved live Moonshot gauge returns:
   - `pool_id == "moonshot_kun_kimi_k3_wallet"`
   - `big == "$33.30"`
   - available/cash/voucher equal `33.30 / 33.30 / 0.00`
   - `fill_pct is None`
   - peak comparison classified `PLANNING ENVELOPE`
2. Private snapshot with one live public observation plus the `$80.41442` cache returns exactly one Moonshot card.
3. That card uses `$33.30` as `big` and current routing balance.
4. `$80.41442` appears only in `historical_observations` with timestamp/age and superseded status.
5. `_fetch_kimi_direct_balance()` is not called while building the private snapshot.
6. `refresh unavailable` is absent from the canonical card and history.
7. Exact current-percent source counts exclude percent-of-peak.
8. Stale-wrapper fixture retains one canonical Moonshot card and Decision 2 historical/unknown semantics.
9. Missing live source yields `UNAVAILABLE / UNKNOWN`; stale cache is not promoted.
10. Missing cash/voucher source fields remain unknown rather than defaulting to zero.

Tests must monkeypatch URL access and cache reads; authoring/RED may not perform a real provider call.

## Five empty `big` headlines — root-cause analysis

Affected public live-path cards:

- Claude / Fable / Lana
- Gemini app / consumer
- Moonshot / Kun (Kimi K3)
- Antigravity / Gemini
- Codex

### Finding

Yes: one shared structural defect explains all five empty JSON headline fields.

`public_gauge_card()` assigns:

`big = gauge.get("big")`

The public live gauges do not normally populate `big`. Its narrow fallback runs only when `pct is None` and the label starts with `available`, so all five records retain `big: None` even while `percent_label`, `activity`, and detail contain readings.

### Why one blind fallback is unsafe

The root cause is shared, but the safe display semantics are not identical:

- fresh Claude/Gemini percentages may headline their measured provider value;
- Antigravity and Codex must first respect their own stale source timestamps and headline `Stale`, not promote old percentages under a fresh wrapper;
- Moonshot must headline live dollars, not local percent-of-peak.

### Packet scope recommendation

This wallet packet's future GREEN scope should fix Moonshot's `big` by supplying structured live dollars at the source. It should not silently add live-headline behavior for the other four cards.

Duho should receive a separately selectable headline hunk/packet for the shared renderer helper after per-card freshness rules are bound. That preserves the one-root-cause finding without widening wallet apply authority.

## Apply gates

This packet is author-only. No source/test hunk is authorized now.

A later apply decision must specify whether it approves:

1. `WALLET ONLY` — canonical Moonshot card, live dollar headline, stale cache as history, private duplicate call removed; or
2. `WALLET + COMMON HEADLINE` — wallet changes plus a separately reviewed classification-aware headline helper for the other four cards.

Default interpretation is `WALLET ONLY`.

Any later source apply still excludes:

- account/billing/OAuth-page access
- browser capture
- real provider calls outside the approved monitor
- public cockpit publication
- deploy
- Git commit/push/merge
- cron/config/secret action
- DB/wiki/product mutation
- any user-acceptance assertion

Renderer activation/restart must be assessed separately against the provider-call gate after the duplicate private fetch path is removed.

## Rollback plan

A future exact packet must provide split RED-test and GREEN-source patches. Rollback reverses only wallet/headline-approved hunks and leaves Decision 2 stale-visibility behavior intact.

## Safety receipt

This packet records proposed changes only. Tori did not edit wallet source/tests, call Moonshot, inspect credentials, restart the renderer, write generated/public cockpit files, deploy, mutate Git/cron/config/secrets, or assert acceptance.
