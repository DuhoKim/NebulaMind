# Method2 research-topics — Goru + Kun verification

Marker: AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z
Role: Method2 Goru (counts/scan) + Kun (deterministic validation). Read-only. UTC: 2026-07-08T09:06:48Z
Candidate dir: `…/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/`

## Overall: PASS

## Files + sha256
| file | bytes | sha256(16) |
|---|---|---|
| `research-topics-from-wiki-20260708T090359Z.html` | 17387 | `b5dc1b344bf85553` |
| `research-topics-from-wiki-20260708T090359Z.md` | 10214 | `eff3e105489a51a0` |
| `research-topic-map-20260708T090359Z.json` | 9155 | `7516023547e3b539` |
| `manifest-20260708T090359Z.json` | 695 | `17b44be0a5db99cf` |

## Goru — counts + scan
- **Topic count: 10** (within the 6–12 requirement); each card carries all six required fields (title, question, why-from-wiki, source-first basis, scope/limits, next docs-only action).
- Wiki-like structure: **ALL PRESENT** (title, method label, provenance note, TOC, topic cards, limitations, footer, the required "hypotheses/questions not accepted claims" caveat).
- Source-first linkage visible: accepted / accepted-limited / rejected / excluded, **28060 no-target**, **22-vs-21** caveat, **cite-unmatched** — all present.
- Static-safety: **CLEAN** (0 `<script>`/`fetch`/XHR/WebSocket/on-handler/external-URL/`/api/pages`/`page_versions`).
- **Product claim/cite comments: 0** (as required — topics reference claim/evidence IDs as plain text only).

## Kun — deterministic validation
- Links: 14 total = 4 file-relative (**0 broken** — back to the source wiki, its coverage map, the P1 ledger) + 10 in-page TOC anchors + **0 external**.
- **No invention:** claim IDs used ⊆ {2942–2947}; evidence IDs used ⊆ the known 36 ledger IDs; **0 new papers/cites/product bindings**.
- JSON validity: topic-map + manifest both parse; `topic_count`=10 consistent across map/manifest/HTML.

## Note
Topics are honestly framed as future-work hypotheses derived from the local source-first wiki (e.g., cite-unmatched→product-cite resolution, single-observation dependence of 2943, model-dependence of 2946, single-source stacking on 2947, M51 generalization, promoting 28060 positive-feedback, rejected-row reconsideration, stellar/AGN sufficiency boundary, removal-vs-recycling, abstract-only upgrade prioritization). Several explicitly point at gated steps (product DB / full-text verification / new observations) and say so.

## Safety ledger
Read-only verification + this report write only. 0 live-root · 0 restart · 0 DB/SQL · 0 /api/pages · 0 page_versions · 0 publish · 0 git · 0 cockpit/global · 0 cloud/OAuth · 0 browser · 0 cron · 0 P3 binding.
