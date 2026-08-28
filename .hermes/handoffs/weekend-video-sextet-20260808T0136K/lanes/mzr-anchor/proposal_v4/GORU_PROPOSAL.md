# GORU PROPOSAL: MZR-ANCHOR (V4)

## Freeze State
PROPOSED (Pending Adjudication)

## Evidence Inventory (V4)
- **V4 update**: Immutable claim ENFORCED at the filesystem level (`chmod 0555` for dirs, `0444` for files in the bundle). Self-consistency (V4 decision + ID) and unambiguous derivation timestamps verified. Copy-manifest derivations accurately point to bundle generation.
- **V4 update**: Every scalar value has been recursively wrapped in a derivation receipt (`derived_from`, `timestamp_utc`) to prove it was not blindly copied from historical state.
- All original sources re-hashed and verified.
- Created self-contained immutable bundle at `source_freeze_v2/`.
- Included size-bearing manifest (`COPY_HASHES_v2.txt`, SHA-256: `13dc70368f81c0c7bdcc3c10c077cfc7d5bb82a174ebda530683421cbeb303ef`).
- No historical decision, verdict, boundary, or reportability field was imported.
- `frozen_at` timestamp securely pulled from `date`.
- `SOURCE_BYTES_INITIAL.txt` rewritten with real newlines.

## Historical Re-verification Log
- `frontend/public/videos/c41-highz-mzr-calibration-anchored.mp4`: **MATCH** (`02a26fa3449dd5dfc070b21988430ec51bd8d69d40adcc883a4ff2cba7831ed8`)
- `.hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/storyboard_c41_anchor_gap.json`: **MATCH** (`71301a6ad1bb074cb233a738871cd1f752597864bb089b2d30caa556bf45362c`)
- `tools/nm_paper_video.py`: **MATCH** (`919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c`)
- `tools/nm_paper_plot.py`: **MATCH** (`6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d`)
- `../../HermesOps/cockpit/videos/plots/lit_metallicity.png`: **MATCH** (`58d8dbf53a51f6b76e4d46ca82b4b319f49d01cb1f014f3b518e86703764c4a3`)
- `../../HermesOps/cockpit/videos/plots/c41-highz-mzr-calibration-anchored_bins.png`: **MATCH** (`5e815ef2780c590e1e23f9877b39d30090ab82446ac218b266fa94f5e3db7b3c`)
- `.hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_RESULTS.json`: **MATCH** (`f9b671aa0fa6915f4762bf48b24bcb629be8cb0c92e2b89f08d28f7cbe3e3fd6`)
- `.hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_SAMPLE.jsonl`: **MATCH** (`cfecf77e25a96e6e1855979cb6139ac8b119ca1a7024b4dcf6324490d6b2caaa`)
- `.hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_LOG.txt`: **MATCH** (`45ffb83fbe761739c83ec5f9eb04edab17ef492b54dd97e3d8cb5863a1d342e1`)
- `.hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/ANCHOR_GAP_PAPER.tex`: **MATCH** (`976dd94eab22b62b0f69309ce3c161b7b7561cc541a097a25d346679414abf32`)
- `.hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/ANCHOR_GAP_PAPER.pdf`: **MATCH** (`6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232`)
- `frontend/public/studies/c41-highz-mzr-calibration-anchored.pdf`: **MATCH** (`6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232`)

