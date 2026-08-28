# Goru FESC primitive-correction exact-hash rereview

- Review timestamp: `2026-08-09T14:57:42+0900`
- Reviewer: **Goru** (fresh independent mechanical/numeric/source/provenance pass)
- Lane: **FESC only**
- Candidate: `canaries/fesc-method-overhaul-canary-20260809T1420K/fesc-method-overhaul-canary-20260809T1420K.mp4`
- Required candidate SHA-256: `4c8115997e21689508f31587672a3dd7da9c902803427c43490603bad08309b9`
- Correction receipt reviewed: `FESC_PRIMITIVE_CORRECTION_RECEIPT_4c811599.json`
- Correction-receipt SHA-256: `50a305b03d1a6b9b0395ad407342fbf7a600426aa4dbf70454d9b64378f40334`

## Verdict

# **PASS**

**HOLD: NO.** The exact candidate named above passes this independent local rereview. This is a review decision only: it does **not** promote, publish, upload, copy, deploy, restart, commit, push, merge, or make the video reportable. Every external gate remains closed.

## Scope and independence

I treated the correction receipt and candidate-local receipts as assertions to test, not as proof. I independently:

1. recomputed every requested file hash;
2. probed and fully decoded the exact MP4;
3. independently recomputed timeline, pacing, alignment, section, motion, loudness, caption, numeric, source, manifest, and hash predicates;
4. inspected renderer source and exercised its validation dynamically;
5. freshly extracted all 473 two-fps frames, all eight exact reported-time frames, all ten full contact sheets, and the exact-time contact sheet in an automatically deleted temporary directory;
6. compared the fresh derivatives byte-for-byte to the frozen review derivatives;
7. visually reviewed the ten sheets covering all 473 frames and the eight-frame exact-time sheet; and
8. captured opening/interim/closing custody hashes for the candidate, frozen predecessor, and the two pinned comparison lanes.

No candidate byte was written. Temporary replay derivatives were outside the candidate and were deleted automatically. The only persistent write made by this review is this packet.

## Exact hash ledger

Every value below was recomputed from bytes and matched the corresponding build/QA/receipt assertion where one exists.

| Artifact | Bytes | Recomputed SHA-256 |
|---|---:|---|
| exact candidate MP4 | 9,993,751 | `4c8115997e21689508f31587672a3dd7da9c902803427c43490603bad08309b9` |
| `spec.json` | 18,558 | `7a138e2d9b5a0c7e6025533d455599a9ce683bce12d14e688a78c12d198cbad5` |
| `audio/timeline.json` | 35,330 | `5718fe71b41fb9c99fd74925d2670c3c96163eaaf6fcdd088ce8f1576067fcd4` |
| `audio/narration_master.wav` | 22,727,034 | `8e40e71229fc3e0bf2f21e7f02f8c3370e1042a62ffadb03fb2ff10f96adf156` |
| `audio/synthesis_receipt.json` | 18,574 | `796bb3a64aab9f1e24a23185c020f1e47e94a738ac21e4b4359ed9cc3d703372` |
| `subtitles.srt` | 3,781 | `95f9e73d46e2115a080bc7bc7721fb2de0856635876dfa4f18990c0d491a59a1` |
| `provenance/render.py` | 29,312 | `c42037c73c9703dead42d2a8c1752ced74bf8b6cad42877d7b8dffecf8f1810a` |
| `provenance/qa.py` | 15,946 | `8228a5c029ff7b0584b528a1ff4b0b197da742ac1d6768f98abfa329d5020817` |
| `provenance/render_environment.json` | 1,797 | `a097b3e01b974a8998736365b5723e392653a77ae21388f3f5d4e3f5df61852d` |
| `encoded_qa.json` | 6,328 | `cd61c96c990d067eab7667361568ca64a3ca7ea8d86d1170682fb8282fdac2ba` |
| `encoded_qa/encoded-introduction.wav` | 1,075,414 | `5c773d8f186af6e8323a6d2486048dd90ba03deca98124e659dc7bf926d8e8b2` |
| `frame-review-2fps/FRAME_INDEX.json` | 3,932 | `4f6c15059a57cb1c94879026b0a94a77eb2809e408f4fd4a03ed58ff66acd19b` |
| `numeric_guard.json` | 59 | `76e71cf73e7e61e12ae00ab5d8cf5ad3e10889c1799a3a0ba764c3659adfdbb7` |
| `CORRECTION.json` | 2,025 | `baacd4ecae723d8e58d0e18783b62ba4b3937e91b6848d4d2a2a8dafc93cf74b` |
| `build_receipt.json` | 1,024 | `1891bfc1e43668787cdf74e500cc353a7aeed66883b44549d04e03c885a4229c` |
| `source_manifest.json` | 1,526 | `555b2d58cb56f309c439d87b0db3f4ba0e5a8822511a0fee7f6de99905e0c088` |
| `provenance_manifest.json` | 511 | `9911318e77185cbaf6244d8bba3c34c65e3d5206dba5c09a5a764379bf2c5e60` |
| `RECEIPT.json` | 1,790 | `5c72fc7b1a6bf4de0ac479b62806e5ca806d08dcf296c8160a5fb4f3bafc081a` |
| `POST_ENCODE_FREEZE.json` | 566 | `e0cad67c217ddbd89ecd514a66966ca2670bfcf39da767523995930c06df45cd` |
| `PREDECESSOR.json` | 491 | `b57208bd188df4de08bddad4668ba8ab0731153ee0d9175e196abce6ceacf37f` |
| top-level correction receipt | 4,860 | `50a305b03d1a6b9b0395ad407342fbf7a600426aa4dbf70454d9b64378f40334` |

