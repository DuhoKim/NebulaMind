#!/usr/bin/env python3
"""Verify pass-7 obstruction evidence, caption-safe correction, and custody."""

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
AUDIT_ROOT = ROOT / "qa/pass7_obstruction_audit"
V8_AUDIT_ROOT = ROOT / "qa/pass7_v8_obstruction"
MOCKUP_ROOT = ROOT / "qa/pass7_caption_safe_mockup"
SNAPSHOT = ROOT / "qa/pass7_review_snapshot_v1.json"
VARIANTS = ["clean", "caption_15pct", "player_ui_25pct"]
EXPECTED_GATE_LINES = {
    1: "RESULT LOCKED · ARCHIVE FRAME + INDEPENDENT REVIEW REQUIRED",
    2: "OVERLAPPING READOUTS · DO NOT SUM",
    3: "LABEL-FRAME STATISTIC · PHYSICAL INTERPRETATION HELD",
    4: "FRAME UNSTATED · RESULT HELD",
    5: "COLUMN CHECK ONLY · STORAGE FRAME UNRESOLVED",
    6: "CONTROL DESIGN ONLY · OUTCOMES WITHHELD",
    7: "SEPARATE AUTHORIZATION REQUIRED AFTER BOTH BLOCKERS RESOLVE",
}


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


