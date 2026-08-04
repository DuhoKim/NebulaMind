#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import re
import subprocess
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps
from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "canary-g3"
SPEC_PATH = ROOT / "V5_G3_MOTION_GRAPHICS_SPEC.json"
STORYBOARD_PATH = ROOT / "V5_G2_Z9_STORYBOARD.json"
BUILD_PATH = OUT / "V5_G3_BUILD_RECEIPT.json"
AUDIO_PATH = OUT / "V5_G3_AUDIO_RECEIPT.json"
VIDEO = OUT / "NEBULAMIND_Z9_V5_G3_MOTION_CANARY.mp4"
QA_PATH = OUT / "V5_G3_QA.json"
FREEZES = OUT / "freeze-frames"
CONTACT = OUT / "V5_G3_CONTACT_SHEET.png"
ASR_PATH = OUT / "V5_G3_ASR_TRANSCRIPT.txt"
FFMPEG = "/opt/homebrew/bin/ffmpeg"
FFPROBE = "/opt/homebrew/bin/ffprobe"
TESSERACT = "/opt/homebrew/bin/tesseract"
NUMBER_UNITS = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}
NUMBER_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
NUMBER_SCALES = {"hundred": 100, "thousand": 1000, "million": 1000000, "billion": 1000000000}
NUMBER_WORDS = set(NUMBER_UNITS) | set(NUMBER_TENS) | set(NUMBER_SCALES) | {"point"}
ALIASES = {"decks": "dex", "un-lensed": "unlensed", "un lensed": "unlensed", "electron temperature": "electron-temperature", "fifteen-hundred": "fifteen hundred"}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_number(value: str) -> str:
    try:
        number = Decimal(value.replace(",", ""))
    except InvalidOperation:
        return value
    if number == number.to_integral():
        return str(int(number))
    return format(number.normalize(), "f")


def parse_number_words(values: list[str]) -> str:
    if "point" in values:
        split = values.index("point")
        whole = parse_number_words(values[:split]) if split else "0"
        digits = "".join(str(NUMBER_UNITS[value]) for value in values[split + 1:] if value in NUMBER_UNITS)
        return canonical_number(f"{whole}.{digits or '0'}")
    total, current = 0, 0
    for value in values:
        if value in NUMBER_UNITS:
            current += NUMBER_UNITS[value]
        elif value in NUMBER_TENS:
            current += NUMBER_TENS[value]
        elif value == "hundred":
            current = max(1, current) * 100
        elif value in NUMBER_SCALES:
            total += max(1, current) * NUMBER_SCALES[value]
            current = 0
    return str(total + current)


def semantic_tokens(text: str) -> list[str]:
    value = text.lower().replace("’", "'")
    for source, target in ALIASES.items():
        value = value.replace(source, target)
    values = re.findall(r"[a-z]+|[-+]?\d[\d,]*(?:\.\d+)?", value)
    output: list[str] = []
    index = 0
    while index < len(values):
        token = values[index]
        if re.fullmatch(r"[-+]?\d[\d,]*(?:\.\d+)?", token):
            output.append(canonical_number(token))
            index += 1
        elif token in NUMBER_WORDS:
            end = index + 1
            while end < len(values) and values[end] in NUMBER_WORDS:
                end += 1
            output.append(parse_number_words(values[index:end]))
            index = end
        else:
            output.append(token)
            index += 1
    return output


def raw_tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower().replace("’", "'"))


def edit_distance(left: list[str], right: list[str]) -> int:
    previous = list(range(len(right) + 1))
    for index, a in enumerate(left, 1):
        current = [index]
        for j, b in enumerate(right, 1):
            current.append(min(current[-1] + 1, previous[j] + 1, previous[j - 1] + (a != b)))
        previous = current
    return previous[-1]


def ocr(path: Path) -> str:
    return subprocess.check_output([TESSERACT, str(path), "stdout", "--psm", "6"], text=True, stderr=subprocess.DEVNULL).strip()


