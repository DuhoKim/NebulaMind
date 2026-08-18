"""Receipt: equation of state of the paper's rotational 'dark energy'.
Paper asserts: angular momentum of the universe is conserved => Omega decreases as the
universe expands => Lambda_eff = 3 Omega^2/c^2 decreases. Quantify the scaling the paper omits:
rigid rotor / dust vorticity: L ~ M R^2 Omega = const, R ~ a  =>  Omega ~ a^-2
=> rho_Lambda_eff ~ Omega^2 ~ a^-4.
For rho ~ a^-n, w = n/3 - 1 (from d(rho a^3)/da = -3 p a^2 / ... standard continuity).
Compare with the DES paper the source itself cites (arXiv:2503.06712 abstract, fetched
2026-08-19): wCDM w = -0.948 +0.028/-0.027; w0waCDM w0 = -0.673 +0.098/-0.097."""
import sympy as sp
a, n = sp.symbols('a n', positive=True)
rho = a**(-n)
# continuity: drho/da * a + 3(rho + p) = 0 with p = w rho  =>  w = n/3 - 1
w = sp.symbols('w')
sol = sp.solve(sp.Eq(sp.diff(rho, a)*a + 3*(rho + w*rho), 0), w)[0]
print("w(n) =", sp.simplify(sol))
print("n=4 (Omega ~ a^-2):  w =", sp.simplify(sol.subs(n, 4)))
print("n=2 (Omega ~ a^-1, radiation-era vorticity):  w =", sp.simplify(sol.subs(n, 2)))
print()
print("DES (cited by the paper): w = -0.948 +0.028/-0.027  ->  rotational w=+1/3 is excluded by")
dw = (1/3 - (-0.948)) / 0.028
print(f"Delta w = {1/3-(-0.948):.3f}, i.e. ~{dw:.0f} sigma at the wCDM uncertainty")
print("Acceleration requires w < -1/3; w=+1/3 cannot accelerate at all.")
