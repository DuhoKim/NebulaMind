URL: https://heasarc.gsfc.nasa.gov/w3browse/cgro/batse4b.html

|     |     |     |
| --- | --- | --- |
| [Search in\<br>\<br>Xamin](https://heasarc.gsfc.nasa.gov/xamin/?table=batse4b) or [Browse](https://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3table.pl?tablehead=name%3Dbatse4b&Action=More+Options)... | # BATSE4B - CGRO/BATSE 4B Catalog | [HEASARC\<br>\<br>Archive](https://heasarc.gsfc.nasa.gov/docs/archive.html) |

* * *

## Overview

This database table comprises the 4th BATSE Gamma-Ray Burst Catalog,
hereafter referred to as 4B. It specifies the locations and times for 1637
triggered gamma-ray bursts observed from 19 April, 1991 until 29 August,
1996\. It therefore includes the data from the 3B catalog. The only revisions
from the 3B catalog are improved locations for the trigger #s 741, 2311, and
3155.

Bursts since the end of the 1B catalog (March 1992) occurred when the Compton
Gamma-Ray Observatory (CGRO) tape recorders were experiencing numerous
errors. Consequently, there are gaps in the data of many bursts that preclude
valid measurement of peak flux, peak rate, fluence, or duration. Peak rates
on the 1 second timescale from each detector are almost always available.
These data (called MAXBC rates) can be used to determine burst location.
Previous difficulties with this data type have been largely removed, and we
now believe that the systematic errors for MAXBC-located bursts are the same
as for bursts located with other data types. It is still true however, that
the MAXBC-located bursts usually have larger statistical errors than would be
the case if another data type were available. The parameter called
comments\_position in this database contains comments on MAXBC-located bursts.
A number of CGRO and BATSE flight software changes have significantly reduced
the problem of data gaps since March of 1993.

* * *

### Catalog Bibcode

[1998hgrb.symp....3M](https://ui.adsabs.harvard.edu/abs/1998hgrb%2Esymp%2E%2E%2E%2E3M)

* * *

### References

```
The Fourth BATSE Gamma-Ray Burst Catalog, C. A. Meegan et al.,
    "Gamma-Ray Bursts: the Fourth Huntsville Symposium (IAP No. 428)",
    ed. Meegan, C.A., Preece, R.D. and Koshut, T.M., p. 1. (1997).

The Third BATSE BATSE Gamma-Ray Burst Catalog, C. A. Meegan et al.,
    ApJS, 106, 65. (1996).
```

* * *

### Provenance

This database table was created by the HEASARC in March 1999, based
on data supplied by the CGRO Science Support Center.

* * *

### Description

The on-board software determines when a trigger occurs. When a burst trigger
occurs, subsequent triggers are disabled for an accumulation period, during
which the BATSE burst memories accumulate data. The accumulation period was
242 seconds until Dec 17, 1992, and from Jan 8, 1996 to Feb 25, 1997. At all
other times it has been 573 seconds. The stored burst data are then
transmitted; the readout time for all triggers was 90 minutes until Dec 17,
1992\. At that date, the flight software was revised to suspend readouts
during telemetry gaps and to truncate readouts of weak events. This resulted
in a variable readout time. During the burst data readout, the 64 ms
threshold is revised to correspond to the maximum rate attained by the
current burst, and triggering is disabled on the 256 ms and 1024 ms
timescales. Bursts intense enough to trigger over this revised 64 ms value
are termed "overwrites". They appear as triggers in this catalog, with the
overwrite flag is set to 'Y'.

The BATSE trigger numbers are the primary means of identification for events
in this catalog. The trigger number is a running sequence of BATSE triggers
which include cosmic bursts, solar flares and other events. The sequence
begins with trigger 105 and ends with trigger 5586.

Each burst has a unique catalog name. These BATSE catalog names later may be
incorporated into a multi-spacecraft catalog with "GRB" replacing this
designation of "4B". The characters "4B " begin every BATSE catalog burst
name, followed by the "yymmdd" of the burst. "yymmdd" is the two digit year,
two digit month, and two digit day. When more than one gamma-ray burst occurs
on one day, those bursts have a single letter suffix (B,C,D...), generally in
order of intensity. Example: 4B 920504B refers to the second brightest burst
that triggered BATSE May 3, 1992. The brightest burst on that day will have
no suffix. The burst trigger time is the end of the interval (64, 256 or 1024
ms) on which the burst triggered the detector.

The angular error in position is the radius of a circle having the same area
as the 68% confidence ellipse defined by the formal covariance matrix from a
chi2 fit on the assumption of normal errors. The error is based solely on
the Poisson uncertainty in the BATSE measurement of burst flux by each Large
Area Detector. There is, in addition, an RMS systematic error of
approximately 1.6 degrees. Adding 1.6 degrees in quadrature to the error in
the database table (the parameter called error\_radius) yields the BATSE
team's estimate of the 68% confidence interval for the burst location error.
The statistical error is believed to be Gaussian.

* * *

### Data Products

The following is a summary of the most useful BATSE data files and their
contents:

```
Naming Convention         Contents

tte_bfits_YYYY.fits       time-sequenced 4-energy channel data bracketing
                          trigger; combines discla, preb, discsc, and tte.

discsc_bfits_YYYY.fits    time-sequenced 4-energy channel data bracketing
                          time of burst trigger for triggered detectors;
                          combines data types discla, preb and discsc.

(s)her_bfits_X_YYYY.fits  time-sequenced 128 energy channel data bracketing
                          time of burst trigger for specified detector;
                          combines datatypes her and herb - suggested data
                          type for 128 energy channel burst analysis.

mer_bfits_YYYY.fits       time-sequenced 16-energy channel data for times
                          bracketing burst trigger - triggered detectors
                          only; combines mer and cont datatypes - suggested
                          for 16-energy channel burst analysis.

discsc_drm_YYYY.fits      detector response matrix for 4 energy channel burst
                          data triggered detectors only; used with 4-energy
                          channel data to determine burst photon spectra.

her_drm_X_YYYY.fits       detector response matrix for 128-energy channel
                          burst data for specified detector; used with
                          128-energy channel counts data to generate burst
                          photon spectra.

mer_drm_YYYY.fits         detector response matrix for 16-energy channel burst
                          data triggered detectors only; used with 16-energy
                          channel data to generate burst photon spectra.

cont_TJD_fits             8 BATSE detectors, 2.048s resolution/16 energy
                          channels.

discla_TJD.fits           8 BATSE detectors, 1.024 s resolution/4 energy
                          channels.

XXX_TJD1_TJD2_his.fits    Occultation histories.

XXX_TJD1_TJD2_nhis.fits   Data for one or more BATSE detectors for available
                          energy channels as source count rate (counts/sec)
                          from which the background has been subtracted -
                          used for light curves.

XXX_TJD_lad_p11.fits      Pulsar low level data.

XXX_TJD1_TJD2_lad_olc     Light curve file for a given pulsar.
```

where YYYY = trigger number, XXXX = source name, TJD = Truncated Julian Day,
X = detector number.

Notice that, because of the instrument configuration at the time of the event,
the same files are not available for all triggers. Spectral (SD) data are
prefixed with an 's' (e.g. 'sher').

Available data taken prior to the trigger may contain the beginning of the
triggering event before it satisfied the triggering criteria. Background-type
files can be used to remove background signal levels from the triggered
period. The BFITS data files - containing burst and background spectral data
as a function of time - and the detector response matrices (DRM) - modeling
the instrument response to account for scattering and other effects - are
extremely useful for gamma-ray burst analysis. Also, the BFITS and DRM files
can be converted to PHA-II and RMF format for analysis with XSPEC using
available FTOOLS. Other file types exist, notice, and advice on their use
is obtainable at grohelp@athena.gsfc.nasa.gov.

* * *

### Burst Durations

This database contains values for T90 and T50, quantities
related to burst duration, for 1234 gamma-ray bursts that triggered the
BATSE LAD detectors between April 1991 and 29 August 1996.
T90 measures the duration of the time interval during which 90% of the
total observed counts have been detected. The start of the T90 interval
is defined by the time at which 5% of the total counts have been detected,
and the end of the T90 interval is defined by the time at which 95% of the
total counts have been detected. T50 is similarly defined using the times
at which 25% and 75% of the counts have been detected. T90 and T50 are
calculated using data summed over the 4 LAD discriminator channels and
using data summed over only those detectors that satisfied the BATSE
trigger criteria.

Users must note that T90 and T50 are not available for those bursts which
suffer from data gaps during the event; the integration procedure inherently
fails in these cases. However, visual estimates of the burst duration are
provided in the parameter Comments\_Duration for those bursts with
sufficient data coverage. Users may also find other pertinent comments
concerning the calculated value of T90 and T50 therein, and it is highly
recommended that this parameter be consulted before any distribution selected
on T90 or T50 is used.

Notice that the duration measurements for trigger 148 were recalculated
after errors in the 3B values were brought to the BATSE team's attention by
Dr. Jay Norris.

* * *

### Count Rates

This database contains 912 triggered bursts observed
from launch until 29 August 1996 for which peak count rates in units
of the threshold count rate, and threshold count rates, are available.
Many bursts do not have this information, particularly for those after
March 1992, since insufficient data exist to determine either their
peak counts or their threshold.

The BATSE on-board software tests for bursts by comparing the
count rates on the eight large-area detectors to threshold levels
for three separate time intervals: 64 ms, 256 ms, and 1024 ms. A
burst trigger occurs if the count rate is above threshold in two
or more detectors simultaneously. The thresholds are set by
command to a specified number of standard deviations above back-
ground (nominally 5.5 sigma). Background rates are recomputed
every 17 seconds. The thresholds exhibit a coarse quantization
that results from truncating the square root of the 64 ms count
rate. Since we require that rates be above the thresholds of at
least two detectors, the trigger threshold is determined by the
threshold of the second most brightly illuminated detector.
When a burst trigger occurs, subsequent triggers are disabled
during the accumulation period when the BATSE burst memories
accumulate data. These data are then transmitted. During this
readout period, the 64 ms threshold is revised to correspond to
the maximum rate attained by the current burst, and triggering is
disabled on the 256 ms and 1024 ms timescales. Bursts intense
enough to trigger during this readout period are termed "over-
writes". They are recognized in the database by the value of -999
in the threshold values for 256 ms and 1024 ms (called threshold\_256 and
threshold\_1024 in this database).

Since a trigger can occur on any of the three timescales, there
are often cases in which the maximum rate will be below threshold
on one or two of the timescales. The value of V/Vmax can be
determined for any burst by selecting the maximum of the three
peak rates, raised to the -3/2 power. Many bursts have unknown
counts or thresholds on one or more timescales. These are marked
by a "-999" in the database. This can happen for one of the follow-
ing reasons: (1) If the trigger occurs on the 64 ms timescale during
the peak 256 ms rate, then the peak 256 ms rate is not found;
(2) If the 64 ms peak rate never exceeds the 64 ms threshold, and it
occurs before the trigger time, then the peak 64 ms rate is not found;
(3) If the 256 ms peak rate never exceeds the 256 ms threshold,
and it occurs before the trigger time, then the peak 256 ms rate is
not found. Note that items 2 and 3 do not affect V/Vmax, since these
peak rates do not exceed threshold; item 1 can, on rare occasions,
lead to an overestimate of V/Vmax.

* * *

### Fluxes and Fluences

This database contains the fluence and peak flux
values for the BATSE gamma-ray bursts between 19 April, 1991 and
29 August, 1996. There are 1292 bursts, each specified by the BATSE
trigger number. All fluences and their errors have units of of ergs/cm2.
All peak fluxes and their errors have units of photons/cm2/sec. The errors
are the one-sigma statistical errors. The peak flux times are expressed
in decimal seconds relative to the burst trigger time for the end of the
interval in which the flux was calculated. The channel 1,2,3 and 4 fluences
cover the energy ranges 20-50 keV, 50-100 keV, 100-300 keV, and E > 300 keV,
respectively. The peak flux energy range is 50-300 keV, coinciding with the
energy range of the nominal BATSE on-board burst trigger. Since channel 4 is
an integral channel, fluences given for this channel are quite sensitive to
the assumed spectral form. Spectral analyses in this energy range should be
performed with higher resolution data types. Many of the bursts between
March 1992 and March 1993 have significant gaps in the data and therefore
do not have tabulated fluxes and fluences.

* * *

### Parameters

**Trigger\_Num**

The BATSE trigger number; this is a running sequence number
of BATSE triggers which include cosmic bursts, solar flares and other events.
The sequence in the 4B Catalog begins with trigger 105 and ends with
trigger 5586.

**Name**

The BATSE Catalog burst name. Each burst has a unique catalog name.
These BATSE catalog names later may be incorporated into a multi-spacecraft
catalog with "GB" or "GRB" replacing this designation of "4B". The characters
"4B " begin every 4B BATSE catalog burst name, followed by the "yymmdd" of
the burst, where "yymmdd" is the two digit year, two digit month, and two
digit day. When more than one gamma-ray burst occurs on one day, those bursts
have a single letter suffix (B,C,D...) that is generally in order of intensity.
Example: 4B 920503B refers to the second brightest burst that triggered BATSE
on May 3, 1992. The brightest burst on that day will have no suffix.

**RA**

Right Ascension in the default equinox.

**Dec**

Declination in the default equinox.

**LII**

Galactic longitude in decimal degrees.

**BII**

Galactic latitude in decimal degrees.

**Day\_Trigger**

The truncated Julian Date (TJD) of the trigger:
TJD = JD - 2440000.5

**Time**

The burst trigger time, converted to MJD for the Browse database, for the
convenience of searches and cross-correlations. The burst trigger time is the
end of the interval (64, 256 or 1024 ms) in which the burst triggered the
detector.

**Seconds\_Trigger**

The burst trigger time, in decimal seconds of the day (UT)
on which it occurred. The burst trigger time is the end of the interval (64,
256 or 1024 ms) in which the burst triggered the detector.

**Error\_Radius**

The radius in decimal degrees of the positional error box.
The error in angular location is the radius of a circle having
the same area as the 68% confidence ellipse defined by the formal
covariance matrix from a chi2 fit on the assumption of normal
errors. The error is based solely on the Poisson uncertainty in the
BATSE measurement of burst flux by each Large Area Detector. There is,
in addition, an RMS systematic error of approximately 1.6 degrees. Adding
1.6 degrees in quadrature to the value of this parameter yields the
BATSE team's estimate of the 68% confidence interval for the burst
location error. The statistical error is believed to be Gaussian.
The systematic error distribution has a more extended tail than a Gaussian.

**Earth\_Angle**

The angle in decimal degrees of the geocenter, i.e., the angle
between the burst and the nadir, as measured from the satellite.

**Overwrite**

The overwrite flag: this is Y (true) if this burst overwrote
an earlier, weaker trigger, N (false) otherwise.

**Overwritten**

The overwritten flag: this is Y (true) if this burst was
overwritten by a later, more intense trigger, N (false) otherwise.

**Max\_Cts\_64**

The maximum counts in the second most brightly illuminated
detector divided by the threshold count rate on the 64 ms timescale.

**Threshold\_64**

The trigger threshold on the 64 ms time-scale. It is the
number of counts in 64 ms required to trigger the second most brightly
illuminated detector for this particular burst.

**Flux\_64**

The peak flux on the 64 ms timescale in units of photons/cm2/sec.

**Flux\_64\_Error**

The one-sigma statistical error in the peak flux on the
64 ms timescale.

**Flux\_64\_Time**

The time of the peak flux on the 64 ms timescale, in decimal
seconds relative to the burst trigger time for the end of the interval in which
the flux was calculated.

**Max\_Cts\_256**

The maximum counts in the second most brightly illuminated
detector divided by the threshold count rate on the 256 ms timescale.

**Threshold\_256**

The trigger threshold on the 256 ms timescale. It is the
number of counts in 256 ms required to trigger the second most brightly
illuminated detector for this particular burst.

**Flux\_256**

The peak flux on the 256 ms timescale in units of photons/cm2/sec.

**Flux\_256\_Error**

The one-sigma statistical error in the peak flux on the
256 ms timescale.

**Flux\_256\_Time**

The time of the peak flux on the 256 ms timescale, in decimal
seconds relative to the burst trigger time for the end of the interval in which
the flux was calculated.

**Max\_Cts\_1024**

The maximum counts in the second most brightly illuminated
detector divided by the threshold count rate on the 1024 ms timescale.

**Threshold\_1024**

The trigger threshold on the 1024 ms timescale. It is the
number of counts in 1024 ms required to trigger the second most brightly
illuminated detector for this particular burst.

**Flux\_1024**

The peak flux on the 1024 ms timescale in units of
photons/cm2/sec.

**Flux\_1024\_Error**

The one-sigma statistical error in the peak flux on the
1024 ms timescale.

**Flux\_1024\_Time**

The time of the peak flux on the 1024 ms timescale, in
decimal seconds relative to the burst trigger time for the end of the interval
in which the flux was calculated.

**T50**

The 50% duration of the burst in seconds. T50 measures the duration of
the time interval during which 50% of the total observed counts have been
detected. The start of the T50 interval is defined by the time at which
25% of the total counts have been detected, and the end of the T50 interval
is defined by the time at which 75% of the total counts have been detected.

**T50\_Error**

The uncertainly in the T50 duration.

**T50\_Start**

The start time of the T50 interval, relative to the trigger
time (Time), in seconds.

**T90**

The 90% duration of the burst in seconds. T90 measures the duration of
the time interval during which 90% of the total observed counts have been
detected. The start of the T90 interval is defined by the time at which 5%
of the total counts have been detected, and the end of the T90 interval is
defined by the time at which 95% of the total counts have been detected.

**T90\_Error**

The uncertainty in the T90 duration.

**T90\_Start**

The start time of the T90 interval, relative to the trigger time
(Time), in seconds.

**Fluence\_1**

The fluence for Channel 1 (energy range 20-50 keV), in units of
ergs/cm2.

**Fluence\_1\_Error**

The error in the fluence for channel 1.

**Fluence\_2**

The fluence for Channel 2 (energy range 50-100 keV), in units of
ergs/cm2.

**Fluence\_2\_Error**

The error in the fluence for channel 2.

**Fluence\_3**

The fluence for Channel 3 (energy range 100-300 keV), in units of
ergs/cm2.

**Fluence\_3\_Error**

The error in the fluence for channel 3.

**Fluence\_4**

The fluence for Channel 4 (energy range E > 300 keV), in units of
ergs/cm2. Since channel 4 is an integral channel, fluences given for this
channel are quite sensitive to the assumed spectral form. Spectral analyses
in this energy range should be performed with higher resolution data types.

**Fluence\_4\_Error**

The error in the fluence for channel 4.

**Comments\_Quality**

Comments on data quality: not all gamma-ray bursts have
such comments.

**Comments\_Otherobs**

Comments on additional observations by other instruments:
not all gamma-ray bursts have such comments.

**Comments\_General**

General comments: not all gamma-ray bursts have such
comments.

**Comments\_Position**

Comments on the gamma-ray burst co-ordinates: not all
gamma-ray bursts have such comments.

**Comments\_Duration**

Comments on the gamma-ray burst duration: not all
gamma-ray bursts have such comments.

* * *

### Contact Person

Questions regarding the BATSE4B database table can be addressed to the
[HEASARC Help Desk](https://heasarc.gsfc.nasa.gov/cgi-bin/Feedback?selected=heasarc).

* * *

_Page Author:_ [Browse Software Development Team](https://heasarc.gsfc.nasa.gov/cgi-bin/Feedback?selected=w3browse)

_Last Modified:_ Monday, 16-Sep-2024 17:24:55 EDT

* * *

```

```
