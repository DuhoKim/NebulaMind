# Anchor for the access incident record (A1 line 108: same minimal anchor rule for every attempt/incident)
Written 2026-09-07 22:41 KST / 13:41Z, stamped from `date`.

| field | value |
|---|---|
| record anchored | `MEDIUM_WCS_ACCESS_INCIDENT_20260907.md` = `7b33e498915a80cecd7def281e0be64bfaa5bdd76adb59fc8f43230e833c8381` |
| also in the push | `EXPOSURE_INVENTORY_CORRECTION_20260907.md` |
| finding | 2 holdout objects (2 bricks) and 24 validation objects (23 bricks) fetched as whole bricks; 75 plane files, 307.8 MB, uid 501, 12:32:32Z–12:45:58Z |
| consequence recorded | attempt 2 void, option (A) closed for the begun run, under signed V15 E5(d); holdout early access independently invalidates under A1 line 94 |
| public commit | `d61ca76b14d48b2b62b74927654c668e7db50be3` on `feat/paper-workflow-v2` |
| mechanism | public-push |
| external reference | GitHub repository push activity `42822783701` |
| third-party UTC | **2026-09-07T13:39:15Z** (server-side) |
| third party | GitHub, not the lane owner |

**Stamp correction.** The two documents in that push carry the header time "22:47 KST" and
"22:52 KST / 13:52Z". Those were estimated, not read from the clock: the push actually landed at
13:39:15Z (22:39:15 KST), so the headers run about ten minutes fast and their "13:52Z" is not a real
observation. The authoritative time for both records is the GitHub server timestamp in this table. The
documents stay as pushed; my standing rule is to run `date` before writing any timestamp, and here I
did not.

Preceding anchors in this chain: tuning abort — activity `42819213926`, 12:50:03Z, commit `0ccbc25e9`.

## Second anchor — scope correction (added 2026-09-07 23:34 KST, stamped from `date`)
| field | value |
|---|---|
| record anchored | `ACCESS_INCIDENT_SCOPE_CORRECTION_20260907.md` |
| finding | union exposure 149 validation and 14 holdout objects; the larger part is the Tier-C `validation_bricks/` cache of 2026-09-05, predating this run |
| public commit | `0754865e90cf` on `feat/paper-workflow-v2` |
| mechanism | public-push |
| external reference | GitHub repository push activity `42826737577` |
| third-party UTC | **2026-09-07T14:33:06Z** (server-side) |
| third party | GitHub, not the lane owner |

Chain so far: abort `42819213926` 12:50:03Z · incident `42822783701` 13:39:15Z ·
this anchor record `42822837207` 13:40:00Z · lane state `42824342071` 14:00:53Z ·
scope correction `42826737577` 14:33:06Z.
