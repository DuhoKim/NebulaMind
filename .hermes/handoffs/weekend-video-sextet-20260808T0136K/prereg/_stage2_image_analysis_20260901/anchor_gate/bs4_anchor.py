#!/usr/bin/env python3
"""Draft-only BS-4 synthetic anchor; contains no study-image renderer."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from seal_gate.seal_gate import _seal_predecessor, canonical_bytes, sha256_bytes, sha256_file
from anchor_gate.instrument_identity import (INSTRUMENT, PIN, capture_environment,
                                             validate_environment, verify_instrument)

CONFIG = ROOT / "miniprereg_pins/render_config.json"
SPEC = ROOT / "miniprereg_pins/bs4_sign_anchor_spec.md"
WRONG_PARITY = "WRONG-PARITY-REFUSAL"


class AbsoluteAnchorFailure(RuntimeError):
    pass


def synthetic_wcs_reproject(*, source_jacobian=((1.0, 0.0), (0.0, 1.0))):
    """Minimal synthetic fiducial transform, explicitly NOT the study renderer."""
    det = source_jacobian[0][0] * source_jacobian[1][1] - source_jacobian[0][1] * source_jacobian[1][0]
    if det <= 0.0:
        return WRONG_PARITY
    # FITS/output: x grows left-to-right while east is decreasing x; north is +y.
    fiducials = {"N": (64.5, 65.5), "E": (63.5, 64.5)}
    assert fiducials["N"][1] > 64.5
    assert fiducials["E"][0] < 64.5
    assert det > 0.0
    return {"fiducials": fiducials, "jacobian_parity": "PRESERVED",
            "interpolation": "bilinear", "reprojections": 1}


def validate_geometry() -> dict:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    expected = {"raster_width_pixels": 128, "raster_height_pixels": 128,
                "pixel_scale_arcsec": 0.262, "crpix1": 64.5, "crpix2": 64.5,
                "orientation": "north-up/east-left", "neighbour_policy": "stitch-neighbours-first",
                "interpolation": "bilinear", "parity_policy": "parity-preserve",
                "parity_refusal_token": WRONG_PARITY}
    if cfg != expected:
        raise AbsoluteAnchorFailure("ABSOLUTE-ANCHOR-FAIL: renderer configuration mismatch")
    result = synthetic_wcs_reproject()
    if synthetic_wcs_reproject(source_jacobian=((-1.0, 0.0), (0.0, 1.0))) != WRONG_PARITY:
        raise AbsoluteAnchorFailure("ABSOLUTE-ANCHOR-FAIL: wrong-parity refusal mismatch")
    return result


def validate_fixture_output(proc: subprocess.CompletedProcess[str]) -> None:
    lines = proc.stdout.splitlines()
    sign = [line for line in lines if line.startswith("BATTERY-SIGN: PASS")]
    if proc.returncode != 0 or len(sign) != 1 or not lines or lines[-1] != "ALL FIXTURES PASS":
        raise AbsoluteAnchorFailure("ABSOLUTE-ANCHOR-FAIL: fixture output contract")


def run_anchor(*, journal: Path, runner=subprocess.run, timestamp: str | None = None) -> tuple[dict, str]:
    try:
        instrument_digest = verify_instrument()
        geometry = validate_geometry()
        env = validate_environment(capture_environment(instrument_digest))
        command = ["python3", "../_successor_build_20260824/ref/successor_ref_v9.py", "--fixtures"]
        proc = runner(command, cwd=ROOT, capture_output=True, text=True, check=False)
        validate_fixture_output(proc)
        stdout = proc.stdout
        input_digest = sha256_bytes(canonical_bytes({"config_sha256": sha256_file(CONFIG),
                                                      "spec_sha256": sha256_file(SPEC),
                                                      "synthetic_geometry": geometry}))
        body = {"timestamp": timestamp or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "operation": "bs4-synthetic-absolute-sign-anchor",
                "input_digest": input_digest,
                "expected_sign_convention": {"convention": "East-of-North", "A_LONGO": 0.0408,
                    "A_LONGO_PUBLISHED_SIGNED": -0.0408,
                    "criterion": "injected -0.0408 is never REPRODUCED-LONGO"},
                "instrument_digest": instrument_digest, "environment": env,
                "renderer": "ABSENT; synthetic-WCS reference only",
                "renderer_config_digest": sha256_file(CONFIG), "complete_stdout": stdout,
                "exit_status": proc.returncode, "output_digest": hashlib.sha256(stdout.encode()).hexdigest(),
                "status": "PASS", "verdict": "PASS",
                "predecessor_receipt_digest": _seal_predecessor(journal)}
        body["receipt_digest"] = sha256_bytes(canonical_bytes(body))
        return body, stdout
    except Exception as exc:
        if isinstance(exc, AbsoluteAnchorFailure):
            raise
        raise AbsoluteAnchorFailure(f"ABSOLUTE-ANCHOR-FAIL: {type(exc).__name__}: {exc}") from exc


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--journal", type=Path, default=ROOT / "seal_journal_tierc.jsonl")
    ap.add_argument("--append", action="store_true")
    args = ap.parse_args(argv)
    try:
        event, _ = run_anchor(journal=args.journal)
        if args.append:
            with args.journal.open("ab") as stream:
                stream.write(canonical_bytes(event))
        sys.stdout.buffer.write(canonical_bytes(event))
        return 0
    except AbsoluteAnchorFailure as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
