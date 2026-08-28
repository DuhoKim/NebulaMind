#!/usr/bin/env python3
"""Fresh candidate midpoints plus 360p JPEG 4:2:0 recompression variants."""

from __future__ import annotations

import hashlib
import io
import json
import platform
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import PIL
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = Path("/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4")
EXPECTED_SHA = "02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431"
PASS16 = ROOT / "qa/pass16_minimum_scale_geometry_audit"
OUT = ROOT / "qa/pass17_minimum_scale_recompression_audit"
EXPECTED_CUTS = [12.133333, 26.366667, 47.266667, 60.466667, 74.666667, 88.066667, 102.333333, 116.333333, 131.033333, 148.033333, 162.033333, 179.733333, 196.8, 213.433333, 233.866667]
OUTPUT_SIZE = (640, 360)
VARIANTS: dict[str, int | None] = {
    "clean": None,
    "downscale_360p": None,
    "jpeg_q60_420_360p": 60,
    "jpeg_q35_420_360p": 35,
    "jpeg_q20_420_360p": 20,
}


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def detect_cuts() -> tuple[list[float], dict[str, object]]:
    command = [
        "ffmpeg", "-hide_banner", "-loglevel", "info", "-i", str(CANDIDATE),
        "-vf", "scale=160:90,format=gray,select='gt(scene,0.03)',showinfo",
        "-an", "-f", "null", "-",
    ]
    proc = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cuts = []
    for line in proc.stderr.splitlines():
        marker = "pts_time:"
        if marker in line:
            cuts.append(round(float(line.split(marker, 1)[1].split()[0]), 6))
    return cuts, {
        "detector": "ffmpeg 160x90 grayscale scene-score threshold strictly greater than 0.03 with showinfo",
        "threshold": 0.03,
        "cuts": cuts,
    }


def decode(time_s: float, output: Path) -> None:
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{time_s:.6f}",
        "-i", str(CANDIDATE), "-frames:v", "1", "-pix_fmt", "rgb24", str(output),
    ], check=True)


def downscale(image: Image.Image) -> Image.Image:
    return image.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)


def recompress(image_360p: Image.Image, quality: int) -> tuple[Image.Image, str, int]:
    encoded = io.BytesIO()
    image_360p.save(
        encoded,
        format="JPEG",
        quality=quality,
        subsampling=2,
        optimize=False,
        progressive=False,
    )
    jpeg_bytes = encoded.getvalue()
    with Image.open(io.BytesIO(jpeg_bytes)) as decoded:
        output = decoded.convert("RGB")
    return output, hashlib.sha256(jpeg_bytes).hexdigest(), len(jpeg_bytes)


