# Invariant Thomson optical depth in the TOV interior

## 1. Local invariant

For a photon with affinely parametrized tangent `k^a = dx^a/dlambda`, the scattering probability measured by matter with four-velocity `U^a` is

`d tau = sigma_T n_e (-U_a k^a) d lambda`,

with the sign chosen for a future-directed photon and future-directed matter. This scalar expression, rather than a Euclidean radial column, is the starting point.

Here `A=1-N<0`; therefore `rbar` is timelike. A comoving fluid element has constant `(tbar,theta,phi)` and

`U^a = sqrt(-A) (partial_rbar)^a = sqrt(N-1) (partial_rbar)^a`,

which obeys `g_ab U^a U^b = (1/A)(-A) = -1`. Consequently

`U_a k^a = g_rbar_rbar U^rbar k^rbar = (1/A) sqrt(-A) drbar/dlambda = -[drbar/dlambda]/sqrt(N-1)`.

Thus the positive optical-depth increment along either ray orientation is

`d tau = sigma_T n_e |d rbar| / sqrt(N-1)`.

This is the invariant comoving proper-time/path increment sampled by the null ray. It is not `sigma_T n_e |drbar|`: the factor `(N-1)^(-1/2)` is required because `rbar` is timelike. The radial null condition determines `dtbar/drbar` but cancels out of `-U.k`; no value of `B` is needed.

With `n_e = f_b Y_e rhobar/m_p`,

`tau = (sigma_T f_b Y_e/m_p) I_rho`,

`I_rho = integral_(r_s)^(r_h) rhobar(rbar) d rbar/sqrt(N-1)`.

## 2. Constant-w reduction

For `pbar=w rhobar`, `w>0`, the two pinned field equations imply

`w rhobar' = [(1+w)rhobar/2] N'/(N-1)`,

hence

`rhobar/rhobar_s = [(N-1)/(N_s-1)]^alpha`,

`alpha=(1+w)/(2w)`.

Let `y=rbar/rbar_s`, `z=sqrt(N-1)`, and `K=I_rho/(rhobar_s rbar_s)`. The crossing normalization gives

`kappa rhobar_s rbar_s^2 = 3 v N_s`.

The integrated system is

`dy/dz = -2z / D`,

`dK/dz = -2 (z/z_s)^(2 alpha) / D`,

`D = (1+z^2)/y + 3 v N_s w y (z/z_s)^(2 alpha)`,

from `(y,K)=(1,0)` at `z_s=sqrt(N_s-1)` down to `z=0`. The second equation has analytically cancelled the apparent `1/z` endpoint factor.

## 3. Horizon convergence, shown

As `q=N-1 -> 0+`,

`rhobar = O(q^alpha)`.

The pressure term in `N'` is `O(q^alpha)` and vanishes, while `N/rbar -> 1/rbar_h`; therefore

`N' -> -1/rbar_h`, so `|drbar| = rbar_h |dq| [1+o(1)]`.

The endpoint contribution is consequently

`I_rho(endpoint) proportional to integral_0^epsilon q^(alpha-1/2) dq = epsilon^(alpha+1/2)/(alpha+1/2)`.

It converges iff `alpha>-1/2`. Every scanned `w>0` has `alpha=(1+w)/(2w)>1/2`, so all four integrals converge. The weakest scanned exponent is `alpha=2.1666667` at `w=0.30`; its omitted tail scales as `epsilon^2.6666667`.

The numerical cutoff table `p1_convergence.csv` independently exhibits settlement. For the weakest endpoint (`w=0.30`), `K(N-1>=10^-2)` is already 0.9999989832 of the endpoint value, `K(N-1>=10^-4)` is 0.9999999999952, and smaller cutoffs agree to displayed precision.

## 4. Physical conversion

Coordinates are represented in seconds (`c=1`). Then

`sigma_T,geom = sigma_T,SI/c^2`, `m_p,geom = G m_p/c^3`,

so

`tau = [sigma_T,SI c/(G m_p)] f_b Y_e I_rho`,

where `I_rho` is in `s^-1`. The physical electron column is

`N_e = [c/(G m_p)] f_b Y_e I_rho` in `m^-2`.

Optical depth itself is dimensionless in either unit system; the results table therefore supplies the geometry-only `t_crit I_rho`, the converted `I_rho [s^-1]`, the physical electron column, and the resulting dimensionless `tau`.