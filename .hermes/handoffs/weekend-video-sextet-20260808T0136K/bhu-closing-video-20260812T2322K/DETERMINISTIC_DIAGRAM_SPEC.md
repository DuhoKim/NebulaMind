# BHU closure video — deterministic diagram and motion specification

This is implementation detail beneath the gated `STORYBOARD_DRAFT_V3.json`. It adds no scientific claim and does not modify the exact-hash review targets. No frame may be generated before Lana, Goru, and Kun all pass the current script/storyboard hashes.

## Global visual contract

- Canvas: 1920×1080, 30 fps, square pixels.
- Safe area: x=120…1800, y=70…990. Caption baseline must remain above y=990.
- Palette: background `#090e18`; foreground `#edf2f8`; muted `#9aa8bc`; target blue `#76b6ff`; evidence amber `#f0b36b`; closure red `#d97b7b`; reopen green `#79c6a3`.
- Type: Arial/Helvetica. Assertion heading 54–62 px, diagram labels 30–38 px, small provenance 24 px. No critical text below 30 px.
- Heading occupies the top 170 px and remains visible for the full card.
- No divider cards, chapter interludes, logos-as-cards, decorative star fields, or character imagery.
- Motion is explanatory: draw a relation, reveal a comparison, or change a gate state. Nothing drifts merely to avoid a static frame.
- Every visual number must appear in Lana Revision 5. In particular, no numerical 95.4% lower-bound value may be drawn.
- Captions: sentence-level, two lines maximum, 42 px, dark translucent backing, bottom-safe. Suppress caption text that would exactly duplicate a large on-screen label for more than three consecutive seconds only if muted-view comprehension remains complete.
- Muted-view rule: heading + diagram + labels must communicate each card's assertion without narration.
- Transition: 8-frame dissolve between cards. No full-screen title transition.

## Card 01 — opening verdict map, 35 seconds

Assertion: `This route closed because it had no calibrated, identifying target`.

Geometry:

- Left column x=140…530: nested-horizon line icon, not realistic space art. Badge at y=300: `DUHO'S PERSONAL INTEREST`; second line: `NOT A NEBULAMIND RESEARCH FRONTIER`.
- Centre x=650…1050: a document stack labelled `PRIMARY SOURCES` feeding two horizontal arrows.
- Upper-right branch y=390: collapsed-star disk -> blue target marker -> `A NUMBER TO CHECK`.
- Lower-right branch y=680: stylized galaxy pair -> empty ruler -> split-cause glyph -> `NO PREDICTED EFFECT SIZE` and `NOT IDENTIFYING BY ITSELF`.
- Final closure bar y=890: `ROUTE CLOSED · IDEA NOT DECLARED TRUE OR FALSE`.

Motion beats:

- 0.0–3.0: question appears; personal-interest badge locks in immediately.
- 3.0–10.0: source documents draw; label `WE READ THE PRIMARY SOURCES`.
- 10.0–18.0: upper branch draws to number-to-check target.
- 18.0–27.0: lower branch draws; ruler stays blank; causal arrow splits.
- 27.0–35.0: route-closed bar lands and holds. Stakes, work, and verdict are all complete by this point.

Accessibility: do not depend on branch colour; use distinct target and split-arrow shapes.

## Card 02 — one label, different proposals

Assertion: `“Black-hole universe” names different proposals, not one model`.

Geometry:

- `BHU` capsule at x=150, y=440.
- Five proposal tiles in a 3+2 grid: closed-universe identification; collapse bounce; inherited rotation; CNS constants selection; other baby-universe work.
- Each tile has a distinct simple glyph and a different endpoint; no arrows reconverge.
- Bottom assertion: `NO SINGLE SHARED FORECAST`.

Motion:

- Fan out one tile at a time at 1.2-second intervals.
- Endpoints appear only after all tiles exist, making fragmentation the visual result rather than decoration.

## Card 03 — what makes an identifying test

Assertion: `A test needs a target that can be wrong—and identify the idea`.

This is the core reusable diagram.

Geometry:

