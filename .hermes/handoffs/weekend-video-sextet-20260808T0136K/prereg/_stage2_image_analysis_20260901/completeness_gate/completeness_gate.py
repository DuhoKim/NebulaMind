#!/usr/bin/env python3
"""Catalogue-only implementation of MINI_PREREG §§3--5; never opens pixels."""
from __future__ import annotations

import abc
import csv
import gzip
import hashlib
import json
import math
import os
import platform
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

MATCH_ARCSEC = 1.0
PARENT_ARCSEC = 1.0
TIER_A_ARCSEC = 1.0
LABEL_THRESHOLD = 0.8
PINNED_DIGESTS = {
    "table2": "5121e43f502856c9f73e31934a6e7d7282669c3ae065564a31f5d5115f45541d",
    "table3": "282c8049e93c47b5343885210ace8ba5710e9914ce035a6b39061395436d9723",
    "tier_a": "a20682c114508dbdd18ede6a56c61509ea9c16784aaca7eee61f76bf97cdd372",
    "parent": "425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831",
}
TERMINAL_PRIOR = {
    "NO-DR10-WITHIN-1ARCSEC", "ONE-DR10-WITHIN-1ARCSEC",
    "MULTIPLE-DR10-WITHIN-1ARCSEC",
}


class GateError(RuntimeError):
    """An exact, non-ordinary refusal."""


def _fail(kind: str, message: str) -> None:
    raise GateError(f"{kind}: {message}")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def _finite(text: object, field: str) -> float:
    try:
        value = float(str(text).strip())
    except (TypeError, ValueError):
        _fail("DATA-INTEGRITY-FAIL", f"{field} is not uniquely parseable")
    if not math.isfinite(value):
        _fail("DATA-INTEGRITY-FAIL", f"{field} is not finite")
    return value


def parse_ra(text: object) -> float:
    raw = str(text).strip()
    parts = raw.split(":")
    if len(parts) != 3:
        _fail("DATA-INTEGRITY-FAIL", "RA is not sexagesimal HH:MM:SS")
    h, m, s = (_finite(x, "RA") for x in parts)
    if h < 0 or h >= 24 or m < 0 or m >= 60 or s < 0 or s >= 60:
        _fail("DATA-INTEGRITY-FAIL", "RA sexagesimal component out of range")
    value = 15.0 * (h + m / 60.0 + s / 3600.0)
    if not 0.0 <= value < 360.0:
        _fail("DATA-INTEGRITY-FAIL", "RA outside [0,360)")
    return value


def parse_dec(text: object) -> float:
    raw = str(text).strip()
    if not raw or raw[0] not in "+-":
        _fail("DATA-INTEGRITY-FAIL", "DEC lacks printed leading sign")
    sign = -1.0 if raw[0] == "-" else 1.0
    parts = raw[1:].split(":")
    if len(parts) != 3:
        _fail("DATA-INTEGRITY-FAIL", "DEC is not sexagesimal +/-DD:MM:SS")
    d, m, s = (_finite(x, "DEC") for x in parts)
    if d < 0 or d > 90 or m < 0 or m >= 60 or s < 0 or s >= 60:
        _fail("DATA-INTEGRITY-FAIL", "DEC sexagesimal component out of range")
    value = sign * (d + m / 60.0 + s / 3600.0)
    if not -90.0 <= value <= 90.0 or (d == 90 and (m != 0 or s != 0)):
        _fail("DATA-INTEGRITY-FAIL", "DEC outside [-90,90]")
    return value


def parse_decimal_coord(value: object, field: str) -> float:
    out = _finite(value, field)
    if field == "RA" and not 0 <= out < 360:
        _fail("DATA-INTEGRITY-FAIL", "RA outside [0,360)")
    if field == "DEC" and not -90 <= out <= 90:
        _fail("DATA-INTEGRITY-FAIL", "DEC outside [-90,90]")
    return out


def separation_arcsec(ra1: float, dec1: float, ra2: float, dec2: float) -> float:
    """Binary64 stable great-circle separation, including RA wrap."""
    r1, d1, r2, d2 = map(math.radians, (ra1, dec1, ra2, dec2))
    dr = math.remainder(r2 - r1, 2.0 * math.pi)
    sd, cd = math.sin((d2 - d1) / 2.0), math.cos((d2 - d1) / 2.0)
    sr = math.sin(dr / 2.0)
    a = sd * sd + math.cos(d1) * math.cos(d2) * sr * sr
    return math.degrees(2.0 * math.asin(math.sqrt(min(1.0, max(0.0, a))))) * 3600.0


