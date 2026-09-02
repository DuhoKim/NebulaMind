#!/usr/bin/env python3
"""Compare normalized/spliced and raw/no-splice Reading-B spectra."""

import numpy as np
import mpmath as mp
from scipy.integrate import quad, simpson
from scipy.special import spherical_jn
import camb
from camb import initialpower, model

H0, OMBH2, OMCH2, TAU, MNU = 67.36, 0.02237, 0.1200, 0.0544, 0.06
AS, NS, KPIV = 2.1e-9, 0.9649, 0.05
A = 14015.0
BALL_RADIUS = A / 2.0
KSEC = 2.0 * np.pi / A
KMIN = 4.48318609e-10
LMAX = 150
QTOP = 2.0
EXTEND_END = 2.5


def primordial(k):
    return AS * (k / KPIV) ** (NS - 1.0)


def p_lcdm(k):
    return 2.0 * np.pi**2 * primordial(k) / k**3


def wtilde(s):
    z = s * BALL_RADIUS
    f = np.ones_like(z)
    nz = z != 0
    f[nz] = 3.0 * spherical_jn(1, z[nz]) / z[nz]
    return (4.0 * np.pi * BALL_RADIUS**3 / 3.0) * f**2


def fixed_raw_low_table(kmin):
    """Original fixed-run convolution, through its 0.006 /Mpc join point."""
    mu, wm = np.polynomial.legendre.leggauss(320)
    q = np.geomspace(kmin, QTOP, 7200)
    lq = np.log(q)
    dqin = primordial(q)
    integ0 = simpson(dqin * (2.0 * wtilde(q)), x=lq)
    c = integ0 / (2.0 * wtilde(np.array([0.0]))[0])
    klo = np.unique(np.r_[np.geomspace(1.0e-7, 8.0e-5, 35),
                          np.linspace(8.0e-5, 0.006, 190)])
    db = np.empty_like(klo)
    for i, k in enumerate(klo):
        s = np.sqrt(k*k + q[:, None]**2 - 2.0*k*q[:, None]*mu[None, :])
        imu = wtilde(s) @ wm
        integ = simpson(dqin * imu, x=lq)
        conv = k**3 * integ / (4.0 * np.pi**2)
        mono = k**3 * c * wtilde(np.array([k]))[0] / (2.0 * np.pi**2)
        db[i] = conv - mono
    return klo, db, c


ALPHA = 1.0 - NS
G_CONT = float(mp.gamma(NS - 2.0) * mp.sin(mp.pi * (NS - 2.0) / 2.0))
PREF = AS * KPIV**ALPHA


def window(r):
    x = r / A
    return 1.0 - 1.5*x + 0.5*x**3


def moment(alpha, power):
    s = power + alpha + 1.0
    return A**s * (1.0/s - 1.5/(s + 1.0) + 0.5/(s + 3.0))


def e_series(x):
    """Integral_0^x u^(ns-3)(sin(u)-u) du; x is tiny here."""
    out = np.zeros_like(np.asarray(x, dtype=float))
    for coef, n in [(-1/6, 1), (1/120, 2), (-1/5040, 3), (1/362880, 4)]:
        power = NS + 2*n - 1
        out += coef * np.asarray(x, dtype=float)**power / power
    return out


M_ALPHA = moment(ALPHA, 2) / moment(0.0, 2)
E_MEAN = quad(lambda r: r*r*window(r)*float(e_series(KMIN*r))*r**ALPHA,
              0.0, A, epsabs=1e-18, epsrel=2e-12, limit=300)[0] / moment(0.0, 2)


def xi_minus_c(r):
    # Exact finite-k_min expression; the k_min^(-alpha)/alpha constant cancels.
    return PREF * (r**ALPHA * (G_CONT - float(e_series(KMIN*r)))
                   - (G_CONT*M_ALPHA - E_MEAN))


def raw_p_b(k):
    """4 pi int r^2 W(r)[xi(r)-c] sinc(kr) dr."""
    if k < 1.0e-5:
        val = quad(lambda r: r*r*window(r)*xi_minus_c(r)*np.sinc(k*r/np.pi),
                   0.0, A, epsabs=1e-10, epsrel=3e-10, limit=400)[0]
        return 4.0*np.pi*val
    val = quad(lambda r: r*window(r)*xi_minus_c(r), 0.0, A,
               weight='sin', wvar=k, epsabs=1e-11, epsrel=3e-10, limit=500)[0]
    return 4.0*np.pi*val/k


def spliced_table(klo, raw_db):
    db = raw_db.copy()
    norm_band = klo >= 0.0045
    norm = np.median(db[norm_band] / primordial(klo[norm_band]))
    db /= norm
    preblend_min = db.min()
    join = klo >= 0.0045
    t = (klo[join] - 0.0045) / (0.006 - 0.0045)
    smooth = t*t*(3.0 - 2.0*t)
    db[join] = (1.0-smooth)*db[join] + smooth*primordial(klo[join])
    khi = np.geomspace(0.00601, 5.0, 260)
    return np.r_[klo, khi], np.r_[db, primordial(khi)], norm, preblend_min


