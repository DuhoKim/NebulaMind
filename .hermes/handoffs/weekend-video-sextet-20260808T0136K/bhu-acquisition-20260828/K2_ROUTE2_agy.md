ACCESS_SHA=62589338594bf7c054df973f06e4a30e0b9a399e7d3fa7d533e965e49abf9cf3
ENTRY56_CELL=J_SMOOTH_EXPANDING
PATHRIA_CELL=J_SHELL_UNPHYSICAL
B3_NOSHELL=comoving-only

**Controls:**
- **C1:** B1 (k=+1, Λ=0) reproduces textbook Oppenheimer-Snyder smooth matching; Misner-Sharp mass continuity yields $M_T = M_0 \sin^3(\chi^*)$, expanding into the $F(R)<0$ exterior region.
- **C2:** B2 null-junction jump reproduces Khakshournia's $[K_{uu}] = -2\pi \rho a$ and shell pressure $p = \rho a / 4$.
- **C3:** Smooth timelike matching at $r_b=1$ ($\chi=\pi/2$) gives $F(R) = -\dot{a}^2$. A strictly static exterior ($F>0$) thus forces $\dot{a}=0$ everywhere, reproducing Knutsen's static-sphere constraint.
- **C4:** The Pathria cell (B2) shell has $\sigma=0$ and $p = \rho a / 4$. This violates the Dominant Energy Condition ($\sigma \ge |p|$ is false). Removing the DEC test changes its class to J_SHELL_EXPANDING.

**Key Matching Equations (LTB/PG coordinates):**
Interior (FRW): $ds^2 = -d\tau^2 + \frac{R'^2}{1 - k S_k(r)^2} dr^2 + R^2 d\Omega^2$ with $R(\tau,r) = a(\tau)S_k(r)$.
Exterior (SdS in same slicing): $\dot{R}^2 = -k S_k(r)^2 + \frac{2GM_T}{R} + \frac{\Lambda}{3}R^2$.
Smooth matching requires identical induced metrics and continuous Misner-Sharp mass ($[K_{\theta\theta}]=0$): $M_T = M_0 S_k(r^*)^3$. Since $M_T$ is constant, $r^*(\tau)$ must be strictly comoving.
