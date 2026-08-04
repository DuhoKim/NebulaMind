#!/usr/bin/env python3
"""Generate scene-aligned Emma narration for the overnight-report explainer."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

from overnight_content import DURATION, NARRATION, SCENE_BOUNDARIES, SOURCE_CONTRACT

BASE = Path(__file__).resolve().parent
EDGE_TTS = Path("/Users/duhokim/.hermes/hermes-agent/venv/bin/edge-tts")
VOICE = "en-US-EmmaNeural"
INITIAL_RATE_PERCENT = 20
SPEECH_START = 0.35
SPEECH_END_PAD = 0.70
RAW = BASE / "narration_raw"
SCENES = BASE / "narration_scenes"
DRIVERS = BASE / "driver_audio"
for directory in (RAW, SCENES, DRIVERS):
    directory.mkdir(parents=True, exist_ok=True)


def probe(path: Path) -> float:
    return float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=nk=1:nw=1", str(path),
    ], text=True).strip())


def synthesize_scene(index: int, text: str, scene_duration: float) -> dict:
    target_speech = scene_duration - SPEECH_START - SPEECH_END_PAD

    def synthesize(rate_percent: int) -> tuple[Path, float, float, str]:
        rate = f"{rate_percent:+d}%"
        path = RAW / f"scene_{index:02d}_{VOICE}_rate_{rate_percent:+d}.mp3"
        subprocess.run([
            str(EDGE_TTS), "--voice", VOICE, f"--rate={rate}",
            "--text", text, "--write-media", str(path),
        ], check=True)
        seconds = probe(path)
        return path, seconds, seconds / target_speech, rate

    raw, raw_duration, tempo, synthesis_rate = synthesize(INITIAL_RATE_PERCENT)
    if not 0.92 <= tempo <= 1.08:
        derived = round((tempo * (1 + INITIAL_RATE_PERCENT / 100) - 1) * 100)
        derived = max(-15, min(65, derived))
        raw, raw_duration, tempo, synthesis_rate = synthesize(derived)
    if tempo < 0.85:
        tempo = 1.0
    if tempo > 1.15:
        raise RuntimeError(f"scene {index}: atempo {tempo:.4f} exceeds natural limit")

    output = SCENES / f"scene_{index:02d}_female_exact.wav"
    filt = (
        f"[1:a]atempo={tempo:.8f},adelay={int(SPEECH_START * 1000)}ms:all=1,"
        f"aresample=16000[voice];[0:a][voice]amix=2:duration=first:normalize=0,"
        "alimiter=limit=.95[out]"
    )
    subprocess.run([
        "ffmpeg", "-y", "-v", "error",
        "-f", "lavfi", "-t", f"{scene_duration:.6f}", "-i", "anullsrc=r=16000:cl=mono",
        "-i", str(raw), "-filter_complex", filt, "-map", "[out]",
        "-ac", "1", "-ar", "16000", "-t", f"{scene_duration:.6f}",
        "-c:a", "pcm_s16le", str(output),
    ], check=True)
    actual_speech = raw_duration / tempo
    return {
        "scene": index,
        "text": text,
        "scene_duration": round(scene_duration, 6),
        "raw_duration": round(raw_duration, 6),
        "target_speech_duration": round(target_speech, 6),
        "synthesis_rate": synthesis_rate,
        "atempo": round(tempo, 6),
        "actual_speech_duration": round(actual_speech, 6),
        "speech_start": SPEECH_START,
        "trailing_breathing_room": round(scene_duration - SPEECH_START - actual_speech, 6),
        "output": str(output),
    }


def main() -> None:
    rows = []
    for index, text in enumerate(NARRATION, 1):
        rows.append(synthesize_scene(index, text, SCENE_BOUNDARIES[index] - SCENE_BOUNDARIES[index - 1]))
    concat = BASE / "female_concat.txt"
    concat.write_text("".join(f"file '{row['output']}'\n" for row in rows), encoding="utf-8")
    driver = DRIVERS / "overnight_report_female_exact_narration_73s.wav"
    subprocess.run([
        "ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
        "-i", str(concat), "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", str(driver),
    ], check=True)
    duration = probe(driver)
    if abs(duration - DURATION) > 0.02:
        raise RuntimeError(f"driver duration {duration} != {DURATION}")
    if min(row["trailing_breathing_room"] for row in rows) < 0.68:
        raise RuntimeError("one or more scenes violate the 0.7-second breathing-room gate")
    receipt = {
        "marker": "NEBULAMIND_OVERNIGHT_REPORT_V1_EXPLICIT_FEMALE_NARRATION",
        "voice": VOICE,
        "voice_metadata": {"gender": "Female", "style": "Cheerful, Clear, Conversational"},
        "driver": str(driver),
        "duration": duration,
        "source_contract": SOURCE_CONTRACT,
        "scenes": rows,
    }
    (BASE / "narration_receipt.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "marker": receipt["marker"], "driver": str(driver), "duration": duration,
        "rates": [row["synthesis_rate"] for row in rows],
        "atempo": [row["atempo"] for row in rows],
        "breathing_room": [row["trailing_breathing_room"] for row in rows],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
