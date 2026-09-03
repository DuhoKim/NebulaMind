#!/usr/bin/env python3
"""K3 step 1, route 1, seat claude — unpolarized Dirac-spin closure, derived with sympy.

Prereg: K3S1_SPIN_CLOSURE_PREREG_20260903.md (frozen).  Everything printed below is computed
here; nothing is typed in from the papers except the two coefficients under test (3/4, 1/8),
which enter ONLY as comparison targets inside classify().

Conventions (stated once, used throughout):
  * metric eta = diag(+1,-1,-1,-1); Dirac representation; gamma5 = i g0 g1 g2 g3
  * hbar = c = 1 in sections 1-7; restored in C3
  * "|s|^2" means the Euclidean square of the spatial pseudovector; s_i s^i = -|s|^2 in this signature
  * N particles in a volume V, n = N/V; V = 1 wherever the prereg says "per volume"
  * ensemble = product state of N single-particle spinors, orientations i.i.d. uniform on the sphere
Prescriptions the papers do not fix (both are carried; C1 fixes which one the prereg pins):
  P1 operator-ordered square  <psi| S.S |psi>          (single particle -> Casimir 3/4)
  P2 c-number square of the bilinear  (psibar g g5 psi)^2   (single particle -> 1/4)
"""
import sympy as sp
from sympy import I, Rational as R, Matrix, eye, zeros, symbols, sin, cos, exp, pi, simplify, Poly, sqrt

def P(tag, x): print(f"[{tag}] {x}")
def Z(M):
    """robust symbolic zero test for a matrix/scalar of half-angle trig expressions"""
    M = Matrix(M) if not isinstance(M, Matrix) else M
    return all(sp.simplify(sp.expand(e.rewrite(sp.exp))) == 0 for e in M)
def H(t): print("\n" + "=" * 8 + " " + t + " " + "=" * 8)
CONTROL = {}

# ------------------------------------------------------------------ 1. Pauli, Casimir pin
H("1. Pauli matrices and the spin-1/2 Casimir (pin for C1)")
s1 = Matrix([[0, 1], [1, 0]]); s2 = Matrix([[0, -I], [I, 0]]); s3 = Matrix([[1, 0], [0, -1]])
sig = [s1, s2, s3]
S = [x / 2 for x in sig]                      # spin operators, hbar = 1
for a in range(3):
    for b in range(3):
        comm = S[a] * S[b] - S[b] * S[a]
        rhs = zeros(2, 2)
        for c in range(3):
            rhs += I * sp.LeviCivita(a, b, c) * S[c]
        assert comm == rhs, "su(2) algebra failed"
P("su2", "[S_a,S_b] = i eps_abc S_c verified for all a,b")
Cas = S[0] ** 2 + S[1] ** 2 + S[2] ** 2
P("Casimir", f"S.S = {Cas.tolist()}  -> eigenvalue {Cas[0, 0]} = s(s+1) with s=1/2 -> {R(1,2)*(R(1,2)+1)}")
assert Cas == R(3, 4) * eye(2)
CASIMIR = Cas[0, 0]

# ------------------------------------------------------------------ 2. Dirac matrices
H("2. Dirac matrices (Dirac representation), Clifford checks, Sigma^k")
eta = sp.diag(1, -1, -1, -1)
g0 = sp.diag(1, 1, -1, -1)
def blk(a, b, c, d): return Matrix(sp.BlockMatrix([[a, b], [c, d]]))
gi = [blk(zeros(2), s, -s, zeros(2)) for s in sig]
gam = [g0] + gi
g5 = I * g0 * gi[0] * gi[1] * gi[2]
for m in range(4):
    for n_ in range(4):
        assert gam[m] * gam[n_] + gam[n_] * gam[m] == 2 * eta[m, n_] * eye(4)
