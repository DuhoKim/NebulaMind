#!/usr/bin/env python3
"""Color-vision acceptance evidence: audit_cvd.py <canary-dir>.

Implements the human-review side of the spin pass-8 redundant-encoding guard
(REDUNDANT_ENCODING_GUARD_PASS8.json clause 6): contact sheets of the canary's
encoded state frames in color, grayscale BT.709, and Machado-2009 severity-1.0
protanopia/deuteranopia/tritanopia simulations. Matrices are applied directly
to sRGB (the same practical approximation the lane's audit names 'machado100').
Human review of the sheets is the decisive check; this script only produces
the evidence. Writes beneath reviews/yui/qa/<canary-name>/color_vision/.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent

MATRICES = {
    "protanopia_machado100": np.array([
        [0.152286, 1.052583, -0.204868],
        [0.114503, 0.786281, 0.099216],
        [-0.003882, -0.048116, 1.051998]]),
    "deuteranopia_machado100": np.array([
        [0.367322, 0.860646, -0.227968],
        [0.280085, 0.672501, 0.047413],
        [-0.011820, 0.042940, 0.968881]]),
    "tritanopia_machado100": np.array([
        [1.255528, -0.076749, -0.178779],
        [-0.078411, 0.930809, 0.147602],
        [0.004733, 0.691367, 0.303900]]),
}


def simulate(arr: np.ndarray, m: np.ndarray) -> np.ndarray:
    out = arr.astype(np.float64) @ m.T
    return np.clip(out, 0, 255).astype(np.uint8)


def grayscale709(arr: np.ndarray) -> np.ndarray:
    y = arr @ np.array([0.2126, 0.7152, 0.0722])
    return np.clip(np.stack([y] * 3, axis=-1), 0, 255).astype(np.uint8)


def sheet(frames: list[np.ndarray], path: Path) -> None:
    cols, tw, th = 4, 480, 270
    rows = -(-len(frames) // cols)
    canvas = Image.new("RGB", (cols * tw, rows * th), (5, 8, 14))
    for i, arr in enumerate(frames):
        img = Image.fromarray(arr).resize((tw, th), Image.Resampling.LANCZOS)
        canvas.paste(img, ((i % cols) * tw, (i // cols) * th))
    canvas.save(path)


def main() -> int:
    canary = Path(sys.argv[1]).resolve()
    name = canary.name
    frames_dir = HERE / "qa" / name / "state_midpoints"
    out = HERE / "qa" / name / "color_vision"
    out.mkdir(parents=True, exist_ok=True)
    sources = sorted(frames_dir.glob("state_*.jpg"))
    if not sources:
        print(f"no state frames under {frames_dir}")
        return 2
    arrs = [np.asarray(Image.open(p).convert("RGB")) for p in sources]
    sheet(arrs, out / "contact_sheet_color.png")
    sheet([grayscale709(a) for a in arrs], out / "contact_sheet_grayscale_bt709.png")
    for key, m in MATRICES.items():
        sheet([simulate(a, m) for a in arrs], out / f"contact_sheet_{key}.png")
    print(f"{name}: {len(arrs)} frames -> 5 contact sheets in {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
