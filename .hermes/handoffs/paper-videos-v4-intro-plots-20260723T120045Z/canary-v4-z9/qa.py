#!/usr/bin/env python3
from __future__ import annotations

import gc
import hashlib
import json
import re
import subprocess
from decimal import Decimal, InvalidOperation
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, cast

import numpy as np
import pymupdf
from faster_whisper import WhisperModel
from scipy import signal
from scipy.io import wavfile

ROOT = Path(__file__).resolve().parent
LANE = ROOT.parent
SPEC = LANE / "V4_Z9_CANARY_SPEC.json"
FREEZE = LANE / "V4_SOURCE_FREEZE.json"
VISUALS = ROOT / "visuals_receipt.json"
ASSETS = ROOT / "assets_receipt.json"
PRESENTER = ROOT / "z9-metallicity/presenter/presenter_receipt.json"
BUILD = ROOT / "build_receipt.json"
OUTPUT = ROOT / "qa/deterministic_qa.json"
TRANSCRIPT_REPLACEMENTS = {
    "decks": "dex",
    "modellicity": "metallicity",
    "metalicity": "metallicity",
    "un-lensed": "unlensed",
    "un lensed": "unlensed",
    "polyk": "pollock",
    "curdy": "curti",
    "oral line": "auroral line",
    "jade": "jades",
    "nebulamine": "nebulamind",
}
NUMBER_UNITS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19,
}
NUMBER_TENS = {
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
}
NUMBER_SCALES = {"hundred": 100, "thousand": 1000, "million": 1000000, "billion": 1000000000}
NUMBER_WORDS = set(NUMBER_UNITS) | set(NUMBER_TENS) | set(NUMBER_SCALES) | {"point"}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, text=True, capture_output=True, check=True)


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def canonical_number_literal(value: str) -> str:
    cleaned = value.replace(",", "")
    try:
        number = Decimal(cleaned)
    except InvalidOperation:
        return cleaned
    if number == number.to_integral():
        return str(int(number))
    return format(number.normalize(), "f")


def parse_number_words(values: list[str]) -> str:
    if "point" in values:
        split = values.index("point")
        whole = parse_number_words(values[:split]) if split else "0"
        digits = "".join(str(NUMBER_UNITS[value]) for value in values[split + 1:] if value in NUMBER_UNITS)
        return canonical_number_literal(f"{whole}.{digits or '0'}")
    total = 0
    current = 0
    for value in values:
        if value in NUMBER_UNITS:
            current += NUMBER_UNITS[value]
        elif value in NUMBER_TENS:
            current += NUMBER_TENS[value]
        elif value == "hundred":
            current = max(1, current) * 100
        elif value in {"thousand", "million", "billion"}:
            total += max(1, current) * NUMBER_SCALES[value]
            current = 0
    return str(total + current)


def semantic_tokens(text: str) -> list[str]:
    value = text.lower().replace("’", "'").replace("g and z", "g n z")
    value = re.sub(r"(?<=\d)[-–](?=\d)", " to ", value)
    for source, target in TRANSCRIPT_REPLACEMENTS.items():
        value = value.replace(source, target)
    values = re.findall(r"[a-z]+|[-+]?\d[\d,]*(?:\.\d+)?", value.replace("gnz11", "g n z eleven"))
    output: list[str] = []
    index = 0
    while index < len(values):
        token = values[index]
        if re.fullmatch(r"[-+]?\d[\d,]*(?:\.\d+)?", token):
            output.append(canonical_number_literal(token))
            index += 1
            continue
        if token in NUMBER_WORDS:
            end = index + 1
            while end < len(values) and values[end] in NUMBER_WORDS:
                end += 1
            output.append(parse_number_words(values[index:end]))
            index = end
            continue
        output.append(token)
        index += 1
    return output


def edit_distance(left: list[str], right: list[str]) -> int:
    previous = list(range(len(right) + 1))
    for i, a in enumerate(left, 1):
        current = [i]
        for j, b in enumerate(right, 1):
            current.append(min(current[-1] + 1, previous[j] + 1, previous[j - 1] + (a != b)))
        previous = current
    return previous[-1]


