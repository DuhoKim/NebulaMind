# Video briefs — Lab/Topic sub-nav explainers (5 clips)

REQUESTED BY: Duho (via Claude), 2026-07-19. One short explainer per Topic sub-nav step, to embed on
the Lab page (nebulamind.net/lab → Topic → each step). Match the on-page content (already live).

CONSTRAINTS
- 16:9, ~15–25 s each, silent or light ambient; legible ON-SCREEN infographic text is the point
  (use Nano Banana Pro for text panels, per crew capability map — Veo footage is a dim backdrop only).
- INFORMATIVE, not cosmic: each clip must convey its step's facts via on-screen text/infographic,
  not just pretty space footage.
- YouTube: UNLISTED only (per policy) unless Duho okays public per-video.
- Deliver: the 5 YouTube video IDs (or unlisted URLs) back to this dir (e.g. append to a delivery.json),
  so Claude can embed them on the matching sub-nav pages.

## 1 · Corpus  (embed on Topic→Corpus)
Message: the whole modern literature, not a hand-picked sample.
On-screen: "120,676 refereed papers · astro-ph.GA + CO · 2009–2026 · 10× the old 12k corpus".
Beat: a growing bar chart of papers/year (2009→2026), then "8.9M-edge citation graph".

## 2 · Embedding  (embed on Topic→Embedding)   <- NEXT REQUEST (Duho, 2026-07-19): please generate this one next, UNLISTED.
Message: every paper becomes a point in a space of meaning - and it demonstrably works.
On-screen (the page now shows all of this - match it):
  - "qwen3-embedding-4b · 2,560-d vector · 120,676 papers · 1.24 GB index".
  - Leaderboard beat: "won a 9-model citation bake-off - recall@10 0.691" (qwen3-4b beats nomic 0.589; 8b only +0.013, not worth 1.6x).
  - PROOF beat (the highlight): a landmark paper pulls its true neighbors - show
      "Planck 2018 VI -> Planck 2015 (0.92), Planck 2013 (0.89)..."  and/or
      "IllustrisTNG -> MillenniumTNG, Illustris, sibling TNG papers". Same physics, across years, nothing hand-picked.
  - Two-layer beat: "abstract layer (120,676 papers, find related work) + full-text layer (~4,900 top-cited papers, passages embedded -> pull the exact evidence the quality gates read)".
Beat sequence: an abstract -> a 2,560-d vector -> points cluster by topic -> a query paper lights up its true citations -> split into two stacked layers (abstract vs full-text).

## 3 · Clustering  (embed on Topic->Clustering)   <- REQUEST (Duho, 2026-07-19): generate next, UNLISTED.
Message: the field's own structure, read straight out of it - no human labels.
On-screen (match the live page):
  - "UMAP (2,560-d -> 15-d) -> HDBSCAN (min-cluster-size 400) -> c-TF-IDF · 57 emergent themes · no preset count, no human labeling".
  - "68,772 papers clustered (57%) · 43% diffuse tail left as noise · sizes 414 -> 8,913".
Beat: a 120k point cloud self-organizes into 57 colored clusters; a 43% grey haze stays unclustered; top cluster "JWST high-z galaxy formation" lights up #1.

## 4 · Activity overlay  (embed on Topic->Activity overlay)   <- REQUEST (Duho, 2026-07-19): generate next, UNLISTED.
Message: mark where the field is still building vs settled.
On-screen (match the live page):
  - "overlay the citation graph on the clusters · 2.30M edges into clustered papers, 911k from 2023+ work".
  - "recent citations per paper = how hard the field is STILL citing a theme · JWST high-z 39.2 -> pulsars 3.0 (13x spread)".
Beat: clusters glow by recent-citation activity; JWST high-z glows brightest, settled themes (pulsars) go dim.

## 5 · Ranking  (embed on Topic->Ranking)   <- REQUEST (Duho, 2026-07-19): generate next, UNLISTED.
Message: the fastest-moving frontiers rise to the top and become the studies.
On-screen (match the live page):
  - "frontier score = 0.6 x activity + 0.4 x growth (each min-max normalized) · activity = 2023+ cites/paper, growth = 2023+ share of the theme".
  - "57 themes ranked, no hand-picking · 31 galaxy-evolution (in scope -> study) / 26 cosmology (out of scope) · JWST high-z #1".
Beat: the 57 themes sort into a ranked list; galaxy-evolution ones flag green "-> study", cosmology ones grey "out of scope".

## Notes for the correspondent (Yui)
- 5 generations ≈ meaningful Flow credit spend (last known balance 22,096/25,000). Pace per the
  gentle-throttle guidance; stop and flag if the account soft-throttles.
- If Ingredients/character consistency helps keep a shared visual identity across the 5, use it.
