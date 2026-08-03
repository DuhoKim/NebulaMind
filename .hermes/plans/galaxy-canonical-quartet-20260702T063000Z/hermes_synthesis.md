# Hermes independent synthesis — Galaxy canonical page

Created UTC: 2026-07-02T06:29:30Z

Mode: read-only design. No DB writes, SQL, deploy/restart, git commit/push/merge, runtime source edits, or page publish.

## Bottom line

Use page 57 / `galaxy-evolution` as the canonical public identity, but do **not** use its current article structure unchanged. Page 57 is the data/provenance backbone; page 58 is the editorial workbench. The combined page should keep page 57's slug and claim/evidence graph, then graft page 58's clearer reader contract, mechanism-first sectioning, and caveat style into a new preview draft.

## Why not pick one unchanged?

- V1/page 57 has the real public identity and dense provenance: 721 claims, 8 page-citation links, 3 fact-source rows, 22 claim markers in body.
- V2/page 58 has a clearer article shape but is too small to become canonical directly: 8 claims, 0 page-citation links, 0 fact-source rows, 8 claim markers in body.
- Keeping both active creates ambiguous targeting (`galaxy-evolution` vs `galaxy-evolution-v2`) and already caused cockpit mistakes.

## Structural diagnosis

| Axis | V1/page 57 | V2/page 58 | Canonical decision |
|---|---:|---:|---|
| Content words | 1893 | 1369 | Target roughly 2.5k-4k words in preview; concise but evidence-rich. |
| H2 sections | 8 | 9 | Use 8-9 mechanism-first H2s, not duplicate debate furniture. |
| Body claim markers | 22 | 8 | Keep visible markers sparse: key claims only; use provenance layers for full graph. |
| Claim rows | 721 | 8 | Preserve V1 graph; do not auto-merge V2 rows. |
| Citation/fact-source surface | 8 citation links / 3 fact sources | 0 / 0 | V1 must remain source of truth; page-citation cross-page oddities need audit before publish. |

## Proposed canonical H2 spine

1. Lead / reader contract
   - Sources: V2 reader note + V1 baryon-cycle opening
   - Design note: Use a short reader note only if UI claim chips need explanation; otherwise make it article prose.
2. Overview: galaxy evolution as a regulated baryon cycle
   - Sources: V1 Overview + V2 Overview & Historical Framework
   - Design note: Use V1 baryon-cycle frame; graft V2 red sequence/blue cloud as observational landmarks not mechanisms.
3. Dark matter halos, structure formation, and baryon efficiency
   - Sources: V1 Dark Matter Halos + V2 Dark Matter & Structure Formation
   - Design note: Keep halo/baryon efficiency evidence; add V2 JWST/high-z caveat here, not as generic frontier.
4. Gas supply, star formation, and stellar feedback
   - Sources: V1 Gas Supply + V2 Star Formation & Quenching
   - Design note: Separate reservoir supply, depletion, turbulent/morphological regulation, and stellar feedback.
5. Quenching and AGN feedback
   - Sources: V1 Quenching + V2 AGN Feedback
   - Design note: Keep conditional language: mode-, phase-, scale-, environment-dependent; avoid AGN-always-quenches.
6. Environment, morphology, and cosmic web
   - Sources: V1 Environment/Morphology + V2 Environmental Effects
   - Design note: Combine cluster processing, satellites, stripping, tides, filaments; distinguish direct evidence from contextual morphology.
7. Chemical enrichment and population diagnostics
   - Sources: V1 Chemical Enrichment + V2 Observational Evidence
   - Design note: Use metallicity/scaling relations as evidence clocks; move generic observing modes here if tied to what they constrain.
8. Surveys, redshift frontier, and unresolved tensions
   - Sources: V1 High-Redshift/Open Tensions + V2 Current Surveys/Synthesis
   - Design note: Do not make a mission list; organize by uncertainty resolved: early mass budgets, reionization sources, cold streams, feedback efficiency.
9. Synthesis: what regulates galaxy evolution?
   - Sources: V2 Synthesis + V1 caveats
   - Design note: End with mechanism dominance by mass/redshift/environment, plus explicit next evidence gaps.

## Merge rules

1. Identity rule: canonical slug is `galaxy-evolution`; V2 becomes `superseded workbench` or redirect target after publish.
2. Provenance rule: page 57's claim/evidence/vote graph is authoritative until a separate exact-diff packet changes it.
3. Prose rule: V2 prose can be used as editorial scaffolding, but every imported sentence must either map to an existing page-57 claim/evidence surface or be labeled as unsourced preview text.
4. Claim-marker rule: avoid stuffing 721 claim rows into prose. Mark only high-value claims; expose the full graph through claim/evidence UI surfaces.
5. Citation rule: do not auto-accept page citation links until the 8-row-to-5-object/cross-page evidence footprint is adjudicated.
6. Retirement rule: after publish, page 58 should stop being an active public target: archive, redirect, or mark noindex/superseded depending on app support.

## Grand-design phases

Phase 0 — Decision lock (now): agree that canonical = page 57 identity plus V2 editorial improvements.

Phase 1 — Read-only canonical preview packet: produce a side-by-side section map, proposed markdown draft, evidence-use map, and rendered review HTML. No apply SQL.

Phase 2 — Provenance alignment: map each proposed marked claim to existing page-57 claim IDs/evidence; identify V2-only or unsourced prose as `needs evidence` rather than inserting rows automatically.

Phase 3 — Publish preflight packet: backup `wiki_pages`, latest `page_versions`, relevant claim rows, page-citation links, fact sources; produce exact content diff, claim-marker diff, guarded apply SQL, rollback SQL, rendered preview, and separate `APPROVE PUBLISH` phrase.

Phase 4 — Execute only after explicit publish approval: apply guarded packet, verify DB/API/rendered DOM, then mark page 58 superseded/redirected only in a separate or clearly scoped packet.

## What absolutely should not be automatic

- Do not merge page 58's eight claims into page 57's 721-row graph by ID guesswork.
- Do not delete, archive, or redirect page 58 without an explicit packet.
- Do not publish V2 preview disclaimers into the canonical page.
- Do not create new evidence rows merely because a polished sentence lacks an existing citation.
- Do not let current `page_versions.version_num=1708` be described as V2.

## Hermes recommendation

Next move: create a read-only canonical preview packet, not a publish packet. The packet should show one proposed article spine, a draft markdown body, a claim/evidence-use map, and a `do-not-publish-yet` gap list.

Marker: HERMES_GALAXY_CANONICAL_SYNTHESIS_DONE_20260702
