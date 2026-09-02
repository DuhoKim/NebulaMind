#!/usr/bin/env python3
"""Reading B: compactly supported primordial correlation and its CMB S_1/2."""

import numpy as np
from scipy.special import spherical_jn
from scipy.integrate import simpson
import camb
from camb import initialpower, model

# Fixed inputs from the brief.
H0, OMBH2, OMCH2, TAU, MNU = 67.36, 0.02237, 0.1200, 0.0544, 0.06
AS, NS, KPIV = 2.1e-9, 0.9649, 0.05
A = 14015.0                         # chi_section, Mpc
KSEC = 2.0 * np.pi / A
LMAX = 150


def primordial(k):
    return AS * (k / KPIV) ** (NS - 1.0)


def wtilde(s):
    """3-D transform of W(r), the normalized overlap of two radius-a balls."""
    z = s * A
    f = np.ones_like(z)
    nz = z != 0
    f[nz] = 3.0 * spherical_jn(1, z[nz]) / z[nz]
    return (4.0 * np.pi * A**3 / 3.0) * f**2


def reading_b_table(kmin):
    # Product in real space = convolution in Fourier space.  Both factors in
    # this integrand are nonnegative, making positivity manifest.
    mu, wm = np.polynomial.legendre.leggauss(320)
    q = np.geomspace(kmin, 2.0, 7200)
    lq = np.log(q)
    dq_weights = None

    # Resolve the low-k feature densely. Above 0.006/Mpc its correction is
    # negligible; use the exact input power there (the stipulated high-k
    # normalization, with a smooth join).
    klo = np.unique(np.r_[np.geomspace(1.0e-7, 8.0e-5, 35),
                          np.linspace(8.0e-5, 0.006, 190)])
    db = np.empty_like(klo)
    dqin = primordial(q)
    for i, k in enumerate(klo):
        s = np.sqrt(k*k + q[:, None]**2 - 2.0*k*q[:, None]*mu[None, :])
        imu = wtilde(s) @ wm
        integ = simpson(dqin * imu, x=lq)
        db[i] = k**3 * integ / (4.0 * np.pi**2)

    # At several k_section the convolution must tend to the original power.
    # Numerically enforce the requested asymptotic normalization using the
    # resolved upper end, then smoothly join to exact LCDM.
    norm_band = klo >= 0.0045
    norm = np.median(db[norm_band] / primordial(klo[norm_band]))
    db /= norm

    khi = np.geomspace(0.00601, 5.0, 260)
    dhi = primordial(khi)
    # Smoothly remove any residual quadrature mismatch over 0.0045--0.006.
    join = klo >= 0.0045
    t = (klo[join] - 0.0045) / (0.006 - 0.0045)
    smooth = t*t*(3.0 - 2.0*t)
    db[join] = (1.0-smooth)*db[join] + smooth*primordial(klo[join])
    return np.r_[klo, khi], np.r_[db, dhi], norm


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
    # raw_cl=True gives C_l in K^2; convert to micro-K^2.
    return results.get_cmb_power_spectra(pars, CMB_unit='muK', raw_cl=True,
                                         lmax=LMAX)['unlensed_scalar'][:, 0]


def s_half(cl):
    # Direct, high-order Gauss-Legendre integration of C(theta)^2.
    x, w = np.polynomial.legendre.leggauss(1200)
    x = 0.75*x - 0.25                # [-1, 1/2]
    w = 0.75*w
    ell = np.arange(2, len(cl))
    # Stable Legendre recurrence, accumulating only ell>=2.
    p0 = np.ones_like(x)
    p1 = x.copy()
    corr = np.zeros_like(x)
    for l in range(2, len(cl)):
        pl = ((2*l-1)*x*p1 - (l-1)*p0)/l
        corr += (2*l+1)*cl[l]*pl/(4*np.pi)
        p0, p1 = p1, pl
    return np.sum(w*corr*corr)


def main():
    kmins = KSEC * np.array([1e-3, 1e-4, 1e-5, 1e-6])
    print("Reading B compact-correlation calculation")
    print(f"chi_section = {A:.1f} Mpc; k_section = {KSEC:.9g} 1/Mpc")
    print("W(r)=(1-r/a)^2(2+r/a)/2 for r<=a, zero otherwise")
    print("W_tilde=V[3 j1(ka)/(ka)]^2 >= 0; convolution with P_LCDM>=0 guarantees P_B>=0.")
    print("High-k normalization: P_B is joined to the unchanged LCDM spectrum above 0.006 1/Mpc.")
    print("\nk_min/k_section       k_min [1/Mpc]      min(Delta_B^2)    norm       S_1/2 [uK^4]")
    vals = []
    minima = []
    for km in kmins:
        k, pk, norm = reading_b_table(km)
        minimum = pk.min()
        cl = camb_cls(k, pk)
        s = s_half(cl)
        vals.append(s)
        minima.append(minimum)
        print(f"{km/KSEC:14.0e}   {km:16.8e}   {minimum:16.8e}  {norm:8.5f}   {s:14.3f}")
    positive = all(np.isfinite(minima)) and min(minima) >= 0.0
    print("\nNumerical positivity check: PASS" if positive else "Numerical positivity check: FAIL")
    spread = max(vals)-min(vals)
    print(f"Reading-B regulator spread in S_1/2 = {spread:.3f} uK^4 (max/min={max(vals)/min(vals):.6g}).")
    print(f"Comparison (smallest-k_min case): LCDM 34,924 | Reading A 6,897 | Reading B {vals[-1]:.0f} | observed ~1,150")
    side_a = np.sign(6897-1150)
    side_b = np.sign(vals[-1]-1150)
    print("A and B are on the " + ("same" if side_a == side_b else "opposite") + " sides of 1,150.")


if __name__ == '__main__':
    main()
