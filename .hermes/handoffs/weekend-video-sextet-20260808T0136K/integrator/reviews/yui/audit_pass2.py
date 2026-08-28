#!/usr/bin/env python3
"""Pass-2 machine QA on the latest isolated canary (spin-method-canary-20260808T0204).

Read-only against the canary; writes evidence only beneath this review lane's qa/.
Reuses audit_encoded.audit() so pass-2 metrics are comparable with pass-1 targets,
then adds the checks specific to this canary's contract:
  - silence: exactly one stream, video, no audio track to un-mute;
  - integrity: file sha256 equals the sha recorded in the canary's own hashes.txt;
  - structure: detected scene cuts vs the storyboard's cumulative card boundaries
    (the concat demuxer repeats the final entry, so total = storyboard sum + one
    extra hold of the close card).
"""
from __future__ import annotations

import json
from pathlib import Path

import audit_encoded

HERE = Path(__file__).resolve().parent
CANARY = HERE.parent.parent / "canaries" / "spin-method-canary-20260808T0204"
MP4 = CANARY / "spin-method-canary-20260808T0204.mp4"
STORYBOARD = CANARY / "storyboard_spin_method_canary.json"
HASHES = CANARY / "hashes.txt"
NAME = "canary-spin-method-0204"
CUT_TOL = 0.35  # seconds; scene detect reports the first changed frame


def recorded_sha() -> str | None:
    for line in HASHES.read_text().splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[1] == MP4.name:
            return parts[0]
    return None


def main() -> int:
    result = audit_encoded.audit(NAME, MP4)

    sb = json.loads(STORYBOARD.read_text())
    seconds = [float(c.get("seconds", 5)) for c in sb["cards"]]
    expected_cuts, acc = [], 0.0
    for s in seconds[:-1]:
        acc += s
        expected_cuts.append(acc)
    detected = result["detected_cut_times_seconds"]
    matches = []
    for exp in expected_cuts:
        near = min(detected, key=lambda d: abs(d - exp)) if detected else None
        matches.append({
            "expected": exp,
            "nearest_detected": near,
            "delta": (None if near is None else round(near - exp, 3)),
            "ok": near is not None and abs(near - exp) <= CUT_TOL,
        })
    unexpected = [d for d in detected
                  if all(abs(d - e) > CUT_TOL for e in expected_cuts)]

    checks = {
        "silence_video_stream_only": (
            len(result["streams"]) == 1
            and result["streams"][0]["codec_type"] == "video"
        ),
        "sha256_matches_canary_hashes_txt": result["sha256"] == recorded_sha(),
        "recorded_sha256": recorded_sha(),
        "storyboard_cards": len(seconds),
        "storyboard_sum_seconds": sum(seconds),
        "expected_interior_cuts": len(expected_cuts),
        "detected_interior_cuts": len(detected),
        "all_expected_cuts_detected": all(m["ok"] for m in matches),
        "cut_matches": matches,
        "unexpected_cuts": unexpected,
        "close_card_extra_hold_seconds": round(
            result["duration_seconds"] - sum(seconds), 3),
    }
    out = HERE / "qa" / NAME / "pass2_checks.json"
    out.write_text(json.dumps(checks, indent=2) + "\n")

    print(f"{NAME}: states={result['detected_state_count']} "
          f"duration={result['duration_seconds']:.3f}s "
          f"max_hold={result['max_static_hold_seconds']:.3f}s "
          f"sha256={result['sha256'][:16]}")
    for key in ("silence_video_stream_only", "sha256_matches_canary_hashes_txt",
                "all_expected_cuts_detected"):
        print(f"  {key}: {checks[key]}")
    print(f"  unexpected_cuts: {unexpected}")
    print(f"  close_card_extra_hold_seconds: {checks['close_card_extra_hold_seconds']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
