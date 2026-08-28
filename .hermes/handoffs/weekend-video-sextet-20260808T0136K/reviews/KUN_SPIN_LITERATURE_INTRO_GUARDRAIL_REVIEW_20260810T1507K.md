# KUN — Spin Literature Intro Guardrail Review

Request ID: `KUN_SPIN_LITERATURE_INTRO_GUARDRAIL_REQUEST_20260810T1507K`  
Filed: 2026-08-10 15:26 KST  
Verdict: `HOLD_GUARDRAILS_EXACT_HASH`

## Exact Bytes Bound

Candidate:

- MP4: `integrator/canaries/spin-literature-intro-canary-20260810T1434K/spin-literature-intro-canary-20260810T1434K.mp4`
- SHA-256 at review start: `cfb9b1fabb7d4fb46009319d45d33931bf108917f317a184e4074e6f471d968d`
- SHA-256 at review close: `cfb9b1fabb7d4fb46009319d45d33931bf108917f317a184e4074e6f471d968d`
- Container: h264 1920x1080 30 fps + AAC mono 48 kHz, duration `280.565000s`

Freeze and manifest:

- `CANDIDATE_FREEZE.json`: `cf23013350cf4e62e7c76714d73cb6f761b22fd3f6b6e6073149b1ec1ccd1c4d`
- `FILE_MANIFEST.json`: `4603591b148b8aee911313fc17d8c54894c13ae0ae5b1c643a2a749bb2859530`
- Manifest payload recomputed: 138 entries / 121,041,612 bytes; missing `0`; hash/size mismatches `0`
- Candidate directory file count observed: 140 files before this report; I wrote nothing inside the candidate directory

Authorities:

- Lana Part 1 authority file: `reviews/LANA_SPIN_BEAT4_AND_BHU_ASSESSMENT_20260810.md`
  - SHA-256: `88d02d4df045df8249be5ea0d0d817633aa27476265a65ae20bdfec0b4fd40f2`
- A1 withdrawal: `lanes/spin/SOURCE_FREEZE_AMENDMENT_A1_WITHDRAWN_20260810T1424K.md`
  - SHA-256: `7eb5c37ead54863428a6f452462182c2f6230607735483058af39155fca8b891`

Predecessor:

- Requested predecessor MP4 SHA-256 recomputed: `4d230cc0efca0eb68a8d027d614b6b7e500590cff06154f1514d4402a84d7078`
- Requested predecessor script SHA-256 recomputed: `5df1d0a20e1feede746a82cd784ecd43c5cd1f21ebcc74d5418cbb87d69e90f1`
- The freeze field `predecessor_sha256` is `d607e635...`; that is the manifest entry hash for `PREDECESSOR.json`, not the predecessor MP4. `PREDECESSOR.json` itself correctly records the predecessor MP4 as `4d230cc0...`.

## HOLD Defects

1. **Encoded scientific typography fails the exact rendered-glyph guardrail.**
   - At `i05l` / `00:50.928`, the Longo card visibly renders the exponent as `7.9×10-⁴`, with a baseline hyphen before the superscript `4`, not `7.9×10⁻⁴`.
   - At `i05s` / `01:07.938`, the Shamir card visibly renders the exponent as `P<5.8×10-⁶`, with a baseline hyphen before the superscript `6`, not `P<5.8×10⁻⁶`.
   - The bottom caption/subtitle styling in those frames shows the same baseline-hyphen exponent form.
   - This violates required check 8: exact scientific typography visibly rendered without tofu/clipping for `7.9×10⁻⁴` and `P<5.8×10⁻⁶`.

2. **Receipt/local-QA frame count does not match independent decode.**
   - `CANDIDATE_AUTHORITY.json` and `build_receipt.json` claim `encoded_frames` / `frame_count` = `8417`.
   - Independent `ffprobe -count_frames` on the MP4 reports `nb_frames=8416`, `nb_read_frames=8416`, duration `280.533333` for the video stream.
   - Independent ffmpeg full decode to null completed without decode error but also reported `frame=8416`.
   - This does not affect the content HOLD above, but it means the local QA receipt cannot be accepted as exact against current bytes.

## Passing Checks Despite HOLD

