#!/usr/bin/env python3
"""Assemble deterministic cards, exact gateway narration, and captions with ffmpeg."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

import pipeline

FPS = 30
WIDTH = 1920
HEIGHT = 1080
OUTPUT = pipeline.BUILD / "BHU_PHASE2_RESULTS_VIDEO_LOCAL_REVIEW.mp4"
SRT_OUTPUT = pipeline.BUILD / "BHU_PHASE2_RESULTS_VIDEO_LOCAL_REVIEW.srt"
VTT_OUTPUT = pipeline.BUILD / "BHU_PHASE2_RESULTS_VIDEO_LOCAL_REVIEW.vtt"


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def ffprobe(path: Path) -> dict[str, Any]:
    result = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)], check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def validate_media_contract(probe: dict[str, Any], expected_frames: int, expected_duration: float) -> None:
    streams = probe.get("streams", [])
    videos = [stream for stream in streams if stream.get("codec_type") == "video"]
    audios = [stream for stream in streams if stream.get("codec_type") == "audio"]
    subtitles = [stream for stream in streams if stream.get("codec_type") == "subtitle"]
    if len(videos) != 1 or len(audios) != 1 or len(subtitles) != 1:
        raise RuntimeError("candidate must contain exactly one video, audio, and subtitle stream")
    video = videos[0]
    if video.get("codec_name") != "h264" or video.get("width") != WIDTH or video.get("height") != HEIGHT or video.get("r_frame_rate") != f"{FPS}/1" or int(video.get("nb_frames", 0)) != expected_frames:
        raise RuntimeError(f"video stream contract failed: {video}")
    audio = audios[0]
    if audio.get("codec_name") != "aac" or int(audio.get("sample_rate", 0)) != 48000 or int(audio.get("channels", 0)) != 1:
        raise RuntimeError(f"audio stream contract failed: {audio}")
    subtitle = subtitles[0]
    if subtitle.get("codec_name") != "mov_text" or subtitle.get("tags", {}).get("language") != "eng" or subtitle.get("disposition", {}).get("default") != 1:
        raise RuntimeError(f"subtitle stream contract failed: {subtitle}")
    duration = float(probe.get("format", {}).get("duration", 0.0))
    if not 240.0 <= duration <= 360.0 or abs(duration - expected_duration) > 1.0 / FPS:
        raise RuntimeError(f"duration contract failed: {duration}")


def main() -> int:
    frozen = pipeline.load_frozen_inputs()
    timeline_path = pipeline.BUILD / "audio/timeline.json"
    audit_path = pipeline.BUILD / "qa/card-text-and-geometry-audit.json"
    timeline = json.loads(timeline_path.read_text(encoding="utf-8"))
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    if not timeline["all_tts_inputs_byte_identical_to_storyboard_narration"]:
        raise RuntimeError("TTS inputs are not byte-identical to storyboard narration")
    if timeline["gated_storyboard_sha256"] != pipeline.sha256(pipeline.STORYBOARD) or timeline["gated_script_sha256"] != pipeline.sha256(pipeline.SCRIPT):
        raise RuntimeError("audio timeline frozen-input hash mismatch")
    for card, panel in zip(audit["cards"], frozen["panels"]):
        source = pipeline.BUILD / card["path"]
        if pipeline.sha256(source) != card["sha256"] or card["heading"] != panel["assertion_heading"] or card["text_contract_status"] != "PASS_EXACT_CLOSED_WORLD":
            raise RuntimeError(f"source card contract failed: {panel['id']}")

    segments = pipeline.BUILD / "segments"
    segments.mkdir(parents=True, exist_ok=True)
    segment_paths: list[Path] = []
    segment_records: list[dict[str, Any]] = []
    for panel, timing in zip(frozen["panels"], timeline["cards"]):
        card = pipeline.BUILD / f"cards/card-{panel['id']}.png"
        segment = segments / f"card-{panel['id']}.mp4"
        frames = int(timing["frame_count"])
        run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-loop", "1", "-framerate", str(FPS), "-i", str(card), "-frames:v", str(frames), "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), "-video_track_timescale", "90000", str(segment)])
        segment_paths.append(segment)
        segment_records.append({"card_id": panel["id"], "frame_count": frames, "effective_seconds": timing["effective_seconds"], "path": str(segment.relative_to(pipeline.BUILD)), "sha256": pipeline.sha256(segment)})
    concat = segments / "segments.ffconcat"
    concat.write_text("ffconcat version 1.0\n" + "".join(f"file '{path.as_posix()}'\n" for path in segment_paths), encoding="utf-8")
    video_only = segments / "video-only.mp4"
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", "-movflags", "+faststart", str(video_only)])

    master = pipeline.BUILD / timeline["master_audio"]
    srt = pipeline.BUILD / timeline["srt"]
    vtt = pipeline.BUILD / timeline["vtt"]
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(video_only), "-i", str(master), "-i", str(srt), "-map", "0:v:0", "-map", "1:a:0", "-map", "2:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-c:s", "mov_text", "-metadata:s:s:0", "language=eng", "-metadata:s:s:0", "title=English", "-disposition:s:0", "default", "-t", f"{timeline['master_duration_seconds']:.6f}", "-movflags", "+faststart", str(OUTPUT)])
    shutil.copy2(srt, SRT_OUTPUT)
    shutil.copy2(vtt, VTT_OUTPUT)

    probe = ffprobe(OUTPUT)
    expected_frames = sum(int(card["frame_count"]) for card in timeline["cards"])
    validate_media_contract(probe, expected_frames, timeline["master_duration_seconds"])
    qa = pipeline.BUILD / "qa"
    qa.mkdir(exist_ok=True)
    (qa / "final-ffprobe.json").write_text(json.dumps(probe, indent=2) + "\n", encoding="utf-8")
    receipt = {
        "status": "PASS_LOCAL_ASSEMBLY_PENDING_FULL_GATEWAY_ASR",
        "output": str(OUTPUT.relative_to(pipeline.BUILD)),
        "output_sha256": pipeline.sha256(OUTPUT),
        "output_bytes": OUTPUT.stat().st_size,
        "duration_seconds": float(probe["format"]["duration"]),
        "frame_count": expected_frames,
        "resolution": [WIDTH, HEIGHT],
        "fps": FPS,
        "srt": str(SRT_OUTPUT.relative_to(pipeline.BUILD)),
        "srt_sha256": pipeline.sha256(SRT_OUTPUT),
        "vtt": str(VTT_OUTPUT.relative_to(pipeline.BUILD)),
        "vtt_sha256": pipeline.sha256(VTT_OUTPUT),
        "segments": segment_records,
        "publication_state": "LOCAL_ONLY_NOT_UPLOADED",
        "credits_spent": 0,
    }
    (qa / "assembly-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: receipt[key] for key in ("status", "output", "output_sha256", "duration_seconds", "output_bytes")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
