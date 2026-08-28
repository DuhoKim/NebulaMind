#!/usr/bin/env python3
"""Fail-closed preflight for the BHU closure video artifacts.

This does not render. It verifies exact review hashes, source boundaries, script /
storyboard synchronization, structure, and later the presence of three exact-hash
PASS verdicts. The reviewer verdict filenames are intentionally explicit.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

D = Path(__file__).resolve().parent
H = D.parent
EXPECTED = {
    "NARRATION_DRAFT_V7.md": "3380497f0514e906db8463d0fdd2ffd1f0b02b37ac6825e3bfdec86011c2edc0",
    "STORYBOARD_DRAFT_V7.json": "3077f0636385487bb4092d2032c18bbedaedb647780bbfc581e59027c87a8d2b",
    "CLAIM_LINE_LEDGER_V7.md": "871a808c4f2af94e24ef68b19cef416b7f7e3295720dab25ef8676753c845b5a",
    "AUTHORITY_AND_SAFETY.md": "1b0b0df612fdfdf9d1f41d08942bd2999dae0d6e063b73bda1a086ad6278ac64",
}
PACKET = H / "reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md"
PACKET_SHA = "b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516"
REQUIRED_REVIEW_PREFIXES = {
    "LANA": "PASS",
    "GORU": "PASS",
    "KUN": "PASS",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message):
    print("HOLD:", message)
    raise SystemExit(2)


for name, expected in EXPECTED.items():
    path = D / name
    if not path.exists():
        fail(f"missing {name}")
    actual = sha(path)
    if actual != expected:
        fail(f"hash mismatch {name}: {actual} != {expected}")

if sha(PACKET) != PACKET_SHA:
    fail("sole authority packet hash mismatch")

sb = json.loads((D / "STORYBOARD_DRAFT_V7.json").read_text())
if len(sb.get("cards", [])) != 11:
    fail("storyboard is not 11 cards")
if any(not c.get("heading") for c in sb["cards"]):
    fail("missing assertion heading")
if any(c.get("kind") == "divider" for c in sb["cards"]):
    fail("divider card present")
if sb["cards"][0].get("planned_seconds", 999) > 35:
    fail("opening misses 35-second contract")
if sb.get("paid_generation_notes"):
    fail("paid generation note/request present")

text = (D / "NARRATION_DRAFT_V7.md").read_text()
parts = re.split(r"## Card (\d+) — assertion heading\n", text)[1:]
seen = {}
for i in range(0, len(parts), 2):
    cid = parts[i]
    block = parts[i + 1]
    narration = block.split("**", 2)[2].split("\n\nSource:", 1)[0].strip()
    seen[cid] = narration
for card in sb["cards"]:
    if seen.get(card["id"]) != card["narration"]:
        fail(f"narration/storyboard divergence on card {card['id']}")

public_surface = " ".join(
    [sb.get("title", "")]
    + [c["heading"] + " " + c["narration"] + " " + " ".join(c["on_screen_support"])
       for c in sb["cards"]]
).lower()
for forbidden in (
    "our sky test", "1.95", "one point nine five", "other rotating cosmologies",
    "other theories of a rotating universe", "generic effect of rotation", "bhu is true",
    "bhu is false", "definitively falsified", "bhu is supported", "untestable in principle",
):
    if forbidden in public_surface:
        fail(f"forbidden public phrase present: {forbidden}")

# Reviews can live here or in the root reviews directory. Each must name all
# three exact target hashes and start its verdict with PASS, not PASS WITH REPAIRS.
review_dirs = [D, D / "reviews", H / "reviews"]
all_md = []
for rd in review_dirs:
    if rd.exists():
        all_md += list(rd.glob("*.md"))
for seat, required in REQUIRED_REVIEW_PREFIXES.items():
    candidates = []
    for p in all_md:
        upper = p.name.upper()
        if seat not in upper or not any(x in upper for x in ("REREVIEW", "REVIEW", "REGATE", "GATE", "PASS", "FINAL")):
            continue
        blob = p.read_text(errors="replace")
        mandatory_hashes = (
            EXPECTED["NARRATION_DRAFT_V7.md"],
            EXPECTED["STORYBOARD_DRAFT_V7.json"],
        )
        if not all(h in blob for h in mandatory_hashes):
            continue
        ledger_hash = EXPECTED["CLAIM_LINE_LEDGER_V7.md"]
        ledger_bound = ledger_hash in blob
        if not ledger_bound and "byte-identical" in blob.lower():
            # Goru's final V7 report names the carried V5 ledger as byte-identical
            # rather than repeating its hash. Accept that only after proving the
            # V5 and V7 bytes are identical on disk; no prose-only inference.
            prior = D / "CLAIM_LINE_LEDGER_V5.md"
            ledger_bound = (
                "CLAIM_LINE_LEDGER_V5.md" in blob
                and prior.exists()
                and sha(prior) == ledger_hash
                and sha(D / "CLAIM_LINE_LEDGER_V7.md") == ledger_hash
            )
        if not ledger_bound:
            continue
        candidates.append((p, blob))
    if not candidates:
        fail(f"no exact-hash {seat} V7 verdict")
    passing = []
    for p, blob in candidates:
        verdict_lines = [line.strip() for line in blob.splitlines() if "VERDICT" in line.upper() or line.strip().upper().startswith("PASS")]
        joined = " ".join(verdict_lines).upper()
        if "PASS" in joined and "PASS WITH REPAIRS" not in joined and "HOLD" not in joined:
            passing.append(p)
    if not passing:
        fail(f"{seat} exact-hash verdict is not unconditional PASS")
    print(f"{seat}_PASS:", passing[-1])

print("PASS_ALL_THREE_EXACT_HASH_SCRIPT_STORYBOARD_GATES")
