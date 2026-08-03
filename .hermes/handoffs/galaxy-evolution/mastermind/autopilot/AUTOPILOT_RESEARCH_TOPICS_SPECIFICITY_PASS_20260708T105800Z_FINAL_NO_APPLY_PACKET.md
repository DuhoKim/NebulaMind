# Final no-apply rollup — research-topics specificity pass

Marker: AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z
Author: Hwao-director (pane %107). Written 2026-07-08T11:07Z (20:07 KST).
Basis: three method-team in-place revisions of the `research-topics-from-wiki-20260708T090359Z` **wiki**-derived pages + method receipts + this director's independent read-only verification.

## Status: COMPLETE

The three method research-topic pages were revised from general proposal agendas into **specific, evidence-aware** research agendas. Every proposal card now states what prior studies/the method source basis already show, what remains unknown, a named-data measurement plan, and a decisive analysis/test — static-safe, no invented findings, no product bindings. Working-repo only (no autopilot live-root mirror).

## Per-method proposal + section counts (director-verified, read-only)

Revised in place at `…/galaxy-evolution/<method>/research-topics-from-wiki-20260708T090359Z/`.

| Method | proposals | required card sections | literal extra mentions | named-data mentions | static-safe | product claim/cite | jargon | HTML bytes / sha256(12) |
|---|---|---|---|---|---|---|---|---|
| **M1** | 6 | ✅ 6/6 cards have `What studies already show` + `What remains unknown` + `Survey/data plan` + `Analysis/test` | none | 32 | ✅ | 0/0 | 0 | 15,780 / `274efb43aeda` |
| **M2** | 6 | ✅ 6/6 cards have `What studies already show` + `What remains unknown` + `Survey/data plan` + `Analysis/test` | 1 intro mention of `What studies already show` | 41 | ✅ | 0/0 | 0 | 18,812 / `41be81e62f97` |
| **M3** | 6 | ✅ 6/6 cards have `What studies already show` + `What remains unknown` + `Survey/data plan` + `Analysis/test` | appendix/scope repeat the section terms | 52 | ✅ | 0/0 | 0 | 21,176 / `2892a253c3b3` |

Sidecars (sha256(12)/bytes): M1 map `4c56b629716d`/9,995 · md `2f259b3df66e`/10,690 · manifest `0c44aca4d863`/674. M2 map `e22b9d5ecd89`/12,434 · md `b4fac4ffaaa8`/12,807 · manifest `5dbf196dbd9f`/852. M3 map `9483f4c586a7`/6,632 · md `ccf59b6a1b1f`/10,115 · manifest `95121bc2ce92`/2,398.

## How the pages became more specific
Each card gained a `What studies already show` paragraph (2–4 concrete prior findings in plain words, IDs moved to provenance), a direct `What remains unknown` gap statement (variable/scale/denominator/population/redshift/gas-phase/selection), a `Survey/data plan` that ties each named data family to a specific measurement (e.g. ALMA→molecular gas/depletion; Chandra/XMM/eROSITA→cavities & cooling; VLA/LOFAR→jet power/duty cycle; DESI/COSMOS/Euclid/Rubin→matched denominators; JWST/MOSDEF→high-z outflows; TNG-style sims→forward-modeled counterfactuals), and an `Analysis/test` naming the actual comparison. Surveys are labeled proposed data, not existing evidence. Weak/simulation-only support is flagged as such. Method receipts each carry ≥2 generic→specific before/after examples.

## Static validation
All three HTML: 0 `<script>`/`fetch(`/`onclick`/`<form>`/external hosts; product claim/cite comment counts **0/0**; hard-excluded surfaces touched **0**; no invented paper titles/DOI/ADS/numeric findings/source IDs.

## Receipts
- M1: `method1/autopilot/RESEARCH_TOPICS_SPECIFICITY_PASS_M1_20260708T105800Z.md`
- M2: `method2/autopilot/RESEARCH_TOPICS_SPECIFICITY_PASS_M2_20260708T105800Z.md`
- M3: `method3/autopilot/RESEARCH_TOPICS_SPECIFICITY_PASS_M3_20260708T105800Z.md`

## Live-root / public mirror
Autopilot live-root mirror: **0**.

Tori post-rollup static mirror: copied all three verified specificity static sets to `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/.../research-topics-from-wiki-20260708T090359Z/`.

Public verification after copy:
- **M1** public URL: HTTP 200, specificity marker present, `What studies already show`/`What remains unknown`/`Survey/data plan`/`Analysis/test` all 6, old proposal marker absent. Live backup: `packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-specificity-pass-20260708T111138Z/`.
- **M2** and **M3**: initially returned HTTP 404 after copy (new static subdirectory visibility caveat). After explicit user approval, Tori performed one frontend-only static refresh of the existing Next server on `:3000` (old listener PID 48301; new listener PID 64407). Public M2/M3 URLs then returned HTTP 200 with the specificity marker and required section text. No product backend/API restart or deploy occurred.

## Safety ledger
Read-only inspection + method-team in-place revisions under the 3 `research-topics-from-wiki-20260708T090359Z/` dirs + `.hermes` receipts + this rollup. Tori then performed narrow static live-root copies for M1/M2/M3 and, after explicit approval, one frontend-only static refresh of the public Next server so M2/M3 static routes became visible. **Zero** product backend/API restart, deploy, product DB/SQL, `/api/pages`, page_versions, live-wiki publish, trust recompute, git, cockpit/global/shared-parent, cloud/OAuth/secrets, browser, cron; zero Method3 P3 binding; zero invented data; zero director keystrokes into panes; zero solo content authoring. All non-static hard gates remain closed.

AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z
