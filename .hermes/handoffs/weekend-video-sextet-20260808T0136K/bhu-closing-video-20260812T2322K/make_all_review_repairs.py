#!/usr/bin/env python3
"""Apply Goru, Lana, and Kun repairs to a new synchronized BHU draft set.

Inputs are preserved. STORYBOARD_DRAFT_V2.json already contains Goru's sole-packet
repair. This script creates STORYBOARD_DRAFT_V3.json, generates
NARRATION_DRAFT_V4.md from the storyboard narration, and tightens the claim ledger.
"""
from pathlib import Path
import json

D = Path(__file__).resolve().parent
sb = json.loads((D / "STORYBOARD_DRAFT_V2.json").read_text())
sb["title"] = "Inside a black hole? What the sources predict—and why this route closed"
sb["status"] = "ALL_REVIEW_REPAIRS_APPLIED_NOT_CREW_CLEARED"
sb["render_contract"]["target_narration_wpm"] = "120-135; design at 128, then gate the encoded audio"
sb["render_contract"]["caption_plan"] = (
    "Generate timed sentence captions from the final narration; retain assertion headings and "
    "diagram labels so the argument remains legible when muted."
)

updates = {
    "01": {
        "heading": "This route closed because it had no calibrated, identifying target",
        "narration": (
            "Could our universe be inside a black hole? This is Duho's standing personal interest, not a "
            "NebulaMind research frontier. We read primary sources to ask what these ideas predict. Here "
            "is the verdict. One branch gives collapsed stars a number to check. Our galaxy-spin route "
            "has no predicted effect size, and the observation would not identify a black-hole origin. "
            "So this route closes. The idea is not declared true or false."
        ),
        "diagram": (
            "Three-column verdict map. Left: PERSONAL INTEREST badge above a plain nested-horizon icon, "
            "immediately paired with NOT A NEBULAMIND RESEARCH FRONTIER. Centre: PRIMARY SOURCES flow into "
            "two branches. Right branch A: COLLAPSED STARS -> NUMBER TO CHECK. Right branch B: GALAXY SPIN "
            "-> NO PREDICTED EFFECT SIZE + NOT IDENTIFYING BY ITSELF -> ROUTE CLOSED. Animate both branches "
            "early enough that stakes, work, and verdict all land by 35 seconds."
        ),
        "on_screen_support": [
            "DUHO'S PERSONAL INTEREST · NOT A NEBULAMIND RESEARCH FRONTIER",
            "WE READ THE PRIMARY SOURCES",
            "COLLAPSED STARS: A NUMBER TO CHECK",
            "GALAXY SPIN: NO PREDICTED EFFECT SIZE · NOT IDENTIFYING BY ITSELF",
            "ROUTE CLOSED · IDEA NOT DECLARED TRUE OR FALSE",
        ],
    },
    "02": {
        "heading": "“Black-hole universe” names different proposals, not one model",
        "narration": (
            "The first surprise is structural. Lana found at least five different proposals under this "
            "label. One identifies a closed universe with a black hole. Another says collapse rebounds—a "
            "bounce—instead of crushing to a point. Another inherits rotation. Cosmological natural "
            "selection asks whether black-hole production shapes physical constants—the fixed numbers "
            "built into physics. Other baby-universe work points to different observables. They do not "
            "share one forecast."
        ),
        "on_screen_support": ["ONE LABEL", "AT LEAST FIVE PROPOSALS IN THIS SURVEY", "NO SINGLE SHARED FORECAST"],
    },
    "03": {
        "heading": "A test needs a target that can be wrong—and identify the idea",
        "narration": (
            "To test an idea, the model has to risk being wrong. It needs a number, a range, or a "
            "distinctive pattern that a measurement can miss. And the result must point back to the idea, "
            "rather than leave several possible causes. Lana found one clean numerical test in the family "
            "she surveyed. It uses neutron stars—the ultra-dense collapsed cores of exploded stars. The "
            "ones we can time as they spin are called pulsars, and their mass can be measured."
        ),
        "diagram": (
            "Build the central logic that will recur later: MODEL -> TARGET BAND -> MEASUREMENT. First let "
            "the measurement miss the band to show CAN BE WRONG. Then let one observation point back toward "
            "several possible causes to show NOT IDENTIFYING. Finish with the two requirements: A TARGET "
            "THAT CAN BE MISSED and A RESULT THAT IDENTIFIES THE IDEA."
        ),
        "on_screen_support": [
            "MODEL", "TARGET", "MEASUREMENT", "1 · CAN BE WRONG", "2 · CAN IDENTIFY THE IDEA",
            "NEUTRON STARS: ULTRA-DENSE COLLAPSED CORES", "SPINNING, TIMED NEUTRON STARS ARE PULSARS",
        ],
    },
    "04": {
        "heading": "One CNS chain puts a low ceiling on neutron-star mass",
        "narration": (
            "In cosmological natural selection, universes reproduce through black holes with slightly "
            "changed constants. Those constants should sit near values that favour black-hole production. "
            "In the Brown–Lee–Rho chain Lana surveyed, the Brown–Bethe maximum neutron-star mass is about "
            "one and a half times the mass of our Sun—one point five solar masses. Their paper says a "
            "neutron star at approximately two solar masses or above would put that chain in ‘serious doubt "
            "or simply falsify’ it. That is a real, falsifiable number."
        ),
    },
    "05": {
        "narration": (
            "Weighing a star thousands of light-years away is hard, so every measurement comes with an "
            "uncertainty range. Two pulsars reach the critical regime. Demorest's measurement is one point "
            "nine seven, plus or minus zero point zero four solar masses; its centre is below two. "
            "Fonseca's is two point zero eight, plus or minus zero point zero seven. The quoted sixty-eight "
            "point three percent interval stays above two. But at ninety-five point four percent "
            "credibility, the result does not clear two. At the everyday confidence level, the second "
            "measurement clears two Suns; demand near-certainty, and it does not quite."
        ),
        "diagram": (
            "Full, uncropped horizontal interval plot from 1.4 to 2.2 M☉. Draw the source's ~1.5 marker and "
            "the approximate 2 regime. Row 1: Demorest 1.97 ±0.04, central point below 2 and interval "
            "crossing. Row 2: Fonseca 2.08 ±0.07 at 68.3%, entirely above 2. Add a distinct 95.4% marker "
            "showing only the packet-permitted statement that the result does not clear 2.00; do not plot or "
            "print an unstated lower-bound value. Label credibility levels directly; do not hide them in a legend."
        ),
        "on_screen_support": [
            "EVERY DISTANT-STAR MASS HAS AN UNCERTAINTY RANGE",
            "DEMOREST: 1.97 ± 0.04 M☉",
            "FONSECA: 2.08 ± 0.07 M☉ · 68.3%",
            "AT 95.4% CREDIBILITY, THE RESULT DOES NOT CLEAR 2.00 M☉",
        ],
    },
    "06": {
        "narration": (
            "This is where restraint matters. Brown, Lee, and Rho gave two possible readings, joined by an "
            "‘or’: a heavy neutron star would put the chain in serious doubt, or simply falsify it. Lana's "
            "closing record does not decide which side applies, and neither will this video. The finding is "
            "narrower: observations have entered the regime named by the source."
        ),
    },
    "08": {
        "heading": "The handedness claim came after the cited data and never became a numerical forecast",
        "narration": (
            "But that sentence was added in 2025, after the galaxy studies cited as support. It was not a "
            "prediction made before the data—this one came after. The paper gives equations for spinning "
            "systems, but not a numerical forecast for galaxy handedness: no expected size, no rule for how "
            "it changes with scale or redshift, no independently predicted direction, and no range that "
            "would count as a hit or a miss."
        ),
        "on_screen_support": [
            "OBSERVATIONS CITED FIRST", "HANDEDNESS CLAIM ADDED IN 2025",
            "NOT A PREDICTION MADE BEFORE THE DATA", "EQUATIONS PRESENT",
            "NO EXPECTED SIZE OR PASS-OR-FAIL RANGE FOR HANDEDNESS",
        ],
    },
    "09": {
        "narration": (
            "Suppose a controlled survey found a real spin-handedness difference. That would be "
            "interesting. But that broad observation would not identify BHU by itself. One observed number "
            "would have more than one possible interpretation unless a BHU model supplied a unique "
            "signature. A successful measurement is not automatically a successful test of this model."
        ),
        "diagram": (
            "The centerpiece identifying-test diagram. One observed node, CW/CCW DIFFERENCE, points backward "
            "toward BHU? and OTHER POSSIBLE CAUSES. The backward arrow splits, so the observation cannot "
            "select one cause. Do not name or depict specific rival cosmologies. End on the explicit logic "
            "MEASUREMENT ≠ IDENTIFICATION."
        ),
        "on_screen_support": [
            "OBSERVED CW/CCW DIFFERENCE", "BHU?", "OTHER POSSIBLE CAUSES",
            "NOT BHU-SPECIFIC BY ITSELF", "MEASUREMENT ≠ IDENTIFICATION",
        ],
    },
    "10": {
        "narration": (
            "The route therefore fails in two independent ways. Find a small effect, and the idea neither "
            "wins nor loses. Find nothing, and it still does not lose: with no predicted size, no outcome "
            "settles it. And without a unique signature, a positive result cannot identify BHU. We could "
            "build a trustworthy measurement and still be unable to answer the BHU question. The hunt had "
            "a source. It did not have a target."
        ),
        "on_screen_support": [
            "1 · NO PREDICTED EFFECT SIZE", "2 · NO UNIQUE SIGNATURE",
            "A TRUSTWORTHY NUMBER CAN STILL FAIL TO TEST BHU", "THE HUNT HAD A SOURCE · IT DID NOT HAVE A TARGET",
        ],
    },
    "11": {
        "narration": (
            "What would change the verdict? First, a published calculation connecting parent-black-hole "
            "parameters to a handedness amplitude, scale, or redshift dependence, with a pass-or-fail "
            "range. Or second, a fingerprint only a black-hole birth would leave—not merely the broad fact "
            "of spin asymmetry. A confirmed spin asymmetry alone would still not test BHU. This route "
            "reopens only when a BHU model supplies a calibrated target or a unique signature."
        ),
        "diagram": (
            "Return to the model-target-measurement diagram from card 03, now with two locked reopen gates: "
            "CALIBRATED TARGET and UNIQUE SIGNATURE. A standalone CONFIRMED SPIN ASYMMETRY token approaches "
            "but cannot unlock either gate. Finish with both requirements and the heading held alone long "
            "enough to read; no caveat or credit card follows."
        ),
    },
}

