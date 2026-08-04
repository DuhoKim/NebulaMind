#!/usr/bin/env python3
"""Build five evidence-bounded NebulaMind paper explainers."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import math
import random
import re
import subprocess
import time

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

BASE = Path(__file__).resolve().parent
SPEC_PATH = BASE / "paper_video_specs.json"
FREEZE_PATH = BASE / "source_freeze.json"
OUT_ROOT = BASE / "videos"
BUILD_ROOT = BASE / "build"
BATCH_RECEIPT = BASE / "batch_build_receipt.json"
BATCH_SHEET = BASE / "FIVE_PAPER_VIDEO_BATCH_SHEET.png"
PORTRAIT = Path(
    "/Users/duhokim/HermesOps/scripts/clips/subnav_flow_lipsync_v7/"
    "canary/flow_master_shoulder_crop_768x1024.png"
)
EDGE_TTS = Path("/Users/duhokim/.hermes/hermes-agent/venv/bin/edge-tts")
FONT_PATH = Path("/System/Library/Fonts/SFNSMono.ttf")
ITALIC_FONT_PATH = Path("/System/Library/Fonts/SFNSMonoItalic.ttf")

W, H, FPS = 1280, 720, 30
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
PANEL_2 = "#142544"
OUTLINE = "#29466E"
TONE = {"cyan": CYAN, "magenta": MAGENTA, "green": GREEN, "yellow": YELLOW, "red": RED}


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


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def probe_duration(path: Path) -> float:
    return float(capture(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nk=1:nw=1", str(path)]))


def verify_source_freeze() -> None:
    freeze = json.loads(FREEZE_PATH.read_text())
    failures: list[str] = []
    for row in freeze["sources"]:
        p = Path(row["path"])
        if not p.is_file():
            failures.append(f"missing: {p}")
        elif sha256(p) != row["sha256"]:
            failures.append(f"hash drift: {p}")
    if failures:
        raise RuntimeError("SOURCE FREEZE DRIFT\n" + "\n".join(failures))


def color(v: str) -> tuple[int, int, int]:
    v = v.lstrip("#")
    return int(v[:2], 16), int(v[2:4], 16), int(v[4:6], 16)


def rgba(v: str, alpha: int = 255) -> tuple[int, int, int, int]:
    return (*color(v), alpha)


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


def draw_wrapped(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.FreeTypeFont,
                 fill: str, max_width: int, *, line_gap: int = 6, max_lines: int | None = None,
                 fail_on_overflow: bool = False) -> int:
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


def gradient_background(seed: int) -> Image.Image:
    top, bottom = color(BG_TOP), color(BG_BOTTOM)
    image = Image.new("RGB", (W, H), top)
    draw = ImageDraw.Draw(image)
    for y in range(H):
        t = y / (H - 1)
        draw.line((0, y, W, y), fill=tuple(round(top[i] * (1 - t) + bottom[i] * t) for i in range(3)))
    rng = random.Random(22072026 + seed)
    for _ in range(85):
        x, y = rng.randrange(W), rng.randrange(590)
        r = rng.choice((1, 1, 1, 2, 2, 3))
        draw.ellipse((x-r, y-r, x+r, y+r), fill=color(rng.choice((CYAN, MAGENTA, BODY, MUTED))))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-200, 70, 460, 730), fill=rgba(MAGENTA, 22))
    gd.ellipse((820, -180, 1490, 510), fill=rgba(CYAN, 24))
    return Image.alpha_composite(image.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(95)))


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], *, outline: str = OUTLINE,
          fill: str = PANEL, width: int = 2, radius: int = 20) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=rgba(fill, 242), outline=outline, width=width)


def paste_portrait(image: Image.Image, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    size = (x1 - x0, y1 - y0)
    p = Image.open(PORTRAIT).convert("RGB")
    p = ImageOps.fit(p, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.46))
    p = ImageEnhance.Color(p).enhance(0.92).convert("RGBA")
    mask = Image.new("L", size, 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((26, 20, size[0]-26, size[1]-20), radius=52, fill=244)
    p.putalpha(mask.filter(ImageFilter.GaussianBlur(24)))
    image.alpha_composite(p, (x0, y0))


def header(draw: ImageDraw.ImageDraw, paper: dict, index: int, scene: dict) -> int:
    draw.text((64, 26), "NebulaMind", font=font(22), fill=BODY)
    draw.text((220, 28), "PAPER EXPLAINER", font=font(16), fill=CYAN)
    draw.text((1034, 30), f"{index:02d} / 06", font=font(15), fill=MUTED)
    draw.line((64, 64, 1216, 64), fill=OUTLINE, width=1)
    draw.text((64, 84), scene["kicker"], font=font(15), fill=CYAN)
    lines = wrap_text(draw, scene["title"], font(31), 1120)
    if len(lines) > 2:
        raise RuntimeError(f"scene title overflow: {scene['title']}")
    y = 112
    for line in lines:
        draw.text((64, y), line, font=font(31), fill=BODY)
        y += 40
    return max(190, y + 8)


def caption_panel(draw: ImageDraw.ImageDraw, text: str) -> None:
    panel(draw, (52, 604, 1228, 704), outline=OUTLINE, fill="#07101F", width=1, radius=18)
    draw.text((74, 621), "NARRATION", font=font(13), fill=CYAN)
    lines = wrap_text(draw, text, font(14), 1040)
    if len(lines) > 3:
        raise RuntimeError(f"burned narration exceeds 3 lines: {text}")
    y = 620
    for line in lines:
        draw.text((168, y), line, font=font(14), fill=BODY)
        y += 24


def render_open(paper: dict, seed: int) -> Image.Image:
    image = gradient_background(seed)
    paste_portrait(image, (758, 62, 1196, 652))
    d = ImageDraw.Draw(image)
    d.text((64, 42), "NebulaMind", font=font(23), fill=BODY)
    d.text((64, 132), paper["track"], font=font(16), fill=CYAN)
    lines = wrap_text(d, paper["short_title"], font(37), 620)
    if len(lines) > 4:
        raise RuntimeError(f"open title overflow: {paper['short_title']}")
    y = 180
    for line in lines:
        d.text((64, y), line, font=font(37), fill=BODY)
        y += 50
    d.line((64, min(430, y+10), 620, min(430, y+10)), fill=CYAN, width=3)
    panel(d, (64, 500, 625, 570), fill="#0B1630", width=1, radius=17)
    d.text((90, 520), "Silent guide portrait · narration begins next", font=font(14), fill=MUTED)
    d.text((64, 630), "NebulaMind Lab · autonomous run", font=font(14), fill=MUTED)
    return image


def paste_pdf_page(image: Image.Image, page_path: Path, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    source = Image.open(page_path).convert("RGBA")
    white = Image.new("RGBA", source.size, (255, 255, 255, 255))
    white.alpha_composite(source)
    page = white.convert("RGB")
    page.thumbnail((x1-x0-24, y1-y0-24), Image.Resampling.LANCZOS)
    shadow = Image.new("RGBA", (page.width+30, page.height+30), (0,0,0,0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((12,12,page.width+18,page.height+18), radius=10, fill=(0,0,0,150))
    shadow = shadow.filter(ImageFilter.GaussianBlur(8))
    image.alpha_composite(shadow, (x0+(x1-x0-shadow.width)//2, y0+(y1-y0-shadow.height)//2))
    px = x0 + (x1-x0-page.width)//2
    py = y0 + (y1-y0-page.height)//2
    image.paste(page, (px, py))


def render_scene(paper: dict, index: int, scene: dict, seed: int) -> Image.Image:
    image = gradient_background(seed)
    d = ImageDraw.Draw(image)
    body_y = header(d, paper, index, scene)
    cards = scene["cards"]
    if len(cards) != 3:
        raise RuntimeError(f"{paper['key']} scene {index}: expected 3 cards")
    if index == 1:
        page_path = BASE / paper["first_page_path"]
        panel(d, (64, body_y, 402, 574), outline=CYAN, fill="#111B2B")
        paste_pdf_page(image, page_path, (72, body_y+8, 394, 566))
        d = ImageDraw.Draw(image)
        for i, card in enumerate(cards):
            y0 = body_y + i * 105
            accent = TONE[card["tone"]]
            panel(d, (438, y0, 1216, y0+88), outline=accent)
            d.text((462, y0+12), card["value"], font=font(25), fill=BODY)
            d.text((790, y0+19), card["label"], font=font(14), fill=accent)
        panel(d, (438, body_y+315, 1216, 574), outline=OUTLINE, fill="#0D1A31", width=1)
        d.text((462, body_y+327), "WHY IT MATTERS", font=font(12), fill=CYAN)
        draw_wrapped(d, (462, body_y+350), scene["callout"], font(14), BODY, 720, line_gap=4, max_lines=2, fail_on_overflow=True)
    else:
        x_positions = (64, 452, 840)
        for x0, card in zip(x_positions, cards):
            accent = TONE[card["tone"]]
            panel(d, (x0, body_y+12, x0+352, body_y+172), outline=accent)
            value_lines = wrap_text(d, card["value"], font(27), 312)
            if len(value_lines) > 2:
                raise RuntimeError(f"card value overflow: {card['value']}")
            y = body_y+32
            for line in value_lines:
                d.text((x0+20, y), line, font=font(27), fill=BODY)
                y += 34
            draw_wrapped(d, (x0+20, body_y+112), card["label"], font(14), accent, 310, max_lines=2, fail_on_overflow=True)
        panel(d, (64, body_y+210, 1216, 574), outline=OUTLINE, fill="#0D1A31", width=1)
        d.text((92, body_y+238), "INTERPRETATION", font=font(14), fill=CYAN)
        draw_wrapped(d, (92, body_y+286), scene["callout"], font(23), BODY, 1080, line_gap=10, max_lines=4, fail_on_overflow=True)
        d.line((92, body_y+382, 1188, body_y+382), fill=OUTLINE, width=1)
        d.text((92, body_y+413), paper["track"], font=font(14), fill=MUTED)
    caption_panel(d, scene["narration"])
    return image


def render_close(paper: dict, seed: int) -> Image.Image:
    image = gradient_background(seed)
    paste_portrait(image, (68, 64, 508, 654))
    d = ImageDraw.Draw(image)
    d.text((600, 130), "READ THE PAPER.", font=font(34), fill=CYAN)
    d.text((600, 184), "KEEP THE CAVEAT.", font=font(34), fill=YELLOW)
    d.line((600, 245, 1180, 245), fill=CYAN, width=3)
    lines = wrap_text(d, paper["short_title"], font(24), 575)
    y = 292
    for line in lines[:4]:
        d.text((600, y), line, font=font(24), fill=BODY)
        y += 36
    panel(d, (600, 465, 1180, 570), outline=RED, fill="#241822")
    d.text((625, 488), "DESCRIPTIVE · NOT VALIDATED", font=font(17), fill=YELLOW)
    d.text((625, 527), "Human and journal review remain separate", font=font(13), fill=MUTED)
    d.text((600, 625), "NebulaMind Lab · autonomous run", font=font(14), fill=MUTED)
    return image


def sentence_chunks(text: str) -> list[str]:
    chunks = [x.strip() for x in re.split(r"(?<=[.!?])\s+", text.strip()) if x.strip()]
    return chunks or [text.strip()]


def srt_time(seconds: float) -> str:
    ms = round(seconds * 1000)
    hours, ms = divmod(ms, 3_600_000)
    minutes, ms = divmod(ms, 60_000)
    secs, ms = divmod(ms, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"


def write_srt(paper: dict, out: Path, intro: float, durations: list[float], outro: float) -> None:
    cursor = intro
    cue = 1
    blocks: list[str] = []
    for scene, duration in zip(paper["scenes"], durations):
        start, end = cursor + 0.35, cursor + duration - 0.20
        chunks = sentence_chunks(scene["narration"])
        weights = [len(x.split()) for x in chunks]
        total = sum(weights)
        local = start
        for chunk, weight in zip(chunks, weights):
            chunk_end = local + (end-start)*weight/total
            blocks.append(f"{cue}\n{srt_time(local)} --> {srt_time(chunk_end)}\n{chunk}\n")
            cue += 1
            local = chunk_end
        cursor += duration
    out.write_text("\n".join(blocks), encoding="utf-8")


def synthesize(text: str, raw: Path, voice: str, rate_percent: int) -> tuple[float, str]:
    rate = f"{rate_percent:+d}%"
    if raw.is_file() and raw.stat().st_size > 0:
        return probe_duration(raw), rate
    run([str(EDGE_TTS), "--voice", voice, f"--rate={rate}", "--text", text, "--write-media", str(raw)], retries=2)
    return probe_duration(raw), rate


def render_audio_segment(text: str, duration: float, out: Path, raw_dir: Path, index: int, voice: str) -> dict:
    if not text:
        run(["ffmpeg","-y","-v","error","-f","lavfi","-t",f"{duration:.6f}","-i","anullsrc=r=48000:cl=mono","-ac","1","-ar","48000","-c:a","pcm_s16le",str(out)])
        return {"segment": index, "duration": duration, "silence": True, "output": str(out)}
    speech_start, end_pad = 0.35, 0.20
    target = duration - speech_start - end_pad
    initial = 20
    text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()[:10]
    raw = raw_dir / f"segment_{index:02d}_{text_hash}_rate_{initial:+d}.mp3"
    raw_duration, used_rate = synthesize(text, raw, voice, initial)
    tempo = raw_duration / target
    if not 0.90 <= tempo <= 1.10:
        derived = max(-20, min(70, round((tempo * (1 + initial/100) - 1) * 100)))
        raw = raw_dir / f"segment_{index:02d}_{text_hash}_rate_{derived:+d}.mp3"
        raw_duration, used_rate = synthesize(text, raw, voice, derived)
        tempo = raw_duration / target
    if tempo < 0.85:
        tempo = 1.0
    if tempo > 1.15:
        raise RuntimeError(f"audio segment {index}: atempo {tempo:.3f} outside natural range")
    graph = (f"[1:a]aformat=sample_rates=48000:channel_layouts=mono,atempo={tempo:.8f},"
             f"adelay={round(speech_start*1000)}:all=1[voice];[0:a][voice]"
             "amix=inputs=2:duration=first:normalize=0,alimiter=limit=.95[out]")
    run(["ffmpeg","-y","-v","error","-f","lavfi","-t",f"{duration:.6f}","-i","anullsrc=r=48000:cl=mono","-i",str(raw),"-filter_complex",graph,"-map","[out]","-ac","1","-ar","48000","-t",f"{duration:.6f}","-c:a","pcm_s16le",str(out)])
    speech_duration = raw_duration / tempo
    return {"segment": index, "duration": duration, "text": text, "voice": voice, "voice_gender": "Female", "synthesis_rate": used_rate, "raw_duration": round(raw_duration,6), "atempo": round(tempo,6), "actual_speech_duration": round(speech_duration,6), "trailing_room": round(duration-speech_start-speech_duration,6), "output": str(out)}


def concatenate_audio(rows: list[dict], out: Path) -> None:
    args: list[str] = []
    pads: list[str] = []
    for i, row in enumerate(rows):
        args += ["-i", row["output"]]
        pads.append(f"[{i}:a]")
    run(["ffmpeg","-y","-v","error",*args,"-filter_complex","".join(pads)+f"concat=n={len(rows)}:v=0:a=1[a]","-map","[a]","-ac","1","-ar","48000","-c:a","pcm_s16le",str(out)])


def render_video_segments(images: list[Path], durations: list[float], out_dir: Path) -> list[Path]:
    outputs: list[Path] = []
    for i, (image, duration) in enumerate(zip(images, durations)):
        out = out_dir / f"segment_{i:02d}.mp4"
        phase = i * 0.71
        vf = ("scale=1344:756:flags=lanczos," f"crop=1280:720:x='(iw-ow)/2+10*sin(t/5+{phase:.3f})':" f"y='(ih-oh)/2+5*cos(t/6+{phase:.3f})'," f"fade=t=in:st=0:d=0.30,fade=t=out:st={duration-0.30:.3f}:d=0.30,format=yuv420p")
        run(["ffmpeg","-y","-v","error","-loop","1","-framerate",str(FPS),"-i",str(image),"-t",f"{duration:.6f}","-vf",vf,"-an","-r",str(FPS),"-c:v","libx264","-preset","fast","-crf","19","-profile:v","high","-pix_fmt","yuv420p","-g",str(FPS*2),str(out)])
        outputs.append(out)
    return outputs


def concatenate_video(paths: list[Path], out: Path) -> None:
    args: list[str] = []
    pads: list[str] = []
    for i, p in enumerate(paths):
        args += ["-i", str(p)]
        pads.append(f"[{i}:v]")
    run(["ffmpeg","-y","-v","error",*args,"-filter_complex","".join(pads)+f"concat=n={len(paths)}:v=1:a=0[v]","-map","[v]","-an","-r",str(FPS),"-c:v","libx264","-preset","fast","-crf","19","-profile:v","high","-pix_fmt","yuv420p","-g",str(FPS*2),str(out)])


def make_sheet(images: list[Path], out: Path) -> None:
    sheet = Image.new("RGB", (1280, 360), color(BG_TOP))
    d = ImageDraw.Draw(sheet)
    for i, p in enumerate(images):
        thumb = Image.open(p).convert("RGB").resize((320,180), Image.Resampling.LANCZOS)
        x, y = (i%4)*320, (i//4)*180
        sheet.paste(thumb,(x,y)); d.rectangle((x,y,x+319,y+179),outline=color(OUTLINE),width=2)
    sheet.save(out)


def validate_spec(spec: dict) -> None:
    if len(spec["papers"]) != 5 or len(spec["narrated_scene_seconds"]) != 6:
        raise RuntimeError("spec must contain five papers and six narrated durations")
    keys, titles = set(), set()
    boundary = spec["status_boundary"]
    for p in spec["papers"]:
        if p["key"] in keys or p["youtube_title"] in titles:
            raise RuntimeError("duplicate paper key or YouTube title")
        keys.add(p["key"]); titles.add(p["youtube_title"])
        if len(p["youtube_title"]) > 100 or len(p["description"]) > 5000:
            raise RuntimeError(f"metadata length overflow: {p['key']}")
        if len(p["scenes"]) != 6:
            raise RuntimeError(f"{p['key']}: expected six scenes")
        if "not validated" not in p["description"].lower() or "journal or human peer review" not in p["description"].lower():
            raise RuntimeError(f"{p['key']}: missing public status boundary")
        if not (BASE/p["pdf_path"]).is_file() or not (BASE/p["first_page_path"]).is_file():
            raise RuntimeError(f"{p['key']}: missing frozen PDF or title page")
        for scene in p["scenes"]:
            if not scene["narration"].strip() or len(scene["cards"]) != 3:
                raise RuntimeError(f"{p['key']}: incomplete scene")
    if not boundary:
        raise RuntimeError("missing batch status boundary")


def build_paper(spec: dict, paper: dict, paper_index: int) -> dict:
    verify_source_freeze()
    key = paper["key"]
    out_dir = OUT_ROOT/key
    work = BUILD_ROOT/key
    scene_dir, audio_dir, raw_dir, video_dir = work/"scenes", work/"audio", work/"raw", work/"video"
    for d in (out_dir,scene_dir,audio_dir,raw_dir,video_dir): d.mkdir(parents=True,exist_ok=True)
    intro, outro = float(spec["intro_seconds"]), float(spec["outro_seconds"])
    narrated = [float(x) for x in spec["narrated_scene_seconds"]]
    durations = [intro,*narrated,outro]
    images: list[Path] = []
    rendered = [render_open(paper,paper_index*100)]
    rendered += [render_scene(paper,i,s,paper_index*100+i) for i,s in enumerate(paper["scenes"],1)]
    rendered += [render_close(paper,paper_index*100+7)]
    for i,img in enumerate(rendered):
        p=scene_dir/f"scene_{i:02d}.png"; img.convert("RGB").save(p,quality=95); images.append(p)
    sheet=out_dir/f"{key}_SCENE_SHEET.png"; make_sheet(images,sheet)
    srt=out_dir/f"NEBULAMIND_PAPER_{key.upper().replace('-','_')}_V1.srt"; write_srt(paper,srt,intro,narrated,outro)
    audio_rows=[]
    texts=[""]+[x["narration"] for x in paper["scenes"]]+[""]
    for i,(text,duration) in enumerate(zip(texts,durations)):
        audio_rows.append(render_audio_segment(text,duration,audio_dir/f"segment_{i:02d}.wav",raw_dir,i,spec["voice"]))
    narration=out_dir/f"{key}_female_narration.wav"; concatenate_audio(audio_rows,narration)
    scene_videos=render_video_segments(images,durations,video_dir)
    silent=work/"silent_master.mp4"; concatenate_video(scene_videos,silent)
    verify_source_freeze()
    expected=sum(durations)
    final=out_dir/f"NEBULAMIND_PAPER_{key.upper().replace('-','_')}_V1.mp4"
    af=f"loudnorm=I=-16:LRA=7:TP=-1.5,apad=pad_dur={expected:.6f},atrim=duration={expected:.6f}"
    run(["ffmpeg","-y","-v","error","-i",str(silent),"-i",str(narration),"-map","0:v:0","-map","1:a:0","-af",af,"-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2","-movflags","+faststart","-metadata",f"title={paper['youtube_title']}","-metadata","comment=Machine-generated descriptive explainer; not validated","-t",f"{expected:.6f}",str(final)])
    observed=probe_duration(final)
    if abs(observed-expected)>0.08: raise RuntimeError(f"{key}: duration {observed} != {expected}")
    checkpoint=out_dir/"publication_checkpoint.json"
    checkpoint_data = json.loads(checkpoint.read_text()) if checkpoint.exists() else {}
    if checkpoint_data.get("video_id"):
        raise RuntimeError(f"{key}: refusing to rebuild a checkpoint that already owns YouTube ID {checkpoint_data['video_id']}")
    checkpoint_data.update({"key":key,"source_sha256":sha256(final),"caption_sha256":sha256(srt),"title":paper["youtube_title"],"description":paper["description"],"video_id":"","url":"","caption_id":"","privacy":"local","processing":"not_uploaded","status":"LOCAL_QA_PENDING","uploaded_at":"","published_at":""})
    checkpoint.write_text(json.dumps(checkpoint_data,indent=2,ensure_ascii=False)+"\n")
    receipt={"marker":"NEBULAMIND_PAPER_VIDEO_BUILD_COMPLETE_V1","completed_at_utc":datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),"key":key,"source_freeze_verified_before_build":True,"source_freeze_verified_before_final_mux":True,"spec_sha256":sha256(SPEC_PATH),"source_pdf":str(BASE/paper["pdf_path"]),"source_pdf_sha256":sha256(BASE/paper["pdf_path"]),"youtube_title":paper["youtube_title"],"description":paper["description"],"voice":spec["voice"],"voice_gender":"Female","presenter_policy":"approved synthetic Flow portrait appears only during silent opening/outro; no visible narration or false lip-sync","music":"none","expected_duration":expected,"observed_duration":observed,"artifact":str(final),"artifact_sha256":sha256(final),"artifact_bytes":final.stat().st_size,"srt":str(srt),"srt_sha256":sha256(srt),"narration":str(narration),"narration_sha256":sha256(narration),"contact_sheet":str(sheet),"contact_sheet_sha256":sha256(sheet),"segments":audio_rows,"publication_state":"local QA pending; not uploaded or published"}
    (out_dir/"build_receipt.json").write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+"\n")
    return receipt


def make_batch_sheet(receipts: list[dict]) -> None:
    sheet=Image.new("RGB",(1280,1080),color(BG_TOP)); d=ImageDraw.Draw(sheet)
    for i,r in enumerate(receipts):
        thumb=Image.open(r["contact_sheet"]).convert("RGB").resize((640,180),Image.Resampling.LANCZOS)
        x=(i%2)*640; y=(i//2)*360
        sheet.paste(thumb,(x,y)); d.rectangle((x,y,x+639,y+179),outline=color(OUTLINE),width=2)
        d.text((x+18,y+200),r["key"],font=font(17),fill=CYAN)
        d.text((x+18,y+232),"74s · Female Emma · descriptive, not validated",font=font(13),fill=MUTED)
    sheet.save(BATCH_SHEET)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--keys", nargs="*", help="rebuild only these paper keys while preserving verified sibling receipts")
    args = parser.parse_args()
    for p in (PORTRAIT,EDGE_TTS,FONT_PATH,ITALIC_FONT_PATH,SPEC_PATH,FREEZE_PATH):
        if not p.is_file(): raise FileNotFoundError(p)
    verify_source_freeze()
    spec=json.loads(SPEC_PATH.read_text()); validate_spec(spec)
    selected = set(args.keys or [])
    known = {paper["key"] for paper in spec["papers"]}
    if selected - known:
        raise RuntimeError(f"unknown paper keys: {sorted(selected-known)}")
    receipts=[]
    for i,paper in enumerate(spec["papers"],1):
        key = paper["key"]
        if selected and key not in selected:
            receipt_path = OUT_ROOT/key/"build_receipt.json"
            if not receipt_path.is_file():
                raise RuntimeError(f"{key}: no existing receipt for partial rebuild")
            receipt = json.loads(receipt_path.read_text())
            artifact = Path(receipt["artifact"])
            if not artifact.is_file() or sha256(artifact) != receipt["artifact_sha256"]:
                raise RuntimeError(f"{key}: existing sibling artifact drift")
            receipts.append(receipt)
            continue
        print(f"BUILD {i}/5 {key}",flush=True)
        receipts.append(build_paper(spec,paper,i))
    make_batch_sheet(receipts)
    batch={"marker":"NEBULAMIND_FIVE_PAPER_VIDEO_BATCH_BUILD_COMPLETE_V1","completed_at_utc":datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),"source_freeze_verified":True,"spec":str(SPEC_PATH),"spec_sha256":sha256(SPEC_PATH),"voice":spec["voice"],"voice_gender":"Female","paper_count":len(receipts),"batch_sheet":str(BATCH_SHEET),"batch_sheet_sha256":sha256(BATCH_SHEET),"artifacts":[{"key":r["key"],"path":r["artifact"],"sha256":r["artifact_sha256"],"bytes":r["artifact_bytes"],"srt":r["srt"],"srt_sha256":r["srt_sha256"],"title":r["youtube_title"]} for r in receipts],"publication_state":"local QA pending; nothing uploaded or published"}
    BATCH_RECEIPT.write_text(json.dumps(batch,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps(batch,indent=2,ensure_ascii=False))


if __name__ == "__main__":
    main()