@dataclass(frozen=True)
class GZRecord:
    input_index: int
    objid: int
    ra: float
    dec: float
    p_cw: float
    p_acw: float


@dataclass(frozen=True)
class Position:
    objid: str
    ra: float
    dec: float


@dataclass(frozen=True)
class Candidate:
    release: int
    brickid: int
    objid: int
    ra: float
    dec: float
    brickname: str = ""

    @property
    def identity(self) -> tuple[int, int, int]:
        return self.release, self.brickid, self.objid


@dataclass(frozen=True)
class Pair:
    gz1_objid: int
    dr10_release: int
    dr10_brickid: int
    dr10_objid: int
    label: str


def read_gz_tables(paths: Sequence[Path]) -> list[GZRecord]:
    rows: list[GZRecord] = []
    for path in paths:
        opener = gzip.open if path.suffix == ".gz" else open
        with opener(path, "rt", newline="") as f:
            reader = csv.DictReader(f)
            required = {"OBJID", "RA", "DEC", "P_CW", "P_ACW"}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                _fail("DATA-INTEGRITY-FAIL", f"missing required GZ1 columns in {path.name}")
            for raw in reader:
                try:
                    oid = int(raw["OBJID"])
                except (TypeError, ValueError):
                    _fail("DATA-INTEGRITY-FAIL", "OBJID is not an integer")
                pcw, pacw = _finite(raw["P_CW"], "P_CW"), _finite(raw["P_ACW"], "P_ACW")
                if not (0 <= pcw <= 1 and 0 <= pacw <= 1):
                    _fail("DATA-INTEGRITY-FAIL", "probability outside [0,1]")
                rows.append(GZRecord(len(rows), oid, parse_ra(raw["RA"]),
                                     parse_dec(raw["DEC"]), pcw, pacw))
    return rows


