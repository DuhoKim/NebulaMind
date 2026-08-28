#!/usr/bin/env python3
"""The propagation kernel K for the sensitivity-gradient control (BS-3 side, DESIGN/UNFILLED).

WHAT THIS IS
------------
The gain control measures how the instrument's recovered amplitude varies with image quality (`β`,
which needs cutouts) and converts that into a gradient along the tested axis (`γ = β·K`). **K needs
no images**: it is catalogue metadata and frozen geometry. Computing and freezing it now fixes the
conversion before any cutout is fetched, so `β` cannot later be paired with a kernel chosen to suit
it.

Design: `gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`.

WHAT IS AND IS NOT CLAIMED
--------------------------
K is a property of the *sample and the axis*, not of the instrument. It says nothing about whether
the instrument has a gain gradient — only what a given gradient would project to. It does not close
conditional independence, and it does not bound chirality introduced upstream of the raster or
selection by a non-equivariant process.

WHY THE CONTROLS LOOK LIKE THIS
-------------------------------
Three guards written on 2026-08-28 reported clean while unable to fail, and a control battery passed
twice with checks deleted, because each control accepted a superset of what it meant. So every check
here names an exact expected outcome, and `--self-test` asserts each control produces exactly that.
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bs2a_quality_gate as G          # noqa: E402  authenticated read + frozen predicate
import successor_ref_v9 as V9          # noqa: E402  FROZEN axis and cos_theta

# ── Frozen. The v9 digest is checked because AXIS and cos_theta() come from it. ──────────────────
V9_SHA256 = "6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148"

# Values this module must reproduce. PRECUT_CORR is the figure already carried in
# bs2a_quality_gate.py's docstring; reproducing it is the convention check — if the coordinate or
# axis convention here differed from the one that produced it, this number would move.
PRECUT_CORR = 0.3659
RETAINED_CORR = 0.4188
K_PSFSIZE = 0.483014
# Vector kernel: the acceptance statistic is gamma = beta^T K over ALL THREE quality variables.
# A univariate psfsize slope cannot stand in for them - flux_ivar_r and nobs_r correlate at
# +0.7176 on the retained sample (GPT56-V32-3).
K_VECTOR = {"flux_ivar_r": -0.270181, "psfsize_r": +0.483014, "nobs_r": -0.317419}
RETAINED_N = 49_211
TOL = 5e-5


def _v9_digest() -> str:
    return G.verified_bytes.__globals__["hashlib"].sha256(
        Path(V9.__file__).read_bytes()).hexdigest()


def load(acquire: Path):
    """Authenticated evidence joined to authenticated positions. One read path, digest-bound."""
    ev, _ = G.build_evidence(acquire / "positions_selected.csv", acquire / "quality_selected.csv")
    raw = G.verified_bytes(acquire / "positions_selected.csv", G.PARENT_SHA256).decode("utf-8")
    pos = {(r["brickid"].strip(), r["objid"].strip()): r for r in csv.DictReader(io.StringIO(raw))}
    if len(pos) != G.PARENT_ROWS:
        raise G.QualityGateError(f"positions hold {len(pos)} unique keys, expected {G.PARENT_ROWS}")
    return ev, pos


def columns(ev, pos, retained_only: bool):
    rows = [e for e in ev if e["quality_pass"]] if retained_only else list(ev)
    ra = np.array([float(pos[(e["brickid"], e["objid"])]["ra"]) for e in rows])
    dec = np.array([float(pos[(e["brickid"], e["objid"])]["dec"]) for e in rows])
    q = np.array([e["psfsize_r"] for e in rows])
    return q, V9.cos_theta(ra, dec)


def kernel(q, ct, normalise: bool = True) -> float:
    """K = Cov(s, cosθ)/Var(cosθ) with s the quality normalised to unit variance.

    Normalising is what makes β dimensionless ("fractional gain change per 1σ of seeing"); without
    it K silently carries the units of psfsize_r and β means something else. `normalise=False`
    exists so a control can delete that step and show K moves — scaling the *input* cannot
    demonstrate it, because the normalisation is inside this function and divides the scale straight
    back out.
    """
    s = (q - q.mean()) / q.std(ddof=1) if normalise else q
    return float(np.cov(s, ct, ddof=1)[0, 1] / ct.var(ddof=1))


def report(acquire: Path) -> int:
    if _v9_digest() != V9_SHA256:
        print(f"  REFUSED: v9 digest moved; AXIS and cos_theta are not the frozen ones")
        return 1
    ev, pos = load(acquire)
    q_all, ct_all = columns(ev, pos, retained_only=False)
    q_ret, ct_ret = columns(ev, pos, retained_only=True)

    bad_vec = []
    pre = float(np.corrcoef(q_all, ct_all)[0, 1])
    ret = float(np.corrcoef(q_ret, ct_ret)[0, 1])
    K = kernel(q_ret, ct_ret)
    north = ct_ret >= 0
    s = (q_ret - q_ret.mean()) / q_ret.std(ddof=1)

    print(f"  axis (frozen v9)      {list(V9.AXIS)}")
    print(f"  retained N            {len(q_ret):,}")
    print(f"  corr pre-cut          {pre:+.4f}   (expected {PRECUT_CORR:+.4f} — convention check)")
    print(f"  corr retained         {ret:+.4f}   (expected {RETAINED_CORR:+.4f})")
    print(f"  Var(cos theta)        {ct_ret.var(ddof=1):.6f}")
    print(f"  K (psfsize_r)         {K:+.6f}   (expected {K_PSFSIZE:+.6f})")
    print("  vector kernel K_j (gamma = beta^T K):")
    for name, want in K_VECTOR.items():
        qj = np.array([e[name] for e in ev if e["quality_pass"]])
        kj = kernel(qj, ct_ret)
        flag = "" if abs(kj - want) <= TOL else f"  <-- MISMATCH, frozen {want:+.6f}"
        print(f"    K[{name:<12}] = {kj:+.6f}{flag}")
        if abs(kj - want) > TOL:
            bad_vec.append(f"K[{name}] {kj:.6f} != frozen {want}")
    print(f"  hemisphere delta      {s[north].mean() - s[~north].mean():+.4f} sigma "
          f"(n+ {int(north.sum()):,}, n- {int((~north).sum()):,})")
    print(f"  cut RAISED the coupling: {pre:+.4f} -> {ret:+.4f}")

    bad = list(bad_vec)
    if len(q_ret) != RETAINED_N:
        bad.append(f"retained N {len(q_ret)} != {RETAINED_N}")
    if abs(pre - PRECUT_CORR) > 1e-4:
        bad.append(f"pre-cut corr {pre:.6f} != frozen {PRECUT_CORR}")
    if abs(K - K_PSFSIZE) > TOL:
        bad.append(f"K {K:.6f} != frozen {K_PSFSIZE}")
    if ret <= pre:
        bad.append(f"retained corr {ret:.4f} not greater than pre-cut {pre:.4f}")
    for b in bad:
        print(f"  REFUSED: {b}")
    return 1 if bad else 0


# ── Controls. Each must change the kernel in a stated direction, or it is not load-bearing. ──────

def _c_wrong_axis(q, ct):
    """A different axis must move K. If it does not, K is not axis-dependent and the whole
    conversion is meaningless."""
    return q, -ct


def _c_unnormalised(q, ct):
    """Deleting the normalisation step must move K, since psfsize_r carries units. Marked by a
    sentinel the runner turns into `normalise=False`; scaling q here would prove nothing."""
    return q, ct


def _c_shuffled(q, ct):
    """Breaking the quality-position pairing must drive K to ~0. This is the null: it proves K
    measures a real association rather than an artefact of the arithmetic."""
    rng = np.random.default_rng(20260828)
    return rng.permutation(q), ct


CONTROLS = (
    ("axis reversed",        _c_wrong_axis,   "sign flips"),
    ("quality unnormalised", _c_unnormalised, "magnitude changes"),
    ("pairing shuffled",     _c_shuffled,     "collapses to ~0"),
)


def self_test(acquire: Path) -> int:
    if not (acquire / "positions_selected.csv").is_file():
        print(f"  FAIL sources not found under {acquire}")
        return 1
    ev, pos = load(acquire)
    q, ct = columns(ev, pos, retained_only=True)
    base = kernel(q, ct)
    ok0 = abs(base - K_PSFSIZE) <= TOL
    print(f"  {'OK  ' if ok0 else 'FAIL'} baseline K = {base:+.6f}")
    fails = [] if ok0 else ["baseline"]

    checks = {
        "axis reversed":        lambda k: abs(k + base) < TOL,
        "quality unnormalised": lambda k: abs(k - base) > TOL,
        "pairing shuffled":     lambda k: abs(k) < 0.02,
    }
    for name, mutate, expect in CONTROLS:
        qm, ctm = mutate(q.copy(), ct.copy())
        k = kernel(qm, ctm, normalise=(name != "quality unnormalised"))
        ok = checks[name](k)
        print(f"  {'OK  ' if ok else 'FAIL'} {name}: K = {k:+.6f} ({expect})")
        if not ok:
            fails.append(name)

    if _v9_digest() != V9_SHA256:
        print("  FAIL v9 digest moved")
        fails.append("v9")
    else:
        print("  OK   v9 freeze intact")

    print(f"  self-test: {len(CONTROLS) + 1} controls, {len(fails)} failure(s)")
    return 1 if fails else 0


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--acquire", default="")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    d = Path(a.acquire) if a.acquire else Path(__file__).resolve().parent.parent / "acquire"
    if a.self_test:
        print("gain-gradient kernel self-test")
        return self_test(d)
    print("gain-gradient kernel")
    return report(d)


if __name__ == "__main__":
    sys.exit(main())
