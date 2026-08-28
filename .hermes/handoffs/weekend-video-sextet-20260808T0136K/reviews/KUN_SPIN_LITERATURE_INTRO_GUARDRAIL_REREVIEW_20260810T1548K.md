# KUN — Spin Literature Intro Guardrail Rereview

Request ID: `KUN_SPIN_LITERATURE_INTRO_GUARDRAIL_REREVIEW_REQUEST_20260810T1548K`  
Filed: 2026-08-10 16:01 KST  
Verdict: `PASS_GUARDRAILS_EXACT_HASH`

## Exact Bytes Bound

Candidate:

- MP4: `integrator/canaries/spin-literature-intro-canary-20260810T1535K/spin-literature-intro-canary-20260810T1535K.mp4`
- SHA-256 at review start: `fe04bed4605c8ee75b0641ff44c12d61990f388858f97f78103fef3c073678ed`
- SHA-256 at review close: `fe04bed4605c8ee75b0641ff44c12d61990f388858f97f78103fef3c073678ed`
- Container: h264 1920x1080 30 fps + AAC mono 48 kHz, format duration `280.565000s`

Freeze and manifest:

- `CANDIDATE_FREEZE.json`: `44a8a5167a0c630495beb6fcd02082048db442a034cbd4b0c8456434868f05ee`
- `FILE_MANIFEST.json`: `43ffcd00b0a16d90e263ca58f9b20732f1d7c5b6266f1998294a1357a547f57b`
- Manifest payload recomputed: 139 entries / 120,930,574 bytes; missing `0`; hash/size mismatches `0`
- Candidate directory file count observed: 141 files before this report; I wrote nothing inside the candidate directory

Prior HOLD remains preserved:

- Prior Kun report: `00670f4a67c0afaf4975779fab0b5d59492e89eaec5504aa05d0c438b93d3714`
- Prior held MP4: `cfb9b1fabb7d4fb46009319d45d33931bf108917f317a184e4074e6f471d968d`

## Corrected Blockers

1. **Scientific typography is corrected in encoded frames.**
   - Longo frame `encoded_qa/frames/i05l-050.928.jpg` at `00:50.928`: `−0.0408±0.011` is clean; `7.9×10⁻⁴` shows U+207B minus at superscript height in both the card and caption; no baseline hyphen, tofu, clipping, or illegibility observed.
   - Shamir frame `encoded_qa/frames/i05s-067.938.jpg` at `01:07.938`: `z<0.3` is clean; `P<5.8×10⁻⁶` shows U+207B minus at superscript height in both the card and caption; no baseline hyphen, tofu, clipping, or illegibility observed.
   - Renderer binding verified: `build.py` uses `/System/Library/Fonts/Supplemental/STIXTwoText.ttf`, and `encoded_qa.json` records `scientific_unicode_font_is_stix_two_text: true`.

2. **Frame receipt is corrected and independently matches current bytes.**
   - Required derivation: `ceil(280.5652083333333 × 30) = 8417` raw frames submitted.
   - Independent `ffprobe -count_frames`: `nb_frames=8416`, `nb_read_frames=8416`, video stream duration `280.533333s`.
   - Full ffmpeg decode to null completed successfully with `frame=8416`.
   - `build_receipt.json` now records legacy `frame_count: 8416`, plus `raw_frames_submitted: 8417` and `encoded_video_frames: 8416`.
   - Audio-master minus encoded-video duration is `0.03187533333328929s`, nonnegative and under one 30-fps frame (`0.03333333333333333s`).

## Reconfirmed Guardrails

- The three literature narration suffixes are byte-for-byte exact against the required anchors:
  - `i05l` suffix exact after prefix `Longo reported: `
  - `i05s` suffix exact after prefix `Shamir reported: `
  - `i05d` suffix exact after prefix `Land and colleagues reported: `
- `i05u` states: `These studies reported incompatible answers, so the literature remains disputed; this video adopts none of them as its finding.`
- The encoded intro frames keep attribution and non-adoption: `REPORTED CLAIM` / `REPORTED NULL`, `ATTRIBUTED TO ANOTHER STUDY · NOT THIS VIDEO'S FINDING`, `CLAIMED · DISPUTED · UNSETTLED`, `NO ANSWER SELECTED`, and `no winner`.
- Land's null is not presented as the settled answer.
- No result claim by this video found outside the permitted conditional Longo stakes sentence and attributed literature quotes.
- Five-beat opening arc remains intact: isotropy expectation, tidal-torque origin, conditional stakes, attributed literature dispute, sorting-bias handoff.
- `WHY IT MATTERS` is the active rail before `MIRROR TEST`; `NO ANSWER SELECTED` remains visible.
- The conditional Longo stakes sentence is unchanged.
- `s02` through `s24` match the predecessor `narration_script_v4.json` for `section`, `text`, and `visual_action`; mismatches `0`.
- `forbidden_icon_primitives: ["curve"]` is present; `encoded_qa.json` records `generic_curve_dispatch_absent: true`.

## Forbidden Alternate-Cosmology Scan

I did not inspect or use the superseded draft.

Rendered-content scan:

- SRT: no forbidden alternate-cosmology subject hit.
- `storyboard_v5_final.json`: no forbidden alternate-cosmology subject hit.
- `encoded_qa/ocr.txt`: no forbidden alternate-cosmology subject hit; `encoded_qa.json` records `forbidden_hits: []`.
- Encoded intro/contact frames inspected: no forbidden beat or visual.

The only excluded-topic text hit in `narration_script_v5.json` is authority metadata (`no BHU`, Lana filename), not rendered narration/card content.

## Audio / Intelligibility

- Voice/speed: `alloy`, `1.18`.
- Delivered WPM: `115.00000375287189`, inside `105-125`.
- Max A/V start delta: `0.015333333333333421s`, inside `0.3s`.
- Independent astats on encoded MP4: peak level `-2.316897 dB`, RMS `-21.955134 dB`, NaNs `0`, Infs `0`; no clipping indicated.
- Independent ebur128 summary: integrated loudness `-20.8 LUFS`, true peak `-2.3 dBFS`, LRA `6.7 LU`.
- Embedded ASR in `encoded_qa.json` is `PASS` and hears:
  - `z less than 0.3`
  - `p less than 5.8 times 10 to the minus sixth`
  - no equality wording detected.

## Custody / Gates

- Predecessor MP4 remains byte-exact: `4d230cc0efca0eb68a8d027d614b6b7e500590cff06154f1514d4402a84d7078`
- Predecessor script remains byte-exact: `5df1d0a20e1feede746a82cd784ecd43c5cd1f21ebcc74d5418cbb87d69e90f1`
- No MP4 under `/Users/duhokim/HermesOps/cockpit/videos` has the new candidate hash `fe04bed4...`.
- Five current cockpit review copies remain at their expected hashes:
  - spin: `4d230cc0efca0eb68a8d027d614b6b7e500590cff06154f1514d4402a84d7078`
  - fesc: `01a4249beb2351fa25b2d2863eecb59b98dd68a53ced1dcc484ce6b723f45660`
  - brightend: `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8`
  - mzr-anchor: `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`
  - mzr-census: `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b`

No acceptance label is written. `video_reportable_now` remains false.

KUN_SPIN_LITERATURE_INTRO_GUARDRAIL_REREVIEW_DONE