- Model node x=220; target band x=720; measurement node x=1260.
- First pass: measurement dot lands outside a visible blue band; red label `CAN BE WRONG`.
- Second pass: a measurement dot points backward to two grey possible-cause nodes; amber label `NOT IDENTIFYING`.
- Final two-gate summary at bottom: `1 · A TARGET THAT CAN BE MISSED`; `2 · A RESULT THAT IDENTIFIES THE IDEA`.
- Plain-language neutron-star bridge appears on the right: `NEUTRON STARS · ULTRA-DENSE COLLAPSED CORES`; beneath it, `SPINNING, TIMED NEUTRON STARS ARE PULSARS`.

Motion:

- Build target test first, causal-identification test second, then show both gates together.
- This diagram returns in card 11 with the two gates locked/unlocked.

## Card 04 — one CNS chain supplies a mass test

Assertion: `One CNS chain puts a low ceiling on neutron-star mass`.

Geometry:

- Upper half: restrained lineage—universe -> black holes -> child universes with small parameter tick shifts. Label only `COSMOLOGICAL NATURAL SELECTION` and `CONSTANTS NEAR BLACK-HOLE-PRODUCING VALUES`.
- Lower half: mass axis 1.0…2.2 M☉.
- Blue marker at approximately 1.5: `BROWN–BETHE MAXIMUM ~1.5 M☉`.
- Amber source regime beginning around 2: `M ≳ 2 M☉`.
- Exact source consequence in a quote rail: `“SERIOUS DOUBT OR SIMPLY FALSIFY”` with Brown, Lee & Rho attribution.

Motion:

- Parameter lineage compresses into the mass axis.
- The ~1.5 marker lands first; the ≳2 regime appears second; the source quote appears last.

Do not imply all CNS proposals share this chain; heading and body must retain `One CNS chain`.

## Card 05 — pulsar measurements enter the named regime

Assertion: `Measured pulsars have entered the source’s approximately two-solar-mass regime`.

Geometry:

- Full interval plot, x-axis 1.4…2.2 M☉; no crop.
- Vertical reference at 2.00. Secondary muted reference at ~1.5.
- Row 1: `DEMOREST` point 1.97 and interval ±0.04, visibly crossing 2.
- Row 2: `FONSECA · 68.3%` point 2.08 and interval ±0.07, visibly above 2.
- A third qualitative rail labelled `FONSECA · 95.4%` crosses or reaches below 2 only as a categorical graphic. It must not terminate at or print an unstated number.
- Header strip: `EVERY DISTANT-STAR MASS HAS AN UNCERTAINTY RANGE`.

Motion:

- Explain the uncertainty convention by drawing point then whiskers.
- Draw Demorest first; pulse its centre below 2.
- Draw Fonseca 68.3%; shade interval above 2.
- Reveal 95.4% categorical rail and label `DOES NOT CLEAR 2.00`.

Numeric guard: permitted values are 1.97, 0.04, 2.08, 0.07, 68.3%, 95.4%, ~1.5, and 2.00. No inferred bound.

## Card 06 — do not choose a side of the source's “or”

Assertion: `The evidence enters the test regime; the packet does not call it falsification`.

Geometry:

- Dim card-05 plot behind two equal boxes: `SERIOUS DOUBT` and `SIMPLY FALSIFY`, joined by a large `OR`.
- Measurement arrow stops before the fork.
- Stop marker: `NOT ADJUDICATED HERE`.
- Bottom finding: `OBSERVATIONS ENTER THE SOURCE-NAMED REGIME`.

Motion:

- Arrow approaches, stops, and the two possible readings remain equally weighted. Never animate one as selected.

## Card 07 — the source really does assert unequal counts

Assertion: `The rotating-parent source explicitly says the two handedness counts should differ`.

Geometry:

- Parent black-hole cross-section left; simple rotation axis extends into a child-universe circle centre.
- Stylized galaxy disks align around axis.
- Right: two count bins `CW` and `CCW` connected by `≠`, with no bar heights or percentages.
- Footer: `EXPLICIT QUALITATIVE CLAIM · NO AMPLITUDE SHOWN`.

Motion:

- Axis transfers first; galaxy orientations turn toward it; unequal-count sign appears last.
- No invented magnitude, direction, or sky map.

## Card 08 — post-data claim, no numerical forecast

Assertion: `The handedness claim came after the cited data and never became a numerical forecast`.

Geometry:

