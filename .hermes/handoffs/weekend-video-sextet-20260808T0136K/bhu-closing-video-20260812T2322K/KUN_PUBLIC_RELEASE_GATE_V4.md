# KUN PUBLIC-RELEASE GATE V4 -- BHU CLOSURE VIDEO CONSOLIDATED DELTA

Timestamp: 2026-08-12 KST

Lane:

- `bhu-closing-video-20260812T2322K`

Frozen V4 artifacts gated:

- `NARRATION_DRAFT_V4.md` -- SHA-256 `096c893c2d6085bc3588863141ab705097b39a935ad2f243d442918d2cd1d562`
- `STORYBOARD_DRAFT_V3.json` -- SHA-256 `0492c531e8836e6ac5770b22455713ec658ea3ba2f5ddbd308028686da384907`
- `CLAIM_LINE_LEDGER_V3.md` -- SHA-256 `1004ce3bc0f79ef3f05144073e503da93ff4fa1d7c4698da78b1a472ce8a8a9d`

Source packet:

- `reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md` -- SHA-256 `b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516`

Boundary: public-release claim gate on V4 text/storyboard only. I did not render, narrate, publish, upload, accept, or mutate the frozen draft artifacts.

## Verdict

HOLD.

The big V3 repairs mostly landed:

- the title is now `Inside a black hole? What the sources predict--and why this route closed`;
- Card 01 heading is now `This route closed because it had no calibrated, identifying target`;
- I find no surviving `our sky test` wording;
- the Card 09 rival-cosmology frame was narrowed to `OTHER POSSIBLE CAUSES` / `NOT BHU-SPECIFIC BY ITSELF`;
- the CNS heading is now `One CNS chain puts a low ceiling on neutron-star mass`;
- public pacing target was reduced to `120-135`, design at 128 WPM.

But two new/remaining public-release blockers remain, both in the repaired material. They are small enough to fix, but not safe to render.

## Blocking Issue 1 -- The 95.4% Visual Still Can Fabricate A Value

Location:

- `STORYBOARD_DRAFT_V3.json`, Card 05 diagram: `Add a distinct 95.4% marker showing only the packet-permitted statement that the result does not clear 2.00; do not plot or print an unstated lower-bound value.`

Problem:

This repair lands the letter but not the intent. It says not to print an unstated lower-bound value, but it still instructs a "distinct 95.4% marker" inside a full horizontal mass plot. A marker on a scaled axis has a position. A viewer will read that position as a quantitative claim. That recreates the same visual-claim failure Goru caught, just without the numeric label.

Required repair:

Replace the Card 05 diagram instruction with:

> Full horizontal mass axis from 1.4 to 2.2 M_sun. Draw the source's ~1.5 marker and the approximate 2 M_sun regime. Row 1: Demorest 1.97 +/- 0.04, central point below 2 and interval crossing. Row 2: Fonseca 2.08 +/- 0.07 at 68.3%, with the 68.3% interval above 2. Add a separate non-scaled text callout beside the plot: "At 95.4% credibility, the packet states only that the result does not clear 2.00; no lower-bound value is quoted here." Do not draw a 95.4% endpoint, arrow, tick, bracket, or marker on the mass axis.

The current on-screen support sentence can remain only if the render cannot place any 95.4% graphic on the axis.

## Blocking Issue 2 -- Statistical Plain-Language Overreach

Location:

- `NARRATION_DRAFT_V4.md`, Card 05: `At the everyday confidence level, the second measurement clears two Suns; demand near-certainty, and it does not quite.`
- same narration string in `STORYBOARD_DRAFT_V3.json`, Card 05.

Problem:

This is a public-facing overtranslation. `68.3%` is the quoted interval in the packet; calling it "everyday confidence" is informal but tolerable. Calling `95.4%` "near-certainty" is not. A hostile physicist can fairly object that 95.4% credibility is not near-certainty, and the packet itself used the more careful "stronger credibility level" framing.

Required repair:

Replace the last sentence of Card 05 narration with:

> At the quoted 68.3% level, the second measurement clears two solar masses; at the stricter 95.4% level, the packet says it does not.

Use the same wording in the storyboard narration.

## Blocking Issue 3 -- Card 10 Reintroduces The "Untestable In Principle" Reading

Location:

- `NARRATION_DRAFT_V4.md`, Card 10: `Find nothing, and it still does not lose: with no predicted size, no outcome settles it.`
- same narration string in `STORYBOARD_DRAFT_V3.json`, Card 10.

Problem:

Lana's source packet is careful: the axis source has qualitative directional claims, and sufficiently precise measurements could bear on those prose claims. The operational closure is narrower: no finite-precision test can be numerically scored against a source-defined acceptance region, and a positive generic anisotropy would not identify BHU. "Find nothing ... no outcome settles it" reads too close to "untestable in principle," which the packet explicitly refuses.

Required repair:

Replace the Card 10 opening with:

> The route therefore fails in two independent ways. A finite-precision spin result cannot be scored against a source-defined pass-or-fail range, because the source gives no predicted size. And without a unique signature, a positive result cannot identify BHU.

Then continue with:

> We could build a trustworthy measurement and still be unable to answer the BHU question. The hunt had a source. It did not have a target.

## Non-Blocking Clarity Repair

Card 01 says "One branch gives collapsed stars a number to check" and the storyboard label says `COLLAPSED STARS: A NUMBER TO CHECK`. The source claim is specifically neutron-star mass. "Collapsed stars" is not false in a broad explainer sense, but it is imprecise and can blur into black holes for a casual viewer. Prefer:

> One branch gives neutron stars a number to check.

and:

> NEUTRON STARS: A NUMBER TO CHECK

I do not make this a separate HOLD because Card 03 explains neutron stars and pulsars, but it should be fixed while the blocking edits are open.

## What Passes

- Hashes match the V4 dispatch.
- My previous `sky test` repair landed in title, Card 01 heading, narration, storyboard labels, and searchable metadata.
- The public personal-interest framing is clear and early.
- The draft does not say BHU is true, false, supported, mainstream, meaningless, or untestable in principle, except for the Card 10 wording risk above.
- The rival-cosmology comparison is now expressed as non-identification rather than an uncited public catalogue of rivals.
- The CNS heading is properly narrowed to one chain.
- The axis source is still treated fairly: explicit, source-backed qualitative claim; not calibrated and not pre-data.

## What Would Clear The HOLD

Return new frozen hashes after:

1. changing Card 05's 95.4% treatment to a non-scaled text callout, with no axis marker, endpoint, arrow, tick, or bracket;
2. replacing "everyday confidence" / "near-certainty" with the quoted-level wording above;
3. replacing Card 10's "Find nothing ... no outcome settles it" language with the narrower source-defined acceptance-region formulation;
4. preferably changing Card 01's "collapsed stars" shorthand to "neutron stars."

No audio or rendering should start from the three V4 hashes gated here.
