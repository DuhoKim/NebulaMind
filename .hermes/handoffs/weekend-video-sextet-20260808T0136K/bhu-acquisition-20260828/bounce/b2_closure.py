#!/usr/bin/python3
"""B2 symbolic audit; no file writes. Run: /usr/bin/python3 b2_closure.py.
Source: arXiv 2007.11556v2 HTML, read 2026-09-07, equations
(1), (10), (11), (14), (16), (17), (34), (36), (37), section 9.
All calculations are FLUID only. BI is an explicitly added flat reduction;
KS retains curvature. No DIRAC equations or publisher-identity claim.
Requires SymPy (verified with 1.14.0 under /usr/bin/python3).
"""
import sympy as s


def check(label, expression):
    result = s.factor(s.simplify(expression))
    print(label + ' = ' + str(result))
    assert result == 0, (label, result)


alpha, hn, hs, kappa, beta, T = s.symbols(
    'alpha h_n h_star kappa beta T', positive=True)
H, Td, Psi, n, nd, eps, ed, p = s.symbols('H Tdot Psi n ndot eps epsdot p')
E = ed - 2*alpha*n*nd + 3*H*(eps+p-2*alpha*n**2)
N = nd + 3*H*n-Psi
print('SOURCE=arXiv 2007.11556v2 HTML; read 2026-09-07')
print('ROW=FLUID; DIRAC=NOT_ANALYSED')
check('energy balance identity E - [epsdot+3H(eps+p)-2alpha*n*Psi-2alpha*n*N]',
      E-(ed+3*H*(eps+p)-2*alpha*n*Psi-2*alpha*n*N))
thermal = E.subs({eps:hs*T**4, p:hs*T**4/3, n:hn*T**3,
                  ed:4*hs*T**3*Td, nd:3*hn*T**2*Td})
check('thermal factorisation', thermal-(4*hs*T**3-6*alpha*hn**2*T**5)*(Td+H*T))
compat = s.factor(thermal.subs(Td, -H*T+Psi/(3*hn*T**2)))
print('FLUID compatibility residual after (37):', compat)
q = s.solve(2*hs-3*alpha*hn**2*s.Symbol('q'), s.Symbol('q'))[0]
Ts = s.sqrt(q)
ns = s.simplify(hn*Ts**3)
es = s.simplify(hs*Ts**4)
rhos = s.simplify(es-alpha*ns**2)
ps = s.simplify(es/3-alpha*ns**2)
Lam = s.simplify(kappa*rhos)
check('p_eff_star + rho_eff_star', ps+rhos)
check('rho_eff_star - eps_star/3', rhos-es/3)
check('pinned first law', thermal.subs({T:Ts, Td:0}))
check('pinned temperature law', H*Ts-(3*H*ns)/(3*hn*Ts**2))
check('pinned number balance', 3*H*ns-3*H*ns)
print('T_star^2 =', q)
print('n_star =', ns)
print('Lambda_eff =', Lam)
print('Pinned relations: Tdot=ndot=0; Psi=3*H*n_star; beta*H^3=3*n_star; H>0')
t, t0, V0, sint = s.symbols('t t0 V0 s_integration')
V = V0*s.exp(3*H*(t-t0))
check('pinned comoving number growth', s.diff(ns*V,t)-3*H*ns*V)
entropy = 2*alpha*ns**2/Ts+sint/V
check('pinned entropy law (17)', Ts*s.diff(entropy*V,t)-2*alpha*ns*(3*H*ns)*V)
print('Entropy reconstruction: s(t)=2*alpha*n_star^2/T_star + C_s/V(t)')

