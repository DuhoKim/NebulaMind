# GORU PROPOSAL: MZR-CENSUS (V2)

## Freeze State
PROPOSED (Pending Adjudication)

## Evidence Inventory (V2)
- All original sources re-hashed and verified.
- Created self-contained immutable bundle at `source_freeze_v2/`.
- Included size-bearing manifest (`COPY_HASHES_v2.txt`, SHA-256: `0e5475b61d5a38709f3e1af6ae44e17ba7cf8ba35590afa6ac8babbafb7cdff6`).
- No historical decision, verdict, boundary, or reportability field was imported.
- `frozen_at` timestamp securely pulled from `date`.


## Historical Re-verification Log
- `.hermes/handoffs/mzr-archive-census-20260805T1857K/storyboard_mzr_census.json`: **MATCH** (`7484dbcdb7cc31d703fc2f4e43ed3054bb634fe47e02d74357156c33da9e913c`)
- `.hermes/handoffs/mzr-archive-census-20260805T1857K/T1_FINDINGS.md`: **MATCH** (`e2c26155e891b175aeb047c0e1acc7393975f5bfc15a2500b269bb959ba8b964`)
- `.hermes/handoffs/mzr-archive-census-20260805T1857K/T1_MZR_MANIFEST.json`: **MATCH** (`b883b3a6f602cfb2f5ae147ea027c0203d0fe66fdd95eece2bc903722012b1e5`)
- `.hermes/handoffs/mzr-archive-census-20260805T1857K/T1E_GASPHASE_COUNT.json`: **MATCH** (`fc2a9a01d4e6bac609a6bf198a132fc03f0c3e72cf87796c41e1dab7c22ff6c2`)
- `.hermes/handoffs/mzr-archive-census-20260805T1857K/FREEZE_RECORD_T2.md`: **MATCH** (`80e4376c58d29e506a49bbeb5866cb7c8d8d65e32f689a321b3185d8ddf3d978`)
- `.hermes/handoffs/mzr-archive-census-20260805T1857K/T2_ELIGIBILITY_CONTRACT_V1_DRAFT.md`: **MATCH** (`f40e37240c1728dd1a4aedcb7ee47b39230dad8191e8ef73f54ad2500218f383`)
- `.hermes/handoffs/mzr-archive-census-20260805T1857K/GORU_T2_RECOUNT.md`: **MATCH** (`abcd03f4a46b18f398f2e517d680a3f8afaa9059344bc5bc27ad8eac47f6ea06`)
- `.hermes/handoffs/mzr-archive-census-20260805T1857K/KUN_T2_STRUCTURE_GATE.md`: **MATCH** (`8b88323f8cd90b36e452029a24cb250f46e5ebea5723c283a671be3d4f6c9b4b`)
- `.hermes/handoffs/mzr-archive-census-20260805T1857K/KUN_T2_REGATE7.md`: **MATCH** (`674ebb343ee5539f5cbcce7cb38380ab2792bee95b8eef49879145162a6e63b7`)
- `.hermes/handoffs/mzr-archive-census-20260805T1857K/LANA_MZR_SCIENCE_RULING.md`: **MATCH** (`90eb797c20bd782ceb97338b07580e524776d7bedb7f78b65c74c00384387e73`)
- `.hermes/handoffs/mzr-archive-census-20260805T1857K/WORKFLOW_CHECKLIST.json`: **MATCH** (`e7700c976fff7c83a2c163519b2497525c6c64cdd765cfe73f1c89cc6ecd6686`)
- `tools/nm_paper_video.py`: **MATCH** (`919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c`)
- `tools/nm_paper_plot.py`: **MATCH** (`6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d`)
- `frontend/public/videos/mzr-archive-census.mp4`: **MATCH** (`dc2f32a24e5418cb2cf1781401e877e70682dfcf17e4514407cc6cc48d08fcc0`)
- `/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4`: **MATCH** (`0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d`)

