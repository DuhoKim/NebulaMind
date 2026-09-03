#!/usr/bin/env python3
"""Catalogue-only §15 blind guard. Never accepts or resolves an image path."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from seal_gate.seal_gate import canonical_bytes, sha256_file
from completeness_gate.completeness_gate import separation_arcsec

TIER_A = ROOT.parent / "_successor_build_20260824/acquire/positions_selected_cut.csv"
PARENT = ROOT.parent / "_successor_build_20260824/acquire/positions_selected.csv"
PINS = {TIER_A: ("a20682c114508dbdd18ede6a56c61509ea9c16784aaca7eee61f76bf97cdd372", 49_211),
        PARENT: ("425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831", 65_060)}
VOID = "VOID-BLIND-VIOLATION"


def _protected(paths=PINS):
    rows = []
    digests = {}
    for path, (pin, count) in paths.items():
        got = sha256_file(path)
        if got != pin:
            raise RuntimeError("DATA-INTEGRITY-FAIL: protected pin digest mismatch")
        with path.open(newline="", encoding="utf-8") as stream:
            part = list(csv.DictReader(stream))
        if len(part) != count:
            raise RuntimeError("DATA-INTEGRITY-FAIL: protected pin row-count mismatch")
        rows.extend(part); digests[str(path)] = got
    return rows, digests


def guard(requests: list[dict], *, protected_paths=PINS) -> dict:
    # This receipt is fully decided before any downstream/image path can be supplied.
    protected, digests = _protected(protected_paths)
    hits = []
    for index, req in enumerate(requests):
        if set(req) - {"ls_id", "brickid", "objid", "ra", "dec"}:
            raise ValueError("request has forbidden fields (paths are never accepted)")
        identity = {k: str(req[k]) for k in ("ls_id", "brickid", "objid") if k in req}
        for row in protected:
            identity_hit = bool(identity) and all(row[k] == v for k, v in identity.items())
            coordinate_hit = ("ra" in req and "dec" in req and
                separation_arcsec(float(req["ra"]), float(req["dec"]), float(row["ra"]), float(row["dec"])) <= 1.0)
            if identity_hit or coordinate_hit:
                hits.append({"request_index": index, "reason": VOID})
                break
    return {"operation": "blind-guard", "request_count": len(requests),
            "protected_counts": {"tier_a": protected_paths[next(iter(protected_paths))][1],
                                 "combined_rows_checked": len(protected)},
            "protected_digests": digests, "radius_arcsec": 1.0,
            "status": "REFUSE" if hits else "PASS",
            "reason": VOID if hits else None, "hits": hits}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("requests", type=Path, help="JSON list; path fields are forbidden")
    args = ap.parse_args(argv)
    requests = json.loads(args.requests.read_text(encoding="utf-8"))
    receipt = guard(requests)
    sys.stdout.buffer.write(canonical_bytes(receipt))
    return 1 if receipt["status"] == "REFUSE" else 0


if __name__ == "__main__":
    raise SystemExit(main())
