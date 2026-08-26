#!/usr/bin/env python3
"""Blind independent Phase 5b/P6 TOV optical-transfer calculation.

Reads only the gated Phase-4 orbit CSV named in BRIEF_GPT1_BLIND_P6.md.
Writes all products beside this script.  No earlier P5/P6 implementation is used.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import cumulative_trapezoid, quad, solve_ivp
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
INPUT = (HERE / "../../../bhu-theory-phase4-anisotropy-20260823/a1_results.csv").resolve()
T0_K = 2.7255
DIPOLE_LIMIT_K = 3.7e-3
DELTA_LIMIT = DIPOLE_LIMIT_K / T0_K
W_GRID = np.linspace(0.01, 0.999, 100)
LAMBDA_GRID = np.logspace(-4, 4, 81)
ETA_OBS = 2.0
HORIZON_EPS = 1e-10


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load_orbit():
    with INPUT.open(newline="") as f:
        rows = list(csv.DictReader(f))
    t = np.asarray([float(r["t_over_tcrit"]) for r in rows])
    keys = ["sqrtN_hubble_lengths", "u_pbar_over_rho", "v_rhobar_over_rho"]
    vals = {k: np.asarray([float(r[k]) for r in rows]) for k in keys}
    if not np.all(np.diff(t) > 0):
        raise RuntimeError("gated orbit time is not strictly increasing")
    interp = {k: PchipInterpolator(np.log(t), np.log(v)) for k, v in vals.items()}
    return rows, t, vals, interp


ROWS, T_TAB, V_TAB, INTERP = load_orbit()


def shock(eta: float) -> dict[str, float]:
    t = (eta / 2.0) ** 2
    if not (T_TAB[0] <= t <= T_TAB[-1]):
        raise ValueError(f"eta={eta} lies outside the gated orbit")
    out = {k: math.exp(float(p(math.log(t)))) for k, p in INTERP.items()}
    out["t"] = t
    out["N"] = out["sqrtN_hubble_lengths"] ** 2
    out["rstar"] = eta * out["sqrtN_hubble_lengths"]
    out["junction_w"] = out["u_pbar_over_rho"] / out["v_rhobar_over_rho"]
    return out


def rstar(eta: float) -> float:
    return shock(eta)["rstar"]


def centre_crossing() -> float:
    # At x_off=0, chi=rstar(eta) and chi=eta_obs-eta.
    f = lambda eta: ETA_OBS - eta - rstar(eta)
    grid = np.linspace(max(2 * math.sqrt(T_TAB[0]) * 1.001, 1e-5), 1.999999, 2000)
    brackets = [(a, b) for a, b in zip(grid[:-1], grid[1:]) if f(a) * f(b) < 0]
    if len(brackets) != 1:
        raise RuntimeError(f"expected one centre crossing, found {len(brackets)}")
    return brentq(f, *brackets[0], xtol=2e-14, rtol=2e-14)


ETA0 = centre_crossing()
S0 = shock(ETA0)
CHI0 = ETA_OBS - ETA0


def tov_profile(w: float, eta: float) -> dict[str, np.ndarray | float]:
    """Integrate from the shock toward the past horizon N->1.

    z=ln(rbar/rbar_shock), C=kappa*rho*rbar^2, and L=ln(|B|/|B_s|).
    The branch z>0 is the past-directed branch for a black-hole interior.
    """
    s = shock(eta)
    N0 = s["N"]
    C0 = 3.0 * s["v_rhobar_over_rho"] * N0  # exact from pinned shock state
    q = (1.0 + w) / (2.0 * w)

    # The pressure equation integrates exactly to
    # rho/rho_s=[(N-1)/(N_s-1)]^q.  Use that algebraic first integral
    # rather than evolving a tiny C independently near the horizon.
    def rhs(z, y):
        N, L = y
        rho_rel = max((N - 1.0) / (N0 - 1.0), 0.0) ** q
        C = C0 * math.exp(2.0 * z) * rho_rel
        dN = -N - w * C
        dL = -(N + C) / (N - 1.0)
        return dN, dL

    def horizon(z, y):
        return y[0] - 1.0 - HORIZON_EPS

    horizon.terminal = True
    horizon.direction = -1
    sol = solve_ivp(
        rhs, (0.0, 8.0), (N0, 0.0), events=horizon,
        rtol=2e-9, atol=1e-12, max_step=1e-3,
    )
    if not sol.success or len(sol.t_events[0]) != 1:
        raise RuntimeError(f"TOV horizon integration failed at w={w}, eta={eta}: {sol.message}")
    z = sol.t
    N, L = sol.y
    rho_rel = np.maximum((N - 1.0) / (N0 - 1.0), 0.0) ** q
    C = C0 * np.exp(2.0 * z) * rho_rel
    theta_rel = rho_rel ** (w / (1.0 + w))
    g = np.exp(0.5 * L)  # comoving photon frequency at shock / at depth
    source_I = (g * theta_rel) ** 4

    # Grey absorption depth. lambda is defined so d(tau)/dz=lambda at the shock.
    h = rho_rel * np.exp(z) * np.sqrt((N0 - 1.0) / (N - 1.0))
    H = np.r_[0.0, cumulative_trapezoid(h, z)]
    # At very small w the density underflows before the horizon, so H can
    # become numerically flat.  Those zero-opacity tail points carry no
    # transfer weight; remove them before constructing the monotone spline.
    tolH = max(1e-18, float(H[-1]) * 1e-14)
    keep = np.r_[True, np.diff(H) > tolH]
    Hs = H[keep]
    logSs = np.log(np.maximum(source_I[keep], 1e-300))
    logS_of_H = PchipInterpolator(Hs, logSs)
    return {
        "z": z, "N": N, "C": C, "L": L, "rho_rel": rho_rel,
        "g": g, "source_I": source_I, "H": H, "H_total": float(Hs[-1]),
        "logS_of_H": logS_of_H, "g_horizon_cutoff": float(g[-1]),
        "source_horizon_cutoff": float(source_I[-1]),
    }


def emergent_intensity(profile: dict, lam: float) -> float:
    """Formal grey LTE solution at the shock, with no horizon-side incident beam.

    I_s/I_source,s = integral S(H) exp(-lambda H) lambda dH.
    y=lambda*H makes the opaque boundary layer numerically resolved.
    """
    Htot = float(profile["H_total"])
    ymax = lam * Htot
    if ymax <= 0:
        return 0.0
    upper = min(ymax, 50.0)  # omitted e^-y tail < 2e-22 and S<=1 on this branch
    p = profile["logS_of_H"]
    val, err = quad(lambda y: math.exp(float(p(y / lam)) - y), 0.0, upper,
                    epsabs=2e-11, epsrel=2e-9, limit=200)
    return max(0.0, min(1.0, val))


def doppler_temperature(N: float) -> float:
    """Forward emission from inward-moving exterior fluid toward the interior observer."""
    beta = 1.0 / math.sqrt(N)
    return math.sqrt((1.0 + beta) / (1.0 - beta))


def transfer_temperature(w: float, eta: float, lam: float, profile=None) -> tuple[float, float]:
    p = profile if profile is not None else tov_profile(w, eta)
    I = emergent_intensity(p, lam)
    return doppler_temperature(shock(eta)["N"]) * I ** 0.25, I


def geometric_factor() -> tuple[float, float]:
    h = 2e-5
    Rp = (rstar(ETA0 + h) - rstar(ETA0 - h)) / (2.0 * h)
    return Rp, CHI0 / (1.0 + Rp)


RPRIME, DETA_DXR = geometric_factor()


def dipole_for(w: float, lam: float, pminus=None, pplus=None) -> tuple[float, float, float]:
    # d ln Q/d eta, then eta shift = mu*x/(1+rstar') and x=(x/R0)*R0.
    h = 2e-5
    qm, _ = transfer_temperature(w, ETA0 - h, lam, pminus)
    qp, _ = transfer_temperature(w, ETA0 + h, lam, pplus)
    q0, I0 = transfer_temperature(w, ETA0, lam)
    dlnq = (math.log(qp) - math.log(qm)) / (2.0 * h)
    a1 = DETA_DXR * dlnq
    bound_frac = math.inf if abs(a1) < 1e-15 else DELTA_LIMIT / abs(a1)
    return a1, bound_frac, q0


def opaque_dipole() -> tuple[float, float]:
    h = 2e-5
    dm = doppler_temperature(shock(ETA0 - h)["N"])
    dp = doppler_temperature(shock(ETA0 + h)["N"])
    a1 = DETA_DXR * (math.log(dp) - math.log(dm)) / (2.0 * h)
    return a1, DELTA_LIMIT / abs(a1)


def write_csv(path: Path, fieldnames, rows):
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader(); w.writerows(rows)


def main():
    opaque_a1, opaque_bound = opaque_dipole()
    surface = []
    sweep = []
    selected_lams = [1e-4, 1e-2, 1.0, 1e2, 1e4]
    horizon_diags = []

    for wi, w in enumerate(W_GRID):
        h = 2e-5
        pm = tov_profile(float(w), ETA0 - h)
        p0 = tov_profile(float(w), ETA0)
        pp = tov_profile(float(w), ETA0 + h)
        horizon_diags.append({
            "w": float(w), "H_total": p0["H_total"],
            "g_horizon_cutoff": p0["g_horizon_cutoff"],
            "source_horizon_cutoff": p0["source_horizon_cutoff"],
        })
        local = []
        for lam in LAMBDA_GRID:
            Im = emergent_intensity(pm, float(lam)); I0 = emergent_intensity(p0, float(lam)); Ip = emergent_intensity(pp, float(lam))
            qm = doppler_temperature(shock(ETA0-h)["N"]) * Im**0.25
            q0 = doppler_temperature(S0["N"]) * I0**0.25
            qp = doppler_temperature(shock(ETA0+h)["N"]) * Ip**0.25
            a1 = DETA_DXR * (math.log(qp)-math.log(qm))/(2*h)
            bound = DELTA_LIMIT/abs(a1) if abs(a1)>1e-15 else math.inf
            row = {"w":float(w), "lambda":float(lam), "I_ext_over_I_shock":I0,
                   "T_cross_over_T_surrounding":q0, "dipole_a1_per_xoff_over_Rcross":a1,
                   "xoff_over_Rcross_bound":bound, "xoff_comoving_bound":bound*CHI0}
            surface.append(row); local.append(row)
        ext = max(local, key=lambda x: abs(x["dipole_a1_per_xoff_over_Rcross"]))
        by_lam = {min(local, key=lambda x:abs(math.log10(x["lambda"])-math.log10(L)))["lambda"]:
                  min(local, key=lambda x:abs(math.log10(x["lambda"])-math.log10(L))) for L in selected_lams}
        row = {"w":float(w), "H_total_unit_lambda":p0["H_total"],
               "max_abs_dipole_a1":ext["dipole_a1_per_xoff_over_Rcross"],
               "lambda_at_max_abs_dipole":ext["lambda"],
               "bound_at_max_abs_dipole_xoff_over_Rcross":ext["xoff_over_Rcross_bound"],
               "opaque_dipole_a1":opaque_a1, "opaque_bound_xoff_over_Rcross":opaque_bound}
        for L in selected_lams:
            x = min(local, key=lambda q:abs(math.log10(q["lambda"])-math.log10(L)))
            tag = f"lam_{L:g}"
            row[f"{tag}_dipole_a1"] = x["dipole_a1_per_xoff_over_Rcross"]
            row[f"{tag}_bound_xoff_over_Rcross"] = x["xoff_over_Rcross_bound"]
            row[f"{tag}_Tcross_over_Tsky"] = x["T_cross_over_T_surrounding"]
        sweep.append(row)

    write_csv(HERE/"p6_opacity_surface.csv", list(surface[0]), surface)
    write_csv(HERE/"p6_w_sweep.csv", list(sweep[0]), sweep)

    # Direct nonlinear angular check at one small offset: geometry only, using a local eta interpolant.
    wcheck = S0["junction_w"]
    lamcheck = 1.0
    eps = 1e-4
    mus = np.linspace(-1,1,41)
    etas = np.linspace(ETA0-4e-4, ETA0+4e-4, 17)
    Qs = np.array([transfer_temperature(wcheck,float(e),lamcheck)[0] for e in etas])
    qinterp = PchipInterpolator(etas, np.log(Qs))
    Ts=[]
    x=eps*CHI0
    for mu in mus:
        def fchi(chi):
            return math.sqrt(x*x+chi*chi+2*x*chi*mu)-rstar(ETA_OBS-chi)
        chi=brentq(fchi,CHI0-0.02,CHI0+0.02)
        Ts.append(math.exp(float(qinterp(ETA_OBS-chi))))
    Ts=np.asarray(Ts); norm=0.5*np.trapezoid(Ts,mus); y=Ts/norm-1
    a1_fit=1.5*np.trapezoid(y*mus,mus)/eps
    a1_deriv=min(surface,key=lambda r:abs(r["w"]-wcheck)+abs(math.log10(r["lambda"]))) ["dipole_a1_per_xoff_over_Rcross"]

    summary = {
        "blind_input": str(INPUT), "input_sha256": sha256(INPUT), "input_rows": len(ROWS),
        "eta_observer":ETA_OBS, "eta_cross_center":ETA0, "chi_cross_center_Rnorm":CHI0,
        "shock_center":S0, "rstar_prime_center":RPRIME, "deta_d_xoff_over_R":DETA_DXR,
        "dipole_fraction_limit":DELTA_LIMIT,
        "opaque_dipole_a1":opaque_a1, "opaque_xoff_over_R_bound":opaque_bound,
        "opaque_xoff_comoving_bound":opaque_bound*CHI0,
        "w_grid_count":len(W_GRID), "lambda_grid_count":len(LAMBDA_GRID),
        "temperature_min_surface":min(x["T_cross_over_T_surrounding"] for x in surface),
        "temperature_max_surface":max(x["T_cross_over_T_surrounding"] for x in surface),
        "global_max_abs_dipole_row":max(surface,key=lambda x:abs(x["dipole_a1_per_xoff_over_Rcross"])),
        "angular_nonlinear_check":{"w":wcheck,"lambda":lamcheck,"epsilon_x_over_R":eps,
                                   "a1_fit":a1_fit,"a1_derivative_nearest_grid":a1_deriv,
                                   "relative_difference":abs(a1_fit-a1_deriv)/abs(a1_deriv)},
        "horizon_diagnostics":{"min_H_total":min(x["H_total"] for x in horizon_diags),
                               "max_H_total":max(x["H_total"] for x in horizon_diags),
                               "max_g_at_cutoff":max(x["g_horizon_cutoff"] for x in horizon_diags),
                               "max_source_at_cutoff":max(x["source_horizon_cutoff"] for x in horizon_diags)},
    }
    (HERE/"p6_summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    (HERE/"horizon_diagnostics.json").write_text(json.dumps(horizon_diags,indent=2)+"\n")

    # Optional diagnostic plot; CSV/JSON are the authoritative products.
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        plt = None
    if plt is not None:
        fig,axs=plt.subplots(2,1,figsize=(9,9),sharex=True)
        for L in selected_lams:
            rr=[min((x for x in surface if x["w"]==w),key=lambda q:abs(math.log10(q["lambda"])-math.log10(L))) for w in W_GRID]
            axs[0].plot(W_GRID,[x["dipole_a1_per_xoff_over_Rcross"] for x in rr],label=f"lambda={L:g}")
            axs[1].semilogy(W_GRID,[x["xoff_over_Rcross_bound"] for x in rr],label=f"lambda={L:g}")
        axs[0].axhline(opaque_a1,color='k',ls='--',label='opaque limit')
        axs[1].axhline(opaque_bound,color='k',ls='--',label='opaque limit')
        axs[0].set_ylabel('dipole a1 per x_off/R_cross'); axs[1].set_ylabel('bound on x_off/R_cross')
        axs[1].set_xlabel('closure w'); axs[0].legend(ncol=3,fontsize=8); axs[0].grid(alpha=.3);axs[1].grid(alpha=.3)
        fig.tight_layout();fig.savefig(HERE/"p6_w_sweep.png",dpi=170);plt.close(fig)
    print(json.dumps(summary,indent=2))


if __name__ == "__main__":
    main()
