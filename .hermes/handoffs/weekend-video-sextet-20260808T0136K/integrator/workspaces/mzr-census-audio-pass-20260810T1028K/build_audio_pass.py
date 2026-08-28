#!/usr/bin/env python3
"""Build one fixed-visual MZR-census audio-pass A/B candidate."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import wave
from datetime import datetime, timezone
from pathlib import Path

RATE = 48_000
SAMPLE_WIDTH = 2


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(command, check=True, **kwargs)


def loudness(path: Path, target_i: float, target_lra: float, target_tp: float) -> dict:
    command = [
        "ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
        "-af", f"loudnorm=I={target_i}:LRA={target_lra}:TP={target_tp}:print_format=json",
        "-f", "null", "-",
    ]
    result = run(command, capture_output=True, text=True)
    match = re.search(r"\{\s*\"input_i\".*?\}", result.stderr, re.S)
    if not match:
        raise RuntimeError(f"could not parse loudness output for {path}")
    return json.loads(match.group(0))


def parse_silences(path: Path) -> list[dict]:
    text = path.read_text()
    starts = [float(value) for value in re.findall(r"silence_start: ([0-9.]+)", text)]
    ends = [float(value) for value in re.findall(r"silence_end: ([0-9.]+)", text)]
    durations = [float(value) for value in re.findall(r"silence_duration: ([0-9.]+)", text)]
    if not (len(starts) == len(ends) == len(durations)):
        raise RuntimeError("Kun silence evidence has unpaired intervals")
    return [
        {"start_seconds": start, "end_seconds": end, "duration_seconds": duration}
        for start, end, duration in zip(starts, ends, durations)
    ]


def srt_time(seconds: float) -> str:
    milliseconds = round(seconds * 1000)
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    seconds_i, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02}:{minutes:02}:{seconds_i:02},{milliseconds:03}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace")
    parser.add_argument("handoff_root")
    args = parser.parse_args()
    workspace = Path(args.workspace).resolve()
    handoff_root = Path(args.handoff_root).resolve()
    config_path = workspace / "AUDIO_PASS_CONFIG.json"
    config = json.loads(config_path.read_text())

    predecessor = config["predecessor"]
    source_video = handoff_root / predecessor["video_path"]
    source_timeline_path = workspace / predecessor["timeline_path"]
    source_master_path = workspace / predecessor["narration_master_path"]
    silence_path = handoff_root / config["source_of_truth"]["silence_evidence_path"]
    output_video = workspace / config["output"]["video_filename"]
    audio_dir = workspace / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    bindings = [
        (source_video, predecessor["video_sha256"]),
        (source_timeline_path, predecessor["timeline_sha256"]),
        (source_master_path, predecessor["narration_master_sha256"]),
        (silence_path, config["source_of_truth"]["silence_evidence_sha256"]),
    ]
    for path, expected in bindings:
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(f"source binding failed: {path}")

    timeline = json.loads(source_timeline_path.read_text())
    records = timeline["records"]
    if len(records) != 22:
        raise RuntimeError(f"unexpected sentence count: {len(records)}")

    silences = parse_silences(silence_path)
    source_gaps: list[dict] = []
    for index, (current, following) in enumerate(zip(records, records[1:])):
        current_end = float(current["audio_end_seconds"])
        following_start = float(following["audio_start_seconds"])
        matches = [
            interval for interval in silences
            if interval["start_seconds"] <= current_end + 0.35
            and interval["end_seconds"] >= following_start - 0.35
        ]
        if len(matches) != 1:
            raise RuntimeError(
                f"could not bind one Kun silence interval to {current['id']}->{following['id']}: {matches}"
            )
        source_gaps.append(
            {
                "index": index,
                "from": current["id"],
                "to": following["id"],
                **matches[0],
            }
        )

    listed_pairs = {
        (row["from"], row["to"]) for row in config["seam_policy"]["listed_routine_seams"]
    }
    deliberate_pairs = {
        (row["from"], row["to"])
        for row in config["seam_policy"]["deliberate_visual_breaths_preserved"]
    }
    found_pairs = {(row["from"], row["to"]) for row in source_gaps}
    if not listed_pairs <= found_pairs or not deliberate_pairs <= found_pairs:
        raise RuntimeError("configured seam pairs are absent from the bound timeline")

    cap = float(config["seam_policy"]["routine_gap_cap_seconds"])
    shifts = [0.0] * len(records)
    for index in range(len(source_gaps) - 1, -1, -1):
        gap = source_gaps[index]
        pair = (gap["from"], gap["to"])
        if pair in deliberate_pairs:
            shifts[index] = shifts[index + 1]
        else:
            shifts[index] = max(
                0.0,
                shifts[index + 1] + float(gap["duration_seconds"]) - cap,
            )

    shift_samples = [round(value * RATE) for value in shifts]
    shifts = [value / RATE for value in shift_samples]
    derivations: list[dict] = []
    for gap in source_gaps:
        index = gap["index"]
        pair = (gap["from"], gap["to"])
        derived = float(gap["duration_seconds"]) + shifts[index + 1] - shifts[index]
        classification = (
            "listed_routine_seam"
            if pair in listed_pairs
            else "deliberate_visual_breath_preserved"
            if pair in deliberate_pairs
            else "routine_seam_supporting_redistribution"
        )
        derivations.append(
            {
                **gap,
                "classification": classification,
                "from_sentence_shift_seconds": shifts[index],
                "to_sentence_shift_seconds": shifts[index + 1],
                "derived_post_edit_silence_seconds": derived,
                "derivation": "source_silence + to_shift - from_shift",
            }
        )
        if classification == "deliberate_visual_breath_preserved" and abs(derived - gap["duration_seconds"]) > 1 / RATE:
            raise RuntimeError(f"deliberate visual breath changed: {pair}")
        if classification != "deliberate_visual_breath_preserved" and derived > cap + 1 / RATE:
            raise RuntimeError(f"routine seam exceeds cap after derivation: {pair} {derived}")

    with wave.open(str(source_master_path), "rb") as source_wave:
        if (
            source_wave.getnchannels(),
            source_wave.getframerate(),
            source_wave.getsampwidth(),
        ) != (1, RATE, SAMPLE_WIDTH):
            raise RuntimeError("unexpected source master PCM format")
        source_frame_count = source_wave.getnframes()
        source_pcm = source_wave.readframes(source_frame_count)

    output_pcm = bytearray(source_frame_count * SAMPLE_WIDTH)
    audio_rows: list[dict] = []
    for index, record in enumerate(records):
        start = int(record["audio_start_sample"])
        end = int(record["audio_end_sample"])
        shifted_start = start + shift_samples[index]
        shifted_end = end + shift_samples[index]
        visual_start = float(record["audio_start_seconds"])
        visual_end = (
            float(records[index + 1]["audio_start_seconds"])
            if index + 1 < len(records)
            else float(timeline["master_duration_seconds"])
        )
        if shifted_start < start or shifted_end > round(visual_end * RATE):
            raise RuntimeError(f"audio for {record['id']} leaves its original visual card window")
        source_slice = source_pcm[start * SAMPLE_WIDTH : end * SAMPLE_WIDTH]
        target_slice = output_pcm[shifted_start * SAMPLE_WIDTH : shifted_end * SAMPLE_WIDTH]
        if any(target_slice):
            raise RuntimeError(f"retimed audio overlap at {record['id']}")
        output_pcm[shifted_start * SAMPLE_WIDTH : shifted_end * SAMPLE_WIDTH] = source_slice
        copied_slice = bytes(output_pcm[shifted_start * SAMPLE_WIDTH : shifted_end * SAMPLE_WIDTH])
        if hashlib.sha256(source_slice).digest() != hashlib.sha256(copied_slice).digest():
            raise RuntimeError(f"sentence PCM copy mismatch: {record['id']}")
        audio_rows.append(
            {
                "id": record["id"],
                "section": record["section"],
                "original_visual_card_start_seconds": visual_start,
                "original_visual_card_end_seconds": visual_end,
                "original_audio_start_seconds": start / RATE,
                "original_audio_end_seconds": end / RATE,
                "new_audio_start_seconds": shifted_start / RATE,
                "new_audio_end_seconds": shifted_end / RATE,
                "audio_shift_relative_to_fixed_visual_seconds": shifts[index],
                "source_pcm_slice_sha256": hashlib.sha256(source_slice).hexdigest(),
                "retimed_pcm_slice_sha256": hashlib.sha256(copied_slice).hexdigest(),
                "source_pcm_slice_bytes": len(source_slice),
                "visual_card_window_seconds_unchanged": True,
            }
        )

    retimed_raw = audio_dir / "narration_retimed_pre_normalization.wav"
    with wave.open(str(retimed_raw), "wb") as output_wave:
        output_wave.setnchannels(1)
        output_wave.setsampwidth(SAMPLE_WIDTH)
        output_wave.setframerate(RATE)
        output_wave.writeframes(output_pcm)

    target = config["audio_target"]
    before = loudness(
        retimed_raw,
        float(target["integrated_lufs"]),
        float(target["lra_target_lu"]),
        float(target["true_peak_ceiling_dbtp"]),
    )
    second_pass_filter = (
        f"loudnorm=I={target['integrated_lufs']}:LRA={target['lra_target_lu']}:"
        f"TP={target['true_peak_ceiling_dbtp']}:measured_I={before['input_i']}:"
        f"measured_LRA={before['input_lra']}:measured_TP={before['input_tp']}:"
        f"measured_thresh={before['input_thresh']}:offset={before['target_offset']}:linear=true"
    )
    stage1_master = audio_dir / "narration_master_stage1_measured.wav"
    run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(retimed_raw),
            "-af", second_pass_filter, "-ar", str(RATE), "-ac", "1",
            "-c:a", "pcm_s16le", str(stage1_master),
        ]
    )
    stage2_filter = "loudnorm=I=-20.5:LRA=7:TP=-2.3"
    stage2_master = audio_dir / "narration_master_stage2_lra.wav"
    run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(stage1_master),
            "-af", stage2_filter, "-ar", str(RATE), "-ac", "1",
            "-c:a", "pcm_s16le", str(stage2_master),
        ]
    )
    stage2_measurement = loudness(
        stage2_master,
        float(target["integrated_lufs"]),
        float(target["lra_target_lu"]),
        float(target["true_peak_ceiling_dbtp"]),
    )
    # The final -0.1 LU calibration compensates the prior dynamic pass so the
    # encoded AAC, which is the review object, lands at Kun's -20.5 LUFS target.
    final_calibration_filter = "loudnorm=I=-20.6:LRA=7:TP=-2.3"
    normalized_master = audio_dir / "narration_master_audio_pass.wav"
    run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(stage2_master),
            "-af", final_calibration_filter, "-ar", str(RATE), "-ac", "1",
            "-c:a", "pcm_s16le", str(normalized_master),
        ]
    )
    for normalized_path in (stage1_master, stage2_master, normalized_master):
        with wave.open(str(normalized_path), "rb") as normalized_wave:
            if normalized_wave.getnframes() != source_frame_count:
                raise RuntimeError(f"normalization changed audio duration: {normalized_path}")
    after_pcm = loudness(
        normalized_master,
        float(target["integrated_lufs"]),
        float(target["lra_target_lu"]),
        float(target["true_peak_ceiling_dbtp"]),
    )

    if output_video.exists():
        raise RuntimeError(f"refusing to overwrite existing output: {output_video}")
    remux_command = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(source_video), "-i", str(normalized_master),
        "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k", "-ar", str(RATE), "-ac", "1",
        "-movflags", "+faststart", str(output_video),
    ]
    run(remux_command)

    retimed_timeline = {
        "timeline_id": "MZR_CENSUS_AUDIO_PASS_TIMELINE_V1_20260810T1028K",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_visual_timeline_path": predecessor["timeline_path"],
        "source_visual_timeline_sha256": predecessor["timeline_sha256"],
        "source_narration_master_sha256": predecessor["narration_master_sha256"],
        "visual_timing_policy": "unchanged predecessor H.264 stream; no frame or card-state timing edits",
        "audio_edit_policy": "sentence PCM slices shifted later only inside their original visual card windows",
        "maximum_audio_shift_relative_to_fixed_visual_seconds": max(shifts),
        "source_master_frame_count": source_frame_count,
        "output_master_frame_count": source_frame_count,
        "sample_rate_hz": RATE,
        "channels": 1,
        "sentence_pcm_slices_byte_preserved_before_normalization": True,
        "records": audio_rows,
        "per_gap_derivations": derivations,
        "loudness_before_normalization": before,
        "normalization": {
            "target": target,
            "stage1_measured_filter": second_pass_filter,
            "stage1_master_sha256": sha256(stage1_master),
            "stage2_lra_filter": stage2_filter,
            "stage2_master_sha256": sha256(stage2_master),
            "stage2_measurement": stage2_measurement,
            "final_calibration_filter": final_calibration_filter,
            "final_calibration_reason": "compensate the dynamic LRA pass so the encoded AAC lands at the authoritative -20.5 LUFS target",
            "measured_pcm_after": after_pcm,
        },
        "artifacts": {
            "retimed_pre_normalization": str(retimed_raw.relative_to(workspace)),
            "retimed_pre_normalization_sha256": sha256(retimed_raw),
            "normalized_master": str(normalized_master.relative_to(workspace)),
            "normalized_master_sha256": sha256(normalized_master),
        },
    }
    retimed_timeline_path = audio_dir / "AUDIO_EDIT_TIMELINE.json"
    retimed_timeline_path.write_text(json.dumps(retimed_timeline, indent=2) + "\n")

    subtitles: list[str] = []
    for index, row in enumerate(audio_rows, 1):
        text = records[index - 1]["text"]
        subtitles.extend(
            [
                str(index),
                f"{srt_time(row['new_audio_start_seconds'])} --> {srt_time(row['new_audio_end_seconds'])}",
                text,
                "",
            ]
        )
    (workspace / "subtitles_audio_pass.srt").write_text("\n".join(subtitles))

    receipt = {
        "receipt_id": "MZR_CENSUS_AUDIO_PASS_BUILD_V1_20260810T1028K",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "config_path": config_path.name,
        "config_sha256": sha256(config_path),
        "source_video_path": str(source_video),
        "source_video_sha256": sha256(source_video),
        "source_visual_timeline_sha256": sha256(source_timeline_path),
        "source_narration_master_sha256": sha256(source_master_path),
        "audio_edit_timeline_path": str(retimed_timeline_path.relative_to(workspace)),
        "audio_edit_timeline_sha256": sha256(retimed_timeline_path),
        "normalized_audio_master_sha256": sha256(normalized_master),
        "output_video": output_video.name,
        "output_video_sha256": sha256(output_video),
        "remux_command": remux_command,
        "video_codec_action": "stream_copy_no_reencode",
        "audio_codec_action": "AAC 48kHz mono encode from normalized retimed PCM",
        "visual_frame_or_timing_change_intended": False,
        "audio_to_fixed_visual_timing_delta_disclosed": True,
        "maximum_audio_shift_relative_to_fixed_visual_seconds": max(shifts),
        "video_reportable_now": False,
        "gates": config["gates"],
    }
    (workspace / "BUILD_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
