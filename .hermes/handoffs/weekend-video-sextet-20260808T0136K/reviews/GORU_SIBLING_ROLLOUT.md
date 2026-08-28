# Goru sibling-rollout mechanical and numeric-source review

## Verdict

**PASS — 4/4 sibling method-only canaries pass the requested independent mechanical and numeric-source gate.**

**Exact failures: none.**

This verdict is limited to the bytes and checks named below. It does **not** authorize integration, upload, publication, a public/shared MP4, `frontend/public`, `paperVideos.ts`, cockpit mutation, database work, deployment, or Git action.

## Authority and scope

- Authority: `HWAO_SIBLING_ROLLOUT_ORDER.md`
- Independently recomputed authority SHA-256: `220b8b60406c9662f2b73e679cbb6205a98beb9176c14d2f987d5aa0967623f5`
- Every candidate-local copy of that authority matched this digest.
- Required per-lane inputs read: `spec.json`, `numeric_guard.json`, `audio/timeline.json`, `build_receipt.json`, `encoded_qa.json`, `source_manifest.json`, `RECEIPT.json`, `POST_ENCODE_FREEZE.json`, and `PREDECESSOR.json`.
- Independent replay included SHA-256 recomputation; source-manifest census and row verification; `ffprobe`; full H.264/AAC decode; timeline section reconstruction; exact 160×90/2-fps motion replay; encoded-state and peak-frame census; subtitle-line census; visible-digit projection and source lookup; predecessor-byte verification; recursive `SOURCE_FREEZE.json` absence; and public-video-root name/hash absence.
- The existing read-only rollout auditor also returned `PASS`; the verdict below is based on the separate replay, not on that result alone.

## Hash-bound lane verdicts

| lane | verdict | video SHA-256 | spec SHA-256 | timeline SHA-256 | narration-master SHA-256 | encoded-QA SHA-256 | receipt SHA-256 |
|---|---|---|---|---|---|---|---|
| `mzr-census` | **PASS** | `0496435a9488bd946f7453989e7b9c5f4a528a691e698acab6b1e0d56e064536` | `694b32bc1474aa5ad4caf8dc20fc0f0a5292944d173c2bd5b087b46a3fe66c65` | `af224f225fae4ac4b9821a2589f9ab47e51795ea19215d7d93caa4bd58feb820` | `3473b0e6da348119797bbf6dde4d7692d7b1009bc976a14e82dfd2e30d31bdee` | `1da92b8a1a3d45c498632a471d26a4bf37b9f4dcd04c7f13704c7b44c68f9204` | `513a6899713ed38723595434b922dba5568c4a62381ffbce2b76474676bedcc7` |
| `fesc` | **PASS** | `b900383142c0ddeadc32247282f511798d8c4a449cbf5c7b7aef0a56aff4c168` | `6bde037eddc03cccf0e9127da17274270ab764c5844ab1e1be0146535efe5747` | `b3e33fc40724f5816fd8cf8c0cd9afced82435898744ecd3b6919645db4711de` | `8f67aab2b85e0cb9f689d78950bd4aad9228874057876e4b249ad2a83982f974` | `6e2ebef25891858ea7d3480633db77db53f9156c94a7f861f0e4e8a721bce1b5` | `f1f2e6b34f41d9fc8200452ad46844dca7e7d90e472a2d91c3ac9eedc1d0a178` |
| `brightend` | **PASS** | `9a137c61011a3d9629c96ebbf365955295e11082cededa325ceb38f1ce268a2f` | `5bf302de774f067082d4dce1aeb182c18cf60b9412ea11e151057ff5e05e32ae` | `c2d4c804bfa5d68a9b54c33dd2a5bc06c762fc1d5fee79d98d4a52a094836b35` | `57348885d19636e74d1a4abff9c6dabc1d38452df3d2274f5d892b46667a2676` | `73d15d17a3fd1aebd4f4f3fb936c0ea66af2f672fad0c3b4787dd5507fb0cc14` | `07e8d0a5a3fe27ae77644076f62f44ccdd1e61c11eec792b8b1ada2f7cc51b6d` |
| `mzr-anchor` | **PASS** | `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970` | `c868b5bb7509edf1aa1d183c1dca6265c854081bd7f7f63fff72d9fcdd5f4910` | `4dca3a5e0753dde46bffcdc3ee3a39453db46411317b6d205a4119a928f7e450` | `b0900ec6c8146bedae3497d4c4141e81edfc66ad19478faea90b2211d0053df7` | `02efc107be0a903e955e6b530134d81cbe93cca106835f3b49f7fb832e41da38` | `4f9bcd93ab48c16db8809280e546eef47c31fb6fca627a300fdfda7bb1d2c23d` |

