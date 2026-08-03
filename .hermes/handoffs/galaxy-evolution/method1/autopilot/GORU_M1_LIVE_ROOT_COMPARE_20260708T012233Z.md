# Goru — Method1 live-root vs working-repo mechanical comparison

Order marker: AUTOPILOT_LIVE_ROOT_EMPTY_WIKI_REPAIR_PACKET_20260708T012233Z
Continuation marker: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Lane: Method1 Goru (mechanical, read-only). Authored UTC: 2026-07-08T01:29:11Z
Roots:
- WORKING = `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution`
- LIVE = `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution` (served by `next start` on :3000)

## M1 file-by-file diff (bytes / sha256[:12])
| File (relative to method dir) | WORKING | LIVE | Result |
|---|---|---|---|
| `wiki-page.html` | 29,063 / `0a4c56cb1822` | 5,269 / `299115c0945d` | **DIFF** (live = old "Draft not yet filled" stub) |
| `index.html` | 17,899 / `779ead26b26c` | 16,930 / `9f0f4da38a2d` | **DIFF** |
| `same-format-rebuild/page-content-20260707T064500Z.md` | 14,486 / `3e108589bcd7` | — | **LIVE_MISSING** |
| `same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | 24,033 / `425a4335a9db` | — | **LIVE_MISSING** |
| `same-format-rebuild/` (dir) | present (3 files) | **absent** | LIVE_MISSING |

## M1 served-URL HTTP status on :3000 (read-only GET)
| URL (under `/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/`) | Code | Bytes | Note |
|---|---|---|---|
| `wiki-page.html` | 200 | 5,269 | serves the stub; `<title>…wiki draft…</title>`, "Draft not yet filled", 343 words |
| `same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | **404** | 19,504 | Next.js 404 body |
| `same-format-rebuild/page-content-20260707T064500Z.md` | **404** | 19,495 | Next.js 404 body |

## Finding (mechanical)
The user-visible M1 page on :3000 is the pre-build stub, and all M1 same-format-rebuild artifacts 404 because the live root lacks them. To make the served M1 page show the completed content, the live root must receive (mirror from WORKING):
1. `wiki-page.html` (29,063 B) — replace 5,269 B stub
2. `index.html` (17,899 B) — replace 16,930 B (workspace directory overview; working copy is newer)
3. `same-format-rebuild/page-content-20260707T064500Z.md` (14,486 B) — create
4. `same-format-rebuild/wiki-format-preview-20260707T064500Z.html` (24,033 B) — create
5. `same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md` — create (dir completeness; optional)

Status: **PASS (diagnosis complete, read-only)** — exact M1 mirror set identified. No live-root write performed.
