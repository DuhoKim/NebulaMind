#!/usr/bin/env python3
"""Build deterministic, receipt-gated object-to-brick manifests for cutout_runner."""
from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import importlib.util
import io
import json
import math
import os
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Optional, Sequence

HERE = Path(__file__).resolve().parent
PREREG = HERE.parent
RUNNER_PATH = PREREG / "_cutout_runner_20260820" / "cutout_runner.py"
PINNED_ADAPTER_SHA256 = "267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f"
OFFICIAL_SIDECAR_SHA256 = "863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a"
OFFICIAL_POSITIONS_SHA256 = "0edfdef08361f1606f714e59c0dd1472d4d13e357a75df2173824da1ca8ff8ab"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class ManifestBuildError(RuntimeError):
    pass


@dataclass(frozen=True)
class Position:
    ra: float
    dec: float
    ls_id: str


@dataclass(frozen=True)
class AcceptedBrick:
    brickname: str
    destination_relative_path: str
    local_sha256: str


class GeometryIndex:
    def __init__(self, rows: Iterable[Mapping[str, object]], *, sidecar_sha256: str) -> None:
        normalized = []
        seen = set()
        required = ("brickname", "brickid", "ra", "dec", "ra1", "ra2", "dec1", "dec2")
        for source in rows:
            try:
                row = {
                    "brickname": str(source["brickname"]).strip(),
                    "brickid": int(source["brickid"]),
                    "ra": float(source["ra"]),
                    "dec": float(source["dec"]),
                    "ra1": float(source["ra1"]),
                    "ra2": float(source["ra2"]),
                    "dec1": float(source["dec1"]),
                    "dec2": float(source["dec2"]),
                }
            except (KeyError, TypeError, ValueError) as exc:
                raise ManifestBuildError(f"invalid geometry row; required fields are {required}") from exc
            if not row["brickname"] or row["brickname"] in seen:
                raise ManifestBuildError(f"duplicate or empty geometry brickname: {row['brickname']!r}")
            if not all(math.isfinite(row[key]) for key in ("ra", "dec", "ra1", "ra2", "dec1", "dec2")):
                raise ManifestBuildError(f"nonfinite geometry row: {row['brickname']}")
            seen.add(row["brickname"])
            normalized.append(row)
        if not normalized:
            raise ManifestBuildError("geometry sidecar has no rows")
        normalized.sort(key=lambda row: (row["dec"], row["brickname"]))
        self.rows = normalized
        self.decs = [row["dec"] for row in normalized]
        self.by_name = {row["brickname"]: row for row in normalized}
        self.sidecar_sha256 = sidecar_sha256

    def declination_candidates(self, dec: float, radius: float) -> list[dict]:
        low = bisect.bisect_left(self.decs, dec - radius)
        high = bisect.bisect_right(self.decs, dec + radius)
        return self.rows[low:high]


