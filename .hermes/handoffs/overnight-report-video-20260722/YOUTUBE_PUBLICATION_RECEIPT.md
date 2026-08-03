# Overnight-report video — YouTube publication receipt

Marker: `TORI_OVERNIGHT_REPORT_VIDEO_V1_YOUTUBE_PUBLICATION_COMPLETE_20260722`

## Authorization

Duho explicitly directed: “publish the overnight report video.”

This authorized upload and public visibility for the exact QA-approved overnight-report V1 master. It did not authorize a website embed, deployment, deletion, replacement, Git action, database write, process restart, or publication of any other video.

## Exact source

- Video: `render/NEBULAMIND_OVERNIGHT_REPORT_V1_FEMALE_VOICE_EXACT_LIPSYNC.mp4`
- Video SHA-256: `d54764f39ca8ebd7b798fb3cf5c7bf5331b289efd5f0ba7e0b9b05375c7a01d9`
- Captions: `render/NEBULAMIND_OVERNIGHT_REPORT_V1_FEMALE_VOICE_EXACT_LIPSYNC.srt`
- Caption SHA-256: `e768aff4521565107a3c27b97388ee55ab35788a211fab71250e3bffa8a3d71d`
- Source marker: `GE_AUTOPILOT_OVERNIGHT_20260719_CORPUS_GATES_DONE`
- QA marker: `NEBULAMIND_OVERNIGHT_REPORT_V1_QA_COMPLETE`

Both source hashes matched the local delivery manifest immediately before upload.

## Duplicate preflight

The owned NebulaMind channel uploads playlist was inventoried before the write:

- Channel ID: `UCUHBNGk8ozEnisQRuchoS4Q`
- Recent uploads scanned: 49
- Exact-title matches: 0
- Other titles containing “overnight report”: 0

No duplicate or replacement upload was found.

## Published result

- Video ID: `JQfn3eUxRQg`
- Public URL: https://youtu.be/JQfn3eUxRQg
- Title: `NebulaMind Overnight Report — 120,676 Papers, 57 Topics, 3 Quality Gates`
- Channel: `NebulaMind`
- Category: Science & Technology
- Visibility: `public`
- Processing: `succeeded`
- Embeddable: `true`
- Made for kids: `false`
- Published UTC: `2026-07-22T09:38:57Z`
- Published KST: `2026-07-22T18:38:57+09:00`
- Published Pacific: `2026-07-22T02:38:57-07:00`

## Caption result

- Caption ID: `AUieDaYPhoTBDhMNS-J5q-sY_jiMDnVjezIzxpCDwlWBmjc7T5nzdE9hmfXIFqakdoN7ss8Id4xDw-6-eNgqhfkPvgp8XbE`
- Language: `en`
- Name: `English (manual overnight report V1)`
- Track kind: `standard`
- Status: `serving`

The exact QA-approved SRT was attached while the upload was unlisted and verified serving before public visibility.

## Verification

Authenticated owned-video API read-back:

- exact title: PASS
- exact description: PASS
- privacy public: PASS
- processing succeeded: PASS
- embeddable: PASS
- not made for kids: PASS
- manual English caption serving: PASS

Unauthenticated public checks:

- YouTube watch page reports `Visibility: Public`: PASS
- Watch page title and channel match: PASS
- YouTube oEmbed returned HTTP 200: PASS
- oEmbed title, author `NebulaMind`, and video type match: PASS

There was one brief YouTube consistency delay: the first read immediately after the visibility update still returned the prior unlisted state. No second upload was made. The next owned-video read reported public, and the idempotent verifier then confirmed public state and recorded it in the checkpoint.

## Preserved boundaries

- Original local QA and delivery manifests were not rewritten; they remain historical evidence of the pre-publication state.
- No prior video was deleted, unlisted, replaced, or otherwise changed.
- No website/Lab embed or production manifest changed.
- No deployment or restart occurred.
- No Git action occurred.
- No database write occurred.

Publication checkpoint:

`render/youtube_publication_checkpoint.json`

TORI_OVERNIGHT_REPORT_VIDEO_V1_YOUTUBE_PUBLICATION_COMPLETE_20260722
