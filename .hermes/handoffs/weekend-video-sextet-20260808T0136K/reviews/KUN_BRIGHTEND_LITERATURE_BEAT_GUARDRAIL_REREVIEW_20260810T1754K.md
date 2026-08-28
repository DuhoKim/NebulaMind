# KUN — Brightend Literature Beat Guardrail Rereview

Filed: 2026-08-10 18:27 KST  
Lane: `brightend`  
Candidate: `integrator/canaries/brightend-literature-beat-typography-fix-20260810T1748K`

## Exact Bytes Bound

- MP4: `brightend-literature-beat-canary-20260810T1748K.mp4`
- MP4 SHA-256: `6483525852a5fafbb41d82e4c9fba0dc7e98b4f8b7599007e2af0a379ef49dd7`
- Prior HOLD report SHA-256: `c86f62e6eb5bb5dfb4a7b06e7f5a465832c8036736c05e4620702422e2f896b7`
- Prior held MP4 SHA-256: `49f1fe3dcf3fed69d0269c24fefddb67c45f6d558e34727d4b7ee5b823abc05d`
- `RECEIPT.json` SHA-256: `a8ebc87b69b087acb743d1ba21ce7098438c244e8712515c41e9bc5b7857b01c`
- `POST_ENCODE_FREEZE.json` SHA-256: `0584917ae4d38f07122203654612df28f133ed415fbbb36638bec4975272821c`
- `encoded_qa.json` SHA-256: `652500417045407b9ff2eb5824f57dd3aae2fc84fbd9ab57b6de5d90c37331b2`
- Candidate file manifest independently checked: 152 entries / 104,097,164 bytes; missing `0`; hash/size mismatches `0`
- Container: h264 1920x1080 30 fps + AAC mono 48 kHz, format duration `273.782000s`

## Prior HOLD Disposition

The prior HOLD was specific: New York serif made the range hyphen in `z∼7-10` visually disappear in the encoded long quote and caption.

I inspected a fresh frame extracted from this exact MP4 at `00:51.896`, not only the candidate-provided QA PNG. The corrected `i05b` card now renders:

- `z∼7-10` with the relation glyph visible and the range hyphen clearly visible between `7` and `10`
- `ΛCDM` with a visible lambda, no tofu box or clipping
- the same correction visible in the bottom caption
- header `BOYLAN-KOLCHIN 2023 · REPORTED UNRESOLVED HEDGE`
- footer `ATTRIBUTED TO ANOTHER STUDY · NOT THIS VIDEO'S FINDING`
- source line `arXiv:2208.01611v2 · exact abstract sentence`
- running rail `LITERATURE CONTEXT · NO ANSWER SELECTED`

The prior typography blocker is fixed on the encoded artifact.

## Guardrail Review

- `CONTRACT_QA.json`: `PASS`; I spot-checked the underlying checks, not just the status.
- Exact source sentences: the two Boylan-Kolchin abstract sentences in `spec.json`, `sources/ARXIV_2208.01611V2_EXACT_ABSTRACT.txt`, and Lana's ruling copy match the required text, including `z∼7-10` and `ΛCDM`.
- Literature framing remains attributed and disputed: `i05a` says `REPORTED EXCESS CLAIM`; `i05b` says `REPORTED UNRESOLVED HEDGE`; `i05u` says `REPORTED CLAIM · UNRESOLVED CAUSE`, `CLAIMED · DISPUTED · UNSETTLED`, and `NO ANSWER SELECTED`.
- The closing sentence remains: `Boylan-Kolchin reported these claims and left the issue unresolved; the field remains contested, and this video adopts neither claim nor explanation as its finding.`
- No adopted result, archive-gap result, excess adoption, explanation, direction, parity, significance, or substantive finding by this video is asserted. Search hits for `significance`, `dipole`, and `parity` were only the explicit forbidden-term list in `spec.json`.
- `forbidden_curve_hardening=true`; no result-looking curve rail is used for the literature beat.
- `SOURCE_FREEZE.json` remains absent under `lanes/brightend`; this stays method-only and cannot report a substantive result.

## Audio / Sync / Decode

- Independent full decode: pass; ffmpeg completed with no decode error.
- Independent frame count: `nb_frames=8213`, `nb_read_frames=8213`, video stream duration `273.766667s`.
- Audio stream: AAC mono 48 kHz, present and intelligible by encoded-opening ASR.
- Encoded-opening ASR: `PASS`, similarity `0.9980657640232108`; it hears the long quote as `z approximately 7 to 10` and `Lambda CDM`, and preserves the no-finding close.
- Delivered speech timing: 25 sentences / 519 words; delivered WPM `115.0000019234372`, inside 105-125.
- Max A/V start delta: `0.016208333333310065s`, inside the 0.3s requirement.
- Sampled sentence-action starts:
  - `i01`: audio `0.600s`, visual `0.600s`, delta `0.000s`
  - `i02`: audio `8.526s`, visual `8.533s`, delta `0.007s`
  - `i03`: audio `16.284s`, visual `16.300s`, delta `0.016s`
  - `i05a`: audio `35.210s`, visual `35.200s`, delta `-0.010s`
  - `i05b`: audio `42.800s`, visual `42.800s`, delta `0.000s`
  - `i05u`: audio `61.742s`, visual `61.733s`, delta `-0.008s`
- Independent astats: peak `-2.653976 dB`, RMS `-21.385943 dB`, NaNs `0`, Infs `0`; no clipping indication.
- Independent ebur128: integrated loudness `-20.3 LUFS`, true peak `-2.7 dBFS`, LRA `6.0 LU`.

## Custody / Gates

- `RECEIPT.json` status: `LOCAL_SELF_QA_PASS_PROVISIONAL_NOT_ACCEPTED`.
- `POST_ENCODE_FREEZE.json` status: `PROVISIONAL_LOCAL_SELF_QA_PASS_FROZEN_AWAITING_KUN_TORI_DUHO`.
- Gates remain false: `upload=false`, `cockpit_or_video_root_copy=false`, `git=false`, `video_reportable_now=false`, `accepted_by_duho=false`.
- Protected predecessor `brightend-method-overhaul-canary-20260809T1345K` remains bound by SHA-256 `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8`.
- Protected fesc/mzr-census baseline trees: every listed root-relative path/hash/size checked; missing `0`; mismatches `0`.
- Cockpit MP4 baseline: 36/36 listed root-relative files checked; missing `0`; mismatches `0`.
- No `fesc-*literature*` or `mzr-census-*literature*` candidate directory exists at `integrator/canaries` depth; the scope remains brightend-only for this rereview.

Weakest thing: ASR normalizes the scientific symbols to spoken equivalents (`z approximately 7 to 10`, `Lambda CDM`) and hears `Boylan Colchin` without the hyphen, so machine transcript exactness is weaker than the rendered/source exactness. This is not a blocker because the card/caption and source text carry the exact glyphs and attribution, and the audio remains intelligible.

PASS_GUARDRAILS_EXACT_HASH
