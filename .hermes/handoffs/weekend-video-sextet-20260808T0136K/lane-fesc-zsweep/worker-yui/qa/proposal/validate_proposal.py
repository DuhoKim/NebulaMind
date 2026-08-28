#!/usr/bin/env python3
"""Machine-check the review-only FESC storyboard and v2 static proposal."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from PIL import Image

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind")
WORKER = ROOT / ".hermes/handoffs/weekend-video-sextet-20260808T0136K/lane-fesc-zsweep/worker-yui"
STORYBOARD = WORKER / "STORYBOARD_PROPOSAL.json"
MANIFEST = WORKER / "visual_proposal_v4/manifest.json"
SOURCE = ROOT / ".hermes/handoffs/fesc-zsweep-merged-paper-20260804T1040K/TREND_RESULTS.json"
OUTPUT = WORKER / "qa/proposal/machine_validation.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def check(condition: bool, name: str, detail: str, checks: list[dict]) -> None:
    checks.append({"name": name, "pass": bool(condition), "detail": detail})


def main() -> None:
    storyboard = json.loads(STORYBOARD.read_text())
    manifest = json.loads(MANIFEST.read_text())
    source = json.loads(SOURCE.read_text())
    scenes = storyboard["scenes"]
    checks: list[dict] = []

    source_hash = sha256(SOURCE)
    check(source_hash == storyboard["asset_contract"]["numeric_source_sha256"], "storyboard_source_hash", source_hash, checks)
    check(source_hash == manifest["source_sha256"], "manifest_source_hash", source_hash, checks)

    timeline_ok = scenes[0]["start_seconds"] == 0 and scenes[-1]["end_seconds"] == storyboard["duration_seconds"]
    timeline_ok = timeline_ok and all(
        scene["end_seconds"] - scene["start_seconds"] == scene["duration_seconds"]
        for scene in scenes
    )
    timeline_ok = timeline_ok and all(
        scenes[index]["start_seconds"] == scenes[index - 1]["end_seconds"]
        for index in range(1, len(scenes))
    )
    check(timeline_ok, "continuous_timeline", f"0-{storyboard['duration_seconds']} s across {len(scenes)} scenes", checks)

    word_metrics = []
    for scene in scenes:
        words = re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", scene["narration_proposal"])
        wpm = len(words) * 60 / scene["duration_seconds"]
        word_metrics.append({"scene_id": scene["scene_id"], "words": len(words), "wpm": round(wpm, 1)})
    delivered_words = sum(item["words"] for item in word_metrics)
    delivered_wpm = delivered_words * 60 / storyboard["duration_seconds"]
    check(all(100 <= item["wpm"] <= 130 for item in word_metrics), "per_scene_narration_pacing", json.dumps(word_metrics), checks)
    check(105 <= delivered_wpm <= 125, "delivered_narration_pacing", f"{delivered_words} words; {delivered_wpm:.1f} WPM", checks)

    check(all(scene.get("visual_action") for scene in scenes), "visual_action_each_scene", "all scenes", checks)
    check(all(scene.get("source_anchors") for scene in scenes), "source_anchor_each_scene", "all scenes", checks)
    check(all(scene.get("forbidden_implication") for scene in scenes), "forbidden_implication_each_scene", "all scenes", checks)

    rendered_copy = "\n".join("\n".join(scene["on_screen_copy"]) for scene in scenes)
    forbidden_copy = ["where the two curves cross", "every assumption is set against", "part company", ".hermes/", "/Users/", "TREND_RESULTS.json"]
    present_forbidden = [phrase for phrase in forbidden_copy if phrase.lower() in rendered_copy.lower()]
    check(not present_forbidden, "no_stale_or_internal_audience_copy", json.dumps(present_forbidden), checks)
    for key in ("66% @ z=7", "83% @ z=8", "93% @ z=9"):
        check(key in rendered_copy, f"keyed_shortfall_{key[:2]}", key, checks)

    closure = source["closure_crossing_fiducial"]
    median = source["median_crossing_fiducial"]
    no_tail = source["corner_boost_none"]
    check(abs(closure["z_c"] - 8.045284271240234) < 1e-15, "fiducial_zc_exact", repr(closure["z_c"]), checks)
    check(abs(median["z_m"] - 6.327877044677734) < 1e-15, "median_zm_exact", repr(median["z_m"]), checks)
    check(abs(no_tail["closure_crossing_z_c"] - 7.615345001220703) < 1e-15, "no_tail_zc_exact", repr(no_tail["closure_crossing_z_c"]), checks)
    keyed = {row["z"]: row["frac_shortfall"] for row in source["grid_fiducial"]}
    check(round(100 * keyed[7.0]) == 66 and round(100 * keyed[8.0]) == 83 and round(100 * keyed[9.0]) == 93, "keyed_shortfalls_exact", json.dumps({"7": keyed[7.0], "8": keyed[8.0], "9": keyed[9.0]}), checks)
    check(all(a <= b for a, b in zip([row["frac_shortfall"] for row in source["grid_fiducial"]], [row["frac_shortfall"] for row in source["grid_fiducial"]][1:])), "shortfall_monotone", "z=6..10 grid", checks)

    image_checks = []
    for state in manifest["states"]:
        path = Path(state["path"])
        exists = path.exists()
        digest = sha256(path) if exists else None
        dimensions = None
        if exists:
            with Image.open(path) as image:
                dimensions = list(image.size)
        image_checks.append({"path": str(path), "exists": exists, "sha256_match": digest == state["sha256"], "dimensions": dimensions})
    check(len(image_checks) == 8, "state_count", str(len(image_checks)), checks)
    check(all(item["exists"] and item["sha256_match"] and item["dimensions"] == [1920, 1080] for item in image_checks), "state_integrity_and_dimensions", json.dumps(image_checks), checks)
    check(manifest["packet_type"] == "STATIC_REVIEW_PROPOSAL__NOT_CANDIDATE", "proposal_not_candidate", manifest["packet_type"], checks)
    check(manifest["audio"] == "none; static proposal only" and manifest["mp4"] == "not produced", "no_audio_or_mp4", f"audio={manifest['audio']}; mp4={manifest['mp4']}", checks)

    failures = [item for item in checks if not item["pass"]]
    report = {
        "verdict": "PASS" if not failures else "FAIL",
        "checks_total": len(checks),
        "checks_passed": len(checks) - len(failures),
        "checks_failed": len(failures),
        "checks": checks,
        "word_metrics": word_metrics,
        "image_checks": image_checks,
        "manual_full_resolution_review_required": [
            "S04 crossing geometry and rail clipping",
            "S05 keyed percentages",
            "S06 no-tail versus fiducial distinction",
            "S07 model boundary",
            "S08 closing scientific summary"
        ]
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ("verdict", "checks_total", "checks_passed", "checks_failed")}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