For every lane, the recomputed video/spec/timeline/audio hashes agree across the relevant timeline, build receipt, encoded QA, receipt, and post-encode freeze fields. Each post-encode freeze also authenticates the recomputed receipt digest.

## Per-lane mechanical results

### `mzr-census-method-overhaul-canary-20260809T0214K`

- Encoded QA: **27/27 true**, status `PASS`; independent full decode passed; H.264/AAC, 1920×1080, 30 fps.
- First four ordered states: `i01`, `i02`, `i03`, `i04`; all `section=motivation`, `visual=intro`; one encoded state frame exists for each.
- Independently reconstructed section peak: `peak = 47.598250 s`; next-longest `motivation = 29.7586875 s`.
- Five independently hashed peak samples are distinct. Motion replay matched the stored summary exactly: mean MAD `0.44622918220233654`, longest near-unchanged run `0.0 s`.
- Captions: 22/22 state entries covered; maximum **2 lines** in both the encoded-QA map and independent SRT cue census.
- Numeric-source guard: six visible digit occurrences, exactly six evidence rows: `178`, `21`, and `157` in each of `f01` and `f02`. Every occurrence resolves to current `sources/T1_FINDINGS.md`, and the cited lines contain the digit. No unguarded or surplus guarded digit exists.
- Source manifest: **10 listed = 10 actual**, all byte counts and SHA-256 rows match; every sentence grounding resolves to a manifest-listed local source.
- `SOURCE_FREEZE.json`: absent by recursive case-insensitive filename census.
- Predecessor preserved:
  - MP4 declared/actual SHA-256: `07f08990124748e2e074cf393e5d34e064ed655a85ea827356bc98b44d3cc274`
  - storyboard declared/actual SHA-256: `8ddd7951bd0d20673e6832cd66b6993e0c65a4ae54f2a4ec734af72db296c842`
- New candidate absent from `frontend/public/videos` by exact filename and full-file SHA-256 census.
- Gates are exactly false in both `RECEIPT.json` and `POST_ENCODE_FREEZE.json`: `upload`, `cockpit_or_video_root_copy`, `git`, `video_reportable_now`; spec/build reportability is also false.
- **Exact failures: none.**

### `fesc-method-overhaul-canary-20260809T0227K`

- Encoded QA: **27/27 true**, status `PASS`; independent full decode passed; H.264/AAC, 1920×1080, 30 fps.
- First four ordered states: `i01`, `i02`, `i03`, `i04`; all `section=motivation`, `visual=intro`; one encoded state frame exists for each.
- Independently reconstructed section peak: `peak = 48.981750 s`; next-longest `motivation = 33.0223125 s`.
- Five independently hashed peak samples are distinct. Motion replay matched the stored summary exactly: mean MAD `0.4875242761299435`, longest near-unchanged run `0.0 s`.
- Captions: 22/22 state entries covered; maximum **2 lines** in both the encoded-QA map and independent SRT cue census.
- Numeric-source guard: **0 visible digit occurrences**, **0 evidence rows**, status `PASS`; no unguarded digit exists in the renderer-consumed audience projection.
- Source manifest: **8 listed = 8 actual**, all byte counts and SHA-256 rows match; every sentence grounding resolves to a manifest-listed local source.
- `SOURCE_FREEZE.json`: absent by recursive case-insensitive filename census.
- Predecessor preserved:
  - MP4 declared/actual SHA-256: `840ced2b52c2007bc5387fc69b49527c548daca6f6d81b3f14bc9a43b7e9b5af`
  - storyboard declared/actual SHA-256: `e470ca87d630d797acd235b3f4927139971e655805ec36efac81282e5b0bac55`
- New candidate absent from `frontend/public/videos` by exact filename and full-file SHA-256 census.
- Gates are exactly false in both `RECEIPT.json` and `POST_ENCODE_FREEZE.json`: `upload`, `cockpit_or_video_root_copy`, `git`, `video_reportable_now`; spec/build reportability is also false.
- **Exact failures: none.**

