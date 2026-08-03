# P0 Rollback Plan

Status: `PREPARED_NOT_NEEDED`

Rollback applies only if a later source-apply gate is opened and the patches are applied.

## Preferred patch rollback

From the rich live repository root:

1. `git apply --reverse --check <packet>/green_source_only.patch`
2. `git apply --reverse <packet>/green_source_only.patch`
3. `git apply --reverse --check <packet>/red_test_only.patch`
4. `git apply --reverse <packet>/red_test_only.patch`

Then verify the original hashes:

- `after.tex`: `de4b6140d0af6ad68d5077999cc393da09958fa7c469d4ec8015a1c28c608039`
- `FrontierDrafts.tsx`: `071a8cb092513c23cdc5ffb7f886d696f9d2ffed758084352b536aed3ec862c2`
- `paperScores.ts`: `868845cdeb0f824ac03cec3a327fcc5fb9ade43a07d79db7d4dee8fd927eb8bb`
- `frontend/scripts/test-p0-correction-state.mjs`: absent

## Guardrails

- Do not use `git reset --hard`, `git clean`, broad checkout/restore, or history rewriting.
- Do not overwrite a concurrently changed path. Freeze and reconcile instead.
- If a candidate PDF was generated in a temporary directory, delete only that temporary candidate after verifying it is not the current served file.
- Public rollback is not part of this packet because no public apply is authorized.
