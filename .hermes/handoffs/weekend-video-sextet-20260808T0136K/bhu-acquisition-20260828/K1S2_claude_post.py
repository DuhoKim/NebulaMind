#!/usr/bin/env python3
"""
K1S2_claude_post.py -- K1 stage-2 step 2 post-processing, seat "claude" (BLIND of the codex seat).

From the COMPAS HDF5 outputs written by K1S2_claude_driver.sh to
  Y_BH(cap) per box point, the finite-difference derivative dY_BH/dM_NS,max with its Monte-Carlo error,
  the controls C1-C4 of the frozen prereg (K1S2_POPSYN_PREREG_20260903.md section 5), and a PROVISIONAL
  outcome class in the prereg section-3 vocabulary.  Runs on partial output (only jobs with a DONE marker
  are read); the RESULT file is NOT written here.

Definitions (all declared here, none inferred later):
  * Y_BH = number of systems whose final Stellar_Type(1) or Stellar_Type(2) == 14, per unit star-forming
    mass (Msun^-1).  The star-forming mass represented by a run is the repo's own mass-evolved
    normalisation: compas_python_utils/cosmic_integration/totalMassEvolvedPerZ.py, function
    get_COMPAS_fraction(m1_low=5, m1_upp=150, m2_low=0.1, f_bin=0.7, a34=alpha3) -- the fraction of the
    universal (Kroupa 2001, 0.01-200 Msun, flat mass ratio, binary fraction 0.7 as in the repo's
    FastCosmicIntegration default --fbin) star-forming mass that lands inside COMPAS's sampled window.
    M_sf(run) = sum_i w_i (m1_i + m2_i) / fraction(alpha3).  (The count of black holes, N_BH, is reported too.)
  * IMF slope alpha3 in {1.6, 2.3, 3.0} is NOT rerun.  COMPAS samples the primary from Kroupa with
    alpha3 = 2.3 above 1 Msun (window 5-150 Msun); the slope corners are importance weights
        w_i = m1_i^-(alpha3 - 2.3)   for m1_i >= 1 Msun   (unity below, never sampled here),
    applied to every sum (numerator, star-forming mass, the universal fraction is recomputed with a34=alpha3).
    Secondary: COMPAS draws m2 = q m1 with q flat on [0.01, 1] (minimum 0.1 Msun); the pairing law is a
    conditional density p(m2 | m1) that does not depend on the IMF slope, so the joint density of (m1, m2)
    changes only through p(m1) and the primary-mass weight is exact.  The secondary's marginal mass function
    is implied by the pairing, not by the Kroupa slope -- the same convention the repo's normalisation
    (get_COMPAS_fraction) uses.
  * Derivative: central difference across the cap grid, (Y(3.50) - Y(1.97)) / 1.53, computed PER BATCH
    (the three batches share seeds across caps, so this is a paired difference); the Monte-Carlo error is
    the across-batch standard deviation / sqrt(n_batches).  Curvature: the three-point second difference
    on the unequal grid.  A sign is "resolved" when |mean| > k sigma_MC (k = 1 declared; k = 2 also shown).
  * C1: fiducial configuration (cap 2.50, DELAYED, Z = 0.02, default CE/kick) BBH merger rate at z = 0.2,
    Madau & Dickinson 2014 eq. 15 SFH (master row 4) in the repo's functional form
    (FastCosmicIntegration.find_sfr with a=0.015, b=2.7, c=2.9, d=5.6; ClassMSSFR.SFR_Madau), Planck18
    cosmology (astropy, as FastCosmicIntegration.set_cosmology default).  BBH selection mirrors
    ClassCOMPAS.setCOMPASDCOmask(types="BHBH", withinHubbleTime=True, pessimistic=True, noRLOFafterCEE=True).
    Declared settings: S1 = two-bin metallicity mixture (Z = 0.02 run for log-normal star formation above
    Z = 0.002, the Z = 0.0002 run below it; dP/dlogZ from FastCosmicIntegration.find_metallicity_distribution
    defaults, Neijssel+19); S2 = S1 times the Salpeter->Kroupa conversion of the MD14 SFRD (computed below as
    the ratio of star-forming mass per star above 8 Msun).  Descriptive only: the Z = 0.02 run alone.
    Must fall in 17.9-44 Gpc^-3 yr^-1 (prereg section 1).
  * C2: two-sided two-sample KS at alpha = 0.05 between the fiducial-cap synthetic near-birth NS masses and
    the 15 pinned Ozel & Freire masses (master row 5).  Near-birth cut: the supernova-record remnant mass
    Mass(SN) at the moment of NS formation (Stellar_Type(SN) == 13) -- by construction before any accretion --
    restricted to NSs whose binary survives the supernova bound (Unbound == 0), the analogue of the
    binary-pulsar sample.  The unrestricted (all NS births) sample is reported alongside.
  * C3: the same cap grid in --mode SSE (single stars, same seeds); the SSE yield is per unit universal
    star-forming mass with the single-star window fraction  int_5^150 m IMF dm / int_0.01^200 m IMF dm.
  * C4: the centre configuration with six batches; the derivative sign with 3 and with 6 batches.
"""
import argparse, glob, json, math, os, re, sys
import numpy as np
import h5py
from scipy import stats, integrate

