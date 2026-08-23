#!/usr/bin/env python3
"""Selection-design numbers for the successor prereg (SUCCESSOR_SCOPE req 1-2).

Inputs, both custody-verified in the lane:
  - brick centres: _tori_parent_row_count_evidence/.../static/survey-bricks-dr10-south.fits.gz
  - per-brick dered Cut-6 counts (full keyspace): combined_per_brick_counts.csv (sha 4e4ec45d...)

Figure of merit: leverage = N * Var(cos theta) about Longo's frozen axis, computed count-weighted
at brick centres (same convention as TORI_FOOTPRINT_VARIANCE_RECEIPT). Full-sphere-equivalent
N_eq = 3 * leverage. Frozen requirement from the dead prereg: 100,000 N_eq.

Strategies compared:
  FULL        every brick (the baseline the receipt measured)
  DEAD-RULE   contiguous BRICKID <= 121000 (the rule that killed the predecessor)
  POLAR|c|    bricks sorted by |cos theta| descending (both poles first) — variance-optimal
  EQUATOR     bricks sorted by |cos theta| ascending (worst case, for contrast)
"""
import csv, gzip, io, math, os
import numpy as np
from astropy.io import fits

HERE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.join(HERE, "..", "_tori_parent_row_count_evidence", "footprint_variance_brick_counts_20260814")
RA0, DEC0 = 216.984434295527, 32.060611193471

with fits.open(os.path.join(EV, "static", "survey-bricks-dr10-south.fits.gz")) as h:
    d = h[1].data
    bid = np.asarray(d["brickid"], dtype=np.int64)
    ra = np.asarray(d["ra"], dtype=float)
    dec = np.asarray(d["dec"], dtype=float)

counts = {}
with open(os.path.join(EV, "combined_per_brick_counts.csv")) as f:
    for r in csv.DictReader(f):
        counts[int(r["brickid"])] = int(r["n_cut6_dered"])

n = np.array([counts.get(b, 0) for b in bid], dtype=float)
sel = n > 0
bid, ra, dec, n = bid[sel], ra[sel], dec[sel], n[sel]

r0, d0 = math.radians(RA0), math.radians(DEC0)
c = (np.sin(np.radians(dec)) * math.sin(d0)
     + np.cos(np.radians(dec)) * math.cos(d0) * np.cos(np.radians(ra) - r0))

def stats(mask):
    N = n[mask].sum()
    if N == 0: return 0, 0.0, 0.0
    m = (n[mask] * c[mask]).sum() / N
    v = (n[mask] * (c[mask] - m) ** 2).sum() / N
    return int(N), v, N * v

print(f"bricks with Cut-6 objects: {len(bid):,}   total objects: {int(n.sum()):,}")
print(f"{'strategy':<34}{'bricks':>9}{'N_cut6':>10}{'Var(c)':>9}{'leverage':>11}{'N_eq':>11}")
def row(name, mask):
    N, v, L = stats(mask)
    print(f"{name:<34}{mask.sum():>9,}{N:>10,}{v:>9.4f}{L:>11,.0f}{3*L:>11,.0f}")

row("FULL footprint", np.ones_like(c, bool))
row("DEAD-RULE brickid<=121000", bid <= 121000)

order = np.argsort(-np.abs(c))          # both poles first
cum = np.cumsum(n[order])
for frac, label in ((0.10,"POLAR top 10% of objects"),(0.25,"POLAR top 25%"),(0.50,"POLAR top 50%")):
    k = np.searchsorted(cum, frac * n.sum())
    m = np.zeros_like(c, bool); m[order[:k+1]] = True
    row(label, m)

order_eq = np.argsort(np.abs(c))
k = np.searchsorted(np.cumsum(n[order_eq]), 0.25 * n.sum())
m = np.zeros_like(c, bool); m[order_eq[:k+1]] = True
row("EQUATOR worst 25% (contrast)", m)

# minimal-brick subsets reaching the frozen requirement at assumed acceptance rates
print()
REQ = 100_000
for acc in (0.45, 0.25, 0.10):
    # greedy by |c|: find smallest object-count prefix with 3*acc*N*Var >= REQ
    best = None
    for k in range(1000, len(order), 1000):
        m = np.zeros_like(c, bool); m[order[:k]] = True
        N, v, L = stats(m)
        if 3 * acc * N * v >= REQ:
            best = (k, N, v); break
    if best:
        k, N, v = best
        print(f"acceptance {acc:.0%}: polar selection of {k:,} bricks / {N:,} objects reaches "
              f"{REQ:,} N_eq  (Var {v:.3f})")
    else:
        print(f"acceptance {acc:.0%}: not reachable by polar selection")
