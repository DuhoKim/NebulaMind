URL: https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b/4br_efficiency.html

BATSE4B Exposure vs Peak Flux Table

The [TRIGGER EFFICIENCY Table](http://gammaray.nsstc.nasa.gov/batse/grb/catalog/4b/tables/4br_grossc.trig_sen)
provides information about the BATSE instrument's sensitivity.
BATSE will generate a burst trigger if the count rate in two or more detectors
exceeds a threshold specified in units of standard deviations above background
(nominally 5.5). The rates are tested on three time scales: 64 ms, 256 ms and
1024 ms. The energy range is nominally 50 keV to 300 keV. These efficiencies
apply only to the nominal thresholds and energy range. A history of the
thresholds and energy range settings is provided in the Trigger Criteria Table.
The threshold in flux units depends on the background rate and the sky location
relative to the detector normals. The following table gives the efficiency for
generating a burst trigger as a function of peak flux on each of the three
trigger time scales. An efficiency of 100% indicates that a burst will always
generate a BATSE trigger if it is above the horizon and burst triggering is
enabled. Corrections for earth blockage and other flux-independent effects can
be made using the sky exposure map. The effects of atmospheric scattering are
not included in this table. As a result, the efficiencies at low fluxes are
underestimated. The thresholds are sensitive to the spectral shape of a
burst. The threshold for a hard burst is lower than the threshold for a
softer burst. The table assumes a power-law spectrum with an exponent of
-1.5. For an exponent of -2.5, the lower thresholds increase by
approximately 20%.

**The [TRIGGER EFFICIENCY Table](http://gammaray.nsstc.nasa.gov/batse/grb/catalog/4b/tables/4br_grossc.trig_sen)**
**is available for download.**

```
           64 ms                     256 ms                   1024 ms
   Threshold   Efficiency    Threshold   Efficiency    Threshold   Efficiency
 (ph/cm^2-sec)    (%)      (ph/cm^2-sec)    (%)      (ph/cm^2-sec)    (%)
     0.798        0.525        0.399        0.374        0.200        0.345
     0.825        1.126        0.412        0.962        0.206        0.874
     0.854        2.659        0.427        2.515        0.214        2.282
     0.886        7.692        0.443        7.510        0.221        6.864
     0.921       14.102        0.461       13.807        0.230       12.464
     0.960       22.307        0.480       21.900        0.240       19.757
     1.003       30.268        0.502       29.879        0.251       26.950
     1.051       39.003        0.526       38.654        0.263       35.085
     1.106       48.173        0.553       47.720        0.276       43.495
     1.168       57.535        0.584       57.144        0.292       52.898
     1.240       67.035        0.620       66.693        0.310       62.781
     1.324       76.202        0.662       76.024        0.331       72.333
     1.424       84.271        0.712       84.092        0.356       80.937
     1.546       88.856        0.773       88.775        0.386       86.426
     1.696       92.777        0.848       92.696        0.424       91.100
     1.890       96.059        0.945       96.012        0.473       95.123
     2.152       98.886        1.076       98.857        0.538       98.281
     2.527       99.951        1.263       99.944        0.632       99.696
     3.124       99.996        1.562       99.996        0.781       99.988
     6.247      100.000        3.124      100.000        1.562      100.000
```

Modification date:

28 Aug, 2018

Author: [BATSE GRB Team](mailto:jerry.fishman@nasa.gov)

Responsible Manager: [Steve Elrod](mailto:stephen.e.elrod@nasa.gov)

Site Curator: [Valerie Connaughton](mailto:valerie@nasa.gov)
