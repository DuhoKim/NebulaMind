#!/usr/bin/env python3
"""Program (C) numeric control (eval-what-you-print).
Question: for a spherically symmetric window W about the observer, does the linear functional
delta_S = int W(x) delta(x) d^3x correlate with the l>=1 multipoles of the field on a shell?
Setup: Gaussian field with a smooth P(k) (toy: P ~ k^n_s-ish damped), shell radius r_*, window
top-hat radius R. Cross-correlation <delta_S a_lm> is computed two ways:
 (i) analytic in k-space: <delta_S a_lm> = delta_{l0} delta_{m0} * sqrt(4 pi) * int dk k^2/(2 pi^2) P(k) Wt(k) j_0(k r_*)
 (ii) Monte Carlo: synthesize real-space Gaussian fields on a grid, evaluate delta_S and a_lm on the shell, average.
Control passes if MC gives |corr| >> 0 for l=0 and consistent with 0 (within MC error) for l=1,2, AND the l=0 value matches (i).
F2 control: Wt(k) = 3 j1(kR)/(kR) has isolated zeros; int P |Wt|^2 k^2 dk > 0 for any P>0."""
import numpy as np
from scipy.special import spherical_jn, sph_harm
from scipy.optimize import brentq
rng = np.random.default_rng(20260902)
N = 64; Lbox = 8.0; R = 1.0; rstar = 0.6           # box units; window radius R; shell radius r_* < R
dx = Lbox/N; kf = 2*np.pi/Lbox
kx = np.fft.fftfreq(N, d=dx)*2*np.pi; KX,KY,KZ = np.meshgrid(kx,kx,kx, indexing='ij'); K = np.sqrt(KX**2+KY**2+KZ**2)
def P(k):
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(k>0, np.exp(-(k/6.0)**2)/np.where(k>0,k,1.0), 0.0)   # smooth, positive for k>0
Wt = lambda k: np.where(k>0, 3*spherical_jn(1,k*R)/(k*R+1e-300), 1.0)
# shell sampling points (Fibonacci sphere) and window grid
npts = 400; i = np.arange(npts)+0.5; th = np.arccos(1-2*i/npts); ph = (np.pi*(1+5**0.5))*i
pts = rstar*np.stack([np.sin(th)*np.cos(ph), np.sin(th)*np.sin(ph), np.cos(th)],1)
X = (np.arange(N)*dx - Lbox/2); XX,YY,ZZ = np.meshgrid(X,X,X, indexing='ij'); Rg = np.sqrt(XX**2+YY**2+ZZ**2)
Wgrid = (Rg<=R).astype(float)
def field():
    # delta_k = sqrt(P V) * complex normal/sqrt2 ; delta_x = ifftn(delta_k) * N^3 / V  -> <delta_x^2> = int d3k/(2pi)^3 P
    V = Lbox**3; amp = np.sqrt(P(K)*V); phase = (rng.normal(size=K.shape)+1j*rng.normal(size=K.shape))/np.sqrt(2)
    return np.fft.ifftn(amp*phase).real*np.sqrt(2)*N**3/V     # .real of a complex Gaussian halves the variance; sqrt2 restores it
def alm(fvals, l, m):
    Y = sph_harm(m, l, ph, th); return np.sum(fvals*np.conj(Y))*(4*np.pi/npts)
nmc = 400; acc = {}; dS_all=[]
from scipy.interpolate import RegularGridInterpolator
for it in range(nmc):
    f = field(); dS = np.sum(f*Wgrid)*dx**3
    interp = RegularGridInterpolator((X,X,X), f, method='linear')
    fv = interp(pts)
    for (l,m) in [(0,0),(1,0),(1,1),(2,0),(2,1),(2,2)]:
        acc.setdefault((l,m),[]).append(dS*alm(fv,l,m))
    dS_all.append(dS)
print(f"MC realisations: {nmc}; sigma(delta_S) = {np.std(dS_all):.4g}")
for key,v in acc.items():
    v=np.array(v); print(f"  <delta_S a_{key[0]}{key[1]}>  = {v.mean().real:+.4g}  +- {v.std().real/np.sqrt(nmc):.4g}   (|mean|/err = {abs(v.mean())/ (v.std()/np.sqrt(nmc)+1e-300):.2f})")
# analytic l=0 cross term from P(k)
kk = np.linspace(kf/4, 30, 200000); dk = kk[1]-kk[0]
c00 = np.sqrt(4*np.pi)*np.sum(kk**2/(2*np.pi**2)*P(kk)*Wt(kk)*spherical_jn(0,kk*rstar))*dk*(4*np.pi*R**3/3)
print(f"analytic <delta_S a_00> (continuum, top-hat window volume factor) = {c00:+.4g}")
# F2 control: zeros of Wt and positivity of the constrained variance
z = [brentq(lambda k: spherical_jn(1,k), a, b) for a,b in [(3.5,5.5),(6.5,8.5)]]
print(f"F2: first two positive zeros of Wt(k) at kR = {z[0]:.4f}, {z[1]:.4f} (isolated; Wt entire in k by Paley-Wiener)")
var = np.sum(kk**2/(2*np.pi**2)*P(kk)*Wt(kk)**2)*dk
print(f"F2: int P |Wt|^2 k^2 dk/(2pi^2) = {var:.4g} > 0  -> <(W*delta)^2> cannot vanish for a positive P")
