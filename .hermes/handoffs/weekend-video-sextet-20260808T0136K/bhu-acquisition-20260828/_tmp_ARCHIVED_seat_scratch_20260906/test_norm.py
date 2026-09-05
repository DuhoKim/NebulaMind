import numpy as np
from scipy.integrate import simpson

def j0(x):
    return np.sinc(x/np.pi)

As = 2.1e-9
ns = 0.9649
KP = 0.05
L = 3.149 * 299792.458 / 67.36

k_min = 1e-6
k_max = 10.0
k_int = np.geomspace(k_min, k_max, 10000)
Delta2 = As * (k_int / KP)**(ns - 1)

r_grid = np.linspace(1e-5, L, 5000)
xi_LCDM = np.zeros_like(r_grid)
for i, r in enumerate(r_grid):
    integrand = (Delta2 / k_int) * j0(k_int * r)
    xi_LCDM[i] = simpson(integrand, x=k_int)

x = r_grid / L
W = (1 - x)**2 * (2 + x) / 2
xi_B = xi_LCDM * W

k_out = np.geomspace(1e-7, 2.0, 2000)
P_B = np.zeros_like(k_out)
for i, k in enumerate(k_out):
    integrand = r_grid**2 * xi_B * j0(k * r_grid)
    P_raw = 4 * np.pi * simpson(integrand, x=r_grid)
    P_B[i] = (k**3 / (2 * np.pi**2)) * P_raw

idx_norm = np.searchsorted(k_out, 1.0)
ratio = P_B[idx_norm] / (As * (k_out[idx_norm] / KP)**(ns - 1))
print(f"Norm ratio at k=1.0: {ratio}")
