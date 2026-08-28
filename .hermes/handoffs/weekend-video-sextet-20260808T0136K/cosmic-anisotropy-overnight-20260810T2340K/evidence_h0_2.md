URL: https://arxiv.org/pdf/2209.11238

Cosmicows-4

1 1 2 3 4
R. Brent Tully, Ehsan Kourkchi, Helene M. Courtois, Gagandeep S. Anand, John P. Blakeslee,
5 1 6 2 7 8
Dillon Brout, Thomas de Jaeger, Alexandra Dupuy, Daniel Guinet, Cullan Howlett, Joseph B. Jensen,
9 10 11 7 12
Daniel Pomarede, Luca Rizzi, David Rubin, Khaled Said, Daniel Scolnic, and Benjamin E. Stahl¹³

<sup>1</sup>*Institute for Astronomy, University of Hawaii, 2680 Woodlawn Drive, Honolulu, HI 96822, USA*
<sup>2</sup>*University of Lyon, UCB Lyon 1, CNRS/IN2P3, IUF, IP2I Lyon, France*
<sup>3</sup>*Space Telescope Science Institute, 3700 San Martin Drive, Baltimore, MD 21218, USA*
<sup>4</sup>*Gemini Observatory & NSF’s NOIRLab, 950 N. Cherry Ave., Tucson, AZ 85719, USA*
<sup>5</sup>*Center for Astrophysics, Harvard & Smithsonian, 60 Garden St., Cambridge, MA 02138, USA*
<sup>6</sup>*Korea Institute for Advanced Study, 85, Hoegi-ro, Dongdaemun-gu, Seoul 02455, Republic of Korea*
<sup>7</sup>*School of Mathematics and Physics, The University of Queensland, Brisbane, QLD 4072, Australia.*
<sup>8</sup>*Department of Physics, Utah Valley University, 800 W. University Parkway, Orem, UT 84058, USA*
*Institut de Recherche sur les Lois Fondamentales de l’Univers, CEA Universite Paris-Saclay, 91191 Gif-sur-Yvette, France*
<sup>10</sup>*W.M. Keck Observatory, 65-1120 Mamalahoa Highway, Kamuela, HI 96743, USA*
<sup>11</sup>*Department of Physics & Astronomy, University of Hawaii at Manoa, Honolulu, HI 96822, USA*
<sup>12</sup>*Department of Physics, Duke University, Durham, NC 27708, USA*
<sup>13</sup>*Department of Astronomy, University of California, CA 94720-3411, USA*

## ABSTRACT

With *Cosmicows-4*, distances are compiled for 55,877 galaxies gathered into 38,065 groups. Eight
methodologies are employed, with the largest numbers coming from the correlations between the photometric and kinematic properties of spiral galaxies (TF) and elliptical galaxies (FP). Supernovae that
arise from degenerate progenitors (type Ia Sne) are an important overlapping component. Smaller contributions come from distance estimates from the surface brightness uctuations of elliptical galaxies
and the luminosities and expansion rates of core collapse supernovae (SNII). Cepheid period-luminosity
relation and tip of the red giant branch observations founded on local stellar parallax measurements
along with the geometric maser distance to NGC 4258 provide the absolute scaling of distances. The
assembly of galaxies into groups is an important feature of the study in facilitating overlaps between
methodologies. Merging between multiple contributions within a methodology and between methodologies is carried out with Bayesian Markov chain Monte Carlo procedures. The nal assembly of
1 1
distances is compatible with a value of the Hubble constant of *H₀* = 74*:* 6 km s Mpc with the small
1 1 1 1
statistical error of 0*:* 8 km s Mpc but a large potential systematic error of 3 km s Mpc.
Peculiar velocities can be inferred from the measured distances. The interpretation of the eld of
peculiar velocities is complex because of large errors on individual components and invites analyses
beyond the scope of this study.

$$
\pm0.8\ \mathrm{k{}m\ s^{-1}\ M p c^{-1}}
$$

$$
H_{0}=74.6\,\mathrm{{{k m\ {mathrm{s{}}^{-1}}}\,M p c}^{-1}}
$$

$$
\sim3\,\mathrm{k{}m\,s^{-1}\,M\ c{}^{-1}}
$$

## 1. INTRODUCTION

*Cosmicows* is a program to compile galaxy distances
and parse observed velocities into components due to
arXiv:2209.11238v2  [astro-ph.CO]  28 Dec 2022the expansion of the universe and residuals due to gravitational interactions. Our fundamental interest is to
derive inferences regarding the large-scale structure of
the universe from galaxy test particle peculiar motions.
This fourth release of the program follows those ofTully
et al.(2008,2013,2016).

Contributions to the *Cosmicows* program have come
from work within our collaboration and from the literature. We consider methodologies that have been tested
and have physical bases that are reasonably well understood. It is as great a consideration, though, that there

be large overlaps between contributions. A sample with
distances to only a few objects cannot condently be
meshed within a common scale so is not very useful.

We derive distances in signicant numbers mainly
from seven methodologies. By far, the largest quantitative contributions are given by the fundamental plane
(FP) correlation between the luminosity, surface brightness, and central velocity dispersion of early-type galaxies (Dressler et al.1987b;Djorgovski & Davis1987) and
the luminosity-rotation rate relation for spiral galaxies (Tully & Fisher1977) (TF or Tully-Fisher relation
(TFR)). The individual errors in these cases are substantial (20 25%) but the objects are widely dispersed,
providing a dense network of distance information across the sky extending to 0*:* 05*c* and in the celestial and
galactic north to *z* = 0*:* 1, the upper cuto of our compilation.

Three other methods probe substantial distances with
greater accuracy but their contributions remain small.
Type Ia supernovae (SNIa) (Phillips1993) provide distances with an accuracy of 7% out to 0*:* 1*c*. Type-II
supernovae (SNII) (Hamuy & Pinto2002) provide distances with 15% accuracy to similar distances. Surface brightness uctuations (SBF) monitoring the degree
of resolution of the old stellar populations of elliptical
galaxies (Tonry & Schneider1988) can provide distances
with 5% accuracy to targets within 0*:* 03*c*.

While comparisons between these ve methods can
be set on a common relative scale, it remains to provide them an absolute calibration. Two methods provide a bridge: those provided by the Cepheid periodluminosity relation (CPLR) (Leavitt & Pickering1912)
and the constancy of stellar luminosities at the tip of
the red giant branch (TRGB) (Lee et al.1993). These
methods provide accurate distances ( 5%) but are restricted to less than 20 Mpc.

There has been considerable eort to establish the absolute scale of the CPLR and TRGB procedures through
geometrically based observations. Parallax distances
can be established to Cepheids within our own galaxy
(Benedict et al.2007) and parallax distances to RR
Lyrae and horizontal branch (HB) stars can establish
the TRGB scale (Rizzi et al.2007). It is anticipated
that observations with GAIA (Clementini et al.2018;
Mould et al.2019) will provide robust direct Cepheid
and TRGB calibrations in the near future. Meanwhile,
important links to an absolute scale are provided by detached eclipsing binaries in the Large Magellanic Cloud
(LMC) (Pietrzynski et al.2019) and the maser system in
the nuclear region of the galaxy NGC 4258 (Reid et al.
2019).

The main contributions in the rst version of *Cos-*
*micows* (Tully et al.2008) were based on the TFR
with optical photometry obtained object by object and
analog neutral hydrogen (H i ) linewidths. The catalog
contained distances to 1,791 galaxies constrained to the
1
limit 3,000 km s.

$$
\mathrm{s}^{-1}
$$

*Cosmicows-2* (Tully et al.2013) was expanded to
include a much larger volume, peaking in numbers at
1 1
5,000 km s with a tail extending to 15*;*000 km s.
Most of the contributions came from the TFR, with as a
major revision the employment of a rigorous algorithm
in the reduction of digital H i spectra (Courtois et al.
2009,2011b). Likewise, the photometric analysis was
more rigorously dened (Courtois et al.2011a;Sorce

$$
5,000\ \mathrm{k m\ {s}^{-1}}
$$

$$
\mathrm{t o}\sim15,000\,\mathrm{k m\ s^{-1}}
$$

et al.2012). The catalog then grew to include 8,188
galaxies.

The major addition to *Cosmicows-3* (Tully et al.
2016) was FP distance measures from the 6-degree
Field Galaxy Survey (6dFGSv) (Springob et al.2014).
This sample is entirely conned to the celestial south
1
and abruptly cuts o at 16,000 km s. A secondary
addition came from the TFR method with infrared
photometry provided by the Spitzer Space Telescope
(Sorce et al.2014). *Cosmicows-3* provided distances
1
for 17,699 galaxies. Coverage within 8*;*000 km s
was reasonably balanced around the sky but at 8,000-
1
16,000 km s it strongly favored the southern hemisphere. The infrared TFR contribution was conned to
1
within 6*;*000 km s but notably extended coverage
to low galactic latitudes, shrinking the coverage gap between galactic hemispheres.

