AUDIT_HOLDS_PROSPECT

## 1. The torsion density number

The number is derived within the paper's adopted ECKS/Weyssenhoff-fluid closure, although one arithmetic input is only implicit. For unpolarized fermions the paper sets

\[
s^2=\frac18(\hbar c n)^2
\]

(lines 90–93), and defines the negative effective spin energy density by \(\epsilon_S=-\kappa s^2/4\) (lines 98–100). With \(\Omega_S=\epsilon_{S0}/\epsilon_c\), \(\epsilon_c=3H_0^2/(\kappa c^2)\) (lines 119 and 126–128), this gives

\[
\Omega_S=-\frac{\kappa^2c^2(\hbar c n)^2}{96H_0^2},\qquad \kappa=\frac{8\pi G}{c^4}.
\]

The observational inputs are \(H_0^{-1}=4.4\times10^{17}\,\mathrm{s}\) (line 141) and a relic-neutrino density \(5.6\times10^7\,\mathrm{m}^{-3}\) “for each type (out of 6)” (line 143). The printed result requires the unspoken summation \(n=6(5.6\times10^7)=3.36\times10^8\,\mathrm{m}^{-3}\). Using \(G=6.67430\times10^{-11}\), \(c=2.99792458\times10^8\), and \(\hbar=1.054571817\times10^{-34}\) in SI gives \(\kappa=2.07665\times10^{-43}\), \(s^2=1.41053\times10^{-35}\), \(\epsilon_{S0}=-7.32293\times10^{-79}\,\mathrm{J,m^{-3}}\), \(\epsilon_c=8.30255\times10^{-10}\,\mathrm{J,m^{-3}}\), and

\[
\Omega_S=-8.8201\times10^{-70},
\]

consistent with the reported \(-8.6\times10^{-70}\) (lines 143–146), given rounded inputs/constants. If the density were mistakenly used for only one type, the answer would instead be \(-2.45\times10^{-71}\), smaller by 36 because the result is quadratic in \(n\).

No erratum for this PLB 694 paper (or PLB 701, 672) is pinned beside the source. The only erratum-named files found there concern PLB 690, so they were not used. Thus no pinned relevant erratum changes this audit.

This number is placed beyond observability as a present-day density fraction: its magnitude is about 67 orders below a \(\sim10^{-3}\) CMB-scale precision on total density. The paper itself calls it “extremely small” (lines 137–147) and later says it becomes negligible (line 192). A calculated number that no stated instrument could approach does not earn CALIBRATED-FALSIFIER.

## 2. Flatness, horizon, and closure

This is not the entry-11 \(\Omega_{\min}-1=4c\tau/a_i\) construction. Here the paper inserts present-day \(\Omega\), \(\Omega_R\), and \(\Omega_S\) into an early-time Friedmann equation (lines 126–135), derives a bounce at \(\hat a_m=\sqrt{-\Omega_S/\Omega_R}=3.1\times10^{-33}\) (lines 149–153), and finds a local minimum

\[
\Omega(\sqrt2\hat a_m)-1=-\frac{4\Omega_S(\Omega-1)}{\Omega_R^2}=8.9\times10^{-64}
\]

(lines 163–167). It then derives a maximum antipodal recession speed \(1.1\times10^{32}c\) and \(N\sim10^{96}\) Hubble volumes (lines 175–191). These are background-model calculations, not a propagation to a predicted present-day \(\Omega_k\): present-day \(\Omega-1\) is already an input to them.

Closedness is assumed. The FLRW setup explicitly begins “A closed” universe and writes \(k=1\) (line 77). The WMAP statement \(\Omega=1.002\) (line 140) is therefore data selection/initialization plus a consistency check for that assumption, not an out-of-sample prediction. It also supplies \(a_0\) through the closed-universe identity (lines 119, 140–142). Consequently neither positive curvature nor its magnitude earns a directional prediction under A(a).

## 3. The PROSPECT route

The black-hole-origin route is stated at lines 243–246: a universe born from a rotating black hole “should inherit its preferred direction”; that direction “should introduce small corrections to the FLRW metric, containing the Kerr radius”; and those corrections “could then couple to other fields, allowing to verify whether our Universe was born in a black hole.” The paper adds a parent-hole Kerr-radius example, \(a<26\,\mathrm{km}\), and compares it with an unrelated Lorentz-violation length scale of \(820\,\mathrm{m}\) (lines 247–249).

It does not derive the corrected metric, propagate a parent Kerr scale into a present observable, name a specific field/correlation to measure, calculate an amplitude or angular/energy scale, or give an instrumental sensitivity. The preferred-direction sign is conditional on the assumed rotating-parent scenario and is not a derived signed shift in an observable. Hence it does not earn QUALITATIVE-DIRECTIONAL. It nevertheless names a recognizable verification route—preferred-direction FLRW corrections coupling to other fields—so PROSPECT (“route without target”) is more accurate than CONSISTENCY-ONLY.

The paper also names generic torsion experiments: particle quantum effects, torsion-induced spin-spin interactions, Standard-Model anomalies, and, conditional on coupling to rotational angular momentum, gyroscope precession (lines 197–204). These too have no ECKS signal amplitude or threshold here; indeed algebraic torsion vanishes in vacuum and Solar-System effects are described as negligible (lines 200–203).

## 4. Other observation-facing content

No additional reachable falsifier is derived. The negative sign of \(\Omega_S\) follows from the spin-fluid term (lines 98–100, 137), but its present amplitude is unreachable. The bounce radius \(a_m=9\times10^{-6}\,\mathrm{m}\) (lines 149–153), duration \(5.3\times10^{-46}\,\mathrm{s}\) (lines 168–171), \(v_a=1.1\times10^{32}c\) (lines 179–181), and \(N\sim10^{96}\) (lines 186–191) are internal early-universe quantities, not tied to an experimental channel. Moreover, the inferred bounce energy density \(1.1\times10^{116}\,\mathrm{J,m^{-3}}\) exceeds the Planck density by a few orders according to the paper itself (lines 213–215), so it is not an accessible bound and flags extrapolation of the classical treatment.

Claims of particle production, isotropization, spin alignment, entropy production, and inherited rotation are posed as possible mechanisms rather than calculated observables (lines 213–228 and 243–249). There is no perturbation action, spectrum, relic abundance, transfer function, forecast, or detector-level bound in the paper.

## 5. Tier consequence

**PROSPECT holds.** The background torsion number is genuinely calculable after exposing the implicit six-species sum, but it is deliberately located far beyond density-parameter sensitivity and therefore cannot calibrate a falsifier. Flatness and horizon results are conditional background consequences of a closed \(k=1\) model normalized with the observed \(\Omega=1.002\), not present-curvature predictions. The inherited-direction proposal identifies a possible empirical route but supplies neither a derived observable nor its number; the lane may own the missing threshold, but here the theory-side amplitude/mapping is also missing. That prevents QUALITATIVE-DIRECTIONAL and CALIBRATED-FALSIFIER, while the explicit route is enough to remain above CONSISTENCY-ONLY.

In plain language: the paper does real arithmetic, and its tiny torsion fraction checks out once all six neutrino types are counted. But that number is fantastically too small to measure today, while the impressive early-bounce numbers depend on choosing a closed universe and feeding current cosmological measurements into the model. Its best experimental idea is that a rotating parent black hole might leave a preferred direction that affects other fields, but the paper never calculates what an instrument should see. That makes it a legitimate prospect for future test development, not an existing qualitative or calibrated falsifier.
