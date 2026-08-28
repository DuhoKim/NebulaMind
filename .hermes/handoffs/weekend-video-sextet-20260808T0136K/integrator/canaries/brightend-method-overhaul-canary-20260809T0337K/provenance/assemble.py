#!/usr/bin/env python3
"""Decode sibling narration and derive the complete visual timeline from PCM samples."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
import wave
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RATE = 48000
FPS = 30
TARGET_WPM = 115.0
LEAD = 0.6
TAIL = 2.4
BASE_PAUSE = 0.65


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def loudness(path: Path) -> dict:
    p = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", "loudnorm=I=-20.3:LRA=7:TP=-2.3:print_format=json", "-f", "null", "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    m = re.search(r"\{\s*\"input_i\".*?\}", p.stderr, re.S)
    if not m:
        raise RuntimeError("could not parse loudness")
    return json.loads(m.group(0))


def srt_time(seconds: float) -> str:
    ms = round(seconds * 1000)
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate_dir")
    args = ap.parse_args()
    candidate = Path(args.candidate_dir).resolve()
    provenance = candidate / "provenance"
    provenance.mkdir(parents=True, exist_ok=True)
    assembler_snapshot = provenance / "assemble.py"
    shutil.copy2(Path(__file__).resolve(), assembler_snapshot)
    spec = json.loads((candidate / "spec.json").read_text())
    audio = ROOT / "audio" / spec["slug"]
    synth = json.loads((audio / "synthesis_receipt.json").read_text())
    decoded = audio / "decoded"
    decoded.mkdir(parents=True, exist_ok=True)
    source_by_id = {r["id"]: ROOT / r["file"] for r in synth["records"]}
    decoded_paths = {}
    samples = {}
    for item in spec["sentences"]:
        out = decoded / f"{item['id']}.wav"
        subprocess.run(
            ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(source_by_id[item["id"]]), "-ac", "1", "-ar", str(RATE), "-c:a", "pcm_s16le", str(out)],
            check=True,
        )
        with wave.open(str(out), "rb") as w:
            if (w.getnchannels(), w.getframerate(), w.getsampwidth()) != (1, RATE, 2):
                raise RuntimeError(f"unexpected PCM format: {out}")
            samples[item["id"]] = w.getnframes()
        decoded_paths[item["id"]] = out
    sentences = spec["sentences"]
    words = sum(word_count(x["text"]) for x in sentences)
    speech_samples = sum(samples[x["id"]] for x in sentences)
    target_span_samples = round((words / TARGET_WPM * 60.0) * RATE)
    gaps = len(sentences) - 1
    base_total = round(BASE_PAUSE * RATE) * gaps
    extra = target_span_samples - speech_samples - base_total
    if extra < 0:
        raise RuntimeError("raw Alloy speech is slower than the delivered-WPM target")
    weights = []
    for current, nxt in zip(sentences, sentences[1:]):
        weights.append(2.6 if current["section"] != nxt["section"] else 1.0)
    allocations = []
    remaining = extra
    total_weight = sum(weights)
    for i, weight in enumerate(weights):
        add = remaining if i == len(weights) - 1 else round(extra * weight / total_weight)
        allocations.append(round(BASE_PAUSE * RATE) + add)
        remaining -= add
    raw_master = audio / "narration_raw.wav"
    cursor = round(LEAD * RATE)
    records = []
    with wave.open(str(raw_master), "wb") as out:
        out.setnchannels(1); out.setsampwidth(2); out.setframerate(RATE)
        out.writeframes(b"\x00\x00" * cursor)
        for i, item in enumerate(sentences):
            start = cursor
            with wave.open(str(decoded_paths[item["id"]]), "rb") as w:
                payload = w.readframes(w.getnframes())
            out.writeframes(payload)
            cursor += samples[item["id"]]
            end = cursor
            pause = allocations[i] if i < len(allocations) else 0
            visual_frame = round((start / RATE) * FPS)
            visual_time = visual_frame / FPS
            records.append(
                {
                    **item,
                    "word_count": word_count(item["text"]),
                    "raw_file": str(source_by_id[item["id"]].relative_to(ROOT)),
                    "raw_file_sha256": sha256(source_by_id[item["id"]]),
                    "decoded_file": str(decoded_paths[item["id"]].relative_to(ROOT)),
                    "decoded_file_sha256": sha256(decoded_paths[item["id"]]),
                    "audio_start_sample": start,
                    "audio_end_sample": end,
                    "audio_start_seconds": start / RATE,
                    "audio_end_seconds": end / RATE,
                    "visual_action_start_frame": visual_frame,
                    "visual_action_start_seconds": visual_time,
                    "alignment_delta_seconds": visual_time - start / RATE,
                    "pause_after_samples": pause,
                    "pause_after_seconds": pause / RATE,
                }
            )
            if pause:
                out.writeframes(b"\x00\x00" * pause)
                cursor += pause
        tail_samples = round(TAIL * RATE)
        out.writeframes(b"\x00\x00" * tail_samples)
        cursor += tail_samples
    before = loudness(raw_master)
    master = audio / "narration_master.wav"
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw_master), "-af", "loudnorm=I=-20.3:LRA=7:TP=-2.3", "-ar", str(RATE), "-c:a", "pcm_s16le", str(master)],
        check=True,
    )
    with wave.open(str(master), "rb") as normalized:
        if normalized.getnframes() != cursor:
            raise RuntimeError(f"normalization changed PCM duration: {normalized.getnframes()} != {cursor}")
    after = loudness(master)
    first_start = records[0]["audio_start_seconds"]
    last_end = records[-1]["audio_end_seconds"]
    occupied = last_end - first_start
    delivered = words / occupied * 60.0
    section_intervals = {}
    for section in {r["section"] for r in records}:
        rr = [r for r in records if r["section"] == section]
        section_intervals[section] = max(x["audio_end_seconds"] for x in rr) - min(x["audio_start_seconds"] for x in rr)
    peak = spec["peak_section"]
    if any(section_intervals[peak] <= value for key, value in section_intervals.items() if key != peak):
        raise RuntimeError(f"{peak} is not the longest narrated section: {section_intervals}")
    timeline = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": candidate.name,
        "slug": spec["slug"],
        "sample_rate": RATE,
        "video_fps": FPS,
        "sentence_count": len(records),
        "word_count": words,
        "target_delivered_wpm": TARGET_WPM,
        "delivered_wpm": delivered,
        "raw_speech_seconds": speech_samples / RATE,
        "inter_sentence_pause_seconds": sum(allocations) / RATE,
        "master_duration_seconds": cursor / RATE,
        "max_abs_audio_visual_start_delta_seconds": max(abs(r["alignment_delta_seconds"]) for r in records),
        "section_intervals_seconds": section_intervals,
        "peak_section": peak,
        "assembler_path": str(assembler_snapshot.relative_to(candidate)),
        "assembler_sha256": sha256(assembler_snapshot),
        "loudness_before_gain": before,
        "normalization": {"filter":"loudnorm=I=-20.3:LRA=7:TP=-2.3","mode":"dynamic","loudness_after":after},
        "master_raw": str(raw_master.relative_to(ROOT)),
        "master_raw_sha256": sha256(raw_master),
        "master": str(master.relative_to(ROOT)),
        "master_sha256": sha256(master),
        "records": records,
    }
    (audio / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n")
    srt = []
    for i, r in enumerate(records, 1):
        srt += [str(i), f"{srt_time(r['audio_start_seconds'])} --> {srt_time(r['audio_end_seconds'])}", r["text"], ""]
    (candidate / "subtitles.srt").write_text("\n".join(srt))
    snapshot = candidate / "audio"
    if snapshot.exists():
        shutil.rmtree(snapshot)
    shutil.copytree(audio, snapshot)
    print(json.dumps({k: timeline[k] for k in ("sentence_count", "word_count", "delivered_wpm", "master_duration_seconds", "max_abs_audio_visual_start_delta_seconds", "section_intervals_seconds")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