$$
\mathrm{s}^{-1}
$$

$$
\sim8,000~\mathrm{k m~s}^{-1}
$$

$$
\mathrm{s}^{-1}
$$

$$
\sim6,000~\mathrm{k m~\ s^{-1}}
$$

Here, with *Cosmicows-4* a most important addition
is a much-extended TFR sample of 10,000 galaxies drawing in particular on kinematic information from AL-
FALFA, the Arecibo Legacy Fast ALFA survey of the
high galactic latitude sky in the decl. range 0 38 degrees (Haynes et al.2011,2018). Photometry is provided
by SDSS, the Sloan Digital Sky Survey (York et al.2000)
and WISE, the Wide-eld Infrared Explorer (Wright
et al.2010). This component of *Cosmicows-4* substantially redresses the imbalance favoring the southern sky
of the previous catalog.

SDSS also provides the source material for a second
even larger addition to the current catalog. SDSS photometry and spectroscopy are combined to provide FP
1
distances to 34,000 galaxies out to 30,000 km s in the
quadrant of the sky that is celestial north and galactic
north. As a consequence, while *Cosmicows-3* tilted toward coverage of the celestial south, now *Cosmicows-4*
greatly expands our knowledge of the north.

$$
3 0, 0 0 0 \mathrm {k m} \mathrm {s} ^ {- 1}
$$

With the astronomical community’s overriding interest in precision distance measurements in order to secure
the value of the Hubble constant, there are understandable arguments for a maximally homogeneous approach
(Riess et al.2016). The *Cosmicows* assembly is heterogeneous. It is to be appreciated that the primary interest of this program is the mapping of *deviations* from
cosmic expansion, requiring coherence of distance measurements but not an absolute scaling. Nonetheless, the
reasonable establishment of a zero-point is not our most
dicult task. Our heterogeneous approach has virtues.
Results from separate methodologies can be compared
by sectors of the sky or distance, potentially revealing
systematics. Dierent contributions favor ancient populations or young, members of clusters or the eld. Some are better probes of low galactic latitudes. Our samples
are heterogeneous but not indiscriminate.

Coincidences of distance measurements by dierent
methodologies to members of a common group enables
the stitching of samples into a coherent ensemble. Our
discussion will turn rst to the important matter of the
denition of groups in §2. Subsequent sections will focus
on each of the seven methodologies that provide most
of our distances. We begin with the numerically dominant TFR (§3) and FP (§4) components, beneting from
overlaps between large samples to establish coherence in
a core compilation. We then focus on the SBF (§5) and
SN Ia (§6) contributions that are modest in number but
that impose demanding constraints. There is a brief
discussion of SN II (§6.2) that at this point makes a relatively small contribution. This entire edice is then be
linked to foundational TRGB (§7) and CPLR (§8) information, these in turn grounded by geometrical maser¹
, eclipsing binary, and parallax observations. The integration of methodologies is discussed in §10. The data
products and a brief description of properties are discussed in Sections12and13. Then, §14provides a
summary.

## 2. GALAXY GROUPS

Galaxies tend to lie in groups, large and small. If
associations are made correctly, then all distance measures to galaxies in a group should be the same within
uncertainties. The composition of galaxy groups, then,
is of major importance for our study for at least three
reasons. First, averaging over the properties of a group
reduces errors. With weighted averaging of distances,
uncertainties can be brought down from single case 20-
25% values (depending on the methodology) to statistical uncertainties of a few percent with some rich clusters.
The gains apply to velocities as well. Velocity averaging can encompass *all* known group members, not just
those with measured distances. Second, it is particularly
important in the modeling of galaxy ows to accurately
locate the rich clusters, where distance measures from at
least the FP and SBF targets congregate. Rich clusters
tend to lie at focal points of galaxy streams.

Third, and perhaps most importantly, it is through
the groups that we most eectively match the zero-point
scaling of the diverse samples. Given the potential for
systematics within samples, across sectors of the sky,
and with distance, the more overlap the better. While
there can be some overlap at the level of individual

galaxies, by far most of our overlaps occur at the level
of groups and clusters. A corollary benet is the ability to weed out egregiously bad data while comparing
distances to objects in common,

