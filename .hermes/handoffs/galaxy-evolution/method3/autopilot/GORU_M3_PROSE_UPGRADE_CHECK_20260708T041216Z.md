# Goru-role mechanical check — Method3 prose/evidence/trust upgrade

Order marker: `AUTOPILOT_PROSE_EVIDENCE_TRUST_WIKI_UPGRADE_20260708T041216Z`
Role performed: Method3 Hwao autopilot controller running the Goru-role bounded read-only mechanical checks.
Scope: BOUNDED DOCS/STATIC, read-only. Status: **PASS**

## A. Candidate files (all 4 present + non-empty), `prose-evidence-trust-upgrade/`

| file | bytes | sha256 |
|---|---|---|
| `wiki-prose-evidence-trust-upgrade-20260708T041216Z.html` | 22,759 | `dcf96b624fc6da0eb05f36ffce34d603e8b4f7213cbf962238c325a661419821` |
| `page-content-prose-evidence-trust-upgrade-20260708T041216Z.md` | 15,464 | `2ef48ddce55e734ad920853e4d07ca480079fe309c6e4880fbc4c20dde53905b` |
| `evidence-trust-coverage-map-20260708T041216Z.json` | 6,803 | `0ad1a638f507eab06200e2763935a545b6c7a4c25490686149855868c0d96500` |
| `manifest-20260708T041216Z.json` (Kun/Codex) | 3,377 | `750dcebc6676ded320575359c9711edc50f10c22ef1221176862afab73d04232` |

## B. Prose + evidence + trust coverage (the requested upgrade)

| check | result |
|---|---|
| HTML explanatory lead + trust-vocabulary panel | present |
| HTML article `<h2>` | 10 = **9 canonical sections + 1 "Conclusion & limitations"** (intentional per order §1) |
| HTML `<h3>` (chrome) | 2 (trust-vocab panel + TOC "Contents") — no unintended chrome `<h2>` leak |
| per-section **evidence boxes** | 9 (one per content section), each with **Supported by (9) / Limited by (9) / Unbound-Unmatched (9)** fields |
| trust chips | 23 (page legend + per-section, from real axis statuses) |
| evidence links (local) | 12 `ev-link`; 11 to the local ledger `../evidence-trust-rebuild/evidence-basis-…md#sN` |
| coverage-map JSON | valid; 9 sections; real axes/statuses/claim IDs; 3 unmatched items recorded |
| page-content MD | 1 H1, 9 H2, 9 per-section trust-framing + local-provenance blocks |

## C. Static-safety (all must be 0) — PASS

`<script`=0, `fetch(`=0, `XMLHttpRequest`=0, `WebSocket`=0, `onclick=`=0, `onload=`=0, `onerror=`=0, `/api/pages`=0, `page_versions`=0, external `http://`=0, `https://`=0. Fully self-contained static HTML; all evidence links are local relative paths (no external arXiv URLs added for M3).

## D. Honesty / no-invention — PASS

Product markers: **0 claim / 0 cite** in HTML and MD (correct — M3 docs-only). All source/claim IDs, axis statuses, and trust labels trace to the named local ledgers (verified by Kun's P2 repro + this run). 3 unmatched items disclosed explicitly (`2915/2921/2913`; `2133→2605.22497`; `2374`) + `PENDING_RECHECK` baseline. Trust vocabulary is explicitly M3's debate-map scale, stated as distinct from M1/M2.

## E. Served + preservation

- Served :3000 candidate URL = **404** (expected — working-repo candidate; live root is a separate checkout; per order §, 404 is not a failure).
- Preserved (untouched): `wiki-page.html` (18,383 B), `same-format-rebuild/`, `evidence-trust-rebuild/`. New files additive under `prose-evidence-trust-upgrade/`.

## Verdict

**PASS** — M3 prose/evidence/trust upgrade candidate is complete (prose-rich lead + per-section narrative + 9 evidence boxes + on-page trust vocabulary + conclusion/limitations), static-safe (0 scripts/fetch/API/external URLs), honest (0 product binding; unmatched items flagged; trust = real debate-map status), and additive (old artifacts preserved).

## Safety ledger

Read-only mechanical checks + this report. Zero live-root writes; zero DB/`/api/pages`/`page_versions`/publish/restart/deploy/git/cockpit/global/shared-parent/cloud/OAuth/browser/cron; zero product P3 binding; zero invented IDs.
