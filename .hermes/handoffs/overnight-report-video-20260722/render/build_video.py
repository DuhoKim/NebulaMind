#!/usr/bin/env python3
"""Build the source-grounded 73.5-second overnight-report review master."""
from __future__ import annotations

import json
import random
import shutil
import subprocess
import tempfile
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from overnight_content import (
    CAPTION_CUES, DURATION, FPS, GUIDE, NARRATION, SCENE_BOUNDARIES,
    SCENE_FRAMES, SOURCE_CONTRACT, TITLES,
)

BASE = Path(__file__).resolve().parent
V8_BASE = Path("/Users/duhokim/HermesOps/scripts/clips/subnav_flow_female_voice_v8")
PRESENTER_MASK = V8_BASE / "canary/presenter_feather_mask_320x340.png"
AMBIENT = V8_BASE / "original_cosmic_ambient_73s.wav"
TALKING_HEAD = BASE / "talking_head/overnight_report.mp4"
DRIVER_AUDIO = BASE / "driver_audio/overnight_report_female_exact_narration_73s.wav"
NARRATION_RECEIPT = BASE / "narration_receipt.json"
OUTPUT = BASE / "NEBULAMIND_OVERNIGHT_REPORT_V1_FEMALE_VOICE_EXACT_LIPSYNC.mp4"
SRT = BASE / "NEBULAMIND_OVERNIGHT_REPORT_V1_FEMALE_VOICE_EXACT_LIPSYNC.srt"
SOURCES = [Path(f"/Users/duhokim/HermesOps/scripts/clips/clip_{n:02d}_hq.mp4") for n in (1, 3, 5, 7, 9, 11)]

W, H = 1280, 720
FONT_REG = Path("/System/Library/Fonts/Supplemental/Arial.ttf")
FONT_BOLD = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")
FONT_MONO = Path("/System/Library/Fonts/SFNSMono.ttf")
WHITE = (242, 247, 255, 255)
MUTED = (178, 194, 220, 255)
TEAL = (78, 226, 214, 255)
BLUE = (77, 139, 223, 255)
INDIGO = (124, 134, 255, 255)
GOLD = (232, 184, 75, 255)
RED = (255, 118, 118, 255)
GREEN = (108, 225, 147, 255)
PANEL = (8, 16, 42, 240)
BORDER = (80, 113, 168, 190)
ACCENTS = [
    (65, 94, 157, 255), (72, 114, 181, 255), (84, 137, 192, 255),
    (113, 155, 188, 255), (175, 169, 126, 255), GOLD,
]


def font(size: int, bold: bool = False, mono: bool = False):
    path = FONT_MONO if mono and FONT_MONO.exists() else FONT_BOLD if bold else FONT_REG
    return ImageFont.truetype(str(path), size)


def draw_text(draw, xy, value, size, color=WHITE, bold=False, maxw=None, spacing=5, anchor=None, mono=False):
    fnt = font(size, bold, mono)
    x, y = xy
    if maxw is None:
        draw.text((x, y), value, font=fnt, fill=color, anchor=anchor)
        return y + size
    words = value.split()
    lines, current = [], ""
    for word in words:
        candidate = (current + " " + word).strip()
        if draw.textbbox((0, 0), candidate, font=fnt)[2] <= maxw:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=color)
        y += size + spacing
    return y


def panel(draw, box, fill=PANEL, outline=BORDER, radius=18, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw, start, end, color=TEAL, width=4):
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2 - 10, y2), fill=color, width=width)
    draw.polygon([(x2 - 10, y2 - 7), (x2, y2), (x2 - 10, y2 + 7)], fill=color)


