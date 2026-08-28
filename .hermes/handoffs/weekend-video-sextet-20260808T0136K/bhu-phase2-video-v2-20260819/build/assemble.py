#!/usr/bin/env python3
"""Assemble deterministic animated panel states, exact narration, and captions."""
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
OUTPUT = pipeline.BUILD / "BHU_PHASE2_EXPLAINER_V2_LOCAL_REVIEW.mp4"
SRT_OUTPUT = pipeline.BUILD / "BHU_PHASE2_EXPLAINER_V2_LOCAL_REVIEW.srt"
VTT_OUTPUT = pipeline.BUILD / "BHU_PHASE2_EXPLAINER_V2_LOCAL_REVIEW.vtt"


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
    if not 390.0 <= duration <= 480.0 or abs(duration - expected_duration) > 1.0 / FPS:
        raise RuntimeError(f"duration contract failed: {duration}")


def split_frames(total: int, weights: list[float]) -> list[int]:
    raw = [total * weight for weight in weights]
    frames = [int(value) for value in raw]
    remainder = total - sum(frames)
    order = sorted(range(len(weights)), key=lambda index: raw[index] - frames[index], reverse=True)
    for index in order[:remainder]:
        frames[index] += 1
    if any(value <= 0 for value in frames) or sum(frames) != total:
        raise RuntimeError(f"invalid state frame split: total={total}, weights={weights}, frames={frames}")
    return frames


def path_expression(values: list[float], duration: float, cursor_offset: float) -> str:
    if len(values) < 2:
        return f"{values[0] - cursor_offset:.3f}"
    segment = duration / (len(values) - 1)
    expression = f"{values[-1] - cursor_offset:.3f}"
    for index in reversed(range(len(values) - 1)):
        start = index * segment
        end = (index + 1) * segment
        value0 = values[index] - cursor_offset
        delta = values[index + 1] - values[index]
        linear = f"{value0:.3f}+({delta:.3f})*(t-{start:.6f})/{segment:.6f}"
        expression = f"if(lt(t,{end:.6f}),{linear},{expression})"
    return expression


def encode_state(source: Path, destination: Path, frames: int, cursor: Path | None, points: list[list[float]]) -> None:
    base = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-loop", "1", "-framerate", str(FPS), "-i", str(source)]
    if cursor is not None and points:
        duration = frames / FPS
        x_expr = path_expression([point[0] for point in points], duration, 32.0)
        y_expr = path_expression([point[1] for point in points], duration, 32.0)
        command = base + [
            "-loop", "1", "-framerate", str(FPS), "-i", str(cursor),
            "-filter_complex", f"[0:v][1:v]overlay=x='{x_expr}':y='{y_expr}':eval=frame:shortest=1,format=yuv420p[v]",
            "-map", "[v]",
        ]
    else:
        command = base + ["-vf", "format=yuv420p"]
    command += [
        "-frames:v", str(frames), "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-r", str(FPS), "-video_track_timescale", "90000", str(destination),
    ]
    run(command)


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
    if not audit["paper_assets_verified_before_embedding"]:
        raise RuntimeError("paper assets were not pin-verified before embedding")

    segments = pipeline.BUILD / "segments"
    segments.mkdir(parents=True, exist_ok=True)
    cursor = pipeline.BUILD / audit["cursor_asset"]
    state_paths: list[Path] = []
    panel_records: list[dict[str, Any]] = []
    for panel, timing, panel_audit in zip(frozen["panels"], timeline["cards"], audit["panels"]):
        if panel_audit["id"] != panel["id"] or panel_audit["heading"] != panel["assertion_heading"] or panel_audit["text_contract_status"] != "PASS_EXACT_CLOSED_WORLD_ACROSS_PANEL_STATES":
            raise RuntimeError(f"source state contract failed: {panel['id']}")
        weights = [float(state["duration_weight"]) for state in panel_audit["states"]]
        frame_parts = split_frames(int(timing["frame_count"]), weights)
        state_records = []
        for state, frames in zip(panel_audit["states"], frame_parts):
            source = pipeline.BUILD / state["path"]
            if pipeline.sha256(source) != state["sha256"]:
                raise RuntimeError(f"source state changed before assembly: {source}")
            destination = segments / f"panel-{panel['id']}-{state['name']}.mp4"
            encode_state(source, destination, frames, cursor, state["cursor_points"])
            state_paths.append(destination)
            state_records.append({
                "name": state["name"],
                "frame_count": frames,
                "duration_seconds": frames / FPS,
                "source": str(source.relative_to(pipeline.BUILD)),
                "source_sha256": state["sha256"],
                "segment": str(destination.relative_to(pipeline.BUILD)),
                "segment_sha256": pipeline.sha256(destination),
                "animated_walkthrough_cursor": bool(state["cursor_points"]),
                "cursor_points": state["cursor_points"],
            })
        panel_records.append({"panel_id": panel["id"], "frame_count": int(timing["frame_count"]), "states": state_records})

    concat = segments / "states.ffconcat"
    concat.write_text("ffconcat version 1.0\n" + "".join(f"file '{path.as_posix()}'\n" for path in state_paths), encoding="utf-8")
    video_only = segments / "video-only.mp4"
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", "-movflags", "+faststart", str(video_only)])

    master = pipeline.BUILD / timeline["master_audio"]
    srt = pipeline.BUILD / timeline["srt"]
    vtt = pipeline.BUILD / timeline["vtt"]
    run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(video_only), "-i", str(master), "-i", str(srt),
        "-map", "0:v:0", "-map", "1:a:0", "-map", "2:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-c:s", "mov_text", "-metadata:s:s:0", "language=eng", "-metadata:s:s:0", "title=English", "-disposition:s:0", "default",
        "-t", f"{timeline['master_duration_seconds']:.6f}", "-movflags", "+faststart", str(OUTPUT),
    ])
    shutil.copy2(srt, SRT_OUTPUT)
    shutil.copy2(vtt, VTT_OUTPUT)

    probe = ffprobe(OUTPUT)
    expected_frames = sum(int(card["frame_count"]) for card in timeline["cards"])
    validate_media_contract(probe, expected_frames, timeline["master_duration_seconds"])
    qa = pipeline.BUILD / "qa"
    qa.mkdir(exist_ok=True)
    (qa / "final-ffprobe.json").write_text(json.dumps(probe, indent=2) + "\n", encoding="utf-8")
    receipt = {
        "status": "PASS_LOCAL_ANIMATED_ASSEMBLY_PENDING_FULL_GATEWAY_ASR",
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
        "panels": panel_records,
        "animated_plot_walkthrough_states": ["04/plot", "05/plot", "10/figure1", "10/figure2"],
        "publication_state": "LOCAL_ONLY_NOT_UPLOADED",
        "credits_spent": 0,
    }
    (qa / "assembly-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: receipt[key] for key in ("status", "output", "output_sha256", "duration_seconds", "output_bytes")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
