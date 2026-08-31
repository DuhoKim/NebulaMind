CMB_FALSIFIER_CANDIDATE

# RQ-C codex derivation — causal-horizon CMB scale

## Ruling

The **scale** is predicted independently of the low-\(\ell\) anomaly under the BHU assumptions; it is not obtained by fitting the quadrupole. With Gaztañaga's own background inputs, the present physical radius is \(r_S\simeq5.1\)–\(5.2\) Gpc, the early-time comoving causal radius is \(\chi_*\simeq3r_S\simeq15.4\)–\(15.6\) Gpc, and its stated last-scattering angle is \(\theta_*\simeq60^\circ\). The usual angular half-wavelength mapping gives a characteristic cutoff \(\ell_{\rm cut}\simeq\pi/\theta_*\simeq3\).

This earns only **candidate** status. The inspected BHU papers do not give a primordial cutoff function, boundary eigenmodes, cutoff sharpness, or a predicted suppression amplitude for \(C_\ell\). Consequently Planck can test the location/order of scale, but these sources do not furnish a calibrated likelihood-level rejection threshold.

## 1. Independent derivation of \(R\)

Part I defines the FLRW event horizon

\[
R_*(a)=a\chi_*=a\int_a^\infty {da\over Ha^2}<H_\Lambda^{-1}\equiv r_\Lambda .
\]

It then says that at small \(a\), \(\chi_*\simeq3r_\Lambda\), while at late time \(R_*\to r_\Lambda\), and identifies \(r_\Lambda=r_S\). Its equation (33) fixes

\[
r_S={c\over H_0\sqrt{\Omega_\Lambda}}={2GM\over c^2}
\]

(the source uses \(c=1\)), using \(\Omega_\Lambda\simeq0.7\) and \(H_0\simeq70\ {m km\,s^{-1}\,Mpc^{-1}}\). Numerically,

\[
{299792.458/70\over\sqrt{0.7}}=5119\ {m Mpc}.
\]

The paper's rounded \(1.6\times10^{23}\) km gives \(5185\) Mpc; the harmless difference is rounding. It also quotes \(M\simeq5.5\times10^{22}M_\odot\). Therefore

\[
\chi_*(a\ll1)\simeq3r_S\simeq15.4\text{--}15.6\ {m Gpc}.
\]

Part I itself supplies the projection, \(\theta=\chi_*/\chi_o\simeq60^\circ=\pi/3\) at last scattering. Hence

\[
\ell_{\rm cut}\sim{\pi\over\theta}\simeq3.
\]

Equivalently, choosing the lowest radial half-wave \(k_{\min}=\pi/\chi_*\) gives \(k_{\min}\simeq2.0\times10^{-4}\ {m Mpc}^{-1}\) and \(\ell\sim k\chi_o=\pi/\theta\simeq3\). If instead one calls a full periodic wavelength the fundamental, \(k_{\min}=2\pi/\chi_*\), the label becomes \(\ell\simeq6\). **The sources do not specify boundary conditions that select between these conventions.** Their invariant prediction is therefore an order-few multipole / roughly \(60^\circ\) causal scale, not a uniquely derived integer \(\ell\).

### Was this scale read off the anomaly?

No, in the operational sense fixed by the brief. The inputs in equation (33) are background \(H_0\) and \(\Omega_\Lambda\), not low-\(\ell\) power. More decisively, Fosalba & Gaztañaga compare measured CMB horizons with a BHU \(\theta(\Omega_\Lambda)\) curve and state that the curve has **no free parameter** and was published in Gaztañaga (2020) before their CMB analysis.

There is an important separation between prediction and measurement in that paper. Its map pipeline sets a fiducial disc diameter of \(60^\circ\), scans disc diameters \(40^\circ\)–\(90^\circ\), and estimates horizons of about \(40^\circ\)–\(70^\circ\) from Planck. Those measured patch sizes are data-derived. They are not, however, the origin of the independently published BHU curve against which the measurements are compared. Also, that pipeline imposes \(\ell_{\min}=32\); it is not a direct fit of a primordial low-\(\ell\) cutoff.

Calling this “from first principles” needs qualification: the numerical radius uses empirically measured background parameters and the BHU identifications \(r_\Lambda=r_S\) and \(\chi_*\simeq3r_S\). It is nevertheless **out-of-sample with respect to the low-\(\ell\) deficit**, which is the brief's deciding definition of PREDICTED.

## 2. Planck comparison

The predicted half-wave scale \(\ell\sim3\) lands exactly in the quadrupole–octopole regime, not across the whole commonly discussed \(\ell\lesssim30\) low-power range.

Published Planck 2018 reporting gives a realization-specific quadrupole amplitude of about \(226\ \mu{\rm K}^2\) (often plotted as the quadrupole power/amplitude; it should not be confused silently with every convention for raw \(C_2\)). This is roughly one fifth of the order-\(10^3\ \mu{\rm K}^2\) best-fit-\(\Lambda\)CDM expectation, so the sign and order of multipole agree with suppression at \(\ell\sim2\)–3.