LANE = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828"
REPO = os.path.join(LANE, "_tmp_k1s2_codex", "COMPAS")
CI_DIR = os.path.join(REPO, "compas_python_utils", "cosmic_integration")
sys.path.insert(0, CI_DIR)
import totalMassEvolvedPerZ as tmz          # repo file: get_COMPAS_fraction, IMF

CAPS = [1.97, 2.50, 3.50]
CAP_TAGS = ["1.97", "2.50", "3.50"]
ALPHA3 = [1.6, 2.3, 3.0]
ENGINES = ["DELAYED", "RAPID"]
ZS = ["0.02", "0.0002"]
CEKS = ["default", "alt"]
M1_MIN, M1_MAX, M2_MIN, FBIN = 5.0, 150.0, 0.1, 0.7
KROUPA = dict(m1=0.01, m2=0.08, m3=0.5, m4=200.0, a12=0.3, a23=1.3)
FID = ("DELAYED", "0.02", "default")           # centre / fiducial configuration
GWTC3_BBH = (17.9, 44.0)                        # Gpc^-3 yr^-1 at z = 0.2 (prereg section 1)
GWTC3_NSBH = (7.8, 140.0)                       # descriptive only
# master row 5 (K1S2_PIN_GATE_agy.md -> K1S2_claude_pins.md row 5), n = 15
OZEL_NS = [1.559, 1.174, 1.3381, 1.2489, 1.3330, 1.3455, 1.341, 1.230, 1.291, 1.322,
           1.4398, 1.3886, 1.358, 1.354, 1.27]
Z_SPLIT = 0.002                                 # geometric midpoint of the two run metallicities
Z_FIRST_SF = 10.0

# ----------------------------------------------------------------------------- IMF machinery
_frac_cache = {}
def frac_bse(a3):
    """Fraction of universal star-forming mass inside COMPAS's binary window (repo function)."""
    if ("bse", a3) not in _frac_cache:
        _frac_cache[("bse", a3)] = tmz.get_COMPAS_fraction(M1_MIN, M1_MAX, M2_MIN, f_bin=FBIN,
                                                           a34=a3, **KROUPA)
    return _frac_cache[("bse", a3)]

def frac_sse(a3):
    """Single-star window fraction: int_5^150 m IMF / int_0.01^200 m IMF (repo IMF, a34 = alpha3)."""
    if ("sse", a3) not in _frac_cache:
        f = lambda m: float(tmz.IMF(m, a34=a3, **KROUPA)) * m
        num = integrate.quad(f, M1_MIN, M1_MAX, limit=200)[0]
        den = (integrate.quad(f, 0.01, 0.08)[0] + integrate.quad(f, 0.08, 0.5)[0]
               + integrate.quad(f, 0.5, 200.0, limit=200)[0])
        _frac_cache[("sse", a3)] = num / den
    return _frac_cache[("sse", a3)]

def imf_weights(m1, a3):
    w = np.ones_like(m1, dtype=float)
    hi = m1 >= 1.0
    w[hi] = m1[hi] ** (-(a3 - 2.3))
    return w

def salpeter_to_kroupa_factor():
    """Star-forming mass per star above 8 Msun: Kroupa(0.01-200, a3=2.3) / Salpeter(0.1-100, 2.35)."""
    fK = lambda m: float(tmz.IMF(m, **KROUPA))
    MK = (integrate.quad(lambda m: m * fK(m), 0.01, 0.08)[0] + integrate.quad(lambda m: m * fK(m), 0.08, 0.5)[0]
          + integrate.quad(lambda m: m * fK(m), 0.5, 200.0, limit=200)[0])
    NK = integrate.quad(fK, 8.0, 200.0, limit=200)[0]
    MS = integrate.quad(lambda m: m * m ** -2.35, 0.1, 100.0)[0]
    NS = integrate.quad(lambda m: m ** -2.35, 8.0, 100.0)[0]
    return (MK / NK) / (MS / NS)

# ----------------------------------------------------------------------------- run discovery
def discover(runs_dir):
    """Return dict (mode, eng, Z, cek) -> cap_tag -> list of dict(batch, seed, dir, h5) for DONE jobs."""
    runs = {}
    pat = re.compile(r"^(BSE|SSE)_cap([0-9.]+)_(DELAYED|RAPID)_Z([0-9.]+)_(default|alt)$")
    for cfg in sorted(glob.glob(os.path.join(runs_dir, "*_cap*"))):
        m = pat.match(os.path.basename(cfg))
        if not m:
            continue
        mode, cap, eng, Z, cek = m.groups()
        for bdir in sorted(glob.glob(os.path.join(cfg, "b*_s*"))):
            mb = re.match(r"^b(\d+)_s(\d+)$", os.path.basename(bdir))
            if not mb or not os.path.isfile(os.path.join(bdir, "DONE")):
                continue
            h5 = os.path.join(bdir, "out", "COMPAS_Output.h5")
            if not os.path.isfile(h5):
                continue
            runs.setdefault((mode, eng, Z, cek), {}).setdefault(cap, []).append(
                dict(batch=int(mb.group(1)), seed=int(mb.group(2)), dir=bdir, h5=h5))
    return runs

