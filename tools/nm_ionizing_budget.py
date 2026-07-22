#!/usr/bin/env python3
"""Reionization ionizing-photon-budget study for the NebulaMind Lab runner.

Solves for the Lyman-continuum escape fraction *required* of star-forming
galaxies to close the reionization ionizing budget, and confronts it with the
*indirect-proxy-inferred* f_esc. No survey pull — all inputs are fixed,
literature-anchored values (cited inline). The contribution is not a new f_esc
measurement but a systematics reconciliation: how much of any apparent
photon-budget shortfall survives once the dominant systematics
(xi_ion x clumping x proxy-calibration) are propagated, and whether a shortfall
is robust to swapping the O32 calibration for the beta-slope calibration
(the non-circularity test).

Standard reionization-maintenance formalism: Madau, Haardt & Rees (1999);
Robertson et al. (2013, 2015). SFRD: Madau & Dickinson (2014). xi_ion:
Simmonds et al. (2024), Bouwens et al. (2016). f_esc proxy calibrations:
Chisholm et al. (2022), Flury et al. (2022) (LzLCS). All values are
representative anchors from those works; exact numbers are refetched/cited by
the runner's ADS/arXiv grounding layer for the manuscript.
"""
from __future__ import annotations
import numpy as np

# ---- cosmology / atomic constants ----
_H = 0.6774
_CM_PER_MPC = 3.0857e24
_MHZ_MPC3 = _CM_PER_MPC ** 3                 # cm^3 per comoving Mpc^3
_MH_G = 1.6726e-24                            # hydrogen mass [g]
_RHO_CRIT0 = 1.878e-29 * _H * _H             # rho_crit,0 = 1.878e-29 h^2 [g/cm^3]
_OMEGA_B = 0.0486                             # Planck 2018
_XH, _YHE = 0.76, 0.24                        # H, He mass fractions
_NH_COMOV = _XH * _OMEGA_B * _RHO_CRIT0 / _MH_G   # comoving mean n_H [cm^-3] ~1.9e-7
_ALPHA_B = 2.6e-13                            # case-B recomb. coeff, T=2e4 K [cm^3/s] (Osterbrock)
_KAPPA_UV = 1.15e-28                          # SFR -> L_UV [Msun/yr per erg/s/Hz] (Madau & Dickinson 2014)


def sfrd_md14(z):
    """Madau & Dickinson (2014) cosmic SFRD fit [Msun/yr/cMpc^3]."""
    z = np.asarray(z, float)
    return 0.015 * (1 + z) ** 2.7 / (1.0 + ((1 + z) / 2.9) ** 5.6)


def nion_crit(z, C):
    """Comoving critical ionizing emissivity to balance recombinations
    (maintenance criterion ndot = <n_H>/t_rec), in photons s^-1 cMpc^-3.
    t_rec = 1/(C alpha_B n_H(z) (1 + Y/4X)); Robertson et al. (2015)."""
    z = np.asarray(z, float)
    corr = 1.0 + _YHE / (4 * _XH)
    ndot_cm = C * _ALPHA_B * _NH_COMOV ** 2 * (1 + z) ** 3 * corr   # s^-1 cm^-3 (comoving)
    return ndot_cm * _MHZ_MPC3                                       # s^-1 cMpc^-3


def fesc_required(z, log_xi, C, sfrd_boost=1.0):
    """f_esc required to close the budget = ndot_crit / (xi_ion * rho_UV),
    rho_UV = SFRD*boost / kappa_UV."""
    rho_uv = sfrd_md14(z) * sfrd_boost / _KAPPA_UV                   # erg/s/Hz per cMpc^3
    return nion_crit(z, C) / (10 ** log_xi * rho_uv)


# ---- indirect-proxy-inferred f_esc for typical z>6 star-forming galaxies ----
# Representative population values from LzLCS calibrations applied to typical
# high-z galaxy properties (Chisholm et al. 2022; Flury et al. 2022). Large
# intrinsic scatter is the point — these are *indirect* proxies with low-z
# calibrations of uncertain transportability to z>6.
_PROXY = {
    # name : (median f_esc, lognormal sigma in dex)
    "O32":  (0.08, 0.45),   # O32-ratio calibration (Chisholm+22), typical z>6 O32 ~ 5-10
    "beta": (0.05, 0.40),   # UV-slope beta calibration (Chisholm+22), typical beta ~ -2.3
}