def make_sheet(paths: list[Path], output: Path, label: str) -> tuple[int, int]:
    thumb = (448, 252)
    margin, label_h = 20, 42
    sheet = Image.new("RGB", (margin * 5 + thumb[0] * 4, margin * 5 + (thumb[1] + label_h) * 4), (9, 12, 20))
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
    for index, path in enumerate(paths):
        with Image.open(path).convert("RGB") as source:
            image = source.resize(thumb, Image.Resampling.NEAREST if source.size == OUTPUT_SIZE else Image.Resampling.LANCZOS)
        x = margin + (index % 4) * (thumb[0] + margin)
        y = margin + (index // 4) * (thumb[1] + label_h + margin)
        sheet.paste(image, (x, y + label_h))
        draw.text((x, y + 8), f"scene {index + 1:02d} · {label}", fill=(235, 240, 250), font=font)
    sheet.save(output, format="PNG", optimize=False)
    with Image.open(output) as saved:
        return saved.size


def prior_clean_map(receipt: dict[str, object]) -> dict[int, Path]:
    records = receipt["records"]
    if not isinstance(records, list):
        raise TypeError("pass16 records must be a list")
    result: dict[int, Path] = {}
    for record in records:
        if not isinstance(record, dict):
            raise TypeError("pass16 record must be an object")
        samples = record["samples"]
        if not isinstance(samples, list):
            raise TypeError("pass16 samples must be a list")
        sample = next(item for item in samples if isinstance(item, dict) and item.get("variant") == "clean")
        result[int(record["scene"])] = PASS16 / str(sample["frame"])
    return result


def main() -> None:
    if sha(CANDIDATE) != EXPECTED_SHA:
        raise SystemExit("candidate hash mismatch")
    pass16_receipt = json.loads((PASS16 / "extraction_receipt.json").read_text())
    cuts, detector = detect_cuts()
    if cuts != EXPECTED_CUTS or cuts != pass16_receipt["cut_detection"]["cuts"]:
        raise SystemExit(f"cut mismatch: {cuts}")
    if OUT.exists():
        shutil.rmtree(OUT)
    frames = OUT / "frames"
    frames.mkdir(parents=True)
    bounds = [0.0, *cuts, 243.3]
    midpoints = [round((bounds[index] + bounds[index + 1]) / 2, 6) for index in range(16)]
    prior_map = prior_clean_map(pass16_receipt)
    records: list[dict[str, object]] = []
    matches: list[bool] = []
    for scene, time_s in enumerate(midpoints, 1):
        clean = frames / f"scene_{scene:02d}_clean.png"
        decode(time_s, clean)
        with Image.open(clean) as opened:
            image = opened.convert("RGB")
        if image.size != (1920, 1080):
            raise SystemExit(f"scene {scene} dimensions {image.size}")
        prior = prior_map[scene]
        same = sha(clean) == sha(prior)
        matches.append(same)
        if not same:
            raise SystemExit(f"scene {scene} does not reproduce pass16 clean bytes")
        image_360p = downscale(image)
        samples: list[dict[str, object]] = []
        for variant, quality in VARIANTS.items():
            output = frames / f"scene_{scene:02d}_{variant}.png"
            jpeg_hash: str | None = None
            jpeg_size: int | None = None
            if variant == "clean":
                pass
            elif variant == "downscale_360p":
                image_360p.save(output, format="PNG", optimize=False)
            else:
                if quality is None:
                    raise AssertionError("JPEG variant requires quality")
                derived, jpeg_hash, jpeg_size = recompress(image_360p, quality)
                derived.save(output, format="PNG", optimize=False)
            with Image.open(output) as saved:
                width, height, mode = saved.width, saved.height, saved.mode
            samples.append({
                "variant": variant,
                "quality": quality,
                "subsampling": "4:2:0" if quality is not None else None,
                "frame": f"frames/{output.name}",
                "sha256": sha(output),
                "width": width,
                "height": height,
                "mode": mode,
                "jpeg_sha256": jpeg_hash,
                "jpeg_bytes": jpeg_size,
            })
        records.append({
            "scene": scene,
            "sample_time_seconds": time_s,
            "prior_pass16_clean_path": str(prior.relative_to(ROOT)),
            "prior_pass16_clean_sha256": sha(prior),
            "fresh_clean_byte_identical": same,
            "samples": samples,
        })
    sheets: dict[str, dict[str, object]] = {}
    for variant in VARIANTS:
        paths = [frames / f"scene_{scene:02d}_{variant}.png" for scene in range(1, 17)]
        output = OUT / f"contact_sheet_{variant}.png"
        width, height = make_sheet(paths, output, variant)
        sheets[variant] = {"path": output.name, "sha256": sha(output), "width": width, "height": height}
    receipt = {
        "status": "QA_ONLY_NOT_A_CANDIDATE",
        "deepening_pass": 17,
        "created_at": datetime.now(ZoneInfo("Asia/Seoul")).isoformat(),
        "candidate": str(CANDIDATE),
        "candidate_sha256": EXPECTED_SHA,
        "cut_detection": detector,
        "cut_times_seconds": cuts,
        "scene_count": 16,
        "midpoint_times_seconds": midpoints,
        "fresh_clean_match": f"{sum(matches)}/16_BYTE_IDENTICAL_TO_PASS16",
        "variant_order": list(VARIANTS),
        "reference_variant": "downscale_360p",
        "operational_variants": ["downscale_360p", "jpeg_q60_420_360p"],
        "characterization_variants": ["jpeg_q35_420_360p", "jpeg_q20_420_360p"],
        "variant_count": 5,
        "frame_count": 80,
        "records": records,
        "contact_sheets": sheets,
        "implementation": {
            "pillow": PIL.__version__,
            "python": platform.python_version(),
            "downscale_resampler": "Pillow LANCZOS",
            "minimum_scale_output": "640x360 RGB",
            "jpeg_encoder": "Pillow JPEG",
            "jpeg_subsampling": "4:2:0 (subsampling=2)",
            "jpeg_optimize": False,
            "jpeg_progressive": False,
            "jpeg_decode": "Pillow JPEG decode to RGB",
            "storage": "decoded pixels saved as non-optimized RGB PNG",
            "transform_order": "native RGB -> LANCZOS 640x360 -> JPEG 4:2:0 encode -> decode RGB",
        },
        "simulation_limit": "Packet-specific 360p downscale plus JPEG 4:2:0 recompression/decode stress only; quality values are Pillow parameters, not a named codec ladder, display, player, platform, upload route, delivery service, room, viewer, or universal standard.",
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "git_action": False,
    }
    (OUT / "extraction_receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"PASS candidate={EXPECTED_SHA} cuts={len(cuts)} scenes=16 frames=80 variants=5")


if __name__ == "__main__":
    main()
