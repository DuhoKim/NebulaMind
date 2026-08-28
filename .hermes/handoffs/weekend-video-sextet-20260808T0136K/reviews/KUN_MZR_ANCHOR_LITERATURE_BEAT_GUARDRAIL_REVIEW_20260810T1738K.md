# KUN — MZR-Anchor Literature Beat Guardrail Review

Filed: 2026-08-10 18:18 KST  
Lane: `mzr-anchor`  
Candidate: `integrator/canaries/mzr-anchor-literature-beat-motion-fix-20260810T1705K`

## Exact Bytes Bound

- MP4: `mzr-anchor-literature-beat-canary-20260810T1705K.mp4`
- MP4 SHA-256: `47f71fc40e1f81f7e4374e7e867c07cc64f8595ad553137403bff7d52dbec547`
- `RECEIPT.json` SHA-256: `4000266d46565344ac2f8900021d72555bc89c11109148a07c9083ff90df0162`
- `POST_ENCODE_FREEZE.json` SHA-256: `b2aa23206fafe50122afa68e1351b2fa4c65dce257cd21d78d8988d7a7e03419`
- Candidate file manifest independently checked: 146 entries / 91,925,307 bytes; missing `0`; hash/size mismatches `0`
- Container: h264 1920x1080 30 fps + AAC mono 48 kHz, format duration `239.348000s`

## Content Guardrails

- `CONTRACT_QA.json`: `PASS`; spot-checked evidence, not just status.
- `encoded_qa.json`: `PASS`; spot-checked encoded frames, ASR, OCR, frame count, audio, and custody.
- Lana/primary-source quote match:
  - Required sentence: `The absolute metallicity scale (y-int) varies up to 0.7 dex, depending on the calibration used.`
  - `spec.json`, Lana ruling copy, and `sources/ARXIV_0801.1849V1_EXACT_ABSTRACT.txt` match exactly.
- Encoded quote frame `i05q` at `00:35.458` shows:
  - `KEWLEY & ELLISON 2008 · REPORTED CALIBRATION DISAGREEMENT`
  - exact serif quote, readable
  - `ATTRIBUTED TO ANOTHER STUDY · NOT THIS VIDEO'S FINDING`
  - `arXiv:0801.1849v1 · exact abstract sentence`
  - running `LITERATURE CONTEXT · NO ANSWER SELECTED`
  - local `WHY IT MATTERS` rail focus
- Encoded closing frame `i05u` at `00:43.384` shows:
  - Kewley & Ellison attribution
  - `REPORTED CALIBRATION DISAGREEMENT`
  - `CLAIMED · DISPUTED · UNSETTLED`
  - `NO ANSWER SELECTED`
  - caption: `Kewley and Ellison reported disagreement among the measurement rulers; the interpretation remains disputed, and this video adopts no answer as its finding.`

No evolution result is quoted or adopted. No lane result, calibration answer, evolution answer, direction, parity, significance, or substantive finding by this video is asserted.

## Motion / Visual Safety

- Literature beat contains a card architecture copied from the validated spin pattern, not a sweeping rail/result-looking graph.
- `forbidden_curve_hardening` is true in `CONTRACT_QA.json`; `encoded_qa.json` records `generic_curve_dispatch_absent: true`.
- Motion QA reports longest near-unchanged run `0.5s`, below the 8s freeze threshold.

## Audio / Sync / Decode

- Fresh audio/timeline: `audio/timeline.json` created 2026-08-10T08:09:42Z.
- Voice route: alloy; target timing receipt: `115.0 WPM`; measured delivered WPM `114.99999647412324`.
- Sentence count `24`; word count `453`; max A/V start delta `0.014708333333331325s`.
- Raw literature ASR: `PASS`; `i05q` transcript hears the quote semantically, including `Y-intercept`, `0.7`, and `DEX`.
- Encoded-opening ASR: `PASS`; the semantic guard passes.
- Weakest point: encoded-opening ASR hears the closing author name as `Cooley and Ellison`, while the narrower literature ASR and the on-screen/caption text both correctly carry `Kewley and Ellison`. I do not hold on this because the required raw literature ASR passes, the displayed attribution is correct, and the safety role of the closing sentence remains intelligible.
- Independent full decode: pass; no ffmpeg decode error.
- Independent frame count: `nb_frames=7180`, `nb_read_frames=7180`, video stream duration `239.333333s`.
- Independent astats: peak `-2.301687 dB`, RMS `-21.601187 dB`, NaNs `0`, Infs `0`.
- Independent ebur128: integrated loudness `-20.5 LUFS`, true peak `-2.3 dBFS`, LRA `5.7 LU`.

## Custody / Gates

- `SOURCE_FREEZE.json`: absent under `lanes/mzr-anchor` in this handoff tree.
- `video_reportable_now=false`; `accepted_by_duho=false`.
- `RECEIPT.json` and `POST_ENCODE_FREEZE.json` keep `upload=false`, `cockpit_or_video_root_copy=false`, `git=false`.
- Candidate authority state is provisional, awaiting Kun/Tori/Duho; no acceptance is conferred.
- Protected predecessor remains exact:
  - `integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T1406K/...mp4`
  - SHA-256 `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`
- Protected `fesc` and `mzr-census` baseline trees: every listed path/hash/size checked; missing `0`; mismatches `0`.
- Cockpit MP4 baseline: 36/36 listed files checked; missing `0`; mismatches `0`.
- No `fesc-*literature*` or `mzr-census-*literature*` candidate directory exists at `integrator/canaries` depth.

PASS_GUARDRAILS_EXACT_HASH
