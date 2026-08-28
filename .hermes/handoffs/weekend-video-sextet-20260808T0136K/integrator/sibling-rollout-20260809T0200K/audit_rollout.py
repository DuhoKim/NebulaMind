#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind")
BATCH = ROOT / ".hermes/handoffs/weekend-video-sextet-20260808T0136K"
CANARIES = BATCH / "integrator/canaries"
CANDIDATES = [
    CANARIES / "mzr-census-method-overhaul-canary-20260809T0214K",
    CANARIES / "fesc-method-overhaul-canary-20260809T0227K",
    CANARIES / "brightend-method-overhaul-canary-20260809T0235K",
    CANARIES / "mzr-anchor-method-overhaul-canary-20260809T0245K",
]
REQUIRED = [
    "spec.json", "PREDECESSOR.json", "PRE_RENDER_QA.md", "numeric_guard.json",
    "audio/synthesis_receipt.json", "audio/timeline.json", "audio/narration_master.wav",
    "build_receipt.json", "encoded_qa.json", "encoded-contact-sheet.jpg",
    "final-timing-contact-sheet.jpg", "QA.md", "RECEIPT.json",
    "POST_ENCODE_FREEZE.json", "source_manifest.json",
]


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load(path: Path):
    return json.loads(path.read_text())


def fail(message: str) -> None:
    raise RuntimeError(message)


rows = []
for candidate in CANDIDATES:
    missing = [rel for rel in REQUIRED if not (candidate / rel).is_file()]
    if missing:
        fail(f"{candidate.name}: missing {missing}")
    if list(candidate.rglob("SOURCE_FREEZE.json")):
        fail(f"{candidate.name}: unexpected SOURCE_FREEZE.json")

    spec = load(candidate / "spec.json")
    synth = load(candidate / "audio/synthesis_receipt.json")
    timeline = load(candidate / "audio/timeline.json")
    build = load(candidate / "build_receipt.json")
    guard = load(candidate / "numeric_guard.json")
    qa = load(candidate / "encoded_qa.json")
    receipt = load(candidate / "RECEIPT.json")
    predecessor = load(candidate / "PREDECESSOR.json")

    video = candidate / build["output"]
    video_sha = sha(video)
    if video_sha != build["output_sha256"] or video_sha != qa["video_sha256"] or video_sha != receipt["video_sha256"]:
        fail(f"{candidate.name}: video hash binding failed")
    if sha(candidate / "spec.json") != build["spec_sha256"] or build["spec_sha256"] != synth["spec_sha256"]:
        fail(f"{candidate.name}: spec hash binding failed")
    if sha(candidate / "audio/timeline.json") != build["timeline_sha256"]:
        fail(f"{candidate.name}: timeline hash binding failed")
    if sha(candidate / "audio/narration_master.wav") != build["audio_master_sha256"]:
        fail(f"{candidate.name}: master audio hash binding failed")
    if qa["status"] != "PASS" or receipt["status"] != "LOCAL_SELF_QA_PASS":
        fail(f"{candidate.name}: QA status failed")
    failed_checks = [name for name, value in qa["checks"].items() if not value]
    if failed_checks:
        fail(f"{candidate.name}: encoded checks failed {failed_checks}")
    if guard["status"] != "PASS":
        fail(f"{candidate.name}: numeric guard failed")
    if synth["voice"] != "alloy" or synth["speed"] != 1.18 or synth["music"] is not False:
        fail(f"{candidate.name}: narration contract failed")
    if synth["sentence_count"] != len(spec["sentences"]) or synth["synthesis_unit"] != "one exact sentence per call":
        fail(f"{candidate.name}: sentence-aligned synthesis failed")
    if not 105 <= timeline["delivered_wpm"] <= 125:
        fail(f"{candidate.name}: WPM outside contract")
    if timeline["section_intervals_seconds"][spec["peak_section"]] != max(timeline["section_intervals_seconds"].values()):
        fail(f"{candidate.name}: discriminant is not the runtime peak")
    if [s["section"] for s in spec["sentences"][:4]] != ["motivation"] * 4:
        fail(f"{candidate.name}: introduction is not first")
    intro = " ".join(s["text"].lower() for s in spec["sentences"][:4])
    if not all(token in intro for token in ("if ", "would", "could")):
        fail(f"{candidate.name}: introduction not fully conditional")
    if any(token in intro for token in ("value withheld", "no result", "not reportable", "method only")):
        fail(f"{candidate.name}: leading disclaimer detected")
    if qa["introduction_transcription"]["status"] != "PASS" or qa["introduction_transcription"]["similarity"] < 0.94:
        fail(f"{candidate.name}: encoded introduction transcription failed")
    if build["source_grounded_runtime_percent"] < 75:
        fail(f"{candidate.name}: insufficient source-grounded runtime")
    expected_gates = {"upload": False, "cockpit_or_video_root_copy": False, "git": False, "video_reportable_now": False}
    if receipt["gates"] != expected_gates or spec["video_reportable_now"] is not False:
        fail(f"{candidate.name}: closed-gate receipt failed")
    pred_path = Path(predecessor["candidate"])
    if not pred_path.is_file() or sha(pred_path) != predecessor["candidate_sha256"]:
        fail(f"{candidate.name}: predecessor preservation failed")

    sections = timeline["section_intervals_seconds"]
    rows.append({
        "slug": spec["slug"],
        "candidate": candidate.name,
        "video": video.name,
        "sha256": video_sha,
        "duration_seconds": float(qa["probe"]["format"]["duration"]),
        "word_count": timeline["word_count"],
        "wpm": timeline["delivered_wpm"],
        "intro_similarity": qa["introduction_transcription"]["similarity"],
        "peak_section_seconds": sections[spec["peak_section"]],
        "motivation_seconds": sections["motivation"],
        "encoded_checks": len(qa["checks"]),
        "source_grounded_runtime_percent": build["source_grounded_runtime_percent"],
        "predecessor_sha256": predecessor["candidate_sha256"],
        "video_reportable_now": False,
    })

