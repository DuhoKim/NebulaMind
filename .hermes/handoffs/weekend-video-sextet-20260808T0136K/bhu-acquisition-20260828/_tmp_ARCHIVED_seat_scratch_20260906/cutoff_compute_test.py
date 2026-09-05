import numpy as np
from scipy.integrate import simpson
import camb
from camb import initialpower
from scipy.special import eval_legendre
from numpy.polynomial.legendre import leggauss

H0 = 67.36
ombh2 = 0.02237
omch2 = 0.1200
tau = 0.0544
As = 2.1e-9
ns = 0.9649
mnu = 0.06
KP = 0.05
L = 3.149 * 299792.458 / H0

def s12_matrix(l_max):
    n_nodes = l_max + 2
    x_std, w_std = leggauss(n_nodes)
    a, b = -1.0, 0.5
    x = 0.5 * (b - a) * x_std + 0.5 * (b + a)
    w = 0.5 * (b - a) * w_std
    P = np.zeros((l_max + 1, len(x)))
    for l in range(l_max + 1):
        c = np.zeros(l + 1)
        c[l] = 1.0
        P[l] = np.polynomial.legendre.legval(x, c)
    I = (P * w) @ P.T
    l = np.arange(l_max + 1)
    pref = (2 * l + 1) / (4 * np.pi)
    M = np.outer(pref, pref) * I
    return M

def s12_from_cl(cl, M):
    return float(cl @ M @ cl)

def get_S12(k_arr, P_arr):
    p = camb.CAMBparams()
    p.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=mnu, omk=0, tau=tau)
    p.set_for_lmax(300, lens_potential_accuracy=0)
    p.WantTensors = False
    p.DoLensing = False
    p.NonLinear = camb.model.NonLinear_none
    ip = initialpower.SplinedInitialPower()
    ip.set_scalar_table(k_arr, P_arr)
    ip.effective_ns_for_nonlinear = ns
    p.InitPower = ip
    res = camb.get_results(p)
    cl = res.get_unlensed_scalar_cls(CMB_unit='muK', raw_cl=True, lmax=300)[:,0]
    M = s12_matrix(300)
    # Zero out monopole and dipole
    cl_work = cl.copy()
    cl_work[0] = 0
    cl_work[1] = 0
    return s12_from_cl(cl_work, M)

def get_S12_LCDM():
    p = camb.CAMBparams()
    p.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=mnu, omk=0, tau=tau)
    p.set_for_lmax(300, lens_potential_accuracy=0)
    p.WantTensors = False
    p.DoLensing = False
    p.NonLinear = camb.model.NonLinear_none
    p.InitPower.set_params(As=As, ns=ns, pivot_scalar=KP)
    res = camb.get_results(p)
    cl = res.get_unlensed_scalar_cls(CMB_unit='muK', raw_cl=True, lmax=300)[:,0]
    M = s12_matrix(300)
    cl_work = cl.copy()
    cl_work[0] = 0
    cl_work[1] = 0
    return s12_from_cl(cl_work, M)

def j0(x):
    return np.sinc(x/np.pi) # np.sinc is sin(pi x)/(pi x), so np.sinc(x/pi) is sin(x)/x

# k grid for integral
k_max = 10.0
r_grid = np.linspace(1e-5, L, 2000)

for k_min in [1e-4, 1e-5, 1e-6, 1e-7]:
    k_int = np.geomspace(k_min, k_max, 5000)
    # Delta^2(k)
    Delta2 = As * (k_int / KP)**(ns - 1)
    # xi_LCDM(r)
    xi_LCDM = np.zeros_like(r_grid)
    for i, r in enumerate(r_grid):
        integrand = (Delta2 / k_int) * j0(k_int * r)
        xi_LCDM[i] = simpson(integrand, x=k_int)
    
    # window
    x = r_grid / L
    W = (1 - x)**2 * (2 + x) / 2
    xi_B = xi_LCDM * W
    
    # P_B
    k_out = np.geomspace(1e-7, 2.0, 2000)
    P_B = np.zeros_like(k_out)
    for i, k in enumerate(k_out):
        integrand = r_grid**2 * xi_B * j0(k * r_grid)
        P_raw = 4 * np.pi * simpson(integrand, x=r_grid)
        P_B[i] = (k**3 / (2 * np.pi**2)) * P_raw
    
    # Check normalization
    # at k = 1.0 (high k)
    idx_norm = np.searchsorted(k_out, 1.0)
    ratio = P_B[idx_norm] / (As * (k_out[idx_norm] / KP)**(ns - 1))
    # print("Norm ratio at k=1.0:", ratio)
    P_B_norm = P_B / ratio
    # Ensure P_B >= 0
    P_B_norm = np.maximum(P_B_norm, 1e-30*As)
    
    s12 = get_S12(k_out, P_B_norm)
    print(f"k_min = {k_min:.1e}, S_1/2 = {s12:.1f} uK^4")

print(f"LCDM S_1/2 = {get_S12_LCDM():.1f} uK^4")