def header(draw, idx: int):
    accent = ACCENTS[idx - 1]
    title, subtitle = TITLES[idx - 1]
    draw.rectangle((0, 0, W, H), fill=(4, 8, 25, 226))
    draw.rectangle((0, 610, W, H), fill=(accent[0], accent[1], accent[2], 20))
    draw_text(draw, (58, 31), "NEBULAMIND • OVERNIGHT REPORT", 19, accent, True)
    draw_text(draw, (1222, 31), f"{idx}/6", 18, MUTED, True, anchor="ra")
    draw_text(draw, (58, 76), title, 39, WHITE, True, maxw=875)
    draw_text(draw, (60, 132), subtitle, 19, MUTED, maxw=870)
    draw.line((58, 188, 1222, 188), fill=(83, 112, 165, 180), width=2)
    draw_text(draw, (982, 214), "AI-SCIENTIST STATUS BRIEF", 13, accent, True, maxw=225)
    panel(draw, (965, 244, 1216, 318), fill=(8, 18, 43, 190), outline=accent, radius=20, width=2)
    draw_text(draw, (985, 263), GUIDE[idx - 1], 18, WHITE, True, maxw=208, spacing=3)


def footer(draw, idx: int):
    accent = ACCENTS[idx - 1]
    for i in range(6):
        color = accent if i < idx else (74, 92, 127, 255)
        draw.rounded_rectangle((58 + i * 34, 670, 84 + i * 34, 677), radius=4, fill=color)
    draw_text(draw, (925, 657), "same host • overnight status", 15, MUTED, anchor="ra")


def card(draw, box, heading, value, note, accent, value_size=28):
    panel(draw, box, fill=(9, 19, 49, 242), outline=accent, radius=16, width=3)
    x1, y1, x2, _ = box
    draw_text(draw, (x1 + 18, y1 + 16), heading, 15, accent, True, maxw=x2 - x1 - 36)
    draw_text(draw, (x1 + 18, y1 + 50), value, value_size, WHITE, True, maxw=x2 - x1 - 36)
    draw_text(draw, (x1 + 18, y1 + 96), note, 15, MUTED, maxw=x2 - x1 - 36, spacing=3)


def draw_scene_1(draw):
    panel(draw, (75, 225, 935, 530), fill=(7, 15, 40, 242), outline=ACCENTS[0], radius=28, width=3)
    draw_text(draw, (105, 262), "OVERNIGHT OUTCOME", 18, ACCENTS[0], True)
    draw_text(draw, (105, 315), "CORPUS FOUNDATION", 41, WHITE, True)
    draw_text(draw, (105, 377), "+ 3 QUALITY GATES", 41, GOLD, True)
    panel(draw, (105, 455, 535, 505), fill=(40, 29, 17, 240), outline=GOLD, radius=20, width=2)
    draw_text(draw, (320, 480), "0 AUTO-PAPERS • BY DESIGN", 17, GOLD, True, anchor="mm")
    panel(draw, (600, 260, 900, 465), fill=(8, 23, 48, 238), outline=TEAL, radius=24, width=3)
    for y, label in ((305, "CORPUS"), (365, "GROUNDING"), (425, "GATES")):
        draw.ellipse((635, y - 12, 659, y + 12), outline=TEAL, width=3)
        draw_text(draw, (680, y), label, 19, WHITE, True, anchor="lm")
    draw_text(draw, (105, 565), "LOCAL SNAPSHOT • 2026-07-22 11:25 KST", 14, MUTED, True, mono=True)


def draw_scene_2(draw):
    panel(draw, (70, 220, 570, 575), fill=(8, 18, 44, 244), outline=ACCENTS[1], radius=24, width=3)
    draw_text(draw, (105, 252), "PAPERS EMBEDDED", 17, ACCENTS[1], True)
    draw_text(draw, (105, 310), "120,676", 69, WHITE, True)
    draw_text(draw, (105, 400), "astro-ph.GA + astro-ph.CO", 23, TEAL, True)
    draw_text(draw, (105, 440), "2009–2026", 21, MUTED, True)
    draw.rounded_rectangle((105, 505, 520, 531), radius=12, fill=(35, 43, 71, 240))
    draw.rounded_rectangle((105, 505, 480, 531), radius=12, fill=ACCENTS[1])
    draw_text(draw, (105, 545), "1.24 GB semantic index • ≈10× old 12k corpus", 15, MUTED)
    card(draw, (610, 235, 940, 390), "EMBEDDING MODEL", "qwen3-embedding-4b", "won a 10-model citation-retrieval evaluation", TEAL, 23)
    card(draw, (610, 425, 940, 575), "STATUS", "DONE", "embedded foundation ready for local retrieval", GREEN, 30)


