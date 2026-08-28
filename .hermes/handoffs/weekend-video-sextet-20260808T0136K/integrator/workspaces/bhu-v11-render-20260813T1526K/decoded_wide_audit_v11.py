#!/usr/bin/env python3
"""Decode every V11 state midpoint and crop/upscale every caption for robust OCR."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parent
VIDEO = Path("/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v11-local-20260813T1526K.mp4")
EXPECTED_VIDEO_SHA = "8e6a4e564ddc25959ecb17c57fe19d898b9f92850b5c83da234ef3d2295f40fb"
MANIFEST = json.loads((ROOT / "render_manifest.json").read_text())
TIMELINE = json.loads((ROOT / "audio" / "timeline.json").read_text())
STATE_MANIFEST = json.loads((ROOT / "render_state_manifest.json").read_text()) if (ROOT / "render_state_manifest.json").exists() else None
OUT_ROOT = ROOT / "encoded_qa" / "decoded_wide"
STATE_FRAMES = OUT_ROOT / "states"
STATE_OCR = OUT_ROOT / "state_ocr"
CAPTION_FRAMES = OUT_ROOT / "captions"
CAPTION_CROPS = OUT_ROOT / "caption_crops"
CAPTION_OCR = OUT_ROOT / "caption_ocr"
REPORT = OUT_ROOT / "decoded_wide_audit.json"
CREW_TERMS = ("duho", "lana", "goru", "kun", "hwao", "yui", "tori", "fable")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=check, capture_output=True, text=True)


def extract(timestamp: float, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    run(
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-ss", f"{timestamp:.6f}", "-i", str(VIDEO),
        "-frames:v", "1", "-q:v", "1", str(output),
    )


def ocr(path: Path, output_dir: Path, psm: str) -> str:
    output_dir.mkdir(parents=True, exist_ok=True)
    base = output_dir / path.stem
    result = run("tesseract", str(path), str(base), "--psm", psm, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"tesseract failed {path.name}: {result.stderr}")
    return base.with_suffix(".txt").read_text(errors="replace")


def ordered_recall(expected: str, actual: str) -> float:
    wanted = normalize(expected).split()
    got = normalize(actual).split()
    cursor = 0
    matched = 0
    for token in wanted:
        try:
            position = got.index(token, cursor)
        except ValueError:
            continue
        matched += 1
        cursor = position + 1
    return matched / max(1, len(wanted))


def intervals() -> list[dict]:
    # Reconstruct the exact deterministic interval partition used by render_v11.
    boundaries = {0, 415 * 30}
    for card in TIMELINE["cards"]:
        start = float(card["master_start_seconds"])
        end = float(card["master_end_seconds"])
        boundaries.add(round(start * 30))
        boundaries.add(round(end * 30))
        for cue in card["captions"]:
            boundaries.add(max(round((start + float(cue["card_start_seconds"])) * 30), round(start * 30)))
            boundaries.add(min(__import__("math").ceil((start + float(cue["card_end_seconds"])) * 30), round(end * 30)))
        for reveal in card["reveals"]:
            boundaries.add(__import__("math").ceil((start + float(reveal["card_seconds"])) * 30))
    card04_start = float(TIMELINE["cards"][3]["master_start_seconds"])
    card04_heading = float(MANIFEST["card04_heading_reveal_card_seconds"])
    boundaries.add(__import__("math").ceil((card04_start + card04_heading) * 30))
    values = sorted(frame for frame in boundaries if 0 <= frame <= 415 * 30)
    rows = []
    for index, (start, end) in enumerate(zip(values, values[1:])):
        if end <= start:
            continue
        rows.append({
            "index": index,
            "start_frame": start,
            "end_frame": end,
            "midpoint_seconds": ((start + end - 1) / 2) / 30,
        })
    return rows


def main() -> int:
    if sha(VIDEO) != EXPECTED_VIDEO_SHA:
        raise RuntimeError("candidate hash drift")
    state_rows = []
    all_hits = []
    interval_rows = intervals()
    if len(interval_rows) != 177:
        raise RuntimeError(f"interval count drift: {len(interval_rows)}")
    for index, interval in enumerate(interval_rows, 1):
        frame = STATE_FRAMES / f"state-{interval['index']:04d}.png"
        extract(float(interval["midpoint_seconds"]), frame)
        text = ocr(frame, STATE_OCR, "11")
        hits = [term for term in CREW_TERMS if re.search(rf"\b{re.escape(term)}\b", text.lower())]
        all_hits.extend(hits)
        state_rows.append({
            **interval,
            "frame": str(frame.relative_to(ROOT)),
            "frame_sha256": sha(frame),
            "ocr": text,
            "crew_name_hits": hits,
        })
        if index % 20 == 0:
            print(f"decoded state {index}/{len(interval_rows)}")

    cues = [cue for card in TIMELINE["cards"] for cue in card["captions"]]
    caption_rows = []
    for index, cue in enumerate(cues, 1):
        midpoint = (float(cue["master_start_seconds"]) + float(cue["master_end_seconds"])) / 2
        frame = CAPTION_FRAMES / f"{cue['id']}.png"
        crop = CAPTION_CROPS / f"{cue['id']}.png"
        extract(midpoint, frame)
        image = Image.open(frame).convert("L").crop((110, 865, 1810, 1010))
        image = image.resize((3400, 290), Image.Resampling.LANCZOS)
        image = ImageEnhance.Contrast(image).enhance(2.0)
        image = image.filter(ImageFilter.UnsharpMask(radius=1.5, percent=180, threshold=2))
        crop.parent.mkdir(parents=True, exist_ok=True)
        image.save(crop)
        text = ocr(crop, CAPTION_OCR, "6")
        recall = ordered_recall(cue["text"], text)
        caption_rows.append({
            "id": cue["id"],
            "card_id": cue["card_id"],
            "expected": cue["text"],
            "midpoint_seconds": midpoint,
            "decoded_frame": str(frame.relative_to(ROOT)),
            "decoded_frame_sha256": sha(frame),
            "caption_crop": str(crop.relative_to(ROOT)),
            "caption_crop_sha256": sha(crop),
            "ocr": text,
            "in_order_token_recall": recall,
            "status": "PASS" if recall >= 0.85 else "REVIEW",
        })
        if index % 15 == 0:
            print(f"caption crop {index}/{len(cues)}")

    exact_equality = all(
        " ".join(cue["text"] for cue in card["captions"]) == card["narration"]
        for card in TIMELINE["cards"]
    )
    reviews = [row["id"] for row in caption_rows if row["status"] != "PASS"]
    report = {
        "status": "PASS_DECODED_WIDE_STATE_AND_CAPTION_AUDIT" if not all_hits and exact_equality and not reviews else "REVIEW_DECODED_WIDE_STATE_AND_CAPTION_AUDIT",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "candidate": str(VIDEO),
        "candidate_sha256": sha(VIDEO),
        "decoded_state_midpoints": len(state_rows),
        "encoded_frames_partitioned": 12_450,
        "decoded_state_crew_name_hits": sorted(set(all_hits)),
        "caption_cues": len(caption_rows),
        "exact_caption_source_equality_all_cards": exact_equality,
        "caption_ocr_passes": len(caption_rows) - len(reviews),
        "caption_ocr_reviews": reviews,
        "caption_minimum_recall": min(row["in_order_token_recall"] for row in caption_rows),
        "states": state_rows,
        "captions": caption_rows,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({key: report[key] for key in (
        "status", "decoded_state_midpoints", "encoded_frames_partitioned",
        "decoded_state_crew_name_hits", "caption_cues",
        "exact_caption_source_equality_all_cards", "caption_ocr_passes",
        "caption_ocr_reviews", "caption_minimum_recall",
    )}, indent=2))
    return 0 if report["status"].startswith("PASS") else 2


if __name__ == "__main__":
    raise SystemExit(main())