Cross-binding replay passed: video ↔ build ↔ encoded QA ↔ receipt ↔ freeze; spec ↔ build ↔ receipt; timeline ↔ build ↔ receipt; audio master ↔ build ↔ receipt; renderer ↔ build ↔ provenance manifest; encoded QA ↔ receipt; receipt ↔ freeze; and the output-byte counts all agree.

## Primitive-level correction

### Exactly eight icon records, all `paired_strokes`

Both `spec.json` and `audio/timeline.json` contain exactly these eight icon-bearing IDs and values:

| ID | spec icon | timeline icon |
|---|---|---|
| `i01` | `paired_strokes` | `paired_strokes` |
| `i02` | `paired_strokes` | `paired_strokes` |
| `i03` | `paired_strokes` | `paired_strokes` |
| `i04` | `paired_strokes` | `paired_strokes` |
| `d01` | `paired_strokes` | `paired_strokes` |
| `d02` | `paired_strokes` | `paired_strokes` |
| `x01` | `paired_strokes` | `paired_strokes` |
| `x02` | `paired_strokes` | `paired_strokes` |

Census: spec `8/8`, timeline `8/8`, combined mismatches `0`. No icon record says `curve`.

### No available curve **icon** renderer branch

`Renderer.icon` is at `provenance/render.py:214-237`. Its explicit kinds are `archive`, `galaxy`, `paired_strokes`, `plane`, and `anchor`, followed by an unconditional unknown-kind rejection. The source regex used for this exact defect,

```text
elif\s+kind\s*==\s*['"]curve['"]\s*:
```

returned **0** matches. The accepted QA source at `provenance/qa.py:179-180` separately requires the curve icon parameter and that renderer branch to be absent.

Dynamic, read-only validation probes produced:

- `icon='curve'` → rejected with `RuntimeError: result-like curve icon primitive is forbidden: {'probe': 'curve'}`;
- `icon='bogus_icon'` → rejected with `RuntimeError: unknown icon primitives: {'probe': 'bogus_icon'}`.

The paired-stroke source witness is `render.py:223-229`: two lines at `y-30` and `y+30`, both from `x-92` to `x+92`, with equal endpoint caps. A direct in-memory raster probe found exactly two disconnected horizontal bands:

- band 1: `x=114..306`, `y=176..184`, width `193`, height `9`;
- band 2: `x=114..306`, `y=236..244`, width `193`, height `9`;
- inter-band gap: `51` pixels; widths equal; no shared pixels.

