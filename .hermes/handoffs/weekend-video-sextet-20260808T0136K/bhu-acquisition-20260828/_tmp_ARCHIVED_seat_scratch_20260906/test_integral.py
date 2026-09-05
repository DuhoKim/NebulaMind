import numpy as np
from scipy.integrate import quad

ln_10_10_As = 3.044
As_obs = np.exp(ln_10_10_As) * 1e-10
ns_obs = 0.9649
k0 = 0.05 
Gamma = 0.21
def T_CDM(k):
    q = k / Gamma
    return np.log(1 + 2.34*q)/(2.34*q) * (1 + 3.89*q + (16.1*q)**2 + (5.46*q)**3 + (6.71*q)**4)**(-0.25)
def P_R(k, As=As_obs):
    return As * (k / k0)**(ns_obs - 1.0)
def P_m(k, As=As_obs):
    return P_R(k, As) * k**4 * T_CDM(k)**2
def W_th(kR):
    return 3 * (np.sin(kR) - kR * np.cos(kR)) / kR**3
def integrand(lk):
    k = np.exp(lk)
    return (k**3 * P_m(k, As_obs) / (2 * np.pi**2)) * W_th(k * 8.0)**2

print(integrand(-5))
val, err = quad(integrand, -20, 5)
print("quad result:", val)
