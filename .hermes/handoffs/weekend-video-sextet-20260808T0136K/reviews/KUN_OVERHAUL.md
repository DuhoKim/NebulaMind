# KUN_OVERHAUL — Reproducibility, Rendering, A/V Sync

Seat: Kun
Timestamp: 2026-08-08 KST
Scope: adversarial encoded-artifact review for the spin presentation overhaul.

## Verdict

**No new spin overhaul canary is present for KUN acceptance yet.** I found only the rejected spin
sequence through `spin-method-canary-20260808T0648`; the later canary directories currently present
are paused sibling baselines (`mzr-census-method-canary-20260808T1254`,
`fesc-method-canary-20260808T1259`), not the requested spin overhaul.

The rejected `0648` artifact fails the new order immediately:

- encoded MP4 has no audio stream, so intelligibility, clipping, WPM, and sentence/action sync are
  all impossible to pass;
- presentation grammar is static cards, including a presenter/character still, a giant standalone
  number card, and paragraph-dominant slides;
- progressive builds are not real animation in the encoded artifact. The MP4 behaves as static
  holds with hard scene changes.

## Encoded Artifact Checked

Path:
`integrator/canaries/spin-method-canary-20260808T0648/spin-method-canary-20260808T0648.mp4`

Direct `ffprobe` result from the encoded MP4:

- duration: 118.000 s
- streams: 1 total
- video: H.264, 1920x1080, 30 fps, 3540 frames
- audio: **none**

This agrees with the artifact's `QA.md`, but the conclusion above is from `ffprobe` on the MP4
itself, not from the build log or receipt.

## Rejected Grammar Observed

I inspected `contact-sheet.jpg` for `0648`. The artifact is visibly the rejected card deck:

- state 01: title card with character still
- state 02: paragraph/status card with character still
- state 03: paragraph card
- state 04: giant `667,944` number card
- state 05: one static funnel/readout figure
- state 06: equation card with paragraph explanation
- state 07: static mirroring schematic
- states 08-10: paragraph/status cards
- state 11: close card with character still

This is not a conference-science animation grammar. It is the prior 11-card layout with static
holds.

## Frame/Animation Evidence

I ran scene detection against the encoded MP4. The detected substantive scene changes occur at:

| Detected change | Time (s) |
|---|---:|
| 1 | 8.000 |
| 2 | 18.000 |
| 3 | 35.000 |
| 4 | 47.000 |
| 5 | 60.000 |
| 6 | 72.000 |
| 7 | 92.000 |

These are sparse hard changes, not progressive sentence-aligned animation. The contact sheet labels
additional nominal states at 4.000, 13.000, 23.000, 31.500, 41.000, 53.500, 66.000, 76.500,
86.500, 99.000, and 112.000 seconds, but the encoded-video scene detector only sees a subset as
major visual changes. Either way, the visual behavior is long static holds.

## Audio, WPM, and Sentence/Action Sync

For `0648`:

- audio stream exists: **fail, no audio stream**
- intelligibility: **not measurable**
- clipping: **not measurable**
- delivered WPM: **not measurable**
- required WPM range 105-125: **fail by absence**
- substantive sentence/action alignment within +/-0.3 s: **not measurable and cannot pass**

No sentence timings can be sampled from `0648` because there is no audio track to align against.

For the new overhaul canary:

KUN acceptance remains blocked until a new spin MP4 lands. I will require the review packet to name
sampled sentences and report actual audio-start and visual-action-start timings, for example:

| Sentence sampled | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| pending new artifact | pending | pending | pending |

Assertions of compliance without encoded-audio timing evidence should be rejected.

## Reproducibility

The `0648` directory records hashes for the storyboard, source JSON files, generated figures,
renderer copy, contact sheet, and MP4. That is useful receipt evidence, but it is not a complete
rebuild recipe by itself:

- `hashes.txt` references `../../candidate-workspace/tools/nm_paper_video.py`, outside the canary
  directory;
- the receipt says this pass was a bounded renderer-copy edit, so rebuild equivalence depends on
  that external renderer copy and environment;
- no locked dependency/environment manifest is present in the canary directory.

Therefore I would not accept "same hashes are recorded" as proof that a future candidate rebuilds
from recorded inputs to the same hashes. The new overhaul canary should include either a self-contained
renderer snapshot or an exact immutable source reference plus dependency/environment receipt.

## Weakest Thing Found

The weakest technical failure in the rejected artifact is not merely that audio is absent; it is
that the encoded video has no timing substrate for narration at all. The visual state changes are
coarse static holds, so adding audio after the fact would still leave sentence/action sync mostly
fictional unless the overhaul is rebuilt around sentence-level audio durations.

## Acceptance State

Current KUN state: **HOLD**.

Reason: no new spin overhaul canary exists in `integrator/canaries/` at the time of this packet.
The rejected `0648` baseline fails the new order from the encoded artifact.

## Amendment — Provenance Correction to Primary Rejected Artifact

Timestamp: 2026-08-08 KST

After `reviews/REVIEW_BRIEFS.md` and `reviews/TORI_USER_WATCHED_ARTIFACT_CORRECTION.md` were
corrected, I inspected the primary artifact Duho actually watched:

`integrator/canaries/spin-method-canary-20260808T0204/spin-method-canary-20260808T0204.mp4`

The earlier KUN packet above was written from `0648` alone. That was wrong for user-watch
provenance. `0648` remains supplemental evidence only.

### Primary Encoded Artifact Verification

Direct checks on `0204`:

- SHA-256:
  `2b1db4974f9830161015828ae44bb617345db476375204f5f079a7fd0485ccc1`
- duration: 114.000 s
- size: 1,943,640 bytes
- streams: 1 total
- video: H.264, 1920x1080, 30 fps, 3420 frames
- audio: **none**

This confirms the core rejection from the encoded artifact itself: the exact watched file was
video-only, so intelligibility, clipping, delivered WPM, and audio-to-action timing cannot pass.

### Primary Rejected Grammar Observed

I inspected `integrator/canaries/spin-method-canary-20260808T0204/contact-sheet.jpg`. It has the
same rejected 11-card skeleton as `0648`, with card 05 using the earlier static funnel-bar figure
instead of the later `0648` readouts figure:

- title card with character still;
- paragraph/status card with character still;
- paragraph card;
- giant standalone `667,944` number card;
- static funnel-bar figure;
- equation card with paragraph explanation;
- static mirroring schematic;
- column-integrity paragraph card;
- bias-control paragraph card;
- verdict-withheld paragraph card with character still;
- close card with character still.

This contact sheet also shows internal JSON filenames as audience-facing citations, including
`T1_FUNNEL.json`, `STATUS.json`, `SOURCE_FREEZE.json`, and `T1C_COLUMN_INTEGRITY.json`. That is
explicitly banned by the overhaul order.

### Primary Frame/Animation Evidence

Scene detection against the encoded `0204` MP4 found substantive changes at:

| Detected change | Time (s) |
|---|---:|
| 1 | 6.000 |
| 2 | 16.000 |
| 3 | 33.000 |
| 4 | 45.000 |
| 5 | 56.000 |
| 6 | 68.000 |
| 7 | 88.000 |

These are hard state changes, not progressive builds derived from sentence-level audio. The primary
artifact therefore fails the same animation/timing diagnosis as the supplemental `0648` artifact.

### Reproducibility Correction

`0204/hashes.txt` records the MP4 hash above plus hashes for the storyboard, figures, source JSON,
contact sheet, and `../../candidate-workspace/tools/nm_paper_video.py`. As with `0648`, this is
receipt evidence but not a self-contained rebuild recipe because the renderer path is outside the
canary directory and no locked runtime/dependency manifest is present.

Additional discrepancy: the `0204` storyboard card durations sum to 108 s, while the encoded MP4 is
114 s. That makes the storyboard alone insufficient to reconstruct the encoded timing exactly.

### Amended KUN State

Current KUN state remains: **HOLD**.

Reason: the exact watched artifact is `0204`, not `0648`, and `0204` fails from encoded evidence:
video-only stream, rejected static-card grammar, internal filename citations, and coarse hard scene
changes. No new spin overhaul canary is present yet for the required audio/WPM/sentence-action
acceptance checks.

## Post-Build Encoded Review — spin-method-overhaul-canary-20260808T1312K

Timestamp: 2026-08-08 KST

