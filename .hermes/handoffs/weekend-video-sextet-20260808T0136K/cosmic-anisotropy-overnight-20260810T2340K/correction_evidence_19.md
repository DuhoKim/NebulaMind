URL: https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b/4br_trigger_criteria.html

BATSE4B Trigger Criteria Table

The [TRIGGER CRITERIA Table](http://gammaray.nsstc.nasa.gov/batse/grb/catalog/4b/tables/4br_grossc.trig_crit) contains
a history of the GRB trigger criteria.
BATSE will generate a burst trigger if the count rate in two or more detectors
exceeds a threshold specified in units of standard deviations above background
(nominally 5.5). The rates are tested on three time scales: 64 ms, 256 ms and
1024 ms. The energy range is nominally 50 keV to 300 keV. These efficiencies
apply only to the nominal thresholds and energy range. A history of the
thresholds and energy range settings is provided in the Trigger Criteria Table.
The threshold in flux units depends on the background rate and the sky location
relative to the detector normals.

The following table gives the efficiency for
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

**The [TRIGGER CRITERIA Table](http://gammaray.nsstc.nasa.gov/batse/grb/catalog/4b/tables/4br_grossc.trig_crit)**
**is available for download.**

The first column gives the date on which the trigger was changed,
the second column gives the truncated julian day ( _TJD_)
and the time of day in seconds ( _SOD_)
for the trigger change, the third column gives the channels used
for triggering, the fourth, fifth, and sixth columns gives
the trigger threshold above the
background count rate in units of standard deviation on the 64 ms, 256 ms,
and the 1024 ms timescales, and the final column gives the first
trigger occurring under the new criterion.
The channel numbers correspond to the following energy bands:

**Channel 1**: 20 keV to 50 keV

**Channel 2**: 50 keV to 100 keV

**Channel 3**: 100 keV to 300 keV

**Channel 4**: 300 keV and above

### BATSE Trigger Criteria History

```
      -------------------------------------------------------------------
       Date        TJD/SOD       Channels      Thresholds         Trig. #
                                            64   256   1024
      -------------------------------------------------------------------
      19-Apr-91                    2+3     5.5   5.25   5.0
      28-Apr-91   8367/5632                      5.5    5.5         105
      10-May-91   8386/75036                            7.0         179
      04-Jun-91   8411/68201                            5.5         268
      18-Aug-92   8852/56078                           10.0        1852
      24-Aug-92   8858/81762                     8.0    8.0        1874
      26-Aug-92   8860/78199                           10.0        1881
      14-Sep-92   8879/70852                     5.5    5.5        1928
      19-Sep-94   9614/57154       3+4                             3175
      31-Jan-95   9748/55085       1+2     6.0   6.0    6.0        3386
      06-Feb-95   9754/69000                           10.0        3405
      17-Feb-95   9765/62185       3+4     4.5   4.5    4.5        3434
      12-Apr-95   9819/56745       1+2     6.0   6.0    6.0        3504
      10-May-95   9847/74116                           10.0        3570
      20-Jul-95   9918/73523               20.0  10.0              3672
      21-Jul-95   9919/62439               10.                     3679 *
      24-Jul-95   9922/54971     1+2+3+4   26.0  6.0    6.0        3704
      28-Jul-95   9926/66825               10.0                    3713
      05-Sep-95   9965/60364               5.5   5.5    5.5        3778
      02-Oct-95   9992/77028       1+2                  7.0        3843
      23-Oct-95   10013/73672      2+3                  5.5        3883
      11-Dec-95   10062/77542       1                   3.5        3942 **
      18-Dec-95   10069/64796                           4.0        4027
      07-Jan-96   10089/62939     1+2+3                 5.5        4263
      05-Apr-96   10178/85399      2+3                             5413
      25-Jun-96   10259/53576      3+4     4.5   4.5    4.5        5520
      29-Aug-96   10324/77818      2+3     5.5   5.5    5.5        5589
      05-Nov-96   10392/70428      1+2                  7.0        5657 ***
      25-Feb-97   10504/80816      2+3                  5.5        6102
```

**\*** Trigger requires that only one detector be above threshold. No gamma-ray bursts were detected.

**\*\*** Trigger uses detector modules 2 and 3 only.

**\\*\\*\\*** Flight software crash on TJD/SOD 10416/16897 which was fixed TJD/SOD 10418/73555.

Modification date:

28 Aug, 2018

Author: [BATSE GRB Team](mailto:jerry.fishman@nasa.gov)

Responsible Manager: [Steve Elrod](mailto:stephen.e.elrod@nasa.gov)

Site Curator: [Valerie Connaughton](mailto:valerie@nasa.gov)
