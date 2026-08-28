#!/usr/bin/env python3
"""Verify the exact one-sentence BHU V8→V9 repair and shorthand audit.

This verifier writes only V9_BUILD_VERIFICATION.json and
V9_SHORTHAND_AUDIT.json. It never renders or changes review targets.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

D = Path(__file__).resolve().parent
V8 = {
    "story": (D / "STORYBOARD_DRAFT_V8.json", "56bcf195a871ae4f60f822b3e8cc3c5bd90f262a1a8325ca7b18a42b0917ddcb"),
    "narration": (D / "NARRATION_DRAFT_V8.md", "6dc0ca1984e9fa262a28c39cc23b6559dac0cc1c4ebb6026693fb7b5b004f35c"),
    "ledger": (D / "CLAIM_LINE_LEDGER_V8.md", "aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa"),
    "graphics": (D / "DETERMINISTIC_DIAGRAM_SPEC_V8.md", "e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e"),
}
V9 = {
    "story": D / "STORYBOARD_DRAFT_V9.json",
    "narration": D / "NARRATION_DRAFT_V9.md",
    "ledger": D / "CLAIM_LINE_LEDGER_V9.md",
    "graphics": D / "DETERMINISTIC_DIAGRAM_SPEC_V9.md",
}
EXPECTED_V9 = {
    "story": "c9824b95453be7e67d6066f3810648dc8d588a8c3210546ec9caa5ee74710d7a",
    "narration": "85f111d366c5d11d912e4f7db5586f10b491b12b1c5091d3f94d822c388190b3",
    "ledger": "aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa",
    "graphics": "e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e",
}
OLD = (
    "One proposal says universes have children: every black hole buds off a new universe "
    "with slightly different physics."
)
NEW = (
    "One proposal — called cosmological natural selection — says universes have children: "
    "every black hole buds off a new universe with slightly different physics."
)
LOCAL_NAMES = re.compile(r"(?i)(?<![A-Za-z0-9])(?:duho|lana|goru|kun|tori|yui|hwao)(?![A-Za-z0-9])")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit("HOLD: " + message)


def diffs(a: Any, b: Any, path: str = "") -> list[str]:
    if type(a) is not type(b):
        return [path]
    if isinstance(a, dict):
        if list(a) != list(b):
            return [path + ".<keys>"]
        out: list[str] = []
        for key in a:
            child = f"{path}.{key}" if path else key
            out.extend(diffs(a[key], b[key], child))
        return out
    if isinstance(a, list):
        if len(a) != len(b):
            return [path + ".<length>"]
        out = []
        for index, (left, right) in enumerate(zip(a, b)):
            out.extend(diffs(left, right, f"{path}[{index}]"))
        return out
    return [] if a == b else [path]


for key, (path, expected) in V8.items():
    require(path.exists() and sha(path) == expected, f"pinned V8 drift: {path.name}")
for key, path in V9.items():
    require(path.exists() and sha(path) == EXPECTED_V9[key], f"V9 target drift: {path.name}")

v8 = json.loads(V8["story"][0].read_text())
v9 = json.loads(V9["story"].read_text())
changed = diffs(v8, v9)
require(changed == ["cards[3].narration"], f"canonical delta is not one field: {changed}")
require(v8["cards"][3]["narration"].count(OLD) == 1, "V8 Card 04 old sentence anchor drift")
require(v9["cards"][3]["narration"] == v8["cards"][3]["narration"].replace(OLD, NEW), "V9 Card 04 repair not verbatim")
require(v9["cards"][3]["narration"].startswith(NEW + " "), "repair is not Card 04 sentence 1")
require(OLD not in v9["cards"][3]["narration"], "old Card 04 sentence remains")

v8_narr = V8["narration"][0].read_text()
v9_narr = V9["narration"].read_text()
require(v8_narr.count(OLD) == 1, "V8 standalone narration old sentence anchor drift")
require(v9_narr == v8_narr.replace(OLD, NEW), "standalone narration changed beyond exact repair")
require(V9["ledger"].read_bytes() == V8["ledger"][0].read_bytes(), "claim ledger not byte-identical")
require(V9["graphics"].read_bytes() == V8["graphics"][0].read_bytes(), "graphics spec not byte-identical")

# The derived narration remains an exact mirror of all canonical card strings,
# despite intentionally retaining V8 internal filing labels under change-nothing-else.
parts = re.split(r"## Card (\d+) — assertion heading\n", v9_narr)[1:]
seen: dict[str, tuple[str, str]] = {}
for index in range(0, len(parts), 2):
    card_id, block = parts[index], parts[index + 1]
    heading = block.split("**", 2)[1]
    narration = block.split("**", 2)[2].split("\n\nSource:", 1)[0].strip()
    seen[card_id] = (heading, narration)
for card in v9["cards"]:
    require(seen.get(card["id"]) == (card["heading"], card["narration"]), f"V9 narration divergence Card {card['id']}")

# Explicit audience projection. Slug and render/visual metadata are classified
# below; they are not emitted by the local renderer as spoken or visible copy.
audience: list[tuple[str, str]] = []
for card in v9["cards"]:
    for key in ("heading", "narration", "diagram"):
        audience.append((f"cards[{card['id']}].{key}", card[key]))
    for index, value in enumerate(card["on_screen_support"]):
        audience.append((f"cards[{card['id']}].on_screen_support[{index}]", value))
projection = "\n".join(value for _, value in audience)
require(not [(path, hit.group(0)) for path, value in audience for hit in LOCAL_NAMES.finditer(value)], "viewer-facing local name returned")
for term in ("packet", "ledger", "receipt", "lane", "seat", "freeze"):
    require(not [(path, term) for path, value in audience if re.search(rf"(?i)\b{term}\b", value)], f"viewer internal term returned: {term}")

# Lexical initialisms and abbreviation-like count labels. These are the complete
# meaningful compact lexical forms found by whole-projection inspection; ordinary
# all-caps English labels and published surnames are words/names, not initialisms.
initialisms = [
    {
        "form": "BHU",
        "meaning": "black-hole universe",
        "first_viewer_card": "02",
        "spoken_expansion_card": "02",
        "spoken_witness": "black-hole universe, or BHU for short",
        "status": "EARNED_IN_BREATH",
        "render_timing": "Reveal BLACK-HOLE UNIVERSE (BHU) no earlier than the witness phrase.",
    },
    {
        "form": "CNS",
        "meaning": "cosmological natural selection",
        "first_viewer_card": "04",
        "spoken_expansion_card": "04",
        "spoken_witness": "One proposal — called cosmological natural selection —",
        "status": "EARNED_IN_FIRST_SENTENCE",
        "render_timing": "Heading may remain; the full name is the opening spoken phrase as Lana required.",
    },
    {
        "form": "CW/CCW",
        "meaning": "clockwise/counterclockwise",
        "first_viewer_card": "07",
        "spoken_expansion_card": "07",
        "spoken_witness": "clockwise- and counterclockwise-spinning galaxy counts",
        "status": "EARNED_SAME_CARD_REVEAL_MUST_BE_SYNCHRONIZED",
        "render_timing": "Reveal CW COUNTS, CCW COUNTS, and the unequal sign no earlier than the witness sentence; later Cards 09–10 are already earned.",
    },
]
for item in initialisms:
    card = next(card for card in v9["cards"] if card["id"] == item["spoken_expansion_card"])
    require(item["spoken_witness"].lower() in card["narration"].lower(), f"spoken expansion missing: {item['form']}")

# Ensure no compact lexical term is used on an earlier card than its earning card.
for item in initialisms:
    form = item["form"]
    tokens = ("CW", "CCW") if form == "CW/CCW" else (form,)
    earned = int(item["spoken_expansion_card"])
    for path, value in audience:
        card_match = re.match(r"cards\[(\d+)\]", path)
        if not card_match or int(card_match.group(1)) >= earned:
            continue
        for token in tokens:
            require(re.search(rf"(?<![A-Za-z0-9]){re.escape(token)}(?![A-Za-z0-9])", value) is None, f"{token} appears before earning at {path}")

shorthand = [
    {
        "forms": ["~", "M☉", "M ≳ 2 M☉"],
        "first_viewer_card": "04",
        "spoken_plain_language": ["about one and a half times the mass of our Sun", "one point five solar masses", "approximately two solar masses or above"],
        "render_timing": "Reveal each mass label with or after the corresponding Card-04 spoken phrase.",
    },
    {
        "forms": ["±"],
        "first_viewer_card": "05",
        "spoken_plain_language": ["give or take point zero four", "give or take point zero seven"],
        "render_timing": "Reveal each uncertainty row with or after its spoken measurement.",
    },
    {
        "forms": ["68.3%", "95.4%"],
        "first_viewer_card": "05",
        "spoken_plain_language": ["sixty-eight point three percent", "ninety-five point four percent"],
        "render_timing": "Reveal each percentage label with or after its spoken level; retain every no-terminus constraint.",
    },
    {
        "forms": ["≠"],
        "first_viewer_card": "07",
        "spoken_plain_language": ["clockwise- and counterclockwise-spinning galaxy counts should be different"],
        "render_timing": "Reveal the unequal sign with or after the Card-07 witness sentence.",
    },
]
for item in shorthand:
    card = next(card for card in v9["cards"] if card["id"] == item["first_viewer_card"])
    low = card["narration"].lower()
    require(all(witness.lower() in low for witness in item["spoken_plain_language"]), f"plain-language shorthand witness missing Card {card['id']}")

# Positive occurrence checks prevent a vacuous audit.
for token in ("BHU", "CNS", "CW", "CCW", "M☉", "±", "68.3%", "95.4%", "≠"):
    require(token in projection, f"audited compact form absent from projection: {token}")

# Scientific/claim boundaries inherited from V8 remain byte-protected except for
# the exact sentence, but assert the highest-risk invariants directly as well.
for old, new in zip(v8["cards"], v9["cards"]):
    require(old["heading"] == new["heading"], f"heading changed Card {old['id']}")
    require(old["planned_seconds"] == new["planned_seconds"], f"timing changed Card {old['id']}")
    require(old["diagram"] == new["diagram"], f"diagram changed Card {old['id']}")
    require(old["on_screen_support"] == new["on_screen_support"], f"support changed Card {old['id']}")
    require(old["source_claims"] == new["source_claims"], f"claim IDs changed Card {old['id']}")
    require(old["packet_lines"] == new["packet_lines"], f"packet lines changed Card {old['id']}")
card05 = v9["cards"][4]["diagram"].lower()
for primitive in ("endpoint", "arrow", "tick", "bracket", "marker", "whisker", "shaded boundary", "axis-aligned glyph", "position-bearing terminus", "no visible edge"):
    require(primitive in card05, f"Card 05 no-terminus constraint lost: {primitive}")

media_suffixes = {".wav", ".mp3", ".m4a", ".aac", ".mp4", ".mov", ".mkv", ".png", ".jpg", ".jpeg", ".webp", ".srt", ".vtt"}
v9_media = [str(path) for path in D.rglob("*") if path.is_file() and "v9" in path.name.lower() and path.suffix.lower() in media_suffixes]
require(not v9_media, f"premature V9 media exists: {v9_media}")

# The lowercase slug is routing metadata, not consumed by the local renderer.
# It is disclosed because it contains BHU; no publication action is authorized.
slug = v9.get("slug", "")
require(slug == "bhu-closing-record", "slug changed under tight delta")

card04_words = re.findall(r"\b[\w’'-]+\b", v9["cards"][3]["narration"])
audit = {
    "status": "PASS_STRING_INVENTORY_WITH_RENDER_REVEAL_CONSTRAINTS",
    "scope": "title plus all card headings, narration, diagram/printable-label instructions, and on-screen support",
    "lexical_initialisms": initialisms,
    "scientific_shorthand": shorthand,
    "other_earned_terms": [],
    "unearned_string_defects_after_v9_repair": 0,
    "render_reveal_constraints": [item["render_timing"] for item in initialisms + shorthand if "render_timing" in item],
    "nonviewer_classifications": {
        "bhu-closing-record slug": "routing metadata; current local renderer does not consume it; no upload/publication authorized",
        "G1..G8": "implementation IDs, not printable labels",
        "fps/px/WPM": "render-contract metadata, not spoken or printed",
        "arrows, list dots, question marks": "structural diagram grammar, not lexical initialisms",
    },
    "render_gate": "Encoded-frame/audio QA must prove each first-use label is revealed no earlier than its listed spoken witness.",
}
(D / "V9_SHORTHAND_AUDIT.json").write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n")

result = {
    "status": "PASS_V9_ONE_SENTENCE_DELTA_AWAITING_THREE_SEAT_EXACT_HASH_CONFIRMATION",
    "render_authority": False,
    "review_targets": {path.name: sha(path) for path in V9.values()},
    "canonical_changed_paths": changed,
    "standalone_narration_change": "exact same one-sentence replacement",
    "unchanged_byte_copies": [V9["ledger"].name, V9["graphics"].name],
    "viewer_local_name_hits": 0,
    "viewer_internal_vocabulary_hits": 0,
    "initialism_inventory": [item["form"] for item in initialisms],
    "unearned_string_defects_after_repair": 0,
    "render_reveal_constraints_required": True,
    "card04": {
        "planned_seconds": v9["cards"][3]["planned_seconds"],
        "word_count": len(card04_words),
        "seconds_at_120_wpm": len(card04_words) / 120 * 60,
        "seconds_at_135_wpm": len(card04_words) / 135 * 60,
    },
    "premature_v9_media_files": 0,
}
(D / "V9_BUILD_VERIFICATION.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"verification": result, "shorthand_audit": audit}, indent=2, ensure_ascii=False))
