#!/usr/bin/env python3
"""Assemble staged v3 visuals, exact narration, and captions."""
from __future__ import annotations

import json
import math
import shutil
import subprocess
from pathlib import Path
from typing import Any

import pipeline

FPS = 30
WIDTH = 1920
HEIGHT = 1080
STATE_CROSSFADE_SECONDS = 0.50
OUTPUT = pipeline.BUILD / "BHU_PHASE2_EXPLAINER_V3_LOCAL_REVIEW.mp4"
SRT_OUTPUT = pipeline.BUILD / "BHU_PHASE2_EXPLAINER_V3_LOCAL_REVIEW.srt"
VTT_OUTPUT = pipeline.BUILD / "BHU_PHASE2_EXPLAINER_V3_LOCAL_REVIEW.vtt"


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def ffprobe(path: Path) -> dict[str, Any]:
    result = subprocess.run([
        "ffprobe", "-v", "error", "-show_streams", "-show_format", "-count_frames", "-of", "json", str(path)
    ], check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def validate_media_contract(probe: dict[str, Any], expected_frames: int, expected_duration: float) -> None:
    streams = probe.get("streams", [])
    videos = [s for s in streams if s.get("codec_type") == "video"]
    audios = [s for s in streams if s.get("codec_type") == "audio"]
    subtitles = [s for s in streams if s.get("codec_type") == "subtitle"]
    if len(videos) != 1 or len(audios) != 1 or len(subtitles) != 1:
        raise RuntimeError("candidate must have exactly one video, audio, and subtitle stream")
    video = videos[0]
    counted = int(video.get("nb_read_frames") or video.get("nb_frames") or 0)
    if any([
        video.get("codec_name") != "h264",
        int(video.get("width", 0)) != WIDTH,
        int(video.get("height", 0)) != HEIGHT,
        video.get("r_frame_rate") != f"{FPS}/1",
        counted != expected_frames,
    ]):
        raise RuntimeError(f"video stream contract failed: counted={counted} {video}")
    audio = audios[0]
    if audio.get("codec_name") != "aac" or int(audio.get("sample_rate", 0)) != 48000 or int(audio.get("channels", 0)) != 1:
        raise RuntimeError(f"audio stream contract failed: {audio}")
    subtitle = subtitles[0]
    if subtitle.get("codec_name") != "mov_text" or subtitle.get("tags", {}).get("language") != "eng" or subtitle.get("disposition", {}).get("default") != 1:
        raise RuntimeError(f"subtitle stream contract failed: {subtitle}")
    duration = float(probe.get("format", {}).get("duration", 0.0))
    if not 600 <= duration <= 720 or abs(duration - expected_duration) > 1.0 / FPS + 0.02:
        raise RuntimeError(f"duration contract failed: {duration} expected {expected_duration}")


def split_frames(total: int, weights: list[float]) -> list[int]:
    weight_sum = sum(weights)
    raw = [total * weight / weight_sum for weight in weights]
    frames = [int(value) for value in raw]
    remainder = total - sum(frames)
    order = sorted(range(len(weights)), key=lambda i: raw[i] - frames[i], reverse=True)
    for index in order[:remainder]:
        frames[index] += 1
    if any(value <= 0 for value in frames) or sum(frames) != total:
        raise RuntimeError(f"invalid state split: {frames}")
    return frames


def path_expression(values: list[float], duration: float, cursor_offset: float) -> str:
    if len(values) < 2:
        return f"{values[0]-cursor_offset:.3f}"
    segment = duration / (len(values)-1)
    expression = f"{values[-1]-cursor_offset:.3f}"
    for index in reversed(range(len(values)-1)):
        start = index*segment
        end = (index+1)*segment
        value0 = values[index]-cursor_offset
        delta = values[index+1]-values[index]
        linear = f"{value0:.3f}+({delta:.3f})*(t-{start:.6f})/{segment:.6f}"
        expression = f"if(lt(t,{end:.6f}),{linear},{expression})"
    return expression


def encode_state(source: Path, destination: Path, frames: int, cursor: Path | None, points: list[list[float]]) -> None:
    base = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-loop", "1", "-framerate", str(FPS), "-i", str(source)]
    if cursor is not None and points:
        duration = frames / FPS
        x_expr = path_expression([p[0] for p in points], duration, 48.0)
        y_expr = path_expression([p[1] for p in points], duration, 48.0)
        command = base + [
            "-loop", "1", "-framerate", str(FPS), "-i", str(cursor),
            "-filter_complex", f"[0:v][1:v]overlay=x='{x_expr}':y='{y_expr}':eval=frame:shortest=1,format=yuv420p[v]",
            "-map", "[v]",
        ]
    else:
        command = base + ["-vf", "format=yuv420p"]
    command += [
        "-frames:v", str(frames), "-an", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "15",
        "-pix_fmt", "yuv420p", "-r", str(FPS), "-video_track_timescale", "90000", str(destination),
    ]
    run(command)


def crossfade_panel(segments: list[Path], base_frames: list[int], destination: Path) -> None:
    total_frames = sum(base_frames)
    duration = total_frames / FPS
    inputs: list[str] = []
    for path in segments:
        inputs.extend(["-i", str(path)])
    if len(segments) == 1:
        filters = f"[0:v]fade=t=in:st=0:d=0.35,fade=t=out:st={max(0,duration-.45):.6f}:d=0.45,format=yuv420p[v]"
    else:
        parts: list[str] = []
        previous = "[0:v]"
        offset_frames = base_frames[0]
        for index in range(1, len(segments)):
            out = f"[x{index}]"
            parts.append(f"{previous}[{index}:v]xfade=transition=fade:duration={STATE_CROSSFADE_SECONDS:.6f}:offset={offset_frames/FPS:.6f}{out}")
            previous = out
            offset_frames += base_frames[index]
        parts.append(f"{previous}fade=t=in:st=0:d=0.35,fade=t=out:st={max(0,duration-.45):.6f}:d=0.45,format=yuv420p[v]")
        filters = ";".join(parts)
    run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *inputs,
        "-filter_complex", filters, "-map", "[v]", "-frames:v", str(total_frames),
        "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-r", str(FPS), "-video_track_timescale", "90000", str(destination),
    ])


