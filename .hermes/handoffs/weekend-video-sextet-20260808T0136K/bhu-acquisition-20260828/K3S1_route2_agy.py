import sympy as sp

# Set up symbols
n, V, N = sp.symbols('n V N', positive=True)

# 1. Single particle density matrix
# Unpolarized state: equal weights on two orthogonal spin states
# rho = 1/2 |up><up| + 1/2 |down><down| = 1/2 * I
rho = sp.eye(2) / 2

# Pauli matrices
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
sigmas = [sx, sy, sz]

# Spin operators
S = [s / 2 for s in sigmas]

# Single particle
s2_single = sum(sp.trace(rho * S[i] * S[i]) for i in range(3))
print(f"C1 single particle s_i s^i: {s2_single}")

# Macroscopic unpolarized average
# <S_i> = Tr(rho S_i) = 0
# <S_i^2> = Tr(rho S_i^2) = 1/4
# Macroscopic S_i_macro = sum_{A=1}^N S_i^{(A)} / V
# <S_i_macro S_i_macro> = sum_{A,B} <S_i^{(A)} S_i^{(B)}> / V^2
# Cross terms vanish (Tr(rho S_i)Tr(rho S_i) = 0)
# Auto terms give N * 1/4
# Sum over 3 spatial dimensions = 3 * N * 1/4 / V^2 = 3/4 n / V
macro_s2_unpolarized = 3 * N * sp.Rational(1, 4) / V**2
macro_s2_unpolarized_n = macro_s2_unpolarized.subs(N, n*V)
print(f"Unpolarized macro <s_i s^i>: {macro_s2_unpolarized_n}")

# C2 fully polarized limit
rho_pol = sp.Matrix([[1, 0], [0, 0]])
s_z_pol = sp.trace(rho_pol * S[2])
# Cross terms <S_i> <S_i> do not vanish for z
# <S_z> = 1/2
# <S_z^2> = 1/4
# macro <s_z s_z> = (N * 1/4 + N*(N-1) * 1/4) / V**2 = N^2 / (4 V^2) = n^2 / 4
macro_sz2_pol = (N * sp.Rational(1, 4) + N*(N-1) * sp.Rational(1, 4)) / V**2
macro_sz2_pol_n = sp.simplify(macro_sz2_pol.subs(N, n*V))
print(f"C2 polarized macro <s_z s_z>: {macro_sz2_pol_n}")

macro_s2_pol = macro_sz2_pol_n + 0 + 0 # x and y cross terms are 0, auto terms give n/(4V)
macro_s2_pol_full = (N * sp.Rational(3, 4) + N*(N-1) * sp.Rational(1, 4)) / V**2
macro_s2_pol_full_n = sp.expand(macro_s2_pol_full.subs(N, n*V))
print(f"C2 polarized macro <s_i s^i>: {macro_s2_pol_full_n}")

# C4 deletion probe
# Running C2's ensemble (polarized) through unpolarized pipeline (meaning we drop cross terms? No, removing orientation average MEANS using polarized ensemble).
# If we remove the orientation average, <s_i s^i> goes from 3/4 n/V (scales as n) to n^2/4 + 3/4 n/V (scales as n^2).
# This changes the class from CLOSURE_SCALING_FAILS to CLOSURE_34_DERIVED (if we ignore the 1/V term in thermodynamic limit) or something similar.