assert g5 * g5 == eye(4)
assert all(g5 * gam[m] == -gam[m] * g5 for m in range(4))
P("Clifford", "{g^mu,g^nu} = 2 eta^{mu nu}, g5^2 = 1, {g5,g^mu} = 0  verified")
P("gamma5", g5.tolist())
Sigma = [g5 * g0 * gi[k] for k in range(3)]
for k in range(3):
    assert Sigma[k] == blk(sig[k], zeros(2), zeros(2), sig[k])
    assert g0 * gi[k] * g5 == Sigma[k]
P("Sigma", "g0 g^k g5 = g5 g0 g^k = diag(sigma_k, sigma_k) =: Sigma^k  verified for k=1,2,3")

# ------------------------------------------------------------------ 3. rest spinor
H("3. Plane-wave spinor at rest, spin along n(theta,phi), normalised psibar g0 psi = 1")
th, ph = symbols('theta phi', real=True)
m = symbols('m', positive=True)
chi = Matrix([cos(th / 2), exp(I * ph) * sin(th / 2)])
psi = Matrix([chi[0], chi[1], 0, 0])
psibar = psi.H * g0
# Dirac equation at rest: (gamma^0 p_0 - m) psi = 0 with p_0 = m  <=>  g0 psi = psi
assert Z(g0 * psi - psi)
assert Z((gam[0] * m - m * eye(4)) * psi)
P("Dirac_eq", "(g^0 p_0 - m) psi = 0 at p=(m,0,0,0)  verified")
norm = simplify((psibar * g0 * psi)[0])
P("norm", f"psibar g^0 psi = psi^dag psi = {norm}  (one particle per unit volume)")
assert norm == 1
nhat = Matrix([sin(th) * cos(ph), sin(th) * sin(ph), cos(th)])
Sexp = Matrix([simplify((chi.H * S[k] * chi)[0]) for k in range(3)])
P("spin_expect", f"chi^dag S_k chi = {list(Sexp)}  = n/2 -> {Z(Sexp - nhat/2)}")
assert Z(Sexp - nhat / 2)
# helicity/spin projector check: chi is the +1/2 eigenvector of n.S
assert Z((nhat[0]*S[0]+nhat[1]*S[1]+nhat[2]*S[2]) * chi - chi/2)
P("eigen", "chi is the +1/2 eigenvector of n.S  verified")

# ------------------------------------------------------------------ 4. Dirac pseudovector
H("4. Dirac pseudovector s^mu = 1/2 psibar g^mu g5 psi  (entry 10 eq. 4)")
s_up = Matrix([simplify((R(1, 2) * psibar * gam[mu] * g5 * psi)[0]) for mu in range(4)])
P("s^mu", f"{list(s_up)}")
assert s_up[0] == 0
P("s^0", "s^0 = 0 in the rest frame  (=> s_i u^i = 0, entry 10 L112)  verified")
assert Z(s_up[1:, :] - nhat / 2)
P("s_spatial", "s^k = n_k/2  (spin density of one particle at unit density)  verified")
s_dn = eta * s_up
s_dot_s = simplify(sum(s_dn[mu] * s_up[mu] for mu in range(4)))
mag2 = simplify(sum(s_up[k] ** 2 for k in range(1, 4)))
P("P2_single", f"c-number square: s_i s^i = {s_dot_s},  |s|^2 = {mag2}")
# operator-ordered square: S_k = Sigma^k/2 acting on the Dirac spinor
Sop = [Sigma[k] / 2 for k in range(3)]
op_sq = simplify((psi.H * (Sop[0] ** 2 + Sop[1] ** 2 + Sop[2] ** 2) * psi)[0])
P("P1_single", f"operator square: <psi| S.S |psi> = {op_sq}")
cov_op = simplify((psi.H * sum((eta[mu, mu] * (R(1, 2) * g0 * gam[mu] * g5) ** 2 for mu in range(4)), zeros(4, 4)) * psi)[0])
P("remark", f"4-covariant operator square incl. mu=0: <(1/2 g0 g^mu g5)(1/2 g0 g_mu g5)> = {cov_op}  (NOT the object; printed for completeness)")

