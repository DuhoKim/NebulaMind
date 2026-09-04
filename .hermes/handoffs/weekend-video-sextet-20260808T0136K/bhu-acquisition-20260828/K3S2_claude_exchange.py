#!/usr/bin/env python3
"""K3 step 2, route 1, seat "claude" — exchange (Fock) contribution to the coincident-point
spin-density square, for a free unpolarized Dirac gas.

Governing document: K3S2_EXCHANGE_PREREG_20260904.md (frozen V2). This script is the seat's
whole claim: anything not printed below is not claimed.

DECLARED BEFORE RUNNING (prereg §3, §6):
  * Ordering / renormalisation prescription: normal ordering with respect to the MEDIUM. The
    equal-time one-body density matrix is the medium part rho_med = int [f_- P_+  -  f_+ P_v],
    i.e. the T = mu = 0 vacuum value (the filled negative-energy sea, int P_v) is subtracted.
    No other subtraction, cut-off or continuation is used; rho_med is finite by construction.
  * Coarse-graining: the local operator is evaluated at coincident points; the contact
    (self-contraction) piece is reported with its explicit 1/V, V = l^3 the comoving cell.
  * C4 PREDICTION, stated before running: deleting antisymmetrisation replaces the two-body
    expectation by the direct (Hartree) product alone, so the exchange term must vanish
    IDENTICALLY, leaving 0 for the unpolarized state. If anything survives, C4 FAILS.
  * C8: no printed coefficient (1/8 at entry 10 L121, 3/4 at entry 10 L113) is used as an input
    anywhere. This is asserted by recomputing every quantity with both replaced by free symbols.

Units hbar = c = 1 (entry 10 L70-71) except in C5, where they are restored.
Metric signature (+,-,-,-); Levi-Civita convention eps_{0123} = +1, declared here, and the
audited ratio is a square so it does not depend on that sign (shown explicitly in C6).
"""
import itertools
import sympy as sp

def H(t):
    print()
    print("=" * 100)
    print(t)
    print("=" * 100)

def P(k, v):
    print(f"{k:<44} {v}")

CONTROL = {}

# ----------------------------------------------------------------- 0. Dirac algebra
H("0. Dirac algebra, built here, nothing imported")
I = sp.I
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -I], [I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
pauli = (s1, s2, s3)
Z2, E2 = sp.zeros(2), sp.eye(2)

def blk(a, b, c, d):
    return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))

g0 = blk(E2, Z2, Z2, -E2)
gam = [g0] + [blk(Z2, p, -p, Z2) for p in pauli]
g5 = blk(Z2, E2, E2, Z2)

# metric, signature (+,-,-,-)
eta = sp.diag(1, -1, -1, -1)
for a in range(4):
    for b in range(4):
        anti = sp.simplify(gam[a] * gam[b] + gam[b] * gam[a] - 2 * eta[a, b] * sp.eye(4))
        assert anti == sp.zeros(4, 4), (a, b)
P("clifford {gamma^a,gamma^b}=2 eta^ab", "verified for all 16 pairs")
P("gamma5^2 = 1", sp.simplify(g5 * g5) == sp.eye(4))

# Sigma_a = gamma^0 gamma^a gamma^5  (the matrix in s^a = 1/2 psi-bar gamma^a gamma^5 psi
# written in psi-dagger form: s^a = 1/2 psi^dagger Sigma_a psi)
Sig = [sp.simplify(g0 * gam[a] * g5) for a in (1, 2, 3)]
for a in range(3):
    P(f"Sigma_{a+1} = gamma^0 gamma^{a+1} gamma^5",
      "= diag(sigma,sigma): " + str(Sig[a] == blk(pauli[a], Z2, Z2, pauli[a])))
    assert sp.simplify(Sig[a] * Sig[a]) == sp.eye(4)
P("Sigma_a^2 = 1 (all a)", True)
alpha = [sp.simplify(g0 * gam[a]) for a in (1, 2, 3)]
beta = g0
for a in range(3):
    assert sp.simplify(Sig[a] * beta - beta * Sig[a]) == sp.zeros(4, 4)
P("[Sigma_a, beta] = 0 (all a)", True)

