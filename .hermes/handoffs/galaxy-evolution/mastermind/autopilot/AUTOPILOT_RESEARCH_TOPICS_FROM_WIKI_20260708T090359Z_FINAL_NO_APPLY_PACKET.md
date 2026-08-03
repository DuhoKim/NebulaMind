# Final no-apply rollup — research-topics-from-wiki (three method-matched teams)

Marker: AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z
Author: Hwao-director (pane %107). Written 2026-07-08T09:12Z (18:12 KST). Tori post-rollup metadata cleanup applied after validator notes: added M2 markdown parent marker and refreshed M1/M2 manifest checksum metadata.
Basis: three method-team research-topic candidates + Goru/Kun receipts + this director's independent read-only verification (topic counts from the JSON maps, static-safety, product-marker scan, link + caveat checks, fresh checksums).

## Status: COMPLETE

Three additive, method-matched **research-topic** HTML candidates were derived **only** from each method's resulted local **wiki** candidate — reader-facing topic lists (hypotheses/questions for future work), each 6–12 topics, static-safe, no invented evidence, no product bindings. Working-repo only (a live-root mirror + `:3000` restart would be a separate gate if visibility is wanted).

## Per-method artifact table

Output dir: `…/galaxy-evolution/<method>/research-topics-from-wiki-20260708T090359Z/` (each: `research-topics-from-wiki-…html` + `…md` + `research-topic-map-…json` + `manifest-…json`).

| Method | topics | HTML bytes / sha256(16) | rel-links | static-safe | product claim/cite | source wiki candidate |
|---|---|---|---|---|---|---|
| **M1** packet-gated | **8** | 13,925 / `a57245c9f34cbacb` | 2 | ✅ (0 script/fetch/onclick/ext) | 0 / 0 | `…/packet-gated-…/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html` |
| **M2** source-first | **10** | 17,387 / `b5dc1b344bf85553` | 4 | ✅ | 0 / 0 | `…/source-first-…/…/wiki-prose-evidence-trust-deepening-20260708T043427Z.html` |
| **M3** debate-map | **9** | 16,246 / `bdb280e4d3a46f90` | 5 | ✅ | 0 / 0 | `…/debate-map-…/…/wiki-prose-evidence-trust-deepening-20260708T043427Z.html` (repaired) |

Sidecars (sha256(16) / bytes): M1 map `c8005bcf6f3a113c`/6,958 · md `420df00ff6212446`/7,401 · manifest `ef057f38a90e6be0`/997. M2 map `7516023547e3b539`/9,155 · md `c06ebd5e9bfcc8c0`/10,285 · manifest `9335608f6091ec1d`/1,018. M3 map `6e537070a672f5f2`/5,279 · md `a15f82cc980d89a9`/6,665 · manifest `ff069c6325f83265`/1,873.

## Director verification (independent, read-only)
- **Topic counts** (from each `research-topic-map-…json`): 8 / 10 / 9 — all within the 6–12 spec.
- **Static-safety — all PASS:** 0 `<script>`, 0 `fetch(`, 0 `onclick`, 0 external hosts in every HTML.
- **No product binding — PASS:** 0 `<!--claim:-->` and 0 `<!--cite:-->` comments in every HTML (spec expected 0).
- **Caveat present** in all three ("research topics … hypotheses/questions for future work, not accepted claims").
- **No-invent:** derived from each method's existing wiki candidate + local sidecars; no new papers/IDs/DOI/ADS/product bindings introduced.

## Verification receipts (Goru/Kun + method verdicts)
- M1: `method1/autopilot/RESEARCH_TOPICS_GORU_M1_SEED_20260708T090359Z.md` + `method1/autopilot/RESEARCH_TOPICS_KUN_M1_VALIDATE_20260708T090359Z.md` + method verdicts in the method1 tree
- M2: `method2/autopilot/RESEARCH_TOPICS_GORU_M2_SEED_20260708T090359Z.md` + `method2/autopilot/RESEARCH_TOPICS_KUN_M2_VALIDATE_20260708T090359Z.md` + method verdicts in the method2 tree
- M3: `method3/autopilot/RESEARCH_TOPICS_GORU_M3_SEED_20260708T090359Z.md` + `method3/autopilot/RESEARCH_TOPICS_KUN_M3_VALIDATE_20260708T090359Z.md` + method verdicts in the method3 tree
(Director verification above serves as the equivalent deterministic cross-check for any receipt still settling.)

## Plain-English statement
These are **research-topic candidates derived from the resulted local wiki pages** — reader-facing lists of open questions/gaps each method's wiki suggests. They are **hypotheses for future work, not new science evidence and not product claim/citation bindings.** Each method's trust scale is its own (see the cross-method legend); the topic lists inherit each method's honesty limits (M1 3/30 evidenced + 27 unbound; M2 accepted/limited/rejected + cite-unmatched; M3 docs-only, P3 closed).

## Safety ledger
Read-only inspection + method-team static candidate authoring under the three `research-topics-from-wiki-20260708T090359Z/` dirs + `.hermes` receipts + this rollup. **Zero** live-root writes/copies, `:3000` restart/deploy, product DB/SQL, `/api/pages`, page-version, live-wiki publish, git, cockpit/global/shared-parent, cloud/OAuth/secrets, browser, cron; zero Method3 P3 binding; zero invented data; zero director keystrokes into panes. All hard gates remain closed.

AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z
