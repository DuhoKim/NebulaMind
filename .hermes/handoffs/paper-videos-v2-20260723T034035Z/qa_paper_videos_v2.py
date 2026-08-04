#!/usr/bin/env python3
"""Deterministic encoded-media and semantic QA for the five-paper V2 batch."""
from __future__ import annotations

from pathlib import Path
from decimal import Decimal, InvalidOperation
import hashlib
import json
import re
import subprocess

from PIL import Image, ImageDraw, ImageFont
from faster_whisper import WhisperModel  # pyright: ignore[reportMissingImports]

BASE = Path(__file__).resolve().parent
SPEC = json.loads((BASE / "paper_video_specs_v2.json").read_text())
BATCH = json.loads((BASE / "batch_build_receipt.json").read_text())
QA = BASE / "qa"
FRAMES = QA / "encoded_frames"
QA.mkdir(exist_ok=True)
FRAMES.mkdir(exist_ok=True)
FONT = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", 24)
ALIASES = {
    "decks": "dex",
    "metalicity": "metallicity",
    "unlunzed": "unlensed",
    "unlens": "unlensed",
    "pollute": "pollock",
    "curdy": "curti",
    "illustrous": "illustris",
    "illustrist": "illustris",
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
CRITICAL = {
    "z9-metallicity": ["metallicity", "lensing", "5", "unlensed", "uncertain", "validated", "detection"],
    "scaling-relations": ["star", "formation", "metallicity", "calibration", "validated"],
    "massive-abundance": ["mass", "systematic", "quiescent", "validated"],
    "mzr-framework": ["calibration", "aperture", "diffuse", "validated"],
    "tng-validation": ["calibration", "star", "formation", "metallicity", "validated"],
}


def capture(command: list[str], *, stderr: bool = False) -> str:
    result = subprocess.run(command, text=True, capture_output=True, check=True)
    return result.stderr if stderr else result.stdout


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


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
        digits = "".join(str(NUMBER_UNITS[value]) for value in values[split+1:] if value in NUMBER_UNITS)
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


def tokens(text: str, *, semantic: bool = False) -> list[str]:
    values = re.findall(r"[a-z]+|[-+]?\d[\d,]*(?:\.\d+)?", text.lower().replace("’", "'").replace("gnz11", "g n z eleven"))
    if not semantic:
        return values
    output: list[str] = []
    i = 0
    while i < len(values):
        value = values[i]
        if re.fullmatch(r"[-+]?\d[\d,]*(?:\.\d+)?", value):
            output.append(canonical_number_literal(value))
            i += 1
            continue
        if value in NUMBER_WORDS:
            j = i + 1
            while j < len(values) and values[j] in NUMBER_WORDS:
                j += 1
            output.append(parse_number_words(values[i:j]))
            i = j
            continue
        output.append(str(ALIASES.get(value, value)))
        i += 1
    return output


def edit_distance(a: list[str], b: list[str]) -> int:
    row = list(range(len(b)+1))
    for i, left in enumerate(a, 1):
        new = [i]
        for j, right in enumerate(b, 1):
            new.append(min(new[-1]+1, row[j]+1, row[j-1]+(left != right)))
        row = new
    return row[-1]


def parse_srt(path: Path) -> list[dict]:
    blocks = re.split(r"\n\s*\n", path.read_text().strip())
    rows: list[dict] = []
    for block in blocks:
        lines = block.splitlines()
        if len(lines) < 3:
            raise RuntimeError(f"malformed SRT block: {block}")
        match = re.fullmatch(r"(\d\d):(\d\d):(\d\d),(\d\d\d) --> (\d\d):(\d\d):(\d\d),(\d\d\d)", lines[1])
        if not match:
            raise RuntimeError(f"bad SRT timing: {lines[1]}")
        values = [int(x) for x in match.groups()]
        start = values[0]*3600 + values[1]*60 + values[2] + values[3]/1000
        end = values[4]*3600 + values[5]*60 + values[6] + values[7]/1000
        rows.append({"index": int(lines[0]), "start": start, "end": end, "text": " ".join(lines[2:])})
    return rows


def loudness(path: Path) -> dict:
    error = capture([
        "ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
        "-af", "loudnorm=I=-16:LRA=7:TP=-2.0:print_format=json",
        "-f", "null", "-",
    ], stderr=True)
    match = re.search(r'\{\s*"input_i".*?\}', error, re.S)
    if not match:
        raise RuntimeError(f"no loudnorm JSON for {path}")
    return json.loads(match.group(0))


def scan(path: Path, kind: str) -> list[str]:
    if kind == "black":
        flag, filt, pattern = "-vf", "blackdetect=d=0.5:pix_th=0.02", r"black_start:[^\n]+"
    else:
        flag, filt, pattern = "-af", "silencedetect=n=-50dB:d=0.7", r"silence_(?:start|end):[^\n]+"
    error = capture(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), flag, filt, "-f", "null", "-"], stderr=True)
    return [str(value) for value in re.findall(pattern, error)]


