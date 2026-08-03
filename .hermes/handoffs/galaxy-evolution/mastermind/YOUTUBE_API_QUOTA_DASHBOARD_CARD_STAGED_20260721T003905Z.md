# YouTube API quota dashboard card — staged receipt

Marker: `YOUTUBE_API_QUOTA_DASHBOARD_CARD_STAGED_20260721T003905Z`

## Result

The private Galaxy Evolution dashboard renderer now includes one additional card in the existing **Usage limit monitor**. No layout, route, polling interval, or public Baseline cockpit surface was changed.

The card reports:
- 10,000 shared API units/day
- 100 video upload calls/day
- 100 search calls/day
- reset at midnight Pacific
- `videos.list` 1 unit
- `videos.update` 50 units
- `captions.list` 50 units
- `captions.insert` 400 units
- prepared V8 review packet: 4 uploads + about 63 shared units
- four later manual captions: +1,600 shared units
- exact remaining quota: not exposed by YouTube API

## Verification

- Isolated render: PASS
- Isolated JSON: exactly one `YouTube Data API` card
- Targeted tests: 3 passed
- Full test file: 6 passed, 1 unrelated pre-existing stale overnight-marker assertion failed (`20260712` expected versus current `20260719` renderer marker)
- Active watcher output: unchanged, as expected, because the 42-hour-old Python process does not hot-reload source

## Activation gate

Not activated because explicit restart approval was not received.

Narrow activation scope when approved:
- restart only tmux session `ge-autopilot-dashboard-renderer`
- command: `python3 tools/render_ge_autopilot_dashboard_v2.py --watch`
- verify active HTML/JSON and tailnet URL
- do not touch public Baseline cockpit, product runtime, DB, deploy, git, cloud, browser, cron, OAuth, or tokens

Backup: `docs/youtube_quota_dashboard_backup_20260721T003905Z`
