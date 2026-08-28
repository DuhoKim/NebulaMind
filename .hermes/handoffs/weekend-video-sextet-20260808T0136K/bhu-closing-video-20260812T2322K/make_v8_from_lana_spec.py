#!/usr/bin/env python3
"""Build BHU V8 from the exact V7 bytes and the full simplify/de-name spec.

This script performs 27 audited copy replacement units and installs the eight-
graphic V8 contract. It never renders, synthesizes audio, uploads, or edits V7.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path

D = Path(__file__).resolve().parent
V7_STORY = D / "STORYBOARD_DRAFT_V7.json"
V7_NARR = D / "NARRATION_DRAFT_V7.md"
V7_LEDGER = D / "CLAIM_LINE_LEDGER_V7.md"
SPEC = D / "LANA_SIMPLIFY_AND_DENAME_SPEC.md"
V8_STORY = D / "STORYBOARD_DRAFT_V8.json"
V8_NARR = D / "NARRATION_DRAFT_V8.md"
V8_LEDGER = D / "CLAIM_LINE_LEDGER_V8.md"
V8_GRAPHICS = D / "DETERMINISTIC_DIAGRAM_SPEC_V8.md"
V8_MATRIX = D / "V8_BUILD_MATRIX.json"

EXPECTED = {
    V7_STORY.name: "3077f0636385487bb4092d2032c18bbedaedb647780bbfc581e59027c87a8d2b",
    V7_NARR.name: "3380497f0514e906db8463d0fdd2ffd1f0b02b37ac6825e3bfdec86011c2edc0",
    V7_LEDGER.name: "871a808c4f2af94e24ef68b19cef416b7f7e3295720dab25ef8676753c845b5a",
    SPEC.name: "53e2c694334cdb9913e8d14e91032dbfb552e5c2eee5d1aea75360403f4b3274",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for path in (V7_STORY, V7_NARR, V7_LEDGER, SPEC):
    actual = sha(path)
    if actual != EXPECTED[path.name]:
        raise SystemExit(f"input hash mismatch {path.name}: {actual}")

story = json.loads(V7_STORY.read_text())
original = copy.deepcopy(story)
cards = {c["id"]: c for c in story["cards"]}
replacements: list[dict] = []


def replace_once(rid: str, card_id: str, field: str, old: str, new: str, note: str) -> None:
    target = cards[card_id]
    if field.startswith("on_screen_support["):
        idx = int(field.removeprefix("on_screen_support[").removesuffix("]"))
        value = target["on_screen_support"][idx]
        if value.count(old) != 1:
            raise SystemExit(f"{rid} anchor count {value.count(old)} != 1")
        target["on_screen_support"][idx] = value.replace(old, new)
    else:
        value = target[field]
        if value.count(old) != 1:
            raise SystemExit(f"{rid} anchor count {value.count(old)} != 1")
        target[field] = value.replace(old, new)
    replacements.append({"id": rid, "card": card_id, "field": field, "old": old, "new": new, "note": note})


# 27 copy-replacement units from the spec. Graphic geometry updates are tracked
# separately below and do not inflate this count.
replace_once("R01", "01", "narration",
    "This is Duho's personal interest, outside the lab's research programme.",
    "It's a question we were personally curious about — a side-interest, not part of the lab's research programme.",
    "A1 exact personal-curiosity/lab-programme boundary")
replace_once("R02", "01", "on_screen_support[0]",
    "DUHO'S PERSONAL INTEREST · NOT PART OF THE LAB'S RESEARCH PROGRAMME",
    "A PERSONAL SIDE-QUESTION · NOT PART OF THE LAB'S RESEARCH PROGRAMME",
    "A1 exact full-card badge")
replace_once("R03", "01", "diagram",
    "PERSONAL INTEREST badge",
    "A PERSONAL SIDE-QUESTION · NOT PART OF THE LAB'S RESEARCH PROGRAMME badge",
    "A1 diagram badge instruction")
replace_once("R04", "01", "narration",
    "We read primary sources for their predictions.",
    "We read the original scientific papers to see what they actually predict.",
    "B-01 original-paper wording")
replace_once("R05", "01", "narration",
    "One branch gives neutron stars a number to check.",
    "One of these ideas gives us a number we can check against real stars.",
    "B-01 defer neutron-star term")
replace_once("R06", "01", "narration",
    "and a measurement could not identify a black-hole origin.",
    "and even a perfect measurement couldn't tell us a black hole was the cause.",
    "B-01 plain identification failure")
replace_once("R07", "01", "on_screen_support[2]",
    "NEUTRON STARS: A NUMBER TO CHECK",
    "A NUMBER WE CAN CHECK",
    "G8 branch label")
replace_once("R08", "02", "narration",
    "The first surprise is structural.",
    "Here's the first surprise.",
    "B-02 plain opening")
replace_once("R09", "02", "narration",
    "Lana found at least five different proposals under this label—black-hole universe, or BHU for short. One identifies a closed universe with a black hole. Another says collapse rebounds—a bounce—instead of crushing to a point. Another inherits rotation. Cosmological natural selection asks whether black-hole production shapes physical constants—the fixed numbers built into physics. Other baby-universe work points to different observables. They do not share one forecast.",
    "We found at least five different proposals under this label — black-hole universe, or BHU for short. A closed universe inside a black hole. A collapse that bounces instead of crushing to a point. A universe that inherits its parent's spin. Universes that reproduce, tuning the numbers built into physics. And baby universes with entirely different fingerprints. Five ideas — and no shared prediction. We wrote what we found into a closing record — the document this video reports from.",
    "A2 referent introduction plus B-02 compressed list")
replace_once("R10", "03", "narration",
    "And the result must point back to the idea, rather than leave several possible causes.",
    "And if you find it, it has to point back at that one idea — not at three different ones.",
    "B-03 plain identification requirement")
replace_once("R11", "03", "narration",
    "Lana found one clean numerical test in the family she surveyed.",
    "In the whole family we surveyed, the closing record found one clean numerical test.",
    "A2 attribution form")
replace_once("R12", "04", "narration",
    "In cosmological natural selection, universes reproduce through black holes with slightly changed constants. Those constants should sit near values that favour black-hole production.",
    "One proposal says universes have children: every black hole buds off a new universe with slightly different physics. Over many generations, that would tune physics toward making black holes.",
    "B-04 move and simplify the proposal definition")
replace_once("R13", "04", "narration",
    "In the Brown–Lee–Rho chain Lana surveyed,",
    "In the Brown–Lee–Rho chain our record surveyed,",
    "A2 de-name while retaining published authors")
replace_once("R14", "04", "narration",
    "That is a real, falsifiable number.",
    "That's a real test — a number that could be proven wrong.",
    "B-04 plain falsifiability")
replace_once("R15", "05", "narration", cards["05"]["narration"],
    "Weighing a star thousands of light-years away is hard, so every measurement comes with an uncertainty range. Two heavy pulsars matter here. One weighs in at one point nine seven Suns, give or take point zero four — just under two. The other: two point zero eight, give or take point zero seven. At the sixty-eight point three percent level the paper quotes, that one clears two Suns. At the stricter ninety-five point four percent level, the closing record says it does not.",
    "B-05 whole-card S4b merge")
replace_once("R16", "06", "narration",
    "This is where restraint matters.",
    "Here we have to be careful.",
    "B-06 plain opening")
replace_once("R17", "06", "narration",
    "Lana's closing record does not decide which side applies, and neither will this video.",
    "The closing record does not decide which side applies — and neither does this video.",
    "A2 attribution-not-adjudication")
replace_once("R18", "07", "narration",
    "The spin lane was not chasing a phantom.",
    "Our search wasn't chasing a phantom.",
    "B-07 retire crew vocabulary")
replace_once("R19", "07", "narration",
    "It followed an explicit, source-backed qualitative claim.",
    "The claim really is there in the paper — in words. What's missing is any number to go with it.",
    "B-07 plain source/magnitude boundary")
replace_once("R20", "08", "narration",
    "no rule for how it changes with scale or redshift",
    "no rule for where or when it should be stronger",
    "B-08 remove unearned redshift term")
replace_once("R21", "08", "diagram", "SIZE,", "SIZE?,", "G5 plain blank 1")
replace_once("R22", "08", "diagram", "SCALE/REDSHIFT LAW,", "WHERE/WHEN?,", "G5 plain blank 2")
replace_once("R23", "08", "diagram", "INDEPENDENT DIRECTION,", "DIRECTION?,", "G5 plain blank 3")
replace_once("R24", "08", "diagram", "ACCEPTANCE RANGE.", "PASS-OR-FAIL RANGE?.", "G5 plain blank 4")
replace_once("R25", "09", "narration",
    "One observed number would have more than one possible interpretation unless a BHU model supplied a unique signature.",
    "The same lopsided sky could come from several different causes. Without a fingerprint only a black-hole birth would leave, the measurement can't pick one.",
    "B-09 plain split-cause/fingerprint language")
replace_once("R26", "10", "narration",
    "A finite-precision spin result cannot be scored against a source-defined pass-or-fail range, because the source gives no predicted size.",
    "There's no pass-or-fail range to grade a measurement against — the idea never says how big the effect should be.",
    "B-10 proposed line; ships only with Kun sign-off")
replace_once("R27", "11", "narration",
    "a published calculation connecting parent-black-hole parameters to a handedness amplitude, scale, or redshift dependence, with a pass-or-fail range.",
    "a published calculation that says how big the spin difference should be — with a pass-or-fail range.",
    "B-11 plain reopen condition")

if len(replacements) != 27:
    raise SystemExit(f"expected 27 copy replacements, got {len(replacements)}")

# Eight graphics. G4 and G6 are Lana's two unnumbered existing GRAPHIC directives;
# the IDs fill the deliberate gaps without adding content.
graphics = [
    {"id": "G1", "card": "02", "status": "revision", "idea": "five proposals, no shared forecast"},
    {"id": "G2", "card": "04", "status": "new", "idea": "a ceiling on neutron-star mass"},
    {"id": "G3", "card": "05", "status": "new", "idea": "stricter standard means a wider interval, without fabricated precision"},
    {"id": "G4", "card": "03", "status": "existing-retained", "idea": "a target a measurement can miss, plus identifying one idea"},
    {"id": "G5", "card": "08", "status": "revision", "idea": "the missing forecast contract"},
    {"id": "G6", "card": "09", "status": "existing-retained", "idea": "the same signature cannot distinguish several causes"},
    {"id": "G7", "card": "10", "status": "existing-retained", "idea": "a measurement cannot be graded without a range"},
    {"id": "G8", "card": "01", "status": "revision", "idea": "opening verdict map and personal/lab boundary"},
]

# G8 — keep the existing verdict-map geometry. A1 already replaced the badge
# instruction above; change only the branch label named by B-01. The full-card,
# frame-one hold is an execution invariant in the detailed graphics contract.
if cards["01"]["diagram"].count("NEUTRON STARS -> NUMBER TO CHECK") != 1:
    raise SystemExit("G8 branch-label anchor mismatch")
cards["01"]["diagram"] = cards["01"]["diagram"].replace(
    "NEUTRON STARS -> NUMBER TO CHECK", "A NUMBER WE CAN CHECK"
)
cards["01"]["diagram"] += " Keep the exact boundary badge visible from frame one for the full card."

# G1 — the tiles, not narration, carry the structural distinctions.
cards["02"]["diagram"] = (
    "G1 sound-off fan. One label BLACK-HOLE UNIVERSE (BHU) fans into five compact tiles that light "
    "one-by-one in spoken order: CLOSED UNIVERSE INSIDE A BLACK HOLE; COLLAPSE BOUNCES; INHERITS "
    "PARENT'S SPIN; UNIVERSES REPRODUCE AND TUNE PHYSICS; BABY UNIVERSES WITH DIFFERENT "
    "FINGERPRINTS. Give each tile a distinct mechanism glyph. Each output arrow ends at a different "
    "visible point and no arrows reconverge. Final state holds FIVE IDEAS · NO SINGLE SHARED "
    "FORECAST and introduces a document icon labelled CLOSING RECORD · THE DOCUMENT THIS VIDEO "
    "REPORTS FROM. No cosmic montage."
)

# G4 is explicitly unchanged by B-03. The existing on-screen support already
# carries the neutron-star and pulsar definitions when muted.
if cards["03"]["diagram"] != original["cards"][2]["diagram"]:
    raise SystemExit("G4 changed despite B-03 unchanged instruction")

# G2 — the lid is the proposal's maximum, not a measured experimental result.
cards["04"]["diagram"] = (
    "G2 sound-off family tree and mass ceiling. First draw one parent universe producing black holes; "
    "each black hole buds a child universe with a small physics-setting shift. Collapse that lineage "
    "into a full mass gauge. A bar labelled POSSIBLE NEUTRON-STAR MASS rises toward a hard lid labelled "
    "BROWN–BETHE MAXIMUM ~1.5 M☉. Separately shade the source's approximate M ≳ 2 M☉ regime and "
    "place the exact quote inside that region: SERIOUS DOUBT OR SIMPLY FALSIFY — BROWN, LEE & RHO. "
    "Make clear this is one proposal's predicted ceiling, not an experiment being run and not a rule "
    "shared by every proposal. No unsupported equation-of-state detail."
)

# G3 — exact Lana instruction plus an exhaustive position-bearing prohibition.
cards["05"]["diagram"] = (
    "G3 sound-off full horizontal mass axis from 1.4 to 2.2 M☉. Keep the source's ~1.5 marker and the "
    "approximate M ≳ 2 M☉ regime. Row 1 prints DEMOREST: 1.97 ± 0.04 M☉, with its centre below 2.00 "
    "and interval crossing 2.00. Row 2 prints FONSECA: 2.08 ± 0.07 M☉ · 68.3%, with that interval "
    "above 2.00. Animate the Fonseca interval widening as a non-scaled mode label outside the mass "
    "plot changes from 68.3% to 95.4%: the "
    "lower side becomes a continuous open-ended gradient that fades through the 2.00 line with no "
    "drawn terminus. Retain a separate non-scaled callout: AT 95.4% CREDIBILITY, THE CLOSING RECORD "
    "STATES ONLY THAT THE RESULT DOES NOT CLEAR 2.00; NO LOWER-BOUND VALUE IS QUOTED HERE. Hard "
    "constraint: draw no 95.4% endpoint, arrow, tick, bracket, marker, whisker, shaded boundary, "
    "axis-aligned glyph, or other position-bearing terminus at any scaled mass value. The gradient "
    "must have no visible edge that could be read as a lower bound. No inferred bound."
)

# Card 06 diagram remains semantically unchanged; its V7 form already executes A2.

# G5 — four plain blanks; equations remain acknowledged.
cards["08"]["diagram"] = (
    "G5 sound-off timeline and forecast contract. Timeline: CITED GALAXY STUDIES first; HANDEDNESS "
    "CLAIM ADDED IN 2025 later. Beneath it, show EQUATIONS FOR SPINNING SYSTEMS as present, then four "
    "large empty outlined blanks labelled exactly SIZE? · WHERE/WHEN? · DIRECTION? · PASS-OR-FAIL "
    "RANGE?. The blanks pulse once and never fill. End on NOT A PREDICTION MADE BEFORE THE DATA. Do "
    "not say the source contains no numbers or equations and do not imply an experiment was run."
)

# G6 is explicitly unchanged by B-09; preserve the V7 diagram byte-for-byte.
if cards["09"]["diagram"] != original["cards"][8]["diagram"]:
    raise SystemExit("G6 changed despite B-09 unchanged instruction")

# G7 remains the blank-ruler carrier. Remove only the crew-internal word
# 'ledger'; the visual construction and all printable labels are unchanged.
cards["10"]["diagram"] = cards["10"]["diagram"].replace(
    "Two-column fail-closed ledger.", "G7 sound-off two-column fail-closed comparison."
)
if "ledger" in cards["10"]["diagram"].lower():
    raise SystemExit("crew-internal ledger vocabulary remains in Card 10 diagram")

# Storyboard filing and no-render state.
story["status"] = "V8_FROZEN_FOR_FULL_THREE_SEAT_EXACT_HASH_GATE_NO_AUDIO_NO_RENDER"
story["estimated_duration_seconds"] = sum(c["planned_seconds"] for c in story["cards"])
story["paid_generation_notes"] = []

# Preserve claim IDs and packet-line mappings exactly.
for old, new in zip(original["cards"], story["cards"]):
    if old["id"] != new["id"] or old["source_claims"] != new["source_claims"] or old["packet_lines"] != new["packet_lines"]:
        raise SystemExit(f"claim mapping changed on card {old['id']}")

V8_STORY.write_text(json.dumps(story, indent=2, ensure_ascii=False) + "\n")

# Generate the standalone narration from the canonical storyboard, fixing stale
# V5/V7 filing labels while preserving internal source scaffolding.
lines = [
    "# BHU closure video — narration draft V8",
    "",
    "Status: frozen for full three-seat exact-hash re-gate. No audio or render authority.",
    "",
    "This file is generated from `STORYBOARD_DRAFT_V8.json`; narration must match 11/11 before gate.",
    "",
    "Sole source: Lana Revision 5, SHA-256 `b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516`.",
    "",
]
for card in story["cards"]:
    lines += [
        f"## Card {card['id']} — assertion heading",
        "",
        f"**{card['heading']}**",
        "",
        card["narration"],
        "",
        f"Source: {', '.join(card['source_claims'])}; packet lines {', '.join(card['packet_lines'])}.",
        "",
    ]
lines += [
    "## Paid-generation notes",
    "",
    "None. Deterministic local diagrams are more exact than generated footage for every planned shot. No paid-generation placeholder is justified.",
    "",
]
V8_NARR.write_text("\n".join(lines))

# Claim content stays internal and unchanged; update only the stale version H1.
ledger = V7_LEDGER.read_text()
if ledger.count("# BHU closure video — claim-to-line ledger V5") != 1:
    raise SystemExit("ledger H1 anchor mismatch")
V8_LEDGER.write_text(ledger.replace(
    "# BHU closure video — claim-to-line ledger V5",
    "# BHU closure video — claim-to-line ledger V8",
))

# Detailed eight-graphic contract. Viewer text is quoted exactly; build language
# remains non-claiming and sound-off sufficient.
graphics_md = """# BHU closure video — deterministic diagram and motion specification V8

