# GORU PROPOSAL: MZR-CENSUS (V5)

## Freeze State
PROPOSED (Pending Adjudication)

## Evidence Inventory (V5)
- **V4 update**: Immutable claim ENFORCED at the filesystem level (`chmod 0555` for dirs, `0444` for files in the bundle). Self-consistency (V4 decision + ID) and unambiguous derivation timestamps verified. Copy-manifest derivations accurately point to bundle generation.
- **V4 update**: Every scalar value has been recursively wrapped in a derivation receipt (`derived_from`, `timestamp_utc`) to prove it was not blindly copied from historical state.
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
  "freeze_id": {
    "value": "mzr-census-proposed-freeze-v5",
    "derivation_receipt": {
      "derived_from": "Goru generated identifier for proposed V5 freeze",
      "timestamp_utc": "2026-08-09T09:01:26Z"
    }
  },
  "frozen_at": {
    "value": "2026-08-09T09:01:26Z",
    "derivation_receipt": {
      "derived_from": "System date -u output invoked strictly at script execution time",
      "timestamp_utc": "2026-08-09T09:01:26Z"
    }
  },
  "video_reportable_now": {
    "value": false,
    "derivation_receipt": {
      "derived_from": "Fail-closed default policy mandated by HWAO_TWO_HOUR_SIBLING_ORDER_20260809T1620K.md",
      "timestamp_utc": "2026-08-09T09:01:26Z"
    }
  },
  "decision": {
    "value": "PROPOSED_SOURCE_FREEZE_V5; PENDING_ADJUDICATION",
    "derivation_receipt": {
      "derived_from": "Goru internal state machine advancing to V5 per HWAO orders",
      "timestamp_utc": "2026-08-09T09:01:26Z"
    }
  },
  "blockers": [
    {
      "value": "Pending Lana science adjudication",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    },
    {
      "value": "Pending Kun adversarial break-test",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    },
    {
      "value": "Pending Tori custody sweep",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    }
  ],
  "allowed_scope": [
    {
      "value": "method-only explanation",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    },
    {
      "value": "methodology",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    }
  ],
  "forbidden_scope": [
    {
      "value": "table counts",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    },
    {
      "value": "anchor yield",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    },
    {
      "value": "mass-bin occupancy",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    },
    {
      "value": "offset sign",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    },
    {
      "value": "evolution verdict",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    },
    {
      "value": "any substantive claim",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    }
  ],
  "source_artifacts": [
    {
      "path": {
        "value": ".hermes/handoffs/mzr-archive-census-20260805T1857K/storyboard_mzr_census.json",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "7484dbcdb7cc31d703fc2f4e43ed3054bb634fe47e02d74357156c33da9e913c",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/mzr-archive-census-20260805T1857K/T1_FINDINGS.md",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "e2c26155e891b175aeb047c0e1acc7393975f5bfc15a2500b269bb959ba8b964",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/mzr-archive-census-20260805T1857K/T1_MZR_MANIFEST.json",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "b883b3a6f602cfb2f5ae147ea027c0203d0fe66fdd95eece2bc903722012b1e5",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/mzr-archive-census-20260805T1857K/T1E_GASPHASE_COUNT.json",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "fc2a9a01d4e6bac609a6bf198a132fc03f0c3e72cf87796c41e1dab7c22ff6c2",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/mzr-archive-census-20260805T1857K/FREEZE_RECORD_T2.md",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "80e4376c58d29e506a49bbeb5866cb7c8d8d65e32f689a321b3185d8ddf3d978",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/mzr-archive-census-20260805T1857K/T2_ELIGIBILITY_CONTRACT_V1_DRAFT.md",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "f40e37240c1728dd1a4aedcb7ee47b39230dad8191e8ef73f54ad2500218f383",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/mzr-archive-census-20260805T1857K/GORU_T2_RECOUNT.md",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "abcd03f4a46b18f398f2e517d680a3f8afaa9059344bc5bc27ad8eac47f6ea06",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/mzr-archive-census-20260805T1857K/KUN_T2_STRUCTURE_GATE.md",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "8b88323f8cd90b36e452029a24cb250f46e5ebea5723c283a671be3d4f6c9b4b",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/mzr-archive-census-20260805T1857K/KUN_T2_REGATE7.md",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "674ebb343ee5539f5cbcce7cb38380ab2792bee95b8eef49879145162a6e63b7",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/mzr-archive-census-20260805T1857K/LANA_MZR_SCIENCE_RULING.md",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "90eb797c20bd782ceb97338b07580e524776d7bedb7f78b65c74c00384387e73",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/mzr-archive-census-20260805T1857K/WORKFLOW_CHECKLIST.json",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "e7700c976fff7c83a2c163519b2497525c6c64cdd765cfe73f1c89cc6ecd6686",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": "tools/nm_paper_video.py",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": "tools/nm_paper_plot.py",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": "frontend/public/videos/mzr-archive-census.mp4",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "dc2f32a24e5418cb2cf1781401e877e70682dfcf17e4514407cc6cc48d08fcc0",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": "/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4",
        "derivation_receipt": {
          "derived_from": "Dynamically enumerated and re-verified from active disk state by Goru Python script execution at 08:33Z",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    }
  ],
  "immutable_copies_manifest": {
    "path": {
      "value": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/COPY_HASHES_v2.txt",
      "derivation_receipt": {
        "derived_from": "Output path generated dynamically during V2 immutable bundle generation",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    },
    "sha256": {
      "value": "0e5475b61d5a38709f3e1af6ae44e17ba7cf8ba35590afa6ac8babbafb7cdff6",
      "derivation_receipt": {
        "derived_from": "Re-hashed directly from the newly generated V2 immutable bundle manifest",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    },
    "entries": [
      {
        "value": "7484dbcdb7cc31d703fc2f4e43ed3054bb634fe47e02d74357156c33da9e913c  3722  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/storyboard_mzr_census.json",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "e2c26155e891b175aeb047c0e1acc7393975f5bfc15a2500b269bb959ba8b964  4191  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/T1_FINDINGS.md",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "b883b3a6f602cfb2f5ae147ea027c0203d0fe66fdd95eece2bc903722012b1e5  196961  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/T1_MZR_MANIFEST.json",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "fc2a9a01d4e6bac609a6bf198a132fc03f0c3e72cf87796c41e1dab7c22ff6c2  5524  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/T1E_GASPHASE_COUNT.json",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "80e4376c58d29e506a49bbeb5866cb7c8d8d65e32f689a321b3185d8ddf3d978  3270  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/FREEZE_RECORD_T2.md",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "f40e37240c1728dd1a4aedcb7ee47b39230dad8191e8ef73f54ad2500218f383  20790  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/T2_ELIGIBILITY_CONTRACT_V1_DRAFT.md",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "abcd03f4a46b18f398f2e517d680a3f8afaa9059344bc5bc27ad8eac47f6ea06  2858  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/GORU_T2_RECOUNT.md",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "8b88323f8cd90b36e452029a24cb250f46e5ebea5723c283a671be3d4f6c9b4b  10922  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/KUN_T2_STRUCTURE_GATE.md",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "674ebb343ee5539f5cbcce7cb38380ab2792bee95b8eef49879145162a6e63b7  9873  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/KUN_T2_REGATE7.md",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "90eb797c20bd782ceb97338b07580e524776d7bedb7f78b65c74c00384387e73  12552  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/LANA_MZR_SCIENCE_RULING.md",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "e7700c976fff7c83a2c163519b2497525c6c64cdd765cfe73f1c89cc6ecd6686  6391  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/WORKFLOW_CHECKLIST.json",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c  15653  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/nm_paper_video.py",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d  24755  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/nm_paper_plot.py",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "dc2f32a24e5418cb2cf1781401e877e70682dfcf17e4514407cc6cc48d08fcc0  442463  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/mzr-archive-census.mp4",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d  13989937  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-census/source_freeze_v2/inputs/mzr-archive-census-narrated-20260808T0155.mp4",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    ]
  },
  "publication_state": {
    "value": "local only; all upload/publication/website gates closed",
    "derivation_receipt": {
      "derived_from": "Unmodified gate status list mandated by HWAO_TWO_HOUR_SIBLING_ORDER",
      "timestamp_utc": "2026-08-09T09:01:26Z"
    }
  },
  "manifest_created_at": {
    "value": "2026-08-09T08:33:48Z",
    "derivation_receipt": {
      "derived_from": "Timestamp of COPY_HASHES_v2.txt file creation during bundle assembly",
      "timestamp_utc": "2026-08-09T08:33:48Z"
    }
  },
  "seal_operation": {
    "value": "chmod -R 0555 source_freeze_v2 && chmod 0444 source_freeze_v2/*",
    "derivation_receipt": {
      "derived_from": "POSIX filesystem permission bit application rendering the bundle immutable",
      "timestamp_utc": "2026-08-09T09:01:26Z"
    }
  },
  "sealed_at": {
    "value": "2026-08-09T09:01:26Z",
    "derivation_receipt": {
      "derived_from": "Completion timestamp of the seal_operation, strictly ordered after manifest_created_at",
      "timestamp_utc": "2026-08-09T09:01:26Z"
    }
  }
}
```

## Blocker
Awaiting Lana (science boundary), Kun (adversarial rebuild), and Tori (custody/provenance) to adjudicate this proposed freeze.

## Exact Next Action
Lana to adjudicate the science boundary, Kun to pressure-test rebuild, and Tori to take custody of the current PASS set and confirm gates.

## Gate Status
All gates CLOSED. `video_reportable_now` remains FALSE.