def extract_frame(video: Path, out: Path, seconds: float) -> None:
    subprocess.run([
        "ffmpeg", "-y", "-v", "error", "-ss", f"{seconds:.3f}",
        "-i", str(video), "-frames:v", "1", str(out),
    ], check=True)


def make_sheet(paths: list[Path], out: Path, labels: list[str]) -> None:
    thumb_w, thumb_h = 512, 288
    sheet = Image.new("RGB", (thumb_w*5, thumb_h*2), (7, 16, 31))
    draw = ImageDraw.Draw(sheet)
    for i, path in enumerate(paths):
        image = Image.open(path).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x, y = (i % 5)*thumb_w, (i // 5)*thumb_h
        sheet.paste(image, (x, y))
        draw.rectangle((x, y, x+thumb_w-1, y+thumb_h-1), outline=(41, 70, 110), width=3)
        draw.rounded_rectangle((x+12, y+12, x+190, y+52), radius=8, fill=(7, 16, 31))
        draw.text((x+24, y+18), labels[i], font=FONT, fill=(234, 242, 255))
    sheet.save(out)


def transcribe_final(path: Path, model: WhisperModel) -> str:
    segments, info = model.transcribe(str(path), language="en", beam_size=5, vad_filter=True, condition_on_previous_text=True)
    if info.language != "en" or info.language_probability < 0.95:
        raise RuntimeError(f"unexpected ASR language for {path}: {info.language}")
    return " ".join(segment.text.strip() for segment in segments).strip()


def main() -> None:
    if BATCH.get("marker") != "NEBULAMIND_FIVE_PAPER_VIDEO_BATCH_BUILD_COMPLETE_V2":
        raise RuntimeError("V2 batch receipt missing")
    papers = {paper["key"]: paper for paper in SPEC["papers"]}
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    rows: list[dict] = []
    sheets: list[Path] = []
    for artifact in BATCH["artifacts"]:
        key = artifact["key"]
        paper = papers[key]
        video = Path(artifact["path"])
        srt = Path(artifact["srt"])
        receipt = json.loads((video.parent/"build_receipt.json").read_text())
        if sha256(video) != artifact["sha256"] or sha256(video) != receipt["artifact_sha256"]:
            raise RuntimeError(f"{key}: video hash mismatch")
        if sha256(srt) != artifact["srt_sha256"] or sha256(srt) != receipt["srt_sha256"]:
            raise RuntimeError(f"{key}: SRT hash mismatch")
        cues = parse_srt(srt)
        if any(cue["end"] <= cue["start"] for cue in cues):
            raise RuntimeError(f"{key}: invalid caption duration")
        if any(right["start"] < left["end"] - 0.002 for left, right in zip(cues, cues[1:])):
            raise RuntimeError(f"{key}: caption overlap")
        expected_text = normalize(" ".join(scene["narration"] for scene in paper["scenes"]))
        observed_text = normalize(" ".join(cue["text"] for cue in cues))
        if observed_text != expected_text:
            raise RuntimeError(f"{key}: SRT narration mismatch")
        if cues[0]["start"] < 2.35 or cues[-1]["end"] > receipt["observed_duration"] - 2.0:
            raise RuntimeError(f"{key}: captions outside narrated region")
        if any(abs(row["drift_seconds"]) > 0.5 for row in receipt["timeline"]):
            raise RuntimeError(f"{key}: visual/audio boundary drift")
        if not 105.0 <= float(receipt["effective_wpm"]) <= 125.0:
            raise RuntimeError(f"{key}: pace outside comprehension target")

        probe = json.loads(capture([
            "ffprobe", "-v", "error", "-count_frames",
            "-show_entries", "format=duration,size,bit_rate:stream=index,codec_type,codec_name,profile,width,height,pix_fmt,avg_frame_rate,nb_read_frames,sample_rate,channels,bit_rate",
            "-of", "json", str(video),
        ]))
        video_stream = next(stream for stream in probe["streams"] if stream["codec_type"] == "video")
        audio_stream = next(stream for stream in probe["streams"] if stream["codec_type"] == "audio")
        duration = float(probe["format"]["duration"])
        expected_frames = round(duration*30)
        media_ok = (
            video_stream["codec_name"] == "h264"
            and video_stream.get("profile") == "High"
            and video_stream["width"] == 2560
            and video_stream["height"] == 1440
            and video_stream["pix_fmt"] == "yuv420p"
            and video_stream["avg_frame_rate"] == "30/1"
            and abs(int(video_stream["nb_read_frames"]) - expected_frames) <= 2
            and audio_stream["codec_name"] == "aac"
            and audio_stream["sample_rate"] == "48000"
            and audio_stream["channels"] == 2
            and abs(duration - float(receipt["observed_duration"])) <= 0.10
        )
        if not media_ok:
            raise RuntimeError(f"{key}: media contract failed: {probe}")
        subprocess.run([
            "ffmpeg", "-v", "error", "-i", str(video),
            "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-",
        ], check=True)
        loud = loudness(video)
        if not (-16.8 <= float(loud["input_i"]) <= -15.2 and float(loud["input_tp"]) <= -1.5):
            raise RuntimeError(f"{key}: loudness outside target: {loud}")
        black_events = scan(video, "black")
        if black_events:
            raise RuntimeError(f"{key}: unexpected black frames: {black_events}")
        silence_events = scan(video, "silence")

        asr = transcribe_final(video, model)
        reference_tokens = tokens(expected_text, semantic=True)
        asr_tokens = tokens(asr, semantic=True)
        distance = edit_distance(reference_tokens, asr_tokens)
        semantic_wer = 100.0 * distance / len(reference_tokens)
        if semantic_wer > 8.0:
            raise RuntimeError(f"{key}: final AAC ASR WER {semantic_wer:.2f}%")
        asr_set = set(asr_tokens)
        missing_critical = [word for word in CRITICAL[key] if word not in asr_set]
        if missing_critical:
            raise RuntimeError(f"{key}: final AAC ASR missing critical words {missing_critical}; transcript={asr}")

        frame_times = [1.2]
        frame_times.extend(row["visual_start"] + row["duration"]/2 for row in receipt["timeline"])
        frame_times.append(duration - 1.2)
        frame_paths: list[Path] = []
        for i, seconds in enumerate(frame_times):
            path = FRAMES / f"{key}_{i:02d}.png"
            extract_frame(video, path, seconds)
            frame_paths.append(path)
        sheet = QA / f"{key}_ENCODED_TEMPORAL_SHEET.png"
        make_sheet(frame_paths, sheet, [f"{seconds:.1f}s" for seconds in frame_times])
        sheets.append(sheet)
        extract_frame(video, QA/f"{key}_SCENE1_FULL.png", frame_times[1])
        extract_frame(video, QA/f"{key}_STATUS_FULL.png", frame_times[-2])

        rows.append({
            "key": key,
            "status": "PASS",
            "video": str(video),
            "sha256": artifact["sha256"],
            "bytes": video.stat().st_size,
            "duration": duration,
            "frames": int(video_stream["nb_read_frames"]),
            "resolution": [video_stream["width"], video_stream["height"]],
            "video_bit_rate": int(video_stream.get("bit_rate", 0)),
            "audio_bit_rate": int(audio_stream.get("bit_rate", 0)),
            "effective_wpm": receipt["effective_wpm"],
            "srt_cues": len(cues),
            "first_cue": cues[0]["start"],
            "last_cue": cues[-1]["end"],
            "loudness": loud,
            "black_events": black_events,
            "silence_events": silence_events,
            "full_decode": "PASS",
            "semantic_srt": "PASS",
            "timeline_drift": "PASS",
            "media_contract": "PASS",
            "asr_semantic_wer_percent": round(semantic_wer, 3),
            "asr_critical_words": "PASS",
            "asr_transcript": asr,
            "encoded_sheet": str(sheet),
        })

    aggregate = Image.new("RGB", (2560, 576*len(sheets)), (7, 16, 31))
    for i, path in enumerate(sheets):
        aggregate.paste(Image.open(path).convert("RGB").resize((2560, 576), Image.Resampling.LANCZOS), (0, i*576))
    aggregate_path = QA / "FIVE_PAPER_V2_ENCODED_SHEETS.png"
    aggregate.save(aggregate_path)
    result = {
        "marker": "NEBULAMIND_FIVE_PAPER_DETERMINISTIC_QA_PASS_V2",
        "completed_at_utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "paper_count": len(rows),
        "rows": rows,
        "aggregate_sheet": str(aggregate_path),
        "visual_qa": "pending model inspection",
        "publication_state": "local QA only",
    }
    (QA/"deterministic_qa.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
