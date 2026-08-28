#!/usr/bin/env python3
"""Frozen-input helpers for the local Phase-2 BHU explainer v3 build."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
BUILD = Path(__file__).resolve().parent
ASSETS = ROOT / "assets_v3"
SCRIPT = ROOT / "SCRIPT.md"
STORYBOARD = ROOT / "STORYBOARD.json"
DESIGN = ROOT / "DESIGN_SYSTEM.md"
CLAIM_LEDGER = ROOT / "CLAIM_LEDGER.md"
PACKET_GATE = ROOT / "KIMI_P2V3_PACKET_GATE.md"
PINS = ASSETS / "PINS.sha256"
ASR_QA = ROOT / "ASR_QA.md"
DONE = ROOT / "GPT3_F_DONE.md"

EXPECTED_HASHES = {
    "OVERNIGHT_BRIEF_P2V3.md": "1fb37241248ca9e2bef6b1386ee4231656abbf25353a724777131a5fe3908b65",
    "DESIGN_SYSTEM.md": "c2952af327f93c99a0027eb89b4f7572d70bab68008ee1d1998de568d5de2210",
    "SCRIPT.md": "7d88f058426c58b4776ba873a3ab345a20a3f2b71caed6ecf0f40abd1e3321ee",
    "STORYBOARD.json": "963c31ba7f3374b5d37f960ee71bc155e43249bf65ddc5c6ba2c7eed5471a27d",
    "CLAIM_LEDGER.md": "fa24e6cf497085fb99aee2a7e60328df33d46b70ae4b80ce8dfe5b30edf5c956",
    "KIMI_P2V3_PACKET_GATE.md": "077d799e8bacced2e028c3e1400bd60cca172ccc512b330dce76a6de7ef04a5f",
    "assets_v3/PINS.sha256": "09505ab963b6faea7fc2f24aa570c4fc7fdc25b1e06e7c3c33664d965f59130a",
}
EXPECTED_ASSETS = {
    "prd_1111.4595_fig1_scale.jpg": "b93fb4b886c793b4db14f347bb49a628f2d5bb67c972e8b87fc536134a6cc514",
    "prd_1111.4595_fig2_temp.jpg": "f659dfb67ecfab940d107ed48ba8e273335d2b83d46bd8e72e3f74cfd8c047d4",
    "ds_1006.4166_comparison.png": "af9efe93cbaa832f2ec782e689021f097768f6afa13e09303cc7409295a892cb",
    "ds_1006.4166_prefac_Yp.png": "e34abd8af840017a715efc61a7a31943ad02de39a4d6e886edbe47e958d168b3",
    "nbp_p01_cold_open.png": "d7991658f3d15aa1d6e329b1063612e866d1897f1478aea939c96ff215fa5f6f",
}
EXPECTED_EQUATIONS = ["w = +1 vs w = −1", "ε ≤ 10⁻²⁷", "a⁻⁶ = a⁻⁶"]
NO_PLOTS_TEXT = "THIS PAPER CONTAINS NO PLOTS — THE ENTIRE ARGUMENT IS EQUATIONS"
ILLUSTRATION_CHIP = "NebulaMind rendering — Concept Illustration Only"


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


def parse_pins() -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    lines = [line for line in PINS.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(lines) != len(EXPECTED_ASSETS):
        raise RuntimeError(f"asset pin count mismatch: {len(lines)}")
    for line_number, line in enumerate(lines, 1):
        match = re.fullmatch(r"([0-9a-f]{64})  ([^/]+)", line)
        if not match:
            raise RuntimeError(f"invalid lane-local PINS line {line_number}: {line!r}")
        digest, filename = match.groups()
        expected = EXPECTED_ASSETS.get(filename)
        if expected is None or digest != expected:
            raise RuntimeError(f"unexpected pin {filename}: {digest}")
        path = ASSETS / filename
        actual = sha256(path)
        if actual != digest:
            raise RuntimeError(f"asset pin mismatch for {filename}: {actual}")
        records.append({"filename": filename, "sha256": actual, "path": str(path)})
    if {r["filename"] for r in records} != set(EXPECTED_ASSETS):
        raise RuntimeError("asset pin closed-world mismatch")
    return records


def load_frozen_inputs() -> dict[str, Any]:
    for name, expected in EXPECTED_HASHES.items():
        path = ROOT / name
        if not path.is_file():
            raise RuntimeError(f"missing frozen input: {path}")
        actual = sha256(path)
        if actual != expected:
            raise RuntimeError(f"frozen input hash mismatch for {name}: {actual}")
    first = PACKET_GATE.read_text(encoding="utf-8").splitlines()[0].strip()
    if not first.startswith("PASS_P2V3_PACKET"):
        raise RuntimeError(f"packet gate not passed: {first!r}")
    story = json.loads(STORYBOARD.read_text(encoding="utf-8"))
    panels = story["panels"]
    parsed = parse_script(SCRIPT.read_text(encoding="utf-8"))
    if len(panels) != 16 or len(parsed) != 16:
        raise RuntimeError("v3 requires exactly 16 panels")
    for script_panel, panel in zip(parsed, panels):
        if script_panel["id"] != panel["id"]:
            raise RuntimeError(f"panel id mismatch at {panel['id']}")
        if script_panel["heading"] != panel["assertion_heading"]:
            raise RuntimeError(f"heading mismatch at panel {panel['id']}")
        if script_panel["narration"] != panel["narration"]:
            raise RuntimeError(f"narration not byte-identical at panel {panel['id']}")
        if text_sha256(panel["narration"]) != panel["narration_sha256"]:
            raise RuntimeError(f"narration hash mismatch at panel {panel['id']}")
        if panel["viewer_text_closed_world"][0] != panel["assertion_heading"]:
            raise RuntimeError(f"assertion heading not first viewer item at panel {panel['id']}")
    equations = [item for p in panels for item in p["viewer_text_closed_world"] if " = " in item or " ≤ " in item]
    if equations != EXPECTED_EQUATIONS:
        raise RuntimeError(f"equation inventory mismatch: {equations!r}")
    no_plots = [p["id"] for p in panels if NO_PLOTS_TEXT in p["viewer_text_closed_world"]]
    if no_plots != ["03", "04", "09", "11"]:
        raise RuntimeError(f"no-plots panel set mismatch: {no_plots}")
    if sum(int(p["word_count"]) for p in panels) != 1371:
        raise RuntimeError("narration word count changed")
    if sum(float(p["planned_seconds"]) for p in panels) != 674.0:
        raise RuntimeError("planned duration changed")
    return {
        "root": ROOT,
        "build": BUILD,
        "storyboard": story,
        "panels": panels,
        "script_panels": parsed,
        "gate_token": first,
        "asset_pins": parse_pins(),
        "equations": equations,
        "no_plots_panels": no_plots,
    }
