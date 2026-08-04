# Yui C41 Step 2 report

## Outcome

- Sealed records requested: 180
- Manifest records written: 180
- Full text: 180
- Abstract only: 0
- Metadata only: 0
- Cache hits: 42 (23.33%)
- New arXiv fetches: 138
- Failed records: 0
- Runtime: 691.565 seconds
- Hard stop triggered: false

## Input seal

- `SELECTION_INCLUDED.json`: `4a0ba6e7ae1ad7b8249c68ddd0c73ccf81a1ba05c94ffac03febb012589e961f` (272656 bytes)
- Expected selection hash: `4a0ba6e7ae1ad7b8249c68ddd0c73ccf81a1ba05c94ffac03febb012589e961f` — MATCH
- `tools/nm_fulltext_layer.py`: `54479995cbb6733f548b6374672a4f88fc5d05b83196e137db6ce5aa00cfb2ae` (13483 bytes)
- Exactly the sealed 180 were processed; no record was added, removed, or re-admitted.

## Failures and honest access labels

- None.

Every record without extracted full text is labeled `abstract_only` with its failure reason in `STEP2_FULLTEXT_MANIFEST.json`. No unavailable source was promoted to `full_text`.

## Re-admission candidates

- None noticed during exact sealed-set acquisition. The excluded set and in-progress C41 map lanes were not inspected.

## Safety boundary

This run wrote only this C41 lane directory and the engine `fulltext_cache/`. It made no database writes, git writes, product-surface changes, deploys or restarts, Deep Research calls, or credit-spending calls. Network access was limited to arXiv and ADS. The ADS token was used only in memory by the tracked module and was never printed or written. This is a pre-prose acquisition artifact: prose, exact-diff, claim/evidence mutation, trust targeting, publication, and runtime changes remain unauthorized.

YUI_STEP2_COMPLETE_20260804
