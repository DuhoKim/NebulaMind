# GORU PROPOSAL: MZR-ANCHOR (V2)

## Freeze State
PROPOSED (Pending Adjudication)

## Evidence Inventory (V2)
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
  "freeze_id": "mzr-anchor-proposed-freeze-v2",
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
      "path": "frontend/public/videos/c41-highz-mzr-calibration-anchored.mp4",
      "sha256": "02a26fa3449dd5dfc070b21988430ec51bd8d69d40adcc883a4ff2cba7831ed8"
    },
    {
      "path": ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/storyboard_c41_anchor_gap.json",
      "sha256": "71301a6ad1bb074cb233a738871cd1f752597864bb089b2d30caa556bf45362c"
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
      "path": "../../HermesOps/cockpit/videos/plots/lit_metallicity.png",
      "sha256": "58d8dbf53a51f6b76e4d46ca82b4b319f49d01cb1f014f3b518e86703764c4a3"
    },
    {
      "path": "../../HermesOps/cockpit/videos/plots/c41-highz-mzr-calibration-anchored_bins.png",
      "sha256": "5e815ef2780c590e1e23f9877b39d30090ab82446ac218b266fa94f5e3db7b3c"
    },
    {
      "path": ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_RESULTS.json",
      "sha256": "f9b671aa0fa6915f4762bf48b24bcb629be8cb0c92e2b89f08d28f7cbe3e3fd6"
    },
    {
      "path": ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_SAMPLE.jsonl",
      "sha256": "cfecf77e25a96e6e1855979cb6139ac8b119ca1a7024b4dcf6324490d6b2caaa"
    },
    {
      "path": ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/T3_REAL_LOG.txt",
      "sha256": "45ffb83fbe761739c83ec5f9eb04edab17ef492b54dd97e3d8cb5863a1d342e1"
    },
    {
      "path": ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/ANCHOR_GAP_PAPER.tex",
      "sha256": "976dd94eab22b62b0f69309ce3c161b7b7561cc541a097a25d346679414abf32"
    },
    {
      "path": ".hermes/handoffs/c41-trackb-shape2-mzr-20260804T1452K/ANCHOR_GAP_PAPER.pdf",
      "sha256": "6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232"
    },
    {
      "path": "frontend/public/studies/c41-highz-mzr-calibration-anchored.pdf",
      "sha256": "6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232"
    }
  ],
  "immutable_copies_manifest": {
    "path": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/COPY_HASHES_v2.txt",
    "sha256": "13dc70368f81c0c7bdcc3c10c077cfc7d5bb82a174ebda530683421cbeb303ef",
    "entries": [
      "02a26fa3449dd5dfc070b21988430ec51bd8d69d40adcc883a4ff2cba7831ed8  897182  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/c41-highz-mzr-calibration-anchored.mp4",
      "71301a6ad1bb074cb233a738871cd1f752597864bb089b2d30caa556bf45362c  4423  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/storyboard_c41_anchor_gap.json",
      "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c  15653  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/nm_paper_video.py",
      "6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d  24755  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/nm_paper_plot.py",
      "58d8dbf53a51f6b76e4d46ca82b4b319f49d01cb1f014f3b518e86703764c4a3  89827  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/lit_metallicity.png",
      "5e815ef2780c590e1e23f9877b39d30090ab82446ac218b266fa94f5e3db7b3c  37374  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/c41-highz-mzr-calibration-anchored_bins.png",
      "f9b671aa0fa6915f4762bf48b24bcb629be8cb0c92e2b89f08d28f7cbe3e3fd6  4326  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/T3_REAL_RESULTS.json",
      "cfecf77e25a96e6e1855979cb6139ac8b119ca1a7024b4dcf6324490d6b2caaa  25430  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/T3_REAL_SAMPLE.jsonl",
      "45ffb83fbe761739c83ec5f9eb04edab17ef492b54dd97e3d8cb5863a1d342e1  17167  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/T3_REAL_LOG.txt",
      "976dd94eab22b62b0f69309ce3c161b7b7561cc541a097a25d346679414abf32  34695  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/ANCHOR_GAP_PAPER.tex",
      "6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232  157143  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/ANCHOR_GAP_PAPER.pdf",
      "6be02f3ebaf86ea03854df628bd05787929e6a851bcb992240b4cf98453df232  157143  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/mzr-anchor/source_freeze_v2/inputs/c41-highz-mzr-calibration-anchored.pdf"
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
