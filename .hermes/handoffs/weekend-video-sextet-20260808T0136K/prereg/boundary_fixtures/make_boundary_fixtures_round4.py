#!/usr/bin/env python3
"""Generate production-shaped RICE_1 image-HDU-1 boundary fixtures.

Round 4 changes only the FITS storage/read-path representation.  It reuses a
centre and corner from round 1 plus an exact extreme-declination edge from
round 3.  The geometry and expected arrays remain owned by those independent
fixture oracles; this module does not import or inspect the production adapter.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np
from astropy.io import fits

import make_boundary_fixtures as round1
import make_boundary_fixtures_round2 as round2
import make_boundary_fixtures_round3 as round3

PINNED_ROUND1_SHA256 = "24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d"
PINNED_ROUND2_SHA256 = "60e3d662d72fbc87e0c82889b4f9174c033882b8f9a2019011c5104bb4aa15bc"
PINNED_ROUND3_SHA256 = "6b410fb40def2869d4f3431f029654d8fa7cacd20741dca5a84b12409d5e5e62"
ROUND4_BRIEF_SHA256 = "17641b84ff89811534b1cb297d91c2da894dcd5ad3350920da0e528464748db2"

ROUND4_CASE_IDS = (
    "centre",
    "dec_max_exact_boundary",
    "corner_north_west_exact",
)
CASE_ROLES = {
    "centre": "centre",
    "dec_max_exact_boundary": "edge",
    "corner_north_west_exact": "corner",
}
CASE_SOURCE_ROUNDS = {
    "centre": "round1",
    "dec_max_exact_boundary": "round3",
    "corner_north_west_exact": "round1",
}

COMPRESSION_TYPE = "RICE_1"
RICE_TILE_SHAPE = (100, 100)
RICE_ABSOLUTE_QUANTIZATION = -1e-7
REQUIRED_RAW_COMPRESSION_KEYWORDS = (
    "ZIMAGE",
    "ZCMPTYPE",
    "ZNAXIS1",
    "ZNAXIS2",
    "ZTILE1",
    "ZTILE2",
)


def _read_raw_header_cards(blob: bytes, offset: int) -> tuple[dict[str, bytes], int]:
    """Read one FITS header as literal 80-byte cards from 2880-byte blocks."""
    cards: dict[str, bytes] = {}
    cursor = offset
    while True:
        block = blob[cursor : cursor + 2880]
        if len(block) != 2880:
            raise RuntimeError("truncated FITS header block")
        for card_offset in range(0, 2880, 80):
            card = block[card_offset : card_offset + 80]
            try:
                keyword = card[:8].decode("ascii").strip()
            except UnicodeDecodeError as error:
                raise RuntimeError("non-ASCII FITS header card") from error
            if keyword and keyword not in cards:
                cards[keyword] = card
            if keyword == "END":
                return cards, cursor + 2880
        cursor += 2880


def _verify_parent_custody() -> dict[str, str]:
    fixture_root = Path(__file__).resolve().parent
    observed = {
        "round1": round1.sha256_path(fixture_root / "make_boundary_fixtures.py"),
        "round2": round1.sha256_path(fixture_root / "make_boundary_fixtures_round2.py"),
        "round3": round1.sha256_path(fixture_root / "make_boundary_fixtures_round3.py"),
    }
    expected = {
        "round1": PINNED_ROUND1_SHA256,
        "round2": PINNED_ROUND2_SHA256,
        "round3": PINNED_ROUND3_SHA256,
    }
    if observed != expected:
        raise RuntimeError(
            "round-1/round-2/round-3 generator custody mismatch; round 4 refuses to generate"
        )
    return observed


def _round1_bricks() -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for row in (-1, 0, 1):
        for column in (-1, 0, 1):
            brick_id = f"r{row:+d}c{column:+d}"
            records[brick_id] = {
                "brick_id": brick_id,
                "source_round": "round1",
                "grid_row": row,
                "grid_column": column,
                "origin_x": column * round1.STRIDE,
                "origin_y": row * round1.STRIDE,
            }
    return records


def _selected_parent_contracts() -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    round1_cases = {row["object_id"]: row for row in round1.fixture_cases()}
    round3_geometry, round3_cases_list = round3.build_geometry_and_cases()
    round3_cases = {row["object_id"]: row for row in round3_cases_list}
    round3_bricks = {row["brick_id"]: row for row in round3_geometry}

    selected: list[dict[str, Any]] = []
    for object_id in ROUND4_CASE_IDS:
        source_round = CASE_SOURCE_ROUNDS[object_id]
        parent = round1_cases[object_id] if source_round == "round1" else round3_cases[object_id]
        row = json.loads(json.dumps(parent))
        row["source_round"] = source_round
        row["source_object_id"] = object_id
        row["fixture_role"] = CASE_ROLES[object_id]
        selected.append(row)

    source_records = _round1_bricks()
    source_records.update(
        {
            brick_id: {**json.loads(json.dumps(row)), "source_round": "round3"}
            for brick_id, row in round3_bricks.items()
        }
    )
    required_ids = sorted(
        {
            brick_id
            for object_row in selected
            for brick_id in object_row["expected_bricks"]
        }
    )
    return selected, {brick_id: source_records[brick_id] for brick_id in required_ids}


def _source_data_and_header(brick: dict[str, Any]) -> tuple[np.ndarray, fits.Header]:
    if brick["source_round"] == "round1":
        data = round1.brick_pattern(brick["origin_x"], brick["origin_y"])
        header = round1.brick_header(
            brick["origin_x"],
            brick["origin_y"],
            brick["grid_row"],
            brick["grid_column"],
        )
        return data, header
    if brick["source_round"] == "round3":
        data = round2._source_pattern(brick["wcs"], brick["value_offset"])
        return data, round2._source_header(brick)
    raise RuntimeError(f"unsupported parent fixture round: {brick['source_round']}")


def _parent_expected(
    object_row: dict[str, Any], source_records: dict[str, dict[str, Any]]
) -> np.ndarray:
    if object_row["source_round"] == "round1":
        return round1.expected_cutout(object_row["center_x"], object_row["center_y"])
    if object_row["source_round"] == "round3":
        expected, _ = round2._analytic_expected(object_row, source_records)
        return expected
    raise RuntimeError(f"unsupported parent fixture round: {object_row['source_round']}")


def _raw_compression_proof(path: Path) -> dict[str, Any]:
    blob = path.read_bytes()
    if not blob.startswith(b"SIMPLE  =") or blob.startswith(b"\x1f\x8b"):
        raise RuntimeError(f"{path.name} is not a FITS file with a raw primary header")
    primary_cards, extension_offset = _read_raw_header_cards(blob, 0)
    extension_cards, extension_data_offset = _read_raw_header_cards(blob, extension_offset)
    if b"NAXIS   =                    0" not in primary_cards.get("NAXIS", b""):
        raise RuntimeError(f"{path.name} primary HDU is not empty")
    missing = [keyword for keyword in REQUIRED_RAW_COMPRESSION_KEYWORDS if keyword not in extension_cards]
    if missing:
        raise RuntimeError(
            f"{path.name} raw extension header lacks tile-compression cards: {', '.join(missing)}"
        )

    with fits.open(path, memmap=False, disable_image_compression=True) as raw_hdus:
        if len(raw_hdus) != 2:
            raise RuntimeError(f"{path.name} must contain exactly primary plus image extension")
        header = raw_hdus[1].header
        if not header["ZIMAGE"] or header["ZCMPTYPE"] != COMPRESSION_TYPE:
            raise RuntimeError(f"{path.name} is not a raw {COMPRESSION_TYPE} compressed image table")
        axes = {
            "NAXIS1": int(header["NAXIS1"]),
            "NAXIS2": int(header["NAXIS2"]),
            "ZNAXIS1": int(header["ZNAXIS1"]),
            "ZNAXIS2": int(header["ZNAXIS2"]),
            "ZTILE1": int(header["ZTILE1"]),
            "ZTILE2": int(header["ZTILE2"]),
        }
    if axes["ZNAXIS1"] != round1.BRICK_SIZE or axes["ZNAXIS2"] != round1.BRICK_SIZE:
        raise RuntimeError(f"{path.name} has the wrong logical image dimensions")
    if axes["NAXIS1"] == axes["ZNAXIS1"] or axes["NAXIS2"] == axes["ZNAXIS2"]:
        raise RuntimeError(f"{path.name} does not distinguish compressed-table and image dimensions")

    return {
        "tile_compression_verified_from_raw_bytes": True,
        "primary_header_offset_bytes": 0,
        "extension_header_offset_bytes": extension_offset,
        "extension_data_offset_bytes": extension_data_offset,
        "raw_compression_header_cards": {
            keyword: extension_cards[keyword].decode("ascii")
            for keyword in REQUIRED_RAW_COMPRESSION_KEYWORDS
        },
        "raw_table_axes": axes,
    }


def _write_rice_brick(root: Path, brick: dict[str, Any]) -> dict[str, Any]:
    path = root / "bricks" / (
        f"synthetic-{brick['source_round']}-{brick['brick_id']}-image-r.fits.fz"
    )
    data, header = _source_data_and_header(brick)
    image = fits.CompImageHDU(
        data=data,
        header=header,
        compression_type=COMPRESSION_TYPE,
        quantize_level=RICE_ABSOLUTE_QUANTIZATION,
        tile_shape=RICE_TILE_SHAPE,
        name="IMAGE",
    )
    fits.HDUList([fits.PrimaryHDU(), image]).writeto(
        path,
        overwrite=False,
        checksum=True,
    )

    with fits.open(path, memmap=False) as logical_hdus:
        if len(logical_hdus) != 2 or logical_hdus[0].data is not None:
            raise RuntimeError(f"{path.name} does not expose an empty primary plus HDU-1 image")
        if not isinstance(logical_hdus[1], fits.CompImageHDU):
            raise RuntimeError(f"{path.name} HDU 1 is not a compressed image")
        restored = np.asarray(logical_hdus[1].data)
        if logical_hdus[1].compression_type != COMPRESSION_TYPE:
            raise RuntimeError(f"{path.name} logical compression type is not {COMPRESSION_TYPE}")
        if not np.array_equal(restored, data):
            mismatch_count = int(np.count_nonzero(restored != data))
            max_abs_error = float(
                np.max(np.abs(restored.astype(np.float64) - data.astype(np.float64)))
            )
            raise RuntimeError(
                f"{path.name} RICE round trip is not exact: "
                f"mismatches={mismatch_count}, max_abs_error={max_abs_error}"
            )

    record = json.loads(json.dumps(brick))
    record["relative_path"] = path.relative_to(root).as_posix()
    record["file_sha256"] = round1.sha256_path(path)
    record["data_sha256"] = hashlib.sha256(data.tobytes(order="C")).hexdigest()
    record["logical_image_hdu_index"] = 1
    record["primary_hdu_empty"] = True
    record["exact_float32_roundtrip"] = True
    record.update(_raw_compression_proof(path))
    return record


def generate_round4_fixture_tree(root: Path) -> dict[str, Any]:
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    (root / "bricks").mkdir(exist_ok=False)
    (root / "expected").mkdir(exist_ok=False)

    parent_hashes = _verify_parent_custody()
    objects, source_records = _selected_parent_contracts()
    bricks = [_write_rice_brick(root, source_records[brick_id]) for brick_id in source_records]
    written_records = {row["brick_id"]: row for row in bricks}

    for object_row in objects:
        expected = _parent_expected(object_row, source_records)
        expected_path = root / "expected" / f"{object_row['object_id']}.npy"
        np.save(expected_path, expected, allow_pickle=False)
        object_row["expected_array_path"] = expected_path.relative_to(root).as_posix()
        object_row["expected_array_sha256"] = round1.sha256_path(expected_path)
        object_row["expected_data_sha256"] = hashlib.sha256(
            expected.tobytes(order="C")
        ).hexdigest()
        object_row["storage_read_contract"] = {
            "image_hdu_index": 1,
            "compression_type": COMPRESSION_TYPE,
            "expected_source_bricks": [
                written_records[brick_id]["relative_path"]
                for brick_id in object_row["expected_bricks"]
            ],
        }

    objects_path = root / "objects.json"
    objects_path.write_text(
        json.dumps(objects, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    manifest: dict[str, Any] = {
        "schema_version": "yui-boundary-fixtures-round4-v1",
        "synthetic_only": True,
        "brief_sha256": ROUND4_BRIEF_SHA256,
        "parent_generator_sha256": parent_hashes,
        "object_count": len(objects),
        "brick_count": len(bricks),
        "case_ids": list(ROUND4_CASE_IDS),
        "objects_path": "objects.json",
        "objects_sha256": round1.sha256_path(objects_path),
        "brick_size": [round1.BRICK_SIZE, round1.BRICK_SIZE],
        "cutout_size": [round1.CUTOUT_SIZE, round1.CUTOUT_SIZE],
        "image_hdu_index": 1,
        "primary_hdu_empty": True,
        "compression_type": COMPRESSION_TYPE,
        "tile_shape": list(RICE_TILE_SHAPE),
        "quantize_level": RICE_ABSOLUTE_QUANTIZATION,
        "exact_roundtrip_contract": (
            "every selected float32 synthetic source must read back bit-for-bit identical; "
            "generation fails on any value difference and applies no tolerance"
        ),
        "raw_header_contract": {
            "required_keywords": list(REQUIRED_RAW_COMPRESSION_KEYWORDS),
            "compressed_table_axes_must_differ_from_logical_image_axes": True,
        },
        "scope": {
            "fixture_purpose": "production-shaped .fits.fz image-HDU-1 read-path test",
            "tests_production_shaped_fits_fz_hdu1_read_path": True,
            "tests_raw_compressed_table_header_axes": True,
            "tests_exact_selected_parent_expectations": True,
            "introduces_new_geometry": False,
            "validates_production_adapter": False,
            "uses_real_survey_data": False,
            "uses_network": False,
            "proves_general_float_codec_losslessness": False,
            "proves_real_dr10_transfer_or_endpoint_behavior": False,
        },
        "bricks": bricks,
    }
    (root / "fixture_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def verify_round4_fixture_tree(root: Path) -> dict[str, Any]:
    """Replay the generated tree against raw FITS bytes and the parent oracles."""
    root = Path(root)
    _verify_parent_custody()
    manifest_path = root / "fixture_manifest.json"
    objects_path = root / "objects.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    objects = json.loads(objects_path.read_text(encoding="utf-8"))
    if manifest["schema_version"] != "yui-boundary-fixtures-round4-v1":
        raise RuntimeError("round-4 manifest schema mismatch")
    if manifest["objects_sha256"] != round1.sha256_path(objects_path):
        raise RuntimeError("round-4 objects table digest mismatch")
    if [row["object_id"] for row in objects] != list(ROUND4_CASE_IDS):
        raise RuntimeError("round-4 object case list mismatch")

    _, parent_source_records = _selected_parent_contracts()
    bricks = {row["brick_id"]: row for row in manifest["bricks"]}
    if set(bricks) != set(parent_source_records):
        raise RuntimeError("round-4 brick set differs from selected parent source set")

    raw_proofs = 0
    exact_source_roundtrips = 0
    axis_divergences = 0
    for brick_id, brick in bricks.items():
        path = root / brick["relative_path"]
        if round1.sha256_path(path) != brick["file_sha256"]:
            raise RuntimeError(f"{brick_id} file digest mismatch")
        proof = _raw_compression_proof(path)
        if proof["raw_compression_header_cards"] != brick["raw_compression_header_cards"]:
            raise RuntimeError(f"{brick_id} raw compression cards differ from manifest")
        if proof["raw_table_axes"] != brick["raw_table_axes"]:
            raise RuntimeError(f"{brick_id} raw table axes differ from manifest")
        raw_proofs += 1
        axes = proof["raw_table_axes"]
        if axes["NAXIS1"] != axes["ZNAXIS1"] and axes["NAXIS2"] != axes["ZNAXIS2"]:
            axis_divergences += 1

        expected_data, _ = _source_data_and_header(parent_source_records[brick_id])
        with fits.open(path, memmap=False) as logical_hdus:
            restored = np.asarray(logical_hdus[1].data)
        if not np.array_equal(restored, expected_data):
            raise RuntimeError(f"{brick_id} differs from its exact parent source array")
        observed_data_sha256 = hashlib.sha256(restored.tobytes(order="C")).hexdigest()
        if observed_data_sha256 != brick["data_sha256"]:
            raise RuntimeError(f"{brick_id} logical data digest mismatch")
        exact_source_roundtrips += 1

    exact_parent_expectations = 0
    for object_row in objects:
        expected_path = root / object_row["expected_array_path"]
        if round1.sha256_path(expected_path) != object_row["expected_array_sha256"]:
            raise RuntimeError(f"{object_row['object_id']} expected-array file digest mismatch")
        expected = np.load(expected_path, allow_pickle=False)
        parent_expected = _parent_expected(object_row, parent_source_records)
        if not np.array_equal(expected, parent_expected):
            raise RuntimeError(
                f"{object_row['object_id']} differs from its exact parent expectation"
            )
        observed_data_sha256 = hashlib.sha256(expected.tobytes(order="C")).hexdigest()
        if observed_data_sha256 != object_row["expected_data_sha256"]:
            raise RuntimeError(f"{object_row['object_id']} expected-data digest mismatch")
        exact_parent_expectations += 1

    regular_files = [path for path in root.rglob("*") if path.is_file()]
    return {
        "status": "PASS_REPLAYED_SYNTHETIC_BOUNDARY_FIXTURES_ROUND4",
        "case_ids": list(ROUND4_CASE_IDS),
        "brick_count": len(bricks),
        "object_count": len(objects),
        "raw_tile_compression_proof_count": raw_proofs,
        "exact_source_roundtrip_count": exact_source_roundtrips,
        "compressed_table_axis_divergence_count": axis_divergences,
        "exact_parent_expectation_count": exact_parent_expectations,
        "regular_file_count": len(regular_files),
        "total_generated_bytes": sum(path.stat().st_size for path in regular_files),
        "manifest_sha256": round1.sha256_path(manifest_path),
        "objects_sha256": round1.sha256_path(objects_path),
    }


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main() -> int:
    arguments = build_argument_parser().parse_args()
    manifest = generate_round4_fixture_tree(arguments.output)
    print(
        json.dumps(
            {
                "status": "PASS_GENERATED_SYNTHETIC_BOUNDARY_FIXTURES_ROUND4",
                "bricks": manifest["brick_count"],
                "objects": manifest["object_count"],
                "compression_type": manifest["compression_type"],
                "image_hdu_index": manifest["image_hdu_index"],
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
