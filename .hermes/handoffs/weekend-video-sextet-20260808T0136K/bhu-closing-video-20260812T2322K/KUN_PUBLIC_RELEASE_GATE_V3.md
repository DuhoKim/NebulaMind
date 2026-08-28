# KUN PUBLIC-RELEASE GATE V3 -- BHU CLOSURE VIDEO REPAIRED BYTES

Timestamp: 2026-08-12 KST

Lane:

- `bhu-closing-video-20260812T2322K`

Frozen repaired artifacts gated:

- `NARRATION_DRAFT_V3.md` -- SHA-256 `ffed91f6d5625726170d149b5c78987f7b1371104ad469a3651f01156feacd6d`
- `STORYBOARD_DRAFT_V2.json` -- SHA-256 `ac1c18fb9b5da1a2dc68330477ae42c0265bbf8e9620fe599929c612cd72ee91`
- `CLAIM_LINE_LEDGER_V2.md` -- SHA-256 `f0fce1fdc9404d8d799064bbe5a44ac564e38b2b4bb11f45ac9ff42ce38eb89e`

Source packet:

- `reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md` -- SHA-256 `b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516`

Boundary: public-release claim gate on repaired text/storyboard only. I did not render, narrate, publish, upload, accept, or mutate the frozen draft artifacts.

## Verdict

HOLD.

The predecessor verdict is historical only; this verdict binds to the three repaired hashes above. The repaired artifacts do remove the explicit fabricated `1.95` value, and `CLAIM_LINE_LEDGER_V2.md` correctly states that the packet gives no 95.4% lower-bound value. But the repaired storyboard still contains public-release blockers.

The main lesson from Goru's catch is now directly load-bearing: a visual can fabricate a measurement even when the narration is clean. `STORYBOARD_DRAFT_V2.json` still asks for a scaled plot element that requires an unstated numerical endpoint for the 95.4% interval. That remains a HOLD.

## Blocking Issue 1 -- 95.4% Visual Still Requires An Unstated Number

Location:

- `STORYBOARD_DRAFT_V2.json`, Card 05 diagram: `Full, uncropped horizontal interval plot from 1.4 to 2.2 M☉... Add a distinct 95.4% interval marker showing that the result does not clear 2.00.`
- `STORYBOARD_DRAFT_V2.json`, Card 05 on-screen support: `AT 95.4% CREDIBILITY, THE RESULT DOES NOT CLEAR 2.00 M☉`
- `CLAIM_LINE_LEDGER_V2.md`, C07: the packet does not state the 95.4% lower-bound value, so no value may appear in the video.

Problem:

The numeric label `1.95` is gone, but a "full, uncropped horizontal interval plot" with a "distinct 95.4% interval marker" still forces the renderer to draw a lower endpoint somewhere on a 1.4--2.2 solar-mass axis. A viewer will read that endpoint as a quantitative measurement, even if the number is not printed. This is still a public assertion not present in Lana's packet.

Required repair:

Do not draw the 95.4% interval to scale. Replace Card 05 diagram instruction with:

> Full horizontal mass axis from 1.4 to 2.2 M_sun. Draw the source's ~1.5 marker and the approximate 2 M_sun regime. Row 1: Demorest 1.97 +/- 0.04, central point below 2 and interval crossing. Row 2: Fonseca 2.08 +/- 0.07 at 68.3%, with the 68.3% interval above 2. Add a separate non-scaled annotation beside the Fonseca row: "At 95.4% credibility, the packet states only that the result does not clear 2.00; no lower-bound value is quoted here." Do not draw a scaled 95.4% endpoint or arrow.

The current on-screen support sentence is acceptable only if the visual does not draw a scaled 95.4% interval.

## Blocking Issue 2 -- "Our Sky Test" Still Implies An Experiment

Locations:

- `STORYBOARD_DRAFT_V2.json`, title: `Inside a black hole? What the sources predict—and why our sky test closed`
- `NARRATION_DRAFT_V3.md`, Card 01 heading: `This route closed because it had no calibrated, identifying sky test`
- `STORYBOARD_DRAFT_V2.json`, Card 01 heading: same wording.

Problem:

