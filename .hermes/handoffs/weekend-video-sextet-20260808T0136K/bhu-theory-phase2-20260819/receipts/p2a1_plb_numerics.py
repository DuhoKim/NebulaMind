"""R-P2A1-2: independent recomputation of EVERY number in PLB 694,181 (arXiv:1007.0587).
Constants: SI-exact (hbar, c, eV since 2019 redefinition); G = 6.67430e-11 (CODATA 2018, same
value used in the gate-passed Phase 1 receipts). Paper inputs (its own quoted values):
H0^-1 = 4.4e17 s, Omega = 1.002, Omega_R = 8.8e-5, n_nu = 5.6e7 m^-3 per type, 6 types."""
import math
hbar = 1.054571817e-34   # J s (SI exact via h)
c    = 2.99792458e8      # m/s (exact)
G    = 6.67430e-11       # m^3 kg^-1 s^-2 (CODATA 2018)
kappa = 8*math.pi*G/c**4
H0 = 1/4.4e17
Om, OR = 1.002, 8.8e-5
n1, ntypes = 5.6e7, 6
eps_c = 3*H0**2*c**2/(8*math.pi*G)
print(f"eps_c = {eps_c:.4e} J/m^3")
a0 = c/(H0*math.sqrt(Om-1))
print(f"a0 = {a0:.3e} m   (paper: 2.9e27)")
# Omega_S two ways
def OmS(n): return -(kappa/4)*((hbar*c*n)**2/8)/eps_c
OmS_tot  = OmS(n1*ntypes)          # all six species summed INSIDE the square
OmS_sum6 = ntypes*OmS(n1)          # six incoherent species, s^2 additive
print(f"Omega_S (n_total coherent) = {OmS_tot:.3e}   (paper: -8.6e-70)")
print(f"Omega_S (6 species incoherent) = {OmS_sum6:.3e}   (factor {OmS_tot/OmS_sum6:.2f} smaller in |.|)")
OS = OmS_tot   # use the paper's own value hereafter to test internal consistency
OSp = -8.6e-70 # paper's printed value
for name, OSv in [("recomputed", OS), ("paper-printed", OSp)]:
    am_hat = math.sqrt(-OSv/OR)
    print(f"[{name} OS={OSv:.2e}]  a_m^ = {am_hat:.3e} (paper 3.1e-33);  a_m = {am_hat*a0:.2e} m (paper 9e-6)")
# remaining numbers with the paper's printed OS = -8.6e-70 (internal-consistency test)
OSv = OSp
am_hat = math.sqrt(-OSv/OR)
dev = -4*OSv*(Om-1)/OR**2     # Omega(sqrt2 a_m) - 1, computed without catastrophic float cancellation
print(f"Omega(sqrt2 a_m)-1 = {dev:.3e}   (paper: 8.9e-64)")
f_sqrt2 = math.sqrt(2)/2*1 + 0.5*math.log(math.sqrt(2)+1)
t = -OSv/(OR**1.5*H0)*f_sqrt2
print(f"t(sqrt2 a_m) = {t:.3e} s   (paper: 5.3e-46)")
va = math.pi*OR/(2*math.sqrt(-OSv*(Om-1)))
print(f"v_a/c = {va:.3e}   (paper: 1.1e32);  N = (v_a/c)^3 = {va**3:.2e} (paper ~1e96)")
epsR_am = OR*eps_c*am_hat**-4
print(f"eps_R(a_m) = {epsR_am:.3e} J/m^3   (paper: 1.1e116)  <-- ratio {epsR_am/1.1e116:.2f}")
eps_Planck = c**7/(hbar*G**2)
print(f"Planck energy density = {eps_Planck:.3e} J/m^3; eps_R(a_m)/eps_P = {epsR_am/eps_Planck:.1f}")
# consistency of Omega(min)-1 with v_a:  Omega-1 = pi^2 c^2/v_a^2
print(f"pi^2/(v_a)^2 = {math.pi**2/va**2:.3e}  vs Omega(min)-1 = {dev:.3e}  -> consistent:",
      abs(math.pi**2/va**2/dev - 1) < 0.02)
