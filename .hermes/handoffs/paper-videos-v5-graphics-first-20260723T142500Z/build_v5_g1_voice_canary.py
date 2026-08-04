#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
from kokoro_onnx.config import EspeakConfig

ROOT = Path(__file__).resolve().parent
SPEC_PATH = ROOT / "V5_G1_VOICE_CANARY_SPEC.json"
SIGNOFF_PATH = ROOT / "V5_G1_SEMANTIC_SIGNOFF.md"
AUDIO_DIR = ROOT / "v5_g1_audio"
MODEL = Path("/Users/duhokim/HermesOps/tools/kokoro-onnx/kokoro-v1.0.onnx")
VOICES = Path("/Users/duhokim/HermesOps/tools/kokoro-onnx/voices-v1.0.bin")
ESPEAK_LIB = Path("/opt/homebrew/opt/espeak-ng/lib/libespeak-ng.dylib")
ESPEAK_DATA = Path("/opt/homebrew/opt/espeak-ng/share/espeak-ng-data")
VOICE = "am_michael"
MODEL_SPEED = 1.0
SAMPLE_RATE = 48000
TARGET_WPM = 115.0
RECEIPT = ROOT / "V5_G1_AUDIO_RECEIPT.json"
MASTER = ROOT / "V5_G1_Z9_MICHAEL_LISTENING_CANARY.wav"
SCRIPT = ROOT / "V5_G1_Z9_MICHAEL_LISTENING_CANARY.txt"


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


