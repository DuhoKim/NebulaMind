# Goru-role mechanical check — Method3 evidence + trust candidate

Order marker: `AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z`
Role performed: Method3 Hwao autopilot controller running the Goru-role bounded read-only mechanical checks.
Scope: BOUNDED DOCS/STATIC, read-only. NO live-root mutation, NO product binding.
Status: **PASS**

## A. Candidate artifacts (exist + non-empty), working-repo, order-named subdir `evidence-trust-rebuild/`

| file | bytes | role |
|---|---|---|
| `page-content-evidence-trust-20260708T014205Z.md` | 17,173 | narrative + per-section trust chips + evidence links |
| `wiki-format-preview-evidence-trust-20260708T014205Z.html` | (rebuilt) | static preview: trust summary + per-section chips + evidence panels |
| `evidence-basis-20260708T014205Z.md` | 8,091 | local provenance & trust ledger (link target) |

## B. Structure / same-format conformance (HTML preview)

| check | result |
|---|---|
| `<h1>` | 1 |
| article `<h2 id=…>` | 9 (exact canonical order) |
| **raw `<h2>` total** | **9** (no chrome `<h2>` leak — trust-summary + TOC headings are `<h3>`) |
| `<h3>` | 2 (`Contents` rail + `Trust & evidence summary` panel) |
| product `<!--claim:-->` / `<!--cite:-->` | 0 / 0 (correct — M3 docs-only) |

page-content MD: 1 H1, 9 H2, 9 per-section `**Trust:**` lines, 11 evidence-basis links.

## C. Evidence links + trust leveling (the requested additions)

| check | count |
|---|---|
| trust chips rendered (`.chip`) | 23 (page legend + per-section) |
| evidence-basis links (`.ev-link`) | 13 |
| clickable links to local ledger `evidence-basis-…md` | 11 (HTML) / 11 (MD) |
| unbound/unmatched labels shown | 4 (`2915/2921/2913`, `2133→2605.22497`, `2374`, baseline PENDING_RECHECK) |
| evidence-basis sidecar anchors `#s1…#s9` | 9/9 present |

Trust leveling is plain-English + visible: page-level trust summary panel + per-section chips derived from **real** debate-map axis statuses (`widely_supported` / `emerging_sample_limited` / `actively_debated` / `contradicted_or_model_dependent`) and coverage scope. No invented trust levels/IDs.

## D. Static-safety scan (all must be 0) — PASS

`<script`=0, `fetch(`=0, `XMLHttpRequest`=0, `WebSocket`=0, `onclick=`=0, `onload=`=0, `/api/pages`=0, `page_versions`=0, external `http://`=0, `https://`=0. Fully self-contained static HTML; evidence links are local relative paths only.

## E. Served-HTTP note (expected 404 — working-repo candidate)

On :3000 the three new candidate URLs return **404** — expected, because :3000 serves the **live root** (`NebulaMind-origin-main-live/frontend`), and these are **working-repo** candidates (per order: additive working-repo static candidates). Serving them requires the separate, user-approval-gated live-root mirror. No mirror performed.

## F. Preservation

Old `wiki-page.html` (18,383 B) and the `same-format-rebuild/` preview are **untouched/preserved**. New artifacts are additive under `evidence-trust-rebuild/`.

## G. Honesty / no-invention

All source IDs, claim IDs, axis statuses, and trust levels trace to existing local ledgers (`status_debate_map.json`, `debate_map_data.json`, `evidence_source_inventory.json`, Lana P2 author report §6). 0 product claim/cite markers — no pretend binding. Known unmatched items surfaced explicitly, not hidden. Nothing invented.

## Verdict

**PASS** — M3 evidence + trust candidate is complete, same-format conformant (9 H2s, TOC `<h3>`), static-safe (0 scripts/fetch/API/external URLs), and honest (trust = real debate-map status; evidence links → local provenance ledger; 0 product binding; unmatched items flagged). Ready for the Hwao verdict + no-apply live-root mirror gate.

## Safety ledger

Read-only mechanical checks + candidate authoring under the order-named working-repo subdir + this report. Zero live-root writes; zero DB/`/api/pages`/`page_versions`/publish/deploy/restart/git/cockpit/global/shared-parent/cloud/OAuth/browser/cron; zero product P3 binding; zero invented IDs.
