#!/usr/bin/env python3
from __future__ import annotations

import gc
import importlib.util
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from faster_whisper import WhisperModel
from scipy import signal
from scipy.io import wavfile

BASE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v3-male-lipsync-20260723T050645Z")
BATCH = BASE / "batch"
ASSETS = BATCH / "assets_batch_receipt.json"
V2 = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v2-20260723T034035Z")
V2_QA_PATH = V2 / "qa_paper_videos_v2.py"
V2_SPEC = V2 / "paper_video_specs_v2.json"
QA_ROOT = BATCH / "qa"
INTRO_SECONDS = 2.5
TRANSCRIPT_REPLACEMENTS = {
    "modellicity": "metallicity",
    "metalicity": "metallicity",
    "un-lensed": "unlensed",
    "un lensed": "unlensed",
    "polyk": "pollock",
    "curdy": "curti",
    "oral line": "auroral line",
    "illustrous": "illustris",
    "illustrist": "illustris",
}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def capture(args: list[str], *, stderr: bool = False) -> str:
    result = subprocess.run(args, text=True, capture_output=True, check=True)
    return result.stderr if stderr else result.stdout


def sha256(path: Path) -> str:
    import hashlib
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def normalize_transcript(text: str) -> str:
    value = text.lower()
    for source, target in TRANSCRIPT_REPLACEMENTS.items():
        value = value.replace(source, target)
    return value


def audio_lag(video: Path, master: Path, duration: float, output: Path) -> dict[str, Any]:
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-ss", f"{INTRO_SECONDS:.3f}", "-i", str(video), "-t", f"{duration:.6f}",
        "-vn", "-ac", "1", "-ar", "48000", "-c:a", "pcm_s16le", str(output),
    ], check=True)
    sample_rate, source = wavfile.read(master)
    decoded_rate, decoded = wavfile.read(output)
    if sample_rate != 48000 or decoded_rate != 48000:
        raise RuntimeError("audio sample-rate drift")
    count = min(len(source), len(decoded))
    left = source[:count].astype(np.float64)
    right = decoded[:count].astype(np.float64)
    left -= left.mean()
    right -= right.mean()
    left /= np.linalg.norm(left) + 1e-12
    right /= np.linalg.norm(right) + 1e-12
    correlation = signal.correlate(right, left, mode="full", method="fft")
    lags = signal.correlation_lags(len(right), len(left), mode="full")
    mask = np.abs(lags) <= 24000
    peak_index = int(np.argmax(correlation[mask]))
    lag = int(lags[mask][peak_index])
    peak = float(correlation[mask][peak_index])
    del source, decoded, left, right, correlation, lags
    gc.collect()
    return {
        "lag_samples": lag,
        "lag_ms": lag * 1000 / sample_rate,
        "correlation": peak,
        "source_samples": count,
        "decoded_samples": count,
    }


