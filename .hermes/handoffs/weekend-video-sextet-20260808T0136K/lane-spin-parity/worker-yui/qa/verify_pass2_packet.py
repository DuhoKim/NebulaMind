#!/usr/bin/env python3
"""Deterministically verify the pass-2 custody and exact blocker predicates."""

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


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


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


def main() -> None:
    snapshot = json.loads((WORKER / "qa/pass2_review_snapshot_v7.json").read_text())
    blocker = json.loads((WORKER / "BLOCKER_PACKET_PASS2.json").read_text())
    status = json.loads((WORKER / "STATUS.json").read_text())
    extraction = json.loads((WORKER / "qa/pass2_encoded_audit/extraction_receipt.json").read_text())

    candidate = Path(snapshot["candidate"]["path"])
    assert sha256(candidate) == snapshot["candidate"]["sha256"]
    for row in snapshot["artifacts"]:
        assert sha256(WORKER / row["path"]) == row["sha256"], row["path"]

    t4 = SOURCE / "T4_PAIRED_FLIP.json"
    t4_sha = "6e3480d4087b971d8331979a9d26926add7f9a600c5bfaa8e54da2b88e6e6873"
    assert sha256(t4) == t4_sha
    assert recursive_review_keys(json.loads(t4.read_text())) == []

    verdict_files = sorted(
        path.name for path in SOURCE.iterdir()
        if path.is_file() and "verdict" in path.name.casefold()
    )
    assert verdict_files == [
        "KUN_VERDICT_REVIEW.md",
        "RUN_kun_verdict.txt",
        "VERDICT_RECORD_COLUMNS_DRAFT.md",
        "VERDICT_RECORD_FRAME_DRAFT.md",
        "_KUN_VERDICT_REVIEW_BRIEF.md",
    ]
    t4_mtime = t4.stat().st_mtime_ns
    assert all((SOURCE / name).stat().st_mtime_ns < t4_mtime for name in verdict_files)
    recorded_verdicts = blocker["blocker_1_post_run_independent_verdict"]["verdict_named_file_census"]
    assert recorded_verdicts["count"] == len(verdict_files) == 5
    assert sorted(row["name"] for row in recorded_verdicts["files"]) == verdict_files

    post_t4_mentions: dict[str, int] = {}
    for path in SOURCE.iterdir():
        if not path.is_file():
            continue
        try:
            text = path.read_text()
        except (UnicodeDecodeError, OSError):
            continue
        if "T4_PAIRED_FLIP.json" in text and path.stat().st_mtime_ns > t4_mtime:
            post_t4_mentions[path.name] = len(re.findall(r"A3\.8", text, re.IGNORECASE))
    assert post_t4_mentions == {
        "_LANA_ZEROCONC_BRIEF.md": 0,
        "LANA_ZERO_CONCORDANCE.md": 0,
        "storyboard_spin_parity.json": 0,
        "storyboard_spin_parity.json.pre-intro.bak": 0,
    }
    recorded_mentions = blocker["blocker_1_post_run_independent_verdict"]["post_result_documents_that_name_t4"]
    assert {row["name"]: row["a3_8_mentions"] for row in recorded_mentions} == post_t4_mentions

    amendment = SOURCE / "AMENDMENT_A4_DRAFT.md"
    review_contract = SOURCE / "AMENDMENT_A3.8_DRAFT.md"
    frame_review = SOURCE / "KUN_FRAME_REVIEW.md"
    assert sha256(amendment) == "8343c1947384cdb36355a0fe2f6965d4445ab013fda25e3f33b4d8300ce58974"
    assert sha256(review_contract) == "d2d494ddfe0c16524b65fc9e9b7e80d067ec06ceede5a14e384a9421707791b0"
    assert sha256(frame_review) == "ccedf6846391a8f0661a88b2eec0ce21fbfd7c44ad16201080bb196f56d258e5"
    assert frame_review.read_text().rstrip().endswith("FRAME REVIEW: AGREES FRAME_UNSTATED")

    assert blocker["video_reportable_now"] is False
    assert blocker["extraction_receipt_replay_at"] == extraction["extracted_at_utc"]
    assert snapshot["chronology"]["initial_packet_draft_at"] == blocker["initial_packet_draft_at"]
    assert snapshot["chronology"]["extraction_receipt_replay_at"] == blocker["extraction_receipt_replay_at"]
    assert snapshot["chronology"]["exact_current_reverified_at"] == blocker["checked_at"]
    assert datetime.fromisoformat(blocker["initial_packet_draft_at"]) < datetime.fromisoformat(blocker["extraction_receipt_replay_at"])
    assert datetime.fromisoformat(blocker["checked_at"]) > datetime.fromisoformat(blocker["extraction_receipt_replay_at"])
    assert blocker["blocker_1_post_run_independent_verdict"]["state"] == "OPEN"
    assert len(blocker["blocker_1_post_run_independent_verdict"]["minimum_unblock_record_fields"]) == 6
    assert blocker["blocker_2_archive_frame"]["state"] == "OPEN"
    assert status["video_reportable_now"] is False

    media = []
    for extension in ("*.mp4", "*.mp3", "*.wav", "*.aac", "*.m4a"):
        media.extend(WORKER.rglob(extension))
    assert media == []

    print(
        "PASS pass2: snapshot exact; T4 has no review/verdict keys; "
        "5/5 verdict-named files predate T4; only 4 post-T4 T4 mentions and none invokes A3.8; "
        "FRAME_UNSTATED exact; video_reportable_now=false; no worker media"
    )


if __name__ == "__main__":
    main()
