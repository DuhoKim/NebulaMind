import sympy as sp

I2 = sp.eye(2)
O2 = sp.zeros(2)
sigma_1 = sp.Matrix([[0, 1], [1, 0]])
sigma_2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sigma_3 = sp.Matrix([[1, 0], [0, -1]])
sigmas = [sigma_1, sigma_2, sigma_3]

gamma_0 = sp.BlockMatrix([[I2, O2], [O2, -I2]]).as_explicit()
gamma_1 = sp.BlockMatrix([[O2, sigma_1], [-sigma_1, O2]]).as_explicit()
gamma_2 = sp.BlockMatrix([[O2, sigma_2], [-sigma_2, O2]]).as_explicit()
gamma_3 = sp.BlockMatrix([[O2, sigma_3], [-sigma_3, O2]]).as_explicit()
gamma_5 = sp.I * gamma_0 * gamma_1 * gamma_2 * gamma_3

print("gamma_5:", gamma_5)

Sigma = [gamma_0 * g * gamma_5 for g in [gamma_1, gamma_2, gamma_3]]
print("Sigma 1:", Sigma[0])