Galaxy groups come in a wide range of scales. We
want to benet from the advantages of grouping over
the full range down to the instances of pairs. Typical
friends-of-friends and related group algorithms do not
scale physically over the three decades of mass of inter-
12 15
est (10 10 *M*). Appreciating the importance of
the matter, we initiated studies that resulted in three papers. In the rst (Tully2015a), we provided detailed account of eight well-studied groups/clusters ranging from
the Local Group to the Coma Cluster. It was possible
in these eight clean cases to isolate an observable proxy
for the virial radius of collapsed halos; the radius of the
second turnaround, *R₂*<sub>t</sub>(related to the *splashback* radius
(Adhikari et al.2014)). This radius is found to scale, as
=3
theory predicts, as *R₂*<sub>t</sub>*/ M¹* and *R₂*<sub>t</sub>*/*<sub>p</sub>for halos
(groups, clusters) with mass *M* and velocity dispersion
*p*. This rst paper establishes the coecients of the
scaling relationships.

$$
\ 10^{12}-10^{15}~M_{\odot})
$$

$$
R_{2t}
$$

$$
R_{2t}\propto M^{1/3}
$$

$$
R_{2t}\propto\sigma_{p}
$$

$$
\sigma_{p}
$$

In the second paper (Tully2015b), the scaling relationships were applied to build a group catalog involving 43,000 galaxies in the Two Micron All Sky Survey
(2MASS) redshift survey essentially complete over the
sky at *jbj >* 5 for galaxies brighter than *K*<sub>s</sub>= 11*:* 75
(Huchra et al.2012). The 2MASS survey, given its sensitivity to old stars, provides a good representation of
the mass distribution within the volume extending to
1
15,000 km s which is our principal concern. Relative
distances are based on redshifts. We favor the use of
this group catalog at systemic velocities greater than
1
3000 km s. Were we to consider an alternative, we
would use the similarly physically motivated catalog by
Lim et al.(2017).

$$
|b|>5^{0}
$$

$$
K_{s}\ 1=11.75
$$

$$
15,000~\mathrm{k m~s}{}^{-1}
$$

$$
\sim3000\ \mathrm{k m\ s^{-1}}
$$

$$
\sim 3 0 0 0 \mathrm {k m s} ^ {- 1}
$$

1
Nearer than 3000 km s confusion arising from
peculiar velocities is severe and we have knowledge of a
profusion of low surface brightness galaxies that failed
to be entered into the 2MASS catalog. Hence, for the
nearby volume we turn to the group catalog assembled
in the third paper (Kourkchi & Tully2017), based on
a heterogeneous collection of all 15,000 galaxies with
1
known velocities within 3,500 km s. The groups are
constituted based on the same scaling relations. The
availability of distance information from *Cosmicows-3*
is tremendously helpful in resolving confusion issues and
evaluating masses, and hence, scaling parameters.

$$
3,\ 500\ \mathrm{k m\ s^{-1}}
$$

With both the near and far catalogs, the groups are
roughly bounded by the radius of second turnaround.
Hence, they represent collapsed halos. As a naming convention, we identify a group by the Principal Galaxies

<sup>1</sup>Studies of nuclear maser systems provide an eighth methodology
and one that gives independent absolute distance estimates but
these are only available for six galaxies discussed in §9.

---

Catalog number (Paturel et al.1996) of the dominant
member, which we call 1PGC. There can be inconsis-
1
tencies between the two catalogs within 3,500 km s.
In such cases, we favor the specications byKourkchi &
Tully(2017).

$$
3.500\,\,\mathrm{k m\ s^{-1}}
$$

These group catalogs provide an excellent description
1
of clustering within 15*;*000 km s, the useful range
of the 2MASS *K*<sub>s</sub>= 11*:* 75 redshift survey. However,
the SDSS-based FP sample extends to 0*:* 1*c*. This SDSS
FP sample is a subcomponent of theTempel et al.(2014,
2017) SDSS group catalogs. The supernova samples also
extend to *z* = 0*:* 1, well beyond the range of theTully
(2015b) groups. If a group aliation is unavailable for
a galaxy within the groups described above then we opt
for memberships in the 2017 Tempel et al. catalog. The
relevant galaxies have PGC identications. We take as
the 1PGC name for a Tempel et al. group the PGC
number of the brightest member within our catalog.

$$
\sim15,000~\mathrm{k m~s^{-1}}
$$

$$
K_{s}\,=\,11.75
$$

$$
z=0.1
$$

## 3. LUMINOSITY-LINEWIDTH DISTANCES TO SPIRAL GALAXIES

Distances derived from the TFR are an extremely important component of the *Cosmicows* program. They
are numerous and the most widely distributed. Spiral
galaxies are found in all environments, providing links
with other methodologies in groups and sparse but invaluable coverage in voids.

## 3.1. The Baryonic TFR

Conventionally in the past, TFR samples have been
acquired by individual targeting of selected candidates
for both the photometric (imaging) and kinematic
(linewidth) required components. Nowadays, wide-eld
optical, infrared, and H i radio surveys provide access to
much larger samples. Specically, here, we make use
of serendipitous SDSS DR12 *u;g;r;i;z* optical imaging (Alam et al.2015), WISE *W* 1 and *W* 2 infrared
imaging (Wright et al.2010;Mainzer et al.2011), and
Arecibo Legacy Fast ALFA Survey (ALFALFA) neutral
hydrogen spectral detections (Haynes et al.2018), supplemented in the radio with pointed observations with
the Green Bank Telescope and Parkes Telescope (Dupuy
et al.2021).

$$
u,g,r,i,z
$$

In a series of three papers, we explored the properties of the optical and infrared photometric material
particularly pertaining to issues of extinction (Kourkchi
et al.2019), then provided optical and infrared calibrations of the TFR based on 600 galaxies in 20 clusters (Kourkchi et al.2020a), and then used the calibrations to derived TFR distances for 10*;*000 galaxies (Kourkchi et al.2020b). It was subsequently revealed that the distances in the latter publication are

aected by a bias: a trend in Hubble parameter values,
2
*H*<sub>i</sub>= *f*<sub>i</sub>*cz*<sub>i</sub>*=d*<sub>i</sub>, as functions of apparent magnitude.
The bias strongly aects distance estimates to intrin-
1
sically fainter galaxies within 4,000 km s and arises
from faint end curvature in the TFR. Distances to galax-
1
ies with velocities greater than 4,000 km s are mildly
aected.

$$
H_{i}\:=\:f_{i}c z_{i}/d_{i}.
$$

$$
4,000\,\,\mathrm{k m\ s^{-1}}
$$

$$
4,000~\mathrm{k m~{s}^{-1}}
$$

Much, and even a majority, of baryonic mass in faint
galaxies is in the form of interstellar gas. It has been
noted that adding this constituent to the stellar component represented by optical or infrared light, formulating the baryonic Tully-Fisher relation (BTFR), eectively linearizes the relation between the logarithms of
baryonic mass and H i prole linewidth (McGaugh et al.
2000;McGaugh2005;Lelli et al.2016,2019). Consequently, and in response to our concern regarding the
bias with faint galaxies in the TFR study byKourkchi
et al.(2020b), the same sample has been reanalyzed with
the BTFR methodology byKourkchi et al.(2022).

The BTFR requires the additional component of
H i uxes, an observable acquired simultaneously with
linewidths. The need for a robust H i detection gives
focus to the condition that the sample is H i ux limited: photometry for any target with sucient H i ux
is easily obtained. However, an H i ux limit translates
to a cut in gas mass that increases with distance. This
trend results in a bias that must be addressed in order
to obtain distance measures of value.Kourkchi et al.
(2022) developed a procedure that was demonstrated
with mock data to provide unbiased distance estimates.

Application of the BTFR also requires the translation
of luminosities into approximations of stellar mass, involving color terms. The conversions are linear, but uncertainties are further compounded by the summation
of stellar and gas mass components. On the one hand,
there is a greater complexity with the BTFR, but on the
other hand, the linkage with the dark matter-dominated
total mass is expected to be tighter. Scatter as evalu-
1
ated from *H*<sub>i</sub>values at *V >* 4*;*000 km s is 22% in
distances, comparable to that with the TFR.Kourkchi
et al.(2022) provide BTFR distance estimates for 9967
galaxies.

$$
H_{i}
$$

$$
V\,>\,4,000\,\mathrm{k m\ s^{-1}}
$$

## 3.2. Ensemble of TFR and BTFR Sources

*Cosmicows-4* assembles TFR distances to 12*;*412
galaxies, the largest, most coherent compilation to date
by this methodology. The most important contribution
(9,967 galaxies) is the new BTFR sample discussed by
Kourkchi et al.(2022) (hereafter cf4). This new sam-

<sup>2</sup>The cosmological model parameter *f* <sub>i</sub>s dened in connection
i
with Eq.3.

$$
f_{i}
$$

$$
\ mathrm E q.
$$

---

Figure 1. Cumulative histogram of TF targets with systemic velocity and a breakdown by subsample as given by
the legend.

ple is compared and merged with ve TFR samples:
the assembly of 5,980 cases in *Cosmicows-2* that itself is broken into a part (4,069) derived within our collaboration (hereafter cf2) and a part (3,957) emanating
from the SFI++ study (Springob et al.2007) (hereafter
s), 2,251 galaxies discussed in *Cosmicows-3* incorporating photometry from Spitzer Space Telescope images
(spitzer), 1,715 galaxies utilizing 2MASS photometry
(2mtf) (Hong et al.2019), and 551 extreme edge on
galaxies (Makarov et al.2018) (at).

Figure1is a histogram of the run of velocities for the
TF subsamples and the full TF sample. The distribution
of the combined TF sample is displayed in supergalactic coordinates in Figure2. The bands of high object
density crossing the two supergalactic hemispheres lie
in the 0 < < 38 decl. zone accessed by the Arecibo
Telescope.

$$
0\,<\,\delta\,<\,38
$$

Our analysis began with each sample alone. At sys-
1
temic velocities above 4*;*000 km s cosmic expansion velocities are expected to overwhelmingly dominate
deviant velocities. Hence, a necessary (not sucient)
criterion a sample should satisfy is approximate constancy in the Hubble parameter for individual galaxies,
*H*<sub>i</sub>= *f*<sub>i</sub>*cz*<sub>i</sub>*=d*<sub>i</sub>, averaged in velocity bins. The results of
this test for all but the most recent at galaxy sample
were presented inKourkchi et al.(2020b). A signicant
drift toward smaller *hHi*i (larger derived distances) was
evident in the 2mtf sample. An adjustment to negate
this trend was introduced byKourkchi et al.(2020b),
see §5, and is incorporated in the current work. The
at sample passes the *hHi*i constancy test. Note that

$$
4,000\,\mathrm{\ k m\ s^{-1}}
$$

$$
H_{i}=f_{i}c z_{i}/d_{i}
$$

$$
\langle H_{i}\rangle
$$

$$
\S5
$$

$$
\langle H_{i}\rangle
$$

absolute *hHi*i values are not an issue at this stage; they
can be (and are) dierent for each sample.

$$
\langle H_{i}\rangle
$$

This test of the constancy of *H*<sub>i</sub>with redshift provides as a side product an evaluation of the rms dispersion in measurements within each sample. The measured values include dispersion in velocities and intrinsic
dispersion but these components are unimportant if, as
we do, we restrict attention to velocities greater than
1
4,000 km s. We nd the following characteristic rms
dispersions for seven samples (treating separately the
optical and infrared components of cf4 (whence, cf4-op
and cf4-ir), the two components of *Cosmicows-2*, cf2
and s, and the components of spitzer with and without color corrections (spitzer-cc and spitzer-nc). The
rms dispersions for the BTFR cf4-ir and cf4-op are 0.45
and 0.47 mag respectively, while for the two-parameter
TF studies dispersions are 0.40 for all three cf2, s, and
spitzer-cc, 0.50 for both spitzer-nc and 2mtf, and 0.55
for at. Distance values for 2mtf at Local Group frame
1
velocities less than 2000 km s, as evaluated by the
Hubble parameter test and the test to be discussed next,
are systematically too low and we reject all those 2mtf
measurements.

$$
H_{i}
$$

$$
4,000\ \mathrm{k m\ {s}^{-1}}
$$

$$
2000\,\mathrm{{k m\ s^{-1}}}
$$

Another test of the samples applied byKourkchi et al.
(2020b) was to focus on dierences in distance moduli
between cf4 and an alternate sample: *h*<sub>cf</sub><sub>4</sub> <sub>alt</sub>*i* where
*alt* is any of the other samples (now extended to include
at). This test is particularly useful for the isolation of
egregiously bad distance values in one of the samples.
Much less than 1% of cases in cf2, s, spitzer, and cf4
are rejected by this test. With 2mtf 2%, and with at
5%, are rejected.

$$
\langle\mu_{c f4}-\mu_{a l t}\rangle
$$

$$
\sim5\%.
$$

We now turn our attention to the integration of these
samples into a global maximally consistent compilation
of TFR distances.

## 3.3. Preliminaries

Our goal is to combine the distinct TFR subsamples
into a single TFR sample. Before this integration, each
subsample has its own zero-point scaling. Here, we revise the zero-points of subsamples to achieve statistical
equality between them. We stress that we do not make
relative changes in moduli *within* a subsample in this
process. Doing so would subvert the utility provided by
multiple subsamples in reducing systematics.

It is evident that TFR samples have non-Gaussian
outliers. Steps have been described to remove strongly
deviant cases but our initial integration of subsamples
reveals additional instances. Applying a 3*:* 5 rejection criterion caught 275 cases among 22,233 measures
(1.2%) where there would be nine with a normal distribution. These outliers are removed.

---

Figure 2. An Aito projection in supergalactic coordinates of the distribution of the 12,223 galaxies constituting an ensemble
of TFR samples. Colors relate to systemic velocities of the group of a galaxy as given in the table below the map. Milky Way
extinction levels are cast in shades of gray. The dense roughly vertical swaths of objects in both supergalactic hemispheres lie
in the decl. band of the Arecibo Telescope.

Next, we want to prot from the advantages of averaging over groups discussed in §2. We begin by weighted
averaging of the distance moduli of all galaxies within
a 1PGC group within a single subsample. Individual weights are formed from the inverse square of rms
uncertainties. This average and associated weight is
one object in the ensuing analysis. Accordingly, each
subsample is reduced to a quantity of objects (halos,
groups, clusters) composed of from one to many individual galaxies, each identied by a 1PGC number.

## 3.4. Combining all TFR distances: Bayesian approach

Ultimately, we want to merge all samples by all
methodologies into a coherent set with a zero-point established by geometric distance measurements. At this
stage, it is sucient to bring all TFR subsamples onto
a common scale. The baseline TFR scale will be set by
our new cf4 subsample that should lie close to our nal
scale, given its linkage to Cepheid and TRGB measures
as discussed byKourkchi et al.(2020a,b,2022).

Here, we pursue our goal to nd the global modulus oset of each sample, \s", from that of cf4, where
\s" stands for any of the samples we introduced earlier
in this chapter (cf2, s, spitzer, 2mtf, at). We will
adjust the reported distance moduli within each sam-
(s) (s) (s)
ple, *DM*<sub>in</sub>, following *DM* = *DM*<sub>in</sub>+ <sup>s</sup>in order
to set all cataloged distances on the same scale. By
our convention,<sub>cf</sub><sub>4</sub>= 0. We treat these adjusting
values as a set of free parameters that are optimized
together in a Bayesian framework. The best oset parameters minimize the total deviation of adjusted object
distance moduli (groups and individual galaxies) from
the weighted distance modulus averages oered by all
samples together.

$$
" S"
$$

$$
^{6}\underset{\mathrm{S}}{^{93}}
$$

$$
D M_{i n}^{(s)}
$$

$$
D M^{(s)}=D M_{i n}^{(s)}+\Delta\mu_{s}
$$

$$
\Delta\mu_{c f4}\,=\,0
$$

Our objective is to nd the posterior probability distribution *P*(*jD*), with being the vector of all moduli
osets, (<sub>s</sub><sub>1</sub>, <sub>s</sub><sub>2</sub>, ...). *D* holds the original cataloged
(s)
distance moduli, *DM*<sub>in</sub>. According to conditional probability theory, *P*(*jD*) */P*(*Dj*)*P*(). Having no prior
knowledge about the distribution of the moduli osets

