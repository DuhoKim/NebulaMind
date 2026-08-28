# KUN OVERNIGHT VIDEO-QUALITY AUDIT

Created: 2026-08-10 01:15 KST

Order read in full:

- `HWAO_OVERNIGHT_VIDEO_QUALITY_20260810T0055K.md`

Scope: audio, legibility, and encoded spin guardrails. No builds, uploads, public/frontend/cockpit
replacement, DB, deploy, Git, billing/config, secrets, source freezes, result claims, or
`accepted_by_duho` labels.

Evidence directory:

- `reviews/kun-overnight-video-quality-20260810T0055K/`

## Exact Candidates Bound

- `spin`: `4d230cc0efca0eb68a8d027d614b6b7e500590cff06154f1514d4402a84d7078`
  `integrator/canaries/spin-method-overhaul-canary-20260809T2340K/spin-method-overhaul-canary-20260809T2340K.mp4`
- `fesc`: `01a4249beb2351fa25b2d2863eecb59b98dd68a53ced1dcc484ce6b723f45660`
  `integrator/canaries/fesc-method-overhaul-canary-20260809T1501K/fesc-method-overhaul-canary-20260809T1501K.mp4`
- `brightend`: `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8`
  `integrator/canaries/brightend-method-overhaul-canary-20260809T1345K/brightend-method-overhaul-canary-20260809T1345K.mp4`
- `mzr-anchor`: `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`
  `integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T1406K/mzr-anchor-method-overhaul-canary-20260809T1406K.mp4`
- `mzr-census`: `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b`
  `integrator/canaries/mzr-census-method-overhaul-canary-20260809T0320K/mzr-census-method-overhaul-canary-20260809T0320K.mp4`

Note: the same `c892f3fa...` bytes also exist under the excluded/mid-build `1300K` path. I reviewed the
current `1406K` candidate path.

## Audio Verdict

**HOLD FOR SERIES NORMALIZATION, NOT FOR CLIPPING.**

Measured from the encoded MP4s with `ffmpeg ebur128=peak=true`:

| lane | LUFS | LRA | true peak |
|---|---:|---:|---:|
| brightend | -20.0 | 7.5 LU | -2.3 dBFS |
| fesc | -20.2 | 7.0 LU | -2.3 dBFS |
| mzr-anchor | -20.9 | 7.4 LU | -2.3 dBFS |
| spin | -21.3 | 7.6 LU | -2.3 dBFS |
| mzr-census | -21.6 | 8.3 LU | -2.3 dBFS |

No clipping found: every lane peaks at about `-2.3 dBFS`. Streams are mono AAC 48 kHz and start at 0.
Audio/video duration mismatch is under one frame in the checked files.

Decision: normalize the series to **-20.5 LUFS integrated, true peak <= -2.3 dBFS, LRA target 7 LU
with tolerance 6.5-7.8 LU**. That keeps the existing clear narration tone while removing the audible
series jump. Under that target:

- `brightend` is too hot by ~0.5 LU.
- `mzr-census` is too quiet by ~1.1 LU and has the widest LRA at 8.3 LU.
- `spin` is too quiet by ~0.8 LU.
- `fesc` and `mzr-anchor` are close but should still be normalized with the set.

Inter-sentence gaps: no catastrophic dead air, but cadence differs. Long silences detected above -35 dB:

- `mzr-census`: repeated ~4.87s gaps at 32.817-37.683, 54.599-59.473, 109.202-114.073,
  131.775-136.655, 194.693-199.573, 207.767-212.642.
- `fesc`: repeated ~4.6-5.0s gaps at 33.369-38.358, 54.678-59.357, 111.179-116.019,
  134.094-138.939, 201.270-205.992.
- `spin`: many deliberate ~3.6-4.2s pauses, including 35.729-39.546 and 157.031-161.205.

Recommendation: keep the deliberate visual-breath pauses, but cap routine card-seam quiet gaps at
about 3.5-4.0s unless the animation genuinely needs more time. `mzr-census` is the main offender.

## Legibility Verdict

**PASS BASIC READABILITY; HOLD FOR WATCHING-EXPERIENCE POLISH ON STATUS/BOUNDARY CARDS.**

