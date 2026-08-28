#!/usr/bin/env python3
"""Fresh candidate midpoints plus deterministic centered anisotropic-resampling variants."""

from __future__ import annotations

import hashlib
import json
import platform
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
EXPECTED_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
PASS14 = ROOT / "qa/pass14_shadow_floor_audit"
OUT = ROOT / "qa/pass15_geometry_audit"
EXPECTED_CUTS = [12.133333, 26.366667, 47.266667, 60.466667, 74.666667, 88.066667, 102.333333, 116.333333, 131.033333, 148.033333, 162.033333, 179.733333, 196.8, 213.433333, 233.866667]
# variant, x scale, y scale
VARIANTS = [
    ("clean", 1.0, 1.0),
    ("squeeze_x90", 0.90, 1.0),
    ("squeeze_y90", 1.0, 0.90),
    ("squeeze_x80", 0.80, 1.0),
    ("squeeze_y80", 1.0, 0.80),
]


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def detect_cuts() -> tuple[list[float], dict]:
    command = [
        "ffmpeg", "-hide_banner", "-loglevel", "info", "-i", str(CANDIDATE),
        "-vf", "scale=160:90,format=gray,select='gt(scene,0.03)',showinfo",
        "-an", "-f", "null", "-",
    ]
    proc = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cuts: list[float] = []
    for line in proc.stderr.splitlines():
        marker = "pts_time:"
        if marker not in line:
            continue
        token = line.split(marker, 1)[1].split()[0]
        cuts.append(round(float(token), 6))
    return cuts, {
        "detector": "ffmpeg 160x90 grayscale scene-score threshold strictly greater than 0.03 with showinfo",
        "threshold": 0.03,
        "cuts": cuts,
    }


def decode(time_s: float, output: Path) -> None:
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{time_s:.6f}",
        "-i", str(CANDIDATE), "-frames:v", "1", "-pix_fmt", "rgb24", str(output)
    ], check=True)


def squeeze(image: Image.Image, sx: float, sy: float) -> tuple[Image.Image, dict]:
    w, h = image.size
    nw, nh = int(round(w * sx)), int(round(h * sy))
    resized = image.resize((nw, nh), Image.Resampling.LANCZOS)
    out = Image.new("RGB", (w, h), (0, 0, 0))
    x0, y0 = (w - nw) // 2, (h - nh) // 2
    out.paste(resized, (x0, y0))
    return out, {"source_size": [w, h], "resampled_size": [nw, nh], "offset": [x0, y0], "scale_x": sx, "scale_y": sy}


def make_sheet(paths: list[Path], output: Path, label: str) -> None:
    thumb = (448, 252)
    margin, label_h = 20, 42
    sheet = Image.new("RGB", (margin * 5 + thumb[0] * 4, margin * 5 + (thumb[1] + label_h) * 4), (9, 12, 20))
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
    for i, path in enumerate(paths):
        image = Image.open(path).convert("RGB").resize(thumb, Image.Resampling.LANCZOS)
        x = margin + (i % 4) * (thumb[0] + margin)
        y = margin + (i // 4) * (thumb[1] + label_h + margin)
        sheet.paste(image, (x, y + label_h))
        draw.text((x, y + 8), f"scene {i + 1:02d} · {label}", fill=(235, 240, 250), font=font)
    sheet.save(output)


def main() -> None:
    if sha(CANDIDATE) != EXPECTED_SHA:
        raise SystemExit("candidate hash mismatch")
    pass14_receipt = json.loads((PASS14 / "extraction_receipt.json").read_text())
    cuts, detector = detect_cuts()
    if cuts != EXPECTED_CUTS or cuts != pass14_receipt["cut_detection"]["cuts"]:
        raise SystemExit(f"cut mismatch: {cuts}")
    if OUT.exists():
        shutil.rmtree(OUT)
    frames = OUT / "frames"
    frames.mkdir(parents=True)
    bounds = [0.0, *cuts, 243.3]
    midpoints = [round((bounds[i] + bounds[i + 1]) / 2, 6) for i in range(16)]
    records = []
    geometry = {}
    fresh_clean_match = []
    for scene, time_s in enumerate(midpoints, 1):
        clean = frames / f"scene_{scene:02d}_clean.png"
        decode(time_s, clean)
        with Image.open(clean) as im:
            image = im.convert("RGB")
        if image.size != (1920, 1080):
            raise SystemExit(f"scene {scene} dimensions {image.size}")
        prior = PASS14 / "frames/clean" / f"scene_{scene:02d}.png"
        same = sha(clean) == sha(prior)
        fresh_clean_match.append(same)
        if not same:
            raise SystemExit(f"scene {scene} does not reproduce pass14 clean bytes")
        samples = []
        for variant, sx, sy in VARIANTS:
            output = frames / f"scene_{scene:02d}_{variant}.png"
            if variant != "clean":
                derived, geom = squeeze(image, sx, sy)
                derived.save(output)
                geometry[variant] = geom
            samples.append({"variant": variant, "scale_x": sx, "scale_y": sy, "frame": f"frames/{output.name}", "sha256": sha(output), "width": 1920, "height": 1080, "mode": "RGB"})
        records.append({"scene": scene, "sample_time_seconds": time_s, "prior_pass14_clean_sha256": sha(prior), "fresh_clean_byte_identical": same, "samples": samples})
    sheets = {}
    for variant, _, _ in VARIANTS:
        paths = [frames / f"scene_{scene:02d}_{variant}.png" for scene in range(1, 17)]
        output = OUT / f"contact_sheet_{variant}.png"
        make_sheet(paths, output, variant)
        sheets[variant] = {"path": output.name, "sha256": sha(output), "width": 1892, "height": 1276}
    receipt = {
        "status": "QA_ONLY_NOT_A_CANDIDATE",
        "deepening_pass": 15,
        "created_at": datetime.now(ZoneInfo("Asia/Seoul")).isoformat(),
        "candidate": str(CANDIDATE),
        "candidate_sha256": EXPECTED_SHA,
        "cut_detection": detector,
        "cut_times_seconds": cuts,
        "scene_count": 16,
        "midpoint_times_seconds": midpoints,
        "fresh_clean_match": f"{sum(fresh_clean_match)}/16_BYTE_IDENTICAL_TO_PASS14",
        "variants": [x[0] for x in VARIANTS],
        "operational_variants": ["squeeze_x90", "squeeze_y90"],
        "characterization_variants": ["squeeze_x80", "squeeze_y80"],
        "geometry": geometry,
        "variant_count": 5,
        "frame_count": 80,
        "records": records,
        "contact_sheets": sheets,
        "implementation": {"pillow": Image.__version__, "python": platform.python_version(), "resampler": "Pillow LANCZOS", "padding": "centered black RGB"},
        "simulation_limit": "Packet-specific anisotropic resampling only; not a named display, player, projector, codec, browser, delivery platform, or pixel-aspect standard.",
        "tts_invoked": False, "audio_generated": False, "video_encoded": False, "git_action": False,
    }
    (OUT / "extraction_receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"PASS candidate={EXPECTED_SHA} cuts={len(cuts)} scenes=16 frames=80 variants=5")


if __name__ == "__main__":
    main()
