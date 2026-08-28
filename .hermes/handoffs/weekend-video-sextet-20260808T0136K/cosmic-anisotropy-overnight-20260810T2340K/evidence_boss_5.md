URL: https://arxiv.org/html/2407.03397v1

HTML conversions [sometimes display errors](https://info.dev.arxiv.org/about/accessibility_html_error_messages.html) due to content that did not convert correctly from the source. This paper uses the following packages that are not yet supported by the HTML conversion tool. Feedback on these issues are not necessary; they are known and are being worked on.

- failed: acro

Authors: achieve the best HTML results from your LaTeX submissions by following these [best practices](https://info.arxiv.org/help/submit_latex_best_practices.html).

[License: CC BY-NC-SA 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2407.03397v1 \[astro-ph.CO\] 03 Jul 2024

\\DeclareAcronym

2LPTshort=2LPT, long=second-order Lagrangian perturbation theory
\\DeclareAcronym2PCFshort=2PCF, long=two-point correlation function
\\DeclareAcronym3PCFshort=3PCF, long=three-point correlation function
\\DeclareAcronym4PCFshort=4PCF, long=four-point correlation function
\\DeclareAcronym8PCFshort=8PCF, long=eight-point correlation function
\\DeclareAcronymBAOshort=BAO, long=baryon acoustic sscillations
\\DeclareAcronymBOSSshort=BOSS, long=Baryon Oscillation Spectroscopic Survey
\\DeclareAcronymCLshort=CL, long=confidence levels
\\DeclareAcronymCMASSshort=CMASS, long=“Constant Stellar Mass”
\\DeclareAcronymCMBshort=CMB, long=cosmic microwave background
\\DeclareAcronymDECshort=DEC, long=declination
\\DeclareAcronymDESIshort=DESI, long=Dark Energy Spectroscopic Instrument
\\DeclareAcronymFKPshort=FKP, long=Feldman–Kaiser–Peacock
\\DeclareAcronymLSSshort=LSS, long=large-scale structure
\\DeclareAcronymNGCshort=NGC, long=North Galactic Cap
\\DeclareAcronymPDFshort=PDF, long=probability density function
\\DeclareAcronymRAshort=RA, long=right ascension
\\DeclareAcronymSGCshort=SGC, long=South Galactic Cap

Report issue for preceding element

# No evidence for parity violation in BOSS

Report issue for preceding element

Alex Krolewski
Simon May
Kendrick Smith

Hans Hopkins

Report issue for preceding element

###### Abstract

Report issue for preceding element

Recent studies have found evidence for parity violation in the BOSS spectroscopic galaxy survey, with statistical significance as high as 7⁢σ7𝜎7\\sigma7 italic\_σ.
These analyses assess the significance of the parity-odd four-point correlation function (4PCF) with a statistic called χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT.
This statistic is biased if the _parity-even_ eight-point correlation function (8PCF) of the data differs from the mock catalogs.
We construct new statistics χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT, χnull2subscriptsuperscript𝜒2null\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT that separate the parity violation signal from the 8PCF bias term, allowing them to be jointly constrained.
Applying these statistics to BOSS, we find that the parity violation signal ranges from 00 to 2.5⁢σ2.5𝜎2.5\\sigma2.5 italic\_σ depending on analysis choices, whereas the 8PCF bias term is ∼6⁢σsimilar-toabsent6𝜎\\sim 6\\sigma∼ 6 italic\_σ.
We conclude that there is no compelling evidence for parity violation in BOSS.
Our new statistics can be used to search for parity violation in future surveys, such as DESI, without 8PCF biases.

Report issue for preceding element

## 1 Introduction

Report issue for preceding element

### 1.1 Background: Parity violation in BOSS?

Report issue for preceding element

Recently, two groups \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 ""), [2](https://arxiv.org/html/2407.03397v1#bib.bib2 "")\] reported evidence for parity violation in the \\acBOSS, following the proposal of \[ [3](https://arxiv.org/html/2407.03397v1#bib.bib3 "")\] and using methods developed in \[ [4](https://arxiv.org/html/2407.03397v1#bib.bib4 "")\].
In \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\], statistical significance as high as 7.1⁢σ7.1𝜎7.1\\sigma7.1 italic\_σ was reported, and in \[ [2](https://arxiv.org/html/2407.03397v1#bib.bib2 "")\] statistical significance as high as 2.9⁢σ2.9𝜎2.9\\sigma2.9 italic\_σ was reported.111Refs. \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 ""), [2](https://arxiv.org/html/2407.03397v1#bib.bib2 "")\] report different statistical significances mainly because a key analysis parameter Nβsubscript𝑁𝛽N\_{\\beta}italic\_N start\_POSTSUBSCRIPT italic\_β end\_POSTSUBSCRIPT (number of radial bins in the χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT estimator) is chosen differently.
In \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 ""), [2](https://arxiv.org/html/2407.03397v1#bib.bib2 "")\], Nβsubscript𝑁𝛽N\_{\\beta}italic\_N start\_POSTSUBSCRIPT italic\_β end\_POSTSUBSCRIPT is chosen to be 18, 10 respectively.
(Note that \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\] also presents results with Nβ=10subscript𝑁𝛽10N\_{\\beta}=10italic\_N start\_POSTSUBSCRIPT italic\_β end\_POSTSUBSCRIPT = 10, and these agree qualitatively with \[ [2](https://arxiv.org/html/2407.03397v1#bib.bib2 "")\].)
The parameter Nβsubscript𝑁𝛽N\_{\\beta}italic\_N start\_POSTSUBSCRIPT italic\_β end\_POSTSUBSCRIPT is defined precisely in [section3.1](https://arxiv.org/html/2407.03397v1#S3.SS1 "3.1 The parity-odd four-point estimator ℰ̂_𝑎 ‣ 3 Reproducing results from [1, 2] ‣ No evidence for parity violation in BOSS").

Report issue for preceding element

Cosmological parity violation, if confirmed, would have profound implications for fundamental physics, and so the results of \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 ""), [2](https://arxiv.org/html/2407.03397v1#bib.bib2 "")\] have attracted a great deal of interest.222E. g. three recent workshops were devoted to parity violation:
[https://events.asiaa.sinica.edu.tw/workshop/20231204/](https://events.asiaa.sinica.edu.tw/workshop/20231204/ ""),
[https://inspirehep.net/seminars/2170834](https://inspirehep.net/seminars/2170834 ""),
[https://parity.cosmodiscussion.com/](https://parity.cosmodiscussion.com/ "").
A variety of models were proposed which generate parity violation on cosmological scales (e. g. \[ [5](https://arxiv.org/html/2407.03397v1#bib.bib5 ""), [6](https://arxiv.org/html/2407.03397v1#bib.bib6 ""), [7](https://arxiv.org/html/2407.03397v1#bib.bib7 ""), [8](https://arxiv.org/html/2407.03397v1#bib.bib8 ""), [9](https://arxiv.org/html/2407.03397v1#bib.bib9 ""), [10](https://arxiv.org/html/2407.03397v1#bib.bib10 "")\] and references therein).

Report issue for preceding element

On the observational side, the situation has been puzzling.
Follow-up searches in \\acBOSS for specific parity-violating models of inflation produced null results \[ [11](https://arxiv.org/html/2407.03397v1#bib.bib11 "")\].
A re-analysis of \\acBOSS using a different set of mock catalogs shifted the detection significance of parity violation by around 2⁢σ2𝜎2\\sigma2 italic\_σ\[ [12](https://arxiv.org/html/2407.03397v1#bib.bib12 "")\], suggesting that the analysis may not be very robust to the choice of mocks.
In the \\acCMB, some analyses have found tentative evidence for parity violation (e. g. \[ [13](https://arxiv.org/html/2407.03397v1#bib.bib13 ""), [14](https://arxiv.org/html/2407.03397v1#bib.bib14 ""), [15](https://arxiv.org/html/2407.03397v1#bib.bib15 "")\] and references therein) whereas others have found null results \[ [16](https://arxiv.org/html/2407.03397v1#bib.bib16 "")\].

Report issue for preceding element

These follow-up studies may suggest that the original detection of parity violation is spurious.
On the other hand, no follow-up study has directly refuted the 7⁢σ7𝜎7\\sigma7 italic\_σ detection from \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\], so the current observational situation is unclear.
(It is also unclear how to interpret results from future datasets, e. g. the \\acDESI survey \[ [17](https://arxiv.org/html/2407.03397v1#bib.bib17 "")\], until the 7⁢σ7𝜎7\\sigma7 italic\_σ excess in \\acBOSS is diagnosed.)

Report issue for preceding element

One may ask, is there a statistical procedure which will unambiguously determine whether the 7⁢σ7𝜎7\\sigma7 italic\_σ detection of parity violation in \\acBOSS is spurious or not?
In this paper, we develop such a procedure.
We construct improved statistics (denoted χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT, χnull2subscriptsuperscript𝜒2null\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT) which separate the 7⁢σ7𝜎7\\sigma7 italic\_σ detection from \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\] into two contributions: a parity violation contribution, and a “data–mock mismatch” contribution which is nonzero if the _parity-even_\\ac8PCF of the data differs from the mock catalogs.

Report issue for preceding element

We apply these statistics to \\acBOSS data, and find that the parity violation signal is not statistically significant (significance varies between 00 to 2.5⁢σ2.5𝜎2.5\\sigma2.5 italic\_σ depending on analysis choices, see [figures5](https://arxiv.org/html/2407.03397v1#S4.F5 "In 4.4 The statistic 𝜒²ₙᵤₗₗ ‣ 4 The new statistics 𝜒²_× and 𝜒²ₙᵤₗₗ ‣ No evidence for parity violation in BOSS") and [6](https://arxiv.org/html/2407.03397v1#S4.F6 "Figure 6 ‣ 4.5 Combined NGC + SGC significance ‣ 4 The new statistics 𝜒²_× and 𝜒²ₙᵤₗₗ ‣ No evidence for parity violation in BOSS")), whereas the data–mock mismatch signal is ∼6⁢σsimilar-toabsent6𝜎\\sim 6\\sigma∼ 6 italic\_σ.
Our interpretation is that there is not compelling evidence for parity violation in \\acBOSS.

Report issue for preceding element

Our new statistics χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT, χnull2subscriptsuperscript𝜒2null\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT are conceptually simple, but the details are complicated, since algebraically messy objects arise, e. g. the parity-odd \\ac4PCF, [eq.3.3](https://arxiv.org/html/2407.03397v1#S3.E3 "In 3.1 The parity-odd four-point estimator ℰ̂_𝑎 ‣ 3 Reproducing results from [1, 2] ‣ No evidence for parity violation in BOSS"), and its analytic covariance ( [appendixA](https://arxiv.org/html/2407.03397v1#A1 "Appendix A Deriving the analytic covariance ‣ No evidence for parity violation in BOSS")).
In the rest of this extended introduction ( [sections1.2](https://arxiv.org/html/2407.03397v1#S1.SS2 "1.2 The 𝜒² statistic and the difficulty of modeling the 4PCF covariance ‣ 1 Introduction ‣ No evidence for parity violation in BOSS") to [1.3](https://arxiv.org/html/2407.03397v1#S1.SS3 "1.3 New statistics that distinguish parity violation and data–mock mismatch ‣ 1 Introduction ‣ No evidence for parity violation in BOSS")), we present the main results of the paper in streamlined form.
Details and derivations will be given in later sections ( [sections2](https://arxiv.org/html/2407.03397v1#S2 "2 BOSS data ‣ No evidence for parity violation in BOSS") to [5](https://arxiv.org/html/2407.03397v1#S5 "5 Discussion ‣ No evidence for parity violation in BOSS")).

Report issue for preceding element

### 1.2 The χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT statistic and the difficulty of modeling the 4PCF covariance

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2407.03397v1/x1.png)![Refer to caption](https://arxiv.org/html/2407.03397v1/x2.png)

Report issue for preceding elementFigure 1: Analysis of parity violation in the \\acBOSS \\acs\*CMASS-\\acs\*NGC dataset.
(Results for CMASSLOWZTOT-\\acs\*SGC are qualitatively similar and shown in [section4](https://arxiv.org/html/2407.03397v1#S4 "4 The new statistics 𝜒²_× and 𝜒²ₙᵤₗₗ ‣ No evidence for parity violation in BOSS").)
Left panel. When the χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT statistic defined in [eq.1.4](https://arxiv.org/html/2407.03397v1#S1.E4 "In 2nd item ‣ 1.2 The 𝜒² statistic and the difficulty of modeling the 4PCF covariance ‣ 1 Introduction ‣ No evidence for parity violation in BOSS") is evaluated on \\acBOSS data (dashed vertical line), the result is a ∼7⁢σsimilar-toabsent7𝜎\\sim 7\\sigma∼ 7 italic\_σ outlier relative to mock catalogs (solid histogram).
This reproduces the main result from \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\].
Right panel. We interpret this 7⁢σ7𝜎7\\sigma7 italic\_σ signal as a sum of parity violation and “data–mock mismatch” contributions ( [eq.1.7](https://arxiv.org/html/2407.03397v1#S1.E7 "In 1.3 New statistics that distinguish parity violation and data–mock mismatch ‣ 1 Introduction ‣ No evidence for parity violation in BOSS")).
If only χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT is used, these contributions are perfectly degenerate (red regions). The new statistics χ×2,χnull2subscriptsuperscript𝜒2subscriptsuperscript𝜒2null\\chi^{2}\_{\\times},\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT , italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT defined in [eqs.1.5](https://arxiv.org/html/2407.03397v1#S1.E5 "In 1.3 New statistics that distinguish parity violation and data–mock mismatch ‣ 1 Introduction ‣ No evidence for parity violation in BOSS") and [1.6](https://arxiv.org/html/2407.03397v1#S1.E6 "Equation 1.6 ‣ 1.3 New statistics that distinguish parity violation and data–mock mismatch ‣ 1 Introduction ‣ No evidence for parity violation in BOSS") break this degeneracy (blue regions).
We see that the parity violation signal drops to <2⁢σabsent2𝜎<2\\sigma< 2 italic\_σ, while the data-mismatch signal remains at high significance.
Throughout this panel, statistical errors are assumed Gaussian, with covariance estimated from mock catalogs.
Light/dark regions are 68%times68percent68\\text{\\,}\\mathrm{\\char 37\\relax}start\_ARG 68 end\_ARG start\_ARG times end\_ARG start\_ARG % end\_ARG and 95%times95percent95\\text{\\,}\\mathrm{\\char 37\\relax}start\_ARG 95 end\_ARG start\_ARG times end\_ARG start\_ARG % end\_ARG\\acfCL.Report issue for preceding element

\\acuse

CL

Report issue for preceding element

The analysis in \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 ""), [2](https://arxiv.org/html/2407.03397v1#bib.bib2 "")\] is based on a particular statistic applied to galaxy catalogs, denoted χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT and defined below, which is sensitive to parity violation.
Statistical significance is assigned by computing χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT on the \\acBOSS data, and comparing it to χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT values from an ensemble of \\acBOSS mock galaxy catalogs (as first proposed for the two-point correlation function in \[ [18](https://arxiv.org/html/2407.03397v1#bib.bib18 "")\], applied to the three-point function in \[ [19](https://arxiv.org/html/2407.03397v1#bib.bib19 "")\], and the parity-odd four-point function in \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\]).
Following \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 ""), [2](https://arxiv.org/html/2407.03397v1#bib.bib2 "")\], we have used the MultiDark-PATCHY \\acBOSS mock catalogs \[ [20](https://arxiv.org/html/2407.03397v1#bib.bib20 ""), [21](https://arxiv.org/html/2407.03397v1#bib.bib21 "")\] (or “PATCHY mocks” for short) throughout this paper.
We have reproduced the result from \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\] in the left panel of [figure1](https://arxiv.org/html/2407.03397v1#S1.F1 "In 1.2 The 𝜒² statistic and the difficulty of modeling the 4PCF covariance ‣ 1 Introduction ‣ No evidence for parity violation in BOSS").
We find that χdata2subscriptsuperscript𝜒2data\\chi^{2}\_{\\mathrm{data}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_data end\_POSTSUBSCRIPT is indeed a 7⁢σ7𝜎7\\sigma7 italic\_σ outlier, relative to a histogram of χmock2subscriptsuperscript𝜒2mock\\chi^{2}\_{\\mathrm{mock}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_mock end\_POSTSUBSCRIPT values.
Here are three possible interpretations of this 7⁢σ7𝜎7\\sigma7 italic\_σ result:

Report issue for preceding element

1. 1.


Parity-violating new physics: The spatial clustering of galaxies in the universe is not parity-invariant.

Report issue for preceding element

2. 2.


Parity-violating systematics:\\acBOSS has undiagnosed systematics which are not parity-invariant.

Report issue for preceding element

3. 3.


Data–mock mismatch: There is no evidence for parity violation (either physical or systematic) in \\acBOSS, but the mocks do not perfectly model the _parity-even_ higher N𝑁Nitalic\_N-point functions of the data.
(More precisely, if the parity-even \\ac8PCF of the mock catalogs differs from the data, then the mocks may underpredict the covariance of the \\ac4PCF, leading to a biased χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT.)333This possibility is emphasized throughout \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 ""), [2](https://arxiv.org/html/2407.03397v1#bib.bib2 "")\], where it is described as underestimating the covariance (or noise) of the statistic ℰ^asubscript^ℰ𝑎\\smash{\\widehat{\\mathcal{E}}\_{a}}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT (defined later in the paper).
E. g. the abstract of \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\] reads “Underestimation of the noise could also lead to a spurious detection”, and \[ [2](https://arxiv.org/html/2407.03397v1#bib.bib2 "")\] writes “A spurious detection of parity-violation could be caused by the simulations underestimating the true covariance”.
\[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\] estimated the impact of a wrong covariance matrix on the detection significance in their section 7.

Report issue for preceding element


To explore the “data–mock mismatch” possibility in more detail, we explain how χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT is defined.
The steps are (schematically):

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | (Galaxy catalog)→(Parity-odd \\ac4PCF ⁢ℰ^a)→(Parity-even \\ac8PCF ⁢χ2)→Galaxy catalogParity-odd \\ac4PCF subscript^ℰ𝑎→Parity-even \\ac8PCF superscript𝜒2\\Big{(}\\text{Galaxy catalog}\\Big{)}\\rightarrow\\Big{(}\\text{Parity-odd \\ac{4PCF%<br>} }\\widehat{\\mathcal{E}}\_{a}\\Big{)}\\rightarrow\\Big{(}\\text{Parity-even \\ac{8%<br>PCF} }\\chi^{2}\\Big{)}( Galaxy catalog ) → ( Parity-odd 4PCF over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT ) → ( Parity-even 8PCF italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT ) |  | (1.1) |

The new quantities ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT and (Cana)a⁢bsubscriptsubscript𝐶ana𝑎𝑏(C\_{\\mathrm{ana}})\_{ab}( italic\_C start\_POSTSUBSCRIPT roman\_ana end\_POSTSUBSCRIPT ) start\_POSTSUBSCRIPT italic\_a italic\_b end\_POSTSUBSCRIPT will be defined precisely later ( [section3](https://arxiv.org/html/2407.03397v1#S3 "3 Reproducing results from [1, 2] ‣ No evidence for parity violation in BOSS")).
In the introduction, the following qualitative descriptions of ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT and (Cana)a⁢bsubscriptsubscript𝐶ana𝑎𝑏(C\_{\\mathrm{ana}})\_{ab}( italic\_C start\_POSTSUBSCRIPT roman\_ana end\_POSTSUBSCRIPT ) start\_POSTSUBSCRIPT italic\_a italic\_b end\_POSTSUBSCRIPT will suffice:

Report issue for preceding element

- •


Each component a=1,…,Ndof𝑎1…subscript𝑁dofa=1,\\dots,N\_{\\mathrm{dof}}italic\_a = 1 , … , italic\_N start\_POSTSUBSCRIPT roman\_dof end\_POSTSUBSCRIPT of ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT is a parity-odd four-point function in the galaxy catalog.
“Parity-odd” means that if a spatial reflection is applied to the galaxy catalog, then ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT transforms as ℰ^a→−ℰ^a→subscript^ℰ𝑎subscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}\\rightarrow-\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT → - over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT.
This implies:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℰ¯a=0if the statistics of the galaxy field are parity-invariantsubscript¯ℰ𝑎0if the statistics of the galaxy field are parity-invariant\\bar{\\mathcal{E}}\_{a}=0\\hskip 42.67912pt\\text{if the statistics of the galaxy %<br>field are parity-invariant}over¯ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT = 0 if the statistics of the galaxy field are parity-invariant |  | (1.2) |



where ℰ¯asubscript¯ℰ𝑎\\bar{\\mathcal{E}}\_{a}over¯ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT denotes the true (i. e. cosmic average) parity-odd four-point function ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT.444In most of the paper, we denote the parity-odd four-point function ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT using a single index a=1,…,Ndof𝑎1…subscript𝑁dofa=1,\\dots,N\_{\\mathrm{dof}}italic\_a = 1 , … , italic\_N start\_POSTSUBSCRIPT roman\_dof end\_POSTSUBSCRIPT. However, the “natural” definition of ℰ^^ℰ\\widehat{\\mathcal{E}}over^ start\_ARG caligraphic\_E end\_ARG ( [section3.1](https://arxiv.org/html/2407.03397v1#S3.SS1 "3.1 The parity-odd four-point estimator ℰ̂_𝑎 ‣ 3 Reproducing results from [1, 2] ‣ No evidence for parity violation in BOSS")) is a six-index object ℰ^ℓ1⁢ℓ2⁢ℓ3β1⁢β2⁢β3subscriptsuperscript^ℰsubscript𝛽1subscript𝛽2subscript𝛽3subscriptℓ1subscriptℓ2subscriptℓ3\\smash{\\widehat{\\mathcal{E}}^{\\beta\_{1}\\beta\_{2}\\beta\_{3}}\_{\\ell\_{1}\\ell\_{2}%
\\ell\_{3}}}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUPERSCRIPT italic\_β start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT italic\_β start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT italic\_β start\_POSTSUBSCRIPT 3 end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_ℓ start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT roman\_ℓ start\_POSTSUBSCRIPT 3 end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT, where βisubscript𝛽𝑖\\beta\_{i}italic\_β start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT denotes a radial bin and 0≤li≤40subscript𝑙𝑖40\\leq l\_{i}\\leq 40 ≤ italic\_l start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ≤ 4 denotes an “angular momentum” (index of the spherical harmonics).
When we use the compressed notation ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT, each value of the “flattened” index a=1,…,Ndof𝑎1…subscript𝑁dofa=1,\\dots,N\_{\\mathrm{dof}}italic\_a = 1 , … , italic\_N start\_POSTSUBSCRIPT roman\_dof end\_POSTSUBSCRIPT represents a different six-tuple ((βi),(li))subscript𝛽𝑖subscript𝑙𝑖((\\beta\_{i}),(l\_{i}))( ( italic\_β start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) , ( italic\_l start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) ).
The number of components Ndofsubscript𝑁dofN\_{\\mathrm{dof}}italic\_N start\_POSTSUBSCRIPT roman\_dof end\_POSTSUBSCRIPT can be large.
In [figure1](https://arxiv.org/html/2407.03397v1#S1.F1 "In 1.2 The 𝜒² statistic and the difficulty of modeling the 4PCF covariance ‣ 1 Introduction ‣ No evidence for parity violation in BOSS"), we have used an “18-bin” setup with Ndof=18768subscript𝑁dof18768N\_{\\mathrm{dof}}=18768italic\_N start\_POSTSUBSCRIPT roman\_dof end\_POSTSUBSCRIPT = 18768.
See [section3.1](https://arxiv.org/html/2407.03397v1#S3.SS1 "3.1 The parity-odd four-point estimator ℰ̂_𝑎 ‣ 3 Reproducing results from [1, 2] ‣ No evidence for parity violation in BOSS") for details.

Report issue for preceding element

- •


The “analytic” covariance matrix (Cana)a⁢bsubscriptsubscript𝐶ana𝑎𝑏(C\_{\\mathrm{ana}})\_{ab}( italic\_C start\_POSTSUBSCRIPT roman\_ana end\_POSTSUBSCRIPT ) start\_POSTSUBSCRIPT italic\_a italic\_b end\_POSTSUBSCRIPT is the Ndofsubscript𝑁dofN\_{\\mathrm{dof}}italic\_N start\_POSTSUBSCRIPT roman\_dof end\_POSTSUBSCRIPT-by-Ndofsubscript𝑁dofN\_{\\mathrm{dof}}italic\_N start\_POSTSUBSCRIPT roman\_dof end\_POSTSUBSCRIPT matrix:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | (Cana)a⁢b=⟨ℰ^a⁢ℰ^b⟩assuming that the galaxy field δg is Gaussiansubscriptsubscript𝐶ana𝑎𝑏delimited-⟨⟩subscript^ℰ𝑎subscript^ℰ𝑏assuming that the galaxy field δg is Gaussian(C\_{\\mathrm{ana}})\_{ab}=\\big{\\langle}\\widehat{\\mathcal{E}}\_{a}\\widehat{%<br>\\mathcal{E}}\_{b}\\big{\\rangle}\\hskip 42.67912pt\\text{assuming that the galaxy %<br>field $\\delta\_{\\mathrm{g}}$ is Gaussian}( italic\_C start\_POSTSUBSCRIPT roman\_ana end\_POSTSUBSCRIPT ) start\_POSTSUBSCRIPT italic\_a italic\_b end\_POSTSUBSCRIPT = ⟨ over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_b end\_POSTSUBSCRIPT ⟩ assuming that the galaxy field italic\_δ start\_POSTSUBSCRIPT roman\_g end\_POSTSUBSCRIPT is Gaussian |  | (1.3) |



The assumption that δgsubscript𝛿g\\delta\_{\\mathrm{g}}italic\_δ start\_POSTSUBSCRIPT roman\_g end\_POSTSUBSCRIPT is Gaussian is not intended to be an accurate approximation.
It is only intended to give a calculable, well-motivated, invertible covariance matrix that can be used for data compression purposes when defining the χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT statistic:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | χ2≡ℰ^a⁢(Cana−1)a⁢b⁢ℰ^bsuperscript𝜒2subscript^ℰ𝑎superscriptsubscriptsuperscript𝐶1ana𝑎𝑏subscript^ℰ𝑏\\chi^{2}\\equiv\\widehat{\\mathcal{E}}\_{a}(C^{-1}\_{\\mathrm{ana}})^{ab}\\widehat{%<br>\\mathcal{E}}\_{b}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT ≡ over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT ( italic\_C start\_POSTSUPERSCRIPT - 1 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_ana end\_POSTSUBSCRIPT ) start\_POSTSUPERSCRIPT italic\_a italic\_b end\_POSTSUPERSCRIPT over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_b end\_POSTSUBSCRIPT |  | (1.4) |


Note that the definition ( [1.4](https://arxiv.org/html/2407.03397v1#S1.E4 "Equation 1.4 ‣ 2nd item ‣ 1.2 The 𝜒² statistic and the difficulty of modeling the 4PCF covariance ‣ 1 Introduction ‣ No evidence for parity violation in BOSS")) of χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT involves squaring the parity-odd \\ac4PCF ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT.
Therefore, χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT is a parity-even eight-point statistic, whereas ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT is a parity-odd four-point statistic.
This makes the χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT statistic more fragile: it can be biased by parity-even effects
(whereas many observational systematics cannot generate a parity-odd signal).
In particular, if the parity-even \\ac8PCF of the mock catalogs does not agree with the data (“data–mock mismatch”), then there is no symmetry which protects the χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT statistic from bias.
Quantitatively, a ∼20%similar-toabsenttimes20percent\\sim$20\\text{\\,}\\mathrm{\\char 37\\relax}$∼ start\_ARG 20 end\_ARG start\_ARG times end\_ARG start\_ARG % end\_ARG discrepancy between the parity-even \\ac8PCF of the mocks and data would explain the results of \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 ""), [2](https://arxiv.org/html/2407.03397v1#bib.bib2 "")\] without parity violation (either cosmological or systematic).

Report issue for preceding element

A priori, a ∼20%similar-toabsenttimes20percent\\sim$20\\text{\\,}\\mathrm{\\char 37\\relax}$∼ start\_ARG 20 end\_ARG start\_ARG times end\_ARG start\_ARG % end\_ARG\\ac8PCF discrepancy between mocks and data is entirely plausible.
The PATCHY mocks include free parameters (mostly pertaining to the galaxy–halo relation) which are adjusted so that the \\ac2PCF of the mocks agrees with the data.
The mocks are not intended to model higher-point correlation functions precisely.555This is a natural consequence of the fact that \\acLSS analyses have focused on the two-point function, and the massive catalogs of mocks necessary for this analysis have only been created for analyses of the large-scale power spectrum and correlation function.
Large simulation suites devoted to higher-point statistics have only recently become available (e. g. Quijote \[ [22](https://arxiv.org/html/2407.03397v1#bib.bib22 "")\]) and have not generally been used to create mocks for the \\acBOSS survey, partially because the 1h−1Gpctimes1timeshHubble1gigapc1\\text{\\,}{\\mathrm{\\mathnormal{h}}}^{-1}\\text{\\,}\\mathrm{Gpc}start\_ARG 1 end\_ARG start\_ARG times end\_ARG start\_ARG start\_ARG power start\_ARG italic\_h end\_ARG start\_ARG - 1 end\_ARG end\_ARG start\_ARG times end\_ARG start\_ARG roman\_Gpc end\_ARG end\_ARG boxes are smaller than the \\acBOSS survey volume.
Indeed, the \\ac3PCF of the PATCHY mocks generally agrees with the data \[ [23](https://arxiv.org/html/2407.03397v1#bib.bib23 ""), [20](https://arxiv.org/html/2407.03397v1#bib.bib20 "")\], but has some discrepancies \[ [21](https://arxiv.org/html/2407.03397v1#bib.bib21 "")\].
In section 4.2.3 of \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\] it is reported that the parity-even \\acp4PCF disagree at 4.9⁢σ4.9𝜎4.9\\sigma4.9 italic\_σ (for some choices of binning).
Generally speaking, higher-point functions are sensitive to tails of distributions, and can magnify small modeling issues.
Therefore, it seems completely plausible that the \\acp8PCF of the mocks and data could disagree by ∼20%similar-toabsenttimes20percent\\sim$20\\text{\\,}\\mathrm{\\char 37\\relax}$∼ start\_ARG 20 end\_ARG start\_ARG times end\_ARG start\_ARG % end\_ARG.

Report issue for preceding element

(As an aside, squaring ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT seems to be necessary in an analysis where no model of the parity-odd \\ac4PCF is assumed. On the other hand, if a model for ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT is assumed, then the optimal statistic is linear in ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT, and \\ac8PCF bias is not an issue. This may explain why model-based analyses have produced null results so far \[ [11](https://arxiv.org/html/2407.03397v1#bib.bib11 "")\].)

Report issue for preceding element

### 1.3 New statistics that distinguish parity violation and data–mock mismatch

Report issue for preceding element

Now we can present the main idea of this paper.
So far, we have proposed data–mock mismatch as a possible explanation for the 7⁢σ7𝜎7\\sigma7 italic\_σ signal in [figure1](https://arxiv.org/html/2407.03397v1#S1.F1 "In 1.2 The 𝜒² statistic and the difficulty of modeling the 4PCF covariance ‣ 1 Introduction ‣ No evidence for parity violation in BOSS") (left panel), but we have not presented evidence for or against this possibility.
We will now construct new statistics, denoted χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT and χnull2subscriptsuperscript𝜒2null\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT, which cleanly separate parity violation from data–mock mismatch.

Report issue for preceding element

Our construction is based on the following simple idea.
If χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT excess is due to parity violation, then the true parity-odd four-point function ℰ¯asubscript¯ℰ𝑎\\bar{\\mathcal{E}}\_{a}over¯ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT of the universe is nonzero.
In this case, we should see the same (within statistical errors) parity-odd four-point function ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT in different parts of the sky.
On the other hand, if the χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT excess is due to data–mock mismatch, then ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT has mean zero, but the mocks underestimate the covariance ⟨ℰ^a⁢ℰ^b⟩delimited-⟨⟩subscript^ℰ𝑎subscript^ℰ𝑏\\langle\\widehat{\\mathcal{E}}\_{a}\\widehat{\\mathcal{E}}\_{b}\\rangle⟨ over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_b end\_POSTSUBSCRIPT ⟩.
In this case, we should see uncorrelated (within statistical errors) parity-odd four-point functions ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT in different parts of the sky.

Report issue for preceding element

To make this idea precise, we start by splitting the \\acBOSS survey area into Npsubscript𝑁𝑝N\_{p}italic\_N start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT patches of roughly equal area, where Np=3subscript𝑁𝑝3N\_{p}=3italic\_N start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT = 3 for the \\acBOSS \\acCMASS \\acNGC dataset, denoted as \\acCMASS-\\acNGC (which we focus on in this introduction), and Np=2subscript𝑁𝑝2N\_{p}=2italic\_N start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT = 2 for the CMASSLOWZTOT \\acSGC dataset, denoted as CMASSLOWZTOT-\\acSGC.666We explain in [section2.2](https://arxiv.org/html/2407.03397v1#S2.SS2 "2.2 Sample definition: CMASS vs. CMASSLOWZTOT ‣ 2 BOSS data ‣ No evidence for parity violation in BOSS") why we consider two different samples in the northern and southern galactic caps.
We separate patches by gaps of 5–10 degrees, to make the patches approximately statistically independent.
The patches are shown in [section4.1](https://arxiv.org/html/2407.03397v1#S4.SS1 "4.1 Splitting BOSS into patches ‣ 4 The new statistics 𝜒²_× and 𝜒²ₙᵤₗₗ ‣ No evidence for parity violation in BOSS") and [figure3](https://arxiv.org/html/2407.03397v1#S4.F3 "In 4.1 Splitting BOSS into patches ‣ 4 The new statistics 𝜒²_× and 𝜒²ₙᵤₗₗ ‣ No evidence for parity violation in BOSS").

Report issue for preceding element

We estimate the parity-odd \\ac4PCF independently in each patch μ=1,⋯,Np𝜇1⋯subscript𝑁𝑝\\mu=1,\\cdots,N\_{p}italic\_μ = 1 , ⋯ , italic\_N start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT, and denote the result by ℰ^aμsuperscriptsubscript^ℰ𝑎𝜇\\widehat{\\mathcal{E}}\_{a}^{\\mu}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_μ end\_POSTSUPERSCRIPT, now with an extra index μ𝜇\\muitalic\_μ. We then define new statistics:

Report issue for preceding element

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|  | χ×2subscriptsuperscript𝜒2\\displaystyle\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT | ∝∑μ≠νℰ^aμ⁢(Cana−1)a⁢b⁢ℰ^bνproportional-toabsentsubscript𝜇𝜈superscriptsubscript^ℰ𝑎𝜇superscriptsuperscriptsubscript𝐶ana1𝑎𝑏superscriptsubscript^ℰ𝑏𝜈\\displaystyle\\propto\\sum\_{\\mu\\neq\\nu}\\widehat{\\mathcal{E}}\_{a}^{\\mu}(C\_{%<br>\\mathrm{ana}}^{-1})^{ab}\\widehat{\\mathcal{E}}\_{b}^{\\nu}∝ ∑ start\_POSTSUBSCRIPT italic\_μ ≠ italic\_ν end\_POSTSUBSCRIPT over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_μ end\_POSTSUPERSCRIPT ( italic\_C start\_POSTSUBSCRIPT roman\_ana end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT - 1 end\_POSTSUPERSCRIPT ) start\_POSTSUPERSCRIPT italic\_a italic\_b end\_POSTSUPERSCRIPT over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_b end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_ν end\_POSTSUPERSCRIPT |  | (1.5) |
|  | χnull2subscriptsuperscript𝜒2null\\displaystyle\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT | ∝∑μ≠ν(ℰ^aμ−ℰ^aν)⁢(Cana−1)a⁢b⁢(ℰ^bμ−ℰ^bν)proportional-toabsentsubscript𝜇𝜈superscriptsubscript^ℰ𝑎𝜇superscriptsubscript^ℰ𝑎𝜈superscriptsuperscriptsubscript𝐶ana1𝑎𝑏superscriptsubscript^ℰ𝑏𝜇superscriptsubscript^ℰ𝑏𝜈\\displaystyle\\propto\\sum\_{\\mu\\neq\\nu}\\big{(}\\widehat{\\mathcal{E}}\_{a}^{\\mu}-%<br>\\widehat{\\mathcal{E}}\_{a}^{\\nu}\\big{)}(C\_{\\mathrm{ana}}^{-1})^{ab}\\big{(}%<br>\\widehat{\\mathcal{E}}\_{b}^{\\mu}-\\widehat{\\mathcal{E}}\_{b}^{\\nu}\\big{)}∝ ∑ start\_POSTSUBSCRIPT italic\_μ ≠ italic\_ν end\_POSTSUBSCRIPT ( over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_μ end\_POSTSUPERSCRIPT - over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_ν end\_POSTSUPERSCRIPT ) ( italic\_C start\_POSTSUBSCRIPT roman\_ana end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT - 1 end\_POSTSUPERSCRIPT ) start\_POSTSUPERSCRIPT italic\_a italic\_b end\_POSTSUPERSCRIPT ( over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_b end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_μ end\_POSTSUPERSCRIPT - over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_b end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_ν end\_POSTSUPERSCRIPT ) |  | (1.6) |

(The overall normalizations of χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT and χnull2subscriptsuperscript𝜒2null\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT will be defined in [section4](https://arxiv.org/html/2407.03397v1#S4 "4 The new statistics 𝜒²_× and 𝜒²ₙᵤₗₗ ‣ No evidence for parity violation in BOSS").)
At an intuitive level, we expect that χ×2superscriptsubscript𝜒2\\chi\_{\\times}^{2}italic\_χ start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT will only be sensitive to parity violation, and χnull2subscriptsuperscript𝜒2null\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT will only be sensitive to data–mock mismatch, by the following argument:

Report issue for preceding element

- •


The χ×2superscriptsubscript𝜒2\\chi\_{\\times}^{2}italic\_χ start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT statistic measures correlations between parity-odd four-point functions ℰ^aμsuperscriptsubscript^ℰ𝑎𝜇\\widehat{\\mathcal{E}}\_{a}^{\\mu}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_μ end\_POSTSUPERSCRIPT in different (μ≠ν𝜇𝜈\\mu\\neq\\nuitalic\_μ ≠ italic\_ν) patches of sky.
Such correlations do not acquire expectation values from data–mock mismatch (which acts as “noise” that is uncorrelated between well-separated patches).
On the other hand, if parity is violated, then ℰ¯asubscript¯ℰ𝑎\\bar{\\mathcal{E}}\_{a}over¯ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT is the same in all patches, leading to a nonzero expectation value ⟨χ×2⟩∝ℰ¯a⁢(Cana−1)a⁢b⁢ℰ¯bproportional-todelimited-⟨⟩subscriptsuperscript𝜒2subscript¯ℰ𝑎superscriptsubscriptsuperscript𝐶1ana𝑎𝑏subscript¯ℰ𝑏\\langle\\chi^{2}\_{\\times}\\rangle\\propto\\bar{\\mathcal{E}}\_{a}(C^{-1}\_{\\mathrm{%
ana}})^{ab}\\bar{\\mathcal{E}}\_{b}⟨ italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT ⟩ ∝ over¯ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT ( italic\_C start\_POSTSUPERSCRIPT - 1 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_ana end\_POSTSUBSCRIPT ) start\_POSTSUPERSCRIPT italic\_a italic\_b end\_POSTSUPERSCRIPT over¯ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_b end\_POSTSUBSCRIPT.

Report issue for preceding element

- •


The χnull2subscriptsuperscript𝜒2null\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT statistic defines a null test: it measures consistency between four-point functions in different parts of the sky.
Parity violation does not contribute to χnull2subscriptsuperscript𝜒2null\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT, since we still expect consistent values of ℰ¯asubscript¯ℰ𝑎\\bar{\\mathcal{E}}\_{a}over¯ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT in different parts of the sky.
However, systematics or data–mock mismatch will add “noise” to ℰ^asubscript^ℰ𝑎\\widehat{\\mathcal{E}}\_{a}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT, which does contribute to χnull2subscriptsuperscript𝜒2null\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT.

Report issue for preceding element


More formally, in [section4](https://arxiv.org/html/2407.03397v1#S4 "4 The new statistics 𝜒²_× and 𝜒²ₙᵤₗₗ ‣ No evidence for parity violation in BOSS") we will show that the new statistics χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT and χnull2subscriptsuperscript𝜒2null\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT separate parity violation and data–mock mismatch, in the following precise sense.
Going back to the original χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT statistic in [eq.1.4](https://arxiv.org/html/2407.03397v1#S1.E4 "In 2nd item ‣ 1.2 The 𝜒² statistic and the difficulty of modeling the 4PCF covariance ‣ 1 Introduction ‣ No evidence for parity violation in BOSS"), we calculate the expectation value ⟨χ2⟩delimited-⟨⟩superscript𝜒2\\langle\\chi^{2}\\rangle⟨ italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT ⟩ relative to mocks, and find two terms:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |

[... middle omitted — see footer ...]

These are different null tests, and may succeed or fail independently of each other.
We expect that χnull2subscriptsuperscript𝜒2null\\chi^{2}\_{\\mathrm{null}}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT roman\_null end\_POSTSUBSCRIPT is more sensitive to covariance mismatch (Cdata≠Cmock)subscript𝐶datasubscript𝐶mock(C\_{\\mathrm{data}}\\neq C\_{\\mathrm{mock}})( italic\_C start\_POSTSUBSCRIPT roman\_data end\_POSTSUBSCRIPT ≠ italic\_C start\_POSTSUBSCRIPT roman\_mock end\_POSTSUBSCRIPT ), whereas the patch-based tests from \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 ""), [2](https://arxiv.org/html/2407.03397v1#bib.bib2 "")\] is more sensitive to systematics which break statistical isotropy.

Report issue for preceding element

### E.3 The rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT-statistic (correlating NGC and SGC)

Report issue for preceding element

In section 5.2 of \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\], there is a statistic rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT which is very closely related to our statistic χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT.
The rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT-statistic is defined for a survey with Np=2subscript𝑁𝑝2N\_{p}=2italic\_N start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT = 2 patches.
In \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\], the patches are chosen to be the \\acNGC and \\acSGC.
To define rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT, it will be convenient to diagonalize Cana=RT⁢Λ⁢Rsubscript𝐶anasuperscript𝑅𝑇Λ𝑅C\_{\\mathrm{ana}}=R^{T}\\Lambda Ritalic\_C start\_POSTSUBSCRIPT roman\_ana end\_POSTSUBSCRIPT = italic\_R start\_POSTSUPERSCRIPT italic\_T end\_POSTSUPERSCRIPT roman\_Λ italic\_R, and change variables from ℰ^aμsuperscriptsubscript^ℰ𝑎𝜇\\widehat{\\mathcal{E}}\_{a}^{\\mu}over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_μ end\_POSTSUPERSCRIPT to the length-Ndofsubscript𝑁dofN\_{\\mathrm{dof}}italic\_N start\_POSTSUBSCRIPT roman\_dof end\_POSTSUBSCRIPT “data vector” daμsuperscriptsubscript𝑑𝑎𝜇d\_{a}^{\\mu}italic\_d start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_μ end\_POSTSUPERSCRIPT defined by:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | daμ=(Λ−1/2⁢R)a⁢b⁢ℰ^bμsuperscriptsubscript𝑑𝑎𝜇subscriptsuperscriptΛ12𝑅𝑎𝑏superscriptsubscript^ℰ𝑏𝜇d\_{a}^{\\mu}=(\\Lambda^{-1/2}R)\_{ab}\\,\\widehat{\\mathcal{E}}\_{b}^{\\mu}italic\_d start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_μ end\_POSTSUPERSCRIPT = ( roman\_Λ start\_POSTSUPERSCRIPT - 1 / 2 end\_POSTSUPERSCRIPT italic\_R ) start\_POSTSUBSCRIPT italic\_a italic\_b end\_POSTSUBSCRIPT over^ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_b end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_μ end\_POSTSUPERSCRIPT |  | (E.1) |

Then rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT is defined to be the correlation coefficient between the data vectors da(1)superscriptsubscript𝑑𝑎1d\_{a}^{(1)}italic\_d start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( 1 ) end\_POSTSUPERSCRIPT, da(2)superscriptsubscript𝑑𝑎2d\_{a}^{(2)}italic\_d start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( 2 ) end\_POSTSUPERSCRIPT:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | rp≡∑a(da(1)−d¯(1))⁢(da(2)−d¯(2))(∑a(da(1)−d¯(1))2)⁢(∑b(db(2)−d¯(2))2)where ⁢d¯(i)≡1Ndof⁢∑i=1Ndofda(i)formulae-sequencesubscript𝑟𝑝subscript𝑎superscriptsubscript𝑑𝑎1superscript¯𝑑1superscriptsubscript𝑑𝑎2superscript¯𝑑2subscript𝑎superscriptsuperscriptsubscript𝑑𝑎1superscript¯𝑑12subscript𝑏superscriptsuperscriptsubscript𝑑𝑏2superscript¯𝑑22where superscript¯𝑑𝑖1subscript𝑁dofsuperscriptsubscript𝑖1subscript𝑁dofsubscriptsuperscript𝑑𝑖𝑎r\_{p}\\equiv\\frac{\\sum\_{a}(d\_{a}^{(1)}-\\bar{d}^{(1)})(d\_{a}^{(2)}-\\bar{d}^{(2)}%<br>)}{\\sqrt{\\big{(}\\sum\_{a}(d\_{a}^{(1)}-\\bar{d}^{(1)})^{2}\\big{)}\\big{(}\\sum\_{b}(%<br>d\_{b}^{(2)}-\\bar{d}^{(2)})^{2}\\big{)}}}\\hskip 28.45274pt\\mbox{where }\\bar{d}^{%<br>(i)}\\equiv\\frac{1}{N\_{\\mathrm{dof}}}\\sum\_{i=1}^{N\_{\\mathrm{dof}}}d^{(i)}\_{a}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT ≡ divide start\_ARG ∑ start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT ( italic\_d start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( 1 ) end\_POSTSUPERSCRIPT - over¯ start\_ARG italic\_d end\_ARG start\_POSTSUPERSCRIPT ( 1 ) end\_POSTSUPERSCRIPT ) ( italic\_d start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( 2 ) end\_POSTSUPERSCRIPT - over¯ start\_ARG italic\_d end\_ARG start\_POSTSUPERSCRIPT ( 2 ) end\_POSTSUPERSCRIPT ) end\_ARG start\_ARG square-root start\_ARG ( ∑ start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT ( italic\_d start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( 1 ) end\_POSTSUPERSCRIPT - over¯ start\_ARG italic\_d end\_ARG start\_POSTSUPERSCRIPT ( 1 ) end\_POSTSUPERSCRIPT ) start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT ) ( ∑ start\_POSTSUBSCRIPT italic\_b end\_POSTSUBSCRIPT ( italic\_d start\_POSTSUBSCRIPT italic\_b end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( 2 ) end\_POSTSUPERSCRIPT - over¯ start\_ARG italic\_d end\_ARG start\_POSTSUPERSCRIPT ( 2 ) end\_POSTSUPERSCRIPT ) start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT ) end\_ARG end\_ARG where over¯ start\_ARG italic\_d end\_ARG start\_POSTSUPERSCRIPT ( italic\_i ) end\_POSTSUPERSCRIPT ≡ divide start\_ARG 1 end\_ARG start\_ARG italic\_N start\_POSTSUBSCRIPT roman\_dof end\_POSTSUBSCRIPT end\_ARG ∑ start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_N start\_POSTSUBSCRIPT roman\_dof end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT italic\_d start\_POSTSUPERSCRIPT ( italic\_i ) end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT |  | (E.2) |

In \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\], the statistic rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT is found to be statistically consistent with zero, but section 5.2 of \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\] argues that this _does not_ rule out parity violation.
On the other hand, in this paper, we find that χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT is statistically consistent with zero, but we show that this _does_ rule out parity violation.
One may wonder how these statements can be consistent, since the statistics χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT and rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT are so conceptually similar.

Report issue for preceding element

To answer this question, we first note that our χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT statistic can be written in “data vector” notation as follows:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | χ×2=∑ada(1)⁢da(2)subscriptsuperscript𝜒2subscript𝑎superscriptsubscript𝑑𝑎1superscriptsubscript𝑑𝑎2\\chi^{2}\_{\\times}=\\sum\_{a}d\_{a}^{(1)}d\_{a}^{(2)}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT = ∑ start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT italic\_d start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( 1 ) end\_POSTSUPERSCRIPT italic\_d start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( 2 ) end\_POSTSUPERSCRIPT |  | (E.3) |

Comparing [eqs.E.2](https://arxiv.org/html/2407.03397v1#A5.E2 "In E.3 The 𝑟_𝑝-statistic (correlating NGC and SGC) ‣ Appendix E Comments on related null tests from [1, 2] ‣ No evidence for parity violation in BOSS") and [E.3](https://arxiv.org/html/2407.03397v1#A5.E3 "Equation E.3 ‣ E.3 The 𝑟_𝑝-statistic (correlating NGC and SGC) ‣ Appendix E Comments on related null tests from [1, 2] ‣ No evidence for parity violation in BOSS"), we see that the rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT-statistic differs from χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT in two ways: rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT is defined with d¯¯𝑑\\bar{d}over¯ start\_ARG italic\_d end\_ARG-subtraction, and rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT is defined with a denominator which ensures rp∈\[−1,1\]subscript𝑟𝑝11r\_{p}\\in\[-1,1\]italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT ∈ \[ - 1 , 1 \].

Report issue for preceding element

The denominator of [eq.E.2](https://arxiv.org/html/2407.03397v1#A5.E2 "In E.3 The 𝑟_𝑝-statistic (correlating NGC and SGC) ‣ Appendix E Comments on related null tests from [1, 2] ‣ No evidence for parity violation in BOSS") is not important (as far as we can tell), but the d¯¯𝑑\\bar{d}over¯ start\_ARG italic\_d end\_ARG-subtraction in the numerator has an important consequence.
Consider the following toy model of parity violation:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | ⟨daμ⟩=C(where C is a constant independent of a,μ)delimited-⟨⟩superscriptsubscript𝑑𝑎𝜇𝐶where C is a constant independent of a,μ\\big{\\langle}d\_{a}^{\\mu}\\big{\\rangle}=C\\hskip 28.45274pt(\\text{where $C$ is a %<br>constant independent of $a,\\mu$})⟨ italic\_d start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_μ end\_POSTSUPERSCRIPT ⟩ = italic\_C ( where italic\_C is a constant independent of italic\_a , italic\_μ ) |  | (E.4) |

In this toy model, the statistic χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT is sensitive to the value of C𝐶Citalic\_C, but the statistic rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT is not sensitive to C𝐶Citalic\_C because of the d¯¯𝑑\\bar{d}over¯ start\_ARG italic\_d end\_ARG-subtraction in the definition ( [E.2](https://arxiv.org/html/2407.03397v1#A5.E2 "Equation E.2 ‣ E.3 The 𝑟_𝑝-statistic (correlating NGC and SGC) ‣ Appendix E Comments on related null tests from [1, 2] ‣ No evidence for parity violation in BOSS")).

Report issue for preceding element

This toy model shows that it is possible for parity violation to make a large contribution to χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT, but a small (or even zero) contribution to rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT.
For this reason, \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\] concluded that a small value of rpsubscript𝑟𝑝r\_{p}italic\_r start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT is inconclusive, and does not rule out parity violation.
(The argument in section 5.2 of \[ [1](https://arxiv.org/html/2407.03397v1#bib.bib1 "")\] is based on a different toy model than ( [E.4](https://arxiv.org/html/2407.03397v1#A5.E4 "Equation E.4 ‣ E.3 The 𝑟_𝑝-statistic (correlating NGC and SGC) ‣ Appendix E Comments on related null tests from [1, 2] ‣ No evidence for parity violation in BOSS")), but the principle is the same.)

Report issue for preceding element

This issue does not arise for the χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT statistic, which is defined without d¯¯𝑑\\bar{d}over¯ start\_ARG italic\_d end\_ARG-subtraction ( [eq.E.3](https://arxiv.org/html/2407.03397v1#A5.E3 "In E.3 The 𝑟_𝑝-statistic (correlating NGC and SGC) ‣ Appendix E Comments on related null tests from [1, 2] ‣ No evidence for parity violation in BOSS")).
If parity violation makes a statistically significant contribution to χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT, then it must also make a statistically significant contribution to χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT.
This follows formally from [eqs.4.9](https://arxiv.org/html/2407.03397v1#S4.E9 "In 4.2 Definitions and notation ‣ 4 The new statistics 𝜒²_× and 𝜒²ₙᵤₗₗ ‣ No evidence for parity violation in BOSS") and [4.13](https://arxiv.org/html/2407.03397v1#S4.E13 "Equation 4.13 ‣ 4.3 The statistic 𝜒²_× ‣ 4 The new statistics 𝜒²_× and 𝜒²ₙᵤₗₗ ‣ No evidence for parity violation in BOSS"), which show that the statistics χ2superscript𝜒2\\chi^{2}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT and χ×2subscriptsuperscript𝜒2\\chi^{2}\_{\\times}italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT have the same expectation value ℰ¯a⁢(Cana−1)a⁢b⁢ℰ¯bsubscript¯ℰ𝑎superscriptsuperscriptsubscript𝐶ana1𝑎𝑏subscript¯ℰ𝑏\\smash{\\bar{\\mathcal{E}}\_{a}\\big{(}C\_{\\mathrm{ana}}^{-1}\\big{)}^{ab}\\bar{%
\\mathcal{E}}\_{b}}over¯ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_a end\_POSTSUBSCRIPT ( italic\_C start\_POSTSUBSCRIPT roman\_ana end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT - 1 end\_POSTSUPERSCRIPT ) start\_POSTSUPERSCRIPT italic\_a italic\_b end\_POSTSUPERSCRIPT over¯ start\_ARG caligraphic\_E end\_ARG start\_POSTSUBSCRIPT italic\_b end\_POSTSUBSCRIPT due to parity violation, plus the statement that Var⁢(χ×2)≲Var⁢(χ2)less-than-or-similar-toVarsubscriptsuperscript𝜒2Varsuperscript𝜒2\\mathrm{Var}(\\chi^{2}\_{\\times})\\lesssim\\mathrm{Var}(\\chi^{2})roman\_Var ( italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT × end\_POSTSUBSCRIPT ) ≲ roman\_Var ( italic\_χ start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT ).
(See [appendixB](https://arxiv.org/html/2407.03397v1#A2 "Appendix B Why is Var⁢(𝜒²_×) smaller than Var⁢(𝜒²)? ‣ No evidence for parity violation in BOSS") for more discussion of this latter statement.)

Report issue for preceding element

Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)

──────── [TRUNCATED] ────────
Showing 44,392 chars (head) + 14,716 chars (tail) of 553,100 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-fd0f3cbbca.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-fd0f3cbbca.md" offset=320 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
