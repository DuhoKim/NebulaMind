#!/usr/bin/env python3
"""Reproducible Phase-1 CAMB calculations; no low-l data enter parameters."""
import numpy as np
import sys
import camb
from camb import initialpower
from numpy.polynomial.legendre import leggauss
from scipy.special import sici, eval_legendre

H0 = 67.36
L = 3.15 * 299792.458 / H0       # Mpc, fixed by the causal-scale argument
AS, NS, KP = 2.100549e-9, 0.9649, 0.05

def base_pars():
    p = camb.CAMBparams()
    p.set_cosmology(H0=H0, ombh2=0.02237, omch2=0.1200,
                    mnu=0.06, omk=0, tau=0.0544)
    p.set_for_lmax(300, lens_potential_accuracy=0)
    p.WantTensors = False
    p.DoLensing = True
    p.NonLinear = camb.model.NonLinear_none
    p.Accuracy.AccuracyBoost = 1
    p.Accuracy.lAccuracyBoost = 1
    p.Accuracy.lSampleBoost = 1
    return p

def window_r1(k):
    # xi(r)=C ln(L/r) 1_(r<L); W normalized by the Cesaro/high-k mean.
    x = k*L
    si = sici(x)[0]
    return (2/np.pi)*(si-np.sin(x))

def run(kind):
    p = base_pars()
    if kind == 'lcdm':
        p.InitPower.set_params(As=AS, ns=NS, pivot_scalar=KP)
    else:
        k = np.geomspace(1e-7, 2.0, 2000)
        primordial = AS*(k/KP)**(NS-1)
        if kind == 'r1':
            primordial *= window_r1(k)
        elif kind == 'r2_pi':
            # CAMB-compatible continuum surrogate for a ball's lowest Dirichlet
            # radial wavenumber. The true ball problem is discrete/anisotropic.
            kc=np.pi/L
            primordial *= .5*(1+np.tanh((k-kc)/(kc/100)))
            primordial = np.maximum(primordial, 1e-30*AS)
        elif kind == 'r2_4493':
            # Alternative first zero j_1 for removal of monopole sector.
            kc=4.493409/L
            primordial *= .5*(1+np.tanh((k-kc)/(kc/100)))
            primordial = np.maximum(primordial, 1e-30*AS)
        ip = initialpower.SplinedInitialPower()
        ip.set_scalar_table(k, primordial)
        ip.effective_ns_for_nonlinear = NS
        p.InitPower = ip
    res = camb.get_results(p)
    # raw_cl=True gives C_l, not l(l+1)C_l/2pi; CMB_unit supplies microK^2.
    cl = res.get_lensed_scalar_cls(CMB_unit='muK', raw_cl=True,
                                   lmax=300)[:,0]
    return cl

def s_half(cl, lmax=300):
    # deterministic high-order Gauss-Legendre integral over mu in [-1,1/2]
    q, w = leggauss(1600)
    mu = .75*q - .25
    wt = .75*w
    ell = np.arange(2, min(lmax, len(cl)-1)+1)
    corr = np.zeros_like(mu)
    for l in ell:
        corr += (2*l+1)*cl[l]*eval_legendre(l, mu)/(4*np.pi)
    return np.sum(wt*corr*corr)

if __name__ == '__main__':
    print(f'L_Mpc {L:.9f} kpi {np.pi/L:.10g} k4493 {4.493409/L:.10g}')
    names = sys.argv[1:] or ('lcdm','r1','r2_pi','r2_4493')
    for name in names:
        cl = run(name)
        print(name, f'S1/2={s_half(cl):.8f}', f'C2={cl[2]:.8f}',
              f'C3={cl[3]:.8f}', 'uK units')