$$
\mathcal{P}(\Theta|\mathcal{D})
$$

$$
\left(\Delta\mu_{s1},\thinspace\Delta\mu_{s2},\thinspace...)\right.
$$

$$
D M_{i n}^{(s)}
$$

$$
\mathcal{P}(\Theta|\mathcal{D})\propto\mathcal{P}(\mathcal{D}|\Theta)\mathcal{P}(\Theta)
$$

---

Figure 3. The posterior distribution of the optimized zero-points of TFR catalogs with respect to cf4. Contours represent
*=*2,, 3*=*2 and 2 levels of the two-dimensional distributions and they enclose 12%, 39%, 68%, and 86% of the distributed
points, respectively. Two vertical dashed lines in each of the one-dimensional histograms specify the region that accommodates
68% of the points, and the red vertical line identies the median of the distribution. Each panel covers 0*:* 08 mag about the
center of the distribution.

$$
\sigma/2,\,\sigma,\,3\sigma/2
$$

implies *P*() = 1 and subsequently *P*(*jD*) */P*(*Dj*),
where the right-hand side is the likelihood function, *L*.
We assume that all measured object distances are independent with Gaussian uncertainties. Therefore, for
each object, *n*, the likelihood function is the multiplication of a set of independent probabilities given as

$$
\pm0.08
$$

$$
\mathcal{P}(\Theta|\mathcal{D})\propto\mathcal{P}(\mathcal{D}|\Theta)
$$

$$
\mathcal{P}(\Theta)=1
$$

$$
n,
$$

$$
\mathcal{L}_{n}=\prod_{A l l`n`}\frac{1}{\sqrt{2\pi\sigma_{n,s}^{2}}}\ \operatorname{e x p}{\frac{-1}{2}\Big(\frac{D M_{n}^{(s)}-\langle D M D\rangle_{n}}{\sigma_{n,s}}\Big)^{2}}\ ,
$$

(1)

iterating over all distance catalogs. *hDM i*<sub>n</sub>is the
th
weighted average distance modulus of the *n* object
<sup>th</sup>at is derived from the adjusted distance moduli,
<sup>(</sup><sup>s</sup><sup>)</sup>
*DM*<sup>n</sup>is the distance modulus of the object in the sam-
2 (s)
ple \s", and<sub>n;s</sub>is the variance of *DM*<sub>n</sub>*hDM i*<sub>n</sub>,
which is determined by adding the uncertainties of the
associated parameters in quadrature. Likewise, the to-
QN
tal likelihood function for all objects is *L*<sub>tot</sub>=<sub>n</sub><sub>=1</sub>*L*<sub>n</sub>,
where *N* is the total number of objects (groups and individuals). It is simpler to work with the logarithm of
the likelihood function, which is expressed as

$$
\langle D M\rangle_{n}
$$

$$
n^{t h}
$$

$$
D M_{n}^{(s)}
$$

$$
"s"
$$

$$
D M_{n}^{(s)}-\langle D M\rangle_{n},
$$

$$
\sigma_{n,s}^{2}
$$

$$
\begin{array}{l}{\mathcal{L}_{t o t}=\prod_{n=1}^{N}\mathcal{L}_{n},}\\ \end{array}
$$

---

P<sub>N</sub>
2
log*L*<sub>tot</sub>=<sub>n</sub>*=*1 <sub>n</sub>=<sup>2</sup>, where

$$
:\mathcal{L}_{t o t}=-\sum_{n=1}^{N}\chi_{n}^{2}/2.
$$

$$
\chi_{n}^{2}=\Big(\frac{D M_{n}^{(s)}-\langle D M\rangle_{n}}{\sigma_{n,s}}\Big)^{2}\ .
$$

(2)

Adopting a at prior distribution for the moduli o-
2
sets leaves us with a minimization problem. We
are interested in a set of moduli osets that minimizes
PN
2 <sub>2</sub>
<sub>tot</sub>=<sub>n</sub><sub>=1</sub> <sub>n</sub>.

$$
\chi^{2}
$$

$$
\chi_{t o t}^{2}=\sum_{n=1}^{N}\chi_{n}^{2}
$$

To sample the posterior distribution, *P*(*jD*), we
use the Python package *emcee* (Foreman-Mackey et al.
2013), which implements Markov chain Monte Carlo
(MCMC) simulations to explore the parameter space.
Starting from our likelihood function, we generate 128
chains each with the length of 10,000. We remove the
rst 1,000 steps which are conservatively chosen to ensure that the remaining steps adhere to Markov chain
statistics. Figure3illustrates the corner plots for the
resulting posterior distribution of<sub>s</sub>. The topmost
panel of each column shows the one-dimensional distribution of the corresponding sampled parameter, overlaid with the median values (red solid line) and the
lower/upper bounds corresponding to 16/84 percentiles
(black dashed line). Horizontal and vertical red lines in
the two-dimensional distributions exhibit the location
of the median values that are adopted as the optimum
moduli osets of the corresponding catalogs with respect
to cf4.

