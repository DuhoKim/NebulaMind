#!/usr/bin/env python3
"""Derive the visual timeline from freshly decoded sentence audio at exact sample precision."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import wave
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUDIO = ROOT / "audio"
SYNTHESIS = AUDIO / "synthesis_receipt.json"
MASTER_RAW = AUDIO / "narration_raw.wav"
MASTER = AUDIO / "narration_master.wav"
TIMELINE = AUDIO / "timeline.json"
SAMPLE_RATE = 48_000
TARGET_WPM = 115.0
LEAD_SECONDS = 0.6
TAIL_SECONDS = 2.4
BASE_PAUSE_SECONDS = 0.75


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
    spec = json.loads((ROOT / "spec.json").read_text())
    spec_by_id = {record["id"]: record for record in spec["sentences"]}
    receipt = json.loads(SYNTHESIS.read_text())
    decoded_dir = AUDIO / "decoded"
    decoded_dir.mkdir(parents=True, exist_ok=True)
    sentence_pcm = []
    for record in receipt["records"]:
        source = ROOT / record["file"]
        decoded = decoded_dir / f"{record['id']}.wav"
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(source), "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "pcm_s16le", str(decoded)])
        with wave.open(str(decoded), "rb") as wav:
            if (wav.getframerate(), wav.getnchannels(), wav.getsampwidth()) != (SAMPLE_RATE, 1, 2):
                raise RuntimeError(f"unexpected decoded format: {decoded}")
            frames = wav.getnframes()
            pcm = wav.readframes(frames)
        sentence_pcm.append((record, pcm, frames))
    words = sum(word_count(record["text"]) for record, _, _ in sentence_pcm)
    speech_samples = sum(frames for _, _, frames in sentence_pcm)
    desired_occupied_samples = round(words / TARGET_WPM * 60 * SAMPLE_RATE)
    gap_count = len(sentence_pcm) - 1
    base_pause_samples = round(BASE_PAUSE_SECONDS * SAMPLE_RATE)
    pause_total_samples = desired_occupied_samples - speech_samples
    if pause_total_samples < base_pause_samples * gap_count:
        raise RuntimeError("raw speech plus minimum pauses is slower than target WPM")
    section_gaps = [i for i in range(gap_count) if sentence_pcm[i][0]["section"] != sentence_pcm[i + 1][0]["section"]]
    if not section_gaps:
        raise RuntimeError("no section boundaries available for pause distribution")
    pause_samples = [base_pause_samples] * gap_count
    extra = pause_total_samples - sum(pause_samples)
    section_extra, remainder = divmod(extra, len(section_gaps))
    for position, index in enumerate(section_gaps):
        pause_samples[index] += section_extra + (1 if position < remainder else 0)
    if sum(pause_samples) != pause_total_samples:
        raise RuntimeError("pause solver failed exact accounting")
    lead_samples = round(LEAD_SECONDS * SAMPLE_RATE)
    tail_samples = round(TAIL_SECONDS * SAMPLE_RATE)
    cursor = lead_samples
    timeline_records = []
    with wave.open(str(MASTER_RAW), "wb") as output:
        output.setnchannels(1); output.setsampwidth(2); output.setframerate(SAMPLE_RATE)
        output.writeframes(b"\x00\x00" * lead_samples)
        for index, (record, pcm, frames) in enumerate(sentence_pcm):
            start = cursor; output.writeframes(pcm); cursor += frames; end = cursor
            visual_frame = round(start / SAMPLE_RATE * 30)
            decoded = decoded_dir / f"{record['id']}.wav"
            timeline_record = dict(spec_by_id[record["id"]])
            timeline_record.update({"word_count": word_count(record["text"]), "raw_file": record["file"], "raw_file_sha256": record["file_sha256"], "decoded_file": str(decoded.relative_to(ROOT)), "decoded_file_sha256": sha256(decoded), "audio_start_sample": start, "audio_end_sample": end, "audio_start_seconds": start / SAMPLE_RATE, "audio_end_seconds": end / SAMPLE_RATE, "visual_action_start_frame": visual_frame, "visual_action_start_seconds": visual_frame / 30, "alignment_delta_seconds": visual_frame / 30 - start / SAMPLE_RATE, "pause_after_samples": pause_samples[index] if index < gap_count else 0, "pause_after_seconds": pause_samples[index] / SAMPLE_RATE if index < gap_count else 0})
            timeline_records.append(timeline_record)
            if index < gap_count:
                output.writeframes(b"\x00\x00" * pause_samples[index]); cursor += pause_samples[index]
        output.writeframes(b"\x00\x00" * tail_samples); cursor += tail_samples
    measurement = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(MASTER_RAW), "-af", "loudnorm=I=-20.3:LRA=7:TP=-2.3:print_format=json", "-f", "null", "-"])
    match = re.search(r"\{\s*\"input_i\".*?\}", measurement.stderr, re.S)
    if not match:
        raise RuntimeError("could not parse loudness measurement")
    loudness = json.loads(match.group(0))
    gain_db = min(-20.3 - float(loudness["input_i"]), -2.3 - float(loudness["input_tp"]))
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(MASTER_RAW), "-af", f"volume={gain_db:.6f}dB", "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "pcm_s16le", str(MASTER)])
    with wave.open(str(MASTER_RAW), "rb") as raw_wav, wave.open(str(MASTER), "rb") as master_wav:
        if raw_wav.getnframes() != master_wav.getnframes():
            raise RuntimeError("normalization changed sample count")
        final_samples = master_wav.getnframes()
    first_start = timeline_records[0]["audio_start_seconds"]
    last_end = timeline_records[-1]["audio_end_seconds"]
    occupied = last_end - first_start
    section_intervals = {}
    for section in dict.fromkeys(r["section"] for r in timeline_records):
        members = [r for r in timeline_records if r["section"] == section]
        section_intervals[section] = members[-1]["audio_end_seconds"] - members[0]["audio_start_seconds"]
    timeline = {"created_at_utc": datetime.now(timezone.utc).isoformat(), "revision": spec["revision"], "sample_rate": SAMPLE_RATE, "video_fps": 30, "sentence_count": len(timeline_records), "word_count": words, "target_delivered_wpm": TARGET_WPM, "delivered_wpm": words / occupied * 60, "raw_speech_seconds": speech_samples / SAMPLE_RATE, "inter_sentence_pause_seconds": sum(pause_samples) / SAMPLE_RATE, "occupied_seconds_first_start_to_last_end": occupied, "lead_seconds": lead_samples / SAMPLE_RATE, "tail_seconds": tail_samples / SAMPLE_RATE, "master_duration_seconds": final_samples / SAMPLE_RATE, "max_abs_audio_visual_start_delta_seconds": max(abs(r["alignment_delta_seconds"]) for r in timeline_records), "loudness_measurement_before_gain": loudness, "scalar_gain_db": gain_db, "section_intervals_seconds": section_intervals, "master_raw": str(MASTER_RAW.relative_to(ROOT)), "master_raw_sha256": sha256(MASTER_RAW), "master": str(MASTER.relative_to(ROOT)), "master_sha256": sha256(MASTER), "records": timeline_records}
    TIMELINE.write_text(json.dumps(timeline, indent=2) + "\n")
    srt = ROOT / f"{Path(spec['candidate_filename']).stem}.srt"
    blocks = [f"{index}\n{srt_time(item['audio_start_seconds'])} --> {srt_time(item['audio_end_seconds'])}\n{item['text']}\n" for index, item in enumerate(timeline_records, 1)]
    srt.write_text("\n".join(blocks) + "\n")
    print(json.dumps({"word_count": words, "raw_speech_seconds": speech_samples / SAMPLE_RATE, "inter_sentence_pause_seconds": sum(pause_samples) / SAMPLE_RATE, "delivered_wpm": timeline["delivered_wpm"], "master_duration_seconds": timeline["master_duration_seconds"], "max_abs_alignment_delta_seconds": timeline["max_abs_audio_visual_start_delta_seconds"], "master": str(MASTER), "timeline": str(TIMELINE), "srt": str(srt)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
