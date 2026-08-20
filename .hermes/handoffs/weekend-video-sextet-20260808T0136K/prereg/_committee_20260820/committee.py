#!/usr/bin/env python3
"""Synthetic-only HC-1H committee members and state mapping."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
import sys
from pathlib import Path
from typing import Sequence, Tuple

import numpy as np
import torch
from torch import nn

HERE = Path(__file__).resolve().parent
PREREG_ROOT = HERE.parent
if str(PREREG_ROOT) not in sys.path:
    sys.path.insert(0, str(PREREG_ROOT))
from committee_state_vocabulary import COMMITTEE_STATES, to_hc1h

AGREE_CONFIDENT, DISAGREE, LOW_CONFIDENCE = COMMITTEE_STATES
MEMBER_B_WEIGHTS_PATH = HERE / "member_b_weights_frozen.pt"
MEMBER_B_WEIGHTS_SHA256 = "6e4a6efaf9e9db55e8ca23f1ffa7e61ef437c62bc959c9630b90db0d18aeff0a"
GENERATOR_PATH = HERE.parent.parent / "spike" / "yui_identity" / "w_chi.py"
GENERATOR_SHA256 = "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75"
GEOMETRIC_THRESHOLD = 0.08
CNN_THRESHOLD = 0.15
TRAIN_DOMAIN = "HC1H-COMMITTEE-B-TRAIN-20260820"
VALIDATION_DOMAIN = "HC1H-COMMITTEE-VALIDATE-20260820"
TRAIN_SEED = 20260820
IC6_BYTES = 65_536


class ContractError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


if sha256_file(GENERATOR_PATH) != GENERATOR_SHA256:
    raise RuntimeError("frozen BS-3 generator hash mismatch")
_spec = importlib.util.spec_from_file_location("hc1h_frozen_bs3_generator", GENERATOR_PATH)
if _spec is None or _spec.loader is None:
    raise RuntimeError("cannot load frozen BS-3 generator")
_generator = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_generator)


def domain_seed(domain: str, index: int, purpose: str = "parameters") -> int:
    payload = f"{domain}||{index}||{purpose}".encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big") % (2**63)


def synth_parameters(domain: str, index: int) -> Tuple[int, float, float, float, float, float]:
    rng = np.random.default_rng(domain_seed(domain, index))
    parity = 1 if index % 2 == 0 else -1
    pitch = float(rng.uniform(10.0, 40.0))
    inclination = float(rng.uniform(0.0, 60.0))
    snr = float(np.exp(rng.uniform(np.log(2.0), np.log(50.0))))
    arm_amplitude = float(rng.uniform(0.5, 1.1))
    phase = float(rng.uniform(0.0, 2.0 * np.pi))
    return parity, pitch, inclination, snr, arm_amplitude, phase


def synth_sample(domain: str, index: int) -> Tuple[np.ndarray, int]:
    parity, pitch, inclination, snr, arm_amplitude, phase = synth_parameters(domain, index)
    image = _generator.synth_spiral(
        parity,
        pitch,
        inclination,
        snr,
        seed=domain_seed(domain, index, "noise"),
        arms=2,
        arm_amp=arm_amplitude,
        phase=phase,
    )
    return np.ascontiguousarray(image, dtype=np.float32), parity


def mirror(image: np.ndarray) -> np.ndarray:
    return np.ascontiguousarray(np.fliplr(image))


_y, _x = np.mgrid[0:128, 0:128]
_dx = _x - 63.5
_dy = _y - 63.5
_radius = np.hypot(_dx, _dy)
_theta = np.arctan2(_dy, _dx)
_annulus_edges = np.linspace(10.0, 48.0, 13)
_annulus_masks = [
    (_radius >= _annulus_edges[i]) & (_radius < _annulus_edges[i + 1])
    for i in range(12)
]
_mode_factor = np.exp(-2j * _theta)
_border_mask = _radius >= 54.0


def geometric_raw(image: np.ndarray) -> float:
    array = np.asarray(image, dtype=np.float64)
    residual = np.maximum(array - np.median(array[_border_mask]), 0.0)
    modes = np.asarray([np.sum(residual[mask] * _mode_factor[mask]) for mask in _annulus_masks])
    amplitudes = np.abs(modes)
    valid = amplitudes > 1e-12
    modes = modes[valid]
    amplitudes = amplitudes[valid]
    if len(modes) < 3:
        return 0.0
    numerators = np.imag(modes[1:] * np.conjugate(modes[:-1]))
    denominators = amplitudes[1:] * amplitudes[:-1]
    increments = numerators / denominators
    weights = np.sqrt(denominators)
    return float(-np.sum(weights * increments) / np.sum(weights))


def geometric_chi(image: np.ndarray) -> float:
    image = np.ascontiguousarray(image, dtype=np.float32)
    return (geometric_raw(image) - geometric_raw(mirror(image))) / 2.0


def accepted_sign(score: float, threshold: float) -> int:
    if abs(score) <= threshold:
        return 0
    return 1 if score > 0.0 else -1


def committee_state(member_a: int, member_b: int) -> str:
    if member_a == 0 or member_b == 0:
        return LOW_CONFIDENCE
    if member_a == member_b:
        return AGREE_CONFIDENT
    return DISAGREE


class SmallPlainCNN(nn.Module):
    """Plain sequential CNN; no residual blocks or shared CE-ResNet trunk."""

    def __init__(self) -> None:
        super().__init__()
        self.conv_stack = nn.Sequential(
            nn.Conv2d(1, 8, kernel_size=5, stride=2, padding=2),
            nn.ReLU(),
            nn.Conv2d(8, 16, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 24, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),
        )
        self.output = nn.Linear(24, 1)

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        return self.output(self.conv_stack(images).flatten(1)).squeeze(1)


def cnn_chi_batch(model: nn.Module, images: torch.Tensor) -> torch.Tensor:
    return (model(images) - model(torch.flip(images, dims=[3]))) / 2.0


def cnn_chi(model: nn.Module, image: np.ndarray) -> float:
    tensor = torch.from_numpy(np.ascontiguousarray(image, dtype=np.float32))[None, None]
    with torch.no_grad():
        return float(cnn_chi_batch(model, tensor).item())


def canonical_parameter_hash(model: nn.Module) -> str:
    digest = hashlib.sha256()
    for name, parameter in sorted(model.state_dict().items()):
        encoded_name = name.encode("utf-8")
        digest.update(len(encoded_name).to_bytes(4, "little"))
        digest.update(encoded_name)
        array = parameter.detach().cpu().contiguous().numpy().astype("<f4", copy=False)
        digest.update(array.tobytes(order="C"))
    return digest.hexdigest()


def load_frozen_member_b(path: Path = MEMBER_B_WEIGHTS_PATH) -> SmallPlainCNN:
    path = Path(path)
    actual = sha256_file(path)
    if actual != MEMBER_B_WEIGHTS_SHA256:
        raise ContractError(
            f"member-B weights SHA-256 mismatch: expected {MEMBER_B_WEIGHTS_SHA256}, got {actual}"
        )
    model = SmallPlainCNN().to(device="cpu", dtype=torch.float32)
    model.load_state_dict(torch.load(path, map_location="cpu", weights_only=True), strict=True)
    model.eval()
    for parameter in model.parameters():
        parameter.requires_grad_(False)
    return model


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
            raise ContractError("input manifest JSON must be a list of nonempty path strings")
        values = document
    if not values:
        raise ContractError("input manifest is empty")
    return [Path(value) for value in values]


def score_manifest(input_manifest: Path, output: Path) -> int:
    model = load_frozen_member_b()
    rows = []
    for path in _manifest_paths(input_manifest):
        payload = path.read_bytes()
        if len(payload) != IC6_BYTES:
            raise ContractError(f"IC-6 tensor must contain exactly {IC6_BYTES} bytes: {path}")
        image = np.frombuffer(payload, dtype="<f4").reshape(128, 128).copy(order="C")
        if not np.all(np.isfinite(image)):
            raise ContractError(f"IC-6 tensor contains nonfinite values: {path}")
        score_a = geometric_chi(image)
        sign_a = accepted_sign(score_a, GEOMETRIC_THRESHOLD)
        score_b = cnn_chi(model, image)
        sign_b = accepted_sign(score_b, CNN_THRESHOLD)
        state = committee_state(sign_a, sign_b)
        rows.append(
            {
                "input_path": str(path),
                "input_tensor_sha256": hashlib.sha256(payload).hexdigest(),
                "member_a_score": score_a,
                "member_a_sign": sign_a,
                "member_b_score": score_b,
                "member_b_sign": sign_b,
                "state": state,
                "hc1h_state": to_hc1h(state),
                "member_b_weights_sha256": MEMBER_B_WEIGHTS_SHA256,
            }
        )
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(output.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(
                json.dumps(row, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n"
            )
    os.replace(temporary, output)
    return len(rows)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Score an IC-6 tensor manifest with the frozen HC-1H committee."
    )
    parser.add_argument("--input-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        count = score_manifest(args.input_manifest, args.output)
    except ContractError as exc:
        print(json.dumps({"status": "REFUSED", "message": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps({"status": "PASS", "scored": count}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