$$
\Delta\mu_{s}
$$

The variance for a given subsample that is recorded
in Fig.3depends on both the uncertainties in individual measurements and the number of intersections with
other subsamples. The individual uncertainties between
the alternate TF subsamples are only modestly dierent,
so it is the numbers of intersections that dominate.

## 4. FP DISTANCES TO EARLY-TYPE GALAXIES

The FP methodology (Dressler et al.1987b;Djorgovski & Davis1987), with its applicability to earlytype galaxies, provides a complement to the TFR. The
accuracies of individual measurements are comparable.
While the gas-rich systems observed with the TFR are
widely dispersed, the old star-dominated systems favored for FP observations tend to clump in regions of
high density.

Here, in *Cosmicows-4* we combine results from ve
programs. Three of these were already included in
*Cosmicows-2*: contributions for a total of 1508 galaxies
to be referred to as smac (Hudson et al.2001), efar (Colless et al.2001), and enear (Bernardi et al.2002). Individually these sources provide distances for 690, 696, and
447 galaxies, respectively. Contributions from a fourth
program, 6dFGSv (Springob et al.2014) were included
in *Cosmicows-3*. This sample of 7,099 galaxy distances

is particularly important as the numerically dominant
source of distances in the celestial south. However, by
far the largest sample containing 34,059 galaxies is a
new contribution restricted to the celestial and galactic
north that draws on data extracted from the SDSS. The
three earliest FP surveys, smac, efar, and enear provide
valuable bridges across the celestial hemispheres, and
are important given there is only a slight overlap (41
cases) between the 6dFGSv and SDSS samples.

## 4.1. The 6dFGSv Sample

While the 6dFGSv sample was originally included in
*Cosmicows-3*, in this latest work we provide a new recalibration of this sample based on the ndings ofQin
et al.(2018) designed to explore and remove spurious
ows. In total, the 6dFGSv sample subtends the entire < 0 sky, except for regions with galactic latitude jbj < 10 . Its 8,885 objects incorporate many of
the brightest early-type galaxies in 6dFGSJones et al.
2009), nominally selected to have a spectral signal-tonoise ratio > 5, total J-band magnitude < 13: 65, red-
1
shift cz < 16;500 km s and velocity dispersion greater
1
than 1<sup>1</sup>2 km s (Campbell et al.2014). Further renements to this selection include visual classication and
removal of galaxies based on their morphological type
(although as demonstrated inTully et al.(2016) not all
remaining galaxies are classied as ellipticals) and removal of objects with undesirable spectral features or
poor spectral template ts (Campbell et al.2014). Photometry for the Fundamental Plane sample was obtained
by cross-matching with the 2MASS survey (Jarrett et al.
2000;Skrutskie et al.2006).

$$
\delta\:<\:0^{\circ}
$$

$$
|b|\,<\,10^{\circ}
$$

$$
c z<16,500\,\mathrm{k m\ s^{-1}}
$$

$$
<13.65
$$

$$
\mathrm{s}^{-1}
$$

Springob et al.(2014) produce peculiar velocity measurements with this sample by modeling the logarithmic dierence in observed and cosmological distances to
each galaxy as a function of the logarithmic dierence
between their observed eective radii and the eective
radii predicted from the best-t FP. For each galaxy,
one can compute the probability of it having a particular distance modulus by assuming a Gaussian probability distribution function (PDF) about the FP. However,
this procedure is complicated by Malmquist bias and the
selection function of the 6dFGSv data, particularly the
magnitude limit. The presence of a magnitude limit cuts
a slice through the FP, such that the PDF is no longer
normalized. Because the magnitude limit is in apparent magnitudes, the portion of the Fundamental Plane
that cannot be observed varies with distance, and so the
normalization of the PDF for each galaxy also depends
on distance. To counteract this eect,Springob et al.
(2014) produced a calculation of this normalization as

---

9

a function of distance using simulations drawn from the
best-t 6dFGSv FP with a J < 13: 65 limit.

In subsequent work byQin et al.(2018), similar simulations reproducing the FP, selection function, and
methodology applied to the 6dFGSv data were used to
measure the bulk ow. A signicant oset between the
measured and true bulk ows in the simulations was
identied in the direction directly toward the southern
celestial pole. It was found to be possible to remove this
eect in the simulations (and subsequently the data) by
recalculating the normalization of the probability distribution for each galaxy using an ad hoc, brighter, magnitude limit of J < 13: 217. In this work we repeat this
calculation, paying special attention to not only the bulk
ow, but also the Hubble parameter in radial shells.

$$
J<13.217
$$

We start by generating 128 mock 6dFGSv surveys
matching the methods inMagoulas et al.(2012) andQin
et al.(2019), which are then run through a reconstruction of the 6dFGSv pipeline using a magnitude limit of
J < 13: 65. Unlike previous works, the normalization of
the PDF for each galaxy is computed using numerical
Monte Carlo integration of the truncated 3D Gaussian
PDF, rather than summing over simulations. This procedure was found to result in less noise and was far more
reliable for computing an accurate value at large comoving distances where by design the number of galaxies
available to compute the probability, even over 128 simulations, quickly falls to zero.

$$
J<13.65
$$

The bulk ow in each simulation was then computed
using the-maximum likelihood estimator (Kaiser1988;
Qin et al.2018), as was the weighted mean value of

$$
\log_{10}(H_{i})=\log_{10}\biggl(\frac{f_{i}c z_{i}}{d_{i}}\biggr).
$$

(3)

in redshift bins, where *f*<sub>i</sub>= 1 + 1*=*2[1 *q₀*]*z*<sub>i</sub>1*=*6[1
2 <sup>2</sup>
*q₀* 3*q₀* + *j₀*]*z*<sub>i</sub>, *z*<sub>i</sub>is the redshift of the galaxy, *q₀* and
*j₀* are the acceleration and jerk parameters, and *c* is the
speed of light. Here, *d*<sub>i</sub>is the luminosity distance to each
1 1
galaxy, computed assuming *H₀* = 75 km s Mpc.
For comparison, the same quantities are computed for
each simulation using the true luminosity distance and
peculiar velocity of each simulated galaxy.

$$
f_{i}=1+1\big/2\big[1-q_{0}\big]z_{i}-1\big/6\big[1-
$$

$$
q_{0}-3q_{0}^{2}+j_{0}]z_{i}^{2},\:z_{i}
$$

$$
d_{i}
$$

$$
H_{0}\,=\,75\,\,\mathrm{k m\,s^{-1}\,M p c^{-1}}
$$

The results of this procedure are shown in Figures4
and5. Also plotted alongside are the results for the
original 6dFGSv data. From the binned Hubble parameters, it is clear that the mocks with distance moduli
computed using the 6dFGSv pipeline exhibit an outow
1 1
and do not lie on the expected *H₀* = 75 km s Mpc
line. The distribution of these same mocks matches the
data, which leads us to conclude the same is likely true
for the data too. This trend is not obvious without the
presence of simulations (and so not highlighted previ-

$$
H_{0}=75\;\mathrm{k m\;s^{-1}\;M p c^{-1}}
$$

Figure 4. Measurements of the weighted mean Hubble
1
parameter in redshift bins of width 1000 km s from the
6dFGSv data (points) and simulations (band). The bands
show the median value and 68% percentile region for the
128 mock realizations while the horizontal dashed line de-
1 1
notes the input value *H₀* = 75 km s Mpc used to compute the distance. We expect the Hubble parameter to be
roughly constant with redshift and lie close to the input
value. The blue band/points show the Hubble parameter
using the original 6dFGSv methodology with a magnitude
limit of J < 13: 65 for the Malmquist bias correction. The red
band/points show the recalibrated results using J < 13: 38,
which clearly reduces the bias seen in the mocks. Though
1
high, the 6dFGSv data for czcmb< 5000 km s are still
within the 95% region computed from the simulations.

$$
\mathrm{s}^{-1}
$$

$$
H_{0}=75
$$

$$
\mathrm{s^{-1}\ \mathrm p p c^{-1}}
$$

$$
J<13.65
$$

$$
J\,<\,13.38
$$

$$
c z_{\mathrm{c m b}}\,<\,5000\,\,{\mathrm{k m}}\,{\mathrm{s}}^{-1}
$$

ously), particularly because cosmic variance at czcmb<
1
5000 km s seems to be scattering the observed Hubble
parameters high in the data.

$$
\ z_{\mathrm{c m b}}<
$$

$$
\mathrm{s}^{-1}
$$

