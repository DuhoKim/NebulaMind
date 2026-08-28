#!/usr/bin/env python3
"""Create BHU V7 by applying only the two required Card 06 repairs to V6.

Canonical storyboard changes:
1. Card 06 assertion heading.
2. Card 06 printable diagram label.

The standalone narration mirrors change 1. Every other byte is preserved where
possible; the internal claim ledger is copied byte-for-byte.
"""
from pathlib import Path
import json
import shutil

D = Path(__file__).resolve().parent
v6_story_path = D / "STORYBOARD_DRAFT_V6.json"
v7_story_path = D / "STORYBOARD_DRAFT_V7.json"
v6_narr_path = D / "NARRATION_DRAFT_V6.md"
v7_narr_path = D / "NARRATION_DRAFT_V7.md"
v6_ledger_path = D / "CLAIM_LINE_LEDGER_V6.md"
v7_ledger_path = D / "CLAIM_LINE_LEDGER_V7.md"

story = json.loads(v6_story_path.read_text())
card = next(c for c in story["cards"] if c["id"] == "06")

old_heading = "The evidence enters the test regime; the packet does not call it falsification"
new_heading = "The evidence enters the test regime; the closing record does not call it falsification"
if card["heading"] != old_heading:
    raise SystemExit("Card 06 heading anchor mismatch")
card["heading"] = new_heading

old_label = "label PACKET DOES NOT ADJUDICATE"
new_label = "label CLOSING RECORD DOES NOT ADJUDICATE"
if card["diagram"].count(old_label) != 1:
    raise SystemExit("Card 06 diagram-label anchor mismatch")
card["diagram"] = card["diagram"].replace(old_label, new_label)

# Preserve all other JSON fields and use the same serialization as V6.
v7_story_path.write_text(json.dumps(story, indent=2, ensure_ascii=False) + "\n")

# The assertion heading is duplicated in the standalone narration document.
narration = v6_narr_path.read_text()
if narration.count(old_heading) != 1:
    raise SystemExit("standalone Card 06 heading anchor mismatch")
v7_narr_path.write_text(narration.replace(old_heading, new_heading))

# Internal metadata may retain packet/ledger vocabulary; no claim mapping changed.
shutil.copyfile(v6_ledger_path, v7_ledger_path)

print("wrote V7 two-string artifacts")
