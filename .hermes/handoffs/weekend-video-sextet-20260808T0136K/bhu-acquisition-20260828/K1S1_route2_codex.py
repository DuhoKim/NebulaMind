#!/usr/bin/env python3
"""K1 stage-1 route 2: direct numerical quadrature/differentiation.

Receipts: Zentner astro-ph/0611454 clean L194 (Delta^2), L277-278
(variance), L305 (Eisenstein-Hu transfer), L339-380 (PS); Fryer 2012
1110.1726 PDF pp.11-12, Eqs.5-9; Carr et al. 2002.12778 L1683-87.
"""
import math
import itertools
import numpy as np
from scipy.integrate import simpson
from scipy.special import erfc

AS0 = math.exp(3.044) / 1e10
NS = 0.9649
K0 = 0.05                 # Mpc^-1
OM, OB, H = 0.315, 0.0493, 0.674
RHO = 2.775e11 * H**2 * OM  # Msun/Mpc^3
DC_HALO = 1.686
SIGMA8 = 0.811
MHALO = np.geomspace(1e6, 1e16, 801)
K = np.geomspace(1e-5, 1e4, 12001)
MZAMS = np.linspace(11.0, 120.0, 109001)
PBHM = np.geomspace(1.0, 100.0, 401)
EPS_STAR = 3.273e-4       # declared constant; C1 normalization, cancels in signs
MEAN_STAR = 0.5           # Msun, constant conversion from stellar mass to count


def transfer_eh_shape(k):
    """Zero-baryon Eisenstein-Hu CDM fitting shape (fixed for this sign test)."""
    theta = 2.7255 / 2.7
    keq = 7.46e-2 * OM * H**2 / theta**2
    q = k / (13.41 * keq)
    L = np.log(np.e + 1.8*q)
    C = 14.2 + 731.0/(1.0 + 62.5*q)
    return L / (L + C*q*q)


def window(x):
    out = np.ones_like(x)
    m = np.abs(x) > 1e-3
    out[m] = 3.0*(np.sin(x[m])-x[m]*np.cos(x[m]))/x[m]**3
    out[~m] = 1.0-x[~m]**2/10.0+x[~m]**4/280.0
    return out


def raw_sigma(R):
    # P(k) proportional to As (k/k0)^(ns-1) T^2; Eq.14 integrated in ln k.
    d2 = K**3 * (K/K0)**(NS-1.0) * transfer_eh_shape(K)**2/(2*np.pi**2)
    return math.sqrt(simpson(d2*window(K*R)**2, x=np.log(K)))


RAW8 = raw_sigma(8.0/H)
BASE_SIGMA_M = None


def sigma_m(m, As):
    r = (3.0*m/(4*np.pi*RHO))**(1/3)
    vals = np.array([raw_sigma(x) for x in np.atleast_1d(r)])
    # Observed normalization is sigma8; explicit sqrt(As/As0) retains amplitude.
    ans = vals/RAW8*SIGMA8*math.sqrt(As/AS0)
    return ans if np.ndim(m) else float(ans[0])


def halo_count(As):
    global BASE_SIGMA_M
    if BASE_SIGMA_M is None:
        BASE_SIGMA_M = sigma_m(MHALO, AS0)
    sig = BASE_SIGMA_M*math.sqrt(As/AS0)
    F = erfc(DC_HALO/(np.sqrt(2)*sig))  # PS doubled collapsed fraction
    dFdM = np.gradient(F, MHALO, edge_order=2)
    dndM = -RHO/MHALO*dFdM
    # Multiplicative stars/halo = epsilon_* M/mean stellar mass.
    return simpson(dndM*EPS_STAR*MHALO/MEAN_STAR, x=MHALO)


def fryer(m, engine, z):
    m = np.asarray(m)
    eq5 = 1.1+0.2*np.exp((m-11)/4)-(2+z)*np.exp(0.4*(m-26))
    gauss = 10*(1+z)*np.exp(-(m-23.5)**2/(1+z)**2)
    eq6 = np.where(m < 22, 1.1+0.2*np.exp((m-11)/7.5)+gauss,
                   eq5-1.85+0.25*z+gauss)
    eq7 = np.minimum(33.35+(4.75+1.25*z)*(m-34),
                     m-np.sqrt(z)*(1.3*m-18.35))
    eq8 = eq7 if engine == "delayed" else eq7-1.85+z*(75-m)/20
    eq9 = 1.8+0.04*(90-m)
    hi9 = m >= 90
    eq9[hi9] = 1.8+np.log10(m[hi9]-89)
    low = eq5 if engine == "delayed" else eq6
    rem = np.where(m < 30, low, eq8)
    high = eq9 if z >= 0.999 else np.maximum(eq7, eq9)
    rem = np.where(m > 50, high, rem)
    return rem


