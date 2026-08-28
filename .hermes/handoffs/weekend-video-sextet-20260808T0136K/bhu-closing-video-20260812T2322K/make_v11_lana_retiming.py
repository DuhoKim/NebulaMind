#!/usr/bin/env python3
"""Build BHU V11 from exact V10 bytes under Lana's retiming ruling.

Authored deltas only:
- Card 01 narration, verbatim in storyboard and standalone narration.
- planned_seconds on Cards 01, 02, 03, 07, and 09.

The aggregate estimated duration is recomputed from card durations (399 -> 415).
Cards 05 and 10 retain deliberate visual dwell. Claims, graphics, on-screen
support, and every other canonical field remain unchanged. No media is made.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

D = Path(__file__).resolve().parent
INPUTS = {
    "STORYBOARD_DRAFT_V10.json": "dc853f90c3299c5e1c051c0c37a45b6612f5418eaa9bbaad63608fd10ec56ae9",
    "NARRATION_DRAFT_V10.md": "4324c9b73de038e760c67e80fee70b60656599cf22d95cb1d92167e818f5ef75",
    "CLAIM_LINE_LEDGER_V10.md": "aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa",
    "DETERMINISTIC_DIAGRAM_SPEC_V10.md": "e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e",
    "V10_WPM_AUDIT.json": "5ca591ca336e991381662d865a9cb8a3434829d097af73427d0c3c32b6457678",
    "V10_SHORTHAND_AUDIT.json": "ec8a8d2095785b0db936fbdd009da0872a086d9a5acb82c3b02b9bfb2095224c",
    "V10_FREEZE_RECEIPT.json": "2bc19869459219c9909691b33c174bf32e17ebfe8f6f9e13f42c7d14da66da13",
    "LANA_CONFIRM_V10.md": "436e5596f8ef874d7bb5ec0945327e0bef7106c82badce4ceef93926c30008c4",
    "GORU_CONFIRM_V10.md": "4c65cebcf6a99e268ed59218a64f064f6641526599c14fa441717a4f10efcff3",
    "KUN_CONFIRM_V10.md": "48a53432753041ca7acfc0b5a46424c8ee7adacb8edd7d7e6d364524039d9fff",
}
OUTPUTS = {
    "story": D / "STORYBOARD_DRAFT_V11.json",
    "narration": D / "NARRATION_DRAFT_V11.md",
    "ledger": D / "CLAIM_LINE_LEDGER_V11.md",
    "graphics": D / "DETERMINISTIC_DIAGRAM_SPEC_V11.md",
    "delta": D / "V11_DELTA_RECEIPT.json",
}
OLD_CARD01 = (
    "Could our universe be inside a black hole? It's a question we were personally curious about — "
    "a side-interest, not part of the lab's research programme. We read the original scientific "
    "papers to see what they actually predict. One of these ideas gives us a number we can check "
    "against real stars. For galaxy spin, the sources give no expected size for the effect, and even "
    "a perfect measurement couldn't tell us a black hole was the cause. So this route closes. The "
    "idea is not declared true or false."
)
NEW_CARD01 = (
    "Could our universe be inside a black hole? It's a personal side-interest — not part of the lab's "
    "research programme. We read the original papers to see what they actually predict. One idea "
    "gives us a number to check against real stars. For galaxy spin, the sources give no expected "
    "size for the effect — and even a perfect measurement couldn't tell us a black hole was the "
    "cause. So this route closes. The idea is not declared true or false."
)
TIMINGS = {"01": 38, "02": 40, "03": 42, "07": 33, "09": 29}
OLD_TIMINGS = {"01": 35, "02": 36, "03": 39, "07": 29, "09": 27}
DELIBERATE_LOW = {"05": 51, "10": 36}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for name, expected in INPUTS.items():
    path = D / name
    if not path.exists() or sha(path) != expected:
        actual = sha(path) if path.exists() else "MISSING"
        raise SystemExit(f"pinned V10 input drift {name}: {actual}")

story_path = D / "STORYBOARD_DRAFT_V10.json"
narration_path = D / "NARRATION_DRAFT_V10.md"
ledger_path = D / "CLAIM_LINE_LEDGER_V10.md"
graphics_path = D / "DETERMINISTIC_DIAGRAM_SPEC_V10.md"

story = json.loads(story_path.read_text())
cards = {card["id"]: card for card in story["cards"]}
if cards["01"]["narration"] != OLD_CARD01:
    raise SystemExit("Card 01 exact V10 narration anchor drift")
for card_id, expected in OLD_TIMINGS.items():
    if cards[card_id]["planned_seconds"] != expected:
        raise SystemExit(f"Card {card_id} exact V10 planned_seconds anchor drift")
for card_id, expected in DELIBERATE_LOW.items():
    if cards[card_id]["planned_seconds"] != expected:
        raise SystemExit(f"Card {card_id} deliberate-LOW timing anchor drift")
if story["estimated_duration_seconds"] != 399:
    raise SystemExit("V10 aggregate duration anchor drift")

cards["01"]["narration"] = NEW_CARD01
for card_id, seconds in TIMINGS.items():
    cards[card_id]["planned_seconds"] = seconds
story["estimated_duration_seconds"] = sum(card["planned_seconds"] for card in story["cards"])
if story["estimated_duration_seconds"] != 415:
    raise SystemExit("V11 aggregate duration is not 415 seconds")
OUTPUTS["story"].write_text(json.dumps(story, indent=2, ensure_ascii=False) + "\n")

narration = narration_path.read_text()
if narration.count(OLD_CARD01) != 1:
    raise SystemExit("standalone narration exact V10 Card 01 anchor count is not one")
OUTPUTS["narration"].write_text(narration.replace(OLD_CARD01, NEW_CARD01))

# Lana's Section-3 invariants require exact unchanged claim and graphics bytes.
OUTPUTS["ledger"].write_bytes(ledger_path.read_bytes())
OUTPUTS["graphics"].write_bytes(graphics_path.read_bytes())

delta = {
    "status": "V11_LANA_RETIMING_BUILT_AWAITING_TIGHT_THREE_SEAT_EXACT_HASH_CONFIRMATION_NO_RENDER",
    "render_authority": False,
    "base_review_targets": {
        name: INPUTS[name]
        for name in (
            "NARRATION_DRAFT_V10.md",
            "STORYBOARD_DRAFT_V10.json",
            "CLAIM_LINE_LEDGER_V10.md",
            "DETERMINISTIC_DIAGRAM_SPEC_V10.md",
        )
    },
    "authority_receipts": {
        "LANA_CONFIRM_V10.md": {
            "sha256": INPUTS["LANA_CONFIRM_V10.md"],
            "role": "retiming ruling; exact Card-01 narration; deliberate-LOW disposition; V11 invariants",
        },
        "GORU_CONFIRM_V10.md": {
            "sha256": INPUTS["GORU_CONFIRM_V10.md"],
            "role": "V10 pacing HOLD; recommendation superseded by Lana's explicit LOW-card adjudication",
        },
        "KUN_CONFIRM_V10.md": {
            "sha256": INPUTS["KUN_CONFIRM_V10.md"],
            "role": "opening boundary/pacing HOLD and Card-01 release conditions",
        },
    },
    "authored_canonical_changes": [
        {"path": "cards[0].narration", "old": OLD_CARD01, "new": NEW_CARD01},
        *[
            {
                "path": f"cards[{index}].planned_seconds",
                "card_id": card_id,
                "old": OLD_TIMINGS[card_id],
                "new": TIMINGS[card_id],
            }
            for index, card_id in ((0, "01"), (1, "02"), (2, "03"), (6, "07"), (8, "09"))
        ],
    ],
    "derived_canonical_change": {
        "path": "estimated_duration_seconds",
        "old": 399,
        "new": 415,
        "rule": "sum(cards[*].planned_seconds)",
    },
    "derived_changed_channel": {
        "file": "NARRATION_DRAFT_V11.md",
        "change": "Card 01 spoken narration only; exact same replacement as canonical storyboard",
    },
    "deliberate_low_timings_preserved": DELIBERATE_LOW,
    "unchanged_byte_copies": {
        "CLAIM_LINE_LEDGER_V11.md": INPUTS["CLAIM_LINE_LEDGER_V10.md"],
        "DETERMINISTIC_DIAGRAM_SPEC_V11.md": INPUTS["DETERMINISTIC_DIAGRAM_SPEC_V10.md"],
    },
    "explicitly_unchanged": [
        "all assertion headings",
        "all narration except Card 01",
        "all planned_seconds except Cards 01, 02, 03, 07, and 09",
        "Cards 05 and 10 deliberate-LOW timings",
        "all diagrams and printable labels",
        "all on-screen support including the full-card Card-01 boundary badge",
        "all source-claim IDs and packet-line mappings",
        "all scientific numbers, dates, and published-author citations",
        "all shorthand/reveal constraints",
        "all Card-05 no-terminus constraints",
        "all V10 internal H1/status/scaffolding labels under the tight-delta order",
    ],
}
OUTPUTS["delta"].write_text(json.dumps(delta, indent=2, ensure_ascii=False) + "\n")

print(json.dumps({
    "status": delta["status"],
    "outputs": {path.name: sha(path) for path in OUTPUTS.values()},
    "authored_canonical_changes": [item["path"] for item in delta["authored_canonical_changes"]],
    "derived_canonical_change": delta["derived_canonical_change"]["path"],
}, indent=2))
