#!/usr/bin/env python3
"""Deterministic display-only IC-6 tensor to PNG renderer.

Transform DISPLAY-LIN-NEG1-POS1-V1:
- input is exactly 65,536 bytes: one C-order (1,128,128) little-endian float32 tensor;
- all samples must be finite;
- each sample x is clipped to the fixed global interval [-1, +1];
- grayscale byte is floor((clip(x,-1,1)+1)*127.5 + 0.5), cast to uint8;
- bytes are laid out as 128 C-order rows in Pillow mode L;
- PNG uses no metadata, optimize=False, compress_level=9.

There is no per-image normalization. PNG outputs are for HC-1H display only and must
never be used as input to chi or any machine score.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import sys
from pathlib import Path
from typing import Sequence

import numpy as np
from PIL import Image

IC6_BYTES = 65_536
DISPLAY_TRANSFORM = "DISPLAY-LIN-NEG1-POS1-V1"


class RenderContractError(RuntimeError):
    pass


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def render_tensor_to_png(source: Path, destination: Path) -> dict[str, str]:
    source = Path(source)
    payload = source.read_bytes()
    if len(payload) != IC6_BYTES:
        raise RenderContractError(f"IC-6 tensor must contain exactly {IC6_BYTES} bytes: {source}")
    tensor = np.frombuffer(payload, dtype="<f4").reshape(1, 128, 128)
    if not np.all(np.isfinite(tensor)):
        raise RenderContractError(f"IC-6 tensor contains nonfinite values: {source}")
    pixels = np.floor((np.clip(tensor[0], -1.0, 1.0) + 1.0) * 127.5 + 0.5).astype(
        np.uint8
    )
    image = Image.frombytes("L", (128, 128), pixels.tobytes(order="C"))
    encoded = io.BytesIO()
    image.save(encoded, format="PNG", optimize=False, compress_level=9)
    png = encoded.getvalue()
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    temporary.write_bytes(png)
    os.replace(temporary, destination)
    return {
        "source_tensor_sha256": _sha256(payload),
        "display_png_sha256": _sha256(png),
        "display_transform": DISPLAY_TRANSFORM,
        "use": "HC-1H display only; forbidden as chi input",
    }


def _manifest_paths(path: Path) -> list[Path]:
    text = Path(path).read_text(encoding="utf-8")
    try:
        document = json.loads(text)
    except json.JSONDecodeError:
        values = [line for line in text.splitlines() if line]
    else:
        if not isinstance(document, list) or not all(
            isinstance(value, str) and value for value in document
        ):
            raise RenderContractError("input manifest JSON must be a list of nonempty path strings")
        values = document
    if not values:
        raise RenderContractError("input manifest is empty")
    return [Path(value) for value in values]


def render_manifest(input_manifest: Path, output_dir: Path, bindings: Path) -> int:
    rows = []
    for source in _manifest_paths(input_manifest):
        source_payload = source.read_bytes()
        object_id = f"{source.stem}-{_sha256(source_payload)[:16]}"
        destination = Path(output_dir) / f"{object_id}.png"
        binding = render_tensor_to_png(source, destination)
        rows.append({"object_id": object_id, "tensor_path": str(source), "image_path": str(destination), **binding})
    bindings = Path(bindings)
    bindings.parent.mkdir(parents=True, exist_ok=True)
    temporary = bindings.with_suffix(bindings.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")
    os.replace(temporary, bindings)
    return len(rows)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--bindings", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        rendered = render_manifest(args.input_manifest, args.output_dir, args.bindings)
    except RenderContractError as exc:
        print(json.dumps({"status": "REFUSED", "message": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps({"status": "PASS", "rendered": rendered}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
