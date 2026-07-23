#!/usr/bin/env python3
"""nm_alpha_knee.py — the age-resolved alpha-knee for the NebulaMind Lab runner.

The "alpha-knee" is the [Fe/H] at which [alpha/Fe] turns over from the
core-collapse plateau to the SN-Ia-driven decline: a chemical clock for the
star-formation timescale of a stellar population. Its dependence on
*galactocentric radius* is a classic inside-out-disk probe; its dependence on
*stellar age* is the genuinely novel, still-contested axis this module opens.
We map [Fe/H]_knee across an (R_g x age) grid of APOGEE giants and measure both
partial gradients, d[Fe/H]_knee/d(age)|_{R_g} and d[Fe/H]_knee/dR_g|_{age}.

Data (SDSS DR18 SkyServer, raw-HTTP, no astroquery): an in-process 3-table join
on APOGEE_ID of
  * apogeeDistMass  -> spectroscopic C/N age [yr] + heliocentric distance [pc]
                       (giants; realistic 1-14 Gyr ages),
  * apogeeStar      -> Galactic coordinates glon, glat, and combined-spectrum SNR,
  * aspcapStar      -> fe_h, mg_fe / o_fe / si_fe, calibrated m_h, alpha_m
                       (+ *_err), aspcapflag and per-element flags.
The value-added-catalog WHERE-clause aggregates on the 156-column aspcapStar
return HTTP 500 on SkyServer, so we pull *bare columns* chunked by sky region
(RA-hour x hemisphere via the 2MASS APOGEE_ID prefix), paced, retried and
disk-cached by nm_external_data, then apply the flag/quality cuts in-process.

Non-circularity: the headline age-gradient is recomputed with an abundance-scale
swap (calibrated fe_h <-> calibrated m_h on the metallicity axis, and
[Mg/Fe] <-> [alpha/M] on the alpha axis). We report noncircular_robust=True only
if the SIGN of the gradient survives the swap.

CLI self-test:  python3 tools/nm_alpha_knee.py            # paced few-chunk pull
"""
from __future__ import annotations
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nm_external_data import skyserver_sql, id_join, to_arrays  # noqa: E402

_SENTINEL = -9000.0          # APOGEE fill value is -9999; anything below this is "missing"
_STAR_BAD = 1 << 23          # ASPCAPFLAG bit 23 (STAR_BAD)


# ----------------------------------------------------------------------------- pull
def _chunk_patterns(spec):
    """LIKE patterns that partition the APOGEE 2MASS-designated sample by sky
    region: RA-hour x hemisphere. 'ra_chunks' overrides; else ra_hours x signs."""
    if spec.get("ra_chunks"):
        return list(spec["ra_chunks"])
    hours = spec.get("ra_hours", list(range(24)))          # 00..23
    signs = spec.get("signs", ["+", "-"])                  # N / S galactic hemisphere of dec
    # APOGEE_ID = '2M' + HHMMSSss + <sign> + DDMMSSs : 6 wildcard chars, then the sign.
    return [f"2M{h:02d}" + "_" * 6 + s + "%" for h in hours for s in signs]


def _pull_chunk(pat, *, pace, cache=True):
    """Pull the 3 tables for one sky-region chunk (bare columns, minimal WHERE)."""
    dm = skyserver_sql(
        "SELECT TOP 200000 apogee_id, age, distance FROM apogeeDistMass "
        f"WHERE apogee_id LIKE '{pat}' AND age>0 AND distance>0", cache=cache)
    st = skyserver_sql(
        "SELECT TOP 200000 apogee_id, glon, glat, snr FROM apogeeStar "
        f"WHERE apogee_id LIKE '{pat}'", cache=cache)
    ap = skyserver_sql(
        "SELECT TOP 200000 apogee_id, fe_h, fe_h_err, m_h, m_h_err, alpha_m, alpha_m_err, "
        "mg_fe, mg_fe_err, o_fe, o_fe_err, si_fe, si_fe_err, "
        "aspcapflag, fe_h_flag, mg_fe_flag, teff, logg FROM aspcapStar "
        f"WHERE apogee_id LIKE '{pat}'", cache=cache)
    # in-process 3-way inner join on the shared string key
    joined = id_join(id_join(dm, st, "apogee_id"), ap, "apogee_id")
    if pace and not (cache and joined):          # be polite to SkyServer between live pulls
        time.sleep(pace)
    return joined


