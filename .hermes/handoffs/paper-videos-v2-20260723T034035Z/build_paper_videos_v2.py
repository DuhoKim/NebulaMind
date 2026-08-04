#!/usr/bin/env python3
"""Build five source-frozen, comprehension-first NebulaMind paper explainers."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import math
import os
import random
import re
import subprocess
import sys
import textwrap
from typing import Any

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from faster_whisper import WhisperModel  # pyright: ignore[reportMissingImports]

HERMES_AGENT = Path("/Users/duhokim/.hermes/hermes-agent")
sys.path.insert(0, str(HERMES_AGENT))
from tools.tts_tool import _generate_openai_tts  # noqa: E402  # pyright: ignore[reportMissingImports]

BASE = Path(__file__).resolve().parent
SPEC_PATH = BASE / "paper_video_specs_v2.json"
FREEZE_PATH = BASE / "source_freeze.json"
OUT_ROOT = BASE / "videos"
BUILD_ROOT = BASE / "build"
BATCH_RECEIPT = BASE / "batch_build_receipt.json"
BATCH_SHEET = BASE / "FIVE_PAPER_V2_BATCH_SHEET.png"
PORTRAIT = Path(
    "/Users/duhokim/HermesOps/scripts/clips/subnav_flow_lipsync_v7/"
    "canary/flow_master_shoulder_crop_768x1024.png"
)
FONT_PATH = Path("/System/Library/Fonts/SFNSMono.ttf")
ITALIC_FONT_PATH = Path("/System/Library/Fonts/SFNSMonoItalic.ttf")

W, H, FPS = 2560, 1440, 30
INTRO_SECONDS = 2.5
OUTRO_SECONDS = 2.8
LAST_SCENE_BREATHING_ROOM = 0.7
BG_TOP = "#07101F"
BG_BOTTOM = "#0B1630"
CYAN = "#35D9F2"
MAGENTA = "#D95CFF"
GREEN = "#4EE09A"
YELLOW = "#F2C14E"
RED = "#FF6B78"
BODY = "#EAF2FF"
MUTED = "#91A4C4"
PANEL = "#101E39"
OUTLINE = "#29466E"
TONE = {"cyan": CYAN, "magenta": MAGENTA, "green": GREEN, "yellow": YELLOW, "red": RED}
ASR_ALIASES = {
    "decks": "dex",
    "tng": "tng",
    "metallicity": "metallicity",
    "illustrist": "illustris",
    "illustrous": "illustris",
}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def capture(command: list[str]) -> str:
    return subprocess.check_output(command, text=True).strip()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def probe_duration(path: Path) -> float:
    return float(capture([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=nk=1:nw=1", str(path),
    ]))


def atomic_json(path: Path, value: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    os.replace(tmp, path)


def verify_source_freeze() -> None:
    freeze = json.loads(FREEZE_PATH.read_text())
    if freeze.get("paper_count") != 5 or not freeze.get("all_live_pdfs_match_v1_freeze"):
        raise RuntimeError("source freeze incomplete")
    failures: list[str] = []
    for row in freeze["sources"]:
        p = Path(row["path"])
        if not p.is_file():
            failures.append(f"missing: {p}")
        elif sha256(p) != row["sha256"]:
            failures.append(f"hash drift: {p}")
    if failures:
        raise RuntimeError("SOURCE FREEZE DRIFT\n" + "\n".join(failures))


def color(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return int(value[:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def rgba(value: str, alpha: int = 255) -> tuple[int, int, int, int]:
    return (*color(value), alpha)


def font(size: int, *, italic: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(ITALIC_FONT_PATH if italic else FONT_PATH), size=size)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        proposal = word if not current else f"{current} {word}"
        if draw.textlength(proposal, font=fnt) <= max_width:
            current = proposal
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    *,
    line_gap: int = 12,
    max_lines: int | None = None,
    fail_on_overflow: bool = False,
) -> int:
    lines = wrap_text(draw, text, fnt, max_width)
    if max_lines is not None and len(lines) > max_lines:
        if fail_on_overflow:
            raise RuntimeError(f"text exceeds {max_lines} lines: {text}")
        lines = lines[:max_lines]
    x, y = xy
    box = draw.textbbox((0, 0), "Ag", font=fnt)
    height = box[3] - box[1]
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += height + line_gap
    return round(y)


def gradient_background(seed: int, *, warning: bool = False) -> Image.Image:
    top, bottom = color(BG_TOP), color(BG_BOTTOM)
    image = Image.new("RGB", (W, H), top)
    draw = ImageDraw.Draw(image)
    for y in range(H):
        t = y / (H - 1)
        draw.line((0, y, W, y), fill=tuple(round(top[i] * (1 - t) + bottom[i] * t) for i in range(3)))
    rng = random.Random(23072026 + seed)
    for _ in range(150):
        x, y = rng.randrange(W), rng.randrange(H - 170)
        r = rng.choice((1, 1, 2, 2, 3, 4))
        draw.ellipse((x-r, y-r, x+r, y+r), fill=color(rng.choice((CYAN, MAGENTA, BODY, MUTED))))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-380, 100, 980, 1540), fill=rgba(MAGENTA, 22))
    gd.ellipse((1680, -400, 3100, 1100), fill=rgba(RED if warning else CYAN, 28))
    return Image.alpha_composite(image.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(190)))


def panel(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    *,
    outline: str = OUTLINE,
    fill: str = PANEL,
    width: int = 4,
    radius: int = 32,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=rgba(fill, 244), outline=outline, width=width)


def paste_portrait(image: Image.Image, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    size = (x1 - x0, y1 - y0)
    source = Image.open(PORTRAIT).convert("RGB")
    source = ImageOps.fit(source, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.45))
    source = ImageEnhance.Color(source).enhance(0.94).convert("RGBA")
    mask = Image.new("L", size, 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((42, 28, size[0]-42, size[1]-28), radius=96, fill=245)
    source.putalpha(mask.filter(ImageFilter.GaussianBlur(44)))
    image.alpha_composite(source, (x0, y0))


def paste_pdf_page(image: Image.Image, page_path: Path, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    source = Image.open(page_path).convert("RGBA")
    white = Image.new("RGBA", source.size, (255, 255, 255, 255))
    white.alpha_composite(source)
    page = white.convert("RGB")
    page.thumbnail((x1-x0-36, y1-y0-36), Image.Resampling.LANCZOS)
    px = x0 + (x1-x0-page.width)//2
    py = y0 + (y1-y0-page.height)//2
    shadow = Image.new("RGBA", (page.width+50, page.height+50), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((18, 18, page.width+32, page.height+32), radius=18, fill=(0, 0, 0, 160))
    image.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(16)), (px-25, py-25))
    image.paste(page, (px, py))


def render_open(paper: dict[str, Any], seed: int) -> Image.Image:
    image = gradient_background(seed)
    paste_portrait(image, (1505, 86, 2415, 1325))
    d = ImageDraw.Draw(image)
    d.text((120, 72), "NebulaMind", font=font(44), fill=BODY)
    d.text((120, 184), paper["track"], font=font(28), fill=CYAN)
    y = 280
    lines = wrap_text(d, paper["short_title"], font(72), 1260)
    if len(lines) > 5:
        raise RuntimeError(f"opening title overflow: {paper['key']}")
    for line in lines:
        d.text((120, y), line, font=font(72), fill=BODY)
        y += 94
    d.line((120, min(900, y+26), 1330, min(900, y+26)), fill=CYAN, width=7)
    panel(d, (120, 1040, 1350, 1190), fill="#0B1630", width=2)
    d.text((165, 1074), "A plain-language paper explainer", font=font(34), fill=BODY)
    d.text((165, 1128), "Silent title card · narration begins next", font=font(23), fill=MUTED)
    d.text((120, 1332), "NebulaMind Lab · autonomous run", font=font(24), fill=MUTED)
    return image


def draw_header(draw: ImageDraw.ImageDraw, paper: dict[str, Any], index: int, scene: dict[str, Any]) -> int:
    draw.text((110, 54), "NebulaMind", font=font(38), fill=BODY)
    draw.text((420, 60), "PAPER EXPLAINER · PLAIN-ENGLISH V2", font=font(25), fill=CYAN)
    draw.text((2200, 60), f"{index:02d} / 08", font=font(25), fill=MUTED)
    draw.line((110, 122, 2450, 122), fill=OUTLINE, width=2)
    draw.text((110, 166), scene["kicker"], font=font(26), fill=CYAN)
    lines = wrap_text(draw, scene["title"], font(56), 2250)
    if len(lines) > 2:
        raise RuntimeError(f"scene title overflow: {paper['key']} {index}")
    y = 225
    for line in lines:
        draw.text((110, y), line, font=font(56), fill=BODY)
        y += 72
    return max(380, y + 26)


def render_scene(paper: dict[str, Any], index: int, scene: dict[str, Any], seed: int) -> Image.Image:
    warning = index == 8
    image = gradient_background(seed, warning=warning)
    d = ImageDraw.Draw(image)
    body_y = draw_header(d, paper, index, scene)
    cards = scene["cards"]
    if not 2 <= len(cards) <= 3:
        raise RuntimeError(f"{paper['key']} scene {index}: expected 2–3 cards")
    if index == 1:
        page_path = Path(paper["first_page_path"])
        panel(d, (110, body_y, 830, 1190), outline=CYAN, fill="#111B2B")
        paste_pdf_page(image, page_path, (130, body_y+20, 810, 1170))
        d = ImageDraw.Draw(image)
        card_x0, card_x1 = 900, 2450
        card_h = 180
        for i, card in enumerate(cards):
            y0 = body_y + i * (card_h + 28)
            accent = TONE[card.get("tone", "cyan")]
            panel(d, (card_x0, y0, card_x1, y0+card_h), outline=accent)
            draw_wrapped(d, (card_x0+45, y0+32), str(card["value"]), font(48), BODY, 610, max_lines=2, fail_on_overflow=True)
            draw_wrapped(d, (card_x0+760, y0+46), str(card["label"]), font(28), accent, 690, max_lines=3, fail_on_overflow=True)
        call_y = body_y + len(cards) * (card_h + 28) + 8
        panel(d, (card_x0, call_y, card_x1, 1190), outline=OUTLINE, fill="#0D1A31", width=2)
        d.text((card_x0+45, call_y+32), "WHY THIS MATTERS", font=font(23), fill=CYAN)
        draw_wrapped(d, (card_x0+45, call_y+84), scene["callout"], font(36), BODY, 1450, line_gap=15, max_lines=4, fail_on_overflow=True)
    else:
        gap = 42
        total_w = 2340
        card_w = (total_w - gap*(len(cards)-1)) // len(cards)
        for i, card in enumerate(cards):
            x0 = 110 + i*(card_w+gap)
            accent = TONE[card.get("tone", "cyan")]
            panel(d, (x0, body_y+20, x0+card_w, body_y+360), outline=accent)
            draw_wrapped(d, (x0+40, body_y+72), str(card["value"]), font(56), BODY, card_w-80, line_gap=10, max_lines=3, fail_on_overflow=True)
            draw_wrapped(d, (x0+40, body_y+250), str(card["label"]), font(28), accent, card_w-80, line_gap=8, max_lines=3, fail_on_overflow=True)
        panel(d, (110, body_y+420, 2450, 1190), outline=RED if warning else OUTLINE, fill="#241822" if warning else "#0D1A31", width=3)
        d.text((165, body_y+480), "WHAT TO REMEMBER" if index == 8 else "INTERPRETATION", font=font(25), fill=YELLOW if warning else CYAN)
        draw_wrapped(d, (165, body_y+565), scene["callout"], font(48), BODY, 2230, line_gap=18, max_lines=5, fail_on_overflow=True)
    d.line((110, 1285, 2450, 1285), fill=OUTLINE, width=2)
    d.text((110, 1320), paper["track"], font=font(23), fill=MUTED)
    d.text((1850, 1320), "Manual captions available on YouTube", font=font(21), fill=MUTED)
    return image


def render_close(paper: dict[str, Any], seed: int) -> Image.Image:
    image = gradient_background(seed, warning=True)
    paste_portrait(image, (120, 90, 990, 1320))
    d = ImageDraw.Draw(image)
    d.text((1150, 185), "READ THE PAPER.", font=font(66), fill=CYAN)
    d.text((1150, 285), "KEEP THE CAVEAT.", font=font(66), fill=YELLOW)
    d.line((1150, 405, 2370, 405), fill=CYAN, width=7)
    y = 500
    for line in wrap_text(d, paper["short_title"], font(42), 1200)[:5]:
        d.text((1150, y), line, font=font(42), fill=BODY)
        y += 58
    panel(d, (1150, 900, 2370, 1120), outline=RED, fill="#241822")
    d.text((1200, 950), "DESCRIPTIVE · NOT VALIDATED", font=font(36), fill=YELLOW)
    d.text((1200, 1020), "Human and journal review remain separate", font=font(25), fill=MUTED)
    d.text((1150, 1290), "NebulaMind Lab · autonomous run", font=font(24), fill=MUTED)
    return image


def text_tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower().replace("’", "'").replace("–", "-"))


def normalize_asr_token(token: str) -> str:
    token = re.sub(r"[^a-z0-9]", "", token.lower())
    return ASR_ALIASES.get(token, token)


def align_tokens(reference: list[str], observed: list[str]) -> dict[int, int]:
    n, m = len(reference), len(observed)
    dp = [[0]*(m+1) for _ in range(n+1)]
    back: list[list[str]] = [[""]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = i
        back[i][0] = "D"
    for j in range(1, m+1):
        dp[0][j] = j
        back[0][j] = "I"
    for i in range(1, n+1):
        for j in range(1, m+1):
            sub = dp[i-1][j-1] + (reference[i-1] != observed[j-1])
            delete = dp[i-1][j] + 1
            insert = dp[i][j-1] + 1
            best = min(sub, delete, insert)
            dp[i][j] = best
            back[i][j] = "M" if best == sub else ("D" if best == delete else "I")
    mapping: dict[int, int] = {}
    i, j = n, m
    while i or j:
        step = back[i][j]
        if step == "M":
            mapping[i-1] = j-1
            i -= 1
            j -= 1
        elif step == "D":
            i -= 1
        else:
            j -= 1
    return mapping


def synthesize_whole_script(text: str, raw: Path, speed: float) -> None:
    if raw.is_file() and raw.stat().st_size > 1000:
        return
    cfg = {"provider": "openai", "speed": speed, "openai": {"model": "gpt-4o-mini-tts", "speed": speed}}
    _generate_openai_tts(text, str(raw), cfg, voice="shimmer", speed=speed)


def normalize_audio(raw: Path, out: Path) -> dict[str, Any]:
    scan = subprocess.run([
        "ffmpeg", "-hide_banner", "-i", str(raw),
        "-af", "loudnorm=I=-16:TP=-2.0:LRA=7:print_format=json",
        "-f", "null", "-",
    ], capture_output=True, text=True, check=False)
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
        "ffmpeg", "-y", "-v", "error", "-i", str(raw), "-af", filt,
        "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", str(out),
    ])
    verify = subprocess.run([
        "ffmpeg", "-hide_banner", "-i", str(out),
        "-af", "loudnorm=I=-16:TP=-2.0:LRA=7:print_format=json",
        "-f", "null", "-",
    ], capture_output=True, text=True, check=False)
    final = json.loads(re.findall(r'\{\s*"input_i".*?\}', verify.stderr, re.S)[-1])
    return {
        "integrated_lufs": float(final["input_i"]),
        "true_peak_dbtp": float(final["input_tp"]),
        "lra_lu": float(final["input_lra"]),
    }


def transcribe_words(audio: Path, model: WhisperModel) -> tuple[list[dict[str, Any]], str]:
    segments, info = model.transcribe(
        str(audio), language="en", beam_size=5, vad_filter=True,
        condition_on_previous_text=True, word_timestamps=True,
    )
    words: list[dict[str, Any]] = []
    transcript_parts: list[str] = []
    for segment in segments:
        transcript_parts.append(segment.text.strip())
        for word in segment.words or []:
            token = normalize_asr_token(word.word)
            if token:
                words.append({"token": token, "text": word.word.strip(), "start": round(word.start, 4), "end": round(word.end, 4)})
    if info.language != "en" or info.language_probability < 0.95:
        raise RuntimeError(f"unexpected ASR language: {info.language} {info.language_probability}")
    return words, " ".join(transcript_parts).strip()


def mapped_word_time(mapping: dict[int, int], words: list[dict[str, Any]], ref_index: int, *, end: bool = False) -> float | None:
    if ref_index in mapping:
        return float(words[mapping[ref_index]]["end" if end else "start"])
    for delta in range(1, 12):
        for candidate in (ref_index-delta, ref_index+delta):
            if candidate in mapping:
                return float(words[mapping[candidate]]["end" if end else "start"])
    return None


def sentence_chunks(text: str, max_words: int = 16) -> list[str]:
    chunks: list[str] = []
    for sentence in [x.strip() for x in re.split(r"(?<=[.!?])\s+", text.strip()) if x.strip()]:
        words = sentence.split()
        if len(words) <= max_words:
            chunks.append(sentence)
            continue
        while words:
            take = min(max_words, len(words))
            if len(words) > max_words:
                for j in range(min(max_words, len(words))-1, max(7, max_words-6), -1):
                    if words[j-1].endswith((",", ";", ":")):
                        take = j
                        break
            piece = " ".join(words[:take])
            words = words[take:]
            chunks.append(piece)
    return chunks


def srt_time(seconds: float) -> str:
    ms = round(seconds * 1000)
    hours, ms = divmod(ms, 3_600_000)
    minutes, ms = divmod(ms, 60_000)
    secs, ms = divmod(ms, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"


def derive_timeline_and_srt(
    paper: dict[str, Any],
    audio_duration: float,
    words: list[dict[str, Any]],
    srt_path: Path,
) -> tuple[list[float], list[dict[str, Any]], dict[str, Any]]:
    scene_texts = [scene["narration"].strip() for scene in paper["scenes"]]
    full_text = " ".join(scene_texts)
    reference = text_tokens(full_text)
    observed = [w["token"] for w in words]
    mapping = align_tokens(reference, observed)
    errors = len(reference) - sum(1 for i, j in mapping.items() if reference[i] == observed[j])
    wer = 100.0 * errors / max(1, len(reference))

    scene_starts_ref: list[int] = []
    cursor = 0
    for text in scene_texts:
        scene_starts_ref.append(cursor)
        cursor += len(text_tokens(text))
    scene_audio_starts = [0.0]
    for ref_index in scene_starts_ref[1:]:
        t = mapped_word_time(mapping, words, ref_index)
        if t is None:
            t = audio_duration * ref_index / len(reference)
        scene_audio_starts.append(round(t, 4))
    if any(b-a < 5.0 for a, b in zip(scene_audio_starts, scene_audio_starts[1:])):
        raise RuntimeError(f"{paper['key']}: implausible ASR scene boundaries {scene_audio_starts}")
    scene_audio_ends = scene_audio_starts[1:] + [audio_duration + LAST_SCENE_BREATHING_ROOM]
    scene_durations = [round(b-a, 6) for a, b in zip(scene_audio_starts, scene_audio_ends)]

    cues: list[dict[str, Any]] = []
    ref_cursor = 0
    previous_end = INTRO_SECONDS
    cue_index = 1
    for scene in paper["scenes"]:
        for chunk in sentence_chunks(scene["narration"]):
            count = len(text_tokens(chunk))
            start_ref = ref_cursor
            end_ref = ref_cursor + count - 1
            start = mapped_word_time(mapping, words, start_ref)
            end = mapped_word_time(mapping, words, end_ref, end=True)
            if start is None:
                start = audio_duration * start_ref / len(reference)
            if end is None:
                end = audio_duration * (end_ref+1) / len(reference)
            start += INTRO_SECONDS
            end += INTRO_SECONDS
            start = max(start, previous_end + 0.03)
            end = max(end, start + 0.6)
            wrapped = "\n".join(textwrap.wrap(chunk, width=58, break_long_words=False, break_on_hyphens=False))
            cues.append({"index": cue_index, "start": round(start, 3), "end": round(end, 3), "text": chunk, "wrapped": wrapped})
            previous_end = end
            cue_index += 1
            ref_cursor += count
    blocks = [f"{c['index']}\n{srt_time(c['start'])} --> {srt_time(c['end'])}\n{c['wrapped']}\n" for c in cues]
    srt_path.write_text("\n".join(blocks), encoding="utf-8")
    timeline = [{
        "scene": i+1,
        "visual_start": round(INTRO_SECONDS + scene_audio_starts[i], 4),
        "spoken_start": round(INTRO_SECONDS + scene_audio_starts[i], 4),
        "drift_seconds": 0.0,
        "duration": scene_durations[i],
    } for i in range(8)]
    return scene_durations, timeline, {
        "reference_words": len(reference),
        "observed_words": len(observed),
        "aligned_words": len(mapping),
        "approx_raw_wer_percent": round(wer, 3),
    }


def render_silent_video(images: list[Path], durations: list[float], out: Path) -> None:
    if len(images) != len(durations):
        raise RuntimeError("image/duration mismatch")
    args: list[str] = []
    filters: list[str] = []
    labels: list[str] = []
    for i, (image, duration) in enumerate(zip(images, durations)):
        args += ["-loop", "1", "-framerate", str(FPS), "-i", str(image)]
        phase = i * 0.67
        filters.append(
            f"[{i}:v]trim=duration={duration:.6f},setpts=PTS-STARTPTS,"
            f"scale=2688:1512:flags=lanczos,"
            f"crop={W}:{H}:x='64+18*sin(t/7+{phase:.3f})':y='36+10*cos(t/8+{phase:.3f})',"
            f"fps={FPS},setsar=1,format=yuv420p[v{i}]"
        )
        labels.append(f"[v{i}]")
    filters.append("".join(labels) + f"concat=n={len(images)}:v=1:a=0[vout]")
    expected = sum(durations)
    run([
        "ffmpeg", "-y", "-v", "error", *args,
        "-filter_complex", ";".join(filters), "-map", "[vout]",
        "-t", f"{expected:.6f}", "-an", "-r", str(FPS),
        "-c:v", "libx264", "-preset", "medium", "-crf", "16",
        "-profile:v", "high", "-level", "5.1", "-pix_fmt", "yuv420p",
        "-g", str(FPS*2), "-movflags", "+faststart", str(out),
    ])


def make_sheet(images: list[Path], out: Path) -> None:
    thumb_w, thumb_h = 512, 288
    sheet = Image.new("RGB", (thumb_w*5, thumb_h*2), color(BG_TOP))
    d = ImageDraw.Draw(sheet)
    for i, path in enumerate(images):
        thumb = Image.open(path).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x, y = (i % 5) * thumb_w, (i // 5) * thumb_h
        sheet.paste(thumb, (x, y))
        d.rectangle((x, y, x+thumb_w-1, y+thumb_h-1), outline=color(OUTLINE), width=3)
    sheet.save(out)


def validate_spec(spec: dict[str, Any]) -> None:
    if spec.get("marker") != "NEBULAMIND_FIVE_PAPER_VIDEO_SPECS_V2" or len(spec.get("papers", [])) != 5:
        raise RuntimeError("invalid V2 spec marker/count")
    keys: set[str] = set()
    titles: set[str] = set()
    for paper in spec["papers"]:
        key = paper["key"]
        if key in keys or paper["youtube_title"] in titles:
            raise RuntimeError("duplicate key/title")
        keys.add(key)
        titles.add(paper["youtube_title"])
        if len(paper["youtube_title"]) > 100 or len(paper["description"]) > 5000:
            raise RuntimeError(f"metadata overflow: {key}")
        if len(paper.get("scenes", [])) != 8:
            raise RuntimeError(f"{key}: expected 8 scenes")
        if "not validated" not in paper["description"].lower() or "journal or human peer review" not in paper["description"].lower():
            raise RuntimeError(f"{key}: missing description status boundary")
        if not Path(paper["pdf_path"]).is_file() or not Path(paper["first_page_path"]).is_file():
            raise RuntimeError(f"{key}: missing frozen media")
        counts = []
        for scene in paper["scenes"]:
            count = len(text_tokens(scene["narration"]))
            counts.append(count)
            if not 26 <= count <= 52:
                raise RuntimeError(f"{key}: scene narration {count} words outside 26–52")
            if not 2 <= len(scene["cards"]) <= 3:
                raise RuntimeError(f"{key}: invalid card count")
        total = sum(counts)
        if not 250 <= total <= 340:
            raise RuntimeError(f"{key}: total narration {total} outside 250–340")
        final_text = paper["scenes"][-1]["narration"].lower()
        if "not validated" not in final_text or "journal" not in final_text:
            raise RuntimeError(f"{key}: final spoken status boundary incomplete")


def build_paper(spec: dict[str, Any], paper: dict[str, Any], index: int, asr_model: WhisperModel) -> dict[str, Any]:
    verify_source_freeze()
    key = paper["key"]
    out_dir = OUT_ROOT / key
    work = BUILD_ROOT / key
    scene_dir = work / "scenes"
    raw_dir = work / "raw"
    for directory in (out_dir, scene_dir, raw_dir):
        directory.mkdir(parents=True, exist_ok=True)

    narration_text = "\n\n".join(scene["narration"].strip() for scene in paper["scenes"])
    narration_hash = hashlib.sha256(narration_text.encode("utf-8")).hexdigest()
    speed = float(spec["provider_speed"])
    raw = raw_dir / f"shimmer_speed_{speed:.2f}_{narration_hash[:16]}.wav"
    synthesize_whole_script(narration_text, raw, speed)
    narration = out_dir / f"{key}_SHIMMER_V2_MASTER.wav"
    loudness = normalize_audio(raw, narration)
    audio_duration = probe_duration(narration)
    word_count = len(text_tokens(narration_text))
    wpm = word_count / (audio_duration / 60.0)
    if not 105.0 <= wpm <= 125.0:
        raise RuntimeError(f"{key}: effective pace {wpm:.2f} WPM outside 105–125")

    asr_words, asr_transcript = transcribe_words(narration, asr_model)
    srt = out_dir / f"NEBULAMIND_PAPER_{key.upper().replace('-', '_')}_V2.srt"
    scene_durations, timeline, asr_metrics = derive_timeline_and_srt(paper, audio_duration, asr_words, srt)

    rendered = [render_open(paper, index*100)]
    rendered += [render_scene(paper, i, scene, index*100+i) for i, scene in enumerate(paper["scenes"], 1)]
    rendered += [render_close(paper, index*100+9)]
    image_paths: list[Path] = []
    for i, image in enumerate(rendered):
        path = scene_dir / f"scene_{i:02d}.png"
        image.convert("RGB").save(path, quality=96)
        image_paths.append(path)
    contact_sheet = out_dir / f"{key}_SCENE_SHEET.png"
    make_sheet(image_paths, contact_sheet)

    durations = [INTRO_SECONDS, *scene_durations, OUTRO_SECONDS]
    expected = sum(durations)
    silent = work / "silent_master.mp4"
    render_silent_video(image_paths, durations, silent)
    final = out_dir / f"NEBULAMIND_PAPER_{key.upper().replace('-', '_')}_V2.mp4"
    delay_ms = round(INTRO_SECONDS * 1000)
    audio_filter = (
        f"adelay={delay_ms}:all=1,apad=pad_dur={expected:.6f},"
        f"atrim=duration={expected:.6f}"
    )
    run([
        "ffmpeg", "-y", "-v", "error", "-i", str(silent), "-i", str(narration),
        "-map", "0:v:0", "-map", "1:a:0", "-af", audio_filter,
        "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
        "-movflags", "+faststart", "-metadata", f"title={paper['youtube_title']}",
        "-metadata", "comment=Plain-language machine-generated explainer; not validated",
        "-t", f"{expected:.6f}", str(final),
    ])
    observed = probe_duration(final)
    if abs(observed - expected) > 0.10:
        raise RuntimeError(f"{key}: final duration {observed} != {expected}")
    verify_source_freeze()

    checkpoint_path = out_dir / "publication_checkpoint.json"
    checkpoint = json.loads(checkpoint_path.read_text()) if checkpoint_path.exists() else {}
    if checkpoint.get("video_id"):
        raise RuntimeError(f"{key}: checkpoint already owns YouTube ID {checkpoint['video_id']}")
    checkpoint.update({
        "key": key,
        "source_sha256": sha256(final),
        "caption_sha256": sha256(srt),
        "title": paper["youtube_title"],
        "description": paper["description"],
        "video_id": "",
        "url": "",
        "caption_id": "",
        "privacy": "local",
        "processing": "not_uploaded",
        "status": "LOCAL_QA_PENDING",
        "uploaded_at": "",
        "published_at": "",
    })
    atomic_json(checkpoint_path, checkpoint)

    receipt = {
        "marker": "NEBULAMIND_PAPER_VIDEO_BUILD_COMPLETE_V2",
        "completed_at_utc": now(),
        "key": key,
        "spec_sha256": sha256(SPEC_PATH),
        "source_pdf": paper["pdf_path"],
        "source_pdf_sha256": sha256(Path(paper["pdf_path"])),
        "youtube_title": paper["youtube_title"],
        "description": paper["description"],
        "voice_provider": "openai_managed_nous_gateway",
        "voice_model": "gpt-4o-mini-tts",
        "voice": "shimmer",
        "provider_speed": speed,
        "post_tempo": 1.0,
        "word_count": word_count,
        "audio_occupied_seconds": round(audio_duration, 6),
        "effective_wpm": round(wpm, 3),
        "loudness": loudness,
        "presenter_policy": "approved Flow identity master appears only in silent opening/outro; no implied speech or lip-sync",
        "music": "none",
        "timeline": timeline,
        "expected_duration": round(expected, 6),
        "observed_duration": round(observed, 6),
        "artifact": str(final.resolve()),
        "artifact_sha256": sha256(final),
        "artifact_bytes": final.stat().st_size,
        "srt": str(srt.resolve()),
        "srt_sha256": sha256(srt),
        "narration": str(narration.resolve()),
        "narration_sha256": sha256(narration),
        "raw_tts": str(raw.resolve()),
        "raw_tts_sha256": sha256(raw),
        "narration_text_sha256": narration_hash,
        "asr_transcript": asr_transcript,
        "asr_metrics": asr_metrics,
        "contact_sheet": str(contact_sheet.resolve()),
        "contact_sheet_sha256": sha256(contact_sheet),
        "publication_state": "local QA pending; not uploaded",
    }
    atomic_json(out_dir / "build_receipt.json", receipt)
    return receipt


def make_batch_sheet(receipts: list[dict[str, Any]]) -> None:
    sheet = Image.new("RGB", (2560, 1440), color(BG_TOP))
    d = ImageDraw.Draw(sheet)
    for i, receipt in enumerate(receipts):
        thumb = Image.open(receipt["contact_sheet"]).convert("RGB").resize((1280, 288), Image.Resampling.LANCZOS)
        x = (i % 2) * 1280
        y = (i // 2) * 480
        sheet.paste(thumb, (x, y))
        d.rectangle((x, y, x+1279, y+287), outline=color(OUTLINE), width=3)
        d.text((x+30, y+318), receipt["key"], font=font(32), fill=CYAN)
        d.text((x+30, y+370), f"{receipt['effective_wpm']:.1f} WPM · Shimmer · descriptive, not validated", font=font(23), fill=MUTED)
    sheet.save(BATCH_SHEET)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--keys", nargs="*", help="build only selected local, unpublished siblings")
    args = parser.parse_args()
    for path in (PORTRAIT, FONT_PATH, ITALIC_FONT_PATH, SPEC_PATH, FREEZE_PATH):
        if not path.is_file():
            raise FileNotFoundError(path)
    verify_source_freeze()
    spec = json.loads(SPEC_PATH.read_text())
    validate_spec(spec)
    selected = set(args.keys or [])
    known = {paper["key"] for paper in spec["papers"]}
    if selected - known:
        raise RuntimeError(f"unknown keys: {sorted(selected-known)}")
    asr_model = WhisperModel("base.en", device="cpu", compute_type="int8")
    receipts: list[dict[str, Any]] = []
    for index, paper in enumerate(spec["papers"], 1):
        key = paper["key"]
        if selected and key not in selected:
            receipt_path = OUT_ROOT / key / "build_receipt.json"
            if not receipt_path.is_file():
                raise RuntimeError(f"{key}: missing sibling receipt")
            receipt = json.loads(receipt_path.read_text())
            if sha256(Path(receipt["artifact"])) != receipt["artifact_sha256"]:
                raise RuntimeError(f"{key}: sibling artifact drift")
            receipts.append(receipt)
            continue
        print(f"BUILD {index}/5 {key}", flush=True)
        receipts.append(build_paper(spec, paper, index, asr_model))
    make_batch_sheet(receipts)
    batch = {
        "marker": "NEBULAMIND_FIVE_PAPER_VIDEO_BATCH_BUILD_COMPLETE_V2",
        "completed_at_utc": now(),
        "source_freeze_verified": True,
        "spec": str(SPEC_PATH.resolve()),
        "spec_sha256": sha256(SPEC_PATH),
        "voice": "shimmer",
        "voice_model": "gpt-4o-mini-tts",
        "provider_speed": float(spec["provider_speed"]),
        "paper_count": len(receipts),
        "batch_sheet": str(BATCH_SHEET.resolve()),
        "batch_sheet_sha256": sha256(BATCH_SHEET),
        "artifacts": [{
            "key": receipt["key"],
            "path": receipt["artifact"],
            "sha256": receipt["artifact_sha256"],
            "bytes": receipt["artifact_bytes"],
            "srt": receipt["srt"],
            "srt_sha256": receipt["srt_sha256"],
            "title": receipt["youtube_title"],
            "duration": receipt["observed_duration"],
            "effective_wpm": receipt["effective_wpm"],
        } for receipt in receipts],
        "publication_state": "local QA pending; nothing uploaded",
    }
    atomic_json(BATCH_RECEIPT, batch)
    print(json.dumps(batch, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