def no_splice_table(klo):
    # Evaluate the constructed spectrum to the q-grid top.  Above 2 /Mpc,
    # smoothly remove its 0.064% residual over [2, 2.5], then use LCDM to 5.
    kmid = np.geomspace(0.00601, QTOP, 300)
    kraw = np.r_[klo, kmid]
    praw = np.array([raw_p_b(k) for k in kraw])
    draw = kraw**3 * praw / (2.0*np.pi**2)
    kext = np.geomspace(QTOP * (1.0 + 1e-8), 5.0, 90)
    dext = primordial(kext)
    transition = kext < EXTEND_END
    u = (kext[transition] - QTOP) / (EXTEND_END - QTOP)
    h = u*u*(3.0 - 2.0*u)
    ratio_top = praw[-1] / p_lcdm(QTOP)
    dext[transition] *= (1.0-h)*ratio_top + h
    return np.r_[kraw, kext], np.r_[draw, dext], praw, ratio_top


def camb_cls(k, pk):
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0, ombh2=OMBH2, omch2=OMCH2, tau=TAU, mnu=MNU)
    pars.InitPower.set_params(As=AS, ns=NS)
    ip = initialpower.SplinedInitialPower()
    ip.set_scalar_table(k, pk)
    ip.effective_ns_for_nonlinear = NS
    pars.InitPower = ip
    pars.NonLinear = model.NonLinear_none
    pars.set_for_lmax(LMAX, lens_potential_accuracy=0)
    pars.Want_CMB_lensing = False
    results = camb.get_results(pars)
    return results.get_cmb_power_spectra(
        pars, CMB_unit='muK', raw_cl=True, lmax=LMAX)['unlensed_scalar'][:, 0]


def s_half(cl):
    x, w = np.polynomial.legendre.leggauss(1200)
    x = 0.75*x - 0.25
    w = 0.75*w
    p0, p1 = np.ones_like(x), x.copy()
    corr = np.zeros_like(x)
    for ell in range(2, len(cl)):
        pl = ((2*ell-1)*x*p1 - (ell-1)*p0)/ell
        corr += (2*ell+1)*cl[ell]*pl/(4*np.pi)
        p0, p1 = p1, pl
    return np.sum(w*corr*corr)


def main():
    print("Residual normalization test: fixed support and deepest regulator")
    print(f"support = {A:.1f} Mpc; ball radius = {BALL_RADIUS:.1f} Mpc; k_min = {KMIN:.8e} 1/Mpc")
    klo, raw_low, c = fixed_raw_low_table(KMIN)

    ks, ds, norm, min_spliced = spliced_table(klo, raw_low)
    ss = s_half(camb_cls(ks, ds))
    print("\nSPLICED: original fixed prescription (divide by norm; smooth join 0.0045--0.006; LCDM above 0.006).")
    print(f"c = {c:.8e}; norm = {norm:.8f}")
    print(f"min(P_B) before the join = {np.min(2*np.pi**2*(raw_low/norm)/klo**3):.8e} Mpc^3")
    print(f"min(P_B) on the full spliced CAMB table = {np.min(2*np.pi**2*ds/ks**3):.8e} Mpc^3")
    print(f"min(Delta_B^2) before the join = {min_spliced:.8e}")
    print(f"S_1/2 spliced = {ss:.3f} uK^4")

    kn, dn, praw, ratio_top = no_splice_table(klo)
    sn = s_half(camb_cls(kn, dn))
    probes = np.array([0.01, 0.05, 0.2, 1.0, 2.0])
    pprobe = np.array([raw_p_b(k) for k in probes])
    print("\nNO-SPLICE: raw finite-k_min monopole-subtracted P_B, with no norm divide and no low-k join.")
    print("Above the q-grid top k=2, its endpoint ratio is continued with a cubic smoothstep to ratio 1")
    print("over 2 < k < 2.5 1/Mpc, and exact LCDM is used from 2.5 through the CAMB table top k=5.")
    print(f"P_B/P_LCDM at q-grid top k=2 = {ratio_top:.8f}")
    print("P_B/P_LCDM probe ratios:")
    for k, p in zip(probes, pprobe):
        print(f"  k = {k:4.2f} 1/Mpc : {p/p_lcdm(k):.8f}")
    print(f"min(P_B) on the raw CAMB grid through k=2 = {praw.min():.8e} Mpc^3")
    print(f"min(P_B) on the full extended no-splice CAMB table = {np.min(2*np.pi**2*dn/kn**3):.8e} Mpc^3")
    print(f"min(Delta_B^2) on the raw CAMB grid through k=2 = {np.min(kn[:praw.size]**3*praw/(2*np.pi**2)):.8e}")
    print(f"S_1/2 no-splice = {sn:.3f} uK^4")
    pct = 100.0*(sn-ss)/ss
    print(f"\nPercent difference (no-splice - spliced)/spliced = {pct:+.3f}%")


if __name__ == '__main__':
    main()
