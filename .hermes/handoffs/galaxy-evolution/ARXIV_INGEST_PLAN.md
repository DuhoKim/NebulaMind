# Feed new arXiv papers into the full process — Trio design (2026-07-20 KST)

## The core insight
There are TWO ADS paths, keyed differently. Daily `arxiv_fetch.py` → `arxiv_papers` (arxiv_id) → WIKI, but it
throws away the fields the frontier engine needs (keyword/reference/citation_count). The one-shot `pull_ads.py`
→ `corpus_ga_co_2009_2026.jsonl` (bibcode) → embed→cluster→rank is refereed-only and FROZEN at 2026-07-18.
**Bridge = a date-windowed twin of `pull_ads.py` (bibcode-keyed, rich fields) — NOT reading arxiv_papers.**

## The loop
new arXiv/ADS paper → [dedup vs bibcodes.json] → [relevance/quality gate] → [embed-append to emb_qwen4b.f32]
→ [nearest-centroid assign in raw 2560-d] → cluster membership grows → [weekly re-rank] → frontier_map_v3.json
→ {live Topic map (frontiersData.ts), motivation grounding, research-idea gen}.

## What EXISTS vs NEW
- EXISTS: daily fetch + wiki feed (BM25 candidates→validate→promote); the whole embed/cluster/rank engine
  (embed_corpus.py qwen3-embedding:4b 2560-d, derive_topics.py UMAP+HDBSCAN, rank_frontiers.py + rank_frontiers_v3.py).
- NEW glue (small): `pull_ads_incremental.py` (windowed twin), embed-append driver (append raw float32 bytes +
  extend bibcodes.json — never re-embed the 120,676; ~17s/100 papers), `centroids_v2.npy` builder +
  nearest-centroid assigner, and `gen_frontiers_data.py` (the MISSING adapter, see gap).

## THE #1 GAP (build first)
`frontend/src/app/lab/frontiersData.ts` is generated from an OLD 32-cluster / 12k snapshot
(research-frontiers-20260716) — TWO snapshots behind the 57-cluster / 120k engine — and its schema
(name/desc/nDebates/topic) doesn't match `frontier_map_v3.json` (keywords/strict_tension/score_v1). There is
NO generator v3→frontiersData.ts. Nothing new can reach the live map until this adapter exists.

## Guardrails (must-haves)
- **FREEZE the minmax normalization constants** (v1_constants: a_half, tension/growth min-max) at each full
  snapshot. rank_frontiers_v3 recomputes them per run → one high-tension preprint would silently rescale EVERY
  cluster. This is the single biggest lurch risk.
- Nearest-centroid assign is an APPROXIMATION (HDBSCAN persists no model; runs in 2560-d not UMAP-15d) — fine
  for routine assign; drift only FLAGS for a supervised re-cluster, never corrupts silently.
- Frontier stability: EMA (~90d) + 14-day persistence before a rank change is headline; ranked clusters need
  ≥400 members + 2 quarters (new ones → a "watch list", never rank #1); anti-gaming by distinct author groups.
- Quality gates: per-paper GA/CO scope gate (reuse deterministic_tag), drop catalogs/errata/withdrawn/thin
  abstracts, version (v2/v3) reconciliation (update in place, never duplicate).
- source_tier: refereed = full weight; preprint = provisional 0.5, CANNOT be a claim's sole support, labeled.
- Retraction/erratum handling (full gap): detect withdrawal → down-weight to 0 + wiki banner + demote
  sole-support claims; reversible.
- Freshness honesty on the site: TWO dates — "structure as-of" (last re-cluster) + "counts current-through".
- NOTE: the Atom (atom-astronomy-7b) validator is broken → the dual-validator wiki gate runs on one leg;
  use AstroSage-only fallback explicitly.

## Cadence
- Daily: delta pull → embed-append → nearest-centroid assign + drift accounting (seconds, ~free).
- Daily/2×wk: windowed pull_references.py (recent citation inflow = freshest frontier signal).
- Weekly: rank_frontiers.py → rank_frontiers_v3.py → regenerate frontiersData.ts (minutes, CPU).
- Monthly: Track-A pull_ads.py refereed backfill (overwrite arXiv stubs with authoritative ADS metadata).
- Rare/quarterly/drift-triggered + SUPERVISED: full re-cluster (derive_topics.py UMAP+HDBSCAN, tens of min).

## First increment (smallest thing that makes the loop real)
pull_ads_incremental.py + centroid-assign + gen_frontiers_data.py adapter. Definition of done: run daily ingest
for a week, weekly re-rank, regenerate frontiersData.ts, and see ≥1 cluster's score/ordering change on the live
Lab Topic page driven solely by post-2026-07-18 papers — with the as-of date shown. Motivation-grounding and
idea-gen wiring consume the same appended artifacts and follow.
