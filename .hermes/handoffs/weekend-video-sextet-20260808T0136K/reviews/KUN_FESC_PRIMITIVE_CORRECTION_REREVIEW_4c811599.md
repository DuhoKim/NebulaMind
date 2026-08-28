# Kun FESC primitive-correction exact-hash rereview — `4c811599…`

Reviewed: 2026-08-09T14:50:41+0900 (KST)  
Reviewer: Kun  
Scope: audio, synchronization, encoded-media conformance, narration custody, current-host exact replay, and renderer portability for exactly one frozen FESC candidate.

## Disposition

- **TECHNICAL VERDICT: PASS** for exact MP4 SHA-256 `4c8115997e21689508f31587672a3dd7da9c902803427c43490603bad08309b9`.
- **AUDIO / SYNCHRONIZATION: PASS.** Full decode, stream format, delivered pace, frame-aligned timing, encoded loudness/true peak, no-music evidence, and introduction intelligibility all pass.
- **CURRENT-HOST EXACT REPRODUCIBILITY: PASS.** A reviewer-owned replay from the frozen spec, timeline, mastered narration, nine source files, and exact archived renderer produced the same 9,993,751-byte MP4 and the same full SHA-256.
- **RENDERER PORTABILITY: PASS WITH NON-BLOCKING CURRENT-HOST CAVEATS; ARBITRARY-HOST BYTE IDENTITY NOT PROVEN.** The exact current production environment remains available on this host. The packet does not embed that environment or establish identical output on materially different hosts.
- **ADMINISTRATIVE DISPOSITION: HOLD / GATES CLOSED.** This packet is review evidence only. It does not promote, publish, upload, integrate, report, or revive any withdrawn order. `video_reportable_now` remains `false`.

The technical PASS and administrative HOLD are intentionally separate.

## Exact target and governing receipts

| Item | Independently recomputed SHA-256 | Result |
|---|---|---|
| Frozen MP4 | `4c8115997e21689508f31587672a3dd7da9c902803427c43490603bad08309b9` | **PASS**; required exact hash |
| MP4 bytes | `9,993,751` | **PASS**; build and receipt agree |
| Primitive-correction receipt | `50a305b03d1a6b9b0395ad407342fbf7a600426aa4dbf70454d9b64378f40334` | **PASS**; required exact receipt hash |
| Candidate `RECEIPT.json` | `5c72fc7b1a6bf4de0ac479b62806e5ca806d08dcf296c8160a5fb4f3bafc081a` | **PASS** |
| `spec.json` | `7a138e2d9b5a0c7e6025533d455599a9ce683bce12d14e688a78c12d198cbad5` | **PASS** |
| `audio/timeline.json` | `5718fe71b41fb9c99fd74925d2670c3c96163eaaf6fcdd088ce8f1576067fcd4` | **PASS** |
| `audio/narration_master.wav` | `8e40e71229fc3e0bf2f21e7f02f8c3370e1042a62ffadb03fb2ff10f96adf156` | **PASS** |
| Candidate-local renderer | `c42037c73c9703dead42d2a8c1752ced74bf8b6cad42877d7b8dffecf8f1810a` | **PASS** |
| Candidate-local QA tool | `8228a5c029ff7b0584b528a1ff4b0b197da742ac1d6768f98abfa329d5020817` | **PASS** |
| `build_receipt.json` | `1891bfc1e43668787cdf74e500cc353a7aeed66883b44549d04e03c885a4229c` | **PASS** |
| `encoded_qa.json` | `cd61c96c990d067eab7667361568ca64a3ca7ea8d86d1170682fb8282fdac2ba` | **PASS** |
| `source_manifest.json` | `555b2d58cb56f309c439d87b0db3f4ba0e5a8822511a0fee7f6de99905e0c088` | **PASS** |
| `provenance_manifest.json` | `9911318e77185cbaf6244d8bba3c34c65e3d5206dba5c09a5a764379bf2c5e60` | **PASS** |
| `POST_ENCODE_FREEZE.json` | `e0cad67c217ddbd89ecd514a66966ca2670bfcf39da767523995930c06df45cd` | **PASS** |

All nine source-manifest entries and all three provenance-manifest entries matched their declared paths, byte counts, and hashes. The candidate receipt's contact-sheet hash binds `encoded-contact-sheet.jpg`; it matches that file exactly. In total, 142 independent receipt/custody checks passed with no failed binding.

