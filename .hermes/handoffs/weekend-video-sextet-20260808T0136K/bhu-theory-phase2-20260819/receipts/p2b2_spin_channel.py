"""p2b2-R2: the a* channel — ECSK first principles, order-of-magnitude, every assumption named.
FACT (pinned): torsion couples to INTRINSIC spin only (PLB main.tex line 98: Dirac fields
couple minimally to torsion; the Cartan equation sources torsion with the spin tensor).
The parent's macroscopic J is ORBITAL: it enters the interior as fluid vorticity in the
metric sector, exactly as in GR. Two derivable pieces:
(A) Self-consistency ceiling on inherited J: the published bounce assumes a homogeneous
    non-rotating interior; rotation must be sub-relativistic at the bounce patch
    (v_rot = J_b/(xi M R_b) < c), else centrifugal dynamics invalidates the bounce solution.
    => epsilon_max = J_b,max/J_parent = xi M c R_b / (a* G M^2/c) = xi c^2 R_b/(a* G M).
(B) Spin-polarization channel (torsion-visible): rotational polarization fraction
    ~ hbar Omega / k_B T at the bounce — computed to show it is negligible.
Assumptions named: rigid rotation; uniform-sphere inertia xi = 2/5 (bracket 0.2-0.5);
bounce density per treatment from B1/A2-certified values; V1 Planck-regime limit applies."""
import math
G, c, hbar = 6.67430e-11, 2.99792458e8, 1.054571817e-34
kB, eV = 1.380649e-23, 1.602176634e-19
Msun = 1.989e30
zeta3 = 1.2020569031595943
g_star = 28 + 7/8*90
h_dimless = math.pi**2/30*g_star
hbar_c = hbar*c
# bounce temperatures (energy units), per treatment:
T_I_K = 1.152e32                      # Treatment I: A2-certified T_max (spin-fluid, ApJ chain)
T_I = kB*T_I_K                        # J
mP_J = math.sqrt(hbar*c**5/(8*math.pi*G))
T_II = 0.785*mP_J                     # Treatment II: T_cr (B1-receipted)
print(f"bounce T: Treatment I = {T_I_K:.3e} K ({T_I/eV/1e9:.2e} GeV); "
      f"Treatment II = {T_II/eV/1e9:.2e} GeV ({T_II/kB:.2e} K)")
def eps_b(T):   # energy density at bounce, thermal form
    return h_dimless*T**4/hbar_c**3
for tag, T in (("I", T_I), ("II", T_II)):
    print(f"  eps_b({tag}) = {eps_b(T):.3e} J/m^3  (rho = {eps_b(T)/c**2:.3e} kg/m^3)")
xi = 0.4
print(f"\n(A) epsilon ceiling, xi = {xi} (bracket 0.2-0.5 noted):")
print(f"{'M':>10s} {'a*':>5s} {'treat':>6s} {'R_b [m]':>10s} {'J_par [J s]':>12s} {'eps_max':>10s}")
for Mfac in (10, 1e9):
    M = Mfac*Msun
    for astar in (0.7,):
        J = astar*G*M**2/c
        for tag, T in (("I", T_I), ("II", T_II)):
            rho = eps_b(T)/c**2
            Rb = (3*M/(4*math.pi*rho))**(1/3)
            epsmax = xi*M*c*Rb/J
            print(f"{Mfac:10.0e} {astar:5.2f} {tag:>6s} {Rb:10.2e} {J:12.2e} {epsmax:10.2e}")
# sanity: rotation rate if J were conserved vs c/R_b
M = 10*Msun; J = 0.7*G*M**2/c
rho = eps_b(T_I)/c**2; Rb = (3*M/(4*math.pi*rho))**(1/3)
Om_cons = J/(xi*M*Rb**2); Om_lim = c/Rb
print(f"\nsanity (10 Msun, a*=0.7, treat I): Omega if J conserved = {Om_cons:.2e} s^-1"
      f" vs causal limit c/R_b = {Om_lim:.2e} s^-1  -> excess {Om_cons/Om_lim:.1e}")
# scaling: eps_max ~ M^(-2/3)
print("scaling check: eps_max ratio (1e9/10 Msun) =", end=" ")
def em(Mfac, T):
    M = Mfac*Msun; J = 0.7*G*M**2/c
    rho = eps_b(T)/c**2; Rb = (3*M/(4*math.pi*rho))**(1/3)
    return xi*M*c*Rb/J
r = em(1e9, T_I)/em(10, T_I)
print(f"{r:.3e} vs (1e8)^(-2/3) = {(1e8)**(-2/3):.3e}")
# (B) polarization fraction at bounce, using the sub-relativistic ceiling rotation rate
Om_max = c/Rb
for tag, T in (("I", T_I), ("II", T_II)):
    print(f"(B) polarization ~ hbar*Omega_max/kB T ({tag}): "
          f"{hbar*(c/(3*10*Msun/(4*math.pi*eps_b(T)/c**2))**(1/3)*0+Om_max)/T:.1e}"
          if tag=="I" else
          f"(B) polarization ~ hbar*Omega_max/kB T ({tag}): {hbar*Om_max/T:.1e}")
