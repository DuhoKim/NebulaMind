import math

# REPRO_EXACT exhibition: rho_c = 3 H0^2 / (8 pi G)
# H0 = 67.36 km/s/Mpc and G = 6.67430e-11 m^3 kg^-1 s^-2 are both on C3's closed STANDARD list.
H0 = 67.36 / 3.0856775814913673e19  # s^-1 (1 Mpc = 3.0856775814913673e19 km)
G = 6.67430e-11
rho_c = 3 * H0**2 / (8 * math.pi * G)
print("H0 [s^-1]        =", H0)
print("rho_c [kg/m^3]   =", rho_c)
print("2 s.f.           = %.1e" % rho_c)
print("3 s.f.           = %.2e" % rho_c)

# REPRO_FAILED exhibition: same recipe and inputs, paper prints 9.8e-27 kg/m^3
print("9.8e-27 mismatch = %.1f%% off" % (abs(9.8e-27 - rho_c) / rho_c * 100))

# CENSUS_ORIGIN_DISPUTED threshold check
print("5/40 =", 5 / 40 * 100, "percent (exceeds 10)")
print("4/40 =", 4 / 40 * 100, "percent (does not exceed 10)")
