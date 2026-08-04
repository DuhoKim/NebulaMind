#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
LANE = ROOT.parent
ASSETS = ROOT / "assets_receipt.json"
SPEC = LANE / "V4_Z9_CANARY_SPEC.json"
V3_SCRIPT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v3-male-lipsync-20260723T050645Z/render_v3_musetalk_presenters.py")
KEY = "z9-metallicity"
SPEEDS = [0.83, 1.02, 1.15, 0.91, 1.08, 0.87, 1.12, 0.96, 1.04, 0.89]
PHASES = [0, 71, 143, 34, 188, 106, 236, 52, 165, 20]


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_module() -> Any:
    module_spec = importlib.util.spec_from_file_location("v3_presenter", V3_SCRIPT)
    if module_spec is None or module_spec.loader is None:
        raise RuntimeError("could not load proven V3 presenter renderer")
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


def main() -> None:
    for required in (ASSETS, SPEC, V3_SCRIPT):
        if not required.is_file():
            raise FileNotFoundError(required)
    asset = json.loads(ASSETS.read_text())
    if asset.get("marker") != "NEBULAMIND_V4_Z9_AUDIO_ASSETS_COMPLETE" or asset.get("key") != KEY:
        raise RuntimeError("unexpected audio asset receipt")
    if asset["spec_sha256"] != sha256(SPEC):
        raise RuntimeError("audio lineage uses an older spec")
    if len(asset["timeline"]) != 10:
        raise RuntimeError("presenter requires ten-slot timeline")

    presenter_dir = ROOT / KEY / "presenter"
    presenter_dir.mkdir(parents=True, exist_ok=True)
    final_output = presenter_dir / f"{KEY}_MICHAEL_MUSETALK_MLX_V4.mp4"
    receipt_path = presenter_dir / "presenter_receipt.json"
    if final_output.is_file() and receipt_path.is_file():
        existing = json.loads(receipt_path.read_text())
        if (
            existing.get("marker") == "NEBULAMIND_V4_Z9_MUSETALK_PRESENTER_COMPLETE"
            and existing.get("output_sha256") == sha256(final_output)
            and existing.get("audio_sha256") == asset["narration_sha256"]
            and existing.get("spec_sha256") == sha256(SPEC)
        ):
            print(json.dumps({"status": "SKIP_VERIFIED", "output": str(final_output), "sha256": sha256(final_output)}, indent=2))
            return

    module = load_module()
    module.BATCH = ROOT
    module.ASSETS_RECEIPT = ASSETS
    module.SCENE_SPEEDS = SPEEDS
    module.SCENE_PHASES = PHASES
    for required in (module.GESTURE, module.BOXES, module.MODEL / "config.json"):
        if not required.is_file():
            raise FileNotFoundError(required)

    module.mx.set_default_device(module.mx.gpu)
    pipe = module.MuseTalkPipeline.from_pretrained_mlx(module.MODEL)
    frames, boxes = module.load_source()
    crops = []
    for frame, box in zip(frames, boxes):
        x1, y1, x2, y2 = box
        y2 = min(frame.shape[0], y2 + 10)
        crops.append(module.cv2.resize(frame[y1:y2, x1:x2], (256, 256), interpolation=module.cv2.INTER_LANCZOS4))
    print("Encoding 144 approved gesture crops once", flush=True)
    latents = [pipe.get_latents_for_unet(crop) for crop in crops]
    mask = module.make_mask()
    receipt = module.render_one(pipe, frames, boxes, latents, mask, asset)
    generated = Path(receipt["output"])
    if not generated.is_file():
        raise FileNotFoundError(generated)
    os.replace(generated, final_output)
    media = module.probe(final_output)
    receipt.update({
        "marker": "NEBULAMIND_V4_Z9_MUSETALK_PRESENTER_COMPLETE",
        "completed_at_utc": now(),
        "spec": str(SPEC),
        "spec_sha256": sha256(SPEC),
        "audio": asset["narration_master"],
        "audio_sha256": asset["narration_sha256"],
        "slot_count": len(asset["timeline"]),
        "scene_source_ranges": receipt["scene_source_ranges"],
        "output": str(final_output),
        "output_sha256": sha256(final_output),
        "probe": media,
        "publication_state": "local V4 z9 canary only; not uploaded",
        "youtube_mutation": False,
        "website_mutation": False,
        "git_mutation": False,
    })
    receipt_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "PASS",
        "output": str(final_output),
        "sha256": receipt["output_sha256"],
        "frames": receipt["frames"],
        "duration_seconds": receipt["duration_seconds"],
        "render_seconds": receipt["render_seconds"],
    }, indent=2))


if __name__ == "__main__":
    main()