The immediate frozen predecessor MP4 remains present at exact SHA-256 `acfb7fee70d5a131d4a44e8962cfe3fe3cd22104bf9cf8fa00bbbd6c2c00cbc0`.

## Independent encoded-media verification

I mapped both streams and decoded through EOF with decoder errors fatal. The full mapped decode returned success with no decode error.

| Measurement | Fresh result | Gate |
|---|---:|---|
| Video codec / pixel format | H.264 / `yuv420p` | **PASS** |
| Resolution | 1920 × 1080 | **PASS** |
| Frame rate | `30/1` average and real rate | **PASS** |
| Decoded video frames | 7,102 | **PASS**; agrees with frozen encoded QA |
| Video start | 0.000000 s | **PASS** |
| Video duration | 236.733333 s | **PASS** |
| Audio codec | AAC | **PASS** |
| Encoded audio format | 48,000 Hz, mono | **PASS** |
| Decoded AAC packets/frames read | 11,098 | **PASS**; agrees with frozen encoded QA |
| Audio start | 0.000000 s | **PASS** |
| Audio duration | 236.739000 s | **PASS** |
| Container duration | 236.739000 s | **PASS** |
| Video–audio stream-start delta | 0.000000 s | **PASS** |
| Video duration minus PCM master | −0.005792 s | **PASS**; inside one 30-fps frame |
| Audio duration minus PCM master | −0.000125 s | **PASS** |

The renderer submits `ceil(236.739125 × 30) = 7,103` raw frames and applies an FFmpeg `-t 236.739125` cutoff; the frozen encoded stream contains 7,102 timestamp-bounded frames. I treat the freshly decoded 7,102 count, not the renderer-loop count, as the encoded invariant.

## Narration receipt, per-sentence assets, and PCM custody

The hash-bound synthesis receipt attests:

- provider route: `Hermes managed OpenAI audio gateway`;
- model: `gpt-4o-mini-tts`;
- voice: `alloy`;
- speed: `1.18`;
- music: `false`;
- synthesis unit: `one exact sentence per call`;
- sentence count: 22.

I independently checked that the 22 records have 22 unique IDs and 22 unique raw assets. Every exact sentence and sentence-text SHA-256 agrees across the synthesis receipt, current spec, and current timeline. Every raw MP3 matches its declared byte count and SHA-256.

For every one of the 22 MP3s, I freshly decoded to mono signed 16-bit PCM at 48 kHz. Results:

- **22/22** fresh PCM payloads are byte-identical to the candidate's stored decoded WAV payloads;
- **22/22** decoded frame counts equal `audio_end_sample - audio_start_sample`;
- every sentence cursor is continuous through its declared pause;
- rebuilding the complete zero-filled timeline from those fresh sentence decodes produces PCM byte-identical to `audio/narration_raw.wav`;
- raw and mastered narration both contain 11,363,478 samples;
- the derived terminal tail is 115,200 samples = 2.400000 s, and every tail sample is zero;
- raw-to-master correlation is `0.9992689717`; the measured optimal gain is `+0.453724 dB`, consistent with the recorded dynamic loudness mastering rather than an added program bed.

The actual narration assets are byte-identical to the immediate `T1345K` predecessor: synthesis receipt, all 22 raw MP3s, all 22 decoded WAVs, `narration_raw.wav`, and `narration_master.wav`. The current timeline differs from that predecessor only in the eight visual-only `params.icon` edits from `curve` to `paired_strokes` (`i01–i04`, `d01–d02`, `x01–x02`); all audio timing fields and other timeline values are unchanged.

### Attestation boundary

Voice identity, managed route, requested speed, and API call granularity are not encoded into MP3/AAC headers and therefore cannot be reverse-proven from codec bytes alone. The exact receipt, one-record/one-asset structure, text hashes, raw hashes, and fresh decodes make the production contract internally consistent and hash-bound; those route/voice/speed fields remain production attestations rather than codec-forensic findings.

## Delivered pace and frame-accurate A/V alignment

Delivered pace was recomputed from the first sentence start through the final sentence end:

- word count: 448;
- first-to-last speech span: 233.739125 s;
- delivered WPM: `448 ÷ (233.739125 / 60) = 115.0000027`;
- required range: 105–125 WPM;
- result: **PASS**.

Every visual action time was independently recomputed as `frame / 30`; every audio time was independently recomputed as `sample / 48000`.