# ------------------------------------------------------------------ C1
H("C1 single particle at rest: expect the Casimir 3/4")
P("C1_operator_square", op_sq)
P("C1_cnumber_square", mag2)
CONTROL['C1'] = (op_sq == CASIMIR)
P("C1", "PASS" if CONTROL['C1'] else "FAIL")
print("   note: the prereg's 3/4 is the OPERATOR-ordered square (P1); the square of the bilinear itself (P2) is 1/4.")
print("   C1 therefore fixes the prescription P1 for the classification; P2 is carried alongside.")

# ------------------------------------------------------------------ 5. unpolarized average
H("5. Unpolarized ensemble = uniform average over the sphere; maximally mixed state pin")
def avg(f, t=th, p=ph):
    return simplify(sp.integrate(sp.integrate(f * sin(t), (t, 0, pi)), (p, 0, 2 * pi)) / (4 * pi))
avg_n = Matrix([avg(nhat[k]) for k in range(3)])
avg_nn = Matrix(3, 3, lambda i, j: avg(nhat[i] * nhat[j]))
P("<n_i>", list(avg_n)); P("<n_i n_j>", avg_nn.tolist())
assert avg_n == zeros(3, 1) and avg_nn == eye(3) / 3
rho = Matrix(2, 2, lambda i, j: avg(chi[i] * sp.conjugate(chi[j])))
P("rho_avg", f"<|chi><chi|>_sphere = {rho.tolist()} = 1/2 * identity")
assert rho == eye(2) / 2
up = Matrix([1, 0]); dn = Matrix([0, 1])
rho_mm = R(1, 2) * (up * up.H + dn * dn.H)
P("rho_mixed", f"1/2(|up><up| + |dn><dn|) = {rho_mm.tolist()}  == sphere average: {rho_mm == rho}")
assert rho_mm == rho
TrSS = Matrix(3, 3, lambda i, j: simplify((rho * S[i] * S[j]).trace()))
P("Tr(rho S_i S_j)", f"{TrSS.tolist()}  -> Tr(rho S.S) = {TrSS.trace()}")
assert TrSS.trace() == CASIMIR

# ------------------------------------------------------------------ 6. N particles
H("6. N uncorrelated particles in volume V: square of the SUM, both prescriptions")
N, V = symbols('N V', positive=True)
# per-particle quantities (hbar=1), particle a has angles (th_a, ph_a)
# diagonal terms
diag_P1 = avg(op_sq)                      # <S_a.S_a>
diag_P2 = avg(mag2)                       # |<S_a>|^2
# cross terms: independent angles for particles a and b
th2, ph2 = symbols('theta2 phi2', real=True)
nhat2 = nhat.subs({th: th2, ph: ph2})
cross = sum((nhat[k] / 2) * (nhat2[k] / 2) for k in range(3))   # <S_a>.<S_b> = (n_a/2).(n_b/2)
cross_avg = avg(avg(cross), th2, ph2)
P("diag_P1", f"<S_a.S_a> = {diag_P1}");  P("diag_P2", f"|<S_a>|^2 = {diag_P2}")
P("cross", f"<S_a>.<S_b> = {simplify(cross)} -> averaged over both orientations = {cross_avg}")
assert cross_avg == 0
# For a product state, <(sum_a S_a).(sum_b S_b)> = sum_a <S_a.S_a> + sum_{a!=b} <S_a>.<S_b>  (verified explicitly at N=2,3 below)
def kron_list(ms):
    out = ms[0]
    for x in ms[1:]:
        out = sp.kronecker_product(out, x)
    return out