I inspected the frozen candidate named in `reviews/POST_RENDER_REVIEW_ORDER.md`:

`integrator/canaries/spin-method-overhaul-canary-20260808T1312K/spin-method-overhaul-canary-20260808T1312K.mp4`

### Exact Artifact

Direct hash check against disk:

- SHA-256:
  `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`
- duration: 159.000 s
- size: 13,697,038 bytes
- video: H.264, 1920x1080, 30 fps, 4770 frames
- audio: AAC LC, 48000 Hz, mono, 129 kb/s

Full decode check:

- `ffmpeg -v error -i ... -f null -` completed with no decode errors.
- `freezedetect=n=0.001:d=8` completed with no freeze event reported.

### Audio, Loudness, Clipping

The encoded audio stream is real: one AAC mono stream exists for the full 159.000 s encode.

Measurements from the encoded MP4:

- `loudnorm`: integrated loudness `-20.31 LUFS`, true peak `-2.31 dBTP`, LRA `5.60`.
- `volumedetect`: mean volume `-21.4 dB`, max volume `-2.5 dB`.
- `astats`: peak level `-2.501636 dB`, RMS level `-21.364480 dB`, no NaNs/Infs/denormals.
- no clipping found; there is at least 2.3 dB true-peak headroom.

Intelligibility: the encode contains continuous speech-form narration at usable speech loudness,
with sentence-aligned subtitles and no decode/clipping failure. Limitation: this environment has no
local ASR or audio-playback transcript verifier installed (`whisper`/`whisper-cli` unavailable), so
I verified audibility/loudness and stream integrity from the encode but did not independently
transcribe the AAC by ear.

### WPM Re-Measurement

I re-counted the frozen v2 SRT text from the encoded candidate directory:

- spoken words: 299
- full encoded duration: 159.000 s
- first subtitle starts: 0.600 s
- last subtitle ends: 156.600 s
- first-speech-to-last-speech occupied span: 156.000 s

Delivered WPM:

- strict full-encode rate: `299 / 159.000 * 60 = 112.8 WPM`
- speech-span rate: `299 / 156.000 * 60 = 115.0 WPM`

Both are inside the required 105-125 WPM range. I cannot reproduce the reported `101.5 WPM` from
the frozen v2 SRT/timeline or the 159.0 s encoded duration.

### Sampled Sentence/Action Timing

These timings come from the v2 PCM-derived timeline in the candidate directory, with visual starts
quantized to encoded 30 fps frames and checked against decoded QA frames/contact sheet.

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "Can an apparent imbalance between clockwise and anticlockwise labels be separated from one introduced by the labeling process?" | 5.406000 | 5.400000 | -0.006000 |
| "The geometry reverses, and its apparent label inverts from clockwise to anticlockwise." | 33.835500 | 33.833333 | -0.002167 |
| "Three parallel readouts apply the spiral flag and two frozen thresholds; exact counts stay attached to their branches." | 71.199000 | 71.200000 | +0.001000 |
| "The sign would indicate which label is more numerous, but the predeclared asymmetry value remains withheld." | 90.816750 | 90.833333 | +0.016583 |
| "That standard makes the independent post-run verdict the next gate; the stored-direction frame and evidence, receipt, and referee checks must also meet the frozen rules." | 119.744250 | 119.733333 | -0.010917 |
| "Its gate-cleared answer is still missing; the scientific discriminant is not." | 151.752000 | 151.766667 | +0.014667 |

All sampled deltas are well inside the +/-0.3 s requirement. The recorded maximum over all 24
sentences is `0.016583 s`.

### Progressive Builds / Motion

The overhaul is not the old hard-cut card deck. Encoded evidence:

- motion QA sampled at 2 fps over 159 s: median absolute luma difference `0.1946`, maximum
  `15.0720`, longest near-unchanged run `6.5 s`;
- no freeze event of 8 s or longer was found by `freezedetect`;
- encoded contact sheet shows materially different sentence states, not a static paragraph deck;
- mirror sequence has five distinct decoded frame hashes at `34.125`, `35.282`, `36.728`,
  `38.174`, and `39.330` s.

The mirror section is genuine animation: the spiral visibly changes orientation across the five
sampled frames while the label reaches `appears ANTICLOCKWISE - ACW`. This is not a crossfade
between two still cards.

### Rebuild Receipts

Receipts present in the canary:

- `POST_ENCODE_FREEZE.json`
- `build_receipt.json`
- `source_manifest_v2.json`
- `audio_v2/synthesis_receipt.json`
- `audio_v2/timeline.json`
- local renderer `build.py`
- local audio assembly `assemble_audio_v2.py`
- preserved raw sentence audio under `audio_v2/raw/`
- preserved master audio `audio_v2/narration_master.wav`

I tested rebuild determinism without touching the frozen canary by copying the whole directory to
`/tmp/kun-rebuild-spin-method-overhaul-canary-20260808T1312K` and running:

`python3 build.py --render`

The rebuilt MP4 hash matched exactly:

`40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`

This satisfies KUN's reproducibility check for rebuilding from the preserved local inputs. The
remaining caveat is that fresh TTS regeneration from the provider route is not deterministic and
would require network/provider state; the reproducible path is from the recorded v2 audio files and
timeline, not from resynthesizing speech.

### Weakest Thing Found

The weakest technical point is the WPM/intelligibility measurement boundary. The candidate passes
WPM by both full-encode and speech-span measurements, but the build receipt's headline `115.0 WPM`
uses the first-speech-to-last-speech span, while a stricter full-encode measurement is `112.8 WPM`.
That is still compliant, but reviewers should cite the denominator. Also, absent local ASR/playback
verification, my intelligibility check is signal-level and subtitle-consistency evidence rather
than an independent transcript-by-ear check.

### Post-Build KUN State

Current KUN state: **PASS WITH CAVEAT**.

Reason: the exact frozen candidate hash matches; encoded audio exists, decodes, and is not clipped;
re-measured WPM is inside 105-125; sampled sentence/action deltas are within +/-0.3 s; progressive
animation and continuous mirror motion are present in decoded frames; the MP4 rebuilds to the same
hash from the preserved local inputs. Caveat: intelligibility was not independently ASR-transcribed
or human-listened in this tool environment.

## Corrected Post-Build Re-Run — Exact 1312K Candidate

Timestamp: 2026-08-08 KST

This section is appended to remove any ambiguity from the preserved pre-build record above. The
`0204` analysis and HOLD verdict describe the rejected baseline before a new canary existed. They
are not the current verdict on the candidate below.

Current artifact under review:

`integrator/canaries/spin-method-overhaul-canary-20260808T1312K/spin-method-overhaul-canary-20260808T1312K.mp4`

Exact hash re-run against disk:

`40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`

### Encoded Streams and Decode

`ffprobe` on the exact hash reports:

- duration: 159.000 s
- video: H.264, 1920x1080, 30 fps, 4770 frames
- audio: AAC LC, mono, 48000 Hz, 129 kb/s
- streams: exactly one video and exactly one audio stream

Full decode:

- `ffmpeg -v error -i ... -f null -` produced no errors.
- `freezedetect=n=0.001:d=8` produced no freeze events of 8 s or longer.

### Audio Intelligibility and Clipping

The encoded audio stream is present for the full MP4 and decodes cleanly. Signal-level checks:

- `loudnorm`: integrated loudness `-20.31 LUFS`, true peak `-2.31 dBTP`, LRA `5.60`.
- no clipping: peak remains below 0 dBFS/0 dBTP with about 2.3 dB headroom.
- AAC stream is mono 48 kHz and continuous; no decode faults.

Intelligibility adjudication: technically acceptable from the encode. The narration is carried by a
real speech stream with usable speech loudness and sentence-aligned captions. I still cannot claim a
fresh independent ear/ASR transcription from this tool environment because no local ASR/playback
verifier is available, but there is no encoded-media evidence of unintelligibility.

### Delivered WPM Adjudication

The frozen v2 SRT contains 299 spoken words.

Two denominators matter:

- Full MP4 runtime denominator: `299 / 159.000 * 60 = 112.8 WPM`.
- Delivered-speech span denominator, from first subtitle start `0.600 s` to last subtitle end
  `156.600 s`: `299 / 156.000 * 60 = 115.0 WPM`.

