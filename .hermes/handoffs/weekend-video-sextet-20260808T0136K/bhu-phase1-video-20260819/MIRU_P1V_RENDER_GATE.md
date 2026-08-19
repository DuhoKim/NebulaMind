PASS_RENDERED_EXPLAINER

# Miru — Phase 1 results video render gate (second reviewer, fresh one-shot)

Candidate: `build/BHU_PHASE1_RESULTS_VIDEO_LOCAL_REVIEW.mp4`
Pinned SHA-256: `e32cc6109c7b7a514b0b0336a6ac65783f25d0407e764f2504307cb49aa5e4fc`
Freeze: `build/FREEZE.json` (`FROZEN_LOCAL_ONLY_READY_FOR_MIRU_REVIEW`)
Method honored: local only, grep extraction, time-boxed, python for hashes/probes. No portal.nersc.gov. No writes outside this report. Findings only.

## 1. Hash of the rendered candidate — PASS

Recomputed SHA-256 over the file this session:
`e32cc6109c7b7a514b0b0336a6ac65783f25d0407e764f2504307cb49aa5e4fc` — exact match to the pin.
Byte count 13,645,108 matches FREEZE.json `candidate_bytes`.

## 2. Container and duration probe — PASS

My ffprobe of the candidate: `mov,mp4` container, 3 streams —
video h264 1920x1080 @ 30 fps (10,663 frames), audio aac 48 kHz, subtitle mov_text (eng).
Format duration `355.433333` s — matches the expected 355.433 s and the freeze value exactly.
Consistent with `build/qa/final-ffprobe.json`. Panel 01 spans 0.0–34.0 s (inside the 35 s stakes contract).

## 3. Embedded captions vs gated SCRIPT.md — PASS

Extracted the embedded mov_text stream myself (`ffmpeg -map 0:s:0`): 48 cues.
SCRIPT.md yields 48 narration sentences across the 10 panels.
Every cue diffs byte-exact against its script sentence: 0 mismatches out of 48.
My extracted dump is byte-identical to the QA artifact `encoded-captions.srt`
(sha256 `785b7051f6fa8cd76aad39b4e323844bf3d5f179e571f14066982165366fe693`), and cue text plus
timing match the frozen sidecar `.srt`/`.vtt`, whose hashes match their FREEZE pins
(`07713233…`, `b548ed2a…`). Encoded vtt sha `41525f78…` matches the caption QA pin.

## 4. ASR reports and the retake cycle — PASS, with one documentation discrepancy (4.4)

### 4.1 Final candidate's ASR is the one that passed — confirmed

`final-qa-report.json` (sha matches FREEZE pin) names the ASR report under
`qa/candidate-e32cc610…/` — the same hash as the pinned candidate. `asr-word-diff.json`
(sha matches pin `b60ae79b…`) carries `candidate_sha256` equal to the pinned mp4 hash, status
`PASS_EXACT_ASR_WORD_DIFF_WITH_TARGETED_CONTEXT_ADJUDICATION`, 0 aggregate word errors after the
declared normalization policy. The policy's forbidden list (negation removal, arbitrary
homophones, scientific-name substitution, claim paraphrase) is intact; I recounted negations
independently: 7 `not` in expected text, 7 in the effective transcripts. The report's scope says
ASR ran on audio decoded from the exact final MP4 — I re-decoded the mp4 audio myself and it is
byte-identical to the QA's `encoded-audio.wav` (sha `aa19913b…`), so that scope claim is true.

### 4.2 Adjudicated, not erased — confirmed

Panel 08's full-card ASR dropped "observable universes" (a 2-word delete). The original
card-context diff is preserved verbatim in both `asr-word-diff.json` and `ASR_WORD_DIFF.md`,
and the resolution came from a targeted sentence-window re-decode of all six panel-08 sentences
(c08s01–c08s06), each with its own pinned audio file and ASR json. All 16 audio evidence files
(10 card windows + 6 adjudication windows) exist and hash-match the report records. The earlier
TTS-stage retakes are likewise recorded, not erased: sentence receipts keep the retake
instruction-policy versions (e.g. `inflation-era-pinned-retake-v2`, `saadeh-pronunciation-retake-v1`).

### 4.3 Forbidden sweep — independently re-run, PASS

0 hits for `is falsified`, `we proved`, `theory is dead`, `smolin` across the embedded captions
and SCRIPT.md, matching the report's empty hit list.

