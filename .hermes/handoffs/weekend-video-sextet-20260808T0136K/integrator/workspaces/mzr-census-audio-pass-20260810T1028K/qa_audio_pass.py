#!/usr/bin/env python3
"""Exact fixed-visual QA for the MZR-census audio-pass candidate."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import wave
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

RATE = 48_000


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(command, check=True, **kwargs)


def ffprobe(path: Path) -> dict:
    result = run(
        [
            "ffprobe", "-v", "error", "-count_frames", "-show_entries",
            "format=start_time,duration,size,bit_rate:stream=index,codec_name,codec_type,width,height,"
            "avg_frame_rate,sample_rate,channels,start_time,duration,nb_frames,nb_read_frames,time_base",
            "-of", "json", str(path),
        ],
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def ebur128(path: Path, evidence_path: Path) -> dict:
    result = run(
        [
            "ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
            "-filter_complex", "ebur128=peak=true", "-f", "null", "-",
        ],
        capture_output=True,
        text=True,
    )
    evidence_path.write_text(result.stderr)
    summary = result.stderr.rsplit("Summary:", 1)[-1]
    integrated_match = re.search(r"I:\s*([-0-9.]+) LUFS", summary)
    lra_match = re.search(r"LRA:\s*([-0-9.]+) LU", summary)
    peak_match = re.search(r"Peak:\s*([-0-9.]+) dBFS", summary)
    if not (integrated_match and lra_match and peak_match):
        raise RuntimeError("could not parse ebur128 summary")
    return {
        "integrated_lufs": float(integrated_match.group(1)),
        "lra_lu": float(lra_match.group(1)),
        "true_peak_dbtp": float(peak_match.group(1)),
    }


def silence_intervals(path: Path, evidence_path: Path) -> list[dict]:
    result = run(
        [
            "ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
            "-af", "silencedetect=noise=-35dB:d=0.5", "-f", "null", "-",
        ],
        capture_output=True,
        text=True,
    )
    evidence_path.write_text(result.stderr)
    starts = [float(value) for value in re.findall(r"silence_start: ([0-9.]+)", result.stderr)]
    ends = [float(value) for value in re.findall(r"silence_end: ([0-9.]+)", result.stderr)]
    durations = [float(value) for value in re.findall(r"silence_duration: ([0-9.]+)", result.stderr)]
    if not (len(starts) == len(ends) == len(durations)):
        raise RuntimeError("output silence intervals are not paired")
    return [
        {"start_seconds": start, "end_seconds": end, "duration_seconds": duration}
        for start, end, duration in zip(starts, ends, durations)
    ]


def ffmpeg_stream_hash(path: Path, arguments: list[str]) -> str:
    process = subprocess.Popen(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(path), *arguments, "-"],
        stdout=subprocess.PIPE,
    )
    assert process.stdout is not None
    digest = hashlib.sha256()
    while True:
        chunk = process.stdout.read(1024 * 1024)
        if not chunk:
            break
        digest.update(chunk)
    if process.wait() != 0:
        raise RuntimeError(f"ffmpeg stream hash failed: {path}")
    return digest.hexdigest()


def packet_timing_hash(path: Path) -> str:
    result = run(
        [
            "ffprobe", "-v", "error", "-select_streams", "v:0", "-show_packets",
            "-show_entries", "packet=pts,dts,duration,size,flags", "-of", "compact=p=0:nk=1",
            str(path),
        ],
        capture_output=True,
    )
    return hashlib.sha256(result.stdout).hexdigest()


def read_wav(path: Path) -> np.ndarray:
    with wave.open(str(path), "rb") as handle:
        if (handle.getnchannels(), handle.getframerate(), handle.getsampwidth()) != (1, RATE, 2):
            raise RuntimeError(f"unexpected PCM format: {path}")
        return np.frombuffer(handle.readframes(handle.getnframes()), dtype="<i2").astype(np.float64)


def correlation(left: np.ndarray, right: np.ndarray) -> float:
    if len(left) != len(right) or not len(left):
        raise RuntimeError("correlation arrays are incompatible")
    left = left - left.mean()
    right = right - right.mean()
    denominator = float(np.linalg.norm(left) * np.linalg.norm(right))
    return float(np.dot(left, right) / denominator) if denominator else 1.0


def subtitle_text(path: Path) -> str:
    lines = []
    for line in path.read_text().splitlines():
        stripped = line.strip()
        if not stripped or stripped.isdigit() or " --> " in stripped:
            continue
        lines.append(stripped)
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace")
    parser.add_argument("handoff_root")
    args = parser.parse_args()
    workspace = Path(args.workspace).resolve()
    handoff_root = Path(args.handoff_root).resolve()
    qa_dir = workspace / "qa" / "final"
    qa_dir.mkdir(parents=True, exist_ok=True)

    config = json.loads((workspace / "AUDIO_PASS_CONFIG.json").read_text())
    build = json.loads((workspace / "BUILD_RECEIPT.json").read_text())
    edit_timeline = json.loads((workspace / "audio/AUDIO_EDIT_TIMELINE.json").read_text())
    predecessor = config["predecessor"]
    source_video = handoff_root / predecessor["video_path"]
    output_video = workspace / config["output"]["video_filename"]
    source_master = workspace / predecessor["narration_master_path"]
    final_master = workspace / "audio/narration_master_audio_pass.wav"
    source_timeline = workspace / predecessor["timeline_path"]

    if sha256(source_video) != predecessor["video_sha256"]:
        raise RuntimeError("predecessor video changed before QA")
    if sha256(source_master) != predecessor["narration_master_sha256"]:
        raise RuntimeError("source narration master changed before QA")
    if sha256(source_timeline) != predecessor["timeline_sha256"]:
        raise RuntimeError("source visual timeline changed before QA")
    if sha256(output_video) != build["output_video_sha256"]:
        raise RuntimeError("output hash does not match build receipt")

    run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(output_video),
            "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-",
        ]
    )
    source_probe = ffprobe(source_video)
    output_probe = ffprobe(output_video)
    source_streams = {stream["codec_type"]: stream for stream in source_probe["streams"]}
    output_streams = {stream["codec_type"]: stream for stream in output_probe["streams"]}

    source_h264 = ffmpeg_stream_hash(source_video, ["-map", "0:v:0", "-c:v", "copy", "-f", "h264"])
    output_h264 = ffmpeg_stream_hash(output_video, ["-map", "0:v:0", "-c:v", "copy", "-f", "h264"])
    source_framemd5 = ffmpeg_stream_hash(source_video, ["-map", "0:v:0", "-f", "framemd5"])
    output_framemd5 = ffmpeg_stream_hash(output_video, ["-map", "0:v:0", "-f", "framemd5"])
    source_packet_timing = packet_timing_hash(source_video)
    output_packet_timing = packet_timing_hash(output_video)

    loudness = ebur128(output_video, qa_dir / "output_ebur128.txt")
    silences = silence_intervals(output_video, qa_dir / "output_silence.txt")

    output_gap_rows = []
    listed_pairs = {
        (row["from"], row["to"]) for row in config["seam_policy"]["listed_routine_seams"]
    }
    deliberate_pairs = {
        (row["from"], row["to"])
        for row in config["seam_policy"]["deliberate_visual_breaths_preserved"]
    }
    cap = float(config["seam_policy"]["routine_gap_cap_seconds"])
    for derivation in edit_timeline["per_gap_derivations"]:
        index = derivation["index"]
        current = edit_timeline["records"][index]
        following = edit_timeline["records"][index + 1]
        current_end = float(current["new_audio_end_seconds"])
        following_start = float(following["new_audio_start_seconds"])
        matches = [
            interval for interval in silences
            if interval["start_seconds"] <= current_end + 0.35
            and interval["end_seconds"] >= following_start - 0.35
        ]
        if len(matches) != 1:
            raise RuntimeError(f"could not bind output silence to {derivation['from']}->{derivation['to']}: {matches}")
        pair = (derivation["from"], derivation["to"])
        classification = (
            "listed_routine_seam"
            if pair in listed_pairs
            else "deliberate_visual_breath_preserved"
            if pair in deliberate_pairs
            else "routine_seam_supporting_redistribution"
        )
        output_gap_rows.append(
            {
                "from": pair[0],
                "to": pair[1],
                "classification": classification,
                "source_measured_silence_seconds": derivation["duration_seconds"],
                "derived_post_edit_silence_seconds": derivation["derived_post_edit_silence_seconds"],
                "output_measured_silence_seconds": matches[0]["duration_seconds"],
                "output_silence_start_seconds": matches[0]["start_seconds"],
                "output_silence_end_seconds": matches[0]["end_seconds"],
                "measurement_minus_derivation_seconds": matches[0]["duration_seconds"] - derivation["derived_post_edit_silence_seconds"],
            }
        )

    listed_rows = [row for row in output_gap_rows if row["classification"] == "listed_routine_seam"]
    deliberate_rows = [row for row in output_gap_rows if row["classification"] == "deliberate_visual_breath_preserved"]
    other_routine_rows = [row for row in output_gap_rows if row["classification"] == "routine_seam_supporting_redistribution"]

    source_pcm = read_wav(source_master)
    final_pcm = read_wav(final_master)
    sentence_correlations = []
    for row in edit_timeline["records"]:
        source_start = round(float(row["original_audio_start_seconds"]) * RATE)
        source_end = round(float(row["original_audio_end_seconds"]) * RATE)
        output_start = round(float(row["new_audio_start_seconds"]) * RATE)
        output_end = round(float(row["new_audio_end_seconds"]) * RATE)
        value = correlation(source_pcm[source_start:source_end], final_pcm[output_start:output_end])
        sentence_correlations.append({"id": row["id"], "correlation": value})

    source_srt = workspace / "source_snapshot/subtitles.srt"
    output_srt = workspace / "subtitles_audio_pass.srt"
    target = config["audio_target"]
    checks = {
        "source_video_hash_unchanged": sha256(source_video) == predecessor["video_sha256"],
        "source_visual_timeline_hash_unchanged": sha256(source_timeline) == predecessor["timeline_sha256"],
        "source_audio_master_hash_unchanged": sha256(source_master) == predecessor["narration_master_sha256"],
        "full_h264_aac_decode_pass": True,
        "video_h264_1920x1080_30fps": output_streams["video"]["codec_name"] == "h264" and [output_streams["video"]["width"], output_streams["video"]["height"]] == [1920, 1080] and output_streams["video"]["avg_frame_rate"] == "30/1",
        "video_frame_count_unchanged": output_streams["video"]["nb_read_frames"] == source_streams["video"]["nb_read_frames"] == "6899",
        "h264_elementary_stream_identical": source_h264 == output_h264,
        "decoded_frame_hash_timeline_identical": source_framemd5 == output_framemd5,
        "video_packet_timing_identical": source_packet_timing == output_packet_timing,
        "format_duration_unchanged": output_probe["format"]["duration"] == source_probe["format"]["duration"],
        "audio_aac_48khz_mono_start_zero": output_streams["audio"]["codec_name"] == "aac" and output_streams["audio"]["sample_rate"] == "48000" and output_streams["audio"]["channels"] == 1 and float(output_streams["audio"]["start_time"]) == 0.0,
        "integrated_loudness_exact_target": loudness["integrated_lufs"] == float(target["integrated_lufs"]),
        "lra_inside_authoritative_band": float(target["lra_allowed_lu"][0]) <= loudness["lra_lu"] <= float(target["lra_allowed_lu"][1]),
        "true_peak_at_or_below_authoritative_ceiling": loudness["true_peak_dbtp"] <= float(target["true_peak_ceiling_dbtp"]),
        "six_listed_routine_seams_in_3p5_to_4p0_band": len(listed_rows) == 6 and all(3.5 <= row["output_measured_silence_seconds"] <= 4.0 for row in listed_rows),
        "other_routine_seams_at_or_below_4p0": all(row["output_measured_silence_seconds"] <= 4.0 for row in other_routine_rows),
        "two_deliberate_visual_breaths_preserved": len(deliberate_rows) == 2 and all(abs(row["output_measured_silence_seconds"] - row["source_measured_silence_seconds"]) <= 0.05 for row in deliberate_rows),
        "visual_card_windows_explicitly_unchanged": all(row["visual_card_window_seconds_unchanged"] is True for row in edit_timeline["records"]),
        "all_audio_shifts_disclosed": max(row["audio_shift_relative_to_fixed_visual_seconds"] for row in edit_timeline["records"]) == edit_timeline["maximum_audio_shift_relative_to_fixed_visual_seconds"],
        "sentence_text_unchanged": subtitle_text(source_srt) == subtitle_text(output_srt),
        "all_sentence_waveform_correlations_above_0p97": min(row["correlation"] for row in sentence_correlations) >= 0.97,
        "video_reportable_now_false": build["video_reportable_now"] is False,
        "all_external_gates_closed": all(value is False for value in build["gates"].values()),
    }

    report = {
        "qa_id": "MZR_CENSUS_AUDIO_PASS_EXACT_QA_V1_20260810T1028K",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "PASS" if all(checks.values()) else "HOLD",
        "source_video": str(source_video),
        "source_video_sha256": sha256(source_video),
        "output_video": output_video.name,
        "output_video_sha256": sha256(output_video),
        "source_probe": source_probe,
        "output_probe": output_probe,
        "visual_identity": {
            "source_h264_sha256": source_h264,
            "output_h264_sha256": output_h264,
            "source_framemd5_stream_sha256": source_framemd5,
            "output_framemd5_stream_sha256": output_framemd5,
            "source_video_packet_timing_sha256": source_packet_timing,
            "output_video_packet_timing_sha256": output_packet_timing,
        },
        "loudness": loudness,
        "gap_rows": output_gap_rows,
        "sentence_correlations": sentence_correlations,
        "minimum_sentence_correlation": min(row["correlation"] for row in sentence_correlations),
        "maximum_disclosed_audio_shift_relative_to_fixed_visual_seconds": edit_timeline["maximum_audio_shift_relative_to_fixed_visual_seconds"],
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
    }
    report_path = workspace / "EXACT_QA.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    if report["status"] != "PASS":
        raise RuntimeError(f"QA HOLD: {[key for key, value in checks.items() if not value]}")
    print(json.dumps({key: report[key] for key in ("status", "output_video_sha256", "loudness", "minimum_sentence_correlation", "maximum_disclosed_audio_shift_relative_to_fixed_visual_seconds", "passed", "total")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