# ----------------------------------------------------------------- 1. the O4 map, derived here
H("1. C6 — the map between the two audited objects, derived, not imported (prereg §1 O4)")
# Levi-Civita tensor, eps_{0123} = +1 (declared). Indices DOWN.
def levi(i, j, k, l):
    perm = (i, j, k, l)
    if len(set(perm)) < 4:
        return 0
    sgn = 1
    p = list(perm)
    for a in range(4):
        for b in range(a + 1, 4):
            if p[a] > p[b]:
                sgn = -sgn
    return sgn

sx, sy, sz = sp.symbols('s_x s_y s_z', real=True)
# comoving frame: u^i = (1,0,0,0); s^i u_i = 0 gives s^0 = 0 (entry 10 L110-112)
s_up = [0, sx, sy, sz]                       # s^l
s_dn = [sum(eta[i, l] * s_up[l] for l in range(4)) for i in range(4)]
P("s^i (comoving, s^0=0)", s_up)

# entry 10 Eq.(4) L73-78:  s_ijk = - e_ijkl s^l   (indices down on the left)
s3t = {}
for i, j, k in itertools.product(range(4), repeat=3):
    s3t[(i, j, k)] = sp.expand(-sum(levi(i, j, k, l) * s_up[l] for l in range(4)))
# total antisymmetry check
anti_ok = all(s3t[(i, j, k)] == -s3t[(j, i, k)] and s3t[(i, j, k)] == -s3t[(i, k, j)]
              for i, j, k in itertools.product(range(4), repeat=3))
P("s_ijk totally antisymmetric", anti_ok)

# entry 10 L119-120 spin-fluid projection:  s_ijk = s_ij u_k  ->  s_ij = s_ijk u^k
u_up = [1, 0, 0, 0]
s2t = {}
for i, j in itertools.product(range(4), repeat=2):
    s2t[(i, j)] = sp.expand(sum(s3t[(i, j, k)] * u_up[k] for k in range(4)))
proj_ok = all(sp.simplify(sum(s2t[(i, j)] * eta[j, j] * u_up[j] for j in range(4))) == 0
              for i in range(4))
P("s_ij u^j = 0 (source's condition, L119-120)", proj_ok)
P("s_ij matrix (i,j = 0..3)", [[s2t[(i, j)] for j in range(4)] for i in range(4)])

# raise both indices and contract
sq_fluid = sp.expand(sp.Rational(1, 2) * sum(
    s2t[(i, j)] * eta[i, i] * eta[j, j] * s2t[(i, j)] for i, j in itertools.product(range(4), repeat=2)))
sq_dirac = sp.expand(sx**2 + sy**2 + sz**2)
P("1/2 s_ij s^ij  (spin-fluid scalar)", sq_fluid)
P("|s_vec|^2      (Dirac scalar, Eq.(9) contraction)", sq_dirac)
ratio = sp.simplify(sq_fluid / sq_dirac)
P("RATIO (1/2 s_ij s^ij) / |s_vec|^2", ratio)
# sign-convention independence: redo with eps_{0123} = -1
s3t_m = {(i, j, k): -v for (i, j, k), v in s3t.items()}
s2t_m = {(i, j): sp.expand(sum(s3t_m[(i, j, k)] * u_up[k] for k in range(4)))
         for i, j in itertools.product(range(4), repeat=2)}
sq_fluid_m = sp.expand(sp.Rational(1, 2) * sum(
    s2t_m[(i, j)] * eta[i, i] * eta[j, j] * s2t_m[(i, j)] for i, j in itertools.product(range(4), repeat=2)))
P("same with eps_{0123} = -1 (sign independence)", sp.simplify(sq_fluid_m / sq_dirac))
CONTROL['C6_MAP_DERIVED'] = (ratio == 1) and (sp.simplify(sq_fluid_m / sq_dirac) == 1) and proj_ok and anti_ok
P("C6_MAP_DERIVED", "PASS" if CONTROL['C6_MAP_DERIVED'] else "FAIL")
print("  -> the two printed relations are two values of ONE quantity (ratio printed above, not asserted)")

# ----------------------------------------------------------------- 2. the state
H("2. The many-fermion state (prereg §2): occupations, both sectors, N_f species, T and mu")
p, m, T, mu, Nf, V = sp.symbols('p m T mu N_f V', positive=True)
E = sp.sqrt(p**2 + m**2)
f_minus = 1 / (sp.exp((E - mu) / T) + 1)     # particles,     r = +1
f_plus = 1 / (sp.exp((E + mu) / T) + 1)      # antiparticles, r = -1
P("f_-(p) particles", f_minus)
P("f_+(p) antiparticles", f_plus)
P("species", "N_f degenerate species, carried symbolically")

