PASS_P2V_RENDER

# KIMI Phase 2 video — RENDER GATE

kimi (second reviewer, fresh one-shot), 2026-08-19 KST. Findings-only; nothing edited;
exactly one file written (this one); scratch frames/segments under /tmp only, removed after
use; zero web fetches; portal.nersc.gov untouched. Method: one shasum invocation, ffprobe,
ffmpeg frame extraction, gateway ASR re-transcription, and mechanical recount against the
gated packet (SCRIPT.md / STORYBOARD.json / CLAIM_LEDGER.md / VISUALS.md) and the freeze
receipts.

## (1) Custody — PASS

- `shasum -a 256 build/BHU_PHASE2_RESULTS_VIDEO_LOCAL_REVIEW.mp4` (one invocation, one
  file): `f251d43cda0e7383d56864830cc3d0f68023b065205917edc2e2adb37964ffcb` — byte-identical
  to GPT3_DONE.md's frozen value. ✔
- ffprobe duration: `330.466667` s — inside 240–360 s. ✔
- Freeze cross-check: all six FREEZE.json gated inputs (VIDEO_BRIEF_P2.md, SCRIPT.md,
  STORYBOARD.json, VISUALS.md, CLAIM_LEDGER.md, KIMI_P2V_PACKET_GATE.md) re-hashed and
  unchanged since freeze. ✔

## (2) ASR QA audit — PASS (re-transcription performed; nothing UNVERIFIED-AT-GATE)

- Coverage: ASR_QA.md covers all 10 panels (01–10), each with expected text, ASR text,
  alignment, and protected-phrase checks. ✔
- Decoded-from-final-mp4 proof (not intermediate wavs): this gate decoded the audio track
  from the exact frozen MP4 (`ffmpeg -i <mp4> -map 0:a:0`), cut all 10 panel segments with
  qa_final.py's own boundary formula over `audio/timeline.json`, and re-hashed each segment:
  all 10 SHA-256s MATCH the `candidate_audio_sha256` stored in `build/qa/asr-panel-*.json`
  (e.g. panel 09 `ea065a6c…`, panel 10 `fbcceb20…`). The stored ASR transcripts were
  therefore produced from audio decoded from the final MP4 itself. ✔
- The 1 declared cosmetic residual is quoted in ASR_QA.md: panel 10 `replace`
  expected `[poplawski]` → ASR `[popovsky]`. This gate adjudicates it genuinely cosmetic:
  a phonetic ASR rendering of the chain's proper name; no number, negation, caveat,
  Reading-1 clause, or verdict content touched; all three panel-10 protected phrases
  verified contiguous. ✔
- Zero contract-bearing residuals, independently supported: this gate re-ran the declared
  normalization + alignment + judgment logic over all 10 stored transcripts vs the
  storyboard narrations — recount: **0 contract-bearing, exactly 1 cosmetic**, aggregate
  word errors 1/691; all six contract phrases PASS; forbidden-phrase sweep
  (false/impossible/proved-wrong/Smolin-refuted) over the full transcript blob: no hits. ✔
- Gateway ASR was REACHABLE: this gate spot-re-transcribed panels 09 and 10 itself
  (whisper-1 via the managed route, segments byte-identical to the originals). Both
  re-transcripts reproduce the stored transcripts word-for-word, including the two known
  ASR phonetics ("nuclear synthesis" for "nucleosynthesis" in P09 — a declared
  normalization entry, number 45 and claim intact; "Popovsky" in P10 — the declared
  cosmetic residual). Stored ASR is authentic and reproducible. ✔

## (3) Frame audit — PASS

Five frames extracted from the final MP4 (ffmpeg, panel-mid timestamps 17/82/206/237/310 s)
and read against VISUALS.md:

- Panel 01 (verdict panel): heading "The inheritance route now has a ceiling, and it stays
  closed" exact; scope label present ("DUHO'S PERSONAL SIDE-INTEREST" /
  "NOT A NEBULAMIND RESEARCH PROGRAMME"); Reading-1 chip and all-galaxy-floor chip present;
  no equations. ✔
