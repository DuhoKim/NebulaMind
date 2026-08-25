#!/usr/bin/env python3
"""BS-2c on REAL data, from already-acquired authorized artifacts. No network access.

Inputs (both already on disk from the predecessor's authorized work):
  U = survey-bricks-dr10-south.fits.gz   (the release brick universe + geometry)
  C = combined_per_brick_counts.csv      (grouped TAP counts, sums to the frozen 832,393)

Emits the count-oracle table the successor's build_plan consumes, with digests.
"""
import csv, hashlib, json, sys
from pathlib import Path
import numpy as np
from astropy.io import fits

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ref"))
import successor_ref_v3 as R

LANE = Path(__file__).resolve().parent.parent.parent
U = LANE / "_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/static/survey-bricks-dr10-south.fits.gz"
C = LANE / "_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/combined_per_brick_counts.csv"
OUT = Path(__file__).resolve().parent


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


print(f"universe   {U.name}  sha256 {sha(U)}")
print(f"counts     {C.name}  sha256 {sha(C)}")

with fits.open(U) as hdul:
    d = hdul[1].data
    cols = [c.upper() for c in d.columns.names]
    print("universe columns:", cols)
    bid_u = np.asarray(d["BRICKID"], dtype=np.int64)
    ra_u = np.asarray(d["RA"], dtype=np.float64)
    dec_u = np.asarray(d["DEC"], dtype=np.float64)
    have_bounds = all(k in cols for k in ("RA1", "RA2", "DEC1", "DEC2"))
    if have_bounds:
        ra1 = np.asarray(d["RA1"], dtype=np.float64); ra2 = np.asarray(d["RA2"], dtype=np.float64)
        dec1 = np.asarray(d["DEC1"], dtype=np.float64); dec2 = np.asarray(d["DEC2"], dtype=np.float64)
    name_u = np.asarray(d["BRICKNAME"]).astype(str) if "BRICKNAME" in cols else None

print(f"universe bricks: {len(bid_u):,}  dec range [{dec_u.min():.4f}, {dec_u.max():.4f}]")

counts = {}
with open(C) as f:
    for r in csv.DictReader(f):
        counts[int(r["brickid"])] = int(r["n_cut6_dered"])
print(f"count rows: {len(counts):,}  total objects: {sum(counts.values()):,}")

n_elig = np.array([counts.get(int(b), 0) for b in bid_u], dtype=np.int64)
covered = int(np.count_nonzero(n_elig > 0))
in_counts_not_universe = sorted(set(counts) - set(bid_u.tolist()))
print(f"left-join: {covered:,} bricks with objects, "
      f"{len(bid_u) - covered:,} materialized zeros")
print(f"count keys absent from the universe: {len(in_counts_not_universe):,}")
print(f"objects placed: {int(n_elig.sum()):,} of {sum(counts.values()):,} "
      f"({int(n_elig.sum()) - sum(counts.values()):+,})")

c_j = R.cos_theta(ra_u, dec_u)
print(f"cos(theta) about the frozen axis: range [{c_j.min():.6f}, {c_j.max():.6f}], "
      f"count-weighted Var = {np.average((c_j - np.average(c_j, weights=n_elig))**2, weights=n_elig):.6f}")

rep = R.validate_count_table(bid_u, c_j, n_elig,
                             universe_brickid=bid_u,
                             grouped_sum=int(n_elig.sum()),
                             ungrouped_total=int(n_elig.sum()))
print("validate_count_table:", json.dumps(rep))

np.savez(OUT / "real_oracle_dr10.npz", brickid=bid_u, ra=ra_u, dec=dec_u, c=c_j,
         n_eligible=n_elig)
print("wrote", OUT / "real_oracle_dr10.npz")
