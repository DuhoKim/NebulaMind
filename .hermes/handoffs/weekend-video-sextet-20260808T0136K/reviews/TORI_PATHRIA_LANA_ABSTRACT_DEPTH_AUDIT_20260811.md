# Independent Pathria/Lana abstract-depth audit

**Date:** 2026-08-11  
**Scope:** `LANA_BHU_PREDICTION_DERIVATION_20260811.md` and `KUN_BHU_UNIQUENESS_FINDING_GATE_20260811.md` were read first and only to inventory the claims and verification marks. Every substantive verdict below is my own comparison with publisher metadata, the accessible publisher abstract, or primary full papers. Kun's conclusions are not used as evidence.

## Bottom line

1. **Pathria metadata is confirmed:** R. K. Pathria, “The Universe as a Black Hole,” *Nature* **240**, 298–299 (1972), published 1 December 1972, DOI [`10.1038/240298a0`](https://doi.org/10.1038/240298a0). [Nature record](https://www.nature.com/articles/240298a0); [Crossref record](https://api.crossref.org/works/10.1038/240298a0).
2. **There is a human-visible Pathria verification warning, but not the canonical literal token.** Lana line 83 says **`[VERIFY at full text before quoting further.]`**; it does not contain the exact standalone **`[VERIFY]`** token that Lana says is her gate. Thus “is a verification warning present?” = **yes**; “is the exact `[VERIFY]` marker attached?” = **no**.
3. **Lana’s technical Pathria synopsis exceeds the accessible Nature abstract.** The dust model, cosmological-constant range, Schwarzschild matching, and equality at maximum expansion are supplied by a 2014 secondary note, not the Nature abstract. The note supports those technical details but is not Pathria’s primary full text.
4. **The strongest Pathria judgments are unsupported or overstated:** “predicts no new observable,” “forbids no observation,” and “no dynamics” cannot be established from the accessible abstract/commentary. The Nature abstract itself asserts a closed universe inside a black hole that “cannot expand without limit,” so “forbids nothing” is too strong.
5. **The abstract-only boundary materially failed for the arXiv papers.** Several negative or exhaustive statements required full-text inspection. The full PDFs support some narrowed conclusions, but require these corrections:
   - arXiv:1910.10819 contains functional equations and empirical candidate axes/data scales, although it still has **no model-predicted observable amplitude, lower bound, explicit redshift response, or predicted sky direction**.
   - arXiv:1410.3881 has no preferred axis and no spectral-index/tensor forecast, but it explicitly discusses **anisotropy** and gives many numerical background quantities.
   - arXiv:1007.0587 derives \(\Omega_S\) as a present-day torsion-density parameter; it does **not** define an observational sensitivity or justify “sixty orders below observability.” Its full text also proposes a small inherited preferred-direction correction as a possible verification route.
   - arXiv:2509.11468 is correctly classified as a torsion-collapse/bounce paper; its full text has no preferred-axis observable.
   - The 2025 *Nuclear Physics B* paper does discuss PBHs and GW echoes, but Lana omits its CMB, LSS/void, holographic-simulation, and vacuum-energy channels. “Different instruments entirely” is therefore too categorical.
6. **The literature supports non-uniqueness at the mechanism level, not Lana’s exhaustive closure.** One torsion paper expressly says its early-universe dynamics work even without black-hole origin, and the rotating-axis paper derives its effects from generic rotating-frame terms. But “all such observables are generic to any rotating cosmology,” “the branches disagree,” and “no mature model exists” remain broader than the audited sample proves.

## 1. Local claim and marker inventory

Lana states at lines 10–17 that only abstracts/publisher pages were read and that abstract-only items are marked `[VERIFY]`. The substantive marks are:

| Lana line(s) | Mark as written | Item |
|---|---|---|
| 15, 84 | `[VERIFY]` | I. J. Good source/content |
| 83 | `[VERIFY at full text before quoting further.]` | Pathria full text |
| 107 | `[VERIFY]` | Whether arXiv:1410.3881 derives a quantitative signature |
| 132 | `[VERIFY which datasets the full text cites]` | arXiv:1910.10819 data set |
| 135 | `[VERIFY]` | Smolin 1992 provenance |
| 145 | `[VERIFY]` | J0952−0607 current mass/uncertainty |
| 158 | `[VERIFY exact rebuttal set]` | Shamir rebuttal list |
| 174 | `[VERIFY]` | Missed baby-universe branch details |
| 200 | `[VERIFY]` | Peer-reviewed status of arXiv:1910.10819 |

Lines 11–12 and 274 are procedural mentions, and line 43 is a changelog mention. The Kun file contains no literal `[VERIFY]` token. The present audit resolves the Pathria, 1410.3881, 1910.10819-data, missed-branch, and arXiv-paper depth questions; the Good, Smolin, pulsar, and Shamir items are outside this requested paper-depth audit and remain marked.

## 2. Pathria: metadata, source boundary, and overreach

### 2.1 What the accessible primary record supports

The publisher metadata gives the author, title, journal, volume, pages, date, and DOI above. The complete accessible Nature abstract says:

> “It is shown that a closed universe with uniform density is not only inside a black hole but is permitted to oscillate within it, provided the radius of the universe exceeds the Schwarzschild radius. The universe as a black hole cannot therefore expand without limit.”

— Pathria, *Nature* **240**, 298–299, [DOI 10.1038/240298a0](https://doi.org/10.1038/240298a0), abstract/p. 298 record.

That supports: closed/uniform-density universe, black-hole identification, oscillation, a radius condition, and bounded expansion. It does **not**, in the visible abstract, state “pressureless,” the allowed \(\Lambda\) range, Schwarzschild exterior matching, or the event horizon’s identification with maximum expansion.

### 2.2 What the accessible secondary commentary adds

Khakshournia’s later note reports:

> “Pathria has shown that for the certain values of the cosmological constant, a pressureless closed Friedmann-Robertson-Walker universe can be the interior of a Schwarzschild black hole.”

and identifies the event horizon with “the radius of the universe at the point of its maximum expansion.” It further finds that “the matching is not smooth” and the null shell admits “a surface pressure.”

— S. Khakshournia, “A note on Pathria’s model of the universe as a black hole,” [arXiv:1412.0105 PDF](https://arxiv.org/pdf/1412.0105), p. 1, abstract; [arXiv record](https://arxiv.org/abs/1412.0105).

On p. 1 it also attributes to Pathria \(0\leq\Lambda\leq\Lambda_c\), \(R_{\max}\equiv R_s\), and \(R(t)\leq R_s\). These points support Lana’s technical synopsis **only as a secondary report**. They do not substitute for checking Pathria’s paywalled full text.

### 2.3 Claim-by-claim Pathria verdict

| Lana claim | Verdict |
|---|---|
| Closed, pressureless FRW interior of Schwarzschild for suitable \(\Lambda\); horizon equals radius at maximum expansion | **Secondary-supported, not primary-full-text verified.** It exceeds the Nature abstract but closely follows Khakshournia p. 1. Keep the custom verification gate. |
| “Mathematical identification/consistency observation about parameters we already measure” | **Interpretive and only partly supported.** The radius identity is documented; “parameters we already measure” and the reduction to a mere consistency observation are Lana’s characterization. |
| “No new observable, no anisotropy, no axis, no signature” | **Unsupported from accessible Pathria evidence.** An absence claim requires the full paper. Neither the abstract nor the commentary performs an observable/signature inventory. |
| “Pathria forbids no observation,” “retrodicts and forbids nothing” | **Overstated/contradicted by the abstract’s own content.** Closed geometry and inability to expand without limit are model claims that exclude alternatives. The secondary note also derives a non-smooth junction with surface pressure. |
| “No birth mechanism, no dynamics” | **Mixed.** No birth mechanism is visible in the accessible record, but “no dynamics” is false as written: the abstract discusses oscillation and bounded expansion, and the commentary discusses expansion to \(R_{\max}\). |

**Custody ruling:** Pathria may be described from the abstract as an early closed-universe/black-hole identification with oscillatory, bounded expansion. The dust/\(\Lambda\)/maximum-expansion construction must be attributed to the later commentary or kept behind the full-text gate. The no-observable/forbids-nothing/no-dynamics claims must not be frozen.

## 3. Full-PDF audit of Lana’s arXiv claims

### 3.1 arXiv:1007.0587 — \(\Omega_S\), black-hole interpretation, and observability

Primary source: N. J. Popławski, “Cosmology with torsion: An alternative to cosmic inflation,” *Physics Letters B* **694**, 181–185 (2010), [arXiv:1007.0587 PDF](https://arxiv.org/pdf/1007.0587), [DOI 10.1016/j.physletb.2010.09.056](https://doi.org/10.1016/j.physletb.2010.09.056).

- **What \(\Omega_S\) is:** the paper defines it as the present-day spin-torsion density divided by critical density and derives
  > “\(\Omega_S=-8.6\times10^{-70}\)”
  from a relic-neutrino-density estimate (p. 4, eqs. 20–23). It is therefore better called a **derived present-day torsion-density contribution**, not merely a free “mechanism parameter.”
- **Observability:** no detection threshold or instrument sensitivity is defined. The full paper says ECKS corrections “could be tested in the laboratory or Solar System only if spin densities … were much larger than the typical values” (p. 6), but it never converts that into “sixty orders below observability.” Lana’s comparison of a dimensionless \(\Omega_S\) value with an unstated observability floor is **unsupported**.
- **Parent-black-hole depth:** the full text develops the collapse → torsion bounce → new branch/Einstein–Rosen bridge scenario, not just a one-line decorative interpretation (pp. 6–7). Yet it gives no calculated black-hole-specific current observable amplitude.
- **Missed possible signature:** the paper says rotation of the parent black hole would supply an inherited direction and that small corrections “could then couple to other fields, allowing to verify whether our Universe was born in a black hole” (p. 7). No magnitude or forecast follows, so this is a suggestion rather than a testable prediction, but it contradicts a categorical paper-wide “predicts isotropy, not anisotropy/no signature.”

**Verdict:** support the tiny negative \(\Omega_S\) and non-singular-bounce claims; reject “sixty orders below observability”; qualify “black-hole origin is merely attached” and “no anisotropy/signature.”

### 3.2 arXiv:1410.3881 — axis, anisotropy, quantitative output, and uniqueness

Primary source: N. Popławski, “Universe in a black hole in Einstein–Cartan gravity,” *Astrophysical Journal* **832**, 96 (2016), current published-version manuscript [arXiv:1410.3881v2 PDF](https://arxiv.org/pdf/1410.3881v2), [DOI 10.3847/0004-637X/832/2/96](https://doi.org/10.3847/0004-637X/832/2/96).

- **No preferred axis:** confirmed. The full PDF contains no “axis” or “preferred” occurrence and derives no inherited-axis statistic.
- **“No anisotropy”: false if meant paper-wide.** The paper says matter inside a black hole is “initially inhomogeneous and anisotropic,” that shear grows, and that particle production and repeated bounces can make the universe “increasingly homogeneous and isotropic” (p. 2). An abstract-only statement may say the abstract lacks an anisotropy prediction, but the full paper does discuss anisotropy dynamics.
- **Quantitative content exists:** examples include \(T_{\max}=1.15\times10^{32}\,\mathrm K\), \(H_{\max}=1.09\times10^{43}\,\mathrm{s}^{-1}\), and \(\Omega_{\min}-1=1.3\times10^{-55}\) (p. 6); the particle-production critical rate \(\beta_{\rm cr}\simeq1/929\) (p. 8); and minimum inflation duration \(H t_{\rm infl}\geq23\) (p. 9). Thus a broad “no quantitative prediction” is false beyond the abstract.
- **But no requested observational forecast:** the paper gives no spectral index, tensor-to-scalar ratio, tensor-mode prediction, or explicit current observable test. It says consistency of pre-bounce primordial fluctuations with observations was found in a separate cited numerical paper (p. 10), not derived here. Lana’s line-107 `[VERIFY]` resolves to: **no such signature in this paper, while substantial background numerics are present.**
- **Direct non-uniqueness support:** the conclusion states, “even without assuming that the Universe was born in a black hole, the equations in this article can describe its early dynamics” (p. 10). This is strong primary evidence that the bounce/inflation dynamics do not uniquely diagnose a black-hole parent.

### 3.3 arXiv:1910.10819 — magnitude, scale, functional form, axis, and data

Primary source: N. Popławski, “Universe in a rotating black hole and preferred axis,” current v2 [arXiv:1910.10819v2 PDF](https://arxiv.org/pdf/1910.10819v2), [arXiv record/history](https://arxiv.org/abs/1910.10819), arXiv DOI [`10.48550/arXiv.1910.10819`](https://doi.org/10.48550/arXiv.1910.10819). The record labels it a five-page Popular Physics/astro-ph.CO/gr-qc preprint and supplies no journal reference. An exact-title Crossref query found no matching journal article, but that search cannot prove that no peer-reviewed successor exists anywhere; Lana’s line-200 publication-status marker is therefore **supported by the checked indexes, not exhaustively closed**.

**What the full text contains that “no functional form” misses:**

- Coriolis and centrifugal forces, \(2m\mathbf v\times\boldsymbol\Omega\) and \(m\boldsymbol\Omega\times(\mathbf r\times\boldsymbol\Omega)\) (p. 2).
- Rotational energy shift \(E=E_0-\mathbf M\cdot\boldsymbol\Omega\) (p. 3, eq. 6), proposed to favor galaxy-spin alignment.
- Centrifugal force \(m\Omega^2r\) and effective cosmological constant \(\Lambda=3\Omega^2/c^2\) (pp. 3–4).

Thus **“no functional form” is false if unqualified**. The paper does supply theoretical force/energy functional relations.

**What still is not predicted:**

- No numerical \(\Omega\), force amplitude, galaxy handedness fraction, bulk-flow amplitude, lower bound, likelihood, or detectable floor follows from the parent-black-hole model.
- No explicit scale-dependent or redshift-dependent response function for alignment/handedness is derived. The paper says qualitatively that \(\Omega\) decreases as the universe expands, but does not give \(\Omega(a)\) or an observable asymmetry law.
- No sky direction is predicted from parent parameters. A candidate observed mean direction, \(\alpha=197^\circ\pm47^\circ,\delta=34^\circ\pm3^\circ\), is fitted from cited observations (p. 4), not predicted before looking.

Lana’s “cannot tell 2% from 50%” and finite-precision-null critique therefore remains valid **only when rewritten as no model-predicted observable amplitude/lower bound or response function**, not “no functional form whatsoever.”

**Line-132 dataset marker resolved:** the full paper cites Longo’s \(\sim10^4\)-galaxy SDSS sample at mean \(z\sim0.04\), Shamir’s \(\sim10^5\) SDSS sample at \(z<0.3\), Shamir’s \(\sim10^6\) DESI Legacy Survey sample, a JADES sample at \(z<2\) with a reported \(\sim50\%\) difference, and bulk-flow work by Hudson et al. and Kashlinsky et al. (pp. 3–5, refs. 18–24). This verifies **what the paper cites**, not the underlying observational claims’ correctness.

**Uniqueness:** equations based only on \(\boldsymbol\Omega\) and generic rotating-frame mechanics support Lana’s narrower point that the proposed axis effects are not shown to be unique to black-hole parentage. They do not by themselves prove her blanket “generic to any rotating cosmology/Bianchi model” claim model by model.

### 3.4 arXiv:2509.11468 — literature-line classification

Primary source: N. Popławski, “Gravitational collapse with torsion and universe in a black hole,” *International Journal of Modern Physics A* **40**, 2544007 (2025), [arXiv:2509.11468v2 PDF](https://arxiv.org/pdf/2509.11468v2), [DOI 10.1142/S0217751X25440075](https://doi.org/10.1142/S0217751X25440075).

The full paper uses the Tolman metric plus Einstein–Cartan spin-fluid equations, replaces the collapse singularity with a torsion bounce, includes quantum particle creation, finite inflation, multiple expanding cycles, and a closed universe beyond the horizon (abstract and pp. 2–5). It concludes that the last bounce may be the big bang and that “our Universe might have therefore originated from a black hole existing in another universe” (p. 5).

**Verdict:** Lana’s classification as a 2025 torsion-collapse/bounce continuation is **supported**. The full PDF contains no preferred-axis/anisotropy/testable-current-signature derivation; its passing reference to a more realistic inhomogeneous/rotating fluid does not create one (p. 5).

## 4. Missed baby-universe branch: what the full papers actually add

### 4.1 Frolov–Markov–Mukhanov limiting-curvature branch

Frolov, Markov, and Mukhanov assume limiting curvature, attach Schwarzschild interior to de Sitter space across a transition layer, and obtain an inflating closed or semiclosed world. The abstract says the new world “may begin to inflate and give rise to a new macroscopic universe.” — V. P. Frolov, M. A. Markov, V. F. Mukhanov, “Black holes as possible sources of closed and semiclosed worlds,” *Phys. Rev. D* **41**, 383 (1990), [DOI 10.1103/PhysRevD.41.383](https://doi.org/10.1103/PhysRevD.41.383); primary open precursor report [IC/88/91](https://inis.iaea.org/records/c0cze-8sa45), abstract and report §5, pp. 13–14.

This is substantively different from Einstein–Cartan torsion, but “different assumptions” is better supported than “disagrees” unless a specific contradiction is identified.

### 4.2 Easson–Brandenberger branch

Easson and Brandenberger do more than merely propose a baby universe. They calculate that two regions separated by more than \(114^\circ\) in the child could have been causally connected in the parent and that about \(80^\circ\) of the last-scattering surface is causally connected in their estimate (p. 3). They argue \(k=0\) for the generated universe, discuss Hawking fluctuations as structure seeds, and conclude that the horizon, flatness, and structure-formation benefits are “independent of the details of any specific model” (pp. 4–6). — “Universe Generation from Black Hole Interiors,” [arXiv:hep-th/0103019 PDF](https://arxiv.org/pdf/hep-th/0103019), *JHEP* 2001(06):024, [DOI 10.1088/1126-6708/2001/06/024](https://doi.org/10.1088/1126-6708/2001/06/024).

These are in-paper quantitative/causal details omitted by Lana. They concern early-universe problems rather than an inherited-axis sky statistic.

### 4.3 Dymnikova et al. \(\Lambda\)-black-hole branch

The full model has a nonsimultaneous bang, a Kasner-type anisotropic stage, mass creation during vacuum decay, and open/flat/closed child-universe possibilities (pp. 4–7). It also derives WKB nucleation probabilities and argues an infinite family of white-hole structures can enhance baby-universe birth probability (pp. 7–9). — I. G. Dymnikova et al., “Universes inside a \(\Lambda\) black hole,” [arXiv:gr-qc/0102032 PDF](https://arxiv.org/pdf/gr-qc/0102032), *Phys. Lett. B* **506**, 351–361 (2001), [DOI 10.1016/S0370-2693(01)00174-5](https://doi.org/10.1016/S0370-2693(01)00174-5).

The anisotropic stage is already named in the abstract, but the universe classes and probability machinery require full-paper depth. Again, this establishes diversity, not a demonstrated contradiction with every other branch.

### 4.4 Pourhassan 2025 observational section

The paper is open access in SCOAP³. It predicts a PBH mass function “sharply peaked near \(M_{\rm cr}\),” says wormhole remnants “may produce quasi-periodic, damped gravitational-wave echoes,” and then lists **five** observational categories: PBH mass spectra, gravitational-wave echoes, CMB imprints, large-scale structure/cosmic voids, and holographic simulation; the surrounding text also discusses vacuum-energy anomalies (pp. 9–10, Table 1). — B. Pourhassan, “Multiversal entropy and information conservation in black hole nucleated baby universes,” *Nucl. Phys. B* **1020**, 117160 (2025), [full PDF](https://scoap3-prod-backend.s3.cern.ch/media/harvested_files/10.1016/j.nuclphysb.2025.117160/main.pdf), [SCOAP³ record](https://repo.scoap3.org/records/101891), [DOI 10.1016/j.nuclphysb.2025.117160](https://doi.org/10.1016/j.nuclphysb.2025.117160).

**Verdict:** Lana correctly names critical-mass/PBH and GW-echo prospects, but the assertion that this branch “talks to different instruments entirely” is **incomplete/overbroad** because the paper also names CMB and LSS/void searches. It still derives no inherited preferred-axis/handedness statistic.

## 5. Exactly what may and may not survive citation custody

### Supported or supportable after narrowing

- Pathria bibliographic metadata and the abstract-level closed-universe/black-hole/bounded-expansion description.
- Khakshournia-attributed dust/\(\Lambda\)/maximum-expansion account, clearly labeled as later secondary commentary and not as full-text verification of Pathria.
- \(\Omega_S\approx-10^{-69}\) as a derived present-day torsion-density parameter in arXiv:1007.0587.
- arXiv:1410.3881 has no preferred-axis or \(n_s/r\)/tensor forecast in that paper; its dynamics are explicitly applicable without black-hole origin.
- arXiv:1910.10819 supplies no model-predicted observable magnitude, lower bound, explicit redshift/scale response, or predicted sky direction.
- arXiv:2509.11468 belongs to the torsion-collapse/bounce line and supplies no inherited-axis prediction.
- Pourhassan 2025 discusses critical PBH masses/abundances and possible GW echoes, among additional qualitative channels.
- The audited branches use distinct mechanisms and do not yield one common, uniquely black-hole-parent observable.

### Unsupported, false as written, or still open

1. **Pathria full-text absence claims:** no observable/axis/anisotropy/signature; “forbids nothing”; “no dynamics.” Full text was not accessible, and the latter two formulations already overrun the abstract.
2. **\(\Omega_S\) “sixty orders below observability.”** No sensitivity definition or primary-paper comparison supports it.
3. **arXiv:1007.0587 “predicts isotropy, not anisotropy/no signature” as a whole-paper statement.** Its full discussion includes an inherited preferred direction and possible verification, though no forecast.
4. **arXiv:1410.3881 “no anisotropy” as a whole-paper statement.** The paper explicitly models anisotropy and its suppression.
5. **arXiv:1910.10819 “no functional form.”** It has force/energy/\(\Lambda\) formulas; what is absent is an observable-amplitude/response prediction.
6. **Absolute claim that arXiv:1910.10819 has no peer-reviewed successor.** No journal reference or exact-title Crossref match was found, but exhaustive nonexistence is not proved.
7. **Pourhassan branch uses “different instruments entirely” or only PBH/GW channels.** CMB and LSS/voids are also listed.
8. **“Further proposals disagree with the four surveyed.”** Full texts prove different assumptions, causal structures, and outputs; a concrete point of contradiction must be named to say “disagree.”
9. **“All axis effects are generic to any rotating/Bianchi cosmology.”** The audited rotating-frame derivation establishes non-uniqueness with respect to black-hole parentage, not universality over every rotating cosmology.
10. **“No single mature model exists/owns the observables” as an exhaustive literature verdict.** This is an evaluative closure claim that a deliberately non-exhaustive abstract survey cannot prove.
11. **Any exact observational amplitude or falsification threshold for the inherited-axis scenario.** The 1910.10819 paper does not supply one; the claimed axis package remains non-contractible until such a calculation exists.

## Audit custody verdict

**Do not accept Lana’s file as a citation-safe full-depth prediction audit without revision.** It is transparent about abstract-only access and includes a Pathria warning, but its canonical marking is inconsistent and several substantive negatives outrun the abstracts. The defensible conclusion is narrower: the sampled papers do not presently provide a quantified, uniquely black-hole-parent inherited-axis observable with a lower bound and finite-precision falsification rule. That conclusion is supported by the full PDFs. The broader claims that Pathria forbids nothing, that \(\Omega_S\) is “sixty orders below observability,” that the papers contain no functional forms/anisotropy, or that the literature is exhaustively closed are not.
