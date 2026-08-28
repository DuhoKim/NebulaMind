# RECEIPT — spin-method-canary-20260808T0325 (v5)

Seat: `yui-video-integration`. Rendered 2026-08-08 03:25–03:29 KST (stamps from `date`).
Freeze in force: unchanged — `spin-method-canary-pass1-20260808T0153K`.

## What this is

Version 5 of the silent, method-only galaxy-spin visual canary. **v1–v4 preserved unchanged**
as the correction lineage.

## The one change, and its evidence

**Audience-facing citations are now human-readable; verification paths and hashes live only in
receipts.** Standard: upheld by the spin lane's sealed v8 audit (zero internal paths/workflow
identifiers on screen) and requested in identical terms by three lanes (fesc item 7, c41-mzr
item 7, c41-uvlf "do not reuse internal filenames as audience citations").

Applied as one coherent correction:

- `display_citation` fields added to all 9 sourced cards, mirroring the sealed v8 deck's own
  audience citations ("Galaxy Zoo 1 DR · frozen NebulaMind T1 run · 2026-08-05",
  "NebulaMind T1C column-integrity run · 2026-08-05", weekend freeze/status lines). The
  `source` paths are retained and still drive the numeric guard.
- The readouts figure's provenance line drops `T1_FUNNEL.json (sha256 …)` for the same
  audience citation; the sha remains pinned in this receipt's `hashes.txt`.
- **Bounded candidate-workspace renderer-copy edit** (explicitly allowed by DELEGATION):
  `render_card` now prints `display_citation` when present, unchanged `source:` fallback
  otherwise. Previous copy sha `919af6b1…` (identical to the freeze-pinned repo renderer) is
  recorded in `hashes.txt`; the new copy sha is in the same file. **The repo's shared
  `tools/nm_paper_video.py` is untouched** — Git and shared-tool gates remain closed.

All headings, bodies, counts, and figure geometry are otherwise identical to v4.

## Remaining queued corrections

One-A-per-readout bridge on the equation card; on-screen definition of the dominance
threshold. Next in queue.

## Verification

- Numeric-source guard: PASS 11/11 twice (source paths intact for verification).
- Machine QA (`audit_canary.py`): PASS — 11 states, all expected cuts, none unexpected, single
  silent H.264 stream, sha `1cbf445c…` matches `hashes.txt`, 116.0 s = 110.0 s + 6.0 s close
  hold.
- Encoded-frame QA: citation footer verified at full resolution (data card); contact sheet
  covers all 11 states.

## Gates untouched

No TTS, no Git, no upload/publication, no shared-tool or public-asset writes.
