# Lana — visual redesign spec: pictures that carry meaning, a faster voice, and the text cull

**Lana (science / claim-boundary seat), 2026-08-13.** Per Duho after watching V11: *"the narration
is a bit slow. and it's still a bit hard to understand, too many text boxes. if you use more
graphics, it would be much better."* Base bytes: V11 (narration `027a6e17…`, storyboard
`b0ec6a53…`). Yui redesigns from this spec; the full three-seat gate runs on the new bytes. **No
render authority here.**

**Owning it first:** both overturned decisions were ours. The 120–135 WPM band was our assumption —
he watched 128 and finds it slow; the viewer is the measure. And "too many text boxes" indicts the
design we congratulated ourselves on: we treated on-screen text as the comprehension mechanism, and
he is telling us that reading while listening is double work, not understanding. Several of our
eight "graphics" are text arranged in rectangles. This spec replaces the principle, not just the
instances.

---

## 0. The new principle, and the test that enforces it

**A graphic is something a viewer understands by LOOKING with the narration off and the text
blurred.** New render-QA test (extends the sound-off test): blur every text element in the frame —
if the card's claim is no longer recoverable, the card has failed the test. Words on screen are
allowed only as: (1) **verbatim quotations** (the source's own words are irreplaceable — the
Brown–Lee–Rho consequence, the two readings), (2) **chart data** (numbers at their marks on a real
plot), (3) **at most ONE short anchor line per card** — and (4) the **card-01 safety badge**, which
is Kun's release condition, kept as a small persistent corner tag with wording unchanged.

**The assertion-heading-on-every-card rule is retired.** It was our rule, inherited from an earlier
paper-video context, and it is the single largest source of "text boxes." Where a heading survives
below, it survives as the card's one anchor line; most cards now have none.

**A recurring metaphor kit** so pictures accumulate meaning instead of resetting each card: suns
for mass; a road with a gate for the route; a dartboard for testability; a footprint for
underdetermination; locks and keys for closure and reopening. Cards call back to earlier pictures
— that is what makes picture-thinking cheaper than reading by the video's second half.

## 1. Pacing ruling

**New band: 135–150 WPM, design point 142.** Not a polite split: 128 measured as "a bit slow" and
~+10% is the honest correction; if review still reads slow, the next stop is 150 and the band
allows it without re-gating. The constraint that survives: **the verdict must land inside the
spine** — at 142 WPM card 01's verdict sentence arrives at ≈ 29 s (better than V11's 32). Dwell
survives **only where it buys watching, not silence** — every dwell second below is attached to a
named visual event.

| Card | words | narration @142 | dwell (named event) | planned_seconds |
|---|---:|---:|---|---:|
| 01 | 80 | 34 s | +2 — the route gate closes | **36** |
| 02 | 82 | 35 s | +3 — fifth tile lights; five arrows end apart | **38** |
| 03 | 88 | 38 s | +4 — the two-archers beat (§2) | **42** |
| 04 | 101 | 43 s | +4 — the rising star meets the lid | **47** |
| 05 | 85 | 36 s | +8 — the widening band and its fade | **44** |
| 06 | 60 | 26 s | +3 — stopping at the fork | **29** |
| 07 | 68 | 29 s | +3 — unequal stacks; the "?" gap | **32** |
| 08 | 71 | 30 s | +4 — four empty slots revealed | **34** |
| 09 | 61 | 26 s | +4 — three animals appear over one footprint | **30** |
| 10 | 66 | 28 s | +5 — two locks close the gate | **33** |
| 11 | 69 | 30 s | +7 — keys tried, final hold on the gate | **37** |

**Total ≈ 402 s.** Note for Duho's expectation: runtime barely drops (415→402) because his "slow"
is *voice pace*, and the correction moves seconds from listening to looking — the voice gets ~11%
brisker while the freed time becomes animation dwell that is now doing visual work.

## 2. Card-by-card: text DELETED outright, and the picture that replaces it

*(DELETE means gone, not shortened. "Keep" lists are exhaustive — anything not listed is deleted.)*

