#!/usr/bin/env python3
"""Reassemble candidate-local sentence clips under the overnight quality timing/audio policy."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import wave
from datetime import datetime, timezone
from pathlib import Path

RATE = 48_000
FPS = 30


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def loudness(path: Path, target_i: float, target_lra: float, target_tp: float) -> dict:
    command = [
        "ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
        "-af", f"loudnorm=I={target_i}:LRA={target_lra}:TP={target_tp}:print_format=json",
        "-f", "null", "-",
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    match = re.search(r"\{\s*\"input_i\".*?\}", result.stderr, re.S)
    if not match:
        raise RuntimeError(f"could not parse loudness analysis for {path}")
    return json.loads(match.group(0))


def srt_time(seconds: float) -> str:
    milliseconds = round(seconds * 1000)
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    seconds_i, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02}:{minutes:02}:{seconds_i:02},{milliseconds:03}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate_dir")
    args = parser.parse_args()
    candidate = Path(args.candidate_dir).resolve()
    spec_path = candidate / "spec.json"
    spec = json.loads(spec_path.read_text())
    profile = spec.get("quality_profile")
    if not isinstance(profile, dict):
        raise RuntimeError("spec quality_profile is required")

    target_i = float(profile["integrated_lufs_target"])
    target_lra = float(profile["lra_target_lu"])
    target_tp = float(profile["true_peak_target_dbtp"])
    lead_seconds = float(profile.get("lead_seconds", 0.6))
    tail_seconds = float(profile.get("tail_seconds", 3.0))
    routine_pause = float(profile["routine_pause_seconds"])
    section_pause = float(profile["section_boundary_pause_seconds"])
    target_wpm_range = [float(x) for x in profile["delivered_wpm_range"]]
    minimum_dwell = {str(k): float(v) for k, v in profile["minimum_card_dwell_seconds"].items()}
    special_pauses = {str(k): float(v) for k, v in profile.get("special_pause_after_seconds", {}).items()}
    boundary_preroll = float(profile.get("boundary_preroll_seconds", 0.0))

    sentences = spec["sentences"]
    ids = [item["id"] for item in sentences]
    if len(ids) != len(set(ids)):
        raise RuntimeError("duplicate sentence IDs")
    missing_dwell = [item_id for item_id in ids if item_id not in minimum_dwell]
    if missing_dwell:
        raise RuntimeError(f"missing card-dwell policy for {missing_dwell}")

    audio = candidate / "audio"
    synth_path = audio / "synthesis_receipt.json"
    synth = json.loads(synth_path.read_text())
    synth_by_id = {record["id"]: record for record in synth["records"]}
    if set(synth_by_id) != set(ids):
        raise RuntimeError("synthesis receipt IDs do not match final spec IDs")

    provenance = candidate / "provenance"
    provenance.mkdir(parents=True, exist_ok=True)
    assembler_snapshot = provenance / "assemble_quality.py"
    shutil.copy2(Path(__file__).resolve(), assembler_snapshot)

    decoded = audio / "decoded"
    if decoded.exists():
        shutil.rmtree(decoded)
    decoded.mkdir(parents=True)
    decoded_paths: dict[str, Path] = {}
    source_paths: dict[str, Path] = {}
    sample_counts: dict[str, int] = {}

    for item in sentences:
        item_id = item["id"]
        source_record = synth_by_id[item_id]
        if source_record["text"] != item["text"]:
            raise RuntimeError(f"narration text changed for {item_id}; resynthesis is forbidden")
        source = audio / "raw" / Path(source_record["file"]).name
        if not source.is_file():
            raise RuntimeError(f"missing candidate-local raw narration clip: {source}")
        if sha256(source) != source_record["file_sha256"]:
            raise RuntimeError(f"raw narration hash mismatch: {item_id}")
        output = decoded / f"{item_id}.wav"
        subprocess.run(
            [
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(source),
                "-ac", "1", "-ar", str(RATE), "-c:a", "pcm_s16le", str(output),
            ],
            check=True,
        )
        with wave.open(str(output), "rb") as handle:
            if (handle.getnchannels(), handle.getframerate(), handle.getsampwidth()) != (1, RATE, 2):
                raise RuntimeError(f"unexpected decoded PCM format: {output}")
            sample_counts[item_id] = handle.getnframes()
        source_paths[item_id] = source
        decoded_paths[item_id] = output

    raw_master = audio / "narration_raw.wav"
    cursor = round(lead_seconds * RATE)
    records: list[dict] = []
    pause_policy: list[dict] = []
    with wave.open(str(raw_master), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(RATE)
        output.writeframes(b"\x00\x00" * cursor)
        for index, item in enumerate(sentences):
            item_id = item["id"]
            start = cursor
            with wave.open(str(decoded_paths[item_id]), "rb") as clip:
                payload = clip.readframes(clip.getnframes())
            output.writeframes(payload)
            cursor += sample_counts[item_id]
            end = cursor
            speech_seconds = sample_counts[item_id] / RATE
            requested_dwell = minimum_dwell[item_id]
            effective_preroll = boundary_preroll if item.get("visual") == "boundary" else 0.0

            if index + 1 < len(sentences):
                next_item = sentences[index + 1]
                default_pause = section_pause if item["section"] != next_item["section"] else routine_pause
                reason = "section_boundary" if item["section"] != next_item["section"] else "routine"
                if item_id in special_pauses and special_pauses[item_id] > default_pause:
                    default_pause = special_pauses[item_id]
                    reason = "special_named_hold"
                readability_pause = max(0.0, requested_dwell - speech_seconds - effective_preroll)
                pause_seconds = max(default_pause, readability_pause)
                if readability_pause > default_pause:
                    reason = "reading_time_floor"
            else:
                readability_tail = max(0.0, requested_dwell - speech_seconds - effective_preroll)
                pause_seconds = max(tail_seconds, readability_tail)
                reason = "tail_reading_time_floor" if readability_tail > tail_seconds else "tail"

            pause_samples = round(pause_seconds * RATE)
            pause_seconds = pause_samples / RATE
            visual_frame = round((start / RATE) * FPS)
            visual_time = visual_frame / FPS
            card_dwell = speech_seconds + pause_seconds
            effective_visible_dwell = card_dwell + effective_preroll
            if effective_visible_dwell + 1e-6 < requested_dwell:
                raise RuntimeError(f"reading-time floor not met for {item_id}")

            record = {
                **item,
                "word_count": word_count(item["text"]),
                "raw_file": str(source_paths[item_id].relative_to(candidate)),
                "raw_file_sha256": sha256(source_paths[item_id]),
                "decoded_file": str(decoded_paths[item_id].relative_to(candidate)),
                "decoded_file_sha256": sha256(decoded_paths[item_id]),
                "audio_start_sample": start,
                "audio_end_sample": end,
                "audio_start_seconds": start / RATE,
                "audio_end_seconds": end / RATE,
                "visual_action_start_frame": visual_frame,
                "visual_action_start_seconds": visual_time,
                "alignment_delta_seconds": visual_time - start / RATE,
                "pause_after_samples": pause_samples,
                "pause_after_seconds": pause_seconds,
                "card_dwell_seconds": card_dwell,
                "boundary_preroll_seconds": effective_preroll,
                "effective_visible_dwell_seconds": effective_visible_dwell,
                "minimum_reading_dwell_seconds": requested_dwell,
                "reading_time_margin_seconds": effective_visible_dwell - requested_dwell,
                "pause_reason": reason,
            }
            records.append(record)
            pause_policy.append(
                {
                    "id": item_id,
                    "speech_seconds": speech_seconds,
                    "pause_after_seconds": pause_seconds,
                    "pause_reason": reason,
                    "effective_visible_dwell_seconds": effective_visible_dwell,
                    "minimum_reading_dwell_seconds": requested_dwell,
                    "margin_seconds": effective_visible_dwell - requested_dwell,
                }
            )
            if pause_samples:
                output.writeframes(b"\x00\x00" * pause_samples)
                cursor += pause_samples

    before = loudness(raw_master, target_i, target_lra, target_tp)
    master = audio / "narration_master.wav"
    second_pass = (
        f"loudnorm=I={target_i}:LRA={target_lra}:TP={target_tp}:"
        f"measured_I={before['input_i']}:measured_LRA={before['input_lra']}:"
        f"measured_TP={before['input_tp']}:measured_thresh={before['input_thresh']}:"
        f"offset={before['target_offset']}:linear=true"
    )
    subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw_master),
            "-af", second_pass, "-ar", str(RATE), "-c:a", "pcm_s16le", str(master),
        ],
        check=True,
    )
    with wave.open(str(master), "rb") as normalized:
        if normalized.getnframes() != cursor:
            raise RuntimeError(f"normalization changed PCM duration: {normalized.getnframes()} != {cursor}")
    after = loudness(master, target_i, target_lra, target_tp)

    words = sum(word_count(item["text"]) for item in sentences)
    first_start = records[0]["audio_start_seconds"]
    last_end = records[-1]["audio_end_seconds"]
    occupied = last_end - first_start
    delivered_wpm = words / occupied * 60.0
    if not target_wpm_range[0] <= delivered_wpm <= target_wpm_range[1]:
        raise RuntimeError(f"delivered WPM {delivered_wpm:.3f} outside {target_wpm_range}")

    sections = list(dict.fromkeys(record["section"] for record in records))
    section_intervals: dict[str, float] = {}
    for section in sections:
        members = [record for record in records if record["section"] == section]
        section_intervals[section] = max(record["audio_end_seconds"] for record in members) - min(
            record["audio_start_seconds"] for record in members
        )
    peak = spec["peak_section"]
    if section_intervals[peak] < max(section_intervals.values()) - 1e-6:
        raise RuntimeError(f"{peak} is not the longest narrated section: {section_intervals}")

    timeline = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": candidate.name,
        "slug": spec["slug"],
        "sample_rate": RATE,
        "video_fps": FPS,
        "sentence_count": len(records),
        "word_count": words,
        "target_delivered_wpm_range": target_wpm_range,
        "delivered_wpm": delivered_wpm,
        "raw_speech_seconds": sum(sample_counts.values()) / RATE,
        "inter_sentence_pause_seconds": sum(record["pause_after_seconds"] for record in records[:-1]),
        "master_duration_seconds": cursor / RATE,
        "max_abs_audio_visual_start_delta_seconds": max(abs(record["alignment_delta_seconds"]) for record in records),
        "section_intervals_seconds": section_intervals,
        "peak_section": peak,
        "reading_policy": {
            "visible_reading_wpm": profile["visible_reading_wpm"],
            "guard_seconds": profile["reading_guard_seconds"],
            "boundary_preroll_seconds": boundary_preroll,
            "all_cards_meet_floor": all(row["margin_seconds"] >= -1e-6 for row in pause_policy),
            "minimum_margin_seconds": min(row["margin_seconds"] for row in pause_policy),
            "rows": pause_policy,
        },
        "assembler_path": str(assembler_snapshot.relative_to(candidate)),
        "assembler_sha256": sha256(assembler_snapshot),
        "loudness_before_gain": before,
        "normalization": {
            "target_integrated_lufs": target_i,
            "target_lra_lu": target_lra,
            "target_true_peak_dbtp": target_tp,
            "filter_second_pass": second_pass,
            "mode": "measured_two_pass",
            "loudness_after": after,
        },
        "master_raw": str(raw_master.relative_to(candidate)),
        "master_raw_sha256": sha256(raw_master),
        "master": str(master.relative_to(candidate)),
        "master_sha256": sha256(master),
        "source_synthesis_receipt": str(synth_path.relative_to(candidate)),
        "source_synthesis_receipt_sha256": sha256(synth_path),
        "raw_sentence_audio_reused_without_resynthesis": True,
        "records": records,
    }
    (audio / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n")

    subtitles: list[str] = []
    for index, record in enumerate(records, 1):
        subtitles.extend(
            [
                str(index),
                f"{srt_time(record['audio_start_seconds'])} --> {srt_time(record['audio_end_seconds'])}",
                record["text"],
                "",
            ]
        )
    (candidate / "subtitles.srt").write_text("\n".join(subtitles))

    print(
        json.dumps(
            {
                "candidate": candidate.name,
                "sentence_count": len(records),
                "word_count": words,
                "delivered_wpm": delivered_wpm,
                "master_duration_seconds": cursor / RATE,
                "minimum_reading_margin_seconds": timeline["reading_policy"]["minimum_margin_seconds"],
                "loudness_after": after,
                "raw_sentence_audio_reused_without_resynthesis": True,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
