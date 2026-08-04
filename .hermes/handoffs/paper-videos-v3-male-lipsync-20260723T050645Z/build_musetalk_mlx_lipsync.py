#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
import time
from pathlib import Path

import cv2
import mlx.core as mx
import numpy as np

from musetalk_mlx.pipeline_mlx import MuseTalkPipeline

HANDOFF = Path(__file__).resolve().parent
SOURCE = HANDOFF / "omni/gemini_omni_gesture_raw.mp4"
AUDIO = HANDOFF / "lipsync/michael_gesture_excerpt_6s.wav"
BOXES = HANDOFF / "omni/musetalk_face_boxes.json"
OUTPUT = HANDOFF / "omni/gemini_omni_gesture_michael_musetalk_mlx.mp4"
RECEIPT = HANDOFF / "omni/musetalk_mlx_canary_receipt.json"
MODEL = Path("/Users/duhokim/HermesOps/tools/musetalk-mlx/dist/MuseTalk-1.5-MLX-q4")
FPS = 24
DURATION = 6.0
MASK_CENTER = (128, 190)
MASK_RADII = (78, 50)
MASK_SIGMA = 6
EXTRA_BOTTOM = 10


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def read_frames(path: Path) -> tuple[list[np.ndarray], float]:
    capture = cv2.VideoCapture(str(path))
    fps = capture.get(cv2.CAP_PROP_FPS)
    frames: list[np.ndarray] = []
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        frames.append(frame)
    capture.release()
    return frames, fps


def laplacian_variance(frame: np.ndarray, roi: tuple[int, int, int, int]) -> float:
    x1, y1, x2, y2 = roi
    gray = cv2.cvtColor(frame[y1:y2, x1:x2], cv2.COLOR_BGR2GRAY)
    return float(cv2.Laplacian(gray, cv2.CV_64F).var())


