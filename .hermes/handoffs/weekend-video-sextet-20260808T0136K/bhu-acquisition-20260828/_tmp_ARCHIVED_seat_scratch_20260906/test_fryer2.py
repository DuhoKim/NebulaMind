import numpy as np
from scipy.optimize import root_scalar

def m_remnant_delay(m_star, z_metal):
    return 1.1 + 0.2 * np.exp((m_star - 11.0) / 4.0) - (2.0 + z_metal) * np.exp(0.4 * (m_star - 26.0))

def m_remnant_rapid(m_star, z_metal):
    m_star = np.asarray(m_star)
    res = np.zeros_like(m_star, dtype=float)
    mask = m_star < 22.0
    res[mask] = 1.1 + 0.2 * np.exp((m_star[mask] - 11.0) / 7.5) + 10.0 * (1.0 + z_metal) * np.exp(-((m_star[mask] - 23.5)**2) / (1.0 + z_metal)**2)
    res[~mask] = m_remnant_delay(m_star[~mask], z_metal) - 1.85 + 0.25 * z_metal + 10.0 * (1.0 + z_metal) * np.exp(-((m_star[~mask] - 23.5)**2) / (1.0 + z_metal)**2)
    if res.ndim == 0:
        return float(res)
    return res

def find_thresh(z_metal, func, m_ns_max):
    try:
        res = root_scalar(lambda m: func(m, z_metal) - m_ns_max, bracket=[10, 30])
        return res.root
    except ValueError:
        return np.nan

print("Delay Z=0.01:", find_thresh(0.01, m_remnant_delay, 2.5))
print("Rapid Z=0.01:", find_thresh(0.01, m_remnant_rapid, 2.5))
print("Delay Z=1.0:", find_thresh(1.0, m_remnant_delay, 2.5))
print("Rapid Z=1.0:", find_thresh(1.0, m_remnant_rapid, 2.5))