def _assemble(spec, logfn):
    """Pull every requested chunk, join, and return numpy column arrays."""
    pats = _chunk_patterns(spec)
    pace = float(spec.get("pace_s", 7.0))
    rows = []
    for i, pat in enumerate(pats):
        try:
            j = _pull_chunk(pat, pace=pace)
        except Exception as e:                    # one flaky chunk must not sink the run
            logfn(f"alpha-knee: chunk {pat} failed ({type(e).__name__}: {str(e)[:60]}), skipping")
            continue
        rows.extend(j)
        if logfn and (i % 6 == 0 or i == len(pats) - 1):
            logfn(f"alpha-knee: pulled {i + 1}/{len(pats)} sky chunks, {len(rows):,} joined rows so far")
    cols = ["age", "distance", "glon", "glat", "snr", "fe_h", "fe_h_err",
            "m_h", "m_h_err", "alpha_m", "alpha_m_err", "mg_fe", "mg_fe_err",
            "o_fe", "o_fe_err", "si_fe", "si_fe_err",
            "aspcapflag", "fe_h_flag", "mg_fe_flag", "teff", "logg"]
    return to_arrays(rows, cols), len(rows)


# ----------------------------------------------------------------------------- geometry + cuts
def _galactocentric_radius(glon, glat, dist_kpc, R0):
    """R_g from heliocentric distance and Galactic coordinates (planar projection)."""
    l = np.radians(glon); b = np.radians(glat)
    dp = dist_kpc * np.cos(b)                      # projection onto the Galactic plane
    x = R0 - dp * np.cos(l)
    y = dp * np.sin(l)
    return np.sqrt(x * x + y * y)


def _quality_mask(c, spec, met, alpha, met_err, alpha_err):
    """Flag + quality cuts, applied in-process on the bare-column pull."""
    finite = (met > _SENTINEL) & (alpha > _SENTINEL) & \
             (met_err > 0) & (met_err < float(spec.get("err_max", 0.2))) & \
             (alpha_err > 0) & (alpha_err < float(spec.get("err_max", 0.2)))
    age_g = c["age"] / 1e9
    good = finite & np.isfinite(age_g) & (age_g >= float(spec.get("age_min", 1.0))) & \
        (age_g <= float(spec.get("age_max", 14.0))) & (c["distance"] > 0) & \
        (c["snr"] >= float(spec.get("snr_min", 70.0)))
    flags = np.nan_to_num(c["aspcapflag"], nan=0.0).astype(np.int64)
    good &= (flags & _STAR_BAD) == 0               # drop ASPCAP STAR_BAD
    if str(spec.get("flag_strictness", "loose")).lower() == "strict":
        good &= (np.nan_to_num(c["fe_h_flag"], nan=1) == 0) & \
                (np.nan_to_num(c["mg_fe_flag"], nan=1) == 0)
    return good


