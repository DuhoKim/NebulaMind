# GORU BRIEF — Shape-2 T1: catalog reconnaissance + frozen assembly rules

Lane: `c41-trackb-shape2-mzr-20260804T1452K` (write ONLY here; temps `_tmp_goru_*`).
Gate: Duho — "APPROVE C41 TRACK-B MEASUREMENT START". You are Goru, mechanical lane.
Design: `MEASUREMENT_DESIGN_V1.md` (Kun is refuting it in parallel — your T1 is verdict-
independent reconnaissance; you fetch NO science data rows this round).

1. **Assembly rules FIRST** (Step-1 discipline): draft `T1_ASSEMBLY_RULES.md` from measurement
   classes only — inclusion by auroral-line detection class / Te-consistent limit class, z>3,
   declared-scale requirement, mass-convention fields needed — BEFORE looking at any catalog's
   contents. Peek log required.
2. **Reconnaissance via `tools/nm_external_data.py` (VizieR TAP)**: locate candidate tables for
   JWST z>3 Te/auroral metallicity samples (JADES/CEERS/GLASS/UNCOVER-class compilations) and the
   design's named in-corpus samples. For each: record VizieR table ID (or absence), column
   inventory vs the rules' required fields, row counts from METADATA queries only (COUNT-style /
   header reads — no science-row downloads this round), access notes. Politeness: nm_external_data's
   built-in retry/cache; no hammering.
3. Output: `T1_CATALOG_MANIFEST.json` (per-candidate: id, availability, columns-vs-required,
   counts, provenance-chain notes) + `T1_ASSEMBLY_RULES.md` (frozen, sha in the report) +
   `GORU_T1_REPORT.md` with an honest availability verdict vs the design's fallback clause,
   ending with marker `GORU_SHAPE2_T1_COMPLETE_20260804`.
No science-data fetches, no model outputs, no git/DB, lane-only writes.