def _sample_proxy(rng, proxy, n):
    med, sig = _PROXY[proxy]
    return np.clip(med * 10 ** (rng.normal(0.0, sig, n)), 1e-4, 1.0)


def run_ionizing_budget(rec, res, plt, z0=6.0):
    """Compute the study, plot onto the supplied matplotlib `plt`, populate
    `res` (summary/figure_url set by the caller), and return True.

    Monte-Carlo propagates the dominant systematics:
      log xi_ion ~ N(25.5, 0.15)   [Simmonds+24 / Bouwens+16 spread]
      clumping C ~ U(2, 5)         [IGM clumping uncertainty]
      SFRD boost ~ lognormal(mu=0, 0.2 dex) with a JWST high-z tail (up to ~2.5x)
      proxy in {O32, beta}, each with its lognormal scatter
    Non-circularity: compare median Delta(required-inferred) under O32-only vs
    beta-only calibration; a sign flip => the shortfall is calibration-driven.
    """
    spec = rec.get("spec", {}) if isinstance(rec, dict) else {}
    xi_c = float(spec.get("xi_center", 25.5))
    C_lo, C_hi = [float(v) for v in spec.get("clumping", [2.0, 5.0])]
    proxy = str(spec.get("proxy", "both")).lower()
    boost_mode = str(spec.get("sfrd_boost_mode", "jwst")).lower()
    corner = str(spec.get("corner", "fiducial"))

    def _boost(rn, n):
        if boost_mode == "high":     # optimistic JWST-enhanced SFRD
            return 10 ** rn.normal(0.1, 0.2, n) * (1.0 + rn.uniform(0.5, 2.0, n))
        if boost_mode == "none":     # conservative, no high-z enhancement
            return 10 ** rn.normal(0.0, 0.2, n)
        return 10 ** rn.normal(0.0, 0.2, n) * (1.0 + rn.uniform(0.0, 1.5, n) * (rn.random(n) < 0.5))

    rng = np.random.default_rng(20260723)
    N = 40000
    log_xi = rng.normal(xi_c, 0.15, N)
    C = rng.uniform(C_lo, C_hi, N)
    boost = _boost(rng, N)

    f_req = fesc_required(z0, log_xi, C, boost)
    f_req = np.clip(f_req, 1e-4, 5.0)

    # proxy-inferred f_esc (corner selects which LzLCS calibration)
    if proxy == "o32":
        f_inf = _sample_proxy(rng, "O32", N)
    elif proxy == "beta":
        f_inf = _sample_proxy(rng, "beta", N)
    else:
        use_o32 = rng.random(N) < 0.5
        f_inf = np.where(use_o32, _sample_proxy(rng, "O32", N), _sample_proxy(rng, "beta", N))

    delta = f_req - f_inf                       # >0 => shortfall (galaxies need more escape than inferred)
    frac_short = float(np.mean(delta > 0))
    q = lambda a, p: float(np.percentile(a, p))

    # non-circularity: median Delta under each calibration alone
    d_o32 = float(np.median(f_req - _sample_proxy(rng, "O32", N)))
    d_beta = float(np.median(f_req - _sample_proxy(rng, "beta", N)))
    robust = (np.sign(d_o32) == np.sign(d_beta)) and (np.sign(np.median(delta)) == np.sign(d_o32))
    flip = "holds under both O32 and beta calibrations" if robust else \
           "flips sign between the O32 and beta calibrations (calibration-driven, not robust)"

    req_med, req_lo, req_hi = q(f_req, 50), q(f_req, 16), q(f_req, 84)
    inf_med, inf_lo, inf_hi = q(f_inf, 50), q(f_inf, 16), q(f_inf, 84)
    d_med, d_lo, d_hi = q(delta, 50), q(delta, 16), q(delta, 84)
    closes = d_med <= 0 or (d_lo <= 0 <= d_hi)

    # ---- figure: required vs inferred f_esc(z) with systematic bands ----
    zz = np.linspace(5.0, 9.0, 40)
    # required band across the xi_ion x C x boost systematic (per-z percentiles)
    M = 4000
    lx = rng.normal(xi_c, 0.15, M); cc = rng.uniform(C_lo, C_hi, M); bb = _boost(rng, M)
    band = np.array([fesc_required(z, lx, cc, bb) for z in zz])       # (nz, M)
    r16, r50, r84 = (np.percentile(band, p, axis=1) for p in (16, 50, 84))
    plt.fill_between(zz, r16, r84, color="#c0392b", alpha=0.20, label="required (xi x C x SFRD syst.)")
    plt.plot(zz, r50, "-", color="#c0392b", lw=2.0, label="required f$_{esc}$ (median)")
    plt.axhspan(inf_lo, inf_hi, color="#2471a3", alpha=0.16, label="proxy-inferred (LzLCS O32/beta)")
    plt.axhline(inf_med, ls="--", color="#2471a3", lw=1.6)
    plt.ylim(0, min(0.6, max(0.3, r84.max() * 1.1)))
    plt.xlabel("redshift $z$"); plt.ylabel("LyC escape fraction $f_{esc}$")
    plt.title("Reionization ionizing-photon budget: required vs. inferred $f_{esc}$", fontsize=9.5)
    plt.legend(fontsize=8, loc="upper left")

    verdict = "the budget CLOSES within the systematic" if closes else "a genuine SHORTFALL remains"
    res["summary"] = (
        f"Reionization ionizing-photon-budget reconciliation at z~{z0:.0f}: star-forming galaxies "
        f"require f_esc={req_med:.3f} (+{req_hi-req_med:.3f}/-{req_med-req_lo:.3f}) to close the budget "
        f"(Madau-Dickinson SFRD, log xi_ion=25.5+/-0.15, clumping C=2-5, JWST-SFRD tail), versus "
        f"indirect-proxy-inferred f_esc={inf_med:.3f} (+{inf_hi-inf_med:.3f}/-{inf_med-inf_lo:.3f}) "
        f"from LzLCS O32/beta calibrations. Median delta(required-inferred)={d_med:+.3f} dex-frac "
        f"(16-84%: {d_lo:+.3f} to {d_hi:+.3f}); {frac_short*100:.0f}% of the systematic MC shows a "
        f"shortfall. Conclusion: {verdict}, and the sign {flip}. The result is bounded by the "
        f"xi_ion x clumping x proxy-calibration systematic, not by statistics."
    )
    res["fesc"] = {
        "z": z0, "f_required": [req_lo, req_med, req_hi], "f_inferred": [inf_lo, inf_med, inf_hi],
        "delta": [d_lo, d_med, d_hi], "frac_shortfall": frac_short,
        "noncircular_robust": bool(robust), "delta_O32": d_o32, "delta_beta": d_beta,
    }
    _ct = "" if corner == "fiducial" else f" ({corner} systematic corner)"
    res["title"] = (
        (f"The reionization ionizing-photon-budget shortfall for star-forming galaxies is not robust to systematics at z~{z0:.0f}"
         if closes else
         f"A residual reionization ionizing-photon-budget shortfall for star-forming galaxies at z~{z0:.0f}") + _ct
    )
    res["fesc"]["corner"] = corner
    # provenance guard: this is a literature-anchored calculation, NOT a survey-data study.
    res["provenance"] = (
        "Literature-anchored budget calculation — NO survey catalog data is used. The cosmic SFRD is the "
        "Madau & Dickinson (2014) analytic fitting function; xi_ion and the O32/beta f_esc proxy calibrations are "
        "adopted published values (LzLCS: Chisholm+22, Flury+22; Simmonds+24). Do NOT state or imply that this "
        "study uses JWST, SDSS, or TNG observational/catalog data — it is a systematics reconciliation over "
        "published literature values."
    )
    return True


if __name__ == "__main__":  # quick self-check
    class _P:
        def __getattr__(self, k): return lambda *a, **k: None
    r = {}
    run_ionizing_budget({"id": "selfcheck"}, r, _P())
    print(r["summary"])
    print(r["fesc"])
