# Pass 24 encoded-frame audit — color/monochrome → 360p → JPEG q60 4:2:0

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 24  
Extraction started: `2026-08-08T13:56:18+09:00`  
Audit completed: `2026-08-08T14:04:17+09:00`

## Authority and custody

Before this pass I re-read the current `HWAO_WEEKEND_ORDER.md`, `COORDINATION_UPDATE.md`, lane `BRIEF.md`, `STATUS.json`, `SOURCE_STATUS_FREEZE.json`, preserved failed-candidate receipt/QA/hashes, sealed `STORYBOARD_PROPOSAL.json`, v8 render receipt/frames, pass-23 snapshot/guard/audit, and lane receipt.

Custody held:

- failed candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- worker source-freeze SHA-256: `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1`
- sealed storyboard remains v8
- sealed v8, pass-7 proof, and pass-12 proof were read-only
- no v9 or candidate was created

Every method contact sheet uses `GALAXY SPIN`, preserves method/status boundaries, and contains no audience-visible forbidden result/cosmology topic. Candidate 0149 remains result-bearing without a persistent structural held boundary.

## Fresh compound representation boundary

Pass 24 tests a new order-specific interaction not established by standalone pass 11, pass 17, or pass 23:

1. freshly decode each native 1920×1080 RGB midpoint;
2. preserve color or apply linear-light BT.709 grayscale / one fixed Machado severity-100 protanopia, deuteranopia, or tritanopia presentation matrix;
3. sRGB-encode and round with NumPy `rint` to uint8;
4. downscale the complete transformed canvas with Pillow LANCZOS to 640×360;
5. encode with Pillow JPEG quality 60, subsampling 2 (4:2:0), `optimize=false`, `progressive=false`;
6. decode the JPEG stream to RGB and store a lossless PNG for represented-pixel inspection;
7. independently recompute both JPEG bytes and decoded RGB pixels from the matching pass-23 baseline.

These are packet-specific presentation stresses, not clinical diagnostics or universal delivery/codec/viewing standards.

## Fresh extraction and derivatives

Candidate:

- scene cuts: `15/15`, exact pass-23 timestamps
- scenes: `16`
- fresh native midpoint custody: `16/16` byte-identical to pass 23
- pass-23 baseline reproduction: `80/80` pixel-exact
- JPEG streams: `80`
- decoded PNGs: `80`

Method proof across sealed v8, pass-7 caption-safe, and pass-12 strengthened groups:

- source scenes: `21`
- pass-23 baseline reproduction: `105/105` pixel-exact
- JPEG streams: `105`
- decoded PNGs: `105`

## Candidate incremental quantitative result

Metrics compare each decoded JPEG with its exact matching pass-23 360p baseline.

| Variant | Headline | Full text | Lower support | Numeric | Edge recall | RGB PSNR dB | RGB MAE | Structural gates |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| color → 360p → q60 | 0.986033 | 0.928357 | 0.744065 | 0.833333 | 0.996873 | 34.591880 | 2.371461 | 0/16 |
| grayscale → 360p → q60 | 0.988586 | 0.950012 | 0.955303 | 0.862202 | 0.996758 | 35.443069 | 2.113119 | 0/16 |
| protanopia → 360p → q60 | 0.997500 | 0.945956 | 0.821821 | 0.886285 | 0.996946 | 34.854627 | 2.059178 | 0/16 |
| deuteranopia → 360p → q60 | 0.994106 | 0.935846 | 0.763296 | 0.818750 | 0.996991 | 34.701398 | 2.213140 | 0/16 |
| tritanopia → 360p → q60 | 0.993870 | 0.915066 | 0.859779 | 0.844940 | 0.997335 | 34.708860 | 2.123171 | 0/16 |

For held-critical scenes 7, 9, 10, 11, and 16, structural held/status gates remain `0/5` under every variant. Exact JPEG byte-stream and decoded-RGB recomputation pass `16/16` per variant.

Human represented-pixel review finds:

- large result headlines, numbers, plots, bars, matrices, and conclusions remain primary;
- fine axes, error bars, legends, caveats, citations, provenance, and small support weaken first;
- plot/bar/matrix geometry and labels remain present, but small label reliability is uneven;
- recompression causes no new clipping, overlap, category-boundary ambiguity, or meaning change;
- no transform adds a persistent held gate or repairs/authorizes the candidate.

## Method proof

Across all five compound variants:

- sealed-v8 complete `RESULT HELD` badges: `7/7`
- sealed-v8 major method/status boundaries: `7/7`
- pass-7 exact top gates and complete badges: `7/7`
- pass-12 exact top gates and complete badges by represented-pixel review: `7/7`
- exact JPEG streams and decoded RGB pixels: `7/7` per variant
- hue-only required meaning: `0`
- compression-caused clipping, overlap, or ambiguity: none

Pass-12 mapped-crop OCR aid at threshold 0.80:

- color: mean `1.000000`, `7/7`
- grayscale: mean `0.994898`, `7/7`
- protanopia: mean `1.000000`, `7/7`
- deuteranopia: mean `1.000000`, `7/7`
- tritanopia: mean `0.952139`, `6/7`
- disclosed miss: tritanopia scene 2, similarity `0.729730`

Direct represented-pixel review is decisive: scene 2's complete top-gate container and exact text `OVERLAPPING READOUTS · DO NOT SUM` remain directly readable. The single OCR-aid miss does not evidence a missing or ambiguous gate.

## Evidence-backed action

Action: `INTEGRATION_GUARD_NOT_PIXEL_CORRECTION`

`COLOR_MINIMUM_SCALE_RECOMPRESSION_GUARD_PASS24.json` adds the narrow compound requirement: future Hwao-authored layouts must preserve exact gates, complete badges, direct labels, and compression-resilient non-color geometry after the full declared transform chain. Hue, fine chroma edges, small axes/error bars, tiny legends/caveats/citations/provenance, and one-pixel rules cannot solely carry required scientific or status meaning. Exact JPEG bytes and decoded RGB pixels must be reproducible.

No pixel or copy correction is evidence-justified: direct review retains 7/7 exact gates, 7/7 badges, complete containers, and non-color structure across every variant.

## Exact blockers unchanged

- no valid independent post-run A3.8 review exists for the exact frozen all-209-file T4 artifact;
- `KUN_FRAME_REVIEW.md` still ends `FRAME REVIEW: AGREES FRAME_UNSTATED`;
- `video_reportable_now` remains `false`.

No science was invented or adjudicated.

## Safety

- no TTS or audio
- no video encoding or publication
- no shared/public asset modification
- no Git action
- all writes confined to `lane-spin-parity/worker-yui`
