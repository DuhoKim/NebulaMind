# Final no-apply repair packet — live-root empty Galaxy Evolution wiki pages

Marker: AUTOPILOT_LIVE_ROOT_EMPTY_WIKI_REPAIR_PACKET_20260708T012233Z
Order: `mastermind/AUTOPILOT_LIVE_ROOT_EMPTY_WIKI_REPAIR_PACKET_20260708T012233Z.md`
Author: Hwao-director (pane %107). Written 2026-07-08 ~01:16Z (10:16 KST).
Basis: independent read-only comparison of both repo roots + read-only HTTP checks on :3000. No live-root mutation performed.

## STATUS: READY_FOR_USER_APPROVAL

The mismatch is fully diagnosed and the exact fix is a **safe static file copy** (15 files + 3 dirs) from the working repo into the live-served repo's `public/`. Target paths, byte sizes, and sha256 checksums are all pinned below. No build, deploy, restart, git, DB, or product-wiki publish is required or involved. NOT hard-blocked — the target is fully determined without any unsafe action.

## What happened (plain English)

The completed Galaxy Evolution static wiki pages were built and verified in the **working repo** (`/Users/duhokim/NebulaMind/NebulaMind/frontend`), but the site the user sees on **:3000** is `next start` serving a **different checkout** — the live repo `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend` (confirmed: node PID 88217 listening on :3000; root returns 200). That live root is behind: its method pages are old stubs and it has **no `same-format-rebuild/` directory at all**. So the user sees empty/stub pages and 404s even though the work is complete in the working repo. The earlier "COMPLETE" ratification was true for the working-repo artifacts but never reached the user-visible served root.

## Result (measured evidence)

Served on :3000 (from the live root) vs the completed working-repo files:

| Served URL (`/agent-reports/wiki-method-results/galaxy-evolution/…`) | served now | working-repo file | gap |
|---|---|---|---|
| M1 `…/packet-gated-paper-to-wiki-reconciliation/wiki-page.html` | **200, 5,269 B** (stub) | 29,063 B | stale stub |
| M1 `…/packet-gated…/same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | **404** | 24,033 B | missing |
| M1 `…/packet-gated…/same-format-rebuild/page-content-20260707T064500Z.md` | **404** | 14,486 B | missing |
| M2 `…/source-first-paper-adjudication/wiki-page.html` | **200, 7,374 B** (stub) | 28,665 B | stale stub |
| M2 `…/source-first…/same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | **404** | 24,423 B | missing |
| M2 `…/source-first…/same-format-rebuild/page-content-20260707T064500Z.md` | **404** | 13,049 B | missing |
| M3 `…/debate-map-to-wiki-rebuild/wiki-page.html` | **200, 4,806 B** (stub) | 18,383 B | stale stub |
| M3 `…/debate-map…/same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | **404** | 24,402 B | missing |
| M3 `…/debate-map…/same-format-rebuild/page-content-20260707T064500Z.md` | **404** | 14,753 B | missing |

Live-root `same-format-rebuild/` directory: **MISSING for all three methods.**

## What would change (the exact mirror — NO-APPLY spec)

Copy the completed static artifacts from SOURCE (working repo) to TARGET (live repo). Two constants:
- SRC base = `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution`
- DST base = `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution`

For every file: after-copy target size = source size and after-copy target sha256 = source sha256 (both listed). Files marked SAME already match live and are **excluded** (no action).

### Method 1 — `packet-gated-paper-to-wiki-reconciliation` (6 files; incl. new `same-format-rebuild/`)
| rel path | action | before (live) | after (=src) bytes | src sha256 |
|---|---|---|---|---|
| `same-format-rebuild/` (dir) | mkdir | absent | — | — |
| `same-format-rebuild/page-content-20260707T064500Z.md` | create | 404 | 14,486 | `3e108589bcd7256640ac9ec5245cd2ba37c1681c0e4941daffbb757258dc453d` |
| `same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | create | 404 | 24,033 | `425a4335a9db0161bf9a4799ed6f6655e4838d9f4d7e43ae331ab92b1608a3eb` |
| `same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md` | create | 404 | 1,373 | `e721624cb1da2fff30a348da34bbaa3acac4aefc46f4c78e2908c0b3cee1f7d0` |
| `wiki-page.html` | replace stub | 5,269 | 29,063 | `0a4c56cb18220d7743b2fa6470bea190746f081eb60058156b4c1fdc1bfcff8e` |
| `index.html` | replace | 16,930 | 17,899 | `779ead26b26c2efb68b4ceb8659198bef9d4eb92d240ac208c05f75c20b82ca8` |
| `manifest.json` | replace | 13,467 | 14,713 | `3a0e2da246e192501241151ea7520d2191ea966a02a541f508e90c68ef3bdaad` |

