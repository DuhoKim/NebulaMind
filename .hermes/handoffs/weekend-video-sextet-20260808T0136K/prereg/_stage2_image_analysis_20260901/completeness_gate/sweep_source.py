#!/usr/bin/env python3
"""Draft, receipt-gated local DR10-south sweep CandidateSource.

This module is deliberately only a backend.  Its ``run_chunk``/``candidates``
contract lets the existing run_full executor and completeness_gate finalizer be
reused; it does not provide a second finalization path and never reads pixels.
"""
from __future__ import annotations

import json
import math
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from completeness_gate import (Candidate, CandidateSource, GateError, GZRecord,
                               separation_arcsec, sha256_file)
from tap_source import append_jsonl, read_checkpoint, sha256_bytes

RADIUS_ARCSEC = 1.0
IDENTITY_COLUMNS = ("RELEASE", "BRICKID", "OBJID", "BRICKNAME", "RA", "DEC")

try:  # fitsio can read only the requested columns without materializing others.
    import fitsio  # type: ignore
except ImportError:  # pragma: no cover - selected by the installed environment
    fitsio = None

if fitsio is None:
    from astropy import __version__ as _fits_version
    from astropy.io import fits
    FITS_LIB = f"astropy {_fits_version}"
else:  # pragma: no cover - exercised where fitsio is installed
    FITS_LIB = f"fitsio {fitsio.__version__}"


def _fail(message: str) -> None:
    raise GateError(f"COMPLETENESS-FAIL: {message}")


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _load_manifest(path: Path) -> tuple[list[dict], str]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    files = raw.get("files") if isinstance(raw, dict) else None
    if not isinstance(files, list):
        _fail("sweep manifest lacks a files list")
    seen: set[str] = set()
    for item in files:
        if not isinstance(item, dict) or not isinstance(item.get("filename"), str):
            _fail("sweep manifest file entry has invalid schema")
        if item["filename"] in seen:
            _fail(f"duplicate sweep manifest filename: {item['filename']}")
        seen.add(item["filename"])
        box = item.get("box")
        if (not isinstance(box, dict)
                or not all(isinstance(box.get(k), (int, float)) for k in
                           ("ra_min_deg", "ra_max_deg", "dec_min_deg", "dec_max_deg"))
                or not isinstance(item.get("published_sha256"), str)):
            _fail(f"sweep manifest entry is incomplete: {item['filename']}")
    return files, sha256_file(path)


def _load_ok_receipts(path: Path) -> dict[str, list[dict]]:
    if not path.is_file():
        _fail("sweep receipt journal is missing")
    out: dict[str, list[dict]] = {}
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            _fail(f"sweep receipt journal has invalid JSON at line {line_no}")
        if not isinstance(row, dict):
            _fail(f"sweep receipt journal has invalid record at line {line_no}")
        filename = row.get("filename") or Path(str(row.get("path", ""))).name
        status = row.get("status", row.get("result", row.get("outcome")))
        if isinstance(filename, str) and status == "OK":
            out.setdefault(filename, []).append(row)
    return out


def _ra_delta_deg(a: float, b: float) -> float:
    return abs(math.degrees(math.remainder(math.radians(a - b), 2.0 * math.pi)))


def _box_needed(record: GZRecord, box: Mapping[str, object]) -> bool:
    """Whether a 1-arcsec cone can intersect this closed RA/Dec rectangle."""
    dmin, dmax = float(box["dec_min_deg"]), float(box["dec_max_deg"])
    margin = RADIUS_ARCSEC / 3600.0
    if record.dec < dmin - margin or record.dec > dmax + margin:
        return False
    rmin, rmax = float(box["ra_min_deg"]), float(box["ra_max_deg"])
    # The RA projection of a spherical cone grows by sec(dec).  At a pole every
    # RA is possible; elsewhere this conservative margin cannot omit a box.
    cos_dec = abs(math.cos(math.radians(record.dec)))
    ra_margin = 180.0 if cos_dec < margin / 180.0 else margin / cos_dec
    centre = (rmin + (rmax - rmin) / 2.0) % 360.0
    half_width = (rmax - rmin) / 2.0
    return _ra_delta_deg(record.ra, centre) <= half_width + ra_margin


def _decode(value: object) -> str:
    if isinstance(value, bytes):
        return value.decode("ascii").rstrip("\x00 ")
    return str(value).rstrip("\x00 ")


