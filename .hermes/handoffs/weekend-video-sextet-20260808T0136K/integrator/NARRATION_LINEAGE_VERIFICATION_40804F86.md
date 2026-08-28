# Narration lineage verification — candidate 40804f86

Timestamp: 2026-08-08 KST
Disposition: `DISPATCH_PREMISE_CORRECTED_NO_REBUILD`

## Outcome

The request to replace candidate `40804f86…` as “pre-correction narration” was based on the preserved superseded file `narration_script.json`. The encoded candidate does not use that lineage. No new candidate was rendered because the requested three spoken corrections are already present in the actual AAC stream of the frozen MP4.

## Authority readback

`reviews/HWAO_NARRATIVE_CORRECTION.md` requires:

1. two worlds posed before the mirror, with the mirror receiving the most narrative weight and resolving them;
2. discipline framing rather than verdict/evidence/receipt/referee ticket language;
3. a close that re-poses images versus labeling process and lands on the scientific discriminant.

`reviews/LANA_OVERHAUL.md` now contains a timestamped post-build review at 14:07 KST. It explicitly corrects the dispatch premise at lines 235–241: candidate `40804f86…` binds `narration_script_v2.json`, and both the words and visuals implement the correction. Lana records all three fixes as delivered and gives narrative/claim-boundary concurrence.

## Timestamp lineage

- Preserved rejected script `narration_script.json`: 2026-08-08T13:24:14+09:00
- Corrected script `narration_script_v2.json`: 2026-08-08T13:38:20+09:00
- Corrected TTS receipt: 2026-08-08T13:44:08+09:00
- Corrected narration master: 2026-08-08T13:44:17+09:00
- Encoded MP4: 2026-08-08T13:55:06+09:00

The 13:24 file was preserved as the rejected lineage. The candidate was built after the correction from the 13:38 script and 13:44 audio.

## Build and synthesis binding

`build.py` reads:

- `audio_v2/timeline.json`
- `audio_v2/narration_master.wav`

`build_receipt.json` records:

- revision `v2-hwao-narrative-correction`;
- script `narration_script_v2.json`, SHA-256 `3f033dd02d00767c6bb4cc1baf8b7197a78847bad076411cbaed9aab732cd416`;
- master `audio_v2/narration_master.wav`, SHA-256 `e3fffb1d275657aeed183d2d76b4c4656782c2e33462d7be9666bd8a76bc12d8`;
- output SHA-256 `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`.

The corrected synthesis receipt records 24 fresh sentence-level Alloy calls at speed 1.18. Its spoken records include:

- s03–s10: two explanations followed by the five-sentence mirror climax and `that is the discriminant`;
- s19: `We tied our own hands so the answer cannot be shaped by choices made after seeing it.`;
- s20: specific gates as checks that must meet the frozen rules;
- s22–s24: `Ask the opening question again: images or labeling process?` through `the scientific discriminant is not.`

## Actual encoded-audio identity test

The AAC stream was decoded from the frozen MP4 to 24 kHz mono PCM and compared with both masters:

- candidate duration: 159.0187 s decoded PCM;
- corrected v2 master: 159.0000 s;
- rejected v1 master: 146.4783 s;
- normalized waveform correlation, candidate vs corrected v2: `0.999994517`;
- normalized waveform correlation, candidate vs rejected v1: `0.001885989`;
- best 30-second corrected-v2 correlation: `0.999994453` at zero-sample lag.

This directly verifies the spoken AAC, not merely the subtitles or receipt metadata.

## Preservation decision

- The frozen MP4 and every build input remain unchanged.
- The rejected v1 script/audio remain preserved in place.
- No duplicate re-synthesis or semantically identical replacement candidate was created.
- Overall state remains pending Tori/Kun post-encoded acceptance; this verification does not promote the artifact to overall PASS.
