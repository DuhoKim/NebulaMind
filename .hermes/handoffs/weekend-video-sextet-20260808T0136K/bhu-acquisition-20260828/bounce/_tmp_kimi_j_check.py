#!/usr/bin/python3
"""_tmp adversarial check: is GRG 53,18 Eq.(14) identical to B1's required J?
Lane temp; no file writes outside this script's creation."""
import sys
sys.dont_write_bytecode = True
import sympy as s

eps, p, n, H, a = s.symbols('epsilon p n H alpha', positive=True)
ed, nd = s.symbols('eps_dot n_dot', real=True)
Psi = nd + 3*H*n
J = ed + 4*H*eps          # B1's J with p = eps/3

# GRG (14): d(eps_tilde V)/dt + p_tilde dV/dt = 0; dV/dt = 3 H V (GRG (16)).
# Expanded with (1): eps_tilde = eps - a n^2, p_tilde = p - a n^2. Divide by V:
E14 = (ed - 2*a*n*nd) + 3*H*(eps + p - 2*a*n**2)
B1_energy = J - 2*a*n*Psi                                # B1's E_F with p = eps/3
print('GRG(14)/V with p=eps/3  minus  B1 E_F =',
      s.expand(E14.subs(p, eps/3) - B1_energy))

# GRG (17): T d(sV)/dt = d(eps V)/dt + p dV/dt = a[d(n^2 V)/dt + n^2 dV/dt].
rhs17_over_V = a*(2*n*nd + 3*H*n**2) + a*n**2*3*H
print('GRG(17) RHS/V  minus  2*a*n*Psi =', s.expand(rhs17_over_V - 2*a*n*Psi))

# (14) with thermal forms eps = h_* T^4, p = eps/3, n = h_n T^3 gives a T-law;
# GRG (37) gives another. Are they the same?
hs, hn, T, Ps = s.symbols('h_star h_n T Psi', positive=True)
E14_th = E14.subs({eps: hs*T**4, p: hs*T**4/3, n: hn*T**3,
                   ed: 4*hs*T**3*s.Symbol('Td'), nd: 3*hn*T**2*s.Symbol('Td')})
law14 = s.solve(E14_th, s.Symbol('Td'))[0]
law37 = -H*T + Ps/(3*hn*T**2)
print('Tdot required by (14)+thermal =', s.simplify(law14))
print('Tdot printed as GRG (37)      =', law37)
# Insert (37)'s T-law into (14): residual.
resid = s.factor(E14_th.subs(s.Symbol('Td'), law37))
print('(14) residual when (37) holds =', resid)
print('residual/Psi                  =', s.factor(resid/Ps))
