#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import cv2
import mlx.core as mx
import numpy as np

from musetalk_mlx.pipeline_mlx import MuseTalkPipeline

BASE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v3-male-lipsync-20260723T050645Z")
BATCH = BASE / "batch"
ASSETS_RECEIPT = BATCH / "assets_batch_receipt.json"
GESTURE = BASE / "omni/gemini_omni_gesture_raw.mp4"
BOXES = BASE / "omni/musetalk_face_boxes.json"
MODEL = Path("/Users/duhokim/HermesOps/tools/musetalk-mlx/dist/MuseTalk-1.5-MLX-q4")
FPS = 24
BATCH_SIZE = 8
SCENE_SPEEDS = [0.83, 1.02, 1.15, 0.91, 1.08, 0.87, 1.12, 0.96]
SCENE_PHASES = [0, 71, 143, 34, 188, 106, 236, 52]


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def probe(path: Path) -> dict[str, Any]:
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-count_frames",
        "-show_entries", "format=duration,size,bit_rate:stream=codec_name,codec_type,width,height,r_frame_rate,nb_read_frames",
        "-of", "json", str(path),
    ], text=True))


def load_source() -> tuple[list[np.ndarray], list[list[int]]]:
    cap = cv2.VideoCapture(str(GESTURE))
    frames: list[np.ndarray] = []
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        frames.append(frame)
    cap.release()
    box_data = json.loads(BOXES.read_text())
    boxes = [list(map(int, box)) for box in box_data["boxes"]]
    if len(frames) != 144 or len(boxes) != len(frames):
        raise RuntimeError(f"source contract failed: {len(frames)} frames, {len(boxes)} boxes")
    frames[0] = frames[1].copy()
    boxes[0] = boxes[1].copy()
    return frames, boxes


def make_mask() -> np.ndarray:
    mask = np.zeros((256, 256), np.uint8)
    cv2.ellipse(mask, (128, 190), (78, 50), 0, 0, 360, 255, -1)
    return cv2.GaussianBlur(mask, (0, 0), 6).astype(np.float32) / 255.0


def source_indices(count: int, timeline: list[dict[str, Any]]) -> tuple[list[int], list[dict[str, Any]]]:
    pingpong = list(range(144)) + list(range(142, 0, -1))
    indices: list[int] = []
    scene_ranges: list[dict[str, Any]] = []
    starts = [float(row["audio_start"]) for row in timeline]
    starts.append(float("inf"))
    for scene_index, row in enumerate(timeline):
        start_frame = max(0, round(float(row["audio_start"]) * FPS))
        end_frame = count if scene_index == len(timeline) - 1 else min(count, round(starts[scene_index + 1] * FPS))
        scene_ranges.append({
            "scene": scene_index + 1,
            "output_start_frame": start_frame,
            "output_end_frame": end_frame,
            "source_phase": SCENE_PHASES[scene_index],
            "source_speed": SCENE_SPEEDS[scene_index],
        })
    for output_index in range(count):
        seconds = output_index / FPS
        scene_index = max(index for index, start in enumerate(starts[:-1]) if start <= seconds)
        local = output_index - round(starts[scene_index] * FPS)
        position = SCENE_PHASES[scene_index] + local * SCENE_SPEEDS[scene_index]
        indices.append(pingpong[round(position) % len(pingpong)])
    return indices, scene_ranges


def paste_face(frame: np.ndarray, generated: np.ndarray, box: list[int], mask256: np.ndarray) -> np.ndarray:
    x1, y1, x2, y2 = box
    y2 = min(frame.shape[0], y2 + 10)
    width, height = x2 - x1, y2 - y1
    generated = cv2.resize(generated, (width, height), interpolation=cv2.INTER_LANCZOS4)
    alpha = cv2.resize(mask256, (width, height), interpolation=cv2.INTER_LINEAR)[:, :, None]
    source = frame[y1:y2, x1:x2].astype(np.float32)
    blended = generated.astype(np.float32) * alpha + source * (1.0 - alpha)
    output = frame.copy()
    output[y1:y2, x1:x2] = np.clip(blended, 0, 255).astype(np.uint8)
    return output


