#!/usr/bin/env python3
"""Build the BHU V9 tight delta from exact reviewed V8 bytes.

The only canonical content change is Card 04 narration sentence 1. The standalone
narration receives the same replacement. All other V8 bytes are preserved,
including the ledger, diagram spec, metadata, version labels, and status prose.
No audio, frame, render, upload, or publication action occurs here.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

D = Path(__file__).resolve().parent
INPUTS = {
    "STORYBOARD_DRAFT_V8.json": "56bcf195a871ae4f60f822b3e8cc3c5bd90f262a1a8325ca7b18a42b0917ddcb",
    "NARRATION_DRAFT_V8.md": "6dc0ca1984e9fa262a28c39cc23b6559dac0cc1c4ebb6026693fb7b5b004f35c",
    "CLAIM_LINE_LEDGER_V8.md": "aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa",
    "DETERMINISTIC_DIAGRAM_SPEC_V8.md": "e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e",
    "LANA_GATE_V8.md": "4240e33df939a5a0b7bd3cadf7ec54ef5efde04b6066717071e29e9e1d67fb35",
    "GORU_GATE_V8.md": "d3eb719e7176e9c976bba15134ecc293d42157bb0239ff16d4de2b7b6216c805",
    "KUN_GATE_V8.md": "c58c0a70a96f0363cf47f36cff6a5bd0541391bbe3621113b9fa4dd3b1aaaa9a",
}
OUTPUTS = {
    "story": D / "STORYBOARD_DRAFT_V9.json",
    "narration": D / "NARRATION_DRAFT_V9.md",
    "ledger": D / "CLAIM_LINE_LEDGER_V9.md",
    "graphics": D / "DETERMINISTIC_DIAGRAM_SPEC_V9.md",
    "delta": D / "V9_DELTA_RECEIPT.json",
}
OLD = (
    "One proposal says universes have children: every black hole buds off a new universe "
    "with slightly different physics."
)
NEW = (
    "One proposal — called cosmological natural selection — says universes have children: "
    "every black hole buds off a new universe with slightly different physics."
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for name, expected in INPUTS.items():
    path = D / name
    if not path.exists() or sha(path) != expected:
        actual = sha(path) if path.exists() else "MISSING"
        raise SystemExit(f"pinned V8 input drift {name}: {actual}")

story_path = D / "STORYBOARD_DRAFT_V8.json"
narration_path = D / "NARRATION_DRAFT_V8.md"
ledger_path = D / "CLAIM_LINE_LEDGER_V8.md"
graphics_path = D / "DETERMINISTIC_DIAGRAM_SPEC_V8.md"

story = json.loads(story_path.read_text())
card04 = next(card for card in story["cards"] if card["id"] == "04")
if card04["narration"].count(OLD) != 1:
    raise SystemExit("Card 04 exact sentence anchor count is not one")
card04["narration"] = card04["narration"].replace(OLD, NEW)
OUTPUTS["story"].write_text(json.dumps(story, indent=2, ensure_ascii=False) + "\n")

narration = narration_path.read_text()
if narration.count(OLD) != 1:
    raise SystemExit("standalone narration exact sentence anchor count is not one")
OUTPUTS["narration"].write_text(narration.replace(OLD, NEW))

# The user's change-nothing-else order is literal: unchanged review targets are
# copied byte-for-byte rather than receiving cosmetic V9 H1/status edits.
OUTPUTS["ledger"].write_bytes(ledger_path.read_bytes())
OUTPUTS["graphics"].write_bytes(graphics_path.read_bytes())

delta = {
    "status": "V9_TIGHT_DELTA_BUILT_AWAITING_THREE_SEAT_EXACT_HASH_CONFIRMATION_NO_RENDER",
    "render_authority": False,
    "base_review_targets": {name: INPUTS[name] for name in (
        "NARRATION_DRAFT_V8.md",
        "STORYBOARD_DRAFT_V8.json",
        "CLAIM_LINE_LEDGER_V8.md",
        "DETERMINISTIC_DIAGRAM_SPEC_V8.md",
    )},
    "base_verdict_receipts": {name: INPUTS[name] for name in (
        "LANA_GATE_V8.md", "GORU_GATE_V8.md", "KUN_GATE_V8.md"
    )},
    "authority": {
        "receipt": "LANA_GATE_V8.md",
        "receipt_sha256": INPUTS["LANA_GATE_V8.md"],
        "verdict": "PASS WITH ONE REPAIR",
        "repair_scope": "Card 04 narration sentence 1; both canonical storyboard and derived narration channels",
    },
    "canonical_changed_paths": ["cards[3].narration"],
    "derived_changed_files": ["NARRATION_DRAFT_V9.md"],
    "old_sentence": OLD,
    "new_sentence": NEW,
    "unchanged_byte_copies": {
        "CLAIM_LINE_LEDGER_V9.md": INPUTS["CLAIM_LINE_LEDGER_V8.md"],
        "DETERMINISTIC_DIAGRAM_SPEC_V9.md": INPUTS["DETERMINISTIC_DIAGRAM_SPEC_V8.md"],
    },
    "explicitly_unchanged": [
        "all assertion headings",
        "all card timing and planned-duration values",
        "all diagrams and printable labels",
        "all on-screen support",
        "all claim IDs and packet-line mappings",
        "all scientific numbers, dates, and published-author citations",
        "all Card 05 no-terminus constraints",
        "all V8 internal H1/status/scaffolding labels under the one-sentence-only order",
    ],
}
OUTPUTS["delta"].write_text(json.dumps(delta, indent=2, ensure_ascii=False) + "\n")

print(json.dumps({
    "status": delta["status"],
    "outputs": {path.name: sha(path) for path in OUTPUTS.values()},
    "canonical_changed_paths": delta["canonical_changed_paths"],
}, indent=2))
