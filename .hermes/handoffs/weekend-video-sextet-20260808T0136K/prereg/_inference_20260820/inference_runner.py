#!/usr/bin/env python3
"""Frozen CE-ResNet inference runner with a synthetic-only default boundary.

Real-data execution is fail-closed. No input is opened until scope and, when
required, an exact SHA-256-pinned authorization artifact have been verified.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import struct
import sys
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
import torch
from torch import nn

HERE = Path(__file__).resolve().parent
PREREG_ROOT = HERE.parent
WEIGHTS_PATH = PREREG_ROOT / "weights_frozen.pt"
WEIGHTS_SHA256 = "83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d"
COMMITTEE_PATH = PREREG_ROOT / "_committee_20260820" / "committee.py"
COMMITTEE_SHA256 = "c1438d7f1d45fb04b950e3344fd7286244e1d09f659f88208e61f23eb6dc3a95"
COMMITTEE_WEIGHTS_PATH = PREREG_ROOT / "_committee_20260820" / "member_b_weights_frozen.pt"
COMMITTEE_WEIGHTS_SHA256 = "6e4a6efaf9e9db55e8ca23f1ffa7e61ef437c62bc959c9630b90db0d18aeff0a"
REAL_TENSOR_ROOT = Path("/Users/duhokim/NebulaMindData/cutouts_dr10_south/tensors")
AUTHORIZATION_SHA256 = "c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69"
IC6_SHAPE = (1, 128, 128)
IC6_DTYPE = np.dtype("<f4")
IC6_BYTES = 65_536
VALIDATION_DOMAIN = "GPT2-INFERENCE-SYNTHETIC-VALIDATE-20260820"


class ContractError(RuntimeError):
    def __init__(self, message: str, *, code: str, detail: dict | None = None) -> None:
        super().__init__(message)
        self.code = code
        self.detail = dict(detail or {})


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def configure_deterministic_runtime() -> None:
    torch.set_num_threads(1)
    try:
        torch.set_num_interop_threads(1)
    except RuntimeError:
        # PyTorch permits setting inter-op threads only before parallel work starts.
        # A prior identical process-wide setting is acceptable; any non-1 value is not.
        if torch.get_num_interop_threads() != 1:
            raise
    torch.use_deterministic_algorithms(True)
    if hasattr(torch.backends, "mkldnn"):
        torch.backends.mkldnn.enabled = False


class BasicBlock(nn.Module):
    def __init__(self, in_channels: int, out_channels: int, stride: int) -> None:
        super().__init__()
        self.c1 = nn.Conv2d(in_channels, out_channels, 3, stride, 1, bias=False)
        self.b1 = nn.BatchNorm2d(out_channels)
        self.c2 = nn.Conv2d(out_channels, out_channels, 3, 1, 1, bias=False)
        self.b2 = nn.BatchNorm2d(out_channels)
        self.sh = (
            nn.Sequential()
            if stride == 1 and in_channels == out_channels
            else nn.Sequential(
                nn.Conv2d(in_channels, out_channels, 1, stride, bias=False),
                nn.BatchNorm2d(out_channels),
            )
        )

    def forward(self, value: torch.Tensor) -> torch.Tensor:
        hidden = torch.relu(self.b1(self.c1(value)))
        return torch.relu(self.b2(self.c2(hidden)) + self.sh(value))


class FrozenTrunk(nn.Module):
    """Exact frozen ResNet-18-class topology used to serialize weights_frozen.pt."""

    def __init__(self) -> None:
        super().__init__()
        layers: list[nn.Module] = [
            nn.Conv2d(1, 32, 3, 1, 1, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(),
        ]
        widths = [32, 64, 128, 256]
        for stage, width in enumerate(widths):
            prior = widths[max(stage - 1, 0)] if stage else 32
            layers.extend(
                [
                    BasicBlock(prior, width, 1 if stage == 0 else 2),
                    BasicBlock(width, width, 1),
                ]
            )
        layers.extend([nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(256, 1)])
        self.f = nn.Sequential(*layers)

    def forward(self, value: torch.Tensor) -> torch.Tensor:
        return self.f(value).squeeze(-1)


def load_frozen_model(path: Path = WEIGHTS_PATH) -> FrozenTrunk:
    configure_deterministic_runtime()
    path = Path(path)
    actual = sha256_file(path)
    if actual != WEIGHTS_SHA256:
        raise ContractError(
            "frozen primary weights SHA-256 mismatch",
            code="REFUSED_WEIGHTS_SHA256",
            detail={"expected": WEIGHTS_SHA256, "actual": actual, "path": str(path)},
        )
    model = FrozenTrunk().to(device="cpu", dtype=torch.float32)
    state = torch.load(path, map_location="cpu", weights_only=True)
    model.load_state_dict(state, strict=True)
    model.eval()
    for parameter in model.parameters():
        parameter.requires_grad_(False)
    return model


def _is_within(path: Path, root: Path) -> bool:
    # resolve(strict=False) closes a synthetic-flag bypass through a symlink
    # without opening or reading the target tensor.
    absolute = Path(path).resolve(strict=False)
    root_absolute = Path(root).resolve(strict=False)
    return absolute == root_absolute or root_absolute in absolute.parents


def verify_authorization(path: Path | None) -> str:
    if path is None:
        raise ContractError(
            "real-data inference requires --authorization FILE",
            code="REFUSED_REAL_DATA_UNAUTHORIZED",
        )
    actual = sha256_file(Path(path))
    if actual != AUTHORIZATION_SHA256:
        raise ContractError(
            "authorization SHA-256 mismatch",
            code="REFUSED_AUTHORIZATION_SHA256",
            detail={"expected": AUTHORIZATION_SHA256, "actual": actual},
        )
    return actual


def guard_input_scope(path: Path, *, synthetic: bool, authorization: Path | None = None) -> None:
    # A path in the real tensor root is real regardless of a contradictory flag.
    real_path = _is_within(Path(path), REAL_TENSOR_ROOT)
    if real_path or not synthetic:
        verify_authorization(authorization)


def read_ic6_tensor(
    path: Path,
    *,
    synthetic: bool,
    authorization: Path | None = None,
) -> tuple[torch.Tensor, str]:
    path = Path(path)
    guard_input_scope(path, synthetic=synthetic, authorization=authorization)
    with path.open("rb") as handle:
        payload = handle.read(IC6_BYTES + 1)
    if len(payload) != IC6_BYTES:
        raise ContractError(
            "IC-6 tensor must contain exactly 65,536 bytes",
            code="REFUSED_IC6_BYTE_LENGTH",
            detail={"actual": len(payload), "expected": IC6_BYTES},
        )
    array = np.frombuffer(payload, dtype=IC6_DTYPE).reshape(IC6_SHAPE).copy(order="C")
    if array.dtype != IC6_DTYPE or not array.flags.c_contiguous:
        raise ContractError("IC-6 layout postcondition failed", code="REFUSED_IC6_LAYOUT")
    return torch.from_numpy(array), sha256_bytes(payload)


def mirror_tensor(tensor: torch.Tensor) -> torch.Tensor:
    if tensor.dtype != torch.float32 or tuple(tensor.shape) != IC6_SHAPE or tensor.device.type != "cpu":
        raise ContractError("mirror requires a CPU float32 IC-6 tensor", code="REFUSED_MIRROR_INPUT")
    return torch.flip(tensor, dims=[2])


def chi_tensor(model: FrozenTrunk, tensor: torch.Tensor) -> torch.Tensor:
    if model.training:
        raise ContractError("primary model must remain in eval mode", code="REFUSED_MODEL_TRAIN_MODE")
    image = tensor.unsqueeze(0)
    with torch.inference_mode():
        # One shared model object is applied twice. Mirror is width-axis index reversal only.
        return ((model(image) - model(torch.flip(image, dims=[3]))) / 2.0)[0]


def float32_bits(value: torch.Tensor | float) -> int:
    scalar = np.float32(value.item() if isinstance(value, torch.Tensor) else value)
    return int(scalar.view(np.uint32))


def chi_bits(model: FrozenTrunk, tensor: torch.Tensor) -> int:
    return float32_bits(chi_tensor(model, tensor))


def negated_float32_bits(bits: int) -> int:
    return int(bits) ^ 0x80000000


def bits_to_float32(bits: int) -> float:
    return float(struct.unpack("<f", struct.pack("<I", bits))[0])


def _load_pinned_committee_module():
    actual = sha256_file(COMMITTEE_PATH)
    if actual != COMMITTEE_SHA256:
        raise ContractError(
            "HC-1H committee code SHA-256 mismatch",
            code="REFUSED_COMMITTEE_CODE_SHA256",
            detail={"expected": COMMITTEE_SHA256, "actual": actual},
        )
    module_name = "gpt2_inference_pinned_hc1h_committee"
    existing = sys.modules.get(module_name)
    if existing is not None:
        return existing
    specification = importlib.util.spec_from_file_location(module_name, COMMITTEE_PATH)
    if specification is None or specification.loader is None:
        raise ContractError("cannot import HC-1H committee", code="REFUSED_COMMITTEE_IMPORT")
    module = importlib.util.module_from_spec(specification)
    sys.modules[module_name] = module
    specification.loader.exec_module(module)
    return module


_COMMITTEE_MODULE = None


def committee_module():
    global _COMMITTEE_MODULE
    if _COMMITTEE_MODULE is None:
        _COMMITTEE_MODULE = _load_pinned_committee_module()
    return _COMMITTEE_MODULE


def synthetic_sample(domain: str, index: int) -> tuple[np.ndarray, int]:
    return committee_module().synth_sample(domain, index)


class Committee:
    """HC-1H stratification metadata; this API has no primary-chi parameter."""

    def __init__(self) -> None:
        configure_deterministic_runtime()
        module = committee_module()
        actual = sha256_file(COMMITTEE_WEIGHTS_PATH)
        if actual != COMMITTEE_WEIGHTS_SHA256:
            raise ContractError(
                "HC-1H member-B weights SHA-256 mismatch",
                code="REFUSED_COMMITTEE_WEIGHTS_SHA256",
                detail={"expected": COMMITTEE_WEIGHTS_SHA256, "actual": actual},
            )
        self.module = module
        self.member_b = module.SmallPlainCNN().to(device="cpu", dtype=torch.float32)
        state = torch.load(COMMITTEE_WEIGHTS_PATH, map_location="cpu", weights_only=True)
        self.member_b.load_state_dict(state, strict=True)
        self.member_b.eval()
        for parameter in self.member_b.parameters():
            parameter.requires_grad_(False)

    def classify(self, image: np.ndarray) -> dict:
        image = np.ascontiguousarray(image, dtype=np.float32)
        score_a = self.module.geometric_chi(image)
        sign_a = self.module.accepted_sign(score_a, self.module.GEOMETRIC_THRESHOLD)
        with torch.inference_mode():
            score_b = self.module.cnn_chi(self.member_b, image)
        sign_b = self.module.accepted_sign(score_b, self.module.CNN_THRESHOLD)
        state = self.module.committee_state(sign_a, sign_b)
        return {
            "member_a_score": score_a,
            "member_a_sign": sign_a,
            "member_b_score": score_b,
            "member_b_sign": sign_b,
            "state": state,
        }


def code_sha256() -> str:
    return sha256_file(Path(__file__).resolve())


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _atomic_json(path: Path, value: object) -> None:
    payload = _canonical_json(value) + b"\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(payload)
    os.replace(temporary, path)


def _read_ledger(path: Path) -> dict[str, dict]:
    rows: dict[str, dict] = {}
    if not path.exists():
        return rows
    with path.open("rb") as handle:
        for line_number, line in enumerate(handle, start=1):
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ContractError(
                    f"malformed append-only ledger line {line_number}", code="REFUSED_LEDGER_CORRUPTION"
                ) from exc
            digest = row.get("input_tensor_sha256")
            if not isinstance(digest, str) or digest in rows:
                raise ContractError("ledger has missing/duplicate input hash", code="REFUSED_LEDGER_CORRUPTION")
            rows[digest] = row
    return rows


def _append_ledger(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = _canonical_json(row) + b"\n"
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    try:
        os.write(descriptor, payload)
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def resolve_input_paths(
    inputs: Sequence[Path] | None,
    input_manifest: Path | None,
) -> list[Path]:
    if (inputs is None) == (input_manifest is None):
        raise ContractError(
            "provide exactly one of --inputs or --input-manifest",
            code="REFUSED_INPUT_TRANSPORT",
        )
    if inputs is not None:
        return [Path(path) for path in inputs]
    assert input_manifest is not None
    text = Path(input_manifest).read_text(encoding="utf-8")
    try:
        document = json.loads(text)
    except json.JSONDecodeError:
        paths = [line for line in text.splitlines() if line]
    else:
        if not isinstance(document, list) or not all(
            isinstance(path, str) and path for path in document
        ):
            raise ContractError(
                "input manifest JSON must be a list of nonempty path strings",
                code="REFUSED_INPUT_TRANSPORT",
            )
        paths = document
    if not paths:
        raise ContractError("input manifest is empty", code="REFUSED_INPUT_TRANSPORT")
    return [Path(path) for path in paths]


def run_paths(
    paths: Iterable[Path],
    output_dir: Path,
    *,
    synthetic: bool,
    authorization: Path | None = None,
) -> dict[str, int]:
    configure_deterministic_runtime()
    if not synthetic:
        # Validate authorization once before model or committee loading and before any input access.
        verify_authorization(authorization)
    model = load_frozen_model()
    committee = Committee()
    output_dir = Path(output_dir)
    ledger_path = output_dir / "results.jsonl"
    ledger = _read_ledger(ledger_path)
    current_code_sha = code_sha256()
    processed = 0
    resumed = 0
    for raw_path in paths:
        path = Path(raw_path)
        tensor, input_sha = read_ic6_tensor(path, synthetic=synthetic, authorization=authorization)
        prior = ledger.get(input_sha)
        if prior is not None:
            if prior.get("weights_sha256") != WEIGHTS_SHA256 or prior.get("code_sha256") != current_code_sha:
                raise ContractError(
                    "resume refused because frozen code/weights identity changed",
                    code="REFUSED_RESUME_IDENTITY_MISMATCH",
                )
            receipt_path = output_dir / "receipts" / f"{prior['object_id']}.json"
            if not receipt_path.is_file() or sha256_file(receipt_path) != prior.get("receipt_sha256"):
                raise ContractError("resume receipt missing or changed", code="REFUSED_RESUME_RECEIPT_MISMATCH")
            resumed += 1
            continue
        bits = chi_bits(model, tensor)
        chi_value = bits_to_float32(bits)
        committee_metadata = committee.classify(tensor.numpy()[0])
        object_id = f"{path.stem}-{input_sha[:16]}"
        receipt = {
            "receipt_version": 1,
            "scope": "SYNTHETIC" if synthetic else "REAL_AUTHORIZED",
            "object_id": object_id,
            "input_path": str(path),
            "input_tensor_sha256": input_sha,
            "input_layout": {"shape": list(IC6_SHAPE), "dtype": "<f4", "order": "C", "bytes": IC6_BYTES},
            "chi_value": chi_value,
            "chi_bits_hex": f"0x{bits:08x}",
            "committee_state": committee_metadata["state"],
            "committee_metadata": committee_metadata,
            "committee_use": "HC-1H stratification metadata only; never inside chi",
            "weights_sha256": WEIGHTS_SHA256,
            "committee_weights_sha256": COMMITTEE_WEIGHTS_SHA256,
            "code_sha256": current_code_sha,
        }
        receipt_path = output_dir / "receipts" / f"{object_id}.json"
        _atomic_json(receipt_path, receipt)
        row = {
            "object_id": object_id,
            "input_tensor_sha256": input_sha,
            "chi_value": chi_value,
            "chi_bits_hex": f"0x{bits:08x}",
            "committee_state": committee_metadata["state"],
            "weights_sha256": WEIGHTS_SHA256,
            "code_sha256": current_code_sha,
            "receipt_sha256": sha256_file(receipt_path),
        }
        _append_ledger(ledger_path, row)
        ledger[input_sha] = row
        processed += 1
    return {"processed": processed, "resumed": resumed}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    transport = parser.add_mutually_exclusive_group(required=True)
    transport.add_argument("--inputs", type=Path, nargs="+")
    transport.add_argument(
        "--input-manifest",
        type=Path,
        help="UTF-8 file containing one tensor path per line or a JSON path list",
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--synthetic", action="store_true", help="declare all inputs synthetic")
    parser.add_argument("--authorization", type=Path)
    arguments = parser.parse_args(argv)
    try:
        paths = resolve_input_paths(arguments.inputs, arguments.input_manifest)
        result = run_paths(
            paths,
            arguments.output_dir,
            synthetic=arguments.synthetic,
            authorization=arguments.authorization,
        )
    except ContractError as exc:
        print(json.dumps({"status": "REFUSED", "code": exc.code, "message": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps({"status": "PASS", **result}, sort_keys=True))
    return 0


configure_deterministic_runtime()

if __name__ == "__main__":
    raise SystemExit(main())
