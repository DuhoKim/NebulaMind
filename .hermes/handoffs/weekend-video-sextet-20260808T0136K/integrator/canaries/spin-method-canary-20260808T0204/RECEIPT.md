# RECEIPT — spin-method-canary-20260808T0204

Seat: `yui-video-integration` (sole `integrator/` writer, per `integrator/DELEGATION.md`).
Rendered 2026-08-08 02:04–02:09 KST (stamps taken from `date`, not estimated).
Freeze in force: `spin-method-canary-pass1-20260808T0153K` —
`video_reportable_now: false`, decision `BLOCK_SUBSTANTIVE_RESULT_RENDER; ALLOW_METHOD_ONLY_CANARY`.

## What this is

A **silent, method-only, versioned visual canary** for the spin-parity lane — the First Task in
`DELEGATION.md`. It is NOT a result video and does not become one by passing QA. 11 cards, 1920×1080,
30 fps, H.264, **video stream only** (lane audio contract: `silent; narration/TTS not authorized`).

## What changed and why

- New storyboard `storyboard_spin_method_canary.json`, written from scratch strictly inside the
  freeze's `allowed_scope`: frozen source/sample funnel · the predeclared asymmetry equation
  (symbolic only, value withheld) · handedness convention + mirroring/alignment schematic ·
  predeclared bias-control design (design only, no outcomes) · a clearly labelled
  unresolved-result boundary, stated by card 2 and restated at the close.
- Two figures drawn deterministically by `build/make_figures.py` from the pinned copy of
  `T1_FUNNEL.json` (freeze disposition: "canary redraws allowed counts deterministically").
  The quarantined result figures (verdict/significance/paired/decomposition) were not read,
  not reused, not approximated. No asymmetry, ratio, or significance is computed anywhere.
- Renderer: the seeded candidate-workspace **copy** of `nm_paper_video.py`, sha-verified identical
  to the freeze's pinned shared renderer (`919af6b1…`). The repo's `tools/` was not touched.
  Output path passed explicitly with `--out` (the renderer's default lands in
  `frontend/public/videos/`, which is a closed gate).

## Source authority

- Pinned copies in `sources/` sha-match the freeze exactly: `T1_FUNNEL.json ed97758a…`,
  `T1C_COLUMN_INTEGRITY.json fc73061f…`. Gate snapshots `STATUS.json` / `SOURCE_FREEZE.json`
  hashed at copy time.
- Numeric-source guard: PASS, all 11 cards, twice (pre-edit and pre-render). Evidence audit is
  single-hit and on-topic: `667944 → "rows_parsed"`, `29053 → "N_tie"`, `36 → "probed"`.
- **A guard PASS is not semantic authorization.** A separate manual scope audit mapped every card
  to an `allowed_scope` item (see QA.md) and removed two guard-invisible soft spots before render:
  a "monochrome control" mention supported only by quarantined T3 material, and a "three gates"
  count that did not match the freeze's four recorded blockers.

## Deliberately excluded (forbidden scope honoured)

T3/T4 headline or result figures and numbers; MIXED/flip outcomes; significance; dipole-axis,
parity, or any cosmological interpretation; GRB/SN Ia/dark-energy/quasar/H0 context;
black-hole-universe support; any new DESI Legacy Survey or Ganalyzer claim; everything in
`USER_NOTE_GALAXY_SPIN_20260808T0145K.md`.

## Gates untouched

No TTS. No Git. No upload or publication. No write outside `integrator/canaries/…`. No cockpit,
DB, `frontend/public/videos/*`, `paperVideos.ts`, or shared-tool edits. Rejected or superseded
attempts, if any follow, are preserved beside this one — never overwritten.