# ----------------------------------------------------------------------------- knee fit
def _broken_line_knee(fe, al, spec):
    """Locate [Fe/H]_knee where the high-alpha ridge bends from plateau to decline.

    Method: trace the upper-envelope (high-alpha) ridge as the p_ridge percentile
    of [alpha] in narrow [Fe/H] bins, then brute-force a continuous broken line
    y = b0 + b1*fe + b2*(fe-k)_+ over the breakpoint k, keeping the fit that both
    minimises SSE and shows a downturn (b2 < 0). Returns (knee, ok)."""
    ridge_pct = float(spec.get("ridge_pct", 75.0))
    nb = int(spec.get("fe_nbins", 14))
    minbin = int(spec.get("min_per_febin", 8))
    lo, hi = np.percentile(fe, [3, 97])
    lo = max(lo, -1.4); hi = min(hi, 0.55)
    if not (hi - lo > 0.35):
        return np.nan, False
    edges = np.linspace(lo, hi, nb + 1)
    cen, yr, wr = [], [], []
    for i in range(nb):
        s = (fe >= edges[i]) & (fe < edges[i + 1])
        if s.sum() >= minbin:
            cen.append(0.5 * (edges[i] + edges[i + 1]))
            yr.append(np.percentile(al[s], ridge_pct))
            wr.append(np.sqrt(s.sum()))
    cen = np.array(cen); yr = np.array(yr); wr = np.array(wr)
    if len(cen) < 6:
        return np.nan, False
    # candidate breakpoints: interior ridge nodes (never the two end nodes)
    W = np.sqrt(wr)
    best = (np.inf, np.nan, 0.0)
    for k in cen[2:-2]:
        X = np.column_stack([np.ones_like(cen), cen, np.clip(cen - k, 0, None)])
        beta, *_ = np.linalg.lstsq(X * W[:, None], yr * W, rcond=None)
        sse = float(np.sum((W * (yr - X @ beta)) ** 2))
        if beta[2] < 0 and sse < best[0]:          # require a genuine downturn past the knee
            best = (sse, float(k), float(beta[2]))
    return best[1], np.isfinite(best[1])