# ----------------------------------------------------------------------------- per-run loaders
def load_bse(h5):
    with h5py.File(h5, "r") as f:
        sp = f["BSE_System_Parameters"]
        d = dict(m1=sp["Mass@ZAMS(1)"][()], m2=sp["Mass@ZAMS(2)"][()],
                 st1=sp["Stellar_Type(1)"][()], st2=sp["Stellar_Type(2)"][()],
                 err=sp["Error"][()], seed=sp["SEED"][()])
        sn = f["BSE_Supernovae"]
        d["sn"] = dict(mass=sn["Mass(SN)"][()], st=sn["Stellar_Type(SN)"][()], unbound=sn["Unbound"][()],
                       sntype=sn["SN_Type(SN)"][()], rlof=sn["Experienced_RLOF(SN)"][()],
                       seed=sn["SEED"][()])
        dco = f["BSE_Double_Compact_Objects"]
        d["dco"] = dict(st1=dco["Stellar_Type(1)"][()], st2=dco["Stellar_Type(2)"][()],
                        hub=dco["Merges_Hubble_Time"][()], t=dco["Time"][()], tc=dco["Coalescence_Time"][()],
                        seed=dco["SEED"][()])
        if "BSE_Common_Envelopes" in f:
            ce = f["BSE_Common_Envelopes"]
            d["ce"] = dict(seed=ce["SEED"][()], rlof=ce["Immediate_RLOF>CE"][()], opt=ce["Optimistic_CE"][()])
        else:
            d["ce"] = dict(seed=np.array([], int), rlof=np.array([], np.uint8), opt=np.array([], np.uint8))
    return d

def load_sse(h5):
    with h5py.File(h5, "r") as f:
        sp = f["SSE_System_Parameters"]
        return dict(m=sp["Mass@ZAMS"][()], st=sp["Stellar_Type"][()], err=sp["Error"][()])

def yields_bse(d):
    """Y_BH (systems with >=1 BH per Msun) and Y_nBH (BH count per Msun) for each alpha3; plus counts."""
    is_bh_sys = ((d["st1"] == 14) | (d["st2"] == 14)).astype(float)
    n_bh = ((d["st1"] == 14).astype(float) + (d["st2"] == 14).astype(float))
    out = dict(n=len(d["m1"]), n_err="codes:" + "/".join(map(str, np.unique(d["err"]))), n_bh_sys=int(is_bh_sys.sum()), n_bh=int(n_bh.sum()))
    for a3 in ALPHA3:
        w = imf_weights(d["m1"], a3)
        msf = (w * (d["m1"] + d["m2"])).sum() / frac_bse(a3)
        out[a3] = dict(Y=(w * is_bh_sys).sum() / msf, YnBH=(w * n_bh).sum() / msf, Msf=msf)
    return out

def yields_sse(d):
    is_bh = (d["st"] == 14).astype(float)
    out = dict(n=len(d["m"]), n_err="codes:" + "/".join(map(str, np.unique(d["err"]))), n_bh_sys=int(is_bh.sum()), n_bh=int(is_bh.sum()))
    for a3 in ALPHA3:
        w = imf_weights(d["m"], a3)
        msf = (w * d["m"]).sum() / frac_sse(a3)
        out[a3] = dict(Y=(w * is_bh).sum() / msf, YnBH=(w * is_bh).sum() / msf, Msf=msf)
    return out

# ----------------------------------------------------------------------------- derivative machinery
H1, H2 = CAPS[1] - CAPS[0], CAPS[2] - CAPS[1]
def fd(y1, y2, y3):
    """central slope, left slope, right slope, curvature on the unequal grid (1.97, 2.50, 3.50)."""
    return dict(d=(y3 - y1) / (H1 + H2), dl=(y2 - y1) / H1, dr=(y3 - y2) / H2,
                c=2.0 * (H1 * y3 - (H1 + H2) * y2 + H2 * y1) / (H1 * H2 * (H1 + H2)))

def mc(vals):
    v = np.asarray(vals, float)
    n = len(v)
    if n == 0:
        return dict(n=0, mean=float("nan"), sig=float("nan"))
    sig = float(v.std(ddof=1) / math.sqrt(n)) if n > 1 else float("nan")
    return dict(n=n, mean=float(v.mean()), sig=sig)

def FM(m):
    return f"{m['mean']:.4e}" if m['n'] else 'n/a'

def FS(m):
    return f"{m['sig']:.2e}" if np.isfinite(m['sig']) else 'n/a'

def resolved(m, k):
    return (m["n"] >= 2) and np.isfinite(m["sig"]) and abs(m["mean"]) > k * m["sig"]

