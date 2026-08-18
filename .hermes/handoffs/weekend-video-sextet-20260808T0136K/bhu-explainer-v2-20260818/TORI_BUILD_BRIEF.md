# TORI — v2 build brief (local render only)

Read `SEXTET_BRIEF_V2.md` first. Do not start before `KUN_PACKET_GATE_V2.md` exists with first
line `PASS_EXPLAINER_PACKET`. Build entirely under `build/` in THIS directory.

## Adapt, don't reinvent

`../bhu-neutron-star-explainer-20260817/build/` is the working v1 pipeline; copy its structure
and adapt:

- `pipeline.py` — point at v2 files; regenerate `EXPECTED_HASHES` from the gated v2 inputs
  (SCRIPT.md, STORYBOARD.json, VISUALS.md, CLAIM_LEDGER.md, KUN_PACKET_GATE_V2.md, this brief's
  authorising doc is `SEXTET_BRIEF_V2.md`); the gate check reads `KUN_PACKET_GATE_V2.md` first
  line == `PASS_EXPLAINER_PACKET`.
- `render_cards.py` — new drawers for the v2 panel set per `VISUALS.md`. Keep the closed-world
  `TextSurface` enforcement exactly: every drawn string must be in the panel's
  `viewer_text_closed_world`, emitted order must equal the list, mismatch raises.
- `build_audio.py` — unchanged approach: gateway TTS `gpt-4o-mini-tts`, voice `alloy`, per-
  sentence receipts, fixed card grid, loudnorm, captions. Keep the Bethe-pronunciation retake
  policy keyed to whichever v2 sentence ids contain "Brown–Bethe". Duration contract 240–360 s;
  panel 01 ends ≤ 35 s.
- `assemble.py` — output name `BHU_EXPLAINER_V2_LOCAL_REVIEW.mp4` (+ .srt/.vtt), same stream
  contract (h264 1920×1080@30, aac 48k mono, default eng mov_text).
- `qa_final.py` — unchanged approach: decoded-audio ASR (whisper-1 via gateway) word-diff per
  panel with the declared normalization policy, targeted sentence-window adjudication, heading
  pixel QA, caption payload QA, volumedetect, forbidden-affirmation sweep (keep the v1 list).
- `test_pipeline.py`, `verify_freeze.py`, `freeze.py` — adapt names/paths; freeze only on
  `PASS_LOCAL_RENDER_QA_READY_FOR_KUN_REVIEW`.

## Hard boundaries

- Local Pillow + ffmpeg only; TTS/ASR only through the Hermes managed gateway. **No Veo, no
  Flow, no image API, no credits, no upload, no publication.**
- **Do not touch `portal.nersc.gov`** — the checksum harvest is live.
- Write only under this lane directory (`build/`, `_tmp_*`). Report every deviation from the v1
  approach in `build/BUILD_REPORT.md`.
- Finish by writing `TORI_DONE.md` at lane root, first line `TORI_V2_BUILD_COMPLETE`, with the
  candidate SHA-256, duration, and QA statuses; or `TORI_V2_BUILD_HOLD` plus what blocked you.
