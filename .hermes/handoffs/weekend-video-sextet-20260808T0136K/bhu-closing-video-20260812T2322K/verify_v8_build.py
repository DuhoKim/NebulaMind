#!/usr/bin/env python3
"""Deterministic semantic and custody verification for BHU V8.

This verifier does not render. It proves the V8 build matches the full Lana spec,
constructs the complete audience projection, and exercises a fail-closed review
boundary before audio or frames exist.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

D = Path(__file__).resolve().parent
FILES = {
    "story": D / "STORYBOARD_DRAFT_V8.json",
    "narration": D / "NARRATION_DRAFT_V8.md",
    "ledger": D / "CLAIM_LINE_LEDGER_V8.md",
    "graphics": D / "DETERMINISTIC_DIAGRAM_SPEC_V8.md",
    "matrix": D / "V8_BUILD_MATRIX.json",
    "v7_story": D / "STORYBOARD_DRAFT_V7.json",
    "v7_narration": D / "NARRATION_DRAFT_V7.md",
    "v7_ledger": D / "CLAIM_LINE_LEDGER_V7.md",
    "spec": D / "LANA_SIMPLIFY_AND_DENAME_SPEC.md",
}
PINNED_INPUTS = {
    "v7_story": "3077f0636385487bb4092d2032c18bbedaedb647780bbfc581e59027c87a8d2b",
    "v7_narration": "3380497f0514e906db8463d0fdd2ffd1f0b02b37ac6825e3bfdec86011c2edc0",
    "v7_ledger": "871a808c4f2af94e24ef68b19cef416b7f7e3295720dab25ef8676753c845b5a",
    "spec": "53e2c694334cdb9913e8d14e91032dbfb552e5c2eee5d1aea75360403f4b3274",
}
PACKET = D.parent / "reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md"
PACKET_SHA = "b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit("HOLD: " + message)


for key, expected in PINNED_INPUTS.items():
    require(FILES[key].exists(), f"missing pinned input {FILES[key].name}")
    require(sha(FILES[key]) == expected, f"pinned input drift {FILES[key].name}")
require(PACKET.exists() and sha(PACKET) == PACKET_SHA, "sole authority packet drift")
for key in ("story", "narration", "ledger", "graphics", "matrix"):
    require(FILES[key].exists(), f"missing V8 artifact {FILES[key].name}")

story = json.loads(FILES["story"].read_text())
v7 = json.loads(FILES["v7_story"].read_text())
matrix = json.loads(FILES["matrix"].read_text())
require(len(story.get("cards", [])) == 11, "V8 does not contain 11 cards")
require([c["id"] for c in story["cards"]] == [f"{i:02d}" for i in range(1, 12)], "card ID/order drift")
require(all(c.get("heading") for c in story["cards"]), "assertion heading missing")
require(not any(c.get("kind") == "divider" for c in story["cards"]), "divider card present")
require(not story.get("paid_generation_notes"), "paid-generation note/request present")
require(story["cards"][0]["planned_seconds"] <= 35, "opening planned duration exceeds 35 seconds")
require(matrix.get("copy_replacement_count") == 27 and len(matrix.get("copy_replacements", [])) == 27, "copy replacement count != 27")
require(matrix.get("graphics_count") == 8 and len(matrix.get("graphics", [])) == 8, "graphics count != 8")
require({g["id"] for g in matrix["graphics"]} == {f"G{i}" for i in range(1, 9)}, "graphic IDs are not exactly G1..G8")
require({g["card"] for g in matrix["graphics"]} == {"01", "02", "03", "04", "05", "08", "09", "10"}, "eight-graphic card coverage drift")

# Canonical narration equality, including headings and stale filing labels.
text = FILES["narration"].read_text()
require(text.startswith("# BHU closure video — narration draft V8\n"), "stale narration H1")
require("generated from `STORYBOARD_DRAFT_V8.json`" in text, "stale generated-from filing line")
parts = re.split(r"## Card (\d+) — assertion heading\n", text)[1:]
seen: dict[str, tuple[str, str]] = {}
for i in range(0, len(parts), 2):
    cid, block = parts[i], parts[i + 1]
    heading = block.split("**", 2)[1]
    narration = block.split("**", 2)[2].split("\n\nSource:", 1)[0].strip()
    seen[cid] = (heading, narration)
for card in story["cards"]:
    require(seen.get(card["id"]) == (card["heading"], card["narration"]), f"narration/storyboard divergence card {card['id']}")
require(FILES["ledger"].read_text().startswith("# BHU closure video — claim-to-line ledger V8\n"), "stale ledger H1")
require(FILES["ledger"].read_text().splitlines()[1:] == FILES["v7_ledger"].read_text().splitlines()[1:], "claim ledger changed beyond H1")

# Claim IDs and packet-line mappings are byte-for-byte semantic carry-forwards.
for old, new in zip(v7["cards"], story["cards"]):
    require(old["heading"] == new["heading"], f"unapproved assertion-heading change card {old['id']}")
    require(old["source_claims"] == new["source_claims"], f"claim IDs changed card {old['id']}")
    require(old["packet_lines"] == new["packet_lines"], f"packet lines changed card {old['id']}")
require(story["cards"][2]["diagram"] == v7["cards"][2]["diagram"], "Card 03 existing graphic changed")
require(story["cards"][8]["diagram"] == v7["cards"][8]["diagram"], "Card 09 existing graphic changed")
expected_card10 = v7["cards"][9]["diagram"].replace(
    "Two-column fail-closed ledger.", "G7 sound-off two-column fail-closed comparison."
)
require(story["cards"][9]["diagram"] == expected_card10, "Card 10 changed beyond internal-vocabulary retirement")

# Complete audience projection. scientific_authority and Source: scaffolding are
# deliberately excluded by Lana's explicit internal-scaffolding rule.
audience: list[tuple[str, str]] = [("title", story.get("title", "")), ("slug", story.get("slug", ""))]
for key, value in story.get("render_contract", {}).items():
    if isinstance(value, str):
        audience.append((f"render_contract.{key}", value))
for key, value in story.get("visual_language", {}).items():
    if isinstance(value, str):
        audience.append((f"visual_language.{key}", value))
for card in story["cards"]:
    for key in ("heading", "narration", "diagram"):
        audience.append((f"cards[{card['id']}].{key}", card[key]))
    for i, value in enumerate(card["on_screen_support"]):
        audience.append((f"cards[{card['id']}].on_screen_support[{i}]", value))
projection = "\n".join(value for _, value in audience)

forbidden_names = re.compile(r"(?i)(?<![A-Za-z0-9])(?:duho|lana|goru|kun|tori|yui|hwao)(?![A-Za-z0-9])")
name_hits = [(path, m.group(0)) for path, value in audience for m in forbidden_names.finditer(value)]
require(not name_hits, f"viewer-facing local names remain: {name_hits}")
for term in ("packet", "ledger", "receipt", "lane", "seat", "freeze"):
    hits = [path for path, value in audience if re.search(rf"(?i)\b{term}\b", value)]
    require(not hits, f"viewer-facing crew vocabulary {term}: {hits}")
for path, value in audience:
    require(not re.search(r"(?i)(?:\.md\b|\.json\b|sha-?256|\b[0-9a-f]{64}\b)", value), f"viewer-facing filename/hash in {path}")
for forbidden in (
    "near-certainty", "no outcome settles it", "untestable in principle", "definitively falsified",
    "bhu is supported", "bhu is true", "bhu is false", "1.95", "one point nine five",
    "other rotating cosmologies", "other theories of a rotating universe", "generic effect of rotation",
):
    require(forbidden not in projection.lower(), f"forbidden public phrase: {forbidden}")

# Raw-artifact sweep with underscore-safe name boundaries. Internal authority
# custody, unchanged claim-ledger rows, old-text audit anchors, and B-10's named
# sign-off record are allowed by the spec; every other raw occurrence is a HOLD.
def string_leaves(value, path=""):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from string_leaves(child, f"{path}.{key}" if path else key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from string_leaves(child, f"{path}[{index}]")
    elif isinstance(value, str):
        yield path, value

story_raw_hits = [
    (path, match.group(0))
    for path, value in string_leaves(story)
    for match in forbidden_names.finditer(value)
]
require(story_raw_hits == [("scientific_authority.path", "LANA")], f"unexpected raw storyboard name hits: {story_raw_hits}")

narration_raw_hits = []
for number, line in enumerate(text.splitlines(), 1):
    for match in forbidden_names.finditer(line):
        narration_raw_hits.append((number, match.group(0), line))
require(
    len(narration_raw_hits) == 1
    and narration_raw_hits[0][1].lower() == "lana"
    and narration_raw_hits[0][2].startswith("Sole source: Lana Revision 5,"),
    f"unexpected raw narration name hits: {narration_raw_hits}",
)

ledger_raw_hits = []
for number, line in enumerate(FILES["ledger"].read_text().splitlines(), 1):
    for match in forbidden_names.finditer(line):
        ledger_raw_hits.append((number, match.group(0), line))
require(
    bool(ledger_raw_hits)
    and all(
        name.lower() in {"duho", "lana"}
        and (
            line.startswith("| C0")
            or line.startswith("Sole authority: `reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md`,")
        )
        for _, name, line in ledger_raw_hits
    ),
    f"unexpected raw ledger name hits: {ledger_raw_hits}",
)

graphics_raw_hits = forbidden_names.findall(FILES["graphics"].read_text())
require(not graphics_raw_hits, f"raw graphics spec contains local names: {graphics_raw_hits}")

matrix_raw_hits = [
    (path, match.group(0))
    for path, value in string_leaves(matrix)
    for match in forbidden_names.finditer(value)
]
allowed_matrix_paths = re.compile(
    r"^(?:spec\.path|copy_replacements\[\d+\]\.old|copy_replacements\[25\]\.note|b10_disposition)$"
)
require(
    bool(matrix_raw_hits) and all(allowed_matrix_paths.fullmatch(path) for path, _ in matrix_raw_hits),
    f"unexpected raw build-matrix name hits: {matrix_raw_hits}",
)

# Published scientific authors remain in the public copy.
for author in ("Brown", "Lee", "Rho", "Demorest", "Fonseca"):
    require(re.search(rf"(?i)\b{author}\b", projection) is not None, f"published author missing: {author}")

# A1: exact text plus frame-one/full-card visual boundary. Narration timing is
# reported separately because the exact required sentence completes after ten
# seconds at the target cadence; the verifier must not turn marker-start timing
# into a false completion claim.
c1 = story["cards"][0]
a1 = "It's a question we were personally curious about — a side-interest, not part of the lab's research programme."
badge = "A PERSONAL SIDE-QUESTION · NOT PART OF THE LAB'S RESEARCH PROGRAMME"
require(a1 in c1["narration"], "A1 narration not exact")
require(c1["on_screen_support"][0] == badge, "A1 badge not exact")
require(badge in c1["diagram"], "A1 diagram badge not exact")
require("visible from frame one for the full card" in c1["diagram"], "A1 canonical diagram hold missing")
graphics_text = FILES["graphics"].read_text()
require("Card 01 frame one and held for the full card" in graphics_text, "A1 frame-one/full-card execution invariant missing")
words = re.findall(r"\b[\w’'-]+\b", c1["narration"])
side_index = next(i for i, word in enumerate(words, 1) if word.lower() == "side-interest")
not_index = next(i for i, word in enumerate(words, 1) if word.lower() == "not")
programme_index = next(i for i, word in enumerate(words, 1) if word.lower() == "programme")
require(side_index / 120 * 60 <= 10 and not_index / 120 * 60 <= 10, "A1 marker starts miss first ten seconds at 120 WPM")

# A2: document introduced before later attribution; only allowed attribution forms.
c2 = story["cards"][1]["narration"]
intro = "We wrote what we found into a closing record — the document this video reports from."
require(intro in c2, "A2 artifact introduction missing from Card 02")
for card in story["cards"][2:]:
    if "closing record" in card["narration"].lower():
        require(card["id"] in {"03", "05", "06"}, f"unexpected closing-record attribution card {card['id']}")
require("the closing record found" in story["cards"][2]["narration"].lower(), "Card 03 attribution form drift")
require("the closing record says" in story["cards"][4]["narration"].lower(), "Card 05 attribution form drift")
require("the closing record does not decide" in story["cards"][5]["narration"].lower(), "Card 06 attribution form drift")
require("In the Brown–Lee–Rho chain our record surveyed," in story["cards"][3]["narration"], "Card 04 exact A2 replacement drift")

# Card 05 wording and visual negative constraints.
c5 = story["cards"][4]
for phrase in (
    "one point nine seven", "point zero four", "two point zero eight", "point zero seven",
    "sixty-eight point three percent", "ninety-five point four percent",
):
    require(c5["narration"].lower().count(phrase) == 1, f"Card 05 spoken value count drift: {phrase}")
require(c5["on_screen_support"][1] == "DEMOREST: 1.97 ± 0.04 M☉", "Demorest print string drift")
require(c5["on_screen_support"][2] == "FONSECA: 2.08 ± 0.07 M☉ · 68.3%", "Fonseca print string drift")
require("continuous open-ended gradient" in c5["diagram"] and "fades through the 2.00 line" in c5["diagram"], "G3 fade mechanism missing")
require("non-scaled mode label outside the mass plot" in c5["diagram"], "G3 95.4% label is not explicitly outside the axis plot")
for primitive in ("endpoint", "arrow", "tick", "bracket", "marker", "whisker", "shaded boundary", "axis-aligned glyph", "position-bearing terminus"):
    require(primitive in c5["diagram"].lower(), f"G3 hard prohibition omits {primitive}")
require("no visible edge" in c5["diagram"].lower(), "G3 gradient-edge prohibition missing")

# G5 exact plain labels and B-10 review disposition.
c8d = story["cards"][7]["diagram"]
for label in ("SIZE?", "WHERE/WHEN?", "DIRECTION?", "PASS-OR-FAIL RANGE?"):
    require(label in c8d, f"G5 label missing: {label}")
require("There's no pass-or-fail range to grade a measurement against — the idea never says how big the effect should be." in story["cards"][9]["narration"], "B-10 proposed line drift")
require(matrix.get("b10_disposition") == "included exactly as proposed; requires Kun sign-off; no render authority", "B-10 disposition missing")

# No media should exist for V8 before the full exact-hash gate.
for pattern in ("*V8*.wav", "*V8*.mp3", "*V8*.mp4", "*V8*.mov", "*V8*.png", "*V8*.jpg", "*v8*.wav", "*v8*.mp4"):
    require(not list(D.glob(pattern)), f"premature V8 media exists for {pattern}")

result = {
    "status": "PASS_BUILD_SEMANTICS_AWAITING_FULL_THREE_SEAT_GATE",
    "pinned_inputs": {FILES[key].name: PINNED_INPUTS[key] for key in PINNED_INPUTS},
    "outputs": {FILES[key].name: sha(FILES[key]) for key in ("narration", "story", "ledger", "graphics", "matrix")},
    "copy_replacements": 27,
    "graphics": 8,
    "audience_projection_strings": len(audience),
    "viewer_local_name_hits": 0,
    "viewer_internal_vocabulary_hits": 0,
    "raw_local_name_occurrences": {
        "storyboard_internal_authority_path": len(story_raw_hits),
        "narration_internal_source_scaffolding": len(narration_raw_hits),
        "claim_ledger_internal_rows": len(ledger_raw_hits),
        "graphics_spec": len(graphics_raw_hits),
        "build_matrix_allowed_audit_scaffolding": len(matrix_raw_hits),
        "unclassified": 0,
    },
    "a1_visual_boundary": "frame one through full card",
    "a1_narration_marker_seconds_at_120_wpm": {
        "side-interest_complete": side_index / 120 * 60,
        "not-part_marker_start": not_index / 120 * 60,
        "not-part_full_phrase_complete": programme_index / 120 * 60,
    },
    "opening_timing_concern": {
        "word_count": len(words),
        "seconds_at_120_wpm": len(words) / 120 * 60,
        "seconds_at_128_wpm": len(words) / 128 * 60,
        "seconds_at_135_wpm": len(words) / 135 * 60,
        "planned_seconds": c1["planned_seconds"],
        "boundary_phrase_completion_seconds_at_120_wpm": programme_index / 120 * 60,
        "disposition": "SURFACE_TO_FULL_GATE; exact frame-one badge satisfies the visual deadline, but narration and 35-second opening timing require explicit review; do not delete exact spec wording or speed beyond the target contract without review",
    },
    "a2_introduced_card": "02",
    "claim_ids_and_packet_lines": "unchanged",
    "render_authority": False,
}
(D / "V8_BUILD_VERIFICATION.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(result, indent=2, ensure_ascii=False))
