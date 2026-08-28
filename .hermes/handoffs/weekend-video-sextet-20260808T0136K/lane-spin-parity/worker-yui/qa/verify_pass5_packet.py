#!/usr/bin/env python3
"""Deterministically verify pass-5 cut evidence, blocker depth, and custody."""

from __future__ import annotations

import gzip
import hashlib
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

from PIL import Image, ImageChops, ImageStat

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
T4_NAME = "T4_PAIRED_FLIP.json"
T4_SHA = "6e3480d4087b971d8331979a9d26926add7f9a600c5bfaa8e54da2b88e6e6873"
A38_SHA = "d2d494ddfe0c16524b65fc9e9b7e80d067ec06ceede5a14e384a9421707791b0"
EXPECTED_SEQUENCE = ["outgoing", "outgoing", "incoming", "incoming", "incoming"]
BOUNDARY_ROOT = ROOT / "qa/pass5_boundary_audit"
PASS4_ROOT = ROOT / "qa/pass4_encoded_audit"
SNAPSHOT = ROOT / "qa/pass5_review_snapshot_v1.json"


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


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load_json(relative: str) -> Any:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def difference_score(left_path: Path, right_path: Path) -> float:
    with Image.open(left_path).convert("RGB") as left, Image.open(right_path).convert(
        "RGB"
    ) as right:
        difference = ImageChops.difference(left, right)
        return round(sum(ImageStat.Stat(difference).mean) / 3.0, 6)


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


def decode_binary(path: Path, raw: bytes) -> tuple[str, bytes, str]:
    if raw.startswith(b"\x1f\x8b"):
        payload = gzip.decompress(raw)
        return "gzip", payload, payload.decode("utf-8", errors="replace")
    if raw.startswith(b"%PDF-"):
        result = subprocess.run(
            ["pdftotext", str(path), "-"],
            check=True,
            text=False,
            capture_output=True,
        )
        payload = result.stdout
        return "pdf", payload, payload.decode("utf-8", errors="replace")
    fail(f"unexpected binary format {path}")
    raise AssertionError("unreachable")