- Panel 03 (magnitude-ladder + equation panel): heading exact; only the authorized equation
  "w = +1 vs w = −1" visible; ×730 ladder drawn as a linear 730-rung step column with
  color-coded endpoints, magnitude labeled by the in-panel chip "ABOUT ×730 BOUNCE-DENSITY
  GAP"; both bounce drawings (smooth U, sharp cusp) carry Planck-caveat markers (warning
  triangles at the bounce points) with the "PLANCK REGIME · CLASSICAL TREATMENT" chip in the
  same panel. ✔
- Panel 07 (magnitude-ladder + equation panel): heading exact; only "ε ≤ 10⁻²⁷" visible;
  27-step order ladder with labeled in-panel chips "×6.6×10²⁶ ABOVE THE CAUSAL LIMIT",
  Reading-1/Reading-2 branches separate, "CEILING · NOT A TRANSFER FUNCTION" present. ✔
- Panel 08 (equation panel): heading exact; only "a⁻⁶ = a⁻⁶" visible; balanced-scale graphic
  level; "AXIS MEMORY · UNDETERMINED BOTH WAYS" present. ✔
- Panel 10 (final verdict panel): heading exact; the seven verdict rows end on "THE CEILING
  SAYS THE ROUTE STAYS CLOSED"; no caveat, erratum, or future-work text after the verdict;
  no equations. ✔
- Only the three brief-authorized equations appear anywhere; none others. ✔
- Ladders: no unlabeled log compression anywhere. Recorded precisely for the record: the
  ladder graphics carry no on-rung numerals; each magnitude is labeled by deterministic
  text in the same panel, and the geometry is linear step-count (deterministic audit:
  P03 = 730 rungs, P04 = 6 intervals, P07 = 27 order steps, P09 = 45 BBN steps,
  `unlabeled_log_compression: false` in P03/P04/P09) — the dishonest pattern the rule
  prohibits (compressed scale passed off without labels) is not present; the render matches
  the packet-gated VISUALS.md design. ✔
- Planck-caveat marker where a bounce state is drawn: present in P03, the only panel that
  draws bounce states (deterministic audit: `planck_caveat_markers: 2`). ✔

## (4) Contract sweep — PASS

- Narration ends on the verdict: the last panel's ASR text (stored and this gate's own
  re-transcription) ends "…the ceiling says the route stays closed."; the final encoded
  caption cue (291.867–328.067 s) carries the same ending. ✔
- The caveat sentence sits mid-video: the exact honest-caveat sentence is in panel 05 of 10
  (audio window 130.4–155.3 s of 330.47 s, 39–47% through) and appears nowhere in panel 10. ✔
- No divider cards in the frame sequence: `segments/segments.ffconcat` lists exactly
  card-01…card-10 and nothing else; all five extracted frames carry assertion headings;
  the decoded contact sheet is 10 content panels. ✔

## (5) Lane boundary — PASS

- Read-only spot-check: `find /Users/duhokim/HermesOps/cockpit` for *.wav/*.mp4/*.mp3/*.m4a
  newer than 2 hours — zero hits. No build audio or video leaked into the cockpit root. ✔
- FREEZE.json safety block confirms: LOCAL_ONLY_NOT_UPLOADED, no Flow/Veo/image-generation,
  0 credits, portal.nersc.gov unused. ✔

## Decision

All five render-gate checks pass. The frozen MP4 is byte-identical to GPT3_DONE.md's
receipt, inside the duration window; its decoded-audio ASR is fully accounted for with zero
contract-bearing residuals and one genuinely cosmetic proper-name phonetic; the decoded
frames honor the heading, equation, ladder, Planck-marker, and scope rules; the narration
ends on the verdict with the caveat mid-video and no divider cards; nothing was written
outside the lane. Cleared for Tori's registry check and unlisted upload step. This gate
authorizes no upload, publication, or status change by itself — chain order governs.

— kimi, 2026-08-19 KST.
