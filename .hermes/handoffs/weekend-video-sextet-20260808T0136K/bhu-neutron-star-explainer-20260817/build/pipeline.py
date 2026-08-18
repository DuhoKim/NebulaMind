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
PACKET_GATE = ROOT / "KUN_PACKET_GATE_20260818.md"
RENDER_BRIEF = ROOT / "RENDER_BRIEF.md"

EXPECTED_HASHES = {
    "SCRIPT.md": "dc89901803383f027c0ef4f831193937984a3aaa2a951a2fe9a357f821d5f347",
    "STORYBOARD.json": "2d6a56044221b16b3251572350005326e3e4a1a0d13f11ec1c849450042ccaed",
    "VISUALS.md": "0195a92afc788c4cb3d2bffdf3cd38e9152c3f893d82e8249b869298db2612a9",
    "CLAIM_LEDGER.md": "8512af27f15ace9e15153d49376920f138e70a30632cc7b503882d59d6a369ce",
    "KUN_PACKET_GATE_20260818.md": "e47c600d82edccbbc4e7690f66cda7f2e5e71eec9e2006452fce02622b138918",
    "RENDER_BRIEF.md": "d25eb9cfc6fa59b99605107253ad166a62c29dcfdd8c5729b3bb7a7e10b5165c",
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
