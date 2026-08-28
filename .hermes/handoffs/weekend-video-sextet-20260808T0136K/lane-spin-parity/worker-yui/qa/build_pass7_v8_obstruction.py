#!/usr/bin/env python3
"""Build caption/UI obstruction derivatives of sealed v8 proposal frames."""

from __future__ import annotations

import hashlib
import io
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SEALED = ROOT / "proposal_frames/v8"
OUT = ROOT / "qa/pass7_v8_obstruction"
FRAMES = OUT / "frames"
OUTPUT = ROOT / "qa/pass7_v8_obstruction_audit.json"
VARIANTS = {
    "clean": 0.0,
    "caption_15pct": 0.15,
    "player_ui_25pct": 0.25,
}
FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.casefold())


def phrase_present(tokens: list[str], phrase: tuple[str, ...]) -> bool:
    if len(tokens) < len(phrase):
        return False
    return any(tuple(tokens[index : index + len(phrase)]) == phrase for index in range(len(tokens) - len(phrase) + 1))


def ocr_image(image: Image.Image, psm: int) -> tuple[list[str], str]:
    buffer = io.BytesIO()
    image.save(buffer, format="PNG", optimize=False)
    process = subprocess.run(
        ["tesseract", "stdin", "stdout", "--psm", str(psm)],
        input=buffer.getvalue(),
        check=True,
        capture_output=True,
    )
    text = process.stdout.decode("utf-8", errors="replace")
    tokens = normalize_tokens(text)
    return tokens, hashlib.sha256(text.encode("utf-8")).hexdigest()


def obstruct(source: Path, fraction: float, destination: Path) -> int:
    with Image.open(source).convert("RGB") as image:
        y = round(image.height * (1.0 - fraction))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, y, image.width, image.height), fill=(4, 8, 14))
        image.save(destination, format="PNG", optimize=False)
    return y


