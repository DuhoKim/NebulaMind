#!/usr/bin/env python3
"""
Cycle-2 / Goru M3: SFE benchmark for paper #4 (TNG massive-galaxy abundance).
Abundance-match the observed z=5 cumulative number density to a Sheth-Tormen HMF
-> M_halo; compute epsilon = M*/(f_b M_halo) with/without the 0.28 dex shift;
report the upward mass shift (dex) at which epsilon breaches the LCDM ceiling (=1).
Self-contained: EH98 no-wiggle transfer function + ST mass function.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

# --- Planck2015-ish cosmology (matches paper's f_b=0.157 = Ob/Om) ---
Om, Ob, h, ns, sig8 = 0.3089, 0.0486, 0.6774, 0.9667, 0.8159
fb = Ob/Om
rho_m = 2.775e11 * Om * h*h   # Msun / Mpc^3 (comoving), mean matter density
delta_c = 1.686

# --- Eisenstein & Hu 1998 "no-wiggle" transfer function ---
theta = 2.728/2.7
Obh2, Omh2 = Ob*h*h, Om*h*h
s = 44.5*np.log(9.83/Omh2)/np.sqrt(1+10*Obh2**0.75)      # sound horizon (Mpc)
alpha_gamma = 1 - 0.328*np.log(431*Omh2)*Ob/Om + 0.38*np.log(22.3*Omh2)*(Ob/Om)**2
def T_nw(k):   # k in 1/Mpc
    ks = k*s
    gamma_eff = Om*h*(alpha_gamma + (1-alpha_gamma)/(1+(0.43*ks)**4))
    q = k/h * theta**2 / gamma_eff
    L = np.log(2*np.e + 1.8*q)
    C = 14.2 + 731.0/(1+62.5*q)
    return L/(L + C*q*q)

def Pk_unnorm(k):
    return k**ns * T_nw(k)**2

# top-hat window
def W(k,R):
    x = k*R
    return 3*(np.sin(x)-x*np.cos(x))/x**3

def sigma2(R, norm=1.0):
    def integ(lk):
        k = np.exp(lk)
        return k**3 * Pk_unnorm(k) * W(k,R)**2 / (2*np.pi**2)
    val,_ = quad(integ, np.log(1e-4), np.log(1e3), limit=200)
    return norm*val

# normalize to sigma8 (R=8/h Mpc)
R8 = 8.0/h
norm = sig8**2 / sigma2(R8, 1.0)

def sigmaM(M):  # M in Msun (comoving)
    R = (3*M/(4*np.pi*rho_m))**(1/3.)
    return np.sqrt(sigma2(R, norm))

# growth factor D(z), normalized D(0)=1 (matter+Lambda)
def Dz(z):
    def E(zz): return np.sqrt(Om*(1+zz)**3 + (1-Om))
    def integ(zz): return (1+zz)/E(zz)**3
    g,_ = quad(integ, z, np.inf, limit=200)
    g0,_ = quad(integ, 0, np.inf, limit=200)
    return (E(z)*g)/(1.0*g0) * 1.0   # unnormalized ratio below
def growth(z):
    def E(zz): return np.sqrt(Om*(1+zz)**3 + (1-Om))
    def integ(zz): return (1+zz)/E(zz)**3
    num,_ = quad(integ, z, np.inf, limit=200)
    den,_ = quad(integ, 0, np.inf, limit=200)
    return (E(z)*num)/(E(0)*den)

# Sheth-Tormen dn/dlnM
A_ST,a_ST,p_ST = 0.3222, 0.707, 0.3
def dn_dlnM(M,z):
    D = growth(z)
    sig = sigmaM(M)*D
    nu = delta_c/sig
    # d ln sigma / d ln M
    dM = M*0.01
    dlnsig = (np.log(sigmaM(M+dM))-np.log(sigmaM(M-dM)))/(np.log(M+dM)-np.log(M-dM))
    nu2 = a_ST*nu*nu
    f = A_ST*np.sqrt(2*a_ST/np.pi)*(1+nu2**-p_ST)*nu*np.exp(-nu2/2)
    return (rho_m/M) * f * (-dlnsig)   # dn/dlnM in Mpc^-3

def n_gt(Mmin,z):
    val,_ = quad(lambda lm: dn_dlnM(np.exp(lm),z), np.log(Mmin), np.log(1e15), limit=200)
    return val

# --- abundance match: find M_halo st n(>M_halo,z=5)=n_obs ---
z = 5.0
n_obs = 3e-5   # Mpc^-3 (Weibel+2024, comoving, no-h)
Mh = brentq(lambda lm: np.log(n_gt(np.exp(lm),z)) - np.log(n_obs), np.log(1e10), np.log(5e13))
Mh = np.exp(Mh)

Mstar = 10**10.5
eps_un = Mstar/(fb*Mh)
eps_sh = (10**(10.5-0.28))/(fb*Mh)
# upward shift to reach eps=1:
shift_falsif = np.log10(1.0/eps_un)   # dex UPWARD from reported 10^10.5

print("=== cosmology ===")
print(f"Om={Om} Ob={Ob} h={h} f_b={fb:.4f} sigma8={sig8}")
print(f"sanity: n(>1e11,z=5)={n_gt(1e11,z):.3e}  n(>1e12,z=5)={n_gt(1e12,z):.3e} Mpc^-3")
print("=== abundance match (z=5, n_obs=3e-5 Mpc^-3) ===")
print(f"M_halo = {Mh:.3e} Msun  (log10 = {np.log10(Mh):.3f})")
print(f"f_b*M_halo = {fb*Mh:.3e} Msun (log10={np.log10(fb*Mh):.3f})  = max baryon budget")
print("=== epsilon = M*/(f_b M_halo), 1:1 match (MAX epsilon) ===")
print(f"eps_unshifted (M*=10^10.50) = {eps_un:.3f}")
print(f"eps_shifted   (M*=10^10.22) = {eps_sh:.3f}")
print("=== falsification threshold ===")
print(f"upward M* shift to breach eps=1 (LCDM hard bound): +{shift_falsif:.3f} dex")
print(f"  -> reported masses would need to be {shift_falsif:.2f} dex HIGHER than 10^10.5 for LCDM to break")
# also: how far below eps=0.2 realistic expectation?
print(f"eps_unshifted vs realistic eps~0.2: ratio = {eps_un/0.2:.2f}")
