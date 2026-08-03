# Increment 1 — live arXiv → frontier-engine loop (BUILT + TESTED 2026-07-20)

The smallest slice that turns the frozen 2026-07-18 snapshot into a live loop. Frozen snapshot is
NEVER mutated — new papers go to `delta/`. Live `frontiersData.ts` is NOT touched (staging only).

## Scripts (all in this engine dir)
1. `build_centroids.py` → `centroids_v2.npy` (57×2560, native space) + `centroids_meta.json`
   (calibrated TAU_ASSIGN=0.681 / TAU_DRIFT=0.631 from member-to-centroid cosine). Run once per full re-cluster.
2. `ingest_incremental.py [N]` → tokenless arXiv API pull of the N newest astro-ph.GA/CO, dedup, embed
   (qwen3-embedding:4b), nearest-centroid assign, append to `delta/{new_papers.jsonl,new_emb.f32,new_labels.json}`
   with source='arxiv_new', source_tier='preprint'. ~8s/25 papers. Run DAILY (cron/wakeup after fetch_arxiv_daily).
   TESTED: 25 real papers, 20 assigned to semantically-correct clusters (dark-axion→C34 dark/energy;
   low-mass-galaxy→C40 quenching; PBH→C44 inflation), 5 novel, 2 drift-flagged.
3. `gen_frontiers_data.py` → `frontiersData.v3.staging.ts` (57 clusters from frontier_map_v3, sorted by
   score_v1; keyword-derived names/descs; two honest dates). Top frontier = C41 Formation·Metallicity·JWST (0.369).
   Run WEEKLY after re-rank. STAGING — review before swapping the live 32-cluster frontiersData.ts.

## Weekly re-rank (compose existing scripts — the small remaining wiring)
After a week of daily ingest: fold `delta/` into the corpus view, then run `rank_frontiers.py` →
`rank_frontiers_v3.py` → `gen_frontiers_data.py`. **CRITICAL:** rank_frontiers_v3 must REUSE the frozen
v1_constants (a_half=12.16, tension_min=0.026, tension_max=0.434, growth_min=0.074, growth_max=0.458),
NOT recompute them per run, or one high-tension preprint rescales every cluster. (One-line change to freeze.)

## Deferred (not in increment 1)
- Track-A monthly `pull_ads.py` refereed backfill (needs an ADS token) to overwrite arxiv_new stubs.
- Weekly re-rank reading base+delta (small: point rank scripts at corpus+delta; freeze v1_constants).
- Retraction/erratum propagation; source_tier weighting in the wiki validate gate; live-map swap (product call).
- Note: the arxiv_new records lack ADS keyword/reference → 0 citation inflow (fine, new papers) and use
  primary_category for GA/CO scope until the Track-A backfill lands.

## Multi-day ingest run (2026-07-20)
Simulated ~2 weeks of the daily job via `backfill_days.py 5` (paged arXiv, politeness-paced): accumulated
**499 raw → cleaned to the delta store** (dedup vs the 120,673-id refereed corpus = 3.8% overlap removed,
+ intra-dups). 431 assigned to clusters, 68 novel/noise. Hottest recent frontiers: C44 inflation/PBH,
C18 GW/binary-BH, C42 lensing/LSS, C47 molecular gas. Delta store (`delta/`) is now re-rank-ready.
Next: weekly re-rank over base+delta with FROZEN v1_constants, then regenerate frontiersData.v3.staging.ts.
