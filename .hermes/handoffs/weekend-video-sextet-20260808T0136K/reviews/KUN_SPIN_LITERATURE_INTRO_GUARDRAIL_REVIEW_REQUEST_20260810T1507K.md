# KUN REVIEW REQUEST — Spin revised literature intro guardrails

Request ID: `KUN_SPIN_LITERATURE_INTRO_GUARDRAIL_REQUEST_20260810T1507K`

## Review order

Perform a read-only, fail-closed guardrail review of the exact frozen candidate below. Write exactly one new report file and do not mutate the candidate, predecessor, cockpit copies, public roots, source freeze, lane packets, or any other review.

## Exact frozen candidate

- Directory: `integrator/canaries/spin-literature-intro-canary-20260810T1434K`
- MP4: `integrator/canaries/spin-literature-intro-canary-20260810T1434K/spin-literature-intro-canary-20260810T1434K.mp4`
- Expected MP4 SHA-256: `cfb9b1fabb7d4fb46009319d45d33931bf108917f317a184e4074e6f471d968d`
- Freeze: `integrator/canaries/spin-literature-intro-canary-20260810T1434K/CANDIDATE_FREEZE.json`
- Expected freeze SHA-256: `cf23013350cf4e62e7c76714d73cb6f761b22fd3f6b6e6073149b1ec1ccd1c4d`
- Manifest: `integrator/canaries/spin-literature-intro-canary-20260810T1434K/FILE_MANIFEST.json`
- Expected manifest SHA-256: `4603591b148b8aee911313fc17d8c54894c13ae0ae5b1c643a2a749bb2859530`
- Manifest payload: 138 entries / 121,041,612 bytes; manifest excludes itself and freeze; directory total before your report is 140 files.

Predecessor:

- `integrator/canaries/spin-method-overhaul-canary-20260809T2340K/spin-method-overhaul-canary-20260809T2340K.mp4`
- Expected SHA-256: `4d230cc0efca0eb68a8d027d614b6b7e500590cff06154f1514d4402a84d7078`
- Predecessor script SHA-256: `5df1d0a20e1feede746a82cd784ecd43c5cd1f21ebcc74d5418cbb87d69e90f1`

## Live content authority

Use only Part 1, `REVISED BEAT 4`, from `reviews/LANA_SPIN_BEAT4_AND_BHU_ASSESSMENT_20260810.md` as the literature-content authority. The withdrawal at `lanes/spin/SOURCE_FREEZE_AMENDMENT_A1_WITHDRAWN_20260810T1424K.md` has SHA-256 `7eb5c37ead54863428a6f452462182c2f6230607735483058af39155fca8b891` and binds the alternate-cosmology subject back into forbidden scope without qualification.

Do not read or use `LANA_SPIN_BHU_BEAT_DRAFT_20260810.md`; it is preserved but superseded. Authority/evidence filenames and withdrawal text may name the excluded subject solely to prove its exclusion. The content guardrail is strict: no such subject may appear in the MP4, narration, captions, cards, OCR-visible text, beat structure, or delivery filename.

## Required independent checks

1. Recompute the MP4, freeze, manifest, authority, predecessor, and all 138 manifest-entry hashes and sizes. Verify candidate hash at review start and close; candidate directory writes by Kun must be zero.
2. Compare the three literature narration suffixes byte-for-byte with Lana Part 1 and the primary-abstract anchors:
   - Longo: `An unbinned analysis for a dipole component that made no prior assumptions for the dipole axis gives a dipole asymmetry of −0.0408±0.011 with a probability of occurring by chance of 7.9×10⁻⁴.`
   - Shamir: `The results show that the local universe (z<0.3) is not isotropic in terms of galaxy spin, with probability P<5.8×10⁻⁶ of such asymmetry to occur by chance.`
   - Land et al.: `After establishing and correcting for a certain level of bias in our handedness results we find the winding sense of the galaxies to be consistent with statistical isotropy.`
3. Verify every quoted sentence is explicitly attributed in narration and on screen as another study's report, never as this video's finding. Verify the synthesis says claimed/disputed/unsettled and selects no winner. Land's null must not be a settled answer.
4. Independently inspect/scan the encoded MP4 for the forbidden alternate-cosmology subject. Evidence files are not rendered content. Any mention in narration, cards, captions, OCR-visible text, beat structure, or delivery filename is a mandatory `CUT`/`HOLD`.
5. Verify no result claim by this video: no asserted asymmetry, direction, parity violation, or significance. The conditional Longo stakes sentence and attributed literature quotes are the only permitted claim-bearing text.
6. Verify the five-beat opening arc, stakes before method, unchanged conditional Longo sentence, `WHY IT MATTERS` as the active rail before `MIRROR TEST`, `NO ANSWER SELECTED`, and coherent seam into the existing mirror-control spine.
7. Compare `s02` through `s24` in v5 to the predecessor script. They must be structurally and textually identical. Verify the rail focus fix and `forbidden_icon_primitives: ["curve"]` hardening remain and generic curve dispatch is absent.
8. Verify exact scientific typography is visibly rendered without tofu/clipping: `−0.0408±0.011`, `7.9×10⁻⁴`, `z<0.3`, `P<5.8×10⁻⁶`.
9. Verify the encoded audio independently: alloy 1.18 provenance, 115 WPM timing, A/V start alignment, no clipping, and intelligible pronunciation of every inequality and exponent. In particular, the audio must say `z less than zero point three` and `P less than five point eight times ten to the minus sixth`; equality is a mandatory hold.
10. Verify all local QA claims against current bytes rather than trusting their status labels. Confirm predecessor and five cockpit copies were not replaced. Do not write any acceptance label.

## Allowed write and required verdict

Write only:

`reviews/KUN_SPIN_LITERATURE_INTRO_GUARDRAIL_REVIEW_20260810T1507K.md`

Verdict must be exactly one of:

- `PASS_GUARDRAILS_EXACT_HASH`
- `HOLD_GUARDRAILS_EXACT_HASH`

End with a standalone marker:

`KUN_SPIN_LITERATURE_INTRO_GUARDRAIL_DONE`

Nothing is accepted and `video_reportable_now` remains false even on PASS. Tori exact-hash regate waits for your report on disk.
