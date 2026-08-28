This 2020README.txt file contains minimal information to help users access the
CatWISE2020 Catalog, and was written on 2020 May 4. The web page 
https://catwise.github.io contains the latest updates to CatWISE information.

The CatWISE2020 Catalog is available via the Infrared Science Archive 
(https://irsa.ipac.caltech.edu) in the WISE/NEOWISE Enhanced and Contributed 
Products area, and at https://portal.nersc.gov/project/cosmo/data/CatWISE/2020) 
 
The CatWISE2020 Catalog consists of 1,890,715,640 sources over the entire 
sky selected from WISE and NEOWISE survey data at 3.4 and 4.6 microns (W1 and 
W2) collected from 2010 Jan. 7 to 2018 Dec. 13. This dataset includes six times 
as many exposures and spans over sixteen times as large a time baseline as the 
AllWISE catalog. CatWISE adapts AllWISE software to measure the sources in 
co-added images created from six-month subsets of these data, each representing 
one coverage of the inertial sky, or epoch. CatWISE2020 includes the measured 
motion of sources over the 8 year span of the data, typically in 12 epochs. The 
scatter with respect to Spitzer photometry at faint magnitudes in fields out of 
the Galactic plane and at low ecliptic latitude (corresponding to lower WISE 
coverage depth) is similar to the CatWISE Preliminary Catalog, reaching
0.217 mag (equivalent to SNR 5) at approximately W1=17.7 and W2=16.5, vs. 
W1=16.9 and W2=15.9 for AllWISE. The 90% completeness depth for CatWISE2020 is 
at roughly W1=17.7 and W2=17.5, about 1.7 mag deeper than in the Preliminary 
Catalog. From comparison to Gaia, the motions are over a dozen times more 
accurate than those from AllWISE. 

The primary differences between the CatWISE2020 and CatWISE Preliminary 
Catalogs are:

1) The detection list for CatWISE2020 uses an updated version of the unWISE 
Catalog (Schlafly et al., ApJS, 240, 30, 2019) available at 
https://faun.rc.fas.harvard.edu/unwise/neo5/band-merged
The unWISE Catalog was generated using "crowdsource" software, while the 
Preliminary Catalog used the "MDET" software (the detection software used 
for AllWISE; Marsh and Jarrett, PASA, 29, 269, 2012) to generate the detection 
list. The crowdsource software is much better at recovering source detections 
in high-density regions such as the Galactic plane. The identification number 
for the source detection (unwise_objid) is included in the CatWISE2020 output.

2) The CatWISE2020 Catalog is based on data obtained in the W1 and W2 bands 
with WISE and NEOWISE through December 2018, adding two years to the data sets
used for the Preliminary Catalog source measurements. This results in more 
accurate motion measurements.

These two factors result in roughly twice as many sources in CatWISE2020.

3) While both catalogs use the WPHOT point spread function fitting software 
to measure positions, motions, and photometry for detected sources, no attempt 
was made to improve the fit by adding new sources to the detection list in  
CatWISE2020. For the Preliminary Catalog, up to 3 iterations of adding sources 
were made.

4) Both catalogs measured photometry separately in data from survey scans 
with ascending ecliptic latitude vs. descending latitude, but the final 
aperture values are the result of averaging fluxes in the CatWISE2020 Catalog, 
while in the Preliminary Catalog, the aperture magnitudes were averaged.

5) A more accurate algorithm was used for calculating Galactic coordinates 
in the CatWISE2020 Catalog, so these coordinates are provided in the IRSA 
release, while they are hidden in the IRSA release for the Preliminary Catalog.

6) Coordinates in the CatWISE2020 Catalog are in the ICRS system at epoch 
MJD=57170, while in the Preliminary Catalog they are in J2000 at epoch 
MJD=56700.
 
The CatWISE2020 Catalog on NERSC is separated into 18,240 gzipped ascii 
files in IPAC table format, one for each of the same number of spatially 
overlapping tiles, using the same equatorial coordinate grid as for WISE and 
unWISE. The 52 tiles nearest the ecliptic poles used slightly different
processing, and their file names contain the string "opt0_2020" and do not
have an underscore ("_") separating the date and time stamp in the name. All
other file names contain the string "opt1_2019" and have an underscore
separating the date and time stamp in the name. Two of the 52 tiles with
"opt0" processing in the CatWISE2020 Catalog (0816m667 and 2597p666) were
processed with "opt1" in the Preliminary Catalog.   All file names begin 
with an 8 character string of form:

rrrrsddd

where rrrr is the decimal right ascension and sddd is the signed declination 
of the tile center to 0.1 degrees, in J2000, with s being "p" for positive
declination or "m" for negative declination. The WISE tile lookup service at 
https://irsa.ipac.caltech.edu/applications/WISETiles/ 
provides a useful tool for identifying the tile(s) containing a coordinate.

For example, the brown dwarf Gliese 570D, at RA 14h57m16.2s, or 224.3175 in 
decimal form, and declination -21d22m16s, will be found in the file with the 
prefix 2243m213.

The files are organized on NERSC into 359 directories, one for each decimal 
degree of right ascension from 0 to 358 (there are no tiles beginning with 
359). For example the file containing Gliese 570D is in 
https://portal.nersc.gov/project/cosmo/data/CatWISE/2020/224.

Each catalog file contains typically 80,000 rows, one per source, with 
information similar to that in the AllWISE catalog 
(http://wise2.ipac.caltech.edu/docs/release/allwise/expsup/index.html).

On NERSC, there are 187 formatted columns of information about each source, 
with the column format and description specified in the file 
2020cwcat.sis20200318.txt at 
https://portal.nersc.gov/project/cosmo/data/CatWISE/. 
On IRSA, two columns (w1fitr and w2fitr) are hidden as they do not contain
useful information. Clicking on a column name in the query form on IRSA
provides the column format and description. Additional information about 
most of the columns is available via the AllWISE Explanatory Supplement.

CatWISE2020 Catalog sources are required to:
 
1) be "primary" in their tile (i.e. be from the tile where that source is 
furthest from the tile edge) 

and

2) have W1 SNR >= 5 with no identified artifacts (a value of 0 for the 
"ab_flags" in the W1 part (left character) of column 178) 

or

have W2 SNR >= 5 with no identified artifacts (a value of 0 for the "ab_flags" 
in the W2 part (right character) of column 178).

Sources that do not meet these criteria go into the reject file for their tile, 
so there are also 18,240 gzipped ascii reject files in IPAC table format, in 
the same decimal RA directory as their corresponding catalog file. Reject files 
typically contain 11,000 sources, although near the Galactic center this can 
reach over 120,000 due to the large number of artifacts. Reject files have one 
additional column (for a total of 188) indicating if the source is "primary" in 
its tile. The column format and description are specified in the file 
2020cwrej.sis20200318.txt on NERSC at the same location as the catalog file
specification. Catalog and reject file names for a given tile 
generally differ only in having the letters "cat" or "rej" as appropriate.

Additional information about the "primary" designation and the artifact flags
is given in Eisenhardt et al., ApJS 247, 69, 2020. 
