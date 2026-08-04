#!/usr/bin/env python3
"""Automated and temporal QA for the overnight-report review master."""
from __future__ import annotations

import json
import re
import subprocess
import tempfile
import wave
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
from PIL import Image, ImageStat

from overnight_content import CAPTION_CUES, DURATION, FPS, NARRATION, SCENE_BOUNDARIES

BASE = Path(__file__).resolve().parent
QA_DIR = BASE / "qa"
QA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT = BASE / "NEBULAMIND_OVERNIGHT_REPORT_V1_FEMALE_VOICE_EXACT_LIPSYNC.mp4"
SRT = BASE / "NEBULAMIND_OVERNIGHT_REPORT_V1_FEMALE_VOICE_EXACT_LIPSYNC.srt"
DRIVER = BASE / "driver_audio/overnight_report_female_exact_narration_73s.wav"
TALKING_HEAD = BASE / "talking_head/overnight_report.mp4"


def probe(path: Path) -> dict:
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration,size:stream=index,codec_type,codec_name,width,height,r_frame_rate,nb_frames,sample_rate,channels",
        "-of", "json", str(path),
    ], text=True))


def decode_four_times(path: Path) -> list[dict]:
    rows = []
    for index in range(1, 5):
        result = subprocess.run([
            "ffmpeg", "-v", "error", "-i", str(path), "-map", "0:v:0", "-f", "null", "-",
        ], capture_output=True, text=True)
        rows.append({"pass": index, "returncode": result.returncode, "stderr": result.stderr.strip()})
    return rows


def driver_pitch(path: Path) -> dict:
    with wave.open(str(path), "rb") as reader:
        rate = reader.getframerate()
        channels = reader.getnchannels()
        signal = np.frombuffer(reader.readframes(reader.getnframes()), dtype="<i2").astype(np.float32) / 32768.0
    if channels > 1:
        signal = signal.reshape(-1, channels).mean(axis=1)
    frame, hop = int(0.05 * rate), int(0.02 * rate)
    low_lag, high_lag = rate // 300, rate // 80
    frames = [signal[start:start + frame] for start in range(0, len(signal) - frame, hop)]
    energies = [float(np.sqrt(np.mean(part * part))) for part in frames]
    threshold = max(0.003, float(np.percentile(energies, 45)))
    values, window = [], np.hanning(frame)
    for part, energy in zip(frames, energies):
        if energy < threshold:
            continue
        centered = (part - part.mean()) * window
        corr = np.correlate(centered, centered, mode="full")[frame - 1:]
        if corr[0] <= 0:
            continue
        lag = low_lag + int(np.argmax(corr[low_lag:high_lag + 1]))
        if corr[lag] / corr[0] >= 0.25:
            values.append(rate / lag)
    pitches = np.asarray(values)
    p10, p90 = np.percentile(pitches, [10, 90])
    trimmed = pitches[(pitches >= p10) & (pitches <= p90)]
    median = float(np.median(trimmed))
    return {"median_f0_hz": round(median, 1), "voiced_frames": int(len(trimmed)), "female_voice_gate": 160 <= median <= 240}


def parse_time(value: str) -> float:
    h, m, rest = value.split(":")
    s, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def normalize(value: str) -> str:
    return " ".join(value.replace("\n", " ").split())


def caption_check() -> dict:
    content = SRT.read_text(encoding="utf-8").strip()
    pattern = re.compile(r"(?m)^(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\n\d+\n|\Z)", re.S)
    cues = pattern.findall(content)
    starts = [parse_time(cue[1]) for cue in cues]
    ends = [parse_time(cue[2]) for cue in cues]
    expected = normalize(" ".join(NARRATION))
    actual = normalize(" ".join(cue[3] for cue in cues))
    line_limits = all(len(line) <= 42 for cue in cues for line in cue[3].splitlines())
    two_line_limit = all(len(cue[3].splitlines()) <= 2 for cue in cues)
    monotonic = all(starts[i] < ends[i] <= starts[i + 1] + 0.002 for i in range(len(cues) - 1))
    return {
        "cue_count": len(cues), "expected_cue_count": sum(map(len, CAPTION_CUES)),
        "exact_narration_text": actual == expected, "line_limit_42": line_limits,
        "max_two_lines": two_line_limit, "monotonic_nonoverlap": monotonic,
        "within_master_duration": bool(cues) and starts[0] >= 0 and ends[-1] <= DURATION,
        "pass": len(cues) == sum(map(len, CAPTION_CUES)) and actual == expected and line_limits and two_line_limit and monotonic and ends[-1] <= DURATION,
    }


def extract_frame(video: Path, when: float, output: Path) -> Image.Image:
    subprocess.run([
        "ffmpeg", "-y", "-v", "error", "-ss", f"{when:.3f}", "-i", str(video), "-frames:v", "1", str(output),
    ], check=True)
    return Image.open(output).convert("RGB")


