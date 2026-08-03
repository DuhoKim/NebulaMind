# YouTube API quota dashboard card — live receipt

Marker: `YOUTUBE_API_QUOTA_DASHBOARD_CARD_LIVE_20260721T035422Z`

## Live result

- URL: https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html
- Section: `Usage limit monitor`
- Placement: immediately after `Flow / Veo credits (Ultra)` in the same `usage-grid`
- Desktop layout: Flow/Veo and YouTube cards appear side by side on the second row
- Visual QA: no overlap, clipping, or layout break
- Active card count: 6
- Exact-percent sources: 5/6; YouTube correctly has no invented percentage

## Renderer

- Dedicated tmux session: `ge-autopilot-dashboard-renderer`
- Command: `python3 tools/render_ge_autopilot_dashboard_v2.py --watch --interval 20`
- Restart explicitly approved by the user
- Full-cycle persistence verified: generated timestamp advanced from `2026-07-21T03:54:02Z` to `2026-07-21T03:54:22Z`, card remained present, renderer remained alive

## Preserved boundaries

No public Baseline cockpit, product runtime, DB, deploy, git, cloud, browser automation, cron, OAuth, or token changes were made. Existing dashboard layout, route, styling, polling, and all non-quota cards were preserved.