This is the required non-graph primitive: no axis, slope, order, response, intersection, or crossing.

For completeness, the source still has a non-icon dispatch label `mode == 'curve'` for five `peak` records (`p01..p05`). It calls `peak_curve`, but that routine (`render.py:279-297`) renders equal-height calculation-arm cards, straight arrows, stage controls, and the banner `MATCHED SWEEP DESIGN · NO RESULT GEOMETRY`; it contains no plotted curve primitive. This legacy mode name is not reachable through `params.icon`, is not the predecessor defect, and the reviewed peak frames show no curve or crossing. Thus the requested curve **icon** rendering branch is absent and unavailable.

### Exact-time visual correction evidence

All eight exact reported-time frames were independently re-extracted and byte-matched to the frozen exact frames. Visual inspection found only paired separated horizontal strokes at:

`5.052`, `15.013`, `24.243`, `31.816`, `42.050`, `51.592`, `222.410`, and `231.051` seconds.

No exact-time frame contained a sloped/rising/falling/intersecting icon, an axis, an order implication, or a result-bearing geometry.

## Encoded QA: independently re-derived 30/30

The stored report says `status=PASS`, `passed=30`, `total=30`; it contains exactly 30 named booleans and every value is the literal JSON boolean `true`. I independently recomputed all 30 from the encoded media and source artifacts. The recomputed name set and value map exactly equaled the stored map: **30/30 PASS, zero failures**.

1. `video_stream_h264`
2. `audio_stream_aac`
3. `resolution_1920x1080`
4. `fps_30`
5. `duration_within_one_frame`
6. `delivered_wpm_in_range`
7. `av_alignment_under_one_frame`
8. `all_sentence_states_extracted`
9. `encoded_intro_transcription_pass`
10. `motivation_first_four`
11. `peak_is_longest_section`
12. `five_distinct_peak_frames`
13. `no_eight_second_freeze`
14. `positive_motion`
15. `loudness_in_target_band`
16. `true_peak_safe`
17. `spec_hash_matches_build`
18. `timeline_hash_matches_build`
19. `audio_hash_matches_build`
20. `encoded_hash_matches_build`
21. `renderer_snapshot_matches_build`
22. `numeric_guard_pass`
23. `curve_icon_parameter_absent`
24. `curve_icon_primitive_unavailable`
25. `source_grounded_runtime_at_least_75_percent`
26. `ocr_internal_terms_clean`
27. `captions_at_most_two_lines`
28. `method_only_gate_closed`
29. `no_source_freeze_in_candidate`
30. `full_decode_pass`

Independent numeric witnesses:

- complete H.264/AAC decode return code: `0`;
- probe: H.264, AAC, `1920×1080`, `30/1` fps, `7,102` video frames, `11,098` audio frames;
- encoded duration: `236.739` s; timeline master: `236.739125` s;
- records: `22`; word-count fields and independent token count: `448`;
- occupied speech span: `233.739125` s; independently derived delivered WPM: `115.00000267392119`;
- maximum independently derived A/V action-start delta: `0.015333333333330756` s, below one `30`-fps frame;
- first four records: `i01..i04`, all `motivation` / `intro`;
- peak duration: `52.25366666666667` s, strictly longer than the next-longest section (`motivation`, `33.00425` s);
- fresh five peak samples: five distinct hashes and byte-identical to stored samples;
- two-fps motion replay: `473` samples, mean absolute frame difference `0.39567531779661014`, maximum `11.644097222222221`, longest near-unchanged run `0.0` s;
- integrated loudness: `-20.24` LUFS; true peak: `-2.30` dBTP;
- fresh introduction WAV hash: `5c773d8f186af6e8323a6d2486048dd90ba03deca98124e659dc7bf926d8e8b2`, byte-identical to the stored extraction; transcript similarity `1.0`;
- captions: 22 SRT cues, exact text/order match to timeline, independently wrapped maximum `2` lines;
- recursive case-insensitive `SOURCE_FREEZE.json` census: `0`;
- independently derived grounded runtime: `99.74655646801095%`; missing grounding paths: `0`.