Correct method for the order's delivered WPM is the delivered-speech span, because the requirement
concerns narration pacing, not the lead/tail padding of the container. Lana's `115 WPM` is the
correct delivered-speech measurement. Even the stricter full-container measurement is `112.8 WPM`,
also inside the 105-125 floor/ceiling. The earlier `101.5 WPM` is not reproducible from this
candidate's frozen SRT plus 159.0 s runtime.

### Sentence-Level A/V Timing Samples

Measured from `audio_v2/timeline.json`, whose starts are PCM-derived and whose visual starts are
30 fps frame-quantized. All sampled deltas are far inside the +/-0.3 s requirement.

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "Can an apparent imbalance between clockwise and anticlockwise labels be separated from one introduced by the labeling process?" | 5.406000 | 5.400000 | -0.006000 |
| "The geometry reverses, and its apparent label inverts from clockwise to anticlockwise." | 33.835500 | 33.833333 | -0.002167 |
| "Three parallel readouts apply the spiral flag and two frozen thresholds; exact counts stay attached to their branches." | 71.199000 | 71.200000 | +0.001000 |
| "The sign would indicate which label is more numerous, but the predeclared asymmetry value remains withheld." | 90.816750 | 90.833333 | +0.016583 |
| "That standard makes the independent post-run verdict the next gate; the stored-direction frame and evidence, receipt, and referee checks must also meet the frozen rules." | 119.744250 | 119.733333 | -0.010917 |
| "Its gate-cleared answer is still missing; the scientific discriminant is not." | 151.752000 | 151.766667 | +0.014667 |

Maximum recorded delta over all 24 sentences: `0.016583 s`.

### Progressive Builds Versus Crossfades

Encoded QA reports 19/19 checks true. Motion evidence:

- sampled at 2 fps: 318 frames;
- median absolute luma difference: `0.1946`;
- maximum absolute luma difference: `15.0720`;
- longest near-unchanged run: `6.5 s`, under the 8 s freeze threshold;
- mirror unique frame hashes: `5`.

The mirror sequence is genuine animation, not a crossfade between stills: decoded frames at
`34.125`, `35.282`, `36.728`, `38.174`, and `39.330` s show distinct spiral states through the
horizontal inversion. The broader video also uses sentence-state builds and moving diagram elements,
not the rejected hard-cut paragraph-card grammar.

### Corrected Current KUN State

Current KUN state on the exact `1312K` candidate: **PASS WITH CAVEAT**.

Reason: exact hash verified; audio stream exists and decodes; no clipping; delivered WPM is 115.0
by the correct speech-span method; sentence/action timing is within +/-0.3 s; progressive builds and
mirror motion are genuine in the encoded artifact. Caveat remains limited to the absence of a local
independent ASR/ear transcription tool in this session.

## Superseding Introduction Rebuild Review — spin-method-overhaul-canary-20260808T1959K

Timestamp: 2026-08-09 KST

This section reviews the new introduction rebuild. It supersedes the `40804f86...` candidate for
current KUN purposes, while preserving all earlier evidence above as reviews of different artifacts.

Artifact under review:

`integrator/canaries/spin-method-overhaul-canary-20260808T1959K/spin-method-overhaul-canary-20260808T1959K.mp4`

### Exact Artifact

Direct hash check against disk:

`c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240`

Direct `ffprobe` on that file:

- container duration: 187.695 s
- size: 16,065,978 bytes
- video: H.264, 1920x1080, 30 fps, 5630 frames, 555 kb/s
- audio: AAC LC, mono, 48000 Hz, 120 kb/s
- streams: exactly one video and one audio stream

Full decode:

- `ffmpeg -v error -i ... -f null -` completed with no errors.
- `freezedetect=n=0.001:d=8` reported no freeze events of 8 s or longer.

### Audio, Intelligibility, Clipping

Encoded-audio measurements from this MP4:

- `loudnorm`: integrated loudness `-20.31 LUFS`, true peak `-2.30 dBTP`, LRA `6.30`.
- `volumedetect`: mean volume `-21.5 dB`, max volume `-2.3 dB`.
- `astats`: peak level `-2.307271 dB`, RMS level `-21.545316 dB`, no NaNs/Infs/denormals.

No clipping is present. The audio stream is real, continuous, decodes cleanly, and has usable speech
loudness.

Unlike the prior `1312K` review, this canary includes an encoded-introduction transcription receipt
for the new opening. It reports exact match, normalized similarity `1.0`, for:

`Spirals come in two handednesses. If one were genuinely more common across the sky, that would be a fact about the universe. But humans sorted the images, so an apparent excess could instead be a fact about the sorters. How do we tell the two apart?`

That is strong evidence that the new opening is intelligible and not clipped.

### Delivered WPM

The order's target is delivered narration pace. The correct denominator is therefore the delivered
speech span, not the full MP4 container including lead/tail and designed pauses.

Token-count caveat:

- If the sample number `667,944` is counted as one spoken numeric item, the SRT has 353 words.
- If `667,944` is split into `667` and `944`, the timeline tokenizer reports 354 words.

Measurements:

- full-container, 353-word denominator: `353 / 187.695 * 60 = 112.8 WPM`.
- delivered-speech span, 353-word denominator: first speech `0.600 s` to last speech `185.296 s`,
  so `353 / 184.696 * 60 = 114.7 WPM`.
- delivered-speech span, timeline tokenizer: `354 / 184.696 * 60 = 115.0 WPM`.

Adjudication: Lana's 115 WPM is correct under the build/timeline tokenizer, and the 353-word
speech-span measurement is 114.7 WPM. Both are inside the required 105-125 range. The user-measured
112.8 WPM is also correct if using full-container runtime, but that is not the delivered-speech
pacing denominator.

### Sampled Sentence/Action Timing

These timings come from `audio_v3/timeline.json`, with visual starts quantized to the 30 fps encode.
The new opening is sampled heavily because that is what changed.

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "Spirals come in two handednesses." | 0.600000 | 0.600000 | +0.000000 |
| "If one were genuinely more common across the sky, that would be a fact about the universe." | 3.918000 | 3.933333 | +0.015333 |
| "But humans sorted the images, so an apparent excess could instead be a fact about the sorters." | 9.420000 | 9.433333 | +0.013333 |
| "How do we tell the two apart?" | 15.834000 | 15.833333 | -0.000667 |
| "Can an apparent imbalance between clockwise and anticlockwise labels be separated from one introduced by the labeling process?" | 21.659083 | 21.666667 | +0.007583 |
| "Apply one decisive test to both worlds: mirror the same conceptual spiral horizontally." | 46.041250 | 46.033333 | -0.007917 |
| "The geometry reverses, and its apparent label inverts from clockwise to anticlockwise." | 52.071250 | 52.066667 | -0.004583 |
| "One mirror, two incompatible predicted behaviors: that difference is the scientific discriminant." | 68.673250 | 68.666667 | -0.006583 |
| "The sign would indicate which label is more numerous, but the predeclared asymmetry value remains withheld." | 116.598458 | 116.600000 | +0.001542 |
| "That standard makes the independent post-run verdict the next gate; the stored-direction frame and evidence, receipt, and referee checks must also meet the frozen rules." | 147.916583 | 147.900000 | -0.016583 |
| "Its gate-cleared answer is still missing; the scientific discriminant is not." | 180.183646 | 180.200000 | +0.016354 |

Maximum recorded action-start delta across all 27 sentences: `0.016583 s`. This passes the +/-0.3 s
requirement with a wide margin.

### New Opening Builds and Progressive Motion

Encoded evidence supports genuine animation, not crossfades between stills:

- introduction midpoint frame hashes are all distinct:
  - i01 `1.884 s`: `039caf027494...`
  - i02 `6.294 s`: `977f6dabb899...`
  - i03 `12.252 s`: `0cab4cdcb848...`
  - i04 `16.902 s`: `cb867c9c60ff...`
- encoded contact sheet shows the opening progressively adding the two handednesses, the
  conditional universe/sky branch, the sorter branch, and the question node;
- overall motion QA at 2 fps: 375 samples, median absolute luma difference `0.1835`, maximum
  `15.0058`, longest near-unchanged run `5.5 s`;
- encoded QA reports 26/26 checks true, including `four_move_introduction_is_first`,
  `opening_required_terms_present`, and the conditional universe/sorters clauses;
