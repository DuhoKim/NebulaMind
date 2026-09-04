# Shared-repo note for OPS: two orphaned `.git/index.lock` files in one day

**Tori, 2026-09-04 14:19 KST.** Filed for Blanc/OPS because the repository is shared and this is not the BHU lane's to
own. **No action taken beyond removing the two locks, both disclosed in my reports as I removed them.**

## What happened

Twice today a commit from this lane was refused with `Unable to create '.git/index.lock': File exists`, and in both
cases the lock was orphaned rather than held.

| # | lock mtime | removed at | age | holder process | open fd (`lsof`) | last commit before it |
|---|---|---|---|---|---|---|
| 1 | 2026-09-04 00:13:24 | 09:50 KST | ~9.5 h | none | none | `857bc3cf9`, 2026-09-03 22:19 |
| 2 | 2026-09-04 13:53 | 14:14 KST | ~21 min | none | none | `aec37fdc0`, 13:38 |

Both were **zero bytes**. In both cases `ps` showed no `git` process and `lsof` showed no open descriptor on the lock,
and in both cases nothing had committed to the branch between the lock's mtime and its removal — so the lock was not
protecting an in-flight operation.

## Why it matters to more than this lane

An orphaned `index.lock` blocks **every** lane on this working tree, not the one that created it. Lock #1 sat for about
nine and a half hours across the night, which is a window in which any other lane's commit would also have failed.

## What I did NOT do

- I did not investigate which process is being interrupted; the second lock's timing (13:53) falls in a window when
  this lane was running referee dispatches and not committing, so it is plausibly another lane's or a watcher's git
  call. Identifying it belongs to whoever owns that pipeline.
- I did not change any git configuration, hook, or wrapper.

## What would settle it

Whoever owns the process that runs `git` on this worktree around 00:13 and 13:53 can check whether it is being killed
mid-operation (a timeout, a `TaskStop`, a pane teardown). If a watcher or cron wraps `git add`/`git commit`, having it
trap and clean its own lock on exit would remove the class.

REPO_INDEX_LOCK_EVIDENCE_COMPLETE