### Method 2 — `source-first-paper-adjudication` (5 files; `index.html` already SAME → excluded)
| rel path | action | before (live) | after bytes | src sha256 |
|---|---|---|---|---|
| `same-format-rebuild/` (dir) | mkdir | absent | — | — |
| `same-format-rebuild/page-content-20260707T064500Z.md` | create | 404 | 13,049 | `74be783159bea56ea5845415755953c249e89d6ff5e382b38d8d0f7dfd6e95d7` |
| `same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | create | 404 | 24,423 | `4ec687fd52f1d6183204bd3e078a222e3a4535fab14a57115f33b2eff7cce010` |
| `same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md` | create | 404 | 1,343 | `5ae8f398883c4ff3fc2f875c524d7baa9cfe7091b8014c4c5e9ad369e72fe8e7` |
| `wiki-page.html` | replace stub | 7,374 | 28,665 | `71dd881757b8fad9085258478d151781e0b7497b6187534b7c6b10b486e7649f` |
| `manifest.json` | replace | 9,560 | 9,458 | `8f234be5e57b5327b461e989e1b4755d197d8907325c097c02a98c46ec6d7d36` |

### Method 3 — `debate-map-to-wiki-rebuild` (4 files; `index.html` + `manifest.json` already SAME → excluded)
| rel path | action | before (live) | after bytes | src sha256 |
|---|---|---|---|---|
| `same-format-rebuild/` (dir) | mkdir | absent | — | — |
| `same-format-rebuild/page-content-20260707T064500Z.md` | create | 404 | 14,753 | `39bdd26ad0831f954e3a5e51ecfe3c800e899960d2d96e41b76668ec24fed9ff` |
| `same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | create | 404 | 24,402 | `a608347332b87fda3b497ed7acbbacc96aa2b4bbc922c9a11ebcfe17c19d6a80` |
| `same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md` | create | 404 | 1,326 | `b8f209df25d7f28c0fabd3f50a7ffc0f6a5fd6abab4f61276bef38423f52f202` |
| `wiki-page.html` | replace stub | 4,806 | 18,383 | `75a08173d1f91bbe23dc69ac60ffeb02d84252b3af62a2b433aef38c3708bcc0` |

Total: **15 files + 3 `mkdir`.** Files excluded as already-matching: M2 `index.html`, M3 `index.html`, M3 `manifest.json`.

## Scope boundary — what this mirror does and does NOT do

- **Does:** make the served **static** `/agent-reports/wiki-method-results/galaxy-evolution/…` URLs on :3000 return the completed content (200 with full pages; previews stop 404ing). Because `next start` serves `public/` directly from disk, copied files are served **immediately, with no rebuild/restart**.
- **Does NOT:** touch the product wiki (`/wiki/[slug]`, `/api/pages`, `page_versions`, DB). Publishing the pages into the live product wiki remains a **separate** future user gate (DB/API/page_versions) and is not part of this repair.

## Exact next action (approval-gated apply plan — DO NOT run without user OK)

1. **Backup first** (reversibility): copy the current live stubs being replaced to a timestamped backup dir under the live root (e.g. `…/galaxy-evolution/_backup_before_mirror_<UTC>/`) — the 3 `wiki-page.html` stubs, M1 `index.html`+`manifest.json`, M2 `manifest.json`.
2. `mkdir -p` the 3 `same-format-rebuild/` target dirs.
3. `cp` the 15 files SRC→DST per the tables above.
4. **Validate:** for each of the 15, `shasum -a 256 <dst>` must equal the listed src sha256; and re-run the served-URL checks — every URL in the Result table returns **200** with bytes matching the working-repo file (previews no longer 404).

## Validation commands (run after apply)
- Checksum parity: `shasum -a 256 <DST/rel>` == src sha256 (per table).
- Served re-check: `curl -s -o /dev/null -w '%{http_code} %{size_download}B\n' http://127.0.0.1:3000/agent-reports/wiki-method-results/galaxy-evolution/<dir>/<rel>` → expect `200 <workingbytes>B` for all 9 URLs in the Result table (+ the 3 page-content URLs).

## User approval gate wording (explicit)

> "Approve mirroring the 15 completed Galaxy Evolution static files (+3 `same-format-rebuild/` dirs) from the working repo into the live-served repo `NebulaMind-origin-main-live/frontend/public/…`, replacing 3 stub `wiki-page.html` + 3 landing files and adding the 9 missing `same-format-rebuild/` artifacts, after backing up the replaced live files. This is a static file copy served immediately by the existing `next start` — **no** build, deploy, restart, git, DB, `/api/pages`, `page_versions`, or product-wiki publish. Reversible from the backup. Publishing into the live product wiki remains a separate gate."

Approving that sentence authorizes only the copy-into-live-root step above. Nothing else.

## Safety ledger (this packet)

Read-only comparison of both roots (bytes + sha256), read-only HTTP GETs on :3000, and this one `.hermes` no-apply packet write. **Zero** writes/copies into the live root; zero product DB/SQL, `/api/pages`, `page_versions`, live-wiki publish, deploy/restart, git, public cockpit/global/shared-parent, cloud/OAuth/secrets, browser, cron; zero Method3 P3 binding. All hard gates remain closed; the live root is untouched.

AUTOPILOT_LIVE_ROOT_EMPTY_WIKI_REPAIR_PACKET_20260708T012233Z
