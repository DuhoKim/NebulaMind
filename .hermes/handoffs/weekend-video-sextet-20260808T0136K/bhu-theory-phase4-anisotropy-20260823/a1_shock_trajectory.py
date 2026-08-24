#!/usr/bin/env python3
"""A1: shock-trajectory numerics for the Smoller-Temple inside-the-horizon model.

Tori's implementation, written BLIND to platoon/gpt1_blind_a1/ (the independent seat).
Equation source: astro-ph/0210105 clean text (sha256 82fd8322...), equations cited by number.

System (S = 1/N, N = (shock distance in Hubble lengths)^2 per Sec.6 line "the number of
Hubble lengths sqrt(N)_0 from the FRW center to the shock"):

  (5.4)  du/dS = [(1+u)/(2(1+3u)S)] * [((3u-1)(sigma-u) + 6u(1+u)S) / ((sigma-u) + (1+u)S)]
  (4.3)  v = [-sigma(1+u) + (sigma-u)N] / [(1+u) + (sigma-u)N]
  (4.5)  s = sqrt(N) * (sigma-u)/(1+u)
  (4.2)  dr/dN = -r/((1+3u)N)   ->   d ln r / dS = 1/((1+3u)S)
  (5.6)  admissibility: S < [(1-u)/(1+u)] * [(sigma-u)/(sigma+u)]

Seed (derived by hand from (5.4) near S=0, sigma=1/3; derivation in A1_RECEIPT.md):
  u(S) = 1/3 - (4/3) sqrt(S) + O(S)

Time mapping (derived, FRW side, sigma=1/3 so H=1/(2t), rbar = 2 t sqrt(N)):
  dt/d(sqrtN) = 2t/(s - sqrtN), t(sqrtN=1) = t0
Cross-check: rbar from (4.2) integration must equal 2 t sqrt(N) up to one global constant.
"""
import numpy as np
from scipy.integrate import solve_ivp
import csv, sys

SIGMA = 1.0/3.0
EPS   = 1e-12

def dudS(S, y):
    u = y[0]
    num = (3*u - 1)*(SIGMA - u) + 6*u*(1+u)*S
    den = (SIGMA - u) + (1+u)*S
    return [ (1+u)/(2*(1+3*u)*S) * num/den ]

# --- integrate u(S) BACKWARD from the regular S=1 endpoint ---
# Forward shooting from S=0 is unstable (the orbit is a saddle connection; first attempt
# diverged to den=0 — recorded in A1_RECEIPT.md). At S=1 the endpoint is regular:
# u(1)=0 exactly (5.7), and (5.4) gives du/dS|_{S=1,u=0} = -(1/2)*sigma/(1+sigma) = -1/8
# for sigma=1/3. Seed just inside with the linearization and integrate S: 1-delta -> S0.
S0 = 1e-10
delta = 1e-8
u1 = (1.0/8.0)*delta                     # u ~ -(1/8)(S-1) near S=1
sol = solve_ivp(dudS, [1.0-delta, S0], [u1], method='LSODA', rtol=1e-11, atol=1e-13,
                dense_output=True)
assert sol.success, sol.message

Sg = np.logspace(-10, 0, 40001)          # geometric grid S0..1
Sg[-1] = 1.0 - delta                    # dense solution exists on [S0, 1-delta]
u  = sol.sol(Sg)[0]
N  = 1.0/Sg
v  = (-SIGMA*(1+u) + (SIGMA-u)*N) / ((1+u) + (SIGMA-u)*N)     # (4.3)
s  = np.sqrt(N) * (SIGMA-u)/(1+u)                              # (4.5)

# --- checks against the paper's theorems (pass/fail printed) ---
checks = []
def chk(name, ok, detail=""):
    checks.append((name, bool(ok), detail)); print(("PASS " if ok else "FAIL ")+name+("  "+detail if detail else ""))

