"""Receipt: priority target. If Lambda_obs = 3 Omega^2/c^2 (paper's identification),
what Omega is required, and how does it compare to the pinned CMB rotation bounds?
Inputs (pinned Phase 0 S3, arXiv:1807.06209 abstract): H0 = 67.4 km/s/Mpc, Omega_m = 0.315.
Flat LCDM assumed for Omega_Lambda = 1 - Omega_m (stated assumption).
Bounds (pinned Phase 0 S1/S2): (omega/H)_0 < 7.6e-10 (Planck Bianchi VII_h, 95% CL);
(sigma_V/H)_0 < 4.7e-11 (Saadeh 2016 vector mode, 95% CI)."""
import math
c = 2.99792458e8          # m/s (defined)
Mpc = 3.0856775814913673e22  # m (IAU)
H0 = 67.4e3 / Mpc         # s^-1
Om = 0.315
OL = 1.0 - Om
Lambda_obs = 3.0 * OL * H0**2 / c**2   # m^-2, from H^2 = (Lambda c^2/3) at Lambda domination
print(f"H0 = {H0:.4e} s^-1")
print(f"Lambda_obs = 3(1-Om)H0^2/c^2 = {Lambda_obs:.3e} m^-2  (brief's 1.1e-52 check)")
# Paper: "H=(Lambda/3)^{1/2} c would thus be equal to Omega"; "Lambda = 3 Omega^2/c^2"
Omega_req = c * math.sqrt(Lambda_obs / 3.0)
print(f"Omega_required = c*sqrt(Lambda/3) = {Omega_req:.3e} s^-1")
print(f"(Omega/H)_0 required = {Omega_req/H0:.3f}   [= sqrt(Omega_Lambda) = {math.sqrt(OL):.3f}]")
b_planck = 7.6e-10
b_saadeh = 4.7e-11
print(f"excess over Planck Bianchi VII_h bound: {(Omega_req/H0)/b_planck:.3e}")
print(f"excess over Saadeh vector-mode bound:   {(Omega_req/H0)/b_saadeh:.3e}")
# Converse: if Omega respects the Planck bound, what fraction of Lambda_obs can rotation supply?
frac = (b_planck / (Omega_req/H0))**2
print(f"max rotational Lambda / Lambda_obs at the Planck bound: {frac:.3e}")
