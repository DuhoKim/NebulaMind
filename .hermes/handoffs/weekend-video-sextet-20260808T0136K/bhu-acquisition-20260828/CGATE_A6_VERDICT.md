PROMOTE_REFUTED_ATTACK1_QUALIFIED_CONSEQUENCE
RIGID:        NO
DISTINCTIVE:  NO
FIRES:        UNDETERMINED

## Gate ruling

Attack 1 rules first, and it kills this promotion as framed. I searched the complete pinned entry-25 text for qualifications, mixed causes, time dependence, extra dark-energy content, and changes in the status of the horizon. The decisive qualification is not hidden elsewhere; it is in the proposed quotation itself:

> “The BHU can also be challenged by a measurement a the DE equation of state 𝜔 ≠ − 1. This would indicate that cosmic acceleration is not solely caused by the BHU event horizon 𝑟 𝑆.”

“Not solely caused” is weaker than “the BHU is falsified.” It explicitly leaves the horizon contribution in place and assigns some acceleration to another cause. Thus the sentence is a calibrated test of the paper's **sole-cause acceleration claim**, but not a rigid falsifier of the BHU model family. Promoting entry 25 as a live family falsifier would silently strengthen the author's stated consequence.

I found no later withdrawal of this sentence (it is near the end of Section 4), and no statement that a time-varying Λ is part of the proposed BHU mechanism. But the mixed-cause escape is already explicit. The body also says the exterior “does not need to be exactly empty” and could be “a perturbation inside a lower density FLRW or a dS metric,” and discusses nested FLRW manifolds. Those exterior possibilities are causally separated and do not by themselves generate an observable interior effective w, so they are supporting context rather than the kill. The kill is the author's limited consequence.

## Rigidity join

The narrow horizon term is constant in the construction. Appendix D writes

> “H tends to a constant (H² → 1/r_S²) because ρ → 0”

and then, as R approaches r_S,

> “all that remains is the SBH mass: 2GM = r_S.”

It further says:

> “A physical (or Schwarzschild) observer outside only sees r_S because r < r_S is causally disconnected.”

The intermediate M-dot ≠ 0 is therefore the finite-region Misner–Sharp mass, 2GM = R³H², relaxing asymptotically; the text does not make the exterior Schwarzschild radius time-dependent. R(τ) → r_S likewise describes approach to a fixed asymptote, not evolution of r_S. For that isolated effective-Λ term, ρ_Λ = Λ/(8πG) is constant and the separately conserved-fluid equation gives w = −1.

But that does **not** establish the requested stronger predicate, “w = −1 forced with no auxiliary.” The paper's own “not solely caused” consequence admits an additional acceleration source if w differs. A measured effective w concerns the total inferred acceleration sector; a constant r_S contribution plus another component can have w_eff ≠ −1 while retaining the BHU horizon. Therefore RIGID is NO at the family/observable level even though r_S itself is fixed.

## Symbol and distinctiveness

The symbol is read correctly. Elsewhere the paper defines components by “p = ωρ,” and the challenged sentence explicitly calls ω the “DE equation of state.” The capture's “a the” is evidently a grammatical typo (probably “of the” or “at the”), not a symbol ambiguity. I found no missing equation needed to identify ω, and the quotation order in the pinned reconstruction is coherent.

The test is not distinctive. A significant w(z) ≠ −1 rejects a pure cosmological-constant acceleration sector in both the sole-cause BHU background and ΛCDM. It does not select between them. This does not erase falsifiability of the narrower sole-cause claim; it only makes DISTINCTIVE NO.

## DESI testimony and arithmetic

The pinned third-party paper's Table 1 gives, for DR2+BBN+PP, w0 = −0.916 +0.049/−0.044, and for DR2+BBN+OHD+PP, w0 = −0.922 ± 0.047. Simple one-sided standardized offsets are 0.084/0.049 = 1.71 and 0.078/0.047 = 1.66, respectively. Calling these “approximately 1.8σ” follows that paper's prose and is tolerable rounding, but 1.8 is not independently reproduced exactly from the displayed marginalized numbers. Its DR1 statements of about 1σ and 0.5σ also match its prose. The script labels this source correctly as third-party testimony.

The primary DESI Collaboration DR2 key paper is reachable: [DESI DR2 Results II, arXiv:2503.14738](https://arxiv.org/abs/2503.14738), published as Phys. Rev. D 112, 083515 (2025). It reports that w0waCDM is preferred over ΛCDM at 3.1σ for DESI BAO+CMB and at 2.8–4.2σ after adding supernovae, depending on the supernova sample. It also says the results remain well described by flat ΛCDM and concludes that ΛCDM is “being challenged” unless an unknown systematic is present. The supporting [DESI extended-dark-energy analysis](https://arxiv.org/abs/2503.14743) finds stable trends but says alternatives without phantom crossing cannot yet be ruled out.

Those collaboration results overturn the script's suggestion that the best reachable evidence is only the pinned 1.8σ fit, but they do not yield a clean FIRES = YES. The BHU paper supplies no statistical rejection rule; the script invents 3σ, while DESI's preference depends materially on dataset/model choice and the author's own consequence is only “not solely caused.” FIRES is therefore UNDETERMINED on reachable evidence, not NO.

## Reproduction and predicate audit

`python3 a6_entry25_falsifier.py` reproduced 5/5 and exit 0 with both advertised 12-character hashes. All five check names claim more than their predicates test:

1. Check 1 tests only that a two-sentence regex match exists. It does not test that the observable is DE w, that the threshold is −1, or that the consequence falsifies BHU; indeed the consequence is qualified.
2. Check 2 combines a numerical identity using an arbitrary r_S = 2.7 with a weak text search (`"1 𝑟 𝑆" in T`). It does not locate the Friedmann equation reliably and does not test the claimed absence of a separate DE parameter.
3. Check 3 tests only that “reduces its value” and “all that remains is the SBH mass” occur somewhere. It does not test that both refer to the same M, that the varying M is specifically interior, that r_S is constant, or that no auxiliary exists. The computed `outside` value is printed but is not even included in the predicate.
4. Check 4 sets rho-dot to zero by construction and evaluates a tautology. It does not obtain constant Λ from the paper or test separate conservation, interactions, effective w, or auxiliary components.
5. Check 5 hard-codes `maxdev = 1.8` and tests only `1.8 < 3.0`. It parses no constraint from the source, gives no source for a 3σ firing threshold, and cannot establish either “LIVE” or “does NOT currently fire.” Current primary DESI results also make that categorical name source-dependent.

Accordingly, the script's successful self-checks validate its hard-coded assertions, not the promotion.
