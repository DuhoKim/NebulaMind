# Gemini quota pools, and the app-usage gauge

## The problem this fixes

The cockpit's `Gemini / Goru` gauge reads the Antigravity CLI's `/usage` panel. That panel reports
**Antigravity's agent-request quota**. It is not the meter you see at
<https://gemini.google.com/usage>. The two are billed separately against the same Google AI
subscription, so the gauge could sit at 4% while the Gemini app itself was exhausted.

A gauge labelled "Gemini" that tracks a different pool than the one you check by hand is worse than
no gauge, because you trust it.

## The four pools

One subscription, four budgets that do not share a pot:

| Pool | Governs | Where it is visible | Tracked by the cockpit |
|---|---|---|---|
| Antigravity agent requests | `agy` agent turns | `agy` → `/usage` panel | yes — `Gemini / Goru` |
| Consumer app compute meter | gemini.google.com chats, Deep Research, image/video gen | Settings → Usage Limits | yes — `Gemini app / consumer` |
| Gemini CLI OAuth quota | `gemini` CLI turns | `gemini` → `/stats model` | no |
| `generativelanguage` API key | backend jury/batch calls (RPM/TPM/RPD) | Google AI Studio / Cloud console | no (`NM_GEMINI_API_KEY` disabled 2026-07-08) |

Spending one does not draw down another. Check the pool that matches the work you are about to route.

## Why the app meter is captured by hand

`gemini.google.com/usage` has **no API**. There is no documented endpoint and no OAuth scope. It is a
private `batchexecute` RPC behind a logged-in session. Everything else is a reverse-engineering
route:

- The published libraries (`gemini-webapi`, `HanaokaYuzu/Gemini-API`) only wrap *chat*. None of them
  read the usage page; the closest they get is a `USAGE_LIMIT_EXCEEDED` error *after* you hit the cap.
- A headless browser driving your logged-in Google profile would work, but it reads your session
  cookies and constitutes automated access under the Google Terms of Service ("Don't abuse our
  services": *using automated means to access content*, *bypassing our systems or protective
  measures*). It also breaks the monitor's own stated safety model — see the docstring at the top of
  `tools/live_provider_usage_monitor.py`.
- A bookmarklet cannot `fetch()` to `127.0.0.1` either: the page ships
  `default-src 'none'; connect-src 'self' https://*.google.com …`, so CSP blocks the request.

So the supported path is a **clipboard capture that you confirm by eye**. You are already on the
page; nothing automates a session, nothing reads a cookie, and no port is opened.

## Capturing a reading

Install once — create a bookmark whose URL is the line this prints:

```sh
python3 tools/gemini_app_usage_ingest.py --emit-bookmarklet
```

Then, whenever you want a fresh number:

1. Open <https://gemini.google.com/usage> (Settings → Usage Limits).
2. Click the bookmark. It reads the page, then asks you to confirm three things — the percent used,
   the reset text, and your plan tier. Each is pre-filled from the DOM where it can be found, but the
   page does not reliably name the plan, so the tier is usually yours to type. If it cannot parse the
   percentage it asks you to type that too — it never emits a guess.
3. Run `python3 tools/gemini_app_usage_ingest.py --from-clipboard`.

Chrome's address bar strips the `javascript:` scheme on paste. Create the bookmark through
**Bookmark Manager → ⋮ → Add new bookmark** instead, or you will end up bookmarking a Google search
for the script's source.

No browser? `python3 tools/gemini_app_usage_ingest.py --used-pct 47 --resets "Resets at 2:59 AM" --tier "AI Pro"`.

Inspect what is on file with `--show`.

## Freshness, and never inventing a number

The app meter is a 5-hour rolling window rolling into a weekly cap. A reading older than **6 hours**
(the window plus an hour of grace) describes a window that has already turned over, so the gauge
withholds the percentage and reports `stale capture` rather than painting an old number as current.
The same applies when no capture exists, or when the drop-file fails validation.

This matches how the rest of the cockpit behaves: `model_usage_status.json` already notes that Codex
headroom is labelled *unknown* "instead of inventing a number."

The reading lives at `.hermes/state/gemini_app_usage.json` (override with `NM_GEMINI_APP_USAGE_JSON`).
It holds a percentage and a reset time. No secrets.

## Using the headroom

`tools/gemini_app_usage.py` turns a reading into a burn lane, surfaced live on the gauge and in
`provider_usage_monitor.gemini_app_burn_advice`:

