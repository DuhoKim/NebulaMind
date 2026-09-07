"""Exact KS symmetry/kinematic checks; no evolution integration or matter closure.

Run from any directory: python3 /absolute/path/to/ks_spin_checks.py
Writes only the adjacent ks_spin_checks.txt. Requires SymPy.
All spatial matrices below use a positive orthonormal Euclidean metric.
"""
from pathlib import Path
import sympy as s

out = []
def emit(label, value):
    out.append(f"{label}: {value}")

t, r, th, ph = s.symbols("t r theta phi", real=True)
X, Y, T, m = [s.Function(z)(t) for z in ("X", "Y", "T", "m")]
coords = [t, r, th, ph]
g = s.diag(1, -X**2, -Y**2, -Y**2*s.sin(th)**2)
gi = g.inv()
G = [[[s.simplify(sum(gi[a,d]*(s.diff(g[d,c],coords[b])
                 +s.diff(g[d,b],coords[c])-s.diff(g[b,c],coords[d]))
                 for d in range(4))/2) for c in range(4)]
                 for b in range(4)] for a in range(4)]
HX, HY = s.diff(X,t)/X, s.diff(Y,t)/Y
H, D, K = (HX+2*HY)/3, HX-HY, 1/Y**2
beta = [1/T, 0, 0, 0]
db = s.Matrix(4,4,lambda a,b:s.simplify(s.diff(beta[b],coords[a])
                      -sum(G[c][a][b]*beta[c] for c in range(4))))
frame = s.diag(1,1/X,1/Y,1/(Y*s.sin(th)))
dbhat = s.simplify(frame*db*frame)
assert dbhat == dbhat.T
assert dbhat == s.diag(-s.diff(T,t)/T**2,-HX/T,-HY/T,-HY/T)
assert all(G[a][0][0] == 0 for a in range(4))
emit("KS covariant derivative beta in orthonormal frame", dbhat)
emit("thermal vorticity and comoving acceleration", "both identically zero")

q0,q1,q2,q3,q4,q5 = s.symbols("q0:6")
Q = s.Matrix([[q0,q1,q2],[q1,q3,q4],[q2,q4,q5]])
J = s.Matrix([[0,0,0],[0,0,-1],[0,1,0]])
constraints = s.solve(list(J*Q-Q*J),[q1,q2,q4,q5],dict=True)
assert constraints == [{q1:0,q2:0,q4:0,q5:q3}]
emit("SO(2)-invariant symmetric moment/stress", constraints)
mx,my,mz = s.symbols("mx my mz")
assert s.solve(list(J*s.Matrix([mx,my,mz])),[my,mz]) == {my:0,mz:0}
reflection = s.diag(1,-1,1)
assert reflection.det()*reflection*s.Matrix([mx,0,0]) == s.Matrix([-mx,0,0])
emit("connected symmetry mean / tangential reflection", "radial mean allowed / radial axial mean changes sign")

delta = s.symbols("Delta",real=True)
sigma = s.diag(2*delta/3,-delta/3,-delta/3)
S = s.Matrix([[0,0,0],[0,0,m],[0,-m,0]])
linear_stress = sigma*S.T + S*sigma.T
assert linear_stress == s.zeros(3)
emit("symmetric shear-spin product for radial spin", linear_stress)

# Exact spatial covariant divergence on R x S^2; do not confuse
# coordinate component derivatives with derivatives of an invariant tensor.
Sc = s.zeros(4)
Sc[2,3],Sc[3,2] = m*Y**2*s.sin(th),-m*Y**2*s.sin(th)
div = []
for a in range(1,4):
    v = 0
    for j in range(1,4):
        for k in range(1,4):
            v += (-gi[j,k])*(s.diff(Sc[a,j],coords[k])
                   -sum(G[b][k][a]*Sc[b,j]+G[b][k][j]*Sc[a,b]
                        for b in range(1,4)))
    div.append(s.simplify(v))
assert div == [0,0,0]
emit("D^j S_ij on KS spatial slice", div)
cov_time_S23 = s.simplify(s.diff(Sc[2,3],t)
        -sum(G[b][0][2]*Sc[b,3]+G[b][0][3]*Sc[2,b] for b in range(4)))
assert s.simplify(cov_time_S23/(Y**2*s.sin(th))-s.diff(m,t)) == 0
emit("projected Weyssenhoff Eq. (52)", "m_dot + (HX+2 HY)m = 0; conditional, without production")

# Local angular pattern from epsilon Q sigma, with normalization factored out.
nx,ny,nz = s.symbols("nx ny nz",real=True)
n = s.Matrix([nx,ny,nz])
v = s.simplify(n.cross(sigma*n))
assert v == s.Matrix([0,delta*nx*nz,-delta*nx*ny])
emit("n cross (sigma n)", v)
def angular_average(poly):
    result = 0
    for powers,coef in s.Poly(s.expand(poly),nx,ny,nz).terms():
        if any(k%2 for k in powers):
            continue
        # Uniform S^2 monomial moments; (-1)!! = 1.
        num = s.prod(s.factorial2(k-1) if k else 1 for k in powers)
        result += coef*num/s.factorial2(sum(powers)+1)
    return s.simplify(result)
mean = v.applyfunc(angular_average)
pattern_square = (v*v.T).applyfunc(angular_average)
assert mean == s.zeros(3,1)
assert pattern_square == s.diag(0,delta**2/15,delta**2/15)
emit("isotropic angular mean of response", mean)
emit("angular product of mean-response pattern, NOT physical spin covariance", pattern_square)
emit("mixed angular moment <v_y n_x n_z>", angular_average(v[1]*nx*nz))
emit("mixed angular moment <v_z n_x n_y>", angular_average(v[2]*nx*ny))

# Pauli algebra: the single-particle symmetrized rest-spin product is fixed.
pauli = [s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
for i in range(3):
    for j in range(3):
        assert s.simplify((pauli[i]*pauli[j]+pauli[j]*pauli[i])/8
                         -(s.eye(2)/4 if i==j else s.zeros(2))) == s.zeros(2)
emit("spin-1/2 rest operator check", "{s_i,s_j}/2 = hbar^2 delta_ij/4; does not fix two-particle/density correlations")

# Direct Einstein-tensor check, conventional R_mu_nu definition and +---.
Ric = s.Matrix(4,4,lambda a,b:s.simplify(sum(
    s.diff(G[c][a][b],coords[c])-s.diff(G[c][a][c],coords[b])
    +sum(G[c][c][d]*G[d][a][b]-G[c][b][d]*G[d][a][c] for d in range(4))
    for c in range(4))))
Rscalar = s.simplify(s.trace(gi*Ric))
Einmixed = s.simplify(gi*Ric-s.eye(4)*Rscalar/2)
assert s.simplify(Einmixed[0,0]-(HY**2+2*HX*HY+K)) == 0
assert s.simplify(Einmixed[2,2]-Einmixed[1,1]-(s.diff(D,t)+3*H*D-K)) == 0
emit("G^theta_theta - G^r_r", "Delta_dot + 3 H Delta - K")
emit("pressure-anisotropy identity", "Delta_dot + 3 H Delta = K + kappa(P_parallel-P_perp)")
emit("shear-scalar identity", "(sigma^2)_dot + 6 H sigma^2 = 2 Delta [K+kappa(P_parallel-P_perp)]/3")
emit("result", "ALL ASSERTIONS PASSED; no microscopic response coefficient, relaxation time, or collapse trajectory calculated")
text = "\n\n".join(out)+"\n"
Path(__file__).with_suffix('.txt').write_text(text)
print(text)
