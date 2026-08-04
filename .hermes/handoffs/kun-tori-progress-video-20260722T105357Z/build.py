#!/usr/bin/env python3
"""Build the evidence-bounded Kun report + Tori progress status video."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import math
import random
import subprocess
import time

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

BASE = Path(__file__).resolve().parent
TMP = BASE / "build"
SCENES_DIR = TMP / "scenes"
AUDIO_DIR = TMP / "audio"
RAW_AUDIO_DIR = AUDIO_DIR / "raw"
for directory in (TMP, SCENES_DIR, AUDIO_DIR, RAW_AUDIO_DIR):
    directory.mkdir(parents=True, exist_ok=True)

FREEZE = BASE / "source_freeze.json"
PORTRAIT = Path(
    "/Users/duhokim/HermesOps/scripts/clips/subnav_flow_lipsync_v7/"
    "canary/flow_master_shoulder_crop_768x1024.png"
)
EDGE_TTS = Path("/Users/duhokim/.hermes/hermes-agent/venv/bin/edge-tts")
VOICE = "en-US-EmmaNeural"
FONT_PATH = Path("/System/Library/Fonts/SFNSMono.ttf")
ITALIC_FONT_PATH = Path("/System/Library/Fonts/SFNSMonoItalic.ttf")

W, H, FPS = 1280, 720, 30
FINAL = BASE / "KUN_REPORT_TORI_PROGRESS_REVIEW_V1.mp4"
SRT = BASE / "KUN_REPORT_TORI_PROGRESS_REVIEW_V1.srt"
NARRATION_WAV = BASE / "kun_tori_progress_female_narration.wav"
CONTACT_SHEET = BASE / "KUN_REPORT_TORI_PROGRESS_SCENE_SHEET.png"
BUILD_RECEIPT = BASE / "build_receipt.json"

BG_TOP = "#07101F"
BG_BOTTOM = "#0B1630"
CYAN = "#35D9F2"
MAGENTA = "#D95CFF"
SUCCESS = "#4EE09A"
WARNING = "#F2C14E"
FAIL = "#FF6B78"
BODY = "#EAF2FF"
MUTED = "#91A4C4"
PANEL = "#101E39"
PANEL_2 = "#142544"


@dataclass(frozen=True)
class Scene:
    index: int
    key: str
    duration: float
    narration: str
    captions: tuple[str, ...]


SCENES = (
    Scene(0, "open", 3.0, "", ()),
    Scene(
        1,
        "correction",
        11.5,
        "Kun’s oversight report rated the project healthy, with risks. One correction changed the plan: Claim Ledger Contract version one had already passed. The team would preserve and reconcile finished work, not rebuild it.",
        (
            "Kun’s oversight report rated the project healthy, with risks.",
            "One correction changed the plan: Claim Ledger Contract version one had already passed.",
            "The team would preserve and reconcile finished work, not rebuild it.",
        ),
    ),
    Scene(
        2,
        "preserve",
        13.0,
        "Phase zero preserved the contract: thirty-six files, sixteen ledger entries, forty-five evidence spans, forty-five stance rows, and twenty-six unique bibcodes. Source and backup digests and modification times matched, with zero validation errors.",
        (
            "Phase zero preserved the contract: 36 files, 16 ledger entries, 45 evidence spans, 45 stance rows, and 26 unique bibcodes.",
            "Source and backup digests and modification times matched, with zero validation errors.",
        ),
    ),
    Scene(
        3,
        "classify",
        12.0,
        "Phase one classified all three hundred eighty worktree entries before touching anything: two hundred twenty-two keep-commit, one hundred thirty archive, eighteen deletion candidates, and ten unknown. Nothing moved or deleted.",
        (
            "Phase one classified all 380 worktree entries before touching anything: 222 keep-commit, 130 archive, 18 deletion candidates, and 10 unknown.",
            "Nothing moved or deleted.",
        ),
    ),
    Scene(
        4,
        "rework",
        14.0,
        "Phases Two and Three chose rework piecemeal. Surveys would be rebuilt on current main; the wiki fix re-applied; the backend runner held for a product decision; superseded Lab front-end commits abandoned. Four intent patches preserved all twenty modified files.",
        (
            "Phases Two and Three chose rework piecemeal.",
            "Surveys: rebuild. Wiki fix: re-apply. Backend runner: hold. Superseded Lab front end: abandon.",
            "Four intent patches preserved all 20 modified files.",
        ),
    ),
    Scene(
        5,
        "tori",
        15.0,
        "Tori’s role was custody and receipt verification. In the Surveys unit, three independent fail-closed reviews produced two honest failures, then one unconditional pass across all ten acceptance items. Hwao closed the unit on that stronger evidence. The passing V2 stays frozen and uncommitted.",
        (
            "Tori’s role was custody and receipt verification.",
            "Three independent fail-closed reviews produced two honest failures, then one unconditional pass across all 10 acceptance items.",
            "Hwao closed the unit on that stronger evidence.",
            "The passing V2 stays frozen and uncommitted.",
        ),
    ),
    Scene(
        6,
        "kun_latest",
        17.0,
        "Kun’s latest check passed the corrected Phase Four scope: eighteen test database files, and ten cache directories split into two in ordinary future scope and eight held. Safety counters stayed at zero. Cleanup scope is defined, but cleanup, Git landing, database work, status-map work, runtime, and publication remain gated.",
        (
            "Kun’s latest check passed the corrected Phase Four scope: 18 test database files.",
            "Ten cache directories split into two in ordinary future scope and eight held. Safety counters stayed at zero.",
            "Cleanup scope is defined, but cleanup has not started.",
            "Git landing, database work, status-map work, runtime, and publication remain gated.",
        ),
    ),
    Scene(7, "close", 2.5, "", ()),
)


def run(command: list[str], *, retries: int = 0) -> None:
    attempt = 0
    while True:
        try:
            subprocess.run(command, check=True)
            return
        except subprocess.CalledProcessError:
            if attempt >= retries:
                raise
            time.sleep(2 ** attempt)
            attempt += 1


def capture(command: list[str]) -> str:
    return subprocess.check_output(command, text=True).strip()


def probe_duration(path: Path) -> float:
    return float(
        capture(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=nk=1:nw=1",
                str(path),
            ]
        )
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_source_freeze() -> None:
    freeze = json.loads(FREEZE.read_text())
    failures: list[str] = []
    for row in freeze["sources"]:
        path = Path(row["path"])
        if not path.is_file():
            failures.append(f"missing: {path}")
            continue
        observed = sha256(path)
        if observed != row["sha256"]:
            failures.append(f"hash drift: {path}: {observed} != {row['sha256']}")
    if failures:
        raise RuntimeError("SOURCE FREEZE DRIFT\n" + "\n".join(failures))


def color(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return (
        int(value[0:2], 16),
        int(value[2:4], 16),
        int(value[4:6], 16),
    )


def rgba(value: str, alpha: int = 255) -> tuple[int, int, int, int]:
    return (*color(value), alpha)


def font(size: int, *, italic: bool = False) -> ImageFont.FreeTypeFont:
    path = ITALIC_FONT_PATH if italic else FONT_PATH
    return ImageFont.truetype(str(path), size=size)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, text_font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        proposed = word if not current else f"{current} {word}"
        if draw.textlength(proposed, font=text_font) <= max_width:
            current = proposed
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
    text_font: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    line_gap: int = 6,
    max_lines: int | None = None,
) -> int:
    lines = wrap_text(draw, text, text_font, max_width)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while draw.textlength(last + "…", font=text_font) > max_width and last:
            last = last[:-1]
        lines[-1] = last.rstrip() + "…"
    x, y = xy
    bbox = draw.textbbox((0, 0), "Ag", font=text_font)
    height = bbox[3] - bbox[1]
    for line in lines:
        draw.text((x, y), line, font=text_font, fill=fill)
        y += height + line_gap
    return round(y)


def gradient_background(seed: int) -> Image.Image:
    top = color(BG_TOP)
    bottom = color(BG_BOTTOM)
    image = Image.new("RGB", (W, H), top)
    draw = ImageDraw.Draw(image)
    for y in range(H):
        t = y / max(1, H - 1)
        rgb = tuple(round(top[i] * (1 - t) + bottom[i] * t) for i in range(3))
        draw.line((0, y, W, y), fill=rgb)
    rng = random.Random(7100 + seed)
    for _ in range(95):
        x = rng.randrange(0, W)
        y = rng.randrange(0, 610)
        r = rng.choice((1, 1, 1, 2, 2, 3))
        hue = rng.choice((CYAN, MAGENTA, BODY, MUTED))
        a = rng.randrange(35, 120)
        draw.ellipse((x - r, y - r, x + r, y + r), fill=rgba(hue, a)[:3])
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-180, 60, 470, 700), fill=rgba(MAGENTA, 22))
    gd.ellipse((800, -160, 1480, 520), fill=rgba(CYAN, 26))
    glow = glow.filter(ImageFilter.GaussianBlur(90))
    return Image.alpha_composite(image.convert("RGBA"), glow)


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], *, outline: str = "#29466E", fill: str = PANEL, width: int = 2, radius: int = 22) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=rgba(fill, 238), outline=outline, width=width)


def header(draw: ImageDraw.ImageDraw, scene: Scene, kicker: str, title: str) -> None:
    draw.text((64, 26), "NebulaMind", font=font(22), fill=BODY)
    draw.text((220, 28), "STATUS BRIEF", font=font(16), fill=CYAN)
    draw.text((1100, 30), f"{scene.index:02d} / 06", font=font(15), fill=MUTED)
    draw.line((64, 64, 1216, 64), fill="#29466E", width=1)
    draw.text((64, 92), kicker.upper(), font=font(17), fill=CYAN)
    draw.text((64, 124), title, font=font(37), fill=BODY)


def caption_panel(draw: ImageDraw.ImageDraw, text: str) -> None:
    if not text:
        return
    panel(draw, (52, 604, 1228, 704), outline="#29466E", fill="#07101F", width=1, radius=18)
    draw.text((75, 621), "NARRATION", font=font(13), fill=CYAN)
    caption_font = font(15)
    lines = wrap_text(draw, text, caption_font, 1040)
    if len(lines) > 3:
        raise RuntimeError(f"burned-in narration exceeds three lines: {text}")
    y = 620
    for line in lines:
        draw.text((170, y), line, font=caption_font, fill=BODY)
        y += 24


def paste_portrait(image: Image.Image, box: tuple[int, int, int, int], opacity: float = 0.95) -> None:
    x0, y0, x1, y1 = box
    size = (x1 - x0, y1 - y0)
    portrait = Image.open(PORTRAIT).convert("RGB")
    portrait = ImageOps.fit(portrait, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.46))
    portrait = ImageEnhance.Color(portrait).enhance(0.90).convert("RGBA")
    mask = Image.new("L", size, 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((28, 20, size[0] - 28, size[1] - 20), radius=54, fill=round(255 * opacity))
    mask = mask.filter(ImageFilter.GaussianBlur(26))
    portrait.putalpha(mask)
    image.alpha_composite(portrait, (x0, y0))


def scene_open(scene: Scene) -> Image.Image:
    image = gradient_background(scene.index)
    paste_portrait(image, (755, 64, 1195, 650))
    draw = ImageDraw.Draw(image)
    draw.text((64, 42), "NebulaMind", font=font(23), fill=BODY)
    draw.text((64, 160), "STATUS REVIEW", font=font(18), fill=CYAN)
    draw.text((64, 205), "Kun’s report", font=font(48), fill=BODY)
    draw.text((64, 263), "+ Tori’s progress", font=font(42), fill=BODY)
    draw.line((64, 335, 610, 335), fill=CYAN, width=3)
    draw.text((64, 370), "Evidence-bounded update", font=font(22), fill=MUTED)
    draw.text((64, 410), "22 July 2026 · local review", font=font(18), fill=WARNING)
    panel(draw, (64, 500, 620, 570), outline="#29466E", fill="#0B1630", width=1, radius=17)
    draw.text((90, 521), "Silent guide portrait · narration begins next", font=font(15), fill=MUTED)
    return image


def scene_correction(scene: Scene) -> Image.Image:
    image = gradient_background(scene.index)
    draw = ImageDraw.Draw(image)
    header(draw, scene, "Kun oversight verdict", "The correction that changed the plan")
    panel(draw, (64, 190, 380, 360), outline=WARNING)
    draw.text((90, 215), "VERDICT", font=font(15), fill=WARNING)
    draw.text((90, 255), "HEALTHY", font=font(36), fill=BODY)
    draw.text((90, 300), "WITH RISKS", font=font(30), fill=WARNING)
    panel(draw, (420, 190, 760, 360), outline=SUCCESS)
    draw.text((446, 215), "MATERIAL CORRECTION", font=font(15), fill=SUCCESS)
    draw.text((446, 255), "CONTRACT V1", font=font(30), fill=BODY)
    draw.text((446, 300), "ALREADY PASS", font=font(27), fill=SUCCESS)
    panel(draw, (800, 190, 1216, 360), outline=CYAN)
    draw.text((826, 215), "RULING", font=font(15), fill=CYAN)
    draw.text((826, 255), "PRESERVE", font=font(28), fill=BODY)
    draw.text((826, 294), "RECONCILE", font=font(28), fill=BODY)
    draw.text((826, 333), "DO NOT REBUILD", font=font(17), fill=MUTED)
    draw.line((224, 402, 1056, 402), fill="#29466E", width=2)
    for x, value, label in ((224, "1", "correction"), (640, "0", "validation errors"), (1056, "0", "rebuilds")):
        draw.ellipse((x - 40, 430, x + 40, 510), fill=rgba(PANEL_2, 255), outline=CYAN, width=2)
        bbox = draw.textbbox((0, 0), value, font=font(30))
        draw.text((x - (bbox[2] - bbox[0]) / 2, 447), value, font=font(30), fill=BODY)
        bbox2 = draw.textbbox((0, 0), label, font=font(14))
        draw.text((x - (bbox2[2] - bbox2[0]) / 2, 528), label, font=font(14), fill=MUTED)
    caption_panel(draw, scene.narration)
    return image


def scene_preserve(scene: Scene) -> Image.Image:
    image = gradient_background(scene.index)
    draw = ImageDraw.Draw(image)
    header(draw, scene, "Phase 0 · complete", "Preserve truth first")
    metrics = (
        ("36 / 36", "files matched", CYAN),
        ("16", "ledger entries", SUCCESS),
        ("45", "evidence spans", MAGENTA),
        ("45", "stance rows", WARNING),
        ("26", "unique bibcodes", CYAN),
        ("0", "validation errors", SUCCESS),
    )
    for i, (value, label, accent) in enumerate(metrics):
        col, row = i % 3, i // 3
        x0 = 64 + col * 385
        y0 = 190 + row * 150
        panel(draw, (x0, y0, x0 + 350, y0 + 120), outline=accent)
        draw.text((x0 + 22, y0 + 18), value, font=font(32), fill=BODY)
        draw.text((x0 + 22, y0 + 72), label, font=font(15), fill=MUTED)
    panel(draw, (64, 505, 1216, 574), outline=SUCCESS, fill="#0D2730", width=2, radius=17)
    draw.text((88, 526), "SOURCE", font=font(15), fill=CYAN)
    draw.line((205, 540, 510, 540), fill=SUCCESS, width=3)
    draw.text((535, 526), "BACKUP", font=font(15), fill=CYAN)
    draw.text((710, 526), "digests + mtimes match", font=font(17), fill=SUCCESS)
    caption_panel(draw, scene.narration)
    return image


def scene_classify(scene: Scene) -> Image.Image:
    image = gradient_background(scene.index)
    draw = ImageDraw.Draw(image)
    header(draw, scene, "Phase 1 · complete, read-only", "Classify before touching")
    counts = ((222, "KEEP-COMMIT", CYAN), (130, "ARCHIVE", MAGENTA), (18, "DELETE-CANDIDATE", WARNING), (10, "UNKNOWN", MUTED))
    x, y, total_width = 64, 205, 1152
    cursor = x
    for count, _, accent in counts:
        width = round(total_width * count / 380)
        draw.rounded_rectangle((cursor, y, cursor + width, y + 72), radius=9, fill=accent)
        cursor += width
    draw.text((64, 293), "380 ENTRIES · EXACT PROPORTIONS", font=font(15), fill=MUTED)
    for i, (count, label, accent) in enumerate(counts):
        x0 = 64 + i * 288
        panel(draw, (x0, 340, x0 + 260, 465), outline=accent)
        draw.text((x0 + 18, 360), str(count), font=font(30), fill=BODY)
        draw.text((x0 + 18, 410), label, font=font(13), fill=accent)
    panel(draw, (64, 500, 1216, 575), outline=SUCCESS, fill="#0D2730", width=2, radius=17)
    draw.text((100, 523), "0 MOVES", font=font(20), fill=SUCCESS)
    draw.text((355, 523), "0 DELETES", font=font(20), fill=SUCCESS)
    draw.text((640, 523), "protected categories stayed protected", font=font(16), fill=MUTED)
    caption_panel(draw, scene.narration)
    return image


def scene_rework(scene: Scene) -> Image.Image:
    image = gradient_background(scene.index)
    draw = ImageDraw.Draw(image)
    header(draw, scene, "Phases 2–3 · decisions complete", "Rework piecemeal — never replay blindly")
    fates = (
        ("SURVEYS", "REWORK", SUCCESS),
        ("WIKI SOURCES", "RE-APPLY", CYAN),
        ("BACKEND RUNNER", "HOLD", WARNING),
        ("LAB FRONT END", "ABANDON · SUPERSEDED", FAIL),
    )
    for i, (unit, fate, accent) in enumerate(fates):
        col, row = i % 2, i // 2
        x0 = 64 + col * 360
        y0 = 200 + row * 155
        panel(draw, (x0, y0, x0 + 330, y0 + 125), outline=accent)
        draw.text((x0 + 20, y0 + 20), unit, font=font(15), fill=MUTED)
        draw.text((x0 + 20, y0 + 68), fate, font=font(18), fill=accent)
    panel(draw, (800, 200, 1216, 480), outline=MAGENTA, fill="#161A3B", width=2, radius=24)
    draw.text((830, 228), "DIRTY INTENT", font=font(16), fill=MAGENTA)
    draw.text((830, 282), "4", font=font(62), fill=BODY)
    draw.text((930, 310), "patches", font=font(18), fill=MUTED)
    draw.line((830, 375, 1170, 375), fill="#493A70", width=2)
    draw.text((830, 402), "20 / 20", font=font(31), fill=SUCCESS)
    draw.text((1015, 414), "modified paths", font=font(14), fill=MUTED)
    draw.text((64, 530), "No whole-branch rebase · no blind cherry-pick · no wholesale abandon", font=font(16), fill=MUTED)
    caption_panel(draw, scene.narration)
    return image


def scene_tori(scene: Scene) -> Image.Image:
    image = gradient_background(scene.index)
    draw = ImageDraw.Draw(image)
    header(draw, scene, "Tori progress · Surveys custody chain", "Fail closed until the evidence passed")
    xs = (150, 455, 760, 1065)
    draw.line((xs[0], 285, xs[-1], 285), fill="#29466E", width=4)
    timeline = (
        ("REVIEW 1", "FAIL", FAIL),
        ("REVIEW 2", "FAIL", FAIL),
        ("REVIEW 3", "PASS", SUCCESS),
        ("HWAO", "CLOSED", CYAN),
    )
    for x, (top, bottom, accent) in zip(xs, timeline):
        draw.ellipse((x - 34, 251, x + 34, 319), fill=rgba(PANEL_2, 255), outline=accent, width=4)
        bbox = draw.textbbox((0, 0), "✓" if bottom in ("PASS", "CLOSED") else "×", font=font(25))
        glyph = "✓" if bottom in ("PASS", "CLOSED") else "×"
        draw.text((x - (bbox[2] - bbox[0]) / 2, 269), glyph, font=font(25), fill=accent)
        bbox1 = draw.textbbox((0, 0), top, font=font(13))
        draw.text((x - (bbox1[2] - bbox1[0]) / 2, 335), top, font=font(13), fill=MUTED)
        bbox2 = draw.textbbox((0, 0), bottom, font=font(18))
        draw.text((x - (bbox2[2] - bbox2[0]) / 2, 365), bottom, font=font(18), fill=accent)
    panel(draw, (64, 430, 570, 570), outline=CYAN)
    draw.text((90, 452), "TORI", font=font(15), fill=CYAN)
    draw.text((90, 490), "custody + receipt verification", font=font(18), fill=BODY)
    draw.text((90, 532), "three independent reviews preserved", font=font(14), fill=MUTED)
    panel(draw, (610, 430, 1216, 570), outline=WARNING)
    draw.text((636, 452), "V2 STATUS", font=font(15), fill=WARNING)
    draw.text((636, 490), "FROZEN · UNCOMMITTED", font=font(21), fill=BODY)
    draw.text((636, 532), "Git landing remains a future explicit gate", font=font(14), fill=MUTED)
    caption_panel(draw, scene.narration)
    return image


def scene_kun_latest(scene: Scene) -> Image.Image:
    image = gradient_background(scene.index)
    draw = ImageDraw.Draw(image)
    header(draw, scene, "Kun latest check · PASS", "Cleanup scope defined — execution still gated")
    metrics = (
        ("18", "test database files", CYAN),
        ("10", "cache directories", MAGENTA),
        ("2 + 8", "future scope + held", WARNING),
        ("0", "safety counters", SUCCESS),
    )
    for i, (value, label, accent) in enumerate(metrics):
        x0 = 64 + i * 288
        panel(draw, (x0, 190, x0 + 260, 310), outline=accent)
        draw.text((x0 + 18, 208), value, font=font(30), fill=BODY)
        draw.text((x0 + 18, 260), label, font=font(13), fill=accent)
    panel(draw, (64, 345, 570, 570), outline=SUCCESS, fill="#0D2730")
    draw.text((90, 370), "COMPLETE", font=font(17), fill=SUCCESS)
    complete = ("preservation", "classification", "IA + branch decisions", "Surveys review unit", "Phase 4 scope")
    for i, item in enumerate(complete):
        draw.text((90, 411 + i * 29), f"✓  {item}", font=font(15), fill=BODY)
    panel(draw, (610, 345, 1216, 570), outline=WARNING, fill="#2A2318")
    draw.text((636, 370), "HELD / CLOSED", font=font(17), fill=WARNING)
    held = ("cleanup", "Git landing", "database work", "status-map work", "runtime + publication")
    for i, item in enumerate(held):
        draw.text((636, 411 + i * 29), f"—  {item}", font=font(15), fill=BODY)
    caption_panel(draw, scene.narration)
    return image


def scene_close(scene: Scene) -> Image.Image:
    image = gradient_background(scene.index)
    paste_portrait(image, (70, 68, 510, 654))
    draw = ImageDraw.Draw(image)
    draw.text((600, 155), "PROGRESS IS REAL.", font=font(36), fill=SUCCESS)
    draw.text((600, 215), "GATES STILL MATTER.", font=font(36), fill=WARNING)
    draw.line((600, 285, 1180, 285), fill=CYAN, width=3)
    draw.text((600, 330), "Completed", font=font(16), fill=SUCCESS)
    draw_wrapped(draw, (600, 365), "preservation · classification · decisions · Surveys review · scope definition", font(17), BODY, 560, line_gap=8)
    draw.text((600, 465), "Still gated", font=font(16), fill=WARNING)
    draw_wrapped(draw, (600, 500), "cleanup · Git · database · status map · runtime · publication", font(17), BODY, 560, line_gap=8)
    draw.text((600, 625), "LOCAL REVIEW · NO ACTION AUTHORIZED", font=font(14), fill=MUTED)
    return image


SCENE_RENDERERS = {
    "open": scene_open,
    "correction": scene_correction,
    "preserve": scene_preserve,
    "classify": scene_classify,
    "rework": scene_rework,
    "tori": scene_tori,
    "kun_latest": scene_kun_latest,
    "close": scene_close,
}


def render_scene_images() -> list[Path]:
    paths: list[Path] = []
    for scene in SCENES:
        image = SCENE_RENDERERS[scene.key](scene).convert("RGB")
        path = SCENES_DIR / f"scene_{scene.index:02d}_{scene.key}.png"
        image.save(path, quality=95)
        paths.append(path)
    return paths


def make_contact_sheet(scene_paths: list[Path]) -> None:
    sheet = Image.new("RGB", (W, H // 2), color(BG_TOP))
    draw = ImageDraw.Draw(sheet)
    for i, path in enumerate(scene_paths):
        thumb = Image.open(path).convert("RGB").resize((320, 180), Image.Resampling.LANCZOS)
        x = (i % 4) * 320
        y = (i // 4) * 180
        sheet.paste(thumb, (x, y))
        draw.rectangle((x, y, x + 319, y + 179), outline=color("#29466E"), width=2)
    sheet.save(CONTACT_SHEET)


def synthesize(scene: Scene, rate_percent: int) -> tuple[Path, float, str]:
    rate = f"{rate_percent:+d}%"
    raw = RAW_AUDIO_DIR / f"scene_{scene.index:02d}_{VOICE}_rate_{rate_percent:+d}.mp3"
    run(
        [
            str(EDGE_TTS),
            "--voice",
            VOICE,
            f"--rate={rate}",
            "--text",
            scene.narration,
            "--write-media",
            str(raw),
        ],
        retries=2,
    )
    return raw, probe_duration(raw), rate


def render_scene_audio(scene: Scene) -> dict:
    output = AUDIO_DIR / f"scene_{scene.index:02d}.wav"
    if not scene.narration:
        run(
            [
                "ffmpeg",
                "-y",
                "-v",
                "error",
                "-f",
                "lavfi",
                "-t",
                f"{scene.duration:.6f}",
                "-i",
                "anullsrc=r=48000:cl=mono",
                "-ac",
                "1",
                "-ar",
                "48000",
                "-c:a",
                "pcm_s16le",
                str(output),
            ]
        )
        return {"scene": scene.index, "duration": scene.duration, "silence": True, "output": str(output)}

    speech_start = 0.35
    speech_end_pad = 0.20
    target = scene.duration - speech_start - speech_end_pad
    initial_rate = 20
    raw, raw_duration, actual_rate = synthesize(scene, initial_rate)
    tempo = raw_duration / target
    if not 0.90 <= tempo <= 1.10:
        derived = round((tempo * (1 + initial_rate / 100) - 1) * 100)
        derived = max(-20, min(70, derived))
        raw, raw_duration, actual_rate = synthesize(scene, derived)
        tempo = raw_duration / target
    if tempo < 0.85:
        tempo = 1.0
    if tempo > 1.15:
        raise RuntimeError(f"scene {scene.index}: timing adjustment {tempo:.3f} outside natural range")
    filter_graph = (
        f"[1:a]aformat=sample_rates=48000:channel_layouts=mono,"
        f"atempo={tempo:.8f},adelay={round(speech_start * 1000)}:all=1[voice];"
        f"[0:a][voice]amix=inputs=2:duration=first:normalize=0,alimiter=limit=.95[out]"
    )
    run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-f",
            "lavfi",
            "-t",
            f"{scene.duration:.6f}",
            "-i",
            "anullsrc=r=48000:cl=mono",
            "-i",
            str(raw),
            "-filter_complex",
            filter_graph,
            "-map",
            "[out]",
            "-ac",
            "1",
            "-ar",
            "48000",
            "-t",
            f"{scene.duration:.6f}",
            "-c:a",
            "pcm_s16le",
            str(output),
        ]
    )
    speech_duration = raw_duration / tempo
    return {
        "scene": scene.index,
        "duration": scene.duration,
        "text": scene.narration,
        "voice": VOICE,
        "voice_gender": "Female",
        "synthesis_rate": actual_rate,
        "raw_duration": round(raw_duration, 6),
        "atempo": round(tempo, 6),
        "actual_speech_duration": round(speech_duration, 6),
        "trailing_room": round(scene.duration - speech_start - speech_duration, 6),
        "output": str(output),
    }


def render_audio() -> list[dict]:
    rows = [render_scene_audio(scene) for scene in SCENES]
    inputs: list[str] = []
    pads: list[str] = []
    for i, row in enumerate(rows):
        inputs.extend(("-i", row["output"]))
        pads.append(f"[{i}:a]")
    run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            *inputs,
            "-filter_complex",
            "".join(pads) + f"concat=n={len(rows)}:v=0:a=1[a]",
            "-map",
            "[a]",
            "-ac",
            "1",
            "-ar",
            "48000",
            "-c:a",
            "pcm_s16le",
            str(NARRATION_WAV),
        ]
    )
    return rows


def srt_time(seconds: float) -> str:
    milliseconds = round(seconds * 1000)
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    secs, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"


def write_srt() -> None:
    cursor = 0.0
    cue_index = 1
    blocks: list[str] = []
    for scene in SCENES:
        scene_start = cursor
        scene_end = cursor + scene.duration
        if scene.captions:
            usable_start = scene_start + 0.35
            usable_end = scene_end - 0.20
            weights = [max(1, len(chunk.split())) for chunk in scene.captions]
            total_weight = sum(weights)
            local = usable_start
            for chunk, weight in zip(scene.captions, weights):
                duration = (usable_end - usable_start) * weight / total_weight
                end = local + duration
                blocks.append(f"{cue_index}\n{srt_time(local)} --> {srt_time(end)}\n{chunk}\n")
                cue_index += 1
                local = end
        cursor = scene_end
    SRT.write_text("\n".join(blocks), encoding="utf-8")


def render_scene_videos(scene_paths: list[Path]) -> list[Path]:
    outputs: list[Path] = []
    for scene, image_path in zip(SCENES, scene_paths):
        output = SCENES_DIR / f"scene_{scene.index:02d}.mp4"
        phase = scene.index * 0.67
        vf = (
            "scale=1344:756:flags=lanczos,"
            f"crop=1280:720:x='(iw-ow)/2+10*sin(t/5+{phase:.3f})':"
            f"y='(ih-oh)/2+5*cos(t/6+{phase:.3f})',"
            f"fade=t=in:st=0:d=0.35,fade=t=out:st={scene.duration - 0.35:.3f}:d=0.35,"
            "format=yuv420p"
        )
        run(
            [
                "ffmpeg",
                "-y",
                "-v",
                "error",
                "-loop",
                "1",
                "-framerate",
                str(FPS),
                "-i",
                str(image_path),
                "-t",
                f"{scene.duration:.6f}",
                "-vf",
                vf,
                "-an",
                "-r",
                str(FPS),
                "-c:v",
                "libx264",
                "-preset",
                "medium",
                "-crf",
                "18",
                "-profile:v",
                "high",
                "-pix_fmt",
                "yuv420p",
                "-g",
                str(FPS * 2),
                str(output),
            ]
        )
        outputs.append(output)
    return outputs


def concatenate_video(scene_videos: list[Path]) -> Path:
    silent = TMP / "silent_master.mp4"
    inputs: list[str] = []
    pads: list[str] = []
    for i, path in enumerate(scene_videos):
        inputs.extend(("-i", str(path)))
        pads.append(f"[{i}:v]")
    run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            *inputs,
            "-filter_complex",
            "".join(pads) + f"concat=n={len(scene_videos)}:v=1:a=0[v]",
            "-map",
            "[v]",
            "-an",
            "-r",
            str(FPS),
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-profile:v",
            "high",
            "-pix_fmt",
            "yuv420p",
            "-g",
            str(FPS * 2),
            str(silent),
        ]
    )
    return silent


def mux_final(silent_video: Path) -> None:
    verify_source_freeze()
    expected_duration = sum(scene.duration for scene in SCENES)
    audio_filter = (
        f"loudnorm=I=-16:LRA=7:TP=-1.5,apad=pad_dur={expected_duration:.6f},"
        f"atrim=duration={expected_duration:.6f}"
    )
    run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-i",
            str(silent_video),
            "-i",
            str(NARRATION_WAV),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-af",
            audio_filter,
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-profile:v",
            "high",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-ar",
            "48000",
            "-ac",
            "2",
            "-movflags",
            "+faststart",
            "-metadata",
            "title=Kun report and Tori progress — local review",
            "-metadata",
            "comment=Evidence-bounded local review; no action authorized",
            "-t",
            f"{expected_duration:.6f}",
            str(FINAL),
        ]
    )


def main() -> None:
    verify_source_freeze()
    scene_paths = render_scene_images()
    make_contact_sheet(scene_paths)
    write_srt()
    audio_rows = render_audio()
    scene_videos = render_scene_videos(scene_paths)
    silent = concatenate_video(scene_videos)
    mux_final(silent)
    final_duration = probe_duration(FINAL)
    expected_duration = sum(scene.duration for scene in SCENES)
    if abs(final_duration - expected_duration) > 0.08:
        raise RuntimeError(f"final duration {final_duration} != expected {expected_duration}")
    receipt = {
        "marker": "KUN_TORI_PROGRESS_VIDEO_BUILD_COMPLETE_V1",
        "completed_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_freeze_verified_before_build": True,
        "source_freeze_verified_before_final_mux": True,
        "voice": VOICE,
        "voice_gender": "Female",
        "presenter_policy": "approved synthetic portrait appears only during silent opening/outro; no visible narration or false lip-sync",
        "music": "none",
        "expected_duration": expected_duration,
        "observed_duration": final_duration,
        "artifact": str(FINAL),
        "artifact_sha256": sha256(FINAL),
        "artifact_bytes": FINAL.stat().st_size,
        "srt": str(SRT),
        "srt_sha256": sha256(SRT),
        "narration": str(NARRATION_WAV),
        "narration_sha256": sha256(NARRATION_WAV),
        "contact_sheet": str(CONTACT_SHEET),
        "contact_sheet_sha256": sha256(CONTACT_SHEET),
        "scenes": audio_rows,
        "publication_state": "local review only; not uploaded or published",
    }
    BUILD_RECEIPT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
