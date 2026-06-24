# Page 58 Slice-2B Stance Gold Rebalance

Gold-prep only. No staking rollup was rerun. Stance remains NOT LOCKED pending Papa spot-check.

## Counts

- Rows: 130
- Draft labels: {'contradicts': 20, 'neither': 53, 'supports': 57}
- Sample buckets: {'contradict_oversample': 27, 'negative_contradiction_probe': 30, 'sub_tau_neither_boundary': 24, 'neither_oversample': 24, 'support_control': 24, 'rare_contradict_fill_from_same_panel_pass': 1}
- Papa attention rows: 89
- qwen_default rows: 28
- qwen/gpt disagreement rows: 40
- cap-exhausted disagreement rows: 28
- sub-tau relevance-boundary rows: 24

## Notes

- The sampler widened beyond cosine survivors using a sub-tau boundary bucket and a negation/contrast probe bucket.
- One nonduplicate contradicts row from the earlier same-panel guarded full pass was included to bring the review draft to 20 contradicts rows.
- Rows with `qwen_default`, qwen/gpt disagreement, and cap-exhausted disagreement flags are the highest-priority Papa review rows.

## Containment

- HEAD 4ba9675; --no-apply; db_write_count=0; paid_lane_touched=false; local_only=true; claude_p_invocations=15; migration_applied=false.

## Files

- `stance_gold_draft_for_papa_v2.jsonl` sha256 `9bb319a41c7f9ee127fb9e076022b981138b7bb8111b34bbac275f8768b480a9`
- `summary.json` sha256 `9c570aa5cc023c02efbdd272792763e6eea40bc8c2b8b8c0b07eb78bbf3167d2`

- `SHA256SUMS.txt` records final stable hashes, including `summary.json` sha256 `231ecdf8b4997b6b2a0f9f6d94f576f4cb33378d120eaa1d8a4d35331afb6a8b`.
