#!/usr/bin/env python3
"""Build the exact-hash BHU V5 script/storyboard/ledger delta.

Inputs remain byte-preserved. The narration is generated from the storyboard so
reviewed speech cannot diverge from the eventual render source.
"""
from pathlib import Path
import json

D = Path(__file__).resolve().parent
sb = json.loads((D / "STORYBOARD_DRAFT_V3.json").read_text())
sb["status"] = "V5_FROZEN_FOR_DELTA_REGATE_NO_AUDIO_NO_RENDER"

cards = {card["id"]: card for card in sb["cards"]}

# Lana S1 + the R10 plain-language sub-item, plus Kun's neutron-star precision note.
cards["01"]["narration"] = (
    "Could our universe be inside a black hole? This is Duho's personal interest, outside the lab's "
    "research programme. We read primary sources for their predictions. One branch "
    "gives neutron stars a number to check. For galaxy spin, the sources give no expected size for the "
    "effect, and a measurement could not identify a black-hole origin. So this route closes. The idea "
    "is not declared true or false."
)
cards["01"]["diagram"] = (
    "Three-column verdict map. Left: PERSONAL INTEREST badge above a plain nested-horizon icon, "
    "immediately paired with NOT PART OF THE LAB'S RESEARCH PROGRAMME. Centre: PRIMARY SOURCES flow "
    "into two branches. Right branch A: NEUTRON STARS -> NUMBER TO CHECK. Right branch B: GALAXY SPIN "
    "-> NO CALIBRATED TARGET (THE SOURCES GIVE NO EXPECTED SIZE FOR THE EFFECT) + NOT IDENTIFYING BY ITSELF -> ROUTE "
    "CLOSED. Animate both branches early enough that stakes, work, and verdict all land by 35 seconds."
)
cards["01"]["on_screen_support"] = [
    "DUHO'S PERSONAL INTEREST · NOT PART OF THE LAB'S RESEARCH PROGRAMME",
    "WE READ THE PRIMARY SOURCES",
    "NEUTRON STARS: A NUMBER TO CHECK",
    "GALAXY SPIN: THE SOURCES GIVE NO EXPECTED SIZE FOR THE EFFECT · NOT IDENTIFYING BY ITSELF",
    "ROUTE CLOSED · IDEA NOT DECLARED TRUE OR FALSE",
]

# Lana S2: earn the initialism before cards 09–11 speak it.
cards["02"]["narration"] = (
    "The first surprise is structural. Lana found at least five different proposals under this "
    "label—black-hole universe, or BHU for short. One identifies a closed universe with a black hole. "
    "Another says collapse rebounds—a bounce—instead of crushing to a point. Another inherits "
    "rotation. Cosmological natural selection asks whether black-hole production shapes physical "
    "constants—the fixed numbers built into physics. Other baby-universe work points to different "
    "observables. They do not share one forecast."
)

# Kun blocker 1: copied verbatim. Do not paraphrase this instruction.
cards["05"]["diagram"] = (
    "Full horizontal mass axis from 1.4 to 2.2 M_sun. Draw the source's ~1.5 marker and the "
    "approximate 2 M_sun regime. Row 1: Demorest 1.97 +/- 0.04, central point below 2 and interval "
    "crossing. Row 2: Fonseca 2.08 +/- 0.07 at 68.3%, with the 68.3% interval above 2. Add a separate "
    "non-scaled text callout beside the plot: \"At 95.4% credibility, the packet states only that the "
    "result does not clear 2.00; no lower-bound value is quoted here.\" Do not draw a 95.4% endpoint, "
    "arrow, tick, bracket, or marker on the mass axis."
)
# Kun blocker 2: exact replacement sentence, synchronized in storyboard and generated narration.
cards["05"]["narration"] = (
    "Weighing a star thousands of light-years away is hard, so every measurement comes with an "
    "uncertainty range. Two pulsars reach the critical regime. Demorest's measurement is one point "
    "nine seven, plus or minus zero point zero four solar masses; its centre is below two. Fonseca's "
    "is two point zero eight, plus or minus zero point zero seven. The quoted sixty-eight point three "
    "percent interval stays above two. But at ninety-five point four percent credibility, the result "
    "does not clear two. At the quoted 68.3% level, the second measurement clears two solar masses; "
    "at the stricter 95.4% level, the packet says it does not."
)
cards["05"]["on_screen_support"] = [
    "EVERY DISTANT-STAR MASS HAS AN UNCERTAINTY RANGE",
    "DEMOREST: 1.97 ± 0.04 M☉",
    "FONSECA: 2.08 ± 0.07 M☉ · 68.3%",
    "AT 95.4% CREDIBILITY, THE PACKET STATES ONLY THAT THE RESULT DOES NOT CLEAR 2.00",
    "NO 95.4% LOWER-BOUND VALUE IS QUOTED OR PLOTTED HERE",
]

# Lana S3.
cards["07"]["narration"] = cards["07"]["narration"].replace(
    "A different programme led to our sky work.",
    "A different proposal led to our sky work.",
)

