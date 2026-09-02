#!/usr/bin/env python3
"""Program A: Reading B S_1/2 computation with monopole subtraction
Constructs the real-space regulated primordial field and computes S_1/2.
"""
import numpy as np
from scipy.integrate import simpson
import camb
from camb import initialpower
from scipy.special import eval_legendre
from numpy.polynomial.legendre import leggauss

# Cosmological parameters (Planck-like)
H0 = 67.36
ombh2 = 0.02237
omch2 = 0.1200
tau = 0.0544
As = 2.1e-9
ns = 0.9649
mnu = 0.06
KP = 0.05
L = 3.149 * 299792.458 / H0

def s12_matrix(l_max):
    n_nodes = l_max + 2
    x_std, w_std = leggauss(n_nodes)
    a, b = -1.0, 0.5
    x = 0.5 * (b - a) * x_std + 0.5 * (b + a)
    w = 0.5 * (b - a) * w_std
    P = np.zeros((l_max + 1, len(x)))
    for l in range(l_max + 1):
        c = np.zeros(l + 1)
        c[l] = 1.0
        P[l] = np.polynomial.legendre.legval(x, c)
    I = (P * w) @ P.T
    l = np.arange(l_max + 1)
    pref = (2 * l + 1) / (4 * np.pi)
    M = np.outer(pref, pref) * I
    return M

def s12_from_cl(cl, M):
    return float(cl @ M @ cl)

def get_S12(k_arr, P_arr):
    p = camb.CAMBparams()
    p.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=mnu, omk=0, tau=tau)
    p.set_for_lmax(300, lens_potential_accuracy=0)
    p.WantTensors = False
    p.DoLensing = False
    p.NonLinear = camb.model.NonLinear_none
    
    ip = initialpower.SplinedInitialPower()
    ip.set_scalar_table(k_arr, P_arr)
    ip.effective_ns_for_nonlinear = ns
    p.InitPower = ip
    
    p.Accuracy.AccuracyBoost = 1
    p.Accuracy.lAccuracyBoost = 1
    p.Accuracy.lSampleBoost = 1

    res = camb.get_results(p)
    cl = res.get_unlensed_scalar_cls(CMB_unit='muK', raw_cl=True, lmax=300)[:,0]
    M = s12_matrix(300)
    cl_work = cl.copy()
    if len(cl_work) > 0: cl_work[0] = 0
    if len(cl_work) > 1: cl_work[1] = 0
    return s12_from_cl(cl_work, M)

def j0(x):
    return np.sinc(x / np.pi)

def main():
    print("="*70)
    print("PROGRAM A2: MONOPOLE SUBTRACTED READING B")
    print("="*70)
    
    # High-resolution r-grid to avoid integration aliasing
    k_max_int = 20.0
    r_grid = np.linspace(1e-5, L, 20000)
    x = r_grid / L
    W = (1 - x)**2 * (2 + x) / 2
    norm_W = simpson(r_grid**2 * W, x=r_grid)
    
    k_out = np.geomspace(1e-7, 2.0, 2000)
    k_S = 2 * np.pi / L
    
    print(f"\nk_S (cutoff scale) = {k_S:.2e} Mpc^-1")
    
    k_mins = [1e-4, 1e-5, 1e-6, 1e-7, 1e-8]
    
    print("\n[1] k_min SENSITIVITY TABLE")
    print(f"{'k_min (Mpc^-1)':<15} | {'S_1/2 (uK^4)':<15} | {'c (Monopole)':<15} | {'Min P_B':<15}")
    print("-" * 65)
    
    results = {}
    for k_min in k_mins:
        q_grid = np.geomspace(k_min, k_max_int, 20000)
        Delta2 = As * (q_grid / KP)**(ns - 1)
        
        q_2d = q_grid[:, None]
        r_2d = r_grid[None, :]
        integrand = (Delta2[:, None] / q_2d) * j0(q_2d * r_2d)
        xi_LCDM = simpson(integrand, x=q_grid, axis=0)
        
        c_monopole = simpson(r_grid**2 * W * xi_LCDM, x=r_grid) / norm_W
        xi_B = (xi_LCDM - c_monopole) * W
        
        k_2d = k_out[:, None]
        r_2d_k = r_grid[None, :]
        integrand_k = r_2d_k**2 * xi_B[None, :] * j0(k_2d * r_2d_k)
        P_raw = 4 * np.pi * simpson(integrand_k, x=r_grid, axis=1)
        
        Delta2_B = (k_out**3 / (2 * np.pi**2)) * P_raw
        
        min_P = np.min(P_raw)
        
        Delta2_B = np.maximum(Delta2_B, 1e-30 * As)
        
        # Splice precisely to LCDM at k=0.1 to avoid very high-k numerical integration artifacts
        idx_splice = np.searchsorted(k_out, 0.1)
        Delta2_B[idx_splice:] = As * (k_out[idx_splice:] / KP)**(ns - 1)
        
        s12 = get_S12(k_out, Delta2_B)
        results[k_min] = s12
        
        print(f"{k_min:<15.1e} | {s12:<15.1f} | {c_monopole:<15.2e} | {min_P:<15.2e}")

    s12_subtracted = results[1e-8]
    
    print("\n[2] COMPARISON & CONCLUSION")
    print(f"LCDM (unlensed) : 34,924 uK^4")
    print(f"Reading A       : 6,897 uK^4")
    print(f"Reading B (subtracted) : {s12_subtracted:,.0f} uK^4 (at k_min=1e-8)")
    print(f"Observed        : ~1,150 uK^4")

if __name__ == '__main__':
    main()