chk("Thm1: u -> 1/3 as S->0",       abs(u[0]-1/3) < 2e-5,            f"u(S0)={u[0]:.8f}")
chk("Thm1: u -> 0 as S->1",         abs(u[-1]) < 1e-6,               f"u(1)={u[-1]:.3e}")
chk("Thm1: 0 < u < 1/3 on (0,1)",   np.all((u[1:-1] > -1e-14) & (u[1:-1] < 1/3)))
chk("(5.7): v -> 0 as S->1",        abs(v[-1]) < 1e-6,               f"v(1)={v[-1]:.3e}")
chk("(4.6): 0 < v < 1 (rho entropy)", np.all((v[:-1] > 0) & (v[:-1] < 1)))
chk("(4.6): 0 < u < sigma (p entropy)", np.all(u[:-1] < SIGMA))
chk("(5.5): pbar < rhobar (u < v)", np.all(u[:-1] < v[:-1] + 1e-12))
adm = Sg < ((1-u)/(1+u))*((SIGMA-u)/(SIGMA+u) + 1e-300)
chk("(5.6) admissibility on (0,1)", np.all(adm[:-1]))
chk("Thm2: s < 1 for S in (0,1]",   np.all(s[1:] < 1.0),             f"max s={s.max():.6f}")
chk("Thm3: s -> 1 at S->0 (sigma=1/3), rate O(sqrt(S))", abs(s[0]-1.0) < 1e-4,  f"s(S0)={s[0]:.8f} (expected 1-O(sqrt(S0))=1-1e-5 scale)")

# --- rbar(S) from (4.2), normalized rbar(S=1)=1 ---
lnr = np.zeros_like(Sg)
integrand = 1.0/((1+3*u)*Sg)
for i in range(len(Sg)-2, -1, -1):     # integrate d ln r = integrand dS, anchored at S=1
    lnr[i] = lnr[i+1] - 0.5*(integrand[i]+integrand[i+1])*(Sg[i+1]-Sg[i])
rbar = np.exp(lnr)                      # rbar / rbar(N=1)

# --- t(sqrtN) from dt/dsqrtN = 2t/(s - sqrtN), anchored t=1 at sqrtN=1 (t in units of t0) ---
sqrtN = np.sqrt(N)
def u_of_S(S): return sol.sol(np.atleast_1d(min(S, 1.0-delta)))[0][0]
def dlnt_dq(q, y):                      # q = sqrtN
    S = 1.0/(q*q); uu = u_of_S(S)
    ss = q*(SIGMA-uu)/(1+uu)
    return [2.0/(ss - q)]
qspan = [1.0, sqrtN[0]]
solt = solve_ivp(dlnt_dq, qspan, [0.0], method='LSODA', rtol=1e-11, atol=1e-13, dense_output=True)
assert solt.success, solt.message
lnt = solt.sol(sqrtN)[0]
t = np.exp(lnt)                         # t / t0

# cross-check: rbar (ODE) vs 2 t sqrtN (FRW-side identity) — ratio must be one global constant
ratio = rbar/(2*t*sqrtN)
chk("cross-check (4.2) vs FRW identity rbar=2t*sqrtN: ratio constant",
    (ratio.max()-ratio.min())/ratio.mean() < 1e-5,
    f"spread={(ratio.max()-ratio.min())/ratio.mean():.2e}")
chk("t -> 0 toward Big Bang (N large)", t[0] < 1e-3, f"t(sqrtN={sqrtN[0]:.0f})={t[0]:.3e} t0")

with open("a1_results.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["S","N","sqrtN_hubble_lengths","u_pbar_over_rho","v_rhobar_over_rho",
                "shock_speed_s","rbar_over_rbar_at_N1","t_over_t0"])
    for i in range(len(Sg)):
        w.writerow([f"{Sg[i]:.10e}",f"{N[i]:.10e}",f"{sqrtN[i]:.10e}",f"{u[i]:.10e}",
                    f"{v[i]:.10e}",f"{s[i]:.10e}",f"{rbar[i]:.10e}",f"{t[i]:.10e}"])

nfail = sum(1 for _,ok,_ in checks if not ok)
print(f"\n{len(checks)-nfail}/{len(checks)} checks passed; rows={len(Sg)}")
sys.exit(1 if nfail else 0)