candidate_hashes = {r["sha256"] for r in rows}
public_hashes = {sha(path) for path in (ROOT / "frontend/public/videos").glob("*.mp4")}
if candidate_hashes & public_hashes:
    fail("a rollout candidate was copied to frontend/public/videos")

accepted = CANARIES / "spin-method-overhaul-canary-20260808T1959K/spin-method-overhaul-canary-20260808T1959K.mp4"
accepted_sha = "c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240"
if sha(accepted) != accepted_sha:
    fail("accepted c5e7deed template changed")

head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
if not head.startswith("ebe9c7f"):
    fail(f"unexpected Git HEAD change: {head}")

report = {
    "status": "PASS",
    "candidate_count": len(rows),
    "candidates": rows,
    "shared_contract": {
        "voice": "alloy",
        "speed": 1.18,
        "wpm_range": [105, 125],
        "sentence_aligned_synthesis": True,
        "pcm_derived_timing": True,
        "method_only": True,
        "source_freeze_present": False,
        "video_reportable_now": False,
    },
    "preservation": {
        "accepted_spin_template_sha256": accepted_sha,
        "accepted_spin_template_unchanged": True,
        "all_predecessor_hashes_match": True,
        "rejected_mzr_census_attempt_preserved": (CANDIDATES[0] / "rejected-attempts/d940a7e8-freeze-hold/mzr-census-method-overhaul-canary-20260809T0214K.mp4").is_file(),
    },
    "closed_gates": {
        "upload": False,
        "cockpit_or_video_root_copy": False,
        "git_commit_push_merge": False,
        "candidate_hash_absent_from_public_video_root": True,
        "git_head": head,
    },
}
print(json.dumps(report, indent=2))
