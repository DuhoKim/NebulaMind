import numpy as np

def m_remnant_delay(m_star, z_metal):
    return 1.1 + 0.2 * np.exp((m_star - 11.0) / 4.0) - (2.0 + z_metal) * np.exp(0.4 * (m_star - 26.0))

def m_remnant_rapid(m_star, z_metal):
    res = np.zeros_like(m_star)
    mask = m_star < 22.0
    res[mask] = 1.1 + 0.2 * np.exp((m_star[mask] - 11.0) / 7.5) + 10.0 * (1.0 + z_metal) * np.exp(-((m_star[mask] - 23.5)**2) / (1.0 + z_metal)**2)
    res[~mask] = m_remnant_delay(m_star[~mask], z_metal) - 1.85 + 0.25 * z_metal + 10.0 * (1.0 + z_metal) * np.exp(-((m_star[~mask] - 23.5)**2) / (1.0 + z_metal)**2)
    return res

m = np.linspace(10, 30, 100)
for z in [0.01, 1.0]:
    d = m_remnant_delay(m, z)
    r = m_remnant_rapid(m, z)
    print(f"Z={z}")
    print("Delay min, max:", d.min(), d.max())
    print("Rapid min, max:", r.min(), r.max())