## Proposed SOURCE_FREEZE.json
```json
{
  "freeze_id": "mzr-census-proposed-freeze-v2",
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
      "path": ".hermes/handoffs/mzr-archive-census-20260805T1857K/storyboard_mzr_census.json",
      "sha256": "7484dbcdb7cc31d703fc2f4e43ed3054bb634fe47e02d74357156c33da9e913c"
    },
    {
      "path": ".hermes/handoffs/mzr-archive-census-20260805T1857K/T1_FINDINGS.md",
      "sha256": "e2c26155e891b175aeb047c0e1acc7393975f5bfc15a2500b269bb959ba8b964"
    },
    {
      "path": ".hermes/handoffs/mzr-archive-census-20260805T1857K/T1_MZR_MANIFEST.json",
      "sha256": "b883b3a6f602cfb2f5ae147ea027c0203d0fe66fdd95eece2bc903722012b1e5"
    },
    {
      "path": ".hermes/handoffs/mzr-archive-census-20260805T1857K/T1E_GASPHASE_COUNT.json",
      "sha256": "fc2a9a01d4e6bac609a6bf198a132fc03f0c3e72cf87796c41e1dab7c22ff6c2"
    },
    {
      "path": ".hermes/handoffs/mzr-archive-census-20260805T1857K/FREEZE_RECORD_T2.md",
      "sha256": "80e4376c58d29e506a49bbeb5866cb7c8d8d65e32f689a321b3185d8ddf3d978"
    },
    {
      "path": ".hermes/handoffs/mzr-archive-census-20260805T1857K/T2_ELIGIBILITY_CONTRACT_V1_DRAFT.md",
      "sha256": "f40e37240c1728dd1a4aedcb7ee47b39230dad8191e8ef73f54ad2500218f383"
    },
    {
      "path": ".hermes/handoffs/mzr-archive-census-20260805T1857K/GORU_T2_RECOUNT.md",
      "sha256": "abcd03f4a46b18f398f2e517d680a3f8afaa9059344bc5bc27ad8eac47f6ea06"
    },
    {
      "path": ".hermes/handoffs/mzr-archive-census-20260805T1857K/KUN_T2_STRUCTURE_GATE.md",
      "sha256": "8b88323f8cd90b36e452029a24cb250f46e5ebea5723c283a671be3d4f6c9b4b"
    },
    {
      "path": ".hermes/handoffs/mzr-archive-census-20260805T1857K/KUN_T2_REGATE7.md",
      "sha256": "674ebb343ee5539f5cbcce7cb38380ab2792bee95b8eef49879145162a6e63b7"
    },
    {
      "path": ".hermes/handoffs/mzr-archive-census-20260805T1857K/LANA_MZR_SCIENCE_RULING.md",
      "sha256": "90eb797c20bd782ceb97338b07580e524776d7bedb7f78b65c74c00384387e73"
    },
    {
      "path": ".hermes/handoffs/mzr-archive-census-20260805T1857K/WORKFLOW_CHECKLIST.json",
      "sha256": "e7700c976fff7c83a2c163519b2497525c6c64cdd765cfe73f1c89cc6ecd6686"
    },
    {
      "path": "tools/nm_paper_video.py",
      "sha256": "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c"
    },
    {
      "path": "tools/nm_paper_plot.py",
      "sha256": "6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d"
    },
    {
      "path": "frontend/public/videos/mzr-archive-census.mp4",
      "sha256": "dc2f32a24e5418cb2cf1781401e877e70682dfcf17e4514407cc6cc48d08fcc0"
    },
    {
      "path": "/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4",
      "sha256": "0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d"
    }
  ],
  "immutable_copies_manifest": {
    "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/COPY_HASHES_v2.txt",
    "sha256": "0e5475b61d5a38709f3e1af6ae44e17ba7cf8ba35590afa6ac8babbafb7cdff6",
    "entries": [
      "7484dbcdb7cc31d703fc2f4e43ed3054bb634fe47e02d74357156c33da9e913c  3722  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/storyboard_mzr_census.json",
      "e2c26155e891b175aeb047c0e1acc7393975f5bfc15a2500b269bb959ba8b964  4191  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/T1_FINDINGS.md",
      "b883b3a6f602cfb2f5ae147ea027c0203d0fe66fdd95eece2bc903722012b1e5  196961  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/T1_MZR_MANIFEST.json",
      "fc2a9a01d4e6bac609a6bf198a132fc03f0c3e72cf87796c41e1dab7c22ff6c2  5524  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/T1E_GASPHASE_COUNT.json",
      "80e4376c58d29e506a49bbeb5866cb7c8d8d65e32f689a321b3185d8ddf3d978  3270  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/FREEZE_RECORD_T2.md",
      "f40e37240c1728dd1a4aedcb7ee47b39230dad8191e8ef73f54ad2500218f383  20790  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/T2_ELIGIBILITY_CONTRACT_V1_DRAFT.md",
      "abcd03f4a46b18f398f2e517d680a3f8afaa9059344bc5bc27ad8eac47f6ea06  2858  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/GORU_T2_RECOUNT.md",
      "8b88323f8cd90b36e452029a24cb250f46e5ebea5723c283a671be3d4f6c9b4b  10922  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/KUN_T2_STRUCTURE_GATE.md",
      "674ebb343ee5539f5cbcce7cb38380ab2792bee95b8eef49879145162a6e63b7  9873  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/KUN_T2_REGATE7.md",
      "90eb797c20bd782ceb97338b07580e524776d7bedb7f78b65c74c00384387e73  12552  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/LANA_MZR_SCIENCE_RULING.md",
      "e7700c976fff7c83a2c163519b2497525c6c64cdd765cfe73f1c89cc6ecd6686  6391  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/WORKFLOW_CHECKLIST.json",
      "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c  15653  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/nm_paper_video.py",
      "6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d  24755  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/nm_paper_plot.py",
      "dc2f32a24e5418cb2cf1781401e877e70682dfcf17e4514407cc6cc48d08fcc0  442463  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/mzr-archive-census.mp4",
      "0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d  13989937  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/mzr-archive-census-narrated-20260808T0155.mp4"
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
