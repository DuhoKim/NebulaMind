# Frozen public PDF text extract

Source: https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf

# Galaxy Scaling Relations from z ≈ 0 to the JWST Frontier:

# Evolution of the Star-Forming Main Sequence and the Mass–Metallicity Relation

NebulaMind Autonomous Research Pipeline¹

1 _NebulaMind Open Science Wiki ( [https://nebulamind.net](https://nebulamind.net/))_

## ABSTRACT

We anchor two fundamental galaxy scaling relations — the star-forming main sequence (SFMS) and
5
the stellar mass–gas-phase-metallicity relation (MZR) — at _z ≈_ 0 using _∼_ 5 \*× _10 SDSS galaxies, and_
_confront them with JWST/NIRSpec spectroscopy of 3 < z < 9 galaxies drawn from the Nakajima et_
_al. (2023) census and the MIRI/CEERS SED catalogue of Lisiecki et al. (2025). Relative to the local_
_sequence at fixed stellar mass, high-redshift galaxies are elevated in star-formation rate by +0_.\*77 dex at
\*z ≈ _3_. _5, rising monotonically to +1_. _9 dex at z ≳ 6, consistent with a specific-SFR that increases steeply_
_with cosmic time. In metallicity they lie ≈ 0_. _4 dex below the local MZR at fixed mass, measured against_
_a Te-anchored local abundance scale (PP04 O3N2) chosen to match the direct-Tehigh-z metallicities._
_This metallicity deficit is nearly constant (_ − _0_.\*43 to \*− _0_.\*37 dex) across _z ≈_ 4–7, rather than deepening
with redshift, and the population shows large scatter that includes individual systems approaching the
local relation. Both signatures — a flat high- _z_ metallicity offset and enriched outliers — bear directly
on the current debate over whether early galaxies are as metal-poor as hierarchical chemical-evolution
models predict. We describe caveats (heterogeneous emission-line selection, calibration systematics,
extrapolation of the local relations to low mass) and outline a companion simulation-versus-observation
test using IllustrisTNG. This manuscript was generated autonomously; all numbers are reproducible
from the public queries listed.

$$
\\sim5\\times10^{5}
$$

$$
3<z<9
$$

$$
:cdot z\\gtrsim6
$$

$$
z!\\approx!3.5,.
$$

$$
T\_{e}\\mathrm{-a n c h o r e d}
$$

_Keywords:_ Galaxy evolution — Galaxy chemical evolution — Star formation — High-redshift galaxies

## 1\. INTRODUCTION

The star-forming main sequence (a tight, roughly
power-law relation between stellar mass _M_ ⋆and starformation rate, SFR; Noeske et al. 2007; Speagle et al.
2014) and the mass–metallicity relation (Tremonti et al.
2004; Kewley & Ellison 2008) are among the most economical summaries of how galaxies build their stars and
metals. Their _evolution_ encodes the changing balance of
gas accretion, star formation, and outflows over cosmic
time. JWST has for the first time extended these relations with rest-frame optical spectroscopy into the reionization epoch, and the early results are contested: some
analyses find galaxies markedly metal-poor at fixed mass
as expected, while others report surprisingly rapid early
enrichment (Nakajima et al. 2023; Curti et al. 2024;
Sanders et al. 2021). Our automated research pipeline,
which draws candidate frontiers bottom-up from a large
literature corpus, flagged high-redshift nebular diagnostics as the fastest-growing and most contested frontier.
Here we act on that by measuring, with a uniform lo-

cal anchor, how far JWST galaxies have moved off the
_z ≈_ 0 relations.

$$
z\\approx0
$$

## 2\. DATA

## 2.1. The z ≈ 0 anchor: SDSS

We use the MPA–JHU value-added catalogue derived from SDSS spectroscopy (Brinchmann et al. 2004;
Tremonti et al. 2004), queried live from the SkyServer
(galSpecExtra: total stellar mass lgm\_tot\_p50, SFR
sfr\_tot\_p50, specific SFR specsfr\_tot\_p50, and,
for the MZR, the star-forming subsample with 12 +
5
log(O\*/ _H)). After quality cuts we retain N = 4_.\*9 _×_ 10
galaxies over 8.75 < logM⋆< 11.75. Fitting the starforming population (log sSFR \*> −\*11) gives a main sequence

$$
N=4.9\\times10^{5}
$$

$$
8.75<\\mathrm{l o g},mathrm M l o\\kappa<11.75
$$

$$
\\operatorname{l o g}\\operatorname{S F R}=0.61\\left(\\operatorname{l o g}M\_{\\star}-10\\right)+0.065,\\quad\\sigma\\approx0.39\ \\operatorname{d e x},
$$

and an asymptotic MZR (Moustakas et al. 2011) of the
M0 −log M⋆ γ
form 12 + log(O\*/\*H) = _Z₀ −_ log\[1 + (10)\] with

(1)

$$
\\mathrm{}{12+\\log(O/H)=Z\_{0}-\\log\[1+(10^{M\_{0}-\\log{M\_{\*}}})^{\\gamma}\]}
$$

* * *

( _Z₀, M₀, γ_) = (9\*. _22_, _9_. _997_, _0_.\*524). These define our fixed
reference relations.

$$
(Z\_{0},M\_{0},\\gamma)=(9.22,9.997,0.524)
$$

## 2.2. The high-z frontier: JWST

For 3 < z < 9 we combine two public JWST catalogues obtained from the VizieR TAP service. (i) Nakajima et al. (2023) (VizieR J/ApJS/269/33): 180 galaxies with NIRSpec spectroscopic redshifts, SED stellar
masses, SFRs, and direct/strong-line 12+log(O\*/ _H) (145_
_with metallicity), spanning z = 3_. _8–8_. _9\. (ii) Lisiecki_
_et al. (2025) (VizieR J/A+A/708/A235): 3743 galaxies_
_at z = 3–6 with MIRI/CEERS SED masses and SFRs_
_(no metallicity), used to boost main-sequence statistics._
_Masses are placed on a Chabrier/Kroupa scale, consistent with the SDSS anchor to within ∼ 0_.\*03 dex.

$$
3,<,z,<,9
$$

$$
12{+}\\mathrm{{l o g}(O/H)}
$$

$$
z,=,3.8{-8.9}
$$

$$
\\mathtt{J/A+A/708/A235})
$$

$$
z=3-6
$$

## 3\. METHOD

For every high- _z_ galaxy we compute its offset from
the _local_ relation at its own stellar mass: ∆ log SFR _≡_
log SFR _−_ SFMSz≈0(log _M_ ⋆) and ∆O/H _≡_ \[12 +\
log(O\*/ _H)\] − MZRz≈0(log_ M\*⋆). We report the median
and 16–84th percentile of these offsets in redshift bins.
This differential approach cancels the (identical) mass
axis and isolates evolution in the SFR and metallicity directions. Critically, to avoid an abundance-scale
mismatch, the MZR anchor is recomputed on a _T_ e-
anchored strong-line scale (PP04 O3N2) from SDSS
5
galSpecLine fluxes ( _N_ = 2\*. _0 × 10), matched to the_
_direct-Tescale on which the high-z metallicities are derived; the earlier photoionization-model (Tremonti) anchor lies ∼ 0_. _24 dex higher and by itself overstated the_
_deficit by ∼ 0_. _1–0_.\*13 dex.

$$
\\Delta\\log\\mathrm{S F R}\\equiv
$$

$$
\\mathrm{ ~~R\~~-~S F M S} _{z\\approx0}(\\log M_{\\star})
$$

$$
\\Delta\_ {\\mathrm {O} / \\mathrm {H}} \\equiv \[ 1 2 +\
$$\
\
$$\
\\mathrm{l o g}(0/\\mathrm{H})\]-\\mathrm{M Z R} _{z\\approx0}(\\mathrm{l o g},M_{\\star})
$$

$$
T \_ {e} -
$$

$$
(N,=,2.0\\times10^{5})
$$

$$
\\cdot T\_{e}
$$

## 4\. RESULTS

**Main sequence.** High- _z_ galaxies are elevated above
the local sequence at fixed mass by +0\*.\*77 dex (\*z ≈ _3_. _5),_
_+0_.\*89 dex (\*z ≈ _4_. _7), +0_.\*96 dex (\*z ≈ _5_. _4), and +1_. _94 dex_
_(z ≈ 6_.\*7; Fig. 1 left, Fig. 2 left). A factor of _∼_ 6 enhancement in SFR at fixed mass by _z ∼_ 3–5, growing
toward two orders of magnitude by _z_ ≳ 6, is the expected consequence of higher gas fractions and shorter
gas-consumption timescales in the early Universe. The
highest-redshift bin ( _z >_ 6, _n_ = 46) should be read cautiously given the small sample and the strong emissionline selection.

$$
+0.89
$$

$$
(z!\\approx!3.5)
$$

$$
(z!\\approx!4.7)
$$

$$
(z!\\approx!5.4)
$$

$$
(z\\approx6.7.
$$

$$
\\sim6
$$

$$
z\\gtrsim6,
$$

$$
(z>6,,n=46,
$$

**Mass–metallicity relation.** At fixed mass, high- _z_
galaxies are metal-poor relative to _z ≈_ 0 by \*− _0_. _43 dex_
_(z ≈ 4_.\*6), \*− _0_. _37 dex (z ≈ 5_.\*3), and \*− _0_. _40 dex (z ≈ 7_.\*2;
Fig. 2 right), all on the _T_ e-anchored scale. Two features stand out. First, the deficit is _nearly constant_ from
_z ≈_ 4 to _z ≈_ 7 rather than deepening — early galaxies

$$
(z\\approx5.3)
$$

$$
(z,\ \ \\mathrm4.6),,-0.37
$$

$$
-0.43
$$

$$
z\\approx0
$$

$$
(z\\approx7.2;
$$

$$
T\_{e^{\\mathrm{-a n c h o r e}}}
$$

$$
z\\approx4\ \\mathrm{t o}\ z\\approx7
$$

are not progressively more pristine with lookback time
in this sample. Second, the scatter is large (16–84th
range spanning _∼_ 0\*. _5 dex) and includes systems within_
_∼ 0_.\*15 dex of the local relation. Both are directly relevant to the ongoing debate over “surprisingly enriched”
early galaxies: a flat offset plus enriched outliers is more
consistent with rapid early enrichment followed by a
slowly evolving equilibrium than with monotonic metal
build-up.

$$
\\sim0.15
$$

## 5\. DISCUSSION AND CAVEATS

The measurements above are differential and therefore robust to the absolute calibration of the local
relations, but several systematics temper interpretation. (1) The JWST samples are emission-line selected
and thus biased toward high-sSFR, high-EW systems,
which inflates the apparent main-sequence elevation and
may bias metallicities. (2) We mitigate the dominant
abundance-scale systematic by placing the local anchor
on the same _T_ e-anchored scale as the high- _z_ data; a
residual _∼_ 0\*. _1 dex uncertainty between direct-Teand_
_Te-anchored strong-line calibrations remains, and highionization conditions at early times may add scatter. (3)_
_We extrapolate the SDSS relations below log_ M\*⋆ _≈_ 8 to
overlap the low-mass JWST galaxies; the main-sequence
extrapolation is mild (linear) but the MZR extrapolation is more uncertain. (4) Aperture and IMF differences are sub-dominant (≲ 0\*.\*05 dex). (5) The _z >_ 6
bins are small. A natural next step — enabled by the
same pipeline — is to confront these observed relations
with a cosmological simulation (IllustrisTNG) processed
identically, testing whether a model tuned to _z ≈_ 0 reproduces the _evolution_ we measure. That “calibration is
not validation” test is the single highest-ranked frontier
in our topic map and is deferred to a companion study.

$$
T\\cdot
$$

$$
\ .T\_{e}
$$

$$
\\sim0.1
$$

$$
T\_{e^{\\mathrm{-a n c h o r e}}}
$$

$$
M\_{\\star}\\approx8
$$

$$
z,>,6
$$

$$
\ \ (\\lesssim\ 0.05\ \\mathrm{d e x})
$$

$$
z\\approx0
$$

## 6\. CONCLUSION

Using a uniform SDSS anchor and public JWST catalogues, we find that 3 < z < 9 galaxies are elevated
0\*. _8–1_. _9 dex above the local star-forming main sequence_
_and depressed ≈ 0_.\*4 dex below the local ( _T_ e-anchored)
mass–metallicity relation, with the metallicity deficit remaining flat across _z ≈_ 4–7. The combination of a
non-deepening metallicity offset with enriched outliers
favours rapid early enrichment toward an evolving equilibrium, and provides a concrete, reproducible target
for cosmological simulations. This study was produced
autonomously as a demonstration of literature-to-data
frontier research; the SDSS SkyServer and VizieR TAP
queries are public and the analysis is fully reproducible.

$$
3,<,z,<,9
$$

$$
\\approx0.4
$$

$$
\ T\_{e}\\mathrm{-a n c h o r e d})
$$

$$
z,\\approx,4-7
$$

* * *

Figure 1. JWST galaxies at 3 < z < 9 (points, coloured by redshift) overlaid on the SDSS z ≈ 0 relations (black). Left: the
star-forming) main sequence; high-) _z_ galaxies sit systematically above the local sequence. _Right:_ the mass–metallicity relation;
x x
high- _z_ galaxies lie below the local relation, with large scatter.
de de
( (

$$
3<z<9
$$

$$
\\mathrm{S D S S}\ z\\approx0
$$

**Figure 2.** Evolution of the offsets from the _z ≈_ 0 relations.
_Left:_ main-sequence elevation ∆ log SFR grows with redshift.
_Right:_ the metallicity deficit ∆O/His \*≈ − _0_.\*4 dex ( _Te_ scale)
and nearly flat across _z ≈_ 4–7. Error bars are 16–84th percentiles; _n_ per bin annotated.

$$
z\\approx0
$$

$$
\\Delta\_{\\mathrm{O/H}}
$$

$$
\\approx-0.4
$$

$$
z\\approx4{-}7
$$

$$
(T\_{e}
$$

Brinchmann, J., et al. 2004, MNRAS, 351, 1151
Curti, M., et al. 2024, A&A, 684, A75
Kewley, L. J., & Ellison, S. L. 2008, ApJ, 681, 1183
Lisiecki, K., et al. 2025, A&A, 708, A235
Moustakas, J., et al. 2011, arXiv:1112.3300
Nakajima, K., et al. 2023, ApJS, 269, 33

## REFERENCES

Noeske, K. G., et al. 2007, ApJ, 660, L43
Sanders, R. L., et al. 2021, ApJ, 914, 19
Speagle, J. S., et al. 2014, ApJS, 214, 15
Tremonti, C. A., et al. 2004, ApJ, 613, 898
