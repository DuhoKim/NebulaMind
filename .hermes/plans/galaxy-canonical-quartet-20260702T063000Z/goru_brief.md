GORU BRIEF — GALAXY_CANONICAL_MECHANICAL_MAP_20260702 — exact counts/surface-map lane
Context: User asks the Quartet (Hermes + Lana + Goru + Fable) to scrutinize the current format/structure of the two Galaxy Evolution versions and grand-design how to combine them into one canonical page.
Mode: READ-ONLY DESIGN REVIEW. No DB writes, no SQL/apply SQL, no migrations, no deploy/restart, no git commits/pushes/merges, no runtime source edits, no deletes, no secrets, no unrelated paths, no external web unless explicitly needed and then report it.
Important page mapping:
- V1/public canonical candidate: page id 57, slug galaxy-evolution, title Galaxy Evolution, latest page_versions.version_num 1708, 721 claims.
- V2/workbench pilot: page id 58, slug galaxy-evolution-v2, title Galaxy Evolution (Intro-Synthesis V2 Pilot), latest page_versions.version_num 7, 8 claims.
Baseline artifacts to read:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/baseline_compare.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/baseline_compare.json
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/page_57_galaxy-evolution.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/page_58_galaxy-evolution-v2.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/page_57_galaxy-evolution_claims.jsonl
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/page_58_galaxy-evolution-v2_claims.jsonl
Goal: produce advisory report only; Hermes will integrate and verify. Do not attempt to mutate either page.

Your role: mechanically verify structure and surfaces. Do not make product strategy judgments except where counts imply risk.
Tasks:
1. Read baseline_compare JSON/MD and both markdown pages.
2. Verify H1/H2/H3 counts, claim-marker counts, approximate paragraph/list/table/code counts, URL counts, word counts.
3. Compare V1 H2 spine vs V2 H2 spine and produce a normalized section-alignment table.
4. From claims jsonl, list claim-section counts for V1/V2, evidence_count distribution summary, and identify claim-section names that do not align with content H2s.
5. Produce mechanical merge constraints: which rows/surfaces need explicit mapping before publish.
Output: write only /Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/goru_mechanical_map.md and /Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/galaxy-canonical-quartet-20260702T063000Z/goru_mechanical_map.json. End markdown with standalone marker GORU_GALAXY_CANONICAL_MAP_DONE_20260702.
