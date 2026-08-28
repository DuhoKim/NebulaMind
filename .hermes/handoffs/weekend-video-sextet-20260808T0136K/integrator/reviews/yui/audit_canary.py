#!/usr/bin/env python3
"""Parameterized canary QA runner: audit_canary.py <canary-dir>.

Generalizes audit_pass2.py (which is pinned to the 0204 canary) so each new
isolated canary gets identical machine QA without editing the harness. Expects
the canary dir to contain exactly one .mp4, one storyboard_*.json, and a
hashes.txt whose entry for the .mp4 is the integrity reference. Writes evidence
beneath reviews/yui/qa/<canary-dir-name>/ and appends the result to the
ENCODED_AUDIT.json aggregate (idempotent by name).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import audit_encoded

HERE = Path(__file__).resolve().parent
CUT_TOL = 0.35


def main() -> int:
    canary = Path(sys.argv[1]).resolve()
    mp4s = sorted(canary.glob("*.mp4"))
    boards = sorted(canary.glob("storyboard_*.json"))
    if len(mp4s) != 1 or len(boards) != 1:
        print(f"expected exactly one mp4 and one storyboard in {canary}")
        return 2
    mp4, board = mp4s[0], boards[0]
    name = canary.name

    recorded = None
    hashes = canary / "hashes.txt"
    if hashes.exists():
        for line in hashes.read_text().splitlines():
            parts = line.split()
            if len(parts) == 2 and parts[1] == mp4.name:
                recorded = parts[0]

    result = audit_encoded.audit(name, mp4)

    seconds = [float(c.get("seconds", 5)) for c in json.loads(board.read_text())["cards"]]
    expected_cuts, acc = [], 0.0
    for s in seconds[:-1]:
        acc += s
        expected_cuts.append(acc)
    detected = result["detected_cut_times_seconds"]
    matches = [{
        "expected": e,
        "nearest_detected": (min(detected, key=lambda d: abs(d - e)) if detected else None),
        "ok": bool(detected) and abs(min(detected, key=lambda d: abs(d - e)) - e) <= CUT_TOL,
    } for e in expected_cuts]
    unexpected = [d for d in detected if all(abs(d - e) > CUT_TOL for e in expected_cuts)]

    checks = {
        "silence_video_stream_only": (len(result["streams"]) == 1
                                      and result["streams"][0]["codec_type"] == "video"),
        "sha256_matches_canary_hashes_txt": (recorded is not None
                                             and result["sha256"] == recorded),
        "recorded_sha256": recorded,
        "storyboard_cards": len(seconds),
        "storyboard_sum_seconds": sum(seconds),
        "expected_interior_cuts": len(expected_cuts),
        "detected_interior_cuts": len(detected),
        "all_expected_cuts_detected": all(m["ok"] for m in matches),
        "cut_matches": matches,
        "unexpected_cuts": unexpected,
        "close_card_extra_hold_seconds": round(result["duration_seconds"] - sum(seconds), 3),
    }
    (HERE / "qa" / name / "canary_checks.json").write_text(
        json.dumps(checks, indent=2) + "\n")

    agg_path = HERE / "qa" / "ENCODED_AUDIT.json"
    agg = json.loads(agg_path.read_text())
    if name not in [t["name"] for t in agg["targets"]]:
        agg["targets"].append(result)
        agg_path.write_text(json.dumps(agg, indent=2) + "\n")

    print(f"{name}: states={result['detected_state_count']} "
          f"duration={result['duration_seconds']:.3f}s sha256={result['sha256'][:16]}")
    for key in ("silence_video_stream_only", "sha256_matches_canary_hashes_txt",
                "all_expected_cuts_detected"):
        print(f"  {key}: {checks[key]}")
    print(f"  unexpected_cuts: {unexpected}")
    print(f"  close_card_extra_hold_seconds: {checks['close_card_extra_hold_seconds']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
