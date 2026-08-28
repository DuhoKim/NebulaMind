URL: https://www.sdss4.org/dr12/algorithms/magnitudes

- [Datasets](https://www.sdss4.org/dr12/data_access/)
- [Imaging Data](https://www.sdss4.org/dr12/imaging/)
- [Optical Spectra](https://www.sdss4.org/dr12/spectro/)
- [APOGEE Spectra](https://www.sdss4.org/dr12/irspec/)
- [MARVELS Spectra](https://www.sdss4.org/dr12/marvels/)
- [Algorithms](https://www.sdss4.org/dr12/algorithms/)
- [Software](https://www.sdss4.org/dr12/software/)
- [Help](https://www.sdss4.org/dr12/help/)
- [Tutorials](https://www.sdss4.org/dr12/tutorials/)

# Measures of Flux and Magnitude

## Introduction

This page provides detailed descriptions of various measures of magnitude and related outputs of the photometry pipelines. We also provide discussion of some methodology. For details of the Photo pipeline processing please read the [corresponding EDR paper section](http://www.adsabs.harvard.edu/abs/2002AJ....123..485S) (section 4.4). There is also a separate page describing the [photometric flux calibration](https://www.sdss4.org/dr12/algorithms/fluxcal/).

Jump to:

- [Nanomaggies](https://www.sdss4.org/dr12/algorithms/magnitudes/#nmgy)
- [Asinh Magnitudes](https://www.sdss4.org/dr12/algorithms/magnitudes/#asinh)
- [Fiber Magnitudes](https://www.sdss4.org/dr12/algorithms/magnitudes/#mag_fiber)
- [Model Magnitudes](https://www.sdss4.org/dr12/algorithms/magnitudes/#mag_model)
- [cModel Magnitudes](https://www.sdss4.org/dr12/algorithms/magnitudes/#cmodel)
- [Petrosian Magnitudes](https://www.sdss4.org/dr12/algorithms/magnitudes/#mag_petro)
- [PSF Magnitudes](https://www.sdss4.org/dr12/algorithms/magnitudes/#mag_psf)
- [Extinction](https://www.sdss4.org/dr12/algorithms/magnitudes/#extinction)
- [Which Magnitude To Use?](https://www.sdss4.org/dr12/algorithms/magnitudes/#which_mags)
- [Object Radial Profiles](https://www.sdss4.org/dr12/algorithms/magnitudes/#photo_profile)

## Flux units: maggies and nanomaggies

In SDSS-III, we express all fluxes in terms of nanomaggies, which are a convenient linear unit. For example, quantities labeled petroFlux, psfFlux, etc. are (unless otherwise stated) in these units. In each case, there is a corresponding [asinh magnitude](https://www.sdss4.org/dr12/algorithms/magnitudes/#asinh), such as petroMag, psfMag etc., explained further below.

A “maggy” is the flux f of the source relative to the standard source f0 (which defines the zeropoint of the magnitude scale). Therefore, a “nanomaggy” is 10-9 times a maggy. To relate these quantities to standard magnitudes, an object with flux f given in nMgy has a [Pogson magnitude](https://www.sdss4.org/dr12/help/glossary/#mag_pogson):

m = \[22.5 mag\] – 2.5 log10f.

Note that magnitudes listed in the SDSS catalog, however, are _not_ standard Pogson magnitudes, but [asinh magnitudes](https://www.sdss4.org/dr12/algorithms/magnitudes/#asinh).

The standard source for each SDSS band is close to but not exactly the AB source (3631 Jy), meaning that a nanomaggy is approximately 3.631×10-6 Jy. However, our current understanding is that the absolute calibration of the SDSS system has some percent-level offsets relative to AB, discussed in detail in the section on [AB calibration](https://www.sdss4.org/dr12/algorithms/fluxcal/#SDSStoAB).

## SDSS Asinh Magnitudes

Magnitudes within the SDSS are expressed as inverse hyperbolic sine (or “asinh”) magnitudes, described in detail by [Lupton, Gunn & Szalay (1999)](http://adsabs.harvard.edu/abs/1999AJ....118.1406L). They are sometimes referred to informally as _luptitudes_. The transformation from linear flux measurements to asinh magnitudes is designed to be virtually identical to the standard astronomical magnitude at high signal-to-noise ratio, but to behave reasonably at low signal-to-noise ratio and even at negative values of flux, where the logarithm in the [Pogson magnitude](https://www.sdss4.org/dr12/help/glossary/#mag_pogson) fails. This allows us to report a magnitude even in the absence of a formal detection; we quote no upper limits in our photometry.

The asinh magnitudes are characterized by a softening parameter b, the typical 1-sigma noise of the sky in a PSF aperture in 1′′ seeing. The relation between detected flux f and asinh magnitude m is:

m = -2.5/ln(10) \* \[asinh((f/f0)/(2b)) \+ ln(b)\].

Here, f0 is given by the _classical_ zero point of the magnitude scale, _i.e._, f0 is the flux of an object with _conventional_ magnitude of zero. The quantity b is measured relative to f0, and thus is in maggies; it is given in the [table of asinh softening parameters](https://www.sdss4.org/dr12/algorithms/magnitudes/#asinh_table) below (Table 21 in the [EDR paper](http://www.adsabs.harvard.edu/abs/2002AJ....123..485S)), along with the asinh magnitude associated with a zero flux object. The table also lists the flux corresponding to 10f0, above which the asinh magnitude and the traditional logarithmic magnitude differ by less than 1% in flux. For details on converting asinh magnitudes to other flux measures, see [converting counts to magnitudes](https://www.sdss4.org/dr12/algorithms/fluxcal/#counts2mag).

| Filter | b | Zero-flux Magnitude \[m(f/f0 = 0)\] | m(f/f0 = 10b) |
| --- | --- | --- | --- |
| u | 1.4×10-10 | 24.63 | 22.12 |
| g | 0.9×10-10 | 25.11 | 22.60 |
| r | 1.2×10-10 | 24.80 | 22.29 |
| i | 1.8×10-10 | 24.36 | 21.85 |
| z | 7.4×10-10 | 22.83 | 20.32 |

Asinh Softening Parameters

[\[Back to top\]](https://www.sdss4.org/dr12/algorithms/magnitudes/#intro)

## Fiber Magnitudes: fiberMag and fiber2Mag

Fiber magnitudes reflect the flux contained within the aperture of an [spectroscopic fiber](https://www.sdss4.org/dr12/help/glossary/#fiber) in each band. In the case of fiberMag we assume an aperture appropriate to the SDSS spectrograph (3′′ in diameter). In the case of fiber2Mag we assume an aperture appropriate to the BOSS spectrograph (2′′ in diameter).

- For [children](https://www.sdss4.org/dr12/help/glossary/#child) of [deblended](https://www.sdss4.org/dr12/help/glossary/#deblend) galaxies, some of the pixels within a 1.5′′ radius may belong to other children; we now measure the flux of the parent at the position of the child; this properly reflects the amount of light which the spectrograph will see.
- Images are convolved to 2′′ seeing before fiberMags are measured. This also makes the fiber magnitudes closer to what is seen by the spectrograph.

[\[Back to top\]](https://www.sdss4.org/dr12/algorithms/magnitudes/#intro)

## Model Magnitudes: devMag, expMag, modelMag

There are several “model” magnitudes associated with each catalog object. First, there are devMag and expMag magnitudes, associated with de Vaucouleurs and exponential model fits, as explained more fully below. These magnitudes are calculated from independent models in each band. Second, there is modelMag, which uses the better of the two fits in the r-band as a matched aperture to calculate the flux in all bands. For extended objects, modelMag usually provides the best available SDSS colors.

Just as the [PSF magnitudes](https://www.sdss4.org/dr12/algorithms/magnitudes/#mag_psf) are optimal measures of the fluxes of stars, the optimal measure of the flux of a galaxy uses a matched galaxy model. With this in mind, the code fits two models to the two-dimensional image of each object in each band:

1. **A pure de Vaucouleurs profile**: I(r) = I0 exp{-7.67 \[(r/re)1/4\]} (truncated beyond _7re_ to smoothly go to zero at _8re_, and with some softening within _r=re/50_).
2. **A pure exponential profile**: I(r) = I0 exp(-1.68r/re) (truncated beyond _3re_ to smoothly go to zero at _4re_.

Each model has an arbitrary axis ratio and position angle. Although for large objects it is possible and even desirable to fit more complicated models ( _e.g._, bulge plus disk), the computational expense to compute them is not justified for the majority of the detected objects. The models are convolved with a double-Gaussian fit to the PSF, which is provided by `psp`. Residuals between the double-Gaussian and the full KL PSF model are added on for just the central PSF component of the image. These fitting procedures yield the quantities:

- `rdeV` and `rExp`, the effective radii of the models;
- `abDeV` and `abExp`, the axis ratio of the best fit models;
- `phiDeV` and `phiExp`, the position angles of the ellipticity (in degrees East of North).
- `deVlnL` and `explnL`, the likelihoods associated with each model from the chi-squared fit;
- `deVMag` and `expMag`, the total magnitudes associated with each fit.

Note that these quantities roughly correctly model the effects of the PSF. Errors for each of the last two quantities (which are based only on photon statistics) are also reported. We apply aperture corrections to make these model magnitudes equal the PSF magnitudes in the case of an unresolved object.

In order to measure unbiased colors of galaxies, we measure their flux through equivalent apertures in all bands. We choose the model (exponential or de Vaucouleurs) of higher likelihood in the _r_ filter, and apply that model ( _i.e._, allowing only the amplitude to vary) in the other bands after convolving with the appropriate PSF in each band. The resulting magnitudes are termed `modelMag`. The resulting estimate of galaxy color will be unbiased in the absence of color gradients. Systematic differences from Petrosian colors are in fact often seen due to color gradients, in which case the concept of a global galaxy color is somewhat obviously aperture-dependent. For faint galaxies, the model colors have appreciably higher signal-to-noise ratio than do the Petrosian colors.

For the current version of the photometric pipeline, the model magnitude is a good proxy for point spread function (PSF) magnitude for point sources, and Petrosian magnitude (which have larger errors than model magnitude) for extended sources.

Due to the way in which model fits are carried out, there is some weak discretization of model parameters, including `rExp` and `rDeV` but especially `phiDeV` and `phiDeV`.

[\[Back to top\]](https://www.sdss4.org/dr12/algorithms/magnitudes/#intro)

## Composite Model Magnitudes: cModelMag

The code also takes the best fit exponential and de Vaucouleurs fits in each band and asks for the linear combination of the two that best fits the image. The coefficient (clipped between zero and one) of the de Vaucouleurs term is stored in the quantity `fracDeV`. From this we calculate and store a composite flux as follows:

`Fcomposite` = `fracDeV``FdeV` \+ (1 – `fracDeV`) `Fexp`,

where `FdeV` and `Fexp` are the de Vaucouleurs and exponential fluxes ( _not_ magnitudes) of the object in question. The magnitude derived from `Fcomposite` is referred to below as the `cmodel` magnitude (as distinct from the `model` magnitude, which is based on the better-fitting of the exponential and de Vaucouleurs models in the _r_ band).

There is excellent agreement between `cmodel` and Petrosian magnitudes of galaxies, and `cmodel` and PSF magnitudes of stars. `Cmodel` and Petrosian magnitudes are not expected to be identical, of course; as [Strauss et al. (2002)](http://adsabs.harvard.edu/abs/2002AJ....124.1810S) describe, the Petrosian aperture excludes the outer parts of galaxy profiles, especially for elliptical galaxies. As a consequence, there is an offset of 0.05-0.1 mag between `cmodel` and Petrosian magnitudes of bright galaxies, depending on the photometric bandpass and the type of galaxy. The rms scatter between model and Petrosian magnitudes at the bright end is between 0.05 and 0.08 magnitudes, depending on bandpass; the scatter between `cmodel` and Petrosian magnitudes for galaxies is smaller, 0.03 to 0.05 magnitudes.

The `cmodel` and PSF magnitudes of stars are in good agreement (they are forced to be identical in the mean by aperture corrections, as was true in older versions of the pipeline). The rms scatter between model and PSF magnitudes for stars is much reduced, going from 0.03 mag to 0.02 magnitudes, the exact values depending on bandpass. In the EDR and DR1, star-galaxy separation was based on the difference between model and PSF magnitudes. We do star-galaxy separation using the difference between `cmodel` and PSF magnitudes, with the threshold at the same value (0.145 magnitudes).

Please note that while cModelMag is a good total flux indicator, it is based on the independent model fits (devMag and expMag) in each bandpass. For that reason, it generally does _not_ yield as a high signal-to-noise color as the aperture-matched modelMag values do. For this reason, photometric redshift algorithms and other color-sensitive procedures are usually better off relying on modelMag.

[\[Back to top\]](https://www.sdss4.org/dr12/algorithms/magnitudes/#intro)

## Petrosian Magnitudes: petroMag

For galaxy photometry, measuring flux is more difficult than for stars, because galaxies do not all have the same radial surface brightness profile, and have no consistently distinct edges. In order to avoid biases, we wish to measure a constant fraction of the total light, independent of the position and distance of the object. To satisfy these requirements, the SDSS has adopted a modified form of the [Petrosian (1976)](http://adsabs.harvard.edu/abs/1976ApJ...209L...1P) system, measuring galaxy fluxes within a circular aperture whose radius is defined by the shape of the azimuthally averaged light profile.

We define the “Petrosian ratio” RP at a radius r from the center of an object to be the ratio of the local surface brightness in an annulus at r to the mean surface brightness within r, as described by [Blanton et al. (2001)](http://adsabs.harvard.edu/abs/2001AJ....121.2358B) and [Yasuda et al. (2001)](http://adsabs.harvard.edu/abs/2001AJ....122.1104Y):

|     |
| --- |
| ![eqn 1](https://www.sdss4.org/wp-content/uploads/2014/10/petroeq1.gif) |

where I(r) is the azimuthally averaged surface brightness profile. The Petrosian radius rP is defined as the radius at which RP(rP) equals some specified value RP,lim, set to 0.2 in our case. The Petrosian flux in any band is then defined as the flux within a certain number NP (equal to 2.0 in our case) of r Petrosian radii:

|     |
| --- |
| ![eqn 2](https://www.sdss4.org/wp-content/uploads/2014/10/petroeq2.gif) |

In the SDSS five-band photometry, the aperture in all bands is set by the profile of the galaxy in the r band alone. This procedure ensures that the color measured by comparing the Petrosian flux FP in different bands is measured through a consistent aperture.

The aperture 2rP is large enough to contain nearly all of the flux for typical galaxy profiles, but small enough that the sky noise in FP is small. Thus, even substantial errors in rP cause only small errors in the Petrosian flux (typical statistical errors near the spectroscopic flux limit of r ~17.7 are < 5%), although these errors are correlated.

The Petrosian radius in each band is the parameter `petroRad`, and the Petrosian magnitude in each band (calculated, remember, using only `petroRad` for the _r_ band) is the parameter `petroMag`.

In practice, there are a number of complications associated with this definition, because noise, substructure, and the finite size of objects can cause objects to have no Petrosian radius, or more than one. Those with more than one are flagged as `MANYPETRO`; the largest one is used. Those with none have `NOPETRO` set. Most commonly, these objects are faint ( _r_ \> 20.5 or so); the Petrosian ratio becomes unmeasurable before dropping to the limiting value of 0.2; these have `PETROFAINT` set and have their “Petrosian radii” set to the default value of the larger of 3′′ or the outermost measured point in the radial profile. Finally, a galaxy with a bright stellar nucleus, such as a Seyfert galaxy, can have a Petrosian radius set by the nucleus alone; in this case, the Petrosian flux misses most of the extended light of the object. This happens quite rarely, but one dramatic example is the Seyfert galaxy NGC 7603 = Arp 092, at RA(2000) = 23:18:56.6, Dec(2000) = +00:14:38.

How well does the Petrosian magnitude perform as a reliable and complete measure of galaxy flux? Theoretically, the Petrosian magnitudes defined here should recover essentially all of the flux of an exponential galaxy profile and about 80% of the flux for a de Vaucouleurs profile. As shown by Blanton et al. (2001), this fraction is fairly constant with axis ratio, while as galaxies become smaller (due to worse seeing or greater distance) the fraction of light recovered becomes closer to that fraction measured for a typical PSF, about 95% in the case of the SDSS. This implies that the fraction of flux measured for exponential profiles decreases while the fraction of flux measured for de Vaucouleurs profiles increases as a function of distance. However, for galaxies in the spectroscopic sample ( _r_ < 17.7), these effects are small; the Petrosian radius measured by `frames` is extraordinarily constant in physical size as a function of redshift.

[\[Back to top\]](https://www.sdss4.org/dr12/algorithms/magnitudes/#intro)

## PSF Magnitudes: psfMag

For isolated stars, which are well-described by the point spread function (PSF), the optimal measure of the total flux is determined by fitting a PSF model to the object. In practice, we do this by sync-shifting the image of a star so that it is exactly centered on a pixel, and then fitting a Gaussian model of the PSF to it. This fit is carried out on the local PSF KL model at each position as well; the difference between the two is then a local aperture correction, which gives a corrected PSF magnitude. Finally, we use bright stars to determine a further aperture correction to a radius of 7.4′′ as a function of seeing, and apply this to each frame based on its seeing. This involved procedure is necessary to take into account the full variation of the PSF across the field, including the low signal-to-noise ratio wings. Empirically, this reduces the seeing-dependence of the photometry to below 0.02 mag for seeing as poor as 2′′. The resulting magnitude is stored in the quantity `psfMag`.

The flag `PSF_FLUX_INTERP` warns that the PSF photometry might be suspect. The flag `BAD_COUNTS_ERROR` warns that because of interpolated pixels, the error may be under-estimated.

[\[Back to top\]](https://www.sdss4.org/dr12/algorithms/magnitudes/#intro)

## Extinction Correction

Galactic extinction corrections in magnitudes at the position of each object, `extinction`, are computed following Schlegel, Finkbeiner & Davis (1998). These corrections are _not_ applied to the magnitudes in the databases unless otherwise noted; if desired, they must be explicitly applied by the user.

The conversions we use from E(B–V) to total extinction Aλ, assuming a z=0 elliptical galaxy spectral energy distribution, are tabulated in Table 22 of the EDR Paper.

[\[Back to top\]](https://www.sdss4.org/dr12/algorithms/magnitudes/#intro)

## Which Magnitude Should I Use?

Faced with this array of different magnitude measurements to choose from, which one is appropriate in which circumstances? We cannot give any guarantees of what is appropriate for the science _you_ want to do, but here we present some examples, where we use the general guideline that one usually wants to maximize some combination of signal-to-noise ratio, fraction of the total flux included, and freedom from systematic variations with observing conditions and distance.

Given the excellent agreement between `cmodel` magnitudes (see [cmodel magnitudes](https://www.sdss4.org/dr12/algorithms/magnitudes/#cmodel) above) and PSF magnitudes for point sources, and between `cmodel` magnitudes and Petrosian magnitudes (albeit with intrinsic offsets due to aperture corrections) for galaxies, the `cmodel` magnitude is now an adequate proxy to use as a universal magnitude for all types of objects. As it is approximately a matched aperture to a galaxy, it has the great advantage over Petrosian magnitudes, in particular, of having close to optimal noise properties.

### Example magnitude usage

- **Photometry of Bright Stars**: If the objects are bright enough, add up all the flux from the profile `profMean` and generate a large aperture magnitude. We recommend using the first 7 annuli.
- **Photometry of Distant Quasars**: These will be unresolved, and therefore have images consistent with the PSF. For this reason, `psfMag` is unbiased and optimal.
- **Colors of Stars**: Again, these objects are unresolved, and `psfMag` is the optimal measure of their brightness.
- **Photometry of Nearby Galaxies**: Galaxies bright enough to be included in our spectroscopic sample have relatively high signal-to-noise ratio measurements of their Petrosian magnitudes. Since these magnitudes are model-independent and yield a large fraction of the total flux, roughly constant with redshift, `petroMag` is the measurement of choice for such objects. In fact, the noise properties of Petrosian magnitudes remain good to _r=20_ or so.
- **Photometry of Galaxies**: Under most conditions, the `cmodel` magnitude is now a reliable estimate of the galaxy flux. In addition, this magnitude account for the effects of local seeing and thus are less dependent on local seeing variations.
- **Colors of Galaxies**: For measuring _colors_ of extended objects, we continue to recommend using the model (not the `cmodel`) magnitudes. The model magnitude is calculated using the best-fit parameters in the _r_ band, and applies it to all other bands; the light is therefore measured consistently through the same aperture in all bands.

Of course, it would _not_ be appropriate to study the evolution of galaxies and their colors by using Petrosian magnitudes for bright galaxies, and model magnitudes for faint galaxies, without fully modeling and accounting for the resulting aperture corrections.

Finally, we note that azimuthally-averaged radial profiles are also provided, as described [below](https://www.sdss4.org/dr12/algorithms/magnitudes/#photo_profile), and can easily be used to create circular aperture magnitudes of any desired type. For instance, to study a large dynamic range of galaxy fluxes, one could measure alternative Petrosian magnitudes with parameters tuned such that the Petrosian flux includes a small fraction of the total flux, but yields higher signal-to-noise ratio measurements at faint magnitudes.

[\[Back to top\]](https://www.sdss4.org/dr12/algorithms/magnitudes/#intro)

## Radial Profiles

The ` frames` pipeline extracts an azimuthally-averaged radial surface brightness profile. In the catalogs, it is given as the average surface brightness in a series of annuli. This quantity is in units of [nanomaggies](https://www.sdss4.org/dr12/algorithms/magnitudes/#nmgy) per square arcsec, as described above. The number of annuli for which there is a measurable signal is listed as `nprof` (in CAS, in the photoObjAll table). The mean surface brightness is listed as ` profMean`, and the error is listed as `profErr` (in CAS, both of these values are stored separately in the photoProfile table). The error includes both photon noise, and the small-scale “bumpiness” in the counts as a function of azimuthal angle.

When converting the `profMean` values to a local surface brightness, it is not the best approach to assign the mean surface brightness to some radius within the annulus and then linearly interpolate between radial bins. Do not use smoothing splines, as they will not go through the points in the cumulative profile and thus (obviously) will not conserve flux. What `frames` does, _e.g._, in determining the Petrosian ratio, is to fit a taut spline to the _cumulative_ profile and then differentiate that spline fit, after transforming both the radii and cumulative profiles with asinh functions. We recommend doing the same here.

The annuli used are:

| Aperture | Radius (pixels) | Radius (arcsec) | Area (pixels) |
| --- | --- | --- | --- |
| 1 | 0.56 | 0.23 | 1 |
| 2 | 1.69 | 0.68 | 9 |
| 3 | 2.58 | 1.03 | 21 |
| 4 | 4.41 | 1.76 | 61 |
| 5 | 7.51 | 3.00 | 177 |
| 6 | 11.58 | 4.63 | 421 |
| 7 | 18.58 | 7.43 | 1085 |
| 8 | 28.55 | 11.42 | 2561 |
| 9 | 45.50 | 18.20 | 6505 |
| 10 | 70.15 | 28.20 | 15619 |
| 11 | 110.50 | 44.21 | 38381 |
| 12 | 172.50 | 69.00 | 93475 |
| 13 | 269.50 | 107.81 | 228207 |
| 14 | 420.50 | 168.20 | 555525 |
| 15 | 657.50 | 263.00 | 1358149 |

[\[Back to top\]](https://www.sdss4.org/dr12/algorithms/magnitudes/#intro)