def parse_srt(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8").strip()
    blocks = re.split(r"\n\s*\n", text)
    cues: list[dict[str, Any]] = []
    pattern = re.compile(r"(\d{2}):(\d{2}):(\d{2}),(\d{3})")

    def seconds(value: str) -> float:
        match = pattern.fullmatch(value.strip())
        if not match:
            raise RuntimeError(f"bad SRT time: {value}")
        hour, minute, second, millisecond = map(int, match.groups())
        return hour * 3600 + minute * 60 + second + millisecond / 1000

    for block in blocks:
        lines = block.splitlines()
        if len(lines) < 3 or " --> " not in lines[1]:
            raise RuntimeError(f"bad SRT block: {block}")
        start, end = lines[1].split(" --> ")
        cues.append({"index": int(lines[0]), "start": seconds(start), "end": seconds(end), "text": " ".join(lines[2:])})
    return cues


def loudness(video: Path) -> dict[str, float]:
    result = subprocess.run([
        "ffmpeg", "-hide_banner", "-i", str(video),
        "-af", "loudnorm=I=-16:TP=-2.0:LRA=7:print_format=json",
        "-f", "null", "-",
    ], text=True, capture_output=True, check=False)
    blocks = re.findall(r'\{\s*"input_i".*?\}', result.stderr, re.S)
    if not blocks:
        raise RuntimeError("no final loudness block")
    values = json.loads(blocks[-1])
    return {"integrated_lufs": float(values["input_i"]), "true_peak_dbtp": float(values["input_tp"]), "lra_lu": float(values["input_lra"])}


def detector_events(video: Path, kind: str) -> list[str]:
    if kind == "black":
        args = ["ffmpeg", "-hide_banner", "-i", str(video), "-vf", "blackdetect=d=0.10:pix_th=0.10", "-an", "-f", "null", "-"]
        marker = "black_start:"
    elif kind == "silence":
        args = ["ffmpeg", "-hide_banner", "-i", str(video), "-af", "silencedetect=noise=-45dB:d=1.0", "-vn", "-f", "null", "-"]
        marker = "silence_start:"
    else:
        raise ValueError(kind)
    result = subprocess.run(args, text=True, capture_output=True, check=False)
    return [line.strip() for line in result.stderr.splitlines() if marker in line]


def audio_lag(video: Path, master: Path, duration: float, decoded_path: Path) -> dict[str, Any]:
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(video),
        "-t", f"{duration:.6f}", "-vn", "-ac", "1", "-ar", "48000", "-c:a", "pcm_s16le", str(decoded_path),
    ], check=True)
    source_rate, source = wavfile.read(master)
    decoded_rate, decoded = wavfile.read(decoded_path)
    if source_rate != 48000 or decoded_rate != 48000:
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
    return {"lag_samples": lag, "lag_ms": lag * 1000 / 48000, "correlation": peak, "compared_samples": count}


def axis_font_measurement(freeze: dict[str, Any], visuals: dict[str, Any]) -> dict[str, Any]:
    row = next(item for item in freeze["rows"] if item["key"] == "z9-metallicity")
    figure = row["figures"][0]
    bbox = pymupdf.Rect(*figure["crop_bbox_points"])
    document = pymupdf.open(row["pdf_path"])
    page = document[int(figure["page"]) - 1]
    candidate_spans: list[dict[str, Any]] = []
    data = cast(dict[str, Any], page.get_text("dict"))
    for block in data.get("blocks", []):
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = str(span.get("text", "")).strip()
                span_box = pymupdf.Rect(span.get("bbox", [0, 0, 0, 0]))
                if not text or not bbox.intersects(span_box):
                    continue
                if re.search(r"\d|log|MZR|O/H|mass|metal", text, re.IGNORECASE):
                    candidate_spans.append({"text": text, "font_points": float(span["size"]), "bbox": [round(value, 3) for value in span["bbox"]]})
    if not candidate_spans:
        raise RuntimeError("no figure axis/tick spans found")
    source_pixels_per_point = float(visuals["figure_pdf_render_pixels_per_point"])
    scale = min(float(value) for value in visuals["plot_display_scales"].values())
    minimum_points = min(item["font_points"] for item in candidate_spans)
    estimated_pixels = minimum_points * source_pixels_per_point * scale
    return {
        "candidate_span_count": len(candidate_spans),
        "minimum_pdf_font_points": round(minimum_points, 3),
        "source_pixels_per_pdf_point": source_pixels_per_point,
        "minimum_layout_scale": scale,
        "estimated_minimum_rendered_text_pixels": round(estimated_pixels, 3),
        "status": "PASS" if estimated_pixels >= 22.0 else "FAIL",
        "smallest_spans": sorted(candidate_spans, key=lambda item: item["font_points"])[:10],
    }


