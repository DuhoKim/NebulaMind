#!/usr/bin/env python3
"""K2 junction classification -- Claude computation seat (blind double).
Prereg: K2_JUNCTION_PREREG_20260903.md (frozen).  Pins: K2_claude_pins.md.
Units G=c=1 (Khakshournia L56).  Israel (timelike) and Barrabes-Israel (null) formalisms.
Runs controls C1..C4 first; a failed control raises and no class is filed.
"""
import sys, itertools
import sympy as sp

t, chi, th, ph = sp.symbols('t chi theta phi', real=True)
a_ = sp.Symbol('a', positive=True); ad, add = sp.symbols('adot addot', real=True)   # a>0, da/dt, d2a/dt2 on Sigma
rho0 = sp.Symbol('rho0', positive=True)
Lam, M, m_sh = sp.symbols('Lambda M m_shell', real=True)
X_, Xd, Xdd = sp.symbols('X Xdot Xddot', real=True)           # boundary chi=X(t) and derivatives
LOG = []
def out(s=''):
    print(s); LOG.append(s)

def christoffel(g, x):
    ginv = g.inv(); n = len(x)
    G = [[[sp.S(0)]*n for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                G[i][j][k] = sp.simplify(sum(ginv[i, l]*(sp.diff(g[l, j], x[k]) + sp.diff(g[l, k], x[j]) - sp.diff(g[j, k], x[l])) for l in range(n))/2)
    return G

def K_components(g, x, emb, param, n_low, G):
    """Extrinsic curvature K_ab = -n_mu (d^2 x^mu/dxi^a dxi^b + Gamma^mu_{nu rho} dx^nu/dxi^a dx^rho/dxi^b)
    for a spherically symmetric surface embedded as x^mu(param, theta, phi) = emb.  Returns (K_pp, K_thth)."""
    xd = [sp.diff(e, param) for e in emb]
    xdd = [sp.diff(e, param, 2) for e in emb]
    n = len(x)
    Kpp = -sum(n_low[mu]*(xdd[mu] + sum(G[mu][nu][rh]*xd[nu]*xd[rh] for nu in range(n) for rh in range(n))) for mu in range(n))
    Kthth = -sum(n_low[mu]*G[mu][2][2] for mu in range(n))
    return sp.simplify(Kpp), sp.simplify(Kthth)

# ---------------- interior: FRW dust, ds^2 = -dt^2 + a^2[dchi^2 + S_k(chi)^2 dOmega^2] ----------------
def interior(k):
    S = sp.sin(chi) if k == 1 else chi
    a = sp.Function('a')(t); X = sp.Function('X')(t)
    x = [t, chi, th, ph]
    g = sp.diag(-1, a**2, a**2*S**2, a**2*S**2*sp.sin(th)**2)
    G = christoffel(g, x)
    emb = [t, X, th, ph]
    gam2 = 1 - a**2*sp.diff(X, t)**2                       # (ds/dt)^2 on Sigma
    n_low = [ -sp.diff(X, t)*a/sp.sqrt(gam2), a/sp.sqrt(gam2), 0, 0 ]   # unit normal, outward = increasing chi
    Ktt, Kthth = K_components(g, x, emb, t, n_low, G)
    Kss = Ktt/gam2                                          # proper-time component
    R = a*S.subs(chi, X)
    sub = {sp.Derivative(a, (t, 2)): add, sp.Derivative(a, t): ad, a: a_,
           sp.Derivative(X, (t, 2)): Xdd, sp.Derivative(X, t): Xd, X: X_}
    fix = lambda e: sp.simplify(e.subs(sp.Derivative(a,(t,2)), add).subs(sp.Derivative(X,(t,2)), Xdd)
                                 .subs(sp.Derivative(a,t), ad).subs(sp.Derivative(X,t), Xd).subs(a, a_).subs(X, X_))
    Kss_, Kthth_, R_ = fix(Kss), fix(Kthth.subs(chi, X)), fix(R)
    # u.n and beta_- = n^mu d_mu R, Rdot = dR/ds
    ginv = g.inv()
    n_up = [sum(ginv[mu, nu]*n_low[nu] for nu in range(4)) for mu in range(4)]
    Rfield = a*S
    beta_m = fix(sum(n_up[mu]*sp.diff(Rfield, x[mu]) for mu in range(4)).subs(chi, X))
    u_dot_n = fix(-n_low[0])          # u^mu = (1,0,0,0): u.n = g_tt n^t = n_t * (-1)... n_t lowered: u.n = u^mu n_mu = n_t
    u_dot_n = fix(n_low[0])
    Rdot_s = fix((sp.diff(Rfield.subs(chi, X), t))/sp.sqrt(gam2))
    return dict(S=S, Kss=Kss_, Kthth=Kthth_, R=R_, beta=beta_m, udotn=u_dot_n, Rdot=Rdot_s,
                Ks_s=sp.simplify(-Kss_), Kth_th=sp.simplify(Kthth_/R_**2))

# ---------------- exterior: Schwarzschild-de Sitter, F = 1 - 2M/R - Lambda R^2/3 ----------------
s = sp.Symbol('s', real=True)
def exterior():
    T = sp.Function('T')(s); Rf = sp.Function('R')(s)
    Tc, Rc = sp.symbols('T R', real=True)
    x = [Tc, Rc, th, ph]
    F = 1 - 2*M/Rc - Lam*Rc**2/3
    g = sp.diag(-F, 1/F, Rc**2, Rc**2*sp.sin(th)**2)
    G = christoffel(g, x)
    # embedding (T(s), R(s), th, ph); substitute coordinate symbols by functions after Christoffels
    Gs = [[[G[i][j][k].subs({Tc: T, Rc: Rf}) for k in range(4)] for j in range(4)] for i in range(4)]
    emb = [T, Rf, th, ph]
    n_low = [-sp.diff(Rf, s), sp.diff(T, s), 0, 0]      # Knutsen eq (26): n+ = (-Rdot, Tdot, 0, 0)
    Kss, Kthth = K_components(g.subs({Tc: T, Rc: Rf}), x, emb, s, n_low, Gs)
    Td, Tdd, Rd, Rdd, Rb = sp.symbols('Tdot Tddot Rdot Rddot R_b', real=True)
    Fb = 1 - 2*M/Rb - Lam*Rb**2/3
    fix = lambda e: sp.simplify(e.subs(sp.Derivative(T,(s,2)), Tdd).subs(sp.Derivative(Rf,(s,2)), Rdd)
                                 .subs(sp.Derivative(T,s), Td).subs(sp.Derivative(Rf,s), Rd).subs(T, 0).subs(Rf, Rb))
    Kss_, Kthth_ = fix(Kss), fix(Kthth)
    # first-fundamental-form constraint (Easson eq 23/68, Knutsen eq 22): F Tdot^2 - Rdot^2/F = 1, and its s-derivative
    constr = Fb*Td**2 - Rd**2/Fb - 1
    dconstr = sp.diff(Fb, Rb)*Rd*Td**2 + 2*Fb*Td*Tdd - 2*Rd*Rdd/Fb + sp.diff(Fb, Rb)*Rd**3/Fb**2
    Tdd_sol = sp.solve(dconstr, Tdd)[0]
    Kss_elim = sp.simplify(Kss_.subs(Tdd, Tdd_sol))
    return dict(Kss=Kss_, Kss_elim=Kss_elim, Kthth=Kthth_, F=Fb, Td=Td, Rd=Rd, Rdd=Rdd, Rb=Rb, Tdd=Tdd, constr=constr,
                Ks_s_elim=sp.simplify(-Kss_elim), Kth_th=sp.simplify(Kthth_/Rb**2))

# Friedmann substitutions (Khakshournia eqs 3-4, L77-80; rho = rho0 a^-3, entry 56 L141)
def friedmann(k):
    rho = rho0/a_**3
    return {ad**2: sp.Rational(8,3)*sp.pi*rho*a_**2 - k + Lam*a_**2/3,
            add: (-sp.Rational(4,3)*sp.pi*rho + Lam/3)*a_}

def energy_conditions_timelike(sigma, p):
    """WEC: sigma>=0 and sigma+p>=0 ; DEC: sigma>=|p|."""
    return dict(WEC=[sigma >= 0, sigma + p >= 0], DEC=[sigma >= 0, sigma - p >= 0, sigma + p >= 0])

def energy_conditions_null(mu, p):
    """Null shell S^{ab} = mu n^a n^b + p sigma^{ab}: T_UU>=0 for all timelike U <=> mu>=0 and p>=0 (WEC);
    -T^mu_nu U^nu causal for all U <=> mu>=0 and p==0 (DEC): the pressure part gives a spacelike flux (norm^2 = p^2 |U_perp|^2)."""
    return dict(WEC=(sp.simplify(mu) == 0 or sp.simplify(mu).is_nonnegative) and p.is_nonnegative,
                DEC=(sp.simplify(mu) == 0 or sp.simplify(mu).is_nonnegative) and sp.simplify(p) == 0)

# =====================================================================================
out('K2 junction classification -- Claude seat.  sympy %s' % sp.__version__)
EXT = exterior()
INT = {1: interior(1), 0: interior(0)}
Td, Rd, Rdd, Rb, Fb = EXT['Td'], EXT['Rd'], EXT['Rdd'], EXT['Rb'], EXT['F']

out('\n== exterior SdS extrinsic curvature (surface (T(s),R(s)), n_mu = (-Rdot, Tdot, 0, 0)) ==')
out('  K^theta_theta+ = %s' % EXT['Kth_th'])
out('  K^s_s+ (Tddot eliminated by the first-fundamental-form constraint) = %s' % EXT['Ks_s_elim'])
chk = sp.simplify((EXT['Ks_s_elim']*Fb*Td - (Rdd + sp.diff(Fb, Rb)/2)).subs(Td**2, (1 + Rd**2/Fb)/Fb))
chk = sp.simplify(sp.expand(chk))
out('  check  K^s_s+ * (F Tdot) - (Rddot + F\'/2) on the constraint surface = %s' % chk)
assert chk == 0, 'exterior K^s_s closed form failed'
# identity beta_+ := F Tdot, beta_+^2 = F + Rdot^2 (Easson eq 69, L1028)
out('  beta_+ := F Tdot,  beta_+^2 = F + Rdot^2  [constraint]')

for k in (1, 0):
    I = INT[k]
    out('\n== interior FRW k=%d, surface chi = X(t) (general B3; B1 is Xdot=0) ==' % k)
    out('  K^theta_theta- = %s' % I['Kth_th'])
    out('  K^s_s-         = %s' % I['Ks_s'])
    out('  beta_- = n.dR  = %s' % I['beta'])
    out('  u.n (dust 4-velocity dotted with the unit normal) = %s' % I['udotn'])

# ---------------- B1 (comoving, Xdot = 0) machinery ----------------
def B1(k, Mval=None):
    I = INT[k]
    sub0 = {Xd: 0, Xdd: 0}
    S = I['S'].subs(chi, X_)
    R = a_*S
    Kth_m = sp.simplify(I['Kth_th'].subs(sub0)); Ks_m = sp.simplify(I['Ks_s'].subs(sub0))
    beta_m = sp.simplify(I['beta'].subs(sub0))
    Rd_ = ad*S; Rdd_ = add*S
    Mv = M if Mval is None else Mval
    Fv = (1 - 2*Mv/R - Lam*R**2/3)
    beta_p_sq = sp.simplify((Fv + Rd_**2).subs(friedmann(k)))
    return dict(S=S, R=R, Kth_m=Kth_m, Ks_m=Ks_m, beta_m=beta_m, beta_p_sq=beta_p_sq, Rd=Rd_, Rdd=Rdd_, F=Fv)

def israel_shell(beta_p, beta_m, Ks_p, Ks_m, R):
    """S^a_b = -(1/8pi)([K^a_b] - delta^a_b [K]); sigma = -S^s_s, p = S^theta_theta."""
    Kth_jump = (beta_p - beta_m)/R
    Ks_jump = Ks_p - Ks_m
    Kjump = Ks_jump + 2*Kth_jump
    sigma = sp.simplify(-(-(Ks_jump - Kjump)/(8*sp.pi)))
    p = sp.simplify(-(Kth_jump - Kjump)/(8*sp.pi))
    return sp.simplify(Kth_jump), sp.simplify(Ks_jump), sigma, p

M_OS = {k: sp.Rational(4,3)*sp.pi*rho0*(INT[k]['S'].subs(chi, X_))**3 for k in (1, 0)}   # (4pi/3) rho a^3 S_k(chi*)^3

# =====================================================================================
out('\n########## CONTROLS ##########')
# ---- C1: B1, k=+1, Lambda=0 reproduces Oppenheimer-Snyder smooth matching with M = (4pi/3) rho a^3 sin^3 chi* ----
b = B1(1)
eq_beta = sp.simplify((b['beta_p_sq'] - b['beta_m']**2).subs(Lam, 0))
Msol = sp.solve(sp.Eq(eq_beta, 0), M)
out('C1: B1,k=+1,Lam=0: [K^theta_theta]=0  <=>  F+Rdot^2 = beta_-^2 = cos^2(chi*)  <=>  M = %s' % Msol)
assert len(Msol) == 1 and sp.simplify(Msol[0] - M_OS[1]) == 0, 'C1 mass relation failed'
# with that M, also [K^s_s]=0: exterior K^s_s = (Rddot + F'/2)/beta_+ with beta_+ = cos chi*
bO = B1(1, M_OS[1])
num = sp.simplify((bO['Rdd'] + sp.diff(bO['F'], a_)/S if False else bO['Rdd'] + sp.diff(1 - 2*M_OS[1]/Rb - Lam*Rb**2/3, Rb).subs(Rb, bO['R'])/2).subs(friedmann(1)).subs(Lam, 0))
out('C1: with M=M_OS:  Rddot + F\'(R_b)/2 = %s   (so [K^s_s]=0 too; beta_+ = F Tdot = cos chi* > 0 for chi*<pi/2)' % num)
assert num == 0, 'C1 K^s_s failed'
beta_p_sq_OS = sp.simplify(bO['beta_p_sq'].subs(Lam, 0))
out('C1: F + Rdot^2 with M=M_OS, Lam=0 = %s = cos^2 chi*  -> PASS' % beta_p_sq_OS)
assert sp.simplify(beta_p_sq_OS - sp.cos(X_)**2) == 0
# same at k=0 (entry 56 L143: M = 4/3 pi chi^3 rho0)
b0 = B1(0); Msol0 = sp.solve(sp.Eq(sp.simplify((b0['beta_p_sq'] - b0['beta_m']**2).subs(Lam, 0)), 0), M)
out('C1 (k=0 check, entry 56 L143): M = %s' % Msol0)
assert sp.simplify(Msol0[0] - M_OS[0]) == 0
# Lambda generalisation: identity holds for every Lambda (Lambda cancels)
for k in (1, 0):
    bb = B1(k, M_OS[k]); e1 = sp.simplify(bb['beta_p_sq'] - bb['beta_m']**2)
    e2 = sp.simplify((bb['Rdd'] + sp.diff(1 - 2*M_OS[k]/Rb - Lam*Rb**2/3, Rb).subs(Rb, bb['R'])/2).subs(friedmann(k)))
    out('C1 (Lambda general, k=%d): beta_+^2 - beta_-^2 = %s ;  Rddot + F\'/2 = %s' % (k, e1, e2))
    assert e1 == 0 and e2 == 0
out('C1 PASS')

# ---- C2: entry-5 null junction at the horizon: [K_uu] = -2 pi rho a, p = rho a / 4 ----
out('\nC2: Barrabes-Israel null junction, Khakshournia prescription (eqs 1-12; M = (4pi/3) rho r^3|Sigma pointwise, L91; chi=pi/2, L161)')
# exterior: ds^2 = -du(f du + 2 dr) + r^2 dOmega^2 (L86), n = e_u = (1, -f/2, 0, 0) (L112), N_mu = (-1,0,0,0) (L131)
u, r = sp.symbols('u r', real=True)
f = sp.Function('f')(r)
gp = sp.Matrix([[-f, -1, 0, 0], [-1, 0, 0, 0], [0, 0, r**2, 0], [0, 0, 0, r**2*sp.sin(th)**2]])
Gp = christoffel(gp, [u, r, th, ph])
n_p = [1, -f/2, 0, 0]; N_p = [-1, 0, 0, 0]
# K_uu = n^mu n^nu nabla_mu N_nu = -N_nu (dn^nu/du + Gamma^nu_{mu rho} n^mu n^rho)  (using n.N = -1 along Sigma)
dn_du_p = [sum(n_p[m]*sp.diff(n_p[nu], [u, r, th, ph][m]) for m in range(4)) for nu in range(4)]
Kuu_p = sp.simplify(-sum(N_p[nu]*(dn_du_p[nu] + sum(Gp[nu][m][q]*n_p[m]*n_p[q] for m in range(4) for q in range(4))) for nu in range(4)))
Kthth_p = sp.simplify(-sum(N_p[nu]*Gp[nu][2][2] for nu in range(4)))
out('  K_uu|+ = %s   (paper eq 16: -f_,r/2)' % Kuu_p)
out('  K_thth|+ = %s   (paper eq 15: r)' % Kthth_p)
assert sp.simplify(Kuu_p + sp.diff(f, r)/2) == 0 and sp.simplify(Kthth_p - r) == 0
# interior in (t, chi): ds^2 = -dt^2 + a^2 dchi^2 + a^2 sin^2 chi dOmega^2 (Khakshournia eq 1 with dv = dt/a - dchi, eq 2)
a = sp.Function('a')(t)
gm = sp.diag(-1, a**2, a**2*sp.sin(chi)**2, a**2*sp.sin(chi)**2*sp.sin(th)**2)
Gm = christoffel(gm, [t, chi, th, ph])
# Sigma: ingoing null (2 dchi = -dv, eq 7): dt/dchi = -a.  Parameter u on Sigma: du/dchi = (du/dr)(dr/dchi) = (-2/f)(dr/dchi) (eq 10)
# r|Sigma = a sin chi (eq 7); dr/dchi along Sigma = a (cos chi - adot sin chi)  (eq 10)
# Khakshournia prescription (L91 + eqs 3,6): f|Sigma = 1 - 2M/r - Lam r^2/3 with M = (4pi/3) rho r^3 => f = cos^2 chi - adot^2 sin^2 chi
fS = sp.cos(chi)**2 - ad**2*sp.sin(chi)**2
drdchi = a_*(sp.cos(chi) - ad*sp.sin(chi))
dchidu = -fS/(2*drdchi)
# tangent n^mu = dx^mu/du = (dchi/du)(-a, 1, 0, 0); transverse null N_mu = (du/dchi)/(2a) (1, -a, 0, 0)  [from N_v = (1/2)du/dchi, eq 11]
DU = sp.Symbol('DU', real=True)   # stands for du/dchi on Sigma (a function of chi along Sigma)
n_m = [-DU**-1*a, DU**-1, 0, 0]
N_m = [DU/(2*a), -DU/2, 0, 0]
# check N.n = -1, N null
assert sp.simplify(sum(n_m[i]*N_m[i] for i in range(4))) == -1
assert sp.simplify(sum(gm.inv()[i, j]*N_m[i]*N_m[j] for i in range(4) for j in range(4))) == 0
# derivative along Sigma: d/du = (dchi/du) d/dchi|Sigma with dt/dchi = -a ; a(t) -> a_, adot, addot along Sigma
def dSigma_dchi(expr):
    """total derivative along Sigma w.r.t. chi of an expression in (t, chi, DU) with a(t): da/dchi = -a adot, d(adot)/dchi = -a addot."""
    e = expr
    return (sp.diff(e, chi) + sp.diff(e, t)*(-a))
# assemble K_uu|- = -N_nu (dn^nu/du + Gamma^nu_{mu rho} n^mu n^rho)
dn_du_m = [DU**-1*dSigma_dchi(n_m[nu]) + DU**-1*sp.diff(n_m[nu], DU)*sp.Symbol('dDUdchi') for nu in range(4)]
Kuu_m_raw = -sum(N_m[nu]*(dn_du_m[nu] + sum(Gm[nu][m][q]*n_m[m]*n_m[q] for m in range(4) for q in range(4))) for nu in range(4))
Kuu_m_raw = Kuu_m_raw.subs(sp.Derivative(a, t), ad).subs(a, a_)
# now insert DU = du/dchi = 1/dchidu and dDU/dchi along Sigma (a depends on chi through t: da/dchi = -a adot, dadot/dchi = -a addot)
DUexpr = 1/dchidu
def dSig(e):  # d/dchi along Sigma for expressions in (chi, a_, ad)
    return sp.diff(e, chi) + sp.diff(e, a_)*(-a_*ad) + sp.diff(e, ad)*(-a_*add)
Kuu_m = sp.simplify(Kuu_m_raw.subs(sp.Symbol('dDUdchi'), dSig(DUexpr)).subs(DU, DUexpr))
Kthth_m = sp.simplify(-sum(N_m[nu]*Gm[nu][2][2] for nu in range(4)).subs(sp.Derivative(a, t), ad).subs(a, a_).subs(DU, DUexpr))
out('  K_thth|- (general chi) = %s   (paper eq 13: a sin chi)' % Kthth_m)
assert sp.simplify(Kthth_m - a_*sp.sin(chi)) == 0
# f_,r at fixed M (eq 6, L89) with M = (4pi/3) rho r^3: f_,r = 2M/r^2 - 2 Lam r/3 = 8 pi rho r/3 - 2 Lam r/3 ; at chi=pi/2, r = a
rho = rho0/a_**3
f_r = sp.Rational(8,3)*sp.pi*rho*a_ - 2*Lam*a_/3
Kuu_m_pi2 = sp.simplify(Kuu_m.subs(chi, sp.pi/2).subs(friedmann(1)))
Kuu_p_pi2 = -f_r/2
jump = sp.simplify(Kuu_p_pi2 - Kuu_m_pi2)
out('  K_uu|- at chi=pi/2 (Friedmann k=+1 inserted) = %s' % Kuu_m_pi2)
out('  K_uu|- - (-f_,r/2) at chi=pi/2 = %s   (paper eq 14: +2 pi rho a)' % sp.simplify(Kuu_m_pi2 - Kuu_p_pi2))
out('  [K_uu] = K_uu|+ - K_uu|- = %s   (target -2 pi rho a; WARRANT_5_claude)' % jump)
p_null = sp.simplify(-jump/(8*sp.pi))
out('  null-shell pressure p = -(1/8pi)[K_uu] = %s   (target rho a/4 = %s)' % (p_null, sp.simplify(rho*a_/4)))
assert sp.simplify(jump + 2*sp.pi*rho*a_) == 0 and sp.simplify(p_null - rho*a_/4) == 0, 'C2 failed'
mu_null = sp.simplify(-(Kthth_p.subs(r, a_) - Kthth_m.subs(chi, sp.pi/2))/(8*sp.pi)*2/a_**2)  # mu = -(1/8pi) sigma^AB [K_AB] = 0
out('  null-shell energy density mu = -(1/8pi) sigma^AB [K_AB] = %s' % mu_null)
out('  Lambda-dependence of [K_uu]: %s' % sp.diff(jump, Lam))
out('C2 PASS  (note: with M frozen along Sigma instead of the pointwise prescription, u is singular at chi=pi/2: f=0=dr/dchi there; the paper\'s prescription is what is reproduced)')

# ---- C3: smooth timelike matching at Pathria's boundary r_b = 1 (chi* = pi/2, Knutsen L1063-1088) reproduces the static sphere ----
out('\nC3: B1 k=+1 at r_b = sin chi* = 1 (chi* = pi/2):')
bP = B1(1)
beta_m_pi2 = sp.simplify(bP['beta_m'].subs(X_, sp.pi/2))
out('  beta_- = cos(chi*) -> %s  so [K^theta_theta]=0 requires beta_+ = F Tdot = 0 => F(R_b) + Rdot^2 = 0' % beta_m_pi2)
Fpi2 = sp.simplify(bP['F'].subs(X_, sp.pi/2))
cond = sp.simplify((bP['beta_p_sq']).subs(X_, sp.pi/2))   # = F + Rdot^2 with Friedmann
Msol_pi2 = sp.solve(sp.Eq(cond, 0), M)
out('  F(R_b) + Rdot^2 = %s = 0  <=>  M = %s  (Pathria eq 14 / Knutsen eq 8: (4pi/3) rho a^3 = C/2)' % (cond, Msol_pi2))
assert sp.simplify(Msol_pi2[0] - sp.Rational(4,3)*sp.pi*rho0) == 0
F_on_shell = sp.simplify(Fpi2.subs(M, Msol_pi2[0]).subs(friedmann(1)))
out('  then F(R_b) = 1 - 2M/a - Lam a^2/3 = %s = -adot^2  (Friedmann k=+1)' % F_on_shell)
assert sp.simplify(F_on_shell - (-ad**2).subs(friedmann(1))) == 0, 'C3: F(R_b) != -adot^2'
out('  Knutsen hypothesis (24), L652-689: T timelike on Sigma <=> F(R_b) > 0.  With F(R_b) = -adot^2 <= 0 the only solution is adot = 0, F(R_b) = 0:')
out('  => R_b = a = R_s, the sphere is static and sits on its horizon = Knutsen eq (44), L1072-1088.  C3 PASS')
out('  (without hypothesis (24): the same matching is smooth for every adot, with the boundary inside the horizon, F(R_b) = -adot^2 < 0, on the T=const surface Tdot=0;')
out('   both K_ab vanish identically there: interior chi=pi/2 and exterior T=const are totally geodesic.)')
Kss_T0 = sp.simplify(EXT['Kss'].subs({EXT['Td']: 0, EXT['Tdd']: 0}))
out('  exterior K_ss at Tdot=Tddot=0 (direct, no division by beta): %s ; K_thth = %s' % (Kss_T0, sp.simplify(EXT['Kthth'].subs(EXT['Td'], 0))))
assert Kss_T0 == 0

# =====================================================================================
out('\n########## SURFACE STRESS-ENERGY (Israel), symbolic, per placement ##########')
Kth_p_sym = sp.Symbol('beta_plus')/Rb
Ks_p_sym = EXT['Ks_s_elim']
for k in (1, 0):
    bb = B1(k)
    R = bb['R']; S = bb['S']
    beta_p = sp.sqrt(bb['beta_p_sq'])   # exterior, outward orientation (F Tdot > 0); the other sign glues the exterior on the far side
    Ks_p = sp.simplify(((bb['Rdd'] + sp.diff(1 - 2*M/Rb - Lam*Rb**2/3, Rb).subs(Rb, R)/2)/beta_p).subs(friedmann(k)))
    Kth_jump, Ks_jump, sigma, p = israel_shell(beta_p, bb['beta_m'], Ks_p, bb['Ks_m'], R)
    out('\nB1, k=%d, general exterior mass M (M = M_OS + m_shell):' % k)
    out('  beta_-^2 = %s ;  beta_+^2 = F + Rdot^2 = %s' % (sp.simplify(bb['beta_m']**2), bb['beta_p_sq']))
    out('  [K^theta_theta] = %s' % Kth_jump)
    out('  [K^s_s]         = %s' % Ks_jump)
    out('  sigma = -[beta]/(4 pi R) = %s' % sigma)
    out('  p     = %s' % p)
    dM = sp.simplify((bb['beta_p_sq'] - bb['beta_m']**2).subs(M, M_OS[k] + m_sh))
    out('  beta_+^2 - beta_-^2 = %s  => sigma > 0 iff m_shell > 0; no real embedding if m_shell > R beta_-^2/2' % dM)
    out('  energy conditions: WEC = {sigma>=0, sigma+p>=0}; DEC = {sigma>=|p|}; smooth (M=M_OS): sigma=p=0, all satisfied.')

out('\nB3, general timelike surface chi = X(t) (theorem: no-shell => comoving):')
for k in (1, 0):
    I = INT[k]; S = I['S'].subs(chi, X_)
    # [K^theta_theta]=0 <=> beta_+ = beta_-  <=> F + Rdot^2 = beta_-^2
    F3 = 1 - 2*M/I['R'] - Lam*I['R']**2/3
    diffsq = sp.simplify((F3 + I['Rdot']**2 - I['beta']**2))
    out('  k=%d: F + Rdot^2 - beta_-^2 = %s' % (k, sp.factor(diffsq)))
    Msol3 = sp.solve(sp.Eq(diffsq, 0), M)
    Msol3s = sp.simplify(Msol3[0].subs(friedmann(k)))
    out('       [K^theta_theta]=0  <=>  M = %s  (the Misner-Sharp dust mass inside X(t); Xdot drops out identically)' % Msol3s)
    assert sp.simplify(Msol3s - sp.Rational(4,3)*sp.pi*rho0*S**3) == 0
    out('       M constant (Birkhoff, Knutsen L284-289) and rho0 != 0  =>  S_k(X(t)) constant  =>  Xdot = 0: the no-shell boundary is comoving (B1).')
    out('       u.n = %s  (non-zero iff Xdot != 0: dust crosses a non-comoving surface; the shell then carries the flux)' % I['udotn'])

out('\nB2, null reading (entry 5): S^ab = p g_*^ab with mu = %s, j = 0, p = %s' % (mu_null, p_null))
ecn = energy_conditions_null(mu_null, p_null)
out('  WEC (mu>=0 and p>=0): %s ;  DEC (mu>=0 and p==0): %s ;  NEC: %s' % (ecn['WEC'], ecn['DEC'], ecn['WEC']))
out('B2, timelike reading (Pathria\'s surface chi=pi/2 = Knutsen r_b=1): smooth for M = C/2 = (4pi/3) rho a^3, all 0<=Lambda<=Lambda_c;')
out('  F(R_b) = -adot^2: boundary at the bifurcation sphere at max expansion (R_max = R_s, Pathria eq 18-19), inside the white-hole region while expanding, inside the black hole while contracting.')
# Pathria identity R_max = R_s for every Lambda: F(a) = -adot^2 => adot=0 <=> F(a)=0 ; Lambda_c from the double root
C = sp.Symbol('C', positive=True)
Fc = 1 - C/Rb - Lam*Rb**2/3
sol = sp.solve([Fc, sp.diff(Fc, Rb)], [Rb, Lam], dict=True)
out('  Lambda_c (double root of F = 1 - C/R - Lambda R^2/3, C = 2M): %s  -> Lambda_c = 4/(9 C^2) = 1/(9 M^2), R_max(Lambda_c) = 3C/2 (Pathria L233-234: R_max from C to 3C/2)' % sol)
# proper-mass reading of the dust mass (second reading, prereg section 7): M_prop = 4 pi rho a^3 int_0^{pi/2} sin^2 = pi^2 rho a^3
Mprop = sp.pi**2*rho0
bq = B1(1, Mprop); bq2 = sp.simplify(bq['beta_p_sq'].subs(X_, sp.pi/2))
out('  second reading of the mass relation (proper dust mass of the half 3-sphere, M = pi^2 rho a^3): F + Rdot^2 at chi*=pi/2 = %s = %s < 0  => no real embedding at all (no junction, smooth or shelled)' % (bq2, sp.N(bq2/(rho0/a_))))

# =====================================================================================
def classify(cell, ec_test=True):
    placement, k, lam = cell
    if placement == 'B1':
        return 'J_SMOOTH_EXPANDING'          # OS comoving matching, M = M_OS, expanding branch adot>0 exists for every k, Lambda cell
    if placement == 'B3':
        return 'J_SMOOTH_EXPANDING'          # smooth members are exactly the comoving ones (theorem above) -> contains B1
    if placement == 'B2':
        if k == 0:
            return 'J_NONE'                  # no maximum-expansion surface exists for k=0 (S_k' = 1 never vanishes): vacuous cell
        return 'J_SMOOTH_EXPANDING'          # chi=pi/2 comoving worldsheet, smooth with M=C/2, expanding branch inside F<0
    if placement == 'B2-null':
        if k == 0:
            return 'J_NONE'
        smooth = (jump == 0)
        if smooth:
            return 'J_SMOOTH_EXPANDING'
        if not ec_test:
            return 'J_SHELL_EXPANDING'
        return 'J_SHELL_EXPANDING' if (ecn['WEC'] and ecn['DEC']) else 'J_SHELL_UNPHYSICAL'

cells = [(pl, k, lam) for pl in ('B1', 'B2', 'B3', 'B2-null') for k in (1, 0) for lam in ('Lam=0', '0<Lam<=Lam_c')]
table = {c: classify(c, True) for c in cells}
table_noEC = {c: classify(c, False) for c in cells}
# ---- C4 deletion probe: exact failure set ----
changed = sorted([c for c in cells if table[c] != table_noEC[c]])
expected = sorted([('B2-null', 1, 'Lam=0'), ('B2-null', 1, '0<Lam<=Lam_c')])
out('\nC4 deletion probe: cells whose class changes when the energy-condition test is removed: %s' % changed)
out('    expected exact set: %s' % expected)
assert changed == expected, 'C4 failed: exact failure set mismatch'
for c in changed:
    out('    %s : %s -> %s' % (c, table[c], table_noEC[c]))
out('C4 PASS')

out('\n########## CLASSIFICATION TABLE ##########')
for c in cells:
    out('  %-8s k=%d  %-14s : %s' % (c[0], c[1], c[2], table[c]))
out('\nHEADLINE entry 56 cell (B1, k=0, Lam=0): %s' % table[('B1', 0, 'Lam=0')])
out('HEADLINE Pathria cell (B2, k=+1, 0<=Lam<=Lam_c): %s  [timelike chi=pi/2 reading]; entry-5 null-horizon reading: %s' % (table[('B2', 1, '0<Lam<=Lam_c')], table[('B2-null', 1, '0<Lam<=Lam_c')]))
out('ALL CONTROLS PASSED: C1 C2 C3 C4')
