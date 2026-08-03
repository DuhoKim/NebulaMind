# Five Nebula paper videos — unlisted review receipt

Marker: `NEBULAMIND_FIVE_PAPER_UNLISTED_REVIEW_READY_V1`

Verified: `2026-07-22T12:43:48Z`
Channel: `NebulaMind` (`UCUHBNGk8ozEnisQRuchoS4Q`)
Status: **five unlisted review videos complete**

## Review lineup

### 1. The z≈9–10 unlensed metallicity deficit

- Review URL: https://youtu.be/hHxmycvPalE
- Video ID: `hHxmycvPalE`
- Privacy: `unlisted`
- Processing: `succeeded`
- Embeddable: `true`
- Manual English captions: `serving`
- Master SHA-256: `1bd1ae30668c3941431a4d99f323458d60dd54e110bd4248caf145fc200aa13b`
- SRT SHA-256: `c300f859a76138935547dc6a927101f51e025dbfa47f03672288f7eb67f4120c`

### 2. Galaxy scaling relations from SDSS to JWST

- Review URL: https://youtu.be/QjdJ1WZpiJY
- Video ID: `QjdJ1WZpiJY`
- Privacy: `unlisted`
- Processing: `succeeded`
- Embeddable: `true`
- Manual English captions: `serving`
- Master SHA-256: `d3ef10101962c83eaa76210d23ff4b50e1baac1374f935a1bcdb30d29db252e8`
- SRT SHA-256: `cbfed01639a3dda02abb2060d8f31fdded8b9122cfc10e5de5a698e04df51b19`

### 3. Is “Too Massive, Too Early” robust?

- Review URL: https://youtu.be/XiB4dpn2o3g
- Video ID: `XiB4dpn2o3g`
- Privacy: `unlisted`
- Processing: `succeeded`
- Embeddable: `true`
- Manual English captions: `serving`
- Master SHA-256: `57af454c94bbaa0b793a0a3fb7a624ae7ed7937412da967f46eca4ea0d85a6d7`
- SRT SHA-256: `aafe6dc03eadb7a9d43d5e476c1b1d87da7994b137a2805d6bf968dbcdfce40f`

### 4. How to compare galaxy metallicity correctly

- Review URL: https://youtu.be/jVyK-y_KQ14
- Video ID: `jVyK-y_KQ14`
- Privacy: `unlisted`
- Processing: `succeeded`
- Embeddable: `true`
- Manual English captions: `serving`
- Master SHA-256: `73530c60c8352377a6b817f75e8dda7a4a5f6f1af98948cf596790029d8657d0`
- SRT SHA-256: `560770ea2590d3047448f79ad7b8b22773508e0a85b1f47b422c5f0f20a49ec8`

### 5. Calibration is not validation — testing TNG

- Review URL: https://youtu.be/gDIVbF8ZUFg
- Video ID: `gDIVbF8ZUFg`
- Privacy: `unlisted`
- Processing: `succeeded`
- Embeddable: `true`
- Manual English captions: `serving`
- Master SHA-256: `75104afb617d102a55fc7187992cd39d993c85e4417701ed188e7ae66b5f768f`
- SRT SHA-256: `9cf5eed04eb452ddfb481043aa09b00cce877b3db871dbe026ef676c18e47542`

## QA evidence

All five pass:

- 74.0 seconds; 1280×720; 30 fps; 2,220 frames
- H.264 High / yuv420p video and AAC stereo 48 kHz audio
- female `en-US-EmmaNeural` narration
- exact narration-to-SRT equivalence
- full audio/video decode
- approximately −16 LUFS integrated loudness
- no black segments
- only intended opening/outro and scene-boundary silence
- actual white manuscript page visible
- complete burned narration; no clipping or truncation
- Hwao-approved numbers and status boundaries
- approved Flow portrait only during silent opening/outro
- independent ASR recovered substantive facts and statuses
- compact `z≈5–6` speech was corrected to explicit `redshift five-to-six` and re-verified

Deterministic QA: `qa/deterministic_qa.json`
ASR QA: `qa/asr_base_en.json`
Visual boards: `qa/*_VISUAL_REVIEW_BOARD.png`

## Independent server verification

For every ID:

- authenticated exact-ID owner API matched exact title and description;
- privacy remained `unlisted`;
- processing was `succeeded`;
- embed permission was enabled;
- made-for-kids declaration was false;
- exactly one manual English caption track was `serving`;
- the local checkpoint owned the same ID;
- unauthenticated oEmbed resolved the intended title and NebulaMind author;
- signed-out extraction reported the intended title, description, and `Visibility: Unlisted`.

## Explicit non-actions

- No video was made public.
- No Nebula frontend source was changed.
- No Git commit, push, merge, or history action occurred.
- No frontend build, restart, deploy, or live embed occurred.
- No database, SQL, cockpit, cleanup, or watcher action occurred.

## Remaining explicit gates

1. Change these exact five IDs from unlisted to public.
2. Add these exact five IDs to the existing Flagship/Frontier manuscript cards and run focused tests.
3. Commit/push the reviewed frontend patch.
4. Build/restart/deploy and verify the live Nebula Paper stage.
