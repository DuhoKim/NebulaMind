from pathlib import Path
from bs4 import BeautifulSoup
import hashlib
root=Path('bounce')
s=BeautifulSoup((root/'b4_source_2007.11556v2.html').read_text(),'html.parser')
def equation(n):
    tex=s.find(id='S0.E'+str(n)).find('math')['alttext']
    return f'[{n}: arXiv v2](https://arxiv.org/html/2007.11556v2#S0.E{n})\n\n\\[\n{tex} \\tag{{{n}}}\n\\]\n'
text=r'''# B4 — source beta and B3 units, 2026-09-07

`BETA_VALUES=UNRESOLVABLE_FROM_SOURCE`

The inspected source specifies the production prescription and its dimensional convention, but supplies neither a numerical beta nor sufficient independent inputs to calculate one. Its thermal degrees of freedom are numerical inputs to thermal densities, not a determination of beta. A numerical placement against B3's exploratory interval is therefore unavailable. This completes the source-comparison deliverable only; it does not file a class or reconsider B3.

**Version and access.** Equation numbers and verbatim mathematical transcriptions below refer exclusively to Nikodem J. Popławski, *A nonsingular, anisotropic universe in a black hole with torsion and particle production*, **arXiv:2007.11556v2**, whose inspected HTML header is dated **23 June 2026**. This is the arXiv manuscript/preprint endpoint associated with the published paper, not an assumed copy of the version of record. [Inspected v2](https://arxiv.org/html/2007.11556v2).

The peer-reviewed publication is *General Relativity and Gravitation* **53**, article **18** (2021), published 7 February 2021, DOI **10.1007/s10714-021-02790-7**. The browser retrieval exposed a subscription preview. A separate direct HTTP retrieval returned status 200 and readable publisher full text, including sections 2, 8–10 and equations (33)–(38), even though its final URL was `https://link.springer.com/article/10.1007/s10714-021-02790-7?error=cookies_not_supported&code=c731bb66-abba-4833-b8aa-368c388ba8ee`. Thus the cookie-error URL did **not** prevent this particular full-text inspection. The six equations, unit declaration, beta definition, thermal coefficients and qualitative beta discussion were checked against that retrieved publisher HTML and agree in mathematical content. This limited comparison does not establish whole-document or byte identity. [Publisher article](https://link.springer.com/article/10.1007/s10714-021-02790-7).

**Verbatim source inventory.** Mathematical expressions retain v2's symbols, factors and punctuation; equation tags are displayed alongside them. Prose excerpts are deliberately short. Source beta is denoted **β_S** only in the analysis below; quotations retain **β**. The symbol **Ψ** is our label for the left-hand side of (33), not a symbol printed in these source equations.

In §8, paragraph p22, immediately after (33), the definition is: “\(\beta\) is the production rate”. The preceding prose presents the prescription phenomenologically; it cites v2 reference [5], without importing numerical values from that reference. The complete law and neighbouring comparison are:

'''
for n in (33,34,35): text+=equation(n)+'\n'
text+=r'''The determinant printed beside (33) is \(g=-X^{2}Y^{4}=-a^{6}\). No angular factor or extra normalising coefficient has been inserted here. Equation (35) is a state-dependent inequality, not a numerical beta interval. [v2 §8, p22](https://arxiv.org/html/2007.11556v2#p22).

In §9, p23, the unnumbered thermal relations before (36), transcribed verbatim, are:

\[
\epsilon=h_{\star}T^{4},\qquad p=\epsilon/3,\qquad n_{\textrm{f}}=h_{n\textrm{f}}T^{3},
\]
\[
h_{\star}=(\pi^{2}/30)(g_{\textrm{b}}+(7/8)g_{\textrm{f}})k_{\textrm{B}}^{4}/(\hbar c)^{3},
\]
\[
h_{n\textrm{f}}=(\zeta(3)/\pi^{2})(3/4)g_{\textrm{f}}k_{\textrm{B}}^{3}/(\hbar c)^{3}.
\]

The numerical assignments are **\(g_{\textrm{b}}=29\)** and **\(g_{\textrm{f}}=90\)**, unnumbered before (36). They specify the source's standard-model thermal species counts. They are not beta values, nor does the source define beta as a function of these counts. [v2 §9, p23](https://arxiv.org/html/2007.11556v2#p23).

'''
for n in (36,37,38): text+=equation(n)+'\n'
text+=r'''All other beta occurrences and nearby bounds were inspected:

- **§9, p24, after (37):** beta remains a model parameter alongside parent mass; symbolic initial data are discussed, not numerical beta inputs. [p24](https://arxiv.org/html/2007.11556v2#p24).
- **§9, p25:** the coefficient must be “big enough”; no threshold is evaluated. [p25](https://arxiv.org/html/2007.11556v2#p25).
- **§10, p26, after (38):** “too small” and “too big” qualify the production coefficient; the proposed acceptable range has no numerical endpoints. [p26](https://arxiv.org/html/2007.11556v2#p26).
- **§10, p27, after (38):** the text applies “slightly lesser than 1” to the right-hand side of (38). This wording is retained as written. It supplies neither a numerical tolerance nor a value of beta. [p27](https://arxiv.org/html/2007.11556v2#p27).

**Dimensions and normalisation — analysis of the inspected v2 equations.** Section 2, after (2), explicitly states: “We use units in which \(c=1\).” No declaration setting \(G\), \(\hbar\), \(k_B\), \(\kappa\), or the thermal coefficients to one was found. In §3 before (9), \(\kappa=8\pi G\); beside (1), \(\alpha=\kappa(\hbar c)^2/32\). These are physical coefficients, not B3's sensitivity parameters. [v2 §2](https://arxiv.org/html/2007.11556v2#p9), [v2 (1)](https://arxiv.org/html/2007.11556v2#S0.E1), [v2 (9)](https://arxiv.org/html/2007.11556v2#S0.E9).

The source's Hubble normalisation is exactly:

'''
text+=equation(16)
text+=r'''
With length as the common space/time dimension in this \(c=1\) convention, fermion number is a count, \([n_f]=L^{-3}\), \([t]=L\), \([H]=L^{-1}\). Thus (33) has \([\Psi]=L^{-4}\) and **\([\beta_S]=1\)**. This is dimensional analysis, not a source assertion that Planck units or B3 units have been selected. There is no factor of 3 absorbed into beta: the 3 belongs to the mean-volume expansion in (16)/(34), and the 81 in (35) is \(3^4\).

For a seconds-and-metres convention, define physical proper time \(t_s\), \(\ell=ct_s\), and \(H_s=d\ln a/dt_s\). Restoring dimensions in v2 (33) gives, by change of variable,

\[
\frac{dn_f}{dt_s}+3H_s n_f=\frac{\beta_S}{c^3}H_s^4
       \equiv\beta_{\mathrm{sec}}H_s^4,
\qquad [\beta_{\mathrm{sec}}]=\mathrm{s^3\,m^{-3}}.
\]

Hence \(\beta_{\mathrm{sec}}=\beta_S/c^3\); a dimensionful coefficient multiplying a seconds-based \(H_s^4\) must not be identified numerically with \(\beta_S\).

There is a further limit on using the *printed* (35) as a calibrated bound: with the dimensions just established, its left-hand side has dimension \(L^{-7}\) and its right-hand side \(L^{-3}\). Equation (32) compares \(\kappa\alpha n_f^2\) with shear, whereas (35) as printed compares unweighted rates. No rescaling of number density that resolves this difference is declared in the inspected text. We preserve (35) and do not repair it or use it to infer a physical beta threshold. This local units observation does not change the normalisation obtained directly from (33)–(34), and does not reopen B3.

Likewise, the literal right-hand side of (38) has inverse-time dimension; comparison to the bare number 1 in p27 cannot itself specify a coefficient. If one instead examines the dimensionless combination appearing inside (38),

\[
R=\frac{\beta_S H^3}{3h_{n\mathrm f}T^3},
\]

then \(R\approx1\) would imply \(\beta_S\approx3h_{n\mathrm f}(T/H)^3\) for a suitable expanding state. That is our conditional algebraic reading, not a corrected quotation or a source-supplied estimate. The source gives no numerical \(T/H\), tolerance, or independently specified trajectory at which to evaluate it. Its \(g_f=90\) determines \(h_{n\mathrm f}\) in selected physical units but does not determine \(T/H\).

**Conversion to the exploratory script — analysis, not source physics.** The inspected local [b3_rescue.py](b3_rescue.py) sets \(\kappa=\epsilon_0=h_\star=a_0=1\) and scans beta values \(0,0.001,0.01,0.1,1,10\). The normalisation is documented in [B3_RESCUE_20260907.md](B3_RESCUE_20260907.md), under “Inputs and all added assumptions”. Denote script quantities with subscript B. For a chosen physical initial ordinary energy density \(\epsilon_0\), number-density unit \(n_{\rm ref}\), and length-time unit \(\ell_{\rm ref}\),

\[
\ell_{\rm ref}=(\kappa\epsilon_0)^{-1/2},\qquad
\hat t=\ell/\ell_{\rm ref},\quad n_B=n_f/n_{\rm ref},\quad H_B=\ell_{\rm ref}H.
\]

Here \(\kappa\) and \(\epsilon_0\) are expressed consistently with the source's \(c=1\) energy-density convention. In SI the corresponding \(\kappa_{\rm SI}=8\pi G/c^4\) gives \(\ell_{\rm ref}=(\kappa_{\rm SI}\epsilon_0)^{-1/2}\) and \(t_{\rm ref,s}=\ell_{\rm ref}/c\). Substitution into (34) yields

\[
\boxed{\beta_B=\frac{\beta_S}{n_{\rm ref}\ell_{\rm ref}^{3}}
=\frac{\beta_{\rm sec}}{n_{\rm ref}t_{\rm ref,s}^{3}}.}
\]

This is B3's documented conversion with its time convention made explicit. Both \(\beta_B\) and \(\beta_S\) are dimensionless, but they coincide only for the additional choice \(n_{\rm ref}\ell_{\rm ref}^3=1\). B3 does not impose that choice. Its temperature unit fixes \(h_\star=1\) in closure (b), not the independently selectable number-density unit. Its \(\alpha_B=\alpha_{\rm phys}n_{\rm ref}^2/\epsilon_0\) and exploratory interval \([0.25,1]\) also do not specify a physical density scale.

A numerical conversion requires (i) an independently specified \(\beta_S\), (ii) the physical \(\epsilon_0\) defining the script's initial-density unit, and (iii) \(n_{\rm ref}\), or an equivalent complete normalisation. To infer beta from (33) instead requires an independent physical fermion-production density rate \(\Psi\) and nonzero \(H\) at the same state: \(\beta_S=\Psi/H^4\) in \(c=1\) units. Neither is numerically supplied. A microscopic alternative would have to supply a production calculation (species, couplings and state/geometry, and any needed cutoff), evaluate its net fermion rate, establish an approximately constant \(\Psi/H^4\), and then apply the conversion above. The paper does not specify such a cross-section or cutoff chain. A rate per unit volume defined by (33) is not an independent input to (33).

For any eventual normalisation \(Q=n_{\rm ref}\ell_{\rm ref}^3>0\), the exact comparison would be

\[
\beta_B\in[0.001,10]\quad\Longleftrightarrow\quad
\beta_S\in[0.001Q,10Q].
\]

Neither \(\beta_S\) nor \(Q\) is fixed here. Therefore no below/inside/above placement is available, and setting them to convenient values would manufacture the requested comparison. This is a units comparison only, not validation of B3. The source thermal relation \(n_f=h_{n\mathrm f}T^3\) has not been imposed on B3's independently sourced number density.

**Search coverage and verdict.** The complete retrieved v2 text, including references, was read and searched for beta, production/rate, numerical assignments, estimates, bounds, units, cross-sections, cutoffs and Planck references. Its ten beta-bearing mathematical elements occur only in p22 (four), p23 (one), p24 (one), p25 (one), and p26 (three). Equations (33)–(38), all those paragraphs and p27 are covered above. No numerical beta assignment, order of magnitude, evaluated lower/upper bound, microscopic beta formula, or independent numerical rate was found. No values from the papers cited in v2 reference [5] are silently substituted for this paper's own values.

The thermal species counts and conditional relations do not close a calculation of beta. Formal rearrangement of a phenomenological law is not a derivation from independent supplied physical inputs. Thus the selected verdict is **BETA_VALUES=UNRESOLVABLE_FROM_SOURCE**, rather than SUPPLIED or DERIVABLE. The normalisation is understandable; the numerical comparison is unresolvable from the inspected source and B3's declared scale choices.

**Audit artifacts.** Retrieved source and publisher HTML are preserved under `bounce/`; the text extraction uses the HTML's mathematical `alttext` rather than discarding equations. No B3 execution or modification was needed for this source-and-units audit. Input hashes:

'''
for name in ['b4_source_2007.11556v2.html','b4_springer_access.html','b3_rescue.py','B3_RESCUE_20260907.md']:
    text+=f'- `{name}`: `{hashlib.sha256((root/name).read_bytes()).hexdigest()}`\n'
(root/'B4_BETA_COMPARISON_20260907.md').write_text(text)
