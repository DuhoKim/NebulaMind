#!/usr/bin/env python3
"""Build BHU V10 from exact V9 bytes with two authorized Card-04 repairs.

Authored deltas:
- Card 04 heading: expand CNS in the assertion heading.
- Card 04 planned_seconds: 41 -> 48.

The aggregate estimated duration is recomputed from card durations (392 -> 399).
The standalone narration receives only the heading replacement; spoken narration,
claims, graphics, and all other card fields remain unchanged. No media is made.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

D = Path(__file__).resolve().parent
INPUTS = {
    "STORYBOARD_DRAFT_V9.json": "c9824b95453be7e67d6066f3810648dc8d588a8c3210546ec9caa5ee74710d7a",
    "NARRATION_DRAFT_V9.md": "85f111d366c5d11d912e4f7db5586f10b491b12b1c5091d3f94d822c388190b3",
    "CLAIM_LINE_LEDGER_V9.md": "aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa",
    "DETERMINISTIC_DIAGRAM_SPEC_V9.md": "e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e",
    "V9_SHORTHAND_AUDIT.json": "2cd55bd9698ec11ccf002b3e1810ab51408bfdbe18f4bca3fa51314e46931624",
    "V9_FREEZE_RECEIPT.json": "3df2d6638aa13cd0db58b3926fb523a90506be28f3749f37b3897b2840150bcc",
    "LANA_CONFIRM_V9.md": "f553e690201c3eaccfeee5b8b12c34e9defe6924166fa7397ed0a3fb95a35b3c",
    "GORU_CONFIRM_V9.md": "d4ae02987ab1269d3c777b47031f56e81cbe5b1f9b106e808d11b970191c49bd",
    "KUN_CONFIRM_V9.md": "0ed5627ebef10460755151719a1313a3304dc0705d48c3fff8e20e7078f361f9",
}
OUTPUTS = {
    "story": D / "STORYBOARD_DRAFT_V10.json",
    "narration": D / "NARRATION_DRAFT_V10.md",
    "ledger": D / "CLAIM_LINE_LEDGER_V10.md",
    "graphics": D / "DETERMINISTIC_DIAGRAM_SPEC_V10.md",
    "delta": D / "V10_DELTA_RECEIPT.json",
}
OLD_HEADING = "One CNS chain puts a low ceiling on neutron-star mass"
NEW_HEADING = "One cosmological-natural-selection chain puts a low ceiling on neutron-star mass"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for name, expected in INPUTS.items():
    path = D / name
    if not path.exists() or sha(path) != expected:
        actual = sha(path) if path.exists() else "MISSING"
        raise SystemExit(f"pinned V9 input drift {name}: {actual}")

story_path = D / "STORYBOARD_DRAFT_V9.json"
narration_path = D / "NARRATION_DRAFT_V9.md"
ledger_path = D / "CLAIM_LINE_LEDGER_V9.md"
graphics_path = D / "DETERMINISTIC_DIAGRAM_SPEC_V9.md"

story = json.loads(story_path.read_text())
card04 = next(card for card in story["cards"] if card["id"] == "04")
if card04["heading"] != OLD_HEADING:
    raise SystemExit("Card 04 exact V9 heading anchor drift")
if card04["planned_seconds"] != 41:
    raise SystemExit("Card 04 exact V9 planned_seconds anchor drift")
if story["estimated_duration_seconds"] != 392:
    raise SystemExit("V9 aggregate duration anchor drift")
card04["heading"] = NEW_HEADING
card04["planned_seconds"] = 48
story["estimated_duration_seconds"] = sum(card["planned_seconds"] for card in story["cards"])
if story["estimated_duration_seconds"] != 399:
    raise SystemExit("V10 aggregate duration is not 399 seconds")
OUTPUTS["story"].write_text(json.dumps(story, indent=2, ensure_ascii=False) + "\n")

narration = narration_path.read_text()
if narration.count(OLD_HEADING) != 1:
    raise SystemExit("standalone narration exact V9 heading anchor count is not one")
OUTPUTS["narration"].write_text(narration.replace(OLD_HEADING, NEW_HEADING))

# Claims and graphic instructions are unchanged, so preserve exact reviewed bytes.
OUTPUTS["ledger"].write_bytes(ledger_path.read_bytes())
OUTPUTS["graphics"].write_bytes(graphics_path.read_bytes())

delta = {
    "status": "V10_TWO_REPAIRS_BUILT_AWAITING_TIGHT_THREE_SEAT_EXACT_HASH_CONFIRMATION_NO_RENDER",
    "render_authority": False,
    "base_review_targets": {
        name: INPUTS[name]
        for name in (
            "NARRATION_DRAFT_V9.md",
            "STORYBOARD_DRAFT_V9.json",
            "CLAIM_LINE_LEDGER_V9.md",
            "DETERMINISTIC_DIAGRAM_SPEC_V9.md",
        )
    },
    "authority_receipts": {
        "LANA_CONFIRM_V9.md": {
            "sha256": INPUTS["LANA_CONFIRM_V9.md"],
            "verdict": "PASS WITH ONE TIMING REPAIR",
            "repair": "cards[3].planned_seconds 41 -> 48",
        },
        "GORU_CONFIRM_V9.md": {
            "sha256": INPUTS["GORU_CONFIRM_V9.md"],
            "verdict": "PASS CLEAR FOR RENDER on V9",
        },
        "KUN_CONFIRM_V9.md": {
            "sha256": INPUTS["KUN_CONFIRM_V9.md"],
            "verdict": "HOLD_RENDER_ON_SHORTHAND_AUDIT",
            "repair": "cards[3].heading CNS -> cosmological-natural-selection",
        },
    },
    "authored_canonical_changes": [
        {
            "path": "cards[3].heading",
            "old": OLD_HEADING,
            "new": NEW_HEADING,
        },
        {
            "path": "cards[3].planned_seconds",
            "old": 41,
            "new": 48,
        },
    ],
    "derived_canonical_change": {
        "path": "estimated_duration_seconds",
        "old": 392,
        "new": 399,
        "rule": "sum(cards[*].planned_seconds)",
    },
    "derived_changed_channel": {
        "file": "NARRATION_DRAFT_V10.md",
        "change": "Card 04 assertion heading only",
    },
    "unchanged_byte_copies": {
        "CLAIM_LINE_LEDGER_V10.md": INPUTS["CLAIM_LINE_LEDGER_V9.md"],
        "DETERMINISTIC_DIAGRAM_SPEC_V10.md": INPUTS["DETERMINISTIC_DIAGRAM_SPEC_V9.md"],
    },
    "explicitly_unchanged": [
        "all spoken narration",
        "all Card 01-03 and Card 05-11 headings",
        "all Card 01-03 and Card 05-11 planned_seconds values",
        "all diagrams and printable labels",
        "all on-screen support",
        "all source-claim IDs and packet-line mappings",
        "all scientific numbers, dates, and published-author citations",
        "all Card 05 no-terminus constraints",
        "all V9 internal H1/status/scaffolding labels under the tight-delta order",
    ],
}
OUTPUTS["delta"].write_text(json.dumps(delta, indent=2, ensure_ascii=False) + "\n")

print(json.dumps({
    "status": delta["status"],
    "outputs": {path.name: sha(path) for path in OUTPUTS.values()},
    "authored_canonical_changes": [item["path"] for item in delta["authored_canonical_changes"]],
    "derived_canonical_change": delta["derived_canonical_change"]["path"],
}, indent=2))