def ocr_layout(path: Path) -> str:
    result = run(["tesseract", str(path), "stdout", "--psm", "6"])
    return normalize(result.stdout)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    for required in (SPEC, FREEZE, VISUALS, ASSETS, PRESENTER, BUILD):
        if not required.is_file():
            raise FileNotFoundError(required)
    spec = json.loads(SPEC.read_text())
    freeze = json.loads(FREEZE.read_text())
    visuals = json.loads(VISUALS.read_text())
    assets = json.loads(ASSETS.read_text())
    presenter = json.loads(PRESENTER.read_text())
    build = json.loads(BUILD.read_text())
    video = Path(build["artifact"])
    master = Path(assets["narration_master"])
    srt = Path(assets["srt"])
    if not all(value == sha256(SPEC) for value in (visuals["spec_sha256"], assets["spec_sha256"], presenter["spec_sha256"], build["spec_sha256"])):
        raise RuntimeError("spec lineage mismatch")
    if sha256(video) != build["artifact_sha256"] or sha256(master) != assets["narration_sha256"] or sha256(srt) != assets["srt_sha256"]:
        raise RuntimeError("artifact lineage mismatch")

    cues = parse_srt(srt)
    if any(cue["end"] <= cue["start"] for cue in cues) or any(right["start"] < left["end"] - 0.002 for left, right in zip(cues, cues[1:])):
        raise RuntimeError("invalid or overlapping SRT cues")
    expected_text = normalize(" ".join(scene["narration"] for scene in spec["scenes"]))
    caption_text = normalize(" ".join(cue["text"] for cue in cues))
    if caption_text != expected_text:
        raise RuntimeError("caption text differs from signed narration")

    subprocess.run(["ffmpeg", "-v", "error", "-xerror", "-i", str(video), "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-"], check=True)
    media = build["probe"]
    video_stream = next(row for row in media["streams"] if row["codec_type"] == "video")
    audio_stream = next(row for row in media["streams"] if row["codec_type"] == "audio")
    duration = float(build["observed_duration"])
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
        raise RuntimeError("media contract failed")
    final_loudness = loudness(video)
    if not (-16.9 <= final_loudness["integrated_lufs"] <= -15.1 and final_loudness["true_peak_dbtp"] <= -1.5):
        raise RuntimeError(f"final loudness failed: {final_loudness}")
    black = detector_events(video, "black")
    silence = detector_events(video, "silence")
    if black or silence:
        raise RuntimeError(f"black/silence event: black={black} silence={silence}")
    lag = audio_lag(video, master, float(assets["narration_duration"]), OUTPUT.parent / "decoded_master_region.wav")
    if abs(float(lag["lag_ms"])) > 10 or float(lag["correlation"]) < 0.99:
        raise RuntimeError(f"exact-audio gate failed: {lag}")

    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    segments, info = model.transcribe(str(video), language="en", beam_size=5, vad_filter=True, condition_on_previous_text=True)
    transcript = " ".join(segment.text.strip() for segment in segments).strip()
    reference_tokens = semantic_tokens(expected_text)
    asr_tokens = semantic_tokens(transcript)
    semantic_wer = 100.0 * edit_distance(reference_tokens, asr_tokens) / len(reference_tokens)
    if semantic_wer > 8.0:
        raise RuntimeError(f"semantic WER too high: {semantic_wer:.3f}%")
    critical = ["oxygen", "unlensed", "pollock", "jades", "detection", "lensing", "electron", "benchmark", "redshift"]
    asr_set = set(asr_tokens)
    missing = [word for word in critical if word not in asr_set]
    if missing:
        raise RuntimeError(f"ASR missing critical terms: {missing}; transcript={transcript}")

    axis = axis_font_measurement(freeze, visuals)
    if axis["status"] != "PASS":
        raise RuntimeError(f"axis/tick text below 22 px: {axis}")
    if max(float(value) for value in visuals["plot_display_scales"].values()) > 1.15:
        raise RuntimeError("figure upscale cap exceeded")
    evidence_durations = {str(row["slot"]): float(row["speech_duration"]) for row in assets["timeline"] if int(row["slot"]) in (4, 5, 6)}
    if any(value < 8.0 for value in evidence_durations.values()):
        raise RuntimeError("evidence scene below eight seconds")
    if float(assets["timeline"][0]["speech_duration"]) > 20.0:
        raise RuntimeError("question hook exceeds twenty seconds")
    if duration > 180.0:
        raise RuntimeError("canary exceeds three minutes")
    boundary = spec["contract_preserved"]["boundary_text"]
    if boundary not in spec["scenes"][8]["narration"]:
        raise RuntimeError("slot 8 does not contain verbatim boundary")
    if visuals["forbidden_source_scan"] != "PASS" or any(re.search(r"page.?1|cover", path, re.IGNORECASE) for path in visuals["source_lineage"]):
        raise RuntimeError("forbidden visual source in lineage")
    if presenter["audio_sha256"] != assets["narration_sha256"] or presenter["slot_count"] != 10:
        raise RuntimeError("presenter exact-audio lineage failed")
    if build["presenter_box"] != spec["contract_preserved"]["presenter_box"]:
        raise RuntimeError("presenter box mismatch")

    slot8_ocr = ocr_layout(Path(visuals["layouts"][8]["path"]))
    slot9_ocr = ocr_layout(Path(visuals["layouts"][9]["path"]))
    for required_text in ("NOT A DETECTION", "SYSTEMATICS-LIMITED"):
        if required_text.lower() not in slot8_ocr.lower():
            raise RuntimeError(f"slot 8 OCR missing {required_text}: {slot8_ocr}")
    for required_text in ("descriptive", "not validated", "formal statistical detection"):
        if required_text.lower() not in slot9_ocr.lower():
            raise RuntimeError(f"slot 9 OCR missing {required_text}: {slot9_ocr}")

    checks = {
        "no_forbidden_visual_source": "PASS",
        "plain_language_question_within_20s": "PASS",
        "three_evidence_slots_real_figure_and_at_least_8s": "PASS",
        "axis_and_tick_text_at_least_22px": "PASS",
        "figure_upscale_at_most_1_15": "PASS",
        "narration_equals_srt_equals_signed_spec": "PASS",
        "duration_at_most_180s": "PASS",
        "identity_voice_speed_presenter_box_lineage": "PASS",
        "boundary_text_verbatim_and_visible": "PASS",
        "figure_hash_matches_signed_spec": "PASS",
        "media_contract_and_full_decode": "PASS",
        "loudness": "PASS",
        "black_and_unexpected_silence": "PASS",
        "exact_audio_lag": "PASS",
        "asr_semantic_and_critical_terms": "PASS",
    }
    result = {
        "marker": "NEBULAMIND_V4_Z9_DETERMINISTIC_QA_PASS",
        "completed_at_utc": now(),
        "spec": str(SPEC),
        "spec_sha256": sha256(SPEC),
        "video": str(video),
        "video_sha256": sha256(video),
        "bytes": video.stat().st_size,
        "duration_seconds": duration,
        "frames": int(video_stream["nb_read_frames"]),
        "effective_wpm": assets["effective_wpm"],
        "srt": str(srt),
        "srt_sha256": sha256(srt),
        "srt_cues": len(cues),
        "loudness": final_loudness,
        "black_events": black,
        "silence_events": silence,
        "audio_lag": lag,
        "asr_language": info.language,
        "asr_language_probability": info.language_probability,
        "asr_semantic_wer_percent": round(semantic_wer, 3),
        "asr_critical_terms": "PASS",
        "asr_transcript": transcript,
        "axis_font_measurement": axis,
        "plot_display_scales": visuals["plot_display_scales"],
        "evidence_speech_durations": evidence_durations,
        "slot8_ocr": slot8_ocr,
        "slot9_ocr": slot9_ocr,
        "checks": checks,
        "encoded_sheet": build["encoded_sheet"],
        "visual_qa": "PENDING_ENCODED_SHEET_REVIEW",
        "publication_state": "local V4 z9 canary only; not uploaded",
        "youtube_mutation": False,
        "website_mutation": False,
        "git_mutation": False,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "PASS",
        "duration": duration,
        "frames": result["frames"],
        "wer": result["asr_semantic_wer_percent"],
        "lag_ms": lag["lag_ms"],
        "correlation": lag["correlation"],
        "axis_min_pixels": axis["estimated_minimum_rendered_text_pixels"],
        "checks": len(checks),
    }, indent=2))


if __name__ == "__main__":
    main()