Status: frozen for full three-seat exact-hash re-gate. No audio or render authority.

This implementation specification is subordinate to `STORYBOARD_DRAFT_V8.json` and the sole scientific authority packet. It adds no claim. Every assertion heading remains visible for its full card. Every graphic must communicate its card's assertion with the sound off. No graphic may imply an experiment was run.

## Global invariants

- 1920×1080, 30 fps, deterministic local diagrams only; no paid generation.
- Assertion heading on every card; no divider cards.
- Personal/lab boundary badge is visible from Card 01 frame one and held for the full card.
- Published-author attributions Brown, Lee, Rho, Brown–Bethe, Demorest, and Fonseca remain.
- No viewer-facing personal or seat names; no crew-internal vocabulary, filenames, or hashes.
- No fabricated precision. In particular, no 95.4% endpoint, arrow, tick, bracket, marker, whisker, shaded boundary, axis-aligned glyph, or position-bearing terminus at any scaled mass value.
- A 95.4% gradient may widen and fade through 2.00 only with no visible lower edge or terminus; the separate non-scaled text states only that the result does not clear 2.00.
- The closing record is introduced as a document in Card 02 before Cards 03–06 attribute any finding to it.

## G8 — Card 01: verdict map and boundary

- Frame-one full-card badge: `A PERSONAL SIDE-QUESTION · NOT PART OF THE LAB'S RESEARCH PROGRAMME`.
- Retain the V7 three-column verdict map; change its target branch label only to `A NUMBER WE CAN CHECK`.
- Retain the galaxy-spin branch's no-size and non-identifying logic without adding geometry.
- Both boundary markers are visible inside the first ten seconds; route verdict is complete by 35 seconds.

