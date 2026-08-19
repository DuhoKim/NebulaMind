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
ANNOTATION_REVIEW = ROOT / "LANA_ANNOTATION_REVIEW.md"
PACKET_GATE = ROOT / "MIRU_P1V_PACKET_GATE.md"
RENDER_BRIEF = ROOT / "SEXTET_BRIEF_P1_VIDEO.md"

EXPECTED_HASHES = {
    "SCRIPT.md": "befcce2b46d9da37721a1dc78344ccbe5a7925643a53fde6141ab5b95390ae70",
    "STORYBOARD.json": "6ae0aa429831ff4824b06e27f75e5e4abde3803dae99dd45d5f47beecf5bc592",
    "VISUALS.md": "e0bf240d81f4f7bbd95f73a9fd7d2bb52c778d0dda3a5c0708a742ae0f104971",
    "CLAIM_LEDGER.md": "caf0005ef8292c73baeacea8ff8991747d7459be80a786deee9953bea0edd476",
    "LANA_ANNOTATION_REVIEW.md": "310a5cc59eb01e52db75627601f127206c1837c632c115fd0d88674ad8fdaa69",
    "MIRU_P1V_PACKET_GATE.md": "65753f1f220469a8a4cc23b96a01f91e5fc5953cc004d75b313c99f6a05e0cd7",
    "SEXTET_BRIEF_P1_VIDEO.md": "a28956d71999b5121c86dd23a4053f381a0c279bb47c39e75b3efbe15f4bbaae",
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
        "annotation_review_path": ANNOTATION_REVIEW,
        "packet_gate_path": PACKET_GATE,
        "render_brief_path": RENDER_BRIEF,
        "gate_token": gate_token,
        "storyboard": story,
        "panels": story["panels"],
        "script_panels": script_panels,
    }
