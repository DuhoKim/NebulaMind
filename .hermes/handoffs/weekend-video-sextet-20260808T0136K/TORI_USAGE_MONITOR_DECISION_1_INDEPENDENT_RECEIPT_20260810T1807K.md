# Tori independent receipt — Decision 1 usage monitor restoration

- Marker: `TORI_USAGE_MONITOR_DECISION_1_INDEPENDENT_RECEIPT_20260810T1807K`
- Verified: 2026-08-10 18:07 KST
- Authority: `HWAO_USAGE_MONITOR_APPROVAL_FRAME_20260810T1740K.md`
- Authority SHA-256: `bf081384503a090a1c6ddbf39ae14e07898b215d39d2181c5998194460bd3bc2`
- User-supplied prefix matched: `bf081384503a090a`
- Verification mode: local process/tmux/status-file reads only; Tori made no provider/account/browser call.

## Verdict

`PASS_DECISION_1_MONITOR_RESTORED_AND_PRIVATE_RENDERER_INGESTED_WITHOUT_RESTART`

The approved upstream monitor restoration worked. The private renderer moved from the inventory's `stale-source-hidden` / three-card state to `public-realtime-feed` / nine cards without a private-renderer restart.

## Running monitor evidence

- tmux session: `usage-monitor`
- pane: `%34`
- pane PID: `5257`
- pane start command: `python3 tools/live_provider_usage_monitor.py --watch --interval 300 2>&1 | tail -200`
- Python monitor PID: `5259`
- Monitor process start: 2026-08-10 17:42:20 KST
- Process state at verification: alive
- Watch interval: 300 seconds

## Private renderer non-restart evidence

- Renderer PID: `31235`
- Command: `python tools/render_ge_autopilot_dashboard_v2.py --watch --interval 20`
- Process start: 2026-08-08 14:09:54 KST
- The PID and start time predate Decision 1. No renderer restart was needed for ingestion.

## Before and after

Before, from `TORI_COCKPIT_USAGE_LIMIT_COVERAGE_INVENTORY_20260810T1733K.md`:

- upstream observation: `2026-08-09T04:02:37Z`
- `cache_state: stale-source-hidden`
- `provider_monitor_status: stale-hidden`
- visible cards: 3
- provider records built/hidden as stale: 9

Independent private-status snapshot at 2026-08-10 18:07 KST:

- path: `/Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json`
- SHA-256: `5afc235b1d27a7be1cdaa1bd60e20cbc9c4720619fc3de5f84389ef1f533b2e8`
- `cache_state: public-realtime-feed`
- `provider_monitor_status: LIVE_SAFE_MONITOR_ACTIVE`
- `sources.provider_gauge_count: 9`
- visible cards: 9
- private snapshot observation: `2026-08-10T09:02:26Z`
- rendered source-age label: `3m 58s`
- snapshot generated: `2026-08-10T09:06:24Z`

The later public monitor pass was present at `2026-08-10T09:07:27Z`; the 20-second renderer had not yet consumed that immediately newer pass when the receipt snapshot was taken. The user's 21-second reading is consistent with checking immediately after a 300-second pass, but Tori's later independent snapshot records the cadence point actually observed rather than copying `21s` as a new measurement.

Post-write recheck at approximately 18:10 KST confirmed the same renderer PID had consumed that newer pass without restart:

- private snapshot observation: `2026-08-10T09:07:27Z`
- private snapshot generated: `2026-08-10T09:09:21Z`
- source-age label at generation: `1m 54s`
- `cache_state: public-realtime-feed`
- `provider_monitor_status: LIVE_SAFE_MONITOR_ACTIVE`
- visible cards / provider gauge count: `9 / 9`

## Six restored provider cards

All six cards that were hidden by the stale branch are again present in the private JSON:

1. `Claude / Fable / Lana`
2. `Gemini app / consumer`
3. `Hermes / Nous credits`
4. `Moonshot / Kun (Kimi K3)`
5. `Antigravity / Gemini`
6. `Codex (seat unassigned)`

The three cards visible during the outage also remain present:

1. `Kimi / Moonshot direct API`
2. `Flow / Veo credits (Ultra)`
3. `YouTube Data API`

## Restoration-exposed defects — not cleared by Decision 1

Decision 1 restored visibility; it did not establish that every restored card is truthful or current.

- Five restored live-path cards have `big: null`: Claude, Gemini app, Moonshot/Kun, Antigravity, and Codex.
- The two Moonshot/Kimi cards hit the same endpoint but display contradictory observations. Duho's authoritative resolution and timestamp evidence identify `$33.30` as current and `$80.41` as five-day-old history.
- Antigravity and Codex retain old pane observations under fresh wrapper state and require per-meter freshness handling.

These are separate from the Decision 2 stale-outage visibility correction unless Duho later authorizes their own exact-diff scopes.

## Safety ledger

Tori performed no monitor start/restart, pane input, provider/account/OAuth/browser call, generated-HTML write, renderer restart, public cockpit write, deploy, Git, cron, config, secret, DB, or wiki action. This receipt is the only Decision 1 artifact written by Tori.
