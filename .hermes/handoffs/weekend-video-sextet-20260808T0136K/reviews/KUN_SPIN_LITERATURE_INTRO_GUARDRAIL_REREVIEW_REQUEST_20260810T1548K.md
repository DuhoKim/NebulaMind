# KUN REREVIEW REQUEST — Spin literature intro typography + frame-receipt correction

Request ID: `KUN_SPIN_LITERATURE_INTRO_GUARDRAIL_REREVIEW_REQUEST_20260810T1548K`

Read-only, fail-closed rereview of a new frozen candidate. The prior `cfb9b1fa...` candidate remains frozen under HOLD and is not eligible for Tori. Write only the new report requested below; mutate neither candidate.

## Corrected frozen candidate

- Directory: `integrator/canaries/spin-literature-intro-canary-20260810T1535K`
- MP4: `integrator/canaries/spin-literature-intro-canary-20260810T1535K/spin-literature-intro-canary-20260810T1535K.mp4`
- Expected MP4 SHA-256: `fe04bed4605c8ee75b0641ff44c12d61990f388858f97f78103fef3c073678ed`
- Freeze SHA-256: `44a8a5167a0c630495beb6fcd02082048db442a034cbd4b0c8456434868f05ee`
- Manifest SHA-256: `43ffcd00b0a16d90e263ca58f9b20732f1d7c5b6266f1998294a1357a547f57b`
- Manifest payload: 139 entries / 120,930,574 bytes; directory total before your report: 141 files.

Prior HOLD:

- Report: `reviews/KUN_SPIN_LITERATURE_INTRO_GUARDRAIL_REVIEW_20260810T1507K.md`
- SHA-256: `00670f4a67c0afaf4975779fab0b5d59492e89eaec5504aa05d0c438b93d3714`
- Held MP4: `cfb9b1fabb7d4fb46009319d45d33931bf108917f317a184e4074e6f471d968d`

## Required correction checks

1. Recompute candidate/freeze/manifest hashes and every manifest entry at start; candidate hash again at close. Write nothing inside the candidate directory.
2. Inspect the encoded Longo frame `encoded_qa/frames/i05l-050.928.jpg` and Shamir frame `encoded_qa/frames/i05s-067.938.jpg`, plus the encoded contact sheet. `7.9×10⁻⁴` and `P<5.8×10⁻⁶` must now show U+207B minus visibly at the same superscript height as 4/6 in both card and caption, with no baseline-hyphen appearance, tofu, clipping, or illegibility. Confirm `−0.0408±0.011` and `z<0.3` too. Renderer must bind STIX Two Text for these exact scientific strings.
3. Independently run `ffprobe -count_frames` and full decode. Required exact relationship:
   - `raw_frames_submitted = ceil(280.5652083333333 × 30) = 8417`
   - `encoded_video_frames = nb_read_frames = 8416`
   - encoded video stream duration `280.533333s`
   - audio-master minus encoded-video duration approximately `0.031875s`, nonnegative and under one 30-fps frame (`0.033333s`)
   - build receipt's legacy `frame_count` must be 8416, not 8417; raw and encoded counts must be separate.
4. Verify all local-QA status claims against current bytes, especially the four new frame-count checks and `scientific_unicode_font_is_stix_two_text`.
5. Reconfirm every passing guardrail from the prior report on the new hash: exact attributed Longo/Shamir/Land sentences; claimed/disputed/unsettled; Land null not settled; no winner; no result claim by this video; no forbidden alternate-cosmology content in narration/SRT/storyboard/OCR/encoded visuals/delivery filename; five-beat arc; conditional stakes; active WHY IT MATTERS rail; NO ANSWER SELECTED; coherent mirror seam; s02–s24 unchanged; curve hardening; alloy 1.18; 115 WPM; inequality/exponent pronunciation; no clipping; predecessor and five cockpit copies unchanged.
6. Evidence/authority files may name excluded material solely to prove exclusion. Do not inspect or use the superseded draft.
7. No acceptance label. `video_reportable_now` remains false even on PASS.

## Allowed write

Write only:

`reviews/KUN_SPIN_LITERATURE_INTRO_GUARDRAIL_REREVIEW_20260810T1548K.md`

Verdict exactly one of:

- `PASS_GUARDRAILS_EXACT_HASH`
- `HOLD_GUARDRAILS_EXACT_HASH`

End with standalone marker:

`KUN_SPIN_LITERATURE_INTRO_GUARDRAIL_REREVIEW_DONE`

Tori exact-hash regate waits for this disk report.
