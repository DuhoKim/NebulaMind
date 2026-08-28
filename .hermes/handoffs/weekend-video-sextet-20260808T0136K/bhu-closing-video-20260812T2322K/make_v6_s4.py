#!/usr/bin/env python3
"""Create BHU V6 by applying only Lana S4 to frozen V5.

The canonical storyboard has exactly three changed Card 05 string fields:
1. narration,
2. diagram callout instruction,
3. on-screen support.

The standalone narration is a derived mirror of field 1. All administrative V5
labels, timing, and every other byte are deliberately preserved. The ledger is
copied byte-for-byte.
"""
from pathlib import Path
import json
import shutil

D = Path(__file__).resolve().parent
v5_story_path = D / "STORYBOARD_DRAFT_V5.json"
v6_story_path = D / "STORYBOARD_DRAFT_V6.json"
v5_narr_path = D / "NARRATION_DRAFT_V5.md"
v6_narr_path = D / "NARRATION_DRAFT_V6.md"
v5_ledger_path = D / "CLAIM_LINE_LEDGER_V5.md"
v6_ledger_path = D / "CLAIM_LINE_LEDGER_V6.md"

story = json.loads(v5_story_path.read_text())
card = next(c for c in story["cards"] if c["id"] == "05")

old_narration = (
    "At the quoted 68.3% level, the second measurement clears two solar masses; "
    "at the stricter 95.4% level, the packet says it does not."
)
new_narration = (
    "At the quoted 68.3% level, the second measurement clears two solar masses; "
    "at the stricter 95.4% level, the closing record says it does not."
)
if card["narration"].count(old_narration) != 1:
    raise SystemExit("S4 narration anchor mismatch")
card["narration"] = card["narration"].replace(old_narration, new_narration)

old_callout = (
    '"At 95.4% credibility, the packet states only that the result does not clear '
    '2.00; no lower-bound value is quoted here."'
)
new_callout = (
    '"At 95.4% credibility, the closing record states only that the result does not '
    'clear 2.00; no lower-bound value is quoted here."'
)
if card["diagram"].count(old_callout) != 1:
    raise SystemExit("S4 callout anchor mismatch")
card["diagram"] = card["diagram"].replace(old_callout, new_callout)

old_support = "AT 95.4% CREDIBILITY, THE PACKET STATES ONLY THAT THE RESULT DOES NOT CLEAR 2.00"
new_support = "AT 95.4% CREDIBILITY, THE CLOSING RECORD STATES ONLY THAT THE RESULT DOES NOT CLEAR 2.00"
if card["on_screen_support"].count(old_support) != 1:
    raise SystemExit("S4 support anchor mismatch")
card["on_screen_support"][card["on_screen_support"].index(old_support)] = new_support

# Same serialization that created V5; only the three fields above may differ.
v6_story_path.write_text(json.dumps(story, indent=2, ensure_ascii=False) + "\n")

# Derived narration mirror: one physical occurrence reflects canonical field 1.
narration = v5_narr_path.read_text()
if narration.count(old_narration) != 1:
    raise SystemExit("standalone narration mirror anchor mismatch")
v6_narr_path.write_text(narration.replace(old_narration, new_narration))

# S4 does not touch the internal ledger; preserve it byte-for-byte.
shutil.copyfile(v5_ledger_path, v6_ledger_path)

print("wrote V6 S4-only artifacts")
