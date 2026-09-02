#!/usr/bin/env python3
"""Reading B with the weighted monopole removed (P_B(0)=0)."""

import numpy as np
from scipy.special import spherical_jn
from scipy.integrate import simpson
import camb
from camb import initialpower, model

H0, OMBH2, OMCH2, TAU, MNU = 67.36, 0.02237, 0.1200, 0.0544, 0.06
AS, NS, KPIV = 2.1e-9, 0.9649, 0.05
A = 14015.0
KSEC = 2.0 * np.pi / A
LMAX = 150


def primordial(k):
    return AS * (k / KPIV) ** (NS - 1.0)


def wtilde(s):
    """Transform of the normalized overlap window of two radius-A/2 balls."""
    z = s * A
    f = np.ones_like(z)
    nz = z != 0
    f[nz] = 3.0 * spherical_jn(1, z[nz]) / z[nz]
    return (4.0 * np.pi * A**3 / 3.0) * f**2


def reading_b_table(kmin):
    mu, wm = np.polynomial.legendre.leggauss(320)
    q = np.geomspace(kmin, 2.0, 7200)
    lq = np.log(q)
    dqin = primordial(q)

    # At k=0, the angular integral is exactly 2 W_tilde(q).  In the
    # conventions below P_conv(0)=integral/2, hence c=P_conv(0)/W_tilde(0).
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

    # Preserve the stipulated normalization to unchanged LCDM at high k.
    norm_band = klo >= 0.0045
    norm = np.median(db[norm_band] / primordial(klo[norm_band]))
    db /= norm
    raw_min = db.min()
    raw_kmin = klo[np.argmin(db)]
    p_dim = 2.0 * np.pi**2 * db / klo**3
    p_dim_min = p_dim.min()

    khi = np.geomspace(0.00601, 5.0, 260)
    dhi = primordial(khi)
    join = klo >= 0.0045
    t = (klo[join] - 0.0045) / (0.006 - 0.0045)
    smooth = t*t*(3.0 - 2.0*t)
    db[join] = (1.0-smooth)*db[join] + smooth*primordial(klo[join])
    return (np.r_[klo, khi], np.r_[db, dhi], norm, c, raw_min,
            raw_kmin, p_dim_min)


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
    kmins = KSEC * np.array([1e-3, 1e-4, 1e-5, 1e-6])
    print("Monopole-subtracted Reading B calculation")
    print(f"chi_section = {A:.1f} Mpc; k_section = {KSEC:.9g} 1/Mpc")
    print("Condition: c=<W xi>/<W>, so P_B(0)=0; high-k spectrum joins unchanged LCDM above 0.006 1/Mpc.")
    print("\nk_min/k_section       k_min [1/Mpc]                 c    min(Delta_B^2)       min(P_B)       norm       S_1/2 [uK^4]")
    vals, minima, pminima = [], [], []
    for km in kmins:
        k, pk, norm, c, minimum, k_at_min, pminimum = reading_b_table(km)
        cl = camb_cls(k, pk)
        s = s_half(cl)
        vals.append(s)
        minima.append(minimum)
        pminima.append(pminimum)
        print(f"{km/KSEC:14.0e}   {km:16.8e}   {c:16.8e}   {minimum:16.8e}  {pminimum:13.6e}  {norm:8.5f}   {s:14.3f}")
    positive = all(np.isfinite(minima)) and min(minima) >= 0.0
    print("\nNumerical positivity check: " + ("PASS" if positive else "FAIL"))
    print(f"Global grid minimum Delta_B^2 = {min(minima):.8e}")
    print(f"Global grid minimum P_B = {min(pminima):.8e} Mpc^3")
    spread = max(vals)-min(vals)
    print(f"Regulator spread in S_1/2 = {spread:.3f} uK^4 (max/min={max(vals)/min(vals):.9g}).")
    print(f"Successive fractional changes = " + ", ".join(f"{(vals[i]-vals[i-1])/vals[i-1]:+.3e}" for i in range(1, len(vals))))
    print(f"Comparison (smallest-k_min case): LCDM 34,924 | Reading A 6,897 | Reading B (subtracted) {vals[-1]:.0f} | observed ~1,150")


if __name__ == '__main__':
    main()