def crop_hash(path: Path, bottom: int) -> str:
    with Image.open(path).convert("RGB") as image:
        return hashlib.sha256(image.crop((0, 0, image.width, bottom)).tobytes()).hexdigest()


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
        snapshot["snapshot_id"] == "spin-worker-yui-pass7-review-v1-20260808T054919K",
        "snapshot id",
    )
    require(snapshot["supersedes"]["path"] == "qa/pass6_review_snapshot_v1.json", "supersession path")
    require(
        sha256(ROOT / snapshot["supersedes"]["path"]) == snapshot["supersedes"]["sha256"],
        "superseded snapshot hash",
    )
    for artifact in snapshot["pinned_artifacts"]:
        path = ROOT / artifact["path"]
        require(path.is_file(), f"missing pinned artifact {artifact['path']}")
        require(sha256(path) == artifact["sha256"], f"hash {artifact['path']}")

    require(sha256(CANDIDATE) == CANDIDATE_SHA, "candidate closing hash")
    receipt = load_json("qa/pass7_obstruction_audit/extraction_receipt.json")
    require(receipt["deepening_pass"] == 7, "extraction pass")
    require(receipt["candidate_sha256"] == CANDIDATE_SHA, "receipt candidate")
    require(receipt["candidate_hash_match"] is True, "candidate hash match")
    require(receipt["candidate_modified"] is False, "candidate modified")
    require(receipt["detected_cut_count"] == 15, "cut count")
    require(receipt["scene_count"] == 16, "scene count")
    require(receipt["variant_count"] == 3 and receipt["frame_count"] == 48, "variant frame census")
    require([row["label"] for row in receipt["variants"]] == VARIANTS, "variant order")
    pass6 = load_json("qa/pass6_resolution_audit/extraction_receipt.json")
    require(receipt["detected_cut_times_seconds"] == pass6["detected_cut_times_seconds"], "fresh cut reproduction")
    pass6_clean = {
        int(scene["scene"]): next(
            sample["frame_sha256"]
            for sample in scene["samples"]
            if sample["resolution"] == "1080p"
        )
        for scene in pass6["scenes"]
    }

    frame_hashes: list[str] = []
    clean_matches = 0
    top_identity = {"caption_15pct": 0, "player_ui_25pct": 0}
    for expected_scene, scene in enumerate(receipt["scenes"], start=1):
        require(scene["scene"] == expected_scene, f"scene order {expected_scene}")
        require([sample["variant"] for sample in scene["samples"]] == VARIANTS, f"scene variants {expected_scene}")
        sample_map = {sample["variant"]: sample for sample in scene["samples"]}
        clean = AUDIT_ROOT / sample_map["clean"]["frame"]
        clean_matches += sha256(clean) == pass6_clean[expected_scene]
        for variant, sample in sample_map.items():
            frame = AUDIT_ROOT / sample["frame"]
            require(frame.is_file(), f"missing frame {sample['frame']}")
            actual = sha256(frame)
            require(actual == sample["frame_sha256"], f"frame hash {sample['frame']}")
            frame_hashes.append(actual)
            with Image.open(frame) as image:
                require(image.mode == "RGB", f"frame mode {sample['frame']}")
                require(image.size == (1920, 1080), f"frame size {sample['frame']}")
            if variant != "clean":
                bottom = int(sample["mask_start_y"])
                top_identity[variant] += crop_hash(frame, bottom) == crop_hash(clean, bottom)
    require(clean_matches == 16, "clean midpoint reproduction")
    require(len(frame_hashes) == 48 and len(set(frame_hashes)) == 48, "frame hash census")
    require(top_identity == {"caption_15pct": 16, "player_ui_25pct": 16}, "unobstructed pixel identity")
    for label, expected_hash in snapshot["pass7_encoded_evidence"]["contact_sheet_sha256"].items():
        sheet = receipt["contact_sheets"][label]
        require(sheet["sha256"] == expected_hash, f"snapshot sheet {label}")
        require(sha256(AUDIT_ROOT / sheet["path"]) == expected_hash, f"sheet hash {label}")

    ocr = load_json("qa/pass7_obstruction_ocr_audit.json")
    require(ocr["scene_count"] == 16 and ocr["frame_count"] == 48, "OCR census")
    require(ocr["variant_order"] == VARIANTS, "OCR variants")
    require(ocr["ocr"]["raw_ocr_text_stored"] is False, "raw OCR custody")
    expected_aggregates = {
        "clean": (1.0, 1.0, 1.0, 0, 16),
        "caption_15pct": (0.866911, 0.96625, 0.295149, 0, 16),
        "player_ui_25pct": (0.756673, 0.946477, 0.164207, 0, 16),
    }
    for label, expected in expected_aggregates.items():
        row = ocr["aggregates"][label]
        actual = (
            row["mean_full_token_retention_vs_clean"],
            row["mean_headline_token_retention_vs_clean"],
            row["mean_lower_support_token_retention_vs_clean"],
            row["scenes_with_any_structural_gate"],
            row["scenes_with_top_region_pixel_identity"],
        )
        require(actual == expected, f"OCR aggregate {label}")
    require(
        ocr["obstruction_zone_loss"]["caption_15pct"]
        == {
            "region": "bottom_15pct",
            "scenes_with_reference_copy": 14,
            "reference_token_count": 161,
            "surviving_token_count": 0,
            "scenes_with_zero_token_retention": 14,
        },
        "caption zone loss",
    )
    require(
        ocr["obstruction_zone_loss"]["player_ui_25pct"]
        == {
            "region": "bottom_25pct",
            "scenes_with_reference_copy": 14,
            "reference_token_count": 335,
            "surviving_token_count": 0,
            "scenes_with_zero_token_retention": 14,
        },
        "player zone loss",
    )
    critical = ocr["critical_scene_metrics"]["player_ui_25pct"]
    require(critical["scenes"] == [7, 9, 10, 11, 16], "critical scenes")
    require(critical["mean_full_token_retention_vs_clean"] == 0.454035, "critical full retention")
    require(critical["mean_headline_token_retention_vs_clean"] == 0.856, "critical headline retention")
    require(critical["mean_lower_support_token_retention_vs_clean"] == 0.325462, "critical lower retention")
    require(critical["structural_gate_scene_count"] == 0, "critical gate count")
    require(
        ocr["aggregates"]["player_ui_25pct"]["mean_headline_token_retention_vs_clean"]
        > ocr["aggregates"]["player_ui_25pct"]["mean_lower_support_token_retention_vs_clean"],
        "obstruction hierarchy direction",
    )

    v8 = load_json("qa/pass7_v8_obstruction_audit.json")
    require(v8["sealed_v8_modified"] is False, "v8 modified flag")
    require(v8["variant_order"] == VARIANTS and v8["frame_count"] == 21, "v8 census")
    for scene in v8["scenes"]:
        sealed = ROOT / "proposal_frames/v8" / scene["sealed_input"]
        require(sha256(sealed) == scene["sealed_input_sha256"], f"sealed input scene {scene['scene']}")
        require([sample["variant"] for sample in scene["samples"]] == VARIANTS, f"v8 variants scene {scene['scene']}")
        for sample in scene["samples"]:
            frame = V8_AUDIT_ROOT / sample["frame"]
            require(sha256(frame) == sample["frame_sha256"], f"v8 derivative {sample['frame']}")
            require(sample["top_region_pixel_identical_to_sealed"] is True, f"v8 top identity {sample['frame']}")
            with Image.open(frame) as image:
                require(image.size == (1920, 1080), f"v8 size {sample['frame']}")
    for variant in VARIANTS:
        aggregate = v8["aggregates"][variant]
        require(aggregate["scene_count"] == 7, f"v8 aggregate scene count {variant}")
        require(aggregate["result_held_badge_detected"] == 4, f"v8 auxiliary badge OCR {variant}")
        require(aggregate["top_region_pixel_identical_to_sealed"] == 7, f"v8 top identity aggregate {variant}")
        sheet = v8["contact_sheets"][variant]
        require(sha256(V8_AUDIT_ROOT / sheet["path"]) == sheet["sha256"], f"v8 sheet {variant}")
    require(
        v8["aggregates"]["clean"]["semantic_phrase_scene_counts"]["separate_authorization"] == 1
        and v8["aggregates"]["player_ui_25pct"]["semantic_phrase_scene_counts"]["separate_authorization"] == 0,
        "v8 separate-authorization loss",
    )

    correction = load_json("CAPTION_SAFE_STORYBOARD_CORRECTION_PASS7.json")
    require(correction["status"] == "PROPOSAL_ONLY_NOT_V9_NOT_A_CANDIDATE", "correction status")
    require(correction["base"]["sealed_v8_modified"] is False, "correction v8 custody")
    require(correction["qa_only_mockup"]["sealed_v8_modified"] is False, "mockup v8 custody")
    require(correction["qa_only_mockup"]["visual_review"] == "PASS_7/7_SCENE_SPECIFIC_LINES_AND_7/7_RESULT_HELD_BADGES_SURVIVE_PLAYER_UI_25PCT", "mockup visual result")
    require(correction["science_boundary"]["video_reportable_now"] is False, "correction reportability")
    require(correction["science_boundary"]["does_not_authorize_render_or_narration"] is True, "correction authorization")
    require(correction["proposed_storyboard_correction"]["scene_lines"] == {f"S{key}": value for key, value in EXPECTED_GATE_LINES.items()}, "correction gate lines")

    mockup = load_json("qa/pass7_caption_safe_mockup/receipt.json")
    require(mockup["status"] == "QA_STATIC_MOCKUP_ONLY_NOT_V9_NOT_A_CANDIDATE", "mockup status")
    require(mockup["sealed_v8_modified"] is False and mockup["storyboard_modified"] is False, "mockup custody")
    require(mockup["scene_count"] == 7 and mockup["frame_count"] == 14, "mockup census")
    for scene in mockup["scenes"]:
        scene_number = int(scene["scene"])
        require(scene["gate_line"] == EXPECTED_GATE_LINES[scene_number], f"mockup line scene {scene_number}")
        require(scene["gate_line_box"] == [38, 83, 1882, 129], f"mockup box scene {scene_number}")
        require(scene["gate_line_max_y_fraction"] == 0.119444, f"mockup y fraction scene {scene_number}")
        require(scene["top_75pct_pixel_identical_clean_to_masked"] is True, f"mockup top identity scene {scene_number}")
        sealed = ROOT / "proposal_frames/v8" / scene["sealed_input"]
        require(sha256(sealed) == scene["sealed_input_sha256"], f"mockup sealed source scene {scene_number}")
        for key in ("clean", "player_ui_25pct"):
            frame = MOCKUP_ROOT / scene[key]["frame"]
            require(sha256(frame) == scene[key]["sha256"], f"mockup frame {scene_number} {key}")
            with Image.open(frame) as image:
                require(image.size == (1920, 1080), f"mockup size {scene_number} {key}")
    for sheet in mockup["contact_sheets"].values():
        require(sha256(MOCKUP_ROOT / sheet["path"]) == sheet["sha256"], f"mockup sheet {sheet['path']}")
    gate_copy = "\n".join(EXPECTED_GATE_LINES.values())
    for forbidden in (r"cosmolog", r"\bdipole\b", r"\bparity\b", r"\bH0\b", r"black[- ]hole"):
        require(not re.search(forbidden, gate_copy, re.IGNORECASE), f"gate line forbidden term {forbidden}")

    packet = load_json("BLOCKER_PACKET_PASS7.json")
    require(packet["video_reportable_now"] is False, "packet reportability")
    require(packet["candidate"]["sha256"] == CANDIDATE_SHA, "packet candidate")
    require(packet["sealed_v8_disposition"]["v9_created"] is False, "packet v9 disposition")
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
    render_receipt = load_json("proposal_frames/v8/render_receipt.json")
    require(render_receipt["storyboard_sha256"] == sha256(ROOT / "STORYBOARD_PROPOSAL.json"), "v8 storyboard pin")
    require(render_receipt["lane_renderer_sha256"] == sha256(ROOT / "render_proposal_frames.py"), "v8 renderer pin")
    require(render_receipt["scenes"] == 7 and len(render_receipt["outputs"]) == 7, "v8 output count")
    require(load_json("qa/static_proposal_validation.json")["verdict"] == "PASS", "v8 static validation")

    extraction_time = parse_time(receipt["extracted_at_utc"])
    packet_time = parse_time(packet["checked_at"])
    snapshot_time = parse_time(snapshot["created_at"])
    require(extraction_time < packet_time < snapshot_time, "pass7 chronology")

    status = load_json("STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS7_V1", "status phase")
    require(status["video_reportable_now"] is False, "status reportability")
    receipt_text = (ROOT / "LANE_RECEIPT.md").read_text(encoding="utf-8")
    require("SPIN_WORKER_YUI_DEEPENING_PASS7_COMPLETE" in receipt_text, "receipt marker")
    require(snapshot["snapshot_id"] in receipt_text, "receipt snapshot pin")
    integrator = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(encoding="utf-8")
    require(snapshot["snapshot_id"] in integrator, "integrator snapshot pin")
    require("caption-safe" in integrator and "bottom 25%" in integrator, "integrator correction")

    media = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.casefold()
        in {".mp4", ".mp3", ".wav", ".aac", ".m4a", ".mov", ".webm"}
    ]
    require(not media, f"worker media outputs present: {media}")
    print(
        "PASS pass7 snapshot/candidate/48-obstruction-frames/hierarchy/"
        "v8-boundary-loss/caption-safe-proof/source-blockers/status/no-media"
    )


if __name__ == "__main__":
    main()
