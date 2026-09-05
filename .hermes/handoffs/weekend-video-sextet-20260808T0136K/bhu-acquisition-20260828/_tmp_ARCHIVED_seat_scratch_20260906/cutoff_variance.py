import numpy as np
from scipy.special import legendre
from scipy.integrate import simps

cl_cut = {2: 559.22, 3: 245.19, 4: 133.53, 5: 71.35, 6: 53.48, 7: 33.70, 8: 22.16, 9: 21.75, 10: 13.77, 11: 9.98, 12: 11.47, 13: 7.70, 14: 5.74, 15: 6.90, 16: 5.0, 17: 3.94, 18: 4.0, 19: 3.68, 20: 3.7, 21: 3.72, 22: 3.0, 23: 2.43, 24: 2.5, 25: 2.46, 26: 2.5, 27: 2.66, 28: 2.0, 29: 1.88, 30: 1.9, 31: 1.93}

# Fill in missing Cls roughly
for L in range(2, 80):
    if L not in cl_cut:
        cl_cut[L] = 2.0

x_vals = np.linspace(-1, 0.5, 1000)

I_ij = np.zeros((80, 80))
for i in range(2, 40):
    for j in range(2, 40):
        P_i = legendre(i)(x_vals)
        P_j = legendre(j)(x_vals)
        I_ij[i,j] = simps(P_i * P_j, x_vals)

var_S12 = 0
for l1 in range(2, 40):
    for l2 in range(2, 40):
        # Var(S_1/2) = 2 \sum_{l1, l2} (2l1+1)(2l2+1) / (16 pi^2) C_l1^2 C_l2^2 (I_l1_l2)^2 / (2l1+1)?
        # Wait, the covariance of C(theta)
        # <C(theta) C(theta')> = \sum (2l+1)/(4pi)^2 2 C_l^2 P_l(x) P_l(x')
        # S_1/2 = \int_{-1}^{1/2} dx C(x)^2
        pass

# Simpler: just do Monte Carlo
np.random.seed(42)
N_sim = 10000
S12_sims = np.zeros(N_sim)

for sim in range(N_sim):
    C_theta = np.zeros_like(x_vals)
    for L in range(2, 40):
        # Sample Cl_hat from chi-square distribution with 2L+1 dof
        # Cl_hat = Cl / (2L+1) * sum(z_i^2)
        # where z_i are N(0,1)
        cl_hat = cl_cut[L] * np.random.chisquare(2*L+1) / (2*L+1)
        C_theta += (2*L+1)/(4*np.pi) * cl_hat * legendre(L)(x_vals)
    S12_sims[sim] = simps(C_theta**2, x_vals)

print(f"Mean S1/2: {np.mean(S12_sims):.2f}")
print(f"Std S1/2: {np.std(S12_sims):.2f}")
print(f"95th percentile: {np.percentile(S12_sims, 95):.2f}")
print(f"5th percentile: {np.percentile(S12_sims, 5):.2f}")
print(f"0.1th percentile: {np.percentile(S12_sims, 0.1):.2f}")

