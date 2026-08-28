URL: https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b/4br_basic.html

BATSEBATSE 4B GRB Catalog: Basic Information Table

The [BASIC Table](http://gammaray.nsstc.nasa.gov/batse/grb/catalog/4b/tables/4br_grossc.basic)
specifies the locations and times for 1637 triggered gamma-ray
bursts observed from 19 April, 1991 until 29 August, 1996. It therefore
includes the data from the 3B catalog. The current version (4Br) has been
revised from the version first circulated on CD-ROM in September 1997 (4B)
to include improved locations for a subset of bursts that have been
reprocessed using additional data.

Bursts since the end of the 1B catalog (March 1992) occurred when the
GRO tape recorders were experiencing numerous errors. Consequently,
there are gaps in the data of many bursts that preclude valid measurement
of peak flux, peak rate, fluence, or duration. Peak rates on the 1 second
timescale from each detector are almost always available. These data
(called MAXBC rates) can be used to determine burst location. Previous
difficulties with this data type have been largely removed, and we now
believe that the systematic errors for MAXBC-located bursts are the same
as for bursts located with other data types. It is still true however, that
the MAXBC-located bursts usually have larger statistical errors than would
be the case if another data type were available. The comments table provides
"L" comments for MAXBC-located bursts. A number of CGRO and BATSE flight
software changes have significantly reduced the problem of data gaps since
March of 1993.


The on-board software determines when a trigger occurs. When a burst
trigger occurs, subsequent triggers are disabled for an accumulation
period, during which the BATSE burst memories accumulate data. The
accumulation period was 242 seconds until Dec 17, 1992, and from
Jan 8, 1996 to Feb 25, 1997. At all other times it has been 573 seconds.
The stored burst data are then transmitted; the readout time for all
triggers was 90 minutes until Dec 17, 1992. At that date, the flight
software was revised to suspend readouts during telemetry gaps and to
truncate readouts of weak events. This resulted in a variable readout time.
During the burst data readout, the 64 ms threshold is revised to correspond
to the maximum rate attained by the current burst, and triggering is disabled
on the 256 ms and 1024 ms timescales. Bursts intense enough to trigger over
this revised 64 ms value are termed "overwrites". They appear as triggers in
this file, with the overwrite flag is set to 'Y'.

The BATSE trigger numbers correlate all the files for this catalog.
The trigger number is a running sequence of BATSE triggers which
include cosmic bursts, solar flares and other events. The sequence
begins with trigger 105 and ends with trigger 5586.

Each burst has a unique catalog name. These BATSE catalog names
later may be incorporated into a multi-spacecraft catalog with
"GB" or "GRB" replacing this designation of "4B". The characters
"4B " begin every BATSE catalog burst name, followed by the "yymmdd"
of the burst. "yymmdd" is the two digit year, two digit month, and
two digit day. When more than one gamma-ray burst occurs on one
day, those bursts have a single letter suffix (B,C,D...), generally
in order of intensity. Example: 4B 920503B
refers to the second brightest burst that triggered BATSE May 3, 1992.
The brightest burst on that day will have no suffix.

The burst trigger time is the end of the interval (64, 256 or 1024 ms)
on which the burst triggered the detector.

For burst locations, the table lists statistical errors only. The
systematic errors are [described online](https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b/locerr/locerr.html), and
in a companion paper to the 4B catalog, which is currently available
in
[ApJS](http://www.journals.uchicago.edu/ApJ/journal/issues/ApJS/v122n2/38846/38846.html) or on
[astro-ph](http://xxx.lanl.gov/abs/astro-ph/9901111).

**The [BASIC Table](http://gammaray.nsstc.nasa.gov/batse/grb/catalog/4b/tables/4br_grossc.basic)**
**is available for download.**

There are twelve columns in this file:


01. The BATSE trigger number.

02. The BATSE Catalog burst name.

03. The truncated Julian Date (TJD) of the trigger
     TJD = JD - 2440000.5

04. The time in decimal seconds of day (UT) of the trigger.

05. right ascension (J2000) in decimal degrees.

06. declination (J2000) in decimal degrees.

07. Galactic longitude in decimal degrees.

08. Galactic latitude in decimal degrees.

09. radius in decimal degrees of positional error box.

10. angle in decimal degrees of geocenter (the angle between the
     burst and the nadir, as measured from the satellite).

11. overwrite flag: Y(true) if this burst overwrote an
     earlier, weaker trigger. N(false) otherwise.

12. overwritten flag: Y(true) if this burst was overwritten
     by a later, more intense trigger. N(false) otherwise.


Modification date:

28 Aug, 2018

Author: [BATSE GRB Team](mailto:jerry.fishman@nasa.gov)

Responsible Manager: [Steve Elrod](mailto:stephen.e.elrod@nasa.gov)

Site Curator: [Valerie Connaughton](mailto:valerie@nasa.gov)
