#!/usr/bin/env python3
"""Independent recomputation of PARENT_KEYSET_SHA256, EVIDENCE_SHA256, EXPECTED_RETAINED.

Deliberately does NOT import bs2a_quality_gate.py. Re-implements the join, predicate,
and digest algorithms from the module's own docstrings/spec so that a bug shared between
the module's build path and its own self-test cannot hide from this check.
"""
import csv
import hashlib
import sys
from pathlib import Path

ACQ = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("../acquire")

T_FLUX_IVAR_R_GT = 8.4000532
T_PSFSIZE_R_LT = 1.5699703
T_NOBS_R_GE = 3.0

JOIN_KEYS = ("brickid", "objid")
QUALITY_COLUMNS = ("flux_ivar_r", "psfsize_r", "nobs_r")

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while True:
            b = f.read(1 << 20)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def load_rows(p: Path):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def key(row):
    return tuple(str(row[k]).strip() for k in JOIN_KEYS)

def enc(*parts) -> str:
    return "".join(f"{len(s)}:{s}" for s in map(str, parts))

def quality_pass(f, ps, nb):
    return f > T_FLUX_IVAR_R_GT and ps < T_PSFSIZE_R_LT and nb >= T_NOBS_R_GE

def main():
    parent_path = ACQ / "positions_selected.csv"
    quality_path = ACQ / "quality_selected.csv"

    parent_sha = sha256_file(parent_path)
    quality_sha = sha256_file(quality_path)
    print(f"parent_source_sha256   independently computed: {parent_sha}")
    print(f"quality_source_sha256  independently computed: {quality_sha}")

    parent = load_rows(parent_path)
    quality = load_rows(quality_path)
    print(f"parent rows: {len(parent)}   quality rows: {len(quality)}")

    qmap = {}
    dup_q = 0
    for r in quality:
        k = key(r)
        if k in qmap:
            dup_q += 1
        qmap[k] = r
    print(f"duplicate quality keys (last-wins in this map): {dup_q}")

    pkeys = []
    dup_p = 0
    seen = set()
    for r in parent:
        k = key(r)
        if k in seen:
            dup_p += 1
        seen.add(k)
        pkeys.append(k)
    print(f"duplicate parent keys: {dup_p}   unique parent keys: {len(seen)}")

    missing = seen - set(qmap)
    extra = set(qmap) - seen
    print(f"parent keys missing a quality row: {len(missing)}")
    print(f"quality keys with no parent: {len(extra)}")

    if missing or extra or dup_p or dup_q:
        print("STOP: join is not clean one-to-one; independent evidence cannot be built safely.")
        sys.exit(2)

    evidence = []
    for r in parent:
        k = key(r)
        q = qmap[k]
        vals = {c: float(q[c]) for c in QUALITY_COLUMNS}
        qp = quality_pass(vals["flux_ivar_r"], vals["psfsize_r"], vals["nobs_r"])
        evidence.append({
            "brickid": k[0], "objid": k[1],
            **vals,
            "quality_pass": qp,
        })

    n_retained = sum(1 for e in evidence if e["quality_pass"])
    n_excluded = len(evidence) - n_retained
    print(f"n_joined={len(evidence)} n_retained={n_retained} n_excluded={n_excluded}")

    # keyset digest: sorted encoded (brickid, objid) pairs
    keyset_digest = hashlib.sha256("\n".join(sorted(
        enc(e["brickid"], e["objid"]) for e in evidence
    )).encode("utf-8")).hexdigest()
    print(f"PARENT_KEYSET_SHA256 independently computed: {keyset_digest}")

    # evidence digest: sorted encoded full rows
    def row_enc(e):
        return enc(e["brickid"], e["objid"],
                    repr(float(e["flux_ivar_r"])), repr(float(e["psfsize_r"])),
                    repr(float(e["nobs_r"])), "1" if e["quality_pass"] else "0")
    evidence_digest = hashlib.sha256("\n".join(sorted(
        row_enc(e) for e in evidence
    )).encode("utf-8")).hexdigest()
    print(f"EVIDENCE_SHA256 independently computed: {evidence_digest}")

    print(f"EXPECTED_RETAINED independently computed: {n_retained}")

if __name__ == "__main__":
    main()
