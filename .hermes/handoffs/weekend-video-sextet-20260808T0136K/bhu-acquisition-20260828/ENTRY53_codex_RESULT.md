AUDIT_HOLDS_CONSISTENCY_ONLY

## 1. Delta versus entry 52

The paper's actual increment is a refined internal dynamical analysis, not an independent observation-facing test. It says that the earlier bounce calculation neglected the curvature term and appeared cusp-like, and that this paper restores `k`, analyzes all `k=+1,0,-1`, and studies the turning points (lines 54–59). Starting from the curvature-retaining Friedmann equation (8), lines 112–116, it derives the dimensionless evolution equation

`ydot^2 + k = (3x^4 - 2x^6)y^2` (17; lines 167–171)

and, after inserting `y=(C/x)exp(x^2/2)`,

`ydot^2 + k = C^2(3x^2 - 2x^4)exp(x^2)` (20; lines 173–189).

That framework yields separate turning-point equations: `F(x)=+1/C^2` for closed curvature (23; lines 210–216), `F(x)=0` for flat curvature (25; lines 284–290), and `F(x)=-1/C^2` for open curvature (26; lines 329–335), where `F(x)=(3x^2-2x^4)exp(x^2)`. Tables 1–3 then give the corresponding dimensionless turning points and scale factors (lines 236–281, 301–327, 344–382).

The other substantive refinement is local time behavior near the bounce. Equations (27)–(30) show that `x(tau)` has a vertical inflection at `x=1` while `y(tau)` has finite nonzero slope there for allowed parameters (lines 384–415). The resulting sequence is scale factor decrease, increase, decrease, increase: two local minima separated by a small local maximum, i.e. a symmetric double bounce when `C` is constant and an asymmetric one otherwise (lines 417–427). The conclusion expressly says this removes the earlier reported cusp (lines 429–432).

The trapped-null-surface statement is not a further calculation. It is asserted in the introduction—“a closed universe forms in a region of space within a trapped null surface” (lines 57–61)—and rephrased in the conclusion as the moment when `C` begins satisfying the threshold in such a region (lines 442–443). No trapped-surface equation, formation rate, mass, radius, or observable is derived here. Relative to the disclosed entry-52 findings, entry 53 therefore adds the all-curvature turning-point classification, tabulated dimensionless solutions, and double-bounce/cusp analysis; the closed-branch existence threshold and broad cosmological narrative are the same physics family, not an independent empirical line.

## 2. Closure

`k=+1` is not derived or selected from data. The paper first assumes homogeneity and isotropy (lines 63–70), then explicitly begins the relevant branch: “Let us consider a closed relativistic universe, for which k=1” (lines 210–212). Within that assumed branch, `F(x)` has maximum `e` at `x=1` (lines 218–220), so two turning points require `C>e^{-1/2}` (lines 222–226); equality gives one stationary solution and smaller `C` gives no solution (lines 228–232). Equation (31) merely rewrites this as `xy exp(-x^2/2)>e^{-1/2}` (lines 429–438). Thus the threshold is an existence exclusion internal to an assumed closed construction, not a derivation that our universe is closed.

The flat and open branches are unrestricted in positive `C`: Table 2 gives flat-domain `C in (0,infinity)` (lines 325–327), Table 3 gives the same for open curvature (lines 381–382), and the conclusion states both can exist for every positive integration constant (lines 440–440). All three cases remain nonsingular for every allowed `C` because `a_min=C exp(1/2)a_cr>0` (lines 191–204).

## 3. Printed numbers, inputs, and recomputation

The numerical inputs explicitly supplied are Standard-Model spin-state counts `g_b=29` and `g_f=90` (lines 108–111), used in the stated equilibrium formulas for `h_*` and `h_nf` (line 109), together with `alpha=(9/16) kappa (hbar c)^2` (lines 84–94) and `kappa=8 pi G/c^4` as defined earlier (line 31). These produce the printed dimensional scales `T_cr=2.218×10^31 K` (equation 11; lines 130–136) and `a_cr=6.661×10^-35 m` (equation 16; lines 160–164). The numerical values of `G`, `hbar`, `c`, `k_B`, and `zeta(3)`, the unit convention/rounding, and the assumed particle-content validity at `T_cr` are not separately printed; those are unstated numerical/physical inputs. Also noteworthy is that the introductory spin-fluid coefficient is `alpha=kappa(hbar c)^2/32` (line 31), while the Dirac-field dynamics actually calculated uses `alpha=(9/16)kappa(hbar c)^2` (lines 84–94); the reported scales use the latter.

All non-bibliographic numbers printed in the quantitative analysis are as follows.