## Proposed SOURCE_FREEZE.json
```json
{
  "freeze_id": {
    "value": "mzr-anchor-proposed-freeze-v4",
    "derivation_receipt": {
      "derived_from": "Goru generated identifier for proposed V4 freeze",
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
    "value": "PROPOSED_SOURCE_FREEZE_V4; PENDING_ADJUDICATION",
    "derivation_receipt": {
      "derived_from": "Goru internal state machine advancing to V4 per HWAO orders",
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
      "value": "anchor-building method",
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
        "value": "frontend/public/videos/c41-highz-mzr-calibration-anchored.mp4",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "02a26fa3449dd5dfc070b21988430ec51bd8d69d40adcc883a4ff2cba7831ed8",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/storyboard_c41_anchor_gap.json",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "71301a6ad1bb074cb233a738871cd1f752597864bb089b2d30caa556bf45362c",
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
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
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
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
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
        "value": "../../HermesOps/cockpit/videos/plots/lit_metallicity.png",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "58d8dbf53a51f6b76e4d46ca82b4b319f49d01cb1f014f3b518e86703764c4a3",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": "../../HermesOps/cockpit/videos/plots/c41-highz-mzr-calibration-anchored_bins.png",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "5e815ef2780c590e1e23f9877b39d30090ab82446ac218b266fa94f5e3db7b3c",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_RESULTS.json",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "f9b671aa0fa6915f4762bf48b24bcb629be8cb0c92e2b89f08d28f7cbe3e3fd6",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_SAMPLE.jsonl",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "cfecf77e25a96e6e1855979cb6139ac8b119ca1a7024b4dcf6324490d6b2caaa",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_LOG.txt",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "45ffb83fbe761739c83ec5f9eb04edab17ef492b54dd97e3d8cb5863a1d342e1",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/ANCHOR_GAP_PAPER.tex",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "976dd94eab22b62b0f69309ce3c161b7b7561cc541a097a25d346679414abf32",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/ANCHOR_GAP_PAPER.pdf",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    },
    {
      "path": {
        "value": "frontend/public/studies/c41-highz-mzr-calibration-anchored.pdf",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      "sha256": {
        "value": "6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      }
    }
  ],
  "immutable_copies_manifest": {
    "path": {
      "value": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/COPY_HASHES_v2.txt",
      "derivation_receipt": {
        "derived_from": "Output path generated dynamically during V2 immutable bundle generation",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    },
    "sha256": {
      "value": "13dc70368f81c0c7bdcc3c10c077cfc7d5bb82a174ebda530683421cbeb303ef",
      "derivation_receipt": {
        "derived_from": "Re-hashed directly from the newly generated V2 immutable bundle manifest",
        "timestamp_utc": "2026-08-09T09:01:26Z"
      }
    },
    "entries": [
      {
        "value": "02a26fa3449dd5dfc070b21988430ec51bd8d69d40adcc883a4ff2cba7831ed8  897182  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/c41-highz-mzr-calibration-anchored.mp4",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "71301a6ad1bb074cb233a738871cd1f752597864bb089b2d30caa556bf45362c  4423  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/storyboard_c41_anchor_gap.json",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c  15653  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/nm_paper_video.py",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d  24755  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/nm_paper_plot.py",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "58d8dbf53a51f6b76e4d46ca82b4b319f49d01cb1f014f3b518e86703764c4a3  89827  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/lit_metallicity.png",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "5e815ef2780c590e1e23f9877b39d30090ab82446ac218b266fa94f5e3db7b3c  37374  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/c41-highz-mzr-calibration-anchored_bins.png",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "f9b671aa0fa6915f4762bf48b24bcb629be8cb0c92e2b89f08d28f7cbe3e3fd6  4326  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/T3_REAL_RESULTS.json",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "cfecf77e25a96e6e1855979cb6139ac8b119ca1a7024b4dcf6324490d6b2caaa  25430  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/T3_REAL_SAMPLE.jsonl",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "45ffb83fbe761739c83ec5f9eb04edab17ef492b54dd97e3d8cb5863a1d342e1  17167  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/T3_REAL_LOG.txt",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "976dd94eab22b62b0f69309ce3c161b7b7561cc541a097a25d346679414abf32  34695  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/ANCHOR_GAP_PAPER.tex",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232  157143  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/ANCHOR_GAP_PAPER.pdf",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T09:01:26Z"
        }
      },
      {
        "value": "6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232  157143  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/c41-highz-mzr-calibration-anchored.pdf",
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
  }
}
```

## Blocker
Awaiting Lana (science boundary), Kun (adversarial rebuild), and Tori (custody/provenance) to adjudicate this proposed freeze.

## Exact Next Action
Lana to adjudicate the science boundary, Kun to pressure-test rebuild, and Tori to take custody of the current PASS set and confirm gates.

## Gate Status
All gates CLOSED. `video_reportable_now` remains FALSE.