The eect on the bulk ow is particularly pronounced.
It was found byQin et al.(2018) that the measured bulk
ow in the simulations is biased quite negatively in the
direction of the southern celestial pole compared to the
bulk ow known to exist in the simulations. Although
the *true* bulk ow in the 6dFGSv is not known and can
only be estimated, the measured value is consistent with
the biased mock results, leading us to conclude that the
data is similarly biased.

As with the previous work byQin et al.(2018), we correct for this problem by modifying the magnitude limit
used in the Malmquist bias correction/normalization of
each galaxy’s PDF. By iterating, a magnitude limit of
J < 13: 38 was found to produce binned Hubble parameters that are at with redshift while also substantially
reducing the dierence between the adjusted and measured bulk ows. The results of applying this limit to
the mocks and data are shown in Figs.4and5. The
small dierences between the optimal value found here
and that used inQin et al.(2018) are likely the result of

$$
J<13.38
$$

---

10

Figure 5. Measurements of the bulk ow in each direction from 6dFGSv mocks (points) and data (bands) using the-MLE
method ofQin et al.(2018). For each simulation, we plot the measured maximum likelihood bulk ow against the true bulk
ow calculated by averaging over the true peculiar velocity of each galaxy. The true bulk ow for the data is not known *a*
*priori* and so the measurement is included as a horizontal band. In both cases, error bars/regions denote the equal likelihood
bounds encapsulating 68% of the posterior. The left-hand panel shows the results using the original 6dFGSv methodology and
J < 13: 65 magnitude limit for the Malmquist bias correction/PDF normalization. The right-hand panel shows the recalibrated
results using J < 13: 38. The recalibration removes the strong negative bias in the bulk ow in the direction of the south celestial
pole (*z*-axis in this coordinate system) seen in the simulations and believed to also be present in the data.

$$
J<13.65
$$

$$
J<13.38
$$

the more rigorous calculation of the normalization using
numerical integration adopted in this work.

We believe this recalibration to be robust and so use
the updated 6dFGSv data in *Cosmicows-4*. The source
of the discrepancy between the magnitude limit used to
construct the simulations and the optimal value found
for the Malmquist bias correction is unclear, but indicates a discrepancy between the best-t 6dFGSv FP
(from which the simulation apparent magnitudes are derived) and the assumed magnitude limit of the data. It
is not inconceivable that the true magnitude limit of the
6dFGSv data is in reality brighter than the nominal selection function, particularly in light of the other aspects
of the sample selection required to go from the 2MASS
photometry and 6dFGS spectra to the FP sample, and
then again to the peculiar velocity sample. However,
there may be more to the picture. A preferable solution
would be to perform a joint t for the FP parameters
and peculiar velocities simultaneously, again validated
against simulations; however, such an analysis is beyond
the scope of the current work.

The systematic problem as a function of morphological type identied byTully et al.(2016) remains in the
revised bias-adjusted 6dFGSv distances. Candidates in
the 6dFGSv compilation are given a morphology *M* description, with *M* = 0 for ellipticals, *M* = 2 for lenticulars, and *M* = 4 for spirals. As seen in Figure6, there
is a clear drift in *hf*<sub>i</sub>*V*<sub>i</sub>*=di*i with *M*, where *V*<sub>i</sub>and *d*<sub>i</sub>are

[... middle omitted — see footer ...]

139, 120, doi:10.1088/0004-6256/139/1/120
Foreman-Mackey, D., Hogg, D. W., Lang, D., & Goodman,
J. 2013, PASP, 125, 306, doi:10.1086/670067
Freedman, W. L., Madore, B. F., Gibson, B. K., et al. 2001,
ApJ, 553, 47, doi:10.1086/320638
Freedman, W. L., Madore, B. F., Hatt, D., et al. 2019, ApJ,
882, 34, doi:10.3847/1538-4357/ab2f73
Freedman, W. L., Madore, B. F., Hoyt, T., et al. 2020,
ApJ, 891, 57, doi:10.3847/1538-4357/ab7339
Ganeshalingam, M., Li, W., & Filippenko, A. V. 2013,
MNRAS, 433, 2240, doi:10.1093/mnras/stt893
Garnavich, P., Wood, C. M., Milne, P., et al. 2022, arXiv
e-prints, arXiv:2204.12060.
https://arxiv.org/abs/2204.12060
Garofalo, A., Delgado, H. E., Sarro, L. M., et al. 2022,
MNRAS, 513, 788, doi:10.1093/mnras/stac735
Gott, J. Richard, I., Juric, M., Schlegel, D., et al. 2005,
ApJ, 624, 463, doi:10.1086/428890
Graziani, R., Courtois, H. M., Lavaux, G., et al. 2019,
MNRAS, 488, 5438, doi:10.1093/mnras/stz078
Hamuy, M., & Pinto, P. A. 2002, ApJL, 566, L63,
doi:10.1086/339676
Hayden, B. T., Gupta, R. R., Garnavich, P. M., et al. 2013,
ApJ, 764, 191, doi:10.1088/0004-637X/764/2/191
Haynes, M. P., Giovanelli, R., Martin, A. M., et al. 2011,
AJ, 142, 170, doi:10.1088/0004-6256/142/5/170
Haynes, M. P., Giovanelli, R., Kent, B. R., et al. 2018, ApJ,
861, 49, doi:10.3847/1538-4357/aac956
Hicken, M., Wood-Vasey, W. M., Blondin, S., et al. 2009,
ApJ, 700, 1097, doi:10.1088/0004-637X/700/2/1097
Homan, Y., Courtois, H. M., & Tully, R. B. 2015,
MNRAS, 449, 4494, doi:10.1093/mnras/stv615
Homan, Y., Nusser, A., Valade, A., Libeskind, N. I., &
Tully, R. B. 2021, MNRAS, 505, 3380,
doi:10.1093/mnras/stab1457
Hong, T., Staveley-Smith, L., Masters, K. L., et al. 2019,
MNRAS, 487, 2061, doi:10.1093/mnras/stz1413
Howlett, C., Said, K., Lucey, J. R., et al. 2022, MNRAS,
515, 953, doi:10.1093/mnras/stac1681
Huchra, J. P., Macri, L. M., Masters, K. L., et al. 2012,
ApJS, 199, 26, doi:10.1088/0067-0049/199/2/26
Hudson, M. J., Lucey, J. R., Smith, R. J., Schlegel, D. J.,
& Davies, R. L. 2001, MNRAS, 327, 265,
doi:10.1046/j.1365-8711.2001.04786.x
Humphreys, E. M. L., Reid, M. J., Moran, J. M., Greenhill,
L. J., & Argon, A. L. 2013, ApJ, 775, 13,
doi:10.1088/0004-637X/775/1/13

## doi:10.1093/mnras/stac303 http://doi.org/10.1093/mnras/stac303
884, 82, doi:10.3847/1538-4357/ab4192 http://doi.org/10.3847/1538-4357/ab4192

861, 49, doi:10.3847/1538-4357/aac956 http://doi.org/10.3847/1538-4357/aac956

## MNRAS, 449, 4494, doi:10.1093/mnras/stv615 http://doi.org/10.1093/mnras/stv615

417, 553, doi:10.1086/173334 http://doi.org/10.1086/173334

## doi:10.1093/mnras/stab1457 http://doi.org/10.1093/mnras/stab1457

## doi:10.1093/mnras/stz205 http://doi.org/10.1093/mnras/stz205

515, 953, doi:10.1093/mnras/stac1681 http://doi.org/10.1093/mnras/stac1681

## doi:10.1093/mnras/stab2009 http://doi.org/10.1093/mnras/stab2009

## doi:10.1086/117391 http://doi.org/10.1086/117391

## doi:10.1088/0004-637X/775/1/13 http://doi.org/10.1088/0004-637X/775/1/13

473, 576, doi:10.1086/178173 http://doi.org/10.1086/178173

332, doi:10.1088/0004-6256/138/2/332 http://doi.org/10.1088/0004-6256/138/2/332
## doi:10.3847/1538-4357/835/1/28 http://doi.org/10.3847/1538-4357/835/1/28

## J. 2013, PASP, 125, 306, doi:10.1086/670067 http://doi.org/10.1086/670067

2498, doi:10.1086/301330 http://doi.org/10.1086/301330

## ApJ, 553, 47, doi:10.1086/320638 http://doi.org/10.1086/320638

## doi:10.1051/0004-6361/201833710 http://doi.org/10.1051/0004-6361/201833710

882, 34, doi:10.3847/1538-4357/ab2f73 http://doi.org/10.3847/1538-4357/ab2f73

808, 91, doi:10.1088/0004-637X/808/1/91 http://doi.org/10.1088/0004-637X/808/1/91
255, 21, doi:10.3847/1538-4365/ac01e7 http://doi.org/10.3847/1538-4365/ac01e7

