URL: https://heasarc.gsfc.nasa.gov/w3browse/fermi/fermigbrst.html

|     |     |     |
| --- | --- | --- |
| [Search in\<br>\<br>Xamin](https://heasarc.gsfc.nasa.gov/xamin/?table=fermigbrst) or [Browse](https://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3table.pl?tablehead=name%3Dfermigbrst&Action=More+Options)... | # FERMIGBRST - Fermi GBM Burst Catalog | [HEASARC\<br>\<br>Archive](https://heasarc.gsfc.nasa.gov/docs/archive.html) |

* * *

## Overview

When referencing results from this online catalog, please cite
[von Kienlin, A. et al. 2020](https://iopscience.iop.org/article/10.3847/1538-4357/ab7a18),
[Gruber, D. et al. 2014](http://iopscience.iop.org/0067-0049/211/1/12/),
[von Kienlin, A. et al. 2014](http://iopscience.iop.org/0067-0049/211/1/13/), and
[Bhat, P. et al. 2016](http://iopscience.iop.org/article/10.3847/0067-0049/223/2/28/).

This table lists all of the triggers observed by a subset of the 14 GBM
detectors (12 NaI and 2 BGO) which have been classified as gamma-ray bursts
(GRBs). Note that there are two Browse catalogs resulting from GBM triggers. All
GBM triggers are entered in the [Fermi GBM Trigger Catalog](https://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigtrig.html),
while only those triggers classified as bursts are entered in the Burst
Catalog. Thus, a burst will be found in both the Trigger and Burst Catalogs.
The Burst Catalog analysis requires human intervention; therefore, GRBs will
be entered in the Trigger Catalog before the Burst Catalog. The latency
requirements are 1 day for triggers and 3 days for bursts. There are four
fewer bursts in the online catalog than in the Gruber et al. 2014 paper. The
four missing events (081007224, 091013989, 091022752, and 091208623) have not
been classified with certainty as GRBs and are not included in the general
GRB catalog. This classification may be revised at a later stage.

The GBM consists of an array of 12 sodium iodide (NaI) detectors which cover
the lower end of the energy range up to 1 MeV. The GBM triggers off of the
rates in the NaI detectors, with some Terrestrial Gamma-ray Flash
(TGF)-specific algorithms using the bismuth germanate (BGO) detectors,
sensitive to higher energies, up to 40 MeV. The NaI detectors are placed
around the Fermi spacecraft with different orientations to provide the
required sensitivity and FOV. The cosine-like angular response of the thin
NaI detectors is used to localize burst sources by comparing rates from
detectors with different viewing angles. The two BGO detectors are placed on
opposite sides of the spacecraft so that all sky positions are visible to at
least one BGO detector.

The signals from all 14 GBM detectors are collected by a central Data
Processing Unit (DPU). This unit digitizes and time-tags the detectors' pulse
height signals, packages the resulting data into several different types for
transmission to the ground (via the Fermi spacecraft), and performs various
data processing tasks such as autonomous burst triggering.

The GRB science products are transmitted to the FSSC in two types of files.
The first file, called the "bcat" file, provides basic burst parameters such
as duration, peak flux and fluence, calculated from 8-channel data using
a spectral model which has a power-law in energy that falls exponentially
above an energy EPeak, known as the Comptonized model. The crude 8-channel
binning and the simple spectral model allow data fits in batch mode over
numerous time bins in an efficient and robust fashion, including intervals
with little or no flux, yielding both values for the burst duration, and
deconvolved lightcurves for the detectors included in the fit. The bcat file
includes two extensions. The first, containing detailed information about
energy channels and detectors used in the calculations, is detector-specific,
and includes the time history of the deconvolved flux over the time intervals
of the burst. The second shows the evolution of the spectral parameters
obtained in a joint fit of the included detectors for the model used, usually
the Comptonized model described above. The bcat files and their time-varying
quantities contained in these two extensions are available at the HEASARC FTP
site. Quantities derived from these batch fits are given in the bcat primary
header and presented in the Browse table, as described below. The main
purpose of the analysis contained in the bcat file is to produce a measure of
the duration of the burst after deconvolving the instrument response. The
duration quantities are:

```
 * 't50' - the time taken to accumulate 50% of the burst fluence starting at the 25% fluence level.
 * 't90' - the time taken to accumulate 90% of the burst fluence starting at the 5% fluence level.
```

By-products of this analysis include fluxes on various timescales and
fluences, both obtained using the simple Comptonized model described above.
These quantities are detailed in the Browse table using the following prefixes:

```
 * 'flux' - the peak flux over 3 different timescales obtained in the batch mode fit used to calculate t50/t90.
 * 'fluence' - the total fluence accumulated in the t50/t90 calculation.
```

The fluxes and fluences derived from the 8-channel data for these bcat files
should be considered less reliable than those in the spectral analysis files
described below.

Analysis methods used in obtaining these quantities are detailed in the first
GBM GRB Catalog (Paciesas et al. 2011). Updates of bcat files will be sent
(with new version numbers) as these parameters are refined. This "bcat" file
is produced for triggers that are classified as GRBs (with exceptions as
described below), and supplements the initial data in the trigger or "tcat"
file that is produced for all triggers.

The second type of file (the spectrum or "scat" file) provides parameter
values and goodness-of-fit measures for different types of spectral fits and
models. These fits are performed using 128-channel data, either CSPEC or, for
short bursts, TTE data. The type and model are coded into the file name. There
are currently two spectrum categories:

```
 * Peak flux ('pflx') - a single spectrum over the time range of the peak flux of the burst
 * Fluence ('flnc') - a single spectrum over the entire burst duration selected by the duty scientist.
```

Like the bcat files, the scat files have two extensions. The first extension
gives detector-specific information, including photon fluxes and fluences for
each detector, which are provided for each energy channel. The second
extension provides derived quantities such as flux, fluence and model
parameters for the joint fit of all included detectors. The scat files and
their energy-resolved quantities contained in these two extensions are
available in the Fermi data archive at the HEASARC. Quantities derived from
these spectral fits are available in the Browse table, as described below
and in Goldstein et al. (2011).

The spectra are fit with a number of models, with the signal-to-noise ratio
of the spectrum often determining whether a more complex model is
statistically favored. The current set is:

```
 * Power law ('plaw'),
 * Comptonized (exponentially attenuated power law; 'comp')
 * Band ('band')
 * Smoothly broken power law ('sbpl')
```

**Warnings**

The bcat and scat files result from two completely independent analyses,
and consequently, it is possible that the same quantities might show
differences. Indeed,

1) the fluxes and fluences in the "scat" files should be considered more
reliable than those in the "bcat" files, with the official fluxes and
fluences being those yielded by the statistically favored model
("Best\_Fitting\_Model" in the Browse table) and with the full energy
resolution of the instrument;

2) in both the bcat and scat analyses, the set of detectors used for the
fits ("Scat\_Detector\_Mask" in the Browse table) may not be the same as
the set of detectors that triggered GBM ("Bcat\_Detector\_Mask" in the
Browse table);

3) background definitions are different for the bcat and scat analysis
(see References below).

Finally, for weak events, it is not always possible to perform duration or
spectral analyses, and some bursts occur too close in time to South Atlantic
Anomaly entries or exits by Fermi with resultant data truncations that prevent
background determinations for the duration analysis. There is not an exact
one-to-one correspondence between those events for which the duration analysis
fails and those which are too weak to have a useful spectral characterization.
This means that in the HEASARC Browse table there are a handful of GRBs which
have duration parameters but not spectral fit parameters, and vice versa. In
these cases, blank entries in the table indicate missing values where an
analysis was not possible. Values of 0.0 for the uncertainties on spectral
parameters indicate those parameters have been fixed in the fit from which other
parameters or quantities in the table were derived. Missing values for model fit
parameters indicate that the fit failed to converge for this model. This is
true mostly for the more complicated models (SBPL or BAND) when the fits fail
to converge for weaker bursts. Bad spectral fits can often result in
unphysical flux and fluence values with undefined errors. We include these
bad fits but leave the error fields blank when they contain undefined values.
The selection criteria used in the first catalog (Goldstein et al. 2011) for
the determination of the best-fit spectral model are different from those in
the second catalog (Gruber et al. 2014). The results using the two methods
on the sample included in Goldstein et al. (2011) are compared in Gruber et
al. (2014). The old catalog files can be retrieved using the HEASARC ftp
archive tree, under "previous" directories. The values returned by Browse
always come from the "current" directories. The chi-squared statistic was not
used in the 2nd catalog, either for parameter optimization or model
comparison. The chi-squared values are missing for a few GRBs. This is
believed to be because of a known software issue and should not be considered
indicative of a bad fit.

The variable "scatalog" included in the Browse tables and in the FITS files
indicates which catalog a file belongs to, with 2 being the current catalog,
and 1 (or absent) the first catalog (preliminary values may appear with value
0).

* * *

### Catalog Bibcodes

[2020ApJ...893...46V](https://ui.adsabs.harvard.edu/abs/2020ApJ%2E%2E%2E893%2E%2E%2E46V)

[2016ApJS..223...28N](https://ui.adsabs.harvard.edu/abs/2016ApJS%2E%2E223%2E%2E%2E28N)

[2014ApJS..211...13V](https://ui.adsabs.harvard.edu/abs/2014ApJS%2E%2E211%2E%2E%2E13V)

[2014ApJS..211...12G](https://ui.adsabs.harvard.edu/abs/2014ApJS%2E%2E211%2E%2E%2E12G)

* * *

### Bulletin

The FERMIGBRST database table was last updated on 9 August 2026.

* * *

### Caveats

Please see the warnings on the GBM Caveats page, [http://fermi.gsfc.nasa.gov/ssc/data/analysis/GBM\_caveats.html](http://fermi.gsfc.nasa.gov/ssc/data/analysis/GBM_caveats.html).

* * *

### References

```
 * The fourth (current) catalog is described in von Kienlin, A. et al. 2020.
 * The third general catalog is described in Bhat, P. et al. 2016.
 * The current (second) spectral catalog is described in Gruber, D. et al. 2014.
 * The second general catalog is described in von Kienlin, A. et al. 2014.
 * The first general catalog is described in Paciesas, W.S. et al. 2011, ApJS, 199, 18.
 * The first spectral catalog is described in Goldstein, A. et al. 2011, ApJS, 199, 19.
```

Also, see the [Fermi Science Data Product Interface Control Document](http://fermi.gsfc.nasa.gov/ssc/library/support/Science_DP_ICD_RevA.pdf).

* * *

### Provenance

The information in this table is provided by the Fermi Gamma-ray Burst
Monitor Instrument Operations Center (GIOC) and the Fermi Science Support
Center (FSSC). The values come from burst and spectral catalog entry FITS
files provided by the GIOC to the FSSC. These FITS files may contain
additional data and are available for download. This table is updated
automatically within a day or so of new data files being processed and made
available.

* * *

### Parameters

**Trigger\_Name**

The Fermi trigger designation that is assigned for each new trigger detected.
The name is the same as the one used in the Trigger Catalog. The naming
scheme used is bnyymmddfff, where yymmdd is the date of the burst (yy, the
year minus 2000; mm, the two-digit month; and dd, the two-digit day of the
month) and fff = fraction of day.

**Name**

The designation of the source of the burst. The name will initially be
GRByymmddfff, where yymmdd is the 2-digit year, month and day of the burst
and fff the fraction of the day, as assigned by pipeline processing. The name
will eventually be changed to the GRByymmddx format, where x is null or 'A'
or 'B' etc. Re-naming to this format requires human intervention, noting
whether another burst was detected on the same day.

**RA**

The Right Ascension of the burst in the selected equinox. This was
given in J2000 decimal degree coordinates in the original data.

**Dec**

The Declination of the burst in the selected equinox. This was given
in J2000 decimal degree coordinates in the original data.

**LII**

The Galactic Longitude of the burst, derived from the burst RA and Dec.

**BII**

The Galactic Latitude of the burst, derived from the burst RA and Dec.

**Error\_Radius**

This parameter is the uncertainty in the position, in degrees. A value of 0
means that the source localization was done using something other than Fermi
GBM (for example, Swift, XMM, Chandra, etc.), so that the error radius is
negligible by GBM standards. A value of 50 means that the localization is not
well determined. As noted in footnote (22) of von Kienlin et al. (2014), this
error is the statistical 1-sigma error; the GBM errors are not symmetric, and
the given value is the average of the error ellipse.

**Trigger\_Time**

The time at which the trigger occurred, originally provided in Fermi Mission
Elapsed Time (MET) format and converted to UTC.

**Duration\_Energy\_Low**

The lower limit of duration integration, in keV. This is a parameter,
nominally 50 keV.

**Duration\_Energy\_High**

The upper limit of duration integration, in keV. This is a parameter,
nominally 300 keV.

**Back\_Interval\_Low\_Start**

The start of the pre-burst background interval (in seconds relative to
trigger time) used as a plateau for the duration calculation. This value
might not be used for the spectral analysis.

**Back\_Interval\_Low\_Stop**

The end of the pre-burst background interval (in seconds relative to
trigger time) used as a plateau for the duration calculation. This value
might not be used for the spectral analysis.

**Back\_Interval\_High\_Start**

The start of the post-burst background interval (in seconds relative to
trigger time) used as a plateau for the duration calculation. This value
might not be used for the spectral analysis.

**Back\_Interval\_High\_Stop**

The end of the post-burst background interval (in seconds relative to
trigger time) used as a plateau for the duration calculation. This value
might not be used for the spectral analysis.

**T50**

The duration, in seconds, during which 50% of the burst fluence was
accumulated. The start of the T50 interval is defined by the time at which
25% of the total fluence has been detected, and the end of the T50 interval
is defined by the time at which 75% of the fluence been detected. The fluence
for the T50 calculation is measured between duration\_energy\_low and
duration\_energy\_high.

**T50\_Error**

The 1-sigma statistical uncertainty in the T50 duration.

**T50\_Start**

The start of the T50 interval (in seconds) relative to the trigger time.

**T90**

The duration, in seconds, during which 90% of the burst fluence was
accumulated. The start of the T90 interval is defined by the time at which 5%
of the total fluence has been detected, and the end of the T90 interval is
defined by the time at which 95% of the fluence been detected. The fluence
for the T90 calculation is measured between duration\_energy\_low and
duration\_energy\_high.

**T90\_Error**

The 1-sigma statistical uncertainty in the T90 duration.

**T90\_Start**

The start of T90 interval (in seconds) relative to the trigger
time.

**Bcat\_Detector\_Mask**

A mask, or string of 14 boolean flags (either '0' or 1'), that indicates which
detectors were included in the fits for the duration calculation, with '1'
representing inclusion. The mask reads from left to right: NaI 0 to NaI 11,
then BGO 0 and 1.

**Flu\_Low**

The lower limit of flux/fluence integration, in keV. This is a parameter,
nominally 10 keV.

**Flu\_High**

The upper limit of flux/fluence integration, in keV. This is a parameter,
nominally 1000 keV.

**Fluence**

The fluence (flux integrated over the burst duration, 100% level) in the
flu\_low - flu\_high energy band, nominally 10-1000 keV, in erg/cm2.

**Fluence\_Error**

The 1-sigma statistical uncertainty of the fluence in the in the flu\_low -
flu\_high energy band, nominally 10-1000 keV, in erg/cm2.

**Fluence\_BATSE**

The fluence (flux integrated over the burst duration, 100% level) in the BATSE
standard 50-300 keV energy band, in erg/cm2.

**Fluence\_BATSE\_Error**

The 1-sigma statistical uncertainty of the fluence in the BATSE standard
50-300 keV energy band, in erg/cm2.

**Flux\_1024**

The peak flux in the flu\_low - flu\_high energy band, nominally 10-1000 keV,
(1024ms timescale).

**Flux\_1024\_Error**

The 1-sigma statistical uncertainty in the in the flu\_low - flu\_high
energy band, nominally 10-1000 keV, peak flux (1024ms timescale).

**Flux\_1024\_Time**

The start time (in seconds relative to trigger time) of the interval for the
peak flux (1024 ms timescale) in the flu\_low - flu\_high energy band,
nominally 10-1000 keV.

**Flux\_64**

The peak flux in the flu\_low - flu\_high energy band, nominally 10-1000 keV,
(64ms timescale).

**Flux\_64\_Error**

The 1-sigma statistical uncertainty in the in the flu\_low - flu\_high
energy band, nominally 10-1000 keV, peak flux (64ms timescale).

**Flux\_64\_Time**

The start time (in seconds relative to trigger time) of the interval for the
peak flux (64 ms timescale) in the flu\_low - flu\_high energy band, nominally
10-1000 keV.

**Flux\_256**

The peak flux in the flu\_low - flu\_high energy band, nominally 10-1000 keV,
(256 ms timescale).

**Flux\_256\_Error**

The 1-sigma statistical uncertainty in the in the flu\_low - flu\_high
energy band, nominally 10-1000 keV, peak flux (256 ms timescale).

**Flux\_256\_Time**

The start time (in seconds relative to trigger time) of the interval for the peak flux (256 ms timescale) in the flu\_low - flu\_high energy band, nominally 10-1000 keV.

**Flux\_BATSE\_1024**

The peak flux in the BATSE standard 50-300 keV energy band (1024 ms timescale).

**Flux\_BATSE\_1024\_Error**

The 1-sigma statistical uncertainty in the 50-300 keV peak flux (1024 ms
timescale).

**Flux\_BATSE\_1024\_Time**

The start time (in seconds relative to trigger time) of the interval for the
peak flux (1024 ms timescale) in the BATSE standard 50-300 keV energy band.

**Flux\_BATSE\_64**

The peak flux in the BATSE standard 50-300 keV energy band (64 ms timescale).

**Flux\_BATSE\_64\_Error**

The 1-sigma statistical uncertainty in the 50-300 keV peak flux (64 ms
timescale).

**Flux\_BATSE\_64\_Time**

The start time (in seconds relative to trigger time) of the interval for the
peak flux (64 ms timescale) in the BATSE standard 50-300 keV energy band.

**Flux\_BATSE\_256**

The peak flux in the BATSE standard 50-300 keV energy band (256 ms timescale).

**Flux\_BATSE\_256\_Error**

The 1-sigma statistical uncertainty in the 50-300 keV peak flux (256 ms
timescale).

**Flux\_BATSE\_256\_Time**

The start time (in seconds relative to trigger time) of the interval for the
peak flux (256 ms timescale) in the BATSE standard 50-300 keV energy band.

**Actual\_64ms\_Interval**

The actual length of nominal 64ms timescale for peak flux measurement.

**Actual\_256ms\_Interval**

The actual length of nominal 256ms timescale for peak flux measurement.

**Actual\_1024ms\_Interval**

The actual length of nominal 1024ms timescale for peak flux measurement.

**Scat\_Detector\_Mask**

A mask, or string of 14 boolean flags (either '0' or 1'), that indicates
which detectors were included in the spectral catalog fits, with '1'
representing inclusion. The mask reads from left to right: NaI 0 to NaI 11,
then BGO 0 and 1.

**Pflx\_Spectrum\_Start**

The start of the interval (in seconds relative to trigger time) used in the
spectral fits over the time range of the peak flux of the burst.

**Pflx\_Spectrum\_Stop**

The end of the interval (in seconds relative to trigger time) used in the
spectral fits over the time range of the peak flux of the burst.

**Pflx\_PLaw\_Ampl**

The amplitude of a power law fit to a single spectrum over the time range of
the peak flux of the burst, in photon/cm2/s/keV.

**Pflx\_PLaw\_Ampl\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the power
law fit amplitude for the peak flux spectrum, in photon/cm2/s/keV. An error
of 0.0 implies a fixed parameter.

**Pflx\_PLaw\_Ampl\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the power
law fit amplitude for the peak flux spectrum, in photon/cm2/s/keV. An error
of 0.0 implies a fixed parameter.

**Pflx\_PLaw\_Pivot**

The pivot energy of a power law fit to a single spectrum over the time range
of the peak flux of the burst, in keV. This parameter is typically fixed.

**Pflx\_PLaw\_Pivot\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the pivot
energy of a power law fit for the peak flux spectrum, in keV. An error of 0.0
implies a fixed parameter.

**Pflx\_PLaw\_Pivot\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the pivot
energy of a power law fit for the peak flux spectrum, in keV. An error of 0.0
implies a fixed parameter.

**Pflx\_PLaw\_Index**

The power law index of a power law fit to a single spectrum over the time
range of the peak flux of the burst.

**Pflx\_PLaw\_Index\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the power
index of a power law fit for the peak flux spectrum. An error of 0.0 implies
a fixed parameter.

**Pflx\_PLaw\_Index\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the power
index of a power law fit for the peak flux spectrum. An error of 0.0 implies
a fixed parameter.

**Pflx\_PLaw\_Phtflux**

The photon flux, in photon/cm2/s, for a power law fit to a single spectrum
over the time range of the peak flux of the burst.

**Pflx\_PLaw\_Phtflux\_Error**

The 1-sigma statistical error on the photon flux, in photon/cm2/s, for the
power law peak flux spectrum.

**Pflx\_PLaw\_Phtflnc**

The photon fluence, in photon/cm2, for a power law fit to a single spectrum
over the time range of the peak flux of the burst.

**Pflx\_PLaw\_Phtflnc\_Error**

The 1-sigma statistical error in the photon fluence, in photon/cm2, for the
power law peak flux spectrum.

**Pflx\_PLaw\_Ergflux**

The energy flux, in erg/cm2/s, for a power law fit to a single spectrum over
the time range of the peak flux of the burst.

**Pflx\_PLaw\_Ergflux\_Error**

The 1-sigma statistical error on the energy flux, in erg/cm2/s, for the
power law peak flux spectrum.

**Pflx\_PLaw\_Ergflnc**

The energy fluence in erg/cm2 for a power law fit to a single spectrum over
the time range of the peak flux of the burst.

**Pflx\_PLaw\_Ergflnc\_Error**

The 1-sigma statistical error in the energy fluence, in erg/cm2, for the
power law peak flux spectrum.

**Pflx\_PLaw\_Phtfluxb**

The photon flux, in photon/cm2/s between 50 and 300 keV (BATSE standard),
for a power law fit to a single spectrum over the time range of the peak flux
of the burst.

**Pflx\_PLaw\_Phtfluxb\_Error**

The 1-sigma statistical error on the photon flux, in photon/cm2/s between 50
and 300 keV (BATSE standard), for the power law peak flux spectrum.

**Pflx\_PLaw\_Phtflncb**

The photon fluence, in photon/cm2 between 50 and 300 keV (BATSE standard),
for a power law fit to a single spectrum over the time range of the peak flux
of the burst.

**Pflx\_PLaw\_Phtflncb\_Error**

The 1-sigma statistical error in the photon fluence, in photon/cm2 between
50 and 300 keV (BATSE standard), for the power law peak flux spectrum.

**Pflx\_PLaw\_Ergflncb**

The energy fluence in erg/cm2 between 50 and 300 keV (BATSE standard) for a
power law fit to a single spectrum over the time range of the peak flux of
the burst.

**Pflx\_PLaw\_Ergflncb\_Error**

The 1-sigma statistical error in the energy fluence, in erg/cm2 between 50
and 300 keV (BATSE standard), for the power law peak flux spectrum.

**Pflx\_PLaw\_Redchisq**

The reduced chi-squared statistic for the power law fit to the peak flux
spectrum. This may not be the statistic used to determine the best fit
parameters (see pflx\_plaw\_statistic), but it is used for model comparison
purposes. This value of reduced chi-squared is calculated for the best-fit
parameters evaluated using the pflx\_plaw\_statistic statistic. Using these
best-fit parameters, a model is considered the best-fit model if it yields
the lowest chi-squared value by a margin of at least 6 units for each extra
parameter in the model.

**Pflx\_PLaw\_Redfitstat**

The reduced fitting statistic for the power law fit to the peak flux
spectrum. This is the value of the statistic used to determine the best fit
parameters, specified in pflx\_plaw\_statistic.

**Pflx\_PLaw\_DoF**

The degrees of freedom for the power law fit to the peak flux spectrum.

**Pflx\_PLaw\_Statistic**

The statistical merit function for the power law fit to the peak flux spectrum.

**Pflx\_Comp\_Ampl**

The amplitude of a Comptonized model fit to a single spectrum over the time
range of the peak flux of the burst, in photon/cm2/s/keV.

**Pflx\_Comp\_Ampl\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the
Comptonized model amplitude for the peak flux spectrum, in photon/cm2/s/keV.
An error of 0.0 implies a fixed parameter.

**Pflx\_Comp\_Ampl\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the
Comptonized model amplitude for the peak flux spectrum, in photon/cm2/s/keV.
An error of 0.0 implies a fixed parameter.

**Pflx\_Comp\_Epeak**

The peak energy of a Comptonized model fit to a single spectrum over the time
range of the peak flux of the burst, in keV.

**Pflx\_Comp\_Epeak\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the
Comptonized model peak energy for the peak flux spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Pflx\_Comp\_Epeak\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the
Comptonized model peak energy for the peak flux spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Pflx\_Comp\_Index**

The power law index of a Comptonized model fit to a single spectrum over the
time range of the peak flux of the burst.

**Pflx\_Comp\_Index\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the
Comptonized model power law index for the peak flux spectrum. An error of 0.0
implies a fixed parameter.

**Pflx\_Comp\_Index\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the
Comptonized model power law index for the peak flux spectrum. An error of 0.0
implies a fixed parameter.

**Pflx\_Comp\_Pivot**

The pivot energy of a Comptonized model fit to a single spectrum over the
time range of the peak flux of the burst, in keV. This parameter is typically
fixed.

**Pflx\_Comp\_Pivot\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the
Comptonized model pivot energy for the peak flux spectrum, in keV. An error
of 0.0 implies a fixed parameter.

**Pflx\_Comp\_Pivot\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the
Comptonized model pivot energy for the peak flux spectrum, in keV. An error
of 0.0 implies a fixed parameter.

**Pflx\_Comp\_Phtflux**

The photon flux, in photon/cm2/s, for a Comptonized model fit to a single
spectrum over the time range of the peak flux of the burst.

**Pflx\_Comp\_Phtflux\_Error**

The 1-sigma statistical error on the photon flux, in photon/cm2/s, for the
Comptonized model peak flux spectrum.

**Pflx\_Comp\_Phtflnc**

The photon fluence in photon/cm2 for a Comptonized model fit to a single
spectrum over the time range of the peak flux of the burst.

**Pflx\_Comp\_Phtflnc\_Error**

The 1-sigma statistical error in the photon fluence, in photon/cm2, for the
Comptonized model peak flux spectrum.

**Pflx\_Comp\_Ergflux**

The energy flux, in erg/cm2/s, for a Comptonized model fit to a single
spectrum over the time range of the peak flux of the burst.

**Pflx\_Comp\_Ergflux\_Error**

The 1-sigma statistical error on the energy flux, in erg/cm2/s, for the
Comptonized model peak flux spectrum.

**Pflx\_Comp\_Ergflnc**

The energy fluence in erg/cm2 for a Comptonized model fit to a single
spectrum over the time range of the peak flux of the burst.

**Pflx\_Comp\_Ergflnc\_Error**

The 1-sigma statistical error in the energy fluence, in erg/cm2, for the
Comptonized model peak flux spectrum.

**Pflx\_Comp\_Phtfluxb**

The photon flux, in photon/cm2/s between 50 and 300 keV (BATSE standard),
for a Comptonized model fit to a single spectrum over the time range of the
peak flux of the burst.

**Pflx\_Comp\_Phtfluxb\_Error**

The 1-sigma statistical error on the photon flux, in photon/cm2/s between 50
and 300 keV (BATSE standard), for the Comptonized model peak flux spectrum.

**Pflx\_Comp\_Phtflncb**

The photon fluence, in photon/cm2 between 50 and 300 keV (BATSE standard),
for a Comptonized model fit to a single spectrum over the time range of the
peak flux of the burst.

**Pflx\_Comp\_Phtflncb\_Error**

The 1-sigma statistical error in the photon fluence, in photon/cm2 between
50 and 300 keV (BATSE standard), for the Comptonized model peak flux
spectrum.

**Pflx\_Comp\_Ergflncb**

The energy fluence in erg/cm2 between 50 and 300 keV (BATSE standard) for a
Comptonized model fit to a single spectrum over the time range of the peak
flux of the burst.

**Pflx\_Comp\_Ergflncb\_Error**

The 1-sigma statistical error in the energy fluence, in erg/cm2 between 50
and 300 keV (BATSE standard), for the Comptonized model peak flux spectrum.

**Pflx\_Comp\_Redchisq**

The reduced chi-squared statistic for the Comptonized fit to the peak flux
spectrum. This may not be the statistic used to determine the best fit
parameters (see pflx\_comp\_statistic), but it is used for model comparison
purposes. This value of reduced chi-squared is calculated for the best-fit
parameters evaluated using the pflx\_comp\_statistic statistic. Using these
best-fit parameters, a model is considered the best-fit model if it yields
the lowest chi-squared value by a margin of at least 6 units for each extra
parameter in the model.

**Pflx\_Comp\_Redfitstat**

The reduced fitting statistic for the Comptonized model fit to the peak flux
spectrum. This is the value of the statistic used to determine the best fit
parameters, specified in pflx\_comp\_statistic.

**Pflx\_Comp\_DoF**

The degrees of freedom for the Comptonized model fit to the peak flux spectrum.

**Pflx\_Comp\_Statistic**

The statistical merit function for the Comptonized model fit to the peak flux
spectrum.

**Pflx\_Band\_Ampl**

The amplitude of a Band function fit to a single spectrum over the time range
of the peak flux of the burst, in photon/cm2/s/keV.

**Pflx\_Band\_Ampl\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the Band
function amplitude for the peak flux spectrum, in photon/cm2/s/keV. An error
of 0.0 implies a fixed parameter.

**Pflx\_Band\_Ampl\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the Band
function amplitude for the peak flux spectrum, in photon/cm2/s/keV. An error
of 0.0 implies a fixed parameter.

**Pflx\_Band\_Epeak**

The peak energy of a Band function fit to a single spectrum over the time
range of the peak flux of the burst, in keV.

**Pflx\_Band\_Epeak\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the Band
function peak energy for the peak flux spectrum, in keV. An error of 0.0
implies a fixed parameter.

**Pflx\_Band\_Epeak\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the Band
function peak energy for the peak flux spectrum, in keV. An error of 0.0
implies a fixed parameter.

**Pflx\_Band\_Alpha**

The power law index, alpha, of a Band function fit to a single spectrum over
the time range of the peak flux of the burst.

**Pflx\_Band\_Alpha\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the to the Band
function power law, alpha, for the peak flux spectrum. An error of 0.0
implies a fixed parameter.

**Pflx\_Band\_Alpha\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the to the Band
function power law, alpha, for the peak flux spectrum. An error of 0.0
implies a fixed parameter.

**Pflx\_Band\_Beta**

The power law index, beta, of a Band function fit to a single spectrum over
the time range of the peak flux of the burst.

**Pflx\_Band\_Beta\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the to the Band
function power law, beta, for the peak flux spectrum. An error of 0.0 implies
a fixed parameter.

**Pflx\_Band\_Beta\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the to the Band
function power law, beta, for the peak flux spectrum. An error of 0.0 implies
a fixed parameter.

**Pflx\_Band\_Phtflux**

The photon flux, in photon/cm2/s, for a Band function fit to a single
spectrum over the time range of the peak flux of the burst.

**Pflx\_Band\_Phtflux\_Error**

The 1-sigma statistical error on the photon flux, in photon/cm2/s, for the
Band function peak flux spectrum.

**Pflx\_Band\_Phtflnc**

The photon fluence, in photon/cm2, for a Band function fit to a single spectrum over the time range of the peak flux of the burst.

**Pflx\_Band\_Phtflnc\_Error**

The 1-sigma statistical error in the photon fluence, in photon/cm2, for the
Band function peak flux spectrum.

**Pflx\_Band\_Ergflux**

The energy flux, in erg/cm2/s, for a Band function fit to a single spectrum
over the time range of the peak flux of the burst.

**Pflx\_Band\_Ergflux\_Error**

The 1-sigma statistical error on the energy flux, in erg/cm2/s, for the Band
function peak flux spectrum.

**Pflx\_Band\_Ergflnc**

The energy fluence in erg/cm2 for a Band function fit to a single spectrum
over the time range of the peak flux of the burst.

**Pflx\_Band\_Ergflnc\_Error**

The 1-sigma statistical error in the energy fluence, in erg/cm2, for the
Band function peak flux spectrum.

**Pflx\_Band\_Phtfluxb**

The photon flux, in photon/cm2/s between 50 and 300 keV (BATSE standard),
for a Band function fit to a single spectrum over the time range of the peak
flux of the burst.

**Pflx\_Band\_Phtfluxb\_Error**

The 1-sigma statistical error on the photon flux, in photon/cm2/s between 50
and 300 keV (BATSE standard), for the Band function peak flux spectrum.

**Pflx\_Band\_Phtflncb**

The photon fluence, in photon/cm2 between 50 and 300 keV (BATSE standard),
for a Band function fit to a single spectrum over the time range of the peak
flux of the burst.

**Pflx\_Band\_Phtflncb\_Error**

The 1-sigma statistical error in the photon fluence, in photon/cm2 between
50 and 300 keV (BATSE standard), for the Band function peak flux spectrum.

**Pflx\_Band\_Ergflncb**

The energy fluence, in erg/cm2 between 50 and 300 keV (BATSE standard), for
a Band function fit to a single spectrum over the time range of the peak flux
of the burst.

**Pflx\_Band\_Ergflncb\_Error**

The 1-sigma statistical error in the energy fluence, in erg/cm2 between 50
and 300 keV (BATSE standard), for the Band function peak flux spectrum.

**Pflx\_Band\_Redchisq**

The reduced chi-squared statistic for the Band function fit to the peak flux
spectrum. This may not be the statistic used to determine the best fit
parameters (see pflx\_band\_statistic), but it is used for model comparison
purposes. This value of reduced chi-squared is calculated for the best-fit
parameters evaluated using the pflx\_band\_statistic statistic. Using these
best-fit parameters, a model is considered the best-fit model if it yields
the lowest chi-squared value by a margin of at least 6 units for each extra
parameter in the model.

**Pflx\_Band\_Redfitstat**

The reduced fitting statistic for the Band function fit to the peak flux
spectrum. This is the value of the statistic used to determine the best fit
parameters, specified in pflx\_band\_statistic.

**Pflx\_Band\_DoF**

The degrees of freedom for the Band function fit to the peak flux spectrum.

**Pflx\_Band\_Statistic**

The statistical merit function for the Band function fit to the peak flux
spectrum.

**Pflx\_SBPL\_Ampl**

The amplitude of a smoothly broken power law fit to a single spectrum over
the time range of the peak flux of the burst, in photon/cm2/s/keV.

**Pflx\_SBPL\_Ampl\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the smoothly
broken power law amplitude for the peak flux spectrum, in photon/cm2/s/keV.
An error of 0.0 implies a fixed parameter.

**Pflx\_SBPL\_Ampl\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the smoothly
broken power law amplitude for the peak flux spectrum, in photon/cm2/s/keV.
An error of 0.0 implies a fixed parameter.

**Pflx\_SBPL\_Pivot**

The pivot energy of a smoothly broken power law fit to a single spectrum over
the time range of the peak flux of the burst, in keV. Typically this
parameter is fixed.

**Pflx\_SBPL\_Pivot\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the smoothly
broken power law pivot energy for the peak flux spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Pflx\_SBPL\_Pivot\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the smoothly
broken power law pivot energy for the peak flux spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Pflx\_SBPL\_Indx1**

The 1st power law of a smoothly broken power law fit to a single spectrum
over the time range of the peak flux of the burst.

**Pflx\_SBPL\_Indx1\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the smoothly
broken power law 1st power law for the peak flux spectrum. An error of 0.0
implies a fixed parameter.

**Pflx\_SBPL\_Indx1\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the smoothly
broken power law 1st power law for the peak flux spectrum. An error of 0.0
implies a fixed parameter.

**Pflx\_SBPL\_Brken**

The break energy of a smoothly broken power law fit to a single spectrum over
the time range of the peak flux of the burst, in keV.

**Pflx\_SBPL\_Brken\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the smoothly
broken power law break energy for the peak flux spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Pflx\_SBPL\_Brken\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the smoothly
broken power law break energy for the peak flux spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Pflx\_SBPL\_Brksc**

The break scale of a smoothly broken power law fit to a single spectrum over
the time range of the peak flux of the burst, in keV. Typically, this
parameter is fixed.

**Pflx\_SBPL\_Brksc\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the smoothly
broken power law break scale for the peak flux spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Pflx\_SBPL\_Brksc\_Neg\_Err**

The 1-sigma statistical negative error giving the upper bound to the smoothly
broken power law break scale for the peak flux spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Pflx\_SBPL\_Indx2**

The second power law of a smoothly broken power law fit to a single spectrum
over the time range of the peak flux of the burst.

**Pflx\_SBPL\_Indx2\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the smoothly
broken power law 2nd power law for the peak flux spectrum. An error of 0.0
implies a fixed parameter.

**Pflx\_SBPL\_Indx2\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the smoothly
broken power law 2nd power law for the peak flux spectrum. An error of 0.0
implies a fixed parameter.

**Pflx\_SBPL\_Phtflux**

The photon flux, in photon/cm2/s, for a smoothly broken power law fit to a
single spectrum over the time range of the peak flux of the burst.

**Pflx\_SBPL\_Phtflux\_Error**

The 1-sigma statistical error on the photon flux, in photon/cm2/s, for the
smoothly broken power law peak flux spectrum.

**Pflx\_SBPL\_Phtflnc**

The photon fluence in photon/cm2 for a smoothly broken power law fit to a
single spectrum over the time range of the peak flux of the burst.

**Pflx\_SBPL\_Phtflnc\_Error**

The 1-sigma statistical error in the photon fluence, in photon/cm2, for the
smoothly broken power law peak flux spectrum.

**Pflx\_SBPL\_Ergflux**

The energy flux, in erg/cm2/s, for a smoothly broken power law fit to a
single spectrum over the time range of the peak flux of the burst.

**Pflx\_SBPL\_Ergflux\_Error**

The 1-sigma statistical error on the energy flux, in erg/cm2/s, for the
smoothly broken power law peak flux spectrum.

**Pflx\_SBPL\_Ergflnc**

The energy fluence, in erg/cm2, for a smoothly broken power law fit to a
single spectrum over the time range of the peak flux of the burst.

**Pflx\_SBPL\_Ergflnc\_Error**

The 1-sigma statistical error in the energy fluence, in erg/cm2, for the
smoothly broken power law peak flux spectrum.

**Pflx\_SBPL\_Phtfluxb**

The photon flux, in photon/cm2/s between 50 and 300 keV (BATSE standard),
for a smoothly broken power law fit to a single spectrum over the time range
of the peak flux of the burst.

**Pflx\_SBPL\_Phtfluxb\_Error**

The 1-sigma statistical error on the photon flux, in photon/cm2/s between 50
and 300 keV (BATSE standard), for the smoothly broken power law peak flux
spectrum.

**Pflx\_SBPL\_Phtflncb**

The photon fluence, in photon/cm2 between 50 and 300 keV (BATSE standard),
for a smoothly broken power law fit to a single spectrum over the time range
of the peak flux of the burst.

**Pflx\_SBPL\_Phtflncb\_Error**

The 1-sigma statistical error in the photon fluence, in photon/cm2 between
50 and 300 keV (BATSE standard), for the smoothly broken power law peak flux
spectrum.

**Pflx\_SBPL\_Ergflncb**

The energy fluence, in erg/cm2 between 50 and 300 keV (BATSE standard), for
a smoothly broken power law fit to a single spectrum over the time range of
the peak flux of the burst.

**Pflx\_SBPL\_Ergflncb\_Error**

The 1-sigma statistical error in the energy fluence, in erg/cm2 between 50
and 300 keV (BATSE standard), for the smoothly broken power law peak flux
spectrum.

**Pflx\_SBPL\_Redchisq**

The reduced chi-squared statistic for the smoothly broken power law fit to
the peak flux spectrum. This may not be the statistic used to determine the
best fit parameters (see pflx\_sbpl\_statistic), but it is used for model
comparison purposes. This value of reduced chi-squared is calculated for the
best-fit parameters evaluated using the pflx\_sbpl\_statistic statistic. Using
these best-fit parameters, a model is considered the best-fit model if it
yields the lowest chi-squared value by a margin of at least 6 units for each
extra parameter in the model.

**Pflx\_SBPL\_Redfitstat**

The reduced fitting statistic for the smoothly broken power law fit to the
peak flux spectrum. This is the value of the statistic used to determine the
best fit parameters, specified in pflx\_sbpl\_statistic.

**Pflx\_SBPL\_DoF**

The degrees of freedom for the smoothly broken power law fit to the peak flux
spectrum.

**Pflx\_SBPL\_Statistic**

The statistical merit function for the smoothly broken power law fit to the
peak flux spectrum.

**Pflx\_Best\_Fitting\_Model**

The model which best fits the data for a spectrum accumulated over the peak
flux of the burst. The determination of the best fitting model compares the
values of the likelihood-based statistic CSTAT (or other statistic defined in
pflx\_xxxx\_statistic) among the tested models. The COMP model is preferred
over the PLAW model if there is a decrease in 8.58 units of CSTAT. The BAND
or SBPL models are preferred over the COMP model if there is a decrease in
11.83 units of CSTAT, then the lower of BAND and SBPL is selected as best.

[... middle omitted — see footer ...]

best-fit parameters, a model is considered the best-fit model if it yields
the lowest chi-squared value by a margin of at least 6 units for each extra
parameter in the model.

**Flnc\_Comp\_Redfitstat**

The reduced fitting statistic for the Comptonized model fit to the fluence
spectrum. This is the value of the statistic used to determine the best fit
parameters, specified in flnc\_comp\_statistic.

**Flnc\_Comp\_DoF**

The degrees of freedom for the Comptonized model fit to the fluence spectrum.

**Flnc\_Comp\_Statistic**

The statistical merit function for the Comptonized model fit to the fluence
spectrum.

**Flnc\_Band\_Ampl**

The amplitude of a Band function fit to a single spectrum over the duration
of the burst, in photon/cm2/s/keV.

**Flnc\_Band\_Ampl\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the Band
function amplitude for the fluence spectrum, in photon/cm2/s/keV. An error
of 0.0 implies a fixed parameter.

**Flnc\_Band\_Ampl\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the Band
function amplitude for the fluence spectrum, in photon/cm2/s/keV. An error
of 0.0 implies a fixed parameter.

**Flnc\_Band\_Epeak**

The peak energy of a Band function fit to a single spectrum over the duration
of the burst, in keV.

**Flnc\_Band\_Epeak\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the Band
function peak energy for the fluence spectrum, in keV. An error of 0.0
implies a fixed parameter.

**Flnc\_Band\_Epeak\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the Band
function peak energy for the fluence spectrum, in keV. An error of 0.0
implies a fixed parameter.

**Flnc\_Band\_Alpha**

The power law index, alpha, of a Band function fit to a single spectrum over
the duration of the burst.

**Flnc\_Band\_Alpha\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the to the Band
function power law, alpha, for the fluence spectrum. An error of 0.0 implies
a fixed parameter.

**Flnc\_Band\_Alpha\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the to the Band
function power law, alpha, for the fluence spectrum. An error of 0.0 implies
a fixed parameter.

**Flnc\_Band\_Beta**

The power law index, beta, of a Band function fit to a single spectrum over
the duration of the burst.

**Flnc\_Band\_Beta\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the to the Band
function power law, beta, for the fluence spectrum. An error of 0.0 implies a
fixed parameter.

**Flnc\_Band\_Beta\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the to the Band
function power law, beta, for the fluence spectrum. An error of 0.0 implies a
fixed parameter.

**Flnc\_Band\_Phtflux**

The average photon flux, in photon/cm2/s, for a Band function law fit to a
single spectrum over the duration of the burst.

**Flnc\_Band\_Phtflux\_Error**

The 1-sigma statistical error on the average photon flux, in photon/cm2/s,
for the Band function fluence spectrum.

**Flnc\_Band\_Phtflnc**

The photon fluence, in photon/cm2, for a Band function fit to a single
spectrum over the duration of the burst.

**Flnc\_Band\_Phtflnc\_Error**

The 1-sigma statistical error in the photon fluence, in photon/cm2, for the
Band function peak flux spectrum.

**Flnc\_Band\_Ergflux**

The average energy flux, in erg/cm2/s, for a Band function law fit to a
single spectrum over the duration of the burst.

**Flnc\_Band\_Ergflux\_Error**

The 1-sigma statistical error on the average energy flux, in erg/cm2/s, for
the Band function fluence spectrum.

**Flnc\_Band\_Ergflnc**

The energy fluence, in erg/cm2, for a Band function fit to a single spectrum
over the duration of the burst.

**Flnc\_Band\_Ergflnc\_Error**

The 1-sigma statistical error in the energy fluence, in erg/cm2, for the
Band function peak flux spectrum.

**Flnc\_Band\_Phtfluxb**

The average photon flux, in photon/cm2/s between 50 and 300 keV (BATSE
standard), for a Band function law fit to a single spectrum over the duration
of the burst.

**Flnc\_Band\_Phtfluxb\_Error**

The 1-sigma statistical error on the average photon flux, in photon/cm2/s
between 50 and 300 keV (BATSE standard), for the Band function fluence
spectrum.

**Flnc\_Band\_Phtflncb**

The photon fluence, in photon/cm2 between 50 and 300 keV (BATSE standard),
for a Band function fit to a single spectrum over the duration of the burst.

**Flnc\_Band\_Phtflncb\_Error**

The 1-sigma statistical error in the photon fluence, in photon/cm2 between
50 and 300 keV (BATSE standard), for the Band function peak flux spectrum.

**Flnc\_Band\_Ergflncb**

The energy fluence, in erg/cm2 between 50 and 300 keV (BATSE standard), for
a Band function fit to a single spectrum over the duration of the burst.

**Flnc\_Band\_Ergflncb\_Error**

The 1-sigma statistical error in the energy fluence, in erg/cm2 between 50
and 300 keV (BATSE standard), for the Band function peak flux spectrum.

**Flnc\_Band\_Redchisq**

The reduced chi-squared statistic for the Band function fit to the fluence
spectrum. This may not be the statistic used to determine the best fit
parameters (see flnc\_band\_statistic), but it is used for model comparison
purposes. This value of reduced chi-squared is calculated for the best-fit
parameters evaluated using the flnc\_band\_statistic statistic. Using these
best-fit parameters, a model is considered the best-fit model if it yields
the lowest chi-squared value by a margin of at least 6 units for each extra
parameter in the model.

**Flnc\_Band\_Redfitstat**

The reduced fitting statistic for the Band function fit to the fluence
spectrum. This is the value of the statistic used to determine the best fit
parameters, specified in flnc\_band\_statistic.

**Flnc\_Band\_DoF**

The degrees of freedom for the Band function fit to the fluence spectrum.

**Flnc\_Band\_Statistic**

The statistical merit function for the Band function fit to the fluence
spectrum.

**Flnc\_SBPL\_Ampl**

The amplitude of a smoothly broken power law fit to a single spectrum over
the duration of the burst, in photon/cm2/s/keV.

**Flnc\_SBPL\_Ampl\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the smoothly
broken power law fit amplitude for the fluence spectrum, in
photon/cm2/s/keV. An error of 0.0 implies a fixed parameter.

**Flnc\_SBPL\_Ampl\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the smoothly
broken power law fit amplitude for the fluence spectrum, in
photon/cm2/s/keV. An error of 0.0 implies a fixed parameter.

**Flnc\_SBPL\_Pivot**

The pivot energy of a smoothly broken power law fit to a single spectrum over
the duration of the burst, in keV. Typically this parameter is fixed.

**Flnc\_SBPL\_Pivot\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the smoothly
broken power law pivot energy for the fluence spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Flnc\_SBPL\_Pivot\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the smoothly
broken power law pivot energy for the fluence spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Flnc\_SBPL\_Indx1**

The 1st power law of a smoothly broken power law fit to a single spectrum
over the duration of the burst.

**Flnc\_SBPL\_Indx1\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the smoothly
broken power law 1st power law for the fluence spectrum. An error of 0.0
implies a fixed parameter.

**Flnc\_SBPL\_Indx1\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the smoothly
broken power law 1st power law for the fluence spectrum. An error of 0.0
implies a fixed parameter.

**Flnc\_SBPL\_Brken**

The break energy of a smoothly broken power law fit to a single spectrum over
the duration of the burst, in keV.

**Flnc\_SBPL\_Brken\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the smoothly
broken power law break energy for the fluence spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Flnc\_SBPL\_Brken\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the smoothly
broken power law break energy for the fluence spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Flnc\_SBPL\_Brksc**

The break scale of a smoothly broken power law fit to a single spectrum over
the duration of the burst, in keV. Typically, this parameter is fixed.

**Flnc\_SBPL\_Brksc\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the smoothly
broken power law break scale for the fluence spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Flnc\_SBPL\_Brksc\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the smoothly
broken power law break scale for the fluence spectrum, in keV. An error of
0.0 implies a fixed parameter.

**Flnc\_SBPL\_Indx2**

The second power law of a smoothly broken power law fit to a single spectrum
over the duration of the burst.

**Flnc\_SBPL\_Indx2\_Pos\_Err**

The 1-sigma statistical positive error giving the upper bound to the smoothly
broken power law 2nd power law for the fluence spectrum. An error of 0.0
implies a fixed parameter.

**Flnc\_SBPL\_Indx2\_Neg\_Err**

The 1-sigma statistical negative error giving the lower bound to the smoothly
broken power law 2nd power law for the fluence spectrum. An error of 0.0
implies a fixed parameter.

**Flnc\_SBPL\_Phtflux**

The average photon flux, in photon/cm2/s, for a smoothly broken power law
fit to a single spectrum over the duration of the burst.

**Flnc\_SBPL\_Phtflux\_Error**

The 1-sigma statistical error on the average photon flux, in photon/cm2/s,
for the smoothly broken power law fluence spectrum.

**Flnc\_SBPL\_Phtflnc**

The photon fluence, in photon/cm2, for a smoothly broken power law fit to a
single spectrum over the duration of the burst.

**Flnc\_SBPL\_Phtflnc\_Error**

The 1-sigma statistical error in the photon fluence, in photon/cm2, for the
smoothly broken power law fluence spectrum.

**Flnc\_SBPL\_Ergflux**

The average energy flux, in erg/cm2/s, for a smoothly broken power law fit
to a single spectrum over the duration of the burst.

**Flnc\_SBPL\_Ergflux\_Error**

The 1-sigma statistical error on the average energy flux, in erg/cm2/s, for
the smoothly broken power law fluence spectrum.

**Flnc\_SBPL\_Ergflnc**

The energy fluence, in erg/cm2, for a smoothly broken power law fit to a
single spectrum over the duration of the burst.

**Flnc\_SBPL\_Ergflnc\_Error**

The 1-sigma statistical error in the energy fluence, in erg/cm2, for the
smoothly broken power law fluence spectrum.

**Flnc\_SBPL\_Phtfluxb**

The average photon flux, in photon/cm2/s between 50 and 300 keV (BATSE
standard), for a smoothly broken power law fit to a single spectrum over the
duration of the burst.

**Flnc\_SBPL\_Phtfluxb\_Error**

The 1-sigma statistical error on the average photon flux, in photon/cm2/s
between 50 and 300 keV (BATSE standard), for the smoothly broken power law
fluence spectrum.

**Flnc\_SBPL\_Phtflncb**

The photon fluence, in photon/cm2 between 50 and 300 keV (BATSE standard),
for a smoothly broken power law fit to a single spectrum over the duration of
the burst.

**Flnc\_SBPL\_Phtflncb\_Error**

The 1-sigma statistical error in the photon fluence, in photon/cm2 between
50 and 300 keV (BATSE standard), for the smoothly broken power law fluence
spectrum.

**Flnc\_SBPL\_Ergflncb**

The energy fluence, in erg/cm2 between 50 and 300 keV (BATSE standard), for
a smoothly broken power law fit to a single spectrum over the duration of the
burst.

**Flnc\_SBPL\_Ergflncb\_Error**

The 1-sigma statistical error in the energy fluence, in erg/cm2 between 50
and 300 keV (BATSE standard), for the smoothly broken power law fluence
spectrum.

**Flnc\_SBPL\_Redchisq**

The reduced chi-squared statistic for the smoothly broken power law fit to
the fluence spectrum. This may not be the statistic used to determine the
best fit parameters (see flnc\_sbpl\_statistic), but it is used for model
comparison purposes. This value of reduced chi-squared is calculated for the
best-fit parameters evaluated using the flnc\_sbpl\_statistic statistic. Using
these best-fit parameters, a model is considered the best-fit model if it
yields the lowest chi-squared value by a margin of at least 6 units for each
extra parameter in the model.

**Flnc\_SBPL\_Redfitstat**

The reduced fitting statistic for the smoothly broken power law fit to the
fluence spectrum. This is the value of the statistic used to determine the
best fit parameters, specified in flnc\_sbpl\_statistic.

**Flnc\_SBPL\_DoF**

The degrees of freedom for the smoothly broken power law fit to the fluence
spectrum.

**Flnc\_SBPL\_Statistic**

The statistical merit function for the smoothly broken power law fit to the
fluence spectrum.

**Flnc\_Best\_Fitting\_Model**

The model which best fits the data for a spectrum accumulated over the duration
of the burst. The determination of the best fitting model compares the values of
the likelihood-based statistic CSTAT (or other statistic defined in
flnc\_xxxx\_statistic), among the tested models. The COMP model is preferred
over the PLAW model if there is a decrease in 8.58 units of CSTAT. The BAND or
SBPL models are preferred over the COMP model if there is a decrease in 11.83
units of CSTAT, then the lower of BAND and SBPL is selected as best. For a
model to be selected as best, its parameters must be well-determined, as
follows: the low-energy power-law index must be known to at least 0.4 (68% CL);
the high-energy power-law index within 1.0; all other parameters within 40% of
their value.

**Flnc\_Best\_Model\_Redchisq**

The reduced chi-squared statistic for the model that provides the best fit to
the fluence spectrum using the parameters optimized using flnc\_xxxx\_statistic.
This is not the statistic used to determine the best fit parameters but is
provided as a "goodness-of-fit" estimate for the model.

**Bcatalog**

The burst catalog version of the file: zero for preliminary (unpublished)
data, integer value (1, 2, 3, etc.) for official catalog releases.

**Scatalog**

The spectral catalog version of the file: zero for preliminary
(unpublished) data, integer value (1, 2, 3, etc.) for official catalog releases.

**Last\_Modified**

The time (in UTC) of the last modification to the burst information.

* * *

### Contact Person

Questions regarding the FERMIGBRST database table can be addressed to the
[HEASARC Help Desk](https://heasarc.gsfc.nasa.gov/cgi-bin/Feedback?selected=heasarc).

* * *

_Page Author:_ [Browse Software Development Team](https://heasarc.gsfc.nasa.gov/cgi-bin/Feedback?selected=w3browse)

_Last Modified:_ Monday, 16-Sep-2024 17:27:24 EDT

* * *

```

```

──────── [TRUNCATED] ────────
Showing 44,964 chars (head) + 14,943 chars (tail) of 70,500 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/heasarc.gsfc.nasa.gov-9a05f8dbab.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/heasarc.gsfc.nasa.gov-9a05f8dbab.md" offset=1208 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
