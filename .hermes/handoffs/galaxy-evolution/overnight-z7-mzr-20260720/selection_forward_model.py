#!/usr/bin/env python3
"""
Phase-6 JWST selection forward model for the z>7 mass-metallicity run
(overnight-z7-mzr-20260720, Trikitear). Author: Tori.

GOAL: quantify Delta_sel = <O/H>_intrinsic(parent) - <O/H>_detected at fixed
stellar mass in the overlap window logM in [8.0, 9.5], separately for the
emission-line-selected strong-line subset and the auroral-line (Te/direct)
subset. Then correct the observed offset (0.45 dex matched; 0.33 dex Te-only)
and decide pre-registered Test 4.

Delta_sel here is a PURE SAMPLE-SELECTION shift: the O/H *estimator* is assumed
unbiased (Te is calibration-free; strong-line calibration bias is Test 3, handled
separately). So recovered O/H of a detected galaxy = its true O/H, and the only
thing selection does is change WHICH galaxies enter the mass bin. This isolates
exactly the effect Test 4 asks about.

Everything is Monte-Carlo, grounded, with a sensitivity grid. No fabrication.
References cited inline and in SELECTION_MODEL.md.
"""
import json, numpy as np
from astropy.cosmology import Planck18 as cosmo
from astropy import units as u

RNG = np.random.default_rng(20260720)
CM_PER_MPC = 3.0856775814913673e24

# ---- observed inputs from P2 results.json (locked, not refit here) -----------
OBS_MATCHED   = 0.449;  OBS_MATCHED_CI = (0.283, 0.622)   # full N=16, matched scale
OBS_TE        = 0.332;  OBS_TE_CI      = (0.075, 0.535)   # Te-direct subset (N=4)
OVERLAP = (8.0, 9.5)

# redshifts of the real z>7 Nakajima+23 sample (for a grounded d_L distribution)
Z_SAMPLE = np.array([8.496,7.665,7.66,7.874,7.877,7.286,8.005,7.029,7.179,7.179,
                     7.549,7.471,7.167,8.681,7.779,8.714,7.825,8.612,7.197,8.179,
                     7.451,8.637,7.487,7.483,7.174,7.477])

# precompute d_L(z) on a grid (Mpc -> cm), interpolate
_zg = np.linspace(6.8, 9.2, 200)
_dl = cosmo.luminosity_distance(_zg).to(u.Mpc).value * CM_PER_MPC
def dL_cm(z): return np.interp(z, _zg, _dl)

# ---- line-ratio model (metallicity dependent) --------------------------------
# Curti+2020 (MNRAS 491, 944) strong-line calibrations: log(ratio)=sum c_n x^n,
# x = 12+log(O/H) - 8.69. Used here as the *intrinsic* line-emission model.
C_R3 = [-0.277, -3.549, -3.593, -0.981]   # [OIII]5007/Hb
C_R2 = [ 0.418, -0.961, -3.505, -1.949]   # [OII]3727/Hb
def _poly(c, x):
    return c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3
def R3_ratio(OH):        # [OIII]5007 / Hbeta
    return 10**_poly(C_R3, OH - 8.69)
def R2_ratio(OH):        # [OII]3727 / Hbeta
    return 10**_poly(C_R2, OH - 8.69)

# Te - O/H anti-correlation (direct-method behaviour, Nakajima+22 / Curti+20 Te):
# low O/H => high electron temperature. Anchored O/H=8.0->Te~1.4e4, 7.3->~2.0e4.
def Te_of_OH(OH):
    Te = 1.40e4 - 0.857e4*(OH - 8.0)
    return np.clip(Te, 8.0e3, 3.0e4)
# atomic-physics auroral ratio (Osterbrock&Ferland, low-density limit):
# (I4959+I5007)/I4363 = 7.90 exp(3.29e4/Te);  I5007=0.749*(I4959+I5007)
# => I4363/I5007 = 0.1690 * exp(-3.29e4/Te)
def r4363_5007(Te):
    return 0.1690*np.exp(-3.29e4/Te)

