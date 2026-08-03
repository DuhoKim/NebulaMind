# Gate C apply plan

1. Revalidate the promotion receipt, preview hashes, target before-hashes, scoped cleanliness, protected siblings, and pipeline lock/transaction state.
2. Hold the frontier pipeline lock.
3. Apply exact text replacements to four hash-pinned targets using the verified preview JSON/TypeScript.
4. On any replacement/readback failure, restore all four snapshots immediately and verify before-hashes.
5. Confirm target after-hashes and protected sibling hashes.
6. Run run-local ranking tests and a clean frontend build in the non-live worktree.
7. Do not rebuild or restart the running live production process.
8. Seal an application receipt and guarded rollback handoff.
