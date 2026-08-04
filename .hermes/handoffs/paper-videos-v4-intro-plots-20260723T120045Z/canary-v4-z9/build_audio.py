#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import textwrap
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
from kokoro_onnx.config import EspeakConfig

ROOT = Path(__file__).resolve().parent
LANE = ROOT.parent
SPEC_PATH = LANE / "V4_Z9_CANARY_SPEC.json"
VISUALS_RECEIPT = ROOT / "visuals_receipt.json"
AUDIO_DIR = ROOT / "audio"
ASSETS_RECEIPT = ROOT / "assets_receipt.json"
KOKORO_MODEL = Path("/Users/duhokim/HermesOps/tools/kokoro-onnx/kokoro-v1.0.onnx")
KOKORO_VOICES = Path("/Users/duhokim/HermesOps/tools/kokoro-onnx/voices-v1.0.bin")
ESPEAK_LIB = Path("/opt/homebrew/opt/espeak-ng/lib/libespeak-ng.dylib")
ESPEAK_DATA = Path("/opt/homebrew/opt/espeak-ng/share/espeak-ng-data")
VOICE = "am_michael"
VOICE_SPEED = 1.0
SAMPLE_RATE = 48000
INTER_SLOT_GAP = 0.35
FINAL_BREATH = 0.8


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def capture(args: list[str]) -> str:
    return subprocess.check_output(args, text=True).strip()


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower().replace("’", "'").replace("–", "-"))


def sentence_chunks(text: str, max_words: int = 16) -> list[str]:
    chunks: list[str] = []
    for sentence in [part.strip() for part in re.split(r"(?<=[.!?])\s+", text.strip()) if part.strip()]:
        words = sentence.split()
        while len(words) > max_words:
            take = max_words
            for index in range(max_words - 1, 7, -1):
                if words[index - 1].endswith((",", ";", ":")):
                    take = index
                    break
            chunks.append(" ".join(words[:take]))
            words = words[take:]
        if words:
            chunks.append(" ".join(words))
    return chunks


def srt_time(seconds: float) -> str:
    milliseconds = round(seconds * 1000)
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    secs, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"


def loudnorm(raw: Path, output: Path) -> dict[str, float]:
    scan = subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-i", str(raw),
            "-af", "loudnorm=I=-16:TP=-2.0:LRA=7:print_format=json",
            "-f", "null", "-",
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    blocks = re.findall(r'\{\s*"input_i".*?\}', scan.stderr, re.S)
    if not blocks:
        raise RuntimeError("no loudnorm scan")
    measured = json.loads(blocks[-1])
    filt = (
        "loudnorm=I=-16:TP=-2.0:LRA=7:"
        f"measured_I={measured['input_i']}:measured_LRA={measured['input_lra']}:"
        f"measured_TP={measured['input_tp']}:measured_thresh={measured['input_thresh']}:"
        f"offset={measured['target_offset']}:"
        f"linear={'true' if measured['normalization_type'] == 'linear' else 'false'}"
    )
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw),
        "-af", filt, "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "pcm_s24le", str(output),
    ])
    verify = subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-i", str(output),
            "-af", "loudnorm=I=-16:TP=-2.0:LRA=7:print_format=json",
            "-f", "null", "-",
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    values = json.loads(re.findall(r'\{\s*"input_i".*?\}', verify.stderr, re.S)[-1])
    return {
        "integrated_lufs": float(values["input_i"]),
        "true_peak_dbtp": float(values["input_tp"]),
        "lra_lu": float(values["input_lra"]),
    }


