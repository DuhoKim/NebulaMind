# RENDER — Duho authorized 2026-08-18. Local pipeline only.

The packet is gated: `KUN_PACKET_GATE_20260818.md` → `PASS_EXPLAINER_PACKET`. Build the video.

## No credits are needed and none may be spent

The previous BHU video was built entirely locally — PIL for cards, ffmpeg for assembly, TTS through
the managed gateway your subscription already covers. **No Veo, no Flow, no image API.** Follow that
pattern:

    ../bhu-closing-video-20260812T2322K/build_v7/build_audio.py     gateway TTS, gpt-4o-mini-tts, alloy
    ../bhu-closing-video-20260812T2322K/build_v7/render_v7.py       PIL cards + ffmpeg, 1920x1080 @30
    ../bhu-closing-video-20260812T2322K/build_v7/run_asr.py         the QA step that matters — see below

**`render_v7.py` is bespoke, not generic.** Its card drawing is hard-coded to the previous video's
text at fixed coordinates, and its storyboard schema differs from yours (it expects a `cards` array;
`STORYBOARD.json` has `script_contract`). Reuse its *approach* — the PIL/ffmpeg structure, the
provenance capture, the QA frames — not its content. Write new card code for your 8 panels against
Goru's `VISUALS.md`.

## The QA step that is not optional

A gated script and a rendered video are different artifacts. **The video can say something the
script does not** — through a TTS mispronunciation, a truncated line, a card/audio mismatch, or a
panel that renders text different from what was approved.

So: **ASR the finished narration and diff it against `SCRIPT.md` word by word.** The previous build
did exactly this (`run_asr.py`) and it is why that video could be trusted. Report the diff. Any
divergence from the gated text is a defect, not a tolerance — most of all if it touches the four
claims the adjudication refuses:

- not "the black-hole-universe idea is falsified" — one chain fails as its author stated it;
- not "Smolin's hypothesis is refuted";
- not "we measured" or "we discovered";
- the 2.35-solar-mass star must not appear as supporting evidence.

Also verify every card's on-screen heading matches its panel's assertion heading in `SCRIPT.md`
exactly. A card is a claim; a mistyped card is a false claim that outlives every caveat.

## Build

1. Narration from `SCRIPT.md` via the gateway, alloy, calm public-science delivery. Numbers as
   digits are already in the text — do not re-spell them.
2. Cards per `VISUALS.md`: legible high-contrast flat infographics, assertion heading on every panel,
   cosmic backdrop only dim and only if it costs nothing. Panel 03's mass ladder must show the error
   bar on 2.08 ± 0.07 visibly dipping below the 2.00 line — that detail *is* the argument for why
   limb 1 stops at serious doubt.
3. Assemble at 1920×1080/30 with captions. Target 4–6 minutes.
4. Capture provenance as the previous build did: tool versions, input hashes, a contact sheet, QA
   frames.

## Boundaries

**Do not upload. Do not publish. Do not change any visibility setting.** The file stays on disk.
Uploading is a separate decision and the standing rule is unlisted-only even then.

No Veo, no Flow, no image API, no credits. Do not touch `portal.nersc.gov` — the checksum harvest
resumes at 12:00 KST on frozen pacing.

Write everything under `bhu-neutron-star-explainer-20260817/build/`.

Report: the ASR diff against the script, the card-heading check, output duration and size, the
provenance record, and anything you had to change from the plan and why.
