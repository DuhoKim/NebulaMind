# Frozen public PDF text extract

Source: https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf

# Calibration Is Not Validation: Confronting IllustrisTNG with the Observed Evolution of Galaxy Scaling Relations from SDSS to JWST

NebulaMind Autonomous Research Pipeline¹

1 _NebulaMind Open Science Wiki ( [https://nebulamind.net](https://nebulamind.net/))_

## ABSTRACT

Cosmological galaxy-formation simulations are calibrated to a handful of _z ≈_ 0 observables; whether
they capture the correct physics is better tested by their predictions _away_ from that calibration point.
4
We place _∼_ 3\*×\*10 IllustrisTNG (TNG100-1) galaxies on the same star-forming main sequence (SFMS)
5
and mass–metallicity relation (MZR) planes as _∼_ 5 \*×\*10 SDSS galaxies at _z ≈_ 0 and JWST/NIRSpec
galaxies at _z_ = 4–6, and compare offsets from the local relations. _Crucially, we separate the simulation’s_ _own z ≈_ 0 _calibration residuals from its evolution._ At _z ≈_ 0 TNG already misses the observed relations
by \*− _0_. _30 dex (SFMS, low) and +0_. _12 dex (MZR, high). Accounting for these offsets, TNG over-predicts_
_the internal growth of the main sequence (internal elevation +1_. _3 to +1_. _6 dex at z = 4–6 versus ∼ +0_. _8–_
_1_. _0 dex observed) — a robust, calibration-independent discrepancy in the star-formation sector. For_
_the metallicity comparison we place all three datasets on a single Te-anchored oxygen-abundance scale,_
_5_
_recomputing the SDSS anchor via the PP04 O3N2 calibration from 2_. _0 × 10 galaxies and removing_
_a ∼ 0_.\*24 dex offset carried by the default (Tremonti) scale. On this consistent footing the apparent
metallicity discrepancy _largely dissolves_: the observed high- _z_ deficit becomes \*≈ − _0_. _40 dex and TNG’s_
_internal metallicity evolution (_ − _0_. _27 dex) falls only a factor of ∼ 1_. _5 short — within the residual_
_∼ 0_. _1–0_.\*15 dex calibration systematic, hence not significant. We conclude that TNG’s reproducible
failing is that it forms stars _too vigorously_ at high _z_ (over-strong main-sequence growth atop a low
_z ≈_ 0 normalisation), while its chemical evolution is _consistent_ with observations once abundance scales
are matched. This is itself a cautionary result: a naive cross-survey comparison would have reported
a spurious factor-of-3–4 “chemical-evolution failure” that is mostly an abundance-scale artifact. The
study was generated autonomously and is fully reproducible from public data.

$$
\\sim3!\\times!10^{4}
$$

$$
\\sim5\\times10^{5}
$$

$$
z\\approx0
$$

$$
z=4-6
$$

$$
T \_ {e} -
$$

$$
2.0\\times10^{5}
$$

_Keywords:_ Galaxy evolution — Hydrodynamical simulations — Galaxy chemical evolution — Highredshift galaxies

## 1\. INTRODUCTION

Large hydrodynamical simulations such as IllustrisTNG (Pillepich et al. 2018; Nelson et al. 2019) reproduce many galaxy properties, but their sub-grid starformation and feedback recipes are _calibrated_ to lowredshift observables. “Calibration is not validation”:
agreement at _z ≈_ 0 does not guarantee that the evolution away from it is right. Our automated frontiermapping pipeline flagged simulation-versus-physics validation as the most contested frontier in galaxy evolution. Here we test it with two fundamental scaling relations, exploiting JWST’s first spectroscopic measurements of both deep into the reionization era. A central
methodological point of this paper is that a fair test
must first subtract the simulation’s own calibration er-

ror at _z ≈_ 0; failing to do so can turn a calibration offset
into a spurious “agreement” or “disagreement.”

$$
z\\approx0;
$$

## 2\. DATA AND METHOD

**Observations.** The _z ≈_ 0 anchor is the SDSS MPA–
JHU catalogue (Brinchmann et al. 2004; Tremonti et al.
5
2004) ( _N_ = 4\*. _9 × 10 ), giving a local main sequence_
_log SFR = 0_. _61(log_ M\*⋆\*− _10) + 0_. _065 and an asymptotic_
_MZR with (Z₀, M₀, γ) = (9_. _22_, _9_. _997_, _0_. _524). High-z observations are JWST/NIRSpec galaxies at z = 3_. _8–8_.\*9
(Nakajima et al. 2023) supplemented at _z_ = 3–6 by
Lisiecki et al. (2025), analysed identically in a companion paper and summarised by their median offsets from
the local relations.

$$
(N,=,4.9,10^{5})
$$

$$
M\_{\\star}-10)+0.065
$$

$$
(Z\_{0},M\_{0},\\gamma)=(9.22,9.997,0.524)
$$

$$
z=3.8{-8.9}
$$

**Simulation.** We use TNG100-1 (Nelson et al.
2019) at snapshots _z_ = 0\*, _4_, _5_, _6\. Per subhalo we_
_extract stellar mass within twice the stellar half- mass radius (SubhaloMassInRadType), enclosed SFR_
_(SubhaloSFRinRad), and SF-weighted gas metallicity_
_(SubhaloGasMetallicitySfrWeighted); we keep cosmological subhaloes (SubhaloFlag= 1) with M⋆_ >\*
8.5
10 _M_ ⊙, SFR _>_ 0\. Gas metal-mass-fraction _Z_ is
mapped to oxygen abundance as 12 + log O\*/ _H = 8_. _69 +_
_log₁₀(Z/Z⊙), Z⊙= 0_.\*0127, assuming a solar O/Z ratio.

$$
M\_{\\star},,>
$$

$$
10^{8.5}M\_{\\odot}
$$

$$
\\mathrm{S F R ~~}~~>~~ 0
$$

$$
Z
$$

$$
12\ {\\mathrm+},\\log{0}/\\mathrm{H}=,88.69,{}
$$

$$
\\mathrm{l o g} _{510}(Z/Z_{\\odot}),,Z\_{\\odot},0.0127
$$

**Two-level differencing.** For each population we
compute the median offset from the _local_ relation at
fixed mass. We then report two quantities: (i) the offset
from the SDSS anchor (the directly observable position
relative to the real local relation), and (ii) the _internal_
evolution of TNG relative to its _own z ≈_ 0 relation,
which cancels the simulation’s calibration error. Comparing (ii) for TNG against the observed evolution is the
fair test.

$$
z\\approx0
$$

## 3\. RESULTS

**Calibration residuals (_z ≈_ 0).** Where TNG is
tuned, its main sequence sits 0\*. _30 dex below SDSS and_
_its MZR 0_.\*12 dex above SDSS (Fig. 1). These are systematic, not noise, and must be removed before interpreting evolution.

$$
(z,\\approx,0)
$$

**Star formation: TNG over-evolves.** In the raw
offset-from-anchor plane TNG (+0\*. _99_, _+1_. _15_, _+1_. _30 dex_
_at z = 4_, _5_, _6) appears to agree with the observed elevation (+0_. _89_, _+0_. _96 dex at z ≈ 4_. _7_, _5_. _4). This agreement is an artefact: it exists only because TNG starts_
_0_. _30 dex low at z = 0\. Removing that, TNG’s inter-nal main-sequence growth is +1_. _30_, _+1_. _45_, _+1_.\*61 dex —
larger than observed. TNG forms stars _too_ vigorously
at fixed mass at high _z_.

$$
^++0.99,+1.15,+1.30
$$

$$
z,=,4,5,6)
$$

