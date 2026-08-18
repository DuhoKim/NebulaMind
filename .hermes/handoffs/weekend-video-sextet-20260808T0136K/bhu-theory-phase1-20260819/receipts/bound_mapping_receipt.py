"""R9: map present-day rotation bounds to the spin-acquisition epoch and confront.
omega ∝ a^-2 through matter+Lambda eras (R6; the rotating component is matter, rho+P ∝ a^-3
holds through Lambda domination). (omega/H)(z) = (omega/H)_0 (1+z)^2/E(z),
E(z) = sqrt(Om(1+z)^3 + OL), flat, Om = 0.315 (Phase 0 pin S3).
Bounds: S2 (omega/H)_0 < 7.6e-10 (Planck Bianchi VII_h); S1 < 4.7e-11 (Saadeh vector mode).
Floors (Phase 0 certified): design sigma_A = 1/sqrt(1e5) = 3.16e-3, 3sigma A >= 9.5e-3;
all-sky N = 2.0e12: sigma_A = 7.07e-7. Transfer: A = C (omega/H)_ta, C = 7.19 [1.36, 12.78] (R8)."""
import math
Om, OL = 0.315, 0.685
b2, b1 = 7.6e-10, 4.7e-11
C, Clo, Chi = 7.19, 1.36, 12.78
E = lambda z: math.sqrt(Om*(1+z)**3 + OL)
print("z_ta  (w/H)@S2      A@S2(C=7.19)  [bracket]              A@S1(C=7.19)")
for z in (0.5, 1, 2, 3, 5, 10):
    r = (1+z)**2 / E(z)
    wh2, wh1 = b2*r, b1*r
    print(f"{z:4}  {wh2:.3e}  {C*wh2:.3e}  [{Clo*wh2:.1e},{Chi*wh2:.1e}]  {C*wh1:.3e}")
# confrontation
z = 3.0; r = (1+z)**2/E(z); A = C*b2*r
print(f"\nfiducial z_ta=3, S2, headline C: A = {A:.2e}")
print(f"vs 3sigma design floor 9.5e-3: {9.5e-3/A:.1e}x short ({math.log10(9.5e-3/A):.1f} orders)")
print(f"vs all-sky 1sigma 7.07e-7: significance = {A/7.07e-7:.3f} sigma")
print(f"vs Phase 0 generous bracket edge 5.2e-7: strict/generous = {A/5.2e-7:.3f}")
Nneed = 9/A**2
print(f"N for 3sigma at strict A: {Nneed:.2e} galaxies = {Nneed/2.0e12:.1e} observable universes")