for card in sb["cards"]:
    u = updates.get(card["id"], {})
    card.update(u)

# Design timing for 128 spoken words/min plus a modest card-tail/readability floor.
# Opening remains capped at 35 seconds by structure; its text is deliberately short.
def word_count(text):
    import re
    return len(re.findall(r"\b[\w’'-]+\b", text))

for card in sb["cards"]:
    speech = word_count(card["narration"]) / 128.0 * 60.0
    planned = max(float(card.get("planned_seconds", 5)), round(speech + 1.8))
    card["planned_seconds"] = int(planned)
if sb["cards"][0]["planned_seconds"] > 35:
    raise SystemExit(f"opening misses 35-second contract: {sb['cards'][0]['planned_seconds']}")
sb["estimated_duration_seconds"] = sum(c["planned_seconds"] for c in sb["cards"])

(D / "STORYBOARD_DRAFT_V3.json").write_text(json.dumps(sb, indent=2, ensure_ascii=False) + "\n")

# Generate narration from the exact storyboard strings to prohibit silent divergence.
lines = [
    "# BHU closure video — narration draft V4, synchronized crew-repair revision",
    "",
    "Status: candidate for exact-hash crew re-review. No narration or render authority.",
    "",
    "This file is generated from `STORYBOARD_DRAFT_V3.json`; narration must match 11/11 before gate.",
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
    "## Paid-generation notes", "",
    "None. The explanatory burden is logical and diagrammatic. Deterministic local diagrams are more exact than generated footage for every planned shot. No paid-generation placeholder is justified.", "",
]
(D / "NARRATION_DRAFT_V4.md").write_text("\n".join(lines))

