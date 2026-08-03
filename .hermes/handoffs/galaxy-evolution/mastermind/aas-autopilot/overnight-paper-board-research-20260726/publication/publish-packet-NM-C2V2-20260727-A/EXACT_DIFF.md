# Exact Diff — NM-C2V2-20260727-A (four creates only)

**Classification: HIGH-RISK** (a live/public/current-Lab mutation, bounded by create-only controls). Every operation below is a CREATE whose `before` state is `ABSENT`. There is **no replace, update, delete, or baseline mutation**.

All target paths are repo-relative to the NebulaMind repo root (`/Users/duhokim/NebulaMind/NebulaMind`).

## Operations
| # | target (repo-relative) | op | before | after — source → bytes / SHA-256 |
|---|---|---|---|---|
| 0 | `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/` (directory) | MKDIR | ABSENT | new empty directory |
| 1 | `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/draft.pdf` | CREATE | ABSENT | ← V2 `candidate.pdf` → 84,831 B / `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d` |
| 2 | `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/draft.tex` | CREATE | ABSENT | ← V2 `candidate.tex` → 6,647 B / `bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6` |
| 3 | `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/result.png` | CREATE | ABSENT | ← V2 `result.png` → 38,386 B / `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` |
| 4 | `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a.json` | CREATE (LAST) | ABSENT | ← `PREVIEW_MANIFEST.json` → 2,566 B / `fa4c815578aef3f01a7e18985f83725fefab052d4735987577f77f76f4d6b0ba` (byte-identical copy) |

Total: 1 new directory + 4 new files. The manifest (op 4) is created LAST so the run is never discoverable while incomplete.

## Explicitly NOT changed
- No file is replaced, updated, or deleted.
- The baseline run `gated-e2e-demo` is untouched: `.hermes/handoffs/galaxy-evolution/lab-runs/gated-e2e-demo/draft.pdf` `0d863bff4d4d260fe32e56617ca6f920f2943574aaff2a5faeee3f7460575933`, `.../gated-e2e-demo/draft.tex` `f1aeadd8ea43f2fd1e22e9686d23066fdf95e3d5c95937a42d8ddd076bc95a8a`, `.../gated-e2e-demo.json` `46ddd75d5f0e5814e814333336d8e6d1b011382c46509012af2aea8cc20af5e2` — unchanged before and after.
- No other `.hermes/handoffs/galaxy-evolution/lab-runs/` entry, no public/static root, no DB/wiki, no `backend/**` source, no git/cron/deploy changes.
