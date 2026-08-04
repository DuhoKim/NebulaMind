#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
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
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

BASE = Path(__file__).resolve().parent
V2 = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v2-20260723T034035Z")
SPEC_PATH = V2 / "paper_video_specs_v2.json"
FREEZE_PATH = V2 / "source_freeze.json"
OUT = BASE / "batch"
IDENTITY = BASE / "identity/candidate_c_young_black_male.png"
KOKORO_MODEL = Path("/Users/duhokim/HermesOps/tools/kokoro-onnx/kokoro-v1.0.onnx")
KOKORO_VOICES = Path("/Users/duhokim/HermesOps/tools/kokoro-onnx/voices-v1.0.bin")
ESPEAK_LIB = Path("/opt/homebrew/opt/espeak-ng/lib/libespeak-ng.dylib")
ESPEAK_DATA = Path("/opt/homebrew/opt/espeak-ng/share/espeak-ng-data")
FONT_PATH = Path("/System/Library/Fonts/SFNSMono.ttf")
ITALIC_FONT_PATH = Path("/System/Library/Fonts/SFNSMonoItalic.ttf")
W, H = 2560, 1440
INTRO_SECONDS = 2.5
INTER_SCENE_GAP = 0.35
LAST_SCENE_BREATHING_ROOM = 0.7
OUTRO_SECONDS = 2.8
VOICE = "am_michael"
VOICE_SPEED = 1.0
CYAN = "#35D9F2"
BODY = "#EAF2FF"
MUTED = "#91A4C4"
PANEL = "#101E39"
OUTLINE = "#29466E"
BG = "#07101F"


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def capture(args: list[str]) -> str:
    return subprocess.check_output(args, text=True).strip()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def font(size: int, italic: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(ITALIC_FONT_PATH if italic else FONT_PATH), size=size)


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


def loudnorm(raw: Path, out: Path) -> dict[str, float]:
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
        raise RuntimeError(f"no loudnorm scan for {raw}")
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
        "-af", filt, "-ar", "48000", "-ac", "1", "-c:a", "pcm_s24le", str(out),
    ])
    verify = subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-i", str(out),
            "-af", "loudnorm=I=-16:TP=-2.0:LRA=7:print_format=json",
            "-f", "null", "-",
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    final = json.loads(re.findall(r'\{\s*"input_i".*?\}', verify.stderr, re.S)[-1])
    return {
        "integrated_lufs": float(final["input_i"]),
        "true_peak_dbtp": float(final["input_tp"]),
        "lra_lu": float(final["input_lra"]),
    }


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], *, outline: str = OUTLINE) -> None:
    draw.rounded_rectangle(box, radius=30, fill=PANEL, outline=outline, width=4)


def soft_identity(size: tuple[int, int]) -> Image.Image:
    source = Image.open(IDENTITY).convert("RGB")
    source = ImageOps.fit(source, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.38))
    source = ImageEnhance.Color(source).enhance(0.96).convert("RGBA")
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((24, 20, size[0] - 24, size[1] - 20), radius=88, fill=248)
    source.putalpha(mask.filter(ImageFilter.GaussianBlur(26)))
    return source


def make_presenter_mask() -> Path:
    path = OUT / "presenter_mask_530x850.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    mask = Image.new("L", (530, 850), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((12, 10, 518, 826), radius=58, fill=255)
    for y in range(760, 850):
        alpha = max(0, round(255 * (1 - (y - 760) / 90)))
        draw.rectangle((12, y, 518, y), fill=alpha)
    mask = mask.filter(ImageFilter.GaussianBlur(9))
    mask.save(path)
    return path


def make_intro(source: Path, out: Path, key: str) -> None:
    image = Image.open(source).convert("RGB").resize((W, H), Image.Resampling.LANCZOS).convert("RGBA")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((1430, 38, 2520, 1380), radius=34, fill="#07101F", outline=OUTLINE, width=4)
    image.alpha_composite(soft_identity((900, 1180)), (1520, 125))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((1510, 104, 2428, 235), radius=20, fill="#07101F", outline=CYAN, width=3)
    draw.text((1550, 132), "PRESENTER C · MICHAEL", font=font(34), fill=BODY)
    draw.text((1550, 184), "Male presenter V3 · local review", font=font(23), fill=CYAN)
    draw.text((120, 1370), f"{key} · silent title card", font=font(22), fill=MUTED)
    image.convert("RGB").save(out, quality=96)


