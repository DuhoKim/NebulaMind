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
from kokoro_onnx import EspeakConfig, Kokoro

ROOT = Path(__file__).resolve().parent
SPEC_PATH = ROOT / "V5_G3_MOTION_GRAPHICS_SPEC.json"
STORYBOARD_PATH = ROOT / "V5_G2_Z9_STORYBOARD.json"
SIGNOFF_PATH = ROOT / "V5_G3_SEMANTIC_SIGNOFF.md"
OUT = ROOT / "canary-g3"
AUDIO = OUT / "audio"
MASTER = OUT / "V5_G3_NARRATION_MASTER.wav"
RECEIPT = OUT / "V5_G3_AUDIO_RECEIPT.json"
TRANSCRIPT = OUT / "V5_G3_NARRATION_EXACT.txt"
MODEL = Path("/Users/duhokim/HermesOps/tools/kokoro-onnx/kokoro-v1.0.onnx")
VOICES = Path("/Users/duhokim/HermesOps/tools/kokoro-onnx/voices-v1.0.bin")
ESPEAK_LIB = Path("/opt/homebrew/lib/libespeak-ng.dylib")
ESPEAK_DATA = Path("/opt/homebrew/share/espeak-ng-data")
FFMPEG = "/opt/homebrew/bin/ffmpeg"
FFPROBE = "/opt/homebrew/bin/ffprobe"
VOICE = "am_michael"
SPEED = 1.0
SAMPLE_RATE = 48000
PAUSE_SECONDS = 1.0
EXPECTED_STORYBOARD_SHA = "4ff525782afeeee7d8462c18f45ba16cf6fdabe1fe739dea2a5d84246165c33e"


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def duration(path: Path) -> float:
    return float(subprocess.check_output([
        FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)
    ], text=True).strip())


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def loudnorm(raw: Path, output: Path) -> dict[str, float]:
    scan = subprocess.run([
        FFMPEG, "-hide_banner", "-i", str(raw),
        "-af", "loudnorm=I=-16:TP=-2.3:LRA=7:print_format=json", "-f", "null", "-",
    ], text=True, capture_output=True, check=False)
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
    run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw), "-af", filt,
         "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "pcm_s24le", str(output)])
    verify = subprocess.run([
        FFMPEG, "-hide_banner", "-i", str(output),
        "-af", "loudnorm=I=-16:TP=-2.3:LRA=7:print_format=json", "-f", "null", "-",
    ], text=True, capture_output=True, check=False)
    values = json.loads(re.findall(r'\{\s*"input_i".*?\}', verify.stderr, re.S)[-1])
    return {
        "integrated_lufs": float(values["input_i"]),
        "true_peak_dbtp": float(values["input_tp"]),
        "lra_lu": float(values["input_lra"]),
    }


