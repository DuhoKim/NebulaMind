# KUN PUBLIC-RELEASE GATE -- BHU CLOSURE VIDEO DRAFT

Timestamp: 2026-08-12 KST

Lane:

- `bhu-closing-video-20260812T2322K`

Frozen draft artifacts gated:

- `NARRATION_DRAFT_V2.md` -- SHA-256 `640d43e1ff299d7e4f28a1d6ef2f3f2e6d21c7d1ea91a60fdf68c330a251d937`
- `STORYBOARD_DRAFT_V1.json` -- SHA-256 `8f99c03d7af951d71dd11c1028c0510d02c244b766b056c93f7dbb3e390930bc`
- `CLAIM_LINE_LEDGER.md` -- SHA-256 `89ac87be41a62c33135be72106781069b434514df663a649c03dc216be95cfb2`

Source packet:

- `reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md` -- SHA-256 `b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516`

Boundary: public-release claim gate on text/storyboard only. I did not render, narrate, publish, upload, accept, or mutate the frozen draft artifacts.

## Verdict

HOLD.

The draft is close, and the core closure is mostly stated at the right strength. It does not say BHU is true, false, supported, mainstream, or falsified. It preserves Duho's personal-interest framing in the opening. It also handles the neutron-star section with the needed restraint: Brown-Lee-Rho's "serious doubt or simply falsify" disjunction survives, and the draft explicitly refuses to adjudicate which side applies.

But this is for public YouTube, and two wording seams are too risky to let render:

1. The storyboard title says "why our sky test closed." A casual viewer can hear that as an empirical sky test that was run and failed. We did not run a BHU sky test.
2. The rival-cosmology language is stronger than the externally safe claim boundary. The packet permits the operational statement that a positive generic anisotropy would not identify BHU. It does not freeze a public class-level comparison where "other rotating cosmologies" are asserted as producing the same signal without citations.

Either issue is enough to hold before narration/render.

## Blocking Issue 1 -- "Our Sky Test" Implies An Experiment

Location:

- `STORYBOARD_DRAFT_V1.json`, title: `Inside a black hole? What the sources predict—and why our sky test closed`
- Related wording: Card 01 heading in both draft and storyboard, `This route closed because it had no calibrated, identifying sky test`

Problem:

The source packet closes a line of enquiry because no calibrated BHU-specific target exists for the sky-statistics routes. It does not report a completed sky test. On a public channel, "our sky test closed" is too easy to quote as "they tested BHU on the sky."

Required repair:

Replace the storyboard title with:

> Inside a black hole? What the sources predict -- and why this route closed

Replace Card 01 heading with:

> This route closed because it had no calibrated, identifying target

Do not use "our sky test" in the title, card heading, chapter labels, or metadata.

## Blocking Issue 2 -- Rival-Cosmology Claim Is Too Strong For Public Release

Locations:

- `NARRATION_DRAFT_V2.md`, Card 01: "other rotating cosmologies can give the same broad signal"
- `NARRATION_DRAFT_V2.md`, Card 09: "Other rotating cosmologies can lead to the same broad effect."
- `NARRATION_DRAFT_V2.md`, Card 11: "rather than a generic effect of rotation or a bounce"
- `STORYBOARD_DRAFT_V1.json`, Card 09 diagram/on-screen support: `OTHER ROTATING COSMOLOGIES`, `SAME BROAD SIGNAL`
- `CLAIM_LINE_LEDGER.md`, C12 boundary says the safe packet-level statement is that a positive generic anisotropy would not identify BHU, and that alternative-model citations remain `[VERIFY]` for an external class-level freeze.

Problem:

The narration mostly avoids naming specific rivals, but it still tells the public that other rotating cosmologies can produce the same broad effect. That may be true, but the source packet itself says the external class-level comparison needs primary citations before freezing. For YouTube, the safe claim must be epistemic and operational: the observed signal would not uniquely identify BHU.

Required repairs:

Card 01 replacement sentence:

> But our galaxy-spin route cannot identify a black-hole origin: it has no calibrated target, and the same broad observation would not by itself choose a cause.

Card 09 replacement narration:

> Suppose a controlled survey found a real spin-handedness difference. That would be interesting. But a positive generic anisotropy would not identify BHU. One observed number would have more than one possible interpretation unless a BHU model supplied a unique signature. A successful measurement is not automatically a successful test of this model.

Card 09 diagram/on-screen replacements:

- replace `OTHER ROTATING COSMOLOGIES` with `OTHER POSSIBLE CAUSES`
- replace `SAME BROAD SIGNAL` with `NOT BHU-SPECIFIC BY ITSELF`
- keep `MEASUREMENT != IDENTIFICATION`

Card 11 replacement phrase:

> Or second, a signature unique to birth behind a parent horizon, not merely the broad fact of spin asymmetry.

These preserve the claim boundary without laundering an unresolved comparative literature claim into a public video.

## Required Softening -- CNS Heading

Location:

- `NARRATION_DRAFT_V2.md`, Card 04 heading
- `STORYBOARD_DRAFT_V1.json`, Card 04 heading

Current:

> Cosmological natural selection puts a low ceiling on neutron-star mass

Repair:

> One CNS chain puts a low ceiling on neutron-star mass

Reason:

The narration correctly narrows to the Brown-Lee-Rho chain, but the public heading is broader than the body. A hostile physicist could quote the heading as overclaiming all CNS rather than the surveyed chain.

## What Already Passes

- Personal-interest framing is present in Card 01 narration and on-screen support.
- The draft does not present BHU as mainstream or as a NebulaMind frontier.
- The draft says the idea is not declared true or false.
- The neutron-star section preserves Demorest/Fonseca numerical nuance and refuses to call falsification.
- The axis source is described fairly after Tori's correction: explicit qualitative claim, not calibrated or pre-data forecast.
- The "no rival idea predicts the same number" logic is conceptually right after repair: an identifying test needs a target that can be missed and not shared. The draft must express that as a rule of inference, not as an unfrozen catalogue of rival cosmologies.

## Public-Comprehension Note

Not a separate HOLD, because the claim repairs already block rendering, but the render contract's `target_narration_wpm` of `145-150` is aggressive for a dense public science explainer. If this returns for encoded review, I will treat unintelligible pacing as a release blocker. A safer public target is closer to `120-135` WPM unless Lana/Goru deliberately choose a faster editorial style and the encoded audio proves intelligible.

## What Would Clear The HOLD

Return a new frozen draft set with new hashes after:

1. removing "our sky test" from title/heading/metadata and replacing it with "route";
2. replacing the rival-cosmology wording with the operational "not identifying by itself" language above;
3. narrowing the CNS heading to "One CNS chain";
4. preserving all existing neutron-star caveats and the Duho personal-interest opening.

No audio or rendering should start from the three hashes gated here.