## MNRAS, 433, 2240, doi:10.1093/mnras/stt893 http://doi.org/10.1093/mnras/stt893

122, doi:10.1086/512054 http://doi.org/10.1086/512054

## https://arxiv.org/abs/2204.12060 https://arxiv.org/abs/2204.12060

## doi:10.1093/mnras/231.2.149 http://doi.org/10.1093/mnras/231.2.149

## MNRAS, 513, 788, doi:10.1093/mnras/stac735 http://doi.org/10.1093/mnras/stac735
## ApJ, 624, 463, doi:10.1086/428890 http://doi.org/10.1086/428890

## doi:10.3847/1538-4357/aa76db http://doi.org/10.3847/1538-4357/aa76db

## MNRAS, 488, 5438, doi:10.1093/mnras/stz078 http://doi.org/10.1093/mnras/stz078

896, 3, doi:10.3847/1538-4357/ab901c http://doi.org/10.3847/1538-4357/ab901c

## doi:10.1086/339676 http://doi.org/10.1086/339676

Jacobs, B. A., Rizzi, L., Tully, R. B., et al. 2009, AJ, 138,
332, doi:10.1088/0004-6256/138/2/332
Jang, I. S., & Lee, M. G. 2017, ApJ, 835, 28,
doi:10.3847/1538-4357/835/1/28
Jarrett, T. H., Chester, T., Cutri, R., et al. 2000, AJ, 119,
2498, doi:10.1086/301330
Jasche, J., & Lavaux, G. 2019, A&A, 625, A64,
doi:10.1051/0004-6361/201833710
Jensen, J. B., Blakeslee, J. P., Gibson, Z., et al. 2015, ApJ,
808, 91, doi:10.1088/0004-637X/808/1/91
Jensen, J. B., Blakeslee, J. P., Ma, C.-P., et al. 2021, ApJS,
255, 21, doi:10.3847/1538-4365/ac01e7
Jha, S., Riess, A. G., & Kirshner, R. P. 2007, ApJ, 659,
122, doi:10.1086/512054
Jones, D. H., Read, M. A., Saunders, W., et al. 2009,
MNRAS, 399, 683, doi:10.1111/j.1365-2966.2009.15338.x
Kaiser, N. 1988, MNRAS, 231, 149,
doi:10.1093/mnras/231.2.149
Karachentsev, I. D., Makarova, L. N., Tully, R. B., et al.
2017, MNRAS, 469, L113, doi:10.1093/mnrasl/slx061
Kourkchi, E., & Tully, R. B. 2017, ApJ, 843, 16,
doi:10.3847/1538-4357/aa76db
Kourkchi, E., Tully, R. B., Anand, G. S., et al. 2020a, ApJ,
896, 3, doi:10.3847/1538-4357/ab901c
Kourkchi, E., Tully, R. B., Courtois, H. M., Dupuy, A., &
Guinet, D. 2022, MNRAS, 511, 6160,
doi:10.1093/mnras/stac303
Kourkchi, E., Tully, R. B., Neill, J. D., et al. 2019, ApJ,
884, 82, doi:10.3847/1538-4357/ab4192
Kourkchi, E., Tully, R. B., Eftekharzadeh, S., et al. 2020b,
ApJ, 902, 145, doi:10.3847/1538-4357/abb66b
Leavitt, H. S., & Pickering, E. C. 1912, Harvard College
Observatory Circular, 173, 1
Lee, M. G., Freedman, W. L., & Madore, B. F. 1993, ApJ,
417, 553, doi:10.1086/173334
Lelli, F., McGaugh, S. S., & Schombert, J. M. 2016, ApJL,
816, L14, doi:10.3847/2041-8205/816/1/L14
Lelli, F., McGaugh, S. S., Schombert, J. M., Desmond, H.,
& Katz, H. 2019, MNRAS, 484, 3267,
doi:10.1093/mnras/stz205
Lilow, R., & Nusser, A. 2021, MNRAS, 507, 1557,
doi:10.1093/mnras/stab2009
Lim, S. H., Mo, H. J., Lu, Y., Wang, H., & Yang, X. 2017,
MNRAS, 470, 2982, doi:10.1093/mnras/stx1462
Ma, C.-P., Greene, J. E., McConnell, N., et al. 2014, ApJ,
795, 158, doi:10.1088/0004-637X/795/2/158
Madore, B. F., & Freedman, W. L. 1995, AJ, 109, 1645,
doi:10.1086/117391
Magoulas, C., Springob, C. M., Colless, M., et al. 2012,
MNRAS, 427, 245, doi:10.1111/j.1365-2966.2012.21421.x

---

Mainzer, A., Bauer, J., Grav, T., et al. 2011, ApJ, 731, 53,
doi:10.1088/0004-637X/731/1/53
Makarov, D., Makarova, L., Rizzi, L., et al. 2006, AJ, 132,
2729, doi:10.1086/508925
Makarov, D. I., Zaitseva, N. A., & Bizyaev, D. V. 2018,
MNRAS, 479, 3373, doi:10.1093/mnras/sty1629
Makarova, L. N., Makarov, D. I., Karachentsev, I. D.,
Tully, R. B., & Rizzi, L. 2017, MNRAS, 464, 2281,
doi:10.1093/mnras/stw2502
Maoz, D., Mannucci, F., & Nelemans, G. 2014, ARA&A,
52, 107, doi:10.1146/annurev-astro-082812-141031
McGaugh, S. S. 2005, ApJ, 632, 859, doi:10.1086/432968
McGaugh, S. S., Schombert, J. M., Bothun, G. D., & de
Blok, W. J. G. 2000, ApJL, 533, L99, doi:10.1086/312628
McQuinn, K. B. W., Skillman, E. D., Dolphin, A. E., Berg,
D., & Kennicutt, R. 2017, AJ, 154, 51,
doi:10.3847/1538-3881/aa7aad
Mei, S., Blakeslee, J. P., C^ote, P., et al. 2007, ApJ, 655,
144, doi:10.1086/509598
Mendez, B., Davis, M., Moustakas, J., et al. 2002, AJ, 124,
213, doi:10.1086/341168
Monelli, M., Fiorentino, G., Bernard, E. J., et al. 2017,
ApJ, 842, 60, doi:10.3847/1538-4357/aa738d
Mould, J., Clementini, G., & Da Costa, G. 2019, PASA, 36,
e001, doi:10.1017/pasa.2018.46
Nagarajan, P., Weisz, D. R., & El-Badry, K. 2022, ApJ,
932, 19, doi:10.3847/1538-4357/ac69e6
Paturel, G., Garnier, R., Petit, C., & Marthinet, M. C.
1996, A&A, 311, 12
Pesce, D. W., Braatz, J. A., Reid, M. J., et al. 2020, ApJL,
891, L1, doi:10.3847/2041-8213/ab75f0
Phillips, M. M. 1993, ApJL, 413, L105, doi:10.1086/186970
Pietrzynski, G., Graczyk, D., Gallenne, A., et al. 2019,
Nature, 567, 200, doi:10.1038/s41586-019-0999-4
Prieto, J. L., Rest, A., & Suntze, N. B. 2006, ApJ, 647,
501, doi:10.1086/504307
Qin, F., Howlett, C., & Staveley-Smith, L. 2019, MNRAS,
487, 5235, doi:10.1093/mnras/stz1576
Qin, F., Howlett, C., Staveley-Smith, L., & Hong, T. 2018,
MNRAS, 477, 5150, doi:10.1093/mnras/sty928
Reid, M. J., Pesce, D. W., & Riess, A. G. 2019, ApJL, 886,
L27, doi:10.3847/2041-8213/ab552d
Rest, A., Scolnic, D., Foley, R. J., et al. 2014, ApJ, 795, 44,
doi:10.1088/0004-637X/795/1/44
Riess, A. G., Casertano, S., Yuan, W., et al. 2021, ApJL,
908, L6, doi:10.3847/2041-8213/abdbaf
Riess, A. G., Casertano, S., Yuan, W., Macri, L. M., &
Scolnic, D. 2019, ApJ, 876, 85,
doi:10.3847/1538-4357/ab1422

## http://doi.org/10.3847/2041-8213/ab75f0

## http://doi.org/10.1086/186970
## http://doi.org/10.1038/s41586-019-0999-4

## MNRAS, doi:10.1093/mnras/stab1446 http://doi.org/10.1093/mnras/stab1446

501, doi:10.1086/504307 http://doi.org/10.1086/504307
487, 5235, doi:10.1093/mnras/stz1576 http://doi.org/10.1093/mnras/stz1576

## doi:10.1051/0004-6361/201730499 http://doi.org/10.1051/0004-6361/201730499