ledger = (D / "CLAIM_LINE_LEDGER_V2.md").read_text()
ledger = ledger.replace("claim-to-line ledger V2", "claim-to-line ledger V3", 1)
old = (
    "| C12 | A positive spin asymmetry would not identify BHU because other rotating cosmologies can produce the same generic observables. | 159–167; 319–328; 351–366; 386–401 | Alternative-model citations are `[VERIFY]` for an external class-level freeze. The safe packet-level statement is \"a positive generic anisotropy would not identify BHU.\" Do not name unsupported rivals in narration. |"
)
new = (
    "| C12 | A broad spin-handedness observation would not identify BHU by itself; it would have more than one possible interpretation unless a BHU model supplied a unique signature. | 159–167; 319–328; 351–366; 386–401 | Public wording must remain epistemic and operational. Do not assert that a named or unnamed rival class produces the same effect; alternative-model citations remain `[VERIFY]` for an external class-level freeze. |"
)
if ledger.count(old) != 1:
    raise SystemExit("C12 ledger anchor mismatch")
ledger = ledger.replace(old, new)
old2 = (
    "| C15 | Reopening the line requires a published magnitude/scale/redshift derivation or a signature unique to birth behind a parent horizon. | 403–418 | These are the ending requirements. A collaboration-grade spin confirmation alone would still not test BHU. |"
)
new2 = (
    "| C15 | Reopening the line requires a published magnitude/scale/redshift derivation with a pass-or-fail range, or a fingerprint only black-hole birth would leave. | 403–418 | These are the ending requirements. A confirmed spin asymmetry alone would still not test BHU; do not freeze an uncited public comparison to rival model classes. |"
)
if ledger.count(old2) != 1:
    raise SystemExit("C15 ledger anchor mismatch")
ledger = ledger.replace(old2, new2)
(D / "CLAIM_LINE_LEDGER_V3.md").write_text(ledger)

print("wrote STORYBOARD_DRAFT_V3.json, NARRATION_DRAFT_V4.md, CLAIM_LINE_LEDGER_V3.md")
