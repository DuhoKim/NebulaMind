# Moonshot wallet canonicalisation execution receipt

- Marker: `TORI_MOONSHOT_WALLET_CANONICALISATION_EXECUTION_RECEIPT_20260810T2006K`
- Authority: Duho verbatim `approve both`, applied only to wallet GREEN designs A-D and binding per-card freshness metadata
- State: `APPLIED_TESTED_AND_PRIVATE_RENDERER_ACTIVATED`
- User-acceptance label: **not asserted**

## Verdict

`PASS_WALLET_CANONICALISED_ONE_LIVE_CARD_STALE_CACHE_HISTORICAL_ONLY`

The private dashboard now has one Moonshot wallet card fed by the approved public monitor path. Its live headline is `$33.30`. The superseded `$80.41442` record is nested historical data with its original timestamp and dynamic age; it is not a card, headline, current field, percentage, total, or routing balance.

The duplicate private endpoint-fetch implementation was removed from the renderer before activation, so restarting the renderer could not perform a Moonshot/provider call.

## RED phase

Command:

`PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider tools/tests/test_moonshot_wallet_canonicalisation.py -q`

Expected RED result: 5 failed in 0.05s.

All failures were the intended missing behavior:

1. live gauge lacked `pool_id` and structured dollar fields;
2. missing cash/voucher fields had been defaulted to zero;
3. the private renderer called/appended the duplicate Kimi card;
4. the stale wrapper left the private `$80.41` card confident and outside historicalisation;
5. per-card freshness metadata did not exist.

There was no import, fixture, syntax, credential, provider, browser, or public-write failure. No real endpoint was contacted; the source test replaced `urlopen` with a local response object and used temporary key/high-water files.

## GREEN A — approved monitor gauge

Changed `tools/moonshot_balance_usage.py:73-129`:

- stable pool ID: `moonshot_kun_kimi_k3_wallet`;
- live classification and source timestamp;
- structured available/cash/voucher fields;
- `big` populated from live available dollars;
- provider-quota `fill_pct` set to `None`;
- percent-of-peak moved under `PLANNING ENVELOPE`;
- missing cash/voucher remain unknown instead of becoming `$0.00`.

The running monitor was not restarted and no provider call was initiated by Tori. The private renderer includes an exact-name migration fallback for the monitor's currently loaded pre-change gauge shape.

## GREEN B — structured normalisation and freshness binding

Changed `tools/render_ge_autopilot_dashboard_v2.py`:

- `provider_card_freshness()`: lines 1090-1109;
- `public_gauge_card()`: lines 1112-1166;
- five affected providers now carry their own source timestamp, age, one-hour limit, and four-way freshness classification independently of the wrapper timestamp;
- structured wallet and planning/history fields survive public-to-private normalisation;
- the common percentage headline helper was **not** applied.

Bound one-hour rules:

- Claude / Fable / Lana
- Gemini app / consumer
- Moonshot / Kun (Kimi K3)
- Antigravity / Gemini
- Codex, including the seat-label variant

## GREEN C-D — one wallet and no false status

Changed:

- `historicalize_usage_card()`: lines 1186-1297;
- `_cached_moonshot_history()`: lines 1330-1344;
- `canonicalize_moonshot_wallet()`: lines 1347-1476;
- `build_public_usage_snapshot()`: lines 1634-1738.

Behavior:

- the public Moonshot card is selected by pool ID, with exact-name migration fallback;
- the private renderer no longer has or calls `_fetch_kimi_direct_balance()` or `kimi_direct_balance_card()`;
- the old cache is read locally and attached as `historical_observations` only;
- `refresh unavailable` is absent;
- if live data is absent, one canonical `UNAVAILABLE / UNKNOWN` card remains and stale cache is not promoted;
- a stale wrapper historicalises the most recent `$33.30` observation too, clears structured current/routing fields, and retains both `$33.30` and `$80.41442` only as dated history;
- duplicate removal changes current membership from nine apparent records to eight unique product/budget cards.

