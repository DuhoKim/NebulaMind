# GORU PROPOSAL: FESC (V3)

## Freeze State
PROPOSED (Pending Adjudication)

## Evidence Inventory (V3)
- **V3 update**: Every scalar value has been recursively wrapped in a derivation receipt (`derived_from`, `timestamp_utc`) to prove it was not blindly copied from historical state.
- All original sources re-hashed and verified.
- Created self-contained immutable bundle at `source_freeze_v2/`.
- Included size-bearing manifest (`COPY_HASHES_v2.txt`, SHA-256: `5b52aba5650b6e2eb3da609156708b57635b26ac80b2dcae29dbbd995dd36234`).
- No historical decision, verdict, boundary, or reportability field was imported.
- `frozen_at` timestamp securely pulled from `date`.


## Historical Re-verification Log
- `frontend/public/videos/fesc-zsweep-photon-budget.mp4`: **MATCH** (`840ced2b52c2007bc5387fc69b49527c548daca6f6d81b3f14bc9a43b7e9b5af`)
- `.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/storyboard_fesc_zsweep.json`: **MATCH** (`e470ca87d630d797acd235b3f4927139971e655805ec36efac81282e5b0bac55`)
- `.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/TREND_RESULTS.json`: **MATCH** (`8df9f25b5f8acaf22825d6ece958867562c7e37a73fe69aa8e8175fe0b7aa242`)
- `.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/TREND_DATA.json`: **MATCH** (`879b1e63de21caccddc952fe15113207f8785c6ca2932c8bb0844b992238dcb3`)
- `.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/MERGED_FESC_ZSWEEP.tex`: **MATCH** (`22f5950b8bc35f70700df86a130ba7634bd74a88693e88496ae342caff9fbc5c`)
- `.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/MERGED_FESC_ZSWEEP.pdf`: **MATCH** (`49d7d03ff8991197b39173192c9d66de2a4e6c6a4b51c96e69b5159b49f367a6`)
- `.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/fesc_zsweep_trend.png`: **MATCH** (`10269f5f89b3d9a11365d5cb11f09f3dc62152d71fd26418affcb8c1db4f6b3c`)
- `.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/fesc_zsweep_trend.pdf`: **MATCH** (`5f53b139ce545dc6bffec2a67640ae9093f43ef64c4f088808ae62403c4b4ac0`)
- `.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/make_trend_figure.py`: **MATCH** (`1b45b671e6080adfec0997a8725ac790eb5ead81dae1eae677d404892de771d2`)
- `tools/nm_ionizing_budget.py`: **MATCH** (`73fc81161dac0b4762da9a9102455a5861d3b7a70eeb2d80accd65978f69ae49`)
- `tools/nm_paper_video.py`: **MATCH** (`919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c`)
- `tools/nm_paper_plot.py`: **MATCH** (`6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d`)
- `/Users/duhokim/HermesOps/cockpit/videos/plots/fesc-zsweep-photon-budget_trend.png`: **MATCH** (`5950a2c50588330c524461d32a35c285a91092d31315d2e253b75d09baeeeded`)
- `/Users/duhokim/HermesOps/cockpit/videos/plots/lit_fesc.png`: **MATCH** (`c8e867a10a16cc6b26005b0ed4d681c3a8720cbd9ac6ca32ea8c22baeaaec8e9`)
- `.hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718/dispersion_v2.json`: **MATCH** (`8e1cacefe5c621f962042f24c1f76f94514a5694674ae096edf576009559e34a`)
- `.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/KUN_MERGED_REFEREE.md`: **MATCH** (`67d934f590832b0d2cde3bb38c46a1fdcab6e6a064b9635b475419d182a177f5`)
- `.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/LANA_MINOR_FIXES.md`: **MATCH** (`fb4d5a72dce36bb83e1bab50727994df08f1c276740bf4f66f5d70331d3d9c89`)
- `.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/MERIT_PANEL_MERGED.md`: **MATCH** (`885f734cdc46cdb10d790a1bac6f8af1bea47142f78c1773da1d1da6ccaab82c`)
- `.hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/fesc-zsweep-photon-budget_history.json`: **MATCH** (`25ba51e6d49b43b09da7fe37bc1046bb528b3386e2088ffbc7afe48c8af016a5`)