- mirror remains the longest section: `28.440 s`, versus introduction/motivation at `17.370 s`;
- mirror has five unique encoded frame hashes at `52.320`, `53.313`, `54.555`, `55.797`, and
  `56.791 s`.

The new opening is a real progressive build. The previously accepted mirror peak, discipline frame,
withheld estimator, method-design banner, and closing payoff remain present in the encoded contact
sheet and QA.

### Reproducibility and Receipt Check

Receipts are present for the v3 script, renderer, audio master, timeline, synthesis receipt,
encoded QA, subtitles, source manifest, and post-encode freeze. `POST_ENCODE_FREEZE_V3.json`
records the predecessor `40804f86...` as preserved.

I did not rerun a full deterministic rebuild for this `1959K` candidate during this amendment.

### Weakest Thing Found

The weakest thing is bookkeeping precision, not encoded behavior:

- word count is 353 or 354 depending on whether `667,944` is counted as one spoken numeric item or
  two numeric tokens;
- `ffprobe` reports 5630 video frames, while `build_receipt.json` records `frame_count: 5631`.

Neither issue breaks playback, sync, WPM compliance, or clipping checks, but the receipt should name
the counting convention and explain the one-frame video-count discrepancy.

### Current KUN State

Current KUN state on the superseding `1959K` candidate: **PASS WITH CAVEAT**.

Reason: exact hash verified; encoded audio exists, is intelligible by transcription receipt, and is
not clipped; delivered WPM is inside 105-125 by speech-span measurement; sampled A/V deltas pass the
0.3 s requirement including the new opening; and the introduction/mirror builds are genuine encoded
animation. Caveat: receipt bookkeeping has minor word-count and frame-count convention mismatches.

## Sibling Rollout Review — mzr-census-method-overhaul-canary-20260809T0214K

Timestamp: 2026-08-09 KST

Order checked: `HWAO_SIBLING_ROLLOUT_ORDER.md`. No sibling lane has `SOURCE_FREEZE.json`; this lane
therefore remains method-only and may not state a result.

Artifact requested by user:

`integrator/canaries/mzr-census-method-overhaul-canary-20260809T0214K/mzr-census-method-overhaul-canary-20260809T0214K.mp4`

### Exact Hash

**HOLD: hash mismatch.**

- user-specified SHA-256: `d940a7e8a8c126f462ed5cc36734459775d1da05c8e37bce8c83f85214f30d5d`
- disk SHA-256 measured by KUN: `0496435a9488bd946f7453989e7b9c5f4a528a691e698acab6b1e0d56e064536`
- `POST_ENCODE_FREEZE.json` and `RECEIPT.json` also record the disk hash `0496435a...`

I cannot pass this lane against the requested exact hash. The rest of this section is diagnostic
against the disk artifact only.

### Encoded A/V Diagnostics

- full decode: no ffmpeg decode errors.
- audio: AAC present; loudnorm `-21.51 LUFS`, true peak `-2.31 dBTP`; volumedetect mean `-22.8 dB`,
  max `-2.3 dB`; no clipping evidence.
- introduction ASR receipt: PASS, similarity `0.9925`.
- delivered WPM: 424 words over speech span 221.217 s = `115.0 WPM`.

Sampled A/V starts:

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "Archive metadata can make a table look ready for a mass-metallicity census in two very different ways." | 0.600000 | 0.600000 | +0.000000 |
| "If mass, gas-phase abundance, and redshift were genuinely joined within one galaxy sample..." | 8.767563 | 8.766667 | -0.000896 |
| "But an apparent three-axis match could instead be a fact about archive symbols and metadata..." | 18.783125 | 18.766667 | -0.016458 |
| "How do we tell a reachable table from an eligible one?" | 27.334688 | 27.333333 | -0.001354 |
| "Counting metadata hits cannot settle that question..." | 34.517562 | 34.533333 | +0.015771 |
| "Only a same-table evidence chain can support eligibility..." | 86.946687 | 86.933333 | -0.013354 |
| "Now we have a method that can tell those explanations apart..." | 215.697396 | 215.700000 | +0.002604 |

Maximum recorded sentence/action delta: `0.016458 s`, inside +/-0.3 s.

### Animation and Rebuild

Intro and peak frame hashes are distinct across sampled frames, so this is not merely one still
crossfaded:

- intro hash prefixes: `ebca50f03926`, `e82fc809ec57`, `14a90b9d8619`, `45c744e037fc`
- peak hash prefixes: `41da4fc9c9d7`, `8faf3fad9776`, `2a7b5c1208c2`, `58a10bd7f3da`, `448810400146`

However, strict encoded `freezedetect=n=0.001:d=8` reports long unchanged holds, including 10.0 s,
12.0 s, and 13.93 s runs. That conflicts with the rollout expectation that nothing remain unchanged
beyond about 8 s.

Rebuild: **not independently reproducible from the canary directory alone.** `build_receipt.json`
records a `shared sibling renderer` hash, but no renderer script is present in this canary directory.
I could verify receipts, not rebuild to the same hash from local recorded inputs.

### Weakest Thing

The weakest thing is the artifact identity failure: the MP4 on disk does not match the exact hash
given for review. Secondary weaknesses are missing self-contained rebuild inputs and long freeze
runs.

### KUN State

**HOLD.** Media diagnostics on the disk artifact are mostly good, but the requested hash is absent,
and this is not independently rebuildable from local recorded inputs.

## Sibling Rollout Review — fesc-method-overhaul-canary-20260809T0227K

Timestamp: 2026-08-09 KST

Order checked: `HWAO_SIBLING_ROLLOUT_ORDER.md`. No `SOURCE_FREEZE.json` is present; this remains
method-only and may not state a result.

### Exact Artifact

- path: `integrator/canaries/fesc-method-overhaul-canary-20260809T0227K/fesc-method-overhaul-canary-20260809T0227K.mp4`
- SHA-256 verified: `b900383142c0ddeadc32247282f511798d8c4a449cbf5c7b7aef0a56aff4c168`
- full decode: no ffmpeg decode errors.

### Encoded A/V

- audio: AAC present; loudnorm `-21.48 LUFS`, true peak `-2.31 dBTP`; volumedetect mean `-22.9 dB`,
  max `-2.3 dB`; no clipping evidence.
- introduction ASR receipt: PASS, similarity `1.0`.
- delivered WPM: 448 words over speech span 233.739 s = `115.0 WPM`.

Sampled A/V starts:

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "At each redshift, a photon budget can look open..." | 0.600000 | 0.600000 | +0.000000 |
| "If galaxies were genuinely leaking too little ionizing radiation..." | 11.207437 | 11.200000 | -0.007437 |
| "But an apparent shortfall could instead be a fact about low-redshift proxy transport..." | 19.870875 | 19.866667 | -0.004208 |
| "How do we tell a source shortfall from an assumption shortfall?" | 30.046312 | 30.033333 | -0.012979 |
| "One redshift cannot settle that question..." | 38.321625 | 38.333333 | +0.011708 |
| "The inferred side transports both proxy calibrations..." | 81.467250 | 81.466667 | -0.000583 |
| "Now we have a test that can separate those explanations..." | 228.339125 | 228.333333 | -0.005792 |

Maximum recorded sentence/action delta: `0.012979 s`, inside +/-0.3 s.

### Animation and Rebuild

Intro and peak frame hashes are distinct:

- intro hash prefixes: `ed51ac64f404`, `9a4e8cd50013`, `1096aa5f4101`, `a4a191c4d34a`
- peak hash prefixes: `7e3aab6d5472`, `ed6652265f2e`, `38c97d4eef60`, `24d4faa66c92`, `9c4b2df4d76d`

This supports genuine state/build changes rather than one still. But strict `freezedetect` found
unchanged runs of 8.33 s, 8.67 s, 10.17 s, 8.27 s, 11.63 s, and 10.87 s. That is the main animation
weakness.

Rebuild: receipts exist for spec, timeline, audio, encoded QA, and source manifest, but the renderer
is recorded only as `shared sibling renderer` with hash `d14a5643...`; no local renderer script is
present in the canary. I did not and cannot rebuild this MP4 from the canary directory alone.

### Claim Boundary

Narration and OCR repeatedly withhold curve values, crossings, signs, and galaxy claims. I did not
find a result value in the sampled narration. The visible phrase "source shortfall" is conditional
in the opening question, but it is strong language for an unfrozen lane and should stay under Lana/Tori
watch.

