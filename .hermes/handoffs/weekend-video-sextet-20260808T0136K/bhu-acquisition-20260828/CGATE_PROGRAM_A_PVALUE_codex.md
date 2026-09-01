C2_REFUTED

C2 FAILS. The numerical experiment shows that one particular Fourier-space cutoff suppresses the chosen full-sky statistic, but it does not establish that the source paper’s real-space causal model predicts \(S_{1/2}=6897\), nor does it validly compare that number with the cut-sky observed value \(1150\).

1. ISW and lensing

C2 is not a fair test of a primordial-only assertion if the paper explicitly excludes late-time ISW and lensing from that assertion. These effects can generate correlations beyond the primordial causal scale.

The requested sign is: if ISW adds positive large-angle correlation coherently with the remaining signal, it raises \(S_{1/2}\) and widens the \(6897-1150\) gap. It cannot close that gap merely by “adding correlations.” However, because
\[
S_{1/2}=\int(C_{\rm prim}+C_{\rm ISW})^2\,d\mu,
\]
the cross term can be negative; “ISW adds correlations” alone does not mathematically guarantee that \(S_{1/2}\) increases. Lensing is generally negligible for this large-angle statistic. Without separately computing primordial, ISW, and cross contributions, C2’s inference about the completed model is unsupported.

2. \(k_S\) convention

Both tested conventions overshoot \(1150\):

- \(2\pi/\chi_S\): \(6897/1150=6.00\), with suppression \(34924/6897=5.06\).
- \(\pi/\chi_S\): \(14000/1150=12.17\), with suppression only \(34924/14000=2.49\).

Thus the narrow statement “these two implementations remain above 1150” survives either convention. But the factor-of-two ambiguity changes the residual statistic by a factor \(14000/6897=2.03\), so it undermines any claim that \(6897\) is a definite prediction.

\(2\pi/\chi_S\) is defensible if \(\chi_S\) is treated as a wavelength; \(\pi/\chi_S\) is defensible if it represents a maximum half-wavelength or separation. Neither is uniquely implied without deriving the Fourier mapping from the paper’s boundary condition.

3. Cut sky versus full sky

The comparison is not like-for-like. The observed \(1150\) is produced by a masked-sky estimator, whereas \(6897\) is an ensemble statistic from full-sky \(\widehat C_\ell\) draws.

There is no universal sign by which a mask moves \(S_{1/2}\): it depends on the estimator, reconstruction, mask, mode coupling, and the particular sky. In the observed CMB, masking can preferentially remove regions contributing substantial large-angle correlation, making the cut-sky statistic smaller than a corresponding full-sky reconstruction. If so, comparing full-sky \(6897\) directly with cut-sky \(1150\) exaggerates the model’s overshoot.

This could overturn the claimed factor-six discrepancy. It would not erase the demonstrated suppression relative to the same full-sky LCDM calculation, but it is fatal to the stated observed-versus-model comparison unless the identical mask and estimator are applied to every simulation.

4. Fourier cutoff versus causal boundary

A hard condition \(P(k)=0\) below \(k_S\) is not equivalent to a real-space condition \(C(\theta)=0\) above \(60^\circ\). A spectral step is nonlocal in real space and produces ringing and long-range correlation tails. It therefore does not enforce compact support in the correlation function.

Consequently, the nonzero \(6897\) may be guaranteed largely by the chosen implementation. It establishes that a hard infrared cutoff does not reproduce a vanishing angular correlation—not that the source paper’s correctly formulated causal-boundary model cannot do so. This is the central refutation of C2.

There is also a conceptual mismatch: \(S_{1/2}=0\) requires \(C(\theta)=0\) almost everywhere over \(60^\circ\)–\(180^\circ\), an infinite set of angular constraints. Adjusting one cutoff scale in an otherwise standard spectrum cannot generally satisfy all those constraints.

5. LCDM transfer functions

Using unchanged LCDM transfer functions assumes standard superhorizon evolution, recombination, projection, and late-time source terms. If the proposed causal horizon changes only the primordial spectrum, that is appropriate. If it changes causal boundary conditions or perturbation evolution, it smuggles standard large-scale correlations back into the calculation.

Therefore the result tests “LCDM transfer physics plus an infrared spectral window,” not necessarily the causal model claimed by the paper. C2 needs evidence that the paper itself prescribes exactly this restricted modification.

6. Other fatal issues

The quoted tail probabilities do not rescue C2. They answer how often a full-sky realization of each implementation yields \(S_{1/2}\le1150\), but \(1150\) was obtained with a different estimator. The reported \(3.3\%\) versus \(0.1\%\) therefore is not calibrated to the observation.

Calling the hard cut “the most favourable implementation” is also unjustified. The supplied smooth windows happen to give \(6113\)–\(10095\), but that small family does not span legitimate causal kernels or spectra engineered from a real-space boundary condition.

Finally, “partial suppression” is defensible only as an empirical description of this proxy: \(6897\) is about \(19.8\%\) of the LCDM value. The stronger conclusion—“the causal cut delivers partial rather than vanishing correlation”—does not follow.

Minimum repairs

- Recast the conclusion as applying only to the specified hard-\(k\) proxy with standard LCDM transfer functions.
- Apply the actual mask and identical cut-sky estimator to every simulated realization.
- Separate primordial, ISW, lensing, and cross-term contributions.
- Derive \(k_S\) and its \(2\pi\) or \(\pi\) convention from the source model.
- Implement the causal condition in real space, or prove that the proposed spectral kernel is mathematically equivalent to it.
- Replace “the paper’s model leaves 6897” with “this particular Fourier-cut implementation has full-sky ensemble value 6897.”
