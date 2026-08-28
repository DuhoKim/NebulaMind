# GORU PROPOSAL: MZR-ANCHOR (CORRECTED)

## Freeze State
PROPOSED (Pending Adjudication)

## Evidence Inventory
- All 12 named original sources re-hashed.
- `SOURCE_BYTES_INITIAL.txt` updated to include all 12 paths and their sizes.
- The 11 immutable frozen copies have been bound via their path+size+hash manifest (`COPY_HASHES.txt`, SHA-256: `009af57e31f0741f86a975016ec9ca7079f196f4feb2578a316b81bdb1f771a0`).
- No historical decision, verdict, boundary, or reportability field was imported.
- `frozen_at` timestamp is securely pulled from `date` at time of writing.

## Historical Re-verification Log


## Proposed SOURCE_FREEZE.json
```json
{
  "freeze_id": "mzr-anchor-proposed-freeze-corrected",
  "frozen_at": "2026-08-09T08:25:45Z",
  "video_reportable_now": false,
  "decision": "PROPOSED_SOURCE_FREEZE; PENDING_ADJUDICATION",
  "blockers": [
    "Pending Lana science adjudication",
    "Pending Kun adversarial break-test",
    "Pending Tori custody sweep"
  ],
  "allowed_scope": [
    "method-only explanation",
    "anchor-building method"
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
      "path": "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/videos/c41-highz-mzr-calibration-anchored.mp4",
      "sha256": "02a26fa3449dd5dfc070b21988430ec51bd8d69d40adcc883a4ff2cba7831ed8"
    },
    {
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/storyboard_c41_anchor_gap.json",
      "sha256": "71301a6ad1bb074cb233a738871cd1f752597864bb089b2d30caa556bf45362c"
    },
    {
      "path": "/Users/duhokim/NebulaMind/NebulaMind/tools/nm_paper_video.py",
      "sha256": "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c"
    },
    {
      "path": "/Users/duhokim/NebulaMind/NebulaMind/tools/nm_paper_plot.py",
      "sha256": "6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d"
    },
    {
      "path": "/Users/duhokim/HermesOps/cockpit/videos/plots/lit_metallicity.png",
      "sha256": "58d8dbf53a51f6b76e4d46ca82b4b319f49d01cb1f014f3b518e86703764c4a3"
    },
    {
      "path": "/Users/duhokim/HermesOps/cockpit/videos/plots/c41-highz-mzr-calibration-anchored_bins.png",
      "sha256": "5e815ef2780c590e1e23f9877b39d30090ab82446ac218b266fa94f5e3db7b3c"
    },
    {
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_RESULTS.json",
      "sha256": "f9b671aa0fa6915f4762bf48b24bcb629be8cb0c92e2b89f08d28f7cbe3e3fd6"
    },
    {
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_SAMPLE.jsonl",
      "sha256": "cfecf77e25a96e6e1855979cb6139ac8b119ca1a7024b4dcf6324490d6b2caaa"
    },
    {
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_LOG.txt",
      "sha256": "45ffb83fbe761739c83ec5f9eb04edab17ef492b54dd97e3d8cb5863a1d342e1"
    },
    {
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/ANCHOR_GAP_PAPER.tex",
      "sha256": "976dd94eab22b62b0f69309ce3c161b7b7561cc541a097a25d346679414abf32"
    },
    {
      "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/ANCHOR_GAP_PAPER.pdf",
      "sha256": "6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232"
    },
    {
      "path": "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/studies/c41-highz-mzr-calibration-anchored.pdf",
      "sha256": "6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232"
    }
  ],
  "immutable_copies_manifest": {
    "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze/COPY_HASHES.txt",
    "sha256": "009af57e31f0741f86a975016ec9ca7079f196f4feb2578a316b81bdb1f771a0",
    "entries": [
      "6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze/inputs/ANCHOR_GAP_PAPER.pdf",
      "976dd94eab22b62b0f69309ce3c161b7b7561cc541a097a25d346679414abf32  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze/inputs/ANCHOR_GAP_PAPER.tex",
      "02a26fa3449dd5dfc070b21988430ec51bd8d69d40adcc883a4ff2cba7831ed8  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze/inputs/current_public_video.mp4",
      "58d8dbf53a51f6b76e4d46ca82b4b319f49d01cb1f014f3b518e86703764c4a3  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze/inputs/lit_metallicity.png",
      "6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze/inputs/nm_paper_plot.py",
      "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze/inputs/nm_paper_video.py",
      "5e815ef2780c590e1e23f9877b39d30090ab82446ac218b266fa94f5e3db7b3c  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze/inputs/source_bins.png",
      "71301a6ad1bb074cb233a738871cd1f752597864bb089b2d30caa556bf45362c  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze/inputs/source_storyboard.json",
      "45ffb83fbe761739c83ec5f9eb04edab17ef492b54dd97e3d8cb5863a1d342e1  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze/inputs/T3_REAL_LOG.txt",
      "f9b671aa0fa6915f4762bf48b24bcb629be8cb0c92e2b89f08d28f7cbe3e3fd6  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze/inputs/T3_REAL_RESULTS.json",
      "cfecf77e25a96e6e1855979cb6139ac8b119ca1a7024b4dcf6324490d6b2caaa  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze/inputs/T3_REAL_SAMPLE.jsonl"
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
