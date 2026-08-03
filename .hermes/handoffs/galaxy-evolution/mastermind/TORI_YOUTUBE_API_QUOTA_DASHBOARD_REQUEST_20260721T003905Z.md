# Tori relay — YouTube API quota dashboard card

Marker: `TORI_YOUTUBE_API_QUOTA_DASHBOARD_REQUEST_20260721T003905Z`

User direction: add the verified YouTube Data API quota values to the existing dashboard.

Bounded execution:
- Target only the private tailnet Galaxy Evolution dashboard renderer: `tools/render_ge_autopilot_dashboard_v2.py`.
- Add one card to the existing Usage limit monitor; preserve layout, styling, routes, polling, and all public Baseline cockpit surfaces.
- Show official June 1, 2026 defaults: 10,000 shared units/day, 100 video uploads/day, 100 searches/day; reset midnight Pacific; videos.list 1, videos.update 50, captions.list 50, captions.insert 400.
- Show exact remaining quota as `not exposed`, not a guessed percentage.
- Read only the local V8 YouTube checkpoint for the current wording; no YouTube, cloud, billing, OAuth, token, browser, cron, deploy, restart, DB, or git action.

Hwao lanes observed in tmux were stale or assigned to unrelated prior work, so Tori is proceeding under the user's direct bounded instruction without interrupting those lanes.
