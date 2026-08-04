#!/usr/bin/env python3
"""
Cycle-3 Goru — quantify how much of the observed SFMS 'elevation' in paper #3
(and the load-bearing sim-vs-obs SFR gap in #6) is an EMISSION-LINE SELECTION
artifact, by forward-modelling that selection onto a mock high-z population.

Standalone. Reuses only the public SDSS SkyServer TAP endpoint (same as
tools/lab_runner_worker.sdss_pull) to ground the SFMS scatter empirically.
Does NOT touch the worker daemon/queue or any tracked file.
"""
import warnings; warnings.filterwarnings("ignore")
import numpy as np, requests
from scipy.stats import norm
from astropy.cosmology import FlatLambdaCDM

rng = np.random.default_rng(7)
cosmo = FlatLambdaCDM(H0=67.74, Om0=0.3089)  # Planck15-ish, matches TNG

# ---- paper #3 claimed elevations (Δlog SFR above z≈0 SFMS, at fixed M*) ----
OBS = [(3.5, 0.77), (4.7, 0.89), (5.4, 0.96), (6.7, 1.94)]
# local SFMS (both papers): log SFR = 0.61(logM*-10) + 0.065
def sfms_local(lgm): return 0.61*(lgm-10.0)+0.065

# ============================================================
# 1. Ground the SFMS scatter sigma(M) on real SDSS
# ============================================================
TAP="https://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch"
def sdss_pull(cols,where):
    r=requests.get(TAP,params={"cmd":f"SELECT TOP 120000 {cols} FROM galSpecExtra WHERE {where}","format":"csv"},timeout=240)
    return np.genfromtxt(r.text.splitlines(),delimiter=",",skip_header=2)
print("pulling SDSS SFMS to measure intrinsic scatter sigma(M*)…")
raw=sdss_pull("lgm_tot_p50, sfr_tot_p50, specsfr_tot_p50",
              "lgm_tot_p50 BETWEEN 8.5 AND 11.5 AND specsfr_tot_p50>-11 AND sfr_tot_p50>-50")
lgm,sfr=raw[:,0],raw[:,1]; g=np.isfinite(lgm)&np.isfinite(sfr); lgm,sfr=lgm[g],sfr[g]
res=sfr-sfms_local(lgm)
# robust scatter in mass bins (dominant SF ridge; clip the passive/AGN lower wing)
sig_bins=[]
for lo in np.arange(8.5,11.0,0.5):
    m=(lgm>=lo)&(lgm<lo+0.5); r=res[m]
    r=r[np.abs(r-np.median(r))<1.5]  # trim
    sig_bins.append((lo+0.25, np.std(r), m.sum()))
sig_sf = np.median([s for _,s,_ in sig_bins])
print(f"  SDSS N={len(lgm):,}; SF-ridge scatter by mass: "+
      ", ".join(f'{c:.2f}:{s:.2f}dex' for c,s,_ in sig_bins))
print(f"  adopted local SF-ridge sigma ~ {sig_sf:.2f} dex "
      f"(paper quotes 0.39 incl. green-valley; intrinsic SF ridge is tighter)")

# high-z scatter is larger than local; carry a grid
SIGMAS = {"lo":0.30, "mid":0.45, "hi":0.60}   # dex, intrinsic high-z SFMS scatter

# ============================================================
# 2. Forward model: emission-line (Hbeta-flux) selection on a mock high-z pop
# ============================================================
# SFR->Halpha (Kennicutt98, Chabrier): logL(Ha)=41.1+log SFR ; L(Hb)=L(Ha)/2.86
# Detection: Hbeta line flux F(Hb) > F_lim  ->  SFR floor rising as d_L(z)^2.
LHA0=41.1
def sfr_floor(z, F_lim):
    dL=cosmo.luminosity_distance(z).to('cm').value
    Lhb_lim=4*np.pi*dL**2*F_lim          # erg/s
    Lha_lim=Lhb_lim*2.86
    return np.log10(Lha_lim)-LHA0        # log SFR floor [Msun/yr]