We did not run a BHU sky test. The source packet closes a route because no calibrated BHU-specific target exists. For a public title or heading, "our sky test closed" can be quoted as a completed empirical test.

Required repairs:

Replace the storyboard title with:

> Inside a black hole? What the sources predict -- and why this route closed

Replace Card 01 heading with:

> This route closed because it had no calibrated, identifying target

Do not use "our sky test" in title, headings, chapter labels, captions, or metadata.

## Blocking Issue 3 -- Rival-Cosmology Visual/Narration Exceeds The Public Claim Boundary

Locations:

- `NARRATION_DRAFT_V3.md`, Card 01: `other rotating cosmologies can give the same broad signal`
- `NARRATION_DRAFT_V3.md`, Card 09: `Other rotating cosmologies can lead to the same broad effect.`
- `NARRATION_DRAFT_V3.md`, Card 11: `rather than a generic effect of rotation or a bounce`
- `STORYBOARD_DRAFT_V2.json`, Card 09 diagram/on-screen support: `OTHER ROTATING COSMOLOGIES`, `SAME BROAD SIGNAL`
- `CLAIM_LINE_LEDGER_V2.md`, C12 boundary: alternative-model citations are `[VERIFY]` for an external class-level freeze; the safe packet-level statement is that a positive generic anisotropy would not identify BHU.

Problem:

The public-safe statement is operational: a generic spin anisotropy would not identify BHU by itself. The current draft and visual labels assert the comparative reason as a public fact about "other rotating cosmologies" producing the same signal, while the ledger itself says that external class-level comparison needs primary citations.

Required repairs:

Card 01 replacement sentence:

> But our galaxy-spin route cannot identify a black-hole origin: it has no calibrated target, and the same broad observation would not by itself choose a cause.

Card 09 replacement narration:

> Suppose a controlled survey found a real spin-handedness difference. That would be interesting. But a positive generic anisotropy would not identify BHU. One observed number would have more than one possible interpretation unless a BHU model supplied a unique signature. A successful measurement is not automatically a successful test of this model.

Card 09 visual replacements:

- replace `OTHER ROTATING COSMOLOGIES` with `OTHER POSSIBLE CAUSES`;
- replace `SAME BROAD SIGNAL` with `NOT BHU-SPECIFIC BY ITSELF`;
- keep `MEASUREMENT != IDENTIFICATION`.

Card 11 replacement phrase:

> Or second, a signature unique to birth behind a parent horizon, not merely the broad fact of spin asymmetry.

## Blocking Issue 4 -- CNS Heading Still Overgeneralizes

Locations:

- `NARRATION_DRAFT_V3.md`, Card 04 heading: `Cosmological natural selection puts a low ceiling on neutron-star mass`
- `STORYBOARD_DRAFT_V2.json`, Card 04 heading: same wording.

Problem:

The body narrows to the Brown-Lee-Rho chain Lana surveyed. The heading reads as a statement about cosmological natural selection as a whole. Public headings get quoted independently.

Required repair:

Replace with:

> One CNS chain puts a low ceiling on neutron-star mass

## What Passes In The Repaired Bytes

- The three repaired hashes match the dispatch.
- The explicit fabricated `1.95` value is purged from narration, storyboard, and ledger.
- The opening states Duho's personal-interest framing and says this is not a NebulaMind research frontier.
- The draft does not say BHU is true, false, supported, mainstream, meaningless, or untestable in principle.
- The neutron-star narration preserves the source disjunction and refuses to adjudicate falsification.
- The axis source is treated fairly as an explicit, source-backed qualitative claim, not a calibrated or pre-data forecast.

## What Would Clear The HOLD

Return new frozen hashes after:

1. removing every "our sky test" / "sky test" title-heading formulation and replacing it with route/target language;
2. replacing rival-cosmology claims and visuals with the operational "not identifying by itself" language;
3. narrowing the CNS heading to "One CNS chain";
4. changing Card 05 so the 95.4% credibility statement is a non-scaled textual annotation, not a plotted interval endpoint, arrow, or to-scale marker;
5. preserving the existing personal-interest framing and neutron-star caveats.

No audio or rendering should start from the three hashes gated here.