def _read_identity_rows(path: Path) -> Iterable[Candidate]:
    if fitsio is not None:  # pragma: no cover - depends on optional dependency
        data = fitsio.read(path, columns=list(IDENTITY_COLUMNS), ext=1)
        names = {n.upper(): n for n in data.dtype.names or ()}
        for row in data:
            yield Candidate(int(row[names["RELEASE"]]), int(row[names["BRICKID"]]),
                            int(row[names["OBJID"]]), float(row[names["RA"]]),
                            float(row[names["DEC"]]), _decode(row[names["BRICKNAME"]]))
        return
    with fits.open(path, memmap=True, mode="readonly") as hdus:
        data = hdus[1].data
        names = {n.upper(): n for n in data.names}
        missing = [n for n in IDENTITY_COLUMNS if n not in names]
        if missing:
            _fail(f"sweep {path.name} lacks identity/position columns: {','.join(missing)}")
        # Access only the six named column arrays; the underlying FITS table is mmap-backed.
        columns = {n: data.field(names[n]) for n in IDENTITY_COLUMNS}
        for i in range(len(data)):
            yield Candidate(int(columns["RELEASE"][i]), int(columns["BRICKID"][i]),
                            int(columns["OBJID"][i]), float(columns["RA"][i]),
                            float(columns["DEC"][i]), _decode(columns["BRICKNAME"][i]))


