#!/usr/bin/env python3
"""Audit FITS pixel-to-sky parity without computing any sky statistic."""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Union

import numpy as np
from astropy.io import fits


@dataclass(frozen=True)
class ParityAudit:
    matrix_source: str
    matrix: tuple[tuple[float, float], tuple[float, float]]
    determinant: float
    parity: str
    certainty: str


@dataclass(frozen=True)
class ArrayConversion:
    data: np.ndarray
    row_order: str
    array_transform_determinant: int
    header: fits.Header


def _linear_matrix(header: fits.Header) -> tuple[str, np.ndarray]:
    cd_keys = ("CD1_1", "CD1_2", "CD2_1", "CD2_2")
    if any(key in header for key in cd_keys) and not all(key in header for key in cd_keys):
        raise ValueError("incomplete CD matrix; refusing fallback to PC/CDELT")
    if all(key in header for key in cd_keys):
        return "CD", np.array(
            [
                [float(header["CD1_1"]), float(header["CD1_2"])],
                [float(header["CD2_1"]), float(header["CD2_2"])],
            ],
            dtype=np.float64,
        )

    pc11 = float(header.get("PC1_1", header.get("PC001001", 1.0)))
    pc12 = float(header.get("PC1_2", header.get("PC001002", 0.0)))
    pc21 = float(header.get("PC2_1", header.get("PC002001", 0.0)))
    pc22 = float(header.get("PC2_2", header.get("PC002002", 1.0)))
    if "CDELT1" not in header or "CDELT2" not in header:
        raise ValueError("header has neither a complete CD matrix nor PC with CDELT1/2")
    pc = np.array([[pc11, pc12], [pc21, pc22]], dtype=np.float64)
    cdelt = np.diag([float(header["CDELT1"]), float(header["CDELT2"])])
    return "PC*CDELT", cdelt @ pc


def audit_header(header: fits.Header) -> ParityAudit:
    """Return the parity of the 2-D linear FITS pixel-to-sky mapping."""

    ctype1 = str(header.get("CTYPE1", ""))
    ctype2 = str(header.get("CTYPE2", ""))
    if not (ctype1.startswith(("RA---", "GLON-", "ELON-")) and ctype2.startswith(("DEC--", "GLAT-", "ELAT-"))):
        raise ValueError("CTYPE1/2 are not a celestial longitude/latitude axis pair")
    distortion_prefixes = ("A_", "B_", "AP_", "BP_", "PV1_", "PV2_", "CPDIS", "DET2IM")
    if "-SIP" in ctype1 or "-SIP" in ctype2 or any(
        str(key).startswith(distortion_prefixes) for key in header.keys()
    ):
        raise ValueError("distortion keywords present; linear determinant alone is insufficient")
    source, matrix = _linear_matrix(header)
    determinant = float(np.linalg.det(matrix))
    if not np.isfinite(determinant) or determinant == 0.0:
        raise ValueError(f"singular or non-finite linear WCS determinant: {determinant!r}")
    scale = max(float(np.linalg.norm(matrix, ord=np.inf)) ** 2, 1.0)
    tolerance = np.finfo(np.float64).eps * scale * 16.0
    if abs(determinant) <= tolerance:
        raise ValueError(
            f"numerically indeterminate linear WCS determinant: {determinant!r}; "
            f"tolerance={tolerance!r}"
        )
    parity = "PRESERVING" if determinant > 0.0 else "REVERSING"
    return ParityAudit(
        matrix_source=source,
        matrix=tuple(tuple(float(value) for value in row) for row in matrix),
        determinant=determinant,
        parity=parity,
        certainty="DETERMINATE_LINEAR_WCS",
    )


