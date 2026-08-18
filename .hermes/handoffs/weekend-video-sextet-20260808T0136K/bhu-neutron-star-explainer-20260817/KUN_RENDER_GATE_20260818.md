PASS_RENDERED_EXPLAINER

# Render Gate Verdict — BHU neutron-star explainer

Kun, 2026-08-18 KST.

Requested target path was `bhu-neutron-star-explainer-20260817/KUN_RENDER_GATE_20260818.md`.
That sibling directory is readable from this sandbox but not writable, so this verdict is written
in the current writable handoff workspace instead.

## Scope Checked

Reviewed pinned local artifact:

- `../bhu-neutron-star-explainer-20260817/build/BHU_NEUTRON_STAR_EXPLAINER_LOCAL_REVIEW.mp4`
- SHA-256: `e5d6fae9436e6f66ac5825802236f4f6cba095c1e9b6676b46bc55d1bc160e18`
- Container check: 1920x1080, 30 fps, 334.100 s, h264 video, aac audio, embedded `mov_text` captions.
- Freeze status: `FROZEN_LOCAL_ONLY_READY_FOR_KUN_REVIEW`.

No upload, publication, visibility change, credit spend, or external portal access performed.

## Verdict Basis

The rendered artifact passes the gate as a local review object.

Embedded captions extracted from the MP4 match the gated script content, including the repaired
Panel 02 sentence: "Their masses can be measured through pulsar timing." The TTS timeline
reconstructs all panel narration exactly from `SCRIPT.md` and records
`tts_inputs_reconstruct_all_panel_narration_exactly: true`.

I could not independently rerun ASR: no local Whisper, faster-whisper, or speech-recognition
package is installed, and network access is restricted. I therefore did not treat Yui's ASR report
as independently rederived evidence. The pass rests on the exact embedded captions, deterministic
TTS input/timeline, and visual/card checks I could perform locally.

## On-Screen Text and Headings

The card audit emits a closed-world text list for all 8 rendered source cards, and the final video
is assembled from static card segments. I extracted encoded frames from the final MP4 and visually
checked the card set/contact sheet. Assertion headings match the script's panel headings:

1. `This specific chain fails its own second neutron-star test`
2. `This cosmic chain offered 2 checkable neutron-star tests`
3. `The famous mass-ceiling test reaches serious doubt, not strict falsification`
4. `The same paper gives an independent 4% binary test`
5. `PSR J1913+1102 exceeds the 4% limit by a wide margin`
6. `A sealed rule keeps the result from following the answer`
7. `The neutron-star prediction dies; broader ideas do not`
8. `The forgotten test had already finished`

The card text remains bounded: it does not say the whole black-hole-universe family is falsified,
does not say Smolin's hypothesis is refuted, does not claim we measured or discovered the stars,
and does not mention the 2.35-solar-mass star as supporting evidence.

The text sweep found only bounded/negated forms such as `not thereby refuted`, `not falsified`,
and `does not mean every black-hole-universe idea is false`.

## Panel 03 Uncertainty Rendering

This is the key check.

The rendered Panel 03 shows the corrected uncertainty picture, not the mistaken instruction.

Measured from the encoded MP4 frame and the deterministic card geometry:

- The dashed 2.00 threshold line is at approximately y=462-466.
- The hard green 68.3% interval runs approximately y=353-460.
- The green lower cap is therefore visibly above the 2.00 line.
- The center is 2.08, with one-sigma interval [2.01, 2.15].
- The soft purple strict-credibility halo extends below the dashed 2.00 threshold.

So the visual says exactly the intended truth: PSR J0740+6620 clears 2.00 at the quoted 68.3%
level, but does not clear 2.00 at the stricter 95.4% standard. It does not draw the 68.3% error
bar dipping below 2.00.

## Local-Only Status

The freeze and assembly records report local-only review state:

- `FROZEN_LOCAL_ONLY_READY_FOR_KUN_REVIEW`
- `LOCAL_ONLY_NOT_UPLOADED`
- `credits_spent: 0`

I performed only local reads, local frame extraction, hash/probe checks, caption extraction,
OCR/tool availability checks, and this verdict write.