# intrinsic high-z stellar mass function over the JWST range (steep faint end).
# dN/dlogM ~ 10^{-beta*logM}. detected mass distn emerges self-consistently.
LGM_LO, LGM_HI = 7.0, 10.5
def mock_pop(z, E_true, sigma, F_lim, beta=0.9, N=400000):
    # draw masses from declining MF
    u=rng.random(N)
    # inverse-CDF for p(logM)∝10^{-beta logM} on [LGM_LO,LGM_HI]
    a=10**(-beta*LGM_LO); b=10**(-beta*LGM_HI)
    lgm=-np.log10(a-u*(a-b))/beta
    mu=sfms_local(lgm)+E_true
    logsfr=mu+rng.normal(0,sigma,N)
    floor=sfr_floor(z,F_lim)
    det=logsfr>floor
    return lgm[det], logsfr[det], floor

def observed_elevation(lgm_d, logsfr_d):
    # paper's estimator: median of Δ=logSFR-SFMS_local(M) over detected sample
    return np.median(logsfr_d - sfms_local(lgm_d))

def recover_Etrue(z, E_obs_target, sigma, F_lim, beta=0.9):
    # scan E_true, find value whose forward-modelled observed elevation matches target
    grid=np.arange(-0.4, 2.01, 0.02)
    best=None
    for Et in grid:
        lgm_d,ls_d,_=mock_pop(z,Et,sigma,F_lim,beta)
        if len(lgm_d)<2000: continue
        Eo=observed_elevation(lgm_d,ls_d)
        d=abs(Eo-E_obs_target)
        if best is None or d<best[0]: best=(d,Et,Eo,len(lgm_d),lgm_d)
    return best  # (resid, E_true, E_obs_check, Ndet, masses)

# central config + sensitivity grid
F_CENTRAL=3e-19   # deep NIRSpec Hbeta line sensitivity (erg/s/cm^2), central
F_GRID={"shallow":1e-18,"central":3e-19,"deep":1e-19}

print("\n=== FORWARD-MODEL: selection-induced inflation of SFMS elevation ===")
print("(E_obs = paper value; E_true = de-biased; inflation = E_obs - E_true)\n")
print(f"{'z':>4} {'E_obs':>6} | {'model':>8} {'sig':>4} {'Flim':>6} | "
      f"{'E_true':>6} {'infl':>5} {'%sel':>5} {'lgMdet50':>8} {'Ndet':>7}")
central_rows={}
for z,Eo in OBS:
    for sk,sig in [("mid",SIGMAS["mid"])]:
        for fk,Fl in F_GRID.items():
            r=recover_Etrue(z,Eo,sig,Fl)
            if r is None: continue
            _,Et,Eochk,Nd,masses=r
            infl=Eo-Et; pct=100*infl/Eo
            m50=np.median(masses)
            tag=" *" if (sk=="mid" and fk=="central") else ""
            print(f"{z:>4} {Eo:>6.2f} | {sk:>8} {sig:>4.2f} {Fl:>6.0e} | "
                  f"{Et:>6.2f} {infl:>5.2f} {pct:>4.0f}% {m50:>8.2f} {Nd:>7d}{tag}")
            if sk=="mid" and fk=="central": central_rows[z]=(Et,infl,pct,m50)
    print()

# full sensitivity envelope on the CENTRAL (deep-ish) flux, varying sigma + flux
print("=== SENSITIVITY ENVELOPE (inflation range over sigma∈{.30,.45,.60}, "
      "Flim∈{1e-19..1e-18}) ===")
for z,Eo in OBS:
    infls=[]
    for sig in SIGMAS.values():
        for Fl in F_GRID.values():
            r=recover_Etrue(z,Eo,sig,Fl)
            if r: infls.append(Eo-r[1])
    lo,hi=min(infls),max(infls); md=np.median(infls)
    print(f"  z≈{z}: E_obs={Eo:+.2f}  ->  inflation {md:+.2f} dex "
          f"[{lo:+.2f},{hi:+.2f}];  residual PHYSICAL E_true≈{Eo-md:+.2f} "
          f"[{Eo-hi:+.2f},{Eo-lo:+.2f}]")

