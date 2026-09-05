import sympy as sp
I2 = sp.eye(2); O2 = sp.zeros(2)
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
gamma_0 = sp.BlockMatrix([[I2, O2], [O2, -I2]]).as_explicit()
gamma_1 = sp.BlockMatrix([[O2, s1], [-s1, O2]]).as_explicit()
gamma_2 = sp.BlockMatrix([[O2, s2], [-s2, O2]]).as_explicit()
gamma_3 = sp.BlockMatrix([[O2, s3], [-s3, O2]]).as_explicit()
gamma_5 = sp.I * gamma_0 * gamma_1 * gamma_2 * gamma_3
Sigmas = [gamma_0 * g * gamma_5 for g in [gamma_1, gamma_2, gamma_3]]
I4 = sp.eye(4)

v1, v2 = sp.symbols('v1 v2')
v3_1, v3_2, v3_3 = sp.symbols('v3_1 v3_2 v3_3')
A = v1 * I4 + v2 * gamma_0 + v3_1 * gamma_1 * gamma_0 + v3_2 * gamma_2 * gamma_0 + v3_3 * gamma_3 * gamma_0

exchange_C_integrand = 0
for a in range(3):
    exchange_C_integrand -= (1/4) * sp.trace(Sigmas[a] * A * Sigmas[a] * A)

print("Exchange C integrand:", sp.simplify(exchange_C_integrand))