def main() -> int:
    frozen = pipeline.load_frozen_inputs()
    timeline = json.loads((pipeline.BUILD / "audio/timeline.json").read_text(encoding="utf-8"))
    visuals = json.loads((pipeline.BUILD / "visual-receipt.json").read_text(encoding="utf-8"))
    if not timeline["all_tts_inputs_byte_identical_to_storyboard_narration"]:
        raise RuntimeError("TTS input mirror failed")
    if timeline["voice_was_sped_up"] or not 124.5 <= float(timeline["measured_narration_wpm"]) <= 135.5:
        raise RuntimeError("measured voice-pace contract failed")
    if float(timeline["all_panel_turn_gaps_at_least_seconds"]) < 1.75:
        raise RuntimeError("panel-turn breathing-gap contract failed")
    if not visuals["paper_assets_verified_before_embedding"]:
        raise RuntimeError("paper plots were not pin-verified")
    if visuals["equations_projected_exactly"] != pipeline.EXPECTED_EQUATIONS or visuals["other_equations_projected"]:
        raise RuntimeError("equation projection failed")

    segments_dir = pipeline.BUILD / "segments"
    state_dir = segments_dir / "states"
    panel_dir = segments_dir / "panels"
    state_dir.mkdir(parents=True, exist_ok=True)
    panel_dir.mkdir(parents=True, exist_ok=True)
    cursor = pipeline.BUILD / "cards/plot-cursor.png"
    panel_paths: list[Path] = []
    panel_records: list[dict[str, Any]] = []
    transition_frames = round(STATE_CROSSFADE_SECONDS * FPS)

    for panel, timing, visual in zip(frozen["panels"], timeline["cards"], visuals["panels"]):
        if panel["id"] != timing["card_id"] or panel["id"] != visual["id"]:
            raise RuntimeError("panel order mismatch")
        weights = [float(s["duration_weight"]) for s in visual["states"]]
        base_parts = split_frames(int(timing["frame_count"]), weights)
        state_paths: list[Path] = []
        state_records: list[dict[str, Any]] = []
        for index, (state, base_count) in enumerate(zip(visual["states"], base_parts)):
            source = pipeline.BUILD / state["path"]
            if pipeline.sha256(source) != state["sha256"]:
                raise RuntimeError(f"visual state changed: {source}")
            # Each state except the final one carries the transition tail; the
            # next visual begins exactly on its scheduled narration beat.
            encoded_frames = base_count + (transition_frames if index < len(visual["states"])-1 else 0)
            destination = state_dir / f"panel-{panel['id']}-{state['name']}.mp4"
            encode_state(source, destination, encoded_frames, cursor, state["cursor_points"])
            state_paths.append(destination)
            state_records.append({
                "name": state["name"], "base_frame_count": base_count, "encoded_frame_count": encoded_frames,
                "scheduled_start_seconds": sum(base_parts[:index]) / FPS,
                "source": state["path"], "source_sha256": state["sha256"],
                "segment": str(destination.relative_to(pipeline.BUILD)), "segment_sha256": pipeline.sha256(destination),
                "animated_plot_walkthrough": bool(state["cursor_points"]), "cursor_points": state["cursor_points"],
            })
        panel_path = panel_dir / f"panel-{panel['id']}.mp4"
        crossfade_panel(state_paths, base_parts, panel_path)
        panel_paths.append(panel_path)
        panel_records.append({
            "panel_id": panel["id"], "frame_count": int(timing["frame_count"]),
            "duration_seconds": int(timing["frame_count"]) / FPS,
            "panel_turn_silence_seconds": timing["panel_turn_silence_seconds"],
            "states": state_records, "panel_segment": str(panel_path.relative_to(pipeline.BUILD)),
            "panel_segment_sha256": pipeline.sha256(panel_path),
        })
        print(f"panel {panel['id']}: {len(state_records)} stages, {timing['frame_count']} frames")

    concat = segments_dir / "panels.ffconcat"
    concat.write_text("ffconcat version 1.0\n" + "".join(f"file '{p.as_posix()}'\n" for p in panel_paths), encoding="utf-8")
    video_only = segments_dir / "video-only.mp4"
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", "-movflags", "+faststart", str(video_only)])

    master = pipeline.BUILD / timeline["master_audio"]
    srt = pipeline.BUILD / timeline["srt"]
    vtt = pipeline.BUILD / timeline["vtt"]
    run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(video_only), "-i", str(master), "-i", str(srt),
        "-map", "0:v:0", "-map", "1:a:0", "-map", "2:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-c:s", "mov_text", "-metadata:s:s:0", "language=eng", "-metadata:s:s:0", "title=English",
        "-disposition:s:0", "default", "-t", f"{timeline['master_duration_seconds']:.6f}",
        "-movflags", "+faststart", str(OUTPUT),
    ])
    shutil.copy2(srt, SRT_OUTPUT)
    shutil.copy2(vtt, VTT_OUTPUT)

    probe = ffprobe(OUTPUT)
    expected_frames = sum(int(card["frame_count"]) for card in timeline["cards"])
    validate_media_contract(probe, expected_frames, timeline["master_duration_seconds"])
    receipt = {
        "status": "PASS_LOCAL_V3_ASSEMBLY_PENDING_FULL_FINAL_MP4_ASR",
        "output": str(OUTPUT.relative_to(pipeline.BUILD)), "output_sha256": pipeline.sha256(OUTPUT),
        "output_bytes": OUTPUT.stat().st_size, "duration_seconds": float(probe["format"]["duration"]),
        "frame_count": expected_frames, "resolution": [WIDTH, HEIGHT], "fps": FPS,
        "srt": str(SRT_OUTPUT.relative_to(pipeline.BUILD)), "srt_sha256": pipeline.sha256(SRT_OUTPUT),
        "vtt": str(VTT_OUTPUT.relative_to(pipeline.BUILD)), "vtt_sha256": pipeline.sha256(VTT_OUTPUT),
        "panels": panel_records,
        "animated_plot_walkthrough_states": [
            f"{p['panel_id']}/{s['name']}" for p in panel_records for s in p["states"] if s["animated_plot_walkthrough"]
        ],
        "panel_transition": "fade-through-black entirely inside explicit panel-turn silence; no divider cards",
        "state_transition": f"{STATE_CROSSFADE_SECONDS:.2f}s crossfade beginning exactly at each scheduled stage boundary",
        "publication_state": "LOCAL_ONLY_NOT_UPLOADED", "generation_credits_spent": 0,
    }
    (pipeline.BUILD / "assembly-receipt.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({key: receipt[key] for key in ("status", "output", "output_sha256", "duration_seconds", "output_bytes", "animated_plot_walkthrough_states")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
