#!/usr/bin/env python3
"""Freeze the completed v3 MP4, 16 narration WAVs, and 16 panel stills."""
from __future__ import annotations

import json
from pathlib import Path

import pipeline


def main() -> int:
    qa_path = pipeline.BUILD / "qa/final-qa-report.json"
    qa = json.loads(qa_path.read_text(encoding="utf-8"))
    if qa["status"] != "PASS_LOCAL_V3_RENDER_QA_READY_FOR_BOUNDED_KIMI_GATE":
        raise RuntimeError(f"refusing freeze before clean final QA: {qa['status']}")
    if qa["contract_bearing_residual_count"] != 0:
        raise RuntimeError("refusing freeze with contract-bearing ASR residuals")
    candidate = pipeline.BUILD / qa["candidate"]
    if pipeline.sha256(candidate) != qa["candidate_sha256"]:
        raise RuntimeError("candidate changed after final QA")
    timeline = json.loads((pipeline.BUILD / "audio/timeline.json").read_text(encoding="utf-8"))
    visuals = json.loads((pipeline.BUILD / "visual-receipt.json").read_text(encoding="utf-8"))
    wavs = []
    for item in timeline["panel_wavs"]:
        path = pipeline.BUILD / item["audio"]
        digest = pipeline.sha256(path)
        if digest != item["audio_sha256"]:
            raise RuntimeError(f"narration changed before freeze: {path}")
        wavs.append({"panel_id": item["panel_id"], "path": item["audio"], "sha256": digest, "bytes": path.stat().st_size})
    stills = []
    for panel in visuals["panels"]:
        path = pipeline.BUILD / panel["representative_still"]
        digest = pipeline.sha256(path)
        if digest != panel["representative_still_sha256"]:
            raise RuntimeError(f"still changed before freeze: {path}")
        stills.append({"panel_id": panel["id"], "path": panel["representative_still"], "sha256": digest, "bytes": path.stat().st_size})
    if len(wavs) != 16 or len(stills) != 16:
        raise RuntimeError("freeze requires 16 WAVs and 16 stills")
    freeze = {
        "status": "GPT3_F_COMPLETE",
        "candidate": {"path": str(candidate.relative_to(pipeline.ROOT)), "sha256": pipeline.sha256(candidate), "bytes": candidate.stat().st_size},
        "duration_seconds": qa["duration_seconds"], "resolution": qa["resolution"], "fps": qa["fps"],
        "narration_model": timeline["model"], "narration_voice": timeline["voice"], "narration_speed": timeline["speed"],
        "voice_was_sped_up": timeline["voice_was_sped_up"], "measured_narration_wpm": timeline["measured_narration_wpm"],
        "minimum_panel_turn_silence_seconds": timeline["all_panel_turn_gaps_at_least_seconds"],
        "asr_status": qa["asr_status"], "contract_bearing_residual_count": qa["contract_bearing_residual_count"],
        "cosmetic_residual_count": qa["cosmetic_residual_count"], "narration_wavs": wavs, "panel_stills": stills,
        "packet_gate": pipeline.load_frozen_inputs()["gate_token"], "publication_state": "LOCAL_ONLY_NOT_UPLOADED",
        "generation_credits_spent": 0,
    }
    freeze_path = pipeline.BUILD / "FREEZE.json"
    freeze_path.write_text(json.dumps(freeze, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "GPT3_F_COMPLETE", "",
        "# GPT3 build-seat completion — BHU Phase 2 explainer v3", "",
        f"Packet gate: `{freeze['packet_gate']}`",
        f"Final MP4: `{freeze['candidate']['path']}`",
        f"Final MP4 SHA-256: `{freeze['candidate']['sha256']}`",
        f"Final MP4 bytes: `{freeze['candidate']['bytes']}`",
        f"Duration: `{freeze['duration_seconds']:.3f} s` ({freeze['duration_seconds']/60:.3f} min)",
        f"Media: `{freeze['resolution'][0]}x{freeze['resolution'][1]}` at `{freeze['fps']} fps`", "",
        "## Final QA judgment", "",
        f"- Overall: `{qa['status']}`",
        f"- Full final-MP4 ASR: `{freeze['asr_status']}`",
        f"- Cosmetic residuals: `{freeze['cosmetic_residual_count']}`",
        f"- Contract-bearing residuals: `{freeze['contract_bearing_residual_count']}` — none accepted",
        f"- Captions: `{qa['caption_status']}`",
        f"- Plot walkthroughs: `{qa['plot_status']}`",
        f"- Stills: `{qa['still_status']}`",
        f"- Equations: `{qa['equation_status']}`",
        f"- Full decode: `{qa['full_decode_status']}`", "",
        "Judgment: every residual reported by ASR is explicitly classified cosmetic versus contract-bearing in `ASR_QA.md`. The freeze is permitted only because contract-bearing residuals are zero.", "",
        "## Narration contract", "",
        f"- Gateway model / voice: `{freeze['narration_model']}` / `{freeze['narration_voice']}`",
        f"- TTS speed parameter: `{freeze['narration_speed']}`; voice sped up: `{freeze['voice_was_sped_up']}`",
        f"- Measured narration-only pace: `{freeze['measured_narration_wpm']:.3f} wpm`",
        f"- Explicit panel-turn silence floor: `{freeze['minimum_panel_turn_silence_seconds']:.3f} s`",
        "- All 16 TTS input strings are byte-identical to `STORYBOARD.json`.", "",
        "## Frozen narration WAV SHA-256", "",
    ]
    lines.extend(f"- Panel {item['panel_id']}: `{item['sha256']}`  `{item['path']}`" for item in wavs)
    lines.extend(["", "## Frozen representative panel-still SHA-256", ""])
    lines.extend(f"- Panel {item['panel_id']}: `{item['sha256']}`  `{item['path']}`" for item in stills)
    lines.extend(["", "## Boundary", "", "Local-only review artifact. No upload, publication, deploy, cockpit write, database write, git write, generation-credit spend, or portal.nersc.gov access occurred.", ""])
    pipeline.DONE.write_text("\n".join(lines), encoding="utf-8")
    if pipeline.DONE.read_text(encoding="utf-8").splitlines()[0] != "GPT3_F_COMPLETE":
        raise RuntimeError("completion marker write failed")
    print(json.dumps({"status": freeze["status"], "mp4_sha256": freeze["candidate"]["sha256"], "wavs": len(wavs), "stills": len(stills), "done": str(pipeline.DONE)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
