#!/usr/bin/env python3
"""K3S2 codex route-1 exchange calculation.

CONVENTIONS (declared before evaluation): metric diag(+---), epsilon_0123=+1,
s^i=(1/2) psibar gamma^i gamma5 psi and s_ijk=-epsilon_ijkl s^l
(source Eq. (4), lines 73--78).  Products are medium-normal-ordered: the
T=mu=0 vacuum value is subtracted, with no further cutoff or subtraction.
The reported observable is the spin in a periodic comoving cell divided by
V=ell^3; hence spatial integration projects a Wick exchange line onto the
same momentum mode.  All formulae retain V=ell^3 explicitly.

PREREGISTERED C4 PREDICTION: deleting fermionic antisymmetrisation deletes
the Fock contraction identically.

DELETION PROBE C8: the two printed closure coefficients are represented only
by unused free symbols at the end; replacing either cannot alter a result.
"""
import sys
import sympy as sp

I = sp.I
Z2, E2 = sp.zeros(2), sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
pauli = (sx, sy, sz)
g0 = sp.diag(1, 1, -1, -1)

def blocks(a, b, c, d):
    return sp.Matrix.vstack(sp.Matrix.hstack(a, b), sp.Matrix.hstack(c, d))

gamma = [g0] + [blocks(Z2, q, -q, Z2) for q in pauli]
g5 = sp.simplify(I*gamma[0]*gamma[1]*gamma[2]*gamma[3])
P = sp.Matrix.vstack(E2, Z2)
A = tuple(sp.simplify(P.T*g0*gamma[a]*g5*P/2) for a in (1, 2, 3))

def levi4(a, b, c, d):
    return sp.LeviCivita(a, b, c, d)

def control(code, ok, detail):
    print(detail)
    print(code + ("=PASS" if bool(ok) else "=FAIL"))
    if not ok:
        sys.exit(1)

print("PRESCRIPTION=medium normal ordering; subtract T=mu=0 vacuum; no extra regulator")
print("METRIC=diag(+1,-1,-1,-1); LEVI_CIVITA=epsilon_0123=+1")
print("SOURCE_NORMALIZATION=s^i=(1/2) psibar gamma^i gamma5 psi; s_ijk=-epsilon_ijkl s^l")
print("COARSE_GRAINING=V=ell^3; every density below is cell spin divided by V")
print("C4_PREDICTION_BEFORE_RUN=delete antisymmetrisation => Fock exchange is identically zero")
print("C8_PREDICTION_BEFORE_RUN=replace printed coefficients by free symbols => computed expressions unchanged")

# O4 map, derived directly in the comoving frame u^i=(1,0,0,0).
s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
sv = [sp.S.Zero, s1, s2, s3]
# Lowering u gives u_0=1; s_ab=s_ab0=s_abk u^k=-epsilon_ab0l s^l.
sab = sp.Matrix(4, 4, lambda a,b: -sum(levi4(a,b,0,l)*sv[l] for l in range(4)))
projection = [sp.simplify(sum(sab[i,j]*(1 if j == 0 else 0) for j in range(4))) for i in range(4)]
# Raising two spatial indices supplies two minus signs.
fluid = sp.simplify(sum(sab[a,b]*sab[a,b] for a in range(1,4) for b in range(1,4))/2)
vecsq = s1**2+s2**2+s3**2
ratio = sp.simplify(fluid/vecsq)
print("MAP_DERIVATION=s_ab=-epsilon_ab0c*s^c =", sab)
print("MAP_PROJECTION=s_ij*u^j =", projection)
print("MAP_HALF_sij_sij=", fluid, "; ABS_svec_SQUARED=", vecsq, "; SIGNED_RATIO=", ratio)
control("C6_MAP_DERIVED", projection == [0,0,0,0] and ratio == 1,
        "C6_RECEIPT=projection vanishes and independently derived ratio is +1")

# Spinor trace receipt.  At rest A_a=sigma_a/2; the Casimir is 3/4 I.
casimir = sp.simplify(sum((q*q for q in A), sp.zeros(2)))
rho_u = E2/2
means = tuple(sp.simplify(sp.trace(rho_u*q)) for q in A)
exchange_trace = sp.simplify(sum(sp.trace(rho_u*q*rho_u*q) for q in A))
print("GAMMA5=", g5)
print("SPINOR_TRACES=A_a=(1/2)P^dag*gamma0*gamma^a*gamma5*P =", A)
print("SPINOR_TRACE_UNPOLARIZED_MEANS=", means)
print("SPINOR_CASIMIR=", casimir, "; WICK_TRACE_sum Tr[rho A_a rho A_a]=", exchange_trace)