## G1 — Card 02: five proposals, no shared forecast

- One BHU label fans to five distinct mechanism tiles in spoken order.
- Each tile lights with its phrase; each output ends at a different point; nothing reconverges.
- Final hold: `FIVE IDEAS · NO SINGLE SHARED FORECAST`.
- Introduce a visible document icon: `CLOSING RECORD · THE DOCUMENT THIS VIDEO REPORTS FROM`.

## G4 — Card 03: a missable target and an identifying result

- Retain the V7 Card-03 `MODEL → TARGET BAND → MEASUREMENT` diagram byte-for-byte.
- Its existing miss and backward-splitting states already show the two test requirements.
- Its existing on-screen support, not new geometry, defines neutron stars and pulsars.

## G2 — Card 04: proposal family tree and mass ceiling

- One proposal's black holes bud child universes with small physics-setting shifts.
- The lineage becomes a mass gauge with a hard lid at `BROWN–BETHE MAXIMUM ~1.5 M☉`.
- The separate `M ≳ 2 M☉` region carries `SERIOUS DOUBT OR SIMPLY FALSIFY — BROWN, LEE & RHO`.
- The lid is a source prediction, not an experiment result and not a rule shared by all proposals.

## G3 — Card 05: stricter credibility, wider interval

- Print `DEMOREST: 1.97 ± 0.04 M☉` and `FONSECA: 2.08 ± 0.07 M☉ · 68.3%` exactly once.
- The 68.3% interval is finite and remains above 2.00.
- At 95.4%, widen into a continuous open-ended gradient whose lower side fades through 2.00 with no visible terminus; the 95.4% mode label stays non-scaled and outside the mass plot.
- Keep the non-scaled callout and `NO 95.4% LOWER-BOUND VALUE IS QUOTED OR PLOTTED HERE`.
- Absolute prohibition: no 95.4% endpoint, arrow, tick, bracket, marker, whisker, shaded boundary, axis-aligned glyph, or position-bearing terminus.

