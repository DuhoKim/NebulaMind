from pathlib import Path
from bs4 import BeautifulSoup
import re
base=Path('bounce')
soup=BeautifulSoup((base/'b4_springer_access.html').read_text(),'html.parser')
article=soup.find('article')
paras=[p.get_text(' ',strip=True) for p in article.find_all('p')]
def para(starts):
    matches=[p for p in paras if p.startswith(starts)]
    if len(matches)!=1: raise ValueError((starts,len(matches)))
    return matches[0]
def quote(p):
    return '> '+p+'\n\n'
report=r'''# B5 — physical validity at the fluid bounce, 2026-09-07

**Physical validity at the target bounce is NOT ESTABLISHED for all three assumptions.** Published work supplies necessary coarse-graining requirements and conditional spin-fluid results, but no demonstrated validity window containing this route's strongly sheared, contracting, spin-dominated regime. This is an assessment of support for the assumptions, not a finding that every effective-fluid bounce is impossible.

**Scope.** The target is the **FLUID row in spatially flat Bianchi I**, with ordinary density \(\epsilon\), effective density \(\rho_F=\epsilon-\alpha_F n_f^2\), and effective pressure \(P_F=p-\alpha_F n_f^2\). In natural units \(\alpha_F=\kappa/32\). The matter form is read directly from publisher GRG Eq. (1). [Publisher GRG, Eq. (1)](https://link.springer.com/article/10.1007/s10714-021-02790-7#Equ1).

The already-established diagnostic is \(R_F=\alpha_F n_f^2/\epsilon=1\) at the **fluid's flat, shear-free limiting turning point**, as recorded in [C1_REEXAM_20260907.md](C1_REEXAM_20260907.md). For a sheared turning point, the same flat constraint \(3H^2=\kappa\rho_F+\sigma^2\) requires \(R_F=1+\sigma^2/(\kappa\epsilon)\geq1\), assuming \(\epsilon>0\). This identifies the regime being audited; it does not redo the bounce analysis. No Dirac turning-point ratio is used. The publisher GRG paper itself uses **Kantowski–Sachs (KS)**; quotations about that geometry are explicitly separated below.

**Source convention.** “GRG” means N. J. Popławski, *A nonsingular, anisotropic universe in a black hole with torsion and particle production*, **General Relativity and Gravitation 53, 18 (2021)**, DOI 10.1007/s10714-021-02790-7. All GRG quotations below come from the user-specified saved **publisher HTML**, [b4_springer_access.html](b4_springer_access.html), not arXiv. Its article information identifies the version of record as 7 February 2021. Mathematical notation and whitespace are rendered legibly; reference numbers remain those of the publisher. No whole-document publisher/arXiv identity is claimed. No conclusion about later corrections is drawn. The local arXiv:2007.11556v2 is a manuscript/preprint endpoint, not the quotation source for this report.

## 1. Effective-fluid description at an order-one spin correction

**What the source establishes.** GRG §1 describes macroscopic averaging and uses the resulting fluid source. Immediately before Eq. (1), it states:

> Hehl et al. [ 50 ] found that macroscopic averaging of the spin terms in the energy–momentum tensor gives a nonzero value even for randomly oriented spins.

Immediately after Eq. (1), it states:

> At lower densities, the effects of torsion can be neglected and EC effectively reduces to general relativity.

> At extremely high densities, much greater than nuclear density, the negative corrections from the spin-torsion coupling in ( 1 ) violate the strong energy condition and manifest themselves as repulsive gravity that may prevent the formation of a gravitational singularity in a black hole.

These are quotations from **publisher GRG §1**, not arXiv. They describe the intended importance of the correction; they provide neither an averaging error estimate nor a density cutoff below which the high-density matter approximation is controlled. GRG §9 assumes kinetic equilibrium and ideal ultrarelativistic thermal densities; its complete condition is quoted in §3 below. The paper does not calculate an equilibration rate, spin correlation length, or interacting equation of state at the turning point. [Publisher GRG §§1, 9](https://link.springer.com/article/10.1007/s10714-021-02790-7#Sec9).

**There is a published coarse-graining condition.** GRG's reference [50] is F. W. Hehl, P. von der Heyde and G. D. Kerlick, *General relativity with spin and torsion and its deviations from Einstein's theory*, **Physical Review D 10, 1066–1069 (1974)**. On p. 1067, §I, it requires:

> an “infinitesimal” volume element must contain a large number of atoms or elementary particles.

Quotation source: **publisher APS PDF**, p. 1067, left column; line-break hyphenation removed. The same page, after Eq. (13b), says the spin–vorticity contribution vanishes without vorticity, or when spin-density fluctuations have a “shorter characteristic length than the local fluid vorticity.” This additional quotation is from the same publisher PDF, p. 1067, right column. That is a specific cancellation condition, not a proof that all spin correlations can be replaced by a scalar at arbitrary density. Its neutron mass-density estimate \(\bar\rho\sim10^{54}\,\mathrm{g\,cm^{-3}}\) marks the importance of spin corrections in that model, not an upper validity limit or our ultrarelativistic bounce density. [Publisher Hehl et al. 1974, p. 1067, §§I–II and Eqs. (12)–(13)](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevD.10.1066/fulltext).

**The RMP warning is explicit.** F. W. Hehl, P. von der Heyde, G. D. Kerlick and J. M. Nester, *General relativity with spin and torsion: Foundations and prospects*, **Reviews of Modern Physics 48, 393–416 (1976)**, §V.B.7, p. 409, discusses extending inverse-volume-squared scaling to random spins:

> Of course, such an assumption must be justified physically.

It then characterizes its high-density matter descriptions as:

> a very naive approximation to physical reality, since we have neglected nongravitational interactions.

Both quotations: **publisher APS PDF**, p. 409, left column, first two paragraphs; line-break hyphenation removed. Section V.B.7, p. 408, expects random spins with rapid temporal fluctuations and retains quadratic terms after averaging. It supplies no numerical density or correlation-length validity interval. Section V.C.3, p. 410, warns that its radiation-loaded neutron cosmology reaches a minimum radius below the neutron Compton wavelength, outside its nonquantized treatment. That example is not a transferable density bound for our ultrarelativistic fluid or a verdict on our sheared trajectory. [Publisher Hehl et al. RMP, §§V.B.7, V.C.3](https://harvest.aps.org/v2/journals/articles/10.1103/RevModPhys.48.393/fulltext).

**Separate source admission: DIRAC methodology, not the target row.** In **Physical Review D 85, 107502 (2012)**, p. 107502-2, upper right column, Popławski writes:

> The particle approximation for Dirac fields, however, is not self-consistent [4].

> The spin-fluid description also violates the cosmological principle [14].

Quotation source: **publisher APS PDF**, not arXiv. These sentences explain that paper's choice of a Dirac spin tensor and closed FLRW setting. They are an author's published challenge to the microscopic identification of a spin fluid, not a density-dependent breakdown theorem for the unpolarised FLUID row in Bianchi I. No pressure sign, critical temperature, or bounce result is transferred from that paper. [Publisher Popławski 2012, p. 107502-2](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevD.85.107502/fulltext).

**What is NOT ESTABLISHED.** Neither the nonzero quadratic average nor the formal elimination of algebraic torsion establishes that a prescribed macroscopic fluid remains an accurate description when its spin term cancels or exceeds the entire ordinary density. Conversely, \(R_F\geq1\) alone is not a theorem of fluid breakdown: an effective description can include an interaction nonperturbatively. What is missing here is a controlled microscopic/statistical justification of this particular source and its thermal assumptions in that regime. The published many-particle requirement is necessary; it is not a sufficient density window.

**Condition our regime would have to satisfy — diagnostic, not an adopted closure.** There must be a physically meaningful averaging cell of size \(L\), with \(n_fL^3\gg1\), that is small compared with local gravitational and matter-variation scales. To justify a random-spin scalar average, spin correlations must also be sufficiently short compared with the averaging cell, with the relevant moments remaining isotropic. A useful statement of the required separation is \(\max(n_f^{-1/3},\ell_{\rm spin})\ll L\ll L_{\rm macro}\). This hierarchy is our formulation of what needs checking, not a quantitative bound proved by GRG or the RMP. For the kinetic-equilibrium thermal formulas, microscopic equilibration must be faster than local deformation and thermal evolution, and interaction corrections to those formulas must be controlled. No values of \(\ell_{\rm spin}\), equilibration times, or such an error bound are established for this bounce. At \(H=0\), an infinite mean Hubble time does not remove directional shear or finite curvature/evolution scales. **Membership in a controlled fluid regime: NOT ESTABLISHED.**

## 2. Does the unpolarised isotropic average survive sheared contraction?

**What published Weyssenhoff cosmology establishes conditionally.** S. D. Brechet, M. P. Hobson and A. N. Lasenby, *Classical big-bounce cosmology: dynamical analysis of a homogeneous and irrotational Weyssenhoff fluid*, **Classical and Quantum Gravity 25, 245016 (2008)**, §3.2, p. 6, permits extension of the averaging to anisotropic models:

> provided that on small macroscopic scales the spin-density pseudo-vectors are assumed to be randomly oriented.

Quotation source: **IOP publisher-formatted PDF held by EPFL**, not arXiv. Its Eqs. (30)–(32) retain spin variance while removing mean spin. Its unaveraged Eq. (12) contains the shear–spin term \(-2\sigma_{(\mu}{}^{\lambda}S_{\nu)\lambda}\) and a projected spin-divergence term; Eq. (32) becomes a perfect-fluid source after averaging. This is a conditional reduction of an assumed Weyssenhoff medium, not a kinetic demonstration that initially random spins remain random in a strongly sheared contraction. It provides no density-dependent polarisation-growth or randomisation rate. [Brechet et al., publisher PDF, pp. 4, 6–7, Eqs. (12), (30)–(32)](https://infoscience.epfl.ch/server/api/core/bitstreams/66a4adbd-9c64-44ae-98ec-b323e021bc76/content).

**Separate setting: relativistic spin hydrodynamics, not an EC bounce.** Published calculations show that shear can produce spin structure even without invoking a rotating cosmology:

- F. Becattini, M. Buzzegoli and A. Palermo, *Spin-thermal shear coupling in a relativistic fluid*, **Physics Letters B 820, 136519 (2021)**, abstract: “also the shear tensor contributes to the polarization of particles in a fluid.” Quotation source: **Elsevier publisher PDF distributed through SCOAP3**, not arXiv. Their first-gradient, local-thermodynamic-equilibrium calculation obtains a momentum-dependent spin contribution from the symmetric derivative of \(b_\mu=u_\mu/T\) (their symbol is \(\beta_\mu\), unrelated to GRG's production coefficient). Their expansion requires thermodynamic variation scales long compared with the relevant correlation lengths (§2, pp. 2–3). The particle-spin formula assumes free or quasi-free fields (§3, p. 3) and depends on an integration hypersurface. This does not validate it in a spin-dominated gravitational collapse. [Becattini et al., publisher PDF, §§2–3 and Eq. (23)](https://scoap3-prod-backend.s3.cern.ch/media/files/63428/10.1016/j.physletb.2021.136519_a.pdf).
- S. Y. F. Liu and Y. Yin, *Spin polarization induced by the hydrodynamic gradients*, **JHEP 07 (2021) 188**, find shear-induced quadrupolar polarisation in momentum space using first derivatives and one-loop linear response. Their hydrodynamic condition is \(q_0,|\mathbf q|\ll\tau_R^{-1}\), with \(\tau_R\) the relaxation time (§2 and §3.1); the coefficient calculation also assumes a separation from the single-particle energy scale and weak coupling (§3.1). This establishes an allowed, calculable shear response within that approximation, not net uniform alignment of every spin. Their target application is heavy-ion matter, not a self-consistent EC cosmology. Source read: **Springer publisher PDF**, not arXiv. [Liu and Yin, §§2–3, 5.2, 6](https://link.springer.com/content/pdf/10.1007/JHEP07%282021%29188.pdf).

**What does not follow.** These results prevent us from treating kinetic equilibrium or zero vorticity as a general proof of an unpolarised distribution. They also do not prove that shear necessarily creates a nonzero cell-averaged polarisation here: a momentum-dependent quadrupole can cancel in an integrated mean. A vanishing first moment alone does not demonstrate isotropic second moments or the vanishing of mixed spin–flow correlations. No published calculation establishing either preservation or destruction of this route's full isotropic spin average through its \(R_F\geq1\) Bianchi I contraction was identified in the sources inspected. Both a negligible response and a dynamically important response in this particular regime are **NOT ESTABLISHED**.

**Consequence and required condition in flat Bianchi I.** The condition needed by the retained shear argument is that the actual averaged effective anisotropic stress \(\pi_{ij}\) vanish (or be quantitatively negligible for the intended approximation), along with the spin terms discarded by the isotropic average. Polarisation or surviving spin–shear correlations can leave anisotropic source terms, so the source-free shear evolution cannot simply be retained. Special symmetric polarised configurations can cancel particular terms; polarisation alone is not a universal theorem that every component of \(\pi_{ij}\) is nonzero. The relevant stress must be checked.

A physical justification would have to show that the spin distribution, its second moments and relevant mixed correlations remain sufficiently isotropic, with any generated polarisation/stress negligible over the contraction time. This requires spin-response and relaxation information at the actual density, temperature and shear; fast equilibration alone is insufficient, since a local-equilibrium state itself can have a shear-induced response. The small-gradient conditions quoted above would need verification before those microscopic formulas could be used, and satisfying them still would not prove zero polarisation. **Persistence of the required average at this bounce: NOT ESTABLISHED.** No polarised model is computed here.

## 3. Extrapolating the phenomenological production law

**Verdict on physical validity of our full-collapse extrapolation: SIMPLY NOT ADDRESSED by the source; NOT ESTABLISHED.** GRG explicitly proposes its prescription for contraction as well as expansion and uses it in a collapse scenario. Thus it does support such use **as phenomenological modelling in its own KS setting**. It neither proves validity of fixed \(\beta\) throughout the entire flat Bianchi I collapse nor expressly forbids that extrapolation. Calling the law “expansion-only” or “valid only immediately after the bounce” would misquote this source.

**Complete inventory of applicability language and nearby bounds — publisher GRG, KS setting.** A read of the complete saved article, checked for `valid`, `approx`, `phenomen`, `equilibrium`, density, correlation/length and production-rate terms, found no explicit domain-of-validity inequality for Eq. (33). The sentences that could otherwise be mistaken for such a restriction are reproduced below, grouped with their surrounding parameter and phase qualifications. These quotations are from the user-provided publisher HTML, including its reference numbers; they are not copied from arXiv. Full contextual paragraphs are included where separating a single sentence could change the meaning. The bounds describe proposed outcomes, not approximation-error bounds.

**(a) §8: physical setting, the prescription, and its singularity-avoidance qualifications.** [Publisher GRG §8](https://link.springer.com/article/10.1007/s10714-021-02790-7#Sec8).

'''
report+=quote(para('The interior of a forming black hole'))
report+=quote(para('The production rate of particles'))
report+=r'''> \[
> \frac{1}{\sqrt{-g}}\frac{d(\sqrt{-g}n_f)}{dt}=\beta H^4,\tag{33}
> \]

'''
report+=quote(para('where \\(g=-X').removesuffix(' Accordingly,')) if any(p.startswith('where \\(g=-X') for p in paras) else quote(para('where \\(g=-').removesuffix(' Accordingly,'))
report+=quote(para('To avoid a singularity').split(' Comparing')[0])
report+=quote(para('After the formation of the event horizon'))
report+=r'''The reference to Eq. (30) and inequality (35) belongs to KS. Those equations are not substituted for flat Bianchi I shear evolution. Equation (34), immediately after the law, rewrites it as \(\dot n_f+3Hn_f=\beta H^4\); that algebraic rewriting supplies no additional validity condition.

**(b) §9: thermal regime, choice of parameters and initial epoch, and proposed subsequent cycles.** [Publisher GRG §9](https://link.springer.com/article/10.1007/s10714-021-02790-7#Sec9).

'''
report+=quote(para('The spin fluid in the early universe').split(' In the presence')[0])
report+=quote(para('Equations ('))
report+=quote(para('If \\(\\beta \\) is big enough'))
report+=r'''The equilibrium statement bounds the assumed thermal matter description; it does not derive the production prescription or show that equilibrium is maintained by the source term. The horizon initial data and cycles show the breadth of the proposed use, but do not supply a calibrated interval of validity. All geometry and rotation statements in these quotations belong to the publisher's KS/Kerr discussion, not the target Bianchi I calculation.

**(c) §10: all production-coefficient bounds and the approximate inflationary regime.** Equation (38), to which these sentences refer, is \(\dot T/T=H[\beta H^3/(3h_{n_f}T^3)-1]\). The wording of the comparison with 1 below is retained as printed; it is neither repaired nor used to infer a coefficient. [Publisher GRG §10](https://link.springer.com/article/10.1007/s10714-021-02790-7#Sec10).

'''
report+=quote(para('When the mean scale factor'))
report+=quote(para('If the right-hand side'))
report+=r'''These specify possible singular, inflationary and post-inflationary outcomes of the assumed equations. They do not establish a density, shear, curvature, adiabaticity, particle-species or duration window in which \(\beta H^4\) is a justified microscopic rate. In particular, a condition chosen to obtain finite inflation is not a proof of validity during contraction.

**(d) Source's own approximate-scenario admissions — explicitly KS geometry.** The abstract, the end of §1 and §11 each qualify the scenario. These are all three occurrences of that admission, with the summary's explanatory sentences. [Publisher GRG abstract and §§1, 11](https://link.springer.com/article/10.1007/s10714-021-02790-7#Sec11).

'''
abstract=para('We consider a universe formed')
report+=quote(abstract[abstract.index('This scenario is only approximate:'):])
intro=para('A closed, homogeneous and anisotropic universe')
report+=quote(intro[intro.index('This scenario is only approximate:'):])
report+=quote(para('This scenario is only approximate.'))
report+=r'''These admissions concern the KS metric and its proposed replacement. They must not be recast as either a high-density averaging criterion or a theorem about flat Bianchi I. The separate §1 statement about particle production immediately after the bounce is an application, not an exclusivity restriction:

'''
p=para('Quantum particle production immediately')
report+=quote(p.split(' A bouncing scenario')[0])
report+=r'''**What is missing, and the condition our use would need.** To certify the extrapolation, a published microscopic or controlled effective calculation would have to establish that the net fermion production rate in the relevant state and geometry is approximated by \(\beta H^4\), with approximately constant \(\beta\) and a controlled error throughout the density/shear/curvature history being used. No such condition is supplied in this GRG source. At a volume turning point the adopted law gives zero production because \(H=0\); that is a property of the ansatz, not evidence that all gravitational pair-production effects vanish there. A physical check at that point would require the underlying state-dependent calculation. No replacement law, coefficient, conservation closure, or new model is selected here.

## Source custody and limits of this report

All literature used affirmatively above is published in peer-reviewed journals. The RMP and 1974 Hehl PDFs are APS publisher copies; the 2012 quotation is from the existing APS publisher copy; the Brechet PDF bears IOP's journal imprint and pagination and is served by EPFL; the Becattini PDF bears Elsevier's journal imprint and is served through SCOAP3; the Liu–Yin PDF is served directly by Springer. Repository delivery of a publisher-formatted PDF is identified separately from an arXiv manuscript. No preprint supplies a validity claim in this report.

The evidence extraction, downloaded publisher copies and access metadata are confined to [b5_sources/](b5_sources/), including [access.json](b5_sources/access.json). Existing APS sources remain in [prd_publisher_verify_20260907/](prd_publisher_verify_20260907/). Quoted PDF passages were checked against rendered publisher pages. GRG was inspected directly from the saved HTML; its section/equation IDs provide the quotation locators. Input SHA-256 values:

- `b4_springer_access.html`: `fb94da36db11823ed1081fd39226a7134dec64883a7811c4011a1ea7234efc88`
- `prd_publisher_verify_20260907/rmp_pdf.pdf`: `a5aa872c97e88f2a5e72554974166e3c51c5b078889bcf8e531afda4b958bcb9`
- `prd_publisher_verify_20260907/prd_pdf.pdf`: `edbbf7279e40d044130df35ce2b10c1281669dc2b9e90c2d61a0e6d308d744da`

The search covered published Weyssenhoff averaging/bounce analyses, the source's cited 1974 averaging paper and the 1976 RMP, and published shear-induced spin-polarisation calculations. **NOT ESTABLISHED** means not demonstrated by the inspected evidence, not a claim that no paper could exist. A failed IOP access attempt for the source's 2016 reference is logged but supplies no evidence here. The relevant 2021 GRG text was available in full. No finding reopens B1/B2/B3, adopts a closure, files a class, or changes files outside `bounce/`.

| Assumption | Established validity condition | Is our bounce regime inside it? | Source read (publisher/arXiv/NOT ESTABLISHED) |
|---|---|---|---|
| Macroscopic spin-fluid averaging | Many particles per macroscopically small element; a short spin-fluctuation scale can cancel the specific spin–vorticity term. No sufficient high-density validity window supplied. | **NOT ESTABLISHED** at \(R_F\geq1\); cell/variation/correlation scales and error control are missing. | **Publisher:** Hehl 1974 p. 1067; RMP pp. 408–409; GRG §1. |
| Ideal ultrarelativistic thermal matter used with that fluid | Ultrarelativistic matter in kinetic equilibrium is stipulated; preservation and interaction accuracy are not proved. | **NOT ESTABLISHED**; no equilibration or interacting-thermodynamics check at the bounce. | **Publisher:** GRG §9. |
| Unpolarised isotropic spin average and negligible anisotropic stress | Random orientations on small macroscopic scales are assumed in anisotropic Weyssenhoff averaging. General persistence criterion is **NOT ESTABLISHED**. | **NOT ESTABLISHED**; published shear responses in other settings neither validate nor refute persistence here. | **Publisher:** Brechet §3.2; Becattini §§2–3; Liu–Yin §§2–3, 5–6. |
| Fixed-\(\beta\), \(\beta H^4\) production through the entire collapse | Phenomenological use for contraction/expansion; no physical validity window for the full extrapolation. | **NOT ESTABLISHED**; physical support for the full flat Bianchi I extrapolation is **not addressed**. | **Publisher:** GRG §§8–10; its KS caveats in abstract, §§1, 11. |
'''
(base/'B5_VALIDITY_20260907.md').write_text(report)
print('Wrote',len(report.split()),'words',len(report.encode()),'bytes')