# ============================================================
# 3. Analytic cross-check: truncated-Gaussian median shift at char. mass
# ============================================================
print("\n=== ANALYTIC CROSS-CHECK (truncated-normal median shift q(a)*sigma) ===")
def q(a):  # median shift of below-truncated N(0,1), in sigma units
    return norm.ppf((1+norm.cdf(a))/2)
for z,Eo in OBS:
    sig=SIGMAS["mid"]; Fl=F_CENTRAL
    for lgmc in (8.0,9.0):
        mu=sfms_local(lgmc)+Eo   # use observed as proxy for elevated median
        a=(sfr_floor(z,Fl)-mu)/sig
        print(f"  z≈{z} logM*={lgmc}: floor={sfr_floor(z,Fl):+.2f} "
              f"mu={mu:+.2f} a={a:+.2f} -> shift={sig*q(a):+.2f} dex")

# ============================================================
# 4. Paper #6 implication: does the sim-vs-obs SFR gap survive?
# ============================================================
print("\n=== PAPER #6 CHECK: sim-vs-obs SFR gap under selection-matching ===")
# #6 internal TNG growth: +1.30,+1.45,+1.61 at z=4,5,6 ; obs elevation +0.89,+0.96
TNG={4:1.30,5:1.45,6:1.61}; OBS6={4.7:0.89,5.4:0.96}
for z,Eo in [(4.7,0.89),(5.4,0.96)]:
    Et,infl,pct,_=central_rows.get(z,(None,None,None,None))
    zt=round(z-0.7) if z<5 else round(z-0.4)
    tng=TNG.get(4 if z<5 else 5)
    print(f"  z≈{z}: obs raw={Eo:+.2f} (selection-inflated by {infl:+.2f}) -> "
          f"obs de-biased={Et:+.2f};  TNG internal={tng:+.2f}")
    print(f"        gap(raw)={tng-Eo:+.2f}  gap(de-biased)={tng-Et:+.2f}  "
          f"-> de-biasing WIDENS the TNG over-evolution by {(tng-Et)-(tng-Eo):+.2f} dex")

# ============================================================
# 5. SAMPLE-MATCHED central: pin F_lim per bin so detected median mass
#    matches the paper's actual sample composition.
#    z<6 MS bins are Lisiecki/MIRI-dominated (n~900-1900, brighter, logM*~9.3)
#    z>6 bin (n=46) is Nakajima/NIRSpec-dominated (fainter, logM*~8.3)
# ============================================================
print("\n=== SAMPLE-MATCHED CENTRAL (flux pinned to paper's detected mass) ===")
TARGET_M50={3.5:9.3, 4.7:9.3, 5.4:9.3, 6.7:8.3}
def match_flux(z,Eo,sig,m_target):
    best=None
    for Fl in np.geomspace(3e-20,2e-18,22):
        r=recover_Etrue(z,Eo,sig,Fl)
        if r is None: continue
        _,Et,_,Nd,masses=r; m50=np.median(masses)
        d=abs(m50-m_target)
        if best is None or d<best[0]: best=(d,Fl,Et,m50,Nd)
    return best
sm_central={}
for z,Eo in OBS:
    _,Fl,Et,m50,Nd=match_flux(z,Eo,SIGMAS["mid"],TARGET_M50[z])
    infl=Eo-Et; pct=100*infl/Eo; sm_central[z]=(Et,infl,pct)
    print(f"  z≈{z}: E_obs={Eo:+.2f}  Flim={Fl:.1e}  logMdet50={m50:.2f}  "
          f"-> E_true(phys)={Et:+.2f}  selection inflation={infl:+.2f} dex ({pct:.0f}%)")

print("\n=== PAPER #6 (sample-matched central) ===")
TNG={4:1.30,5:1.45,6:1.61}
for z,tngz in [(4.7,4),(5.4,5)]:
    Eo=dict(OBS)[z]; Et,infl,_=sm_central[z]; tng=TNG[tngz]
    print(f"  z≈{z}: obs raw {Eo:+.2f} -> de-biased {Et:+.2f}; TNG internal {tng:+.2f}; "
          f"gap raw {tng-Eo:+.2f} -> de-biased {tng-Et:+.2f} (WIDENS {(tng-Et)-(tng-Eo):+.2f})")