class SweepCandidateSource(CandidateSource):
    """Memory-bounded, manifest- and receipt-gated local sweep source."""

    def __init__(self, sweep_dir: Path, manifest: Path, receipts: Path,
                 artifacts: Path):
        self.sweep_dir, self.manifest_path = Path(sweep_dir), Path(manifest)
        self.receipts_path, self.artifacts = Path(receipts), Path(artifacts)
        self._files, self._manifest_sha = _load_manifest(self.manifest_path)
        self._results: dict[int, list[Candidate]] = {}

    @property
    def provenance(self) -> Mapping[str, object]:
        entries = self._checkpoint_entries()
        return {"backend": "local-DR10-south-sweeps-DRAFT",
                "release_identity": "DR10-south/sweep/10.0",
                "enumeration": "complete-all-candidates",
                "query_artifacts": [
                    {"chunk_id": e["chunk_id"], "raw_result": e["raw_result"],
                     "raw_sha256": e["raw_sha256"],
                     "consulted_sweeps": e["consulted_sweeps"]} for e in entries],
                "manifest": str(self.manifest_path),
                "manifest_sha256": self._manifest_sha,
                "receipt_journal": str(self.receipts_path),
                "receipt_journal_sha256": sha256_file(self.receipts_path),
                "fits_lib": FITS_LIB, "magnitude_predicate": False,
                "truncated": False}

    def _checkpoint_entries(self) -> list[dict]:
        entries = read_checkpoint(self.artifacts / "checkpoint.jsonl", repair_tail=True,
                                  run_log=self.artifacts / "run.log.jsonl")
        for entry in entries:
            raw = self.artifacts / str(entry.get("raw_result", ""))
            if not raw.is_file() or sha256_file(raw) != entry.get("raw_sha256"):
                _fail(f"resume hash mismatch for chunk {entry.get('chunk_id')}")
        return entries

    def _needed(self, records: Sequence[GZRecord]) -> list[dict]:
        return [item for item in self._files
                if any(_box_needed(record, item["box"]) for record in records)]

    def _verify(self, needed: Sequence[dict]) -> list[dict]:
        ok = _load_ok_receipts(self.receipts_path)
        proof = []
        for item in needed:
            name, expected = item["filename"], item["published_sha256"]
            matching = ok.get(name, [])
            if not matching:
                _fail(f"needed sweep lacks an OK receipt: {name}")
            receipt_hashes = {str(r.get("sha256", r.get("on_disk_sha256", expected)))
                              for r in matching}
            if expected not in receipt_hashes:
                _fail(f"OK receipt sha256 disagrees with manifest: {name}")
            path = self.sweep_dir / name
            if not path.is_file():
                _fail(f"needed sweep is absent on disk: {name}")
            observed = sha256_file(path)
            if observed != expected:
                _fail(f"on-disk sweep sha256 mismatch: {name}")
            proof.append({"filename": name, "manifest_sha256": expected,
                          "on_disk_sha256": observed})
        return proof

    def _admit(self, associations: Sequence[Mapping[str, object]],
               records: Sequence[GZRecord]) -> None:
        allowed = {r.input_index: r for r in records}
        seen: set[tuple[int, tuple[int, int, int]]] = set()
        for row in associations:
            idx = int(row["input_index"])
            if idx not in allowed:
                _fail("sweep artifact input_index is outside its chunk")
            candidate = Candidate(int(row["release"]), int(row["brickid"]),
                                  int(row["objid"]), float(row["ra"]),
                                  float(row["dec"]), str(row.get("brickname", "")))
            if separation_arcsec(allowed[idx].ra, allowed[idx].dec,
                                 candidate.ra, candidate.dec) > RADIUS_ARCSEC:
                _fail("sweep artifact contains a source outside its attributed cone")
            key = idx, candidate.identity
            if key in seen:
                _fail("sweep artifact has duplicate candidate identity/provenance")
            seen.add(key)
            self._results.setdefault(idx, []).append(candidate)

    def run_chunk(self, chunk_id: int, records: Sequence[GZRecord]) -> dict:
        self.artifacts.mkdir(parents=True, exist_ok=True)
        entries = self._checkpoint_entries()
        completed = [e for e in entries if e.get("chunk_id") == chunk_id]
        if len(completed) > 1:
            _fail(f"multiple successful checkpoint entries for chunk {chunk_id}")
        if completed:
            entry = completed[0]
            payload = json.loads((self.artifacts / entry["raw_result"]).read_text())
            if payload.get("manifest_sha256") != self._manifest_sha:
                _fail(f"resume manifest hash mismatch for chunk {chunk_id}")
            current_proof = self._verify(self._needed(records))
            if current_proof != payload.get("consulted_sweeps"):
                _fail(f"resume sweep proof mismatch for chunk {chunk_id}")
            self._admit(payload["associations"], records)
            return entry | {"resumed": True}
        expected = list(range(records[0].input_index,
                              records[0].input_index + len(records))) if records else []
        if [r.input_index for r in records] != expected:
            _fail("chunk input_index sequence is not contiguous")
        started = time.monotonic()
        needed = self._needed(records)
        proof = self._verify(needed)
        associations: list[dict] = []
        seen: set[tuple[int, tuple[int, int, int]]] = set()
        for item in needed:  # exactly one sweep is open at a time
            for candidate in _read_identity_rows(self.sweep_dir / item["filename"]):
                for record in records:
                    if separation_arcsec(record.ra, record.dec,
                                         candidate.ra, candidate.dec) <= RADIUS_ARCSEC:
                        key = record.input_index, candidate.identity
                        if key in seen:
                            continue
                        seen.add(key)
                        associations.append({"input_index": record.input_index,
                                             "release": candidate.release,
                                             "brickid": candidate.brickid,
                                             "objid": candidate.objid,
                                             "brickname": candidate.brickname,
                                             "ra": candidate.ra, "dec": candidate.dec})
        associations.sort(key=lambda r: (r["input_index"], r["release"],
                                         r["brickid"], r["objid"]))
        payload = {"version": 1, "chunk_id": chunk_id,
                   "manifest_sha256": self._manifest_sha,
                   "receipt_journal_sha256": sha256_file(self.receipts_path),
                   "fits_lib": FITS_LIB, "consulted_sweeps": proof,
                   "associations": associations}
        raw = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
        attempt = f"chunk_{chunk_id:04d}_{_stamp()}_{uuid.uuid4().hex[:8]}"
        attempt_dir = self.artifacts / attempt
        attempt_dir.mkdir()
        raw_path = attempt_dir / "result.json"
        raw_path.write_bytes(raw)
        metadata = {"chunk_id": chunk_id, "attempt": attempt,
                    "rows_in": len(records), "client_row_count": len(associations),
                    "consulted_sweeps": proof, "manifest_sha256": self._manifest_sha,
                    "receipt_journal_sha256": sha256_file(self.receipts_path),
                    "fits_lib": FITS_LIB, "magnitude_predicate": False,
                    "truncated": False, "wall_s": time.monotonic() - started,
                    "raw_result": f"{attempt}/result.json",
                    "raw_sha256": sha256_bytes(raw)}
        (attempt_dir / "metadata.json").write_text(
            json.dumps(metadata, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        append_jsonl(self.artifacts / "checkpoint.jsonl", metadata)
        self._admit(associations, records)
        return metadata

    def candidates(self, record: GZRecord, radius_arcsec: float) -> Sequence[Candidate]:
        if radius_arcsec != RADIUS_ARCSEC:
            _fail("sweep source is fixed at the preregistered 1.0 arcsec radius")
        return tuple(self._results.get(record.input_index, ()))