- Definitions and exact factors: `p=epsilon/3`; `(7/8)` in `h_*`; `(3/4)` in `h_nf`; `g_b=29`, `g_f=90` (lines 108–111); `T_cr=2.218×10^31 K` (lines 130–136); `a_cr=6.661×10^-35 m` with prefactor `27/8` (lines 160–164); the illustrative Figure 1 uses `C=1` (lines 203–208).
- Closed branch: threshold `C>e^-1/2=0.606530660`; equality has `x_min=x_max=y(x_min)=y(x_max)=y_min=1` (lines 218–234, 253–258). Table 1 prints, in column order `(C,x_min,y(x_min),x_max,y(x_max),y_min)`: `(1,0.555209,2.10126,1.18912,1.70538,e^1/2)`; `(10,0.057703,173.590,1.22444,17.2831,10e^1/2)`; `(100,0.005773,17320.9,1.22474,172.852,100e^1/2)` (lines 246–281). Its domain is `[1/sqrt(e),infinity)` (lines 281–282). The printed large-`C` limits are `x_min→1/(sqrt(3)C)`, `x_max→sqrt(3/2)`, `y(x_min)→sqrt(3)C^2`, `y(x_max)→sqrt(2/3)e^(3/4)C`, and the three ratios in line 244 (lines 236–244).
- Flat branch: `x_min=0`, `x_max=sqrt(3/2)` and `y(x_max)=sqrt(2/3)e^(3/4)C` (lines 292–299). Table 2 prints rows `C=1,10,100` with those same exact expressions scaled by `C`, and `y_min=C e^1/2` (lines 301–325). It also prints `x_max≈1.22474`, `y(x_max)≈1.72852C`, and domain `(0,infinity)` (lines 325–327).
- Open branch: Table 3 prints `(C,x_max,y(x_max),y_min)` as `(0.01,2.33420,0.06531,e^1/2)`, `(0.1,1.64821,0.23599,e^1/2)`, `(1,1.25165,1.74866,e^1/2)`, `(10,1.22505,17.2874,10e^1/2)`, and `(100,1.22475,172.853,100e^1/2)` (lines 351–381); its domain is `(0,infinity)` (lines 381–382). Here `x_min=0`, and the large-`C` limits are again `x_max→sqrt(3/2)` and `y(x_max)→sqrt(2/3)e^(3/4)C` (lines 337–349). As rendered in the pinned source, the first two `y_min` cells conflict with equation (21): for `C=0.01` and `0.1` they should be `0.01e^1/2≈0.0164872` and `0.1e^1/2≈0.164872`, not unscaled `e^1/2`. This may be a source-conversion omission, but on the allowed record it is a flagged table inconsistency.

Independent recomputation of the Table 1 `C=10` row: solve `(3x^2-2x^4)e^(x^2)=1/100`. Bisection on `(0,1)` and `(1,sqrt(3/2))` gives `x_min=0.057703067` and `x_max=1.224440815`. Substitution into `y=(10/x)e^(x^2/2)` gives `y(x_min)=173.589768` and `y(x_max)=17.283089`; equation (21) gives `y_min=10sqrt(e)=16.487213`. These round exactly to the printed `0.057703`, `1.22444`, `173.590`, and `17.2831` (lines 267–272). As a cross-check, `sqrt(3/2)=1.224744871` and `sqrt(2/3)e^(3/4)=1.728523275`, matching the flat approximations at line 326.

## 4. Observation-facing content

The Planck sentence contains no calculation in this paper: it says the expansion “predicts” CMB parameters consistent with Planck 2015 “as was shown in SD” (lines 36–39), and the bibliography identifies SD as Desai and Popławski (2016) (lines 492–496). There is no likelihood, fitted CMB parameter, uncertainty, Planck comparison, or reproduced numerical prediction here; attribution belongs to that cited paper.

Nothing else supplies a calibrated observable. The number of bounces is left dependent on particle-production rate (lines 36–39), `C` may change by unspecified quantum pair production (lines 442–444), and the threshold needed for observed present acceleration is neither calculated nor tied to a measured value (lines 451–455). The black-hole/trapped-surface origin is framed as “could,” “may,” and “possibly” and has no predicted mass, abundance, relic, present-day `Omega_k`, bounce count, or data constraint (lines 59–61, 442–455). The tables are dimensionless internal solutions for selected `C`, not observational fits.

## 5. Tier consequence

**CONSISTENCY-ONLY; A(a).** The paper checks the internal existence and turning-point structure of an assumed Einstein–Cartan FLRW construction, including an assumed `k=+1` branch, and corrects/refines earlier bounce dynamics. Its quantitative outputs are theoretical scales and dimensionless examples conditioned on Standard-Model equilibrium inputs and a free integration constant. It neither calibrates those outputs to observations nor derives a qualitative observable unique enough to confront data. The sole explicit CMB-success claim is delegated to Desai and Popławski (2016), so under A(a) it belongs to the cited paper. The trapped-surface and present-acceleration remarks are uncalibrated scenario statements. Entry 53 therefore remains CONSISTENCY-ONLY.

In plain language: this paper does useful bookkeeping inside the Einstein–Cartan bounce model. It keeps the curvature term, shows exactly when the assumed closed solution exists, works out the flat and open cases, and explains why the scale factor makes a smooth double bounce rather than a cusp. But it never establishes that our universe chooses the closed branch, and it does not calculate a measurable CMB, curvature, relic, or bounce-count prediction. Its one appeal to Planck points to another paper. That makes it a stronger internal-consistency analysis, not an observational test.
