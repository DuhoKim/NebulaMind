# Hwao-led corrective order — live-root empty wiki pages repair packet

Marker: `AUTOPILOT_LIVE_ROOT_EMPTY_WIKI_REPAIR_PACKET_20260708T012233Z`

## Why this order exists

User checked the resulted Galaxy Evolution wiki pages and found most of them empty/stub-like. Tori verified the mismatch:

- Running local public site process on port 3000 is `next start` from:
  `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend`
- Prior M1/M2/M3 autopilot verified artifacts under the working repo:
  `/Users/duhokim/NebulaMind/NebulaMind/frontend`
- Example mismatch:
  - repo M1 `wiki-page.html`: 29,063 bytes, full method wiki page
  - served/live-root M1 `wiki-page.html`: 5,269 bytes, stub/empty-looking draft canvas
- Same-format preview URLs under `/agent-reports/.../same-format-rebuild/...` return 404 on port 3000 because the live root does not have the rebuilt artifacts.

Therefore the previous COMPLETE was scoped to static artifacts in the working repo, not to the user-visible served root. Treat that as an incomplete deliverable from the user's perspective.

## Goal

Keep M1/M2/M3 active again, but stay safe:

1. Independently compare working-repo artifacts vs live-root served/static artifacts for all three methods.
2. Confirm exactly which files must be mirrored or patched for the user-visible static method pages/previews to show the completed content.
3. Produce a no-apply exact repair packet under `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/` with:
   - source path
   - target live-root path
   - byte size / checksum before and after
   - expected served URL
   - validation command
   - clear user approval gate wording for applying the mirror/patch.
4. Do not mutate the live root yet. Do not restart/deploy. Do not publish to product wiki DB/API.

## Required final artifact

Write:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot/AUTOPILOT_LIVE_ROOT_EMPTY_WIKI_REPAIR_PACKET_20260708T012233Z_FINAL_NO_APPLY_PACKET.md`

It must contain:
- `STATUS: READY_FOR_USER_APPROVAL` if the exact mirror/patch is safe and fully specified.
- `STATUS: HARD_BLOCKED` only if the target cannot be determined without an unsafe action.
- The marker `AUTOPILOT_LIVE_ROOT_EMPTY_WIKI_REPAIR_PACKET_20260708T012233Z`.
- Plain English: what happened, result, what would change, exact next action.

## Method lane assignments

- Hwao-director: coordinate, own final no-apply packet.
- Method1: compare packet-gated method files between working repo and live root; write method1 receipt.
- Method2: compare source-first method files between working repo and live root; write method2 receipt.
- Method3: compare debate-map method files between working repo and live root; write method3 receipt.
- Goru lanes: mechanical counts/checks only: file exists, byte counts, hashes, served URL status/word counts.

## Scope allowed without further approval

Allowed:
- read-only inspection of both roots:
  - `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/`
  - `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/`
- read-only HTTP checks against `http://127.0.0.1:3000/agent-reports/...`
- writing `.hermes` handoff/receipt/no-apply packet files only.

Hard denied until explicit user approval:
- writing or copying into `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/...`
- product DB/SQL
- `/api/pages` / `page_versions` / live wiki publish
- deploy/restart/service mutation
- git commit/push/merge/rebase/reset
- public cockpit/global/shared-parent mutation
- cloud/API/billing/OAuth/token/secrets/credentials
- browser automation
- cron

## Stop condition

Do not stop after one lane receipt. Continue until the final no-apply packet exists at the required path and says either `READY_FOR_USER_APPROVAL` or `HARD_BLOCKED`.
