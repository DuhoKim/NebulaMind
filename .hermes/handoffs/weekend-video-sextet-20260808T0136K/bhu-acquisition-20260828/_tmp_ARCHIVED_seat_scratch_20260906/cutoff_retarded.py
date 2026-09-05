import numpy as np
import camb
from camb import model, initialpower
from scipy.interpolate import interp1d
from scipy.integrate import simps
import sys

# Parameters
A_s = 2.1e-9
n_s = 0.965
H0 = 67.4
ombh2 = 0.0224
omch2 = 0.120
tau = 0.054
r_c = 3.15 * 299792.458 / H0 # in Mpc

# Set up CAMB
pars = camb.CAMBparams()
pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=0.06, omk=0, tau=tau)
pars.InitPower.set_params(As=A_s, ns=n_s, pivot_scalar=0.05)
pars.set_for_lmax(2500, lens_potential_accuracy=0)
pars.WantTransfer = True
pars.set_accuracy(AccuracyBoost=2.0, lSampleBoost=2.0, lAccuracyBoost=2.0)

results = camb.get_results(pars)
# Get un-cut Cls to verify
cl_uncut = results.get_total_cls(2500, CMB_unit='muK')

# We need the transfer functions Delta_ell(k)
# CAMB's get_cmb_transfer_data returns the transfer functions.
trans = results.get_cmb_transfer_data()
# trans is a TransferData object.
# The q values (k in CAMB's internal units)
q = trans.q
# The ell values
ells = trans.L

# The temperature transfer function is index 0.
# Delta_ell(k) for temperature
delta_T = trans.delta_p_l_k[0, :, :] # shape (n_ell, n_q)

# Calculate P(k) for R
# k is in Mpc^-1. But CAMB q might be in Mpc^-1 if omk=0.
k = q
P_R = A_s * (k / 0.05)**(n_s - 1) * (2 * np.pi**2 / k**3)

# We need to compute I_ell(z) = 2/pi \int k^2 dk \sqrt{P(k)} \Delta_\ell(k) j_\ell(kz)
# CAMB delta_T is such that C_ell = \int dk/k |delta_T|^2 P_R(k) ?
# Wait, CAMB's transfer function definition:
# C_ell = \int dk/k (delta_ell)^2 \mathcal{P}_R(k)
# So delta_ell_CAMB = \Delta_\ell(k) * k ? 
# Let's check the un-cut C_ell from the transfer functions:
cl_trans = np.zeros_like(ells, dtype=float)
for i, L in enumerate(ells):
    integrand = (delta_T[i, :])**2 * (A_s * (k/0.05)**(n_s-1)) / k
    cl_trans[i] = np.trapz(integrand, k) * (2.7255e6)**2

print("L=", ells[2], " Cl_uncut=", cl_uncut[ells[2], 0], " Cl_trans=", cl_trans[2])

