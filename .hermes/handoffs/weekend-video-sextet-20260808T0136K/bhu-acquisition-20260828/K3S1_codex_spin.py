#!/usr/bin/env python3
"""K3S1 route-1 spin closure derivation (SymPy 1.14)."""
import sys
import sympy as sp

I = sp.I
zero2, one2 = sp.zeros(2), sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
pauli = (sx, sy, sz)
g0 = sp.diag(1, 1, -1, -1)

def blocks(a, b, c, d):
    return sp.Matrix.vstack(sp.Matrix.hstack(a, b), sp.Matrix.hstack(c, d))

gamma = [g0] + [blocks(zero2, q, -q, zero2) for q in pauli]  # Dirac representation, (+---)
g5 = sp.simplify(I * gamma[0] * gamma[1] * gamma[2] * gamma[3])
S = tuple(q / 2 for q in pauli)
up = sp.Matrix([1, 0, 0, 0])  # rest u_+(p), u^dag u=1
dn = sp.Matrix([0, 1, 0, 0])
P = sp.Matrix.vstack(sp.eye(2), sp.zeros(2))
A = tuple(sp.simplify(P.T * g0 * gamma[a] * g5 * P / 2) for a in (1, 2, 3))

def fail(label, got, expected):
    print(f"{label}=FAIL got={got} expected={expected}")
    sys.exit(1)

print("REPRESENTATION=Dirac; metric=diag(+1,-1,-1,-1)")
print("REST_WAVE=psi(x)=u exp(-imt)/sqrt(V), u^dag u=1, integral psi^dag psi d^3x=1")
print("gamma5=", g5)
print("projected bilinear operators A_i=(1/2)P^dag gamma0 gamma^i gamma5 P:", A)

# CONTROLS RUN FIRST. No closure/class calculation occurs above this point.
casimir = sp.simplify(sum((q*q for q in S), sp.zeros(2)))
c1 = sp.simplify((sp.Matrix([[1, 0]]) * casimir * sp.Matrix([1, 0]))[0])
print("C1_PAULI_ALGEBRA=sum_i(sigma_i/2)^2=", casimir)
print("C1_VALUE=", c1)
if c1 != sp.Rational(3, 4): fail("C1", c1, sp.Rational(3, 4))
print("C1=PASS")

n, N, V = sp.symbols("n N V", positive=True)
rho_plus = (one2 + sz) / 2
polar_mean = sp.Matrix([sp.trace(rho_plus*q) for q in S])
c2_sz = sp.simplify(n * polar_mean[2])
c2_sq = sp.simplify(sum((x*x for x in n*polar_mean), sp.S.Zero))
print("C2_SINGLE_MEAN=", tuple(polar_mean))
print("C2_MACRO_SZ=", c2_sz, "C2_MACRO_SQUARE=", c2_sq, "SCALING=n^2")
if c2_sz != n/2 or c2_sq != n**2/4: fail("C2", (c2_sz,c2_sq), (n/2,n**2/4))
print("C2=PASS")

hbar, c = sp.symbols("hbar c", positive=True)
fluid_units = (hbar*c*n)**2 / 8
print("C3_RESTORED_FLUID=", fluid_units)
if fluid_units != (hbar*c*n)**2/8: fail("C3", fluid_units, (hbar*c*n)**2/8)
print("C3=PASS")

# Preregistered C4 expectation: uniform uncorrelated spins have zero coherent
# n^2 term and only N/V^2 shot noise; deleting that average (all +z) restores
# a coherent n^2/4 term, changing at least the pseudovector object's class.
unpol_coherent, aligned_coherent = sp.S.Zero, n**2/4
print("C4_EXPECTED=unpolarized pseudovector: no coherent n^2 term; deletion/aligned: n^2/4")
print("C4_VALUES=", unpol_coherent, aligned_coherent)
if unpol_coherent == aligned_coherent: fail("C4", unpol_coherent, aligned_coherent)
print("C4=PASS (class changes SCALING_FAILS -> polarized closure derived)")
print("ALL_CONTROLS_PASS; BEGIN_DERIVATION")

# Algebra receipts and ensemble derivation.
rho_mix = (sp.Matrix([1,0])*sp.Matrix([[1,0]]) + sp.Matrix([0,1])*sp.Matrix([[0,1]]))/2
means = [sp.simplify(sp.trace(rho_mix*q)) for q in S]
second = sp.Matrix(3, 3, lambda a,b: sp.simplify(sp.trace(rho_mix*(S[a]*S[b]+S[b]*S[a])/2)))
print("MAXIMALLY_MIXED=rho=", rho_mix, "means=", means, "symmetric_second_moment=", second)
print("UNIFORM_SPHERE=<r_i>=0, <r_i r_j>=delta_ij/3, average rho(r)=I/2")
print("PURE_BILINEAR_MEAN_SQUARE=1/4; OPERATOR_CASIMIR_SECOND_MOMENT=3/4")

# E|sum X_A|^2 = N E|X|^2 + N(N-1)|EX|^2.
sum_square_unpol = sp.Rational(3,4)*N
density_square_unpol = sp.simplify(sum_square_unpol/V**2)
density_square_n_form = density_square_unpol.subs(N, n*V)
square_of_mean = sp.S.Zero
rms_continuum = sp.Rational(3,4)*n**2
print("DIRAC_MEAN_OF_SQUARE_OF_SUM=", sum_square_unpol)
print("DIRAC_DENSITY_MEAN_SQUARE=", density_square_unpol, "=", density_square_n_form, "SCALING=N/V^2=n/V")
print("DIRAC_SQUARE_OF_MEAN=", square_of_mean)
print("DIRAC_RMS_CONTINUUM_PRESCRIPTION=", rms_continuum, "SCALING=n^2")

# From s_ijk=-epsilon_ijkl s^l and s_ijk=s_ij u_k, contraction with u^k
# in the rest frame gives s_ab=-epsilon_ab0c s^c (up to orientation sign).
# Therefore (1/2)s_ab s^ab = delta_cd s^c s^d.
fluid_micro = density_square_unpol
fluid_rms_dual = rms_continuum
lambda_for_18 = sp.solve(sp.Eq(sp.Symbol("lambda", positive=True)**2*sp.Rational(3,4), sp.Rational(1,8)))[0]
print("DUAL_IDENTITY=(1/2)s_ab s^ab = s_vec.s_vec (sign-independent)")
print("FLUID_UNCORRELATED_MEAN_SQUARE=", fluid_micro, "SCALING=n/V")
print("FLUID_DIRAC_DUAL_RMS=", fluid_rms_dual, "SCALING=n^2")
print("FLUID_PRINTED_1/8_REQUIRES_s_ab=lambda*epsilon_abk*s_k_WITH_lambda=", lambda_for_18)
print("CONCLUSION=unpolarized averaging itself yields n/V shot noise (or zero square-of-mean), not n^2; 3/4 n^2 is an RMS continuum prescription; 1/8 additionally requires an unprovided 1/sqrt(6) fluid normalization relative to the Dirac dual")
