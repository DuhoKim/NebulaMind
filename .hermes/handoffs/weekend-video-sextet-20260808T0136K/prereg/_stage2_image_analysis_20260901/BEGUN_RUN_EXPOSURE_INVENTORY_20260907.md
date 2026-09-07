# Verified exposure inventory of the begun (aborted) run — read from the journal, not from memory
2026-09-07 22:34 KST. HWAO. Preparation record for the disposition decision. **No new access:** every
number below comes from artefacts this run already produced. Holdout and validation labels were never
opened and were not touched to write this.

## What exists, and what does not
`OUT_A1_REPAIRED/` contains `input-anchor`, `designation`, `seed`, `draw`, the three drawn lists,
`tuning.access`, `tuning.inventory`, `tuning.labels`, `tuning.created-digests`, `tuning.abort`.
**Absent, verified by name:** `tuning.json`, `holdout.json`, `validation.json`, `winner.json`.
There is no holdout or validation label file of any kind. So there is no scored configuration, no
objective, no winner — **no selection information exists that could leak.**

| exposure | count | kind |
|---|---|---|
| tuning identities **with labels** | 400 | labels read (values ∈ {−1, +1}) |
| holdout identities | 200 | catalogue IDs only — A1 line 92: not opening |
| validation identities | 2,000 | catalogue IDs only — not opening |
| image planes fetched | 398 bricks | pixel data, no labels |

## What excluding the 400 would cost a future draw
Counted from the three pinned selection inputs: eligible 11,837; dry-run exclusion list 2,644 (2,600 of
them in eligible); failed set 2,000 (1,954 in eligible) → **effective pool 7,283**. All 400 exposed
tuning identities are inside it. Removing them leaves **6,883 for a 2,600 draw — 2.65×**, so the
exclusion is affordable, though the margin is thinner than the raw eligible count suggests. That is the
arithmetic the decision needs; the decision itself is not mine.
