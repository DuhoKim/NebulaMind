#!/usr/bin/env python3
"""Independent calculation from the constants specified in the task."""

import math

G = 6.67430e-11
c = 2.99792458e8
MPC = 3.0856775814913673e22
LIGHT_YEAR = 9.4607304725808e15
M_SUN = 1.98892e30
OMEGA_LAMBDA = 0.6889


def h0_si(h0_km_s_mpc):
    return h0_km_s_mpc * 1000.0 / MPC


def quantities(h0_km_s_mpc):
    h0 = h0_si(h0_km_s_mpc)
    rho_c = 3.0 * h0**2 / (8.0 * math.pi * G)
    r_h = c / h0
    mass_volume = (4.0 / 3.0) * math.pi * rho_c * r_h**3
    mass_closed = c**3 / (2.0 * G * h0)
    r_s = 2.0 * G * mass_volume / c**2
    return h0, rho_c, r_h, mass_volume, mass_closed, r_s


def gly(metres):
    return metres / LIGHT_YEAR / 1.0e9


def main():
    h0, rho_c, r_h, mass, mass_closed, r_s = quantities(67.4)
    rel_diff = abs(mass - mass_closed) / abs(mass_closed)
    print(f"1. H0 = (67.4 x 1000) / {MPC:.16e} = {h0:.15e} s^-1")
    print(f"2. rho_c = 3 H0^2 / (8 pi G) = {rho_c:.15e} kg/m^3")
    print(f"3. R_H = c / H0 = {r_h:.15e} m = {gly(r_h):.12f} billion light years")
    print(f"4. M = (4/3) pi rho_c R_H^3 = {mass:.15e} kg = {mass/M_SUN:.15e} M_sun")
    print(f"5. M_closed = c^3 / (2 G H0) = {mass_closed:.15e} kg; relative difference = {rel_diff:.15e}")
    print(f"6. R_s = 2 G M / c^2 = {r_s:.15e} m = {gly(r_s):.12f} billion light years")
    print(f"7. R_s / R_H = {r_s/r_h:.12f}")
    print("8. H0 sweep:")
    for h in (50.0, 73.0, 100.0, 500.0):
        _, _, sweep_rh, sweep_m, _, sweep_rs = quantities(h)
        print(f"   H0={h:g}: M=(4/3) pi rho_c R_H^3={sweep_m:.15e} kg ({sweep_m/M_SUN:.15e} M_sun); R_s/R_H={sweep_rs/sweep_rh:.12f}")
    mass73 = quantities(73.0)[3]
    pct = (mass73 - mass) / mass * 100.0
    print(f"9. M(H0=73.0) = {mass73:.15e} kg = {mass73/M_SUN:.15e} M_sun")
    print(f"   percentage difference [M(73)-M(67.4)]/M(67.4) x 100 = {pct:.12f}%")
    r_s_alt = c / (h0 * math.sqrt(OMEGA_LAMBDA))
    m_alt = c**2 * r_s_alt / (2.0 * G)
    print(f"10. r_S_alt = c/[H0 sqrt(Omega_Lambda)] = {r_s_alt:.15e} m")
    print(f"    r_S_alt/R_H = 1/sqrt(Omega_Lambda) = {r_s_alt/r_h:.15f}")
    print(f"    M_alt = c^2 r_S_alt/(2G) = {m_alt/M_SUN:.15e} M_sun")


if __name__ == "__main__":
    main()
