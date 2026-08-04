# GORU BRIEF — Step 3 V3: zone redesign (V2 zones failed re-check; fidelity is FIXED — keep it)

Read `TORI_STEP3_RECHECK.md` first. Quote handling is now correct — DO NOT touch it. Zones failed
again, systematically (finding on methods/captions/references; references mislabeled; a caption as
method). Third and final zone attempt — by DESIGN CHANGE, not tuning:

1. `finding` requires BOTH a result-verb signal AND (results/conclusions/abstract heading
   proximity). Anything less → `unknown`. `unknown` is honest and passes; a wrong `finding` fails.
2. Caption detection: block starts matching Figure/Fig./Table/Extended Data + number → `caption`.
   Reference detection: citation-dense lines (≥3 bracketed/year citations, or bibliography-style
   author-year runs) and everything after a References/Bibliography heading → `references`.
   `caption`/`references` spans are NEVER `finding`/`method`.
3. FALLBACK (pre-authorized): if after implementing 1–2 you cannot trust a zone class, set that
   class to `unknown` wholesale. A table that says `unknown` mostly is acceptable; one that lies
   about `finding` is not.
4. Re-run as `C41_STEP3_V3`; back up V2 to `_tmp_goru_v2_backup/`; append a `## Repair round (V3)`
   section to your report (what changed, new zone histogram, V2→V3 deltas) ending with marker:
   `GORU_STEP3_V3_COMPLETE_20260804`.
Same constraints as before.