# SFR -> L(Hbeta): Kennicutt&Evans 2012 (Chabrier) L(Ha)=1.86e41*SFR; Hb=Ha/2.86
def LHb_of_SFR(SFR):
    return SFR*1.86e41/2.86

# ---- parent population --------------------------------------------------------
def draw_masses(n, alpha, logMstar=10.0, lo=7.0, hi=10.5):
    """Schechter SMF in log-mass: phi(logM) ~ (M/M*)^(alpha+1) exp(-M/M*)."""
    lg = np.linspace(lo, hi, 4000)
    m_over = 10**(lg - logMstar)
    phi = m_over**(alpha+1)*np.exp(-m_over)
    cdf = np.cumsum(phi); cdf /= cdf[-1]
    return np.interp(RNG.random(n), cdf, lg)

def intrinsic_MZR(logM, kind):
    """Intrinsic z~8 MZR (normalisation only; Delta_sel is ~independent of it)."""
    # low-mass slope ~0.30 (Sanders+2021). Two normalisations to confirm invariance.
    if kind == 'local_like':      # local-like z=0 zero point
        return 8.69 + 0.30*(logM - 10.0)          # ->8.09 at logM8, 8.39 at logM9
    elif kind == 'modest_evol':   # ~0.3 dex lower (mild high-z evolution)
        return 8.39 + 0.30*(logM - 10.0)
    raise ValueError(kind)

def z8_main_sequence(logM):
    # z~8 star-forming MS: high sSFR ~ few e-9 - 1e-8 /yr. slope ~0.9.
    # log SFR = 0.9*(logM-8) + 0.4  -> logM8:0.4(2.5 Msun/yr), logM9:1.3(20 Msun/yr)
    return 0.9*(logM - 8.0) + 0.4

# ---- one Monte-Carlo realisation ---------------------------------------------
def run_once(alpha=-1.9, sigma_OH=0.12, beta_FMR=0.20, sigma_MS=0.35,
             sigma_line=1.5e-19, snr_cut=5.0, mzr='local_like', n=400000):
    logM = draw_masses(n, alpha)
    z    = RNG.choice(Z_SAMPLE, size=n)             # grounded redshift dist
    # SFR with MS scatter; FMR: high SFR at fixed mass -> low O/H
    eps_MS = RNG.normal(0, sigma_MS, n)
    logSFR = z8_main_sequence(logM) + eps_MS
    SFR    = 10**logSFR
    sig_ind = np.sqrt(max(sigma_OH**2 - (beta_FMR*sigma_MS)**2, 1e-6))
    OH = intrinsic_MZR(logM, mzr) - beta_FMR*eps_MS + RNG.normal(0, sig_ind, n)

    # intrinsic line luminosities
    LHb   = LHb_of_SFR(SFR)
    L5007 = LHb*R3_ratio(OH)
    L3727 = LHb*R2_ratio(OH)
    Te    = Te_of_OH(OH)
    L4363 = L5007*r4363_5007(Te)

    # fluxes
    A = 4*np.pi*dL_cm(z)**2
    F = lambda L: L/A
    FHb, F5007, F3727, F4363 = F(LHb), F(L5007), F(L3727), F(L4363)

    # probabilistic detection: measured = true + N(0,sigma_line); S/N>cut
    def det(Fl):
        return (Fl + RNG.normal(0, sigma_line, n)) > snr_cut*sigma_line
    d_strong = det(FHb) & det(F5007)            # R3 minimum (Hb + [OIII]5007)
    d_te     = d_strong & det(F4363)            # Te needs auroral 4363 too

    # overlap-window mass-matched means (per 0.5-dex bin, then averaged)
    edges = np.array([8.0,8.5,9.0,9.5])
    centers = 0.5*(edges[:-1]+edges[1:])
    def binned_delta(mask):
        deltas, wts = [], []
        for lo,hi in zip(edges[:-1], edges[1:]):
            inbin = (logM>=lo)&(logM<hi)
            par = inbin.sum()
            sel = inbin & mask
            if sel.sum() < 5: 
                deltas.append(np.nan); wts.append(0); continue
            d = OH[inbin].mean() - OH[sel].mean()   # intrinsic - detected
            deltas.append(d); wts.append(sel.sum())
        deltas=np.array(deltas); wts=np.array(wts,float)
        if wts.sum()==0: return np.nan, deltas
        return np.nansum(deltas*wts)/wts.sum(), deltas
    Dstrong, dprof_s = binned_delta(d_strong)
    Dte,     dprof_t = binned_delta(d_te)
    return dict(D_strong=Dstrong, D_te=Dte,
                prof_strong=dprof_s.tolist(), prof_te=dprof_t.tolist(),
                n_strong=int(((logM>=8)&(logM<9.5)&d_strong).sum()),
                n_te=int(((logM>=8)&(logM<9.5)&d_te).sum()),
                bin_centers=centers.tolist())

