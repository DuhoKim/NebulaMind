#!/usr/bin/python3
"""Clean zero-production control check (no NaN from 0*inf), Riccati bound verification."""
import math
import numpy as np
from scipy.integrate import solve_ivp

def rhs(t, y):
    lx, ly, u, v, n, e = y
    H = (u + 2*v)/3.0
    K = math.exp(-2*ly)
    P = e/3.0 - 0.5*n*n   # a=0.5, b=0
    return np.array([u, v, -u*u - u*v + (v*v + K - P)/2.0,
                     -(3*v*v + K + P)/2.0, -3*H*n, -4*H*e])

H0, D0, K0, w0 = -1.0, 3.0, 1.0, 0.1
e0 = 3*H0*H0 - D0*D0/3 + K0 + w0
y0 = np.array([0.0, -0.5*math.log(K0), H0 + 2*D0/3, H0 - D0/3, math.sqrt(w0/0.5), e0])

def cap(t, y):
    return 1e6 - max(abs(y[2]), abs(y[3]), y[4], y[5])
cap.direction, cap.terminal = -1, True

sol = solve_ivp(rhs, (0., 1.0), y0, method="DOP853", rtol=1e-11, atol=1e-13,
                max_step=1e-4, events=cap, dense_output=True)
print("stop t=%.8f  (cap or end); Riccati blowup time = 1.0" % sol.t[-1])
ts = np.linspace(0, sol.t[-1], 5001)
yy = sol.sol(ts)
H = (yy[2]+2*yy[3])/3
D = yy[2]-yy[3]
K = np.exp(-2*yy[1])
n, e = yy[4], yy[5]
w = 0.5*n*n
S = D*D/3
bound = -1.0/(1.0 - ts)
print("H monotone decreasing:", bool(np.all(np.diff(H) < 0)))
print("H <= Riccati bound -1/(1-t) at all sample points:", bool(np.all(H <= bound + 1e-9)))
print("min margin w-S over interval (must stay <0):", float(np.max(w-S)), "< 0 ?")
print("Delta stays > 0:", bool(np.all(D > 0)), " Delta(last)=%.3g" % D[-1])
print("R=w/S: first=%.6f last=%.6g monotone decreasing:" % (w[0]/S[0], w[-1]/S[-1]),
      bool(np.all(np.diff(w/S) < 0)))
print("V(last)=%.3g  Y(last)=%.3g  K(last)=%.3g  e(last)=%.3g  H(last)=%.6g"
      % (math.exp(yy[0,-1]+2*yy[1,-1]), math.exp(yy[1,-1]), K[-1], e[-1], H[-1]))
# comoving number conserved (b=0): V n = const
V = np.exp(yy[0]+2*yy[1])
print("Vn conservation: max rel dev =", float(np.max(np.abs(V*n - V[0]*n[0]))/ (V[0]*n[0])))
# Kretschmann growth at end (their formula)
print("Hdot at last point =", float(-H[-1]**2 - 2*(S[-1]-w[-1])/3 - e[-1]/3))