- The three literature narration suffixes are byte-for-byte exact against the requested anchors:
  - `i05l` suffix exact after prefix `Longo reported: `
  - `i05s` suffix exact after prefix `Shamir reported: `
  - `i05d` suffix exact after prefix `Land and colleagues reported: `
- The claims are explicitly attributed in narration, SRT, and inspected encoded frames as other-study reports.
- `i05u` states: `These studies reported incompatible answers, so the literature remains disputed; this video adopts none of them as its finding.`
- The Land card at `00:80.976` is visually labelled `LAND ET AL. 2008 · REPORTED NULL` and `ATTRIBUTED TO ANOTHER STUDY · NOT THIS VIDEO'S FINDING`; it is not presented as the settled answer.
- The synthesis frame at `00:90.834` says `CLAIMED · DISPUTED · UNSETTLED`, `NO ANSWER SELECTED`, and `no winner`.
- `s02` through `s24` in `narration_script_v5.json` are structurally/textually identical to the predecessor `narration_script_v4.json` for `section`, `text`, and `visual_action`; mismatches `0`.
- The opening keeps the five-beat arc: isotropy expectation, tidal-torque origin, conditional mirror-symmetry stakes, attributed literature dispute, sorting-bias handoff.
- `WHY IT MATTERS` is the active rail before `MIRROR TEST` in the inspected intro frames.
- The conditional Longo stakes sentence is unchanged in the script and SRT.
- `forbidden_icon_primitives: ["curve"]` is present; renderer text scan found no generic curve dispatch.
- No result claim by this video found outside the permitted conditional Longo stakes sentence and attributed literature quotes. Existing later text still says no result value, direction, or interpretation is reportable.

## Forbidden Alternate-Cosmology Scan

I did not read or use `reviews/LANA_SPIN_BHU_BEAT_DRAFT_20260810.md`.

Rendered-content scan:

- SRT: no forbidden alternate-cosmology subject hit.
- `storyboard_v5_final.json`: no forbidden alternate-cosmology subject hit.
- Encoded OCR text recorded in `encoded_qa/ocr.txt`: `forbidden_hits: []` in `encoded_qa.json`.
- Inspected encoded intro/contact-sheet frames show no such beat or visual.

Non-rendered evidence/authority files do contain exclusion/provenance strings naming the withdrawn subject, as allowed by the request. The only hit in `narration_script_v5.json` is authority metadata, not a sentence/card.

## Audio Check

- Voice/speed provenance: `voice=alloy`, `speed=1.18` in `narration_script_v5.json` and candidate authority.
- Delivered WPM by decoded-speech-span/timeline method: `115.00000375287189`, inside `105-125`.
- A/V start alignment: max absolute delta `0.015333333333333421s`.
- Independent astats on the encoded MP4: peak level `-2.316897 dB`, RMS `-21.955134 dB`, NaNs `0`, Infs `0`; no clipping indicated.
- Independent ebur128 summary: integrated loudness `-20.8 LUFS`, true peak `-2.3 dBFS`, LRA `6.7 LU`.
- Embedded ASR in `encoded_qa.json` heard `z less than 0.3` and `p less than 5.8 times 10 to the minus sixth`; no equality wording detected.
- Caveat: separate files named `transcribe_symbol_qa.json` and `transcribe_intro_qa.json` are absent; the ASR evidence is embedded in `encoded_qa.json`.

## Cockpit / Replacement Check

- Predecessor MP4 remains byte-exact at `4d230cc0...`.
- I found no MP4 under `/Users/duhokim/HermesOps/cockpit/videos` with the new candidate hash `cfb9b1fa...`.
- The five current cockpit review copies are present at their expected hashes:
  - spin: `4d230cc0efca0eb68a8d027d614b6b7e500590cff06154f1514d4402a84d7078`
  - fesc: `01a4249beb2351fa25b2d2863eecb59b98dd68a53ced1dcc484ce6b723f45660`
  - brightend: `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8`
  - mzr-anchor: `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`
  - mzr-census: `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b`

No acceptance label is written. `video_reportable_now` remains false.

KUN_SPIN_LITERATURE_INTRO_GUARDRAIL_DONE
