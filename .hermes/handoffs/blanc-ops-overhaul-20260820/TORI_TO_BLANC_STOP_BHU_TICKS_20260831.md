# TORI → BLANC: stop the BHU (tori) tick sources — Duho's call

**Date:** 2026-08-31 · **Requested by Duho, verbatim:** "stop the ticks for now, nothing to do."

Both BHU tick sources are yours to stop; I did not touch either — the nudger is your HermesOps
single-writer file and also drives **hwao**, and the backstop cron is in your session where I have
no access. So this is a request, not a change I made.

## Please stop these two tori tick sources (keep hwao's untouched):

1. **launchd lane-nudger** (`com.nebulamind.lane-nudger` → `scripts/nm_lane_nudger.sh`), currently
   `SESSIONS=(hwao tori)`. **Drop `tori`, keep `hwao`** — Duho only asked to stop BHU. Either edit
   the default in the script or set `NM_NUDGE_SESSIONS=hwao` in the plist env + reload. Fully
   reversible: re-add `tori` when BHU work resumes.
2. **Your BHU backstop cron** (the "BHU lane tick (Tori)" fires). Stop/pause it for tori; I cannot
   reach it.

## BHU state at stop (nothing is unfinished):
- Corpus complete + double-gated; OPEN_QUESTIONS empty; battery 78/78 green.
- `/lab/bhu` deployed live (pin 117a5273b; nebulamind.net/lab/bhu = HTTP 200).
- Branch in sync with origin (0 0).
- SSH Downloads drop-check suspended (host asleep, 2 timeouts) — recorded in
  `bhu-acquisition-20260828/WRAP_UP_20260830_FULL_DAY.md`.

Resume the tori ticks when Duho drops a holdout PDF (42/47/Silk) into ~/Downloads or reopens the lane.
