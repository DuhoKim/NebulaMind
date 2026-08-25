#!/usr/bin/env python3
"""Blind independent Phase-5 S2 kinematic shock-crossing calculation.

Uses only the physics in BRIEF_GPT1_BLIND_S2.md and the gated Phase-4 orbit.
No Phase-5 S1/S2 implementation or receipt is imported or read.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[2] / "bhu-theory-phase4-anisotropy-20260823" / "a1_results.csv"
OUT = HERE / "s2_kinematic_pattern.csv"
ETA_OBS = 2.0
OFFSET_FRACTIONS = (0.001, 0.01, 0.05, 0.1)


def load_orbit(path: Path):
    t, sqrt_n = [], []
    with path.open(newline="") as f:
        for row in csv.DictReader(f):
            t.append(float(row["t_over_tcrit"]))
            sqrt_n.append(float(row["sqrtN_hubble_lengths"]))
    if len(t) < 2 or any(b <= a for a, b in zip(t, t[1:])):
        raise ValueError("orbit time column must be strictly increasing")
    return t, sqrt_n


T, SQRT_N = load_orbit(DATA)
LOG_T = [math.log(x) for x in T]
ETA_MIN = 2.0 * math.sqrt(T[0])
ETA_MAX = 2.0 * math.sqrt(T[-1])


def interp_log_t(t: float, values):
    """Piecewise-linear interpolation in log(t), with endpoint tolerance."""
    if t <= T[0]:
        if t < T[0] * (1.0 - 1e-12):
            raise ValueError(f"t={t} below gated orbit")
        return values[0]
    if t >= T[-1]:
        # t_obs=1 differs from the final gated sample by only 1.5e-8.
        if t > 1.0 + 1e-12:
            raise ValueError(f"t={t} above observer epoch")
        return values[-1]
    lo, hi = 0, len(T) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if T[mid] <= t:
            lo = mid
        else:
            hi = mid
    x = math.log(t)
    w = (x - LOG_T[lo]) / (LOG_T[hi] - LOG_T[lo])
    return values[lo] * (1.0 - w) + values[hi] * w


def shock(eta: float):
    """Return (r_star, sqrtN) on the gated orbit."""
    t = 0.25 * eta * eta
    sn = interp_log_t(t, SQRT_N)
    return eta * sn, sn


R_OBS = ETA_OBS * SQRT_N[-1]  # endpoint is t/tcrit=0.999999985


def endpoint_function(eta: float, mu: float, xoff: float) -> float:
    chi = ETA_OBS - eta
    ray_radius = math.sqrt(xoff*xoff + chi*chi + 2.0*xoff*chi*mu)
    return ray_radius - shock(eta)[0]


def crossing(mu: float, xoff: float):
    """Bisection for the unique past-light-cone/shock intersection."""
    lo, hi = ETA_MIN, ETA_MAX
    flo, fhi = endpoint_function(lo, mu, xoff), endpoint_function(hi, mu, xoff)
    if flo < 0.0 or fhi > 0.0:
        return None
    # Direct bracket. A separate limiting-case check in main scans representative
    # rays and verifies that each has exactly one sign change.
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if endpoint_function(mid, mu, xoff) > 0.0:
            lo = mid
        else:
            hi = mid
    eta = 0.5 * (lo + hi)
    chi = ETA_OBS - eta
    radius, sn = shock(eta)
    beta = 1.0 / sn
    # n dot m, where m=(x_off e_z + chi n)/r_star is the outward normal.
    q = (chi + xoff * mu) / radius
    q = max(-1.0, min(1.0, q))
    gamma = 1.0 / math.sqrt(1.0 - beta*beta)
    # Convention: in the FRW frame the static exterior/TOV fluid moves inward,
    # v_TOV=-beta*m. The inward photon has direction -n. Therefore
    # nu_FRW/nu_TOV = 1/[gamma*(1-beta*q)].
    doppler = 1.0 / (gamma * (1.0 - beta*q))
    return {
        "eta": eta, "t": 0.25*eta*eta, "chi": chi, "r": radius,
        "sqrtN": sn, "beta": beta, "q": q,
        "deltaT_over_T": doppler - 1.0,
    }


def solved_crossing(mu: float, xoff: float):
    result = crossing(mu, xoff)
    if result is None:
        raise RuntimeError(f"no gated crossing at mu={mu}, xoff={xoff}")
    return result


def golden_extremum(fn, a, b, maximize=False):
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    c, d = b - gr*(b-a), a + gr*(b-a)
    fc, fd = fn(c), fn(d)
    for _ in range(80):
        take_left = (fc > fd) if maximize else (fc < fd)
        if take_left:
            b, d, fd = d, c, fc
            c = b - gr*(b-a); fc = fn(c)
        else:
            a, c, fc = c, d, fd
            d = a + gr*(b-a); fd = fn(d)
    x = 0.5*(a+b)
    return x, fn(x)


def case_summary(frac: float):
    xoff = frac * R_OBS
    # Existence check over the whole sky. For these cases f(eta_min)>0 for
    # every direction and f(eta_obs)<0, hence the crossing region is 4pi.
    endpoint_margin = min(endpoint_function(ETA_MIN, mu, xoff)
                          for mu in (-1.0, 0.0, 1.0))
    if endpoint_margin <= 0.0:
        raise RuntimeError("crossing is not full-sky; boundary solver required")

    ngrid = 20001
    theta_grid = [math.pi*i/(ngrid-1) for i in range(ngrid)]
    vals = [solved_crossing(math.cos(th), xoff)["deltaT_over_T"] for th in theta_grid]
    i_min = min(range(ngrid), key=vals.__getitem__)
    i_max = max(range(ngrid), key=vals.__getitem__)

    def val(th):
        return solved_crossing(math.cos(th), xoff)["deltaT_over_T"]

    def refine(i, maximize):
        if i in (0, ngrid-1):
            return theta_grid[i], vals[i]
        return golden_extremum(val, theta_grid[i-1], theta_grid[i+1], maximize)

    th_min, v_min = refine(i_min, False)
    th_max, v_max = refine(i_max, True)
    center = solved_crossing(1.0, xoff)
    edge = solved_crossing(-1.0, xoff)
    return {
        "offset_fraction": frac,
        "xoff": xoff,
        "angular_radius_deg": 180.0,
        "full_sky": True,
        "center": center,
        "edge": edge,
        "min": v_min,
        "min_theta_deg": math.degrees(th_min),
        "max": v_max,
        "max_theta_deg": math.degrees(th_max),
        "endpoint_margin": endpoint_margin,
    }


def main():
    cases = [case_summary(f) for f in OFFSET_FRACTIONS]
    fields = [
        "offset_fraction", "xoff", "angular_radius_deg", "full_sky",
        "deltaT_T_min", "min_theta_deg", "deltaT_T_max", "max_theta_deg",
        "deltaT_T_center", "deltaT_T_edge", "center_t_cross", "edge_t_cross",
        "center_beta", "edge_beta", "endpoint_margin_at_eta_min",
    ]
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for c in cases:
            w.writerow({
                "offset_fraction": f"{c['offset_fraction']:.9g}",
                "xoff": f"{c['xoff']:.12g}",
                "angular_radius_deg": f"{c['angular_radius_deg']:.9g}",
                "full_sky": c["full_sky"],
                "deltaT_T_min": f"{c['min']:.12g}",
                "min_theta_deg": f"{c['min_theta_deg']:.12g}",
                "deltaT_T_max": f"{c['max']:.12g}",
                "max_theta_deg": f"{c['max_theta_deg']:.12g}",
                "deltaT_T_center": f"{c['center']['deltaT_over_T']:.12g}",
                "deltaT_T_edge": f"{c['edge']['deltaT_over_T']:.12g}",
                "center_t_cross": f"{c['center']['t']:.12g}",
                "edge_t_cross": f"{c['edge']['t']:.12g}",
                "center_beta": f"{c['center']['beta']:.12g}",
                "edge_beta": f"{c['edge']['beta']:.12g}",
                "endpoint_margin_at_eta_min": f"{c['endpoint_margin']:.12g}",
            })
    max_abs = max(abs(c[k]) for c in cases for k in ("min", "max"))
    print(f"data={DATA}")
    print(f"rows={len(T)} eta_min={ETA_MIN:.12g} r_obs={R_OBS:.12g}")
    for c in cases:
        print(f"f={c['offset_fraction']:.3g} radius=180 deg "
              f"range=[{c['min']:.9g},{c['max']:.9g}] "
              f"center={c['center']['deltaT_over_T']:.9g} "
              f"edge={c['edge']['deltaT_over_T']:.9g}")
    print(f"maximum_abs_deltaT_over_T={max_abs:.12g}")
    print(f"ratio_to_1e-5={max_abs/1e-5:.12g}")
    print(f"wrote={OUT}")


if __name__ == "__main__":
    main()
