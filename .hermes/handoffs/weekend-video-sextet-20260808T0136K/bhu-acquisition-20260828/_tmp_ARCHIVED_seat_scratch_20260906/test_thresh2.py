import numpy as np
from scipy.optimize import root_scalar
def m_remnant_delay(m_star, z_metal):
    return 1.1 + 0.2 * np.exp((m_star - 11.0) / 4.0) - (2.0 + z_metal) * np.exp(0.4 * (m_star - 26.0))

print("10:", m_remnant_delay(10, 0.5) - 2.5)
print("22:", m_remnant_delay(22, 0.5) - 2.5)
res = root_scalar(lambda m: m_remnant_delay(m, 0.5) - 2.5, bracket=[10, 22])
print(res.root)
