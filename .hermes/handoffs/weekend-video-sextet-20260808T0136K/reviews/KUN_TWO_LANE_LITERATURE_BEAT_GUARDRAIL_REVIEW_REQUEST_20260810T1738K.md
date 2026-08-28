# KUN BRIEF — TWO-LANE LITERATURE-BEAT GUARDRAIL REVIEW — 20260810T1738K

User-authorized task: independently review the two and only two new literature-beat candidates below. This is the first external gate. Read-only candidate review; do not mutate either frozen candidate.

## Binding order and source

- User order: build only `mzr-anchor` and `brightend`; do not build `fesc` or `mzr-census`.
- Lana ruling: `reviews/LANA_FOUR_LANE_LITERATURE_BEAT_20260810.md`.
- Architecture: copy the validated spin literature-card safety architecture.
- SOURCE_FREEZE remains absent. `video_reportable_now=false`. Nothing is accepted until Duho watches it.

## Candidate A — mzr-anchor

Directory:
`integrator/canaries/mzr-anchor-literature-beat-motion-fix-20260810T1705K`

Video:
`integrator/canaries/mzr-anchor-literature-beat-motion-fix-20260810T1705K/mzr-anchor-literature-beat-canary-20260810T1705K.mp4`

Required SHA-256:
`47f71fc40e1f81f7e4374e7e867c07cc64f8595ad553137403bff7d52dbec547`

Receipt SHA-256:
`4000266d46565344ac2f8900021d72555bc89c11109148a07c9083ff90df0162`

POST_ENCODE_FREEZE SHA-256:
`b2aa23206fafe50122afa68e1351b2fa4c65dce257cd21d78d8988d7a7e03419`

Lane-specific ruling:
- Quote only Kewley & Ellison's calibration-disagreement finding about the rulers themselves.
- Exact sentence: `The absolute metallicity scale (y-int) varies up to 0.7 dex, depending on the calibration used.`
- Never quote an evolution finding; no evolution result may be adopted.
- Card must visually attribute the quote to Kewley & Ellison 2008 and mark it `REPORTED CALIBRATION DISAGREEMENT`.

## Candidate B — brightend

Directory:
`integrator/canaries/brightend-literature-beat-qa-fix-20260810T1732K`

Video:
`integrator/canaries/brightend-literature-beat-qa-fix-20260810T1732K/brightend-literature-beat-canary-20260810T1732K.mp4`

Required SHA-256:
`49f1fe3dcf3fed69d0269c24fefddb67c45f6d558e34727d4b7ee5b823abc05d`

Receipt SHA-256:
`8ac3b2a280aa38444cca4019abfbfde509b10a93f05e6b533e11be6a380f984f`

POST_ENCODE_FREEZE SHA-256:
`0ba78e125aac19c04ce22b9758f2132bdf3e8ad843132570bff31e6610238aa3`

Lane-specific ruling:
- Quote the reported excess as a contested field claim and the primary source's own unresolved hedge that names the observational-verification angle.
- Exact sentence 1: `Early data from JWST have revealed a bevy of high-redshift galaxy candidates with unexpectedly high stellar masses.`
- Exact sentence 2: `the most massive galaxy candidates in JWST observations at z∼7-10 lie at the very edge of these limits, indicating an important unresolved issue with the properties of galaxies derived from the observations, how galaxies form at early times in ΛCDM, or within this standard cosmology itself.`
- Encoded frame must visibly render a real `∼` and `Λ`, never missing-glyph boxes; long quote and caption must remain readable.
- Card headers must be `BOYLAN-KOLCHIN 2023 · REPORTED EXCESS CLAIM` and `BOYLAN-KOLCHIN 2023 · REPORTED UNRESOLVED HEDGE`.

## Required checks, separately for each lane

1. Recompute video, receipt, and freeze SHA-256; bind report to the exact video hash.
2. Verify `CONTRACT_QA.json` and `encoded_qa.json` are PASS and independently spot-check their evidence rather than self-certifying from the status word.
3. Verify every quoted abstract sentence matches Lana's ruling and the included primary-source receipt exactly; no paraphrase.
4. Inspect encoded quote and closing frames at the recorded timeline mids.
5. Verify per-study/claim header; exact serif quote; distinct safe color; footer `ATTRIBUTED TO ANOTHER STUDY · NOT THIS VIDEO'S FINDING`; arXiv id plus `exact abstract sentence`; running `LITERATURE CONTEXT · NO ANSWER SELECTED`; local `WHY IT MATTERS` rail focus.
6. Verify the closing sentence is fully audible/captioned and plays the same safety role as spin: attributed claim(s), explicitly disputed/contested/unsettled, and this video adopts no answer/claim/explanation as its finding.
7. Verify no lane result is asserted: no adopted asymmetry, shortfall, excess, evolution, calibration answer, direction, parity violation, or significance.
8. Verify forbidden `curve` icon primitive hardening and absence of a sweeping rail/result-looking graph in the literature beat.
9. Verify fresh alloy 1.18 audio, re-derived timeline, exact 115 WPM receipt, raw literature ASR PASS, encoded-opening ASR PASS, one-frame A/V/frame-count custody, loudness/peak bounds, full decode, and caption line limits.
10. Verify SOURCE_FREEZE absent, `video_reportable_now=false`, `accepted_by_duho=false`, no upload/public/cockpit/git gate, and final state is only provisional awaiting review/watch.
11. Verify protected predecessors remain exact: mzr-anchor `c892f3fa…`, brightend `c772e643…`; protected fesc/mzr-census canary trees and the whole cockpit MP4 manifest remain unchanged per custody baseline/QA.
12. Confirm no `fesc` or `mzr-census` literature candidate was built by this order.

## Output

Write two separate reports only:

- `reviews/KUN_MZR_ANCHOR_LITERATURE_BEAT_GUARDRAIL_REVIEW_20260810T1738K.md`
- `reviews/KUN_BRIGHTEND_LITERATURE_BEAT_GUARDRAIL_REVIEW_20260810T1738K.md`

Each report must end with exactly one verdict:

- `PASS_GUARDRAILS_EXACT_HASH`
- or `HOLD_GUARDRAILS_EXACT_HASH` followed by precise blockers.

Do not edit candidates, specs, audio, video, cockpit, predecessors, fesc/mzr-census, git, DB, deploy/runtime, or public surfaces. Do not mark accepted. Tori regate is not authorized until the corresponding Kun report lands with PASS.