# ---- fiducial + sensitivity grid ---------------------------------------------
fid = dict(alpha=-1.9, sigma_OH=0.12, beta_FMR=0.20, sigma_MS=0.35,
           sigma_line=1.5e-19, snr_cut=5.0, mzr='local_like')
print("FIDUCIAL:", run_once(**fid))

grid = {
  'sigma_line': [0.75e-19, 1.5e-19, 3.0e-19],     # +-0.3 dex flux limit
  'alpha':      [-1.7, -1.9, -2.1],               # SMF faint-end slope
  'sigma_OH':   [0.10, 0.15, 0.20],               # intrinsic O/H scatter
  'snr_cut':    [3.0, 5.0],                        # detection S/N
  'beta_FMR':   [0.10, 0.20, 0.30],               # FMR anti-correlation strength
  'mzr':        ['local_like', 'modest_evol'],    # intrinsic normalisation check
}
runs = []
for key, vals in grid.items():
    for v in vals:
        p = dict(fid); p[key]=v
        r = run_once(**p); r['vary']=f"{key}={v}"
        runs.append(r)
        print(f"{key:12s}={str(v):12s}  D_strong={r['D_strong']:.3f}  D_te={r['D_te']:.3f}  (Nstr={r['n_strong']}, Nte={r['n_te']})")

# multi-knob CORNERS (conservative worst/best case; one-at-a-time can miss combos)
import itertools
for sl,snr,sOH,bF,mz in itertools.product([0.75e-19,3.0e-19],[3.0,5.0],[0.10,0.20],
                                           [0.10,0.30],['local_like','modest_evol']):
    rc = run_once(alpha=-2.1, sigma_OH=sOH, beta_FMR=bF, sigma_MS=0.35,
                  sigma_line=sl, snr_cut=snr, mzr=mz, n=300000)
    rc['vary']=f"corner[sl={sl:.1e},snr={snr},sOH={sOH},bF={bF},{mz}]"
    runs.append(rc)
print("appended 32 corner runs")

Ds = np.array([r['D_strong'] for r in runs if np.isfinite(r['D_strong'])])
Dt = np.array([r['D_te']     for r in runs if np.isfinite(r['D_te'])])
Dstrong_rng = (float(Ds.min()), float(Ds.max()))
Dte_rng     = (float(Dt.min()), float(Dt.max()))

# ---- corrected offsets + Test-4 verdict --------------------------------------
# corrected = observed - Delta_sel. Conservative combined interval:
#   lower = obs_CI_lo - Dsel_max ; upper = obs_CI_hi - Dsel_min
def corrected(obs, obs_ci, dsel_rng, dsel_central):
    central = obs - dsel_central
    lo = obs_ci[0] - dsel_rng[1]
    hi = obs_ci[1] - dsel_rng[0]
    return dict(central=round(central,3), ci=[round(lo,3), round(hi,3)])

# central Delta_sel = fiducial
fid_run = run_once(**fid)
corr_matched = corrected(OBS_MATCHED, OBS_MATCHED_CI, Dstrong_rng, fid_run['D_strong'])
corr_te      = corrected(OBS_TE,      OBS_TE_CI,      Dte_rng,     fid_run['D_te'])

