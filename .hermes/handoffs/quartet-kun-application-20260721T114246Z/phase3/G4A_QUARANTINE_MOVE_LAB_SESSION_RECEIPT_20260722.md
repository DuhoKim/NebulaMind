# G4a quarantine MOVE — executed (non-destructive) by the Lab session

Run: quartet-kun-application-20260721T114246Z · G4a stage
By: Claude Code (Lab session) on Duho's explicit authorization ("go ahead with the cleanup move").
Date: 2026-07-22 ~21:30 KST.

## What was done — MOVE only, NOT deletion
Moved the 18 ratified G4a debris candidates (throwaway scripts, one .bak, temp files) OUT of the
primary checkout into an out-of-repo quarantine, with a SHA-256 manifest and a reverse script.
- Quarantine dir: /Users/duhokim/NebulaMind/quarantine-g4a-20260722/  (MANIFEST.txt + RESTORE.sh)
- 18/18 moved; each byte-verified (sha256 identical before/after); all were UNTRACKED (0 tracked touched).
- Primary untracked count: 364 -> 346 (exactly -18).
- Fully reversible: `sh quarantine-g4a-20260722/RESTORE.sh` moves them all back.

## Scope discipline (per Phase-4 ratification R3-R7)
- G4a ONLY. G4b (test .db files + 2 caches) and G4c (.env) NOT touched — separate gates, unbundled.
- The 8 HELD cache paths under .claude/worktrees + mastermind: NOT touched (need individual adjudication).
- DELETION not performed — this is the quarantine/dwell stage. Deletion is a later explicit step.
- No tracked file, no source, no parallel-track work, no .env content touched. HEAD unchanged (826e733).
