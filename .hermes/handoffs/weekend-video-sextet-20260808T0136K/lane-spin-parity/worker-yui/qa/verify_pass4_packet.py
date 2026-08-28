#!/usr/bin/env python3
"""Deterministically verify pass-4 temporal evidence, blocker depth, and custody."""

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
T4_NAME = "T4_PAIRED_FLIP.json"
T4_SHA = "6e3480d4087b971d8331979a9d26926add7f9a600c5bfaa8e54da2b88e6e6873"
A38_SHA = "d2d494ddfe0c16524b65fc9e9b7e80d067ec06ceede5a14e384a9421707791b0"
SNAPSHOT = ROOT / "qa/pass4_review_snapshot_v1.json"


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
        snapshot["snapshot_id"] == "spin-worker-yui-pass4-review-v1-20260808T044638K",
        "snapshot id",
    )
    require(
        snapshot["supersedes"]["path"] == "qa/pass3_review_snapshot_v1.json",
        "snapshot supersession path",
    )
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
    receipt = load_json("qa/pass4_encoded_audit/extraction_receipt.json")
    require(receipt["deepening_pass"] == 4, "extraction pass")
    require(receipt["candidate_sha256"] == CANDIDATE_SHA, "receipt candidate hash")
    require(receipt["candidate_hash_match"] is True, "candidate receipt match")
    require(receipt["scene_count"] == 16, "scene count")
    require(receipt["sample_count"] == 48, "sample count")
    require(len(receipt["detected_cut_times_seconds"]) == 15, "cut count")
    require(receipt["candidate_modified"] is False, "candidate modified flag")
    require(receipt["tts_invoked"] is False, "extraction TTS flag")
    require(receipt["encoded_output_created"] is False, "encoded output flag")

    frame_hashes: list[str] = []
    pass3 = load_json("qa/pass3_encoded_audit/extraction_receipt.json")
    pass3_mid_hashes = {
        int(row["scene"]): row["frame_sha256"] for row in pass3["frames"]
    }
    for expected_scene, scene in enumerate(receipt["scenes"], start=1):
        require(scene["scene"] == expected_scene, f"scene order {expected_scene}")
        samples = scene["samples"]
        require([row["sample"] for row in samples] == ["early", "mid", "late"], f"sample labels {expected_scene}")
        times = [float(row["time_seconds"]) for row in samples]
        require(times[0] < times[1] < times[2], f"sample chronology {expected_scene}")
        require(times[0] > float(scene["start_seconds"]), f"early bound {expected_scene}")
        require(times[2] < float(scene["end_seconds"]), f"late bound {expected_scene}")
        for row in samples:
            frame = ROOT / "qa/pass4_encoded_audit" / row["frame"]
            require(frame.is_file(), f"missing frame {row['frame']}")
            actual = sha256(frame)
            require(actual == row["frame_sha256"], f"frame hash {row['frame']}")
            frame_hashes.append(actual)
            with Image.open(frame) as image:
                require(list(image.size) == [1920, 1080], f"frame size {row['frame']}")
                require(image.mode == "RGB", f"frame mode {row['frame']}")
        require(
            samples[1]["frame_sha256"] == pass3_mid_hashes[expected_scene],
            f"pass3 midpoint reproduction scene {expected_scene}",
        )
    require(len(frame_hashes) == 48, "frame hash count")
    require(len(set(frame_hashes)) == 47, "unique frame hash count")
    for label in ("early", "mid", "late"):
        sheet = receipt["contact_sheets"][label]
        require(
            sha256(ROOT / "qa/pass4_encoded_audit" / sheet["path"])
            == sheet["sha256"],
            f"contact sheet {label}",
        )

    temporal = load_json("qa/pass4_temporal_content_audit.json")
    require(temporal["deepening_pass"] == 4, "temporal pass")
    require(temporal["candidate_sha256"] == CANDIDATE_SHA, "temporal candidate")
    require(temporal["scene_count"] == 16, "temporal scene count")
    require(temporal["samples_checked"] == 48, "temporal sample count")
    require(temporal["ocr_confidence_floor"] == 50, "OCR confidence floor")
    require(temporal["ocr_text_not_reproduced"] is True, "OCR text custody")
    require(temporal["byte_static_scene_count"] == 0, "byte-static count")
    require(
        sum(row["ocr_normalized_text_stable"] for row in temporal["scenes"]) == 8,
        "exact OCR stable count",
    )
    minimum = min(
        (row["ocr_min_pairwise_token_multiset_similarity"], row["scene"])
        for row in temporal["scenes"]
    )
    require(minimum == (0.888889, 7), "minimum OCR token similarity")

    scan = load_json("qa/pass4_unblock_contract_scan.json")
    regular = sorted(
        path for path in SOURCE.rglob("*") if path.is_file() and not path.is_symlink()
    )
    t4_mtime_ns = (SOURCE / T4_NAME).stat().st_mtime_ns
    utf8_rows: list[tuple[Path, str]] = []
    binary_rows: list[Path] = []
    for path in regular:
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            binary_rows.append(path)
        else:
            utf8_rows.append((path, text))
    post_t4_text = [
        (path, text) for path, text in utf8_rows if path.stat().st_mtime_ns > t4_mtime_ns
    ]
    post_t4_binary = [
        path for path in binary_rows if path.stat().st_mtime_ns > t4_mtime_ns
    ]
    require(len(regular) == scan["regular_file_count"] == 209, "regular-file count")
    require(len(utf8_rows) == scan["utf8_decodable_count"] == 203, "UTF-8 count")
    require(len(binary_rows) == scan["non_utf8_count"] == 6, "binary count")
    require(len(post_t4_text) == scan["post_t4_utf8_count"] == 9, "post-T4 text count")
    require(len(post_t4_binary) == scan["post_t4_non_utf8_count"] == 0, "post-T4 binary count")
    require(all(path.stat().st_mtime_ns < t4_mtime_ns for path in binary_rows), "binary chronology")
    formats = []
    for path in binary_rows:
        raw = path.read_bytes()
        if raw.startswith(b"\x1f\x8b"):
            formats.append("gzip")
        elif raw.startswith(b"%PDF-"):
            formats.append("pdf")
        else:
            formats.append("other")
    require(formats.count("gzip") == 4 and formats.count("pdf") == 2, "binary formats")
    identifiers = [text for _, text in post_t4_text if T4_NAME in text or T4_SHA in text]
    hash_pairs = [text for _, text in post_t4_text if T4_SHA in text and A38_SHA in text]
    require(len(identifiers) == scan["post_t4_t4_identifier_count"] == 4, "T4 identifier count")
    require(len(hash_pairs) == scan["post_t4_exact_t4_and_a3_8_hash_pair_count"] == 0, "exact hash-pair count")
    require(scan["post_t4_complete_minimum_marker_candidate_count"] == 0, "minimum candidate count")

    packet = load_json("BLOCKER_PACKET_PASS4.json")
    require(packet["video_reportable_now"] is False, "packet reportability")
    require(packet["candidate"]["sha256"] == CANDIDATE_SHA, "packet candidate")
    require(packet["sealed_v8_disposition"]["v9_warranted"] is False, "v9 disposition")
    require(packet["temporal_integration_guard"]["changes_sealed_v8_bytes"] is False, "v8 guard custody")
    packet_text = json.dumps(packet, sort_keys=True)
    for raw_result_field in (
        "primary_pairs_read",
        "control_pairs_reported_never_read",
        '"cells"',
        '"reading"',
        '"reading_why"',
    ):
        require(raw_result_field not in packet_text, f"raw result field leaked: {raw_result_field}")

    storyboard = load_json("STORYBOARD_PROPOSAL.json")
    visible = "\n".join(visible_strings(storyboard))
    for forbidden in (r"cosmolog", r"\bdipole\b", r"\bparity\b", r"\bH0\b", r"black[- ]hole"):
        require(not re.search(forbidden, visible, re.IGNORECASE), f"visible forbidden term: {forbidden}")
    for internal in ("T1", "T1C", "T3", "T4", "Hwao", "/Users/"):
        require(internal not in visible, f"visible internal token: {internal}")
    render_receipt = load_json("proposal_frames/v8/render_receipt.json")
    require(
        render_receipt["status"] == "STATIC_PROPOSAL_ONLY_NOT_A_CANDIDATE",
        "v8 receipt status",
    )
    require(render_receipt["storyboard_sha256"] == sha256(ROOT / "STORYBOARD_PROPOSAL.json"), "v8 storyboard pin")
    require(
        render_receipt["lane_renderer_sha256"]
        == sha256(ROOT / "render_proposal_frames.py"),
        "v8 renderer pin",
    )
    require(render_receipt["scenes"] == 7, "v8 scene count")
    require(len(render_receipt["outputs"]) == 7, "v8 output count")
    for output in render_receipt["outputs"]:
        frame = Path(output)
        require(frame.is_file(), f"missing v8 frame {frame.name}")
        with Image.open(frame) as image:
            require(list(image.size) == [1920, 1080], f"v8 frame size {frame.name}")
    static_validation = load_json("qa/static_proposal_validation.json")
    require(static_validation["verdict"] == "PASS", "v8 static validation")
    require(static_validation["iteration"] == "v8", "v8 validation iteration")
    require(
        static_validation["visible_forbidden_or_internal_hits"] == 0,
        "v8 visible boundary validation",
    )

    extraction_time = parse_time(receipt["extracted_at_utc"])
    audit_time = parse_time(packet["checked_at"])
    snapshot_time = parse_time(snapshot["created_at"])
    require(extraction_time < audit_time < snapshot_time, "pass4 chronology")

    status = load_json("STATUS.json")
    require(status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS4_V1", "status phase")
    require(status["video_reportable_now"] is False, "status reportability")
    receipt_text = (ROOT / "LANE_RECEIPT.md").read_text(encoding="utf-8")
    require("SPIN_WORKER_YUI_DEEPENING_PASS4_COMPLETE" in receipt_text, "receipt marker")
    require(snapshot["snapshot_id"] in receipt_text, "receipt snapshot pin")
    integrator = (ROOT / "INTEGRATOR_REQUEST_PROPOSAL.md").read_text(encoding="utf-8")
    require(snapshot["snapshot_id"] in integrator, "integrator snapshot pin")

    media = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.casefold()
        in {".mp4", ".mp3", ".wav", ".aac", ".m4a", ".mov", ".webm"}
    ]
    require(not media, f"worker media outputs present: {media}")
    print(
        "PASS pass4 snapshot/artifacts/candidate/48-frames/midpoint-reproduction/"
        "temporal-audit/unblock-scan/v8-boundary/status/no-media"
    )


if __name__ == "__main__":
    main()
