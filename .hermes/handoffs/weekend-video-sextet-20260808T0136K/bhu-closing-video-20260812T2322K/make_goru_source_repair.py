#!/usr/bin/env python3
"""Create source-bound BHU script/storyboard/ledger revisions after Goru's audit.

Preserves every frozen predecessor. Only removes the unsupported exact 95.4%
lower-bound value; the permitted packet-level statement that it does not clear
2.00 at 95.4% remains.
"""
from pathlib import Path
import json

D = Path(__file__).resolve().parent

# Narration V2 -> V3
src = (D / "NARRATION_DRAFT_V2.md").read_text()
old = (
    "But the ninety-five point four percent lower bound is one point nine five. "
    "At that stronger credibility level, it does not clear two."
)
new = (
    "But at ninety-five point four percent credibility, the result does not clear two."
)
if src.count(old) != 1:
    raise SystemExit("narration replacement anchor mismatch")
(D / "NARRATION_DRAFT_V3.md").write_text(src.replace(old, new).replace(
    "narration draft V2, stranger rewrite",
    "narration draft V3, Goru source-bound repair",
    1,
))

# Storyboard V1 -> V2
p = D / "STORYBOARD_DRAFT_V1.json"
sb = json.loads(p.read_text())
sb["status"] = "SCRIPT_STORYBOARD_REPAIRED_NOT_CREW_CLEARED"
card = next(c for c in sb["cards"] if c["id"] == "05")
old_narr = (
    "But the ninety-five point four percent lower bound is one point nine five. "
    "At that stronger credibility level, it does not clear two."
)
new_narr = "But at ninety-five point four percent credibility, the result does not clear two."
if old_narr not in card["narration"]:
    raise SystemExit("storyboard narration anchor mismatch")
card["narration"] = card["narration"].replace(old_narr, new_narr)
old_diagram = "Add a distinct 95.4% lower-bound arrow ending at 1.95."
new_diagram = "Add a distinct 95.4% interval marker showing that the result does not clear 2.00."
if old_diagram not in card["diagram"]:
    raise SystemExit("storyboard diagram anchor mismatch")
card["diagram"] = card["diagram"].replace(old_diagram, new_diagram)
old_support = "95.4% LOWER BOUND: 1.95 M☉"
new_support = "AT 95.4% CREDIBILITY, THE RESULT DOES NOT CLEAR 2.00 M☉"
if old_support not in card["on_screen_support"]:
    raise SystemExit("storyboard support anchor mismatch")
card["on_screen_support"] = [
    new_support if x == old_support else x for x in card["on_screen_support"]
]
(D / "STORYBOARD_DRAFT_V2.json").write_text(
    json.dumps(sb, indent=2, ensure_ascii=False) + "\n"
)

# Claim ledger V1 -> V2
ledger = (D / "CLAIM_LINE_LEDGER.md").read_text()
old_row = (
    "| C07 | Fonseca measured 2.08 ± 0.07 solar masses; its quoted 68.3% interval clears 2.00, "
    "but it does not clear 2.00 at 95.4% credibility. | 47; 91–97; 268–277 | Exact nuance required; "
    "do not collapse to \"falsified.\" |"
)
new_row = (
    "| C07 | Fonseca measured 2.08 ± 0.07 solar masses; it clears 2.00 at the quoted 68.3% "
    "credibility, but not at 95.4% credibility. | 47; 91–97; 268–277 | Exact nuance required. "
    "The packet does not state the 95.4% lower-bound value, so no value may appear in the video; "
    "do not collapse the result to \"falsified.\" |"
)
if ledger.count(old_row) != 1:
    raise SystemExit("ledger replacement anchor mismatch")
ledger = ledger.replace(old_row, new_row).replace(
    "# BHU closure video — claim-to-line ledger",
    "# BHU closure video — claim-to-line ledger V2",
    1,
)
(D / "CLAIM_LINE_LEDGER_V2.md").write_text(ledger)

print("wrote NARRATION_DRAFT_V3.md, STORYBOARD_DRAFT_V2.json, CLAIM_LINE_LEDGER_V2.md")