def make_teaching(source: Path, out: Path, paper: dict[str, Any], scene_index: int) -> None:
    original = Image.open(source).convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
    background = ImageEnhance.Brightness(original.filter(ImageFilter.GaussianBlur(34))).enhance(0.42)
    image = background.convert("RGBA")
    dark = Image.new("RGBA", (W, H), (7, 16, 31, 186))
    image = Image.alpha_composite(image, dark)
    science = original.crop((70, 130, 2490, 1260)).resize((1800, 840), Image.Resampling.LANCZOS)
    image.paste(science, (55, 250))
    draw = ImageDraw.Draw(image)
    draw.text((55, 44), "NebulaMind", font=font(38), fill=BODY)
    draw.text((350, 50), "PAPER EXPLAINER · MALE PRESENTER V3", font=font(25), fill=CYAN)
    draw.text((2205, 50), f"{scene_index:02d} / 08", font=font(25), fill=MUTED)
    draw.line((55, 115, 2485, 115), fill=OUTLINE, width=2)
    panel(draw, (1895, 145, 2490, 1280), outline=CYAN)
    draw.text((1940, 188), "PRESENTER C · MICHAEL", font=font(27), fill=BODY)
    draw.text((1940, 238), "Local MLX · exact-audio lip-sync", font=font(19), fill=CYAN)
    draw.text((1940, 277), "Fictional presenter · no generated dialogue", font=font(16), fill=MUTED)
    draw.rounded_rectangle((1928, 328, 2462, 1210), radius=48, fill="#07101F", outline=OUTLINE, width=2)
    draw.line((55, 1300, 2485, 1300), fill=OUTLINE, width=2)
    draw.text((55, 1332), paper["track"], font=font(22), fill=MUTED)
    draw.text((1835, 1332), "Manual captions included · local review", font=font(20), fill=MUTED)
    image.convert("RGB").save(out, quality=96)


def make_outro(source: Path, out: Path, key: str) -> None:
    image = Image.open(source).convert("RGB").resize((W, H), Image.Resampling.LANCZOS).convert("RGBA")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((45, 42, 1055, 1380), radius=34, fill="#07101F", outline=OUTLINE, width=4)
    image.alpha_composite(soft_identity((870, 1180)), (115, 120))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((105, 1030, 1010, 1190), radius=24, fill="#07101F", outline=CYAN, width=3)
    draw.text((145, 1062), "PRESENTER C · MICHAEL", font=font(31), fill=BODY)
    draw.text((145, 1112), "Male presenter V3 · local review", font=font(21), fill=CYAN)
    draw.text((120, 1370), f"{key} · silent close", font=font(22), fill=MUTED)
    image.convert("RGB").save(out, quality=96)


def write_srt(paper: dict[str, Any], scene_rows: list[dict[str, Any]], path: Path) -> list[dict[str, Any]]:
    cues: list[dict[str, Any]] = []
    cue_index = 1
    for scene, row in zip(paper["scenes"], scene_rows):
        chunks = sentence_chunks(scene["narration"])
        counts = [len(tokens(chunk)) for chunk in chunks]
        total = sum(counts)
        cursor = 0
        for chunk, count in zip(chunks, counts):
            start = row["visual_start"] + row["speech_duration"] * cursor / total
            cursor += count
            end = row["visual_start"] + row["speech_duration"] * cursor / total
            start = max(start, cues[-1]["end"] + 0.03 if cues else INTRO_SECONDS)
            end = max(end - 0.02, start + 0.55)
            cues.append({"index": cue_index, "start": round(start, 3), "end": round(end, 3), "text": chunk})
            cue_index += 1
    blocks = []
    for cue in cues:
        wrapped = "\n".join(textwrap.wrap(cue["text"], width=58, break_long_words=False, break_on_hyphens=False))
        blocks.append(f"{cue['index']}\n{srt_time(cue['start'])} --> {srt_time(cue['end'])}\n{wrapped}\n")
    path.write_text("\n".join(blocks), encoding="utf-8")
    expected = " ".join(scene["narration"].strip() for scene in paper["scenes"])
    observed = " ".join(cue["text"] for cue in cues)
    if re.sub(r"\s+", " ", expected).strip() != re.sub(r"\s+", " ", observed).strip():
        raise RuntimeError(f"{paper['key']}: SRT text drift")
    return cues