def read_positions(path: Path) -> list[Position]:
    with path.open("rt", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or not {"ra", "dec"}.issubset(reader.fieldnames):
            _fail("DATA-INTEGRITY-FAIL", f"missing ra/dec columns in {path.name}")
        return [Position(str(r.get("ls_id", r.get("objid", i))),
                         parse_decimal_coord(r["ra"], "RA"),
                         parse_decimal_coord(r["dec"], "DEC"))
                for i, r in enumerate(reader)]


class CandidateSource(abc.ABC):
    """Backend contract: return every candidate in the inclusive cone."""

    @property
    @abc.abstractmethod
    def provenance(self) -> Mapping[str, object]:
        pass

    @abc.abstractmethod
    def candidates(self, record: GZRecord, radius_arcsec: float) -> Sequence[Candidate]:
        pass


class InMemoryCandidateSource(CandidateSource):
    def __init__(self, candidates: Iterable[Candidate], release_identity: str = "SYNTHETIC-DR10"):
        self._candidates = tuple(candidates)
        self._provenance = {
            "backend": "synthetic-in-memory", "release_identity": release_identity,
            "enumeration": "complete-all-candidates", "query_artifacts": [],
            "magnitude_predicate": False, "truncated": False,
        }

    @property
    def provenance(self) -> Mapping[str, object]:
        return self._provenance

    def candidates(self, record: GZRecord, radius_arcsec: float) -> Sequence[Candidate]:
        return tuple(c for c in self._candidates
                     if separation_arcsec(record.ra, record.dec, c.ra, c.dec) <= radius_arcsec)


class AstroDataLabCandidateSource(CandidateSource):
    """Non-networking stub. A reviewed artifact-backed implementation is required."""

    @property
    def provenance(self) -> Mapping[str, object]:
        return {"backend": "NOIRLab-Astro-Data-Lab-TAP-STUB",
                "release_identity": "UNCONFIGURED", "enumeration": "unproven",
                "query_artifacts": [], "magnitude_predicate": False, "truncated": None}

    def candidates(self, record: GZRecord, radius_arcsec: float) -> Sequence[Candidate]:
        _fail("COMPLETENESS-FAIL", "real catalogue backend is a non-executable stub")


def _within(record: GZRecord, positions: Sequence[Position], radius: float) -> bool:
    return any(separation_arcsec(record.ra, record.dec, p.ra, p.dec) <= radius for p in positions)


def _label(record: GZRecord) -> str | None:
    cw, acw = record.p_cw >= LABEL_THRESHOLD, record.p_acw >= LABEL_THRESHOLD
    if cw and acw:
        _fail("DATA-INTEGRITY-FAIL", f"contradictory labels for GZ1 OBJID {record.objid}")
    if cw:
        return "CLOCKWISE"
    if acw:
        return "ANTICLOCKWISE"
    return None


def _prior_disposition(n: int) -> str:
    if n == 0:
        return "NO-DR10-WITHIN-1ARCSEC"
    if n == 1:
        return "ONE-DR10-WITHIN-1ARCSEC"
    return "MULTIPLE-DR10-WITHIN-1ARCSEC"


def run_gate(records: Sequence[GZRecord], tier_a: Sequence[Position], parent: Sequence[Position],
             source: CandidateSource, prior_unresolved_objids: Sequence[int], *,
             input_digests: Mapping[str, str], expected_rows: int = 893_212,
             expected_prior: int = 13_725, tier_a_digest: str = "",
             parent_digest: str = "", software_digest: str = "") -> tuple[list[Pair], dict]:
    if len(records) != expected_rows:
        _fail("COMPLETENESS-FAIL", f"expected {expected_rows} GZ1 rows, considered {len(records)}")
    indices = [r.input_index for r in records]
    if sorted(indices) != list(range(expected_rows)) or len(set(indices)) != expected_rows:
        _fail("COMPLETENESS-FAIL", "GZ1 input_index coverage is not exactly once")
    seen: set[int] = set()
    for r in records:
        if r.objid in seen:
            _fail("DATA-INTEGRITY-FAIL", f"duplicate GZ1 OBJID: {r.objid}")
        seen.add(r.objid)
    if len(prior_unresolved_objids) != expected_prior:
        _fail("COMPLETENESS-FAIL", f"expected {expected_prior} prior-unresolved OBJIDs, got {len(prior_unresolved_objids)}")
    if len(set(prior_unresolved_objids)) != len(prior_unresolved_objids):
        _fail("COMPLETENESS-FAIL", "duplicate prior-unresolved OBJID")
    missing_prior = sorted(set(prior_unresolved_objids) - seen)
    if missing_prior:
        _fail("COMPLETENESS-FAIL", f"prior-unresolved OBJID lacks terminal disposition: {missing_prior[0]}")

    prov = dict(source.provenance)
    if (prov.get("enumeration") != "complete-all-candidates" or
            prov.get("magnitude_predicate") is not False or
            prov.get("truncated") is not False):
        _fail("COMPLETENESS-FAIL", "catalogue backend does not prove complete uncapped enumeration")

    dispositions: dict[int, str] = {}
    candidate_map: dict[int, tuple[Candidate, ...]] = {}
    counts = {k: 0 for k in ("tier_a", "tier_b", "no_dr10", "one_dr10", "multiple_dr10",
                              "collision", "below_threshold", "tier_c_eligible")}
    unique_owner: dict[tuple[int, int, int], list[int]] = {}
    for r in records:
        if _within(r, tier_a, TIER_A_ARCSEC):
            dispositions[r.objid] = "TIER-A-EXCLUDED"
            counts["tier_a"] += 1
            candidate_map[r.objid] = tuple()
            continue
        if _within(r, parent, PARENT_ARCSEC):
            dispositions[r.objid] = "TIER-B-EXCLUDED"
            counts["tier_b"] += 1
            candidate_map[r.objid] = tuple()
            continue
        candidates = tuple(source.candidates(r, MATCH_ARCSEC))
        for c in candidates:
            cra = parse_decimal_coord(c.ra, "RA")
            cdec = parse_decimal_coord(c.dec, "DEC")
            if separation_arcsec(r.ra, r.dec, cra, cdec) > MATCH_ARCSEC:
                _fail("COMPLETENESS-FAIL", f"backend returned out-of-cone DR10 candidate for GZ1 OBJID {r.objid}")
            if not all(isinstance(x, int) and not isinstance(x, bool)
                       for x in (c.release, c.brickid, c.objid)):
                _fail("DATA-INTEGRITY-FAIL", "DR10 release/brickid/objid is not an integer")
        identities = [c.identity for c in candidates]
        if len(set(identities)) != len(identities):
            _fail("COMPLETENESS-FAIL", f"backend returned duplicate DR10 candidate for GZ1 OBJID {r.objid}")
        candidate_map[r.objid] = candidates
        if not candidates:
            dispositions[r.objid] = "NO-DR10-WITHIN-1ARCSEC"
            counts["no_dr10"] += 1
        elif len(candidates) > 1:
            dispositions[r.objid] = "MULTIPLE-DR10-WITHIN-1ARCSEC"
            counts["multiple_dr10"] += 1
        else:
            dispositions[r.objid] = "ONE-DR10-WITHIN-1ARCSEC"
            counts["one_dr10"] += 1
            unique_owner.setdefault(candidates[0].identity, []).append(r.objid)

    collided = {oid for owners in unique_owner.values() if len(owners) > 1 for oid in owners}
    for oid in collided:
        dispositions[oid] = "DR10-COLLISION-AMBIGUOUS"
        counts["collision"] += 1

    # Labels are consulted only after coordinate/identifier exclusions are complete.
    pairs: list[Pair] = []
    by_id = {r.objid: r for r in records}
    for r in records:
        label = _label(r)
        if dispositions[r.objid] != "ONE-DR10-WITHIN-1ARCSEC" or r.objid in collided:
            continue
        if label is None:
            dispositions[r.objid] = "BELOW-LABEL-THRESHOLD"
            counts["below_threshold"] += 1
            continue
        c = candidate_map[r.objid][0]
        dispositions[r.objid] = "TIER-C-ELIGIBLE"
        counts["tier_c_eligible"] += 1
        pairs.append(Pair(r.objid, c.release, c.brickid, c.objid, label))
    pairs.sort(key=lambda p: (int(p.gz1_objid), int(p.dr10_brickid), int(p.dr10_objid)))

    prior_rows = []
    for oid in prior_unresolved_objids:
        # §5.2 is the raw catalogue candidate count, independent of later collision/label state.
        n = len(candidate_map.get(oid, ()))
        terminal = _prior_disposition(n)
        if terminal not in TERMINAL_PRIOR:
            _fail("COMPLETENESS-FAIL", f"prior-unresolved OBJID lacks terminal disposition: {oid}")
        prior_rows.append({"gz1_objid": oid, "disposition": terminal})
    if len(prior_rows) != expected_prior:
        _fail("COMPLETENESS-FAIL", "prior-unresolved terminal-disposition coverage gap")

    receipt = {
        "verdict": "PASS", "rows_expected": expected_rows,
        "rows_considered_exactly_once": len(records), "unique_valid_gz1": len(seen),
        "input_digests": dict(input_digests), "tier_a_digest": tier_a_digest,
        "parent_digest": parent_digest, "dr10_release_identity": prov.get("release_identity"),
        "catalogue_backend": prov, "query_export_artifacts": prov.get("query_artifacts", []),
        "software_environment": {
            "python": sys.version, "platform": platform.platform(),
            "software_sha256": software_digest,
        },
        "match_radius_arcsec": MATCH_ARCSEC,
        "candidate_enumeration": "complete-all-candidates-inclusive",
        "funnel_counts": counts, "terminal_dispositions": dispositions,
        "prior_unresolved_expected": expected_prior,
        "prior_unresolved_terminal": prior_rows,
        "pair_count": len(pairs), "canonical_sort": ["GZ1_OBJID", "DR10_BRICKID", "DR10_OBJID"],
        "pair_sha256": hashlib.sha256(json.dumps([asdict(p) for p in pairs],
                                                   sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
    }
    return pairs, receipt


def write_outputs(output_dir: Path, pairs: Sequence[Pair], receipt: Mapping[str, object]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "tier_c_pairs.csv").open("w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["GZ1_OBJID", "DR10_RELEASE", "DR10_BRICKID", "DR10_OBJID", "LABEL"])
        for p in pairs:
            w.writerow([p.gz1_objid, p.dr10_release, p.dr10_brickid, p.dr10_objid, p.label])
    (output_dir / "completeness_receipt.json").write_text(
        json.dumps(receipt, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def run_pinned_files(table2: Path, table3: Path, tier_a_path: Path, parent_path: Path,
                     prior_unresolved_objids: Sequence[int], source: CandidateSource
                     ) -> tuple[list[Pair], dict]:
    """Digest- and count-check the four §2 inputs, then execute the gate."""
    paths = {"table2": table2, "table3": table3,
             "tier_a": tier_a_path, "parent": parent_path}
    observed = {name: sha256_file(path) for name, path in paths.items()}
    for name, expected in PINNED_DIGESTS.items():
        if observed[name] != expected:
            _fail("COMPLETENESS-FAIL", f"pinned input hash mismatch: {name}")
    rows = read_gz_tables([table2, table3])
    tier_a = read_positions(tier_a_path)
    parent = read_positions(parent_path)
    if len(tier_a) != 49_211:
        _fail("COMPLETENESS-FAIL", f"expected 49211 Tier-A rows, got {len(tier_a)}")
    if len(parent) != 65_060:
        _fail("COMPLETENESS-FAIL", f"expected 65060 parent rows, got {len(parent)}")
    return run_gate(rows, tier_a, parent, source, prior_unresolved_objids,
                    input_digests={"table2": observed["table2"], "table3": observed["table3"]},
                    tier_a_digest=observed["tier_a"], parent_digest=observed["parent"],
                    software_digest=sha256_file(Path(__file__)))
