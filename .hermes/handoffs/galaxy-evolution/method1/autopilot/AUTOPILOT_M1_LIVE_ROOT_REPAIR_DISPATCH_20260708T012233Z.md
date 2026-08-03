# Method1 autopilot — LIVE-ROOT REPAIR dispatch status

Order marker: AUTOPILOT_LIVE_ROOT_EMPTY_WIKI_REPAIR_PACKET_20260708T012233Z
Continuation marker: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Controller: Method1 Hwao (autonomous). Authored UTC: (stamped in receipt)
Class: BOUNDED DOCS/STATIC, NO-APPLY. Read-only two-root compare + `.hermes` no-apply packet only.

## Problem (from order)
Served site on :3000 runs `next start` from `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend` (LIVE ROOT), but the verified artifacts are in `/Users/duhokim/NebulaMind/NebulaMind/frontend` (WORKING REPO). Live root shows stub M1 `wiki-page.html` (~5,269 B) and 404s the same-format-rebuild previews → user sees empty pages.

## Lanes dispatched (this cycle)
- **Goru (mechanical, read-only):** inventory + byte/sha256 diff of M1 files WORKING vs LIVE ROOT; served-URL HTTP status/size on :3000. → method1 receipt below.
- **Hwao (verdict/report-back):** method1 comparison receipt with exact source→target mirror list; feed the director no-apply packet.
- Continue (don't park) until the final no-apply packet exists at the order path with READY_FOR_USER_APPROVAL or HARD_BLOCKED.

## Hard gates (closed)
NO write/copy into the live root · no DB/SQL · /api/pages · page_versions/publish · deploy/restart · git · cockpit/global/shared-parent · cloud/OAuth/secrets · browser automation · cron. curl read-only GET on :3000 is order-allowed. Only `.hermes` receipts written.

Status: **DISPATCHED** — running read-only two-root comparison.