# Curved KS: u=Xdot/X, v=Ydot/Y, K=1/Y^2. These are a
# first-order rewriting of source (10), with no flat substitution.
u,v,K = s.symbols('u v K', real=True)
rho,P = s.symbols('rho P', real=True)
ud = -u**2-u*v+(v**2+K-kappa*P)/2
vd = -(3*v**2+K+kappa*P)/2
Kd = -2*v*K
C = v**2+2*u*v+K-kappa*rho
rhod = -(u+2*v)*(rho+P)
Cdot = s.diff(C,u)*ud+s.diff(C,v)*vd+s.diff(C,K)*Kd-kappa*rhod
check('CURVED_KS constraint propagation Cdot+3H*C', Cdot+(u+2*v)*C)
Hm = (u+2*v)/3
S = (u-v)**2/3
Hd = (ud+2*vd)/3
check('CURVED_KS Raychaudhuri identity on constraint',
      Hd-(-Hm**2-2*S/3-kappa*(rho+3*P)/6)+C/6)

# Necessity on the pinned branch: H is constant, and Raychaudhuri
# makes S constant; constraint makes K constant. K>0 then forces v=0.
# u=3H; the two spatial equations force u^2=Lambda, K=Lambda.
L = s.symbols('Lambda_eff', positive=True)
Sfixed = (L-3*H**2)/2
Kfixed = s.simplify(L+Sfixed-3*H**2)
print('CURVED_KS constant-H necessity: S =', Sfixed, '; K =', Kfixed)
check('CURVED_KS constant-H Raychaudhuri', L/3-H**2-2*Sfixed/3)
check('CURVED_KS constant-H constraint', 3*H**2-L-Sfixed+Kfixed)
print('CURVED_KS: Kdot=-2*v*K=0 and K>0 force v=0; u=3H; u^2=K=Lambda_eff.')
ks_H = s.sqrt(L)/3
ks_beta = s.simplify(3*n/ks_H**3)
ks = {u:s.sqrt(L), v:0, K:L, rho:L/kappa, P:-L/kappa}
check('CURVED_KS constraint special branch', C.subs(ks))
check('CURVED_KS u evolution special branch', ud.subs(ks))
check('CURVED_KS v evolution special branch', vd.subs(ks))
check('CURVED_KS curvature evolution special branch', Kd.subs(ks))
check('CURVED_KS (11) special branch', (u**2-v**2+u*v-v**2-K).subs(ks))
check('CURVED_KS production special branch', ks_beta*ks_H**4-3*ks_H*n)
print('CURVED_KS: Y=1/sqrt(Lambda_eff), X=X0*exp(sqrt(Lambda_eff)*(t-t0))')
print('CURVED_KS: H =', ks_H, '; beta =', ks_beta, '(n=n_star)')

# Flat diagonal BI: three scale factors and isotropic effective FLUID stress.
# This is our flat Einstein-system derivation, not a printed KS equation.
h1,h2,h3 = s.symbols('H1 H2 H3', real=True)
hh = [h1,h2,h3]
theta = sum(hh)
F = [kappa*(rho-P)/2-theta*x for x in hh]
CB = h1*h2+h1*h3+h2*h3-kappa*rho
CBD = sum(s.diff(CB,x)*f for x,f in zip(hh,F))-kappa*(-theta*(rho+P))
check('FLAT_BI constraint propagation Cdot+6H*C', CBD+2*theta*CB)
Sb = sum((x-theta/3)**2 for x in hh)/2
Sbd = sum(s.diff(Sb,x)*f for x,f in zip(hh,F))
check('FLAT_BI shear evolution Sdot+6H*S', Sbd+2*theta*Sb)
Hbd = sum(F)/3
check('FLAT_BI Raychaudhuri identity on constraint',
      Hbd-(-(theta/3)**2-2*Sb/3-kappa*(rho+3*P)/6)+2*CB/3)
print('FLAT_BI: constant H implies constant S; Sdot=-6H*S with H>0 forces S=0.')
bi_H = s.sqrt(L/3)
bi_beta = s.simplify(3*n/bi_H**3)
bi = {x:bi_H for x in hh}
bi.update({rho:L/kappa, P:-L/kappa})
check('FLAT_BI constraint special branch', CB.subs(bi))
for i,f in enumerate(F, 1):
    check('FLAT_BI H'+str(i)+' evolution special branch', f.subs(bi))
