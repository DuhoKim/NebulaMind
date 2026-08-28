HOLD_UNCALIBRATED_CUTOFF
RIGID:    YES
DERIVED:  YES
MATCHES:  CONTESTED

## Ruling

Do not promote entry 23 to `CALIBRATED-FALSIFIER`. The paper does derive a rough cutoff near 60 degrees from measured \(\Omega_\Lambda\) in its no-DE, constant-vacuum branch. It does **not** derive the quoted \(\pm3^\circ\) uncertainty for that forward prediction. That error bar is extracted from the already-observed CMB curve in the reverse calculation. The claim therefore remains a directional/rough quantitative postdiction, not a calibrated prediction with a model-propagated tolerance.

## Attack 1 — qualifications

The two stated hedges are not the worst qualifications. I found these additional ones:

- Before using current measurements, the paper says the inflationary inputs are unknown: “As we dont know the values of \(a_i\) or \(\rho(t_i)\) it seems impossible to estimate how large \(\chi_S\) is from current observations or first principles.” The later boundary-condition calculation supplies an indirect estimate conditional on no evolving DE; inflation alone does not fix it.
- The forward result assumes constant vacuum/no evolving DE: “But imagine that DE does not exist” and “If we assume that vacuum energy does not evolve after inflation.” Appendix B explicitly generalizes to evolving DE, adding another contribution to Eq. 34.
- The claimed comparison is incomplete: “this rough estimate does not take into account the foreground (late) ISW and lensing effects,” followed by “This requires further investigation.”
- The CMB-inferred boundary may differ from the local one: it “might be slightly different to the value near us,” and the conclusion says such differences are “impossible to quantify ... without a model for the initial conditions.”
- The conclusion concedes: “More work is needed to account for the late ISW and lensing and to interpret the CMB measurements with a metric that is not homogeneous.”

I found no alternative numerical cutoff elsewhere in the paper. The radiation-free sensitivity check changes \(\chi_S\) from \(3.149\,c/H_0\) to \(3.081\,c/H_0\), not to a separately advertised angle.

## Attack 2 — rigidity

Within the paper's advertised no-DE, constant-vacuum model, \(\Omega_S=\Omega_\Lambda\) is not an independent fit choice. Its boundary condition gives Eq. 19, \(\rho_\Lambda=\rho_S\), and Eq. 22 maps the measured density to \(\chi_S\). The paper reports

> “We find \(\chi_S\) from Eq.22 numerically using \(\Omega_\Lambda=\Omega_S\ ...\simeq0.69\pm0.01\)”

and obtains \(\chi_S=(3.149\pm0.006)c/H_0\). It then uses the last-scattering distance \(\chi_{CMB}\simeq3.145c/H_0\) and states

> “Thus, we would expect to see no correlations ... \(\theta>\theta_S\equiv\chi_S/\chi_{CMB}\simeq60\) degrees for \(\Omega_\Lambda=\Omega_S\simeq0.7\).”

The printed ratio is dimensionally a ratio but cannot literally equal 60 degrees without the angular geometry/convention implicit in the paper; the text does not expose that mapping well enough to independently reproduce 60 degrees from those two nearly equal distances. Still, the direction of inference is plainly \(\Omega_\Lambda\rightarrow\chi_S\rightarrow\theta_S\), and the paper says removing radiation has little effect. Inflationary duration fixes the primordial interpretation of \(\chi_S\), but it is not a free knob in this forward calculation once measured \(\Omega_\Lambda\) and the boundary equation are imposed.

A robust 40-degree cutoff would contradict this stated branch. The author could move to the Appendix-B evolving-DE model, invoke unquantified patch-to-patch boundary differences, or revise the treatment of ISW/lensing and the non-homogeneous metric. Those are genuine broader-model escape routes, but they require abandoning or enlarging the specific branch that yielded 60 degrees. I therefore mark the tested chain `RIGID: YES`, while treating the surrounding framework's evidential force as weaker.