### Weakest Thing

The weakest thing is reproducibility: the canary depends on an external shared renderer not included
with the recorded local inputs. Second weakest is the strict freeze detector finding long static
holds.

### KUN State

**HOLD on reproducibility; media/sync PASS.** The encoded A/V and timing pass, but KUN cannot certify
same-hash rebuild from recorded local inputs.

## Sibling Rollout Review — brightend-method-overhaul-canary-20260809T0235K

Timestamp: 2026-08-09 KST

Order checked: `HWAO_SIBLING_ROLLOUT_ORDER.md`. No `SOURCE_FREEZE.json` is present; this remains
method-only and may not state a result.

### Exact Artifact

- path: `integrator/canaries/brightend-method-overhaul-canary-20260809T0235K/brightend-method-overhaul-canary-20260809T0235K.mp4`
- SHA-256 verified: `9a137c61011a3d9629c96ebbf365955295e11082cededa325ceb38f1ce268a2f`
- full decode: no ffmpeg decode errors.

### Encoded A/V

- audio: AAC present; loudnorm `-21.38 LUFS`, true peak `-2.31 dBTP`; volumedetect mean `-22.6 dB`,
  max `-2.3 dB`; no clipping evidence.
- introduction ASR receipt: PASS, similarity `0.9977`.
- delivered WPM: timeline count 431 words over speech span 224.870 s = `115.0 WPM`.
- SRT tokenization counts 432 words, giving `115.3 WPM`; both pass 105-125.

Sampled A/V starts:

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "A published bright-end summary can lack a reconstructible object record..." | 0.600000 | 0.600000 | +0.000000 |
| "If the underlying object rows were genuinely absent from public archives..." | 10.195187 | 10.200000 | +0.004812 |
| "But an apparent archival gap could instead be a fact about case-sensitive names..." | 19.310375 | 19.300000 | -0.010375 |
| "How do we tell missing data from missed data?" | 29.073563 | 29.066667 | -0.006896 |
| "Counting catalogues cannot settle that question..." | 36.349063 | 36.333333 | -0.015729 |
| "Only records with a defensible magnitude convention..." | 77.570125 | 77.566667 | -0.003458 |
| "Now we have a method that can tell those explanations apart..." | 219.301562 | 219.300000 | -0.001562 |

Maximum recorded sentence/action delta: `0.015729 s`, inside +/-0.3 s.

### Animation and Rebuild

Intro and peak frame hashes are distinct:

- intro hash prefixes: `214879b1e9d8`, `85d1e1ed495f`, `609ebe31164d`, `c3aa2e09b707`
- peak hash prefixes: `c1ef7f706260`, `70f5508bbd2e`, `e8d6051c2445`, `afb298929538`, `77817ae9e63c`

This supports genuine builds. But strict `freezedetect` found many unchanged runs: 8.77 s, 9.13 s,
9.77 s, 9.97 s, 12.10 s, 8.23 s, 8.33 s, 8.10 s, and 13.80 s. This is the worst static-hold profile
among the four.

Rebuild: receipts exist, but the renderer is an external `shared sibling renderer` hash
`d14a5643...`; no local renderer script is present. I could not rebuild to the same hash from local
canary inputs.

### Claim Boundary

The narration withholds catalogue totals, object counts, archival gap, and luminosity-function pace.
The visible/narrated "missing data" language is framed as a question/possibility, not a result, but
without a source freeze it remains a boundary phrase to watch.

### Weakest Thing

The weakest thing is the long static holds: the encoded video has multiple strict-freeze intervals
above 8 s despite aggregate motion QA passing. Rebuild incompleteness is also unresolved.

### KUN State

**HOLD on reproducibility/static-hold caveat; media/sync PASS.** Encoded A/V and timing pass, but
KUN cannot certify same-hash rebuild from local inputs, and the strict freeze detector contradicts
the intended no-long-hold grammar.

## Sibling Rollout Review — mzr-anchor-method-overhaul-canary-20260809T0245K

Timestamp: 2026-08-09 KST

Order checked: `HWAO_SIBLING_ROLLOUT_ORDER.md`. No `SOURCE_FREEZE.json` is present; this remains
method-only and may not state a result.

### Exact Artifact

- path: `integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T0245K/mzr-anchor-method-overhaul-canary-20260809T0245K.mp4`
- SHA-256 verified: `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970`
- full decode: no ffmpeg decode errors.

### Encoded A/V

- audio: AAC present; loudnorm `-20.92 LUFS`, true peak `-2.30 dBTP`; volumedetect mean `-21.9 dB`,
  max `-2.3 dB`; no clipping evidence.
- introduction ASR receipt: PASS, similarity `0.9988`.
- delivered WPM: 415 words over speech span 216.522 s = `115.0 WPM`.

Sampled A/V starts:

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "At high redshift, metallicity relations can disagree..." | 0.600000 | 0.600000 | +0.000000 |
| "If the relation genuinely evolved..." | 10.574917 | 10.566667 | -0.008250 |
| "But an apparent offset could instead be a fact about strong-line recipes..." | 17.357833 | 17.366667 | +0.008833 |
| "How do we tell evolution from calibration?" | 26.276750 | 26.266667 | -0.010083 |
| "Counting metallicity rows cannot settle that question..." | 32.158729 | 32.166667 | +0.007937 |
| "That temperature becomes a direct oxygen abundance only when..." | 72.861458 | 72.866667 | +0.005208 |
| "Now we have a method that can separate those explanations..." | 210.545729 | 210.533333 | -0.012396 |

Maximum recorded sentence/action delta: `0.016250 s`, inside +/-0.3 s.

### Animation and Rebuild

Intro and peak frame hashes are distinct:

- intro hash prefixes: `e2c2ffd3c65f`, `137eafa062e8`, `d9698b119690`, `32195ae4b556`
- peak hash prefixes: `d939c8c614e7`, `0b0f5091339f`, `0e49db03f8c4`, `bd98dcbbcbfb`, `ed9efb35b4ec`

This supports genuine builds. Strict `freezedetect` still reports 8.77 s, 8.93 s, 8.60 s, 12.70 s,
and 12.73 s unchanged runs.

Rebuild: receipts exist, but the renderer is an external `shared sibling renderer` hash
`7d42ea80...`; no local renderer script is present. I could not rebuild to the same hash from local
canary inputs.

### Claim Boundary

**HOLD-level claim drift risk:** OCR shows the visible phrase `A metallicity offset has two
explanations` repeated throughout the encoded frames. The narration usually says "apparent offset"
or withholds offset sign/value/verdict, but the persistent visual title can be read as asserting an
offset exists. With no `SOURCE_FREEZE.json`, that is drift toward a substantive claim.

### Weakest Thing

The weakest thing is the visual claim-boundary phrase `A metallicity offset has two explanations`.
Secondary weaknesses are missing self-contained rebuild inputs and strict-freeze runs above 8 s.

### KUN State

**HOLD.** Encoded A/V and timing pass, but no-source-freeze claim drift in visible text plus incomplete
local rebuild evidence prevent KUN authorization.

## Sibling Hash Correction Re-Run — mzr-census-method-overhaul-canary-20260809T0214K

Timestamp: 2026-08-09 KST

Correction read: `reviews/HWAO_HASH_CORRECTION_20260809.md`.

The earlier KUN refusal against `d940a7e8...` stands as the right response to a stale hash. Hwao now
confirms the watcher hashed `mzr-census` mid-write. The finished artifact is:

`integrator/canaries/mzr-census-method-overhaul-canary-20260809T0214K/mzr-census-method-overhaul-canary-20260809T0214K.mp4`

Corrected SHA-256, re-run by KUN against disk:

`0496435a9488bd946f7453989e7b9c5f4a528a691e698acab6b1e0d56e064536`

This matches the lane's own `POST_ENCODE_FREEZE.json`, which records the same hash.

### Corrected Encoded A/V

Direct `ffprobe`:

- container duration: 224.233333 s
- size: 9,421,699 bytes
- video: H.264, 1920x1080, 30 fps, 6727 frames
- audio: AAC LC, mono, 48000 Hz, 117 kb/s

Full decode:

- `ffmpeg -v error -i ... -f null -` completed with no errors.

Audio:

