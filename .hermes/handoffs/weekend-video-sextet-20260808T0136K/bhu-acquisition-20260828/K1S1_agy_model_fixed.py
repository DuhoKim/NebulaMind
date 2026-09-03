import numpy as np
from scipy.optimize import root_scalar
from scipy.integrate import quad
from scipy.special import erfc

ln_10_10_As = 3.044
As_obs = np.exp(ln_10_10_As) * 1e-10
ns_obs = 0.9649
k0 = 0.05 
Gamma = 0.21

def T_CDM(k):
    q = k / Gamma
    return np.log(1 + 2.34*q)/(2.34*q) * (1 + 3.89*q + (16.1*q)**2 + (5.46*q)**3 + (6.71*q)**4)**(-0.25)

def W_th(kR):
    return 3 * (np.sin(kR) - kR * np.cos(kR)) / kR**3

def unnorm_sigma_sq(As):
    # Integral with shape As * k^(ns-1) * k^4 * T^2 * W^2
    integrand = lambda lk: np.exp(lk)**3 * As * (np.exp(lk)/k0)**(ns_obs-1.0) * np.exp(lk)**4 * T_CDM(np.exp(lk))**2 * W_th(np.exp(lk)*8.0)**2
    return quad(integrand, -15, 10)[0]

norm_factor = (0.811**2) / unnorm_sigma_sq(As_obs)

def sigma_halo(As):
    return np.sqrt(norm_factor * unnorm_sigma_sq(As))

k_PBH = 1e6
def sigma_PBH(As):
    # For PBH, just use the primordial power spectrum variance approx P_R
    return np.sqrt(As * (k_PBH/k0)**(ns_obs - 1.0))

def m_remnant_delay(m_star, z_metal):
    return 1.1 + 0.2 * np.exp((m_star - 11.0) / 4.0) - (2.0 + z_metal) * np.exp(0.4 * (m_star - 26.0))

def m_remnant_rapid(m_star, z_metal):
    m_star = np.asarray(m_star)
    res = np.zeros_like(m_star, dtype=float)
    mask = m_star < 22.0
    res[mask] = 1.1 + 0.2 * np.exp((m_star[mask] - 11.0) / 7.5) + 10.0 * (1.0 + z_metal) * np.exp(-((m_star[mask] - 23.5)**2) / (1.0 + z_metal)**2)
    res[~mask] = m_remnant_delay(m_star[~mask], z_metal) - 1.85 + 0.25 * z_metal + 10.0 * (1.0 + z_metal) * np.exp(-((m_star[~mask] - 23.5)**2) / (1.0 + z_metal)**2)
    return float(res) if res.ndim == 0 else res

def find_m_thresh(m_ns_max, z_metal, mode):
    func = m_remnant_delay if mode == 'delayed' else m_remnant_rapid
    try:
        res = root_scalar(lambda m: func(m, z_metal) - m_ns_max, bracket=[10, 22])
        return res.root
    except ValueError:
        return np.nan

def imf_fraction(m_thresh, alpha3):
    num = (150**(1-alpha3) - m_thresh**(1-alpha3)) / (1-alpha3)
    den = (150**(1-alpha3) - 1**(1-alpha3)) / (1-alpha3)
    return num / den

delta_c_halo = 1.686
rho_m = 4e10 
obs_mass_density = 5e7

def N_st(As, m_ns_max, alpha3, z_metal, mode, C_eff):
    f_coll = erfc(delta_c_halo / (np.sqrt(2) * sigma_halo(As)))
    m_th = find_m_thresh(m_ns_max, z_metal, mode)
    f_imf = imf_fraction(m_th, alpha3)
    return C_eff * f_coll * f_imf

def N_PBH(As, delta_c):
    beta = erfc(delta_c / (np.sqrt(2) * sigma_PBH(As)))
    return (rho_m / 10.0) * beta

def N_BH(As, m_ns_max, alpha3, z_metal, mode, delta_c, C_eff):
    return N_st(As, m_ns_max, alpha3, z_metal, mode, C_eff) + N_PBH(As, delta_c)

print("--- CONTROLS ---")
center_alpha3 = 2.3
center_z = 0.5
center_mode = 'delayed'
center_dc = 0.483

f_coll_obs = erfc(delta_c_halo / (np.sqrt(2) * sigma_halo(As_obs)))
m_th_obs = find_m_thresh(2.5, center_z, center_mode)
f_imf_obs = imf_fraction(m_th_obs, center_alpha3)
C_eff_obs = (obs_mass_density / 10.0) / (f_coll_obs * f_imf_obs) 

N_st_obs = N_st(As_obs, 2.5, center_alpha3, center_z, center_mode, C_eff_obs)
print(f"C1: stellar-BH density magnitude: N_st = {N_st_obs:.2e}, mass density ~ {N_st_obs*10:.2e} M_sun/Mpc^3 (Target: 5e7)")

beta_obs = erfc(center_dc / (np.sqrt(2) * sigma_PBH(As_obs)))
f_pbh = beta_obs
print(f"C2: PBH fraction f = {f_pbh:.2e} < 1")

N_st_up = N_st(As_obs*1.01, 2.5, center_alpha3, center_z, center_mode, C_eff_obs)
print(f"C3: stellar-only sign of dN_BH/dlnAs = {np.sign(N_st_up - N_st_obs)}")

corners = []
for a3 in [1.6, 3.0]:
    for mode in ['delayed', 'rapid']:
        for z in [0.01, 1.0]:
            for dc in [0.3, 0.666]:
                corners.append((a3, mode, z, dc))
corners.insert(0, (center_alpha3, center_mode, center_z, center_dc)) # add center

print(f"{'alpha3':<6} {'mode':<10} {'Z':<5} {'dc':<6} | {'dAs (FD)':<10} {'dAs (An)':<10} | {'dM (FD)':<10} {'dM (An)':<10}")
for a3, mode, z, dc in corners:
    eps_As = As_obs * 1e-4
    eps_M = 1e-4
    N0 = N_BH(As_obs, 2.5, a3, z, mode, dc, C_eff_obs)
    N_As = N_BH(As_obs + eps_As, 2.5, a3, z, mode, dc, C_eff_obs)
    N_M = N_BH(As_obs, 2.5 + eps_M, a3, z, mode, dc, C_eff_obs)
    fd_As = (N_As - N0) / (eps_As / As_obs)
    fd_M = (N_M - N0) / eps_M
    
    x = delta_c_halo / (np.sqrt(2) * sigma_halo(As_obs))
    d_erfc_dx = -2 / np.sqrt(np.pi) * np.exp(-x**2)
    dx_dlnAs = -0.5 * x
    an_As = C_eff_obs * imf_fraction(find_m_thresh(2.5, z, mode), a3) * d_erfc_dx * dx_dlnAs
    
    m_th = find_m_thresh(2.5, z, mode)
    df_imf_dm = -(m_th**-a3) / ((150**(1-a3) - 1**(1-a3))/(1-a3))
    eps = 1e-5
    func = m_remnant_delay if mode == 'delayed' else m_remnant_rapid
    drem_dm = (func(m_th+eps, z) - func(m_th-eps, z)) / (2*eps)
    an_M = C_eff_obs * erfc(delta_c_halo / (np.sqrt(2) * sigma_halo(As_obs))) * df_imf_dm * (1.0 / drem_dm)
    
    print(f"{a3:<6.1f} {mode:<10} {z:<5.2f} {dc:<6.3f} | {fd_As:>10.2e} {an_As:>10.2e} | {fd_M:>10.2e} {an_M:>10.2e}")

