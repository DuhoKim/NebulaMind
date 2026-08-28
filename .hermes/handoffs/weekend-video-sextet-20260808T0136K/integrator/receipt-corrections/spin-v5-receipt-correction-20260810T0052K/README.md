# Spin V5 receipt correction — no re-encode

Status: `V5_PACKET_FROZEN_PENDING_BOUNDED_TORI_PACKET_RECHECK`

This directory corrects one self-description defect in the preserved V4 provenance packet. It does not contain a replacement MP4 and did not render, re-encode, or mutate the candidate.

## Exact unchanged candidate

- MP4: `integrator/canaries/spin-method-overhaul-canary-20260809T2340K/spin-method-overhaul-canary-20260809T2340K.mp4`
- SHA-256: `4d230cc0efca0eb68a8d027d614b6b7e500590cff06154f1514d4402a84d7078`
- Bytes: `25486290`
- Preserved V4 candidate tree: `210` files, tree SHA-256 `0d217a1efbf7b3aa666dddbf78b17bd01b201b306f81b712a9e929549f7ebafb`

## Corrected self-description

Both frame counts are true about different operations:

- `raw_frames_submitted_to_ffmpeg = 6727`
  - Producing operation: `ceil(224.21739583333334 seconds × 30 fps)`, followed by 6727 RGB24 writes to ffmpeg stdin.
  - Original operation interval is bounded by filesystem evidence: `2026-08-10T00:14:06.339051+09:00` through `2026-08-10T00:15:26.315130+09:00`.
  - V5 static re-derivation ran at `2026-08-10T00:52:06.119379+09:00`.

- `encoded_video_frames = 6726`
  - Producing operation: ffmpeg H.264/AAC mux with `-shortest` during the same original interval.
  - `ffprobe -count_frames` ran `00:52:06.132413`–`00:52:13.419553` KST and returned both `nb_frames=6726` and `nb_read_frames=6726`.
  - An independent full H.264 decode ran `00:52:13.419605`–`00:52:15.182363` KST and returned 6726 decoded frames.

The original V4 `build_receipt.json` remains immutable at SHA-256 `92f96059701c2609678bdd2ba8cc4e6cfdf9db3440ad4ae4c270bedcbfa47a22`. V5 does not silently replace 6727 with 6726; it qualifies both scalars.

## Packet files

- `FRAME_COUNT_DERIVATION_V5.json` — operation- and time-qualified evidence
- `BUILD_RECEIPT_V5.json` — corrected versioned self-description
- `TORI_PACKET_RECHECK_REQUEST_V5.json` — bounded packet-only recheck request
- `POST_ENCODE_FREEZE_V5.json` — V5 freeze binding the unchanged MP4 and preserved V4 tree
- `PACKET_MANIFEST_V5.json` — packet hashes and tree digest

Tori's existing exact-hash findings remain presentation PASS, method-only claim-boundary PASS, and media-integrity PASS. Only the corrected provenance packet is pending recheck. No acceptance is claimed; Duho's watch/listen verdict remains final.
