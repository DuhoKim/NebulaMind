# Independent cosmology-number calculation

All calculations use exactly the constants specified in the request. The executable calculation is in `bhu_video_numbers_codex.py`.

1. **Hubble constant in SI**

   \[
   H_0=67.4\frac{\mathrm{km/s}}{\mathrm{Mpc}}\left(\frac{1000\ \mathrm{m}}{1\ \mathrm{km}}\right)\left(\frac{1\ \mathrm{Mpc}}{3.0856775814913673\times10^{22}\ \mathrm m}\right)
   =2.184285241085502\times10^{-18}\ \mathrm{s^{-1}}.
   \]

2. **Critical density**

   \[
   \rho_c=\frac{3H_0^2}{8\pi G}=8.532855163739318\times10^{-27}\ \mathrm{kg\,m^{-3}}.
   \]

3. **Hubble radius**

   \[
   R_H=\frac{c}{H_0}=1.372496834941828\times10^{26}\ \mathrm m
   =14.507302992297\ \text{billion light years}.
   \]

4. **Mass inside a critical-density sphere of radius \(R_H\)**

   \[
   M=\frac43\pi\rho_cR_H^3=9.240958888601495\times10^{52}\ \mathrm{kg}
   =4.646219500332590\times10^{22}\ M_\odot.
   \]

5. **Independent closed-form mass check**

   \[
   M=\frac{c^3}{2GH_0}=9.240958888601497\times10^{52}\ \mathrm{kg}.
   \]

   Yes, the two evaluations agree. Using \(|M_{\rm volume}-M_{\rm closed}|/|M_{\rm closed}|\), the relative difference is \(2.301454663843575\times10^{-16}\), i.e. floating-point roundoff.

6. **Schwarzschild radius**

   \[
   R_s=\frac{2GM}{c^2}=1.372496834941828\times10^{26}\ \mathrm m
   =14.507302992297\ \text{billion light years}.
   \]

7. **Radius ratio**

   \[
   \frac{R_s}{R_H}=\mathbf{1.000000000000}.
   \]

8. **Hubble-constant sweep**

| \(H_0\) (km/s/Mpc) | \(M=(4/3)\pi\rho_cR_H^3\) (kg) | \(M/M_\odot\) | \(R_s/R_H\) |
|---:|---:|---:|---:|
| 50 | \(1.245681258183482\times10^{53}\) | \(6.263103886448332\times10^{22}\) | 1.000000000000 |
| 73 | \(8.532063412215629\times10^{52}\) | \(4.289797182498858\times10^{22}\) | 1.000000000000 |
| 100 | \(6.228406290917408\times10^{52}\) | \(3.131551943224166\times10^{22}\) | 1.000000000000 |
| 500 | \(1.245681258183481\times10^{52}\) | \(6.263103886448331\times10^{21}\) | 1.000000000000 |

The ratio does not change with \(H_0\). The mass does change: \(M=c^3/(2GH_0)\), so it is inversely proportional to \(H_0\).

9. **Mass at \(H_0=73.0\) km/s/Mpc**

   \[
   M(73.0)=8.532063412215629\times10^{52}\ \mathrm{kg}
   =4.289797182498858\times10^{22}\ M_\odot.
   \]

   \[
   \frac{M(73.0)-M(67.4)}{M(67.4)}\times100=-7.671232876712\%.
   \]

   Thus the mass at 73.0 is **7.671% lower** than at 67.4 (an absolute percentage difference of 7.671%).

10. **Alternative radius and corresponding mass**

   \[
   r_{S,\mathrm{alt}}=\frac{c}{H_0\sqrt{\Omega_\Lambda}}
   =1.653610644508227\times10^{26}\ \mathrm m,
   \]

   \[
   \frac{r_{S,\mathrm{alt}}}{R_H}=\frac{1}{\sqrt{0.6889}}=1.204819277108434,
   \]

   and

   \[
   M_{\mathrm{alt}}=\frac{c^2r_{S,\mathrm{alt}}}{2G}
   =5.597854819677821\times10^{22}\ M_\odot.
   \]

## Algebraic answers

11. Substitute \(\rho_c=3H_0^2/(8\pi G)\) and \(R_H=c/H_0\) into the volume mass:

   \[
   \begin{aligned}
   M&=\frac43\pi\rho_cR_H^3\\
    &=\frac43\pi\left(\frac{3H_0^2}{8\pi G}\right)\left(\frac{c}{H_0}\right)^3\\
    &=\frac{c^3}{2GH_0}.
   \end{aligned}
   \]

12. Substitute that mass into \(R_s=2GM/c^2\):

   \[
   R_s=\frac{2G}{c^2}\left(\frac{c^3}{2GH_0}\right)
   =\frac{c}{H_0}=R_H.
   \]

13. **Conclusion:** Within these definitions—a spatially flat universe at critical density, taking the mass in a sphere whose radius is the Hubble radius—\(R_s=R_H\) is an **algebraic identity**, not a numerical coincidence tied to the measured value of \(H_0\). It does not depend on the value of \(H_0\) at all; changing \(H_0\) changes both radii together and changes the enclosed mass as \(1/H_0\), while their ratio remains exactly one.
