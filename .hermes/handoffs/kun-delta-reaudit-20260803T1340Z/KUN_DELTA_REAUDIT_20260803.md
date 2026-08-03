# KUN DELTA RE-AUDIT — after tonight's merges (2026-08-03 late KST)

Task ID: `kun-delta-reaudit-20260803T1340Z`
Reviewer: Kun on Hermes via Nous Portal route `moonshotai/kimi-k3`
Date: 2026-08-03 (~22:40-23:10 KST / 13:40-14:10 UTC)
Baseline: my own architecture audit (`kun-architecture-audit-20260803T1010Z`) and PR review (`kun-pr-review-20260803T1230Z`).

---

## 1. Verification table — claim → verdict → evidence

| # | Claim | Verdict | Independent evidence |
|---|---|---|---|
| 1a | PR #129 squash-merged → `636f118` | HOLDS | `gh pr view 129`: state MERGED, mergeCommit `636f1180…`, mergedAt 11:10:21Z. Commit on origin/main with full message. |
| 1b | PR #130 squash-merged → `eee27d6`; origin/main tip = eee27d6 | HOLDS | `gh pr view 130`: MERGED, `eee27d61…`, 11:10:24Z. `git rev-parse origin/main` = eee27d61b4519bc51b9b4f7cfbaf6751ebe2a733. |
| 1c | Remote PR branches deleted | HOLDS | `git ls-remote --heads origin` grep: neither `live-state-capture-20260803` nor `frontier-scheduler-lane-20260803` present (fetch --prune also showed the deletion). |
| 1d | (implicit) squashes preserve reviewed content | HOLDS | patch-id(9c7941c→636f118) = `ae3a8748…` = patch-id(9c7941c→e4b4ac5). patch-id(636f118→eee27d6) = `bc964b59…` = patch-id(9c7941c→78c2949) from my PR review. Merged content == reviewed content, exactly. |
| 2a | Live worktree main reset --hard to eee27d6, clean, 0 ahead/0 behind | HOLDS | Live checkout: tip eee27d6, `git status` = 0 entries, rev-list counts 0/0, on branch main. |
| 2b | Frontend byte-identical through the reset | HOLDS (indirect but strong) | Pre-reset I verified all 10 files byte-match e4b4ac5; 1d proves merged 636f118 is patch-identical to e4b4ac5; live is now at eee27d6 = 636f118 + backend-only #130 (zero frontend files). Transitivity closes it. |
| 3a | Production rebuilt from merged commit; new BUILD_ID `t-4cjL-dL-rFMEM4WMxlC` | HOLDS | Live `.next/BUILD_ID` = `t-4cjL-dL-rFMEM4WMxlC`, mtime 2026-08-03 20:11:08 KST (after the 20:0x merges; supersedes `Pja97kcysgU-…`). |
| 3b | Service kickstarted; nebulamind.net/lab 200; chunk carries promoted data | HOLDS | My own probe: `/lab` HTTP 200 (0.95s). Served HTML references chunk `page-dd7fb6189c351d9f.js` (NEW hash ≠ the 19:00 `page-3609d8a748976e0c.js` — consistent with a fresh build). Fetched the chunk: `size:1317` present ×1, `size:1316` absent, promoted cluster name "JWST high-redshift galaxy evolution and emission" present. Served artifact is now end-to-end git-traceable: eee27d6 → build 20:11 → serve. |
| 4a | Dev worktree on branch `studio-dev` fast-forwarded to eee27d6 | HOLDS | HEAD == origin/main == eee27d6 on branch `studio-dev`. Detached HEAD (my R2) resolved. |
| 4b | 3 untracked scheduler copies deleted after byte-verification | HOLDS (deletion verified; byte-verification taken on receipt) | The 3 files exist only as TRACKED files now (`git ls-files` lists all three; no `??` entries). Merged tests run in dev: 5 passed, 1 skipped — consistent with byte-identity of the surviving tracked copies. The pre-deletion comparison itself was Hwao's step; outcome is consistent. |
| 4c | Dev dirt = exactly docker_compose_init.sh + wiki_schema.md modified + ~313 untracked | HOLDS EXACTLY | `git status`: modified = `scripts/docker_compose_init.sh`, `wiki_schema.md` ONLY (frontiersData.ts absorbed; lab_runner_worker.py/overnight_loop.py committed via #128). Untracked count: 313. |
| 5a | C1–C4+C6 deletions executed (24 in-repo + 3 LaunchAgents backups) | HOLDS (spot-verified by absence) | tools/*.bak* now 0 files (was 8+); 5 root *.applescript gone (root untracked now only `.hermes.md`); 3 stale plist backups absent from ~/Library/LaunchAgents. I did not enumerate all 24 pre-deletion, but every target class I named in my audit is gone. |
| 5b | C5 WITHDRAWN — celerybeat .db.db is the LIVE beat schedule DB | HOLDS — and the withdrawal was CORRECT | `backend/celerybeat-schedule-v2.db.db` still present, mtime TODAY 20:24 (actively written). `ps` shows celery beat at pid 2548 running from this repo path — matches the brief's claim exactly (I verified pid 2548 independently before reading it in the brief; it was in my ps output). Deleting it would have been a live-service mutation. Good catch by whoever proved it. |
| 5c | `.env.redacted-…` moved to ~/HermesOps/secure/ (700/600) | HOLDS (name/stat only, per constraint) | Absent from repo (ls: No such file). Present at `~/HermesOps/secure/.env.redacted-before-disable-gemini-20260708_174609`, file perms 600, dir perms 700, owner duhokim. Never opened. |
| 6a | Receipt addendum appended | HOLDS | Read it: "Addendum — merge + traceable rebuild, 2026-08-03 ~22:2x KST" — records squashes, reset, rebuild BUILD_ID, probes, dev ff, cleanups, actor, authorization. Every checkable line matched my independent measurements (see note in §3 about one chunk-hash discrepancy). |
| 6b | Goru's clone removed; stale local branch deleted | HOLDS | `.claude/worktrees/`: `frontier-scheduler-lane` absent (4 other unrelated worktrees remain). No local PR branches remain; local branch count 34 (unchanged from morning — the PR branch was created-and-deleted within the day, others untouched). |

Overall: 14/14 claims hold, 12 fully verified by my own independent evidence, 2 (4b's pre-deletion byte-compare, and the deletion count "24") verified by outcome-consistency rather than re-execution.

## 2. Risk register re-score

- **R1 (live product not reconstructible from git) — CLOSED.** Live = clean main @ eee27d6 == origin/main; build 20:11 KST from that commit; served chunk content verified against promoted data. End-to-end traceable. Residue: none for the frontend; see N3 below for a remaining non-frontend gap.
- **R2 (detached HEAD + live-writing automation) — CLOSED.** Dev now on named branch `studio-dev` at origin/main tip. Residue: 34 local branches + 2 stashes remain (entropy, not a hazard).
- **R3 (receipt-less auto-writers mutating the serving tree) — PARTIALLY CLOSED, residue remains.** The subnavVideos swap it produced is now committed, so the CURRENT mutation is captured. But the writer itself — `tools/watch_subnav_videos.py` — is STILL UNTRACKED in dev (`?? tools/watch_subnav_videos.py`) and there is no governance receipt describing when it may write to the live tree. Same class, reduced instance. New action below.
- **R4 (frontier-daily 429 resilience unproven under launchd) — UNCHANGED, correctly.** Retry patch is in the engine script; first unattended 14:00 KST run with the patched pipeline is tomorrow (2026-08-04). No new evidence either way tonight. Receipts dir shows no post-094048Z daily runs — consistent.
- **R5 (WIP scheduler in production path untracked) — CLOSED.** Module + both tests tracked on main via #130; quarantine verified honest in my PR review; tests green in dev tonight (5 passed, 1 skipped). The production daily job now runs committed code.
- **R6 (hygiene/secret-adjacent) — CLOSED with one deliberate exception.** .bak files, applescripts, stale plists, .env.redacted all cleared (verified). Exception is principled: celerybeat `.db.db` retained because it is the live beat schedule (C5 withdrawal verified correct). Untracked count 341 → 313.
- **R7 (Baseline board staleness) — UNCHANGED.** Board still `Updated: 2026-07-21 22:43:53 KST`; status/debate-map design artifact still absent. 13 days stale now.

## 3. NEW risks / observations introduced or surfaced tonight

- **N1 (LOW) — Receipt addendum chunk-hash mismatch (documentation accuracy, not product truth).** The 19:0x receipt section says the then-served chunk was `page-3609d8a748976e0c.js`; my independent fetch tonight of the post-rebuild page shows `page-dd7fb6189c351d9f.js`. These are consistent (different builds), BUT the addendum's "lab chunk carries promoted data" line doesn't record the NEW chunk hash — a future auditor correlating BUILD_ID → chunk will find the hash only in my report. Trivial fix: append the hash to the addendum.
- **N2 (LOW-MEDIUM) — `.hermes/` and `.hermes.md` are entirely untracked.** Tonight's alignment made this visible: the repo's entire coordination layer — doctrine, boards, receipts (including the promotion receipt both PRs cite), plans, this audit trail — exists in NO commit, in EITHER checkout. If the working tree is lost, the product is reconstructible but the project's memory is not. This predates tonight but is now the single largest unprotected artifact class. (Board protocol may deliberately keep it repo-local-untracked; if so, that decision should be recorded with a backup story.)
- **N3 (LOW) — Squash semantics + reflog are now the only record that the served 18:57 build (`Pja97kcysgU-…`) ever existed.** That build was never a commit (its content became 636f118 only at 20:0x). Fine operationally, but it means "what exactly served between 18:57 and 20:11" is answerable only via receipts, not git. The receipt covers it — this is the receipt culture working as designed; noting the dependency.
- **N4 (INFO) — New untracked frontend WIP appeared:** `frontend/src/app/lab/rankMovement.ts` + `frontend/scripts/test-topic-rank-movement.mjs` + `frontend/public/human-cal/` (3 untracked entries). Not in tonight's claims; likely active work. Watch that it goes through the now-proven commit-and-merge path rather than accumulating as another hand-patched layer.
- **N5 (INFO) — ps-output artifact:** my earlier combined command embedding beat-pid extraction was denied mid-flow once; no retries were made. Beat pid 2548 was verified in a separate approved ps call. No operational impact.

## 4. Prioritized next actions (owner / action / evidence / gate)

1. **Hwao — Close R3's residue: track or govern `tools/watch_subnav_videos.py`.** Commit it (it's small) plus a one-paragraph governance note: when it writes, where receipts go. Evidence: file tracked; note in repo or board. Gate: normal review; user git gate for commit.
2. **Hwao + user — Decide the `.hermes/` protection story (N2).** Options: track it in-repo (it's already inside the repo dir), or a scheduled off-repo backup with receipts. Evidence: recorded decision + either first commit or first backup receipt. Gate: user decision (policy).
3. **Hwao — Append the post-rebuild chunk hash (`page-dd7fb6189c351d9f.js`) to the promotion receipt addendum (N1).** Evidence: receipt line. Gate: none (docs).
4. **Tori — Tomorrow 2026-08-04 after 14:00 KST: verify the first UNATTENDED patched frontier-daily run.** Evidence: fresh `daily_frontier_ingest_*.json` receipt with post-14:00 timestamp + empty 429 tail in error log. Gate: none (read-only verification). This closes R4.
5. **Hwao/Lana — Baseline board refresh or explicit HOLD note (R7).** Either land the status/debate-map design proposal or date-stamp an explicit "held during post-DESI resumption" note so the board's staleness is a decision, not drift. Evidence: board edit. Gate: existing docs-only gate.
6. **Goru — Sweep decision for the remaining 313 untracked** (274 docs/, 29 tools/ incl. `R15_prompt.txt`, 3 frontend incl. N4 WIP, `generate_video_gemini.py`, `tests/`, `playwright_test/`): triage list with keep/archive/delete per cluster. Evidence: inventory report. Gate: user approval before deletions/commits.
7. **Goru — Route the N4 frontend WIP (rankMovement + test-topic-rank-movement + human-cal) through the proven path** when ready: branch → PR → review → squash → live reset → rebuild receipt. Evidence: PR number + rebuild receipt. Gate: standard.

## 5. Evidence ledger

Commands (read-only):
- Dev: `git fetch origin --prune`; `git log --oneline -4 origin/main`; `git rev-parse origin/main` (eee27d6); `git show 636f118|eee27d6 --stat`; patch-id comparisons (e4b4ac5 vs 636f118 = ae3a8748…; 9c7941c→78c2949 reconstructed bc964b59… vs 636f118→eee27d6 bc964b59…); `git cat-file -t 78c2949` (gone from dev store — expected post-clone-removal; review-time verification stands); `git branch --show-current` (studio-dev), HEAD == origin/main; `git status` full + cluster counts (2 modified / 313 untracked); `git ls-files` for the 3 scheduler files + frontierScope + smoke test (tracked); `git ls-files tools/watch_subnav_videos.py` (untracked); `git ls-files .hermes/` (0); `git check-ignore .hermes/...` (not ignored — simply never added); `git check-ignore`/`.gitignore` read; `git ls-files --error-unmatch .hermes.md` (untracked).
- gh (read-only): `gh pr view 129|130 --json state,mergedAt,mergeCommit`; `git ls-remote --heads origin` grep (branches gone).
- Live checkout: `git log -3` (tip eee27d6), `git status` (0), rev-list 0/0, `.next/BUILD_ID` content + mtime (t-4cjL-dL-rFMEM4WMxlC, 20:11:08).
- HTTP probes (GET only, lane-local temp files): `https://nebulamind.net/lab` → 200; saved HTML to `_tmp_lab.html`, extracted chunk name `page-dd7fb6189c351d9f.js`; fetched chunk to `_tmp_chunk.js` (278,205 bytes); greps: `size:1317` ×1, `size:1316` ×0, promoted cluster name ×1.
- Hygiene verification: `ls` absence checks (tools/*.bak* = 0, 5 applescripts gone, .env.redacted absent from repo); `stat` (NOT open) of `~/HermesOps/secure/` (700) and the moved file (600); LaunchAgents listing (3 stale backups gone); `ps aux | grep celery.*beat` (pid 2548 from this repo's venv); celerybeat .db.db stat (16.5MB, mtime today 20:24 — live).
- Receipts: full read of `PROMOTION_RECEIPT_20260803_frontier_staging_to_live.md` incl. addendum; receipts dir listing (no post-094048Z daily runs yet).
- Tests executed: dev `pytest tests/test_frontier_ranking_scheduler.py tests/test_arxiv_daily_intake.py -q` → 5 passed, 1 skipped; `node scripts/test-galaxy-frontier-scope.mjs` → `galaxy_frontier_scope_ok`. No litter (tmp_path fixtures; post-run status unchanged apart from pre-existing entries).
- Board: head read of `paper-prose-distillation-board.md` (Updated 2026-07-21 — R7 unchanged).

Temps: `_tmp_lab.html`, `_tmp_chunk.js` inside this lane dir (per constraint). One earlier combined command (curl|grep pipeline with schemeless-URL flag) was denied by the security gate; it was decomposed into approved single GETs with local saves. No deletions performed anywhere by me.

## 6. Uncertainties

- The "24 in-repo deletions" exact count: I verified the absence of every target class named in my audit and the count delta (341→313 = 28 fewer untracked entries, consistent with 24 deletions + 3 scheduler files becoming tracked + 1 .env move), but did not have tonight's deletion manifest to diff against. Outcome-consistent.
- Hwao's pre-deletion byte-verification of the 3 scheduler copies: the surviving tracked copies pass their tests and patch-id equality with the reviewed PR content holds; the deleted dev copies' byte-identity is receipt-only (low residual risk: even if a deleted copy had differed, the tracked version is the reviewed, merged one — which is what matters).
- The origin of `frontend/public/human-cal/` and rankMovement WIP (N4): unclaimed in tonight's receipts; presumed active work-in-progress, not verified.
- Not inspected (unchanged constraints): .env* contents anywhere; production DB; the 274 untracked docs/ files individually; the 4 remaining `.claude/worktrees/` contents; tmux/live service internals beyond ps/stat/probes above.

---

KUN_DELTA_REAUDIT_COMPLETE_20260803T1340Z
