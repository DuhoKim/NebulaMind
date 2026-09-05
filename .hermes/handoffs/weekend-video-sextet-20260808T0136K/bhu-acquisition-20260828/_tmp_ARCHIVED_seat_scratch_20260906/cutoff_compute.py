import numpy as np
import camb
from scipy.special import spherical_jn
from scipy.integrate import simps

# Parameters from Gaztanaga calibration
A_s = 2.1e-9
n_s = 0.965
H0 = 67.4
ombh2 = 0.0224
omch2 = 0.120
tau = 0.054
r_c = 3.15 * 299792.458 / H0

pars = camb.CAMBparams()
pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=0.06, omk=0, tau=tau)
pars.InitPower.set_params(As=A_s, ns=n_s, pivot_scalar=0.05)
# Set high accuracy
pars.set_for_lmax(2500, lens_potential_accuracy=0)
pars.WantTransfer = True
pars.set_accuracy(AccuracyBoost=2.0, lSampleBoost=2.0, lAccuracyBoost=2.0)

results = camb.get_results(pars)
trans = results.get_cmb_transfer_data()
q = trans.q
ells = trans.L
delta_T = trans.delta_p_l_k[0, :, :]

# Compute P_R(k)
# q is k in Mpc^-1 (for omk=0)
k = q
# primordial power spectrum P_R(k) = (2 pi^2 / k^3) * A_s * (k/k0)^(n_s-1)
P_R = (2 * np.pi**2 / k**3) * A_s * (k / 0.05)**(n_s - 1)
sqrt_P_R = np.sqrt(P_R)

# Grid for z integral
z_grid = np.linspace(0, r_c, 500)
dz = z_grid[1] - z_grid[0]

Cl_cut = {}
Cl_uncut = {}

for i, L in enumerate(ells):
    if L > 100:
        continue
    # I_ell(z) = 2/pi \int k^2 dk \sqrt{P_R(k)} \Delta_\ell(k) j_\ell(kz)
    # delta_T in CAMB is actually \Delta_\ell(k) * \sqrt{A_s (k/k0)^{n_s-1} / k} ? No, it's just \Delta_\ell(k) up to normalization.
    # Wait, earlier I found that:
    # \int dk/k delta_T^2 * \mathcal{P}_R = cl_trans
    # So CAMB's delta_T is literally \Delta_\ell(k).
    # Then I_ell(z) = 2/pi \int k^2 dk \sqrt{P_R(k)} delta_T[i, :] j_\ell(kz)
    
    I_ell = np.zeros_like(z_grid)
    for j, z in enumerate(z_grid):
        jl = spherical_jn(L, k * z)
        integrand = k**2 * sqrt_P_R * delta_T[i, :] * jl
        I_ell[j] = (2.0 / np.pi) * simps(integrand, k)
        
    C_l = simps(z_grid**2 * I_ell**2, z_grid)
    # Convert to muK^2
    C_l_muK = C_l * (2.7255e6)**2
    Cl_cut[L] = C_l_muK
    
    # Check uncut C_l using the same integration, but replacing z-integral by the exact identity
    # \int_0^\infty z^2 I_ell^2 dz = 2/pi \int k^2 dk P_R \Delta_\ell^2
    C_l_uncut = (2.0 / np.pi) * simps(k**2 * P_R * delta_T[i, :]**2, k) * (2.7255e6)**2
    Cl_uncut[L] = C_l_uncut
    if L <= 10:
        print(f"L={L}: cut={Cl_cut[L]:.2f}, uncut={Cl_uncut[L]:.2f}")

