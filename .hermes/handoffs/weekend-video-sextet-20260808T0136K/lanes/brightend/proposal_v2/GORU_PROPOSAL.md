# GORU PROPOSAL: BRIGHTEND (V2)

## Freeze State
PROPOSED (Pending Adjudication)

## Evidence Inventory (V2)
- All original sources re-hashed and verified.
- Created self-contained immutable bundle at `source_freeze_v2/`.
- Included size-bearing manifest (`COPY_HASHES_v2.txt`, SHA-256: `977b1b11c2cf7990df097f8ef720bfc9c1ae2b34cff70617ce5aa082aacdf0c6`).
- No historical decision, verdict, boundary, or reportability field was imported.
- `frozen_at` timestamp securely pulled from `date`.


## Historical Re-verification Log
- `frontend/public/videos/c41-brightend-uvlf-archival-gap.mp4`: **MATCH** (`1d84b8755e0baf726c86625baac6335fb9ca91f3356786b5b363976aa26c76d2`)
- `frontend/public/studies/c41-brightend-uvlf-archival-gap.pdf`: **MATCH** (`7b4e31a41815c755ad9fbad80c4a3714817e82524c8cf5776924f16208452aba`)
- `.hermes/handoffs/c41-trackb-shape1-uvlf-20260804/storyboard_c41_gap.json`: **MATCH** (`f29b8cb4b5790773c516f264d8c449125645c3027c8b6bcb24b6909bc1524482`)
- `tools/nm_paper_video.py`: **MATCH** (`919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c`)
- `.hermes/handoffs/c41-trackb-shape1-uvlf-20260804/T1_CATALOG_MANIFEST.json`: **MATCH** (`50a7a5e81330ba2c251cb84b5e1bb0740a11aa5242e57ba47c96192c6d94b432`)
- `.hermes/handoffs/c41-trackb-shape1-uvlf-20260804/T3_CENSUS_RESULTS.json`: **MATCH** (`4b21d432524a55bf5746fb3685e89360eaa33f143f68c042975f7259dd645ed7`)
- `.hermes/handoffs/c41-trackb-shape1-uvlf-20260804/T3_CENSUS_SAMPLE.jsonl`: **MATCH** (`1cdb3de8738ecf1b80328c147a0dd25a159b147c1b76a1e7dd6473a16eddf5c5`)
- `/Users/duhokim/HermesOps/cockpit/videos/plots/lit_uvlf_alpha.png`: **MATCH** (`016e7df8149103f6db60cea98cdc03ae48951443c5358dbefcfa18d6155827f5`)

## Proposed SOURCE_FREEZE.json
```json
{
  "freeze_id": "brightend-proposed-freeze-v2",
  "frozen_at": "2026-08-09T08:33:48Z",
  "video_reportable_now": false,
  "decision": "PROPOSED_SOURCE_FREEZE_V2; PENDING_ADJUDICATION",
  "blockers": [
    "Pending Lana science adjudication",
    "Pending Kun adversarial break-test",
    "Pending Tori custody sweep"
  ],
  "allowed_scope": [
    "method-only explanation",
    "methodology"
  ],
  "forbidden_scope": [
    "table counts",
    "anchor yield",
    "mass-bin occupancy",
    "offset sign",
    "evolution verdict",
    "any substantive claim"
  ],
  "source_artifacts": [
    {
      "path": "frontend/public/videos/c41-brightend-uvlf-archival-gap.mp4",
      "sha256": "1d84b8755e0baf726c86625baac6335fb9ca91f3356786b5b363976aa26c76d2"
    },
    {
      "path": "frontend/public/studies/c41-brightend-uvlf-archival-gap.pdf",
      "sha256": "7b4e31a41815c755ad9fbad80c4a3714817e82524c8cf5776924f16208452aba"
    },
    {
      "path": ".hermes/handoffs/c41-trackb-shape1-uvlf-20260804/storyboard_c41_gap.json",
      "sha256": "f29b8cb4b5790773c516f264d8c449125645c3027c8b6bcb24b6909bc1524482"
    },
    {
      "path": "tools/nm_paper_video.py",
      "sha256": "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c"
    },
    {
      "path": ".hermes/handoffs/c41-trackb-shape1-uvlf-20260804/T1_CATALOG_MANIFEST.json",
      "sha256": "50a7a5e81330ba2c251cb84b5e1bb0740a11aa5242e57ba47c96192c6d94b432"
    },
    {
      "path": ".hermes/handoffs/c41-trackb-shape1-uvlf-20260804/T3_CENSUS_RESULTS.json",
      "sha256": "4b21d432524a55bf5746fb3685e89360eaa33f143f68c042975f7259dd645ed7"
    },
    {
      "path": ".hermes/handoffs/c41-trackb-shape1-uvlf-20260804/T3_CENSUS_SAMPLE.jsonl",
      "sha256": "1cdb3de8738ecf1b80328c147a0dd25a159b147c1b76a1e7dd6473a16eddf5c5"
    },
    {
      "path": "/Users/duhokim/HermesOps/cockpit/videos/plots/lit_uvlf_alpha.png",
      "sha256": "016e7df8149103f6db60cea98cdc03ae48951443c5358dbefcfa18d6155827f5"
    }
  ],
  "immutable_copies_manifest": {
    "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/brightend/source_freeze_v2/COPY_HASHES_v2.txt",
    "sha256": "977b1b11c2cf7990df097f8ef720bfc9c1ae2b34cff70617ce5aa082aacdf0c6",
    "entries": [
      "1d84b8755e0baf726c86625baac6335fb9ca91f3356786b5b363976aa26c76d2  736251  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/brightend/source_freeze_v2/inputs/c41-brightend-uvlf-archival-gap.mp4",
      "7b4e31a41815c755ad9fbad80c4a3714817e82524c8cf5776924f16208452aba  173975  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/brightend/source_freeze_v2/inputs/c41-brightend-uvlf-archival-gap.pdf",
      "f29b8cb4b5790773c516f264d8c449125645c3027c8b6bcb24b6909bc1524482  4247  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/brightend/source_freeze_v2/inputs/storyboard_c41_gap.json",
      "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c  15653  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/brightend/source_freeze_v2/inputs/nm_paper_video.py",
      "50a7a5e81330ba2c251cb84b5e1bb0740a11aa5242e57ba47c96192c6d94b432  307750  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/brightend/source_freeze_v2/inputs/T1_CATALOG_MANIFEST.json",
      "4b21d432524a55bf5746fb3685e89360eaa33f143f68c042975f7259dd645ed7  83078  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/brightend/source_freeze_v2/inputs/T3_CENSUS_RESULTS.json",
      "1cdb3de8738ecf1b80328c147a0dd25a159b147c1b76a1e7dd6473a16eddf5c5  414988  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/brightend/source_freeze_v2/inputs/T3_CENSUS_SAMPLE.jsonl",
      "016e7df8149103f6db60cea98cdc03ae48951443c5358dbefcfa18d6155827f5  51358  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/brightend/source_freeze_v2/inputs/lit_uvlf_alpha.png"
    ]
  },
  "publication_state": "local only; all upload/publication/website gates closed"
}
```

## Blocker
Awaiting Lana (science boundary), Kun (adversarial rebuild), and Tori (custody/provenance) to adjudicate this proposed freeze.

## Exact Next Action
Lana to adjudicate the science boundary, Kun to pressure-test rebuild, and Tori to take custody of the current PASS set and confirm gates.

## Gate Status
All gates CLOSED. `video_reportable_now` remains FALSE.
