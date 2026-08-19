#!/usr/bin/env python3
"""Freeze exact local render, QA, tools, and gated inputs after a passing final gate."""
from __future__ import annotations

import datetime as dt
import json
import platform
import subprocess
from pathlib import Path

import pipeline

FREEZE = pipeline.BUILD / "FREEZE.json"
REPORT = pipeline.BUILD / "BUILD_REPORT.md"
EXCLUDE_NAMES = {FREEZE.name, REPORT.name}


def file_record(path: Path, base: Path) -> dict:
    return {
        "path": str(path.relative_to(base)),
        "bytes": path.stat().st_size,
        "sha256": pipeline.sha256(path),
    }


def main() -> int:
    final_qa_path = pipeline.BUILD / "qa/final-qa-report.json"
    final_qa = json.loads(final_qa_path.read_text(encoding="utf-8"))
    if final_qa["status"] != "PASS_LOCAL_RENDER_QA_READY_FOR_MIRU_REVIEW":
        raise RuntimeError(f"refusing to freeze non-passing candidate: {final_qa['status']}")
    candidate = pipeline.BUILD / final_qa["candidate"]
    if pipeline.sha256(candidate) != final_qa["candidate_sha256"]:
        raise RuntimeError("candidate changed after final QA")

    gated_inputs = [file_record(pipeline.ROOT / name, pipeline.ROOT) for name in pipeline.expected_input_hashes()]
    build_files = [
        path
        for path in sorted(pipeline.BUILD.rglob("*"))
        if path.is_file()
        and path.name not in EXCLUDE_NAMES
        and "__pycache__" not in path.parts
        and not path.name.startswith(".DS_Store")
    ]
    inventory = [file_record(path, pipeline.BUILD) for path in build_files]
    ffmpeg_version = subprocess.run(["ffmpeg", "-version"], check=True, capture_output=True, text=True).stdout.splitlines()[0]
    ffprobe_version = subprocess.run(["ffprobe", "-version"], check=True, capture_output=True, text=True).stdout.splitlines()[0]
    manifest = {
        "status": "FROZEN_LOCAL_ONLY_READY_FOR_MIRU_REVIEW",
        "created_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "candidate": final_qa["candidate"],
        "candidate_sha256": final_qa["candidate_sha256"],
        "candidate_bytes": final_qa["candidate_bytes"],
        "duration_seconds": final_qa["duration_seconds"],
        "gated_inputs": gated_inputs,
        "build_inventory": inventory,
        "toolchain": {
            "python": platform.python_version(),
            "pillow": __import__("PIL").__version__,
            "ffmpeg": ffmpeg_version,
            "ffprobe": ffprobe_version,
            "tts": {"route": "Hermes managed OpenAI audio gateway", "model": "gpt-4o-mini-tts", "voice": "alloy", "speed": 1.0},
            "asr": {"route": "Hermes managed OpenAI audio gateway", "model": "whisper-1"},
            "visual_pipeline": "local deterministic Pillow cards only",
            "video_pipeline": "local ffmpeg assembly only",
        },
        "qa": {
            "status": final_qa["status"],
            "final_qa_report": file_record(final_qa_path, pipeline.BUILD),
            "asr_status": final_qa["asr_status"],
            "asr_report": final_qa["asr_report"],
            "asr_report_sha256": final_qa["asr_report_sha256"],
            "heading_status": final_qa["heading_status"],
            "heading_report": final_qa["heading_report"],
            "heading_report_sha256": final_qa["heading_report_sha256"],
            "caption_status": final_qa["caption_status"],
            "caption_report": final_qa["caption_report"],
            "caption_report_sha256": final_qa["caption_report_sha256"],
            "forbidden_sweep_status": final_qa["forbidden_sweep_status"],
            "forbidden_sweep_phrases": final_qa["forbidden_sweep_phrases"],
            "forbidden_sweep_hits": final_qa["forbidden_sweep_hits"],
            "full_decode_status": final_qa["full_decode_status"],
        },
        "safety": {
            "publication_state": "LOCAL_ONLY_NOT_UPLOADED",
            "video_generation_services": [],
            "flow_used": False,
            "veo_used": False,
            "credits_spent": 0,
        },
    }
    report_lines = [
        "# Local render build report",
        "",
        f"Status: `{manifest['status']}`",
        f"Candidate: `{manifest['candidate']}`",
        f"SHA-256: `{manifest['candidate_sha256']}`",
        f"Duration: {manifest['duration_seconds']:.3f} seconds",
        "",
        "## QA",
        "",
        f"- Final gate: `{final_qa['status']}`",
        f"- Decoded-audio ASR word diff: `{final_qa['asr_status']}`",
        f"- Encoded card headings: `{final_qa['heading_status']}`",
        f"- Encoded captions: `{final_qa['caption_status']}`",
        f"- Forbidden sweep: `{final_qa['forbidden_sweep_status']}`",
        f"- Full media decode: `{final_qa['full_decode_status']}`",
        f"- Mean/max volume: {final_qa['mean_volume_db']:.1f} / {final_qa['max_volume_db']:.1f} dB",
        "",
        "## Safety and scope",
        "",
        "Local Pillow + ffmpeg pipeline only. Gateway TTS and ASR only. No Veo, no Flow, no credits, no upload.",
        "",
        "Panels 03, 04, 07, 08, and 09 use deterministic, explicitly labeled quantitative geometry; no unlabeled logarithmic compression is used.",
        "",
        "## Deviations from the v1 approach",
        "",
        "No approach deviations. The implementation changes are limited to this lane's 7 hash-pinned gated inputs, Phase 1 graphics, output names, and content-specific ASR normalization.",
        "Gateway stages were invoked with the Hermes checkout virtual-environment Python because the host python3 cannot import the current managed gateway's PEP 604 type syntax; this did not change the v1 media or gateway approach.",
        "",
        "This artifact is ready for Miru render review, not publication.",
    ]
    REPORT.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    manifest["build_report"] = file_record(REPORT, pipeline.BUILD)
    FREEZE.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": manifest["status"], "candidate_sha256": manifest["candidate_sha256"], "inventory_files": len(inventory)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