def fits_to_array(
    input_path: Union[str, Path], *, row_order: str = "fits-native"
) -> ArrayConversion:
    """Load one 2-D image HDU while making row order and its parity explicit."""

    with fits.open(input_path, memmap=False, do_not_scale_image_data=False) as hdul:
        hdu = next((candidate for candidate in hdul if candidate.data is not None), None)
        if hdu is None or hdu.data is None:
            raise ValueError("FITS contains no image data")
        data = np.array(hdu.data, copy=True)
        header = hdu.header.copy()

    if data.ndim != 2:
        raise ValueError(f"expected one 2-D image plane, found shape {data.shape!r}")
    if row_order == "fits-native":
        return ArrayConversion(
            data=data,
            row_order="FITS_NATIVE_Y_INCREASES_WITH_NUMPY_ROW",
            array_transform_determinant=1,
            header=header,
        )
    if row_order == "top-left":
        return ArrayConversion(
            data=np.flipud(data).copy(),
            row_order="TOP_LEFT_VERTICAL_FLIP_FROM_FITS_NATIVE",
            array_transform_determinant=-1,
            header=header,
        )
    raise ValueError("row_order must be 'fits-native' or 'top-left'")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _wcs_cards_digest(header: fits.Header) -> str:
    prefixes = (
        "CTYPE",
        "CRVAL",
        "CRPIX",
        "CD",
        "PC",
        "CDELT",
        "CUNIT",
        "RADESYS",
        "EQUINOX",
        "LONPOLE",
        "LATPOLE",
        "PV",
        "A_",
        "B_",
        "AP_",
        "BP_",
        "CPDIS",
        "DET2IM",
    )
    cards = [
        (str(key), repr(header[key]))
        for key in header.keys()
        if str(key).startswith(prefixes)
    ]
    payload = json.dumps(cards, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def convert_fits_to_npy(
    input_path: Union[str, Path],
    output_path: Union[str, Path],
    *,
    row_order: str = "fits-native",
) -> dict[str, Any]:
    """Write a lossless NumPy raster plus a machine-readable transform receipt."""

    source = Path(input_path).resolve()
    output = Path(output_path).resolve()
    converted = fits_to_array(source, row_order=row_order)
    output.parent.mkdir(parents=True, exist_ok=True)
    np.save(output, converted.data, allow_pickle=False)
    round_trip = np.load(output, allow_pickle=False)
    parity = audit_header(converted.header)
    return {
        "input_path": str(source),
        "input_sha256": _sha256(source),
        "output_path": str(output),
        "output_sha256": _sha256(output),
        "shape": list(converted.data.shape),
        "dtype": str(converted.data.dtype),
        "row_order": converted.row_order,
        "array_transform_determinant": converted.array_transform_determinant,
        "lossless_byte_equal": round_trip.tobytes() == converted.data.tobytes(),
        "wcs_matrix_source": parity.matrix_source,
        "wcs_determinant": parity.determinant,
        "wcs_parity": parity.parity,
        "combined_pixel_to_output_sky_determinant_sign": (
            1 if parity.determinant * converted.array_transform_determinant > 0 else -1
        ),
    }


def audit_fits_file(
    input_path: Union[str, Path], *, row_order: str = "fits-native"
) -> dict[str, Any]:
    """Audit one FITS image's bytes, linear WCS parity, and declared row order."""

    source = Path(input_path).resolve()
    converted = fits_to_array(source, row_order=row_order)
    parity = audit_header(converted.header)
    combined_sign = (
        1
        if parity.determinant * converted.array_transform_determinant > 0.0
        else -1
    )
    return {
        "input_path": str(source),
        "input_bytes": source.stat().st_size,
        "input_sha256": _sha256(source),
        "shape": list(converted.data.shape),
        "dtype": str(converted.data.dtype),
        "ctype": [
            str(converted.header.get("CTYPE1", "")),
            str(converted.header.get("CTYPE2", "")),
        ],
        "radesys": converted.header.get("RADESYS"),
        "matrix_source": parity.matrix_source,
        "linear_matrix": [list(row) for row in parity.matrix],
        "wcs_determinant": parity.determinant,
        "wcs_parity": parity.parity,
        "certainty": parity.certainty,
        "row_order": converted.row_order,
        "array_transform_determinant": converted.array_transform_determinant,
        "combined_pixel_to_output_sky_determinant_sign": combined_sign,
        "combined_mapping_parity": "PRESERVING" if combined_sign > 0 else "REVERSING",
        "chirality_computed": False,
    }


def _spiral_image(size: int, pixel_chirality: int) -> np.ndarray:
    if size < 9:
        raise ValueError("synthetic spiral size must be at least 9")
    yy, xx = np.indices((size, size), dtype=np.float64)
    center = (size - 1) / 2.0
    x = xx - center
    y = yy - center
    radius = np.hypot(x, y)
    theta = np.arctan2(y, x)
    scale = size / 7.0
    pitch = 0.34
    radial_target = scale * np.exp(pixel_chirality * pitch * theta)
    arm_a = np.exp(-0.5 * ((radius - radial_target) / 1.1) ** 2)
    theta_b = np.where(theta >= 0.0, theta - np.pi, theta + np.pi)
    radial_target_b = scale * np.exp(pixel_chirality * pitch * theta_b)
    arm_b = np.exp(-0.5 * ((radius - radial_target_b) / 1.1) ** 2)
    core = 0.35 * np.exp(-0.5 * (radius / 2.0) ** 2)
    taper = np.exp(-((radius / (0.48 * size)) ** 8))
    image = (arm_a + arm_b + core) * taper
    return image.astype(np.float32)


def _synthetic_header(size: int, wcs_parity: str, sky_chirality: int) -> fits.Header:
    if wcs_parity not in {"PRESERVING", "REVERSING"}:
        raise ValueError("wcs_parity must be PRESERVING or REVERSING")
    if sky_chirality not in {-1, 1}:
        raise ValueError("sky_chirality must be -1 or +1")
    header = fits.Header()
    header["CTYPE1"] = "RA---TAN"
    header["CTYPE2"] = "DEC--TAN"
    header["CRVAL1"] = 180.0
    header["CRVAL2"] = 0.0
    header["CRPIX1"] = (size + 1) / 2.0
    header["CRPIX2"] = (size + 1) / 2.0
    header["CD1_1"] = 1.0e-4 if wcs_parity == "PRESERVING" else -1.0e-4
    header["CD1_2"] = 0.0
    header["CD2_1"] = 0.0
    header["CD2_2"] = 1.0e-4
    header["RADESYS"] = "ICRS"
    header["SYNTHET"] = True
    header["SKYCHIR"] = sky_chirality
    header["PIXCIR"] = sky_chirality * (1 if wcs_parity == "PRESERVING" else -1)
    return header


def create_synthetic_spiral_fits(
    output_path: Union[str, Path],
    *,
    wcs_parity: str,
    sky_chirality: int,
    size: int = 65,
) -> Path:
    """Create a synthetic calibration frame with declared sky/pixel chirality."""

    path = Path(output_path).resolve()
    header = _synthetic_header(size, wcs_parity, sky_chirality)
    data = _spiral_image(size, int(header["PIXCIR"]))
    path.parent.mkdir(parents=True, exist_ok=True)
    fits.PrimaryHDU(data=data, header=header).writeto(path, overwrite=False)
    return path


def inject_synthetic_spiral(
    base_path: Union[str, Path],
    output_path: Union[str, Path],
    *,
    sky_chirality: int,
) -> dict[str, Any]:
    """Replace calibration-frame pixels with a known chirality, retaining WCS."""

    source = Path(base_path).resolve()
    output = Path(output_path).resolve()
    converted = fits_to_array(source, row_order="fits-native")
    if converted.data.shape[0] != converted.data.shape[1]:
        raise ValueError("synthetic injection currently requires a square calibration frame")
    parity = audit_header(converted.header)
    wcs_digest_before = _wcs_cards_digest(converted.header)
    wcs_sign = 1 if parity.determinant > 0.0 else -1
    pixel_chirality = sky_chirality * wcs_sign
    injected = _spiral_image(converted.data.shape[0], pixel_chirality)
    header = converted.header.copy()
    header["SYNTHET"] = True
    header["SKYCHIR"] = sky_chirality
    header["PIXCIR"] = pixel_chirality
    output.parent.mkdir(parents=True, exist_ok=True)
    fits.PrimaryHDU(data=injected, header=header).writeto(output, overwrite=False)
    written = fits_to_array(output, row_order="fits-native")
    wcs_after = audit_header(written.header)
    wcs_digest_after = _wcs_cards_digest(written.header)
    wcs_unchanged = parity == wcs_after and wcs_digest_before == wcs_digest_after
    return {
        "base_path": str(source),
        "base_sha256": _sha256(source),
        "output_path": str(output),
        "output_sha256": _sha256(output),
        "base_shape": list(converted.data.shape),
        "declared_sky_chirality": sky_chirality,
        "injected_pixel_chirality": pixel_chirality,
        "wcs_parity": parity.parity,
        "wcs_cards_unchanged": wcs_unchanged,
        "wcs_cards_sha256_before": wcs_digest_before,
        "wcs_cards_sha256_after": wcs_digest_after,
        "status": (
            "PASS_SYNTHETIC_INJECTION" if wcs_unchanged else "FAIL_WCS_CHANGED"
        ),
    }


def mirror_synthetic_fits(
    input_path: Union[str, Path], output_path: Union[str, Path]
) -> dict[str, Any]:
    """Mirror a synthetic calibration raster exactly while retaining its WCS."""

    source = Path(input_path).resolve()
    output = Path(output_path).resolve()
    converted = fits_to_array(source, row_order="fits-native")
    if converted.header.get("SYNTHET") is not True or "SKYCHIR" not in converted.header:
        raise ValueError("mirroring is permitted for synthetic calibration frames only")
    mirrored_data = np.flip(converted.data, axis=1)
    header = converted.header.copy()
    wcs_before = audit_header(header)
    header["SKYCHIR"] = -int(header["SKYCHIR"])
    header["PIXCIR"] = -int(header["PIXCIR"])
    output.parent.mkdir(parents=True, exist_ok=True)
    fits.PrimaryHDU(data=mirrored_data, header=header).writeto(output, overwrite=False)
    written = fits_to_array(output, row_order="fits-native")
    wcs_after = audit_header(written.header)
    pixels_exact = np.array_equal(written.data, np.flip(converted.data, axis=1))
    wcs_unchanged = wcs_before == wcs_after
    return {
        "input_path": str(source),
        "output_path": str(output),
        "input_sha256": _sha256(source),
        "output_sha256": _sha256(output),
        "pixels_exact_horizontal_mirror": pixels_exact,
        "wcs_header_unchanged": wcs_unchanged,
        "original_declared_sky_chirality": -int(header["SKYCHIR"]),
        "mirrored_declared_sky_chirality": int(header["SKYCHIR"]),
        "status": (
            "PASS_EXACT_MIRROR_SWAP"
            if pixels_exact and wcs_unchanged
            else "FAIL_MIRROR_CUSTODY"
        ),
    }


def _estimate_pixel_chirality(data: np.ndarray) -> int:
    """Match the synthetic calibration image against both known-parity templates."""

    if data.ndim != 2 or data.shape[0] != data.shape[1]:
        raise ValueError("synthetic chirality estimator requires a square 2-D image")
    values = np.asarray(data, dtype=np.float64)
    values = values - np.nanmean(values)
    scores: dict[int, float] = {}
    for candidate in (-1, 1):
        template = np.asarray(_spiral_image(data.shape[0], candidate), dtype=np.float64)
        template = template - np.mean(template)
        scores[candidate] = float(np.nansum(values * template))
    if not all(np.isfinite(score) for score in scores.values()):
        raise ValueError("synthetic chirality estimator is indeterminate")
    if scores[-1] == scores[1]:
        raise ValueError("synthetic chirality estimator is tied")
    return max(scores, key=scores.get)


def recover_synthetic_chirality(
    input_path: Union[str, Path],
    *,
    row_order: str,
    honor_array_transform: bool = True,
) -> dict[str, Any]:
    """Recover a known synthetic sky sign and expose any silent row flip."""

    converted = fits_to_array(input_path, row_order=row_order)
    if converted.header.get("SYNTHET") is not True or "SKYCHIR" not in converted.header:
        raise ValueError("chirality recovery is permitted for synthetic calibration frames only")
    parity = audit_header(converted.header)
    expected = int(converted.header["SKYCHIR"])
    pixel_chirality = _estimate_pixel_chirality(converted.data)
    array_sign = converted.array_transform_determinant if honor_array_transform else 1
    wcs_sign = 1 if parity.determinant > 0.0 else -1
    recovered = pixel_chirality * array_sign * wcs_sign
    return {
        "input_path": str(Path(input_path).resolve()),
        "expected_sky_chirality": expected,
        "estimated_output_array_chirality": pixel_chirality,
        "wcs_parity": parity.parity,
        "array_transform_determinant": converted.array_transform_determinant,
        "honored_array_transform": honor_array_transform,
        "recovered_sky_chirality": recovered,
        "status": (
            "PASS"
            if recovered == expected
            else "FAIL_SILENT_ROW_FLIP_DETECTED"
        ),
    }


def scramble_wcs(
    input_path: Union[str, Path], output_path: Union[str, Path]
) -> dict[str, Any]:
    """Flip one WCS axis without changing pixels and prove the mismatch is detected."""

    source = Path(input_path).resolve()
    output = Path(output_path).resolve()
    converted = fits_to_array(source, row_order="fits-native")
    original = audit_header(converted.header)
    header = converted.header.copy()
    if original.matrix_source != "CD":
        raise ValueError("scrambled-WCS harness currently requires an explicit CD matrix")
    header["CD1_1"] = -float(header["CD1_1"])
    header["CD1_2"] = -float(header["CD1_2"])
    output.parent.mkdir(parents=True, exist_ok=True)
    fits.PrimaryHDU(data=converted.data, header=header).writeto(output, overwrite=False)
    scrambled = audit_header(header)
    recovery = recover_synthetic_chirality(output, row_order="fits-native")
    expected = int(header["SKYCHIR"])
    return {
        "original_path": str(source),
        "scrambled_path": str(output),
        "pixels_byte_equal": fits_to_array(source).data.tobytes()
        == fits_to_array(output).data.tobytes(),
        "original_wcs_parity": original.parity,
        "scrambled_wcs_parity": scrambled.parity,
        "expected_sky_chirality": expected,
        "recovered_sky_chirality": recovery["recovered_sky_chirality"],
        "status": (
            "PASS_FAULT_DETECTED"
            if recovery["recovered_sky_chirality"] == -expected
            else "FAIL_FAULT_NOT_DETECTED"
        ),
    }


def run_synthetic_harness(output_dir: Union[str, Path]) -> dict[str, Any]:
    """Create and exercise the complete synthetic pixel-path calibration set."""

    root = Path(output_dir).resolve()
    root.mkdir(parents=True, exist_ok=True)
    frames: list[dict[str, Any]] = []
    recoveries: list[dict[str, Any]] = []
    paths: dict[str, Path] = {}
    for parity_name in ("PRESERVING", "REVERSING"):
        for chirality, suffix in ((-1, "minus"), (1, "plus")):
            name = f"synthetic_{parity_name.lower()}_{suffix}"
            path = root / f"{name}.fits"
            create_synthetic_spiral_fits(
                path, wcs_parity=parity_name, sky_chirality=chirality
            )
            paths[name] = path
            frames.append(
                {
                    "name": name,
                    "audit": audit_fits_file(path),
                    "native_conversion": convert_fits_to_npy(
                        path, root / f"{name}.fits-native.npy"
                    ),
                }
            )
            recoveries.append(
                {
                    "name": name,
                    **recover_synthetic_chirality(path, row_order="fits-native"),
                }
            )

    top_left_source = paths["synthetic_preserving_plus"]
    explicit_top_left = recover_synthetic_chirality(
        top_left_source, row_order="top-left", honor_array_transform=True
    )
    silent_top_left = recover_synthetic_chirality(
        top_left_source, row_order="top-left", honor_array_transform=False
    )
    top_left_conversion = convert_fits_to_npy(
        top_left_source,
        root / "synthetic_preserving_plus.top-left.npy",
        row_order="top-left",
    )
    scrambled_name = "synthetic_preserving_minus_scrambled_wcs"
    scrambled_path = root / f"{scrambled_name}.fits"
    scrambled_control = scramble_wcs(
        paths["synthetic_preserving_minus"], scrambled_path
    )
    frames.append(
        {
            "name": scrambled_name,
            "audit": audit_fits_file(scrambled_path),
            "native_conversion": convert_fits_to_npy(
                scrambled_path, root / f"{scrambled_name}.fits-native.npy"
            ),
        }
    )
    mirror_name = "synthetic_reversing_minus_mirrored"
    mirror_path = root / f"{mirror_name}.fits"
    mirror_receipt = mirror_synthetic_fits(
        paths["synthetic_reversing_minus"], mirror_path
    )
    mirror_control = {
        "receipt": mirror_receipt,
        "original_recovery": recover_synthetic_chirality(
            paths["synthetic_reversing_minus"], row_order="fits-native"
        ),
        "mirrored_recovery": recover_synthetic_chirality(
            mirror_path, row_order="fits-native"
        ),
    }
    frames.append(
        {
            "name": mirror_name,
            "audit": audit_fits_file(mirror_path),
            "native_conversion": convert_fits_to_npy(
                mirror_path, root / f"{mirror_name}.fits-native.npy"
            ),
        }
    )
    summary = (
        "PASS_SYNTHETIC_PIXEL_PATH_AUDIT"
        if all(item["status"] == "PASS" for item in recoveries)
        and explicit_top_left["status"] == "PASS"
        and silent_top_left["status"] == "FAIL_SILENT_ROW_FLIP_DETECTED"
        and scrambled_control["status"] == "PASS_FAULT_DETECTED"
        and mirror_receipt["status"] == "PASS_EXACT_MIRROR_SWAP"
        and mirror_control["mirrored_recovery"]["recovered_sky_chirality"]
        == -mirror_control["original_recovery"]["recovered_sky_chirality"]
        else "FAIL_SYNTHETIC_PIXEL_PATH_AUDIT"
    )
    return {
        "scope": "SYNTHETIC_CALIBRATION_FRAMES_ONLY_NO_SKY_STATISTIC",
        "frames": frames,
        "recoveries": recoveries,
        "top_left_conversion_control": top_left_conversion,
        "explicit_top_left_control": explicit_top_left,
        "silent_row_flip_control": silent_top_left,
        "scrambled_wcs_control": scrambled_control,
        "mirror_control": mirror_control,
        "summary": summary,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Audit FITS WCS/row-order parity without computing sky statistics."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    audit = subparsers.add_parser("audit", help="audit one FITS file without chirality")
    audit.add_argument("input_path")
    audit.add_argument(
        "--row-order", choices=("fits-native", "top-left"), default="fits-native"
    )
    harness = subparsers.add_parser(
        "harness", help="create and run synthetic injected-image controls"
    )
    harness.add_argument("--output-dir", required=True)
    convert = subparsers.add_parser("convert", help="losslessly write a NumPy raster")
    convert.add_argument("input_path")
    convert.add_argument("output_path")
    convert.add_argument(
        "--row-order", choices=("fits-native", "top-left"), default="fits-native"
    )
    inject = subparsers.add_parser(
        "inject", help="replace calibration pixels with a known synthetic chirality"
    )
    inject.add_argument("base_path")
    inject.add_argument("output_path")
    inject.add_argument("--sky-chirality", choices=(-1, 1), type=int, required=True)
    scramble = subparsers.add_parser(
        "scramble-wcs", help="flip one WCS axis on a synthetic calibration frame"
    )
    scramble.add_argument("input_path")
    scramble.add_argument("output_path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "audit":
        result = audit_fits_file(args.input_path, row_order=args.row_order)
    elif args.command == "harness":
        result = run_synthetic_harness(args.output_dir)
    elif args.command == "convert":
        result = convert_fits_to_npy(
            args.input_path, args.output_path, row_order=args.row_order
        )
    elif args.command == "inject":
        injection = inject_synthetic_spiral(
            args.base_path,
            args.output_path,
            sky_chirality=args.sky_chirality,
        )
        result = {
            "injection": injection,
            "audit": audit_fits_file(args.output_path),
            "recovery": recover_synthetic_chirality(
                args.output_path, row_order="fits-native"
            ),
        }
    elif args.command == "scramble-wcs":
        result = scramble_wcs(args.input_path, args.output_path)
    else:  # pragma: no cover - argparse owns command validation
        raise AssertionError(args.command)
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