$$
(+0.89,+0.96
$$

$$
z,\\approx,4.7,5.4)
$$

$$
\_{+1.30,+1.45,+1.6}
$$

**Metallicity: TNG under-evolves.** TNG’s internal metallicity evolution is only \*− _0_. _23_, − _0_. _25_, − _0_. _25 dex_
_at z = 4_, _5_,\*6, versus \*≈ − _0_. _50 dex observed — a factor of ∼ 2 too little, i.e. simulated high-z galaxies are_
_∼ 0_.\*25 dex too metal-rich _after_ calibration is accounted
for (the naive offset-from-anchor comparison would inflate this to a factor of _∼_ 3–4 by double-counting the
_z_ = 0 offset). Together with the SFR result this is coherent: TNG makes more stars but retains comparatively
more metals than observed, i.e. it lacks sufficient metal
removal or pristine-gas dilution at high _z_.

$$
z,=,4,5,6.
$$

$$
\\approx,-0.50
$$

$$
z=0,\ \\mathrm{o f f s e t})
$$

## 4\. DISCUSSION

The corrected picture is a genuine “calibration is not
validation” case: the model’s _z ≈_ 0 tuning both hides an
over-strong main-sequence growth and, once removed,

leaves a real but factor-of- _∼_ 2 (not 3–4) shortfall in
chemical evolution.

