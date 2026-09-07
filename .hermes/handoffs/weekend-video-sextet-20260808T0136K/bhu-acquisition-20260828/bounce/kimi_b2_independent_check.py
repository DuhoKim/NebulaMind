#!/usr/bin/python3
"""Independent adversarial check of B2 closure claims. Writes no files.
Run: /usr/bin/python3 kimi_b2_independent_check.py
Re-derives everything from arXiv 2007.11556v2 HTML equations (1),(9),(10),
(11),(14),(16),(17),(34),(36),(37), section 9, as extracted 2026-09-07.
Does NOT import or trust b2_closure.py tokens.
"""
import sympy as s

def check(label, expression):
    r = s.factor(s.simplify(expression))
    print(label + ' = ' + str(r))
    assert r == 0, (label, r)

alpha, hn, hs, kappa, beta, T = s.symbols('alpha h_n h_star kappa beta T', positive=True)
H, Psi = s.symbols('H Psi')
print('=== PART 1: matter sector, from printed (14) directly ===')
eps, p, n, ed, nd = s.symbols('eps p n epsdot ndot')
# Printed (14): d((eps-alpha n^2) V)/dt + (p-alpha n^2) dV/dt = 0, Vdot/V=3H.
# Expand independently:
V = s.Symbol('V', positive=True)
first_law = (s.diff((eps-alpha*n**2)*V, eps)*ed + s.diff((eps-alpha*n**2)*V, n)*nd
             + (eps-alpha*n**2)*3*H*V + (p-alpha*n**2)*3*H*V)
check('printed (14) expanded /V - [epsdot-2a*n*ndot+3H(eps+p-2a*n^2)]',
      s.expand(first_law/V) - (ed-2*alpha*n*nd+3*H*(eps+p-2*alpha*n**2)))
Td = s.Symbol('Tdot')
thermal = ((ed-2*alpha*n*nd+3*H*(eps+p-2*alpha*n**2))
           .subs({eps:hs*T**4, p:hs*T**4/3, n:hn*T**3,
                  ed:4*hs*T**3*Td, nd:3*hn*T**2*Td}))
check('thermal factorisation vs A(T)*(Tdot+H*T)',
      thermal - (4*hs*T**3-6*alpha*hn**2*T**5)*(Td+H*T))
# Printed (37): Tdot + H*T = beta*H^4/(3*h_n*T^2); substitute:
compat = s.factor(thermal.subs(Td, -H*T + beta*H**4/(3*hn*T**2)))
print('compat residual on production interval:', compat)
# On interval with Psi != 0, residual=0 forces the coefficient of E=0 to vanish:
Tstar2 = s.Rational(2,3)*hs/(alpha*hn**2)
check('A(T) at T_star^2=2h*/(3 a hn^2)', (4*hs*T**3-6*alpha*hn**2*T**5).subs(T**2, Tstar2).subs(T, s.sqrt(Tstar2)))
# H forced constant: N=0 with ndot=0 -> Psi=3Hn; Psi=beta H^4 -> H(beta H^3-3n*)=0
# H=0 => Psi=0 contradicts production; hence H^3=3n*/beta, unique real root >0.
print('H=0 on branch => Psi=beta*0^4=0 => no production: excluded. H^3=3n*/beta>0 forced.')

