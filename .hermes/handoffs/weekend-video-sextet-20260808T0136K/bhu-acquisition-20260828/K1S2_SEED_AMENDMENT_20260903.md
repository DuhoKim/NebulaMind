# K1 stage 2 — master-sheet amendment, row 6 seeds (Tori, 2026-09-03 18:06 KST)

**Fact (Claude seat, launch note; verified by Tori in `_tmp_k1s2_codex/COMPAS/src/main.cpp` L663):** COMPAS sets each system's seed to
`--random-seed + system index`. Three batches of 10⁶ systems started at the pinned seeds 104729, 130363, 155921 verbatim would
share ~97 % of their per-system seeds, so their across-batch dispersion (the prereg's Monte-Carlo error, §4) would be meaningless.
**Amendment:** the pinned seeds become BLOCK STARTS multiplied by 1000 (104729000, 130363000, 155921000; C4 extras likewise
×1000 in each seat's scheme), non-overlapping for N ≤ 10⁶, the same blocks at every cap so cap differences are paired.
**Applied:** the Claude seat did this at launch (17:59 KST) and disclosed it; the codex driver had the verbatim seeds — its grid
was stopped at ~18:10 KST after ~10 minutes, the driver patched (original kept as `_tmp_k1s2_codex/driver_v1_overlapping_seeds.sh`),
the partial run tree wiped, and the grid relaunched. This is a harness correction disclosed to both seats' records, not a
science input; nothing in the prereg's classes or controls changes. Two further flags from the Claude launch note are carried
to the gate: (i) every output row carries error code 43 (FLOATING_POINT_ERROR) with normal evolution status — to be checked as a
logging artefact; (ii) the C2 KS test failed on the 10⁴-system smoke sample under the primary cut — not a result, but if it fails
at 3×10⁶ the prereg says stop, no class.