def sign_str(m, k):
    if m["n"] == 0:
        return "n/a"
    if not resolved(m, k):
        return "0 (unresolved)"
    return "-" if m["mean"] < 0 else "+"

def config_table(per_batch, batches_use=None):
    """per_batch: cap_tag -> {batch: yields dict}.  Returns per alpha3: Y per cap (mean, sig) and the
    paired finite differences across batches present at ALL three caps."""
    common = set.intersection(*[set(per_batch.get(c, {}).keys()) for c in CAP_TAGS]) if all(c in per_batch for c in CAP_TAGS) else set()
    if batches_use is not None:
        common &= set(batches_use)
    common = sorted(common)
    res = dict(batches=common, alpha3={})
    for a3 in ALPHA3:
        r = dict(Y={}, d=None)
        for c in CAP_TAGS:
            r["Y"][c] = mc([per_batch[c][b][a3]["Y"] for b in sorted(per_batch.get(c, {}))])
        fds = [fd(per_batch["1.97"][b][a3]["Y"], per_batch["2.50"][b][a3]["Y"], per_batch["3.50"][b][a3]["Y"]) for b in common]
        r["fd_per_batch"] = {b: f for b, f in zip(common, fds)}
        for key in ("d", "dl", "dr", "c"):
            r[key] = mc([f[key] for f in fds])
        res["alpha3"][a3] = r
    return res

# ----------------------------------------------------------------------------- C1 machinery
def md14_sfrd(z):
    """Madau & Dickinson 2014 eq. 15, Msun yr^-1 Mpc^-3 (repo: ClassMSSFR.SFR_Madau / find_sfr coefficients)."""
    z = np.asarray(z, float)
    return 0.015 * (1 + z) ** 2.7 / (1 + ((1 + z) / 2.9) ** 5.6)

def cosmo_tables():
    from astropy.cosmology import Planck18 as cosmo   # FastCosmicIntegration.set_cosmology default
    zgrid = np.linspace(0.0, Z_FIRST_SF, 4001)
    age = cosmo.age(zgrid).to("Myr").value            # decreasing in z
    return zgrid, age

def p_low_metallicity(zgrid):
    """Fraction of star formation at each z with Z < Z_SPLIT under the Neijssel+19 log-normal dP/dlnZ,
    transcribed from compas_python_utils/cosmic_integration/FastCosmicIntegration.py
    find_metallicity_distribution (L89-150; defaults mu0=0.035, muz=-0.23, sigma_0=0.39, sigma_z=0, alpha=0:
    mean Z = mu0 10^(muz z), mu = ln(mean/2 / (exp(sigma^2/2) Phi(0))) = ln(mean) - sigma^2/2).  Transcribed
    because that module guards against direct import unless the repo is pip-installed (its package __init__),
    and the checkout is not to be modified."""
    mu0, muz, sigma = 0.035, -0.23, 0.39
    mean = mu0 * 10 ** (muz * zgrid)
    mu = np.log(mean) - 0.5 * sigma ** 2
    return stats.norm.cdf((np.log(Z_SPLIT) - mu) / sigma), "Neijssel+19 log-normal, transcribed from FastCosmicIntegration.find_metallicity_distribution defaults"

def bbh_delay_times(d, types="BHBH"):
    """Delay times (Myr) of DCOs merging within a Hubble time, pessimistic CE, no immediate RLOF after CE
    (mirrors ClassCOMPAS.setCOMPASDCOmask).  Returns (delay_Myr, system-parameter row index)."""
    dco = d["dco"]
    if types == "BHBH":
        tm = (dco["st1"] == 14) & (dco["st2"] == 14)
    elif types == "BHNS":
        tm = ((dco["st1"] == 13) & (dco["st2"] == 14)) | ((dco["st1"] == 14) & (dco["st2"] == 13))
    else:
        tm = (dco["st1"] == 13) & (dco["st2"] == 13)
    hub = dco["hub"].astype(bool)
    ce = d["ce"]
    bad = np.unique(np.concatenate([ce["seed"][ce["rlof"].astype(bool)], ce["seed"][ce["opt"].astype(bool)]]))
    keep = tm & hub & ~np.isin(dco["seed"], bad)
    idx = np.searchsorted(d["seed"], dco["seed"][keep])
    return (dco["t"][keep] + dco["tc"][keep]), idx

def merger_rate_z(delays, weights, msf, z_m, zgrid, age, sf_weight_of_z=None):
    """R(z_m) = sum_i w_i SFRD(z_f,i) f(z_f,i) / M_sf  [Gpc^-3 yr^-1], t_f = t(z_m) - t_delay."""
    t_m = np.interp(z_m, zgrid, age)                 # age at merger redshift (Myr)
    t_f = t_m - delays
    ok = t_f > age[-1]                               # formed after z_first_SF
    z_f = np.interp(t_f[ok], age[::-1], zgrid[::-1])
    sf = md14_sfrd(z_f)
    if sf_weight_of_z is not None:
        sf = sf * np.interp(z_f, zgrid, sf_weight_of_z)
    return float((weights[ok] * sf).sum() / msf * 1e9)

# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default=os.path.join(LANE, "_tmp_k1s2_claude", "runs"))
    ap.add_argument("--out", default=os.path.join(LANE, "_tmp_k1s2_claude", "post"))
    ap.add_argument("--k", type=float, default=1.0, help="sigma multiple for a resolved sign (declared 1)")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    k = args.k
    lines = []
    P = lambda s="": (lines.append(s), print(s))

    P("# K1S2 claude post-processing (provisional; not the RESULT)")
    P(f"runs: {args.runs}")
    P(f"grid DONE marker present: {os.path.isfile(os.path.join(args.runs, 'DONE'))}")
    runs = discover(args.runs)
    n_jobs_done = sum(len(v) for cfg in runs.values() for v in cfg.values())
    P(f"jobs with DONE: {n_jobs_done}")
    P(f"binary-window fractions (repo get_COMPAS_fraction, f_bin={FBIN}): " + ", ".join(f"alpha3={a}: {frac_bse(a):.5f}" for a in ALPHA3))
    P(f"single-star window fractions: " + ", ".join(f"alpha3={a}: {frac_sse(a):.5f}" for a in ALPHA3))

    # ---- load everything once
    data = {}     # (mode,eng,Z,cek) -> cap -> batch -> yields
    raw_fid = {}  # cap -> batch -> loaded BSE dict for the fiducial config (C1, C2, channel diagnostics)
    raw_lowz = {}
    for key, caps in runs.items():
        mode = key[0]
        for cap, lst in caps.items():
            for r in lst:
                try:
                    if mode == "BSE":
                        d = load_bse(r["h5"])
                        y = yields_bse(d)
                        if key[1:] == FID:
                            raw_fid.setdefault(cap, {})[r["batch"]] = d
                        elif key[1:] == ("DELAYED", "0.0002", "default"):
                            raw_lowz.setdefault(cap, {})[r["batch"]] = d
                    else:
                        d = load_sse(r["h5"])
                        y = yields_sse(d)
                except Exception as e:
                    P(f"  ! could not read {r['h5']}: {e}")
                    continue
                y["seed"] = r["seed"]
                data.setdefault(key, {}).setdefault(cap, {})[r["batch"]] = y

    # ---- yield tables and derivatives, BSE box
    P()
    P("## Y_BH tables (BSE): systems with >=1 final BH per Msun of universal star-forming mass")
    P("config = engine / Z / CE+kick; per cap: mean over batches (MC error = std/sqrt(n)); derivative = paired central difference, per Msun per Msun")
    box = {}   # (a3, eng, Z, cek) -> fd summary
    for eng in ENGINES:
        for Z in ZS:
            for cek in CEKS:
                key = ("BSE", eng, Z, cek)
                pb = data.get(key, {})
                tab = config_table(pb, batches_use=[1, 2, 3])
                P()
                P(f"### BSE {eng} Z={Z} {cek}   batches complete at all caps: {tab['batches']}   "
                  + "counts: " + "; ".join(f"cap {c}: " + ",".join(f"b{b}:nBHsys={pb[c][b]['n_bh_sys']}/n={pb[c][b]['n']}(err={pb[c][b]['n_err']})" for b in sorted(pb[c])) for c in CAP_TAGS if c in pb))
                P("| alpha3 | Y(1.97) | Y(2.50) | Y(3.50) | dY/dcap (central) | sigma_MC | sign(k=%g) | sign(k=2) | left slope | right slope | curvature |" % k)
                P("|---|---|---|---|---|---|---|---|---|---|---|")
                for a3 in ALPHA3:
                    r = tab["alpha3"][a3]
                    box[(a3, eng, Z, cek)] = r
                    fmt = lambda m: (f"{m['mean']:.4e}" if m["n"] else "n/a")
                    P(f"| {a3} | {fmt(r['Y']['1.97'])} | {fmt(r['Y']['2.50'])} | {fmt(r['Y']['3.50'])} | {fmt(r['d'])} | "
                      f"{FS(r['d'])} | {sign_str(r['d'], k)} | {sign_str(r['d'], 2)} | "
                      f"{fmt(r['dl'])} ({sign_str(r['dl'], k)}) | {fmt(r['dr'])} ({sign_str(r['dr'], k)}) | {fmt(r['c'])} ({sign_str(r['c'], k)}) |")

    # ---- provisional class
    P()
    P("## Provisional class (prereg section 3 vocabulary; the RESULT dispatch decides)")
    pts = {kk: v for kk, v in box.items() if v["d"]["n"] >= 2}
    n_expected = len(ALPHA3) * len(ENGINES) * len(ZS) * len(CEKS)
    P(f"box points with >=2 paired batches: {len(pts)} / {n_expected}")
    verdict = "NO CLASS (grid incomplete)"
    if len(pts) == n_expected:
        signs = {kk: sign_str(v["d"], k) for kk, v in pts.items()}
        neg = [kk for kk, s in signs.items() if s == "-"]
        pos = [kk for kk, s in signs.items() if s == "+"]
        unr = [kk for kk, s in signs.items() if s.startswith("0")]
        is_max = all(sign_str(v["dl"], k) == "+" and sign_str(v["dr"], k) == "-" for v in pts.values())
        curv_neg = all(sign_str(v["c"], k) == "-" for v in pts.values())
        if is_max and curv_neg:
            verdict = "K1S2_MAX (left slope resolved +, right slope resolved -, curvature resolved < 0 at every box point)"
        elif len(neg) == n_expected:
            verdict = "K1S2_MONOTONE_DOWN (dY/dcap resolved < 0 at every box point); curvature signs: " + \
                      ", ".join(f"{kk}:{sign_str(v['c'], k)}" for kk, v in pts.items())
        elif len(pos) == n_expected:
            verdict = "K1S2_MONOTONE_UP (dY/dcap resolved > 0 at every box point) -> premise refuted for theta2"
        elif len(unr) == n_expected:
            verdict = "K1S2_STATIONARY_NOT_MAX candidate (derivative unresolved everywhere, no resolved negative curvature everywhere) -- or increase N (C4)"
        elif neg and pos:
            verdict = ("K1S2_SIGN_INVERTS candidate (resolved - at " + str(len(neg)) + " points, resolved + at " + str(len(pos)) +
                       ") -> INCONCLUSIVE on the sign; channel attribution below. + points: " + "; ".join(map(str, pos)))
        else:
            verdict = ("K1S2_UNIDENTIFIED / INCONCLUSIVE: sign resolved at " + str(len(neg) + len(pos)) +
                       " points, unresolved at " + str(len(unr)) + ": " + "; ".join(map(str, unr)))
    P(f"PROVISIONAL: {verdict}")

    # ---- channel diagnostic (fiducial config, supernova records)
    P()
    P("## Channel diagnostic (fiducial config, BSE_Supernovae): remnants formed with Mass(SN) <= 3.50 Msun, by cap")
    P("| cap | NS births | BH births (M<=3.5) | of which progenitor Experienced_RLOF | BH births total | NS births bound after SN |")
    P("|---|---|---|---|---|---|")
    for c in CAP_TAGS:
        if c not in raw_fid:
            continue
        ns = bh = bhr = bht = nsb = 0
        for b, d in raw_fid[c].items():
            sn = d["sn"]
            isns, isbh = sn["st"] == 13, sn["st"] == 14
            win = sn["mass"] <= 3.5
            ns += int(isns.sum()); nsb += int((isns & (sn["unbound"] == 0)).sum())
            bh += int((isbh & win).sum()); bhr += int((isbh & win & (sn["rlof"] != 0)).sum()); bht += int(isbh.sum())
        P(f"| {c} | {ns} | {bh} | {bhr} | {bht} | {nsb} |")
    P("Reading: the cap moves remnants between the NS and BH columns only at formation (Fryer 2012 mass vs cap); COMPAS's default has no NS accretion in CE "
      "and no NS->BH accretion-induced collapse, so a cap-sensitive BH count with Experienced_RLOF set is the mass-transfer channel, without it the effectively-single channel.")

    # ---- C1
    P()
    P("## C1 -- BBH merger rate at z = 0.2 (fiducial configuration cap 2.50), MD14 eq. 15 SFH, Planck18")
    c1 = dict(status="not computable yet")
    try:
        zgrid, age = cosmo_tables()
        plow, plow_src = p_low_metallicity(zgrid)
        fK = salpeter_to_kroupa_factor()
        P(f"Salpeter->Kroupa SFRD conversion factor (mass per star > 8 Msun; computed, not pinned): {fK:.4f}")
        P(f"low-metallicity (Z < {Z_SPLIT}) star-formation fraction from {plow_src}: z=0: {np.interp(0,zgrid,plow):.3f}, z=1: {np.interp(1,zgrid,plow):.3f}, z=3: {np.interp(3,zgrid,plow):.3f}")
        def pooled(raw, types, zw):
            num = 0.0; msf = 0.0; nsel = 0
            for b, d in raw.items():
                dl, idx = bbh_delay_times(d, types)
                w = imf_weights(d["m1"][idx], 2.3)
                m = (imf_weights(d["m1"], 2.3) * (d["m1"] + d["m2"])).sum() / frac_bse(2.3)
                num += merger_rate_z(dl, w, 1.0, 0.2, zgrid, age, zw) ; msf += m; nsel += len(dl)
            return (num / msf if msf > 0 else float("nan")), nsel
        if "2.50" in raw_fid:
            r_solar, n_solar = pooled(raw_fid["2.50"], "BHBH", None)
            r_hi, _ = pooled(raw_fid["2.50"], "BHBH", 1.0 - plow)
            P(f"fiducial Z=0.02 batches used: {sorted(raw_fid['2.50'])}, selected merging BBH: {n_solar}")
            P(f"descriptive (all star formation at Z=0.02): R_BBH(z=0.2) = {r_solar:.3f} Gpc^-3 yr^-1")
            if "2.50" in raw_lowz:
                r_lo, n_lo = pooled(raw_lowz["2.50"], "BHBH", plow)
                s1 = r_hi + r_lo
                s2 = s1 * fK
                P(f"Z=0.0002 batches used: {sorted(raw_lowz['2.50'])}, selected merging BBH: {n_lo}")
                P(f"S1 two-bin mixture: R_BBH(z=0.2) = {s1:.3f} Gpc^-3 yr^-1  (Z=0.02 part {r_hi:.3f} + Z=0.0002 part {r_lo:.3f})  -> {'PASS' if GWTC3_BBH[0] <= s1 <= GWTC3_BBH[1] else 'FAIL'} vs {GWTC3_BBH}")
                P(f"S2 = S1 x IMF conversion: R_BBH(z=0.2) = {s2:.3f} Gpc^-3 yr^-1  -> {'PASS' if GWTC3_BBH[0] <= s2 <= GWTC3_BBH[1] else 'FAIL'} vs {GWTC3_BBH}")
                nsbh_hi, _ = pooled(raw_fid["2.50"], "BHNS", 1.0 - plow); nsbh_lo, _ = pooled(raw_lowz["2.50"], "BHNS", plow)
                P(f"descriptive NSBH (S1): {nsbh_hi + nsbh_lo:.3f} Gpc^-3 yr^-1 (GWTC-3 {GWTC3_NSBH})")
                c1 = dict(status="computed", R_solar_only=r_solar, S1=s1, S2=s2, pass_S1=bool(GWTC3_BBH[0] <= s1 <= GWTC3_BBH[1]),
                          pass_S2=bool(GWTC3_BBH[0] <= s2 <= GWTC3_BBH[1]), NSBH_S1=nsbh_hi + nsbh_lo)
                P("C1 verdict: " + ("PASS (a declared setting lies in the GWTC-3 interval)" if (c1["pass_S1"] or c1["pass_S2"]) else "FAIL under both declared settings -> pipeline not calibrated; no class"))
            else:
                c1 = dict(status="awaiting Z=0.0002 DELAYED default cap-2.50 batches", R_solar_only=r_solar)
                P("S1/S2 need the Z=0.0002 DELAYED default cap-2.50 batches (not DONE yet)")
        else:
            P("fiducial cap-2.50 batches not DONE yet")
    except Exception as e:
        P(f"C1 error: {e}")
        c1 = dict(status=f"error: {e}")

    # ---- C2
    P()
    P("## C2 -- KS test, synthetic near-birth NS masses (fiducial, cap 2.50) vs the 15 pinned Ozel & Freire masses")
    c2 = dict(status="not computable yet")
    if "2.50" in raw_fid:
        allm, bound = [], []
        for b, d in raw_fid["2.50"].items():
            sn = d["sn"]; isns = sn["st"] == 13
            allm.append(sn["mass"][isns]); bound.append(sn["mass"][isns & (sn["unbound"] == 0)])
        allm, bound = np.concatenate(allm), np.concatenate(bound)
        dns = []
        for b, d in raw_fid["2.50"].items():
            dco = d["dco"]
            with h5py.File(next(r["h5"] for r in runs[("BSE",) + FID]["2.50"] if r["batch"] == b), "r") as f:
                g = f["BSE_Double_Compact_Objects"]; mm1, mm2 = g["Mass(1)"][()], g["Mass(2)"][()]
            sel = (dco["st1"] == 13) & (dco["st2"] == 13)
            dns.append(np.concatenate([mm1[sel], mm2[sel]]))
        dns = np.concatenate(dns)
        obs = np.array(OZEL_NS)
        ks_b = stats.ks_2samp(bound, obs); ks_a = stats.ks_2samp(allm, obs)
        ks_d = stats.ks_2samp(dns, obs) if len(dns) > 1 else None
        P(f"observed n=15: mean {obs.mean():.3f}, sd {obs.std(ddof=1):.3f}, range [{obs.min()}, {obs.max()}]")
        P(f"synthetic bound-after-SN NS births: n={len(bound)}, mean {bound.mean():.3f}, sd {bound.std():.3f}, quantiles 5/50/95 = {np.percentile(bound,5):.3f}/{np.percentile(bound,50):.3f}/{np.percentile(bound,95):.3f}")
        P(f"  KS D = {ks_b.statistic:.4f}, p = {ks_b.pvalue:.3e} -> {'PASS' if ks_b.pvalue >= 0.05 else 'FAIL'} at alpha = 0.05   [primary declared cut]")
        P(f"synthetic all NS births: n={len(allm)}, mean {allm.mean():.3f}, sd {allm.std():.3f}; KS D = {ks_a.statistic:.4f}, p = {ks_a.pvalue:.3e} -> {'PASS' if ks_a.pvalue >= 0.05 else 'FAIL'}")
        if ks_d is not None:
            P(f"synthetic DNS components (BSE_Double_Compact_Objects, both types 13; masses at DCO formation): n={len(dns)}, mean {dns.mean():.3f}, sd {dns.std():.3f}; "
              f"KS D = {ks_d.statistic:.4f}, p = {ks_d.pvalue:.3e} -> {'PASS' if ks_d.pvalue >= 0.05 else 'FAIL'}   [declared secondary cut, sample-matched: 14 of the 15 pinned masses are DNS components]")
        P("DISCLOSURE: the DNS-component cut was added after a 10^4-binary smoke test showed the primary (bound-after-SN births) cut failing; "
          "the primary cut is unchanged and decides C2 here; the RESULT dispatch may weigh the sample-matched cut and must say so.")
        c2 = dict(status="computed", n_bound=int(len(bound)), D_bound=float(ks_b.statistic), p_bound=float(ks_b.pvalue),
                  pass_primary=bool(ks_b.pvalue >= 0.05), D_all=float(ks_a.statistic), p_all=float(ks_a.pvalue),
                  n_dns=int(len(dns)), D_dns=(float(ks_d.statistic) if ks_d else None), p_dns=(float(ks_d.pvalue) if ks_d else None))
        P("C2 verdict (primary cut): " + ("PASS" if c2["pass_primary"] else "FAIL -> prereg section 5: stop; no class (secondary cut reported above)"))
    else:
        P("fiducial cap-2.50 batches not DONE yet")

    # ---- C3
    P()
    P("## C3 -- single-star (SSE) cap grid: derivative sign, and whether binary physics changes it")
    P("| alpha3 | engine | Z | SSE dY/dcap | sigma | sign | BSE default sign | BSE alt sign | binary physics changes sign? |")
    P("|---|---|---|---|---|---|---|---|---|")
    c3 = {}
    for eng in ENGINES:
        for Z in ZS:
            tab = config_table(data.get(("SSE", eng, Z, "default"), {}), batches_use=[1, 2, 3])
            for a3 in ALPHA3:
                r = tab["alpha3"][a3]
                s = sign_str(r["d"], k)
                bd = sign_str(box[(a3, eng, Z, "default")]["d"], k) if (a3, eng, Z, "default") in box else "n/a"
                ba = sign_str(box[(a3, eng, Z, "alt")]["d"], k) if (a3, eng, Z, "alt") in box else "n/a"
                chg = "n/a" if s == "n/a" or bd == "n/a" else ("no" if s == bd == ba else "YES")
                c3[str((a3, eng, Z))] = dict(sse=s, bse_default=bd, bse_alt=ba, changes=chg, d=r["d"])
                P(f"| {a3} | {eng} | {Z} | {FM(r['d'])} | {FS(r['d'])} | {s} | {bd} | {ba} | {chg} |")
    P("C3 passes when the SSE derivative sign is computable (resolved) at the centre point; stage 1's sign was negative (K1_MONOTONE_DOWN).")

    # ---- C4
    P()
    P("## C4 -- Monte-Carlo control at the centre configuration: 3 batches vs 6 batches")
    c4 = {}
    pb = data.get(("BSE",) + FID, {})
    t3 = config_table(pb, batches_use=[1, 2, 3]); t6 = config_table(pb, batches_use=[1, 2, 3, 4, 5, 6])
    P("| alpha3 | d (3 batches) | sigma | sign | d (6 batches) | sigma | sign | per-batch signs | sign stable? |")
    P("|---|---|---|---|---|---|---|---|---|")
    for a3 in ALPHA3:
        r3, r6 = t3["alpha3"][a3], t6["alpha3"][a3]
        per = "".join(("-" if f["d"] < 0 else "+") for b, f in sorted(r6["fd_per_batch"].items()))
        stable = "n/a" if r6["d"]["n"] < 6 else ("yes" if sign_str(r3["d"], k) == sign_str(r6["d"], k) else "NO")
        c4[a3] = dict(d3=r3["d"], d6=r6["d"], stable=stable, per_batch=per, n6=r6["d"]["n"])
        f = lambda m: (f"{m['mean']:.4e}" if m["n"] else "n/a")
        g = lambda m: (f"{m['sig']:.2e}" if np.isfinite(m["sig"]) else "n/a")
        P(f"| {a3} | {f(r3['d'])} | {g(r3['d'])} | {sign_str(r3['d'], k)} | {f(r6['d'])} | {g(r6['d'])} | {sign_str(r6['d'], k)} | {per} ({r6['d']['n']} batches) | {stable} |")

    # ---- write
    md = os.path.join(args.out, "K1S2_claude_post_output.md")
    with open(md, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    js = dict(jobs_done=n_jobs_done, verdict=verdict, C1=c1, C2=c2, C3=c3, C4={str(a): v for a, v in c4.items()},
              box={str(kk): dict(d=v["d"], dl=v["dl"], dr=v["dr"], c=v["c"], Y={c: v["Y"][c] for c in CAP_TAGS}) for kk, v in box.items()})
    with open(os.path.join(args.out, "K1S2_claude_post_output.json"), "w") as fh:
        json.dump(js, fh, indent=1, default=float)
    P()
    P(f"written: {md} and .json")

if __name__ == "__main__":
    main()