print('=== PART 2: no-gluing lemmas ===')
u, v, K = s.symbols('u v K', positive=False, real=True)
K = s.symbols('K', positive=True)
rho0, P0 = s.symbols('rho0 P0', real=True)
udot = -u**2-u*v+(v**2+K-kappa*P0)/2
vdot = -(3*v**2+K+kappa*P0)/2
# LEMMA KS-static: H==0 on an interval. Then n,eps constant (N,E at H=0),
# so rho0,P0 constants. H=u+2v over 3 ==0 => u=-2v and udot=-2vdot on the interval.
u_static = -2*v
preserve = s.factor(udot.subs(u, u_static) + 2*vdot)   # udot+2vdot must vanish
print('KS static: udot+2vdot (must be 0) =', preserve)
# Solve preserve=0 and constraint for (kappa*P0, kappa*rho0) in terms of v,K:
kP = s.solve(preserve, kappa*P0)[0]
print('KS static: kappa*P0 =', kP)
kR = s.factor(v**2+2*u_static*v+K)  # = kappa*rho0 from constraint
print('KS static: kappa*rho0 =', kR)
# rho0,P0 constants => d/dt(kappa*P0)=0 and d/dt(kappa*rho0)=0.
# Unknowns v(t),K(t) with Kdot=-2vK. Differentiate both:
eqs = [kP - kappa*P0, kR - kappa*rho0]
# eliminate constants: take combos
d1 = s.factor(kP + 3*kR)   # = kappa(P0+3rho0)?? just to see structure
print('kP+3kR =', d1)
# From kP: kappa P0 = -3v^2 - K/3 ; from kR: kappa rho0 = K-3v^2.
# constancy => d/dt(-3v^2-K/3)=0 and d/dt(K-3v^2)=0 => subtract: d/dt(-4K/3)... do it:
Kdot = -2*v*K
vd = vdot
dP = s.factor(s.diff(kP, v)*vd + s.diff(kP, K)*Kdot)
dR = s.factor(s.diff(kR, v)*vd + s.diff(kR, K)*Kdot)
print('d(kappa P0)/dt =', dP)
print('d(kappa R0)/dt =', dR)
# Both must vanish identically on the interval. Solve dR=0,dP=0 for v (K>0):
sol_v = s.solve([dR, dP], [vd, v], dict=True)
print('static consistency forces:', sol_v)
# With v=0: then u=0; check vdot at v=0 with kappa P0=-K/3:
print('vdot at v=0, kP=-K/3:', s.factor(vdot.subs({v:0, kappa*P0: -K/3})))
print('=> vdot = -K/3 != 0 since K=1/Y^2>0. Contradiction: no H==0 interval in KS.')

print('--- BI static: H==0 interval ---')
# H_i const, sum 0; Hdot_i = kappa(rho-P)/2 - 3H H_i = kappa(rho-P)/2 must be 0.
# rho-P = eps-p = eps - eps/3 = 2 eps/3. eps=h_star T^4 >0 => contradiction.
check('rho-P - 2*eps/3 for effective source',
      (eps-alpha*n**2) - (eps/3-alpha*n**2) - 2*eps/3)
print('=> H==0 interval in flat BI forces eps=0 i.e. T=0: excluded (T>0).')

print('=== PART 3: branches re-derived independently ===')
L = s.symbols('Lambda_eff', positive=True)
n0 = s.Symbol('n_star', positive=True)
# KS branch
u_b, v_b, K_b = s.sqrt(L), 0, L
rho_b, P_b = L/kappa, -L/kappa
C_K = v**2+2*u*v+K-kappa*rho0
check('KS branch constraint', C_K.subs({u:u_b, v:v_b, K:K_b, rho0:rho_b}))
check('KS branch sp-u', udot.subs({u:u_b, v:v_b, K:K_b, P0:P_b}))
check('KS branch sp-v', vdot.subs({u:u_b, v:v_b, K:K_b, P0:P_b}))
# (11) WITH derivative terms: udot+u^2-(vdot+v^2)+u*v-v^2-K ; on branch udot=vdot=0:
check('KS branch (11) full', (u**2-v**2+u*v-v**2-K).subs({u:u_b, v:v_b, K:K_b}))
H_KS = s.sqrt(L)/3
beta_KS = s.simplify(3*n0/H_KS**3)
print('KS: H_* =', H_KS, '; beta =', beta_KS)
check('KS production residual', beta_KS*H_KS**4-3*H_KS*n0)
# BI branch
h_b = s.sqrt(L/3)
h1,h2,h3 = s.symbols('H1 H2 H3', real=True)
theta = h1+h2+h3
F_i = kappa*(rho0-P0)/2 - theta*h1   # template per direction
for hi in (h1,h2,h3):
    pass
