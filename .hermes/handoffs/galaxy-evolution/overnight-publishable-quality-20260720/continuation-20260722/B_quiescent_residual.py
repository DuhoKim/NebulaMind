import numpy as np
# Honest statistics of the z>6 spectroscopic massive-quiescent residual (Paper B).
# TNG predicts ~0 massive quiescent at z>6; observations: ~1 confirmed object (RUBIES-class).
# So the "excess" is existence vs statistics-of-one, NOT a well-measured density ratio.

# Cosmology (flat LCDM)
H0, Om, OL, c = 70.0, 0.3, 0.7, 299792.458
def E(z): return np.sqrt(Om*(1+z)**3 + OL)
def Dc(z):  # comoving distance [Mpc]
    zz=np.linspace(0,z,2000); return (c/H0)*np.trapz(1/E(zz), zz)

# Survey: RUBIES-class effective area ~150 arcmin^2, redshift window z=6.5-7.5
area_arcmin2 = 150.0
Omega_sr = area_arcmin2/3600.0*(np.pi/180)**2       # solid angle [sr]
z1,z2 = 6.5,7.5
zz=np.linspace(z1,z2,400)
Dcs=np.array([Dc(z) for z in zz])
Vc = Omega_sr*np.trapz(Dcs**2*(c/H0)/E(zz), zz)      # comoving volume [Mpc^3]
print(f"Survey comoving volume (z={z1}-{z2}, {area_arcmin2} arcmin^2): {Vc:.3e} Mpc^3")

# 1 object -> density + Poisson 68% CI (Gehrels 1986 for N=1: [0.173, 3.30])
n_obs = 1/Vc
lo, hi = 0.173/Vc, 3.30/Vc
print(f"Implied n_obs = {n_obs:.2e} Mpc^-3  (Poisson 68% CI [{lo:.2e}, {hi:.2e}])")
print(f"  = 10^{np.log10(n_obs):.1f}  (range 10^{np.log10(lo):.1f} to 10^{np.log10(hi):.1f})")

# Cosmic variance for a single small field at z~7 is order-unity-to-few (~50-100%),
# comparable to the Poisson term -> total uncertainty on n_obs is ~0.5-0.7 dex.
print("\nHonest verdict:")
print("  - The residual is a factor-of-a-few (Poisson) + ~50-100% (cosmic variance) estimate from ONE object.")
print("  - Total uncertainty on log n_obs ~ 0.5-0.7 dex; the '~2 dex excess over TNG' is real in the sense")
print("    TNG predicts ~0, but the OBSERVED density is single-object / statistics-limited, not a measured ratio.")
print("  - Correct framing for B: 'the existence of z>6 massive quiescent galaxies is hard for TNG to produce,")
print("    but the quantitative excess is dominated by statistics-of-one and cosmic variance; a robust density")
print("    needs a larger confirmed sample.' -> keeps B's residual honest, not overclaimed.")
