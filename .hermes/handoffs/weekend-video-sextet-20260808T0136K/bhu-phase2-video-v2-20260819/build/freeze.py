#!/usr/bin/env python3
"""Freeze the passing v2 render and write the build-seat completion receipt."""
from __future__ import annotations

import datetime as dt
import json
import platform
import subprocess
from pathlib import Path

import pipeline


def record(path: Path, base: Path) -> dict:
    return {"path": str(path.relative_to(base)), "bytes": path.stat().st_size, "sha256": pipeline.sha256(path)}


def main() -> int:
    qa_path = pipeline.BUILD / "qa/final-qa-report.json"
    qa = json.loads(qa_path.read_text(encoding="utf-8"))
    if qa["status"] != "PASS_LOCAL_RENDER_QA_READY_FOR_KIMI_REVIEW":
        raise RuntimeError(f"refusing to freeze non-passing render: {qa['status']}")
    if qa["contract_bearing_residual_count"] != 0:
        raise RuntimeError("refusing to freeze contract-bearing ASR residuals")
    candidate = pipeline.BUILD / qa["candidate"]
    if pipeline.sha256(candidate) != qa["candidate_sha256"]:
        raise RuntimeError("candidate changed after final QA")
    narration_wavs = sorted((pipeline.BUILD / "audio").glob("narration*.wav"))
    if len(narration_wavs) != 13:
        raise RuntimeError(f"expected 12 panel narration WAVs plus master, found {len(narration_wavs)}")
    wav_records = [record(path, pipeline.ROOT) for path in narration_wavs]
    pin_receipt = pipeline.BUILD / "qa/asset-pins.json"
    pin_data = json.loads(pin_receipt.read_text(encoding="utf-8"))
    if pin_data["status"] != "PASS_ONE_SHASUM_PER_PIN_BEFORE_EMBEDDING" or len(pin_data["records"]) != 4:
        raise RuntimeError("paper-figure pin receipt is not passing")
    manifest = {
        "status": "FROZEN_LOCAL_ONLY_READY_FOR_KIMI_P2V2_RENDER_GATE",
        "created_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "candidate": record(candidate, pipeline.ROOT),
        "narration_wavs": wav_records,
        "gated_inputs": [record(pipeline.ROOT / name, pipeline.ROOT) for name in pipeline.EXPECTED_HASHES],
        "paper_figure_pins": record(pin_receipt, pipeline.ROOT),
        "qa": record(qa_path, pipeline.ROOT),
        "asr_qa": record(pipeline.ASR_QA, pipeline.ROOT),
        "toolchain": {
            "python": platform.python_version(),
            "pillow": __import__("PIL").__version__,
            "ffmpeg": subprocess.run(["ffmpeg", "-version"], check=True, capture_output=True, text=True).stdout.splitlines()[0],
            "tts": {"route": "Hermes managed OpenAI audio gateway", "model": "gpt-4o-mini-tts", "voice": "alloy", "speed": {"default": 1.14, "panel_overrides": {"02": 1.06, "08": 1.04}}},
            "asr": {"route": "Hermes managed OpenAI audio gateway", "model": "whisper-1"},
            "visuals": "local deterministic Pillow states with local ffmpeg cursor animation, adapted from the prior Phase-2 style base",
            "assembly": "local ffmpeg",
        },
        "safety": {"publication_state": "LOCAL_ONLY_NOT_UPLOADED", "uploads": [], "flow_used": False, "veo_used": False, "image_generation_used": False, "generation_credits_spent": 0, "portal_nersc_used": False, "cockpit_root_audio_writes": False},
    }
    freeze_path = pipeline.BUILD / "FREEZE.json"
    freeze_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    report = [
        "# Local Phase-2 explainer v2 build report", "", f"Status: `{manifest['status']}`",
        f"Candidate: `{manifest['candidate']['path']}`", f"SHA-256: `{manifest['candidate']['sha256']}`",
        f"Duration: {qa['duration_seconds']:.3f} seconds", "", "## QA", "",
        f"- Full decoded-audio gateway ASR: `{qa['asr_status']}`",
        f"- Contract-bearing residuals: {qa['contract_bearing_residual_count']}",
        f"- Cosmetic residuals: {qa['cosmetic_residual_count']}",
        f"- Assertion heading on every decoded state: `{qa['heading_status']}`",
        f"- Encoded captions: `{qa['caption_status']}`",
        f"- Equation projection: `{qa['equation_status']}`",
        f"- Honest no-plots cards: `{qa['no_plots_status']}`",
        f"- Four pinned figures, attributions, walkthroughs: `{qa['plot_status']}`",
        f"- BAND ladders and Planck markers: `{qa['geometry_status']}`",
        f"- Full decode: `{qa['full_decode_status']}`",
        f"- Mean/max volume: {qa['mean_volume_db']:.1f} / {qa['max_volume_db']:.1f} dB", "",
        "## Safety", "", "Local Pillow + ffmpeg pipeline only; Hermes gateway TTS/ASR only. No uploads, Flow, Veo, image-generation credits, or cockpit-root audio writes. portal.nersc.gov was not used.", "",
        "Ready for the Kimi v2 render gate; not publication-authorized.",
    ]
    (pipeline.BUILD / "BUILD_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    done = [
        "GPT3_P2V2_COMPLETE", "", "# GPT3 Phase-2 explainer v2 build receipt", "",
        f"- Candidate: `{manifest['candidate']['path']}`", f"- Candidate SHA-256: `{manifest['candidate']['sha256']}`",
        f"- Duration: `{qa['duration_seconds']:.6f}` seconds (inside 390–480 seconds).",
        f"- Final QA: `{qa['status']}`.",
        f"- Full ASR: `{qa['asr_status']}`; contract-bearing residuals: `0`.",
        f"- Cosmetic ASR residuals: `{qa['cosmetic_residual_count']}`; each is adjudicated in `ASR_QA.md`.",
        f"- Four paper figures: `{qa['plot_status']}`.",
        f"- No-plots cards: `{qa['no_plots_status']}`.",
        f"- Assertion headings: `{qa['heading_status']}`.",
        f"- Exact permitted equations only: `{qa['equation_status']}`.",
        f"- BAND ladders/Planck markers: `{qa['geometry_status']}`.", "", "## Frozen SHA-256 receipts", "",
        f"- `{manifest['candidate']['sha256']}  {manifest['candidate']['path']}`",
    ]
    done.extend(f"- `{item['sha256']}  {item['path']}`" for item in wav_records)
    done.extend(["", "## Final ASR residual judgment", "", f"- Cosmetic residual count: `{qa['cosmetic_residual_count']}` — accepted only as documented ASR representation variance.", "- Contract-bearing residual count: `0` — no number, caveat sentence, Reading-1 clause, repaired F-B two-clause sentence, or verdict residual remains.", "", "## Boundary", "", "Local-only build. No upload or publication. No Flow/Veo/image-generation credits. Audio remained in this lane. portal.nersc.gov untouched.", ""])
    pipeline.DONE.write_text("\n".join(done), encoding="utf-8")
    print(json.dumps({"status": manifest["status"], "candidate_sha256": manifest["candidate"]["sha256"], "narration_wavs": len(wav_records)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