check('FLAT_BI production special branch', bi_beta*bi_H**4-3*bi_H*n)
print('FLAT_BI: ai=ai0*exp(sqrt(Lambda_eff/3)*(t-t0)); shear=0')
print('FLAT_BI: H =', bi_H, '; beta =', bi_beta, '(n=n_star)')

# Independent matter equations after closure in b/c. A prescribed F(T)
# with Fprime != 0 gives a regular two-dimensional matter evolution.
Fp = s.symbols('Fprime', nonzero=True)
Fval = s.symbols('F_of_T')
nd_rhs = Psi-3*H*n
Td_rhs = (2*alpha*n*Psi-4*H*Fval)/Fp
check('case c energy residual', E.subs(
    {eps:Fval, p:Fval/3, ed:Fp*Td_rhs, nd:nd_rhs}))
check('case b energy residual', E.subs(
    {eps:hs*T**4, p:hs*T**4/3,
     ed:4*hs*T**3*((2*alpha*n*Psi-4*H*hs*T**4)/(4*hs*T**3)), nd:nd_rhs}))
check('case c matter derivative determinant',
      s.Matrix([[Fp,-2*alpha*n],[0,1]]).det()-Fp)

# Count differential evolution equations plus algebraic closure equations;
# the propagated Hamiltonian constraint is one initial-data restriction,
# not another independent evolution equation. H and Psi are derived.
print('\nFLUID counting table; initial Hamiltonian constraints=1 in each row')
print('| Geometry | Case | Unknown functions | Evolution eqs | Algebraic closure eqs | Status |')
statuses = {}
for geometry,glist in [('CURVED_KS',['X','Y','u','v']),
                       ('FLAT_BI',['a1','a2','a3','H1','H2','H3'])]:
    for case,closures in [('a',3),('b',2),('c',2),('d',0)]:
        matter = ['eps','p','n'] + ([] if case=='d' else ['T'])
        unknowns = glist+matter
        equations = len(glist)+2  # geometry, first law, number law
        excess = equations+closures-len(unknowns)
        status = ('over-determined (+1 compatibility)' if excess>0 else
                  'under-determined (1 free function)' if excess<0 else 'determined')
        statuses[(geometry,case)] = status
        print('| '+geometry+' | '+case+' | '+','.join(unknowns)+
              ' ('+str(len(unknowns))+') | '+str(equations)+' | '+str(closures)+' | '+status+' |')
determined = [c for c in 'abcd' if all(statuses[(g,c)]=='determined'
              for g in ['CURVED_KS','FLAT_BI'])]
print('Case c assumes a SPECIFIED smooth eps=F(T), Fprime!=0; otherwise one constitutive function is missing.')
print('Case d: supply one pressure EOS p=P(eps,n); T is not a state variable here.')
print('If T is also requested in d, add a caloric relation T=Theta(eps,n).')
print('All counts assume specified Psi=beta*H^4 with fixed beta>0; a number balance alone is not a production prescription.')
print('Independent KS evolution: Xdot=uX, Ydot=vY, udot='+str(ud)+', vdot='+str(vd)+', E=0, N=0.')
print('Independent BI evolution: aidot=Hi*ai, Hidot=kappa*(rho-P)/2-3H*Hi (i=1,2,3), E=0, N=0.')
print('Algebraic closures: a: eps=h_star*T^4,p=eps/3,n=h_n*T^3; b: first two; c: eps=F(T),p=eps/3; d: none.')
print('SPECIAL_BRANCH=EXISTS')
print('Token scope: FLUID simultaneous (14),(37); full CURVED_KS / FLAT_BI branches require their respective beta tuning above.')
print('CLOSURE_SUFFICIENT='+','.join(determined))
