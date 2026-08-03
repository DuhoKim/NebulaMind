# Governance — `tools/watch_subnav_videos.py` (the subnav video embed watcher)

Established 2026-08-03 per Kun architecture-audit R3 / delta-re-audit action #1, on Duho's word
("commit and govern the subnav watcher"). Owner: Hwao. Status at writing: **dormant** (not running,
no launchd job; last activity 2026-07-19).

## What it is

An autonomous production deployer: polls the crew video-delivery file every 60 s and, when Yui's
lane drops new UNLISTED YouTube IDs, patches `subnavVideos.ts` **in the live serving worktree**
(`NebulaMind-origin-main-live`), runs `npm run build`, and kickstarts `com.nebulamind.frontend`.

## Rules

1. **Allowed writes** — exactly one product file: `frontend/src/app/lab/subnavVideos.ts` in the live
   worktree, plus its own log and receipts. Any scope growth requires a new governance entry here.
2. **Input** — only `…/video-briefs/subnav-explainers-delivery.json`, written by Yui's video lane.
   IDs are format-validated (11-char YouTube ID) before use.
3. **Receipts (mandatory)** — every mutation writes
   `…/video-briefs/receipts/subnav_embed_<ts>.json` (git-tracked class): changed/before/after ID
   maps, deploy outcome, and the post-build `BUILD_ID`. Implemented in `write_receipt()`; a
   mutation without a receipt is a bug.
4. **Git capture** — the watcher writes the working tree only, never git. Its mutations make the
   live worktree dirty by design; they must be landed to `main` promptly via the proven path
   (branch → PR → review → squash → live fast-forward), as done for the Ruk9fTgn5_E→piNaIKTedHQ
   swap in PR #129. Dirty-live time should be hours, not weeks.
5. **Single-deployer rule** — before any *manual* promotion/rebuild of the live frontend, check the
   watcher is not mid-build (`pgrep -fl watch_subnav_videos`); stop it or wait out its tick. Two
   concurrent `next build`s in one checkout race each other.
6. **Run/stop** — run manually in a lane pane (`python3 tools/watch_subnav_videos.py`); no cron, no
   launchd (keeps it a supervised lane tool, not unattended infrastructure). Log:
   `…/video-briefs/embed_watch.log` (untracked, rolling).
