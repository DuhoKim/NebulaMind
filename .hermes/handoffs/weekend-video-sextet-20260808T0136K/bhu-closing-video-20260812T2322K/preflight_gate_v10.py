#!/usr/bin/env python3
"""Fail-closed BHU V10 tight three-seat exact-hash render gate.

A pass authorizes only local deterministic rendering: no paid generation, upload,
publication, or user acceptance. Until three exact V10 verdicts land, exit 2.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

D = Path(__file__).resolve().parent
TARGETS = {
    "NARRATION_DRAFT_V10.md": "4324c9b73de038e760c67e80fee70b60656599cf22d95cb1d92167e818f5ef75",
    "STORYBOARD_DRAFT_V10.json": "dc853f90c3299c5e1c051c0c37a45b6612f5418eaa9bbaad63608fd10ec56ae9",
    "CLAIM_LINE_LEDGER_V10.md": "aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa",
    "DETERMINISTIC_DIAGRAM_SPEC_V10.md": "e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e",
}
CONTROLS = {
    "V10_DELTA_RECEIPT.json": "e3fab1248e7511cc7cbf1bac56e5b3d5c89d2b9fcbe40cb33640d277976df643",
    "V10_BUILD_VERIFICATION.json": "814f2f7374239ac5756f7492d425db93d868826ab427aa04c0aa42a244352667",
    "V10_WPM_AUDIT.json": "5ca591ca336e991381662d865a9cb8a3434829d097af73427d0c3c32b6457678",
    "V10_SHORTHAND_AUDIT.json": "ec8a8d2095785b0db936fbdd009da0872a086d9a5acb82c3b02b9bfb2095224c",
}
VERDICTS = ["LANA_CONFIRM_V10.md", "GORU_CONFIRM_V10.md", "KUN_CONFIRM_V10.md"]
VERDICT_LINE = re.compile(
    r"(?im)^\s*(?:#{1,6}\s*)?(?:\*{1,2})?VERDICT(?:\*{1,2})?\s*:\s*"
    r"(?:\*{1,2})?(?:PASS_FOR_RENDER|PASS)(?:\*{1,2})?[.!]?\s*$"
)
BLOCKING_MARKER = re.compile(
    r"(?im)^\s*(?:#{1,6}\s*)?(?:\*{1,2})?(?:VERDICT|STATUS)?(?:\*{1,2})?\s*:?\s*"
    r"(?:PASS\s+WITH\b|CONDITIONAL(?:_PASS)?\b|HOLD\b|FAIL(?:ED|URE)?\b)"
)
REQUIRED_DISPOSITIONS = {
    "DELTA_DISPOSITION": "PASS_EXACT_V9_TO_V10_TWO_REPAIRS",
    "WPM_AUDIT_DISPOSITION": "ACCEPT_V10_TIMING_AS_PLANNED_FOR_RENDER",
    "SHORTHAND_AUDIT_DISPOSITION": "PASS_NO_CNS_EXCEPTION",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def hold(message: str) -> None:
    print("HOLD: " + message)
    raise SystemExit(2)


for name, expected in {**TARGETS, **CONTROLS}.items():
    path = D / name
    if not path.exists():
        hold(f"missing exact V10 file {name}")
    actual = sha(path)
    if actual != expected:
        hold(f"V10 file drift {name}: {actual}")

freeze_path = D / "V10_FREEZE_RECEIPT.json"
if not freeze_path.exists():
    hold("missing V10_FREEZE_RECEIPT.json")
freeze = json.loads(freeze_path.read_text())
if freeze.get("status") != "FROZEN_V10_AWAITING_TIGHT_THREE_SEAT_EXACT_HASH_CONFIRMATION":
    hold("V10 freeze status is not awaiting tight confirmation")
if freeze.get("render_authority") is not False:
    hold("V10 freeze receipt has unexpected pre-gate render authority")
if freeze.get("review_targets") != TARGETS:
    hold("V10 freeze target map does not match preflight target map")
if freeze.get("verification_controls") != CONTROLS:
    hold("V10 freeze control map does not match preflight control map")
if freeze.get("required_verdicts") != {name: None for name in VERDICTS}:
    hold("V10 freeze required-verdict map drift")

for name in VERDICTS:
    path = D / name
    if not path.exists():
        hold(f"missing unconditional exact-hash verdict {name}")
    text = path.read_text()
    if BLOCKING_MARKER.search(text):
        hold(f"conditional or blocking verdict marker in {name}")
    if not VERDICT_LINE.search(text):
        hold(f"no standalone unconditional VERDICT: PASS in {name}")
    for target_name, expected in TARGETS.items():
        if target_name not in text or expected not in text:
            hold(f"{name} does not bind exact {target_name} hash")
    for control_name in ("V10_WPM_AUDIT.json", "V10_SHORTHAND_AUDIT.json"):
        if control_name not in text or CONTROLS[control_name] not in text:
            hold(f"{name} does not bind exact {control_name} hash")
    for field, value in REQUIRED_DISPOSITIONS.items():
        pattern = re.compile(rf"(?im)^\s*{re.escape(field)}\s*:\s*{re.escape(value)}\s*$")
        if not pattern.search(text):
            hold(f"{name} lacks required {field}: {value}")

print("PASS_V10_TIGHT_THREE_SEAT_EXACT_HASH_GATE_LOCAL_RENDER_AUTHORIZED")
print("SCOPE: LOCAL_ONLY_NO_PAID_GENERATION_NO_UPLOAD_NO_PUBLICATION_NO_ACCEPTANCE")
sys.exit(0)