def main() -> None:
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    require(snapshot["snapshot_status"] == "IMMUTABLE_REVIEW_SNAPSHOT", "snapshot status")
    require(
        snapshot["snapshot_id"] == "spin-worker-yui-pass5-review-v1-20260808T050256K",
        "snapshot id",
    )
    require(snapshot["supersedes"]["path"] == "qa/pass4_review_snapshot_v1.json", "supersession path")
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
    receipt = load_json("qa/pass5_boundary_audit/extraction_receipt.json")
    require(receipt["deepening_pass"] == 5, "extraction pass")
    require(receipt["candidate_sha256"] == CANDIDATE_SHA, "receipt candidate hash")
    require(receipt["candidate_hash_match"] is True, "candidate receipt match")
    require(receipt["transition_count"] == 15, "transition count")
    require(receipt["sample_count"] == 75, "sample count")
    require(receipt["fps"] == 30, "receipt fps")
    require(receipt["frame_offsets"] == [-2, -1, 0, 1, 2], "frame offsets")
    require(receipt["candidate_modified"] is False, "candidate modified flag")
    require(receipt["tts_invoked"] is False, "extraction TTS flag")
    require(receipt["encoded_output_created"] is False, "encoded output flag")
    pass4 = load_json("qa/pass4_encoded_audit/extraction_receipt.json")
    require(receipt["detected_cut_times_seconds"] == pass4["detected_cut_times_seconds"], "cut replay")

    frame_hashes: list[str] = []
    expected_labels = ["minus_2f", "minus_1f", "cut", "plus_1f", "plus_2f"]
    for expected_transition, transition in enumerate(receipt["transitions"], start=1):
        require(transition["transition"] == expected_transition, f"transition order {expected_transition}")
        require(transition["from_scene"] == expected_transition, f"from scene {expected_transition}")
        require(transition["to_scene"] == expected_transition + 1, f"to scene {expected_transition}")
        samples = transition["samples"]
        require([row["sample"] for row in samples] == expected_labels, f"labels {expected_transition}")
        require([row["offset_frames"] for row in samples] == [-2, -1, 0, 1, 2], f"offsets {expected_transition}")
        cut_time = float(transition["cut_time_seconds"])
        for row in samples:
            expected_time = round(cut_time + row["offset_frames"] / 30.0, 6)
            require(abs(float(row["time_seconds"]) - expected_time) < 1e-6, f"time {row['frame']}")
            frame = BOUNDARY_ROOT / row["frame"]
            require(frame.is_file(), f"missing frame {row['frame']}")
            actual = sha256(frame)
            require(actual == row["frame_sha256"], f"frame hash {row['frame']}")
            frame_hashes.append(actual)
            with Image.open(frame) as image:
                require(list(image.size) == [1920, 1080], f"frame size {row['frame']}")
                require(image.mode == "RGB", f"frame mode {row['frame']}")
    require(len(frame_hashes) == 75, "frame count")
    require(len(set(frame_hashes)) == 75, "unique frame hashes")
    for label in expected_labels:
        sheet = receipt["contact_sheets"][label]
        require(
            sha256(BOUNDARY_ROOT / sheet["path"]) == sheet["sha256"],
            f"contact sheet {label}",
        )

    classification = load_json("qa/pass5_cut_classification.json")
    require(classification["candidate_sha256"] == CANDIDATE_SHA, "classification candidate")
    require(classification["transition_count"] == 15, "classification transitions")
    require(classification["sample_count"] == 75, "classification samples")
    require(classification["hard_cut_sequence_count"] == 15, "hard-cut count")
    require(classification["all_cut_timestamp_frames_classify_incoming"] is True, "cut incoming")
    pass4_samples: dict[tuple[int, str], dict[str, Any]] = {}
    for scene in pass4["scenes"]:
        for sample in scene["samples"]:
            pass4_samples[(int(scene["scene"]), sample["sample"])] = sample
    all_ratios: list[float] = []
    for boundary_transition, classified in zip(receipt["transitions"], classification["transitions"]):
        from_scene = int(boundary_transition["from_scene"])
        to_scene = int(boundary_transition["to_scene"])
        outgoing = PASS4_ROOT / pass4_samples[(from_scene, "late")]["frame"]
        incoming = PASS4_ROOT / pass4_samples[(to_scene, "early")]["frame"]
        sequence = []
        for sample, stored in zip(boundary_transition["samples"], classified["samples"]):
            frame = BOUNDARY_ROOT / sample["frame"]
            outgoing_score = difference_score(frame, outgoing)
            incoming_score = difference_score(frame, incoming)
            nearest = "outgoing" if outgoing_score < incoming_score else "incoming"
            sequence.append(nearest)
            require(outgoing_score == stored["outgoing_reference_score"], f"outgoing score {sample['frame']}")
            require(incoming_score == stored["incoming_reference_score"], f"incoming score {sample['frame']}")
            require(nearest == stored["nearest_reference"], f"classification {sample['frame']}")
            ratio = max(outgoing_score, incoming_score) / min(outgoing_score, incoming_score)
            all_ratios.append(round(ratio, 6))
        require(sequence == EXPECTED_SEQUENCE, f"hard-cut sequence {from_scene}")
        require(classified["first_incoming_offset_frames"] == 0, f"first incoming {from_scene}")
    require(min(all_ratios) == classification["minimum_reference_separation_ratio"] == 6.275656, "minimum separation")
    require(classification["mixed_or_blank_frame_detected_by_visual_review"] is False, "mixed-frame finding")

    scan = load_json("qa/pass5_binary_content_scan.json")
    regular = sorted(
        path for path in SOURCE.rglob("*") if path.is_file() and not path.is_symlink()
    )
    binary_rows = []
    utf8_rows: list[tuple[Path, str]] = []
    for path in regular:
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            file_format, decoded, decoded_text = decode_binary(path, raw)
            binary_rows.append((path, raw, file_format, decoded, decoded_text))
        else:
            utf8_rows.append((path, text))
    require(len(regular) == scan["regular_file_count"] == 209, "regular-file count")
    require(len(binary_rows) == scan["non_utf8_file_count"] == 6, "binary count")
    require(sum(row[2] == "gzip" for row in binary_rows) == scan["gzip_file_count"] == 4, "gzip count")
    require(sum(row[2] == "pdf" for row in binary_rows) == scan["pdf_file_count"] == 2, "pdf count")
    scan_by_path = {row["path"]: row for row in scan["files"]}
    for path, raw, file_format, decoded, decoded_text in binary_rows:
        relative = path.relative_to(SOURCE).as_posix()
        row = scan_by_path[relative]
        require(row["format"] == file_format, f"binary format {relative}")
        require(row["source_sha256"] == sha256_bytes(raw), f"binary source hash {relative}")
        require(row["decoded_sha256"] == sha256_bytes(decoded), f"binary decoded hash {relative}")
        require(T4_NAME not in decoded_text, f"binary T4 name {relative}")
        require(T4_SHA not in decoded_text, f"binary T4 hash {relative}")
        require(not re.search(r"A3\.8", decoded_text, re.IGNORECASE), f"binary A3.8 name {relative}")
        require(A38_SHA not in decoded_text, f"binary A3.8 hash {relative}")
    require(scan["files_with_any_t4_or_a3_8_identity_marker"] == 0, "binary identity markers")
    require(scan["files_with_exact_t4_and_a3_8_hash_pair"] == 0, "binary hash pairs")

    t4_mtime_ns = (SOURCE / T4_NAME).stat().st_mtime_ns
    post_t4_text = [text for path, text in utf8_rows if path.stat().st_mtime_ns > t4_mtime_ns]
    require(len(utf8_rows) == 203, "UTF-8 count")
    require(len(post_t4_text) == 9, "post-T4 UTF-8 count")
    require(sum(T4_NAME in text or T4_SHA in text for text in post_t4_text) == 4, "T4 identifier count")
    require(sum(T4_SHA in text and A38_SHA in text for text in post_t4_text) == 0, "text hash pairs")

    packet = load_json("BLOCKER_PACKET_PASS5.json")
    require(packet["video_reportable_now"] is False, "packet reportability")
    require(packet["candidate"]["sha256"] == CANDIDATE_SHA, "packet candidate")
    require(packet["sealed_v8_disposition"]["v9_warranted"] is False, "v9 disposition")
    require(packet["hard_cut_integration_guard"]["changes_sealed_v8_bytes"] is False, "v8 guard custody")
    packet_text = json.dumps(packet, sort_keys=True)
    for raw_result_field in (
        "primary_pairs_read",
        "control_pairs_reported_never_read",
        '"cells"',
        '"reading"',
        '"reading_why"',
    ):
        require(raw_result_field not in packet_text, f"raw result field leaked: {raw_result_field}")
    frame_review = SOURCE / "KUN_FRAME_REVIEW.md"
    require(frame_review.read_text(encoding="utf-8").rstrip().endswith("FRAME REVIEW: AGREES FRAME_UNSTATED"), "frame review")

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
    for output in render_receipt["outputs"]:
        frame = Path(output)
        require(frame.is_file(), f"missing v8 frame {frame.name}")
        with Image.open(frame) as image:
            require(list(image.size) == [1920, 1080], f"v8 frame size {frame.name}")
    static_validation = load_json("qa/static_proposal_validation.json")
    require(static_validation["verdict"] == "PASS", "v8 static validation")
    require(static_validation["visible_forbidden_or_internal_hits"] == 0, "v8 visible boundary")

    extraction_time = parse_time(receipt["extracted_at_utc"])
    audit_time = parse_time(packet["checked_at"])
    snapshot_time = parse_time(snapshot["created_at"])
    require(extraction_time < audit_time < snapshot_time, "pass5 chronology")

    status = load_json("STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS5_V1", "status phase")
    require(status["video_reportable_now"] is False, "status reportability")
    receipt_text = (ROOT / "LANE_RECEIPT.md").read_text(encoding="utf-8")
    require("SPIN_WORKER_YUI_DEEPENING_PASS5_COMPLETE" in receipt_text, "receipt marker")
    require(snapshot["snapshot_id"] in receipt_text, "receipt snapshot pin")
    integrator = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(encoding="utf-8")
    require(snapshot["snapshot_id"] in integrator, "integrator snapshot pin")
    require("clean hard cuts" in integrator.lower(), "integrator hard-cut guard")

    media = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.casefold()
        in {".mp4", ".mp3", ".wav", ".aac", ".m4a", ".mov", ".webm"}
    ]
    require(not media, f"worker media outputs present: {media}")
    print(
        "PASS pass5 snapshot/candidate/75-boundary-frames/15-hard-cuts/"
        "binary-content-coverage/v8-boundary/status/no-media"
    )


if __name__ == "__main__":
    main()