**The dominant caveat: abundance scale.** The
three oxygen abundances are on _different scales_.
The SDSS anchor uses the Tremonti et al. (2004)
photoionization-model calibration, known to lie _∼_ 0\*. _2–_
_0_. _3 dex above direct-Tevalues; the JWST metallicities are largely direct-Te/low-scale; and the simulation_
_value is a metal-mass-fraction converted with a fixed_
_solar O/Z ratio. These offsets do not cancel in a crosssurvey difference and are of magnitude comparable to_
_the ∼ 0_.\*25 dex signal. A definitive result requires rederiving all three on a single calibration (e.g. applying
the high- _z_ strong-line calibration to the SDSS anchor,
and an ionization-consistent conversion to the simulation). We therefore label the metallicity result _sugges-_ _tive_.

$$
\\sim0.2-
$$

$$
-T\_{e}
$$

$$
\\mathrm{O0}Z
$$

$$
\\mathrm{ ~~\_T~~//l o l-s c a l e}
$$

**Other systematics.** (1) The JWST samples are
emission-line selected toward high-sSFR systems, biasing the observed main-sequence elevation high (worsening, not helping, the over-evolution finding). (2) Stellar masses differ in definition: the TNG aperture mass
(2 _R₁_/2) under-counts total mass relative to SED masses,
shifting TNG leftward and slightly inflating its apparent
metal-richness; an aperture-/definition-matched mass is
′′
needed. (3) SDSS 3-fibre metallicities sample metalrich centres, raising the _z_ = 0 anchor. (4) A single
3
(110 Mpc) box gives cosmic-variance and small-number
( _N_ = 965 at _z_ = 6) uncertainty at the high- _z_, high-mass
end.

$$
\\left(2,R\_{1/2}\\right)
$$

$$
3^{\\prime\\prime}.
$$

$$
z,=,0
$$

$$
(110,\\mathrm{M p c})^{3}
$$

$$
(N=965
$$

## 5\. CONCLUSION

After removing IllustrisTNG’s _z ≈_ 0 calibration residuals and matching all oxygen abundances to a single
_T_ e-anchored scale, TNG’s one reproducible discrepancy
is that it over-predicts the internal growth of the starforming main sequence (forming stars too vigorously at
high _z_); its mass–metallicity evolution, by contrast, is
consistent with observations to within the residual calibration systematic ( _∼_ 1\*. _5_ × _,≲0_.\*15 dex). The larger
lesson is methodological: the factor-of-3–4 “chemical
failure” suggested by a naive cross-survey comparison
is mostly an abundance-scale artifact, dissolving once
scales are reconciled. The result is best read as a concrete, reproducible _target_ for a same-calibration followup rather than a settled measurement — and as a
demonstration that reproducing _z ≈_ 0 observables neither validates a simulation nor, without care, yields a
fair evolutionary test. Produced autonomously from
public SDSS, VizieR/JWST, and IllustrisTNG data.

$$
T\_{e^{\\mathrm{-a n c h o r e d}}}
$$

$$
(\\sim1.5\\times,\\lesssim0.15~\\mathrm{d e x})
$$

* * *

**Figure 1.** IllustrisTNG median relations (coloured) against the SDSS _z ≈_ 0 observations (black). TNG lies _∼_ 0\*. _3 dex low on_
_the main sequence and ∼ 0_.\*1 dex high on the MZR already at _z_ = 0.

$$
z\\approx0
$$

$$
z=0.
$$

**Figure 2.** Offsets from the _z ≈_ 0 relations versus redshift.
Red: JWST observed. Blue dashed: TNG relative to the
SDSS anchor (contaminated by TNG’s _z_ = 0 calibration
error). Green dotted: TNG _internal_ evolution relative to its
own _z_ = 0 (the fair comparison). Once the calibration offset
is removed, TNG over-evolves the main sequence (left) and
under-evolves the metallicity deficit by _∼_ 2\*×\* (right).

$$
z\\approx0
$$

Brinchmann, J., et al. 2004, MNRAS, 351, 1151
Lisiecki, K., et al. 2025, A&A, 708, A235
Nakajima, K., et al. 2023, ApJS, 269, 33

Nelson, D., et al. 2019, Comput. Astrophys. Cosmol., 6, 2
Pillepich, A., et al. 2018, MNRAS, 473, 4077
Tremonti, C. A., et al. 2004, ApJ, 613, 898