def total_spin_sq_expect(angles):
    """explicit tensor-product state, explicit total spin operator, explicit expectation"""
    Nn = len(angles)
    chis = [chi.subs({th: t, ph: p}) for (t, p) in angles]
    state = kron_list(chis)
    Stot = []
    for k in range(3):
        acc = zeros(2 ** Nn, 2 ** Nn)
        for a in range(Nn):
            acc += kron_list([S[k] if b == a else eye(2) for b in range(Nn)])
        Stot.append(acc)
    op = Stot[0] ** 2 + Stot[1] ** 2 + Stot[2] ** 2
    return simplify((state.H * op * state)[0])
ang = [symbols(f'theta_{a} phi_{a}', real=True) for a in range(1, 4)]
e2 = total_spin_sq_expect(ang[:2])
P("N=2_explicit", f"<S_tot.S_tot> = {e2}")
e2_avg = e2
for (t, p) in ang[:2]:
    e2_avg = avg(e2_avg, t, p)
P("N=2_avg", f"orientation average = {e2_avg}  (= 2 * 3/4: {e2_avg == 2*CASIMIR})")
assert e2_avg == 2 * CASIMIR
e3 = total_spin_sq_expect(ang[:3])
e3_avg = e3
for (t, p) in ang[:3]:
    e3_avg = avg(e3_avg, t, p)
P("N=3_avg", f"orientation average = {e3_avg}  (= 3 * 3/4: {e3_avg == 3*CASIMIR})")
assert e3_avg == 3 * CASIMIR
# general N by the diagonal/cross decomposition (verified above at N=2,3)
sq_P1 = sp.expand(N * diag_P1 + N * (N - 1) * cross_avg)
sq_P2 = sp.expand(N * diag_P2 + N * (N - 1) * cross_avg)
mean_vec = N * avg_n / 2
P("unpol_P1", f"<(sum_a S_a)^2> = {sq_P1}")
P("unpol_P2", f"<(sum_a <S_a>)^2> = {sq_P2}")
P("square_of_mean", f"|<sum_a S_a>|^2 = {simplify((mean_vec.T*mean_vec)[0])}")
dens_P1 = sp.simplify(sq_P1 / V ** 2)
P("density_P1", f"<s^2> for the density s = (1/V) sum_a S_a:  {dens_P1}  = (3/4) n/V with n=N/V -> {simplify(dens_P1 - R(3,4)*(N/V)/V) == 0}")
# scaling bookkeeping
def npoly(expr):
    p = Poly(sp.expand(expr.subs(V, 1)), N)
    return {"leading_power": p.degree(), "coeff_N2": p.coeff_monomial(N ** 2), "coeff_N1": p.coeff_monomial(N)}
P("scaling_P1", npoly(sq_P1)); P("scaling_P2", npoly(sq_P2))
# RMS / coherence conventions that DO give n^2 (these are conventions, not averages)
rms_mag_P1 = sqrt(diag_P1); rms_mag_P2 = sqrt(diag_P2)
P("convention_coherent_P1", f"(N * sqrt<S_a.S_a>)^2 = {sp.expand((N*rms_mag_P1)**2)}   <- coherent sum of per-particle RMS magnitude sqrt(3/4)")
P("convention_coherent_P2", f"(N * |<S_a>|)^2      = {sp.expand((N*rms_mag_P2)**2)}   <- coherent sum of per-particle expectation magnitude 1/2 (= polarized closure)")
P("convention_half_coherent_P2", f"1/2 * (N/2)^2 = {sp.expand(R(1,2)*(N/2)**2)}   <- polarized closure with the 1/2 of s^2=1/2 s_ij s^ij kept but the double-count factor 2 dropped")

# ------------------------------------------------------------------ 7. spin-fluid tensor and the identity
H("7. Spin-fluid tensor from the Dirac tensor s_ijk = -e_ijkl s^l ; s_ij := s_ijk u^k ; 1/2 s_ij s^ij")
def eps4(a, b, c, d): return sp.LeviCivita(a, b, c, d)   # e_0123 = +1 (lower indices); sign irrelevant for squares
u_up = Matrix([1, 0, 0, 0]); u_dn = eta * u_up
s3idx = sp.MutableDenseNDimArray.zeros(4, 4, 4)
for a in range(4):
    for b in range(4):
        for c in range(4):
            s3idx[a, b, c] = -sum(eps4(a, b, c, l) * s_up[l] for l in range(4))
