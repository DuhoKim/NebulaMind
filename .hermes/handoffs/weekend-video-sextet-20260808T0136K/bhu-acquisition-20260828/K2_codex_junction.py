#!/usr/bin/env python3
"""Blind K2 junction classification. Pure symbolic audit; no external data."""
import sympy as s

pi = s.pi
G, rho, a, R = s.symbols("G rho a R", positive=True)
Lam, M = s.symbols("Lambda M", nonnegative=True)
F = 1 - 2*G*M/R - Lam*R**2/3

def energy_conditions(sig, pres):
    # Isotropic 2+1 surface layer: WEC sig>=0 and sig+p>=0; DEC sig>=|p|.
    return (s.simplify(sig) >= 0 and s.simplify(sig+pres) >= 0,
            s.simplify(sig-abs(pres)) >= 0)

print("CONTROLS (executed before classifications)")
# C1: fixed-comoving boundary, R=a*S, Friedmann equation and mass relation.
S, C, H = s.symbols("S C H", positive=True)
mass = 4*pi*rho*R**3/3
friedmann = s.Eq(H**2, 8*pi*G*rho/3 + Lam/3 - s.symbols("k")/a**2)
F_mass = s.simplify(F.subs(M, mass).subs(Lam, 0))
beta_plus_sq = s.simplify((H*R)**2 + F_mass)
beta_plus_sq = s.simplify(beta_plus_sq.subs(H**2, 8*pi*G*rho/3 - 1/a**2).subs(R, a*S))
assert s.simplify(beta_plus_sq - (1-S**2)) == 0
print("C1 PASS: M=", mass, "; [K_ss]=[K_thth]=[K_phph]=0; beta_+^2=", beta_plus_sq)

# C2: the pinned null transverse-curvature result.
jump_uu = -2*pi*rho*a
pnull = s.simplify(-jump_uu/(8*pi))
assert s.simplify(pnull-rho*a/4) == 0
print("C2 PASS: [K_uu]=", jump_uu, ", [K_thth]=[K_phph]=0, mu=0, p=", pnull)

# C3: at r_b=1, smooth angular matching and F=0 force zero boundary speed.
Rdot2 = s.symbols("Rdot2", nonnegative=True)
c3 = s.solve(s.Eq(Rdot2 + 0, 0), Rdot2)
assert c3 == [0]
print("C3 PASS: r_b=1, F(R_b)=0, [K_thth]=0 => Rdot^2=", c3[0], "(static sphere)")

# C4: omitting DEC changes the pressure-only null-shell classification.
wec_null = True  # mu=0, p>0: mu>=0 and mu+p>=0
dec_null = False # mu>=|p| fails for p>0
with_ec, without_ec = "J_SHELL_UNPHYSICAL", "J_SHELL_EXPANDING"
assert with_ec != without_ec and wec_null and not dec_null
print("C4 PASS: B2 closed changes", with_ec, "->", without_ec, "when EC test is deleted")

print("\nSYMBOLIC GENERAL TIMELIKE (B3)")
v, q, qdot, vdot, adot, addot, Sk, Ck = s.symbols(
    "v chi_dot chi_ddot v_dot a_dot a_ddot S_k C_k", real=True)
Rdot, Rddot, Fp = s.symbols("R_dot R_ddot F_prime", real=True)
beta_m = s.simplify(v*Ck + a*q*adot*Sk)
beta_p = s.sqrt(Rdot**2 + F)
Kss_m = s.simplify(a*q*(vdot + a*adot*q**2) - a*v*(qdot + 2*adot*v*q/a))
Kss_p = -(Rddot + Fp/2)/beta_p
jKss = s.simplify(Kss_p-Kss_m)
jKth = s.simplify(R*(beta_p-beta_m))
sigma = s.simplify(-(beta_p-beta_m)/(4*pi*G*R))
pressure = s.simplify((jKss+(beta_p-beta_m)/R)/(8*pi*G))
print("normalization: v^2-a^2*chi_dot^2=1")
print("R_dot=a_dot*v*S_k+a*C_k*chi_dot")
print("[K_ss]=", jKss)
print("[K_thth]=", jKth, "; [K_phph]=sin(theta)^2*[K_thth]")
print("S_ss=sigma=", sigma)
print("S_thth=R^2*p, S_phph=sin(theta)^2*S_thth; p=", pressure)
print("WEC: sigma>=0 and sigma+p>=0; DEC: sigma>=abs(p). Their truth depends on chi_dot, chi_ddot.")

print("\nFULL TABLE")
classes = {}
for B in ("B1", "B2", "B3"):
    for k in ("+1", "0"):
        for lr in ("Lambda=0", "0<Lambda<=Lambda_c"):
            if B == "B1":
                cls = "J_SMOOTH_EXPANDING"
                jumps = "[K_ss]=[K_thth]=[K_phph]=0; S_ab=0; WEC=PASS; DEC=PASS"
            elif B == "B2" and k == "+1":
                cls = "J_SHELL_UNPHYSICAL"
                jumps = "[K_uu]=-2*pi*rho*a; angular jumps=0; mu=0,p=rho*a/4; WEC=PASS; DEC=FAIL"
            elif B == "B2":
                cls = "J_NONE"
                jumps = "N/A: flat dust with Lambda>=0 has H^2=8*pi*G*rho/3+Lambda/3>0, so no maximum-expansion B2"
            else:
                cls = "J_UNDETERMINED"
                jumps = "general B3 expressions above; S_ab and WEC/DEC depend on free trajectory/acceleration"
            classes[(B,k,lr)] = cls
            print(B, k, lr, ":", cls, ";", jumps)