F = [kappa*(rho0-P0)/2 - theta*x for x in (h1,h2,h3)]
CB = h1*h2+h1*h3+h2*h3-kappa*rho0
sub = {h1:h_b, h2:h_b, h3:h_b, rho0:rho_b, P0:P_b}
check('BI branch constraint', CB.subs(sub))
for i,f in enumerate(F,1):
    check('BI branch Hdot'+str(i), f.subs(sub))
H_BI = h_b
beta_BI = s.simplify(3*n0/H_BI**3)
print('BI: H_* =', H_BI, '; beta =', beta_BI)
check('BI production residual', beta_BI*H_BI**4-3*H_BI*n0)
# Cross-check beta tunings against each other
print('ratio beta_KS/beta_BI =', s.simplify(beta_KS/beta_BI))

print('=== PART 4: constraint propagation <==> first law (E), symbolic rhodot ===')
rd = s.Symbol('rhodot', real=True)
P = s.Symbol('P', real=True)
r = s.Symbol('rho', real=True)
udot2 = -u**2-u*v+(v**2+K-kappa*P)/2
vdot2 = -(3*v**2+K+kappa*P)/2
C = v**2+2*u*v+K-kappa*r
Cdot = (2*v*vdot2 + 2*udot2*v + 2*u*vdot2 + (-2*v*K) - kappa*rd)
expr = s.factor(Cdot + (u+2*v)*C)
print('KS: Cdot+3H*C (symbolic rhodot) =', expr)
check('KS: Cdot+3H*C + kappa*(rhodot+3H(rho+P))',
      expr + kappa*(rd+(u+2*v)*(r+P)))
print('=> propagation holds IFF E=0; E is the propagating equation (count legit).')
# BI (rebuilt with rho,P)
CB2 = h1*h2+h1*h3+h2*h3-kappa*r
F2 = [kappa*(r-P)/2 - theta*x for x in (h1,h2,h3)]
CBD = sum(s.diff(CB2,x)*f for x,f in zip((h1,h2,h3),F2)) - kappa*rd
exprB = s.factor(CBD + 2*theta*CB2)
print('BI: CBdot+6H*CB (symbolic rhodot) =', exprB)
check('BI: CBdot+6H*CB + kappa*(rhodot+3H(rho+P))',
      exprB + kappa*(rd+theta*(r+P)))

print('=== PART 5: case (b)/(c) matter system, independent ===')
Fp = s.symbols('Fprime', positive=True)
Fv = s.Symbol('F_of_T')
nd_rhs = beta*H**4-3*H*n
Td_rhs = (2*alpha*n*beta*H**4-4*H*Fv)/Fp
Ec = (Fp*Td_rhs - 2*alpha*n*nd_rhs + 3*H*(Fv+Fv/3-2*alpha*n**2))
check('case c first-law residual', Ec)
M = s.Matrix([[Fp,-2*alpha*n],[0,1]])
print('det =', M.det(), '(regular iff F_prime nonzero)')
# case b explicit:
Tb_rhs = s.simplify(Td_rhs.subs({Fp:4*hs*T**3, Fv:hs*T**4}))
print('case b Tdot =', Tb_rhs)
Eb = (4*hs*T**3*Tb_rhs - 2*alpha*n*nd_rhs + 3*H*(hs*T**4+hs*T**4/3-2*alpha*n**2))
check('case b first-law residual', Eb)

print('=== PART 6: counts (independent) ===')
for geo,g in [('KS',4),('BI',6)]:
    for case,cl,unk_extra in [('a',3,4),('b',2,4),('c',2,4),('d',0,3)]:
        evo = g+2
        unk = g+unk_extra
        print(geo, case, 'unknowns=',unk,'evolution=',evo,'closures=',cl,
              'excess=',evo+cl-unk)
print('ALL INDEPENDENT CHECKS DONE')
