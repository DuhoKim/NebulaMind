URL: https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b/4br_exposure.html

BATSE4B Exposure Table Description

The [EXPOSURE Table](http://gammaray.nsstc.nasa.gov/batse/grb/catalog/4b/tables/4br_grossc.exposure) specifies
the fraction of the time that a burst
at a particular point on the sky is detectable by BATSE, and accounts
for earth blockage, SAA passages, times when the burst trigger is disabled,
and times when a burst readout is in progress. It is a function of
declination only. The burst is assumed bright enough to exceed the
trigger threshold. A separate efficiency correction must also be included
in analysis of burst rates as a function of peak flux. This efficiency
is provided in a separate table; work is in progress to improve the
efficiency calculation by including atmospheric scattering and handling
of telemetry gaps.

Due to the failure of the GRO tape recorders and the presence of telemetry
gaps in the post-1B data, a different algorithm was used in preparing this
table than was used for the 1B catalog. The new algorithm not only handles
telemetry gaps, but is also more accurate in computing SAA passages. In
addition, the old algorithm excluded time intervals during which the trigger
thresholds were not at their standard settings of 5.5 sigma in each trigger
timescale, while the current algorithm does not. A separate table is
provided that specifies the history of the trigger thresholds. The
recomputed 1B exposure is higher (0.42 versus 0.38), due primarily to
the inclusion of times when thresholds were not at 5.5 sigma. The
galactic dipole moment of the sky exposure has changed by about 0.005,
due primarily to the more accurate accounting for the SAA. The change
in the galactic quadrupole moment is negligable.


In the exposure table below, the declination is given in degrees, and the
exposure fraction at that declination is given for each of the cumulative
catalogs (1B through 4B), and for each subset that was added to make the next
catalog. In the previous exposure tables, the exposure was an average over
a range of declinations of typically about 10 degrees. Here, the exposure
applies to a specific declination. The 4B catalog, currently in preparation,
ends on 29 August 1996.

Additional statistics are provided at the end of the table. The average
exposure is the average over the sky of the declination-dependant exposure
fraction. Total time is the time between the start and the end of the
catalog subset, in units of 10^6 seconds. Total exposure, the product
of the previous two numbers, is the total time, in units of 10^6 seconds
and averaged over the sky, that BATSE was sensitive was sensitive to bursts
for that catalog subset. The values of <cos(theta)> and
<sin^2(b)> - 1/3 are the galactic dipole and quadrupole moments
of the exposure. The values of
<sin(dec)> and <sin^2(dec)> - 1/3 are the dipole and quadrupole
moments in the equatorial coordinate system.

The uncertainty in the exposure fractions are roughly estimated at about 4%.
Possible sources of systematic error in the moments are currently under study,
but are expected to be less than 0.003 for the galactic moments.

**The [EXPOSURE Table](http://gammaray.nsstc.nasa.gov/batse/grb/catalog/4b/tables/4br_grossc.exposure)**
**is available for download.**

### Exposure

| dec | 1B exposure | 2B-1B exposure | 3B-2B exposure | 4B-3B exposure | 3B exposure | 4B exposure |
| --- | --- | --- | --- | --- | --- | --- |
| -90 | 0.45553 | 0.49902 | 0.53548 | 0.52248 | 0.50389 | 0.51041 |
| -85 | 0.45542 | 0.50579 | 0.53603 | 0.52286 | 0.50609 | 0.51198 |
| -80 | 0.47268 | 0.51779 | 0.55297 | 0.54599 | 0.52167 | 0.53020 |
| -75 | 0.47837 | 0.53424 | 0.56566 | 0.55382 | 0.53363 | 0.54072 |
| -70 | 0.47336 | 0.53057 | 0.56145 | 0.54889 | 0.52938 | 0.53622 |
| -65 | 0.46557 | 0.52308 | 0.55318 | 0.54085 | 0.52146 | 0.52827 |
| -60 | 0.45694 | 0.51377 | 0.54320 | 0.53163 | 0.51203 | 0.51891 |
| -55 | 0.44766 | 0.50368 | 0.53235 | 0.52180 | 0.50181 | 0.50882 |
| -50 | 0.43768 | 0.49225 | 0.52018 | 0.51085 | 0.49043 | 0.49759 |
| -45 | 0.42658 | 0.47904 | 0.50546 | 0.49780 | 0.47710 | 0.48436 |
| -40 | 0.41195 | 0.46345 | 0.49015 | 0.48016 | 0.46189 | 0.46830 |
| -35 | 0.40406 | 0.45560 | 0.48185 | 0.47065 | 0.45382 | 0.45973 |
| -30 | 0.39899 | 0.45045 | 0.47646 | 0.46457 | 0.44859 | 0.45420 |
| -25 | 0.39556 | 0.44697 | 0.47284 | 0.46047 | 0.44506 | 0.45047 |
| -20 | 0.39329 | 0.44468 | 0.47050 | 0.45775 | 0.44275 | 0.44801 |
| -15 | 0.39193 | 0.44333 | 0.46917 | 0.45610 | 0.44141 | 0.44656 |
| -10 | 0.39133 | 0.44279 | 0.46869 | 0.45536 | 0.44088 | 0.44596 |
| -5 | 0.39141 | 0.44296 | 0.46898 | 0.45543 | 0.44108 | 0.44611 |
| 0 | 0.39214 | 0.44382 | 0.47000 | 0.45626 | 0.44198 | 0.44699 |
| 5 | 0.39352 | 0.44537 | 0.47178 | 0.45786 | 0.44358 | 0.44859 |
| 10 | 0.39560 | 0.44765 | 0.47435 | 0.46028 | 0.44594 | 0.45097 |
| 15 | 0.39845 | 0.45076 | 0.47782 | 0.46361 | 0.44914 | 0.45422 |
| 20 | 0.40222 | 0.45484 | 0.48234 | 0.46803 | 0.45334 | 0.45850 |
| 25 | 0.40714 | 0.46013 | 0.48820 | 0.47381 | 0.45878 | 0.46406 |
| 30 | 0.41358 | 0.46701 | 0.49580 | 0.48141 | 0.46587 | 0.47133 |
| 35 | 0.42227 | 0.47618 | 0.50597 | 0.49170 | 0.47536 | 0.48109 |
| 40 | 0.43490 | 0.48917 | 0.52052 | 0.50682 | 0.48895 | 0.49522 |
| 45 | 0.45731 | 0.51329 | 0.54609 | 0.53375 | 0.51327 | 0.52045 |
| 50 | 0.47454 | 0.53442 | 0.56864 | 0.55250 | 0.53401 | 0.54050 |
| 55 | 0.48814 | 0.55085 | 0.58588 | 0.56754 | 0.55006 | 0.55620 |
| 60 | 0.50004 | 0.56440 | 0.60046 | 0.58048 | 0.56364 | 0.56955 |
| 65 | 0.51062 | 0.57654 | 0.61348 | 0.59207 | 0.57577 | 0.58149 |
| 70 | 0.51995 | 0.58646 | 0.62448 | 0.60197 | 0.58601 | 0.59161 |
| 75 | 0.52689 | 0.59336 | 0.63238 | 0.60909 | 0.59337 | 0.59889 |
| 80 | 0.52581 | 0.58562 | 0.62876 | 0.60688 | 0.58920 | 0.59540 |
| 85 | 0.51748 | 0.58184 | 0.62256 | 0.59335 | 0.58315 | 0.58673 |
| 90 | 0.51965 | 0.57835 | 0.62349 | 0.59353 | 0.58311 | 0.58677 |

### Exposure Statistics

|  | 1B | 2B-1B | 3B-2B | 4B-3B | 3B | 4B |
| --- | --- | --- | --- | --- | --- | --- |
| Average Exposure factor | 0.425 | 0.478 | 0.507 | 0.494 | 0.477 | 0.483 |
| Total Time (10^6s) | 27.9 | 31.1 | 49.1 | 61.36 | 108.1 | 171.5 |
| Total Exposure(10^6s) | 11.86 | 14.9 | 24.9 | 30.31 | 51.6 | 82.8 |
| No. of bursts | 260 | 325 | 537 | 515 | 1122 | 1637 |
| < cos(theta) > | -0.008 | -0.009 | -0.009 | -0.008 | -0.009 | -0.009 |
| < sin^2(b) > - 1/3 | -0.004 | -0.004 | -0.004 | -0.004 | -0.004 | -0.004 |
| < sin(dec) > | 0.017 | 0.018 | 0.019 | 0.017 | 0.018 | 0.018 |
| < sin^2(dec) > - 1/3 | 0.025 | 0.024 | 0.024 | 0.024 | 0.024 | 0.024 |

Modification date:

28 Aug, 2018

Author: [BATSE GRB Team](mailto:jerry.fishman@nasa.gov)

Responsible Manager: [Steve Elrod](mailto:stephen.e.elrod@nasa.gov)

Site Curator: [Valerie Connaughton](mailto:valerie@nasa.gov)
