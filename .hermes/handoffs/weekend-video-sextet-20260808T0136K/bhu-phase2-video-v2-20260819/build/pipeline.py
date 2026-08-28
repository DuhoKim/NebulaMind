#!/usr/bin/env python3
"""Frozen-input helpers for the local Phase-2 BHU explainer v2 build."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
BUILD = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
VIDEO_BRIEF = ROOT / "VIDEO_BRIEF_P2V2.md"
SCRIPT = ROOT / "SCRIPT.md"
STORYBOARD = ROOT / "STORYBOARD.json"
VISUALS = ROOT / "VISUALS.md"
CLAIM_LEDGER = ROOT / "CLAIM_LEDGER.md"
PACKET_GATE = ROOT / "KIMI_P2V2_PACKET_GATE.md"
PINS = ASSETS / "PINS.sha256"
ASR_QA = ROOT / "ASR_QA.md"
DONE = ROOT / "GPT3_DONE.md"

EXPECTED_HASHES = {
    "VIDEO_BRIEF_P2V2.md": "876895c449b855800be7734d29cb5d60d72b460e10b7d5f44e010aa5377722b7",
    "SCRIPT.md": "684b6e038d467e6cc575fef3f54a6e0ca9fc7f250c2bf96f8cd4b380925dae3d",
    "STORYBOARD.json": "2d9469cbc496447e1dfe66b532f9cb0a9046e991903a60911b31e207fa15f385",
    "VISUALS.md": "c73a547298c75b1024dc88cae5ddf0b4bc17b7b432ffd9c3fc609813b5fe2815",
    "CLAIM_LEDGER.md": "a4a9cd813cfefb948da4abf4adde4eb5658c952b36256321c604fd1c6d959073",
    "KIMI_P2V2_PACKET_GATE.md": "de9a644466f11ef1b14e37035a2aab69f74efbaf628af91239fd62919ea1f655",
    "assets/PINS.sha256": "e234a5c8497681ff75390c454092150b0458025da657bf4ac08f1f3b4ff26113",
}
EXPECTED_ASSETS = {
    "prd_1111.4595_fig1_scale.jpg": "b93fb4b886c793b4db14f347bb49a628f2d5bb67c972e8b87fc536134a6cc514",
    "prd_1111.4595_fig2_temp.jpg": "f659dfb67ecfab940d107ed48ba8e273335d2b83d46bd8e72e3f74cfd8c047d4",
    "ds_1006.4166_comparison.png": "af9efe93cbaa832f2ec782e689021f097768f6afa13e09303cc7409295a892cb",
    "ds_1006.4166_prefac_Yp.png": "e34abd8af840017a715efc61a7a31943ad02de39a4d6e886edbe47e958d168b3",
}
EXPECTED_GATE = "PASS_P2V2_PACKET"
EXPECTED_EQUATIONS = ["w = +1 vs w = −1", "ε ≤ 10⁻²⁷", "a⁻⁶ = a⁻⁶"]
EXPECTED_NO_PLOTS_PANELS = ["02", "06", "08"]
NO_PLOTS_TEXT = "THIS PAPER CONTAINS NO PLOTS — THE ENTIRE ARGUMENT IS EQUATIONS"
ORIGINAL_GRAPHIC_TEXT = "NebulaMind rendering"
PANEL_09_FIXED_LABEL = "TREATMENT BRANCHES · WITHIN ×9"


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


def render_viewer_text(panel: dict[str, Any]) -> list[str]:
    """Apply the packet-gated VISUALS FIX RECORD to render labels."""
    labels = list(panel["viewer_text_closed_world"])
    if panel["id"] == "09" and PANEL_09_FIXED_LABEL not in labels:
        ceiling_index = labels.index("CEILING · NOT A MEASURED TRANSFER")
        labels.insert(ceiling_index + 1, PANEL_09_FIXED_LABEL)
    return labels


def parse_pins() -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    lines = PINS.read_text(encoding="utf-8").splitlines()
    if len(lines) != len(EXPECTED_ASSETS):
        raise RuntimeError(f"PINS.sha256 must contain one line per paper figure; found {len(lines)}")
    for line_number, line in enumerate(lines, 1):
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            raise RuntimeError(f"invalid PINS.sha256 line {line_number}: {line!r}")
        digest, raw_path = match.groups()
        path = Path(raw_path)
        if not path.is_absolute() or path.parent != ASSETS:
            raise RuntimeError(f"pin line {line_number} is not lane-local absolute asset path: {raw_path}")
        expected = EXPECTED_ASSETS.get(path.name)
        if expected is None or digest != expected:
            raise RuntimeError(f"unexpected pin on line {line_number}: {path.name} {digest}")
        actual = sha256(path)
        if actual != digest:
            raise RuntimeError(f"asset pin mismatch on line {line_number}: {path.name}: {actual}")
        records.append({"line": str(line_number), "path": str(path), "filename": path.name, "manifest_sha256": digest, "actual_sha256": actual, "status": "OK"})
    if {record["filename"] for record in records} != set(EXPECTED_ASSETS):
        raise RuntimeError("PINS.sha256 closed-world asset set mismatch")
    return records


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

    asset_pins = parse_pins()
    story = json.loads(STORYBOARD.read_text(encoding="utf-8"))
    script_panels = parse_script(SCRIPT.read_text(encoding="utf-8"))
    panels = story["panels"]
    if len(panels) != 12 or len(script_panels) != len(panels):
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
    if sum(int(panel["word_count"]) for panel in panels) != 1127:
        raise RuntimeError("storyboard narration word-count contract changed")
    if sum(float(panel["planned_seconds"]) for panel in panels) != 473.0:
        raise RuntimeError("storyboard timing contract changed")
    no_plot_panels = [panel["id"] for panel in panels if NO_PLOTS_TEXT in panel["viewer_text_closed_world"]]
    if no_plot_panels != EXPECTED_NO_PLOTS_PANELS:
        raise RuntimeError(f"no-plots cards must appear on exactly {EXPECTED_NO_PLOTS_PANELS}: {no_plot_panels}")
    if [panel["id"] for panel in panels if ORIGINAL_GRAPHIC_TEXT in panel["viewer_text_closed_world"]] != ["02", "03", "06", "07", "08", "09", "11"]:
        raise RuntimeError("NebulaMind rendering chip panel set changed")
    if PANEL_09_FIXED_LABEL not in VISUALS.read_text(encoding="utf-8") or PANEL_09_FIXED_LABEL not in render_viewer_text(panels[8]):
        raise RuntimeError("authoritative VISUALS FIX RECORD branch label is not renderable")
    return {
        "root": ROOT,
        "build": BUILD,
        "storyboard": story,
        "panels": panels,
        "script_panels": script_panels,
        "gate_token": token,
        "equations": equations,
        "asset_pins": asset_pins,
    }
