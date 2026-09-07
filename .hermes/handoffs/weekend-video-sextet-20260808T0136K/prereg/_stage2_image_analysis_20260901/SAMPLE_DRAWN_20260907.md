# SAMPLE DRAWN — the repaired prospective start completed (2026-09-07 21:20 KST)
**`SEED ACCEPTED` → `DRAW ACCEPTED` → `SEQUENCE COMPLETE`.** Journal: `OUT_A1_REPAIRED/`.
## THE SEED
| item | value |
|---|---|
| round | **6445084**, scheduled `2026-09-07T12:19:00Z`, collected `12:19:04Z` |
| seed | `783849d4edb36a35d0b5ef8ffbe64c9ec8b9419c6cac4866d700503a7f65b926` |
| chain | `8990e7a9aaed2ffed73dbd7092123d6f28993054` (pinned mainnet) |
| hosts accepted | api.drand.sh, api2.drand.sh, api3.drand.sh — two passes, BLS-verified against the pinned key |
| prospectivity | anchor `12:08:41Z` (GitHub activity `42816279926`, commit `1ac0f1dd…`) → designated `12:09:13Z` → round existed `12:19:00Z`. **Named 9 min 47 s before it existed.** |
## THE SAMPLE — checked by me against the input files, not taken from the runner's word
| split | n | required |
|---|---|---|
| tuning | **400** | 400 ✓ |
| holdout | **200** | 200 ✓ |
| validation | **2,000** | 2,000 ✓ |
- **pairwise overlaps: 0 / 0 / 0** — the three sets are disjoint
- **2,600 drawn; 0 are excluded ids** (dry-run 2,644 ∪ failed 2,000)
- **every drawn id is in the eligible file** — subset check true
Lists: `draw.tuning.json` `08d51c31…`, `draw.holdout.json` `c104692f…`, `draw.validation.json` `9890bc65…`
## WHAT IS AND IS NOT DONE
**Done:** anchor, designation, seed, draw — under the repaired candidate Duho approved (runtime `d1cd15d2…`, CORE `f4f782be…`, C `58f72730…`), the pinned invocation, and the unchanged adopted A1 `6b9ecc79…` and `run_path` `1c4f96fb…`.
**Not done, and each behind its own gate:** no protected image or label has been read, no rendering or scoring has run, no winner is frozen, the **holdout is unopened**, and the **single further validation attempt is unspent**.
**Preserved:** originals frozen (CORE `e9222abf…`, C `bbc08cd6…`), both failed journals `OUT_A1/` and `OUT_A1_FRESH/`, and the exposed rounds 6440756 and 6444980 — neither reused.