## G5 — Card 08: the missing forecast contract

- Timeline places cited studies before the 2025 handedness claim.
- `EQUATIONS FOR SPINNING SYSTEMS` is present.
- Four large blanks remain empty: `SIZE? · WHERE/WHEN? · DIRECTION? · PASS-OR-FAIL RANGE?`.
- End on `NOT A PREDICTION MADE BEFORE THE DATA`.

## G6 — Card 09: same signature, several causes

- Retain the V7 Card-09 backward-splitting inference diagram byte-for-byte.
- It already splits one observed `CW/CCW DIFFERENCE` toward `BHU?` and `OTHER POSSIBLE CAUSES`.
- It already ends on `MEASUREMENT ≠ IDENTIFICATION`; name no rival model.

## G7 — Card 10: no range, nothing to grade against

- Retain the V7 Card-10 construction and printable labels, changing only the internal layout word `ledger` to `comparison` in the non-printing instruction.
- Keep the blank scoring ruler labelled `NO PREDICTED SIZE`.
- Show `MEASUREMENT MAY STILL BE TRUSTWORTHY` separately from route closure.
- The graphic must carry the calibration failure even if the proposed B-10 sentence is vetoed.

## Final sound-off QA

Extract early, transition, and final-hold frames for all 11 cards. A paper-naive viewer must recover each assertion from heading plus diagram without narration. Specifically test the Card-03 miss, Card-09 same-signature split, Card-04 ceiling, and Card-05 no-terminus constraint. Full three-seat exact-hash PASS is required before any TTS, frame generation, or render.
"""
V8_GRAPHICS.write_text(graphics_md)

# Audience projection and build matrix are explicit verification artifacts.
audience_projection = {
    "title": story["title"],
    "slug": story["slug"],
    "cards": [
        {
            "id": c["id"],
            "heading": c["heading"],
            "narration": c["narration"],
            "diagram": c["diagram"],
            "on_screen_support": c["on_screen_support"],
        }
        for c in story["cards"]
    ],
}
matrix = {
    "status": "V8_BUILT_NOT_REVIEWED_NO_AUDIO_NO_RENDER",
    "base": {p.name: EXPECTED[p.name] for p in (V7_STORY, V7_NARR, V7_LEDGER)},
    "spec": {"path": SPEC.name, "bytes": SPEC.stat().st_size, "sha256": EXPECTED[SPEC.name]},
    "copy_replacement_count": len(replacements),
    "copy_replacements": replacements,
    "graphics_count": len(graphics),
    "graphics": graphics,
    "audience_projection": audience_projection,
    "b10_disposition": "included exactly as proposed; requires Kun sign-off; no render authority",
    "unchanged_contracts": [
        "11 assertion headings unchanged",
        "source_claim IDs and packet-line mappings unchanged",
        "published-author citations retained",
        "no fabricated 95.4% lower bound",
        "no experiment-run implication",
        "local deterministic diagrams only",
    ],
}
V8_MATRIX.write_text(json.dumps(matrix, indent=2, ensure_ascii=False) + "\n")

print(json.dumps({
    "wrote": [p.name for p in (V8_STORY, V8_NARR, V8_LEDGER, V8_GRAPHICS, V8_MATRIX)],
    "copy_replacements": len(replacements),
    "graphics": len(graphics),
    "hashes": {p.name: sha(p) for p in (V8_STORY, V8_NARR, V8_LEDGER, V8_GRAPHICS, V8_MATRIX)},
}, indent=2))
