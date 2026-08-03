# Backup & Rollback — NM-C2V2-20260727-A (create-only)

**Classification: HIGH-RISK** live/public/current-Lab mutation, bounded by create-only controls. Paths are repo-relative to `/Users/duhokim/NebulaMind/NebulaMind`.

## Backup
**None** — this is a strictly create-only promotion; no existing byte is overwritten, so there is nothing to back up.
**GUARD (abort condition):** every one of the four exact target paths AND the run directory MUST be `ABSENT` immediately before execution:
- `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a.json`
- `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/` (and its `draft.pdf`, `draft.tex`, `result.png`)
If ANY target is occupied, **ABORT** — do not overwrite, do not proceed. (A create-only promotion must never turn into a replace.)

## Create ordering (so discovery never exposes a partial run)
1. `mkdir` the run directory `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/`.
2. Copy the three artifacts: `draft.pdf`, `draft.tex`, `result.png`.
3. Verify each artifact SHA-256 (`ac59ac60…` / `bb77d38d…` / `ed83a825…`).
4. Create the manifest `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a.json` **LAST** (byte-identical to `PREVIEW_MANIFEST.json`, 2,566 B / `fa4c8155…`).

Rationale: `list_runs` and `get_run` surface a run only when its `<id>.json` exists (with `status:"done"` + non-empty `result.summary`). Creating the manifest last guarantees the run never appears — and no artifact endpoint is advertised — until all three artifacts are present and hash-verified. No partial/broken run is ever discoverable.

## Rollback ordering (manifest-first)
1. Remove the manifest `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a.json` **FIRST** — this immediately removes the run from `list_runs`/`get_run` discovery.
2. Then remove only the three exact files: `.../c2v2e2e0726a/draft.pdf`, `.../draft.tex`, `.../result.png`.
3. Then remove the exact now-empty directory `.../c2v2e2e0726a/` with `rmdir` (fails safe if unexpected content remains).

## Guard conditions (mandatory)
- Only ever target the exact id `c2v2e2e0726a`. Never a wildcard, glob, or parent path.
- Before removing the directory, verify it contains ONLY the three expected files.
- Never touch `gated-e2e-demo` or any other run.
- **Never use `rm -rf` on `lab-runs` or any unguarded broad deletion.** Use explicit per-file `rm -f <exact path>` and a final `rmdir <exact dir>`.
- After rollback, verify all four target paths + the run directory are ABSENT again.