- `loudnorm`: integrated loudness `-21.51 LUFS`, true peak `-2.31 dBTP`, LRA `7.80`.
- prior `volumedetect`: mean `-22.8 dB`, max `-2.3 dB`.
- no clipping evidence.
- introduction ASR receipt: PASS, similarity `0.9925`.

Delivered WPM:

- 424 words over speech span 221.217395833 s = `115.0 WPM`.
- inside the 105-125 target.

Sampled A/V starts:

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "Archive metadata can make a table look ready for a mass-metallicity census in two very different ways." | 0.600000 | 0.600000 | +0.000000 |
| "If mass, gas-phase abundance, and redshift were genuinely joined within one galaxy sample..." | 8.767563 | 8.766667 | -0.000896 |
| "But an apparent three-axis match could instead be a fact about archive symbols and metadata..." | 18.783125 | 18.766667 | -0.016458 |
| "How do we tell a reachable table from an eligible one?" | 27.334688 | 27.333333 | -0.001354 |
| "Counting metadata hits cannot settle that question..." | 34.517562 | 34.533333 | +0.015771 |
| "Abundance must describe an element ratio in gas..." | 76.667125 | 76.666667 | -0.000458 |
| "Only a same-table evidence chain can support eligibility..." | 86.946687 | 86.933333 | -0.013354 |
| "Now we have a method that can tell those explanations apart..." | 215.697396 | 215.700000 | +0.002604 |

Maximum recorded sentence/action delta: `0.016458 s`, inside +/-0.3 s.

### Corrected Animation/Rebuild Finding

Aggregate motion QA passes: 448 sampled frames at 2 fps, mean absolute frame difference `0.4462`,
max `11.7477`, and 27/27 encoded QA checks true. Introduction and peak frame hash prefixes remain
distinct as recorded in the earlier sibling section.

Two KUN caveats remain:

- strict `freezedetect=n=0.001:d=8` found long unchanged holds, including 10.0 s, 12.0 s, and
  13.93 s runs;
- the canary still is not independently rebuildable from local canary inputs because
  `build_receipt.json` names a `shared sibling renderer` hash but no renderer script is present in
  the canary directory.

### Corrected mzr-census KUN State

**HOLD on reproducibility/static-hold caveat; media/sync PASS.**

Reason: artifact identity is now corrected and passes disk==freeze hash verification; encoded audio,
WPM, ASR, and sentence/action timing pass. KUN still cannot certify same-hash rebuild from the local
recorded inputs, and strict freeze detection conflicts with the no-long-hold grammar.

## Sibling Rollout Current Summary After Hash Correction

Timestamp: 2026-08-09 KST

- `mzr-census`: **HOLD on reproducibility/static-hold caveat; media/sync PASS**. Corrected hash
  `0496435a...` now verified.
- `fesc`: **HOLD on reproducibility; media/sync PASS**.
- `brightend`: **HOLD on reproducibility/static-hold caveat; media/sync PASS**.
- `mzr-anchor`: **HOLD** due to visible no-source-freeze claim drift plus incomplete rebuild evidence.

All four have real AAC narration, pass speech-span WPM, pass sampled sentence/action timing, and
decode cleanly. None has `SOURCE_FREEZE.json`; none is authorized to state a result.

## Current-Candidate Sweep Amendment - 2026-08-09 14:48:42 KST

Scope note: this section supersedes KUN's stale-hash sibling sweep findings only for the four
current candidate paths named below. Earlier evidence remains intact because it reviewed different
encoded artifacts. I did not bind `mzr-anchor-1300K`; it has no `POST_ENCODE_FREEZE.json`.

### mzr-census Current Candidate - 20260809T0320K

Artifact:

- path: `integrator/canaries/mzr-census-method-overhaul-canary-20260809T0320K/mzr-census-method-overhaul-canary-20260809T0320K.mp4`
- requested SHA-256: `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b`
- disk SHA-256: `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b`
- `POST_ENCODE_FREEZE.json`: matches disk hash.

Encoded media:

- full decode: PASS (`ffmpeg -v error -i ... -f null -`, exit 0).
- audio stream: AAC, mono, 48000 Hz.
- intelligibility: encoded introduction ASR PASS, similarity `1.000000`.
- loudness/clipping: integrated loudness `-21.65 LUFS`, true peak `-2.32 dBTP`, LRA `9.50`;
  `volumedetect` max volume `-2.4 dB`. I see no clipping evidence.

Delivered WPM:

- method: lane `spec.json`/timeline word count divided by delivered speech span, excluding the
  encoded lead/trailer non-speech, not full container duration.
- 435 words over 226.956520833 s = `115.000000 WPM`, inside 105-125.

Sampled sentence/action starts:

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "Archive metadata can make a table look ready for a mass-metallicity census in two very different ways." | 0.600000 | 0.600000 | +0.000000 |
| "If mass, gas-phase abundance, and redshift were genuinely joined within one galaxy sample..." | 9.204771 | 9.200000 | -0.004771 |
| "But an apparent three-axis match could instead be a fact about archive symbols and metadata..." | 19.897542 | 19.900000 | +0.002458 |
| "How do we tell a reachable table from an eligible one?" | 29.174312 | 29.166667 | -0.007646 |
| "Counting metadata hits cannot settle that question..." | 37.633125 | 37.633333 | +0.000208 |
| "Abundance must describe an element ratio in gas..." | 80.690250 | 80.700000 | +0.009750 |
| "Only a same-table evidence chain can support eligibility..." | 91.887021 | 91.900000 | +0.012979 |
| "Now we have a method that can tell those explanations apart..." | 221.196521 | 221.200000 | +0.003479 |

Maximum sampled/recorded delta I measured: `0.016292 s`, inside +/-0.3 s.

Animation and rebuild:

- encoded QA reports 28/28 checks PASS, mean absolute frame difference `0.4406`, max `11.7506`,
  and no sampled near-unchanged run.
- strict `freezedetect=n=0.001:d=8` still reports long low-motion holds, including
  9.233333-19.900000 s (`10.666667 s`), 47.900000-59.433333 s (`11.533333 s`),
  199.533333-212.600000 s (`13.066667 s`), and an end hold beginning 221.200000 s.
- This is not merely a crossfade between stills: the renderer generates element-level frames and the
  encoded motion metric is nonzero. The weakness is that several built states settle into long
  nearly static diagram holds under a very strict pixel-change threshold.
- rebuild-from-inputs: PASS. I copied the canary to `/tmp/kun-current-rebuild-20260809T2/` and ran
  `python3 integrator/canaries/mzr-census-method-overhaul-canary-20260809T0320K/provenance/render.py <tmp-candidate> --render`;
  rebuilt hash was exactly `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b`.

Weakest thing: strict freeze detection still sees sentence-length low-motion plateaus despite the
frame-by-frame renderer and passing encoded QA motion metric.

KUN state: **PASS WITH ANIMATION CAVEAT**. Media, sync, WPM, hash, full decode, and reproducible
same-hash rebuild pass. No `SOURCE_FREEZE.json` exists, so this remains method-only and may not state
a scientific result.

### fesc Current Candidate - 20260809T1345K

Artifact:

- path: `integrator/canaries/fesc-method-overhaul-canary-20260809T1345K/fesc-method-overhaul-canary-20260809T1345K.mp4`
- requested SHA-256: `acfb7fee70d5a131d4a44e8962cfe3fe3cd22104bf9cf8fa00bbbd6c2c00cbc0`
- disk SHA-256: `acfb7fee70d5a131d4a44e8962cfe3fe3cd22104bf9cf8fa00bbbd6c2c00cbc0`
- `POST_ENCODE_FREEZE.json`: matches disk hash.

Encoded media:

- full decode: PASS.
- audio stream: AAC, mono, 48000 Hz.
- intelligibility: encoded introduction ASR PASS, similarity `1.000000`.
- loudness/clipping: integrated loudness `-20.24 LUFS`, true peak `-2.30 dBTP`, LRA `7.50`;
  `volumedetect` max volume `-2.3 dB`. I see no clipping evidence.

Delivered WPM:

- 448 words over 233.739125 s delivered speech span = `115.000003 WPM`, inside 105-125.