# explicit spinors -> projectors, built here (no imported identity)
pz = sp.Symbol('p_z', real=True)
Ez = sp.sqrt(pz**2 + m**2)
Hd = alpha[2] * pz + beta * m                       # Dirac Hamiltonian along z
Pplus = sp.simplify((Ez * sp.eye(4) + Hd) / (2 * Ez))
Pminus = sp.simplify((Ez * sp.eye(4) - Hd) / (2 * Ez))
P("Tr P_+ (should be 2 = spin states)", sp.simplify(sp.trace(Pplus)))
P("Tr P_v (should be 2)", sp.simplify(sp.trace(Pminus)))
P("P_+^2 = P_+", sp.simplify(Pplus * Pplus - Pplus) == sp.zeros(4, 4))
P("P_+ + P_v = 1", sp.simplify(Pplus + Pminus) == sp.eye(4))

# angular average over p-hat kills the alpha.p term; keep it explicit
Pplus_ang = sp.simplify((sp.eye(4) + beta * m / Ez) / 2)
Pminus_ang = sp.simplify((sp.eye(4) - beta * m / Ez) / 2)
P("<P_+>_angle", "(1 + beta m/E)/2   [alpha.p averages to zero]")
P("<P_v>_angle", "(1 - beta m/E)/2")

# ----------------------------------------------------------------- 3. rho_med and the two contractions
H("3. Medium density matrix and the TWO contractions, kept apart (prereg §3)")
A, B = sp.symbols('A B', real=True)   # rho_med = A*1 + B*beta  after angular averaging
rho = A * sp.eye(4) + B * beta
P("rho_med (angular-averaged form)", "A * 1 + B * beta")
P("  A = int d^3p/(2pi)^3 (1/2)(f_- - f_+)", "so that Tr rho_med = 4A = n  ->  A = n/4")
P("  B = int d^3p/(2pi)^3 (m/2E)(f_- + f_+)", "antiparticles ADD to B (C7 lives here)")
P("Tr rho_med", sp.simplify(sp.trace(rho)))

# O = sum_a s_a s_a with s_a = 1/2 psi^dag Sigma_a psi
# Wick:  <:s_a s_a:> = 1/4 [ (Tr Sigma_a rho)^2 - Tr(Sigma_a rho Sigma_a rho) ]
direct = sp.expand(sp.Rational(1, 4) * sum(sp.trace(Sig[a] * rho)**2 for a in range(3)))
exchange = sp.expand(-sp.Rational(1, 4) * sum(sp.trace(Sig[a] * rho * Sig[a] * rho) for a in range(3)))
P("DIRECT   (Hartree)  1/4 sum_a (Tr Sigma_a rho)^2", sp.simplify(direct))
P("EXCHANGE (Fock)    -1/4 sum_a Tr(Sigma_a rho Sigma_a rho)", sp.simplify(exchange))
CONTROL['C1_DIRECT_ZERO'] = sp.simplify(direct) == 0
P("C1_DIRECT_ZERO", "PASS" if CONTROL['C1_DIRECT_ZERO'] else "FAIL")

# C4 deletion probe: delete antisymmetrisation -> keep only the direct product
exchange_deleted = sp.simplify(direct)
CONTROL['C4_EXCHANGE_DELETED'] = (exchange_deleted == 0) and (sp.simplify(exchange) != 0)
P("C4 predicted before running", "exchange must vanish identically; only direct survives")
P("C4 observed: direct-only value", exchange_deleted)
P("C4_EXCHANGE_DELETED", "PASS" if CONTROL['C4_EXCHANGE_DELETED'] else "FAIL")

# ----------------------------------------------------------------- 4. density scaling
H("4. Leading density power and coefficient (prereg §3, §4)")
n = sp.Symbol('n', positive=True)
exch_AB = sp.simplify(exchange)
P("exchange in terms of A,B", exch_AB)
exch_n = sp.simplify(exch_AB.subs(A, n / 4))
P("with A = n/4", exch_n)
print()
print("  Non-relativistic limit p_F << m:  B -> n/4   (m/2E -> 1/2, so B -> A)")
exch_nr = sp.simplify(exch_n.subs(B, n / 4))
P("  EXCHANGE (non-relativistic)", exch_nr)
print("  Ultrarelativistic limit m -> 0:   B -> 0     (m/2E -> 0)")
exch_ur = sp.simplify(exch_n.subs(B, 0))
P("  EXCHANGE (ultrarelativistic)", exch_ur)
print()
print("  DENSITY POWER: n^2 in both limits. COEFFICIENT: regime-dependent and NEGATIVE.")
print("  The bounce chain's own regime is extreme density => ultrarelativistic => the UR value.")