class _GeometryView:
    def __init__(self, rows: list[dict]) -> None:
        self.rows = rows


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_runner():
    existing = sys.modules.get("nm_objmanifest_pinned_runner")
    if existing is not None:
        return existing
    spec = importlib.util.spec_from_file_location("nm_objmanifest_pinned_runner", RUNNER_PATH)
    if spec is None or spec.loader is None:
        raise ManifestBuildError(f"cannot import cutout runner: {RUNNER_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if module.ADAPTER_SHA256 != PINNED_ADAPTER_SHA256:
        raise ManifestBuildError("cutout runner adapter pin differs from object-manifest pin")
    return module


def _adapter():
    return _load_runner()._adapter()


def planner_module_sha256() -> str:
    adapter = _adapter()
    return _sha256_file(Path(adapter.__file__))


def _verify_companion_sha256(path: Path, actual: str) -> bool:
    companion = path.with_suffix(path.suffix + ".sha256")
    if not companion.is_file():
        return False
    fields = companion.read_text(encoding="ascii").strip().split()
    if not fields or fields[0].lower() != actual:
        raise ManifestBuildError(f"geometry sidecar companion digest mismatch: {companion}")
    return True


def _verify_fixture_manifest(path: Path, actual: str) -> bool:
    manifest_path = path.parent / "fixture_manifest.json"
    if not manifest_path.is_file():
        return False
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("geometry_sidecar_path") != path.name:
        return False
    expected = str(manifest.get("geometry_sidecar_sha256", "")).lower()
    if expected != actual:
        raise ManifestBuildError(f"geometry sidecar fixture-manifest digest mismatch: {path}")
    return True


def _fixture_rows(document: Mapping[str, object]) -> list[dict]:
    if isinstance(document.get("rows"), list):
        return list(document["rows"])
    bricks = document.get("bricks")
    if not isinstance(bricks, list):
        raise ManifestBuildError("JSON sidecar must contain rows or certified-fixture bricks")
    rows = []
    for index, brick in enumerate(bricks, start=1):
        if not isinstance(brick, dict):
            raise ManifestBuildError("invalid certified-fixture brick row")
        wcs = brick["wcs"]
        ra_bounds = brick["unique_ra_bounds_deg"]
        dec_bounds = brick["unique_dec_bounds_deg"]
        rows.append({
            "brickname": brick["brick_id"],
            "brickid": index,
            "ra": wcs["CRVAL1"],
            "dec": wcs["CRVAL2"],
            "ra1": float(ra_bounds[0]) % 360.0,
            "ra2": float(ra_bounds[1]) % 360.0,
            "dec1": dec_bounds[0],
            "dec2": dec_bounds[1],
        })
    return rows


def _fits_rows(path: Path) -> list[dict]:
    try:
        from astropy.io import fits
    except ImportError as exc:
        raise ManifestBuildError("astropy is required to read the production FITS geometry sidecar") from exc
    columns = ("brickname", "brickid", "ra", "dec", "ra1", "ra2", "dec1", "dec2")
    with fits.open(path, memmap=False) as hdus:
        if len(hdus) < 2 or hdus[1].data is None:
            raise ManifestBuildError("geometry FITS sidecar has no table in HDU 1")
        table = hdus[1].data
        names = {str(name).lower() for name in table.names}
        if not set(columns).issubset(names):
            raise ManifestBuildError(f"geometry FITS sidecar lacks required columns: {columns}")
        return [
            {name: table[name][index].item() if hasattr(table[name][index], "item") else table[name][index]
             for name in columns}
            for index in range(len(table))
        ]


def load_geometry_sidecar(path: Path) -> GeometryIndex:
    path = Path(path)
    actual = _sha256_file(path)
    official = path.name == "survey-bricks-dr10-south.fits.gz" and actual == OFFICIAL_SIDECAR_SHA256
    companion = _verify_companion_sha256(path, actual)
    fixture = _verify_fixture_manifest(path, actual)
    if path.name == "survey-bricks-dr10-south.fits.gz" and actual != OFFICIAL_SIDECAR_SHA256:
        raise ManifestBuildError(
            f"production geometry sidecar digest mismatch: expected {OFFICIAL_SIDECAR_SHA256}, got {actual}"
        )
    if not (official or companion or fixture):
        raise ManifestBuildError("geometry sidecar has no verified official, companion, or fixture-manifest digest")
    if path.suffix.lower() == ".json":
        document = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(document, dict):
            raise ManifestBuildError("JSON geometry sidecar root must be an object")
        rows = _fixture_rows(document)
    else:
        rows = _fits_rows(path)
    return GeometryIndex(rows, sidecar_sha256=actual)


def load_positions(path: Path) -> list[Position]:
    path = Path(path)
    if path.name == "positions_runner_view.csv":
        actual = _sha256_file(path)
        if actual != OFFICIAL_POSITIONS_SHA256:
            raise ManifestBuildError(
                f"runner-view positions digest mismatch: expected {OFFICIAL_POSITIONS_SHA256}, got {actual}"
            )
    result = []
    seen = set()
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["ra", "dec", "ls_id"]:
            raise ManifestBuildError("positions CSV header must be exactly ra,dec,ls_id")
        for line_number, row in enumerate(reader, start=2):
            try:
                ra, dec, ls_id = float(row["ra"]), float(row["dec"]), row["ls_id"]
            except (TypeError, ValueError) as exc:
                raise ManifestBuildError(f"invalid positions row at line {line_number}") from exc
            if not math.isfinite(ra) or not 0.0 <= ra < 360.0:
                raise ManifestBuildError(f"invalid RA at positions line {line_number}")
            if not math.isfinite(dec) or not -90.0 <= dec <= 90.0:
                raise ManifestBuildError(f"invalid Dec at positions line {line_number}")
            if not ls_id or ls_id in seen:
                raise ManifestBuildError(f"empty or duplicate ls_id at positions line {line_number}")
            seen.add(ls_id)
            result.append(Position(ra, dec, ls_id))
    return result


def plan_candidate_bricks(geometry: GeometryIndex, ls_id: str, ra: float, dec: float) -> list[str]:
    adapter = _adapter()
    candidate_rows = geometry.declination_candidates(dec, adapter.CANDIDATE_PREFILTER_DEG)
    safe_key = "SYNTH-OBJ-" + hashlib.sha256(ls_id.encode("utf-8")).hexdigest()[:24].upper()
    target = adapter.SyntheticCutTarget(safe_key, ra, dec)
    plan = adapter.plan_object(target, _GeometryView(candidate_rows))
    return list(plan["planned_bricknames"])


def _parse_accepted_receipts(payload: bytes) -> dict[str, AcceptedBrick]:
    accepted = {}
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ManifestBuildError("receipts file is not UTF-8") from exc
    with io.StringIO(text) as handle:
        for line_number, line in enumerate(handle, start=1):
            try:
                receipt = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ManifestBuildError(f"invalid receipt JSON at line {line_number}") from exc
            if receipt.get("outcome") != "ACCEPTED" or receipt.get("digest_verified") is not True:
                continue
            brickname = str(receipt.get("brickname", "")).strip()
            relative = str(receipt.get("destination_relative_path", "")).strip()
            digest = str(receipt.get("local_sha256", "")).lower()
            relative_path = Path(relative)
            if not brickname or not relative or relative_path.is_absolute() or ".." in relative_path.parts:
                raise ManifestBuildError(f"invalid accepted receipt path at line {line_number}")
            if not SHA256_RE.fullmatch(digest):
                raise ManifestBuildError(f"invalid accepted receipt digest at line {line_number}")
            value = AcceptedBrick(brickname, relative, digest)
            previous = accepted.get(brickname)
            if previous is not None and previous != value:
                raise ManifestBuildError(f"conflicting accepted receipts for brick {brickname}")
            accepted[brickname] = value
    return accepted


def load_accepted_receipts(path: Path) -> dict[str, AcceptedBrick]:
    return _parse_accepted_receipts(Path(path).read_bytes())


def load_only_bricks(path: Optional[Path]) -> Optional[set[str]]:
    if path is None:
        return None
    values = {line.strip() for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()}
    if not values:
        raise ManifestBuildError("--only-bricks file is empty")
    return values


def build_object_manifest(
    positions_path: Path,
    receipts_path: Path,
    destination_root: Path,
    sidecar_path: Path,
    *,
    only_bricks_path: Optional[Path] = None,
) -> tuple[dict, dict]:
    positions = load_positions(positions_path)
    geometry = load_geometry_sidecar(sidecar_path)
    receipts_payload = Path(receipts_path).read_bytes()
    accepted = _parse_accepted_receipts(receipts_payload)
    only_bricks = load_only_bricks(only_bricks_path)
    destination_root = Path(destination_root)
    active_root = destination_root / "accepted" if (destination_root / "accepted").exists() else destination_root / "staging"
    receipt_paths = {
        brickname: active_root / receipt.destination_relative_path
        for brickname, receipt in accepted.items()
    }
    receipts_without_file = {
        brickname for brickname, path in receipt_paths.items() if not path.is_file()
    }
    objects = {}
    missing_histogram = Counter()
    waiting_reason_histogram = Counter()
    waiting = 0
    excluded = 0
    adapter = _adapter()
    for position in positions:
        try:
            bricknames = plan_candidate_bricks(geometry, position.ls_id, position.ra, position.dec)
        except adapter.ObjectTerminalError as exc:
            if exc.code != "FAILED_PLAN_NO_SOURCES":
                raise
            waiting += 1
            waiting_reason_histogram["ZERO_INTERSECTING_BRICKS"] += 1
            continue
        if only_bricks is not None and not set(bricknames).issubset(only_bricks):
            excluded += 1
            continue
        missing = [brickname for brickname in bricknames if brickname not in accepted]
        if missing:
            waiting += 1
            missing_histogram.update(missing)
            waiting_reason_histogram["MISSING_ACCEPTED_BRICKS"] += 1
            continue
        missing_files = [brickname for brickname in bricknames if brickname in receipts_without_file]
        # Emission is fail-closed: every planned brick must have an accepted,
        # digest-verified receipt AND resolve to an existing regular file under
        # the transfer's active root at build time. A receipt without its file
        # makes the object wait; it is never emitted from receipt evidence alone.
        if missing_files:
            waiting += 1
            waiting_reason_histogram["RECEIPTED_FILE_MISSING"] += 1
            continue
        entries = []
        for brickname in sorted(bricknames):
            receipt = accepted[brickname]
            row = geometry.by_name[brickname]
            entries.append({
                "brickname": brickname,
                "path": str(receipt_paths[brickname]),
                "row": {"dec": row["dec"], "ra": row["ra"]},
                "sha256": receipt.local_sha256,
            })
        objects[position.ls_id] = entries
    objects = {key: objects[key] for key in sorted(objects)}
    top10 = sorted(missing_histogram.items(), key=lambda item: (-item[1], item[0]))[:10]
    considered = len(positions) - excluded
    summary = {
        "objects_total": len(positions),
        "objects_considered": considered,
        "objects_excluded_by_only_bricks": excluded,
        "objects_ready": len(objects),
        "objects_waiting": waiting,
        "accepted_bricks": len(accepted),
        "active_root": str(active_root),
        "emission_rule": (
            "emit only when every planned brick has an ACCEPTED digest-verified receipt "
            "and resolves to an existing regular file under active_root at build time"
        ),
        "receipts_without_file": len(receipts_without_file),
        "waiting_reason_histogram": {
            reason: waiting_reason_histogram[reason] for reason in sorted(waiting_reason_histogram)
        },
        "missing_bricks_distinct": len(missing_histogram),
        "missing_bricks_top10": [
            {"brickname": brickname, "objects_waiting": count} for brickname, count in top10
        ],
        "positions_sha256": _sha256_file(Path(positions_path)),
        "receipts_sha256": hashlib.sha256(receipts_payload).hexdigest(),
        "sidecar_sha256": geometry.sidecar_sha256,
        "planner_module_sha256": planner_module_sha256(),
    }
    return {"objects": objects, "schema_version": 1}, summary


def write_manifest(path: Path, document: Mapping[str, object]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(document, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii") + b"\n"
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(payload)
    os.replace(temporary, path)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--positions", type=Path, required=True)
    parser.add_argument("--receipts", type=Path, required=True)
    parser.add_argument("--destination-root", type=Path, required=True)
    parser.add_argument("--sidecar", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--only-bricks", type=Path)
    args = parser.parse_args(argv)
    document, summary = build_object_manifest(
        args.positions,
        args.receipts,
        args.destination_root,
        args.sidecar,
        only_bricks_path=args.only_bricks,
    )
    write_manifest(args.output, document)
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