- maximum absolute visual/audio sentence-start delta: `0.0153333333 s`;
- one 30-fps frame: `0.0333333333 s`;
- encoded stream-start delta: `0.0000000000 s`;
- result: **PASS — all sentence starts are within one frame**.

The intended peak remains the longest sample-timed section:

- peak: `52.2536667 s`;
- runner-up motivation: `33.0042500 s`;
- margin: `19.2494167 s`;
- result: **PASS**.

## Loudness, true peak, clipping, and no music

I remeasured the encoded AAC with the recorded production filter:

`loudnorm=I=-20.3:LRA=7:TP=-2.3:print_format=json`

Fresh encoded measurements:

- integrated loudness: **−20.24 LUFS**;
- true peak: **−2.30 dBTP**;
- loudness range: 7.50 LU;
- normalization type reported by the analysis pass: dynamic;
- result: **PASS**; no clipping.

The AAC decoded to 11,364,352 samples. The extra 874 samples (`0.018208 s`) beyond the 11,363,478-sample PCM master are normal codec-tail padding. Over the full master span:

- encoded AAC versus mastered narration correlation: `0.9999945727`;
- optimal-gain residual SNR: `49.6438 dB`;
- renderer build command maps only the frozen narration master as its audio input;
- the synthesis/correction receipts both declare `music: false`;
- result: **NO-MUSIC PASS**. The encoded program is the AAC realization of the frozen narration master, with no evidence of a music bed or second audio source.

## Encoded introduction intelligibility

I freshly extracted encoded audio from 0.350000 s through 33.954250 s at mono 16 kHz PCM. The complete fresh WAV is byte-identical to the stored transcription input and its receipt:

`5c773d8f186af6e8323a6d2486048dd90ba03deca98124e659dc7bf926d8e8b2`

The hash-bound managed Whisper-1 receipt gives normalized similarity `1.0`. Its transcript preserves all critical rhetorical clauses:

- `if galaxies were genuinely …`;
- `that would limit …`;
- `could instead …`;
- `not about the galaxies`;
- the closing question, `how do we tell a source shortfall from an assumption shortfall?`.

**Introduction intelligibility: PASS.** A second local ASR engine was not available on the current host (`whisper`, `faster-whisper`, `mlx-whisper`, and `transformers` were absent), so this row rests on a fresh byte-exact extraction plus the hash-bound managed Whisper-1 transcript, not on two independent ASR models. That is a provenance caveat, not an intelligibility failure.

## Current-host exact replay

I built only under reviewer-owned `/tmp` storage. I did not invoke the archived renderer in place because its provenance step copies `Path(__file__)` to `candidate/provenance/render.py`; direct invocation from that destination would hit the candidate-local self-snapshot `SameFileError` trap. Instead, I copied the exact renderer bytes to a temporary execution path, verified the copy hash, and let those unchanged bytes create their normal temporary candidate-local snapshot.

Frozen replay inputs:

- exact candidate basename;
- `spec.json`;
- `audio/timeline.json`;
- `audio/narration_master.wav`;
- all nine source-manifest files;
- exact archived renderer `c42037c73c9703dead42d2a8c1752ced74bf8b6cad42877d7b8dffecf8f1810a`.

Replay environment:

- Python `3.11.15 (main, Jun 23 2026, 15:46:51) [Clang 22.1.3]` from the current Hermes environment;
- Pillow `12.3.0`;
- FFmpeg `8.1.2` with libx264;
- macOS `26.6.1-arm64`;
- Avenir Next SHA-256 `98dec241f3ee712a37fad61aafdb83e225ed54c3e5b6e9f0abeb24eba13743ba`;
- Menlo SHA-256 `dc256e0b39c2a6fec947129d421fef41b8b429f58f9b6e5d1b148c87f775c1f6`.

The live environment matches the frozen environment on Python build, platform, Pillow, FFmpeg lines, font paths, and font hashes. The only environment-receipt difference is the expected absolute audio input path under `/tmp`; after path normalization, the environment records are equal.

Replay result:

| | Frozen candidate | Current-host replay |
|---|---:|---:|
| Bytes | 9,993,751 | 9,993,751 |
| SHA-256 | `4c8115997e21689508f31587672a3dd7da9c902803427c43490603bad08309b9` | `4c8115997e21689508f31587672a3dd7da9c902803427c43490603bad08309b9` |
| Renderer snapshot | `c42037c7…` | `c42037c7…` |

**Current-host exact replay: PASS.** The temporary replay, output MP4, fresh introduction extract, audit scripts, and reviewer-owned audit trees were removed. No reviewer temporary path remains.

