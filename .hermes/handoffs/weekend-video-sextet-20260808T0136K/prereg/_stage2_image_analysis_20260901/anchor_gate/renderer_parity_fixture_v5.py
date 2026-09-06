# renderer_parity_fixture_v5 (Tier-C V37 draft): identical to its V35 §8.17a predecessor except that the renderer is renderer_v4 (import + metadata string).
#!/usr/bin/env python3
"""Renderer parity and configuration fixture (V27: imports instrument_identity_v4, which
probes venv_torch and hashes the runner; V20-V26 recorded a fabricated instrument environment).

What this is: a synthetic end-to-end check that the pinned renderer preserves
orientation and parity, and that the pinned configuration matches the frozen
§8 constants. What this is NOT: it does not exercise the CE-ResNet instrument
and establishes no absolute handedness. The absolute-sign framing this file
carried as BS-4 was withdrawn in V20, together with its reference-implementation
fixture battery, which exercised a script §9.1a excludes from this study.
Failures route to verdict classes that already exist: a parity or orientation
failure is WRONG-PARITY-REFUSAL, anything else DATA-INTEGRITY-FAIL.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from astropy.wcs import WCS

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from seal_gate.seal_gate import _seal_predecessor, canonical_bytes, sha256_bytes, sha256_file
from anchor_gate.instrument_identity_v4 import (INSTRUMENT, PIN, capture_environment,
                                             validate_environment, verify_instrument)
from study_renderer.renderer_v4 import CD, render_cutout

CONFIG = ROOT / "miniprereg_pins/render_config_v2.json"
SPEC = ROOT / "miniprereg_pins/renderer_parity_fixture_spec_v2.md"
WRONG_PARITY = "WRONG-PARITY-REFUSAL"
DATA_INTEGRITY = "DATA-INTEGRITY-FAIL"


class RendererParityFixtureFailure(RuntimeError):
    pass


def synthetic_wcs_reproject(*, source_jacobian=((1.0, 0.0), (0.0, 1.0)), nexp_value=1):
    """Run asymmetric labelled N/E fiducials through the actual renderer."""
    det = source_jacobian[0][0] * source_jacobian[1][1] - source_jacobian[0][1] * source_jacobian[1][0]
    w = WCS(naxis=2); w.wcs.ctype=["RA---TAN","DEC--TAN"]; w.wcs.cunit=["deg","deg"]
    w.wcs.crval=[40.0,10.0]; w.wcs.crpix=[90.5,90.5]; w.wcs.cd=CD.copy()
    if det <= 0: w.wcs.cd[0,0] *= -1
    w.array_shape=(180,180); w.wcs.set()
    image=np.zeros((180,180)); image[108,89]=10; image[89,70]=20
    nexp=np.full(image.shape, nexp_value, dtype=np.int16)
    try:
        raster=render_cutout([(image,np.zeros_like(image),nexp,w)],(40.0,10.0))
    except ValueError as exc:
        if str(exc) == WRONG_PARITY: return WRONG_PARITY
        raise
    north=np.unravel_index(np.argmax(raster.array[:,58:69]),raster.array[:,58:69].shape)
    east=np.unravel_index(np.argmax(raster.array[58:69]),raster.array[58:69].shape)
    fiducials={"N":(float(north[1]+58),float(north[0])),
               "E":(float(east[1]),float(east[0]+58))}
    if not (fiducials["N"][1] > 63.5 and fiducials["E"][0] < 63.5):
        raise RendererParityFixtureFailure(f"{WRONG_PARITY}: renderer fiducial orientation")
    return {"fiducials":fiducials,"jacobian_parity":"PRESERVED",
            "interpolation":"bilinear","reprojections":1,"renderer_digest":raster.digest}


def validate_geometry() -> dict:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    expected = {"raster_width_pixels": 128, "raster_height_pixels": 128,
                "pixel_scale_arcsec": 0.262, "crpix1": 64.5, "crpix2": 64.5,
                "orientation": "north-up/east-left", "neighbour_policy": "single-brick-containment",
                "interpolation": "bilinear-image-nearest-integer-planes", "parity_policy": "parity-preserve",
                "parity_refusal_token": WRONG_PARITY}
    if cfg != expected:
        raise RendererParityFixtureFailure(f"{DATA_INTEGRITY}: renderer configuration mismatch")
    result = synthetic_wcs_reproject()
    if synthetic_wcs_reproject(source_jacobian=((-1.0, 0.0), (0.0, 1.0))) != WRONG_PARITY:
        raise RendererParityFixtureFailure(f"{WRONG_PARITY}: wrong-parity refusal mismatch")
    return result


def run_fixture(*, journal: Path, timestamp: str | None = None) -> tuple[dict, str]:
    try:
        instrument_digest, runner_digest = verify_instrument()
        geometry = validate_geometry()
        env = validate_environment(capture_environment(instrument_digest, runner_digest))
        input_digest = sha256_bytes(canonical_bytes({"config_sha256": sha256_file(CONFIG),
                                                      "spec_sha256": sha256_file(SPEC),
                                                      "synthetic_geometry": geometry}))
        body = {"timestamp": timestamp or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "operation": "renderer-parity-and-configuration-fixture",
                "input_digest": input_digest,
                "establishes_absolute_sign": False,
                "instrument_digest": instrument_digest, "environment": env,
                "renderer": "study_renderer.renderer_v4.render_cutout",
                "renderer_config_digest": sha256_file(CONFIG),
                "output_digest": sha256_bytes(canonical_bytes(geometry)),
                "status": "PASS", "verdict": "PASS",
                "predecessor_receipt_digest": _seal_predecessor(journal)}
        body["receipt_digest"] = sha256_bytes(canonical_bytes(body))
        return body, ""
    except Exception as exc:
        if isinstance(exc, RendererParityFixtureFailure):
            raise
        raise RendererParityFixtureFailure(f"{DATA_INTEGRITY}: {type(exc).__name__}: {exc}") from exc


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--journal", type=Path, default=ROOT / "seal_journal_tierc.jsonl")
    ap.add_argument("--append", action="store_true")
    args = ap.parse_args(argv)
    try:
        event, _ = run_fixture(journal=args.journal)
        if args.append:
            with args.journal.open("ab") as stream:
                stream.write(canonical_bytes(event))
        sys.stdout.buffer.write(canonical_bytes(event))
        return 0
    except RendererParityFixtureFailure as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
