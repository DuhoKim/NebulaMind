BLOCKED.

Exact exception:
- `28066`: reproducibility chain is mostly sound, but duplicate/stacking metadata incorrectly says `28110` is a “same-source sibling.” `28066` is `arXiv:2512.05584`; `28110` is `arXiv:0901.1880`. This breaks future same-source verification. Keep `28066` pending or scrub that note before gate/apply. No Gemini needed.

Everything else passes:
- Lana issues on `28088` and `28148` are fixed enough to avoid overclaiming.
- Same-source stacking is otherwise documented.
- Required fields look checker-valid after apply.
- No other row needs Gemini web second opinion.

KUN_REMAINING20_REPRO_CHECK_20260705T085714Z
