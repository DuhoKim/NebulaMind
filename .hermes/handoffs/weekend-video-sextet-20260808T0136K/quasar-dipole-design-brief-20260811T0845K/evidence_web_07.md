                          NVSSlist

   NVSSlist is a program for listing selected portions of the NRAO/VLA
Sky Survey (NVSS) radio source catalog.  This survey is being made
with the NRAO VLA telescope at a frequency of 1.4 GHz and is producing
images that will cover the sky north of declination -40 deg with a
resolution of 45".  Both total intensity and linear polarization are
being imaged.  The list of sources found on these images and fitted by
elliptical Gaussians is stored as a FITS binary table.  NVSSlist
provides for selection, display, and interpretation of sources in this
catalog.

   NVSSlist can display selected portions of the catalog with various
corrections and computed errors associated with the source model
parameters (position, flux density, etc.).  All NVSS sources
satisfying several input criteria (e.g., minimum flux density,
location within a specified distance of a given celestial position)
can be displayed.  The selection criteria can be entered from the
keyboard or from a disk file.  NVSSlist is available at
ftp://nvss.nrao.edu/pub/NVSS/CATALOG/NVSSlist210.tar.gz.  Contact
bcotton@nrao.edu about any problems.

Unix Installation
---- ------------

   NVSSlist consists of a number of Fortran routines that call the
fitsio package of Bill Pence et al. at NASA.  Before installing
NVSSlist the fitsio package must first be installed (obtainable via
anonymous ftp://legacy.gsfc.nasa.gov/software/fitsio).  The current
distribution of fitsio (7/98) is fitsio406.tar.

    NVSSlist is distributed in the form of a Unix tar archive.  The
routine config.f must be edited to give the name of the directory in
which the master configuration file (NVSSlist.cfg) and the
documentation file (NVSSlist.hlp) will be installed.

   The Makefile may need to be edited to point to the correct
directory for the fitsio library (libfitsio.a) and possibly the
name and options for the Fortran compiler.  After these modifications,
NVSSlist can be generated using make; "make clean" will delete the
object files.  The resulting executable is NVSSlist.

   The OPEN statment in textfile.f uses the READONLY parameter to
allow users to read write-protected configuration files.  This is an
extension to Fortran and may not be supported on your system.  If the
compilation fails, remove the READONLY and rerun make.  In the latter
case users will need to make local copies of the configuration file.

   There are two text files which need to be available at run time: 
1) the configuration (NVSSlist.cfg) and 2) documentation (NVSSlist.hlp)
files.  These should be installed in the directory pointed to by
config.f. 

   The master configuration file may need to be modified to give the
full path name to the NVSS catalog FITS file.  There are also options
relating to the maximum number of characters in an output line and the
number of lines per page.  These are described in the comments in the
configuration file.

Usage
-----

   NVSSlist needs a number of pieces of information which come from
several places.  The name of the FITS file, the table version number,
the maximum number of characters in an output line etc. are given in a
configuration file (NVSSlist.cfg).  If a file by this name is in the
current working directory then it is used, else the site master
configuration file is used.  If the site master configuration file is
not found then standard defaults are used.  The most important of
these is that the NVSS catalog file is assumed to be in the current
working directory under the name of CATALOG.FIT.  The configuration
file can be edited to provide the desired values; comments follow the
"!".  If there is a problem reading the master configuration file
(usually involving write permission) then copy the master configuration
file to your current working directory.

   During the execution of NVSSlist, various selection/display options
are solicited interactively.  More details about each question can be
obtained by responding with a ?.  Hitting the enter/return key will
enter the default value(s).  The output can be either to the current
display window or to a disk file.  If the display is to the current
window, the program pauses occasionally and gives you a chance to
quit.

   Until the NVSS is completed a there are two possible reasons that a
source is not found at a given position: 1) there is no source
detectable by the NVSS within the search area or 2) the region
specified is not yet included in the catalog.  To help distinguish
between these cases a "verification" search box can be specified.  If
no source is found within the search area but one is found withing the 
search box then the distance to this source is given.  This determines
if there are other sources in the area implying that the NVSS has
included this region.  NOTE: this is not an absolutely certain test as
there are small areas not yet covered because those observations were
lost to excessive interference or other problems. A verification
search box half width of 5 arcmin (0.0833 degree) should include other
source if the area has been cataloged.

   If many fields are to be searched, you may list their positions in
a text file ("... input source list ...").  The text file contains one
line per field, and each line has up to 5 logical columns containing,
in order:
   1. Field center right ascension as hh mm ss.ss
   2. Field center declination as +/-dd mm ss.s
   3. (Optional) Search radius in arcsec (defaults to 15)
   4. (Optional) Verification halfwidth in arcsec (default 0 deg.).
   5. (Optional) Field label (defaults to blank)

   An example of a text file line is:
 12 34 56.78 -00 12 34.5 15  720 My Star
This will search for NVSS sources within 15".
of RA=12 34 56.78, Dec=-00 12 34.5.
If no source meeting the selection criteria is found within the 15"
but there is a source within 720" (12 arcmin.) then a note to this
effect is given. 

Esoteric notes:
-------- -----

   Terminal input is read from Fortran unit 5 which is stdin on Unix
systems; terminal output is to unit 6 (stdout) and error messages are
to unit 0 (stderr). 

   All input lines may contain a trailing comment delimited by a "!".

