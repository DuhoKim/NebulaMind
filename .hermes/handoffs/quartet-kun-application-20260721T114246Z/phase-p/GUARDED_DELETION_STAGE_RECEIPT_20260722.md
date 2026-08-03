# Guarded Deletion Stage — Executed Receipt (G4a delete + G4b delete; G4c excluded)

**Marker:** `KUN_G4_GUARDED_DELETION_EXECUTED_20260722`
**Authorization:** Duho, explicit — *"proceed with the guarded deletion stage."*
**By:** Claude Code (Lab background session), 2026-07-22.
**Result:** G4a debris deleted · G4b test-DBs + 2 primary caches deleted · **G4c `.env` excluded by its own never-delete rule** · 8 protected caches preserved · no tracked file touched · HEAD unchanged (`ba6212c`).

---

## Pre-deletion verification (stop-rules honored)

- **G4a integrity:** recomputed SHA-256 of all 18 quarantined files vs `MANIFEST.txt` → **0 mismatches**; byte-identical to the 2026-07-22 ~21:25 quarantine move. The dwell (move → hours later → delete) is satisfied.
- **G4b safety:** all 18 test `*.db` and both primary `.pytest_cache` dirs confirmed **untracked** (`git ls-files` empty) and **gitignored** (`git check-ignore` positive). No tracked file at risk.
- **G4c:** `.env.redacted-…` confirmed present (2451 bytes) and **left entirely untouched** — not opened, not hashed, not moved, not deleted.

## What was deleted

**G4a — 18 debris files** (from out-of-repo quarantine `/Users/duhokim/NebulaMind/quarantine-g4a-20260722/`, now removed):
throwaway automation experiments (`click.js`, `find_deep.js`, `find_menu.js`, 11 `test_*.applescript`/`test_js_*`), one `.bak` (`backend/app/main.py.bak-labrunner`), temp files (`goru_temp_report.json`, `tmp_build_2929_trust_packet.py`, `wait_and_extract.py`). SHA-256 manifest preserved at `phase-p/G4A_DELETED_MANIFEST.txt`.

**G4b — 18 regenerable test databases + 2 pytest caches:**
- 8 repo-root `test*.db` + 10 `backend/test*.db` (503,808–561,152 bytes each) — ephemeral pytest fixtures, recreated on the next test run.
- `.pytest_cache`, `backend/.pytest_cache` (primary checkout only).
- SHA-256 + size manifest preserved at `phase-p/G4B_DELETED_MANIFEST.txt`.

## What was NOT deleted (deliberately excluded)

- **G4c secret-adjacent `.env`** (`backend/.env.redacted-before-disable-gemini-20260708_174609`). The G4c packet's own Rollback rule is **"NEVER hash, open, or delete."** Deletion is therefore off the table by design; the file is **retained, isolated, and untouched**. Any future disposition needs its own explicit, separate G4c decision — and even then the standing rule is retain-not-delete.
- **8 protected/worktree `.pytest_cache` dirs** (under `.claude/worktrees/…` and the sealed mastermind canary packets) — held for path-specific adjudication; **preserved**, verified present after deletion.

## Post-deletion verification

- `.env` still 2451 bytes, unchanged (never touched). ✅
- 8 protected caches all present. ✅
- `git status` shows **no tracked-file deletion**; HEAD `ba6212c` unchanged. ✅
- Regeneration sanity: `pytest backend/tests/test_trust_debate_stance_caps.py` → **4 passed** (the just-deleted `test_trust_debate_stance_caps.db` regenerated cleanly). ✅

## Safety ledger

`tracked_deletions 0 · git_writes 0 · source_edits 0 · db_content_reads 0 · env_opens 0 · env_hashes 0 · deploy_restart 0 · network 0`.
Reversibility: G4a/G4b were untracked throwaway/ephemeral; test DBs regenerate from tests; deleted-file manifests retained under `phase-p/` for provenance.

**Gate ledger:** G1 ✅ · G2 ✅ · G3 Closed · **G4a DELETED (executed) · G4b DELETED (executed) · G4c EXCLUDED — retain-only by rule** · G5 Closed · G6 map v1 BUILT+PASS · G7 Closed.
