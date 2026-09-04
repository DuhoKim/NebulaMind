#!/usr/bin/env python3
"""Tori's own verification of the two contested algebra claims in K3 step 2.

CLAIM A (third seat, against codex): the per-momentum spinor trace
    sum_a Tr( Sigma_a P_+(p) Sigma_a P_+(p) )  =  2 + 4 m^2 / E^2,
i.e. it DEPENDS on p and may not be pulled out of the momentum integral as a constant.

CLAIM B (Tori's own seat): for an ISOTROPIC medium the integrated density matrix has no
alpha.p piece, so rho_med = A*1 + B*beta exactly, and therefore
    -1/4 sum_a Tr(Sigma_a rho Sigma_a rho)  =  -3 (A^2 + B^2)
with no angular-averaging shortcut needed. Verified here WITHOUT assuming it: the full
alpha.p term is kept, the angular integral is done explicitly, and the result compared.
"""
import sympy as sp

I = sp.I
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -I], [I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
pauli = (s1, s2, s3)
Z2, E2 = sp.zeros(2), sp.eye(2)
blk = lambda a, b, c, d: sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
g0 = blk(E2, Z2, Z2, -E2)
gam = [g0] + [blk(Z2, p, -p, Z2) for p in pauli]
g5 = blk(Z2, E2, E2, Z2)
Sig = [sp.simplify(g0 * gam[a] * g5) for a in (1, 2, 3)]
alph = [sp.simplify(g0 * gam[a]) for a in (1, 2, 3)]
beta = g0

print("=" * 90)
print("CLAIM A — per-momentum trace")
print("=" * 90)
px, py, pz, m = sp.symbols('p_x p_y p_z m', real=True)
p2 = px**2 + py**2 + pz**2
E = sp.sqrt(p2 + m**2)
Pp = (E * sp.eye(4) + (alph[0] * px + alph[1] * py + alph[2] * pz) + beta * m) / (2 * E)
tr = sp.simplify(sum(sp.trace(Sig[a] * Pp * Sig[a] * Pp) for a in range(3)))
tr = sp.simplify(sp.expand(tr))
print("sum_a Tr(Sigma_a P_+ Sigma_a P_+) =", sp.simplify(tr))
target = 2 + 4 * m**2 / E**2
print("claimed 2 + 4 m^2/E^2            =", sp.simplify(target))
claimA = sp.simplify(sp.expand(tr - target)) == 0
print("CLAIM_A_VERIFIED =", claimA)
print("  depends on p?  ", sp.simplify(sp.diff(sp.simplify(tr), px)) != 0)
print("  value at p=0   ", sp.simplify(tr.subs({px: 0, py: 0, pz: 0})))
print("  value at m=0   ", sp.simplify(tr.subs(m, 0)))
print("  -> it is 6 at p=0 and 2 at m=0, so it is NOT a constant and may not leave the integral")

print()
print("=" * 90)
print("CLAIM B — the integrated density matrix, with the alpha.p term kept explicitly")
print("=" * 90)
p, th, ph = sp.symbols('p theta phi', positive=True)
f = sp.Function('f')(p)
# full P_+(p) in spherical components, no angular average assumed
pxs = p * sp.sin(th) * sp.cos(ph)
pys = p * sp.sin(th) * sp.sin(ph)
pzs = p * sp.cos(th)
Es = sp.sqrt(p**2 + m**2)
Pp_s = (Es * sp.eye(4) + (alph[0] * pxs + alph[1] * pys + alph[2] * pzs) + beta * m) / (2 * Es)
# integrate over solid angle only (the radial integral is the symbol A/B below)
ang = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        ang[i, j] = sp.simplify(sp.integrate(sp.integrate(Pp_s[i, j] * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi)))
ang = sp.simplify(ang / (4 * sp.pi))
print("angular average of P_+(p):")
sp.pprint(sp.simplify(ang))
noalpha = sp.simplify(ang - (sp.eye(4) / 2 + beta * m / (2 * Es)))
print("equals (1 + beta m/E)/2 exactly? ", noalpha == sp.zeros(4, 4))
print("  -> the alpha.p piece integrates to zero by isotropy; no shortcut was needed.")

A, B = sp.symbols('A B', real=True)
rho = A * sp.eye(4) + B * beta
exch = sp.simplify(-sp.Rational(1, 4) * sum(sp.trace(Sig[a] * rho * Sig[a] * rho) for a in range(3)))
print()
print("exchange with rho = A*1 + B*beta :", exch)
claimB = sp.simplify(exch + 3 * (A**2 + B**2)) == 0
print("CLAIM_B_VERIFIED =", claimB)

print()
print("=" * 90)
print("Cross-check: Object L coefficients, with N_f species carried")
print("=" * 90)
n, Nf = sp.symbols('n N_f', positive=True)
# per species A_s = n/(4 N_f); N_f species add
exch_species = sp.simplify(Nf * (-3) * ((n / (4 * Nf))**2 + (n / (4 * Nf))**2))
print("NR (B = A = n/(4 N_f)), summed over N_f species :", exch_species)
exch_species_ur = sp.simplify(Nf * (-3) * ((n / (4 * Nf))**2))
print("UR (B = 0),             summed over N_f species :", exch_species_ur)
print("  N_f = 1 reduces to  ", sp.simplify(exch_species.subs(Nf, 1)), "and", sp.simplify(exch_species_ur.subs(Nf, 1)))
print()
print("VERIFY_CLAIM_A=" + ("PASS" if claimA else "FAIL"))
print("VERIFY_CLAIM_B=" + ("PASS" if claimB else "FAIL"))
print("TORI_VERIFY_COMPLETE")