# total antisymmetry
assert all(s3idx[a, b, c] == -s3idx[b, a, c] == -s3idx[a, c, b] for a in range(4) for b in range(4) for c in range(4))
P("antisym", "s_ijk totally antisymmetric  verified")
s_ij = Matrix(4, 4, lambda a, b: sum(s3idx[a, b, c] * u_up[c] for c in range(4)))
P("s_ij", f"s_ij = s_ijk u^k = {simplify(s_ij).tolist()}")
assert Z(s_ij * u_up)
P("transverse", "s_ij u^j = 0  verified (HHK condition holds for the projection)")
hhk = sp.MutableDenseNDimArray.zeros(4, 4, 4)
for a in range(4):
    for b in range(4):
        for c in range(4):
            hhk[a, b, c] = s_ij[a, b] * u_dn[c]
same = all(simplify(hhk[a, b, c] - s3idx[a, b, c]) == 0 for a in range(4) for b in range(4) for c in range(4))
P("HHK_form", f"s_ij u_k == Dirac s_ijk ? {same}  (Dirac tensor has s_0jk, s_i0k components the HHK form lacks: the identification is a projection, a prescription)")
s_IJ_up = eta * s_ij * eta
fluid_sq = simplify(R(1, 2) * sum(s_ij[a, b] * s_IJ_up[a, b] for a in range(4) for b in range(4)))
P("fluid_sq", f"1/2 s_ij s^ij = {fluid_sq}")
full_sq = simplify(sum(s3idx[a, b, c] * eta[a, a] * eta[b, b] * eta[c, c] * s3idx[a, b, c] for a in range(4) for b in range(4) for c in range(4)))
P("full_Dirac_sq", f"s_ijk s^ijk = {full_sq} = 6|s|^2 ;  (1/6) s_ijk s^ijk = {simplify(full_sq/6)}")
P("IDENTITY", f"1/2 s_ij s^ij - |s|^2 = {simplify(fluid_sq - mag2)} ;  1/2 s_ij s^ij + s_i s^i = {simplify(fluid_sq + s_dot_s)}")
assert simplify(fluid_sq - mag2) == 0 and simplify(fluid_sq + s_dot_s) == 0
print("   => 1/2 s_ij s^ij = |s|^2 = -s_i s^i  exactly, for every orientation: the two objects have the SAME square.")
print("      The identity is linear-algebraic in s^l, so it survives the sum over particles and both prescriptions;")
print("      the fluid object's ensemble averages are therefore those of section 6 verbatim.")
sq_fluid_P1, sq_fluid_P2 = sq_P1, sq_P2   # by the identity (checked symbolically above)
# explicit check of the transfer at N=2, P2: build the total pseudovector, form the tensor, square it, compare
sv2 = Matrix([0, 0, 0, 0])
for (t, p) in ang[:2]:
    sv2 += s_up.subs({th: t, ph: p})
t2 = Matrix(4, 4, lambda a, b: -sum(eps4(a, b, 0, l) * sv2[l] for l in range(4)))
f2 = simplify(R(1, 2) * sum(t2[a, b] * (eta * t2 * eta)[a, b] for a in range(4) for b in range(4)))
f2_avg = f2
for (t, p) in ang[:2]:
    f2_avg = avg(f2_avg, t, p)
P("fluid_N=2_P2", f"1/2 s_ij s^ij of the summed pseudovector, averaged = {f2_avg}  (= 2 * 1/4: {f2_avg == 2*diag_P2})")
assert f2_avg == 2 * diag_P2