def make_sheet(name: str, frames: list[Image.Image], cols: int) -> Path:
    thumb = (320, 180)
    rows = (len(frames) + cols - 1) // cols
    sheet = Image.new("RGB", (thumb[0] * cols, thumb[1] * rows), (4, 8, 25))
    for index, frame in enumerate(frames):
        sheet.paste(frame.resize(thumb, Image.Resampling.LANCZOS), ((index % cols) * thumb[0], (index // cols) * thumb[1]))
    path = QA_DIR / name
    sheet.save(path)
    return path


def temporal_review(video: Path) -> dict:
    times = np.linspace(1.0, DURATION - 1.0, 24)
    frames, luminance, presenter_variance = [], [], []
    with tempfile.TemporaryDirectory(prefix="nm_overnight_temporal_") as temp_dir:
        temp = Path(temp_dir)
        for index, when in enumerate(times):
            image = extract_frame(video, float(when), temp / f"{index:02d}.png")
            frames.append(image.copy())
            luminance.append(float(ImageStat.Stat(image.convert("L")).mean[0]))
            presenter_variance.append(float(ImageStat.Stat(image.crop((945, 350, 1279, 719)).convert("L")).var[0]))
    path = make_sheet("temporal_24_sheet.png", frames, 4)
    return {
        "frames_sampled": 24, "sample_times_seconds": [round(float(x), 3) for x in times],
        "sheet": str(path), "mean_luminance_range": [round(min(luminance), 2), round(max(luminance), 2)],
        "presenter_variance_range": [round(min(presenter_variance), 2), round(max(presenter_variance), 2)],
        "nonblank_gate": min(luminance) > 2 and min(presenter_variance) > 5,
    }


def boundary_review(video: Path) -> dict:
    times = []
    for boundary in SCENE_BOUNDARIES[1:-1]:
        times.extend([boundary - 0.08, boundary + 0.08])
    frames = []
    with tempfile.TemporaryDirectory(prefix="nm_overnight_boundaries_") as temp_dir:
        temp = Path(temp_dir)
        for index, when in enumerate(times):
            frames.append(extract_frame(video, when, temp / f"{index:02d}.png").copy())
    path = make_sheet("boundary_10_sheet.png", frames, 5)
    return {"frames_sampled": 10, "times_seconds": times, "sheet": str(path)}


def audio_levels(path: Path) -> dict:
    result = subprocess.run([
        "ffmpeg", "-hide_banner", "-i", str(path), "-map", "0:a:0", "-af", "volumedetect", "-f", "null", "-",
    ], capture_output=True, text=True)
    mean = re.search(r"mean_volume: ([^ ]+ dB)", result.stderr)
    maximum = re.search(r"max_volume: ([^ ]+ dB)", result.stderr)
    return {"returncode": result.returncode, "mean_volume": mean.group(1) if mean else None, "max_volume": maximum.group(1) if maximum else None}


def main() -> None:
    for path in (OUTPUT, SRT, DRIVER, TALKING_HEAD, BASE / "narration_receipt.json"):
        if not path.exists():
            raise FileNotFoundError(path)
    info = probe(OUTPUT)
    stream = next(item for item in info["streams"] if item["codec_type"] == "video")
    duration = float(info["format"]["duration"])
    frames = int(stream.get("nb_frames") or round(duration * FPS))
    decodes = decode_four_times(OUTPUT)
    captions = caption_check()
    pitch = driver_pitch(DRIVER)
    temporal = temporal_review(OUTPUT)
    boundaries = boundary_review(OUTPUT)
    levels = audio_levels(OUTPUT)
    talking_duration = float(probe(TALKING_HEAD)["format"]["duration"])
    narration_receipt = json.loads((BASE / "narration_receipt.json").read_text())
    max_atempo = max(row["atempo"] for row in narration_receipt["scenes"])
    gates = {
        "duration_73_5": abs(duration - DURATION) <= 0.03,
        "resolution_1280x720": stream.get("width") == 1280 and stream.get("height") == 720,
        "frame_rate_24": stream.get("r_frame_rate") == "24/1",
        "frame_count_1764": frames == 1764,
        "decode_pass_4": all(row["returncode"] == 0 and not row["stderr"] for row in decodes),
        "female_pitch": pitch["female_voice_gate"],
        "caption_contract": captions["pass"],
        "temporal_nonblank": temporal["nonblank_gate"],
        "exact_driver_duration": abs(talking_duration - DURATION) <= 0.03,
        "natural_timing": max_atempo <= 1.15,
        "audio_decode": levels["returncode"] == 0 and levels["mean_volume"] is not None,
    }
    receipt = {
        "marker": "NEBULAMIND_OVERNIGHT_REPORT_V1_AUTOMATED_QA_COMPLETE",
        "status": "AWAITING_MANUAL_34_FRAME_VISION_REVIEW",
        "created_kst": datetime.now(ZoneInfo("Asia/Seoul")).isoformat(),
        "output": str(OUTPUT), "probe": info, "duration_seconds": duration, "video_frames": frames,
        "decode_passes": decodes, "pitch": pitch, "captions": captions,
        "temporal_review": temporal, "boundary_review": boundaries, "audio_levels": levels,
        "talking_head_duration_seconds": talking_duration, "maximum_timing_adjustment": max_atempo,
        "automated_gates": gates, "automated_pass": all(gates.values()),
        "manual_visual_review": "PENDING_VISION_REVIEW",
        "publication": {
            "uploaded": False, "website_changed": False, "production_embed_manifest_changed": False,
            "gate": "Explicit user approval required after local review.",
        },
    }
    (BASE / "qa_receipt.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "marker": receipt["marker"], "automated_pass": receipt["automated_pass"],
        "duration": duration, "frames": frames, "pitch_hz": pitch["median_f0_hz"],
        "captions": captions, "audio_levels": levels,
        "temporal_sheet": temporal["sheet"], "boundary_sheet": boundaries["sheet"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
