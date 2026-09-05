import numpy as np
import camb
from scipy.special import spherical_jn
from scipy.integrate import simps
from time import time

start = time()

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
pars.set_for_lmax(2500, lens_potential_accuracy=0)
pars.WantTransfer = True
results = camb.get_results(pars)
trans = results.get_cmb_transfer_data()
q = trans.q
ells = trans.L
delta_T = trans.delta_p_l_k[0, :, :]

k = q
P_R = (2 * np.pi**2 / k**3) * A_s * (k / 0.05)**(n_s - 1)
sqrt_P_R = np.sqrt(P_R)

z_grid = np.linspace(0, r_c, 500)
# Make kz a 2D array: shape (len(z_grid), len(k))
kz = np.outer(z_grid, k)

cl_cut = {}
cl_uncut = {}

for i, L in enumerate(ells):
    if L > 100:
        continue
    # jl shape: (len(z), len(k))
    jl = spherical_jn(L, kz)
    # integrand shape: (len(z), len(k))
    integrand = (k**2 * sqrt_P_R * delta_T[i, :])[None, :] * jl
    # I_ell shape: (len(z),)
    I_ell = (2.0 / np.pi) * simps(integrand, k, axis=1)
    
    C_l = simps(z_grid**2 * I_ell**2, z_grid) * (2.7255e6)**2
    C_l_uncut = (2.0 / np.pi) * simps(k**2 * P_R * delta_T[i, :]**2, k) * (2.7255e6)**2
    
    cl_cut[L] = C_l
    cl_uncut[L] = C_l_uncut
    
    print(f"L={L}: cut={C_l:.2f}, uncut={C_l_uncut:.2f}")

S12 = 0
for L in range(2, 80):
    # wait, the standard definition of S1/2
    pass
# Calculate S1/2 properly
from scipy.special import legendre
x_vals = np.linspace(-1, 0.5, 1000) # cos(theta) from -1 to 1/2
dx = x_vals[1] - x_vals[0]

# Compute C(theta)
C_theta = np.zeros_like(x_vals)
for i, x in enumerate(x_vals):
    val = 0
    for L in range(2, 80):
        if L in cl_cut:
            # Cl is purely the coefficient.
            # C(theta) = \sum (2L+1)/(4 pi) C_L P_L(cos(theta))
            val += (2*L+1)/(4*np.pi) * cl_cut[L] * legendre(L)(x)
    C_theta[i] = val

S12 = simps(C_theta**2, x_vals)
print(f"S_1/2 = {S12:.2f}")