# ------------------------------------------------------------------ C2
H("C2 fully polarized limit: all spins along +z through the same pipeline")
def polarized(expr):   # replace the orientation average by evaluation at theta=0 (all +z)
    return simplify(expr.subs({th: 0, ph: 0, th2: 0, ph2: 0}))
sz_tot = simplify(N * polarized(s_up[3]))
pol_P2 = sp.expand(N * polarized(mag2) + N * (N - 1) * polarized(cross))
pol_P1 = sp.expand(N * polarized(op_sq) + N * (N - 1) * polarized(cross))
e2_pol = simplify(e2.subs({ang[0][0]: 0, ang[0][1]: 0, ang[1][0]: 0, ang[1][1]: 0}))
e3_pol = simplify(e3.subs({a: 0 for pair in ang[:3] for a in pair}))
P("s_z", f"sum_a s_z = {sz_tot}  (expect N/2 = n/2)")
P("P2", f"(sum_a <S_a>)^2 = {pol_P2}   scaling {npoly(pol_P2)}")
P("P1", f"<(sum_a S_a)^2> = {pol_P1}   scaling {npoly(pol_P1)}  = S_tot(S_tot+1) with S_tot=N/2 -> {sp.expand(pol_P1 - (N/2)*(N/2+1)) == 0}")
P("P1_explicit", f"N=2: {e2_pol} (formula {pol_P1.subs(N,2)}),  N=3: {e3_pol} (formula {pol_P1.subs(N,3)})")
assert e2_pol == pol_P1.subs(N, 2) and e3_pol == pol_P1.subs(N, 3)
CONTROL['C2'] = (sz_tot == N / 2) and (pol_P2 == N ** 2 / 4) and (npoly(pol_P1)["coeff_N2"] == R(1, 4)) and (npoly(pol_P1)["leading_power"] == 2)
P("C2", "PASS" if CONTROL['C2'] else "FAIL")
print("   s_z = n/2 exactly; P2 gives n^2/4 exactly; P1 gives n^2/4 + n/2 (n^2 scaling, coefficient 1/4, Casimir of total spin N/2).")

# ------------------------------------------------------------------ C3
H("C3 units: restore hbar and c for the fluid object")
hbar, c = symbols('hbar c', positive=True)
import sympy.physics.units as U
from sympy.physics.units import convert_to
kappa = 8 * pi * U.gravitational_constant / U.speed_of_light ** 4       # entry 9: kappa = 8 pi G / c^4
n_unit = 1 / U.meter ** 3
dim_check = convert_to(kappa * (U.hbar * U.speed_of_light * n_unit) ** 2, U.joule / U.meter ** 3)
P("dim", f"kappa (hbar c n)^2 in J/m^3 with n = 1/m^3: {dim_check}")
assert dim_check.has(U.joule) and not dim_check.has(U.kilogram)
print("   -> (hbar c n)^2 is the unique hbar,c dressing making kappa s^2 an energy density with s ~ n: s_ij(entry 9) = c * (angular-momentum density)")
# per-particle spin (hbar/2) n ; summed; tensor in entry-9 units carries one c
s_phys_pol = sp.expand(c ** 2 * hbar ** 2 * pol_P2 / V ** 2)          # polarized (coherent) fluid closure
s_phys_unpol = sp.expand(c ** 2 * hbar ** 2 * sq_fluid_P1 / V ** 2)   # unpolarized average, P1
nn = symbols('n', positive=True)
P("fluid_polarized", f"1/2 s_ij s^ij = {s_phys_pol.subs(N, nn*V)}  = (1/4)(hbar c n)^2")
P("fluid_unpolarized_avg", f"<1/2 s_ij s^ij> = {sp.simplify(s_phys_unpol.subs(N, nn*V))}  = (3/4)(hbar c)^2 n/V")
form_ok = simplify(s_phys_pol.subs(N, nn * V) / (hbar * c * nn) ** 2) == R(1, 4)
CONTROL['C3'] = bool(form_ok)
P("C3", ("PASS" if CONTROL['C3'] else "FAIL") + "  — the (hbar c n)^2 form is reproduced (coefficient 1/4 for the coherent closure; the printed 1/8 is not what the pipeline returns — C3 tests the form, the coefficient is the question under test)")