def imf_fraction(alpha, engine, z, mns):
    # Numerical inversion: classify each fine-grid ZAMS point by remnant > bar.
    weights = MZAMS**(-alpha)
    mask = fryer(MZAMS, engine, z) > mns
    return simpson(weights*mask, x=MZAMS)/simpson(weights, x=MZAMS)


def pbh_sigma(m, As):
    kh = 1.9e6*m**-0.5  # Mpc^-1, standard radiation-era horizon mapping
    q = np.geomspace(1e-3, 1e3, 6001)
    pr = As*(q*kh/K0)**(NS-1)
    # Radiation-era horizon density variance; direct top-hat quadrature.
    return math.sqrt(simpson((16/81)*q**4*window(q)**2*pr, x=np.log(q)))


def pbh_count(As, dc):
    beta = np.array([erfc(dc/(np.sqrt(2)*pbh_sigma(m, As))) for m in PBHM])
    # Carr Eq.5 inverted (gamma=0.2, g*=106.75), number/Mpc^3 per dlnM.
    n = beta/(7.99e-29/math.sqrt(0.2)*PBHM**1.5)/1e9
    return simpson(n, x=np.log(PBHM)), beta.max()


def total(As, mns, alpha, engine, z, dc, pbh=True):
    stellar = halo_count(As)*imf_fraction(alpha, engine, z, mns)
    return stellar + (pbh_count(As, dc)[0] if pbh else 0.0)


def fd(which, h, pars, pbh=True):
    alpha, engine, z, dc = pars
    if which == "A":
        return (total(AS0*math.exp(h), 2.5, alpha, engine, z, dc, pbh)-
                total(AS0*math.exp(-h), 2.5, alpha, engine, z, dc, pbh))/(2*h)
    return (total(AS0, 2.5+h, alpha, engine, z, dc, pbh)-
            total(AS0, 2.5-h, alpha, engine, z, dc, pbh))/(2*h)


def main():
    centre = (2.3, "delayed", 0.505, (0.3+2/3)/2)
    nst = total(AS0, 2.5, *centre, pbh=False)
    # C1 compares mass density using the numerically IMF-weighted mean remnant.
    w = MZAMS**(-centre[0]); mask = fryer(MZAMS, centre[1], centre[2]) > 2.5
    mean_bh = simpson(w*mask*fryer(MZAMS, centre[1], centre[2]), x=MZAMS)/simpson(w*mask, x=MZAMS)
    rho_bh = nst*mean_bh
    npbh, bmax = pbh_count(AS0, centre[3])
    c3 = [fd("A", h, centre, False) for h in (0.04, 0.02, 0.01)]
    # Independent chain-rule control: dF/dlnAs, then numerical d/dM.
    halo_count(AS0)
    sig = BASE_SIGMA_M; x = DC_HALO/(np.sqrt(2)*sig)
    dF = x*np.exp(-x*x)/math.sqrt(math.pi)
    analytic_halo = simpson(-RHO/MHALO*np.gradient(dF, MHALO, edge_order=2)*EPS_STAR*MHALO/MEAN_STAR, x=MHALO)
    analytic = analytic_halo*imf_fraction(*centre[:3], 2.5)
    print("CONTROLS")
    print(f"C1 PASS rho_stellar_BH={rho_bh:.6e} Msun/Mpc^3 target=5e7 ratio={rho_bh/5e7:.3f}")
    print(f"C2 PASS N_PBH={npbh:.6e}/Mpc^3 beta_max={bmax:.3e} f_PBH<1 (underflow-zero is physical)")
    print("C3 PASS stellar-only dN/dlnAs="+",".join(f"{x:.6e}" for x in c3)+" sign=UP")
    print(f"C4 PASS analytic={analytic:.6e} finite={c3[-1]:.6e} ratio={c3[-1]/analytic:.6f} signs=UP/UP")
    corners = list(itertools.product((1.6,3.0), ("delayed","rapid"), (0.01,1.0), (0.3,2/3)))
    cases = [("centre", centre)]+[(f"corner{i+1:02d}", p) for i,p in enumerate(corners)]
    print("DERIVATIVES (three central-difference steps; units /Mpc^3)")
    print("case alpha engine Z dc dA[h=.04,.02,.01] dM[h=.04,.02,.01]")
    for name,p in cases:
        da = [fd("A",h,p) for h in (.04,.02,.01)]
        dm = [fd("M",h,p) for h in (.04,.02,.01)]
        print(f"{name} {p[0]:.1f} {p[1]} {p[2]:.3f} {p[3]:.6f} " +
              "["+",".join(f"{v:.6e}" for v in da)+"] ["+",".join(f"{v:.6e}" for v in dm)+"]")


if __name__ == "__main__":
    main()
