#!/usr/bin/env python3
"""
THIRD-SEAT ADJUDICATION -- positivity of the monopole-subtracted Reading-B
primordial power spectrum.  Independent of both cutoffA_monopole.py (codex)
and cutoffA_monopole_agy.py (agy).

Construction under test
-----------------------
    W(r)    = (1-x)^2 (2+x) / 2 ,  x = r/chi_S ,  0 <= x <= 1 ; 0 otherwise
    xi(r)   = int dk/k Delta^2(k) sinc(kr) ,  Delta^2 = As (k/k0)^(ns-1)
    c       = int r^2 W xi dr / int r^2 W dr          (=> P_B(0) = 0 exactly)
    xi_B(r) = [xi(r) - c] W(r)
    P_B(k)  = 4 pi int_0^chi_S dr r^2 [xi(r) - c] W(r) sinc(kr)

Everything below is computed FROM THAT REAL-SPACE INTEGRAL.  No CAMB, no
S_1/2: the question adjudicated here is the SIGN of P_B.

Key exact reduction used throughout (validated numerically in STAGE 2)
---------------------------------------------------------------------
With Delta^2 a pure power law, the k_min -> 0 limit is available in closed
form.  Writing alpha = 1 - ns,

    xi(r; k_min) = As k0^alpha [ r^alpha * G  +  k_min^(-alpha)/alpha ] + O(k_min^ns)
    G            = Gamma(ns-2) sin(pi (ns-2)/2)          (analytic continuation)

The k_min-dependent piece is r-INDEPENDENT, so it is annihilated exactly by
the c subtraction.  Hence, with NO regulator at all,

    xi(r) - c = B ( r^alpha - m ),   B = As k0^alpha G ,
    m = < r^alpha >_mu ,   d mu = r^2 W(r) dr .

B < 0, so xi decreases with r, as it must.  This removes the IR regulator
from the problem entirely: the k_min -> 0 limit is exact, not extrapolated.
"""

import sys
import numpy as np
from scipy.special import spherical_jn
from scipy.integrate import quad, simpson
import mpmath as mp

np.seterr(all="raise")
mp.mp.dps = 30

# ----------------------------------------------------------------- constants
A = 14015.0                      # chi_S  [Mpc]
AS, NS, K0 = 2.1e-9, 0.9649, 0.05
ALPHA = 1.0 - NS                 # 0.0351
K_S = 2.0 * np.pi / A            # 4.4832e-4 /Mpc

G_CONT = float(mp.gamma(NS - 2) * mp.sin(mp.pi * (NS - 2) / 2))
B_AMP = AS * K0 ** ALPHA * G_CONT          # < 0


def Wfun(r, chi=A):
    """(1-x)^2 (2+x)/2 == 1 - 1.5 x + 0.5 x^3 , zero outside [0,chi]."""
    x = r / chi
    return np.where(x <= 1.0, 1.0 - 1.5 * x + 0.5 * x ** 3, 0.0)


def Wtilde_analytic(k, chi=A):
    """4 pi int r^2 W sinc(kr) dr for the overlap window of two radius-chi/2
    balls:  (pi chi^3 / 6) [3 j1(k chi/2)/(k chi/2)]^2 .  >= 0 by Bochner."""
    z = k * chi / 2.0
    f = np.where(z == 0.0, 1.0, 3.0 * spherical_jn(1, np.where(z == 0.0, 1.0, z)) / np.where(z == 0.0, 1.0, z))
    return (np.pi * chi ** 3 / 6.0) * f ** 2


def moment_poly(alpha, p, chi=A):
    """int_0^chi r^(p+alpha) W(r) dr  =  chi^(p+alpha+1) *
       [1/(p+alpha+1) - 1.5/(p+alpha+2) + 0.5/(p+alpha+4)]  (exact)."""
    s = p + alpha + 1.0
    return chi ** s * (1.0 / s - 1.5 / (s + 1.0) + 0.5 / (s + 3.0))


# ------------------------------------------------------------ GL machinery
def gl_grid(npan, nnode, a=0.0, b=A):
    xg, wg = np.polynomial.legendre.leggauss(nnode)
    edges = np.linspace(a, b, npan + 1)
    lo, hi = edges[:-1][:, None], edges[1:][:, None]
    half, mid = (hi - lo) / 2.0, (hi + lo) / 2.0
    return (mid + half * xg[None, :]).ravel(), (half * wg[None, :]).ravel()