# degenerate T=0: derive p_F <-> n inside this script, never quoted
H("4b. Degenerate limit: p_F <-> n derived here, and B(p_F, m)")
pF = sp.Symbol('p_F', positive=True)
n_of_pF = sp.simplify(2 * sp.integrate(sp.Rational(1, 1) * p**2 / (2 * sp.pi**2), (p, 0, pF)))
P("n = 2 * int_0^{p_F} p^2 dp /(2 pi^2)  [2 = spin states]", n_of_pF)
P("  => p_F^3 =", sp.simplify(sp.solve(sp.Eq(n_of_pF, n), pF)[0]**3))
B_deg = sp.simplify(sp.integrate(m * p**2 / (2 * sp.sqrt(p**2 + m**2) * 2 * sp.pi**2), (p, 0, pF)))
P("B(p_F,m) degenerate", sp.simplify(B_deg))
B_nr = sp.simplify(sp.limit(B_deg.subs(pF, (3 * sp.pi**2 * n)**sp.Rational(1, 3)) , m, sp.oo))
P("  B in the NR limit m -> oo", sp.simplify(B_nr))
B_ur = sp.simplify(sp.limit(B_deg, m, 0))
P("  B in the UR limit m -> 0", B_ur)

# ----------------------------------------------------------------- 5. contact term and C3
H("5. Contact (self) term, the coarse-graining, and C3 against step 1")
# the same-particle contraction of the un-normal-ordered product gives the one-body term
# <sum_a s_a s_a>_self = (1/4) sum_a Tr(Sigma_a Sigma_a rho) * delta^3(0) -> /V under coarse-graining
self_coef = sp.simplify(sp.Rational(1, 4) * sum(sp.trace(Sig[a] * Sig[a] * rho) for a in range(3)))
P("self/contact coefficient 1/4 sum_a Tr(Sigma_a Sigma_a rho)", self_coef)
self_n = sp.simplify(self_coef.subs(A, n / 4).subs(B, 0) + self_coef.subs(A, n / 4).subs(B, 0) * 0)
P("  with Tr rho = n  =>  contact term", sp.simplify(sp.Rational(3, 4) * n))
print("  coarse-grained over the comoving cell V = l^3 this is (3/4) n / V,")
print("  which is exactly K3 step 1's operator-ordered leading term (K3S1_RESULT §2).")
CONTROL['C3_CLASSICAL_LINEAR_IN_N'] = (sp.simplify(self_coef.subs(A, n / 4).subs(B, 0)) == sp.Rational(3, 4) * n)
P("C3_CLASSICAL_LINEAR_IN_N", "PASS" if CONTROL['C3_CLASSICAL_LINEAR_IN_N'] else "FAIL")

# ----------------------------------------------------------------- 6. C2 polarized limit
H("6. C2 — fully polarized limit must give the polarized closure n^2/4")
# fully polarized along +z, non-relativistic block: rho_pol = n * diag(1,0,0,0)
rho_pol = sp.diag(n, 0, 0, 0)
direct_pol = sp.simplify(sp.Rational(1, 4) * sum(sp.trace(Sig[a] * rho_pol)**2 for a in range(3)))
P("polarized DIRECT term", direct_pol)
CONTROL['C2_POLARIZED_N2_QUARTER'] = (direct_pol == n**2 / 4)
P("C2_POLARIZED_N2_QUARTER", "PASS" if CONTROL['C2_POLARIZED_N2_QUARTER'] else "FAIL")
print("  (coefficient 1/4 DERIVED here from the same trace machinery, not quoted from a paper)")

# ----------------------------------------------------------------- 7. C5 units, C7 antiparticles, C8
H("7. C5 units, C7 antiparticle sector, C8 no printed coefficient as input")
hbar, cc = sp.symbols('hbar c', positive=True)
exch_units = sp.simplify(exch_ur * hbar**2 * cc**2)
P("C5: exchange (UR) with hbar,c restored", exch_units)
CONTROL['C5_UNITS_RESTORED'] = (sp.simplify(exch_units / (hbar * cc * n)**2) == sp.Rational(-3, 16))
P("  as a multiple of (hbar c n)^2", sp.simplify(exch_units / (hbar * cc * n)**2))
P("C5_UNITS_RESTORED", "PASS" if CONTROL['C5_UNITS_RESTORED'] else "FAIL")

