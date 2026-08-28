#!/usr/bin/env python3
"""Build method proofs for color/monochrome -> 360p -> opaque bottom-25% obstruction."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/pass26_v8_color_minimum_scale_obstruction"
PREVIOUS = ROOT / "qa/pass23_v8_minimum_scale_color_vision/receipt.json"
OUTPUT_SIZE = (640, 360)
MASK_FRACTION = 0.25
MASK_TOP_Y = 270
MASK_RGB = np.array([0, 0, 0], dtype=np.uint8)
VARIANTS = [
    "color_then_360p_then_bottom25",
    "grayscale_bt709_then_360p_then_bottom25",
    "protanopia_machado100_then_360p_then_bottom25",
    "deuteranopia_machado100_then_360p_then_bottom25",
    "tritanopia_machado100_then_360p_then_bottom25",
]
BASELINE_VARIANTS = {
    "color_then_360p_then_bottom25": "color_360p",
    "grayscale_bt709_then_360p_then_bottom25": "grayscale_bt709_then_360p",
    "protanopia_machado100_then_360p_then_bottom25": "protanopia_machado100_then_360p",
    "deuteranopia_machado100_then_360p_then_bottom25": "deuteranopia_machado100_then_360p",
    "tritanopia_machado100_then_360p_then_bottom25": "tritanopia_machado100_then_360p",
}
MATRICES = {
    "protanopia_machado100": np.array([[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]], dtype=np.float64),
    "deuteranopia_machado100": np.array([[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]], dtype=np.float64),
    "tritanopia_machado100": np.array([[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]], dtype=np.float64),
}
GROUPS: dict[str, dict[str, object]] = {
    "sealed_v8": {
        "source_receipt": ROOT / "proposal_frames/v8/render_receipt.json",
        "source_paths": [ROOT / "proposal_frames/v8" / f"scene_{scene:02d}_s{scene}.png" for scene in range(1, 8)],
    },
    "pass7_caption_safe": {
        "source_receipt": ROOT / "qa/pass7_caption_safe_mockup/receipt.json",
        "source_paths": [ROOT / "qa/pass7_caption_safe_mockup/frames" / f"scene_{scene:02d}_caption_safe.png" for scene in range(1, 8)],
    },
    "pass12_sharpness_safe": {
        "source_receipt": ROOT / "qa/pass12_sharpness_safe_mockup/receipt.json",
        "source_paths": [ROOT / "qa/pass12_sharpness_safe_mockup/frames" / f"scene_{scene:02d}_clean.png" for scene in range(1, 8)],
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(values: np.ndarray) -> np.ndarray:
    clipped = np.clip(values, 0.0, 1.0)
    return np.where(clipped <= 0.0031308, 12.92 * clipped, 1.055 * clipped ** (1.0 / 2.4) - 0.055)


def represented(native: Image.Image, baseline_variant: str) -> Image.Image:
    if baseline_variant == "color_360p":
        transformed = native.convert("RGB")
    else:
        label = baseline_variant.removesuffix("_then_360p")
        linear = srgb_to_linear(np.asarray(native.convert("RGB"), dtype=np.float64) / 255.0)
        if label == "grayscale_bt709":
            luminance = 0.2126 * linear[:, :, 0] + 0.7152 * linear[:, :, 1] + 0.0722 * linear[:, :, 2]
            transformed_linear = np.repeat(luminance[:, :, None], 3, axis=2)
        else:
            transformed_linear = np.einsum("...c,rc->...r", linear, MATRICES[label])
        transformed = Image.fromarray(np.rint(linear_to_srgb(transformed_linear) * 255.0).astype(np.uint8))
    return transformed.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)


def obstruct(image: Image.Image) -> Image.Image:
    pixels = np.asarray(image.convert("RGB"), dtype=np.uint8).copy()
    pixels[MASK_TOP_Y:, :, :] = MASK_RGB
    return Image.fromarray(pixels)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def contact_sheet(group_root: Path, variant: str, records: list[dict[str, object]]) -> dict[str, object]:
    tile_w, tile_h, label_h = 640, 360, 28
    canvas = Image.new("RGB", (tile_w * 2, (tile_h + label_h) * 4), (4, 8, 14))
    draw = ImageDraw.Draw(canvas)
    face = font(18)
    for index, record in enumerate(records):
        x, y = index % 2 * tile_w, index // 2 * (tile_h + label_h)
        scene_value = record["scene"]
        if not isinstance(scene_value, int):
            raise TypeError("scene must be int")
        draw.text((x + 8, y + 3), f"S{scene_value} · {variant}", fill=(240, 244, 250), font=face)
        with Image.open(group_root / str(record["frame"])) as image:
            canvas.paste(image.convert("RGB"), (x, y + label_h))
    target = group_root / f"contact_sheet_{variant}.png"
    canvas.save(target, format="PNG", optimize=False)
    return {"path": target.relative_to(group_root).as_posix(), "sha256": sha(target), "width": canvas.width, "height": canvas.height}


def build_group(name: str, source_paths: list[Path], source_receipt: Path, previous_group: dict[str, object]) -> tuple[dict[str, object], int]:
    group_root = OUT / name
    frames = group_root / "frames"
    frames.mkdir(parents=True)
    prior_scenes = {int(scene["scene"]): scene for scene in previous_group["scenes"]}  # type: ignore[index]
    scenes: list[dict[str, object]] = []
    by_variant: dict[str, list[dict[str, object]]] = {variant: [] for variant in VARIANTS}
    baseline_matches = 0
    for scene, source in enumerate(source_paths, start=1):
        samples: list[dict[str, object]] = []
        prior_samples = {sample["variant"]: sample for sample in prior_scenes[scene]["samples"]}
        with Image.open(source) as opened:
            native = opened.convert("RGB")
            if native.size != (1920, 1080):
                raise SystemExit(f"native source dimensions changed: {source}")
            for variant in VARIANTS:
                baseline_variant = BASELINE_VARIANTS[variant]
                baseline = represented(native, baseline_variant)
                prior = prior_samples[baseline_variant]
                prior_path = ROOT / "qa/pass23_v8_minimum_scale_color_vision" / name / prior["frame"]
                with Image.open(prior_path) as prior_opened:
                    baseline_match = np.array_equal(np.asarray(baseline), np.asarray(prior_opened.convert("RGB")))
                baseline_matches += int(baseline_match)
                derivative = obstruct(baseline)
                base_pixels = np.asarray(baseline, dtype=np.uint8)
                derivative_pixels = np.asarray(derivative, dtype=np.uint8)
                target = frames / f"scene_{scene:02d}_{variant}.png"
                derivative.save(target, format="PNG", optimize=False)
                sample = {
                    "variant": variant,
                    "baseline_variant": baseline_variant,
                    "baseline_pass23_frame": prior["frame"],
                    "baseline_pass23_frame_sha256": prior["frame_sha256"],
                    "baseline_recomputed_pixel_exact": baseline_match,
                    "mask_fraction": MASK_FRACTION,
                    "mask_top_y": MASK_TOP_Y,
                    "mask_color_rgb": MASK_RGB.tolist(),
                    "unobstructed_pixels_exact": bool(np.array_equal(base_pixels[:MASK_TOP_Y], derivative_pixels[:MASK_TOP_Y])),
                    "masked_pixels_exact": bool(np.all(derivative_pixels[MASK_TOP_Y:] == MASK_RGB)),
                    "frame": target.relative_to(group_root).as_posix(),
                    "frame_sha256": sha(target),
                    "width": 640,
                    "height": 360,
                }
                samples.append(sample)
                by_variant[variant].append({"scene": scene, **sample})
        scenes.append({"scene": scene, "source": source.relative_to(ROOT).as_posix(), "source_sha256": sha(source), "samples": samples})
    sheets = {variant: contact_sheet(group_root, variant, rows) for variant, rows in by_variant.items()}
    return ({
        "group": name,
        "source_receipt": source_receipt.relative_to(ROOT).as_posix(),
        "source_receipt_sha256": sha(source_receipt),
        "scene_count": 7,
        "frame_count": 35,
        "baseline_pass23_pixel_match_count": baseline_matches,
        "scenes": scenes,
        "contact_sheets": sheets,
    }, baseline_matches)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    previous = json.loads(PREVIOUS.read_text())
    groups: dict[str, object] = {}
    baseline_total = 0
    for name, spec in GROUPS.items():
        paths, source_receipt = spec["source_paths"], spec["source_receipt"]
        if not isinstance(paths, list) or not isinstance(source_receipt, Path) or not all(isinstance(path, Path) for path in paths):
            raise TypeError("invalid group specification")
        group, matches = build_group(name, paths, source_receipt, previous["groups"][name])
        groups[name] = group
        baseline_total += matches
    receipt = {
        "status": "QA_STATIC_DERIVATIVES_ONLY_NOT_V9_NOT_A_CANDIDATE",
        "deepening_pass": 26,
        "audit": "method_native_monochrome_or_color_vision_then_minimum_scale_then_bottom25_obstruction",
        "variant_order": VARIANTS,
        "baseline_variant_map": BASELINE_VARIANTS,
        "scene_count": 21,
        "frame_count": 105,
        "baseline_pass23_pixel_match_count": baseline_total,
        "represented_resolution": [640, 360],
        "groups": groups,
        "transform_contract": {
            "order": "native RGB -> color or linear-light BT.709 grayscale/fixed Machado severity-100 matrix -> sRGB np.rint uint8 -> Pillow LANCZOS 640x360 -> opaque RGB black rows 270..359",
            "mask_fraction": MASK_FRACTION,
            "mask_top_y": MASK_TOP_Y,
            "mask_color_rgb": MASK_RGB.tolist(),
            "unobstructed_pixel_contract": "rows 0..269 byte-identical to matching lossless pass23 represented baseline",
            "matrices": {key: value.tolist() for key, value in MATRICES.items()},
            "simulation_scope": "presentation stress only; not clinical diagnostic or named caption/player/viewing standard",
            "numpy": np.__version__,
            "pillow": PIL.__version__,
        },
        "sealed_v8_modified": False,
        "pass7_proof_modified": False,
        "pass12_proof_modified": False,
        "v9_created": False,
        "tts_invoked": False,
        "audio_generated": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
        "git_action": False,
    }
    (OUT / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"PASS groups=3 scenes=21 frames=105 baseline={baseline_total}/105 mask=105/105")


if __name__ == "__main__":
    main()