def draw_scene_3(draw):
    panel(draw, (70, 220, 610, 585), fill=(8, 18, 44, 242), outline=ACCENTS[2], radius=22, width=3)
    draw_text(draw, (105, 245), "57-TOPIC COUNT GRID", 17, ACCENTS[2], True)
    # Uniform count grid only: deliberately no synthetic UMAP geometry.
    for i in range(57):
        row, col = divmod(i, 19)
        x, y = 105 + col * 25, 315 + row * 66
        color = GOLD if i == 0 else (83, 137, 192, 215)
        radius = 9 if i == 0 else 6
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)
    draw_text(draw, (105, 520), "uniform grid = count only; no invented UMAP coordinates", 14, MUTED, mono=True)
    panel(draw, (640, 225, 940, 420), fill=(12, 22, 50, 244), outline=GOLD, radius=20, width=3)
    draw_text(draw, (670, 255), "RANK #1", 17, GOLD, True)
    draw_text(draw, (670, 305), "JWST high-z", 29, WHITE, True)
    draw_text(draw, (670, 348), "galaxy evolution", 27, WHITE, True)
    draw_text(draw, (670, 390), "by a wide margin", 17, GOLD, True)
    panel(draw, (640, 450, 940, 585), fill=(8, 20, 44, 240), outline=ACCENTS[2], radius=18, width=2)
    draw_text(draw, (670, 475), "UMAP → HDBSCAN → c-TF-IDF", 16, TEAL, True)
    draw_text(draw, (670, 517), "8.9M citation edges", 24, WHITE, True)
    draw_text(draw, (670, 553), "ranked by recent citation inflow", 15, MUTED)


def draw_scene_4(draw):
    nodes = [
        (75, "QUERY", "research question", TEAL),
        (290, "LOCAL INDEX", "120,676 papers", ACCENTS[3]),
        (535, "WORKING SET", "semantic retrieval", INDIGO),
        (750, "DEEP READ", "HTML-first • ar5iv", GOLD),
    ]
    for i, (x, head, note, color) in enumerate(nodes):
        panel(draw, (x, 265, x + 175, 400), fill=(9, 19, 49, 244), outline=color, radius=18, width=3)
        draw_text(draw, (x + 87, 310), head, 16, color, True, anchor="mm")
        draw_text(draw, (x + 87, 360), note, 14, WHITE, True, anchor="mm")
        if i < len(nodes) - 1:
            arrow(draw, (x + 182, 333), (nodes[i + 1][0] - 8, 333), color, 3)
    card(draw, (95, 455, 475, 590), "CANONICAL DEEP LAYER", "4,864 papers", "top-cited • full-text embedded", ACCENTS[3], 31)
    panel(draw, (520, 455, 915, 590), fill=(9, 19, 49, 242), outline=TEAL, radius=18, width=3)
    draw_text(draw, (550, 480), "CLEAN HTML", 16, TEAL, True)
    draw.rounded_rectangle((550, 525, 875, 551), radius=12, fill=(35, 43, 71, 240))
    draw.rounded_rectangle((550, 525, 862, 551), radius=12, fill=TEAL)
    draw_text(draw, (875, 480), "96%", 27, WHITE, True, anchor="ra")
    draw_text(draw, (550, 568), "retrieval + grounding are wired", 15, MUTED)


def funnel(draw, x, y, color):
    draw.polygon([(x, y), (x + 42, y), (x + 29, y + 23), (x + 29, y + 42), (x + 13, y + 51), (x + 13, y + 23)], outline=color, fill=(color[0], color[1], color[2], 42))


def draw_scene_5(draw):
    gates = [
        ("NOVELTY", "aborts already-done work • cites the prior paper", TEAL),
        ("EXPECTED VALUE", "numeric targets • physical-sanity rejects gross errors", GOLD),
        ("CITATION ENTAILMENT", "verifies real citations • catches fabricated ones", INDIGO),
    ]
    for i, (head, note, color) in enumerate(gates):
        y = 220 + i * 120
        panel(draw, (75, y, 935, y + 96), fill=(9, 19, 49, 244), outline=color, radius=18, width=3)
        funnel(draw, 105, y + 22, color)
        draw_text(draw, (180, y + 18), head, 21, color, True)
        draw_text(draw, (180, y + 55), note, 16, WHITE, maxw=710)
    panel(draw, (245, 590, 770, 638), fill=(17, 35, 35, 242), outline=GREEN, radius=18, width=2)
    draw_text(draw, (507, 614), "BUILT • WIRED • VALIDATED", 18, GREEN, True, anchor="mm")


