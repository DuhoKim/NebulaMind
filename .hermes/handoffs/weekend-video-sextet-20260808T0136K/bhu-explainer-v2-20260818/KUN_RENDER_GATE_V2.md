PASS_RENDERED_EXPLAINER

# Render Gate Verdict — BHU explainer v2

Kun, 2026-08-18 KST.

## Scope Checked

Gated pinned local artifact, verified from the artifacts themselves:

- `build/BHU_EXPLAINER_V2_LOCAL_REVIEW.mp4`
- SHA-256 re-hashed by me: `fba0964cce7c3734c48df070dfcd5f055aa5ce7b5ff9fc0ac15342a408359de5` — matches the pin and FREEZE.json.
- Size: 11,732,365 bytes — matches FREEZE.json.
- Container probed by me (ffprobe 8.1.2): QuickTime/MP4, 1920x1080, 30 fps, duration 341.300 s,
  h264 High video (10,239 frames), aac LC mono 48 kHz audio, embedded `mov_text` English subtitle
  stream (133 packets). Duration matches FREEZE `duration_seconds: 341.3`.
- Freeze status: `FROZEN_LOCAL_ONLY_READY_FOR_KUN_REVIEW`.

## Safety Block (FREEZE.json)

Confirmed directly from the JSON, not from receipts:

- `publication_state: LOCAL_ONLY_NOT_UPLOADED`
- `video_generation_services: []`
- `flow_used: false`
- `veo_used: false`
- `credits_spent: 0`

No upload, publication, visibility change, credit spend, or external portal access performed by me
either. All six gated inputs (SCRIPT.md, STORYBOARD.json, VISUALS.md, CLAIM_LEDGER.md,
KUN_PACKET_GATE_V2.md, SEXTET_BRIEF_V2.md) re-hashed OK against the freeze manifest.

## Embedded Captions vs Gated Script

I extracted the embedded mov_text stream from the final MP4 myself (`-map 0:s:0`, 66 cues) and
diffed cue payloads against the narration sentences parsed from the gated `SCRIPT.md`
(10 panels, 66 sentences).

- Count parity: 66 == 66.
- Exact payload mismatches: 0. Every embedded caption payload is byte-identical to the
  corresponding SCRIPT.md sentence, including the two sentences ending in the quoted `or.`
  and all uncertainty quantifiers.
- My extraction's payloads are identical to the QA's `encoded-captions.srt` extraction.
- QA `caption-payload-qa.json` status `PASS_EXACT_ENCODED_CAPTION_PAYLOADS` is consistent with
  my independent diff; its file hash matches the freeze inventory.

## ASR Word-Diff and Targeted Adjudication

`build/qa/.../asr-word-diff.json` (hash matches freeze inventory):

- Status: `PASS_EXACT_ASR_WORD_DIFF_WITH_TARGETED_CONTEXT_ADJUDICATION`.
- Aggregate word errors after declared representational normalization: 0, over 674 expected words.
- Card-context residual errors before adjudication: 2, both on Panel 08:
  `red -> read` ("He-red-giant") and `A -> The` (sentence-initial article in the 19.3% sentence).
- The adjudication adjudicates rather than erases: Panel 08 was re-transcribed sentence-by-sentence
  in 9 sentence windows (c08s01..c08s09). The sentence-window transcripts genuinely differ from the
  card-context transcript at exactly the two disputed loci (`He-Red Giant caveat`,
  `A 19.3% difference`), resolving both in favor of the expected words; the other 7 windows confirm
  the card-context transcript. All 9 adjudication audio files exist and hash-match the report, and
  the card-08 context audio hashes match as well. The corrected loci are visible in the report;
  nothing was silently normalized away.
- The declared normalization policy is bounded: case/punctuation, quote/dash forms, UK/US
  programme spelling, digit/spoken-number and ±/percent forms, observed phonetic spellings for
  Brown–Lee–Rho / Brown–Bethe, homophonic spelling of the quoted logical word "or", astronomical
  identifier spacing, and re-measure word-boundary forms. The forbidden list (negation removal,
  arbitrary homophones, scientific-name substitution, claim paraphrase) has zero hits. I confirmed
  the only proper-name renderings in the effective transcripts are the declared phonetic spellings
  (Li/Rowe, Brown-Betha, Brownlee row).

## Forbidden-Affirmation Sweep and Not-Count Parity

Verified independently from the report's per-record texts, not just its counters:

- Not-count parity: expected 9, transcript 9 — confirmed by my own recount over the expected and
  effective transcripts (report values match).
- Dropped-negation sweep: 0 hits. For every expected sentence containing a negation, the
  corresponding effective transcript sentence preserves a matching negation token. No bounded
  verdict ("not falsified", "not refuted", "does not clear", "did not individually falsify",
  "did not discover") was strengthened into an affirmation.

## Frame Spot-Checks vs Card Audit

- All 10 frozen decoded frames and all 10 source cards re-hashed OK against the freeze inventory.
- Heading QA: all 10 script headings project exactly onto renderer headings; decoded heading crops
  match source pixels. I spot-checked card 01 by decoding a frame myself at t=17 s: heading reads
  exactly "This specific chain fails its own second neutron-star test"; visible lines are bounded
  (DUHO'S PERSONAL SIDE-INTEREST / NOT A NEBULAMIND RESEARCH PROGRAMME / SEALED RULE → PUBLISHED
  PULSAR MEASUREMENTS / HEAVY-STAR TEST — SERIOUS DOUBT / BINARY TEST — CHAIN FAILS). No text
  claims the whole BHU family is falsified, Smolin's hypothesis refuted, or that we measured or
  discovered the stars.
- Card 07 (decoded myself at t=213 s): heading "The binary test fails the chain by a wide margin";
  shows PSR J1913+1102, 1.599 ± 0.008 vs 1.290 ± 0.008, SOURCE LIMIT: 4%, MEASURED DIFFERENCE:
  19.3 ± 0.7%, NEARLY 5 TIMES THE THRESHOLD, PUBLISHED 2020 · SHARPENED 2026 — matches the card
  audit's closed-world text list exactly.
- Card 06 uncertainty geometry (the key check, verified on the frozen decoded frame with my own
  pixel measurement): dashed 2.00 threshold line at y≈460–463; the hard 68.3% interval (drawn
  purple in this palette) lower cap at y=443, i.e. visibly above the 2.00 line; the soft 95.4%
  halo decays below the line to about y≈503 with no hard lower endpoint drawn. This matches the
  audit's `panel_06_geometry` block (`strict_95_4_visual_crosses_threshold: true`,
  `strict_95_4_hard_lower_endpoint_drawn: false`) and the intended truth: PSR J0740+6620 clears
  2.00 at 68.3% but not at the stricter 95.4% standard. It does not draw 2.08 ± 0.07 itself
  dipping below 2.00.

## Verdict Basis

The pass rests on: my own re-hash of the candidate; my own container probe; my own extraction and
exact diff of the embedded captions against the gated script; structural verification plus
targeted re-verification of the ASR word-diff artifacts (including that the Panel 08
sentence-window adjudications resolve real context-window ASR errors in favor of the expected
words rather than erasing differences); an independent not-count and dropped-negation sweep; and
my own decoded-frame spot-checks of cards 01, 06, and 07 against the card audit. Freeze inventory
hashes for every QA artifact I relied on re-verified OK.

This artifact passes the gate as a local review object. Publication, upload, visibility change,
and any credit spend remain separate explicit gates. portal.nersc.gov was not touched.