def ocr_conceptual_label(path: Path, row_number: int) -> tuple[str, Path]:
    crop_dir = OUT / "ocr-crops"
    crop_dir.mkdir(parents=True, exist_ok=True)
    crop_path = crop_dir / f"row_{row_number:02d}_conceptual_label_threshold.png"
    image = Image.open(path).convert("RGB").crop((1680, 105, 2500, 205)).resize((2460, 300))
    gray = ImageOps.autocontrast(ImageOps.grayscale(image))
    thresholded = np.where(np.asarray(gray) > 105, 255, 0).astype(np.uint8)
    Image.fromarray(thresholded, mode="L").save(crop_path)
    text = subprocess.check_output([TESSERACT, str(crop_path), "stdout", "--psm", "7"], text=True, stderr=subprocess.DEVNULL).strip()
    return text, crop_path


def norm_ocr(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def extract_frame(time_seconds: float, output: Path) -> None:
    subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{time_seconds:.6f}", "-i", str(VIDEO), "-frames:v", "1", str(output)], check=True)


def probe(path: Path) -> dict[str, Any]:
    return json.loads(subprocess.check_output([
        FFPROBE, "-v", "error", "-show_entries", "format=duration,size:stream=codec_name,codec_type,width,height,r_frame_rate,pix_fmt,sample_rate,channels", "-of", "json", str(path)
    ], text=True))


def make_contact(midpoints: list[Path], rows: list[int]) -> None:
    thumb_w, thumb_h = 500, 281
    columns = 5
    rows_count = math.ceil(len(midpoints) / columns)
    canvas = Image.new("RGB", (columns * thumb_w, rows_count * (thumb_h + 38)), "#07111f")
    draw = ImageDraw.Draw(canvas)
    label_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 24)
    for index, path in enumerate(midpoints):
        image = Image.open(path).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = (index % columns) * thumb_w
        y = (index // columns) * (thumb_h + 38)
        canvas.paste(image, (x, y))
        draw.rectangle((x, y + thumb_h, x + thumb_w, y + thumb_h + 38), fill="#0c192a")
        draw.text((x + 12, y + thumb_h + 19), f"row {rows[index]}", font=label_font, fill="#46d8d2", anchor="lm")
    canvas.save(CONTACT, optimize=True)


def main() -> None:
    for path in (SPEC_PATH, STORYBOARD_PATH, BUILD_PATH, AUDIO_PATH, VIDEO):
        if not path.is_file():
            raise FileNotFoundError(path)
    spec = json.loads(SPEC_PATH.read_text())
    storyboard = json.loads(STORYBOARD_PATH.read_text())
    build = json.loads(BUILD_PATH.read_text())
    audio = json.loads(AUDIO_PATH.read_text())
    if build.get("marker") != "NEBULAMIND_V5_G3_BUILD_PASS" or audio.get("marker") != "NEBULAMIND_V5_G3_AUDIO_PASS":
        raise RuntimeError("upstream G3 receipt not PASS")
    if sha256(VIDEO) != build["video_sha256"] or sha256(SPEC_PATH) != build["spec_sha256"]:
        raise RuntimeError("video/spec hash lineage drift")
    subprocess.run([FFMPEG, "-v", "error", "-xerror", "-i", str(VIDEO), "-f", "null", "-"], check=True)
    media = probe(VIDEO)
    video_stream = next(stream for stream in media["streams"] if stream["codec_type"] == "video")
    audio_stream = next(stream for stream in media["streams"] if stream["codec_type"] == "audio")
    if video_stream["codec_name"] != "h264" or video_stream["width"] != 2560 or video_stream["height"] != 1440 or video_stream["r_frame_rate"] != "30/1":
        raise RuntimeError(f"video format failed: {video_stream}")
    if audio_stream["codec_name"] != "aac" or audio_stream["sample_rate"] != "48000" or audio_stream["channels"] != 1:
        raise RuntimeError(f"audio format failed: {audio_stream}")
    video_duration = float(media["format"]["duration"])
    if video_duration > float(spec["plan_totals"]["contract"]["max_seconds"]):
        raise RuntimeError("duration exceeds G3 contract")
    if float(build["max_action_onset_error_seconds"]) > 0.3:
        raise RuntimeError("action onset sync failed")

    selected = [int(value) for value in build["selected_rows"]]
    rows_by_number = {int(row["n"]): row for row in storyboard["rows"]}
    expected = " ".join(rows_by_number[number]["sentence"] for number in selected)
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    segments, info = model.transcribe(str(VIDEO), language="en", beam_size=5, vad_filter=True, condition_on_previous_text=True)
    transcript = " ".join(segment.text.strip() for segment in segments).strip()
    ASR_PATH.write_text(transcript + "\n", encoding="utf-8")
    reference_raw, observed_raw = raw_tokens(expected), raw_tokens(transcript)
    reference_semantic, observed_semantic = semantic_tokens(expected), semantic_tokens(transcript)
    raw_wer = 100.0 * edit_distance(reference_raw, observed_raw) / len(reference_raw)
    semantic_wer = 100.0 * edit_distance(reference_semantic, observed_semantic) / len(reference_semantic)
    if semantic_wer > 8.0:
        raise RuntimeError(f"semantic WER exceeds 8%: {semantic_wer}")
    critical = ["figure", "stellar", "mass", "oxygen", "benchmark", "red", "circles", "fifth", "dex", "stack", "blue", "square", "galaxies", "machine", "generated", "descriptive", "validated", "peer", "review", "formal", "statistical", "detection"]
    observed_set = set(observed_semantic)
    missing = [term for term in critical if term not in observed_set]
    if missing:
        raise RuntimeError(f"critical ASR terms missing: {missing}")
    if info.language != "en" or info.language_probability < 0.95:
        raise RuntimeError("ASR language confidence failed")

    FREEZES.mkdir(parents=True, exist_ok=True)
    audio_rows = {int(row["storyboard_row"]): row for row in audio["sentences"]}
    frame_receipts: list[dict[str, Any]] = []
    midpoint_paths: list[Path] = []
    for row_info in build["video_rows"]:
        number = int(row_info["storyboard_row"])
        start = float(row_info["video_start_seconds"])
        speech_duration = float(audio_rows[number]["speech_duration_seconds"])
        onset_time = min(video_duration - 0.05, start + 0.04)
        midpoint_time = min(video_duration - 0.05, start + speech_duration / 2.0)
        onset_path = FREEZES / f"row_{number:02d}_onset.png"
        midpoint_path = FREEZES / f"row_{number:02d}_midpoint.png"
        extract_frame(onset_time, onset_path)
        extract_frame(midpoint_time, midpoint_path)
        midpoint_paths.append(midpoint_path)
        frame_receipts.extend([
            {"row": number, "kind": "onset", "time_seconds": round(onset_time, 6), "path": str(onset_path), "sha256": sha256(onset_path)},
            {"row": number, "kind": "midpoint", "time_seconds": round(midpoint_time, 6), "path": str(midpoint_path), "sha256": sha256(midpoint_path)},
        ])
    if len(frame_receipts) != 34:
        raise RuntimeError("freeze-frame count failed")
    make_contact(midpoint_paths, selected)

    adjacent_diffs: list[dict[str, Any]] = []
    for index in range(len(midpoint_paths) - 1):
        left = np.asarray(Image.open(midpoint_paths[index]).convert("RGB"), dtype=np.int16)
        right = np.asarray(Image.open(midpoint_paths[index + 1]).convert("RGB"), dtype=np.int16)
        mean_abs = float(np.abs(left - right).mean())
        if mean_abs <= 0.4:
            raise RuntimeError(f"adjacent midpoint frames too similar rows {selected[index]}->{selected[index + 1]}: {mean_abs}")
        adjacent_diffs.append({"from_row": selected[index], "to_row": selected[index + 1], "mean_abs_rgb_difference": round(mean_abs, 4)})

    ocr_checks: list[dict[str, Any]] = []
    for number in [20, 21, 24, 25, 26, 27, 28, 29]:
        slide_entry = next(item for item in build["slides"] if int(item["storyboard_row"]) == number)
        crop_path = None
        if number in [20, 21, 24, 25, 26, 27]:
            text, crop_path = ocr_conceptual_label(Path(slide_entry["path"]), number)
        else:
            text = ocr(Path(slide_entry["path"]))
        normalized = norm_ocr(text)
        if number in [20, 21, 24, 25, 26, 27]:
            for term in ["conceptual", "illustration", "not", "data"]:
                if term not in normalized.split():
                    raise RuntimeError(f"conceptual label OCR missing {term} on row {number}: {text}")
        if number == 28:
            for term in ["machine", "generated", "descriptive", "validated", "automated", "review", "journal", "human", "peer"]:
                if term not in normalized.split():
                    raise RuntimeError(f"boundary OCR missing {term} on row 28: {text}")
        if number == 29:
            for term in ["formal", "statistical", "detection"]:
                if term not in normalized.split():
                    raise RuntimeError(f"boundary OCR missing {term} on row 29: {text}")
        ocr_checks.append({
            "row": number,
            "status": "PASS",
            "ocr": text,
            "targeted_crop": str(crop_path) if crop_path else None,
            "targeted_crop_sha256": sha256(crop_path) if crop_path else None,
        })

    manifest = build["asset_manifest"]
    if manifest.get("presenter") or manifest.get("face") or manifest.get("office") or manifest.get("opencv"):
        raise RuntimeError(f"banned asset detected: {manifest}")
    if build["figure1_sha256"] != spec["source_locks"]["fig1_sha256"]:
        raise RuntimeError("Figure 1 receipt hash drift")
    if len(build["view_rois_normalized"]) != 6:
        raise RuntimeError("not all six view ROIs recorded")

    result = {
        "marker": "NEBULAMIND_V5_G3_MACHINE_QA_PASS_PENDING_VISUAL_REVIEW",
        "completed_at_utc": now(),
        "host_build": build["host"],
        "qa_host": "local independent verifier",
        "video": str(VIDEO),
        "video_sha256": sha256(VIDEO),
        "video_duration_seconds": video_duration,
        "media": media,
        "delivered_wpm": audio["delivered_wpm"],
        "loudness_master": audio["loudness"],
        "full_decode": "PASS",
        "hash_lineage": "PASS",
        "action_sync_max_error_seconds": build["max_action_onset_error_seconds"],
        "asr": {
            "language": info.language,
            "language_probability": info.language_probability,
            "raw_wer_percent_diagnostic": round(raw_wer, 3),
            "semantic_wer_percent": round(semantic_wer, 3),
            "critical_terms": "PASS",
            "transcript": transcript,
            "transcript_path": str(ASR_PATH),
            "transcript_sha256": sha256(ASR_PATH),
        },
        "freeze_frames": frame_receipts,
        "freeze_frame_count": len(frame_receipts),
        "adjacent_midpoint_differences": adjacent_diffs,
        "contact_sheet": str(CONTACT),
        "contact_sheet_sha256": sha256(CONTACT),
        "ocr_checks": ocr_checks,
        "conceptual_label_ocr": "PASS",
        "boundary_text_ocr": "PASS",
        "six_figure_view_states_recorded": "PASS",
        "source_plot_overlay_policy": build["plot_overlay_policy"],
        "banned_asset_manifest": {"presenter": False, "face": False, "office": False, "opencv": False},
        "visual_contact_sheet_review": "PENDING",
        "human_watch_gate": "PENDING_DUHO",
        "external_mutations": {"youtube": False, "visibility": False, "website": False, "database": False, "git": False, "runtime": False, "cockpit": False},
    }
    QA_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS_PENDING_VISUAL", "video": str(VIDEO), "duration": video_duration, "wpm": audio["delivered_wpm"], "semantic_wer": result["asr"]["semantic_wer_percent"], "freeze_frames": len(frame_receipts), "contact_sheet": str(CONTACT)}, indent=2))


if __name__ == "__main__":
    main()