## Attacks 3 and 4 — match and postdiction

The observational feature is real in the limited sense that COBE, WMAP, and Planck temperature maps repeatedly show unusually low large-angle two-point correlation. It is not a cleanly established physical cutoff at \(60\pm3\) degrees. The \(S_{1/2}\) statistic itself integrates above 60 degrees; that boundary was selected after inspecting the early data. Copi et al. argue that the low correlation persists across WMAP and Planck maps and reasonable choices ([MNRAS 451, 2978](https://academic.oup.com/mnras/article/451/3/2978/1192426)). Efstathiou and Ma show the opposing assessment: estimator and sky-cut choices materially affect the frequentist significance, the 60-degree limit was a posteriori, and a Bayesian analysis does not exclude standard \(\Lambda\)CDM ([MNRAS 407, 2530](https://academic.oup.com/mnras/article/407/4/2530/1002085)). Planck's final isotropy analysis reports persistence of large-scale temperature anomalies while emphasizing limitations in anomaly significance and large-scale polarization systematics ([Planck 2018 VII](https://arxiv.org/abs/1906.02552)). Thus `MATCHES: CONTESTED` is the strongest defensible label.

The 2020 claim is unquestionably a postdiction. That does not erase logical falsifiability: a pre-specified repeat measurement or a different observable could contradict the model. But the proposed promotion depends specifically on *calibration*, not merely falsifiability. Using an a-posteriori observed cutoff to manufacture the only quoted angular error bar weakens both evidential weight and the case for the calibrated tier. The mirror error would be to say postdiction alone makes a claim unfalsifiable; I do not. The hold follows from absent forward calibration and an observational target whose numerical boundary was itself selected a posteriori.

## Attack 5 — the error bar

The decisive sentence is:

> “From Fig.3 we roughly estimate \(\theta_S\simeq60\pm3\) deg. to find (using Eq.22) \(\Omega_\Lambda=0.7\pm0.1\).”

This is observation \(\rightarrow\theta_S\rightarrow\Omega_\Lambda\), not propagation of the independently measured \(\Omega_\Lambda=0.69\pm0.01\) through Eqs. 22–23 into an angular uncertainty. No likelihood, fitting rule, confidence level, or derivation of \(\pm3^\circ\) is supplied. The forward chain does propagate \(\Omega_\Lambda\) into \(\chi_S=(3.149\pm0.006)c/H_0\), but the paper then rounds the angular result to about 60 degrees without propagating that uncertainty or uncertainties in \(\chi_{CMB}\), geometry, ISW, lensing, or patch variation. The \(\pm3^\circ\) is therefore an eyeballed observational range, not a calibrated model prediction.

## Attack 6 — reproduction and predicate audit

Run reproduced: **5/5 PASS, exit 0**, pinned-source hash prefix `25cf2122ba7b`.

All five checks have name/detail overreach:

1. The regex does establish the literal word “predicts” near a CMB statement. It does not establish that the statement is quantitatively falsifiable or tier-distinguishing, as its detail claims.
2. The predicate tests only whether `60±3` occurs anywhere. It does not test that the uncertainty belongs to the forward prediction, is derived, or is “not just a round number.” In context it belongs to the reverse, figure-read estimate. This is the fatal mismatch.
3. Two independent string-presence tests do not establish causal direction, that the scale is *set* rather than assumed, or that the anomaly was not used. The body supports the rough forward chain, but the predicate does not test the name's claims.
4. The predicate only finds two known strings. It cannot establish that they are the only qualifications or that they are weaker. The paper contains the stronger qualifications listed above.
5. “Observed” establishes that the anomaly predates this paper, so the short name is substantially supported. The predicate does not test the detail's additional claim that postdiction leaves falsifiability unchanged.

The script is a useful quotation-presence check, but it cannot support promotion as written.