The independent replay deliberately strengthened several receipt checks: WPM, A/V alignment, section durations, grounding percentage, audience numerics, recursive source-freeze absence, full derivative binding, and all hash links were recomputed rather than accepted from stored summary fields.

## Hash-bound 473-frame review

The frame index is exactly `4f6c15059a57cb1c94879026b0a94a77eb2809e408f4fd4a03ed58ff66acd19b`. It binds:

- video SHA-256 `4c8115997e21689508f31587672a3dd7da9c902803427c43490603bad08309b9`;
- sampling rate `2` fps;
- decoded-frame count `473`;
- ten full contact sheets;
- eight exact reported-time frames; and
- one exact reported-time sheet.

Fresh replay results:

- stored frames: `473`; fresh frames: `473`;
- names are continuous `frame-0001.jpg` through `frame-0473.jpg`;
- fresh-to-stored byte mismatches: `0/473`;
- stored and fresh frame-tree SHA-256: `47525f88fa0582997a7050bdead9c51a8fa537de43f7e9a50ceccefdb939bdf5`;
- all ten frozen sheet hashes match the index;
- all ten sheets rebuilt from the fresh frames byte-match the frozen sheets;
- all eight frozen exact-frame hashes match the index;
- all eight fresh exact frames byte-match the frozen exact frames;
- the rebuilt exact-time sheet byte-matches the frozen sheet.

Full-sheet hash ledger:

1. `full-2fps-01.jpg` — `0371f70955ab5d187a750df56ec0452e3329d3d92cfbd963043bcd988b51ac51`
2. `full-2fps-02.jpg` — `2be9bf3c264af7edfb81288e7c56eed94201f75c307c1bbb94b9850489ce3ab6`
3. `full-2fps-03.jpg` — `f2dc7599b06a0128db05453b42921eeda1cf0a22b9fca0035e5e1f50f86bd29f`
4. `full-2fps-04.jpg` — `0bbcdd47d6ec052ad042f4450e5bf12d86a76af35108f16e5f2bdd5991995589`
5. `full-2fps-05.jpg` — `7182c1f8bd152ba5db8d9963f535676a6a0a768e19bb9dcbf86041e5058469d2`
6. `full-2fps-06.jpg` — `b58ebab434c04f38afb1da9e78eaec14a50a4b2a6b7e2d9f09f80c18510931fa`
7. `full-2fps-07.jpg` — `4397a97e2e37c4ad19060081f7f6d889fa0bcbae7631cf8b48dea238198499d8`
8. `full-2fps-08.jpg` — `84f9f13ed30f8b90844e86b512ca71342762cee3c80d48ffe922921760b7611b`
9. `full-2fps-09.jpg` — `72b3ca19d2810e59a31933c944b07eb476ed043434ff509842e59cb3db9b0dff`
10. `full-2fps-10.jpg` — `215b53050337d2f5dcd6743c0cf903d6c5e7b0399dccff054d9e4467420d8cb5`

Exact-time frame hashes, in the order above:

`988b242a5de080187724c2d0aad22034fb99f3faa79ccdd76d6b52db10e1b145`,
`04346a13669c977be454092fb6be4d55e030f79765e604c952a813c4bc4262ff`,
`2626fb709fbc8ffd778ea1eb5860ea3e299ce804fc75b054a78449bf9f38ba40`,
`034cd5d13937d84014c2dfb7412ca3138f07f7a397b819d80e380c000ef2384d`,
`546c727a49b449a18003350c14ca3ae20ada331317011c79a6ae870b7d24aba1`,
`08d16f131443cb0bc6066dd324cf15e5cce4734d3992f8c971ed48da5e2fbd8d`,
`fb113d0eef61397788db2f148daf125f758a5ad156f00d86f9060fd148c40a65`, and
`5a19d95159b592f20c08e7e6127798bd9ae1bcde839532c41c6c559d52b97605`.

Exact-time sheet SHA-256: `da3d9fe3a2b6b0627168484ccdafffb384059468d366702c5bfe3a53f8584d91`.

