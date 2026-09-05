import numpy as np
import camb
from camb import model, initialpower
from scipy.integrate import simpson
from scipy.special import lpn

pars = camb.CAMBparams()
pars.set_cosmology(H0=67.4, ombh2=0.0224, omch2=0.120, mnu=0.06, omk=0, tau=0.054)
pars.InitPower.set_params(As=2.1e-9, ns=0.965, r=0)
pars.set_for_lmax(2500, lens_potential_accuracy=0)
results = camb.get_results(pars)
powers = results.get_cmb_power_spectra(pars, CMB_unit='muK')
cl_TT_lcdm = powers['total'][:,0]

def get_ctheta(cl, theta_deg):
    theta_rad = np.radians(theta_deg)
    x = np.cos(theta_rad)
    lmax = len(cl) - 1
    val = 0.0
    for l in range(2, min(lmax, 1000)+1): 
        if cl[l] == 0: continue
        Cl_true = cl[l] * 2 * np.pi / (l * (l + 1))
        Pl = lpn(l, x)[0][-1]
        val += (2*l + 1) / (4 * np.pi) * Cl_true * Pl
    return val

# Compute LCDM C(theta)
xs = np.linspace(-1, 1, 1000)
thetas = np.degrees(np.arccos(xs))
C_th = np.array([get_ctheta(cl_TT_lcdm, t) for t in thetas])

# Truncate C(theta) at theta > 60
C_th_trunc = np.copy(C_th)
C_th_trunc[thetas > 60] = 0.0

# Compute S_1/2 for the truncated C(theta)
xs_S12 = np.linspace(-1, 0.5, 500)
thetas_S12 = np.degrees(np.arccos(xs_S12))
C_th_S12 = np.interp(xs_S12, xs, C_th_trunc) # Wait, xs is increasing? No, arccos(xs) means xs is from -1 to 1.
# let's be careful. xs goes from -1 to 1.
S12_trunc = simpson(C_th_S12**2, x=xs_S12)
print(f"Truncated C(theta) S1/2 = {S12_trunc:.5f}")

# Compute C_2 for the truncated C(theta)
# C_l = 2pi * int_{-1}^{1} C(theta) P_l(cos theta) d(cos theta)
P2 = [lpn(2, x)[0][-1] for x in xs]
C2_true = 2 * np.pi * simpson(C_th_trunc * P2, x=xs)
D2_trunc = C2_true * 6 / (2 * np.pi)
print(f"Truncated C(theta) D2 (i.e. l(l+1)C2/2pi) = {D2_trunc:.2f} muK^2")

