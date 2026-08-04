# GORU BRIEF — Shape-2 T2a: join plan + conversion machinery + the frozen forecast (F4)

Lane: `c41-trackb-shape2-mzr-20260804T1452K`. You are Goru. First, a correction to your T1
verdict, with evidence: the design never required a pre-assembled catalog. Your own manifest shows
the components exist (33 candidates; metallicity tables and mass tables that JOIN on object
identifiers/coordinates — exactly like your alpha-knee 3-table APOGEE join, #128). "Fragmented"
is the normal state of VizieR; the join is the job. Your fallback invocation is void — shape
changes are Duho's gate. T1's MANIFEST stands as good recon; its verdict paragraph is superseded
by this brief.

## T2a deliverables (still metadata-only — no science rows yet)

1. `T2A_JOIN_PLAN.md`: from your manifest, the concrete join design — which Te/auroral tables
   join which mass/photometry tables, on what keys (IDs/coordinates+tolerance), per candidate
   pairing; which pairings satisfy the contract fields natively vs need declared conversions;
   the named F7 fallback tables.
2. `T2A_CONVERSION_TABLES.md`: the metrology machinery — mass-convention conversions (IMF/SED),
   Te-scale relations to be used, the UV-vs-optical channel separation implementation (F3),
   lensing-inheritance fields for the 10^5.7 sample (F1). Semantics come from Lana's
   `T2B_CONTRACT_SEMANTICS.md` (read it if it exists; flag conflicts, do not resolve them).
3. **`T2A_FORECAST_FROZEN.json` (F4)**: from manifest row counts + join expectations, the
   pre-fetch forecast — expected Te-anchored N per matched-mass bin per z slice, resulting
   deficit-precision forecast, and the null's information threshold X dex per bin. Sha it in your
   report; it FREEZES before any science fetch.
4. `GORU_T2A_REPORT.md` ending with marker `GORU_SHAPE2_T2A_COMPLETE_20260804`.
Metadata queries only; politeness unchanged; lane-only writes.
