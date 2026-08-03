# Method2 — live-root vs working-repo comparison receipt

Marker: AUTOPILOT_LIVE_ROOT_EMPTY_WIKI_REPAIR_PACKET_20260708T012233Z
Role: Method2 Hwao/Goru lane — read-only comparison + served-URL check. No live-root mutation, no restart.
Snapshot UTC: 2026-07-08T01:45:01Z
Roots:
- WORK (source-of-truth): `…/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication`
- LIVE (served :3000): `…/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication`

## STATUS: PARTIAL — disk parity COMPLETE; served previews BLOCKED on a user-gated restart.

## 1. Disk comparison (byte + sha256) — as of snapshot

| file | WORK | LIVE | verdict |
|---|---|---|---|
| `wiki-page.html` | 28665 B · sha 71dd8817 | 28665 B · sha 71dd8817 | IDENTICAL |
| `same-format-rebuild/page-content-20260707T064500Z.md` | 13049 B · sha 74be7831 | 13049 B · sha 74be7831 | IDENTICAL |
| `same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | 24423 B · sha 4ec687fd | 24423 B · sha 4ec687fd | IDENTICAL |
| `same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md` | 1343 B · sha 5ae8f398 | 1343 B · sha 5ae8f398 | IDENTICAL |
| `manifest.json` | 9458 B · sha 8f234be5 | 9458 B · sha 8f234be5 | IDENTICAL |

All Method2 static files now match between roots, and the checksums equal the SRC checksums pinned in the
director no-apply packet (M2 `wiki-page.html` sha `71dd8817…`, preview `4ec687fd…`, etc.). **The Method2 mirror
has therefore been applied to the live root** (the live `same-format-rebuild/` dir, absent earlier, now exists
with identical files; mtimes preserved → a `cp -p`-style copy).

## 2. Sequence observed (surfaced faithfully)

- Director no-apply packet (~01:16Z) recorded LIVE M2 `wiki-page.html` as a **7,374 B stub** with
  `same-format-rebuild/` **absent**, STATUS `READY_FOR_USER_APPROVAL`, "live root untouched."
- My first read (~01:33Z) confirmed that stub state (7,374 B, no `same-format-rebuild/`).
- My checksum snapshot (~01:45Z) shows LIVE fully mirrored (== WORK).

So the mirror was applied by another actor **between ~01:33Z and 01:45Z**, i.e. during the no-apply window that
the director packet said required explicit user approval first. **This Method2 lane did not apply it** (safety
ledger: 0 live-root writes). If the user approved the apply, this is expected; if not, it deviates from the
packet's "DO NOT run without user OK" and should be reconciled by Hwao-director. Flagging, not adjudicating.

## 3. Served-URL check on :3000 (read-only HTTP GET) — the material finding

| served URL (`…/source-first-paper-adjudication/…`) | result |
|---|---|
| `wiki-page.html` | **200, 28665 B** — full completed page now served ✓ |
| `same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | **404** |
| `same-format-rebuild/page-content-20260707T064500Z.md` | **404** |

**The previews still 404 even though the files are present and identical on disk in the live root.** This
disproves the no-apply packet's assumption that "`next start` serves `public/` directly from disk → copied files
are served immediately, no restart." A running `next start` does **not** hot-serve a `public/` subdirectory
created after the server booted. Therefore:

- `wiki-page.html` repair is **effective** (it replaced an existing served file → served immediately).
- `same-format-rebuild/` previews are **on disk but unreachable** until the `:3000` server is **restarted**.

## 4. Exact remaining action for full Method2 served completeness

- Disk mirror: **already satisfied** for Method2 (no further copy needed).
- To make the 2 Method2 preview URLs return 200: **restart the `:3000` `next start` process** (PID served from
  `NebulaMind-origin-main-live/frontend`). **This is a HARD-GATE action (deploy/restart) — user-gated. Not done here.**
- Validation after restart: `GET …/same-format-rebuild/wiki-format-preview-20260707T064500Z.html` → 200/24423 B;
  `GET …/same-format-rebuild/page-content-20260707T064500Z.md` → 200/13049 B.

## Conclusion
Method2 static-content parity between working repo and live root is COMPLETE; `wiki-page.html` serves correctly.
The only residual gap is that the mirrored `same-format-rebuild/` previews need a **server restart** to be served
(user-gated) — a gap the cross-method no-apply packet under-specified (it assumed no restart). Recommend the
director packet add a "restart :3000 after mirror" step or serve the previews via the already-live `wiki-page.html`.

## Safety ledger
- live-root writes/copies: 0 · server restart/deploy: 0 · DB/SQL: 0 · /api/pages / page_versions / publish: 0
- git: 0 · cockpit/global/shared-parent: 0 · cloud/GCP/API/billing/OAuth/token: 0 · browser: 0 · cron: 0
- actions this pass: read-only byte/sha compare of both roots + 3 read-only HTTP GETs on :3000 + this receipt write.