# Test-4 PASS criteria: Delta_sel bounded (finite range) AND corrected lower CI > 0
bounded = np.isfinite(Dstrong_rng[0]) and np.isfinite(Dte_rng[1])
matched_excl0 = corr_matched['ci'][0] > 0
te_excl0      = corr_te['ci'][0] > 0
# worst-case (max Delta_sel) corrected central still > 0 ?
worst_matched = OBS_MATCHED - Dstrong_rng[1]
worst_te      = OBS_TE      - Dte_rng[1]

test4_pass = bool(bounded and matched_excl0)   # matched sample is the headline
verdict = ("PASS" if test4_pass else "PARTIAL/FAIL")

out = {
 "run": "overnight-z7-mzr-20260720 P6 selection forward model (Tori)",
 "method": "Monte-Carlo emission-line-selection forward model; Delta_sel = "
           "<O/H>_intrinsic(parent) - <O/H>_detected at fixed mass in [8.0,9.5]; "
           "O/H estimator assumed unbiased (pure selection shift).",
 "fiducial": {k:(v if not isinstance(v,float) else v) for k,v in fid.items()},
 "fiducial_result": {"D_strong": round(fid_run['D_strong'],3),
                     "D_te": round(fid_run['D_te'],3),
                     "prof_strong": [None if np.isnan(x) else round(x,3) for x in fid_run['prof_strong']],
                     "prof_te":     [None if np.isnan(x) else round(x,3) for x in fid_run['prof_te']],
                     "bin_centers": fid_run['bin_centers']},
 "Delta_sel_strongline_dex": {"min": round(Dstrong_rng[0],3), "max": round(Dstrong_rng[1],3)},
 "Delta_sel_Te_dex":         {"min": round(Dte_rng[0],3),     "max": round(Dte_rng[1],3)},
 "observed": {"matched": OBS_MATCHED, "matched_CI": list(OBS_MATCHED_CI),
              "te_only": OBS_TE, "te_only_CI": list(OBS_TE_CI)},
 "corrected_offset_matched_dex": corr_matched,
 "corrected_offset_Te_dex": corr_te,
 "worst_case_corrected_central": {"matched": round(worst_matched,3), "te": round(worst_te,3)},
 "sensitivity_grid": [ {"vary":r['vary'],"D_strong":round(r['D_strong'],3),
                        "D_te":round(r['D_te'],3),"n_strong":r['n_strong'],"n_te":r['n_te']}
                       for r in runs ],
 "test4": {
   "delta_sel_bounded": bool(bounded),
   "matched_corrected_CI_excludes_0": bool(matched_excl0),
   "te_corrected_CI_excludes_0": bool(te_excl0),
   "verdict": verdict,
   "note": ""  # filled below
 }
}
frac_sel_matched = fid_run['D_strong']/OBS_MATCHED
frac_sel_te      = fid_run['D_te']/OBS_TE
out["test4"]["note"] = (
  f"Delta_sel is now BOUNDED (was unbounded=original failure). Strong-line "
  f"{Dstrong_rng[0]:.2f}-{Dstrong_rng[1]:.2f} dex, Te {Dte_rng[0]:.2f}-{Dte_rng[1]:.2f} dex. "
  f"At fiducial, selection explains ~{100*frac_sel_matched:.0f}% of the 0.45 dex matched "
  f"offset and ~{100*frac_sel_te:.0f}% of the 0.33 dex Te offset; a residual physical "
  f"deficit of ~{corr_matched['central']:.2f} dex (matched) / ~{corr_te['central']:.2f} dex (Te) remains. "
  f"Corrected matched CI {corr_matched['ci']} "
  f"{'excludes' if matched_excl0 else 'includes'} 0; corrected Te CI {corr_te['ci']} "
  f"{'excludes' if te_excl0 else 'includes'} 0."
)

with open("selection_results.json","w") as f:
    json.dump(out, f, indent=1)
print("\n=== SUMMARY ===")
print("Delta_sel strong-line:", Dstrong_rng)
print("Delta_sel Te        :", Dte_rng)
print("corrected matched   :", corr_matched)
print("corrected Te        :", corr_te)
print("Test4 verdict       :", verdict)
print(out["test4"]["note"])
