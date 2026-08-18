"""Receipt: verify the paper's Eqs (1)-(6) (Landau-Lifshitz rotating-frame mechanics) with sympy.
Claims checked: Lagrangian (1); momentum p = m v + m Omega x r = p0 (4);
energy E = E0 - M.Omega (6); equation of motion (3) incl. centrifugal magnitude m Omega^2 rho."""
import sympy as sp
t = sp.symbols('t'); m = sp.symbols('m', positive=True)
rx, ry, rz = [sp.Function(s)(t) for s in ('rx','ry','rz')]
Wx, Wy, Wz = sp.symbols('Wx Wy Wz')          # constant Omega for (3)-(6) checks
r = sp.Matrix([rx, ry, rz]); W = sp.Matrix([Wx, Wy, Wz])
v = r.diff(t)
U = sp.Function('U')(rx, ry, rz)
cross = lambda a, b: sp.Matrix([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]])
# Eq (1): L in rotating frame from L0 with v0 = v + W x r
v0 = v + cross(W, r)
L0 = m/2 * (v0.T*v0)[0] - U
L1_claim = m/2*(v.T*v)[0] + m*(v.T*cross(W, r))[0] + m/2*(cross(W, r).T*cross(W, r))[0] - U
print("Eq(1) L expansion matches:", sp.simplify(sp.expand(L0 - L1_claim)) == 0)
# Eq (4): p = dL/dv = m v + m W x r  and equals m v0
p = sp.Matrix([sp.diff(L1_claim, v[i]) for i in range(3)])
print("Eq(4) p = m v + m Wxr:", sp.simplify(p - (m*v + m*cross(W, r))) == sp.zeros(3, 1))
print("Eq(4) p = m v0 (= p0):", sp.simplify(p - m*v0) == sp.zeros(3, 1))
# Eq (6): E = p.v - L = E0 - M.W with M = r x p, E0 = m v0^2/2 + U
E = (p.T*v)[0] - L1_claim
E0 = m/2*(v0.T*v0)[0] + U
M = cross(r, p)
print("Eq(6) E = E0 - M.W:", sp.simplify(E - (E0 - (M.T*W)[0])) == 0)
# Eq (3): Euler-Lagrange gives m dv/dt = -dU/dr - 2 m W x v - m W x (W x r)  (alpha=0 here)
EL = sp.Matrix([sp.diff(sp.Matrix([sp.diff(L1_claim, v[i]) for i in range(3)])[i], t)
                - sp.diff(L1_claim, r[i]) for i in range(3)])
acc = m*v.diff(t)
rhs = -sp.Matrix([sp.diff(U, r[i]) for i in range(3)]) - 2*m*cross(W, v) - m*cross(W, cross(W, r))
print("Eq(3) m dv/dt = -dU/dr - 2mWxv - mWx(Wxr):", sp.simplify(EL - (acc - rhs)) == sp.zeros(3, 1))
# centrifugal magnitude: with W = (0,0,W3), |W x (W x r)| = W3^2 * rho, rho = sqrt(rx^2+ry^2)
W3 = sp.symbols('W3', positive=True)
Wz_only = sp.Matrix([0, 0, W3])
cf = -cross(Wz_only, cross(Wz_only, r))
mag = sp.sqrt((cf.T*cf)[0])
rho = sp.sqrt(rx**2 + ry**2)
print("centrifugal |F|/m = W^2 rho:", sp.simplify(mag - W3**2*rho) == 0)