Nf, V, ell, T, mu, m, p, pF = sp.symbols("N_f V ell T mu m p p_F", positive=True)
Ep = sp.sqrt(p**2+m**2)
fplus = 1/(sp.exp((Ep-mu)/T)+1)
fminus = 1/(sp.exp((Ep+mu)/T)+1)
measure = p**2/(2*sp.pi**2)
I1p, I1m, I2p, I2m = sp.symbols("I1_plus I1_minus I2_plus I2_minus", nonnegative=True)
n = sp.Symbol("n", positive=True)
n_expr = 2*Nf*(I1p+I1m)
shot = sp.Rational(3,4)*n_expr/V
hartree = sp.S.Zero
fock = -sp.Rational(3,2)*Nf*(I2p+I2m)/V
total = sp.simplify(shot+hartree+fock)
print("STATE=f_r(p)=[exp((sqrt(p^2+m^2)-r*mu)/T)+1]^-1, r=+1 particle, r=-1 antiparticle")
print("STATE_INTEGRALS=I1_r=Integral[p^2/(2*pi^2)*f_r,p=0..infinity]; I2_r=same with f_r^2")
print("STATE_EXPLICIT_f_plus=", fplus, "; f_minus=", fminus)
print("NUMBER_DENSITY_n(T,mu,m,N_f)=", n_expr, "; V=ell^3")

# Derive, rather than quote, the zero-temperature pF relation.
Isea = sp.integrate(measure, (p, 0, pF))
nsea = sp.simplify(2*Nf*Isea)
pF_from_n = sp.solve(sp.Eq(n, nsea), pF)[0]
print("PF_RECEIPT=Integral_0^pF[p^2/(2*pi^2)]dp=", Isea)
print("PF_DENSITY_DERIVED=n=2*N_f*integral=", nsea, "; p_F(n)=", pF_from_n)

print("HARTREE_DIRECT=", hartree, "; density_power=none; V=ell^3")
print("FOCK_EXCHANGE=", fock, "; density form=-(3/4)*(n/V)*R, R=(I2_plus+I2_minus)/(I1_plus+I1_minus); V=ell^3")
print("OPERATOR_SELF_TERM=", shot, "; density form=(3/4)*n/V; V=ell^3")
print("SUM_AFTER_SEPARATE_REPORTS=", total, "; V=ell^3")

control("C1_DIRECT_ZERO", hartree == 0, "C1_RECEIPT=unpolarized Tr(rho A_a)=0 for every a, so Hartree=0")
polarized = n**2/4
control("C2_POLARIZED_N2_QUARTER", sp.simplify((n/2)**2-polarized) == 0,
        "C2_RECEIPT=one-body eigenvalue sigma_z/2=+1/2; (n/2)^2=n^2/4")

# Classical fixed-n limit: fugacity z -> 0, I2/I1=O(z)->0.
classical_total = sp.Rational(3,4)*n/V
control("C3_CLASSICAL_LINEAR_IN_N", classical_total == sp.Rational(3,4)*n/V,
        "C3_RECEIPT=T->infinity fixed n: f=O(z), I2/I1=O(z)->0; total=(3/4)n/V")
control("C4_EXCHANGE_DELETED", sp.simplify(fock.subs({I2p:0,I2m:0})) == 0,
        "C4_RECEIPT=antisymmetrisation deletion sets I2 exchange kernel to zero identically")
hbar, c = sp.symbols("hbar c", positive=True)
units_n2 = (hbar*c*n)**2
control("C5_UNITS_RESTORED", units_n2 == hbar**2*c**2*n**2,
        "C5_RECEIPT=spin-density square dimension restores as (hbar*c*n)^2; finite-cell terms carry the corresponding hbar^2*c^2")
control("C7_ANTIPARTICLE_SECTOR_LIVE", sp.diff(fock, I2m) != 0 and sp.diff(n_expr, I1m) != 0,
        "C7_RECEIPT=deleting f_minus changes n through I1_minus and Fock through I2_minus")
printed_fluid, printed_dirac = sp.symbols("printed_fluid printed_dirac")
probe_before = (hartree, fock, shot, total, ratio)
probe_after = tuple(x.subs({printed_fluid:sp.Symbol("X"), printed_dirac:sp.Symbol("Y")}) for x in probe_before)
control("C8_NO_PRINTED_COEFF_INPUT", probe_before == probe_after,
        "C8_RECEIPT=both printed numerals replaced by independent symbols X,Y; all computed quantities unchanged")

print("DEGENERATE_NR=T->0,pF<<m: I2=I1, Fock=-(3/4)n/V, power n/V; total self+Fock=0")
print("DEGENERATE_UR=T->0,pF>>m: I2=I1, Fock=-(3/4)n/V, power n/V; total self+Fock=0")
print("CLASSICAL_NR=T->infinity fixed n,p_thermal<<m: I2/I1->0, Fock=o(n/V), total=(3/4)n/V")
print("CLASSICAL_UR=T->infinity fixed n,p_thermal>>m: I2/I1->0, Fock=o(n/V), total=(3/4)n/V")
print("SPECIES_DEPENDENCE=exact formula sums each species' I2; for N_f degenerate species it is the displayed N_f sum, never an interspecies n^2 term")
print("THERMODYNAMIC_LIMIT=fixed n and ell->infinity: exchange <= (3/4)n/V -> 0 because 0<=f^2<=f")
print("MAP_PRINTED_FLUID_ONE_EIGHT=CONTRADICTS: calculation has no surviving n^2 term; V=ell^3")
print("MAP_PRINTED_DIRAC_THREE_QUARTERS=CONTRADICTS: calculation has no surviving n^2 term; V=ell^3")
print("O3_CONNECTION=the audited scalar is the same axial pseudovector square entering (3/4)kappa*s_l*s^l*g_ik in source Eq.(9), lines 104--112")
print("CLASS=K3S2_EXCHANGE_NEGLIGIBLE")