def main() -> None:
    for required in (SOURCE, AUDIO, BOXES, MODEL / "config.json"):
        if not required.is_file():
            raise FileNotFoundError(required)

    frames, source_fps = read_frames(SOURCE)
    metadata = json.loads(BOXES.read_text())
    boxes = [list(map(int, box)) for box in metadata["boxes"]]
    if source_fps != FPS or len(frames) != 144 or len(boxes) != len(frames):
        raise RuntimeError(
            f"unexpected source contract: fps={source_fps}, frames={len(frames)}, boxes={len(boxes)}"
        )

    # The generated source contains one unrelated close-up burn at frame 0.
    # Replace it with frame 1 so the speaking canary starts on the stable shot.
    frames[0] = frames[1].copy()
    boxes[0] = boxes[1].copy()

    mx.set_default_device(mx.gpu)
    start = time.time()
    pipe = MuseTalkPipeline.from_pretrained_mlx(MODEL)
    chunks = pipe.encode_audio_from_wav(AUDIO, fps=FPS)
    if chunks.shape[0] != len(frames):
        raise RuntimeError(f"audio/video frame mismatch: chunks={chunks.shape[0]}, frames={len(frames)}")

    crops: list[np.ndarray] = []
    adjusted_boxes: list[tuple[int, int, int, int]] = []
    latents = []
    for frame, (x1, y1, x2, y2) in zip(frames, boxes):
        y2 = min(y2 + EXTRA_BOTTOM, frame.shape[0])
        if x2 <= x1 or y2 <= y1:
            raise RuntimeError(f"invalid face box: {(x1, y1, x2, y2)}")
        crop = cv2.resize(
            frame[y1:y2, x1:x2],
            (256, 256),
            interpolation=cv2.INTER_LANCZOS4,
        )
        crops.append(crop)
        adjusted_boxes.append((x1, y1, x2, y2))
        latents.append(pipe.get_latents_for_unet(crop))

    latent_stack = mx.concatenate(latents, axis=0).astype(mx.float16)
    generated = pipe.run_batched(latent_stack, chunks.astype(mx.float16), batch_size=8)
    if generated.shape != (len(frames), 256, 256, 3):
        raise RuntimeError(f"unexpected generated shape: {generated.shape}")

    mask = np.zeros((256, 256), np.uint8)
    cv2.ellipse(mask, MASK_CENTER, MASK_RADII, 0, 0, 360, 255, -1)
    mask = cv2.GaussianBlur(mask, (0, 0), MASK_SIGMA)

    composites: list[np.ndarray] = []
    for frame, face, (x1, y1, x2, y2) in zip(frames, generated, adjusted_boxes):
        width, height = x2 - x1, y2 - y1
        face_resized = cv2.resize(face, (width, height), interpolation=cv2.INTER_LANCZOS4)
        alpha = cv2.resize(
            mask.astype(np.float32) / 255.0,
            (width, height),
            interpolation=cv2.INTER_LINEAR,
        )[..., None]
        result = frame.copy()
        original = result[y1:y2, x1:x2].astype(np.float32)
        result[y1:y2, x1:x2] = np.clip(
            original * (1.0 - alpha) + face_resized.astype(np.float32) * alpha,
            0,
            255,
        ).astype(np.uint8)
        composites.append(result)

    with tempfile.TemporaryDirectory(prefix="musetalk-frames-", dir=HANDOFF / "omni") as temp_dir:
        temp = Path(temp_dir)
        for index, frame in enumerate(composites):
            if not cv2.imwrite(str(temp / f"{index:08d}.png"), frame):
                raise RuntimeError(f"failed to write frame {index}")
        run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-framerate", str(FPS), "-i", str(temp / "%08d.png"),
            "-i", str(AUDIO),
            "-map", "0:v:0", "-map", "1:a:0",
            "-t", str(DURATION),
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "15",
            "-pix_fmt", "yuv420p", "-r", str(FPS),
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-movflags", "+faststart", str(OUTPUT),
        ])

    run(["ffmpeg", "-v", "error", "-xerror", "-i", str(OUTPUT), "-f", "null", "-"])
    encoded, encoded_fps = read_frames(OUTPUT)
    if encoded_fps != FPS or len(encoded) != len(frames):
        raise RuntimeError(f"encoded contract mismatch: fps={encoded_fps}, frames={len(encoded)}")

    sample_indices = [10, 34, 58, 82, 106, 130]
    mouth_roi = (565, 245, 715, 330)
    upper_roi = (545, 110, 725, 225)
    source_mouth = np.mean([laplacian_variance(frames[i], mouth_roi) for i in sample_indices])
    output_mouth = np.mean([laplacian_variance(encoded[i], mouth_roi) for i in sample_indices])
    source_upper = np.mean([laplacian_variance(frames[i], upper_roi) for i in sample_indices])
    output_upper = np.mean([laplacian_variance(encoded[i], upper_roi) for i in sample_indices])

    model_files = {}
    for name in ("config.json", "unet.safetensors", "vae.safetensors", "whisper_encoder.safetensors"):
        path = MODEL / name
        model_files[name] = {"bytes": path.stat().st_size, "sha256": sha256(path)}

    probe = json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-count_frames",
        "-show_entries",
        "format=duration,size,bit_rate:stream=codec_name,codec_type,width,height,r_frame_rate,nb_read_frames,sample_rate,channels",
        "-of", "json", str(OUTPUT),
    ], text=True))
    receipt = {
        "marker": "NEBULAMIND_MUSETALK_MLX_LIPSYNC_CANARY_COMPLETE",
        "source": str(SOURCE),
        "source_sha256": sha256(SOURCE),
        "audio": str(AUDIO),
        "audio_sha256": sha256(AUDIO),
        "face_boxes": str(BOXES),
        "face_tracking": "S3FD per-frame detections at 0.5 scale; no temporal smoothing",
        "frame_zero_repair": "replaced source frame 0 close-up burn with source frame 1",
        "model": "mlx-community/MuseTalk-1.5-q4",
        "model_files": model_files,
        "model_code": "xocialize/musetalk-mlx@c6eb30e",
        "mask": {
            "center": MASK_CENTER,
            "radii": MASK_RADII,
            "gaussian_sigma": MASK_SIGMA,
            "extra_bottom_pixels": EXTRA_BOTTOM,
        },
        "output": str(OUTPUT),
        "output_sha256": sha256(OUTPUT),
        "probe": probe,
        "sharpness": {
            "sample_indices": sample_indices,
            "mouth_source_mean": source_mouth,
            "mouth_output_mean": output_mouth,
            "mouth_ratio": output_mouth / source_mouth,
            "upper_face_source_mean": source_upper,
            "upper_face_output_mean": output_upper,
            "upper_face_ratio": output_upper / source_upper,
            "rejected_wav2lip_mouth_ratio": 0.18546214441066852,
        },
        "render_seconds": time.time() - start,
        "youtube_mutation": False,
        "website_mutation": False,
        "git_mutation": False,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