def crop_hash(path: Path, bottom_fraction: float) -> str:
    with Image.open(path).convert("RGB") as image:
        bottom = round(image.height * (1.0 - bottom_fraction))
        return hashlib.sha256(image.crop((0, 0, image.width, bottom)).tobytes()).hexdigest()


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in FONT_CANDIDATES:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def make_sheet(label: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    tile_w, tile_h = 480, 270
    sheet = Image.new("RGB", (tile_w * 4, tile_h * 2), (4, 8, 14))
    draw = ImageDraw.Draw(sheet)
    label_font = font(22)
    for index, row in enumerate(rows):
        path = OUT / row["frame"]
        with Image.open(path).convert("RGB") as image:
            image.thumbnail((tile_w, tile_h), Image.Resampling.LANCZOS)
            x = (index % 4) * tile_w
            y = (index // 4) * tile_h
            sheet.paste(image, (x, y))
        draw.rectangle((x, y, x + 250, y + 28), fill=(4, 8, 14))
        draw.text((x + 8, y + 3), f"S{row['scene']:02d} · {label}", fill=(242, 246, 252), font=label_font)
    destination = OUT / f"contact_sheet_{label}.png"
    sheet.save(destination, format="PNG", optimize=False)
    return {
        "path": destination.relative_to(OUT).as_posix(),
        "sha256": sha256(destination),
        "width": sheet.width,
        "height": sheet.height,
    }


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    FRAMES.mkdir(parents=True, exist_ok=True)
    sealed_inputs = sorted(SEALED.glob("scene_*.png"))
    if len(sealed_inputs) != 7:
        raise SystemExit(f"expected seven sealed frames, found {len(sealed_inputs)}")
    scenes: list[dict[str, Any]] = []
    rows_by_variant: dict[str, list[dict[str, Any]]] = {variant: [] for variant in VARIANTS}
    for scene_number, source in enumerate(sealed_inputs, start=1):
        samples: list[dict[str, Any]] = []
        for variant, fraction in VARIANTS.items():
            destination = FRAMES / f"scene_{scene_number:02d}_{variant}.png"
            if variant == "clean":
                shutil.copyfile(source, destination)
                mask_y = 1080
            else:
                mask_y = obstruct(source, fraction, destination)
            with Image.open(destination).convert("RGB") as image:
                if image.size != (1920, 1080):
                    raise SystemExit(f"invalid derivative size: {destination}")
                full_tokens, full_hash = ocr_image(image, 6)
                badge = image.crop((1344, 0, 1920, 180)).resize((2304, 720), Image.Resampling.LANCZOS)
                badge_tokens, badge_hash = ocr_image(badge, 7)
            semantic_phrases = {
                "result_held": phrase_present(full_tokens, ("result", "held")),
                "result_locked": phrase_present(full_tokens, ("result", "locked")),
                "frame_unstated": phrase_present(full_tokens, ("frame", "unstated")),
                "outcomes_withheld": phrase_present(full_tokens, ("outcomes", "withheld")),
                "no_outcome_shown": phrase_present(full_tokens, ("no", "outcome", "shown")),
                "storage_frame_unresolved": phrase_present(full_tokens, ("storage", "frame", "unresolved")),
                "separate_authorization": phrase_present(full_tokens, ("separate", "authorization")),
            }
            top_identity = variant == "clean" or crop_hash(destination, fraction) == crop_hash(source, fraction)
            row = {
                "scene": scene_number,
                "variant": variant,
                "occluded_bottom_fraction": fraction,
                "mask_start_y": mask_y,
                "frame": destination.relative_to(OUT).as_posix(),
                "frame_sha256": sha256(destination),
                "top_region_pixel_identical_to_sealed": top_identity,
                "full_ocr_sha256": full_hash,
                "badge_ocr_sha256": badge_hash,
                "result_held_badge_detected": phrase_present(badge_tokens, ("result", "held")),
                "semantic_phrases_detected": semantic_phrases,
            }
            samples.append(row)
            rows_by_variant[variant].append(row)
        scenes.append(
            {
                "scene": scene_number,
                "sealed_input": source.name,
                "sealed_input_sha256": sha256(source),
                "samples": samples,
            }
        )
    contact_sheets = {
        variant: make_sheet(variant, rows)
        for variant, rows in rows_by_variant.items()
    }
    aggregates: dict[str, Any] = {}
    for variant, rows in rows_by_variant.items():
        phrase_counts = {
            phrase: sum(row["semantic_phrases_detected"][phrase] for row in rows)
            for phrase in rows[0]["semantic_phrases_detected"]
        }
        aggregates[variant] = {
            "scene_count": 7,
            "result_held_badge_detected": sum(row["result_held_badge_detected"] for row in rows),
            "top_region_pixel_identical_to_sealed": sum(row["top_region_pixel_identical_to_sealed"] for row in rows),
            "semantic_phrase_scene_counts": phrase_counts,
        }
    output = {
        "status": "QA_DERIVATIVES_ONLY_NOT_A_CANDIDATE",
        "deepening_pass": 7,
        "audit": "sealed_v8_caption_and_player_ui_obstruction",
        "sealed_v8_modified": False,
        "sealed_v8_storyboard_sha256": sha256(ROOT / "STORYBOARD_PROPOSAL.json"),
        "sealed_v8_renderer_sha256": sha256(ROOT / "render_proposal_frames.py"),
        "variant_order": list(VARIANTS),
        "frame_count": 21,
        "scenes": scenes,
        "aggregates": aggregates,
        "contact_sheets": contact_sheets,
        "raw_ocr_text_stored": False,
        "human_visual_review_required": True,
        "tts_invoked": False,
        "video_encoded": False,
        "shared_or_public_assets_modified": False,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        "PASS v8=7 frames=21 "
        + " ".join(
            f"{variant}:badge={aggregates[variant]['result_held_badge_detected']}/7"
            for variant in VARIANTS
        )
    )


if __name__ == "__main__":
    main()
