#!/usr/bin/env python3
"""Deterministically verify pass-3 custody, recursive blockers, and lane boundaries."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

WORKER = Path(__file__).resolve().parents[1]
SOURCE = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "spin-parity-census-20260805T1922K"
)
T4_NAME = "T4_PAIRED_FLIP.json"
T4_SHA256 = "6e3480d4087b971d8331979a9d26926add7f9a600c5bfaa8e54da2b88e6e6873"
A38_SHA256 = "d2d494ddfe0c16524b65fc9e9b7e80d067ec06ceede5a14e384a9421707791b0"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def recursive_review_keys(value: object, path: str = "$") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            next_path = f"{path}.{key}"
            if re.search(r"review|verdict", key, re.IGNORECASE):
                found.append(next_path)
            found.extend(recursive_review_keys(child, next_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(recursive_review_keys(child, f"{path}[{index}]"))
    return found


def flatten_strings(value: object) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [text for child in value.values() for text in flatten_strings(child)]
    if isinstance(value, list):
        return [text for child in value for text in flatten_strings(child)]
    return []


def main() -> None:
    snapshot = json.loads((WORKER / "qa/pass3_review_snapshot_v1.json").read_text())
    blocker = json.loads((WORKER / "BLOCKER_PACKET_PASS3.json").read_text())
    extraction = json.loads(
        (WORKER / "qa/pass3_encoded_audit/extraction_receipt.json").read_text()
    )
    pass2_extraction = json.loads(
        (WORKER / "qa/pass2_encoded_audit/extraction_receipt.json").read_text()
    )
    inventory = json.loads((WORKER / "qa/pass3_source_inventory.json").read_text())
    status = json.loads((WORKER / "STATUS.json").read_text())

    assert snapshot["status"] == "IMMUTABLE_REVIEW_SNAPSHOT"
    assert snapshot["decision"] == "DEEPEN_BLOCKER_PACKET_NO_V9"
    candidate = Path(snapshot["candidate"]["path"])
    assert sha256(candidate) == snapshot["candidate"]["sha256"]
    for row in snapshot["artifacts"]:
        assert sha256(WORKER / row["path"]) == row["sha256"], row["path"]

    assert extraction["deepening_pass"] == 3
    assert extraction["candidate_hash_match"] is True
    assert extraction["candidate_sha256"] == snapshot["candidate"]["sha256"]
    assert extraction["scene_count"] == 16
    assert len(extraction["detected_cut_times_seconds"]) == 15
    assert extraction["contact_sheet_sha256"] == sha256(
        WORKER / "qa/pass3_encoded_audit/contact_sheet_fresh.png"
    )
    assert extraction["contact_sheet_sha256"] == pass2_extraction["contact_sheet_sha256"]
    assert len(extraction["frames"]) == len(pass2_extraction["frames"]) == 16
    for current, prior in zip(extraction["frames"], pass2_extraction["frames"]):
        assert current["scene"] == prior["scene"]
        assert current["frame_sha256"] == prior["frame_sha256"]
        assert current["frame_sha256"] == sha256(
            WORKER / "qa/pass3_encoded_audit" / current["frame"]
        )
        assert current["size"] == [1920, 1080]
        assert current["mode"] == "RGB"

    chronology = snapshot["chronology"]
    assert chronology["extraction_completed_at"] == extraction["extracted_at_utc"]
    assert datetime.fromisoformat(chronology["extraction_completed_at"]) < datetime.fromisoformat(
        chronology["audit_completed_at"]
    ) < datetime.fromisoformat(chronology["exact_current_snapshot_at"])

    audit_text = (WORKER / "PASS3_ENCODED_FRAME_AUDIT.md").read_text()
    assert "one opening, ten later text/hero-number cards, and five figures" in audit_text
    assert "internal layout/text-width truncation" in audit_text
    assert "not literal clipping at the outer frame edge" in audit_text
    assert blocker["encoded_frame_audit"]["sha256"] == sha256(
        WORKER / blocker["encoded_frame_audit"]["path"]
    )
    assert blocker["encoded_frame_audit"]["extraction_receipt_sha256"] == sha256(
        WORKER / blocker["encoded_frame_audit"]["extraction_receipt"]
    )

    rows = inventory["rows"]
    source_files = sorted(
        path.relative_to(SOURCE).as_posix()
        for path in SOURCE.rglob("*")
        if path.is_file() and not path.is_symlink()
    )
    assert source_files == [row["path"] for row in rows]
    assert inventory["regular_file_count"] == len(rows) == 209
    assert inventory["utf8_decodable_count"] == 203
    assert inventory["non_utf8_count"] == 6
    assert inventory["symlink_count"] == 0
    for row in rows:
        path = SOURCE / row["path"]
        raw = path.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["sha256"], row["path"]
        assert len(raw) == row["bytes"]
        assert path.stat().st_mtime_ns == row["mtime_ns"]
        try:
            text = raw.decode("utf-8")
            decodable = True
        except UnicodeDecodeError:
            text = ""
            decodable = False
        assert decodable == row["utf8_decodable"]
        assert text.count(T4_NAME) == row["exact_t4_name_mentions"]
        assert text.count(T4_SHA256) == row["t4_sha256_mentions"]
        assert len(re.findall(r"A3\.8", text, re.IGNORECASE)) == row["a3_8_mentions"]
        assert text.count(A38_SHA256) == row["a3_8_sha256_mentions"]
    rows_sha = hashlib.sha256(
        json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    assert rows_sha == inventory["inventory_rows_sha256"]
    assert rows_sha == snapshot["nested_custody"]["recursive_source_rows_sha256"]

    verdict_rows = [row for row in rows if row["filename_contains_verdict_casefold"]]
    assert len(verdict_rows) == inventory["casefold_verdict_filename_count"] == 5
    assert all(row["predates_t4"] for row in verdict_rows)
    t4_rows = [
        row
        for row in rows
        if row["post_t4"]
        and (row["exact_t4_name_mentions"] or row["t4_sha256_mentions"])
    ]
    assert len(t4_rows) == 4
    assert all(row["exact_t4_name_mentions"] > 0 for row in t4_rows)
    assert all(row["t4_sha256_mentions"] == 0 for row in t4_rows)
    assert all(row["a3_8_mentions"] == 0 for row in t4_rows)
    assert all(row["a3_8_sha256_mentions"] == 0 for row in t4_rows)
    assert inventory["post_t4_candidate_review_record_count"] == 0
    assert not any(row["post_t4_candidate_review_record"] for row in rows)

    absence = blocker["blocker_1_post_run_independent_verdict"]["recursive_absence_proof"]
    assert absence["inventory_sha256"] == sha256(WORKER / absence["inventory_path"])
    assert absence["inventory_rows_sha256"] == rows_sha
    assert absence["regular_file_count"] == 209
    assert absence["post_t4_candidate_a3_8_independent_review_record_count"] == 0

    t4 = SOURCE / T4_NAME
    assert sha256(t4) == T4_SHA256
    assert recursive_review_keys(json.loads(t4.read_text())) == []
    blocker_text = (WORKER / "BLOCKER_PACKET_PASS3.json").read_text()
    for forbidden_result_field in (
        '"primary_pairs_read"',
        '"control_pairs_reported_never_read"',
        '"cells"',
        '"reading"',
        '"reading_why"',
    ):
        assert forbidden_result_field not in blocker_text

    review_contract = SOURCE / "AMENDMENT_A3.8_DRAFT.md"
    frame_review = SOURCE / "KUN_FRAME_REVIEW.md"
    assert sha256(review_contract) == A38_SHA256
    assert "Status: **FROZEN, IN FORCE**" in review_contract.read_text()
    assert sha256(frame_review) == blocker["blocker_2_archive_frame"]["review_sha256"]
    assert frame_review.read_text().rstrip().endswith("FRAME REVIEW: AGREES FRAME_UNSTATED")
    assert blocker["blocker_1_post_run_independent_verdict"]["state"] == "OPEN"
    assert blocker["blocker_2_archive_frame"]["state"] == "OPEN"
    assert len(
        blocker["blocker_1_post_run_independent_verdict"]["minimum_unblock_record_fields"]
    ) == 6

    storyboard = json.loads((WORKER / "STORYBOARD_PROPOSAL.json").read_text())
    visible = []
    for scene in storyboard["scenes"]:
        visible.extend(flatten_strings(scene["on_screen_copy"]))
        visible.append(scene["display_citation"])
    visible_copy = "\n".join(visible)
    for pattern in (
        r"cosmolog",
        r"\bdipole\b",
        r"\bparity\b",
        r"\bH0\b",
        r"black[- ]hole",
        r"\bT1C?\b",
        r"\bT3\b",
        r"\bT4\b",
        r"\bHwao\b",
    ):
        assert not re.search(pattern, visible_copy, re.IGNORECASE), pattern
    assert sha256(WORKER / "STORYBOARD_PROPOSAL.json") == blocker["safe_current_output"][
        "storyboard_sha256"
    ]
    assert sha256(WORKER / "render_proposal_frames.py") == blocker["safe_current_output"][
        "renderer_sha256"
    ]
    render_receipt = json.loads((WORKER / "proposal_frames/v8/render_receipt.json").read_text())
    assert render_receipt["storyboard_sha256"] == blocker["safe_current_output"][
        "storyboard_sha256"
    ]
    assert render_receipt["lane_renderer_sha256"] == blocker["safe_current_output"][
        "renderer_sha256"
    ]
    static_validation = json.loads((WORKER / "qa/static_proposal_validation.json").read_text())
    assert static_validation["verdict"] == "PASS"
    assert static_validation["iteration"] == "v8"
    assert static_validation["visible_forbidden_or_internal_hits"] == 0

    assert blocker["video_reportable_now"] is False
    assert status["phase"] == "SEALED_ISOLATED_DEEPENING_PASS3_V1"
    assert status["video_reportable_now"] is False
    media = []
    for extension in ("*.mp4", "*.mp3", "*.wav", "*.aac", "*.m4a"):
        media.extend(WORKER.rglob(extension))
    assert media == []

    print(
        "PASS pass3: snapshot exact; 16/16 fresh frames reproduce pass2; "
        "recursive source inventory 209/209 exact; 5 verdict filenames pre-T4; "
        "4 post-T4 T4 identifiers and zero A3.8 review candidates; FRAME_UNSTATED exact; "
        "sealed v8 unchanged; video_reportable_now=false; no worker media"
    )


if __name__ == "__main__":
    main()
