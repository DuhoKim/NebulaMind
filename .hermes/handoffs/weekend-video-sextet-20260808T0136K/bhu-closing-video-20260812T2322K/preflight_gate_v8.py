#!/usr/bin/env python3
"""Fail-closed full three-seat exact-hash preflight for BHU V8.

No tight-delta carry-forward is accepted. This script returns HOLD until Lana,
Goru, and Kun each issue an unconditional verdict binding all V8 target hashes.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

D = Path(__file__).resolve().parent
H = D.parent
EXPECTED_FILE = D / "V8_EXPECTED_HASHES.json"
PACKET = H / "reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md"
PACKET_SHA = "b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516"
SEATS = ("LANA", "GORU", "KUN")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message: str) -> None:
    print("HOLD:", message)
    raise SystemExit(2)


if not EXPECTED_FILE.exists():
    fail("V8 expected-hash freeze file absent")
expected = json.loads(EXPECTED_FILE.read_text())
for name, digest in expected["review_targets"].items():
    path = D / name
    if not path.exists():
        fail(f"missing review target {name}")
    if sha(path) != digest:
        fail(f"review target hash drift {name}")
if not PACKET.exists() or sha(PACKET) != PACKET_SHA:
    fail("sole authority packet hash drift")

# Re-run semantic build verification. It must not mutate any target.
import subprocess, sys
p = subprocess.run([sys.executable, str(D / "verify_v8_build.py")], cwd=D, capture_output=True, text=True)
if p.returncode:
    fail("V8 semantic verification failed: " + (p.stdout + p.stderr)[-1000:])
for name, digest in expected["review_targets"].items():
    if sha(D / name) != digest:
        fail(f"target changed during verification: {name}")

review_dirs = [D, D / "reviews", H / "reviews"]
all_md: list[Path] = []
for rd in review_dirs:
    if rd.exists():
        all_md.extend(rd.glob("*.md"))
mandatory_hashes = tuple(expected["review_targets"].values())
for seat in SEATS:
    candidates: list[tuple[Path, str]] = []
    for path in all_md:
        upper = path.name.upper()
        if seat not in upper or "V8" not in upper:
            continue
        if not any(token in upper for token in ("REVIEW", "REGATE", "GATE", "PASS", "FINAL")):
            continue
        blob = path.read_text(errors="replace")
        if all(digest in blob for digest in mandatory_hashes):
            candidates.append((path, blob))
    if not candidates:
        fail(f"no full exact-hash {seat} V8 verdict")
    passing: list[Path] = []
    for path, blob in candidates:
        verdict_lines = [
            line.strip() for line in blob.splitlines()
            if "VERDICT" in line.upper() or line.strip().upper().startswith("PASS")
        ]
        verdict = " ".join(verdict_lines).upper()
        if "PASS" in verdict and "PASS WITH REPAIRS" not in verdict and "HOLD" not in verdict:
            passing.append(path)
    if not passing:
        fail(f"{seat} V8 exact-hash verdict is not unconditional PASS")
    print(f"{seat}_V8_PASS:", passing[-1])

print("PASS_V8_FULL_THREE_SEAT_EXACT_HASH_GATE_RENDER_AUTHORIZED")
