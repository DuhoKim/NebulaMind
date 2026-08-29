AUDIT_REFUTED_MISSED_EQ5_1_AND_TIER

# B17 adversarial verdict

## Attack 1 — equation (4.14)

Claim 1 is confirmed. Equation (4.3) is not a model result: it is the Planck+WMAP observational scalar spectrum,

\[
\frac{k^3}{2\pi^2}P_\zeta(k)
=(2.196\pm0.059)\times10^{-9}
\left(\frac{k}{0.05\,\mathrm{Mpc}^{-1}}\right)^{-0.0397\pm0.0073}.
\]

Equation (4.13) is the model's thermal-atmosphere spectrum. In its long-wavelength limit its amplitude is

\[
8.66\times10^{-5}\left(\frac{T_b}{M_5}\right)^6,
\]

up to the displayed scale-dependent correction. The paper then explicitly says that comparing (4.13) with the observed (4.3) “gives the experimental constraint”

\[
T_b/M_5=0.17139\pm0.00077.
\]

Thus (4.14) is an inferred/fitted parameter ratio obtained by normalizing the model to the observed scalar amplitude. It is not a parameter-free forecast subsequently compared with data. The model does genuinely derive the sixth-power dependence and, in the simple limit, exact scale invariance; it does not independently derive the value 0.17139.

## Attack 2 — missed calibrated content

B17 misses important numerical constraints later in the paper.

Most directly, the Conclusions use the observational normal-branch DGP bound \(r_c\gtrsim3H_0^{-1}\), together with (4.15), to derive

\[
H\lesssim M_5\lesssim\left(\frac{H_0M_4^2}{6}\right)^{1/3}\sim9\,\mathrm{MeV}
\tag{5.1}
\]

and then

\[
T\lesssim3\times10^4
\left(\frac{g_*}{100}\right)^{-1/4}\mathrm{TeV}
\ll T_{\rm GUT}\sim10^{12}\,\mathrm{TeV}.
\tag{5.2}
\]

These are not clean, novel parameter-free predictions: (5.1) imports an observational DGP constraint, and (5.2) is a conditional upper bound used to argue that the GUT transition and monopole production never occur. But they directly contradict B17's assertion that the paper does not tie (4.15) or \(M_5\) to anything independently constrained. They also show that the search described in the script was incomplete.

Other testable/numerical content omitted from the audit includes:

- the empirical curvature input \(-\Omega_k\lesssim0.01\) and the parameter regions in Figure 2;
- the conditional scaling \(-\Omega_k\sim(M_5r_h)^{-2}\sim M_5/M_*\);
- the directional correlation that detectable curvature should generically accompany large-scale anisotropy from bulk-black-hole angular momentum;
- the Jeans scale \(k_J\simeq0.2T_b(T_b/M_5)^{3/2}\sim10^{-2}T_b\), though the authors immediately weaken its consequence by noting that growth may be slower than a Hubble time;
- prospective gravitational-wave, non-Gaussianity, and BBN/light-element signatures, all explicitly left for future work.

None of those supplies a clean surviving calibrated forecast: most contain free parameters, imported empirical bounds, qualitative language, or deferred dynamics. The audit is nevertheless wrong to say it found the only relevant bare inequality or that no other numerical bound exists.

## Attack 3 — confrontability of equation (4.15)

The claim that (4.15) “cannot be confronted with anything” is refuted by the paper itself. Section 5 explicitly combines it with the independently observationally constrained DGP crossover scale to obtain (5.1). The definitions in equation (1.2),

\[
M_5=(32\pi G_b)^{-1/3},\qquad r_c=G_b/G_N,
\]

relate \(M_5\) to the bulk gravitational coupling and crossover scale. It is therefore a model parameter rather than a directly observed particle mass, but it is not isolated from observation.

I did not independently verify current short-range-gravity or collider bounds from the sole pinned source, and the brief supplied no external experimental sources for them. I therefore cannot say from the pinned corpus whether present non-cosmological bounds independently exclude or measure the paper's \(M_5\) interval. What is verifiable is narrower and decisive: B17's source-level absence statement is false because the source itself quotes a cosmological \(r_c\) constraint and propagates it into \(M_5\lesssim9\,\mathrm{MeV}\).

## Attack 4 — tier and standing

Claims 2 and 3 are substantially confirmed. The simple Section 4 model predicts no tilt, while (4.3) measures a roughly 4% red tilt. The authors expressly state that this model is already ruled out at greater than \(5\sigma\). Their proposed repair is “easy to imagine,” its desired size is the observed approximately 4%, and the necessary gravitational-backreaction/Jeans calculation is deferred. No corrected spectral index, uncertainty, or threshold is derived.

Claim 4 is not confirmed. The corpus already distinguishes the nature of a claim from its standing: elsewhere it uses forms such as `CALIBRATED-FALSIFIER / FIRED` and `CALIBRATED-FALSIFIER / LIVE`. The simple thermal-free Section 4 model has a sharp prediction, \(n_s=1\), and the authors say that observation fired it. On that schema, `CALIBRATED-FALSIFIER / FIRED` is a better description of that model component than `QUALITATIVE-DIRECTIONAL`.

What survives after the firing is different: a promissory correction mechanism and qualitative directions, properly described as `PROSPECT` or `QUALITATIVE-DIRECTIONAL`. One paper therefore contains at least two claim-level objects with different statuses. If the bibliography insists on one paper-level label, it will necessarily erase either the fired calibrated prediction or the weaker surviving proposal. I recommend retaining the current file unchanged, as instructed, but referring the schema/tier decision to the human: either record the Section 4 claim as calibrated/fired with a separate surviving prospect, or explicitly state that the paper-level tier describes only surviving content.

## Attack 5 — predicate audit

The script ran successfully, reporting 6/6 and exit 0. Several checks claim more than their predicates establish:

- Check 1 tests only the presence of the two decimal strings. It does not establish four significant figures as a falsifier shape or distinguish fit from prediction.
- Check 2 tests only the presence of the authors' phrase “experimental constraint.” Its name says the value is obtained by comparing equations, while the predicate does not check either equation or the comparison. Reading confirms the name, but the predicate does not.
- Check 3 checks two phrases about rejection and scale invariance. It does not independently validate the observational significance or the script detail's “8 sigma, 9 with BAO.”
- Check 4 checks only the “easy to imagine” phrase. It does not test that 4% was taken from measurement rather than independently motivated; context supports that inference, but the predicate does not.
- Check 5 accurately checks the deferral phrase, though its comparison with other entries is untested commentary.
- Check 6 is the decisive overclaim. It tests only that the text contains the (4.15) expression. It does not test whether \(T_b\) or \(M_5\) is independently constrained, whether the inequality “closes on itself,” or whether other inequalities exist. Equations (5.1) and (5.2) affirmatively falsify its name/detail.
- The predictive-verb counts are not an absence test. They neither isolate author predictions from literature discussion nor cover equations, figures, conclusions, or imported observational bounds.

## Bottom line

Equation (4.14) is indeed a fitted normalization, the exact-scale-invariant simple model was genuinely tested and rejected, and the suggested 4% repair remains uncomputed. The audit as a whole is refuted because it overlooks the paper's explicit \(M_5\lesssim9\,\mathrm{MeV}\) and thermal bounds, falsely declares (4.15) observationally closed, and dismisses a tier/standing representation that the corpus already uses. I could not verify present laboratory or collider constraints on \(M_5\) from the pinned source alone.