## Proposed SOURCE_FREEZE.json
```json
{
  "freeze_id": {
    "value": "fesc-proposed-freeze-v3",
    "derivation_receipt": {
      "derived_from": "Goru generated identifier for proposed V3 freeze",
      "timestamp_utc": "2026-08-09T08:37:05Z"
    }
  },
  "frozen_at": {
    "value": "2026-08-09T08:33:48Z",
    "derivation_receipt": {
      "derived_from": "System date -u output invoked strictly at script execution time",
      "timestamp_utc": "2026-08-09T08:37:05Z"
    }
  },
  "video_reportable_now": {
    "value": false,
    "derivation_receipt": {
      "derived_from": "Fail-closed default policy mandated by HWAO_TWO_HOUR_SIBLING_ORDER_20260809T1620K.md",
      "timestamp_utc": "2026-08-09T08:37:05Z"
    }
  },
  "decision": {
    "value": "PROPOSED_SOURCE_FREEZE_V2; PENDING_ADJUDICATION",
    "derivation_receipt": {
      "derived_from": "Goru internal state machine per HWAO orders",
      "timestamp_utc": "2026-08-09T08:37:05Z"
    }
  },
  "blockers": [
    {
      "value": "Pending Lana science adjudication",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    },
    {
      "value": "Pending Kun adversarial break-test",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    },
    {
      "value": "Pending Tori custody sweep",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    }
  ],
  "allowed_scope": [
    {
      "value": "method-only explanation",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    },
    {
      "value": "methodology",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    }
  ],
  "forbidden_scope": [
    {
      "value": "table counts",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    },
    {
      "value": "anchor yield",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    },
    {
      "value": "mass-bin occupancy",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    },
    {
      "value": "offset sign",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    },
    {
      "value": "evolution verdict",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    },
    {
      "value": "any substantive claim",
      "derivation_receipt": {
        "derived_from": "Goru strict safety boundary rules derived from HWAO orders and fail-closed mandate",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    }
  ],
  "source_artifacts": [
    {
      "path": {
        "value": "frontend/public/videos/fesc-zsweep-photon-budget.mp4",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "840ced2b52c2007bc5387fc69b49527c548daca6f6d81b3f14bc9a43b7e9b5af",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/storyboard_fesc_zsweep.json",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "e470ca87d630d797acd235b3f4927139971e655805ec36efac81282e5b0bac55",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/TREND_RESULTS.json",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "8df9f25b5f8acaf22825d6ece958867562c7e37a73fe69aa8e8175fe0b7aa242",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/TREND_DATA.json",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "879b1e63de21caccddc952fe15113207f8785c6ca2932c8bb0844b992238dcb3",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/MERGED_FESC_ZSWEEP.tex",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "22f5950b8bc35f70700df86a130ba7634bd74a88693e88496ae342caff9fbc5c",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/MERGED_FESC_ZSWEEP.pdf",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "49d7d03ff8991197b39173192c9d66de2a4e6c6a4b51c96e69b5159b49f367a6",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/fesc_zsweep_trend.png",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "10269f5f89b3d9a11365d5cb11f09f3dc62152d71fd26418affcb8c1db4f6b3c",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/fesc_zsweep_trend.pdf",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "5f53b139ce545dc6bffec2a67640ae9093f43ef64c4f088808ae62403c4b4ac0",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/make_trend_figure.py",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "1b45b671e6080adfec0997a8725ac790eb5ead81dae1eae677d404892de771d2",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": "tools/nm_ionizing_budget.py",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "73fc81161dac0b4762da9a9102455a5861d3b7a70eeb2d80accd65978f69ae49",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": "tools/nm_paper_video.py",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": "tools/nm_paper_plot.py",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": "/Users/duhokim/HermesOps/cockpit/videos/plots/fesc-zsweep-photon-budget_trend.png",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "5950a2c50588330c524461d32a35c285a91092d31315d2e253b75d09baeeeded",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": "/Users/duhokim/HermesOps/cockpit/videos/plots/lit_fesc.png",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "c8e867a10a16cc6b26005b0ed4d681c3a8720cbd9ac6ca32ea8c22baeaaec8e9",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718/dispersion_v2.json",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "8e1cacefe5c621f962042f24c1f76f94514a5694674ae096edf576009559e34a",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/KUN_MERGED_REFEREE.md",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "67d934f590832b0d2cde3bb38c46a1fdcab6e6a064b9635b475419d182a177f5",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/LANA_MINOR_FIXES.md",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "fb4d5a72dce36bb83e1bab50727994df08f1c276740bf4f66f5d70331d3d9c89",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/MERIT_PANEL_MERGED.md",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "885f734cdc46cdb10d790a1bac6f8af1bea47142f78c1773da1d1da6ccaab82c",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    },
    {
      "path": {
        "value": ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/fesc-zsweep-photon-budget_history.json",
        "derivation_receipt": {
          "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      "sha256": {
        "value": "25ba51e6d49b43b09da7fe37bc1046bb528b3386e2088ffbc7afe48c8af016a5",
        "derivation_receipt": {
          "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    }
  ],
  "immutable_copies_manifest": {
    "path": {
      "value": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/COPY_HASHES_v2.txt",
      "derivation_receipt": {
        "derived_from": "Re-verified existence from active disk state; originally sourced from historical worker freezes or SOURCE_HASHES_INITIAL.txt",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    },
    "sha256": {
      "value": "5b52aba5650b6e2eb3da609156708b57635b26ac80b2dcae29dbbd995dd36234",
      "derivation_receipt": {
        "derived_from": "Re-hashed directly from current immutable disk bundle bytes",
        "timestamp_utc": "2026-08-09T08:37:05Z"
      }
    },
    "entries": [
      {
        "value": "840ced2b52c2007bc5387fc69b49527c548daca6f6d81b3f14bc9a43b7e9b5af  893604  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/fesc-zsweep-photon-budget.mp4",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "e470ca87d630d797acd235b3f4927139971e655805ec36efac81282e5b0bac55  4528  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/storyboard_fesc_zsweep.json",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "8df9f25b5f8acaf22825d6ece958867562c7e37a73fe69aa8e8175fe0b7aa242  10742  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/TREND_RESULTS.json",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "879b1e63de21caccddc952fe15113207f8785c6ca2932c8bb0844b992238dcb3  6667  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/TREND_DATA.json",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "22f5950b8bc35f70700df86a130ba7634bd74a88693e88496ae342caff9fbc5c  20796  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/MERGED_FESC_ZSWEEP.tex",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "49d7d03ff8991197b39173192c9d66de2a4e6c6a4b51c96e69b5159b49f367a6  151441  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/MERGED_FESC_ZSWEEP.pdf",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "10269f5f89b3d9a11365d5cb11f09f3dc62152d71fd26418affcb8c1db4f6b3c  169796  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/fesc_zsweep_trend.png",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "5f53b139ce545dc6bffec2a67640ae9093f43ef64c4f088808ae62403c4b4ac0  41907  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/fesc_zsweep_trend.pdf",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "1b45b671e6080adfec0997a8725ac790eb5ead81dae1eae677d404892de771d2  12631  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/make_trend_figure.py",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "73fc81161dac0b4762da9a9102455a5861d3b7a70eeb2d80accd65978f69ae49  10138  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/nm_ionizing_budget.py",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c  15653  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/nm_paper_video.py",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d  24755  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/nm_paper_plot.py",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "5950a2c50588330c524461d32a35c285a91092d31315d2e253b75d09baeeeded  88294  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/fesc-zsweep-photon-budget_trend.png",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "c8e867a10a16cc6b26005b0ed4d681c3a8720cbd9ac6ca32ea8c22baeaaec8e9  52811  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/lit_fesc.png",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "8e1cacefe5c621f962042f24c1f76f94514a5694674ae096edf576009559e34a  360749  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/dispersion_v2.json",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "67d934f590832b0d2cde3bb38c46a1fdcab6e6a064b9635b475419d182a177f5  12306  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/KUN_MERGED_REFEREE.md",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "fb4d5a72dce36bb83e1bab50727994df08f1c276740bf4f66f5d70331d3d9c89  3878  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/LANA_MINOR_FIXES.md",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "885f734cdc46cdb10d790a1bac6f8af1bea47142f78c1773da1d1da6ccaab82c  9280  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/MERIT_PANEL_MERGED.md",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      },
      {
        "value": "25ba51e6d49b43b09da7fe37bc1046bb528b3386e2088ffbc7afe48c8af016a5  738  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/fesc/source_freeze_v2/inputs/fesc-zsweep-photon-budget_history.json",
        "derivation_receipt": {
          "derived_from": "Read from generated size-bearing manifest COPY_HASHES_v2.txt",
          "timestamp_utc": "2026-08-09T08:37:05Z"
        }
      }
    ]
  },
  "publication_state": {
    "value": "local only; all upload/publication/website gates closed",
    "derivation_receipt": {
      "derived_from": "Unmodified gate status list mandated by HWAO_TWO_HOUR_SIBLING_ORDER",
      "timestamp_utc": "2026-08-09T08:37:05Z"
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