def write_srt(scenes: list[dict[str, Any]], timeline: list[dict[str, Any]], path: Path) -> list[dict[str, Any]]:
    cues: list[dict[str, Any]] = []
    index = 1
    for scene, row in zip(scenes, timeline):
        chunks = sentence_chunks(scene["narration"])
        counts = [len(tokens(chunk)) for chunk in chunks]
        total = sum(counts)
        cursor = 0
        for chunk, count in zip(chunks, counts):
            start = float(row["visual_start"]) + float(row["speech_duration"]) * cursor / total
            cursor += count
            end = float(row["visual_start"]) + float(row["speech_duration"]) * cursor / total
            if cues:
                start = max(start, float(cues[-1]["end"]) + 0.03)
            end = max(end - 0.02, start + 0.55)
            cues.append({"index": index, "start": round(start, 3), "end": round(end, 3), "text": chunk})
            index += 1
    blocks: list[str] = []
    for cue in cues:
        wrapped = "\n".join(textwrap.wrap(cue["text"], width=58, break_long_words=False, break_on_hyphens=False))
        blocks.append(f"{cue['index']}\n{srt_time(cue['start'])} --> {srt_time(cue['end'])}\n{wrapped}\n")
    path.write_text("\n".join(blocks), encoding="utf-8")
    expected = " ".join(scene["narration"].strip() for scene in scenes)
    observed = " ".join(cue["text"] for cue in cues)
    if re.sub(r"\s+", " ", expected).strip() != re.sub(r"\s+", " ", observed).strip():
        raise RuntimeError("SRT text drift")
    return cues