## MNRAS, 477, 5150, doi:10.1093/mnras/sty928 http://doi.org/10.1093/mnras/sty928
## L27, doi:10.3847/2041-8213/ab552d http://doi.org/10.3847/2041-8213/ab552d

431, 1383, doi:10.1093/mnras/stt261 http://doi.org/10.1093/mnras/stt261

## doi:10.1088/0004-637X/795/1/44 http://doi.org/10.1088/0004-637X/795/1/44

## doi:10.1086/114847 http://doi.org/10.1086/114847

908, L6, doi:10.3847/2041-8213/abdbaf http://doi.org/10.3847/2041-8213/abdbaf

546, 681, doi:10.1086/318301 http://doi.org/10.1086/318301

## doi:10.3847/1538-4357/ab1422 http://doi.org/10.3847/1538-4357/ab1422

## doi:10.1088/0004-6256/149/2/54 http://doi.org/10.1088/0004-6256/149/2/54

## doi:10.1088/0004-637X/731/1/53 http://doi.org/10.1088/0004-637X/731/1/53
2729, doi:10.1086/508925 http://doi.org/10.1086/508925

861, 126, doi:10.3847/1538-4357/aac82e http://doi.org/10.3847/1538-4357/aac82e
934, L7, doi:10.3847/2041-8213/ac5c5b http://doi.org/10.3847/2041-8213/ac5c5b
815, doi:10.1086/516566 http://doi.org/10.1086/516566

## doi:10.1093/mnras/stw2502 http://doi.org/10.1093/mnras/stw2502

## Pietrinferni, A. 2017, A&A, 606, A33, http://doi.org/10.3847/1538-3881/aa7aad

Riess, A. G., Macri, L. M., Homann, S. L., et al. 2016,
ApJ, 826, 56, doi:10.3847/0004-637X/826/1/56
Riess, A. G., Casertano, S., Yuan, W., et al. 2018, ApJ,
861, 126, doi:10.3847/1538-4357/aac82e
Riess, A. G., Yuan, W., Macri, L. M., et al. 2022, ApJL,
934, L7, doi:10.3847/2041-8213/ac5c5b
Rizzi, L., Tully, R. B., Makarov, D., et al. 2007, ApJ, 661,
815, doi:10.1086/516566
Roman, M., Hardin, D., Betoule, M., et al. 2018, A&A,
615, A68, doi:10.1051/0004-6361/201731425
Salaris, M., & Cassisi, S. 2005, Evolution of Stars and
Stellar Populations
Scolnic, D., Brout, D., Carr, A., et al. 2021, arXiv e-prints,
arXiv:2112.03863.https://arxiv.org/abs/2112.03863
|. 2022, ApJ, 938, 113, doi:10.3847/1538-4357/ac8b7a
Serenelli, A., Weiss, A., Cassisi, S., Salaris, M., &
Pietrinferni, A. 2017, A&A, 606, A33,
doi:10.1051/0004-6361/201731004
Shaya, E. J., Tully, R. B., Homan, Y., & Pomarede, D.
2017, ApJ, 850, 207, doi:10.3847/1538-4357/aa9525
Skrutskie, M. F., Cutri, R. M., Stiening, R., et al. 2006, AJ,
131, 1163, doi:10.1086/498708
Soltis, J., Casertano, S., & Riess, A. G. 2021, ApJL, 908,
L5, doi:10.3847/2041-8213/abdbad
Sorce, J. G., Courtois, H. M., & Tully, R. B. 2012, AJ, 144,
133, doi:10.1088/0004-6256/144/5/133
Sorce, J. G., Tully, R. B., Courtois, H. M., et al. 2014,
MNRAS, 444, 527, doi:10.1093/mnras/stu1450
Springob, C. M., Masters, K. L., Haynes, M. P., Giovanelli,
R., & Marinoni, C. 2007, ApJS, 172, 599,
doi:10.1086/519527
Springob, C. M., Magoulas, C., Colless, M., et al. 2014,
MNRAS, 445, 2677, doi:10.1093/mnras/stu1743
Stahl, B. E., de Jaeger, T., Boruah, S. S., et al. 2021,
MNRAS, doi:10.1093/mnras/stab1446
Tempel, E., Saar, E., Liivamagi, L. J., et al. 2011, A&A,
529, A53, doi:10.1051/0004-6361/201016196
Tempel, E., Tuvikene, T., Kipper, R., & Libeskind, N. I.
2017, A&A, 602, A100,
doi:10.1051/0004-6361/201730499
Tempel, E., Tamm, A., Gramann, M., et al. 2014, A&A,
566, A1, doi:10.1051/0004-6361/201423585
Thomas, D., Steele, O., Maraston, C., et al. 2013, MNRAS,
431, 1383, doi:10.1093/mnras/stt261
Tonry, J., & Schneider, D. P. 1988, AJ, 96, 807,
doi:10.1086/114847
Tonry, J. L., Dressler, A., Blakeslee, J. P., et al. 2001, ApJ,
546, 681, doi:10.1086/318301
Tully, R. B. 2015a, AJ, 149, 54,
doi:10.1088/0004-6256/149/2/54

---

|. 2015b, AJ, 149, 171, doi:10.1088/0004-6256/149/5/171
Tully, R. B., Courtois, H. M., & Sorce, J. G. 2016, AJ, 152,
50, doi:10.3847/0004-6256/152/2/50
Tully, R. B., & Fisher, J. R. 1977, A&A, 54, 661
Tully, R. B., Shaya, E. J., Karachentsev, I. D., et al. 2008,
ApJ, 676, 184, doi:10.1086/527428
Tully, R. B., Courtois, H. M., Dolphin, A. E., et al. 2013,
AJ, 146, 86, doi:10.1088/0004-6256/146/4/86
Vogeley, M. S., Hoyle, F., Rojas, R. R., & Goldberg, D. M.
2004, in IAU Colloq. 195: Outskirts of Galaxy Clusters:
Intense Life in the Suburbs, ed. A. Diaferio, 5{11,
doi:10.1017/S1743921304000043
Walker, E. S., Baltay, C., Campillay, A., et al. 2015, ApJS,
219, 13, doi:10.1088/0067-0049/219/1/13
Watkins, R., & Feldman, H. A. 2015, MNRAS, 450, 1868,
doi:10.1093/mnras/stv651

## doi:10.3847/1538-4357/ab4bc9 http://doi.org/10.3847/1538-4357/ab4bc9

## doi:10.1017/S1743921304000043 http://doi.org/10.1017/S1743921304000043

913, 3, doi:10.3847/1538-4357/abf24a http://doi.org/10.3847/1538-4357/abf24a

219, 13, doi:10.1088/0067-0049/219/1/13 http://doi.org/10.1088/0067-0049/219/1/13
## http://doi.org/10.1093/mnras/stv651

50, doi:10.3847/0004-6256/152/2/50 http://doi.org/10.3847/0004-6256/152/2/50

## doi:10.1088/0004-6256/148/1/7 http://doi.org/10.1088/0004-6256/148/1/7

## ApJ, 676, 184, doi:10.1086/527428 http://doi.org/10.1086/527428

2000, AJ, 120, 1579, doi:10.1086/301513 http://doi.org/10.1086/301513

## AJ, 146, 86, doi:10.1088/0004-6256/146/4/86 http://doi.org/10.1088/0004-6256/146/4/86

Wright, E. L., Eisenhardt, P. R. M., Mainzer, A. K., et al.
2010, AJ, 140, 1868, doi:10.1088/0004-6256/140/6/1868
Wu, P.-F., Tully, R. B., Rizzi, L., et al. 2014, AJ, 148, 7,
doi:10.1088/0004-6256/148/1/7
York, D. G., Adelman, J., Anderson, John E., J., et al.
2000, AJ, 120, 1579, doi:10.1086/301513
Yuan, W., Riess, A. G., Macri, L. M., Casertano, S., &
Scolnic, D. M. 2019, ApJ, 886, 61,
doi:10.3847/1538-4357/ab4bc9
Yuan, W., Fausnaugh, M. M., Homann, S. L., et al. 2020,
ApJ, 902, 26, doi:10.3847/1538-4357/abb377
Yuan, W., Macri, L. M., Peterson, B. M., et al. 2021, ApJ,
913, 3, doi:10.3847/1538-4357/abf24a
Zgirski, B., Gieren, W., Pietrzynski, G., et al. 2017, ApJ,
847, 88, doi:10.3847/1538-4357/aa88c4

──────── [TRUNCATED] ────────
Showing 44,956 chars (head) + 14,999 chars (tail) of 145,987 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-4b36d0ba43.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-4b36d0ba43.md" offset=1153 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
