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
PACKET_GATE = ROOT / "KUN_TV_PACKET_GATE.md"
RENDER_BRIEF = ROOT / "SEXTET_BRIEF_THEORY_VIDEO.md"

EXPECTED_HASHES = {
    "SCRIPT.md": "fdfa1cccffa27b77730ac43e01bfbd8e925103cc4a0428632871866ca72db788",
    "STORYBOARD.json": "48ddf688406be2ca17837ba41d939f42bd59a8119f30ec021dcd9e896a2f1982",
    "VISUALS.md": "0dac4f3e2cb0f9c98d6f8c0c59f5092e077a96d0dcdf5b573fbfb81738858493",
    "CLAIM_LEDGER.md": "fada5ef9a197021700c7e90caac1fbbbc5d096c337910d2a52d198ca09179652",
    "LANA_ANNOTATION_REVIEW.md": "dda2b20f99f432c5546b03097bd6f9db0721b6225b2b8dead11b2da5c37a0ba6",
    "KUN_TV_PACKET_GATE.md": "1ae12cd33930d1ea02b477938bb70f91091b70d6685a213012e75d0c9f268ccf",
    "SEXTET_BRIEF_THEORY_VIDEO.md": "6d210629fedc7f514aa50c3068d1eaa6c3cc02daf1b7287236ec39e981fa4bc1",
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
