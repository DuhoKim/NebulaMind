# URL: https://www.sdss4.org/dr17/algorithms/classify/

- [Datasets](https://www.sdss4.org/dr17/data_access/)
- [Imaging Data](https://www.sdss4.org/dr17/imaging/)
- [Optical\\
\\
SpectraeBOSS, SPIDERS, TDSS, BOSS, SEGUE, SDSS-I/II](https://www.sdss4.org/dr17/spectro/)
- [APOGEE\\
\\
IR Spectra](https://www.sdss4.org/dr17/irspec/)
- [MaStar\\
\\
Library](https://www.sdss4.org/dr17/mastar/)
- [MaNGA\\
\\
IFU Spectra](https://www.sdss4.org/dr17/manga/)
- [Algorithms](https://www.sdss4.org/dr17/algorithms/)
- [Help](https://www.sdss4.org/dr17/help/)
- [Tutorials](https://www.sdss4.org/dr17/tutorials/)

# Morphology/Classification

[Table of Contents](https://www.sdss4.org/dr17/algorithms/classify/#toc-body)

- Morphology/Classification

  - Overview
  - Star/Galaxy Classification
  - Surface Brightness & Concentration Index
  - Model Fit Likelihood and Parameters
  - Ellipticities
  - Isophotal Quantities
  - Adaptive Moments

## Overview

This page provides detailed descriptions of various morphological outputs of the photometry pipelines. We also provide discussion of some methodology; for details of the Photo pipeline processing please read the corresponding section in [the EDR paper](http://adsabs.harvard.edu/abs/2002AJ....123..485S). Other photometric outputs, specifically the various magnitudes, are described on the [Magnitudes](https://www.sdss4.org/dr17/algorithms/magnitudes/) page.

## Star/Galaxy Classification

The `frames` pipeline provides a simple star/galaxy separator in its `type`parameters (provided separately for each band) and its `objc_type` parameters (one value per object); these are set to:

| Class | Name | Code |
| --- | --- | --- |
| Unknown | UNK | 0 |
| Cosmic Ray | CR | 1 |
| Defect | DEFECT | 2 |
| Galaxy | GALAXY | 3 |
| Ghost | GHOST | 4 |
| Known object | KNOWNOBJ | 5 |
| Star | STAR | 6 |
| Star trail | TRAIL | 7 |
| Sky | SKY | 8 |

The photometric pipeline version used for DR2 and later data (5\_4) classifies objects as extended ("galaxy") or point-like ("star") based on the difference between the [cmodel](https://www.sdss4.org/dr17/help/glossary/#mag_cmodel) and [PSF](https://www.sdss4.org/dr17/help/glossary/#mag_psf) magnitude. An object is classified as extended if

psfMag - cmodelMag > 0.145.

If satisfied, `type` is set to `GALAXY` for that band; otherwise, `type` is set to `STAR`. The global type `objc_type` is set according to the same criterion, applied to the summed fluxes from all bands in which the object is detected.

Experimentation has shown that simple variants on this scheme, such as defining galaxies as those objects classified as such in any two of the three high signal-to-noise ratio bands (namely, _g_, _r_, and _i_), work better in some circumstances. This scheme occasionally fails to distinguish pairs of stars with separation small enough (<2'') that the deblender does not split them; it also occasionally classifies Seyfert galaxies with particularly bright nuclei as stars.

Further information to refine the star-galaxy separation further may be used, depending on scientific application. For example, [Scranton et al. (2002)](http://adsabs.harvard.edu/abs/2002ApJ...579...48S) advocate applying a Bayesian prior to the above difference between the PSF and exponential magnitudes, depending on seeing and using prior knowledge about the counts of galaxies and stars with magnitude.

[Back to Top](https://www.sdss4.org/dr17/algorithms/classify/#)

## Surface Brightness & Concentration Index

The `frames` pipeline also reports the radii containing 50% and 90% of the Petrosian flux for each band, ` petroR50` and ` petroR90` respectively. The usual characterization of surface-brightness in the target selection pipeline of the SDSS is the mean surface brightness within `petroR50`. It turns out that the ratio of ` petroR50` to ` petroR90`, the so-called "inverse concentration index", is correlated with morphology ( [Shimasaku et al. 2001](http://adsabs.harvard.edu/abs/2001AJ....122.1238S), [Strateva et al. 2001](http://adsabs.harvard.edu/abs/2001AJ....122.1861S)). Galaxies with a de Vaucouleurs profile have an inverse concentration index of around 0.3; exponential galaxies have an inverse concentration index of around 0.43. Thus, this parameter can be used as a simple morphological classifier.

An important caveat when using these quantities is that they are _not_ corrected for seeing. This causes the surface brightness to be underestimated, and the inverse concentration index to be overestimated, for objects of size comparable to the PSF. The amplitudes of these effects, however, are not yet well characterized.

[Back to Top](https://www.sdss4.org/dr17/algorithms/classify/#)

## Model Fit Likelihood and Parameters

In addition to the model and PSF magnitudes described on the [Magnitudes](https://www.sdss4.org/dr17/algorithms/magnitudes/) page, the likelihoods ` deV_L`, ` exp_L`, and ` star_L` are also calculated by ` frames`. These are the probabilities of achieving the measured chi-squared for the de Vaucouleurs, exponential, and PSF fits, respectively. For instance, `star_L` is the probability that an object would have at least the measured value of chi-squared if it is really well represented by a PSF. If one wishes to make use of a trinary scheme to classify objects, calculation of the fractional likelihoods is recommended:

f(deV\_L) = deV\_L/\[deV\_L+exp\_L+star\_L\]

and similarly for `f(exp_L)` and `f(star_L)`. A fractional likelihood greater than 0.5 for any of these three profiles is generally a good threshold for object classification. This works well in the range 18< _r_ <21.5; at the bright end, the likelihoods have a tendency to underflow to zero, which makes them less useful. In particular, ` star_L` is often zero for bright stars.

[Back to Top](https://www.sdss4.org/dr17/algorithms/classify/#)

## Ellipticities

The model fits yield an estimate of the axis ratio and position angle of each object, but it is useful to have model-independent measures of ellipticity. In the data released here, ` frames` provides two further measures of ellipticity, one based on second moments, the other based on the ellipticity of a particular isophote. The model fits do correctly account for the effect of the seeing, while the methods presented here do not.

The first method measures flux-weighted second moments, defined as:

Mxx = <x2/r2>

Myy = <y2/r2>

Mxy = <xy/r2>

In the case that the object's isophotes are self-similar ellipses, one can show:

Q = Mxx \- Myy = \[(a-b)/(a+b)\]cos(2φ)

U = Mxy = \[(a-b)/(a+b)\]sin(2φ)

where a and bare the semi-major and semi-minor axes, and φ is the position angle. Q and U are `Q` and `U`in `PhotoObj` and are referred to as "Stokes parameters." They can be used to reconstruct the axis ratio and position angle, measured relative to row and column of the CCDs. This is equivalent to the normal definition of position angle (East of North), for the scans on the Equator. The performance of the Stokes parameters are not ideal at low S/N. As of DR1, `frames` provides measurements of adaptive moments which are better shape estimators than the Stokes parameters. Read the [detailed description of adaptive moments](https://www.sdss4.org/dr17/algorithms/classify/#photo_adaptive).

[Back to Top](https://www.sdss4.org/dr17/algorithms/classify/#)

## Isophotal Quantities

**As of DR8, the isophotal quantities are only retained in the uncalibrated files. Because they are generally unreliable measurements, we have dropped them from the photoObj files and from CAS.** For completeness, we note that these measures of ellipticity use the ellipticity of the 25 magnitudes per square arcsecond isophote (in all bands). In detail, `frames` measures the radius of a particular isophote as a function of angle and Fourier expands this function. It then extracts from the coefficients the centroid (`isoRowC,isoColC`), major and minor axis (`isoA,isoB`), position angle (`isoPhi`), and average radius of the isophote in question (`Profile`). It also reports the derivative of each of these quantities with respect to isophote level, necessary to recompute these quantities if the photometric calibration changes.

[Back to Top](https://www.sdss4.org/dr17/algorithms/classify/#)

## Adaptive Moments

Adaptive moments are the second moments of the object intensity, measured using a particular scheme designed to have near-optimal signal-to-noise ratio. Moments are measured using a radial weight function iteratively adapted to the shape (ellipticity) and size of the object. This elliptical weight function has a signal-to-noise advantage over axially symmetric weight functions. In principle there is an optimal (in terms of signal-to-noise) radial shape for the weight function, which is related to the light profile of the object itself. In practice a Gaussian with size matched to that of the object is used, and is nearly optimal. Details can be found in [Bernstein & Jarvis (2002)](http://adsabs.harvard.edu/abs/2002AJ....123..583B).

The outputs included in the SDSS data release are the following. **Note**: the outputs are the parameters of the matched gaussian rather than actual measured moments, but we will use the moment notation below for clarity.

1. The sum of the second moments in the CCD row and column direction:

`mrr_cc = <col2> + <row2>`


and its error `mrr_cc_err`.


The second moments are defined in the following way:

` <col2>= sum[I(col,row) w(col,row) col2]/sum[I*w]`


where `I` is the intensity of the object and `w` is the weight function.
2. The ellipticity (polarization) components:

`me1 = <col2> - <row2>)/mrr_cc

me2 = 2.*<col*row>/mrr_cc`


and square root of the components of the covariance matrix:`

me1e1err = sqrt( Var(e1) )

me1e2err = sign(Covar(e1,e2))*sqrt( abs( Covar(e1,e2) ) )

me2e2err = sqrt( Var(e2) )`
3. A fourth-order moment

`mcr4 = <r4>/sigma4`


where `r2 = col2 + row2`, and sigma is the size of the gaussian weight. No error is quoted on this quantity.
4. These quantities are also measured for the PSF, reconstructed at the position of the object. The names are the same with an appended `_psf`. No errors are quoted for PSF quantities. These PSF moments can be used to correct the object shapes for smearing due to seeing and PSF anisotropy using the following formulas:


e1 = (e1meas - R\*e1psf)/(1-R)


e2 = (e2meas - R\*e2psf)/(1-R)


R = mrr\_cc\_psf/mrr\_cc\*(4/mcr4\_psf-1)/(4/mcr4-1)


But as Hirata & Seljak point out, this formula results in a small bias. See [Bernstein & Jarvis (2002)](http://adsabs.harvard.edu/abs/2002AJ....123..583B) and [Hirata & Seljak (2003)](http://adsabs.harvard.edu/abs/2003MNRAS.343..459H) for details and more accurate correction formulas. In particular, Hirata & Seljak give accurate correction formulas that use only the above measured parameters.

[Back to Top](https://www.sdss4.org/dr17/algorithms/classify/#)