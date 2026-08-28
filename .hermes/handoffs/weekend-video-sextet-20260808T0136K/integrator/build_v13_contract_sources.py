#!/usr/bin/env python3
"""Materialize V13 as the exact two-repair successor to gated V12."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K")
V12_STORY = SOURCE / "STORYBOARD_DRAFT_V12.json"
V12_CONTRACT = SOURCE / "V12_VISUAL_TEXT_CONTRACT.json"
V12_NARRATION = SOURCE / "NARRATION_DRAFT_V12.md"
V8_DIAGRAM = SOURCE / "DETERMINISTIC_DIAGRAM_SPEC_V8.md"
V8_GATE = SOURCE / "KUN_GATE_V8.md"
REPAIR_A_AUTHORITY = SOURCE / "V13_REPAIR_A_EXACT_AUTHORITY.md"
LANA_GATE = SOURCE / "LANA_GATE_V12.md"
GORU_GATE = SOURCE / "GORU_GATE_V12.md"
KUN_GATE = SOURCE / "KUN_GATE_V12.md"
V13_STORY = SOURCE / "STORYBOARD_DRAFT_V13.json"
V13_CONTRACT = SOURCE / "V13_VISUAL_TEXT_CONTRACT.json"
RECEIPT = SOURCE / "V13_CONTRACT_REPAIR_RECEIPT.json"

EXPECTED = {
    "STORYBOARD_DRAFT_V12.json": "9d55257fe62c7a82d2fe32f424e896ce079393219c08aed6663b6c90c3539399",
    "V12_VISUAL_TEXT_CONTRACT.json": "c91662e15de095161e84d128683dd69150c8a73b4cbb6f303dda8f79c943999c",
    "NARRATION_DRAFT_V12.md": "178ffe4ada125668c8ff84bc156adee7820954591f9781adb7101aac562d80da",
    "DETERMINISTIC_DIAGRAM_SPEC_V8.md": "e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e",
    "KUN_GATE_V8.md": "c58c0a70a96f0363cf47f36cff6a5bd0541391bbe3621113b9fa4dd3b1aaaa9a",
    "V13_REPAIR_A_EXACT_AUTHORITY.md": "35e5fa1e90f8d4e5544b3aab4172e6a894b3c5a5df31d9e954a741991484056b",
    "LANA_GATE_V12.md": "be098a682cd7dde2ab0179f3959717002974641f539cbe60d8fe6a6810671991",
    "GORU_GATE_V12.md": "6ec1339bce1c1d616c8103203fa89880a262e42194ba72f320a3c4226e5c8c25",
    "KUN_GATE_V12.md": "c3faa80332b2ce86b88a322d1faa35104393f415e270029e465d3f2983f87975",
}
EXACT_NO_TERMINUS = (
    "no 95.4% endpoint, arrow, tick, bracket, marker, whisker, shaded boundary, "
    "axis-aligned glyph, or scaled terminus"
)
EXACT_ILLUSTRATION_ROLE = {
    "role": "illustration_tag",
    "text": "ILLUSTRATION",
    "permitted_when": "QA judges a generated asset could be read as an observation",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assert_sources() -> None:
    paths = {
        "STORYBOARD_DRAFT_V12.json": V12_STORY,
        "V12_VISUAL_TEXT_CONTRACT.json": V12_CONTRACT,
        "NARRATION_DRAFT_V12.md": V12_NARRATION,
        "DETERMINISTIC_DIAGRAM_SPEC_V8.md": V8_DIAGRAM,
        "KUN_GATE_V8.md": V8_GATE,
        "V13_REPAIR_A_EXACT_AUTHORITY.md": REPAIR_A_AUTHORITY,
        "LANA_GATE_V12.md": LANA_GATE,
        "GORU_GATE_V12.md": GORU_GATE,
        "KUN_GATE_V12.md": KUN_GATE,
    }
    for name, path in paths.items():
        actual = sha(path)
        if actual != EXPECTED[name]:
            raise RuntimeError(f"authority drift {name}: {actual}")
    if EXACT_NO_TERMINUS not in REPAIR_A_AUTHORITY.read_text():
        raise RuntimeError("exact V13 Repair A nine-term authority drift")
    if "scaled terminus" not in V8_GATE.read_text():
        raise RuntimeError("supporting V8 gate lost the literal scaled terminus term")


def without_repairs(story: dict, contract: dict) -> tuple[dict, dict]:
    story_copy = json.loads(json.dumps(story))
    contract_copy = json.loads(json.dumps(contract))
    story_copy["version"] = "V12"
    story_copy["status"] = "V12_BUILT_FROM_LANA_VISUAL_REDESIGN_SPEC_AWAITING_FULL_THREE_SEAT_GATE"
    story_copy["render_contract"].pop("card_05_no_terminus_prohibition", None)
    contract_copy["status"] = "V12_CLOSED_WORLD_VIEWER_TEXT_CONTRACT"
    contract_copy["rules"].pop("conditionally_permitted_roles", None)
    return story_copy, contract_copy


def main() -> int:
    assert_sources()
    old_story = json.loads(V12_STORY.read_text())
    old_contract = json.loads(V12_CONTRACT.read_text())
    story = json.loads(json.dumps(old_story))
    contract = json.loads(json.dumps(old_contract))
    story["version"] = "V13"
    story["status"] = "V13_TWO_CONTRACT_REPAIRS_AWAITING_FULL_THREE_SEAT_EXACT_HASH_GATE"
    story["render_contract"]["card_05_no_terminus_prohibition"] = EXACT_NO_TERMINUS
    contract["status"] = "V13_CLOSED_WORLD_VIEWER_TEXT_CONTRACT"
    contract["rules"]["conditionally_permitted_roles"] = [EXACT_ILLUSTRATION_ROLE]
    V13_STORY.write_text(json.dumps(story, indent=2, ensure_ascii=False) + "\n")
    V13_CONTRACT.write_text(json.dumps(contract, indent=2, ensure_ascii=False) + "\n")

    stripped_story, stripped_contract = without_repairs(story, contract)
    if stripped_story != old_story:
        raise RuntimeError("V13 storyboard changed beyond version/status and Repair A")
    if stripped_contract != old_contract:
        raise RuntimeError("V13 text contract changed beyond status and Repair B")
    if story["cards"] != old_story["cards"] or story["metaphor_kit"] != old_story["metaphor_kit"]:
        raise RuntimeError("V13 design/card bytes changed")
    if contract["cards"] != old_contract["cards"]:
        raise RuntimeError("V13 per-card closed-world lists changed")
    receipt = {
        "status": "PASS_V13_EXACTLY_TWO_CONTRACT_REPAIRS_AWAITING_THREE_SEAT_GATE",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "authority": {name: {"path": str(path), "sha256": EXPECTED[name]} for name, path in {
            "STORYBOARD_DRAFT_V12.json": V12_STORY,
            "V12_VISUAL_TEXT_CONTRACT.json": V12_CONTRACT,
            "NARRATION_DRAFT_V12.md": V12_NARRATION,
            "DETERMINISTIC_DIAGRAM_SPEC_V8.md": V8_DIAGRAM,
            "KUN_GATE_V8.md": V8_GATE,
            "V13_REPAIR_A_EXACT_AUTHORITY.md": REPAIR_A_AUTHORITY,
            "LANA_GATE_V12.md": LANA_GATE,
            "GORU_GATE_V12.md": GORU_GATE,
            "KUN_GATE_V12.md": KUN_GATE,
        }.items()},
        "outputs": {
            "STORYBOARD_DRAFT_V13.json": {"path": str(V13_STORY), "sha256": sha(V13_STORY), "bytes": V13_STORY.stat().st_size},
            "V13_VISUAL_TEXT_CONTRACT.json": {"path": str(V13_CONTRACT), "sha256": sha(V13_CONTRACT), "bytes": V13_CONTRACT.stat().st_size},
            "NARRATION_DRAFT_V12.md_reused_without_modification": {"path": str(V12_NARRATION), "sha256": sha(V12_NARRATION), "bytes": V12_NARRATION.stat().st_size},
        },
        "repairs": {
            "A": {"location": "STORYBOARD_DRAFT_V13.json.render_contract.card_05_no_terminus_prohibition", "value": EXACT_NO_TERMINUS, "exact_authority": "V13_REPAIR_A_EXACT_AUTHORITY.md", "supporting_v8_enumeration": "KUN_GATE_V8.md:45", "semantic_geometry_authority": "DETERMINISTIC_DIAGRAM_SPEC_V8.md:14-15"},
            "B": {"location": "V13_VISUAL_TEXT_CONTRACT.json.rules.conditionally_permitted_roles[0]", "value": EXACT_ILLUSTRATION_ROLE},
        },
        "proof": {
            "story_equal_v12_after_removing_version_status_and_repair_a": True,
            "text_contract_equal_v12_after_removing_status_and_repair_b": True,
            "all_11_cards_equal_v12": story["cards"] == old_story["cards"],
            "metaphor_kit_equal_v12": story["metaphor_kit"] == old_story["metaphor_kit"],
            "all_per_card_text_lists_equal_v12": contract["cards"] == old_contract["cards"],
            "narration_reused_exact_hash": sha(V12_NARRATION) == EXPECTED["NARRATION_DRAFT_V12.md"],
            "estimated_duration_seconds": story["estimated_duration_seconds"],
            "target_narration_wpm": story["render_contract"]["target_narration_wpm"],
            "allowed_wpm_band": story["render_contract"]["allowed_wpm_band"],
            "embedded_subtitle_stream_required": story["render_contract"]["embedded_subtitle_stream_required"],
            "upload_authorized_before_render_gate": False,
        },
        "gate": {"required": ["Lana", "Goru", "Kun"], "state": "NOT_RUN", "any_hold_blocks": True, "render_authorized": False},
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": receipt["status"], "story_sha256": sha(V13_STORY), "text_contract_sha256": sha(V13_CONTRACT), "narration_sha256": sha(V12_NARRATION), "receipt_sha256": sha(RECEIPT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