def main() -> None:
    if not ASSETS.is_file():
        raise FileNotFoundError(ASSETS)
    QA_ROOT.mkdir(parents=True, exist_ok=True)
    module_spec = importlib.util.spec_from_file_location("v2qa", V2_QA_PATH)
    if module_spec is None or module_spec.loader is None:
        raise RuntimeError("could not load V2 QA helpers")
    v2qa = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(v2qa)
    assets = json.loads(ASSETS.read_text())
    papers = {paper["key"]: paper for paper in json.loads(V2_SPEC.read_text())["papers"]}
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    rows: list[dict[str, Any]] = []
    for index, asset in enumerate(assets["papers"], 1):
        key = asset["key"]
        print(f"QA {index}/5 {key}", flush=True)
        root = BATCH / key
        receipt_path = root / "build_receipt.json"
        if not receipt_path.is_file():
            raise FileNotFoundError(receipt_path)
        receipt = json.loads(receipt_path.read_text())
        video = Path(receipt["artifact"])
        srt = Path(receipt["srt"])
        master = Path(receipt["narration"])
        if sha256(video) != receipt["artifact_sha256"]:
            raise RuntimeError(f"{key}: video hash mismatch")
        if sha256(srt) != receipt["srt_sha256"] or sha256(srt) != asset["srt_sha256"]:
            raise RuntimeError(f"{key}: SRT hash mismatch")
        if sha256(master) != receipt["narration_sha256"] or sha256(master) != asset["narration_sha256"]:
            raise RuntimeError(f"{key}: narration hash mismatch")
        cues = v2qa.parse_srt(srt)
        if any(cue["end"] <= cue["start"] for cue in cues):
            raise RuntimeError(f"{key}: invalid SRT cue duration")
        if any(right["start"] < left["end"] - 0.002 for left, right in zip(cues, cues[1:])):
            raise RuntimeError(f"{key}: SRT overlap")
        expected_text = normalize(" ".join(scene["narration"] for scene in papers[key]["scenes"]))
        caption_text = normalize(" ".join(cue["text"] for cue in cues))
        if caption_text != expected_text:
            raise RuntimeError(f"{key}: caption narration drift")
        duration = float(receipt["observed_duration"])
        if cues[0]["start"] < 2.45 or cues[-1]["end"] > duration - 3.0:
            raise RuntimeError(f"{key}: caption region outside narration")
        media = receipt["probe"]
        video_stream = next(row for row in media["streams"] if row["codec_type"] == "video")
        audio_stream = next(row for row in media["streams"] if row["codec_type"] == "audio")
        expected_frames = round(duration * 30)
        media_ok = (
            video_stream["codec_name"] == "h264"
            and video_stream["profile"] == "High"
            and video_stream["width"] == 2560
            and video_stream["height"] == 1440
            and video_stream["pix_fmt"] == "yuv420p"
            and video_stream["avg_frame_rate"] == "30/1"
            and int(video_stream["nb_read_frames"]) == expected_frames
            and audio_stream["codec_name"] == "aac"
            and audio_stream["sample_rate"] == "48000"
            and audio_stream["channels"] == 2
        )
        if not media_ok:
            raise RuntimeError(f"{key}: media contract failed")
        subprocess.run([
            "ffmpeg", "-v", "error", "-xerror", "-i", str(video),
            "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-",
        ], check=True)
        loudness = v2qa.loudness(video)
        if not (-16.9 <= float(loudness["input_i"]) <= -15.1 and float(loudness["input_tp"]) <= -1.5):
            raise RuntimeError(f"{key}: loudness outside target {loudness}")
        black_events = v2qa.scan(video, "black")
        if black_events:
            raise RuntimeError(f"{key}: black frame event {black_events}")
        silence_events = v2qa.scan(video, "silence")
        lag = audio_lag(
            video, master, float(asset["narration_duration"]),
            QA_ROOT / f"{key}_decoded_narrated_region.wav",
        )
        if abs(float(lag["lag_ms"])) > 10 or float(lag["correlation"]) < 0.99:
            raise RuntimeError(f"{key}: exact-audio gate failed {lag}")
        segments, info = model.transcribe(
            str(video), language="en", beam_size=5, vad_filter=True,
            condition_on_previous_text=True,
        )
        transcript = " ".join(segment.text.strip() for segment in segments).strip()
        reference_tokens = v2qa.tokens(expected_text, semantic=True)
        asr_tokens = v2qa.tokens(normalize_transcript(transcript), semantic=True)
        semantic_wer = 100.0 * v2qa.edit_distance(reference_tokens, asr_tokens) / len(reference_tokens)
        if semantic_wer > 8.0:
            raise RuntimeError(f"{key}: semantic WER {semantic_wer:.2f}%")
        asr_set = set(asr_tokens)
        missing_critical = [word for word in v2qa.CRITICAL[key] if word not in asr_set]
        if missing_critical:
            raise RuntimeError(f"{key}: ASR missing critical {missing_critical}; transcript={transcript}")
        rows.append({
            "key": key,
            "status": "PASS",
            "video": str(video),
            "video_sha256": sha256(video),
            "bytes": video.stat().st_size,
            "duration": duration,
            "frames": int(video_stream["nb_read_frames"]),
            "effective_wpm": asset["effective_wpm"],
            "srt": str(srt),
            "srt_sha256": sha256(srt),
            "srt_cues": len(cues),
            "loudness": loudness,
            "black_events": black_events,
            "silence_events": silence_events,
            "audio_lag": lag,
            "asr_language": info.language,
            "asr_language_probability": info.language_probability,
            "asr_semantic_wer_percent": round(semantic_wer, 3),
            "asr_critical_words": "PASS",
            "asr_transcript": transcript,
            "encoded_sheet": receipt["encoded_sheet"],
            "full_decode": "PASS",
            "media_contract": "PASS",
            "caption_exactness": "PASS",
        })
    result = {
        "marker": "NEBULAMIND_FIVE_PAPER_V3_DETERMINISTIC_QA_PASS",
        "completed_at_utc": now(),
        "paper_count": len(rows),
        "rows": rows,
        "visual_qa": "pending batch sheet inspection",
        "publication_state": "local V3 only; not uploaded",
        "youtube_mutation": False,
        "website_mutation": False,
        "git_mutation": False,
    }
    output = QA_ROOT / "deterministic_qa.json"
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", "rows": [{"key": row["key"], "wer": row["asr_semantic_wer_percent"], "lag_ms": row["audio_lag"]["lag_ms"]} for row in rows]}, indent=2))


if __name__ == "__main__":
    main()
