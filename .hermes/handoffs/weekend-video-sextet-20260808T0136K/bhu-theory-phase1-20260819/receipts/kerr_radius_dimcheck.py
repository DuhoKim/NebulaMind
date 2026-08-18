"""Receipt: dimensional check of the paper's 'Kerr radius a = M/mc' where (paper's notation)
M = angular momentum, m = mass. Also the standard form a = J/(M_bh c) and its magnitude scale."""
import sympy as sp
kg, m_, s = sp.symbols('kg m s', positive=True)
J_ang = kg * m_**2 / s        # angular momentum
mass = kg
c_dim = m_ / s
a_dim = J_ang / (mass * c_dim)
print("dim[a = J/(m c)] =", sp.simplify(a_dim), " -> length: ", sp.simplify(a_dim/m_) == 1)
# magnitude: extremal Kerr a_max = GM/c^2 (half the Schwarzschild radius)
G, c = 6.67430e-11, 2.99792458e8
Msun = 1.989e30
for MBH in (10*Msun, 1e9*Msun):
    print(f"M_BH = {MBH/Msun:.0e} Msun: a_max = GM/c^2 = {G*MBH/c**2:.3e} m")
