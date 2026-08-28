#!/usr/bin/env python3
"""Frozen-input helpers for the local Phase-2 BHU results video build."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
BUILD = Path(__file__).resolve().parent
VIDEO_BRIEF = ROOT / "VIDEO_BRIEF_P2.md"
SCRIPT = ROOT / "SCRIPT.md"
STORYBOARD = ROOT / "STORYBOARD.json"
VISUALS = ROOT / "VISUALS.md"
CLAIM_LEDGER = ROOT / "CLAIM_LEDGER.md"
PACKET_GATE = ROOT / "KIMI_P2V_PACKET_GATE.md"
ASR_QA = ROOT / "ASR_QA.md"
DONE = ROOT / "GPT3_DONE.md"

EXPECTED_HASHES = {
    "VIDEO_BRIEF_P2.md": "808cd93dae7ff621389ca4754fc69b6473b288b68903fd0bf578053ca46c313c",
    "SCRIPT.md": "82fc80e65683aaccf1987e166ef8b3f603bbc167b4771758f274636bc41ecacf",
    "STORYBOARD.json": "2f1f2c0a86329870c570ccdc422d84de72b0346a0d4a6a55be45f79665fb8442",
    "VISUALS.md": "c7fa914fb83ee97d28672a09914fe7e96e7c892860ac1394c2045af2125b93de",
    "CLAIM_LEDGER.md": "5238336c5c37510b8018821257feeb564bf88486b7e1bfe54d6f246f78f99b7b",
    "KIMI_P2V_PACKET_GATE.md": "8a6261d0a071e47aacbaa2da3af8b011c293c8890da97db40dd7c359fb3624dd",
}
EXPECTED_GATE = "PASS_P2V_PACKET"
EXPECTED_EQUATIONS = ["w = +1 vs w = −1", "ε ≤ 10⁻²⁷", "a⁻⁶ = a⁻⁶"]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_script(text: str) -> list[dict[str, str]]:
    parts = re.split(r"^## Panel (\d+) — (.+)$", text, flags=re.MULTILINE)
    panels: list[dict[str, str]] = []
    for index in range(1, len(parts), 3):
        narration = parts[index + 2].split("\n## ", 1)[0].strip()
        panels.append({"id": parts[index], "heading": parts[index + 1], "narration": narration})
    return panels


def equation_projection(panels: list[dict[str, Any]]) -> list[str]:
    return [
        item
        for panel in panels
        for item in panel["viewer_text_closed_world"]
        if " = " in item or " ≤ " in item
    ]


def load_frozen_inputs() -> dict[str, Any]:
    for name, expected in EXPECTED_HASHES.items():
        path = ROOT / name
        if not path.is_file():
            raise RuntimeError(f"missing frozen input: {path}")
        actual = sha256(path)
        if actual != expected:
            raise RuntimeError(f"frozen input hash mismatch for {name}: {actual}")
    gate_lines = PACKET_GATE.read_text(encoding="utf-8").splitlines()
    token = gate_lines[0].strip() if gate_lines else ""
    if token != EXPECTED_GATE:
        raise RuntimeError(f"packet gate not passed: {token!r}")

    story = json.loads(STORYBOARD.read_text(encoding="utf-8"))
    script_panels = parse_script(SCRIPT.read_text(encoding="utf-8"))
    panels = story["panels"]
    if len(panels) != 10 or len(script_panels) != len(panels):
        raise RuntimeError("script/storyboard panel count mismatch")
    for parsed, panel in zip(script_panels, panels):
        if parsed["id"] != panel["id"]:
            raise RuntimeError(f"panel id mismatch: {parsed['id']} != {panel['id']}")
        if parsed["heading"] != panel["assertion_heading"]:
            raise RuntimeError(f"assertion heading mismatch for panel {panel['id']}")
        if parsed["narration"] != panel["narration"]:
            raise RuntimeError(f"narration is not byte-identical for panel {panel['id']}")
        if text_sha256(panel["narration"]) != panel["narration_sha256"]:
            raise RuntimeError(f"narration hash mismatch for panel {panel['id']}")
        if panel["viewer_text_closed_world"][0] != panel["assertion_heading"]:
            raise RuntimeError(f"heading is not first closed-world viewer item for panel {panel['id']}")
    equations = equation_projection(panels)
    if equations != EXPECTED_EQUATIONS:
        raise RuntimeError(f"on-screen equation contract mismatch: {equations!r}")
    if sum(int(panel["word_count"]) for panel in panels) != 691:
        raise RuntimeError("storyboard narration word-count contract changed")
    if sum(float(panel["planned_seconds"]) for panel in panels) != 325.0:
        raise RuntimeError("storyboard timing contract changed")
    return {
        "root": ROOT,
        "build": BUILD,
        "storyboard": story,
        "panels": panels,
        "script_panels": script_panels,
        "gate_token": token,
        "equations": equations,
    }
