PASS_RENDERED_EXPLAINER

# KUN RENDER GATE — BHU theory-closure explainer

Gate seat: Kun. Date: 2026-08-18. Mode: findings-only, verified from artifacts, no edits, no network.
Candidate: build/BHU_THEORY_CLOSURE_VIDEO_LOCAL_REVIEW.mp4
Pinned SHA-256: 26626fc26ee7cfc31f3ce0b8c720588ed4150b195e9454c743b4c91fd6a7988e

## 1. Hash — PASS

Re-hashed the MP4 myself (shasum -a 256). Actual:
26626fc26ee7cfc31f3ce0b8c720588ed4150b195e9454c743b4c91fd6a7988e
Exact match to the pin. 11,421,533 bytes, matching FREEZE.json and the assembly receipt.

## 2. Container / duration — PASS

Probed live with ffprobe/ffmpeg (not from receipts):
- Stream 0: h264 (High), 1920x1080, 30 fps, 9,852 frames, duration 328.400 s
- Stream 1: aac LC, 48 kHz mono, duration 328.400 s
- Stream 2: mov_text subtitle (tx3g), eng, 107 cues, duration 327.620 s
- Format: mov/mp4, probe_score 100 (per receipt); my probe confirms stream set and durations.
- Full-decode sweeps run by me: `ffmpeg -map 0:a:0 -f null -` clean; `-map 0:v:0 -f null -` clean. No decode errors anywhere in the file.

## 3. Embedded captions vs SCRIPT.md — PASS

Extracted the mov_text stream directly from the MP4 to SRT myself and diffed every cue
payload against the narration sentences in the gated SCRIPT.md (fdfa1ccf... per FREEZE):
- 53 encoded cues, 53 SCRIPT.md narration sentences.
- 0 payload mismatches after whitespace normalization (exact sentence-for-sentence equality).
Receipt caption-payload-qa.json (PASS_EXACT_ENCODED_CAPTION_PAYLOADS, 53/53 SRT+VTT exact)
corroborates; my extraction is the primary evidence. Encoded SRT/VTT artifact hashes verified.

## 4. ASR word-diff + targeted adjudication — PASS

Audited build/qa/candidate-26626fc2.../asr-word-diff.json and ASR_WORD_DIFF.md against
the artifacts:
- Status PASS_EXACT_ASR_WORD_DIFF_WITH_TARGETED_CONTEXT_ADJUDICATION; aggregate word errors 0
  across 721 expected words; 10/10 panels pass.
- Negation guard: expected_not_count 8 == transcript_not_count 8; forbidden_affirmation_hits [].
- Normalization policy is declared and bounded (case/punct, number forms, proper-name token
  boundary); forbidden classes include negation removal, arbitrary homophones, scientific-name
  substitution, claim paraphrase — none triggered.
- Panel 01 had 2 residual card-context word errors ("nebulamind" heard as "nebula mind").
  This was adjudicated, not erased: the card-context difference is still recorded verbatim in
  the JSON, and resolution came from 6 targeted sentence-window re-ASR passes
  (c01s01..c01s06). I verified all 6 adjudication audio artifacts exist and hash-match their
  recorded SHA-256s; all 6 sentence windows show zero differences.
- All 10 full-panel decoded card-audio .m4a artifacts hash-match their recorded SHA-256s.
- Card-01 effective transcript carries the adjudicated "nebula-mined" homophone, covered by
  the declared "NebulaMind proper-name token boundary and mined homophone" allowance.

## 5. Decoded frames vs card audit — PASS

Independently decoded frames from the candidate MP4 with ffmpeg and inspected them:
- Panel 06 (grabbed at t=170s, mid-segment): encoded pixels carry all 8 approved strings
  verbatim — heading "Our 100,000-galaxy design needs about 1 extra in 100",
  "COUNTING YARDSTICK · 100,000 GALAXIES", "NEEDED · ABOUT 1 IN 100",
  "ALLOWED · ABOUT 5 IN 10 MILLION", "MORE THAN 10,000 TIMES TOO SMALL",
  "FINITE-SAMPLE NOISE REMAINS", plus ladder callouts "NEEDED (~1/100)" and "ALLOWED (~5/10M)".
  Ladder crop shows the 4 complete tenfold step blocks with honest log spacing. Per the source
  card and BUILD_REPORT, the step blocks are graphical (no ×10 text on ticks by design);
  NEEDED/ALLOWED are the closed-world endpoint labels. Matches the audit's panel_06_geometry
  (6 tenfold ticks, 4 explicit step blocks, unlabeled_log_spacing_used=false).
- Panel 03 (grabbed at t=80s; note first grab at t=120s lands in panel 04 because segments
  02/03/07/08/09/10 carry timing extensions in the assembly receipt — expected, not a defect):
  encoded pixels carry heading "The proposed test is a 2-jar galaxy count",
  "JAR 1 · CLOCKWISE", "JAR 2 · COUNTERCLOCKWISE", "COMPARE THE TOTALS",
  "REAL IMBALANCE MUST BEAT COUNTING NOISE", "THE MISSING PIECE · SIGNAL SIZE", and the
  annotation "Counting noise floor = 1/√N" verbatim, radical included.
- Pixel-level: my decoded frames vs the source cards measure RMS 3.48 (card-03) and 3.99
  (card-06) over full RGB frames — consistent with H.264 lossy noise on a static card, and
  consistent with the QA's heading-crop RMS ~1.36–1.43. No semantic pixel drift.
- All 10 QA decoded-frame artifacts hash-match heading-and-frame-qa.json; all 10 report
  exact_text_projection=true and decoded_heading_pixels_match_source=true.
- Card audit (card-text-and-geometry-audit.json): all 10 source cards hash-match, all
  PASS_EXACT_CLOSED_WORLD, emitted_text == permitted_text on every card.

## 6. FREEZE safety block — PASS

build/FREEZE.json:
- status FROZEN_LOCAL_ONLY_READY_FOR_KUN_REVIEW.
- safety: publication_state LOCAL_ONLY_NOT_UPLOADED, video_generation_services [],
  flow_used false, veo_used false, credits_spent 0. No upload, no credits, no external
  video-generation services. BUILD_REPORT agrees ("No Veo, no Flow, no credits, no upload").
- Provenance: all 7 gated inputs hash-match (SCRIPT.md, STORYBOARD.json, VISUALS.md,
  CLAIM_LEDGER.md, LANA_ANNOTATION_REVIEW.md, KUN_TV_PACKET_GATE.md,
  SEXTET_BRIEF_THEORY_VIDEO.md); all 252 build_inventory entries hash- and size-match;
  verify_freeze.py run by me returns PASS_FROZEN_PROVENANCE_VERIFIED.
- Final QA report: PASS_LOCAL_RENDER_QA_READY_FOR_KUN_REVIEW, forbidden sweep
  ("is falsified", "we proved", "theory is dead") clean, mean/max volume -16.3/-2.2 dB,
  publication_state LOCAL_ONLY_NOT_UPLOADED, credits_spent 0.

## Verdict

PASS_RENDERED_EXPLAINER. The rendered candidate is bit-identical to the pin, the container
decodes cleanly end-to-end, all 53 caption payloads equal the gated script, decoded-audio ASR
shows zero word errors with the single context-window residual properly adjudicated through
hash-verified sentence windows (recorded, not erased), the encoded pixels carry every approved
string including panel 06's NEEDED/ALLOWED ladder and panel 03's 1/√N annotation, and the
freeze is local-only with zero credits and zero upload. This gate authorizes nothing beyond
what the kickoff states; publication remains a separate explicit approval.