def sph_transform(r, w, fvals, kgrid, chunk=200):
    """4 pi int r^2 f(r) sinc(k r) dr on the supplied quadrature."""
    g = w * r * r * fvals
    out = np.empty(kgrid.size, dtype=float)
    for i in range(0, kgrid.size, chunk):
        kk = kgrid[i:i + chunk][:, None]
        z = kk * r[None, :]
        out[i:i + chunk] = 4.0 * np.pi * ((np.sin(z) / z) * g[None, :]).sum(axis=1)
    return out


def P_LCDM(k):
    return 2.0 * np.pi ** 2 * AS * (k / K0) ** (NS - 1.0) / k ** 3


def hr(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ============================================================== STAGE 0
hr("STAGE 0 -- setup")
x = np.linspace(0.0, 1.0, 11)
print("window identity  max|(1-x)^2(2+x)/2 - (1-1.5x+0.5x^3)| = %.3e"
      % np.max(np.abs((1 - x) ** 2 * (2 + x) / 2 - (1 - 1.5 * x + 0.5 * x ** 3))))
print("chi_S = %.1f Mpc     k_S = 2pi/chi_S = %.9e /Mpc" % (A, K_S))
print("alpha = 1-ns = %.6f    G = Gamma(ns-2)sin(pi(ns-2)/2) = %.8f" % (ALPHA, G_CONT))
print("B = As k0^alpha G = %.10e   (B < 0  =>  xi decreasing in r)" % B_AMP)

I_a, I_0 = moment_poly(ALPHA, 2), moment_poly(0.0, 2)
M_MEAN = I_a / I_0                          # m = <r^alpha>_mu
print("int r^2 W dr        = %.10e  (exact chi^3/24 = %.10e)" % (I_0, A ** 3 / 24))
print("int r^2 W r^a dr    = %.10e" % I_a)
print("m = <r^alpha>_mu    = %.12f" % M_MEAN)

# ============================================================== STAGE 1
hr("STAGE 1 -- MACHINERY CONTROL A: numeric W~(k) vs its closed form (Bochner >= 0)")
rG, wG = gl_grid(3000, 16)
kctl = np.geomspace(1e-6, 2.0, 400)
Wt_num = sph_transform(rG, wG, Wfun(rG), kctl)
Wt_ana = Wtilde_analytic(kctl)
PEAK = np.pi * A ** 3 / 6.0                    # = W~(0), the scale of the problem
abserr = np.abs(Wt_num - Wt_ana)
rel = abserr / np.maximum(np.abs(Wt_ana), 1e-300)
jrel = int(np.argmax(rel))
zj = kctl[jrel] * A / 2.0
print("W~(0): numeric %.8e   analytic %.8e" %
      (sph_transform(rG, wG, Wfun(rG), np.array([1e-12]))[0], PEAK))
print("max ABSOLUTE error / W~(0)           : %.3e   <-- the meaningful metric" % (abserr.max() / PEAK))
print("min numeric W~(k)                    : %+.6e   (must be >= 0)" % Wt_num.min())
print("worst POINTWISE-RELATIVE error       : %.3e at k=%.6e (z=kA/2=%.1f, j1(z)=%.2e)"
      % (rel.max(), kctl[jrel], zj, float(spherical_jn(1, zj))))
print("   -- that k sits essentially ON a zero of W~ (W~ there = %.3e = %.1e of the peak)."
      % (Wt_ana[jrel], Wt_ana[jrel] / PEAK))
print("   Pointwise relative accuracy is unattainable at the exact zeros of W~ for ANY")
print("   double-precision real-space quadrature: the cancellation floor is ~1e-16*W~(0).")
print("   The control is therefore stated as absolute error relative to W~(0).")
CTRL_A = (abserr.max() / PEAK < 1e-12) and (Wt_num.min() >= 0.0)
print("CONTROL A: %s" % ("PASS" if CTRL_A else "FAIL"))

hr("STAGE 1b -- what window does codex's wtilde() actually implement?")
print("codex code:  z = s*A ;  wtilde = (4 pi A^3/3) [3 j1(z)/z]^2")
print("correct   :  z = s*A/2 ; W~     = (  pi A^3/6) [3 j1(z)/z]^2")
kk = np.geomspace(1e-6, 0.01, 6)
z_cod = kk * A
f_cod = 3.0 * spherical_jn(1, z_cod) / z_cod
wt_cod = (4.0 * np.pi * A ** 3 / 3.0) * f_cod ** 2
print("\n%14s %18s %18s %18s" % ("k [1/Mpc]", "codex wtilde", "W~ for chi=A", "W~ for chi=2A"))
for i in range(kk.size):
    print("%14.5e %18.9e %18.9e %18.9e"
          % (kk[i], wt_cod[i], Wtilde_analytic(kk[i], A), Wtilde_analytic(kk[i], 2 * A)))
print("\n=> codex's wtilde IS EXACTLY W~ for a window of support 2*chi_S = %.0f Mpc." % (2 * A))
# independent confirmation from codex's own reported c
m_codex = moment_poly(ALPHA, 2, 2 * A) / moment_poly(0.0, 2, 2 * A)
for kmin, c_rep in [(4.48318609e-10, 4.05905805e-08), (4.48318609e-09, 3.16890163e-08)]:
    c_pred_2A = AS * K0 ** ALPHA * (m_codex * G_CONT + kmin ** (-ALPHA) / ALPHA)
    c_pred_A = AS * K0 ** ALPHA * (M_MEAN * G_CONT + kmin ** (-ALPHA) / ALPHA)
    print("k_min=%.6e : codex c=%.8e | closed form chi=2A -> %.8e | chi=A -> %.8e"
          % (kmin, c_rep, c_pred_2A, c_pred_A))

# ============================================================== STAGE 2
hr("STAGE 2 -- CONTROL C: validate the closed-form xi against direct integration")


def E_series(a):
    """int_0^a u^(ns-3) (sin u - u) du , convergent series (|a| <~ 1)."""
    tot = 0.0 * a
    for coef, n in [(-1.0 / 6.0, 1), (1.0 / 120.0, 2), (-1.0 / 5040.0, 3), (1.0 / 362880.0, 4)]:
        p = NS + 2 * n - 1
        tot = tot + coef * a ** p / p
    return tot


def xi_closed(r, kmin):
    """EXACT xi(r) for Delta^2 = As (k/k0)^(ns-1), sharp IR cut at kmin, kmax=inf."""
    return AS * K0 ** ALPHA * (r ** ALPHA * (G_CONT - E_series(kmin * r)) + kmin ** (-ALPHA) / ALPHA)


def xi_mp(r, kmin):
    """Direct  As k0^a int_kmin^inf dk k^(ns-2) sinc(kr)  by mpmath, 40 digits."""
    r, kmin = mp.mpf(r), mp.mpf(kmin)
    f = lambda k: k ** (NS - 2) * mp.sin(k * r) / (k * r)
    pts, x = [kmin], kmin
    while x < mp.pi / r:
        x = x * 10
        pts.append(min(x, mp.pi / r))
    pts += [j * mp.pi / r for j in range(2, 121)]
    v = mp.quad(f, pts) + mp.quadosc(f, [120 * mp.pi / r, mp.inf], omega=float(r))
    return AS * K0 ** ALPHA * v


old_dps, mp.mp.dps = mp.mp.dps, 40
print("%9s %9s %24s %24s %12s" % ("r [Mpc]", "k_min", "mpmath direct integral", "closed form", "rel.err"))
ok2 = True
for r_ in [300.0, 3000.0, 7000.0, 14015.0]:
    for kmin_ in [1e-6, 1e-8]:
        num = float(xi_mp(r_, kmin_))
        ana = xi_closed(np.float64(r_), kmin_)
        e = abs(num - ana) / abs(ana)
        ok2 &= e < 1e-12
        print("%9.1f %9.0e %24.15e %24.15e %12.3e" % (r_, kmin_, num, ana, e))
mp.mp.dps = old_dps
print("=> xi(r) - c = B (r^alpha - m) exactly, with NO IR regulator, since the")
print("   k_min-dependent term k_min^(-alpha)/alpha is r-independent.")
print("CONTROL C: %s" % ("PASS" if ok2 else "FAIL"))

# ============================================================== STAGE 3
hr("STAGE 3 -- the zero-mode condition, checked exactly")
print("By construction  int r^2 W (xi - c) dr = B [ int r^2 W r^a dr - m int r^2 W dr ] = 0")
resid = B_AMP * (moment_poly(ALPHA, 2) - M_MEAN * moment_poly(0.0, 2))
print("analytic residual = %.6e   (relative to |B| int r^2 W r^a dr : %.3e)"
      % (resid, abs(resid) / abs(B_AMP * moment_poly(ALPHA, 2))))
c_at = lambda kmin: AS * K0 ** ALPHA * (M_MEAN * G_CONT + kmin ** (-ALPHA) / ALPHA)
print("\nc(k_min) for the CORRECT window chi_S = %.0f Mpc:" % A)
for kmin in [1e-4, 1e-5, 1e-6, 1e-7, 1e-8]:
    print("   k_min=%8.1e -> c = %.6e" % (kmin, c_at(kmin)))
print("   (agy reported c = 2.26e-09, 8.40e-09, 1.52e-08, 2.26e-08, 3.05e-08 -- compare)")

# ============================================================== STAGE 4
hr("STAGE 4 -- ANALYTIC CURVATURE AT k=0  (the decisive test)")
print("P_B(k) = 4pi int r^2 f(r) [1 - (kr)^2/6 + ...] dr  with f = (xi-c) W")
print("  P_B(0)   = 4pi int r^2 f dr = 0                    (imposed)")
print("  P_B'(0)  = 0                                       (P_B even in k)")
print("  P_B''(0) = -(4pi/3) M4 ,  M4 = int_0^chi r^4 (xi-c) W dr")
print("\nM4 = B [ int r^4 W r^a dr - m int r^4 W dr ] = B * chi^5 * D")
J_a = moment_poly(ALPHA, 4) / A ** (5 + ALPHA)
J_0 = moment_poly(0.0, 4) / A ** 5
D = A ** ALPHA * J_a - M_MEAN * J_0
print("  int_0^1 x^(4+a) W dx  = %.12f ,  chi^a * that = %.12f" % (J_a, A ** ALPHA * J_a))
print("  int_0^1 x^4     W dx  = %.12f ,  m * that     = %.12f  (= 1/80 * m)" % (J_0, M_MEAN * J_0))
print("  D = %.12e   (a %.3f%% cancellation)" % (D, 100 * D / (A ** ALPHA * J_a)))
M4 = B_AMP * A ** 5 * D
P2 = -(4.0 * np.pi / 3.0) * M4
print("  M4       = %.8e   (sign %s, because B<0 and D>0)" % (M4, "NEGATIVE" if M4 < 0 else "POSITIVE"))
print("  P_B''(0) = %.8e Mpc^5   -> %s" % (P2, "POSITIVE" if P2 > 0 else "NEGATIVE"))
print("\nInterpretation: D = Cov_mu(r^2, r^alpha) > 0 identically (both factors")
print("increase with r), and B < 0 because xi decreases with r.  Hence")
print("P_B''(0) > 0 for ANY chi_S and any ns < 1: P_B leaves k=0 UPWARD.")
print("P_B(k) ~ (1/2) P_B''(0) k^2 = %.6e * k^2 for k << k_S" % (0.5 * P2))
# numeric confirmation of M4
rN, wN = gl_grid(4000, 20)
fN = B_AMP * (rN ** ALPHA - M_MEAN) * Wfun(rN)
sc2 = np.sum(wN * rN ** 2 * np.abs(fN))
r2m = np.sum(wN * rN ** 2 * fN)
m4n = np.sum(wN * rN ** 4 * fN)
print("numeric  int r^2 (xi-c) W dr = %+.6e  (target 0; = %.2e of int r^2 |xi-c| W dr)"
      % (r2m, abs(r2m) / sc2))
print("numeric  M4 = int r^4 (xi-c) W dr = %.8e  (analytic %.8e ; rel.diff %.2e)"
      % (m4n, M4, abs(m4n - M4) / abs(M4)))

print("\nSTAGE 4b -- how general is this?  M4 = int d mu r^2 (xi - c) = Cov_mu(r^2, xi),")
print("because c = <xi>_mu.  xi is DECREASING in r, so Cov_mu(r^2, xi) < 0, so")
print("P_B''(0) = -(4pi/3) M4 > 0.  This needs no property of the window beyond")
print("W >= 0, and no property of the spectrum beyond a monotone xi.  Scan over ns:")
print("%10s %12s %14s %16s %16s" % ("ns", "alpha=1-ns", "B (sign)", "D (sign)", "P_B''(0)"))
for ns_try in [0.90, 0.9649, 0.99, 1.01, 1.05, 1.10]:
    a_ = 1.0 - ns_try
    G_ = float(mp.gamma(ns_try - 2) * mp.sin(mp.pi * (ns_try - 2) / 2))
    B_ = AS * K0 ** a_ * G_
    m_ = moment_poly(a_, 2) / moment_poly(0.0, 2)
    D_ = (moment_poly(a_, 4) - m_ * moment_poly(0.0, 4)) / A ** 5
    P2_ = -(4.0 * np.pi / 3.0) * B_ * A ** 5 * D_
    print("%10.4f %12.4f %14.4e %16.4e %16.6e %s"
          % (ns_try, a_, B_, D_, P2_, "POSITIVE" if P2_ > 0 else "NEGATIVE"))
print("B and D flip sign together at ns=1, so P_B''(0) > 0 on both sides.")

# ============================================================== STAGE 5
hr("STAGE 5 -- P_B(k) by direct real-space integration, with grid refinement")
KMIN_SCAN, KMAX_SCAN = 1e-9, 2.0
K_TINY = 1e-9

levels = [1, 2, 4, 8]
store = {}
print("refinement: level L uses 1500*L r-panels (x16 GL nodes) and 1000*L log-k points")
print("%5s %9s %7s %10s %17s %13s %9s %17s"
      % ("lev", "r-panels", "k-pts", "N_r nodes", "min P_B [Mpc^3]", "k at min", "#(P_B<0)",
         "min P_B/P_LCDM"))
print("%78s" % "(ratio min taken over k>=1e-3, where it is O(1))")
for lev in levels:
    npan, nk = 1500 * lev, 1000 * lev
    r, w = gl_grid(npan, 16)
    f = B_AMP * (r ** ALPHA - M_MEAN) * Wfun(r)
    kg = np.geomspace(KMIN_SCAN, KMAX_SCAN, nk)
    pb = sph_transform(r, w, f, kg)
    sel = kg >= 1e-3
    ratio = (pb[sel] / P_LCDM(kg[sel]))
    nneg = int(np.sum(pb < 0.0))
    j = int(np.argmin(pb))
    store[lev] = (kg, pb)
    print("%5d %9d %7d %10d %17.8e %13.5e %9d %17.8e"
          % (lev, npan, nk, r.size, pb[j], kg[j], nneg, ratio.min()))

print("\nSign structure at each level (the mandated stability test):")
for lev in levels:
    kg, pb = store[lev]
    sub = pb[kg >= 1e-6]
    print("  lev %d : min P_B over k>=1e-6 = %+.8e at k=%.5e ; ALL P_B > 0 ? %s"
          % (lev, sub.min(), kg[kg >= 1e-6][int(np.argmin(sub))], bool(np.all(pb > 0))))

print("\nDENSE LINEAR k scans (log grids can step over a narrow dip; these cannot).")
print("Oscillation scale of the window transform is 2pi/chi_S = %.3e /Mpc." % K_S)
rD, wD = gl_grid(9000, 16)
fD = B_AMP * (rD ** ALPHA - M_MEAN) * Wfun(rD)
dense_ok = True
for lo, hi, n in [(1e-5, 5e-3, 60000), (5e-3, 0.2, 40000), (0.2, 2.0, 30000), (2.0, 10.0, 20000)]:
    kd = np.linspace(lo, hi, n)
    pd = sph_transform(rD, wD, fD, kd)
    rr = pd / P_LCDM(kd)
    dense_ok &= bool(np.all(pd > 0))
    print("  k in [%7.1e, %5.2f]  dk=%.3e (%.1f pts per 2pi/chi_S) : min P_B=%+.6e  "
          "min P_B/P_LCDM=%.6f  #neg=%d"
          % (lo, hi, (hi - lo) / (n - 1), K_S / ((hi - lo) / (n - 1)), pd.min(), rr.min(),
             int(np.sum(pd < 0))))

# --- mandated zero-mode ratio -------------------------------------------
hr("STAGE 5b -- MANDATED ZERO-MODE CHECK   |P_B(k_tiny)| / P_B(k_S)  <  1e-3 ?")
r, w = gl_grid(6000, 16)
f = B_AMP * (r ** ALPHA - M_MEAN) * Wfun(r)
kprobe = np.array([1e-12, 1e-11, 1e-10, K_TINY, 1e-8, 1e-7, 1e-6, K_S])
pprobe = sph_transform(r, w, f, kprobe)
p_kS = pprobe[-1]
print("P_B(k_S = %.6e) = %.8e Mpc^3   (this is the reference scale)" % (K_S, p_kS))
print("%14s %20s %16s %22s" % ("k [1/Mpc]", "P_B(k) [Mpc^3]", "|P_B|/P_B(k_S)", "P_B/k^2 [Mpc^5]"))
for kk_, pp in zip(kprobe, pprobe):
    print("%14.4e %20.10e %16.4e %22.10e" % (kk_, pp, abs(pp) / p_kS, pp / kk_ ** 2))
ratio_tiny = abs(pprobe[3]) / p_kS
ZERO_MODE_OK = ratio_tiny < 1e-3
print("\nRATIO |P_B(%.0e)| / P_B(k_S) = %.4e   -- required < 1e-3 -> %s"
      % (K_TINY, ratio_tiny, "PASS" if ZERO_MODE_OK else "FAIL"))
print("NOTE, explicitly: P_B(k_tiny) IS the minimum of the curve on any grid")
print("that reaches down to k_tiny, because P_B(0)=0 is imposed and P_B rises")
print("from it.  That is expected, NOT a silent failure.  The content of the")
print("check is (i) the RATIO above, and (ii) that P_B/k^2 tends to the")
print("POSITIVE constant P_B''(0)/2 = %.6e, which it does." % (0.5 * P2))

# ============================================================== STAGE 6
hr("STAGE 6 -- MACHINERY CONTROL B: Bochner-guaranteed cases must come out >= 0")


rB, wB = gl_grid(6000, 16)
kB = np.geomspace(1e-7, 0.05, 1200)
print("B1: NO subtraction, sharp IR cut -- P_unsub(k) = 4pi int r^2 W xi dr must be >= 0")
ctrlB1 = True
for kmin in [1e-4, 1e-5, 1e-6]:
    xi = xi_closed(rB, kmin)
    pu = sph_transform(rB, wB, xi * Wfun(rB), kB)
    neg = int(np.sum(pu < 0.0))
    print("   k_min=%8.1e : min P_unsub = %+.8e  (peak %.6e, ratio %.2e) ; #neg=%d"
          % (kmin, pu.min(), pu.max(), pu.min() / pu.max(), neg))
    ctrlB1 &= (pu.min() >= -1e-12 * pu.max())
print("   -> %s" % ("PASS" if ctrlB1 else "FAIL"))

print("\nB2: delta-shell control -- xi_ctrl(r)=sinc(k_a r) is p.d.; W p.d.;")
print("    so 4pi int r^2 W sinc(k_a r) sinc(kr) dr must be >= 0 for every k.")
ctrlB2 = True
for ka in [3e-4, 1e-3, 5e-3]:
    z = ka * rB
    pc = sph_transform(rB, wB, np.sin(z) / z * Wfun(rB), kB)
    print("   k_a=%8.1e : min = %+.8e , max = %.6e , ratio = %+.2e"
          % (ka, pc.min(), pc.max(), pc.min() / pc.max()))
    ctrlB2 &= (pc.min() >= -1e-10 * pc.max())
print("   -> %s" % ("PASS" if ctrlB2 else "FAIL"))
CTRL_B = ctrlB1 and ctrlB2

# ============================================================== STAGE 7
hr("STAGE 7 -- independent high-accuracy reference (QAWO oscillatory quadrature)")
print("P_B(k) = (4 pi B / k) int_0^chi r W(r) (r^a - m) sin(kr) dr, via scipy QAWO")
gfun = lambda rr: rr * Wfun(np.array([rr]))[0] * (rr ** ALPHA - M_MEAN)
print("%14s %22s %22s %12s" % ("k [1/Mpc]", "P_B (QAWO)", "P_B (GL lev4)", "rel.diff"))
kref = np.array([1e-6, 1e-5, 1e-4, K_S, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0, 2.0])
r8, w8 = gl_grid(12000, 16)
f8 = B_AMP * (r8 ** ALPHA - M_MEAN) * Wfun(r8)
p_gl = sph_transform(r8, w8, f8, kref)
qawo_ok = True
p_qawo = np.empty_like(kref)
for i, k in enumerate(kref):
    val, err = quad(gfun, 0.0, A, weight="sin", wvar=k, limit=800, maxp1=200, epsabs=0.0, epsrel=1e-11)
    p_qawo[i] = 4.0 * np.pi * B_AMP * val / k
    d = abs(p_qawo[i] - p_gl[i]) / abs(p_qawo[i])
    qawo_ok &= d < 1e-6
    print("%14.5e %22.12e %22.12e %12.3e" % (k, p_qawo[i], p_gl[i], d))
print("all QAWO values positive ? %s" % bool(np.all(p_qawo > 0)))
print("agreement with composite GL: %s" % ("PASS" if qawo_ok else "FAIL"))

print("\nHigh-k physical check: P_B(k)/P_LCDM(k) must -> 1 with no hand-applied splice")
for k in [1e-2, 3e-2, 0.1, 0.3, 1.0, 2.0]:
    pv = 4.0 * np.pi * B_AMP * quad(gfun, 0.0, A, weight="sin", wvar=k, limit=800,
                                    maxp1=200, epsabs=0.0, epsrel=1e-11)[0] / k
    print("   k=%7.3f : P_B=%.6e  P_LCDM=%.6e  ratio=%.6f" % (k, pv, P_LCDM(k), pv / P_LCDM(k)))

# ============================================================== STAGE 8
hr("STAGE 8 -- diagnosis: reproduce agy's numerical scheme and locate his minimum")
print("agy: r = linspace(1e-5, chi_S, 20000) [linear, dr = %.3f Mpc], Simpson;" % (A / 19999))
print("     k_out = geomspace(1e-7, 2.0, 2000).  Half-period of sin(kr) at k=2 is")
print("     pi/2 = 1.571 Mpc -> only %.2f Simpson points per HALF period." % ((A / 19999) ** -1 * np.pi / 2))
r_agy = np.linspace(1e-5, A, 20000)
f_agy = B_AMP * (r_agy ** ALPHA - M_MEAN) * Wfun(r_agy)   # exact xi-c, so ONLY the
                                                          # r->k transform differs
k_out = np.geomspace(1e-7, 2.0, 2000)
P_agy = np.empty_like(k_out)
for i in range(0, k_out.size, 100):
    kk = k_out[i:i + 100][:, None]
    z = kk * r_agy[None, :]
    P_agy[i:i + 100] = 4.0 * np.pi * simpson(r_agy ** 2 * f_agy[None, :] * np.sin(z) / z, x=r_agy, axis=1)
r_ref, w_ref = gl_grid(24000, 16)
f_ref = B_AMP * (r_ref ** ALPHA - M_MEAN) * Wfun(r_ref)
P_ref = sph_transform(r_ref, w_ref, f_ref, k_out)
jm = int(np.argmin(P_agy))
print("\nOn agy's own grid (with an EXACT xi-c, so the only defect is the transform):")
print("   min P_B = %+.6e at k = %.6e   ; #(P_B<0) = %d of %d"
      % (P_agy[jm], k_out[jm], int(np.sum(P_agy < 0)), k_out.size))
print("   converged value at that same k = %+.6e" % P_ref[jm])
print("   first k where agy's grid goes negative: %.6e"
      % (k_out[P_agy < 0][0] if np.any(P_agy < 0) else float("nan")))
print("   converged min over the same k range   = %+.6e at k=%.6e"
      % (P_ref.min(), k_out[int(np.argmin(P_ref))]))
band = k_out > 0.05
print("   max |agy - converged| for k > 0.05    = %.6e  (scale P_LCDM(2)=%.3e)"
      % (np.max(np.abs(P_agy[band] - P_ref[band])), P_LCDM(2.0)))
band2 = k_out < 0.01
print("   max |agy - converged| for k < 0.01    = %.6e" % np.max(np.abs(P_agy[band2] - P_ref[band2])))
print("   => his r->k Simpson transform alone does NOT produce negatives.")

print("\n8b -- now also reproduce agy's xi QUADRATURE (his q-grid), the remaining difference")
print("     agy: q = geomspace(k_min, 20, 20000), Simpson in q (not in ln q).")
print("     At q=20 the step is dq=%.4f, so d(q r)=%.0f radians per Simpson step at r=chi_S."
      % (20.0 * (np.log(20.0 / 1e-7) / 19999), 20.0 * (np.log(20.0 / 1e-7) / 19999) * A))
for kmin_agy in [1e-6, 1e-7, 1e-8]:
    q = np.geomspace(kmin_agy, 20.0, 20000)
    d2 = AS * (q / K0) ** (NS - 1.0)
    xi_a = np.empty_like(r_agy)
    for i in range(0, r_agy.size, 1000):
        rr = r_agy[i:i + 1000][None, :]
        z = q[:, None] * rr
        xi_a[i:i + 1000] = simpson((d2[:, None] / q[:, None]) * (np.sin(z) / z), x=q, axis=0)
    Wr = Wfun(r_agy)
    c_a = simpson(r_agy ** 2 * Wr * xi_a, x=r_agy) / simpson(r_agy ** 2 * Wr, x=r_agy)
    fa = (xi_a - c_a) * Wr
    Pa = np.empty_like(k_out)
    for i in range(0, k_out.size, 100):
        kk = k_out[i:i + 100][:, None]
        z = kk * r_agy[None, :]
        Pa[i:i + 100] = 4.0 * np.pi * simpson(r_agy ** 2 * fa[None, :] * np.sin(z) / z, x=r_agy, axis=1)
    ja = int(np.argmin(Pa))
    xi_ex = xi_closed(r_agy, kmin_agy)
    print("  k_min=%7.1e : c_agy=%.6e (exact %.6e, rel %.2e) ; max|xi_agy-xi_exact|=%.3e"
          % (kmin_agy, c_a, c_at(kmin_agy), abs(c_a - c_at(kmin_agy)) / c_at(kmin_agy),
             np.max(np.abs(xi_a - xi_ex))))
    print("               min P_B = %+.6e at k=%.6e ; #neg=%d ; first neg k=%s"
          % (Pa[ja], k_out[ja], int(np.sum(Pa < 0)),
             ("%.4e" % k_out[Pa < 0][0]) if np.any(Pa < 0) else "none"))
    print("               converged P_B at that k = %+.6e ; |agy-conv| there = %.3e"
          % (P_ref[ja], abs(Pa[ja] - P_ref[ja])))
    if abs(kmin_agy - 1e-7) < 1e-12:
        xi_keep, fa_keep = xi_a.copy(), fa.copy()

print("\n8c -- ATTRIBUTION: swap agy's two numerical stages in and out, k in [1.0, 2.0]")
print("     (his reported minimum, -2.77e-09, lives in exactly this band)")
sel = (r_agy > 100.0)
print("     his xi is accurate to %.2e absolute for r>100 Mpc (xi itself ~ %.2e);"
      % (np.max(np.abs(xi_keep[sel] - xi_closed(r_agy[sel], 1e-7))), xi_keep[sel].mean()))
print("     the whole 1.3e-08 headline error sits at his first node r=1e-05 Mpc and is")
print("     just his k_max=20 UV truncation, which the r^2 measure makes irrelevant.")
kk_att = np.linspace(1.0, 2.0, 401)
rA, wA = gl_grid(9000, 16)
fA_interp = np.interp(rA, r_agy, fa_keep)
fA_exact = B_AMP * (rA ** ALPHA - M_MEAN) * Wfun(rA)
P_i = np.empty_like(kk_att)
for i in range(0, kk_att.size, 100):
    kc = kk_att[i:i + 100][:, None]
    z = kc * r_agy[None, :]
    P_i[i:i + 100] = 4.0 * np.pi * simpson(r_agy ** 2 * fa_keep[None, :] * np.sin(z) / z, x=r_agy, axis=1)
P_ii = sph_transform(rA, wA, fA_interp, kk_att)
P_iii = sph_transform(rA, wA, fA_exact, kk_att)
print("  (i)   agy xi + agy Simpson r->k    : min = %+.6e   #neg = %3d" % (P_i.min(), int((P_i < 0).sum())))
print("  (ii)  agy xi + converged r->k      : min = %+.6e   #neg = %3d" % (P_ii.min(), int((P_ii < 0).sum())))
print("  (iii) exact xi + converged r->k    : min = %+.6e   #neg = %3d" % (P_iii.min(), int((P_iii < 0).sum())))
jj = int(np.argmin(P_i))
print("  at k = %.4f : (i) %+.6e   (ii) %+.6e   (iii) %+.6e"
      % (kk_att[jj], P_i[jj], P_ii[jj], P_iii[jj]))
print("  => BOTH of agy's numerical stages push P_B down; neither is physics.")

# ============================================================== VERDICT
hr("SUMMARY")
signs_stable = all(bool(np.all(store[lev][1] > 0)) for lev in levels)
mins = [store[lev][1].min() for lev in levels]
print("CONTROL A (W~ closed form)          : %s" % ("PASS" if CTRL_A else "FAIL"))
print("CONTROL C (xi power-law reduction)  : %s" % ("PASS" if ok2 else "FAIL"))
print("DENSE LINEAR k scans all positive   : %s" % ("PASS" if dense_ok else "FAIL"))
print("CONTROL B (Bochner positive cases)  : %s" % ("PASS" if CTRL_B else "FAIL"))
print("CONTROL QAWO (independent quadrature): %s" % ("PASS" if qawo_ok else "FAIL"))
print("ZERO-MODE ratio < 1e-3              : %s (%.3e)" % ("PASS" if ZERO_MODE_OK else "FAIL", ratio_tiny))
print("SIGN STABLE under 1x/2x/4x/8x       : %s" % ("PASS" if signs_stable else "FAIL"))
print("min P_B per level                   : " + ", ".join("%.4e" % v for v in mins))
print("P_B''(0)                            : %+.6e Mpc^5 (%s)" % (P2, "POSITIVE" if P2 > 0 else "NEGATIVE"))
allok = CTRL_A and ok2 and CTRL_B and qawo_ok and ZERO_MODE_OK
if not allok:
    print("\nVERDICT TOKEN: CHECK_FAILED")
elif not signs_stable:
    print("\nVERDICT TOKEN: UNDECIDED_AT_THIS_PRECISION")
elif dense_ok and P2 > 0:
    print("\nVERDICT TOKEN: POSITIVITY_HOLDS")
else:
    print("\nVERDICT TOKEN: POSITIVITY_FAILS")