def render_one(
    pipe: MuseTalkPipeline,
    frames: list[np.ndarray],
    boxes: list[list[int]],
    latents: list[Any],
    mask256: np.ndarray,
    asset: dict[str, Any],
) -> dict[str, Any]:
    key = asset["key"]
    root = BATCH / key / "presenter"
    root.mkdir(parents=True, exist_ok=True)
    output = root / f"{key}_MICHAEL_MUSETALK_MLX_V3.mp4"
    receipt_path = root / "presenter_receipt.json"
    audio = Path(asset["narration_master"])
    if sha256(audio) != asset["narration_sha256"]:
        raise RuntimeError(f"{key}: audio drift")
    if output.is_file() and receipt_path.is_file():
        receipt = json.loads(receipt_path.read_text())
        if receipt.get("output_sha256") == sha256(output) and receipt.get("audio_sha256") == sha256(audio):
            print(f"PRESENTER SKIP {key} verified", flush=True)
            return receipt

    audio_chunks = pipe.encode_audio_from_wav(str(audio), fps=FPS)
    count = int(audio_chunks.shape[0])
    indices, scene_ranges = source_indices(count, asset["timeline"])
    selected_latents = mx.concatenate([latents[index] for index in indices], axis=0)
    command = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", "1280x720", "-r", str(FPS), "-i", "-",
        "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "14",
        "-profile:v", "high", "-pix_fmt", "yuv420p", "-g", str(FPS * 2),
        "-movflags", "+faststart", str(output),
    ]
    encoder = subprocess.Popen(command, stdin=subprocess.PIPE)
    if encoder.stdin is None:
        raise RuntimeError("ffmpeg stdin unavailable")
    started = time.time()
    written = 0
    try:
        dtype = getattr(pipe, "_dtype", mx.float32)
        for batch_start in range(0, count, BATCH_SIZE):
            batch_end = min(count, batch_start + BATCH_SIZE)
            generated_values = pipe.generate_faces(
                selected_latents[batch_start:batch_end].astype(dtype),
                audio_chunks[batch_start:batch_end].astype(dtype),
            )
            for generated in generated_values:
                source_index = indices[written]
                output_frame = paste_face(frames[source_index], generated, boxes[source_index], mask256)
                encoder.stdin.write(output_frame.tobytes())
                written += 1
                if written % 240 == 0 or written == count:
                    print(f"{key} {written}/{count} frames", flush=True)
            mx.clear_cache()
    finally:
        encoder.stdin.close()
    return_code = encoder.wait()
    if return_code != 0:
        raise RuntimeError(f"ffmpeg failed for {key}: {return_code}")
    if written != count:
        raise RuntimeError(f"{key}: wrote {written} frames, expected {count}")
    subprocess.run(["ffmpeg", "-v", "error", "-xerror", "-i", str(output), "-f", "null", "-"], check=True)
    media = probe(output)
    stream = next(row for row in media["streams"] if row["codec_type"] == "video")
    if int(stream["nb_read_frames"]) != count or stream["r_frame_rate"] != "24/1":
        raise RuntimeError(f"{key}: presenter frame contract failed {stream}")
    receipt = {
        "marker": "NEBULAMIND_PAPER_V3_MUSETALK_PRESENTER_COMPLETE",
        "completed_at_utc": now(),
        "key": key,
        "gesture_source": str(GESTURE),
        "gesture_source_sha256": sha256(GESTURE),
        "face_boxes": str(BOXES),
        "face_boxes_sha256": sha256(BOXES),
        "audio": str(audio),
        "audio_sha256": sha256(audio),
        "model": str(MODEL),
        "model_hashes": {name: sha256(MODEL / name) for name in ("config.json", "unet.safetensors", "vae.safetensors", "whisper_encoder.safetensors")},
        "fps": FPS,
        "frames": count,
        "duration_seconds": round(count / FPS, 6),
        "render_seconds": round(time.time() - started, 3),
        "batch_size": BATCH_SIZE,
        "frame0_repair": "source frame 0 and box 0 replaced by frame 1",
        "source_motion": "scene-phased variable-speed ping-pong of the approved six-second gesture source",
        "scene_source_ranges": scene_ranges,
        "paste_back": "tight perioral ellipse centered (128,190), radii (78,50), Gaussian sigma 6",
        "output": str(output),
        "output_sha256": sha256(output),
        "probe": media,
        "publication_state": "local V3 build only; not uploaded",
    }
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--keys", nargs="*", help="render selected paper keys; default all")
    args = parser.parse_args()
    for required in (ASSETS_RECEIPT, GESTURE, BOXES, MODEL / "config.json"):
        if not required.is_file():
            raise FileNotFoundError(required)
    assets = json.loads(ASSETS_RECEIPT.read_text())
    papers = {row["key"]: row for row in assets["papers"]}
    selected = args.keys or list(papers)
    unknown = set(selected) - set(papers)
    if unknown:
        raise RuntimeError(f"unknown keys: {sorted(unknown)}")
    mx.set_default_device(mx.gpu)
    pipe = MuseTalkPipeline.from_pretrained_mlx(MODEL)
    frames, boxes = load_source()
    crops = []
    for frame, box in zip(frames, boxes):
        x1, y1, x2, y2 = box
        y2 = min(frame.shape[0], y2 + 10)
        crops.append(cv2.resize(frame[y1:y2, x1:x2], (256, 256), interpolation=cv2.INTER_LANCZOS4))
    print("Encoding 144 approved gesture crops once", flush=True)
    latents = [pipe.get_latents_for_unet(crop) for crop in crops]
    mask256 = make_mask()
    receipts = []
    for index, key in enumerate(selected, 1):
        print(f"PRESENTER {index}/{len(selected)} {key}", flush=True)
        receipts.append(render_one(pipe, frames, boxes, latents, mask256, papers[key]))
    batch_receipt = {
        "marker": "NEBULAMIND_FIVE_PAPER_V3_MUSETALK_PRESENTER_BATCH_PROGRESS",
        "completed_at_utc": now(),
        "selected": selected,
        "completed": [{"key": row["key"], "output": row["output"], "sha256": row["output_sha256"]} for row in receipts],
        "publication_state": "local V3 build only; not uploaded",
    }
    (BATCH / "presenter_batch_progress.json").write_text(json.dumps(batch_receipt, indent=2) + "\n")
    print(json.dumps(batch_receipt, indent=2))


if __name__ == "__main__":
    main()