def main() -> None:
    for required in (SPEC_PATH, VISUALS_RECEIPT, KOKORO_MODEL, KOKORO_VOICES, ESPEAK_LIB, ESPEAK_DATA / "phontab"):
        if not required.is_file():
            raise FileNotFoundError(required)
    spec = json.loads(SPEC_PATH.read_text())
    visuals = json.loads(VISUALS_RECEIPT.read_text())
    if visuals["spec_sha256"] != sha256(SPEC_PATH):
        raise RuntimeError("visual lineage uses an older spec")
    scenes = spec["scenes"]
    if len(scenes) != 10 or any(int(scene["slot"]) != index for index, scene in enumerate(scenes)):
        raise RuntimeError("unexpected slot contract")
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    config = EspeakConfig(lib_path=str(ESPEAK_LIB), data_path=str(ESPEAK_DATA))
    engine = Kokoro(str(KOKORO_MODEL), str(KOKORO_VOICES), espeak_config=config)
    processed_paths: list[Path] = []
    speech_durations: list[float] = []
    slot_hashes: list[dict[str, str]] = []
    for scene in scenes:
        slot = int(scene["slot"])
        text = scene["narration"].strip()
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        raw = AUDIO_DIR / f"slot_{slot:02d}_michael_{text_hash[:12]}_24k.wav"
        processed = AUDIO_DIR / f"slot_{slot:02d}_michael_{text_hash[:12]}_48k.wav"
        if not raw.is_file():
            samples, sample_rate = engine.create(text, voice=VOICE, speed=VOICE_SPEED, lang="en-us")
            sf.write(raw, samples, sample_rate, subtype="PCM_24")
        if not processed.is_file():
            run([
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw),
                "-af", "highpass=f=65", "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "pcm_s24le", str(processed),
            ])
        duration = float(capture([
            "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nk=1:nw=1", str(processed),
        ]))
        if duration <= 3.0:
            raise RuntimeError(f"slot {slot}: speech duration too short")
        processed_paths.append(processed)
        speech_durations.append(duration)
        slot_hashes.append({
            "text_sha256": text_hash,
            "raw_sha256": sha256(raw),
            "processed_sha256": sha256(processed),
        })
        print(f"AUDIO {slot + 1}/10 slot {slot:02d} {duration:.3f}s", flush=True)

    gap = np.zeros(round(SAMPLE_RATE * INTER_SLOT_GAP), dtype=np.float32)
    parts: list[np.ndarray] = []
    for index, path in enumerate(processed_paths):
        samples, sample_rate = sf.read(path, dtype="float32")
        if sample_rate != SAMPLE_RATE or samples.ndim != 1:
            raise RuntimeError(f"unexpected audio format: {path}")
        parts.append(samples)
        if index < len(processed_paths) - 1:
            parts.append(gap)
    combined = np.concatenate(parts)
    premaster = AUDIO_DIR / "z9_V4_MICHAEL_PREMASTER.wav"
    master = AUDIO_DIR / "z9_V4_MICHAEL_MASTER.wav"
    sf.write(premaster, combined, SAMPLE_RATE, subtype="PCM_24")
    loudness = loudnorm(premaster, master)
    master_duration = float(capture([
        "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nk=1:nw=1", str(master),
    ]))

    timeline: list[dict[str, Any]] = []
    cursor = 0.0
    for index, (scene, speech_duration) in enumerate(zip(scenes, speech_durations)):
        gap_after = INTER_SLOT_GAP if index < len(scenes) - 1 else 0.0
        final_breath = FINAL_BREATH if index == len(scenes) - 1 else 0.0
        timeline.append({
            "slot": int(scene["slot"]),
            "audio_start": round(cursor, 6),
            "visual_start": round(cursor, 6),
            "speech_duration": round(speech_duration, 6),
            "gap_after": gap_after,
            "visual_duration": round(speech_duration + gap_after + final_breath, 6),
            **slot_hashes[index],
        })
        cursor += speech_duration + gap_after
    if abs(cursor - master_duration) > 0.03:
        raise RuntimeError(f"combined timing drift: {cursor} != {master_duration}")

    srt = ROOT / "NEBULAMIND_Z9_V4_CANARY.srt"
    cues = write_srt(scenes, timeline, srt)
    word_count = sum(len(tokens(scene["narration"])) for scene in scenes)
    speech_seconds = sum(speech_durations)
    effective_wpm = word_count / speech_seconds * 60.0
    expected_video_duration = master_duration + FINAL_BREATH
    if not 120.0 <= effective_wpm <= 145.0:
        raise RuntimeError(f"Michael pace outside approved range: {effective_wpm:.3f} wpm")
    if expected_video_duration > 180.0:
        raise RuntimeError(f"video duration exceeds signed cap: {expected_video_duration:.3f}s")
    if speech_durations[0] > 20.0:
        raise RuntimeError(f"question hook exceeds 20 seconds: {speech_durations[0]:.3f}s")
    for slot in (4, 5, 6):
        if speech_durations[slot] < 8.0:
            raise RuntimeError(f"evidence slot {slot} under 8 seconds")
    if not (-16.9 <= loudness["integrated_lufs"] <= -15.1 and loudness["true_peak_dbtp"] <= -1.5):
        raise RuntimeError(f"loudness outside target: {loudness}")

    receipt = {
        "marker": "NEBULAMIND_V4_Z9_AUDIO_ASSETS_COMPLETE",
        "completed_at_utc": now(),
        "key": "z9-metallicity",
        "spec": str(SPEC_PATH),
        "spec_sha256": sha256(SPEC_PATH),
        "visuals_receipt": str(VISUALS_RECEIPT),
        "visuals_receipt_sha256": sha256(VISUALS_RECEIPT),
        "voice_provider": "local Kokoro-82M v1.0 ONNX",
        "voice": VOICE,
        "voice_speed": VOICE_SPEED,
        "word_count": word_count,
        "speech_seconds": round(speech_seconds, 6),
        "effective_wpm": round(effective_wpm, 3),
        "narration_master": str(master),
        "narration_sha256": sha256(master),
        "narration_duration": round(master_duration, 6),
        "loudness": loudness,
        "srt": str(srt),
        "srt_sha256": sha256(srt),
        "srt_cues": len(cues),
        "timeline": timeline,
        "layouts": [row["path"] for row in visuals["layouts"]],
        "expected_video_duration": round(expected_video_duration, 6),
        "checks": {
            "caption_exactness": "PASS",
            "duration_under_180s": "PASS",
            "question_hook_within_20s": "PASS",
            "evidence_slots_at_least_8s": "PASS",
            "voice_and_speed": "PASS",
            "loudness": "PASS",
        },
        "publication_state": "local V4 canary only; not uploaded",
        "youtube_mutation": False,
        "website_mutation": False,
        "git_mutation": False,
    }
    temporary = ASSETS_RECEIPT.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    os.replace(temporary, ASSETS_RECEIPT)
    print(json.dumps({
        "status": "PASS",
        "word_count": word_count,
        "effective_wpm": round(effective_wpm, 3),
        "master_duration": round(master_duration, 3),
        "expected_video_duration": round(expected_video_duration, 3),
        "loudness": loudness,
        "srt_cues": len(cues),
    }, indent=2))


if __name__ == "__main__":
    main()