### `brightend-method-overhaul-canary-20260809T0235K`

- Encoded QA: **27/27 true**, status `PASS`; independent full decode passed; H.264/AAC, 1920×1080, 30 fps.
- First four ordered states: `i01`, `i02`, `i03`, `i04`; all `section=motivation`, `visual=intro`; one encoded state frame exists for each.
- Independently reconstructed section peak: `peak = 44.812750 s`; next-longest `motivation = 31.4975625 s`.
- Five independently hashed peak samples are distinct. Motion replay matched the stored summary exactly: mean MAD `0.414502442002442`, longest near-unchanged run `0.0 s`.
- Captions: 22/22 state entries covered; maximum **2 lines** in both the encoded-QA map and independent SRT cue census.
- Numeric-source guard: **0 visible digit occurrences**, **0 evidence rows**, status `PASS`; no unguarded digit exists in the renderer-consumed audience projection.
- Source manifest: **10 listed = 10 actual**, all byte counts and SHA-256 rows match; every sentence grounding resolves to a manifest-listed local source.
- `SOURCE_FREEZE.json`: absent by recursive case-insensitive filename census.
- Predecessor preserved:
  - MP4 declared/actual SHA-256: `1d84b8755e0baf726c86625baac6335fb9ca91f3356786b5b363976aa26c76d2`
  - storyboard declared/actual SHA-256: `f29b8cb4b5790773c516f264d8c449125645c3027c8b6bcb24b6909bc1524482`
- New candidate absent from `frontend/public/videos` by exact filename and full-file SHA-256 census.
- Gates are exactly false in both `RECEIPT.json` and `POST_ENCODE_FREEZE.json`: `upload`, `cockpit_or_video_root_copy`, `git`, `video_reportable_now`; spec/build reportability is also false.
- **Exact failures: none.**

### `mzr-anchor-method-overhaul-canary-20260809T0245K`

- Encoded QA: **27/27 true**, status `PASS`; independent full decode passed; H.264/AAC, 1920×1080, 30 fps.
- First four ordered states: `i01`, `i02`, `i03`, `i04`; all `section=motivation`, `visual=intro`; one encoded state frame exists for each.
- Independently reconstructed section peak: `peak = 47.459667 s`; next-longest `motivation = 28.316750 s`.
- Five independently hashed peak samples are distinct. Motion replay matched the stored summary exactly: mean MAD `0.43963375190258747`, longest near-unchanged run `0.0 s`.
- Captions: 22/22 state entries covered; maximum **2 lines** in both the encoded-QA map and independent SRT cue census.
- Numeric-source guard: **0 visible digit occurrences**, **0 evidence rows**, status `PASS`; no unguarded digit exists in the renderer-consumed audience projection.
- Source manifest: **10 listed = 10 actual**, all byte counts and SHA-256 rows match; every sentence grounding resolves to a manifest-listed local source.
- `SOURCE_FREEZE.json`: absent by recursive case-insensitive filename census.
- Predecessor preserved:
  - MP4 declared/actual SHA-256: `02a26fa3449dd5dfc070b21988430ec51bd8d69d40adcc883a4ff2cba7831ed8`
  - storyboard declared/actual SHA-256: `71301a6ad1bb074cb233a738871cd1f752597864bb089b2d30caa556bf45362c`
- New candidate absent from `frontend/public/videos` by exact filename and full-file SHA-256 census.
- Gates are exactly false in both `RECEIPT.json` and `POST_ENCODE_FREEZE.json`: `upload`, `cockpit_or_video_root_copy`, `git`, `video_reportable_now`; spec/build reportability is also false.
- **Exact failures: none.**

## Cross-lane closure

- Exact encoded-check arithmetic: `27 + 27 + 27 + 27 = 108/108 true`.
- All four introductions begin with four motivation/intro states before technical content.
- `peak` is independently the longest section in all four lanes.
- All 88 sentence captions are covered and use at most two lines.
- Numeric projection: six guarded digit occurrences total, all in `mzr-census`; zero visible digit occurrences in the other three lanes.
- No candidate contains `SOURCE_FREEZE.json`.
- All four predecessor MP4 and storyboard hashes reproduce exactly.
- No new candidate filename or candidate SHA-256 appears under `frontend/public/videos`.
- All named release/reportability gates remain false.

**Final mechanical disposition: PASS. Exact failures: none.**