### 4.4 Discrepancy (documentation, not artifact): superseded candidate dirs

The kickoff parenthetical says two superseded candidate dirs exist. On disk, `build/qa` contains
exactly one candidate dir — the final `candidate-e32cc610…` — and a packet-wide grep finds 86
references to that one candidate hash and zero references to any other candidate hash. No
superseded candidate dirs are physically present in this packet. The substance of the requirement
is nonetheless met: the final candidate's ASR is provably the one that passed (4.1), and the
retake/adjudication trail is recorded inside the surviving artifacts (4.2). If the coordinator
wants superseded QA workspaces retained as first-class evidence in future builds, that is a
process note for the pipeline — nothing in the rendered candidate needs repair for it.

## 5. Encoded-pixel spot checks — PASS

I decoded frames fresh from the candidate (card 03 @ 85.0 s, card 04 @ 119.0 s, card 09 @ 302.0 s).
My decodes sit at RMS 0.86–1.37 from Tori's stored decoded frames (same static card, different
sample instant) and 3.5–4.6 from the source cards (codec noise), and I read the pixels directly:

- Dilemma panel (card 03): `Λ = 3Ω²/c²` present; `HORN 1: 10⁹ × PLANCK BOUND` present;
  `HORN 2: < 10⁻¹⁸ × DARK ENERGY` present including the `<`. All three match
  `card-text-and-geometry-audit.json` `emitted_text` exactly (audit also records
  `horn_2_label` with the `<` and 9/18 tenfold steps with no unlabeled log spacing).
- Seesaw panel (card 04): `w = +1/3` present with the plus sign.
- Panel 09: both parent labels present — `Supermassive Parent` and `Stellar Parent`.

`heading-and-frame-qa.json` (sha matches pin) shows all 10 cards with exact heading projection
and decoded heading-crop pixel matches.

## 6. FREEZE safety block — PASS

`safety`: `publication_state = LOCAL_ONLY_NOT_UPLOADED`, `video_generation_services = []`,
`flow_used = false`, `veo_used = false`, `credits_spent = 0`. Re-ran `build/verify_freeze.py`
this session: `PASS_FROZEN_PROVENANCE_VERIFIED` (7 gated inputs, 237 inventory files). I also
re-hashed all 7 gated inputs (SCRIPT.md, STORYBOARD.json, VISUALS.md, CLAIM_LEDGER.md,
LANA_ANNOTATION_REVIEW.md, MIRU_P1V_PACKET_GATE.md, SEXTET_BRIEF_P1_VIDEO.md) against the freeze
manifest: all match, bytes and sha256.

## 7. Evidence ledger (what I ran)

- python SHA-256 of the candidate mp4; byte count.
- ffprobe JSON probe of the container (format, 3 streams, duration, resolution, fps).
- ffmpeg extraction of the embedded subtitle stream; python SRT parser; exact 48/48 cue diff
  against SCRIPT.md sentences; sha comparisons against sidecar and QA caption artifacts.
- Hash verification of `final-qa-report.json`, `asr-word-diff.json`, `ASR_WORD_DIFF.md`,
  `heading-and-frame-qa.json`, `caption-payload-qa.json`, `BUILD_REPORT.md` against FREEZE pins.
- Byte-identity re-decode of the candidate audio vs QA `encoded-audio.wav`; independent negation
  recount; independent forbidden-phrase sweep; hash check of all 16 ASR audio evidence files.
- Fresh ffmpeg frame decodes at cards 03/04/09; RMS comparison to Tori's decoded frames and the
  source cards; direct visual reads of the required equations and labels.
- Re-ran `verify_freeze.py`; re-hashed all 7 gated inputs.
- Packet-wide `candidate-*` directory and hash-reference sweep for the supersession question (4.4).

## 8. Net finding

The rendered candidate is exactly the frozen, pinned artifact; its duration, embedded captions,
decoded-audio ASR, encoded pixels, and safety posture all verify from local artifacts. The one
discrepancy is in the kickoff's parenthetical about two superseded candidate dirs (see 4.4); it
does not touch the artifact. Verdict: PASS_RENDERED_EXPLAINER. This gate authorizes no upload,
publication, or public status change by itself; those remain separate gates.

— Miru, render gate, 2026-08-19. Findings only; packet files untouched apart from this report.