def loudnorm(raw: Path, output: Path) -> dict[str, float]:
    scan = subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-i", str(raw),
            "-af", "loudnorm=I=-16:TP=-2.3:LRA=7:print_format=json",
            "-f", "null", "-",
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    blocks = re.findall(r'\{\s*"input_i".*?\}', scan.stderr, re.S)
    if not blocks:
        raise RuntimeError("no loudness scan")
    measured = json.loads(blocks[-1])
    filt = (
        "loudnorm=I=-16:TP=-2.3:LRA=7:"
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
            "-af", "loudnorm=I=-16:TP=-2.3:LRA=7:print_format=json",
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


def main() -> None:
    for required in (SPEC_PATH, SIGNOFF_PATH, MODEL, VOICES, ESPEAK_LIB, ESPEAK_DATA / "phontab"):
        if not required.is_file():
            raise FileNotFoundError(required)
    spec = json.loads(SPEC_PATH.read_text())
    signoff = SIGNOFF_PATH.read_text()
    if spec.get("marker") != "NEBULAMIND_V5_G1_VOICE_CANARY_SPEC_V1":
        raise RuntimeError("unexpected V5-G1 spec marker")
    if "HWAO_V5_G1_VOICE_CANARY_SIGNED_COMPLETE" not in signoff:
        raise RuntimeError("semantic sign-off missing")
    contract = spec["voice_contract"]
    if contract["voice"] != "Kokoro-82M ONNX am_michael" or float(contract["model_speed"]) != MODEL_SPEED:
        raise RuntimeError("voice contract drift")
    sentences = spec["sentences"]
    if len(sentences) != 9 or any(int(row["n"]) != index for index, row in enumerate(sentences, 1)):
        raise RuntimeError("sentence order drift")
    word_count = sum(int(row["words"]) for row in sentences)
    if word_count != int(spec["passage_budget"]["word_count"]):
        raise RuntimeError("word-count contract drift")
    exact_script = "\n".join(row["text"] for row in sentences) + "\n"
    SCRIPT.write_text(exact_script, encoding="utf-8")
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    config = EspeakConfig(lib_path=str(ESPEAK_LIB), data_path=str(ESPEAK_DATA))
    engine = Kokoro(str(MODEL), str(VOICES), espeak_config=config)
    processed_paths: list[Path] = []
    sentence_receipts: list[dict[str, Any]] = []
    speech_seconds = 0.0
    for row in sentences:
        number = int(row["n"])
        text = row["text"]
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        raw = AUDIO_DIR / f"sentence_{number:02d}_michael_speed1_{text_hash[:12]}_24k.wav"
        processed = AUDIO_DIR / f"sentence_{number:02d}_michael_speed1_{text_hash[:12]}_48k.wav"
        if not raw.is_file():
            samples, sample_rate = engine.create(text, voice=VOICE, speed=MODEL_SPEED, lang="en-us")
            sf.write(raw, samples, sample_rate, subtype="PCM_24")
        if not processed.is_file():
            run([
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw),
                "-af", "highpass=f=65", "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "pcm_s24le", str(processed),
            ])
        duration = float(capture([
            "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nk=1:nw=1", str(processed),
        ]))
        speech_seconds += duration
        processed_paths.append(processed)
        sentence_receipts.append({
            "n": number,
            "text": text,
            "text_sha256": text_hash,
            "words": int(row["words"]),
            "raw": str(raw),
            "raw_sha256": sha256(raw),
            "raw_format": {"codec": "PCM signed 24-bit little-endian", "sample_rate": 24000, "channels": 1},
            "processed": str(processed),
            "processed_sha256": sha256(processed),
            "processed_duration_seconds": round(duration, 6),
            "anchors": row["anchors"],
        })
        print(f"sentence {number}/9 {duration:.3f}s", flush=True)

    pause_min, pause_max = [float(value) for value in contract["inter_sentence_pause_seconds"]]
    desired_total = word_count / TARGET_WPM * 60.0
    pause_seconds = (desired_total - speech_seconds) / (len(sentences) - 1)
    pause_seconds = min(pause_max, max(pause_min, pause_seconds))
    pause = np.zeros(round(SAMPLE_RATE * pause_seconds), dtype=np.float32)
    parts: list[np.ndarray] = []
    for index, path in enumerate(processed_paths):
        samples, sample_rate = sf.read(path, dtype="float32")
        if sample_rate != SAMPLE_RATE or samples.ndim != 1:
            raise RuntimeError(f"unexpected processed format: {path}")
        parts.append(samples)
        if index < len(processed_paths) - 1:
            parts.append(pause)
    combined = np.concatenate(parts)
    premaster = AUDIO_DIR / "V5_G1_Z9_MICHAEL_PREMASTER.wav"
    sf.write(premaster, combined, SAMPLE_RATE, subtype="PCM_24")
    loudness = loudnorm(premaster, MASTER)
    total_duration = float(capture([
        "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nk=1:nw=1", str(MASTER),
    ]))
    delivered_wpm = word_count / total_duration * 60.0
    duration_min, duration_max = [float(value) for value in spec["passage_budget"]["contract_duration_seconds"]]
    wpm_min, wpm_max = [float(value) for value in spec["passage_budget"]["contract_delivered_wpm"]]
    if not pause_min <= pause_seconds <= pause_max:
        raise RuntimeError(f"pause outside contract: {pause_seconds}")
    if not duration_min <= total_duration <= duration_max:
        raise RuntimeError(f"duration outside contract: {total_duration}")
    if not wpm_min <= delivered_wpm <= wpm_max:
        raise RuntimeError(f"delivered WPM outside contract: {delivered_wpm}")
    if not (-16.9 <= loudness["integrated_lufs"] <= -15.1 and loudness["true_peak_dbtp"] <= -2.0):
        raise RuntimeError(f"loudness outside review target: {loudness}")

    receipt = {
        "marker": "NEBULAMIND_V5_G1_AUDIO_BUILD_PASS",
        "completed_at_utc": now(),
        "gate": "V5-G1 voice canary only",
        "spec": str(SPEC_PATH),
        "spec_sha256": sha256(SPEC_PATH),
        "semantic_signoff": str(SIGNOFF_PATH),
        "semantic_signoff_sha256": sha256(SIGNOFF_PATH),
        "voice_provider": "local Kokoro-82M v1.0 ONNX",
        "voice": VOICE,
        "model_speed": MODEL_SPEED,
        "post_tempo_correction": None,
        "word_count": word_count,
        "sentence_count": len(sentences),
        "raw_speech_seconds": round(speech_seconds, 6),
        "pause_seconds_each": round(pause_seconds, 6),
        "pause_count": len(sentences) - 1,
        "total_duration_seconds": round(total_duration, 6),
        "delivered_wpm": round(delivered_wpm, 3),
        "loudness": loudness,
        "script": str(SCRIPT),
        "script_sha256": sha256(SCRIPT),
        "listening_master": str(MASTER),
        "listening_master_sha256": sha256(MASTER),
        "listening_master_bytes": MASTER.stat().st_size,
        "listening_master_format": {"codec": "PCM signed 24-bit little-endian", "sample_rate": SAMPLE_RATE, "channels": 1},
        "sentences": sentence_receipts,
        "checks": {
            "signed_text_used_exactly": "PASS",
            "native_voice_speed_1_0": "PASS",
            "no_post_tempo_correction": "PASS",
            "pause_range": "PASS",
            "duration_45_to_60_seconds": "PASS",
            "delivered_wpm_105_to_125": "PASS",
            "lossless_listening_master": "PASS",
            "loudness_and_headroom": "PASS",
        },
        "next_gate": "Independent ASR/semantic QA, then Duho ear-check. No facial animation or video.",
        "video_created": False,
        "animation_created": False,
        "youtube_mutation": False,
        "visibility_mutation": False,
        "website_mutation": False,
        "git_mutation": False,
    }
    temporary = RECEIPT.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    os.replace(temporary, RECEIPT)
    print(json.dumps({
        "status": "PASS",
        "master": str(MASTER),
        "sha256": receipt["listening_master_sha256"],
        "duration": receipt["total_duration_seconds"],
        "wpm": receipt["delivered_wpm"],
        "pause_each": receipt["pause_seconds_each"],
        "loudness": loudness,
    }, indent=2))


if __name__ == "__main__":
    main()
