#!/usr/bin/env python3
"""Freeze the exact v4 candidate bytes after internal machine and frame QA."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VIDEO = ROOT / "spin-method-overhaul-canary-20260809T2340K.mp4"
EXPECTED_VIDEO_SHA256 = "4d230cc0efca0eb68a8d027d614b6b7e500590cff06154f1514d4402a84d7078"
PREDECESSOR = ROOT.parent / "spin-method-overhaul-canary-20260808T1959K/spin-method-overhaul-canary-20260808T1959K.mp4"
EXPECTED_PREDECESSOR_SHA256 = "c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240"
OUTPUT = ROOT / "POST_ENCODE_FREEZE_V4.json"
RECEIPT = ROOT / "RECEIPT.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def artifact(path: str) -> dict:
    target = ROOT / path
    return {"path": path, "bytes": target.stat().st_size, "sha256": sha256(target)}


def main() -> int:
    if ROOT.name != "spin-method-overhaul-canary-20260809T2340K":
        raise RuntimeError("freeze script must run inside the final versioned candidate directory")
    if sha256(VIDEO) != EXPECTED_VIDEO_SHA256:
        raise RuntimeError("candidate MP4 changed before freeze")
    if sha256(PREDECESSOR) != EXPECTED_PREDECESSOR_SHA256:
        raise RuntimeError("predecessor MP4 was not preserved")
    qa = json.loads((ROOT / "encoded_qa.json").read_text())
    if qa["status"] != "PENDING_TORI_EXACT_HASH_REGATE" or not all(qa["checks"].values()):
        raise RuntimeError("internal encoded QA is not fully clear")
    timeline = json.loads((ROOT / "audio_v4/timeline.json").read_text())
    asr = json.loads((ROOT / "encoded_qa/encoded-why-study-introduction-transcription-v4.json").read_text())
    if asr["status"] != "PASS" or asr["normalized_similarity"] < 0.99:
        raise RuntimeError("encoded opening ASR is not exact")

    artifact_paths = [
        "spin-method-overhaul-canary-20260809T2340K.mp4",
        "spin-method-overhaul-canary-20260809T2340K-v4.srt",
        "narration_script_v4.json",
        "storyboard_v4_final.json",
        "source_manifest_v4.json",
        "audio_v4/synthesis_receipt.json",
        "audio_v4/timeline.json",
        "audio_v4/narration_master.wav",
        "build.py",
        "build_receipt.json",
        "qa_encoded.py",
        "encoded_qa.json",
        "encoded_qa/encoded-why-study-introduction-transcription-v4.json",
        "final-timing-contact-sheet-v4.jpg",
        "encoded-contact-sheet-v4.jpg",
    ]
    artifacts = [artifact(path) for path in artifact_paths]
    excluded = {OUTPUT.name, RECEIPT.name}
    files = sorted(path for path in ROOT.rglob("*") if path.is_file() and path.name not in excluded)
    tree_lines = [f"{path.relative_to(ROOT)}\0{sha256(path)}" for path in files]
    tree_digest = hashlib.sha256("\n".join(tree_lines).encode()).hexdigest()

    freeze = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": ROOT.name,
        "status": "INTERNAL_QA_PASS_PENDING_TORI_EXACT_HASH_REGATE_AND_DUHO_WATCH_LISTEN",
        "video_reportable_now": False,
        "human_acceptance_conferred": False,
        "candidate_mp4_sha256": EXPECTED_VIDEO_SHA256,
        "predecessor_preserved": {
            "candidate": PREDECESSOR.parent.name,
            "mp4_sha256": EXPECTED_PREDECESSOR_SHA256,
        },
        "narration": {
            "provider": "Hermes managed OpenAI audio gateway",
            "voice": "alloy",
            "speed": 1.18,
            "music": False,
            "word_count": timeline["word_count"],
            "delivered_wpm": timeline["delivered_wpm"],
            "duration_seconds": timeline["master_duration_seconds"],
            "max_abs_audio_visual_start_delta_seconds": timeline["max_abs_audio_visual_start_delta_seconds"],
            "encoded_opening_asr_similarity": asr["normalized_similarity"],
        },
        "internal_gates": qa["checks"],
        "encoded_loudness": qa["loudness"],
        "mandatory_encoded_frame_review": {
            "status": "PASS",
            "reviewed_artifact": "encoded-contact-sheet-v4.jpg extracted from exact candidate bytes",
            "scope": "29 sentence-mid frames plus five mirror-animation frames",
            "finding": "No clipping, overlap, selected result or direction, stale frame, rail regression, or mirror-animation defect found. The five why-study beats remain visibly distinct and precede the method handoff.",
        },
        "artifact_hashes": artifacts,
        "pre_freeze_tree": {
            "file_count": len(files),
            "digest_algorithm": "sha256 over sorted relative-path NUL file-sha256 lines",
            "sha256": tree_digest,
        },
        "forbidden_actions_remain_closed": [
            "public or cockpit replacement",
            "frontend mutation",
            "upload or publication",
            "database or SQL write",
            "deploy or restart",
            "git commit, push, or merge",
        ],
        "next_gate": "Tori must re-gate these exact MP4 bytes by SHA-256; Duho's watch/listen verdict remains the only acceptance gate.",
    }
    OUTPUT.write_text(json.dumps(freeze, indent=2) + "\n")
    RECEIPT.write_text(
        "# Spin why-study candidate v4 receipt\n\n"
        f"- Candidate MP4 SHA-256: `{EXPECTED_VIDEO_SHA256}`\n"
        f"- Preserved predecessor SHA-256: `{EXPECTED_PREDECESSOR_SHA256}`\n"
        f"- Duration: `{timeline['master_duration_seconds']:.6f}s`\n"
        f"- Narration: `Alloy 1.18`, `{timeline['delivered_wpm']:.6f} WPM`, no music\n"
        f"- Encoded opening ASR normalized similarity: `{asr['normalized_similarity']:.6f}`\n"
        "- Internal machine QA: `PASS`\n"
        "- Mandatory encoded-frame review: `PASS`\n"
        "- Status: `PENDING_TORI_EXACT_HASH_REGATE_AND_DUHO_WATCH_LISTEN`\n"
        "- No public/cockpit/frontend/upload/deploy/DB/Git action was taken.\n"
        "- No human acceptance is claimed.\n"
    )
    print(json.dumps({"freeze": str(OUTPUT), "receipt": str(RECEIPT), "mp4_sha256": EXPECTED_VIDEO_SHA256, "pre_freeze_tree_sha256": tree_digest}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