def main() -> None:
    for path in (SPEC_PATH, STORYBOARD_PATH, SIGNOFF_PATH, MODEL, VOICES, ESPEAK_LIB, ESPEAK_DATA / "phontab"):
        if not path.is_file():
            raise FileNotFoundError(path)
    if sha256(STORYBOARD_PATH) != EXPECTED_STORYBOARD_SHA:
        raise RuntimeError("signed storyboard hash drift")
    spec = json.loads(SPEC_PATH.read_text())
    storyboard = json.loads(STORYBOARD_PATH.read_text())
    if spec.get("marker") != "NEBULAMIND_V5_G3_MOTION_GRAPHICS_SPEC_V1":
        raise RuntimeError("unexpected G3 spec marker")
    if "HWAO_V5_G3_MOTION_SPEC_SIGNED_COMPLETE" not in SIGNOFF_PATH.read_text():
        raise RuntimeError("G3 semantic sign-off missing")
    selected = [int(value) for value in spec["canary_selection"]["included_storyboard_rows_in_cut_order"]]
    rows_by_number = {int(row["n"]): row for row in storyboard["rows"]}
    rows = [rows_by_number[number] for number in selected]
    if len(rows) != int(spec["plan_totals"]["sentences"]):
        raise RuntimeError("sentence count drift")
    if sum(int(row["words"]) for row in rows) != int(spec["plan_totals"]["words"]):
        raise RuntimeError("word count drift")
    exact_text = "\n".join(row["sentence"] for row in rows) + "\n"
    OUT.mkdir(parents=True, exist_ok=True)
    AUDIO.mkdir(parents=True, exist_ok=True)
    TRANSCRIPT.write_text(exact_text, encoding="utf-8")
    os.environ["ESPEAK_DATA_PATH"] = str(ESPEAK_DATA)
    engine = Kokoro(str(MODEL), str(VOICES), espeak_config=EspeakConfig(lib_path=str(ESPEAK_LIB), data_path=str(ESPEAK_DATA)))

    sentence_receipts: list[dict[str, Any]] = []
    processed: list[Path] = []
    cursor = 0.0
    for index, row in enumerate(rows):
        number = int(row["n"])
        text = str(row["sentence"])
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        raw = AUDIO / f"row_{number:02d}_{text_hash[:12]}_24k.wav"
        clean = AUDIO / f"row_{number:02d}_{text_hash[:12]}_48k.wav"
        if not raw.is_file():
            samples, rate = engine.create(text, voice=VOICE, speed=SPEED, lang="en-us")
            sf.write(raw, samples, rate, subtype="PCM_24")
        if not clean.is_file():
            run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw),
                 "-af", "highpass=f=65", "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "pcm_s24le", str(clean)])
        seconds = duration(clean)
        start = cursor
        end = start + seconds
        sentence_receipts.append({
            "cut_index": index + 1,
            "storyboard_row": number,
            "text": text,
            "text_sha256": text_hash,
            "words": int(row["words"]),
            "action": row["action"],
            "asset": row["asset"],
            "view_state": row["view_state"],
            "audio": str(clean),
            "audio_sha256": sha256(clean),
            "speech_duration_seconds": round(seconds, 6),
            "actual_start_seconds": round(start, 6),
            "actual_speech_end_seconds": round(end, 6),
        })
        processed.append(clean)
        cursor = end + (PAUSE_SECONDS if index < len(rows) - 1 else 0.0)
        print(f"row {number} ({index + 1}/{len(rows)}) {seconds:.3f}s")

    silence = AUDIO / "silence_1s_48k.wav"
    if not silence.is_file():
        sf.write(silence, np.zeros(int(SAMPLE_RATE * PAUSE_SECONDS), dtype=np.float32), SAMPLE_RATE, subtype="PCM_24")
    concat = OUT / "audio_concat.txt"
    concat_lines: list[str] = []
    for index, path in enumerate(processed):
        concat_lines.append(f"file '{path.as_posix()}'")
        if index < len(processed) - 1:
            concat_lines.append(f"file '{silence.as_posix()}'")
    concat.write_text("\n".join(concat_lines) + "\n")
    raw_master = OUT / "V5_G3_NARRATION_UNMASTERED.wav"
    run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(concat),
         "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "pcm_s24le", str(raw_master)])
    loudness = loudnorm(raw_master, MASTER)
    total = duration(MASTER)
    words = sum(int(row["words"]) for row in rows)
    wpm = words / total * 60.0
    if total > float(spec["plan_totals"]["contract"]["max_seconds"]):
        raise RuntimeError(f"audio exceeds max duration: {total}")
    low, high = [float(value) for value in spec["plan_totals"]["contract"]["wpm"]]
    if not low <= wpm <= high:
        raise RuntimeError(f"delivered WPM outside contract: {wpm}")
    if not -18.0 <= loudness["integrated_lufs"] <= -15.0 or loudness["true_peak_dbtp"] > -2.0:
        raise RuntimeError(f"audio loudness failed: {loudness}")
    if abs(total - cursor) > 0.08:
        raise RuntimeError(f"audio duration drift: master={total} planned_from_parts={cursor}")

    receipt = {
        "marker": "NEBULAMIND_V5_G3_AUDIO_PASS",
        "completed_at_utc": now(),
        "host": "Duhoui-MacStudio.local",
        "voice": "Kokoro-82M ONNX am_michael",
        "model_speed": SPEED,
        "inter_sentence_pause_seconds": PAUSE_SECONDS,
        "spec": str(SPEC_PATH),
        "spec_sha256": sha256(SPEC_PATH),
        "storyboard": str(STORYBOARD_PATH),
        "storyboard_sha256": sha256(STORYBOARD_PATH),
        "semantic_signoff": str(SIGNOFF_PATH),
        "semantic_signoff_sha256": sha256(SIGNOFF_PATH),
        "selected_rows": selected,
        "word_count": words,
        "sentence_count": len(rows),
        "sentences": sentence_receipts,
        "transcript": str(TRANSCRIPT),
        "transcript_sha256": sha256(TRANSCRIPT),
        "master": str(MASTER),
        "master_sha256": sha256(MASTER),
        "duration_seconds": round(total, 6),
        "delivered_wpm": round(wpm, 3),
        "loudness": loudness,
        "format": {"codec": "pcm_s24le", "sample_rate": SAMPLE_RATE, "channels": 1},
        "video_created": False,
        "presenter_or_face_asset": False,
        "office_asset": False,
        "external_mutation": False,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", "master": str(MASTER), "duration": total, "wpm": round(wpm, 3), "loudness": loudness}, indent=2))


if __name__ == "__main__":
    main()