I visually inspected all ten sheets (the complete `0.000` through `236.000` s two-fps sequence) and the exact-time sheet. Excluding only the sheet timestamps, which are QA scaffolding outside the video tiles, I found no suspect tile: no curve-icon crossing/order geometry, no quantified result, no internal path, no foreign-lane identity/content, and no material clipping or collision.

## Numerals, results, paths, and sibling-lane leakage

### Audience-visible projection

I constructed the renderer-consumed audience projection from title/series strings, all 22 narration/caption strings, display citations, all string-valued visual parameters, and hard-coded renderer display strings. Results:

- standalone Arabic-numeral occurrences: `0`;
- candidate forbidden-term hits: `0`;
- internal path/artifact-term hits: `0`;
- foreign sibling-lane identity hits (`MZR census`, `BrightEnd`/`bright-end`, spin lane, MZR anchor): `0`;
- `numeric_guard.json`: `status=PASS`, `problems=[]`, `evidence=[]`.

The estimator uses the symbolic `D(z)` and an algebraic definition while explicitly showing `VALUE WITHHELD` and `NO SIGN SELECTED`; `z` is a variable, not an Arabic numeral. Boundary/payoff states likewise say values, direction, sign, interpretation, and claims remain withheld. No result count, threshold, curve value, direction, or scientific outcome appears.

A 473-frame Tesseract pass completed on every hash-bound frame with zero tool errors and OCR-corpus SHA-256 `8b913b5908dc7c4574dd5b9b9c28de96216205844bdd5993a84a12b87ec1aa8c`. It found zero internal-path hits, zero foreign sibling-lane hits, and zero unsafe-result-phrase hits. Tesseract did emit digit-like false recognitions (`sc1ence`, `D(z) = 5`, and isolated `2`/`5` readings of dots and strokes); I did **not** treat those as proof. I adjudicated them against the zero-digit renderer projection and the complete visual sheets, which show `SCIENCE`, `D(z) =` with the value withheld, and non-text graphic strokes. No Arabic digit is actually rendered in a video frame.

The intended lane-local boundary sentence `Because no sibling source freeze exists...` and the citation `Sibling rollout authority · method only` are present and authorized. They do not import any sibling lane's identity, scientific values, visuals, result, or artifact path. “No unauthorized sibling content” therefore passes; this packet does not claim the literal word `sibling` is absent.

## Audio and source/provenance

Audio is a byte-identical visual-only reuse from the held predecessor:

- master WAV old/new: `8e40e71229fc3e0bf2f21e7f02f8c3370e1042a62ffadb03fb2ff10f96adf156`;
- synthesis receipt old/new: `796bb3a64aab9f1e24a23185c020f1e47e94a738ac21e4b4359ed9cc3d703372`;
- subtitles old/new: `95f9e73d46e2115a080bc7bc7721fb2de0856635876dfa4f18990c0d491a59a1`;
- 22 raw audio files old/new tree: `f2a7a328b1c5d7bcc3884732e08a96f96e18a7d8ecf9bd39ec4014f234937b22`;
- 22 decoded WAVs old/new tree: `2879620a344af851932b2d7d185c2826d7e6b4d7e0597aa4c04ca7303cc3f989`;
- timeline-to-synthesis-to-local raw/decoded hash problems: `0`.

The source manifest contains exactly 9 files and equals a fresh path/hash/byte inventory. The provenance manifest contains exactly 3 files and likewise equals a fresh inventory. All 22 grounding paths resolve inside the candidate. Source-tree SHA-256 is unchanged from predecessor: `bab242d4304b4650a83019a411d9444b415af608e862bbe69000247d605e7fbe`.

A recursive predecessor/new structured diff found exactly eight timeline changes, all `params.icon: curve → paired_strokes`. The spec has those same eight icon changes plus the new required/forbidden primitive declarations and expected candidate/revision metadata; no narration string changed.

## Predecessor and other-lane preservation

Pinned MP4 hashes independently recomputed:

- frozen held FESC predecessor: `acfb7fee70d5a131d4a44e8962cfe3fe3cd22104bf9cf8fa00bbbd6c2c00cbc0` (10,056,847 bytes);
- MZR census comparison lane: `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b` (9,539,823 bytes);
- BrightEnd comparison lane: `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8` (9,812,969 bytes).

