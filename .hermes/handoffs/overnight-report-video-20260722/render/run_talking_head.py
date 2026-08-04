#!/usr/bin/env python3
"""Generate the exact-audio overnight-report talking head from the accepted identity."""
from __future__ import annotations

import json
import os
import subprocess
import time
from pathlib import Path

SADTALKER = Path("/Users/duhokim/HermesOps/tools/SadTalker")
PYTHON = SADTALKER / ".venv/bin/python"
INFERENCE = SADTALKER / "inference.py"
BASE = Path(__file__).resolve().parent
SOURCE = Path(
    "/Users/duhokim/HermesOps/scripts/clips/subnav_flow_lipsync_v7/"
    "canary/flow_master_shoulder_crop_768x1024.png"
)
DRIVER = BASE / "driver_audio/overnight_report_female_exact_narration_73s.wav"
RESULT_DIR = BASE / "talking_head/raw_256"
CANONICAL = BASE / "talking_head/overnight_report.mp4"


def probe(path: Path) -> dict:
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration,size:stream=codec_name,width,height,r_frame_rate,nb_frames",
        "-of", "json", str(path),
    ], text=True))


def main() -> None:
    for path in (PYTHON, INFERENCE, SOURCE, DRIVER):
        if not path.exists():
            raise FileNotFoundError(path)
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    CANONICAL.parent.mkdir(parents=True, exist_ok=True)
    before = {p.resolve() for p in RESULT_DIR.glob("*.mp4")}
    env = os.environ.copy()
    env["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
    started = time.time()
    subprocess.run([
        str(PYTHON), str(INFERENCE),
        "--driven_audio", str(DRIVER),
        "--source_image", str(SOURCE),
        "--result_dir", str(RESULT_DIR),
        "--still", "--preprocess", "crop", "--size", "256",
        "--batch_size", "4", "--expression_scale", "0.72",
    ], cwd=SADTALKER, env=env, check=True)
    candidates = [p for p in RESULT_DIR.glob("*.mp4") if p.resolve() not in before]
    if not candidates:
        candidates = list(RESULT_DIR.glob("*.mp4"))
    if not candidates:
        raise RuntimeError("SadTalker produced no MP4")
    source = max(candidates, key=lambda p: p.stat().st_mtime)
    normalized = CANONICAL.with_suffix(".normalized.mp4")
    subprocess.run([
        "ffmpeg", "-y", "-v", "error", "-i", str(source),
        "-vf", "fps=24,tpad=stop_mode=clone:stop_duration=0.1,trim=duration=73.5,setpts=PTS-STARTPTS",
        "-an", "-frames:v", "1764", "-c:v", "libx264", "-preset", "veryfast",
        "-crf", "18", "-pix_fmt", "yuv420p", "-r", "24", "-movflags", "+faststart",
        str(normalized),
    ], check=True)
    normalized.replace(CANONICAL)
    receipt = {
        "marker": "NEBULAMIND_OVERNIGHT_REPORT_V1_TALKING_HEAD_COMPLETE",
        "source_identity": str(SOURCE),
        "exact_driver": str(DRIVER),
        "raw_output": str(source),
        "canonical": str(CANONICAL),
        "elapsed_seconds": round(time.time() - started, 2),
        "probe": probe(CANONICAL),
    }
    (BASE / "talking_head_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