# Kun blocker 3: exact required source-defined-range formulation.
cards["10"]["narration"] = (
    "The route therefore fails in two independent ways. A finite-precision spin result cannot be "
    "scored against a source-defined pass-or-fail range, because the source gives no predicted size. "
    "And without a unique signature, a positive result cannot identify BHU. We could build a "
    "trustworthy measurement and still be unable to answer the BHU question. The hunt had a source. "
    "It did not have a target."
)
cards["10"]["diagram"] = (
    "Two-column fail-closed ledger. Column A: NO SOURCE-DEFINED PASS-OR-FAIL RANGE—show a finite-precision "
    "spin result beside a blank scoring ruler labelled NO PREDICTED SIZE; do not imply that every possible "
    "qualitative observation is irrelevant. Column B: NO UNIQUE SIGNATURE—show one observed node with split "
    "backward arrows labelled POSITIVE RESULT DOES NOT IDENTIFY BHU. Both columns feed ROUTE CLOSED FOR THIS "
    "CAMPAIGN'S SKY-STATISTICS LINE. Keep MEASUREMENT MAY STILL BE TRUSTWORTHY visibly separate. Final line: "
    "THE HUNT HAD A SOURCE · IT DID NOT HAVE A TARGET."
)
cards["10"]["on_screen_support"] = [
    "1 · NO SOURCE-DEFINED PASS-OR-FAIL RANGE",
    "2 · NO UNIQUE SIGNATURE",
    "A FINITE-PRECISION RESULT CANNOT BE NUMERICALLY SCORED AGAINST A RANGE THE SOURCE DOES NOT GIVE",
    "A POSITIVE RESULT DOES NOT IDENTIFY BHU",
    "THE HUNT HAD A SOURCE · IT DID NOT HAVE A TARGET",
]

# Recompute planned card times at the already-gated 128 WPM design pace.
def word_count(text):
    import re
    return len(re.findall(r"\b[\w’'-]+\b", text))

for card in sb["cards"]:
    speech = word_count(card["narration"]) / 128.0 * 60.0
    card["planned_seconds"] = int(max(float(card.get("planned_seconds", 5)), round(speech + 1.8)))
if sb["cards"][0]["planned_seconds"] > 35:
    raise SystemExit(f"opening misses 35-second contract: {sb['cards'][0]['planned_seconds']}")
sb["estimated_duration_seconds"] = sum(card["planned_seconds"] for card in sb["cards"])

(D / "STORYBOARD_DRAFT_V5.json").write_text(json.dumps(sb, indent=2, ensure_ascii=False) + "\n")

# Generate V5 narration from the exact storyboard strings.
lines = [
    "# BHU closure video — narration draft V5",
    "",
    "Status: frozen for exact-hash delta re-gate. No audio or render authority.",
    "",
    "This file is generated from `STORYBOARD_DRAFT_V5.json`; narration must match 11/11 before gate.",
    "",
    "Sole source: Lana Revision 5, SHA-256 `b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516`.",
    "",
]
for card in sb["cards"]:
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
(D / "NARRATION_DRAFT_V5.md").write_text("\n".join(lines))

# V5 ledger: make the operational boundary explicit enough to prevent Card 10 drift.
ledger = (D / "CLAIM_LINE_LEDGER_V3.md").read_text()
ledger = ledger.replace("claim-to-line ledger V3", "claim-to-line ledger V5", 1)
old_c01 = (
    "| C01 | BHU is Duho's standing personal interest and not a corpus/NebulaMind frontier. | 3–8 | Mandatory opening framing. Do not imply mainstream priority. |"
)
new_c01 = (
    "| C01 | BHU is Duho's standing personal interest, not part of the lab's research programme. | 3–8 | Mandatory opening framing in plain public language. Do not imply mainstream priority. |"
)
if ledger.count(old_c01) != 1:
    raise SystemExit("C01 ledger anchor mismatch")
ledger = ledger.replace(old_c01, new_c01)
old_c11 = (
    "| C11 | For handedness, the source supplies no calibrated amplitude, scale law, redshift law, independently predicted axis, finite lower bound, or source-defined numerical acceptance region. | 157–167; 250–257; 330–342; 351–366; 386–401 | This is an operational, as-published closure; never \"untestable in principle.\" |"
)
new_c11 = (
    "| C11 | For handedness, a finite-precision spin result cannot be numerically scored against a source-defined pass-or-fail range because the source gives no predicted size; the source also gives no calibrated scale/redshift law, independently predicted axis, or finite lower bound. | 157–167; 250–257; 330–342; 351–366; 386–401 | This is an operational, as-published closure. Qualitative directional claims remain, so never imply that no possible observation could bear on them or that BHU is untestable in principle. |"
)
if ledger.count(old_c11) != 1:
    raise SystemExit("C11 ledger anchor mismatch")
ledger = ledger.replace(old_c11, new_c11)
(D / "CLAIM_LINE_LEDGER_V5.md").write_text(ledger)

print("wrote STORYBOARD_DRAFT_V5.json, NARRATION_DRAFT_V5.md, CLAIM_LINE_LEDGER_V5.md")