def draw_scene_6(draw):
    panel(draw, (75, 220, 935, 470), fill=(10, 18, 42, 246), outline=GOLD, radius=28, width=4)
    draw_text(draw, (110, 250), "PAPERS AUTO-GENERATED", 18, MUTED, True)
    draw_text(draw, (110, 300), "0", 82, GOLD, True)
    draw_text(draw, (240, 325), "work held until the gates existed", 23, WHITE, True)
    draw.line((110, 420, 895, 420), fill=(95, 112, 148, 180), width=2)
    draw_text(draw, (110, 438), "NEXT", 15, TEAL, True)
    draw_text(draw, (195, 435), "end-to-end gated study runs", 24, WHITE, True)
    panel(draw, (105, 505, 610, 560), fill=(11, 23, 49, 242), outline=ACCENTS[5], radius=18, width=2)
    draw_text(draw, (357, 532), "EXECUTION PHRASE: NONE ARMED", 17, ACCENTS[5], True, anchor="mm")
    draw_text(draw, (105, 595), "LOCAL REVIEW MASTER • NOT PUBLISHED", 14, MUTED, True, mono=True)
    draw_text(draw, (105, 620), "GE_AUTOPILOT_OVERNIGHT_20260719_CORPUS_GATES_DONE", 12, MUTED, mono=True)


DRAWERS = [draw_scene_1, draw_scene_2, draw_scene_3, draw_scene_4, draw_scene_5, draw_scene_6]


def render_scene(idx: int) -> Image.Image:
    image = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    header(draw, idx)
    DRAWERS[idx - 1](draw)
    footer(draw, idx)
    return image


def timestamp(value: float) -> str:
    ms = int(round(value * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def wrap_caption(value: str) -> str:
    lines = textwrap.wrap(value, width=42, break_long_words=False, break_on_hyphens=False)
    if len(lines) > 2:
        raise RuntimeError(f"caption requires more than two lines: {value!r} -> {lines}")
    return "\n".join(lines)


def write_srt() -> None:
    receipt = json.loads(NARRATION_RECEIPT.read_text(encoding="utf-8"))
    lines, cue_number = [], 1
    for scene_index, cues in enumerate(CAPTION_CUES):
        row = receipt["scenes"][scene_index]
        start = SCENE_BOUNDARIES[scene_index] + row["speech_start"]
        speech_duration = row["actual_speech_duration"]
        weights = [max(1, len(cue.replace("—", "").split())) for cue in cues]
        total = sum(weights)
        cursor = start
        for cue, weight in zip(cues, weights):
            end = cursor + speech_duration * weight / total
            lines += [str(cue_number), f"{timestamp(cursor)} --> {timestamp(end)}", wrap_caption(cue), ""]
            cue_number += 1
            cursor = end
    SRT.write_text("\n".join(lines), encoding="utf-8")


def probe(path: Path) -> dict:
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration,size:stream=codec_name,width,height,r_frame_rate,nb_frames",
        "-of", "json", str(path),
    ], text=True))


def run(command):
    subprocess.run(command, check=True)


