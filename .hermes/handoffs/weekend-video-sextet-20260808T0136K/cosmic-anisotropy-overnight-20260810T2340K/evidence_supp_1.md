URL: https://irsa.ipac.caltech.edu/data/Quaia/docs/quaia_colDescriptions.html

[NASA/IPAC\\
\\
Infrared\\
\\
Science\\
\\
Archive](https://irsa.ipac.caltech.edu/)

About

\|

Holdings

\|

Data Access

\|

Help

Login

# Quaia: the Gaia-unWISE Quasar Catalog Definitions

#### Overview

Quaia samples the largest comoving volume of any
existing spectroscopic quasar sample. The catalog draws on the 6,649,162 quasar candidates identified
by the Gaia mission that have redshift estimates from the space observatory's low-resolution blue
photometer/red photometer spectra.
Quaia combines the Gaia candidates with unWISE infrared data (based on the Wide-field Infrared
Survey Explorer survey) to construct a catalog useful for cosmological and astrophysical quasar studies. The final catalog has 1,295,502
quasars with G < 20.5, and 755,850 candidates in an even cleaner G < 20.0 sample, with accompanying
rigorous selection function models.

If you use Quaia, please cite [Storey-Fisher et al. (2024)](https://iopscience.iop.org/article/10.3847/1538-4357/ad1328) and the dataset Digital Object Identifier (DOI): [https://zenodo.org/records/10403370](https://zenodo.org/records/10403370).

| Name | Intype | Units | Description |
| --- | --- | --- | --- |
| source\_id | long |  | Gaia DR3 source identifier |
| unwise\_objid | char |  | unWISE DR1 source identifier |
| redshift\_quaia | double |  | spectroscopic redshift estimate |
| redshift\_quaia\_err | double |  | uncertainty on redshift\_quaia |
| ra | double | deg | Right Ascension (ICRS 2016.0) |
| dec | double | deg | Declination (ICRS 2016.0) |
| l | double | deg | Galactic longitute |
| b | double | deg | Galactic latitude |
| phot\_g\_mean\_mag | double | mag | Gaia G-band mean magnitude |
| phot\_bp\_mean\_mag | double | mag | Gaia integrated BP mean magnitude |
| phot\_rp\_mean\_mag | double | mag | Gaia integrated RP mean magnitude |
| mag\_w1\_vg | double | mag | unWISE W1 magnitude |
| mag\_w2\_vg | double | mag | unWISE W2 magnitude |
| pm | double | mas/yr | Total proper motion |
| pmra | double | mas/yr | proper motion in right ascension in ICRS at 2016.0 |
| pmdec | double | mas/yr | proper motion in declination in ICRS at 2016.0 |
| pmra\_error | double | mas/yr | standard error in pmra |
| pmdec\_error | double | mas/yr | standard error in pmdec |

- [Contact](https://irsa.ipac.caltech.edu/docs/help_desk.html)
- [Privacy Policy](https://irsa.ipac.caltech.edu/privacy.html)
- [Acknowledge IRSA](https://irsa.ipac.caltech.edu/ack.html)

Search IRSA

[![Icon_ipac](https://irsa.ipac.caltech.edu/frontpage/images/icon_ipac-white-78x60.png)](http://www.ipac.caltech.edu/ "Infrared Processing and Analysis Center")[![Icon_caltech](https://irsa.ipac.caltech.edu/frontpage/images/icon_caltech-new.png)](http://www.caltech.edu/ "California Institute of Technology")[![Icon_jpl](https://irsa.ipac.caltech.edu/frontpage/images/icon_jpl-white-91x60.png)](http://www.jpl.nasa.gov/ "Jet Propulsion Laboratory")[![Icon_nasa](https://irsa.ipac.caltech.edu/frontpage/images/icon_nasa-white-59x60.png)](http://www.nasa.gov/ "National Aeronautics and Space Administration")