Sampled sentence/action starts:

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "At each redshift, a photon budget can look open..." | 0.600000 | 0.600000 | +0.000000 |
| "If the required escape fraction genuinely rises beyond what proxy-inferred leakage can supply..." | 11.569417 | 11.566667 | -0.002750 |
| "But an apparent shortfall could instead be a fact about transported low-redshift proxies..." | 20.522833 | 20.533333 | +0.010500 |
| "How do we tell a budget failure from a proxy failure?" | 30.028250 | 30.033333 | +0.005083 |
| "The discriminant is not a single redshift..." | 37.934333 | 37.933333 | -0.001000 |
| "The method therefore carries both arms through the same redshift grid..." | 82.684667 | 82.700000 | +0.015333 |
| "Only that paired propagation can separate a rising requirement..." | 93.654083 | 93.666667 | +0.012583 |
| "Now we have a method that can separate a real photon-budget tension..." | 227.763125 | 227.766667 | +0.003542 |

Maximum sampled/recorded delta I measured: `0.015333 s`, inside +/-0.3 s.

Animation and rebuild:

- encoded QA reports 28/28 checks PASS, mean absolute frame difference `0.3953`, max `11.6441`,
  and no sampled near-unchanged run.
- strict `freezedetect=n=0.001:d=8` reports long low-motion holds, including
  11.600000-20.533333 s (`8.933333 s`), 48.233333-59.300000 s (`11.066667 s`),
  208.333333-219.133333 s (`10.800000 s`), and an end hold beginning 227.766667 s.
- The progressive builds are genuine rendered animation, not just crossfaded still cards, but the
  final state of several panels remains visually static for long stretches.
- rebuild-from-inputs: PASS. Tmp-copy render produced exact hash
  `acfb7fee70d5a131d4a44e8962cfe3fe3cd22104bf9cf8fa00bbbd6c2c00cbc0`.

Weakest thing: the strict-freeze plateaus are visible risk; the method animation often finishes
early and then rests while narration continues.

KUN state: **PASS WITH ANIMATION CAVEAT**. No `SOURCE_FREEZE.json` exists, so any result-bearing FESC
claim remains unauthorized.

### brightend Current Candidate - 20260809T1345K

Artifact:

- path: `integrator/canaries/brightend-method-overhaul-canary-20260809T1345K/brightend-method-overhaul-canary-20260809T1345K.mp4`
- requested SHA-256: `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8`
- disk SHA-256: `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8`
- `POST_ENCODE_FREEZE.json`: matches disk hash.

Encoded media:

- full decode: PASS.
- audio stream: AAC, mono, 48000 Hz.
- intelligibility: encoded introduction ASR PASS, similarity `0.997722`.
- loudness/clipping: integrated loudness `-20.05 LUFS`, true peak `-2.29 dBTP`, LRA `8.00`;
  `volumedetect` max volume `-2.3 dB`. I see no clipping evidence.

Delivered WPM:

- 431 words over 224.8695625 s delivered speech span = `115.000001 WPM`, inside 105-125.

Sampled sentence/action starts:

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "A published bright-end summary can lack a reconstructible object record..." | 0.600000 | 0.600000 | +0.000000 |
| "If those records were genuinely absent, that would be a fact about archive preservation..." | 8.961250 | 8.966667 | +0.005417 |
| "But an apparent archival gap could instead be a fact about case-sensitive names..." | 17.706500 | 17.700000 | -0.006500 |
| "How do we tell a missing object from a missed object?" | 27.099750 | 27.100000 | +0.000250 |
| "The discriminant is not whether one query returns a table." | 33.989417 | 34.000000 | +0.010583 |
| "The method therefore runs both discovery routes..." | 75.418833 | 75.433333 | +0.014500 |
| "Only object-level projection can separate a real archive absence..." | 85.820083 | 85.833333 | +0.013250 |
| "Now we have a method that can tell those explanations apart..." | 219.253562 | 219.266667 | +0.013104 |

Maximum sampled/recorded delta I measured: `0.014500 s`, inside +/-0.3 s.

Animation and rebuild:

- encoded QA reports 28/28 checks PASS, mean absolute frame difference `0.4115`, max `11.9456`,
  and no sampled near-unchanged run.
- strict `freezedetect=n=0.001:d=8` reports long low-motion holds, including
  44.400000-56.133333 s (`11.733333 s`), 200.000000-210.633333 s (`10.633333 s`),
  210.633333-219.266667 s (`8.633333 s`), and an end hold beginning 219.266667 s.
- The opening and builds are genuine rendered animation, but several states settle into static holds
  after the build completes.
- rebuild-from-inputs: PASS. Tmp-copy render produced exact hash
  `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8`.

Weakest thing: this lane has the longest current strict-freeze segment I measured among the three
new rebuilt lanes (`11.733333 s`), so the animation grammar is its softest point.

KUN state: **PASS WITH ANIMATION CAVEAT**. No `SOURCE_FREEZE.json` exists, so no bright-end result is
authorized.

### mzr-anchor Current Candidate - 20260809T0245K

Artifact:

- path: `integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T0245K/mzr-anchor-method-overhaul-canary-20260809T0245K.mp4`
- requested SHA-256: `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970`
- disk SHA-256: `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970`
- `POST_ENCODE_FREEZE.json`: matches disk hash.

Encoded media:

- full decode: PASS.
- audio stream: AAC, mono, 48000 Hz.
- intelligibility: encoded introduction ASR PASS, similarity `0.998761`.
- loudness/clipping: integrated loudness `-20.92 LUFS`, true peak `-2.30 dBTP`, LRA `7.30`;
  `volumedetect` max volume `-2.3 dB`. I see no clipping evidence.

Delivered WPM:

- 415 words over 216.521729167 s delivered speech span = `115.000005 WPM`, inside 105-125.

Sampled sentence/action starts:

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "At high redshift, metallicity relations can disagree..." | 0.600000 | 0.600000 | +0.000000 |
| "If the relation genuinely evolved..." | 10.574917 | 10.566667 | -0.008250 |
| "But an apparent offset could instead be a fact about strong-line recipes..." | 17.357833 | 17.366667 | +0.008833 |
| "How do we tell evolution from calibration?" | 26.276750 | 26.266667 | -0.010083 |
| "The discriminant is not an offset value." | 32.158729 | 32.166667 | +0.007937 |
| "The source ledger preserves enumeration..." | 72.861458 | 72.866667 | +0.005208 |
| "Only a common-scale comparison can separate enrichment..." | 83.004375 | 83.000000 | -0.004375 |
| "Now we have a method that can separate those explanations..." | 210.545729 | 210.533333 | -0.012396 |

Maximum sampled/recorded delta I measured: `0.016250 s`, inside +/-0.3 s.

Animation and rebuild:

- encoded QA reports 27/27 checks PASS, mean absolute frame difference `0.4396`, max `11.8978`,
  and no sampled near-unchanged run.
- strict `freezedetect=n=0.001:d=8` reports long low-motion holds, including
  40.766667-53.466667 s (`12.700000 s`), 189.666667-202.400000 s (`12.733333 s`), and an
  end hold beginning 210.566667 s.
- rebuild-from-inputs: HOLD. The 0245K canary package has no executable `provenance/render.py`
  counterpart, so I cannot reproduce the hash from lane-local recorded inputs. I intentionally did
  not bind the later `mzr-anchor-1300K` directory because the order says it was mid-build and lacks
  `POST_ENCODE_FREEZE.json`.

Semantic/no-freeze issue:

- This lane still visibly titles the piece `A metallicity offset has two explanations` in
  `encoded_qa/ocr.txt` and `spec.json`.
- With no `SOURCE_FREEZE.json`, even a non-numeric phrase that presupposes an offset is claim drift.
  The narration later withholds value/sign/result, but the title is the first-viewport frame and is
  stronger than a method-only question.

Weakest thing: visible claim drift in the title, not the media encode. Rebuild provenance is also
incomplete.

KUN state: **HOLD**. Audio, WPM, full decode, and A/V timing pass; method-only authorization and
rebuild-from-inputs do not.

## mzr-anchor Current Candidate Amendment - 2026-08-09 14:56 KST

This section reviews only
`integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T1406K/` and supersedes KUN's
0245K mzr-anchor finding for the current candidate set. The 0245K caveat remains historically
accurate for that older artifact: 0245K lacked lane-local provenance render scripts, so KUN could
not rebuild it from its own package. The 1406K candidate is different on that point and includes
`provenance/render.py`.

I did not bind `mzr-anchor-1300K`. Per the board amendment, that was the same build caught
mid-write before freeze, not an independently reviewable frozen candidate.