## GREEN tests

Focused wallet/freshness tests:

- 5 passed in 0.04s.

Wallet + Decision 2 + adjacent provider parsing:

- 14 passed in 0.20s.

A pre-existing Python/LibreSSL `urllib3` warning remained non-blocking; no dependency/config change was authorized.

Local actual-source verification, without writing or calling a provider:

- fresh: `8` cards, one Moonshot card, `big=$33.30`, routing balance `33.3`, old history `[80.41442]`;
- simulated stale wrapper: `8` cards, one Moonshot card, `big=Stale`, routing balance `None`, historical values `[33.3, 80.41442]`;
- stale branch retained all six provider names and stripped their current percentages;
- `refresh unavailable` absent from both snapshots.

## Private activation

Before activation, exact copies were made under:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/wallet-canonicalisation-activation-backup-20260810T200322+0900/`

Pre-activation files:

- HTML SHA-256: `4d5a9dae97c5207d7daf9bc580d833033b5d505bd4dafefbf4ae292f41d19fb8`
- JSON SHA-256: `f7b7c0059519a64b56d80f66d89daa03603dc98343b5fbecf930d4d107d9f11f`

The private `ge-renderer` pane was respawned with its existing start command after the duplicate provider-fetch path had been removed.

- old renderer PID: `31235`
- new renderer PID: `38204`
- command unchanged: `python3 tools/render_ge_autopilot_dashboard_v2.py --watch --interval 20`
- health: `watching`
- monitor session/PID unchanged: `usage-monitor` / `5257`

Activated private status at `2026-08-10T11:03:27Z`:

- cache state: `public-realtime-feed`
- card count: `8`
- one Moonshot card
- pool ID: `moonshot_kun_kimi_k3_wallet`
- `big`: `$33.30`
- current/routing available: `33.3`
- current provider percent: `None`
- historical `$80.41442` age: `437434s` at verification
- historical status: `Historical observation superseded by newer official reading`
- private status SHA-256: `f4cafd31177d5aaf49baa0ae054ad5f21a2ce811910e604cb85e37b98632571e`

Per-card activated metadata:

- Claude: `FRESH LIVE METER`, source age `26s`, `big=None`;
- Gemini app: `FRESH LIVE METER`, source age `766s`, `big=None`;
- Antigravity: `STALE HISTORICAL OBSERVATION`, source age `173074s`, `big=None`;
- Codex: `STALE HISTORICAL OBSERVATION`, source age `112567s`, `big=None`.

Those four empty headlines confirm that the separately selectable common headline helper was not folded into this apply.

The public live-status SHA-256 was byte-identical before and after renderer activation:

`4135c0faef3606d4912a4cffcec2afebc0173441ade10648beae9b4b96faac43`

## Bound hashes

- renderer before: `1c46d1890c2559b6ffcc3696f5961d3ef3a05031bba3f37f3d1503c598053168`
- renderer after: `a3855b4dd9ced190dbe8f5af3733b0fb229c222679c046322680d4994c571d28`
- Moonshot collector before: `54cb169f0cd33689483a8fc0ba4dd012854f7bbf621b6c2ca4b0961678253ec1`
- Moonshot collector after: `f298ef116129491dffcd70d4401b9dd4f6ac2c178300cb2b7100e33fc30661a9`
- wallet/freshness tests: `f40a35033f224cc1b8743092828cb1a0580e6f604ca2c1fc206401ab886800e7`
- updated Decision 2 tests: `e12afbe200edb9a36918fd7566ca2bd94bc451ecf9d5dc1c0c4330ec15e1c79e`

## Safety ledger

- real provider calls by Tori: 0
- account/billing/OAuth-page actions: 0
- browser captures: 0
- monitor restarts: 0
- public cockpit/status writes by Tori: 0
- deploys: 0
- Git commit/push/merge: 0
- cron/config/secret actions: 0
- DB/wiki/product mutations: 0
- common headline hunk applied: no
- user-acceptance assertion: none