- **Card 01.** DELETE four of five support strings ("WE READ THE PRIMARY SOURCES", "A NUMBER WE CAN
  CHECK", the galaxy-spin line, "ROUTE CLOSED · IDEA NOT DECLARED…") and the assertion heading.
  **Picture:** an open book (the sources) forks into two roads: one leads to a star with a small
  tag a hand can check off; the other leads to spinning galaxies dissolving into fog with a "?".
  As the verdict is spoken, a gate closes across the fog road — closed, not demolished (that is
  "not declared true or false", drawn). **Keep:** the safety badge as a persistent corner tag
  ("A PERSONAL SIDE-QUESTION · NOT PART OF THE LAB'S RESEARCH PROGRAMME" — wording frozen, Kun's
  condition), and one anchor line at the close: **ROUTE CLOSED**.
- **Card 02.** DELETE "ONE LABEL", "AT LEAST FIVE PROPOSALS IN THIS SURVEY", "NO SINGLE SHARED
  FORECAST", and the tiles' sentence-length captions. **Picture:** five tiles that are *icons*, not
  labelled boxes: nested circles (a universe inside a black hole); a ball's bounce arc; a spinning
  top handed parent-to-child; a family tree of little universes; a row of unlike fingerprints. Each
  lights as its phrase is spoken (reveal rule already governs this); their five arrows end at five
  visibly different places. **Keep:** tile captions of at most two words; one anchor line:
  **FIVE IDEAS — NO SHARED PREDICTION**. ("BHU" earning stays purely spoken; the fan's root tile
  may keep "BLACK-HOLE UNIVERSE (BHU)" per the witness-timing rule.)
- **Card 03 (the calibrated-target idea — pictorial at last).** DELETE the MODEL/TARGET/MEASUREMENT
  word-boxes and both requirement strings. **Picture — the dartboard sequence:** (i) an idea
  (small glowing orb) throws a dart at a board: *it can miss* — that is testability, watched;
  (ii) the board is removed and the dart sails into empty space — *nothing to miss* — untestable;
  (iii) **two different orbs hit the same board** — you cannot tell who threw — not identifying.
  The two-archers beat is the card's dwell. **Keep:** nothing but the board and the orbs; the
  neutron-star/pulsar definition is carried entirely by narration (it already is).
- **Card 04 (the mass ceiling).** DELETE "BROWN–BETHE MAXIMUM ~1.5 M☉" and "M ≳ 2 M☉" as text
  rows. **Picture:** a star inflating like a balloon, rising along a column of sun-icons; a hard
  lid sits at one-and-a-half suns (one sun icon + a half); above the lid, a zone marked by two sun
  icons. The star meets the lid — dwell. **Keep (exception 1 — quotation):** the source's own words
  **"SERIOUS DOUBT OR SIMPLY FALSIFY" — BROWN, LEE & RHO** on the two-sun zone; that is the one
  verbatim quote this card owns and text is the only honest way to carry a quotation.
- **Card 05 (already the most pictorial card — sharpen, don't rebuild).** DELETE "EVERY
  DISTANT-STAR MASS HAS AN UNCERTAINTY RANGE" (it is spoken — showing it too is the double work
  Duho named) and "NO 95.4% LOWER-BOUND VALUE IS QUOTED OR PLOTTED HERE" (a guard for us, not the
  viewer; it moves into render QA where it belongs). **Picture:** the axis gains sun-icon units
  (1.5 suns, 2 suns as pictograms at their marks); the two measurements are horizontal bars with
  star icons at their centres; **1.97 ± 0.04 and 2.08 ± 0.07 stay printed at their bars — chart
  data, exception 2**; the widening-band animation with the open-ended fade stays exactly as
  frozen (no-terminus rule untouched). **Keep:** one callout only — **AT 95.4% CREDIBILITY, THE
  CLOSING RECORD STATES ONLY THAT THE RESULT DOES NOT CLEAR 2.00** (the packet-permitted statement
  must remain in words; it is the card's single anchor).
- **Card 06 (the two-readings disjunction).** DELETE "NOT ADJUDICATED HERE" and "OBSERVATIONS ENTER
  THE SOURCE-NAMED REGIME". **Picture — the fork:** a road forks at a signpost with two arms
  carrying the quoted words (exception 1): **SERIOUS DOUBT** / **SIMPLY FALSIFY**, joined by a
  small **OR**. The camera (a walking figure, or the measurement-dot from card 05) arrives at the
  fork and **stops** — dwell on the standing-still. Refusal to adjudicate, drawn, not written.
- **Card 07.** DELETE all four support strings. **Picture:** two stacks of small galaxy icons, one
  stack visibly taller; the galaxies in one stack rotate clockwise, the other counterclockwise
  (small animated arrows); between the stack tops, a gap marked only **"?"** — the missing number,
  drawn as a missing number. (The old "NO AMPLITUDE SHOWN" footer is now the "?" itself.)
- **Card 08.** DELETE "OBSERVATIONS CITED FIRST", "HANDEDNESS CLAIM ADDED IN 2025", "NOT A
  PREDICTION MADE BEFORE THE DATA", "EQUATIONS PRESENT", and the long absence string. **Picture:**
  a timeline where survey-photo icons drop first, then a speech bubble pops from a paper icon
  *after* them (the after-ness is watched, not read; keep the year tag **2025** on the bubble —
  chart data). The four absences become four **empty picture slots**: a blank ruler, a blank map,
  a compass with no needle, a pass/fail meter with no needle — each with a small "?".
- **Card 09 (the rival-cause problem — the strongest possible picture exists, use it).** DELETE
  "OBSERVED CW/CCW DIFFERENCE", "BHU?", "OTHER POSSIBLE CAUSES", "NOT BHU-SPECIFIC BY ITSELF".
  **Picture — one footprint, three animals:** a single footprint in the ground; three different
  unlabeled animal silhouettes fade in around it, each of whose paw could have left it. A hand
  points from the print toward the animals and the pointer splits three ways. Underdetermination,
  understood by looking. (Unlabeled silhouettes also honour C12's no-named-rivals boundary better
  than the old labelled boxes did.) **Keep:** one anchor line: **MEASUREMENT ≠ IDENTIFICATION**.
- **Card 10.** DELETE both numbered failure strings, the long scoring sentence, and — yes — the
  on-screen "THE HUNT HAD A SOURCE · IT DID NOT HAVE A TARGET" (it is the *spoken* signature line;
  printing it too was double work). **Picture — the callback:** the card-01 road gate returns; two
  locks close onto it, and each lock's face is a miniature of an earlier picture: the blank ruler
  (no size), the footprint (no unique cause). The gate is locked by exactly the two things the
  viewer has already seen. Dwell on the second lock clicking.
- **Card 11.** DELETE both REOPEN CONDITION strings and "SPIN ASYMMETRY ALONE IS NOT A BHU TEST".
  **Picture:** the same locked gate with two keyholes; two keys are offered — a ruler-key with a
  marked range on its blade (the calibrated target) and a fingerprint-key (the unique signature);
  the unequal-stacks token from card 07 approaches and fits **neither** keyhole. Final hold: the
  gate with its two keyholes, lit. **Keep:** one closing anchor line, the video's last words on
  screen: **REOPENS ONLY WITH A NUMBER — OR A FINGERPRINT** (requirement-first ending preserved).

**Net text census: from ~45 on-screen strings to 11 anchors + 3 quotations + chart data.**

## 3. The six pictorial treatments Hwao named, mapped

Mass ceiling → card 04's balloon-star and lid (suns as units). Two-readings disjunction → card 06's
fork and the stop. Five proposals → card 02's icon tiles diverging. Calibrated target → card 03's
dartboard (miss / no board / same board twice). Rival-cause → card 09's footprint and three
animals. Closing verdict → cards 10–11's gate, locks, and keys — closure and its reopening
conditions as one continuous object.

## 4. What survives untouched (the ledger of things this redesign must not break)

The claim ledger (no picture may overclaim: the fog road is closed, never demolished; the animals
are unlabeled; the "?" gap replaces any invented amplitude); the card-05 **no-terminus** rule and
its fade; the **reveal-no-earlier-than-witness** rule (now cheaper — fewer texts to time); the
card-01 **safety badge verbatim** (Kun re-verifies); all **verbatim quotations**; the spoken
narration of V11 **unchanged word-for-word** (this pass is visual + pace only, so the script gates
carry); verdict-in-spine (improved to ≈29 s); zero seat names; the shorthand audit's witnesses
(unchanged narration keeps every witness phrase intact).

## 5. The generated-imagery layer (added on Duho's authorisation, Hwao's addendum — same day)

Duho has authorised generation tools ("Gemini's image or video and so on"). This is the real
unblock behind §0: a text box is what you make when you cannot make a picture. The boundary,
restated as build rules:

**Allowed (illustrative layer, carries no number):** metaphor and atmosphere. **Forbidden
(claim-bearing layer):** anything quantitative — no generated axes, scales, error bars, plotted
points, magnitude comparisons, or geometry that encodes a measurement. A model that invents a tick
is the fabricated-precision defect in its fourth disguise. **Also out:** anything that could be
read as an actual observation, survey image, real person, or real facility-as-data. **All legible
on-screen text is composited locally** — generated text is unreliable at our sizes, and every
anchor/quote/datum in §2 stays a local composite.

**Per-card assignment (G = generated still, D = deterministic local, C = local composite text):**

| Card | Generate (stills; stylized/painterly, never survey-like) | Stays deterministic |
|---|---|---|
| 01 | the open book, the two roads, fog, the star; the gate as a prop | gate-closing motion (D animation over the G still); badge + ROUTE CLOSED (C) |
| 02 | five tile illustrations: nested universes, bouncing collapse, handed-down spinning top, universe family tree, unlike fingerprints | tile reveal timing (D, witness rule); captions (C) |
| 03 | dartboard, darts, the two orbs — as painterly props | the three-beat sequence logic and motion (D); no text |
| 04 | the inflating star as a prop; backdrop | **the entire mass gauge: column, sun-icon units, lid position, two-sun zone — D, because its geometry encodes 1.5 vs ≳2**; the star composites onto the D gauge; quotation (C) |
| 05 | backdrop atmosphere only | **everything else — the whole card is chart. Axis, bars, values, widening band, fade: D, untouched, no-terminus rule intact**; callout (C) |
| 06 | the fork road, signpost, the walking figure | signpost arm words = quotations (C); the stop timing (D) |
| 07 | galaxy icons for the stacks (visibly spiral, stylized) | stack heights and the "?" gap (D — the inequality is qualitative but the *absence of a number* is the claim; no generated geometry may suggest a ratio); rotation arrows (D) |
| 08 | survey-photo icons, the paper + speech bubble; the four empty props (blank ruler, blank map, needleless compass, needleless meter) | timeline order and 2025 tag (D/C) |
| 09 | the footprint; three unlabeled animal silhouettes | the three-way pointer split (D); anchor line (C) |
| 10 | gate + lock props (reuse 01's gate) | lock-face miniatures (blank ruler, footprint — reuse of D/G assets); click timing (D) |
| 11 | the two keys (ruler-blade key, fingerprint key) | keyhole fit/refusal motion (D); closing anchor (C) |

**Rules that govern the layer:** prefer stills animated deterministically over generated video (per
the addendum; motion is where determinism is cheap and generation is unreliable); any generated
image that could plausibly be read as "this is what we saw" is rejected at build — stylization is
the first defence, and where a card still risks the reading, a small **ILLUSTRATION** corner tag
(C) is mandatory; generated stills are retained as files with their prompts and hashes in the build
matrix so the render is reproducible-in-place even though generation itself is not deterministic;
cost is permitted but logged (Yui notes spend per asset; Goru's lane holds the Gemini access —
coordinate through Hwao's routing, and check actual availability before designing around any
specific tool). **With real pictures available, the §2 deletions stand with more confidence — no
deleted string returns as a caption.** The three quotations, eleven anchors, and chart data remain
the only words on screen.

## 6. Gate notes

Yui builds; the full three-seat gate runs on the new bytes. My delta focus: the blur test on all
eleven cards, the card-05 callout as sole survivor, the badge, whether the metaphor kit stays
consistent card-to-card, and — new with §5 — **the generation boundary: no generated pixel inside
any quantitative element (cards 04 and 05 audited frame-by-frame), no generated on-screen text, no
image readable as an observation, ILLUSTRATION tags where stylization alone doesn't settle it, and
prompts+hashes for every generated asset in the build matrix.** Pacing at 142 gets the per-card WPM audit as standard. If Duho still reads
the voice as slow at review, the band's ceiling (150) is pre-authorized by this ruling — that
adjustment would be planned_seconds arithmetic only, not a design change.

— Lana, 2026-08-13. Spec only; no render authority.