# ------------------------------------------------------------------ classification + C4
H("Classifier (declared before C4), and C4 deletion probe")
PRINTED = {"FLUID": R(1, 8), "DIRAC": R(3, 4)}
def classify(expr, obj):
    d = npoly(expr)
    if d["leading_power"] < 2:
        return "CLOSURE_SCALING_FAILS", d
    if d["coeff_N2"] == PRINTED[obj]:
        return {"FLUID": "CLOSURE_18_DERIVED", "DIRAC": "CLOSURE_34_DERIVED"}[obj], d
    return "CLOSURE_CONFLICT", d
print("   rule: leading power of N < 2 -> CLOSURE_SCALING_FAILS; power 2 and coeff == printed -> CLOSURE_xx_DERIVED;")
print("         power 2 and coeff != printed -> CLOSURE_CONFLICT (an n^2 closure with a coefficient the average contradicts).")
print("   C4 EXPECTED (stated before running): unpolarized pipeline files CLOSURE_SCALING_FAILS for BOTH objects;")
print("   deleting the orientation average (all +z) must move BOTH to CLOSURE_CONFLICT (power 2, coeff 1/4 != 1/8 and != 3/4).")
print("   Exact expected change set: {DIRAC: SCALING_FAILS->CONFLICT, FLUID: SCALING_FAILS->CONFLICT}; anything else = C4 FAIL.")
cls_unpol = {"DIRAC": classify(sq_P1, "DIRAC"), "FLUID": classify(sq_fluid_P1, "FLUID")}
cls_pol = {"DIRAC": classify(pol_P1, "DIRAC"), "FLUID": classify(pol_P1, "FLUID")}   # fluid = same expression by the identity
for k in cls_unpol:
    P(f"C4_{k}", f"with average: {cls_unpol[k]}   |  average deleted: {cls_pol[k]}")
expected = {"DIRAC": ("CLOSURE_SCALING_FAILS", "CLOSURE_CONFLICT"), "FLUID": ("CLOSURE_SCALING_FAILS", "CLOSURE_CONFLICT")}
CONTROL['C4'] = all((cls_unpol[k][0], cls_pol[k][0]) == expected[k] for k in expected)
P("C4", "PASS" if CONTROL['C4'] else "FAIL")
# prescription robustness of the class (P2 alongside)
P("P2_classes", f"DIRAC {classify(sq_P2,'DIRAC')[0]}  FLUID {classify(sq_fluid_P2,'FLUID')[0]}  (class independent of P1/P2; only the n-coefficient 3/4 vs 1/4 depends on it)")

# ------------------------------------------------------------------ verdict
H("RESULT (filed only if C1-C4 all PASS)")
P("controls", CONTROL)
if not all(CONTROL.values()):
    print("A CONTROL FAILED — no class filed.")
    raise SystemExit(1)
P("OBJECT_DIRAC", f"<s_i s^i> = -{sq_P1/V**2} = -(3/4) n/V   [P1; P2: -(1/4) n/V]   class {cls_unpol['DIRAC'][0]}")
P("OBJECT_FLUID", f"1/2<s_ij s^ij> = +{sq_fluid_P1/V**2} = (3/4) n/V   [P1; P2: (1/4) n/V]   class {cls_unpol['FLUID'][0]}")
P("IDENTITY", "1/2 s_ij s^ij = -s_i s^i = |s|^2  (same object; so 1/8 n^2 and 3/4 n^2 cannot both hold — a factor-6 inconsistency at entry 10 L113/L121)")
P("HEADLINE", "CLOSURE_SCALING_FAILS")