def main() -> None:
    required = SOURCES + [PRESENTER_MASK, AMBIENT, TALKING_HEAD, DRIVER_AUDIO, NARRATION_RECEIPT]
    for path in required:
        if not path.exists():
            raise FileNotFoundError(path)
    stills = BASE / "stills"
    stills.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="nm_overnight_report_v1_"))
    try:
        segments = []
        for idx in range(1, 7):
            scene_start = SCENE_BOUNDARIES[idx - 1]
            duration = SCENE_BOUNDARIES[idx] - scene_start
            overlay = work / f"scene_{idx:02d}.png"
            scene_image = render_scene(idx)
            scene_image.save(overlay)
            review_background = Image.new("RGBA", (W, H), (4, 8, 25, 255))
            Image.alpha_composite(review_background, scene_image).convert("RGB").save(stills / f"scene_{idx:02d}.png")
            segment = work / f"scene_{idx:02d}.mp4"
            offset = round((idx * 1.9 + 0.8) % 7.0, 6)
            filt = (
                f"[0:v]trim=start={offset},setpts=PTS-STARTPTS,scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,"
                "fps=24,eq=brightness=-0.36:saturation=0.62,boxblur=2:1[bg];"
                f"[1:v]format=rgba,fade=t=in:st=0:d=0.65:alpha=1,fade=t=out:st={duration - 0.65}:d=0.65:alpha=1[ov];"
                f"[2:v]trim=start={scene_start}:duration={duration},setpts=PTS-STARTPTS,"
                "scale=320:340:force_original_aspect_ratio=increase,crop=320:340,fps=24,"
                f"tpad=stop_mode=clone:stop_duration=1,trim=duration={duration},setpts=PTS-STARTPTS,format=rgba,"
                f"fade=t=in:st=0:d=0.8:alpha=1,fade=t=out:st={duration - 0.8}:d=0.8:alpha=1[face];"
                "[3:v]format=gray,scale=320:340[mask];[face][mask]alphamerge[presenter];"
                "[bg][ov]overlay=0:0:format=auto[base];[base][presenter]overlay=945:350:format=auto"
            )
            run([
                "ffmpeg", "-y", "-v", "error", "-stream_loop", "-1", "-i", str(SOURCES[idx - 1]),
                "-loop", "1", "-i", str(overlay), "-i", str(TALKING_HEAD),
                "-loop", "1", "-i", str(PRESENTER_MASK), "-filter_complex", filt,
                "-t", str(duration), "-an", "-c:v", "libx264", "-preset", "veryfast",
                "-crf", "18", "-pix_fmt", "yuv420p", "-r", "24", str(segment),
            ])
            segments.append(segment)
        visual = work / "visual.mp4"
        inputs = []
        for segment in segments:
            inputs.extend(["-i", str(segment)])
        concat_filter = "".join(f"[{i}:v]" for i in range(6)) + "concat=n=6:v=1:a=0[v]"
        run([
            "ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", concat_filter,
            "-map", "[v]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
            "-pix_fmt", "yuv420p", "-r", "24", str(visual),
        ])
        audio_filter = (
            "[0:v]tpad=stop_mode=clone:stop_duration=0.1,trim=end_frame=1764,setpts=PTS-STARTPTS[v];"
            f"[1:a]loudnorm=I=-16:TP=-1.5:LRA=7,apad,atrim=duration={DURATION}[voice];"
            f"[2:a]volume=.05,afade=t=in:st=0:d=1.5,afade=t=out:st=71.0:d=2.5,atrim=duration={DURATION}[music];"
            "[music][voice]amix=2:duration=longest:normalize=0,alimiter=limit=.92[a]"
        )
        run([
            "ffmpeg", "-y", "-v", "error", "-i", str(visual), "-i", str(DRIVER_AUDIO),
            "-i", str(AMBIENT), "-filter_complex", audio_filter, "-map", "[v]", "-map", "[a]",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-r", "24",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-t", str(DURATION),
            "-movflags", "+faststart", str(OUTPUT),
        ])
    finally:
        shutil.rmtree(work, ignore_errors=True)
    write_srt()
    receipt = {
        "marker": "NEBULAMIND_OVERNIGHT_REPORT_V1_LOCAL_MASTER_BUILT",
        "output": str(OUTPUT), "srt": str(SRT), "stills": str(stills),
        "talking_head": str(TALKING_HEAD), "driver_audio": str(DRIVER_AUDIO),
        "probe": probe(OUTPUT), "source_contract": SOURCE_CONTRACT,
        "frame_contract": {"fps": FPS, "boundaries": SCENE_FRAMES, "total": 1764},
        "topic_map_visual_note": "uniform 57-node count grid; no invented UMAP geometry or proportional inflow bars",
    }
    (BASE / "build_receipt.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False))


if __name__ == "__main__":
    main()
