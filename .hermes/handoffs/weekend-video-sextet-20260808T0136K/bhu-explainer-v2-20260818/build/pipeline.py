#!/usr/bin/env python3
"""Frozen input and exact-text helpers for the local BHU explainer build."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
BUILD = Path(__file__).resolve().parent
SCRIPT = ROOT / "SCRIPT.md"
STORYBOARD = ROOT / "STORYBOARD.json"
VISUALS = ROOT / "VISUALS.md"
CLAIM_LEDGER = ROOT / "CLAIM_LEDGER.md"
PACKET_GATE = ROOT / "KUN_PACKET_GATE_V2.md"
RENDER_BRIEF = ROOT / "SEXTET_BRIEF_V2.md"

EXPECTED_HASHES = {
    "SCRIPT.md": "5c957bef48cdf44e5142affafc54c40af31d84651c69d2d99013ad98c881dc12",
    "STORYBOARD.json": "170d508781bdc187627ee8a71af45f68bd951ae2f3a37de221bb54bed92739f1",
    "VISUALS.md": "44a4cb0f7fee58970368a6d6728510cf453a69fee87973b2bf4d8108f9cc1227",
    "CLAIM_LEDGER.md": "381a8af5fb0d38684192186ac12f5a63e56300320541a0d9d5e37b352e3960bb",
    "KUN_PACKET_GATE_V2.md": "b95ff6586e3f16877dee1020a927b0d763cc1fdbbf0f4eb413e45b7b05baf160",
    "SEXTET_BRIEF_V2.md": "9968ea225b08f80234bc1636d1c1078af1cb20db2f5436e1dc9988954a0ae58a",
}


def expected_input_hashes() -> dict[str, str]:
    return dict(EXPECTED_HASHES)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_script(text: str) -> list[dict[str, str]]:
    parts = re.split(r"^## Panel (\d+) — (.+)$", text, flags=re.MULTILINE)
    panels: list[dict[str, str]] = []
    for index in range(1, len(parts), 3):
        narration = parts[index + 2].split("\n## ", 1)[0].strip()
        panels.append(
            {
                "id": parts[index],
                "heading": parts[index + 1],
                "narration": narration,
            }
        )
    return panels


def split_sentences(text: str) -> list[str]:
    sentences = re.split(
        r"(?<=[.!?])\s+(?=[A-Z])|(?<=[.!?][\"'])\s+(?=[A-Z])",
        text.strip(),
    )
    if " ".join(sentences) != text.strip():
        raise RuntimeError("sentence split failed exact reconstruction")
    return sentences


def load_frozen_inputs() -> dict[str, Any]:
    for name, expected in EXPECTED_HASHES.items():
        path = ROOT / name
        actual = sha256(path)
        if actual != expected:
            raise RuntimeError(f"frozen input hash mismatch for {name}: {actual}")
    gate_token = PACKET_GATE.read_text(encoding="utf-8").splitlines()[0].strip()
    if gate_token != "PASS_EXPLAINER_PACKET":
        raise RuntimeError(f"packet gate not passed: {gate_token!r}")
    story = json.loads(STORYBOARD.read_text(encoding="utf-8"))
    script_panels = parse_script(SCRIPT.read_text(encoding="utf-8"))
    if len(script_panels) != len(story["panels"]):
        raise RuntimeError("script/storyboard panel count mismatch")
    for parsed, panel in zip(script_panels, story["panels"]):
        if parsed["id"] != panel["id"]:
            raise RuntimeError(f"panel id mismatch: {parsed['id']} != {panel['id']}")
        if parsed["heading"] != panel["assertion_heading"]:
            raise RuntimeError(f"heading mismatch for panel {parsed['id']}")
        if parsed["narration"] != panel["narration"]:
            raise RuntimeError(f"narration mismatch for panel {parsed['id']}")
    return {
        "root": ROOT,
        "build": BUILD,
        "script_path": SCRIPT,
        "storyboard_path": STORYBOARD,
        "visuals_path": VISUALS,
        "claim_ledger_path": CLAIM_LEDGER,
        "packet_gate_path": PACKET_GATE,
        "render_brief_path": RENDER_BRIEF,
        "gate_token": gate_token,
        "storyboard": story,
        "panels": story["panels"],
        "script_panels": script_panels,
    }
