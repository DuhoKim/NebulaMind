# RECEIPT — mzr-census-method-canary-20260808T1254 (v1)

Seat: `yui-video-integration`. Rendered 2026-08-08 12:54–13:02 KST (stamps from `date`).
Authority: Duho's order of 2026-08-08 (integrator/METHOD_ONLY_PATTERN.md) — apply the
method-only PATTERN to this lane; never spin's content. Lane state at build time:
no `lanes/mzr-census/SOURCE_FREEZE.json` exists → no authorized result → method-only is the
only honest cut. If the lane publishes a freeze, its scopes supersede this deck.

## What this is

A silent, method-only visual canary for the MZR archive census: 10 cards, 1920×1080 @ 30 fps,
H.264 video-only, 107.0 s (101.0 s storyboard + 6.0 s concat close hold). Persistent
`RESULT HELD` capsule (safe-area compliant), human-readable audience citations, house style.

## Pattern → this lane's content (all from the lane's OWN artifacts)

1 title/question · 2 hold (no freeze, T2 not applied) · 3 frozen rules (T2 freeze record,
Duho 2026-08-06) · 4 sample (157 recorded candidates) · 5 readouts (three search axes →
178 → −21 → 157, parallel-axes figure) · 6 the rule (single-table intersection; joins not
assessed) · 7 control logic (7/7 recall, 0/3 decoys, precision-not-certified taxonomy) ·
8 side check (62-of-157 vocabulary scan, not-a-ruling boundary) · 9 boundary (open gates) ·
close. No move was dropped — every move had a lane source.

## Sources (pinned, sha in hashes.txt)

`T1_MZR_MANIFEST.json` (178/157/dropped list/recall/controls), `T1E_GASPHASE_COUNT.json`
(62/157 + not-a-ruling), `T1_FINDINGS.md` (per-axis reach table, precision taxonomy),
`FREEZE_RECORD_T2.md` (freeze provenance), `WORKFLOW_CHECKLIST.json` (open gates). All copied
from `lane-mzr-census/worker-yui/frozen_sources/pass7/` — the lane's own hash-pinned custody.

## Guard evidence note (PASS ≠ authorization)

Guard PASS 10/10 twice. Two matches flagged multi-hit ("19", "21" landing on table_id
substrings): both values are DERIVED from the manifest's `dropped_candidates` array —
21 entries, of which 19 empty the redshift axis — verified by an assert in
`build/make_figures.py` (178 − 21 = 157) and marked SUPPORTED in the lane's own
`NUMERIC_SOURCE_AUDIT.json`. The derivation, not the substring hit, is the sourcing.

## Gates untouched

No TTS, no Git, no upload/publication, no shared-tool or public-asset writes, no writes
outside `integrator/`.