| Headroom | Lane | What to do |
|---|---|---|
| ≥ 60% | `burn` | Push wide repo/document scans, alternative summaries, HTML/report QA, multi-file classification here. Keep Claude and Codex for reasoning-heavy lanes. |
| 25–60% | `measured` | Batch scans only. Avoid Deep Research and image/video generation — they cost far more compute per prompt than a chat turn. |
| < 25%, reset ≤ 45 min | `wait` | Queue the batch; start it after the window refills. |
| < 25% | `reserve` | Route batch work elsewhere; keep the remainder for interactive prompts. |

The `wait` lane needs a parseable reset. Two wordings are understood: relative (`in 3 hr 20 min`) and
the absolute clock time the live page actually uses (`Resets at 2:59 AM`, interpreted in your local
zone, rolling to tomorrow if the hour has passed). A label neither parser recognises leaves
`reset_at_utc` null, `minutes_to_reset` unavailable, and `wait` unreachable — the lane degrades to
`reserve` rather than guessing a reset.

Because the meter is *compute-based* rather than a prompt counter, a Deep Research run or a Veo video
can consume a large share of a window in one shot. Batch text work is the cheap way to spend it.

To refresh the snapshot in `model_usage_status.json` (which external `ccusage` tooling regenerates,
clobbering hand edits), re-run the idempotent patcher:

```sh
python3 tools/gemini_burn_plan_patch.py          # --check to test without writing
```

## Feeding the lane to a router

`tools/gemini_app_usage_ingest.py --route` prints one self-contained advisory line — the lane, the
headroom that justifies it, the reset, and the reminder that this pool is independent of the
Antigravity/Goru quota:

```
GEMINI APP LANE: burn — 99% headroom, resets ~135m. route wide/cheap/long-context work (…) here;
this pool is independent of the Antigravity/Goru quota. [AI Ultra, capture 30m ago]
```

The galaxy-evolution autopilot injects this line into every `director_prompt()` dispatch (via
`gemini_app_route_line()` in `tools/galaxy_evolution_autopilot.py`), so Hwao sees the current lane
when it sequences a packet. It stays advisory: Hwao decides, and the line degrades to `unknown`
rather than a fabricated number when the capture is missing or stale. The autopilot loads the module
once, so the injection takes effect on its next restart.

## Auto-refresh (optional, unattended)

`tools/gemini_app_usage_autofetch.py` reads `gemini.google.com/usage` by driving your logged-in
Chrome, so the number can refresh without a bookmarklet click. This is **not** wired into
`live_provider_usage_monitor.py`, whose safety model forbids browser automation — it is a separate,
opt-in tool. It is also ToS-adjacent (it automates your logged-in session), so treat it as a
deliberate choice, not a default.

Two one-time macOS grants are required before it can read anything:

1. **System Settings → Privacy & Security → Automation** — allow the controlling terminal to control
   Google Chrome. The first run fails with AppleEvents error `-1743` until this is granted.
2. **Chrome → View → Developer → Allow JavaScript from Apple Events.**

```sh
python3 tools/gemini_app_usage_autofetch.py --dry-run   # scrape and print, store nothing
python3 tools/gemini_app_usage_autofetch.py             # scrape and store
```

An unattended read has no human to confirm it, so it is **more** conservative than the manual path:
it stores only a high-confidence value (a `[role=progressbar]` element or a percentage sitting next
to usage/limit wording). A bare percentage found anywhere else on the page is refused, and any
abstention leaves the existing reading untouched — an auto-scrape can never overwrite a good
human-confirmed capture with a guess. Auto readings carry `capture_method: chrome-auto` and the gauge
labels them "Unattended Chrome scrape" so they are never mistaken for operator-confirmed ones.

To schedule it, run it from `cron`/`launchd` (scheduling is your call — a recurring browser-driving
job is a deliberate action, not something the tools enable for you). A launchd example, every 30 min:

```xml
<!-- ~/Library/LaunchAgents/com.nebulamind.gemini-usage-autofetch.plist -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>com.nebulamind.gemini-usage-autofetch</string>
  <key>ProgramArguments</key><array>
    <string>/usr/bin/python3</string>
    <string>/Users/duhokim/NebulaMind/NebulaMind/tools/gemini_app_usage_autofetch.py</string>
  </array>
  <key>StartInterval</key><integer>1800</integer>
  <key>WorkingDirectory</key><string>/Users/duhokim/NebulaMind/NebulaMind</string>
  <key>StandardErrorPath</key><string>/Users/duhokim/NebulaMind/logs/gemini-usage-autofetch.log</string>
</dict></plist>
```

Load it with `launchctl load ~/Library/LaunchAgents/com.nebulamind.gemini-usage-autofetch.plist`.
