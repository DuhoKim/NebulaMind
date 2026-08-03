# Method1 — research-topics specificity-pass verdict / receipt (COMPLETE)

## Status: PASS / COMPLETE

Order marker: AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z
Lane: Method1 Hwao. UTC: 2026-07-08T11:0xZ

## Exact files written (overwrote the proposal set)
Dir: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/`
| File | Bytes | sha256[:12] |
|------|------:|-------------|
| `research-topics-from-wiki-20260708T090359Z.html` | 15,780 | `274efb43aeda` |
| `research-topics-from-wiki-20260708T090359Z.md` | 10,690 | `2f259b3df66e` |
| `research-topic-map-20260708T090359Z.json` | 9,995 | `4c56b629716d` |
| `manifest-20260708T090359Z.json` | 674 | `0c44aca4d863` |

## Required validation (§120–128)
- **Proposal count:** 6 (5–8).
- **Cards with each key section:** `What studies already show` 6/6 · `What remains unknown` 6/6 · `Survey/data plan` 6/6 · `Analysis/test` 6/6 (also `Research question`, `Expected result or decision point`, `Caveats`, `Provenance` 6/6).
- **Product claim/cite comments:** 0 / 0.
- **Static safety:** PASS — 0 scripts, fetch/XHR/WebSocket, on* handlers, forms, external links/assets/hosts.
- **Hard-excluded surfaces touched:** 0.
- **JSON valid:** topic map + manifest both valid.
- Supporting mechanical check: `GORU_M1_SPECIFICITY_CHECK_20260708T105800Z.md` (PASS).

## Specificity proof (§125) — generic → concrete (≥2)
**Example 1 — RP-1 (AGN causal test).**
- Before (general proposal): "Establish whether AGN feedback causally regulates or shuts down star formation, rather than merely correlating with quiescence."
- After (specific): *What studies show* — the source basis is non-committal on a direct causal link, records kinetic-mode jets/outflows as the mechanism, and discusses rapid AGN-linked shutdown at cosmic noon. *What remains unknown* — whether a matched population shows a star-formation deficit tied to AGN energy, and which gas phase responds. *Data→measurement* — MaNGA/MUSE (resolved SF response), ALMA CO (molecular fuel + depletion time), Chandra/XMM (X-ray AGN energy), VLA/LOFAR (jet power/duty cycle). *Test* — matched AGN vs non-AGN controls as a function of AGN power/mode. *Decision* — a calibrated SF deficit with a sufficient (or insufficient) energy budget.

**Example 2 — RP-3 (maintenance heating).**
- Before (general): "Find direct observational support for sustained AGN heating as a maintenance mechanism."
- After (specific): *What studies show* — maintenance heating is reported but simulation-dependent; direct cavity/hot-halo observations are sparse in the basis. *What remains unknown* — the observed frequency and time-averaged sufficiency of heating vs cooling across a mass-selected population. *Data→measurement* — Chandra (cavity mechanical power), XMM/eROSITA (hot-halo cooling luminosity), VLA/LOFAR (radio duty cycle), IllustrisTNG/HORIZON-AGN as benchmark. *Test* — cavity/heating power vs cooling luminosity across a mass-selected sample. *Decision* — an observed bound on how often heating balances cooling.

(Similar generic→concrete upgrades applied to RP-2 environmental-quenching denominators, RP-4 evidence-gap ranking, RP-5 distinct-study recount, RP-6 acceptance thresholds.)

## Grounding / no invention (§31)
"What studies already show" bullets reflect only what the M1 source basis reports; where support is simulation-only (RP-3) or non-committal (RP-1), the card says so. Real counts used (43 records → 26 distinct studies; 2 of 9 sections evidenced) come from the M1 coverage map — not invented. No fabricated paper titles, DOIs, numeric results, or source IDs; claim IDs demoted to provenance.

## Not done, by design
Director final rollup at `mastermind/autopilot/AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z_FINAL_NO_APPLY_PACKET.md` NOT written — director's cross-method deliverable. M1's row is ready (paths, sha, proposal count 6, section counts 6/6, static-safe PASS, product-binding 0/0).

## Safety ledger
DB/SQL 0 · /api/pages 0 · page_versions/publish 0 · live-root write 0 · restart 0 · deploy 0 · git 0 · cockpit/global/shared-parent 0 · cloud/OAuth/secrets 0 · browser 0 · cron 0 · M3 P3 0 · invented evidence/IDs 0. Writes: M1 research-topics dir (overwrite, allowed) + method1 `.hermes` receipts.

Status: **M1 COMPLETE** — specificity revision produced and verified; ready for the director's rollup.
