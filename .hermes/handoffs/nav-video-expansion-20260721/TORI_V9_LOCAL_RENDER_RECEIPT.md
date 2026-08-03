# Tori receipt — remaining Lab navigation videos rendered locally

Marker: `TORI_V9_REMAINING_NAV_LOCAL_RENDER_COMPLETE_20260721`

## Happened

The user asked to generate videos for the remaining Lab navigation and asked whether the character should change for each Nav.

Hwao coordinated first and wrote `HWAO_VIDEO_EXPANSION_PLAN.md` with marker `HWAO_NAV_VIDEO_EXPANSION_PLAN_COMPLETE_20260721`.

The current served Lab source was used as truth. It defines four top stages: Topic, Data, Methods, and Paper. Topic already has five videos. Data, Methods, and Paper were the remaining top stages.

## Character decision

Do not replace the character per Nav.

The same established female astronomer remains the recognizable host and uses the same clearly female Emma narration. The set changes by stage:

- Data — teal/blue observational astronomer;
- Methods — indigo/violet computational astrophysicist;
- Paper — warm-gold research editor/referee.

This preserves series recognition while giving each Nav a distinct visual identity.

## Result

Three local exact-audio review masters were generated:

- Data: `/Users/duhokim/HermesOps/scripts/clips/lab_stage_overviews_v9/NEBULAMIND_SUBNAV_DATA_V9_FEMALE_VOICE_EXACT_LIPSYNC.mp4`
- Methods: `/Users/duhokim/HermesOps/scripts/clips/lab_stage_overviews_v9/NEBULAMIND_SUBNAV_METHODS_V9_FEMALE_VOICE_EXACT_LIPSYNC.mp4`
- Paper: `/Users/duhokim/HermesOps/scripts/clips/lab_stage_overviews_v9/NEBULAMIND_SUBNAV_PAPER_V9_FEMALE_VOICE_EXACT_LIPSYNC.mp4`

Scene-aligned SRT files, generation scripts, build receipts, contact sheets, QA receipt, and hash-pinned delivery manifest are in:

`/Users/duhokim/HermesOps/scripts/clips/lab_stage_overviews_v9/`

## Verification

All three masters passed:

- exact duration: 73.500 seconds;
- exact frame count: 1,764;
- 1280×720 H.264 video at 24 fps with AAC audio;
- four full clean decode passes per master;
- CFR-normalized presenter intermediates, GOP-safe scene concatenation, and warning-free final video/audio decode;
- exact six-cue caption text and timing;
- calibrated female driver pitch: Data 175.8 Hz, Methods 177.8 Hz, Paper 177.8 Hz;
- 24 evenly spaced visual samples per master, 72 total;
- one stable female identity, varied speaking expressions, no duplicate faces, corruption, black frames, clipped overlays, or unresolved Methods glyph/arrow issues.

QA marker: `NEBULAMIND_V9_REMAINING_NAV_QA_COMPLETE`

Delivery marker: `NEBULAMIND_V9_REMAINING_NAV_LOCAL_DELIVERY_READY`

## Changes and gates

Changed locally:

- created the three video masters, three SRT files, production scripts, QA artifacts, and receipts;
- created this handoff and the Hwao planning receipt.

Not changed:

- no YouTube upload or visibility mutation;
- no website or `subnavVideos.ts` edit;
- no production embed/delivery-manifest edit;
- no deploy/restart;
- no DB/API write;
- no git commit or push.

## Exact next action

Review the three local masters. If approved, authorize uploading them as Unlisted review copies. Public visibility and website embedding remain separate explicit gates.