Order read: `HWAO_SIBLING_BOARD_VERDICT.md`, including `AMENDMENT 14:36 KST`.

### Identity and Freeze

Artifact:

- path: `integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T1406K/mzr-anchor-method-overhaul-canary-20260809T1406K.mp4`
- requested SHA-256: `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`
- disk SHA-256: `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`
- `POST_ENCODE_FREEZE.json`: `video_sha256` is the same `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`.
- build receipt: same output hash, `output_bytes` `9722369`, `video_reportable_now: false`.

Container/media:

- `ffprobe`: 219.533333 s container, 9,722,369 bytes.
- video: H.264, 1920x1080, 30 fps, 6,586 frames.
- audio: AAC LC, mono, 48000 Hz, 10,292 AAC frames.
- full decode: PASS (`ffmpeg -v error -i ... -f null -`, exit 0).

### Audio and WPM

Audio stream is real and intelligible:

- encoded introduction ASR similarity: `0.9987608426270136`.
- loudnorm: integrated loudness `-20.92 LUFS`, true peak `-2.30 dBTP`, LRA `7.30`.
- volumedetect: mean volume `-21.9 dB`, max volume `-2.3 dB`.
- no clipping evidence.

Delivered WPM by speech-span method:

- narration source: `spec.json` / `audio/timeline.json`, not `narration_script.json`.
- 22 sentences, 415 words.
- delivered speech span: `216.52172916666666 s`.
- WPM: `115.000005`, inside the 105-125 target.

### Sentence/Action Sync

Sampled starts from the encoded artifact/timeline:

| Sentence | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| "At high redshift, metallicity relations can disagree..." | 0.600000 | 0.600000 | +0.000000 |
| "If the relation genuinely evolved..." | 10.574917 | 10.566667 | -0.008250 |
| "But an apparent offset could instead be a fact about strong-line recipes..." | 17.357833 | 17.366667 | +0.008833 |
| "How do we tell evolution from calibration?" | 26.276750 | 26.266667 | -0.010083 |
| "Counting metallicity rows cannot settle that question..." | 32.158729 | 32.166667 | +0.007937 |
| "Even an auroral-line label is insufficient..." | 40.765646 | 40.766667 | +0.001021 |
| "The discriminating chain begins with a source-published auroral flux..." | 53.439625 | 53.433333 | -0.006292 |
| "That temperature becomes a direct oxygen abundance..." | 72.861458 | 72.866667 | +0.005208 |
| "Only after seam, lensing, and scale controls pass..." | 91.659292 | 91.666667 | +0.007375 |
| "The estimator is a common-scale direct-abundance difference..." | 127.846167 | 127.833333 | -0.012833 |
| "Scale uncertainty travels beside statistical uncertainty..." | 136.717083 | 136.733333 | +0.016250 |
| "Now we have a method that can separate those explanations..." | 210.545729 | 210.533333 | -0.012396 |

Maximum measured sentence/action start delta: `0.016250 s`, inside the +/-0.3 s requirement.

### Frame Inspection and Animation

Text-level check:

- `spec.json` icon counts from `params.icon`: `{"anchor": 8}`.
- `icon: "curve"` count: zero.

Frame-level check:

- I extracted sampled frames under
  `integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T1406K/_tmp_kun_frame_review_20260809T1450K/`,
  including the fesc-defect timestamps 5.052, 15.013, 24.243, 31.816, 42.050, and 51.592 s.
- Visual inspection of `kun-sampled-frame-sheet.jpg` finds no rising/falling crossing-curve glyph.
  The repeated glyph is an anchor-like mark, not an order/intersection curve.
- The frames show method diagrams with banners such as `METHOD DESIGN · NO MEASURED VALUE`,
  `NO SOURCE FREEZE · NO NUMBER CARD`, `VALUE WITHHELD`, and `METHOD DESIGNED · VALUE AND SIGN
  WITHHELD`.

Animation caveat:

- encoded QA reports 28/28 checks PASS and nonzero motion metrics.
- strict `freezedetect=n=0.001:d=8` still reports long low-motion holds:
  17.366667-26.300000 s (`8.933333 s`), 40.766667-53.466667 s (`12.700000 s`),
  189.666667-202.400000 s (`12.733333 s`), plus an end hold beginning 210.566667 s.
- I classify this as genuine rendered animation that often settles into static holds, not as a
  crossfade-only deck.

### Deterministic Rebuild

Scratch and receipts were kept under the lane directory as ordered:

- scratch root:
  `integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T1406K/_tmp_kun_rebuild_20260809T1452K/`
- copied candidate:
  `_tmp_kun_rebuild_20260809T1452K/candidate/`
- copy command excluded `_tmp_*` so review/rebuild scratch did not recursively enter the rebuild
  input tree.

Command run:

`python3 integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T1406K/provenance/render.py <lane>/_tmp_kun_rebuild_20260809T1452K/candidate --render`

Rebuild result:

- rebuilt SHA-256:
  `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`
- rebuilt bytes: `9722369`
- scratch `build_receipt.json` hashes:
  - renderer: `71953059e2555cae36bf056aa80bdc7440170eb82c106606136dcc4daa74c884`
  - spec: `235b22d09c2485bf69a5f746a95b687bc6a55acf2ea0af56cf64115ca893a746`
  - timeline: `4dca3a5e0753dde46bffcdc3ee3a39453db46411317b6d205a4119a928f7e450`
  - audio master: `b0900ec6c8146bedae3497d4c4141e81edfc66ad19478faea90b2211d0053df7`

Deterministic rebuild: PASS.

### Method-Only Boundary

No `SOURCE_FREEZE.json` exists. This artifact therefore may not state a result.

I do not find a number, sign, offset value, selected evolution verdict, or anchor count stated in
the sampled frames or OCR. The strongest semantic wording is the repeated title:
`An apparent metallicity offset has two explanations`. It is weaker than the older 0245K title
because it says `apparent`, and the adjacent narration/frames consistently present conditionals
and withheld value/sign/result. I do not treat that as a result assertion, but it is still the
weakest wording in the artifact.

KUN state for `c892f3fa`: **PASS WITH CAVEATS**.

Caveats: no `SOURCE_FREEZE.json`, so method-only local canary only; strict low-motion holds remain;
and the repeated `apparent metallicity offset` title is the closest wording to substantive drift,
even though I do not judge it to cross the HOLD line in this encode.

## c892f3fa Directory-Immutability Correction - 2026-08-09 14:56 KST

I read `HWAO_INCIDENT_FROZEN_DIR_INTRUSION.md` and
`reviews/tori-sibling-evidence/c892f3fa/DIRECTORY_IMMUTABILITY_CAVEAT.json`.

Correction accepted: my earlier lane-local rebuild command followed Hwao's instruction, but the
instruction was defective because
`integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T1406K/` is itself a frozen candidate
directory, not a writable lane workspace. The rebuild evidence is valid for the exact video, but
the directory immutability caveat must travel with it.

Current filesystem observation at 2026-08-09 14:56:28 KST:

- `containment/` exists but is empty in my local read.
- `_tmp_kun_rebuild_20260809T1452K/` is still present inside the frozen 1406K candidate directory.
- `_tmp_kun_frame_review_20260809T1450K/` is also still present inside the frozen 1406K candidate
  directory from my frame sampling. That was not called out in the incident text, but it is the same
  class of frozen-directory scratch placement.
- I am not moving or deleting either subtree here; Hwao's incident says containment will be
  moved, never deleted.

Hash recheck:

- top-level frozen MP4:
  `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`
- rebuilt MP4 inside `_tmp_kun_rebuild_20260809T1452K/candidate/`:
  `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`

This does not change KUN's audio/sync/rebuild verdict on the exact MP4 bytes: **PASS WITH CAVEATS**
for `c892f3fa` remains. It does qualify custody: the top-level video is byte-exact and still matches
`POST_ENCODE_FREEZE.json`, but the frozen candidate directory received post-freeze scratch
additions. Future rebuild scratch should go in a non-frozen lane workspace, not `/tmp` and not inside
a frozen candidate directory.

The older 0245K provenance caveat is unchanged: KUN could not rebuild 0245K from its package because
that artifact lacked lane-local provenance render scripts. The 1406K package does include
`provenance/render.py`, and the same-hash rebuild evidence above applies to 1406K only.
