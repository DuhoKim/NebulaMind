#!/usr/bin/env python3
"""Exact contract tests for the two V13 repairs authorized by Lana and Duho."""
from __future__ import annotations

import json
import os
from pathlib import Path

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K")
STORY = Path(os.environ.get("V13_STORY", SOURCE / "STORYBOARD_DRAFT_V13.json"))
TEXT_CONTRACT = Path(os.environ.get("V13_TEXT_CONTRACT", SOURCE / "V13_VISUAL_TEXT_CONTRACT.json"))
EXACT_NO_TERMINUS = (
    "no 95.4% endpoint, arrow, tick, bracket, marker, whisker, shaded boundary, "
    "axis-aligned glyph, or scaled terminus"
)
EXACT_ILLUSTRATION_ROLE = {
    "role": "illustration_tag",
    "text": "ILLUSTRATION",
    "permitted_when": "QA judges a generated asset could be read as an observation",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    require(STORY.exists(), f"missing V13 storyboard: {STORY}")
    require(TEXT_CONTRACT.exists(), f"missing V13 text contract: {TEXT_CONTRACT}")
    story = json.loads(STORY.read_text())
    contract = json.loads(TEXT_CONTRACT.read_text())
    require(story["version"] == "V13", "story version is not V13")
    require(
        story["render_contract"].get("card_05_no_terminus_prohibition") == EXACT_NO_TERMINUS,
        "Repair A absent or paraphrased: exact nine-term enumeration including scaled terminus required",
    )
    require(
        contract["rules"].get("conditionally_permitted_roles") == [EXACT_ILLUSTRATION_ROLE],
        "Repair B absent, broadened, or paraphrased",
    )
    print("PASS_V13_TWO_EXACT_CONTRACT_REPAIRS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