def synthesize_paper(engine: Kokoro, paper: dict[str, Any]) -> dict[str, Any]:
    key = paper["key"]
    root = OUT / key
    audio_dir = root / "audio"
    layout_dir = root / "layouts"
    audio_dir.mkdir(parents=True, exist_ok=True)
    layout_dir.mkdir(parents=True, exist_ok=True)
    processed_paths: list[Path] = []
    scene_durations: list[float] = []
    scene_hashes: list[dict[str, str]] = []
    for index, scene in enumerate(paper["scenes"], 1):
        text = scene["narration"].strip()
        text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        raw = audio_dir / f"scene_{index:02d}_michael_{text_hash[:12]}_24k.wav"
        processed = audio_dir / f"scene_{index:02d}_michael_{text_hash[:12]}_48k.wav"
        if not raw.is_file():
            samples, sample_rate = engine.create(text, voice=VOICE, speed=VOICE_SPEED, lang="en-us")
            sf.write(raw, samples, sample_rate, subtype="PCM_24")
        if not processed.is_file():
            run([
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw),
                "-af", "highpass=f=65", "-ar", "48000", "-ac", "1", "-c:a", "pcm_s24le", str(processed),
            ])
        sample_rate, duration = 48000, float(capture([
            "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nk=1:nw=1", str(processed),
        ]))
        if sample_rate != 48000 or duration <= 3.0:
            raise RuntimeError(f"{key} scene {index}: invalid speech duration")
        processed_paths.append(processed)
        scene_durations.append(duration)
        scene_hashes.append({"raw_sha256": sha256(raw), "processed_sha256": sha256(processed), "text_sha256": text_hash})

    parts: list[np.ndarray] = []
    gap = np.zeros(round(48000 * INTER_SCENE_GAP), dtype=np.float32)
    for index, path in enumerate(processed_paths):
        samples, sample_rate = sf.read(path, dtype="float32")
        if sample_rate != 48000 or samples.ndim != 1:
            raise RuntimeError(f"{key}: unexpected scene audio format {path}")
        parts.append(samples)
        if index < len(processed_paths) - 1:
            parts.append(gap)
    combined = np.concatenate(parts)
    pre_master = audio_dir / f"{key}_MICHAEL_V3_PREMASTER.wav"
    master = audio_dir / f"{key}_MICHAEL_V3_MASTER.wav"
    sf.write(pre_master, combined, 48000, subtype="PCM_24")
    loudness = loudnorm(pre_master, master)
    master_duration = float(capture([
        "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nk=1:nw=1", str(master),
    ]))

    scene_rows: list[dict[str, Any]] = []
    cursor = 0.0
    for index, speech_duration in enumerate(scene_durations):
        gap_after = INTER_SCENE_GAP if index < len(scene_durations) - 1 else 0.0
        scene_rows.append({
            "scene": index + 1,
            "audio_start": round(cursor, 6),
            "visual_start": round(INTRO_SECONDS + cursor, 6),
            "speech_duration": round(speech_duration, 6),
            "gap_after": gap_after,
            "visual_duration": round(speech_duration + gap_after + (LAST_SCENE_BREATHING_ROOM if index == 7 else 0.0), 6),
            **scene_hashes[index],
        })
        cursor += speech_duration + gap_after
    if abs(cursor - master_duration) > 0.02:
        raise RuntimeError(f"{key}: concatenated timing drift {cursor} != {master_duration}")

    srt = root / f"NEBULAMIND_PAPER_{key.upper().replace('-', '_')}_V3.srt"
    cues = write_srt(paper, scene_rows, srt)
    source_scenes = V2 / "build" / key / "scenes"
    make_intro(source_scenes / "scene_00.png", layout_dir / "scene_00.png", key)
    for index in range(1, 9):
        make_teaching(source_scenes / f"scene_{index:02d}.png", layout_dir / f"scene_{index:02d}.png", paper, index)
    make_outro(source_scenes / "scene_09.png", layout_dir / "scene_09.png", key)

    word_count = sum(len(tokens(scene["narration"])) for scene in paper["scenes"])
    speech_seconds = sum(scene_durations)
    effective_wpm = word_count / speech_seconds * 60.0
    if not 120.0 <= effective_wpm <= 145.0:
        raise RuntimeError(f"{key}: Michael pace {effective_wpm:.2f} outside approved range")
    expected_video_duration = INTRO_SECONDS + master_duration + LAST_SCENE_BREATHING_ROOM + OUTRO_SECONDS
    receipt = {
        "marker": "NEBULAMIND_PAPER_V3_MICHAEL_ASSETS_COMPLETE",
        "completed_at_utc": now(),
        "key": key,
        "source_v2_spec": str(SPEC_PATH),
        "source_v2_spec_sha256": sha256(SPEC_PATH),
        "source_v2_video": str(V2 / "videos" / key / f"NEBULAMIND_PAPER_{key.upper().replace('-', '_')}_V2.mp4"),
        "voice_provider": "local Kokoro-82M v1.0 ONNX",
        "voice": VOICE,
        "model_speed": VOICE_SPEED,
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
        "timeline": scene_rows,
        "layouts": [str(layout_dir / f"scene_{index:02d}.png") for index in range(10)],
        "expected_video_duration": round(expected_video_duration, 6),
        "publication_state": "local V3 build only; not uploaded",
    }
    (root / "assets_receipt.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    return receipt


def main() -> None:
    for required in (
        SPEC_PATH, FREEZE_PATH, IDENTITY, KOKORO_MODEL, KOKORO_VOICES,
        ESPEAK_LIB, ESPEAK_DATA / "phontab", FONT_PATH, ITALIC_FONT_PATH,
    ):
        if not required.is_file():
            raise FileNotFoundError(required)
    freeze = json.loads(FREEZE_PATH.read_text())
    if freeze.get("paper_count") != 5 or not freeze.get("all_live_pdfs_match_v1_freeze"):
        raise RuntimeError("V2 source freeze is not valid")
    spec = json.loads(SPEC_PATH.read_text())
    if spec.get("marker") != "NEBULAMIND_FIVE_PAPER_VIDEO_SPECS_V2" or len(spec.get("papers", [])) != 5:
        raise RuntimeError("unexpected V2 spec")
    OUT.mkdir(parents=True, exist_ok=True)
    mask = make_presenter_mask()
    config = EspeakConfig(lib_path=str(ESPEAK_LIB), data_path=str(ESPEAK_DATA))
    engine = Kokoro(str(KOKORO_MODEL), str(KOKORO_VOICES), espeak_config=config)
    receipts = []
    for index, paper in enumerate(spec["papers"], 1):
        print(f"ASSETS {index}/5 {paper['key']}", flush=True)
        receipts.append(synthesize_paper(engine, paper))
    batch = {
        "marker": "NEBULAMIND_FIVE_PAPER_V3_MICHAEL_ASSETS_COMPLETE",
        "completed_at_utc": now(),
        "source_v2_spec": str(SPEC_PATH),
        "source_v2_spec_sha256": sha256(SPEC_PATH),
        "source_freeze_verified": True,
        "voice": VOICE,
        "voice_speed": VOICE_SPEED,
        "presenter_mask": str(mask),
        "presenter_mask_sha256": sha256(mask),
        "paper_count": len(receipts),
        "papers": receipts,
        "youtube_mutation": False,
        "website_mutation": False,
        "git_mutation": False,
    }
    (OUT / "assets_batch_receipt.json").write_text(json.dumps(batch, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", "papers": [{"key": row["key"], "wpm": row["effective_wpm"], "duration": row["expected_video_duration"]} for row in receipts]}, indent=2))


if __name__ == "__main__":
    main()
