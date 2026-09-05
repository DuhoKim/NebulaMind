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
    for l in range(2, min(lmax, 1000)+1): # limit to l=1000 for speed
        if cl[l] == 0: continue
        Cl_true = cl[l] * 2 * np.pi / (l * (l + 1))
        Pl = lpn(l, x)[0][-1]
        val += (2*l + 1) / (4 * np.pi) * Cl_true * Pl
    return val

def get_S12(cl):
    xs = np.linspace(-1, 0.5, 500)
    thetas = np.degrees(np.arccos(xs))
    C_th = np.array([get_ctheta(cl, t) for t in thetas])
    S12 = simpson(C_th**2, x=xs)
    return S12

chi_cmb = results.conformal_time(0) - results.tau_maxvis
print(f"chi_CMB = {chi_cmb:.2f} Mpc")

def get_truncated_cl(kcut):
    pars_trunc = pars.copy()
    ks = np.logspace(-5, 1, 10000)
    Pk = np.zeros_like(ks)
    for i, k in enumerate(ks):
        if k > kcut:
            Pk[i] = 2.1e-9 * (k / 0.05)**(0.965 - 1)
        else:
            Pk[i] = 0.0
    # Provide a very small non-zero value at low k
    Pk[Pk == 0] = 1e-30
    pars_trunc.set_initial_power_table(ks, Pk)
    results_trunc = camb.get_results(pars_trunc)
    powers_trunc = results_trunc.get_cmb_power_spectra(pars_trunc, CMB_unit='muK')
    return powers_trunc['total'][:,0]

S12_lcdm = get_S12(cl_TT_lcdm)
C2_lcdm = cl_TT_lcdm[2] * 2 * np.pi / 6
print(f"LCDM C2 = {C2_lcdm:.2f} muK^2, S1/2 = {S12_lcdm:.2f} muK^4")

# Using theta_cut = 60 deg -> k_cut = pi / R.
# In 2204.11608: theta_cut = 2R / chi_cmb = 60 deg -> R = chi_cmb * (60 deg)/2 = chi_cmb * 30 deg = chi_cmb * pi / 6.
# Then k_cut = pi / R = pi / (chi_cmb * pi / 6) = 6 / chi_cmb.
kcut_R = np.pi / (chi_cmb * np.pi / 6)
cl_trunc_R = get_truncated_cl(kcut_R)
print(f"k_cut = 6/chi_cmb = {kcut_R:.5f}")
print(f"Trunc(R) C2 = {cl_trunc_R[2]*2*np.pi/6:.2f}, S1/2 = {get_S12(cl_trunc_R):.2f}")

# What if it's chi_S = chi_cmb * 60 deg? -> R = chi_cmb * 60 deg = chi_cmb * pi / 3.
# k_cut = pi / R = 3 / chi_cmb
kcut_chiS = np.pi / (chi_cmb * np.pi / 3)
cl_trunc_chiS = get_truncated_cl(kcut_chiS)
print(f"k_cut = 3/chi_cmb = {kcut_chiS:.5f}")
print(f"Trunc(chiS) C2 = {cl_trunc_chiS[2]*2*np.pi/6:.2f}, S1/2 = {get_S12(cl_trunc_chiS):.2f}")

