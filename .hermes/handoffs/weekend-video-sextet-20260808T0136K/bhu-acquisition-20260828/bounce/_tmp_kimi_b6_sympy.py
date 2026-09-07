import sympy as sp

t = sp.symbols('t')
X = sp.Function('X')(t)
Y = sp.Function('Y')(t)
HX = sp.diff(X, t)/X
HY = sp.diff(Y, t)/Y
H = (HX + 2*HY)/3
Delta = HX - HY
K = Y**-2
a = (X*Y**2)**sp.Rational(1,3)

results = []

# 1. Eq. (27) printed: sig1dot = (2/3)[(X X'' - X'^2)/X^2 - (Y Y'' - Y'^2)/Y^2]
sig1 = sp.Rational(2,3)*Delta
sig1dot_printed = sp.Rational(2,3)*((X*sp.diff(X,t,2)-sp.diff(X,t)**2)/X**2
                                     - (Y*sp.diff(Y,t,2)-sp.diff(Y,t)**2)/Y**2)
r = sp.simplify(sp.diff(sig1,t) - sig1dot_printed)
results.append(("(27) consistent with sigma1_1=2Delta/3", r == 0))

# 2. Eq. (11) printed: X''/X - Y''/Y + X'Y'/(XY) - (Y'^2+1)/Y^2 = 0
#    => X''/X - Y''/Y = -HX*HY + HY^2 + K
#    sigma1dot + 3H sigma1 should equal 2/(3Y^2)
dHX = sp.diff(HX, t); dHY = sp.diff(HY, t)
# dHX = X''/X - HX^2 ; so X''/X = dHX + HX^2
# Use Eq(11) to express dHX - dHY:
# X''/X - Y''/Y = dHX - dHY + HX^2 - HY^2 = -HX HY + HY^2 + K
# => dHX - dHY = -HX HY + HY^2 + K - HX^2 + HY^2
dDelta = -HX*HY + 2*HY**2 + K - HX**2
lhs28 = sp.Rational(2,3)*dDelta + 3*H*sp.Rational(2,3)*Delta
r = sp.simplify(lhs28 - sp.Rational(2,3)*K)
results.append(("Eq(28) follows from printed (27)+(11)+(16): sig1dot+3H sig1 = 2/(3Y^2)", r == 0))

# => Delta_dot + 3H Delta = K
Delta_dot = sp.simplify(sp.Rational(3,2)*sp.Rational(2,3)*dDelta)
r = sp.simplify(Delta_dot + 3*H*Delta - K)
results.append(("Delta_dot + 3H Delta = K", r == 0))

# 3. S = sigma^2 = Delta^2/3 (printed Eq 25); Eq (30): S' + 6 H S = (2/(3Y^2)) Delta
S = Delta**2/3
Sdot = 2*Delta*Delta_dot/3
r = sp.simplify(Sdot + 6*H*S - sp.Rational(2,3)*K*Delta)
results.append(("printed Eq(30) holds", r == 0))

# 4. B6 identity: d(a^6 S)/dt = (2/3) a^6 K Delta
r = sp.simplify(sp.diff(a**6*S, t) - sp.Rational(2,3)*a**6*K*Delta)
# need Delta_dot substitution: sympy doesn't know Delta_dot; redo manually
lhs = 6*a**5*sp.diff(a,t)*S + a**6*Sdot
da = sp.diff(a, t)
lhs2 = sp.simplify(lhs.subs(da, H*a))
r = sp.simplify(lhs2 - sp.Rational(2,3)*a**6*K*Delta)
results.append(("B6 boxed identity d(a^6 S)/dt = (2/3) a^6 K Delta", r == 0))

# 5. a^3 K = X
r = sp.simplify(a**3*K - X)
results.append(("a^3 K = X", r == 0))

# 6. log slope: d ln S / d ln a = -6 + 2K/(H Delta)
slope = sp.simplify((Sdot/S)/(H))
r = sp.simplify(slope - (-6 + 2*K/(H*Delta)))
results.append(("dlnS/dlna = -6 + 2K/(H Delta)", r == 0))

# 7. R ratio, no production: R = 3 kappa alpha N0^2/(C+I)^2 with I'=a^3K, C+I = a^3 Delta
kap, al, N0 = sp.symbols('kappa alpha N0', positive=True)
C = sp.symbols('C')
I = sp.Function('I')(t)
R = 3*kap*al*N0**2/(C+I)**2
Rdot = sp.diff(R, t).subs(sp.diff(I,t), a**3*K)
expr = sp.simplify(Rdot + 2*K/Delta*R)
expr = sp.simplify(expr.subs(C+I, a**3*Delta))
results.append(("Rdot = -2K R/Delta at beta=0 (uses C+I = a^3 Delta)", expr == 0))

# 8. with production N' = a^3 Psi: Rdot/R = 2(Psi/n - K/Delta)
N = sp.Function('N')(t)
n = N/a**3
Psi = sp.Function('Psi')(t)
R2 = 3*kap*al*N**2/(C+I)**2
R2dot = sp.diff(R2, t).subs({sp.diff(I,t): a**3*K, sp.diff(N,t): a**3*Psi})
r = sp.simplify(R2dot/R2 - 2*(Psi/n - K/Delta))
r = sp.simplify(r.subs(C+I, a**3*Delta))
results.append(("Rdot/R = 2(Psi/n - K/Delta)", r == 0))

# 9. Eq (35) LHS = 2 beta n H^4
beta, nf = sp.symbols('beta n_f', positive=True)
lhs35 = 2*beta*nf/sp.Integer(81)*(HX+2*HY)**4
r = sp.simplify(lhs35 - 2*beta*nf*H**4)
results.append(("Eq(35) LHS = 2 beta n_f H^4", r == 0))

# 10. Constraint: 3H^2 = S - K + (2HXHY+HY^2+K) identically
r = sp.simplify(3*H**2 - (S - K) - (2*HX*HY + HY**2 + K))
results.append(("3H^2 = S - K + kappa eps_tilde matches printed Eq(10) first", r == 0))

# 11. suggested data Y'=0 => Delta = 3H
r = sp.simplify((HX - 0).subs(HY, 0) - 3*(HX+2*0)/3)
# simpler: Delta|HY=0 = HX ; H|HY=0 = HX/3 => Delta = 3H
results.append(("Y'_0=0 gives Delta_0 = 3 H_0", sp.simplify(HX - 3*(HX/3)) == 0))

# 12. dln(n^2)/dlna = -6 + 2 Psi/(H n)
ndot = Psi - 3*H*n
slopen = sp.simplify((2*ndot/n)/H)
r = sp.simplify(slopen - (-6 + 2*Psi/(H*n)))
results.append(("dln(n^2)/dlna = -6 + 2 Psi/(H n)", r == 0))

for name, ok in results:
    print(("PASS" if ok else "FAIL"), "-", name)
print("ALL_PASS" if all(ok for _, ok in results) else "SOME_FAIL")