The stronger, convention-clean comparison is Planck's real-space result. Planck 2018 VII finds the only temperature excursion outside its 95% simulation band when the lower angular bound is about \(60^\circ\). For \(S_{1/2}^{TT}=S^{TT}(60^\circ,180^\circ)\), the four component-separated maps give \(1142.4\)–\(1209.2\ \mu{\rm K}^4\); fewer than 0.1% of fiducial simulations are as low in the table's probability convention. After removing the fitted quadrupole, that probability becomes about 96%, showing that the low quadrupole contributes materially; Planck also notes that all modes \(\ell\le5\) participate through cancellations. The look-elsewhere-adjusted/global anomaly is more modest: about 98.8%–99.0% (roughly 1% tail), and Planck stresses both the a-posteriori history and the possibility of a statistical fluctuation.

Fosalba & Gaztañaga independently report that the Planck SMICA angular correlation is consistent with zero beyond about \(65^\circ\), close to the BHU \(60^\circ\) scale, while their all-sky point is \(\theta\simeq65^\circ\) at \(\Omega_\Lambda\simeq0.7\).

Thus Planck is **consistent in scale and direction**, but does not confirm a unique BHU spectral cutoff. The broad low-\(\ell\) deficit extending toward \(\ell\sim20\)–30 is not predicted by the simple \(\ell\sim3\) geometry, and the anomaly's modest global significance is not evidence of a sharp cutoff.

## 3. Falsification statement and ownership of proof

The source-supported candidate test is:

> Holding the independently measured background parameters fixed, BHU places its causal angular boundary near \(60^\circ\), equivalently a characteristic \(\ell\) of order 3 (order 3–6 under the unresolved fundamental-mode convention). Robust normal large-angle correlation and unsuppressed quadrupole/order-few power would contradict the claimed causal-cutoff association.

What cannot yet be asserted from these papers is a numerical threshold such as \(C_2<X\), a complete set of affected \(\ell\)'s, or a predicted likelihood ratio. The model owns the missing proof: it must specify the boundary conditions and primordial \(P(k)\) (or transfer function) that propagate the finite domain into \(C_\ell\). Until then the CMB result is a **scale-level calibrated falsifier candidate**, not a precision power-spectrum prediction.

No tier was changed.

## Receipts

- `../bhu-reading-20260823/sources/sym14091849_clean.txt`: equation (32), small-\(a\) \(\chi_*\simeq3r_\Lambda\), \(r_\Lambda=r_S\), equation (33), \(r_S\), \(M\), and the stated \(\theta\simeq60^\circ\) CMB association.
- `../bhu-reading-20260823/sources/sym14101984_clean.txt`: finite \(R\) implies a perturbation-spectrum cutoff; the paper supplies no cutoff kernel or amplitude.
- `../bhu-reading-20260823/sources/2011.00910v4_fosalba_gaztanaga_clean.txt`: disc-size choices, \(\ell_{\min}=32\), measured horizon sizes, equation (8), \(\theta_\Lambda\), the BHU \(\theta(\Omega_\Lambda)\) comparison, and the explicit no-free-parameter/prior-publication statement.
- `../bhu-reading-20260823/sources/2011.00910v4_fosalba_gaztanaga.pdf`, SHA-256 `0facf2c571586d60134e7bf6b4e6395709ebb103e6c6534482366ad29e446df9`; extracted text SHA-256 `8491601f3e9f95e6f3b9f674eab56db97abdc8907bf66c399549998ddd5d88d9`. Source: arXiv `2011.00910v4`, DOI `10.1093/mnras/stab1193`.
- `../bhu-reading-20260823/sources/1906.02552v2_planck2018_isotropy.pdf`, SHA-256 `0387b7aa3b29af85afd4cf4c0f7192dce1e6114e698abf10ac2d66ee3a20d840`; extracted text SHA-256 `583401aa87ad3ec27b1064264ee151a159be39adccec02a5f2126cf61b0a0263`. Source: arXiv `1906.02552v2`, Planck 2018 results VII, especially section 6.1 and tables 11–13.
- Quadrupole cross-check: Colombo et al., *BeyondPlanck XI*, A&A 675 A11 (2023), section 6.1, explicitly records Planck 2018's reported \(226\ \mu{\rm K}^2\) realization-specific quadrupole amplitude and warns about amplitude conventions: `https://doi.org/10.1051/0004-6361/202244619`.

## Explicit assumptions

1. \(R\) at recombination is the comoving event-horizon radius \(\chi_*\), while today's physical asymptote is \(r_S\); substituting today's \(r_S\) directly as a comoving last-scattering radius would omit the source's factor of about 3.
2. Spatial flatness and the source's background values are used.
3. The quoted \(60^\circ\) is treated as an angular radius/characteristic separation exactly as Part I writes it. Fosalba & Gaztañaga mostly describe measured horizon **diameters**; these labels must not be conflated.
4. \(\ell\simeq\pi/\theta\) is the stated half-wavelength convention, not an equation derived in the BHU papers.
