#!/usr/bin/env python3
"""Derive the v5 visual timeline from freshly decoded sentence audio."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import wave
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUDIO = ROOT / "audio_v5"
SYNTH_RECEIPT = AUDIO / "synthesis_receipt.json"
MASTER_RAW = AUDIO / "narration_raw.wav"
MASTER = AUDIO / "narration_master.wav"
TIMELINE = AUDIO / "timeline.json"
SRT = ROOT / "spin-literature-intro-canary-20260810T1535K-v5.srt"
SAMPLE_RATE = 48_000
TARGET_WPM = 115.0
LEAD_SECONDS = 0.6
TAIL_SECONDS = 2.4
BASE_PAUSE_SECONDS = 0.75
SECTION_GAPS_AFTER = {"i02", "i03", "i04", "i05u", "i06", "s02", "s05", "s10", "s11", "s13", "s16", "s18", "s21"}


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=True, capture_output=True, text=True)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def srt_time(seconds: float) -> str:
    milliseconds = round(seconds * 1000)
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    secs, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"


def main() -> int:
    receipt = json.loads(SYNTH_RECEIPT.read_text())
    decoded_dir = AUDIO / "decoded"
    decoded_dir.mkdir(parents=True, exist_ok=True)

    sentence_pcm: list[tuple[dict, bytes, int]] = []
    for record in receipt["records"]:
        source = ROOT / record["file"]
        decoded = decoded_dir / f"{record['id']}.wav"
        run(
            [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-i",
                str(source),
                "-ar",
                str(SAMPLE_RATE),
                "-ac",
                "1",
                "-c:a",
                "pcm_s16le",
                str(decoded),
            ]
        )
        with wave.open(str(decoded), "rb") as wav:
            if (wav.getframerate(), wav.getnchannels(), wav.getsampwidth()) != (SAMPLE_RATE, 1, 2):
                raise RuntimeError(f"unexpected decoded format: {decoded}")
            frames = wav.getnframes()
            pcm = wav.readframes(frames)
        sentence_pcm.append((record, pcm, frames))

    words = sum(word_count(record["text"]) for record, _, _ in sentence_pcm)
    speech_samples = sum(frames for _, _, frames in sentence_pcm)
    desired_occupied_samples = round(words / TARGET_WPM * 60 * SAMPLE_RATE)
    pause_total_samples = desired_occupied_samples - speech_samples
    gap_count = len(sentence_pcm) - 1
    base_pause_samples = round(BASE_PAUSE_SECONDS * SAMPLE_RATE)
    section_gaps = [
        i for i, (record, _, _) in enumerate(sentence_pcm[:-1]) if record["id"] in SECTION_GAPS_AFTER
    ]
    extra_samples = pause_total_samples - base_pause_samples * gap_count
    if extra_samples < 0:
        raise RuntimeError("raw speech is already slower than the target delivered WPM")
    section_extra, remainder = divmod(extra_samples, len(section_gaps))
    pause_samples = [base_pause_samples] * gap_count
    for position, gap_index in enumerate(section_gaps):
        pause_samples[gap_index] += section_extra + (1 if position < remainder else 0)
    if sum(pause_samples) != pause_total_samples:
        raise RuntimeError("pause solver failed exact sample accounting")

    lead_samples = round(LEAD_SECONDS * SAMPLE_RATE)
    tail_samples = round(TAIL_SECONDS * SAMPLE_RATE)
    cursor = lead_samples
    timeline_records = []
    with wave.open(str(MASTER_RAW), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(SAMPLE_RATE)
        output.writeframes(b"\x00\x00" * lead_samples)
        for index, (record, pcm, frames) in enumerate(sentence_pcm):
            start_sample = cursor
            output.writeframes(pcm)
            cursor += frames
            end_sample = cursor
            visual_frame = round((start_sample / SAMPLE_RATE) * 30)
            decoded = decoded_dir / f"{record['id']}.wav"
            timeline_records.append(
                {
                    "id": record["id"],
                    "section": record["section"],
                    "text": record["text"],
                    "word_count": word_count(record["text"]),
                    "raw_file": record["file"],
                    "raw_file_sha256": record["file_sha256"],
                    "decoded_file": str(decoded.relative_to(ROOT)),
                    "decoded_file_sha256": sha256(decoded),
                    "audio_start_sample": start_sample,
                    "audio_end_sample": end_sample,
                    "audio_start_seconds": start_sample / SAMPLE_RATE,
                    "audio_end_seconds": end_sample / SAMPLE_RATE,
                    "visual_action_start_frame": visual_frame,
                    "visual_action_start_seconds": visual_frame / 30,
                    "alignment_delta_seconds": visual_frame / 30 - start_sample / SAMPLE_RATE,
                    "pause_after_samples": pause_samples[index] if index < gap_count else 0,
                    "pause_after_seconds": pause_samples[index] / SAMPLE_RATE if index < gap_count else 0,
                }
            )
            if index < gap_count:
                output.writeframes(b"\x00\x00" * pause_samples[index])
                cursor += pause_samples[index]
        output.writeframes(b"\x00\x00" * tail_samples)
        cursor += tail_samples

    measure = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostats",
            "-i",
            str(MASTER_RAW),
            "-af",
            "loudnorm=I=-16:LRA=7:TP=-2.3:print_format=json",
            "-f",
            "null",
            "-",
        ]
    )
    match = re.search(r"\{\s*\"input_i\".*?\}", measure.stderr, re.S)
    if not match:
        raise RuntimeError("could not parse loudness measurement")
    loudness = json.loads(match.group(0))
    input_i = float(loudness["input_i"])
    input_tp = float(loudness["input_tp"])
    gain_db = min(-16.0 - input_i, -2.3 - input_tp)
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(MASTER_RAW),
            "-af",
            f"volume={gain_db:.6f}dB",
            "-ar",
            str(SAMPLE_RATE),
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            str(MASTER),
        ]
    )

    with wave.open(str(MASTER_RAW), "rb") as raw_wav, wave.open(str(MASTER), "rb") as master_wav:
        if raw_wav.getnframes() != master_wav.getnframes():
            raise RuntimeError("normalization changed the exact audio sample count")
        final_samples = master_wav.getnframes()

    first_start = timeline_records[0]["audio_start_seconds"]
    last_end = timeline_records[-1]["audio_end_seconds"]
    occupied_seconds = last_end - first_start
    delivered_wpm = words / occupied_seconds * 60
    max_alignment = max(abs(item["alignment_delta_seconds"]) for item in timeline_records)
    timeline = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "revision": "v5-duho-literature-beat-only",
        "sample_rate": SAMPLE_RATE,
        "video_fps": 30,
        "sentence_count": len(timeline_records),
        "word_count": words,
        "target_delivered_wpm": TARGET_WPM,
        "delivered_wpm": delivered_wpm,
        "raw_speech_seconds": speech_samples / SAMPLE_RATE,
        "inter_sentence_pause_seconds": sum(pause_samples) / SAMPLE_RATE,
        "occupied_seconds_first_start_to_last_end": occupied_seconds,
        "lead_seconds": lead_samples / SAMPLE_RATE,
        "tail_seconds": tail_samples / SAMPLE_RATE,
        "master_duration_seconds": final_samples / SAMPLE_RATE,
        "max_abs_audio_visual_start_delta_seconds": max_alignment,
        "loudness_measurement_before_gain": loudness,
        "scalar_gain_db": gain_db,
        "master_raw": str(MASTER_RAW.relative_to(ROOT)),
        "master_raw_sha256": sha256(MASTER_RAW),
        "master": str(MASTER.relative_to(ROOT)),
        "master_sha256": sha256(MASTER),
        "records": timeline_records,
    }
    TIMELINE.write_text(json.dumps(timeline, indent=2) + "\n")

    blocks = []
    for index, item in enumerate(timeline_records, 1):
        blocks.append(
            f"{index}\n{srt_time(item['audio_start_seconds'])} --> {srt_time(item['audio_end_seconds'])}\n{item['text']}\n"
        )
    SRT.write_text("\n".join(blocks) + "\n")
    print(
        json.dumps(
            {
                "word_count": words,
                "raw_speech_seconds": speech_samples / SAMPLE_RATE,
                "inter_sentence_pause_seconds": sum(pause_samples) / SAMPLE_RATE,
                "occupied_seconds": occupied_seconds,
                "delivered_wpm": delivered_wpm,
                "master_duration_seconds": final_samples / SAMPLE_RATE,
                "max_abs_alignment_delta_seconds": max_alignment,
                "gain_db": gain_db,
                "master": str(MASTER),
                "timeline": str(TIMELINE),
                "srt": str(SRT),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