def _knee_with_error(fe, al, spec, rng, nboot):
    """Point knee + bootstrap error over resampled stars in the cell."""
    k0, ok = _broken_line_knee(fe, al, spec)
    if not ok:
        return np.nan, np.nan
    ks = []
    n = len(fe)
    for _ in range(nboot):
        idx = rng.integers(0, n, n)
        kb, okb = _broken_line_knee(fe[idx], al[idx], spec)
        if okb:
            ks.append(kb)
    err = float(np.std(ks)) if len(ks) >= max(5, nboot // 3) else np.nan
    return k0, err


# ----------------------------------------------------------------------------- grid + gradients
def _grid(rg, age_g, fe, al, spec, rng):
    rg_edges = np.array(spec.get("rg_edges", [0, 3, 5, 7, 9, 11, 13, 15]), float)
    age_edges = np.array(spec.get("age_edges", [1, 3, 5, 7, 9, 11, 14]), float)
    min_n = int(spec.get("min_n_cell", 40))
    nboot = int(spec.get("n_boot", 100))
    nr, na = len(rg_edges) - 1, len(age_edges) - 1
    knee = np.full((nr, na), np.nan); kerr = np.full((nr, na), np.nan)
    ncell = np.zeros((nr, na), int)
    for i in range(nr):
        rsel = (rg >= rg_edges[i]) & (rg < rg_edges[i + 1])
        for j in range(na):
            s = rsel & (age_g >= age_edges[j]) & (age_g < age_edges[j + 1])
            ncell[i, j] = int(s.sum())
            if s.sum() >= min_n:
                knee[i, j], kerr[i, j] = _knee_with_error(fe[s], al[s], spec, rng, nboot)
    rg_c = 0.5 * (rg_edges[:-1] + rg_edges[1:])
    age_c = 0.5 * (age_edges[:-1] + age_edges[1:])
    return rg_c, age_c, knee, kerr, ncell


def _partial_gradients(rg_c, age_c, knee, kerr):
    """Weighted multiple regression knee ~ b0 + b_age*age + b_rg*R_g over finite cells.
    b_age = d[Fe/H]_knee/d(age)|_{R_g};  b_rg = d[Fe/H]_knee/dR_g|_{age}."""
    X, y, w = [], [], []
    for i, rg in enumerate(rg_c):
        for j, ag in enumerate(age_c):
            k, e = knee[i, j], kerr[i, j]
            if np.isfinite(k) and np.isfinite(e) and e > 0:
                X.append([1.0, ag, rg]); y.append(k); w.append(1.0 / e ** 2)
    X = np.array(X); y = np.array(y); w = np.array(w)
    if len(y) < 4 or np.ptp(X[:, 1]) == 0 or np.ptp(X[:, 2]) == 0:
        return None
    beta, *_ = np.linalg.lstsq(X * np.sqrt(w)[:, None], y * np.sqrt(w), rcond=None)
    XtWX = (X * w[:, None]).T @ X
    cov = np.linalg.inv(XtWX)
    resid = y - X @ beta
    s2 = float(np.sum(w * resid ** 2) / max(1, len(y) - 3))
    covm = cov * s2
    return {"dknee_dage": [float(beta[1]), float(np.sqrt(covm[1, 1]))],
            "dknee_dRg": [float(beta[2]), float(np.sqrt(covm[2, 2]))],
            "n_cells": int(len(y))}


# ----------------------------------------------------------------------------- axis selection
def _axes(c, spec, swap):
    """Return (metallicity, alpha, met_err, alpha_err) for the primary or the
    abundance-scale-swapped run."""
    elem = str(spec.get("alpha_element", "mg")).lower()
    fe = c["fe_h"]
    if swap:
        # calibrated [Fe/H] -> calibrated [M/H];  [X/Fe] -> [alpha/M]
        met = c["m_h"]; met_err = c["m_h_err"]
        al = c["alpha_m"]; al_err = c["alpha_m_err"]
    else:
        met = fe; met_err = c["fe_h_err"]
        col = {"mg": "mg_fe", "o": "o_fe", "si": "si_fe"}.get(elem, "mg_fe")
        al = c[col]; al_err = c[col + "_err"]
    return met, al, met_err, al_err


# ----------------------------------------------------------------------------- entry point
def run_alpha_knee(spec, logfn=None, rng=None):
    """Build the age-resolved alpha-knee and return a `res` dict.

    Keys: knee (headline representative [Fe/H]_knee), noncircular_robust,
    grid, gradients, summary, title, provenance, n_stars, n_cells_fit.
    """
    logfn = logfn or (lambda m: None)
    rng = rng or np.random.default_rng(int(spec.get("seed", 20260724)))
    R0 = float(spec.get("R0", 8.122))

    cols, n_raw = _assemble(spec, logfn)
    if n_raw == 0:
        raise RuntimeError("alpha-knee: no joined APOGEE rows pulled (check chunks/network)")

    # primary axes + quality mask
    met, al, met_err, al_err = _axes(cols, spec, swap=False)
    good = _quality_mask(cols, spec, met, al, met_err, al_err)
    n_good = int(good.sum())
    logfn(f"alpha-knee: {n_good:,} giants pass flag/quality cuts (of {n_raw:,} joined)")
    if n_good < int(spec.get("min_n_cell", 40)) * 2:
        raise RuntimeError(f"alpha-knee: only {n_good} stars survive cuts — insufficient for a grid")

    age_g = (cols["age"] / 1e9)[good]
    dist_kpc = (cols["distance"] / 1000.0)[good]
    rg = _galactocentric_radius(cols["glon"][good], cols["glat"][good], dist_kpc, R0)
    fe = met[good]; alv = al[good]

    rg_c, age_c, knee, kerr, ncell = _grid(rg, age_g, fe, alv, spec, rng)
    n_cells_fit = int(np.isfinite(knee).sum())
    grad = _partial_gradients(rg_c, age_c, knee, kerr)

    # --- non-circularity: recompute headline age-gradient with the abundance-scale swap ---
    met2, al2, met2_err, al2_err = _axes(cols, spec, swap=True)
    good2 = _quality_mask(cols, spec, met2, al2, met2_err, al2_err)
    grad2 = None
    if good2.sum() >= int(spec.get("min_n_cell", 40)) * 2:
        age2 = (cols["age"] / 1e9)[good2]
        rg2 = _galactocentric_radius(cols["glon"][good2], cols["glat"][good2],
                                     (cols["distance"] / 1000.0)[good2], R0)
        _, _, knee2, kerr2, _ = _grid(rg2, age2, met2[good2], al2[good2], spec, rng)
        grad2 = _partial_gradients(rg_c, age_c, knee2, kerr2)

    g_age = grad["dknee_dage"][0] if grad else np.nan
    g_age2 = grad2["dknee_dage"][0] if grad2 else np.nan
    noncircular_robust = bool(np.isfinite(g_age) and np.isfinite(g_age2)
                              and np.sign(g_age) == np.sign(g_age2) and g_age != 0)

    finite_knees = knee[np.isfinite(knee)]
    knee_med = float(np.median(finite_knees)) if finite_knees.size else float("nan")

    res = {
        "knee": knee_med,
        "noncircular_robust": noncircular_robust,
        "n_stars": n_good,
        "n_cells_fit": n_cells_fit,
        "grid": {
            "rg_centers": [float(x) for x in rg_c],
            "age_centers": [float(x) for x in age_c],
            "knee": [[None if not np.isfinite(v) else float(v) for v in row] for row in knee],
            "knee_err": [[None if not np.isfinite(v) else float(v) for v in row] for row in kerr],
            "n": [[int(v) for v in row] for row in ncell],
        },
        "gradients": {
            "dknee_dage": grad["dknee_dage"] if grad else None,
            "dknee_dRg": grad["dknee_dRg"] if grad else None,
            "dknee_dage_swap": grad2["dknee_dage"] if grad2 else None,
            "dknee_dRg_swap": grad2["dknee_dRg"] if grad2 else None,
        },
    }

    elem = str(spec.get("alpha_element", "mg")).lower()
    ga_s = (f"{grad['dknee_dage'][0]:+.4f}+/-{grad['dknee_dage'][1]:.4f} dex/Gyr" if grad else "not constrained")
    gr_s = (f"{grad['dknee_dRg'][0]:+.4f}+/-{grad['dknee_dRg'][1]:.4f} dex/kpc" if grad else "not constrained")
    res["summary"] = (
        f"Age-resolved alpha-knee from an APOGEE (DR18) 3-table join of {n_good:,} giants "
        f"(apogeeDistMass C/N ages + distances, apogeeStar Galactic coordinates, aspcapStar "
        f"[Fe/H]-[{elem.upper()}/Fe]). The [Fe/H]_knee is located per (R_g x age) cell with a "
        f"broken-line ridge fit (bootstrap error) in {n_cells_fit} populated cells; median "
        f"[Fe/H]_knee = {knee_med:+.2f}. Gradients: d[Fe/H]_knee/d(age)|_R_g = {ga_s}; "
        f"d[Fe/H]_knee/dR_g|_age = {gr_s}. Non-circularity: the age-gradient sign "
        f"{'HOLDS' if noncircular_robust else 'does NOT hold'} under the abundance-scale swap "
        f"([Fe/H]->[M/H], [{elem.upper()}/Fe]->[alpha/M])."
    )
    res["title"] = (
        f"An age dependence of the Galactic alpha-knee across galactocentric radius"
        if noncircular_robust and grad else
        f"Mapping the Galactic alpha-knee across stellar age and galactocentric radius"
    )
    res["provenance"] = (
        "Real SDSS DR18 APOGEE catalog data via SkyServer raw-HTTP (no astroquery). Three tables "
        "(apogeeDistMass, apogeeStar, aspcapStar) are pulled as bare columns, chunked by sky region "
        "with pacing + retry/backoff + disk cache, and joined in-process on APOGEE_ID; flag/quality "
        "cuts (STAR_BAD, per-element flags, SNR, abundance errors, 1-14 Gyr ages) are applied in "
        "Python. R_g is computed from glon/glat/distance with R0="
        f"{R0:.3f} kpc. Ages are spectroscopic C/N (data-driven) and carry the known C/N-age "
        "systematics; the alpha-knee and its gradients are the reported quantities, and the "
        "non-circularity test swaps the abundance calibration scale, not the data set."
    )
    return res


# ----------------------------------------------------------------------------- plotting
def plot_knee(res, plt):
    """Draw the (R_g x age) [Fe/H]_knee grid onto the supplied matplotlib `plt`."""
    g = res["grid"]
    rg = np.array(g["rg_centers"]); age = np.array(g["age_centers"])
    K = np.array([[np.nan if v is None else v for v in row] for row in g["knee"]])
    # cell edges for pcolormesh
    def _edges(c):
        c = np.asarray(c, float)
        if len(c) == 1:
            return np.array([c[0] - 0.5, c[0] + 0.5])
        m = 0.5 * (c[:-1] + c[1:])
        return np.concatenate([[c[0] - (m[0] - c[0])], m, [c[-1] + (c[-1] - m[-1])]])
    ax = plt.gca()
    pm = ax.pcolormesh(_edges(age), _edges(rg), np.ma.masked_invalid(K),
                       cmap="viridis", shading="flat")
    cb = plt.colorbar(pm, ax=ax); cb.set_label(r"[Fe/H]$_{\rm knee}$")
    for i, r in enumerate(rg):
        for j, a in enumerate(age):
            if np.isfinite(K[i, j]):
                ax.text(a, r, f"{K[i, j]:+.2f}", ha="center", va="center",
                        fontsize=7, color="white")
    grad = res.get("gradients") or {}
    ga = grad.get("dknee_dage"); gr = grad.get("dknee_dRg")
    sub = []
    if ga: sub.append(rf"$d/d({{\rm age}})={ga[0]:+.3f}\pm{ga[1]:.3f}$ dex/Gyr")
    if gr: sub.append(rf"$d/dR_g={gr[0]:+.3f}\pm{gr[1]:.3f}$ dex/kpc")
    ax.set_xlabel("age [Gyr]"); ax.set_ylabel(r"$R_g$ [kpc]")
    ax.set_title("Age-resolved Galactic $\\alpha$-knee" +
                 ("\n" + ";  ".join(sub) if sub else ""), fontsize=9)


# ----------------------------------------------------------------------------- CLI self-test
if __name__ == "__main__":
    t0 = time.time()
    spec = {
        # modest paced pull: 2 RA-hours x 2 hemispheres = 4 sky chunks (inner disk/bulge)
        "ra_hours": [17, 18], "signs": ["+", "-"], "pace_s": 6.0,
        "rg_edges": [0, 3, 5, 7, 9, 11], "age_edges": [1, 4, 7, 10, 14],
        "min_n_cell": 40, "n_boot": 80, "snr_min": 70, "alpha_element": "mg",
    }
    print("nm_alpha_knee self-test — paced APOGEE pull (4 sky chunks)…")
    r = run_alpha_knee(spec, logfn=lambda m: print("  ", m))
    print(f"\nstars used: {r['n_stars']:,} | cells fit: {r['n_cells_fit']} | "
          f"median knee: {r['knee']:+.3f}")
    g = r["grid"]
    print("\n[Fe/H]_knee grid  (rows=R_g kpc, cols=age Gyr):")
    hdr = "  R_g\\age " + "".join(f"{a:>8.1f}" for a in g["age_centers"])
    print(hdr)
    for i, rg in enumerate(g["rg_centers"]):
        cells = []
        for j in range(len(g["age_centers"])):
            v = g["knee"][i][j]; e = g["knee_err"][i][j]
            cells.append("     .  " if v is None else f"{v:+6.2f} ")
        print(f"  {rg:6.1f}  " + "".join(cells))
    print("\ngradients:", r["gradients"])
    print("noncircular_robust:", r["noncircular_robust"])
    print(f"\nelapsed: {time.time() - t0:.0f}s")