Opening custody trees:

| Root | Files | Bytes | Opening tree SHA-256 |
|---|---:|---:|---|
| exact candidate | 629 | 150,934,381 | `93c878e9327917e6ae1e6a29dc5fcf70dae828c5eb675d689d01d39436e36161` |
| held predecessor | 104 | 83,154,592 | `0a41cfbf830bdc1fa4fddcfb1a50ab6cbeb82267ac1c60f99feb546faefd2add` |
| MZR census | 141 | 84,918,843 | `d91eaf6284b15c5706440427611a24bc35f88e458db984f9c2b143b2eb488351` |
| BrightEnd | 106 | 80,952,468 | `14784aef86257d1b7de77c30bdad72c9359e10af46a4c51b6a98eedffcf3e612` |

The same four trees matched again after all replay work and before writing this packet. Closing values are recorded in the final custody section below.

## External gates remain closed

Candidate-local receipt/freeze gates are all `false`: upload, cockpit/video-root copy, Git, and `video_reportable_now`. `CORRECTION.json` also records `false` for upload, publication, frontend public, `paperVideos`, cockpit, database, deploy/restart, and Git. Spec and build each keep `video_reportable_now=false`.

The top correction receipt remains intentionally pre-promotion: independent-review-complete, promoted, reportable, upload, frontend-public copy, `paperVideos` copy, cockpit, database, deploy/restart, and Git commit/push/merge are all `false`. This review packet does not edit that receipt or open any of those gates.

Independent current-state checks found:

- candidate exact filename anywhere outside its frozen directory: `0`;
- candidate exact hash among MP4s under discovered public/shared roots: `0`;
- candidate exact filename under those roots: `0`;
- target-lane renderer/QA/build processes: `0`.

The correction receipt's recorded repository gate says `frontend_public_tracked_diff=false` and `pipeline_process_active=false`. Per the review prohibition, I did not invoke Git and therefore do not independently restate its recorded HEAD as a new Git observation.

## Final decision rule

The prior `acfb7fee…` HOLD concerned eight decorative icons that encoded readable rising/falling intersections. For exact candidate `4c811599…`, all eight records are the non-graph `paired_strokes` primitive; the curve icon branch is absent; validation rejects curve; the hash-bound full-frame and exact-time visuals show no crossing/order/result geometry; all 30 encoded checks survive independent replay; numeric/source/audio/provenance contracts close; pinned predecessor/other-lane bytes remain fixed; and external gates remain shut.

Therefore the exact-hash disposition is **PASS**. A byte change, a gate opening, or any later replacement would require a new hash and a new review.

## Final custody recomputation

Closing recomputation after the replay and initial packet write found **all four protected trees byte-for-byte identical to opening**:

| Root | Closing files | Closing bytes | Closing tree SHA-256 | Equals opening |
|---|---:|---:|---|---|
| exact candidate | 629 | 150,934,381 | `93c878e9327917e6ae1e6a29dc5fcf70dae828c5eb675d689d01d39436e36161` | yes |
| held predecessor | 104 | 83,154,592 | `0a41cfbf830bdc1fa4fddcfb1a50ab6cbeb82267ac1c60f99feb546faefd2add` | yes |
| MZR census | 141 | 84,918,843 | `d91eaf6284b15c5706440427611a24bc35f88e458db984f9c2b143b2eb488351` | yes |
| BrightEnd | 106 | 80,952,468 | `14784aef86257d1b7de77c30bdad72c9359e10af46a4c51b6a98eedffcf3e612` | yes |

The initial packet before this closing paragraph was 20,256 bytes with SHA-256 `28a918d13ce3773c74f16550b9b74d56905e6e07a2cf0a3f94c76f55e44a6b57`. This paragraph is the only subsequent edit; a final post-edit custody replay again verified the same four protected tree hashes. No candidate, predecessor, comparison-lane, receipt, public, or sibling artifact was changed. The only persistent artifact created or modified by Goru is `reviews/GORU_FESC_PRIMITIVE_CORRECTION_REREVIEW_4c811599.md`.
