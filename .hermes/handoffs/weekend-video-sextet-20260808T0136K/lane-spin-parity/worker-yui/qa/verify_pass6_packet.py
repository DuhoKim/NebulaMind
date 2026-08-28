#!/usr/bin/env python3
"""Verify pass-6 multi-resolution evidence, representation guard, and custody."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "spin-parity-census-20260805T1922K"
)
CANDIDATE = Path(
    "/Users/duhokim/HermesOps/cockpit/videos/"
    "spin-parity-census-narrated-20260808T0149.mp4"
)
CANDIDATE_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
T4_SHA = "6e3480d4087b971d8331979a9d26926add7f9a600c5bfaa8e54da2b88e6e6873"
A38_SHA = "d2d494ddfe0c16524b65fc9e9b7e80d067ec06ceede5a14e384a9421707791b0"
KUN_SHA = "ccedf6846391a8f0661a88b2eec0ce21fbfd7c44ad16201080bb196f56d258e5"
RESOLUTIONS = {
    "1080p": (1920, 1080),
    "720p": (1280, 720),
    "540p": (960, 540),
    "360p": (640, 360),
}
AUDIT_ROOT = ROOT / "qa/pass6_resolution_audit"
V8_AUDIT_ROOT = ROOT / "qa/pass6_v8_legibility"
SNAPSHOT = ROOT / "qa/pass6_review_snapshot_v1.json"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(relative: str) -> Any:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def visible_strings(value: Any, key: str = "") -> list[str]:
    strings: list[str] = []
    if isinstance(value, dict):
        for child_key, child in value.items():
            if child_key in {"on_screen_copy", "display_citation"}:
                strings.extend(visible_strings(child, child_key))
            elif key in {"on_screen_copy", "display_citation"}:
                strings.extend(visible_strings(child, key))
    elif isinstance(value, list):
        for child in value:
            strings.extend(visible_strings(child, key))
    elif isinstance(value, str) and key in {"on_screen_copy", "display_citation"}:
        strings.append(value)
    return strings


def main() -> None:
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    require(snapshot["snapshot_status"] == "IMMUTABLE_REVIEW_SNAPSHOT", "snapshot status")
    require(
        snapshot["snapshot_id"] == "spin-worker-yui-pass6-review-v1-20260808T052446K",
        "snapshot id",
    )
    require(snapshot["supersedes"]["path"] == "qa/pass5_review_snapshot_v1.json", "supersession path")
    require(
        sha256(ROOT / snapshot["supersedes"]["path"])
        == snapshot["supersedes"]["sha256"],
        "superseded snapshot hash",
    )
    for artifact in snapshot["pinned_artifacts"]:
        path = ROOT / artifact["path"]
        require(path.is_file(), f"missing pinned artifact {artifact['path']}")
        require(sha256(path) == artifact["sha256"], f"hash {artifact['path']}")

    require(sha256(CANDIDATE) == CANDIDATE_SHA, "candidate closing hash")
    receipt = load_json("qa/pass6_resolution_audit/extraction_receipt.json")
    require(receipt["deepening_pass"] == 6, "extraction pass")
    require(receipt["candidate_sha256"] == CANDIDATE_SHA, "receipt candidate")
    require(receipt["candidate_hash_match"] is True, "candidate hash match")
    require(receipt["candidate_modified"] is False, "candidate modified")
    require(receipt["scene_count"] == 16, "scene count")
    require(receipt["frame_count"] == 64, "frame count")
    require(receipt["resolution_count"] == 4, "resolution count")
    require(
        {row["label"]: (row["width"], row["height"]) for row in receipt["resolutions"]}
        == RESOLUTIONS,
        "resolution matrix",
    )
    pass4 = load_json("qa/pass4_encoded_audit/extraction_receipt.json")
    require(receipt["detected_cut_times_seconds"] == pass4["detected_cut_times_seconds"], "cut replay")

    pass4_mid = {
        int(scene["scene"]): next(
            sample["frame_sha256"]
            for sample in scene["samples"]
            if sample["sample"] == "mid"
        )
        for scene in pass4["scenes"]
    }
    frame_hashes = []
    native_matches = 0
    for expected_scene, scene in enumerate(receipt["scenes"], start=1):
        require(scene["scene"] == expected_scene, f"scene order {expected_scene}")
        require(len(scene["samples"]) == 4, f"sample count scene {expected_scene}")
        require(
            [sample["resolution"] for sample in scene["samples"]]
            == list(RESOLUTIONS),
            f"resolution order scene {expected_scene}",
        )
        for sample in scene["samples"]:
            width, height = RESOLUTIONS[sample["resolution"]]
            require(sample["width"] == width and sample["height"] == height, f"declared size {sample['frame']}")
            frame = AUDIT_ROOT / sample["frame"]
            require(frame.is_file(), f"missing frame {sample['frame']}")
            actual = sha256(frame)
            require(actual == sample["frame_sha256"], f"frame hash {sample['frame']}")
            frame_hashes.append(actual)
            with Image.open(frame) as image:
                require(image.mode == "RGB", f"frame mode {sample['frame']}")
                require(image.size == (width, height), f"frame size {sample['frame']}")
            if sample["resolution"] == "1080p":
                native_matches += actual == pass4_mid[expected_scene]
    require(len(frame_hashes) == 64 and len(set(frame_hashes)) == 64, "frame hash census")
    require(native_matches == 16, "native midpoint reproduction")
    expected_sheet_hashes = snapshot["pass6_encoded_evidence"]["contact_sheet_sha256"]
    for label, sheet in receipt["contact_sheets"].items():
        require(sheet["sha256"] == expected_sheet_hashes[label], f"snapshot sheet {label}")
        require(sha256(AUDIT_ROOT / sheet["path"]) == sheet["sha256"], f"contact sheet {label}")

    ocr = load_json("qa/pass6_multires_ocr_audit.json")
    require(ocr["scene_count"] == 16 and ocr["frame_count"] == 64, "OCR census")
    require(ocr["resolutions"] == list(RESOLUTIONS), "OCR resolutions")
    require(ocr["ocr"]["raw_ocr_text_stored"] is False, "raw OCR custody")
    expected_aggregates = {
        "1080p": (1.0, 1.0, 1.0, 0),
        "720p": (0.942152, 0.9975, 0.897305, 0),
        "540p": (0.840371, 0.97751, 0.702634, 0),
        "360p": (0.728766, 0.961206, 0.230643, 0),
    }
    for label, expected in expected_aggregates.items():
        row = ocr["aggregates"][label]
        actual = (
            row["mean_full_token_retention_vs_1080p"],
            row["mean_headline_token_retention_vs_1080p"],
            row["mean_support_token_retention_vs_1080p"],
            row["scenes_with_any_structural_gate"],
        )
        require(actual == expected, f"OCR aggregate {label}")
    critical = ocr["critical_resolution_metrics"]["360p"]
    require(critical["scenes"] == [7, 9, 10, 11, 16], "critical scenes")
    require(critical["mean_full_token_retention_vs_1080p"] == 0.380218, "critical full retention")
    require(critical["mean_headline_token_retention_vs_1080p"] == 0.90313, "critical headline retention")
    require(critical["mean_support_token_retention_vs_1080p"] == 0.416629, "critical support retention")
    require(critical["structural_gate_scene_count"] == 0, "critical gate count")
    require(
        ocr["aggregates"]["360p"]["mean_headline_token_retention_vs_1080p"]
        > ocr["aggregates"]["360p"]["mean_support_token_retention_vs_1080p"],
        "hierarchy direction",
    )

    v8_audit = load_json("qa/pass6_v8_legibility_audit.json")
    require(v8_audit["sealed_v8_modified"] is False, "v8 modified flag")
    require(v8_audit["resolution_order"] == list(RESOLUTIONS), "v8 resolution order")
    require(len(v8_audit["scenes"]) == 7, "v8 scene count")
    for scene in v8_audit["scenes"]:
        require(len(scene["samples"]) == 4, f"v8 samples scene {scene['scene']}")
        sealed = ROOT / "proposal_frames/v8" / scene["sealed_input"]
        require(sha256(sealed) == scene["sealed_input_sha256"], f"sealed v8 hash scene {scene['scene']}")
        for sample in scene["samples"]:
            width, height = RESOLUTIONS[sample["resolution"]]
            frame = V8_AUDIT_ROOT / sample["frame"]
            require(sha256(frame) == sample["frame_sha256"], f"v8 derivative hash {sample['frame']}")
            with Image.open(frame) as image:
                require(image.size == (width, height), f"v8 derivative size {sample['frame']}")
    for label in RESOLUTIONS:
        aggregate = v8_audit["aggregates"][label]
        require(aggregate["result_held_badge_detected"] == 5, f"v8 badge OCR {label}")
        require(aggregate["scene_count"] == 7, f"v8 aggregate count {label}")
        sheet = v8_audit["contact_sheets"][label]
        require(sha256(V8_AUDIT_ROOT / sheet["path"]) == sheet["sha256"], f"v8 sheet {label}")

    guard = load_json("LOW_RESOLUTION_REPRESENTATION_GUARD_PASS6.json")
    require(guard["changes_sealed_v8_bytes"] is False, "guard v8 custody")
    require(guard["authorizes_render_or_narration"] is False, "guard authorization")
    require(guard["acceptance_tests"]["seven_of_seven_360p_frames_visually_show_result_held"] is True, "visual badge acceptance")
    require(guard["acceptance_tests"]["human_visual_review_required"] is True, "human visual gate")
    require(guard["acceptance_tests"]["ocr_is_not_sole_gate"] is True, "OCR auxiliary gate")

    packet = load_json("BLOCKER_PACKET_PASS6.json")
    require(packet["video_reportable_now"] is False, "packet reportability")
    require(packet["candidate"]["sha256"] == CANDIDATE_SHA, "packet candidate")
    require(packet["sealed_v8_disposition"]["v9_warranted"] is False, "v9 disposition")
    packet_text = json.dumps(packet, sort_keys=True)
    for raw_result_field in (
        "primary_pairs_read",
        "control_pairs_reported_never_read",
        '"cells"',
        '"reading"',
        '"reading_why"',
    ):
        require(raw_result_field not in packet_text, f"raw result field leaked: {raw_result_field}")

    require(sha256(SOURCE / "T4_PAIRED_FLIP.json") == T4_SHA, "T4 source hash")
    require(sha256(SOURCE / "AMENDMENT_A3.8_DRAFT.md") == A38_SHA, "A3.8 contract hash")
    frame_review = SOURCE / "KUN_FRAME_REVIEW.md"
    require(sha256(frame_review) == KUN_SHA, "frame review hash")
    require(frame_review.read_text(encoding="utf-8").rstrip().endswith("FRAME REVIEW: AGREES FRAME_UNSTATED"), "frame review status")

    storyboard = load_json("STORYBOARD_PROPOSAL.json")
    visible = "\n".join(visible_strings(storyboard))
    for forbidden in (r"cosmolog", r"\bdipole\b", r"\bparity\b", r"\bH0\b", r"black[- ]hole"):
        require(not re.search(forbidden, visible, re.IGNORECASE), f"visible forbidden term {forbidden}")
    for internal in ("T1", "T1C", "T3", "T4", "Hwao", "/Users/"):
        require(internal not in visible, f"visible internal token {internal}")
    render_receipt = load_json("proposal_frames/v8/render_receipt.json")
    require(render_receipt["storyboard_sha256"] == sha256(ROOT / "STORYBOARD_PROPOSAL.json"), "v8 storyboard pin")
    require(render_receipt["lane_renderer_sha256"] == sha256(ROOT / "render_proposal_frames.py"), "v8 renderer pin")
    require(render_receipt["scenes"] == 7 and len(render_receipt["outputs"]) == 7, "v8 output count")
    static_validation = load_json("qa/static_proposal_validation.json")
    require(static_validation["verdict"] == "PASS", "v8 static validation")
    require(static_validation["visible_forbidden_or_internal_hits"] == 0, "v8 visible boundary")

    extraction_time = parse_time(receipt["extracted_at_utc"])
    packet_time = parse_time(packet["checked_at"])
    snapshot_time = parse_time(snapshot["created_at"])
    require(extraction_time < packet_time < snapshot_time, "pass6 chronology")

    status = load_json("STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS6_V1", "status phase")
    require(status["video_reportable_now"] is False, "status reportability")
    receipt_text = (ROOT / "LANE_RECEIPT.md").read_text(encoding="utf-8")
    require("SPIN_WORKER_YUI_DEEPENING_PASS6_COMPLETE" in receipt_text, "receipt marker")
    require(snapshot["snapshot_id"] in receipt_text, "receipt snapshot pin")
    integrator = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(encoding="utf-8")
    require(snapshot["snapshot_id"] in integrator, "integrator snapshot pin")
    require("360p" in integrator and "headline-scale" in integrator, "integrator low-resolution guard")

    media = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.casefold()
        in {".mp4", ".mp3", ".wav", ".aac", ".m4a", ".mov", ".webm"}
    ]
    require(not media, f"worker media outputs present: {media}")
    print(
        "PASS pass6 snapshot/candidate/64-multires-frames/hierarchy/"
        "v8-360p/source-blockers/status/no-media"
    )


if __name__ == "__main__":
    main()