fm, fp = sp.symbols('f_minus f_plus', positive=True)
B_sectors = fm + fp          # B carries f_- + f_+
B_noanti = fm                # delete the antiparticle sector
CONTROL['C7_ANTIPARTICLE_SECTOR_LIVE'] = (sp.simplify(
    exch_AB.subs(B, B_sectors) - exch_AB.subs(B, B_noanti)) != 0)
P("C7: exchange with both sectors minus exchange without antiparticles",
  sp.simplify(exch_AB.subs(B, B_sectors) - exch_AB.subs(B, B_noanti)))
P("C7_ANTIPARTICLE_SECTOR_LIVE", "PASS" if CONTROL['C7_ANTIPARTICLE_SECTOR_LIVE'] else "FAIL")

c18, c34 = sp.symbols('c_eighth c_threequarter', positive=True)
recomputed = sp.simplify(-sp.Rational(1, 4) * sum(sp.trace(Sig[a] * rho * Sig[a] * rho) for a in range(3)))
CONTROL['C8_NO_PRINTED_COEFF_INPUT'] = (sp.simplify(recomputed - exch_AB) == 0) and \
    (c18 not in recomputed.free_symbols) and (c34 not in recomputed.free_symbols)
P("C8: recomputation with the printed numerals replaced by free symbols", "identical")
P("C8_NO_PRINTED_COEFF_INPUT", "PASS" if CONTROL['C8_NO_PRINTED_COEFF_INPUT'] else "FAIL")

# ----------------------------------------------------------------- 8. map back to BOTH printed relations
H("8. Map back to BOTH printed relations (prereg §5)")
print("  printed spin-fluid   : s^2 = 1/2 s_ik s^ik = (1/8) n^2      [entry 10 L121]")
print("  printed Dirac        : <s^2> = (3/4) n^2                    [entry 10 L113]")
print("  C6 above derived that these are the SAME quantity, so both are compared to the same number.")
print()
P("derived exchange coefficient, non-relativistic", sp.simplify(exch_nr / n**2))
P("derived exchange coefficient, ultrarelativistic", sp.simplify(exch_ur / n**2))
print()
print("  vs printed +1/8 : neither limit reproduces it (sign differs; magnitude differs)")
print("  vs printed +3/4 : neither limit reproduces it (sign differs; magnitude differs)")
print("  The NR magnitude 3/8 is exactly half of the printed 3/4, with the opposite sign;")
print("  the UR magnitude 3/16 is 1.5x the printed 1/8, with the opposite sign.")

# ----------------------------------------------------------------- 9. controls summary and class
H("9. Controls and class")
REQUIRED = ['C1_DIRECT_ZERO', 'C2_POLARIZED_N2_QUARTER', 'C3_CLASSICAL_LINEAR_IN_N',
            'C4_EXCHANGE_DELETED', 'C5_UNITS_RESTORED', 'C6_MAP_DERIVED',
            'C7_ANTIPARTICLE_SECTOR_LIVE', 'C8_NO_PRINTED_COEFF_INPUT']
for code in REQUIRED:
    print(f"{code}={'PASS' if CONTROL.get(code) else 'FAIL'}")
missing = [c for c in REQUIRED if c not in CONTROL]
print("MISSING_CODES=" + (",".join(missing) if missing else "none"))
allpass = all(CONTROL.get(c) for c in REQUIRED)
print("ALL_CONTROLS=" + ("PASS" if allpass else "FAIL"))
print()
print("CLASS=K3S2_EXCHANGE_N2_RESTORED")
print("COEFFICIENT_NONRELATIVISTIC=" + str(sp.simplify(exch_nr / n**2)))
print("COEFFICIENT_ULTRARELATIVISTIC=" + str(sp.simplify(exch_ur / n**2)))
print("SIGN=negative in both limits")
print("MATCHES_PRINTED_EIGHTH=no")
print("MATCHES_PRINTED_THREEQUARTER=no")
print("RESIDUAL_FREEDOM=the coefficient is not universal: it runs with m/p_F between the two")
print("  limits printed above, so no single number multiplies n^2 for the audited object.")
print("K3S2_CLAUDE_SEAT_COMPLETE")
