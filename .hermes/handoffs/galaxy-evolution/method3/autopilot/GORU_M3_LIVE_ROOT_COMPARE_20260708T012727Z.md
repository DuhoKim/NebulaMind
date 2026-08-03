# Goru-role mechanical comparison — Method3 working-repo vs live-root

Order marker: `AUTOPILOT_LIVE_ROOT_EMPTY_WIKI_REPAIR_PACKET_20260708T012233Z`
Role performed: Method3 Hwao autopilot controller running the Goru-role bounded read-only mechanical comparison.
Scope: BOUNDED DOCS/STATIC, read-only (both roots + localhost HTTP). NO live-root mutation.
Status: **PASS** (comparison complete; exact M3 mirror determined; matches director packet)

Roots:
- SRC (working) = `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild`
- DST (live-served, :3000) = `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild`

## A. Per-file comparison (bytes + sha256)

| rel path | SRC bytes | SRC sha256 | DST state | action | verdict |
|---|---|---|---|---|---|
| `same-format-rebuild/` (dir) | — | — | ABSENT | mkdir | MISSING→CREATE |
| `same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | 24,402 | `a608347332b87fda3b497ed7acbbacc96aa2b4bbc922c9a11ebcfe17c19d6a80` | 404 (absent) | create | MISSING |
| `same-format-rebuild/page-content-20260707T064500Z.md` | 14,753 | `39bdd26ad0831f954e3a5e51ecfe3c800e899960d2d96e41b76668ec24fed9ff` | 404 (absent) | create | MISSING |
| `same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md` | 1,326 | `b8f209df25d7f28c0fabd3f50a7ffc0f6a5fd6abab4f61276bef38423f52f202` | 404 (absent) | create | MISSING |
| `wiki-page.html` | 18,383 | `75a08173d1f91bbe23dc69ac60ffeb02d84252b3af62a2b433aef38c3708bcc0` | 4,806 B (stub, `9ab44f2d…`) | replace stub | MISMATCH |
| `index.html` | 11,397 | `f0a2241f2eaebf1b4c4a8ef92a5d7d6a3f0f8e206d403654a58c493148291c2f` | 11,397 B, `f0a2241f…` | none | **SAME (exclude)** |
| `manifest.json` | 7,313 | `1d35b26f244a4c11b78e3ee83ecac57c345539209eba718eac6115d9ffa36c5c` | 7,313 B, `1d35b26f…` | none | **SAME (exclude)** |

**M3 mirror = 3 files created (new `same-format-rebuild/`) + 1 file replaced (`wiki-page.html` stub) + 1 `mkdir`.** index.html + manifest.json are byte-identical (working==live) and excluded.

## B. Served-HTTP evidence (:3000, read-only GET)

| URL (`…/debate-map-to-wiki-rebuild/…`) | HTTP now | note |
|---|---|---|
| `same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | **404** | live `same-format-rebuild/` absent |
| `wiki-page.html` | **200, 4,806 B** | stub draft canvas (308 words, 6 `<h2>`, title "Galaxy Evolution wiki draft") |

## C. Nature of the file being mirrored to `wiki-page.html` (WARN-level nuance, non-blocking)

The SRC `wiki-page.html` (18,383 B) that the mirror places at the live entry URL is **not empty** — it carries the **9 canonical same-format H2s** (Overview: Regulated Baryon Cycle … → Synthesis & Open Tensions) + 1 `<h1>`, but in the **P2 report-style shell** (title "Galaxy Evolution — Method 3 (Debate-map-to-wiki) P2 draft"; 4× "Method 3" + provenance chrome). The **cleaner canonical /wiki/[slug]-surface** page is the `same-format-rebuild/wiki-format-preview` (24,402 B, title "Galaxy Evolution · Method3 wiki-format preview", TOC `<h3>`, provenance chip, Reader/Evidence controls).
- Effect of the director's mirror: entry URL `wiki-page.html` serves the full P2 page (fixes the empty/stub); the cleaner canonical preview is additionally available at its own URL (fixes the 404). Both resolve the user's "empty/stub" complaint.
- Optional refinement (user choice, NOT required): if the user wants the *cleanest canonical surface* at the main entry URL, point `wiki-page.html` (or the index.html link) at the preview instead. Non-blocking; out of scope for the minimal safe mirror.

## D. Cross-check vs director final packet

Director `…_FINAL_NO_APPLY_PACKET.md` M3 section: all 4 M3 rows (page-content 14,753/`39bdd26…`, preview 24,402/`a608347…`, manifest 1,326/`b8f209d…`, wiki-page 4,806→18,383/`75a08173…`) and the index.html+manifest.json SAME-exclusion **match this independent measurement exactly**. No discrepancy.

## Verdict

**PASS** — M3 live-root gap fully diagnosed and pinned: 3 missing `same-format-rebuild/` artifacts (404) + 1 stub `wiki-page.html` (4,806 B) to replace with the working 18,383-B page; index.html/manifest.json identical (excluded). Safe static file copy; target fully determined without any unsafe action. Director packet M3 evidence corroborated exactly.

## Safety ledger

Read-only `wc`/`shasum`/`ls`/`find` on both roots + read-only localhost `curl` GETs + this one method-local report. Zero live-root writes/copies; zero DB/`/api/pages`/`page_versions`/publish/deploy/restart/git/cockpit/global/shared-parent/cloud/OAuth/browser/cron; zero P3 binding.