I generated frame contact sheets and inspected selected full-resolution frames:

- `frames/spin_contact.jpg`
- `frames/fesc_contact.jpg`
- `frames/brightend_contact.jpg`
- `frames/mzr_anchor_contact.jpg`
- `frames/mzr_census_contact.jpg`

Specific timestamp findings:

- `spin` 28.0s: Longo quote frame is visually guarded. The card says "IF A PREFERENCE WERE GENUINE,"
  the right panel asks "PREFERRED AXIS?" and says "NO DIRECTION SELECTED," and the subtitle remains
  conditional. No guardrail block.
- `fesc` 75.0s: flow diagram is readable, but the subtitle about recombination/ionizing-efficiency/
  clumping/source-density assumptions competes with many small labels. This is the weakest fesc legibility
  moment.
- `brightend` 202.0s: three-column scientific-boundary card is readable at full 1080p, but the viewer must
  absorb nine bullets plus a 24-word subtitle in the same moment. A viewer will likely miss either the
  card or the sentence before the transition.
- `mzr-anchor` 194.0s: same issue as brightend. The three boundary columns are clear, but the bottom
  subtitle is dense and pulls attention away from the card.
- `mzr-census` 85.0s and 105.0s: internal labels inside the semantic-clause diagram are small/low-contrast
  enough that a laptop viewer may not finish them before the narration moves on. The 203.0s boundary card
  is cleaner than brightend/anchor but still repeats the same split-attention pattern.

Decision: for the series, the correct grammar is the three-column `KNOWN NOW / NOT REPORTABLE / NEXT
SCIENTIFIC GATE` card, but it should not carry a full explanatory subtitle at the same time. Either hold
the card longer with minimal subtitle, or split it into two beats: card first, then spoken boundary.

## Spin Encoded Guardrails

Exact candidate: `4d230cc0...`.

Verdict: **PASS PRESENTATION GUARDRAILS; STILL PENDING DUHO WATCH AND Tori provenance correction.**

Checks against the six stop conditions:

- Asserted asymmetry/direction/parity/significance: **PASS**. The encoded opening uses conditional
  stakes and does not claim this study found any axis, direction, value, or significance.
- Longo/Shamir treated as true: **PASS**. The opening says the question has been "claimed, challenged,
  and left unsettled" and "this video adopts no answer." Longo appears as a conditional quote.
- Land's null treated as settled: **PASS**. Land is not used as the final answer; the method handoff is
  about bias/mirror controls.
- Black-hole-universe as driver: **PASS**. Not present in Tori OCR/forbidden context checks or sampled
  frames.
- Broad reason collapsed into sorter-bias method: **PASS**. Opening beats are visible in order:
  isotropy expectation, no preferred winding, angular-momentum origin, conditional parity/preferred-axis
  stakes, open contested question, then sorting-bias/mirror-control handoff.
- Hedging so heavy the viewer cannot restate why it matters: **PASS**. A viewer can restate:
  "they are testing whether the universe has a preferred spin direction, which it should not under
  large-scale isotropy, and sorting bias makes the test hard."

Weakest spin moment: 25.784-36.008s is a long 31-word Longo sentence. It is accurate and guarded, but it is
the place most likely to lose a listener if the volume is low. If Yui revises audio, this sentence should
not be quieter than the series target.

## Major Overnight Decisions

- One audio target: **-20.5 LUFS integrated, true peak <= -2.3 dBFS, LRA 6.5-7.8 LU**.
- Series legibility grammar to keep: large top title, status rail, paired explanation cards, withheld-result
  banners.
- Series legibility grammar to fix: dense scientific-boundary/status cards should not run at the same time
  as dense subtitles.
- No public/private replacement action taken by Kun.
- No `accepted_by_duho` label conferred.

## Final KUN State

**FAIL-CLOSED QUALITY HOLD.** The existing videos are watchable and intelligible, and spin `4d230cc0` passes
the reopened guardrails on encoded bytes. The main overnight quality defects are series audio normalization
and boundary-card split attention, especially `brightend` 202s, `mzr-anchor` 194s, and `mzr-census` seam
gaps. These are precise fix targets for Yui; they do not authorize publication or acceptance.
