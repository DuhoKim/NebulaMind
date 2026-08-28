# Receipt — spin method conference-science overhaul

Timestamp: 2026-08-08T14:03:11+0900 KST
Seat: `yui-overhaul-integrator`
Artifact status: `PENDING_SEXTET_POST_ENCODED_REVIEW`

## Deliverable

`spin-method-overhaul-canary-20260808T1312K.mp4`

- SHA-256: `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`
- Bytes: 13,697,038
- Duration: 159.000 s
- H.264 video: 1920×1080, 30 fps, 4,770 decoded frames
- AAC narration: 48 kHz mono
- Music: none
- Full decode through EOF: PASS

This hash is frozen for Tori/Kun post-encoded review. No rewrite is permitted without reviewer HOLD; any replacement must be a new version.

## Corrected narrative lineage

- Authority: `sources/HWAO_NARRATIVE_CORRECTION.md`, SHA-256 `0743fd839a520213554a3e60d23de1e0f13e95ae4505cf518e233b0dbfcd036d`
- Script: `narration_script_v2.json`, SHA-256 `3f033dd02d00767c6bb4cc1baf8b7197a78847bad076411cbaed9aab732cd416`
- Sentence TTS receipt: `audio_v2/synthesis_receipt.json`, SHA-256 `403fa8629c108348c7beb448d7628d539cac6dfb41d5ebbd333f7395832bee8f`
- PCM-derived timeline: `audio_v2/timeline.json`, SHA-256 `5be1dca72a29b0469a8acd8ef55092c95905a18b628a7b454a66c535a2f16e4d`
- Master narration: `audio_v2/narration_master.wav`, SHA-256 `e3fffb1d275657aeed183d2d76b4c4656782c2e33462d7be9666bd8a76bc12d8`
- Renderer: `build.py`, SHA-256 `b949c25925686615235227d59cf9b0cbab67aa17d4f4b43816547089bc8847f0`
- Build receipt: `build_receipt.json`, SHA-256 `1a9de9a38a1b0e864837c7cdd6118e757bd8b0fc74db3490b598943ffccd1805`

Audio was freshly synthesized after the Hwao narrative correction. No rejected v1 sentence master was reused.

## Preserved rejected lineage

- Script: `narration_script.json`, SHA-256 `d935427228f3359f0fe90badeecf008902e6639772a0d6604cd019d9df2d4453`
- Master: `audio/narration_master.wav`, SHA-256 `ef28bc8f290a46e59b0a2875fed076711666f37024d06e2cd5c986712eb4cd04`
- Custody note: `REJECTED_NARRATION_V1.md`, SHA-256 `387409b751488a84030ffb2fe4b5412372bf67826512698f767fe3cbdec44d7b`

The v1 script/audio remain intact and explicitly rejected before rendering.

## Authority and integration custody

- Independent pre-review design: `INDEPENDENT_REPRESENTATION_DESIGN.md`, SHA-256 `2a8b3a801f16aee846f74ec9113b49fb1771d99e8e574b07e997454044702522`
- Review integration ledger: `INTEGRATION_LEDGER.md`, SHA-256 `fbf9f2149a47c69bc9701d4a6eb8c10349a1052ec26389c651c7d5ab5348e47c`
- Corrected plan: `plan_v2.md`, SHA-256 `791cccbdbe821e7afbd48bbdf2e7d122435dc3be3a89688c5fa608cdb6aec096`
- Frozen source manifest: `source_manifest_v2.json`, SHA-256 `905c8a2e48d2a4d3b5a44199b444f044e191217b3958e51181d6b99b887cac3b`
- Fresh source/copy replay: 16/16 entries match; no drift.

## QA custody

- Machine report: `encoded_qa.json`, SHA-256 `918cc049b95ea875b8f77741a585a0faae02cf97209e87a9f8fad8ffd89ff4f9`
- Encoded 29-frame sheet: `encoded-contact-sheet-v2.jpg`, SHA-256 `e674cf459b4b36da6cc8542a330fed45bdadcc2bb55f26349d31eaa90755116a`
- Self-QA: `QA.md`
- All 19 encoded machine checks: PASS
- Encoded visual audit: PASS
- Overall external review: pending Tori and Kun amendments

## Closed-gate receipt

No upload, publication, YouTube action, public/shared MP4 replacement, repo-tool edit, cockpit edit, DB/SQL action, deploy/restart, browser automation, billing/provider/config change, secret access, Git commit/push/merge, or prior-attempt deletion was performed.

Git inspection after the build showed HEAD `ebe9c7f587bfbdad30ea8cb62d42e51294e1599e` and an empty cached diff. The working tree was already heavily modified/untracked and was not normalized or written through Git.

## Next action

Wait for timestamped post-encoded amendments in `reviews/TORI_OVERHAUL.md` and `reviews/KUN_OVERHAUL.md`. If both accept this exact SHA-256, reconcile their findings and only then permit an overall PASS declaration. If either issues HOLD, preserve this frozen hash and build a new version rather than replacing it.