- Timeline left-to-right: `CITED GALAXY STUDIES` then `2025 REVISION ADDS HANDEDNESS CLAIM`.
- Forecast contract beneath:
  - checked: `EQUATIONS FOR SPINNING SYSTEMS`;
  - empty outlined fields: `EXPECTED SIZE`; `SCALE / REDSHIFT RULE`; `INDEPENDENT DIRECTION`; `HIT-OR-MISS RANGE`.
- Bottom: `NOT A PREDICTION MADE BEFORE THE DATA`.

Motion:

- Studies appear before the revision marker.
- Mechanics field checks on; four forecast fields remain blank and pulse once, never filling.

## Card 09 — measurement does not identify cause

Assertion: `A real spin difference would still not identify a black-hole origin`.

Geometry:

- Centre node: `OBSERVED CW/CCW DIFFERENCE`.
- Backward inference arrow splits toward `BHU?` and `OTHER POSSIBLE CAUSES`.
- No specific rival model names or model glyphs.
- Bottom: `NOT BHU-SPECIFIC BY ITSELF`; final equation-like rail `MEASUREMENT ≠ IDENTIFICATION`.

Motion:

- Begin with the observation alone.
- Viewer attempts to follow arrow backward; it splits and cannot select one endpoint.
- Hold the final split for at least six seconds.

## Card 10 — the two independent closure failures

Assertion: `The spin route fails twice: no numerical target, and no unique signature`.

Geometry:

- Two-column ledger.
- Column 1, `NO PREDICTED EFFECT SIZE`: show a tiny effect and a zero-like result both entering a blank scoring ruler. Text: `NO OUTCOME SETTLES IT`.
- Column 2, `NO UNIQUE SIGNATURE`: show one observed node with split backward arrows. Text: `POSITIVE RESULT DOES NOT IDENTIFY BHU`.
- Both feed `ROUTE CLOSED`.
- Separate green-outlined box: `MEASUREMENT MAY STILL BE TRUSTWORTHY`.
- Final line: `THE HUNT HAD A SOURCE · IT DID NOT HAVE A TARGET`.

Motion:

- Demonstrate calibration failure, then identification failure, then close the route only after both are visible.

## Card 11 — the exact reopen conditions

Assertion: `Reopen this route only for a calibrated target or a unique signature`.

Geometry:

- Reuse card-03 model-target-measurement layout.
- Two locked gates: `CALIBRATED TARGET` and `UNIQUE SIGNATURE`.
- Token `CONFIRMED SPIN ASYMMETRY ALONE` reaches gates but unlocks neither.
- Two green keys appear as requirements:
  - `PUBLISHED EFFECT SIZE / SCALE / REDSHIFT RULE + PASS-OR-FAIL RANGE`;
  - `A FINGERPRINT ONLY BLACK-HOLE BIRTH WOULD LEAVE`.
- Final hold: `THIS ROUTE REOPENS ONLY WITH A CALIBRATED TARGET OR A UNIQUE SIGNATURE`.

Motion:

- Spin token fails both gates.
- Requirement keys reveal but do not imply they currently exist.
- End on assertion and reopen conditions. No credits, caveats, or publication prompt follows.

## Caption and muted-view QA

For every card, extract three frames: after heading settles, at the main logical transition, and at final hold. A reviewer must be able to state the assertion from each final hold without audio.

Caption checks:

- no caption exceeds two lines or 84 characters per line;
- no caption overlaps axis labels or source quotes;
- mathematical symbols (`≳`, `±`, `M☉`, `≠`) remain visually intact after H.264 encoding;
- caption timing begins within 200 ms of speech and ends no earlier than the spoken sentence;
- captions never introduce a number absent from Lana Revision 5.

## Encoded-artifact release checks

- 1920×1080, 30 fps, H.264 yuv420p, AAC audio.
- Opening verdict complete by encoded time ≤35.5 s, allowing one transition frame margin.
- All 11 headings remain readable at 1080p.
- Card 05 mass plot is full and uncropped; 68.3% versus 95.4% remains visually distinguishable.
- Card 06 never selects a side of the `OR`.
- Card 09 contains no rival-model assertion, named or pictorial.
- Final encoded frame carries the reopen verdict and nothing after it.
- `published.json` hash remains exactly the pre-build hash; no upload or registry write.
