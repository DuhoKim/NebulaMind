"""R-P2A1-4: independent recomputation of PRD 85,107502's worked numbers.
Constants: SI-exact hbar, c, eV; G = 6.67430e-11 (CODATA 2018; same as Phase 1 receipts).
Paper inputs (its own): g_b=28, g_f=90; T_r = T_eq = 0.75 eV; a_0 = 2.9e27 m; z_eq = 3200."""
import math
hbar, c, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
eV = 1.602176634e-19    # J (SI exact)
hbar_c = hbar*c         # J m
mP_red_J = math.sqrt(hbar*c**5/(8*math.pi*G))   # reduced Planck ENERGY in J
print(f"reduced Planck energy = {mP_red_J/eV/1e9:.4e} GeV")
zeta3 = 1.2020569031595943
g_b, g_f = 28, 90
g_star = g_b + 7/8*g_f
g_n = 3/4*g_f
h_s = math.pi**2/30*g_star
h_n = zeta3/math.pi**2*g_n
print(f"g_star = {g_star}, g_n = {g_n}, h_star = {h_s:.4f}, h_n = {h_n:.4f}")
# T_cr = sqrt(2 hs/(3 alpha hn^2)), alpha = 9/(16 mP^2) in natural units -> T_cr in units of mP
Tcr_over_mP = math.sqrt(2*h_s*16/(3*9*h_n**2))
print(f"T_cr = {Tcr_over_mP:.3f} m_P   (paper: 0.78)")
# a_cr = ar Tr sqrt(e)/T_cr   [receipt p2a1_prd_symbolic (c): a_cr = ar Tr sqrt(3 e alpha hn^2/2hs)]
a0, zeq, Tr_eV = 2.9e27, 3200, 0.75
ar = a0/(1+zeq)
Tr_per_m = Tr_eV*eV/hbar_c          # T_r in inverse meters (natural units)
Tcr_per_m = Tcr_over_mP*mP_red_J/hbar_c
a_cr = ar*Tr_per_m/Tcr_per_m*math.sqrt(math.e)
print(f"a_r = {ar:.3e} m;  a_cr = {a_cr:.2e} m   (paper: 5.9e-4)")
# aT invariant check: a_eq T_eq vs a_0 T_0(=2.725K equivalent)
arTr = ar*Tr_per_m
print(f"a_r*T_r (dimensionless) = {arTr:.4e}")
T0_eV = Tr_eV/(1+zeq)
print(f"implied T_0 = {T0_eV*1e3:.4f} meV = {T0_eV*eV/1.380649e-23:.3f} K (sanity: ~2.7 K)")
# v and v_ant
v = math.sqrt(32*math.e/243)*(h_s/h_n)*arTr
print(f"v = {v:.3e};  v_ant = pi v = {math.pi*v:.3e}   (paper v_ant: 8.9e34)")
# reproduce the paper's 8.9e34: use a_0 instead of a_eq
v_wrong = math.sqrt(32*math.e/243)*(h_s/h_n)*(a0*Tr_per_m)
print(f"v with a_r->a_0 (paper's apparent slip): v_ant = {math.pi*v_wrong:.3e}  -> matches 8.9e34:",
      abs(math.pi*v_wrong/8.9e34 - 1) < 0.03)
# Omega(Tcr)-1 = 1/v^2 (paper Eq. density)
print(f"Omega(T_cr)-1 = 1/v^2 = {1/v**2:.3e}   (paper: 1.3e-70)")
print(f"1/v_ant^2 with the a_0-inflated v = {1/(math.pi*v_wrong)**2:.3e}  -> matches 1.3e-70:",
      abs(1/(math.pi*v_wrong)**2/1.3e-70 - 1) < 0.05)
