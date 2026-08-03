# P0 Guarded Apply Plan

Status: `LOCKED__NO_APPLY_APPROVAL`

## Preconditions

1. User supplies the exact apply gate with the final manifest SHA-256.
2. The gate explicitly repins the serve-matching `paper-backups/.../after.tex` snapshot as the P0 candidate source, or names another verified canonical generator.
3. All current-source hashes match `exact_diff.json`.
4. Review scope remains broader, but writable scope stays limited to the four paths in `APPROVAL_PACKET.md`.
5. No stop/freeze marker or overlapping worktree change exists.

## Apply sequence

1. Preserve current scoped `git status`, current file hashes, and the combined patch hash without staging anything.
2. Run all three non-mutating `git apply --check` commands.
3. Apply `red_test_only.patch`.
4. Run the focused test and require the intended stale-claim RED.
5. Apply `green_source_only.patch`.
6. Run the focused test and require `P0_CORRECTION_STATE_PASS`.
7. Compile only in an isolated temporary directory using the pinned figures.
8. Run structural extraction and 300-dpi visual acceptance.
9. Obtain fresh, no-self-review Lana science, Kun adversarial/custody, and Goru mechanical/numeric receipts against the exact candidate PDF/source hashes.
10. If any review changes source, freeze the failed candidate, version a new packet, and use fresh reviewers.
11. Stop with `VERIFIED_IN_WORKTREE_NOT_DEPLOYED`.

## Explicit exclusions

- Do not copy the candidate PDF into the public root.
- Do not change the public audit report or history JSON.
- Do not restart or deploy the frontend.
- Do not mutate a Lab/DB/wiki record.
- Do not run `git add`, commit, push, merge, rebase, reset, restore, checkout, or clean.

## Separate later gates

Publication and runtime activation must be separately approved after the applied candidate passes fresh review and render verification.
