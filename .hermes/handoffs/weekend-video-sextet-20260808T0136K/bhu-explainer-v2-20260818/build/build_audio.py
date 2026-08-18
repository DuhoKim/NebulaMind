#!/usr/bin/env python3
"""Synthesize exact gated narration through the managed gateway on a fixed card grid."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request
import wave
from pathlib import Path
from typing import Any

import pipeline

RATE = 48000
CHANNELS = 1
SAMPLE_WIDTH = 2
MODEL = "gpt-4o-mini-tts"
VOICE = "alloy"
SPEED = 1.0
CARD_LEAD_SECONDS = 0.40
SENTENCE_PAUSE_SECONDS = 0.08
CARD_TAIL_SECONDS = 0.75
FPS = 30
HERMES_CHECKOUT = Path("/Users/duhokim/.hermes/hermes-agent")
HERMES_PYTHON = HERMES_CHECKOUT / "venv/bin/python"
BASE_INSTRUCTIONS = (
    "Read the input exactly as written in a calm, measured public-science voice. "
    "Do not add, omit, summarize, or rewrite words. Speak every number and percentage carefully. "
    "Pronounce Brown-Lee-Rho as Brown, Lee, Row; Brown-Bethe as Brown, Bay-tuh; "
    "and PSR letter by letter."
)
BETHE_RETAKE_IDS = {"c04s05", "c09s02"}


def instruction_policy(ident: str) -> dict[str, str]:
    if ident in BETHE_RETAKE_IDS:
        instructions = (
            BASE_INSTRUCTIONS
            + " For the proper name Brown-Bethe in this sentence, pronounce Bethe exactly as BAY-tuh, "
            "with two clear syllables. Do not say Bessie, Bethy, or Betty."
        )
        version = "bethe-pronunciation-retake-v2"
    else:
        instructions = BASE_INSTRUCTIONS
        version = "generic-exact-read-v1"
    return {"version": version, "instructions": instructions, "instructions_sha256": text_sha(instructions)}


def text_sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def plan_timeline(panels: list[dict], durations: dict[str, list[float]]) -> dict[str, Any]:
    card_start_sample = 0
    records: list[dict[str, Any]] = []
    cards: list[dict[str, Any]] = []
    lead_samples = round(CARD_LEAD_SECONDS * RATE)
    pause_samples = round(SENTENCE_PAUSE_SECONDS * RATE)
    for panel in panels:
        planned_frames = round(float(panel["planned_seconds"]) * FPS)
        speech_frames = [round(duration * RATE) for duration in durations[panel["id"]]]
        required_samples = (
            round(CARD_LEAD_SECONDS * RATE)
            + sum(speech_frames)
            + max(0, len(speech_frames) - 1) * round(SENTENCE_PAUSE_SECONDS * RATE)
            + round(CARD_TAIL_SECONDS * RATE)
        )
        required_frames = (required_samples * FPS + RATE - 1) // RATE
        effective_frames = max(planned_frames, required_frames)
        card_duration_samples = effective_frames * (RATE // FPS)
        card_end_sample = card_start_sample + card_duration_samples
        sentences = pipeline.split_sentences(panel["narration"])
        sentence_durations = durations[panel["id"]]
        if len(sentences) != len(sentence_durations):
            raise RuntimeError(f"panel {panel['id']}: sentence duration count mismatch")
        cursor = card_start_sample + lead_samples
        card_records = []
        for index, (sentence, duration) in enumerate(zip(sentences, sentence_durations), 1):
            duration_samples = round(duration * RATE)
            start_sample = cursor
            end_sample = start_sample + duration_samples
            ident = f"c{int(panel['id']):02d}s{index:02d}"
            record = {
                "id": ident,
                "card_id": panel["id"],
                "sentence_index": index,
                "text": sentence,
                "text_sha256": text_sha(sentence),
                "start_sample": start_sample,
                "end_sample": end_sample,
                "duration_samples": duration_samples,
                "start_seconds": start_sample / RATE,
                "end_seconds": end_sample / RATE,
                "audio_duration_seconds": duration_samples / RATE,
            }
            records.append(record)
            card_records.append(record)
            cursor = end_sample + (pause_samples if index < len(sentences) else 0)
        speech_end_sample = card_records[-1]["end_sample"]
        if speech_end_sample > card_end_sample:
            over = (speech_end_sample - card_end_sample) / RATE
            raise RuntimeError(f"panel {panel['id']}: speech overruns fixed card by {over:.3f}s")
        cards.append(
            {
                "card_id": panel["id"],
                "heading": panel["assertion_heading"],
                "narration": panel["narration"],
                "start_sample": card_start_sample,
                "speech_start_sample": card_records[0]["start_sample"],
                "speech_end_sample": speech_end_sample,
                "end_sample": card_end_sample,
                "start_seconds": card_start_sample / RATE,
                "speech_start_seconds": card_records[0]["start_sample"] / RATE,
                "speech_end_seconds": speech_end_sample / RATE,
                "end_seconds": card_end_sample / RATE,
                "sentence_ids": [record["id"] for record in card_records],
                "tail_dwell_seconds": (card_end_sample - speech_end_sample) / RATE,
                "planned_seconds": float(panel["planned_seconds"]),
                "effective_seconds": card_duration_samples / RATE,
                "frame_count": effective_frames,
                "timing_extension_seconds": card_duration_samples / RATE - float(panel["planned_seconds"]),
            }
        )
        card_start_sample = card_end_sample
    master_duration = card_start_sample / RATE
    if not 240.0 <= master_duration <= 360.0:
        raise RuntimeError(f"audio-first master duration outside 4–6 minute contract: {master_duration:.3f}s")
    if cards[0]["end_seconds"] > 35.0:
        raise RuntimeError(f"opening verdict misses 35-second deadline: {cards[0]['end_seconds']:.3f}s")
    return {
        "sample_rate_hz": RATE,
        "master_sample_count": card_start_sample,
        "master_duration_seconds": card_start_sample / RATE,
        "records": records,
        "cards": cards,
    }


def _gateway() -> Any:
    sys.path.insert(0, str(HERMES_CHECKOUT))
    from tools.managed_tool_gateway import resolve_managed_tool_gateway

    return resolve_managed_tool_gateway("openai-audio")


def synthesize(text: str, instructions: str, output: Path, failure_log: Path) -> None:
    gateway = _gateway()
    body = json.dumps(
        {
            "model": MODEL,
            "voice": VOICE,
            "input": text,
            "speed": SPEED,
            "response_format": "wav",
            "instructions": instructions,
        },
        ensure_ascii=False,
    ).encode("utf-8")
    url = gateway.gateway_origin.rstrip("/") + "/v1/audio/speech"
    for attempt in range(1, 4):
        request = urllib.request.Request(url, data=body, method="POST")
        request.add_header("Authorization", "Bearer " + gateway.nous_user_token)
        request.add_header("Content-Type", "application/json")
        try:
            data = urllib.request.urlopen(request, timeout=240).read()
            if not data:
                raise RuntimeError("empty TTS response")
            output.write_bytes(data)
            probe = subprocess.run(
                [
                    "ffprobe",
                    "-v",
                    "error",
                    "-show_entries",
                    "format=duration",
                    "-of",
                    "csv=p=0",
                    str(output),
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            if float(probe.stdout.strip()) <= 0:
                raise RuntimeError("non-positive TTS duration")
            return
        except Exception as exc:
            failure_log.parent.mkdir(parents=True, exist_ok=True)
            with failure_log.open("a", encoding="utf-8") as handle:
                handle.write(
                    json.dumps(
                        {
                            "text_sha256": text_sha(text),
                            "attempt": attempt,
                            "error_type": type(exc).__name__,
                            "error": str(exc)[:500],
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )
            if output.exists():
                rejected = output.with_name(output.stem + f"-rejected-attempt-{attempt}" + output.suffix)
                output.replace(rejected)
            if attempt == 3:
                raise
            time.sleep(2 * attempt)


def convert_to_pcm(source: Path, destination: Path) -> None:
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(source),
            "-ac",
            str(CHANNELS),
            "-ar",
            str(RATE),
            "-c:a",
            "pcm_s16le",
            str(destination),
        ],
        check=True,
    )


def wav_frames(path: Path) -> tuple[bytes, int]:
    with wave.open(str(path), "rb") as source:
        shape = (source.getnchannels(), source.getsampwidth(), source.getframerate())
        if shape != (CHANNELS, SAMPLE_WIDTH, RATE):
            raise RuntimeError(f"unexpected PCM shape for {path}: {shape}")
        frames = source.readframes(source.getnframes())
        return frames, source.getnframes()


def stamp_srt(seconds: float) -> str:
    milliseconds = round(seconds * 1000)
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    secs, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"


def stamp_vtt(seconds: float) -> str:
    return stamp_srt(seconds).replace(",", ".")


def write_captions(timeline: dict[str, Any], audio_dir: Path) -> tuple[Path, Path]:
    srt_lines: list[str] = []
    vtt_lines: list[str] = ["WEBVTT", ""]
    for index, record in enumerate(timeline["records"], 1):
        srt_lines.extend(
            [
                str(index),
                f"{stamp_srt(record['start_seconds'])} --> {stamp_srt(record['end_seconds'])}",
                record["text"],
                "",
            ]
        )
        vtt_lines.extend(
            [
                str(index),
                f"{stamp_vtt(record['start_seconds'])} --> {stamp_vtt(record['end_seconds'])}",
                record["text"],
                "",
            ]
        )
    srt_path = audio_dir / "narration.srt"
    vtt_path = audio_dir / "narration.vtt"
    srt_path.write_text("\n".join(srt_lines), encoding="utf-8")
    vtt_path.write_text("\n".join(vtt_lines), encoding="utf-8")
    return srt_path, vtt_path


def main() -> int:
    frozen = pipeline.load_frozen_inputs()
    audio_dir = pipeline.BUILD / "audio"
    raw_dir = audio_dir / "raw"
    pcm_dir = audio_dir / "pcm"
    receipt_dir = audio_dir / "sentence_receipts"
    raw_dir.mkdir(parents=True, exist_ok=True)
    pcm_dir.mkdir(parents=True, exist_ok=True)
    receipt_dir.mkdir(parents=True, exist_ok=True)
    failures = audio_dir / "tts_failures.jsonl"

    durations: dict[str, list[float]] = {}
    sentence_assets: dict[str, dict[str, Any]] = {}
    for panel in frozen["panels"]:
        durations[panel["id"]] = []
        for sentence_index, sentence in enumerate(pipeline.split_sentences(panel["narration"]), 1):
            ident = f"c{int(panel['id']):02d}s{sentence_index:02d}"
            raw = raw_dir / f"{ident}.wav"
            pcm = pcm_dir / f"{ident}.wav"
            receipt = receipt_dir / f"{ident}.json"
            expected_text_hash = text_sha(sentence)
            policy = instruction_policy(ident)
            if raw.exists():
                if not receipt.exists():
                    raise RuntimeError(f"refusing filename-only TTS cache without receipt: {raw}")
                cached = json.loads(receipt.read_text(encoding="utf-8"))
                cached_policy = cached.get("instruction_policy", "generic-exact-read-v1")
                if (
                    cached["text_sha256"] != expected_text_hash
                    or cached["model"] != MODEL
                    or cached["voice"] != VOICE
                    or cached_policy != policy["version"]
                ):
                    raise RuntimeError(f"TTS cache contract mismatch: {ident}")
            else:
                synthesize(sentence, policy["instructions"], raw, failures)
            convert_to_pcm(raw, pcm)
            _, frame_count = wav_frames(pcm)
            duration = frame_count / RATE
            durations[panel["id"]].append(duration)
            record = {
                "id": ident,
                "card_id": panel["id"],
                "sentence_index": sentence_index,
                "text": sentence,
                "text_sha256": expected_text_hash,
                "model": MODEL,
                "voice": VOICE,
                "speed": SPEED,
                "instruction_policy": policy["version"],
                "instructions_sha256": policy["instructions_sha256"],
                "provider_route": "Hermes managed OpenAI audio gateway",
                "raw_audio": str(raw.relative_to(pipeline.BUILD)),
                "raw_audio_sha256": pipeline.sha256(raw),
                "pcm_audio": str(pcm.relative_to(pipeline.BUILD)),
                "pcm_audio_sha256": pipeline.sha256(pcm),
                "pcm_frames": frame_count,
                "pcm_duration_seconds": duration,
            }
            receipt.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            sentence_assets[ident] = record
            print(ident, f"{duration:.3f}s")

    timeline = plan_timeline(frozen["panels"], durations)
    total_samples = timeline["master_sample_count"]
    master_bytes = bytearray(total_samples * SAMPLE_WIDTH)
    for record in timeline["records"]:
        asset = sentence_assets[record["id"]]
        pcm_bytes, frame_count = wav_frames(pipeline.BUILD / asset["pcm_audio"])
        if frame_count != record["duration_samples"]:
            raise RuntimeError(f"duration drift for {record['id']}")
        offset = record["start_sample"] * SAMPLE_WIDTH
        master_bytes[offset : offset + len(pcm_bytes)] = pcm_bytes
        record.update(asset)

    raw_master = audio_dir / "narration_master_raw.wav"
    with wave.open(str(raw_master), "wb") as output:
        output.setnchannels(CHANNELS)
        output.setsampwidth(SAMPLE_WIDTH)
        output.setframerate(RATE)
        output.writeframes(master_bytes)

    master = audio_dir / "narration_master.wav"
    master_duration = total_samples / RATE
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(raw_master),
            "-af",
            f"loudnorm=I=-16:LRA=7:TP=-2.3,apad=whole_dur={master_duration:.9f},atrim=end={master_duration:.9f}",
            "-ar",
            str(RATE),
            "-ac",
            str(CHANNELS),
            "-c:a",
            "pcm_s16le",
            str(master),
        ],
        check=True,
    )
    _, normalized_frames = wav_frames(master)
    if normalized_frames != total_samples:
        raise RuntimeError(f"normalized master sample count mismatch: {normalized_frames} != {total_samples}")

    srt_path, vtt_path = write_captions(timeline, audio_dir)
    timeline.update(
        {
            "status": "PASS_EXACT_TTS_INPUT_AND_FIXED_TIMELINE_PENDING_FINAL_ASR",
            "model": MODEL,
            "voice": VOICE,
            "speed": SPEED,
            "provider_route": "Hermes managed OpenAI audio gateway",
            "card_lead_seconds": CARD_LEAD_SECONDS,
            "sentence_pause_seconds": SENTENCE_PAUSE_SECONDS,
            "minimum_card_tail_seconds": CARD_TAIL_SECONDS,
            "gated_script_sha256": pipeline.sha256(pipeline.SCRIPT),
            "gated_storyboard_sha256": pipeline.sha256(pipeline.STORYBOARD),
            "raw_master": str(raw_master.relative_to(pipeline.BUILD)),
            "raw_master_sha256": pipeline.sha256(raw_master),
            "master_audio": str(master.relative_to(pipeline.BUILD)),
            "master_audio_sha256": pipeline.sha256(master),
            "srt": str(srt_path.relative_to(pipeline.BUILD)),
            "srt_sha256": pipeline.sha256(srt_path),
            "vtt": str(vtt_path.relative_to(pipeline.BUILD)),
            "vtt_sha256": pipeline.sha256(vtt_path),
            "sentence_count": len(timeline["records"]),
            "tts_inputs_reconstruct_all_panel_narration_exactly": True,
        }
    )
    timeline_path = audio_dir / "timeline.json"
    timeline_path.write_text(json.dumps(timeline, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": timeline["status"],
                "sentence_count": timeline["sentence_count"],
                "duration_seconds": timeline["master_duration_seconds"],
                "master_audio_sha256": timeline["master_audio_sha256"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
