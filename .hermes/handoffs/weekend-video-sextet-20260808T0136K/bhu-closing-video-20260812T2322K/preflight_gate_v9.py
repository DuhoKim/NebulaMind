#!/usr/bin/env python3
"""Fail-closed V9 tight three-seat exact-hash render gate.

Success authorizes only local, no-paid-generation, no-upload rendering. It does
not authorize publication or acceptance.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

D = Path(__file__).resolve().parent
TARGETS = {
    "NARRATION_DRAFT_V9.md": "85f111d366c5d11d912e4f7db5586f10b491b12b1c5091d3f94d822c388190b3",
    "STORYBOARD_DRAFT_V9.json": "c9824b95453be7e67d6066f3810648dc8d588a8c3210546ec9caa5ee74710d7a",
    "CLAIM_LINE_LEDGER_V9.md": "aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa",
    "DETERMINISTIC_DIAGRAM_SPEC_V9.md": "e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e",
}
CONTROLS = {
    "V9_DELTA_RECEIPT.json": "6835ef6c48f3b2ca70482ae7b5dee67325089c287f993d99eaa975ce05a8c497",
    "V9_BUILD_VERIFICATION.json": "a8776a1b8ba09855d2aa3daa52a7db84ed0e55cd0e3dfb32bc9d69653fc51b6d",
    "V9_SHORTHAND_AUDIT.json": "2cd55bd9698ec11ccf002b3e1810ab51408bfdbe18f4bca3fa51314e46931624",
}
VERDICTS = ["LANA_GATE_V9.md", "GORU_GATE_V9.md", "KUN_GATE_V9.md"]
VERDICT_LINE = re.compile(r"(?im)^\s*(?:#{1,6}\s*)?(?:\*{1,2})?VERDICT(?:\*{1,2})?\s*:\s*(?:\*{1,2})?(?:PASS_FOR_RENDER|PASS)(?:\*{1,2})?[.!]?\s*$")
BLOCKING_MARKER = re.compile(
    r"(?im)^\s*(?:#{1,6}\s*)?(?:\*{1,2})?(?:VERDICT|STATUS)?(?:\*{1,2})?\s*:?\s*"
    r"(?:PASS\s+WITH\b|CONDITIONAL(?:_PASS)?\b|HOLD\b|FAIL(?:ED|URE)?\b)"
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def hold(message: str) -> None:
    print("HOLD: " + message)
    raise SystemExit(2)


for name, expected in {**TARGETS, **CONTROLS}.items():
    path = D / name
    if not path.exists():
        hold(f"missing exact V9 file {name}")
    actual = sha(path)
    if actual != expected:
        hold(f"V9 file drift {name}: {actual}")

freeze_path = D / "V9_FREEZE_RECEIPT.json"
if not freeze_path.exists():
    hold("missing V9_FREEZE_RECEIPT.json")
freeze = json.loads(freeze_path.read_text())
if freeze.get("status") != "FROZEN_V9_AWAITING_TIGHT_THREE_SEAT_EXACT_HASH_CONFIRMATION":
    hold("V9 freeze status is not awaiting tight confirmation")
if freeze.get("render_authority") is not False:
    hold("V9 freeze receipt has unexpected pre-gate render authority")
if freeze.get("review_targets") != TARGETS:
    hold("V9 freeze target map does not match preflight target map")

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
    low = text.lower()
    if not ("card 04" in low and "sentence 1" in low and ("sole" in low or "only" in low)):
        hold(f"{name} does not acknowledge Card 04 sentence 1 as the sole canonical delta")
    if not ("initialism" in low or "shorthand" in low):
        hold(f"{name} does not acknowledge the initialism/shorthand audit")
    if not ("reveal" in low and ("timing" in low or "constraint" in low or "synchron" in low)):
        hold(f"{name} does not acknowledge render reveal constraints")

print("PASS_V9_TIGHT_THREE_SEAT_EXACT_HASH_GATE_LOCAL_RENDER_AUTHORIZED")
print("SCOPE: LOCAL_ONLY_NO_PAID_GENERATION_NO_UPLOAD_NO_PUBLICATION_NO_ACCEPTANCE")
sys.exit(0)