## Portability caveats

These caveats do not block the demonstrated current-host exact replay, but they limit broader claims:

1. **Arbitrary-host identity is unproven.** Exact bytes depend on the recorded macOS fonts, Python/Pillow rasterization, FFmpeg/libx264 build, and codec behavior. Those dependencies are recorded but not embedded or locked as a portable environment image.
2. **Bare `python3` is not the production interpreter.** On this host `/usr/bin/python3` is Python 3.9.6 with Pillow 11.3.0. Exact replay required the still-present Hermes Python 3.11.15 / Pillow 12.3.0 environment. A command that silently uses the system interpreter is not an equivalent replay.
3. **Absolute font paths are macOS-specific.** The renderer requires `/System/Library/Fonts/Avenir Next.ttc` and `/System/Library/Fonts/Menlo.ttc` with the exact recorded hashes.
4. **Direct candidate-local invocation has a self-snapshot trap.** The renderer copies itself to the path where it is already archived. An exact temporary execution copy is required; no byte edit is required or permitted.
5. **Historic audio paths are not candidate-local as written.** The synthesis receipt records `audio/fesc/raw/...`, while the frozen candidate stores matching bytes under `audio/raw/...`; the timeline similarly names `audio/fesc/narration_*.wav`. Hash-based basename resolution succeeds, and the renderer itself consumes candidate-local `audio/narration_master.wav`, but the receipt paths are not relocation-clean.
6. **End-to-end resynthesis/assembly is not turnkey.** The receipt names `provenance/synthesize.py` and the timeline names `provenance/assemble.py`, but those scripts are not in this candidate's three-file provenance manifest. Asset custody and exact renderer replay pass; fresh managed-service resynthesis and standalone assembly replay are separate, unproven claims and are unnecessary for this visual-only correction.
7. **The synthesis receipt retains its historical identity.** It names `fesc-method-overhaul-canary-20260809T0327K` and that historical spec hash. Exact sentence text and all audio bytes match the current correction and immediate predecessor, but the receipt is a reused narration receipt rather than a newly minted current-candidate TTS receipt.
8. **Second-ASR portability was not demonstrated.** The exact stored managed Whisper-1 input and transcript are bound; no second local ASR engine was available.

The weakest portability point is not the frozen MP4 or the demonstrated renderer replay; it is the lack of a self-contained, locked cross-host environment and turnkey synthesis/assembly packet.

## Non-mutation and closed gates

Before heavy QA I recorded a sorted path/size/content-hash manifest of all 629 files in the governed candidate tree. After the full decode, audio reconstruction, introduction extraction, exact replay, and temporary cleanup, I recomputed it.

- baseline candidate-tree digest: `f56d42c6056a26cd0597c52daf3d13256dba553ba77333f8d1f1a216cec88a29`;
- final candidate-tree digest: `f56d42c6056a26cd0597c52daf3d13256dba553ba77333f8d1f1a216cec88a29`;
- file count: 629 before and 629 after;
- added files: none;
- removed files: none;
- changed files: none;
- final MP4 SHA-256: still `4c8115997e21689508f31587672a3dd7da9c902803427c43490603bad08309b9`.

**Candidate non-mutation: PASS.** The predecessor was also read only.

The current candidate receipt, primitive-correction receipt, and post-encode freeze keep the following gates false: promotion/reportability, upload/publication, public/shared/video-root copy, `frontend/public`, `paperVideos`, cockpit, database, deploy/restart, and Git commit/push/merge/history action. I performed none of those actions. I did not build a new candidate, mutate a candidate, promote, upload, copy public files, or perform Git/DB/deploy work.

The prior Hwao sibling-fix order is recorded as withdrawn/stand-down and supplies no promotion authority. This fresh exact-hash review is therefore **receipt-only technical evidence**. It does not alter the administrative board state.

## Final Kun stamp

**PASS — audio, sync, decode, codec/format, pace, loudness/true peak, no-music evidence, managed Alloy 1.18 per-sentence receipt structure, introduction intelligibility, candidate custody, and exact current-host replay all pass for `4c8115997e21689508f31587672a3dd7da9c902803427c43490603bad08309b9`.**

**HOLD — all promotion, reportability, publication, upload, integration, DB, deploy, and Git gates remain closed. Arbitrary-host renderer byte identity and turnkey end-to-end resynthesis/assembly remain unproven portability claims.**
