Exact archive: Generatecode.tar.gz
Verified MD5: ce3dde9577579e057d94f7e1a13dd19c

MEMBER export/README
Final CatWISE AGN sample
0. Retrieve initial sample. Note that since extinction is always strictly
   positive, and the extinction coefficient of W2 is less than that of W1,
   the extinction-corrected W1-W2 will always be bluer than the observed
   W1-W2. So, if we wish to make a final cut of extinction-corrected W1-W2 >= 0.8,
   initially cutting on observed W1-W2 >= 0.8 will not miss objects, as no
   objects with observed W1-W2 < 0.8 will become redder after correction.

   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 80
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 70 and dec <= 80
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 60 and dec <= 70
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 50 and dec <= 60
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 40 and dec <= 50
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 30 and dec <= 40    Stopped
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 20 and dec <= 30    Stopped
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 10 and dec <= 20    Stopped
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 0 and dec <= 10     Stopped
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -10 and dec <= 0    Stopped
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -20 and dec <= -10  Stopped
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -30 and dec <= -20  Stopped
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -40 and dec <= -30
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -50 and dec <= -40
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -60 and dec <= -50
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -70 and dec <= -60
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -80 and dec <= -70
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec <= -80

   Split the ones that stopped:

   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 35 and dec <= 40
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 30 and dec <= 35
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 25 and dec <= 30
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 20 and dec <= 25
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 15 and dec <= 20
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 10 and dec <= 15
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 5 and dec <= 10
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > 0 and dec <= 5
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -5 and dec <= 0
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -10 and dec <= -5
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -15 and dec <= -10
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -20 and dec <= -15
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -25 and dec <= -20
   w1mpro - w2mpro >= 0.8 and w1sigmpro > 0 and w2sigmpro > 0 and dec > -30 and dec <= -25

   run check_tables.py in ~/catalogs/catwise_agn to make sure that the full dec range is
   satisfied and all queries are otherwise identical.

   There are 141,698,603 total objects.

1. Because of AstroPy's slow IPAC table read, open in TOPCAT and save each table as a FITS.

2. Run correct_catwise.py to take FITS files, correct them for extinction, correct their
   positions and proper motions, and make magnitude cuts.

   --> ~/catalogs/catwise_agn/catwise_agns_corr.fits

   (3,082,140 objects)

3. Load the output from step 2, and load the "final" masks

   exclude_master_final.fits

   This is a product of masking the output from step 2, getting the
   HEALPix distribution, converting to ra and dec with hpx_to_radec.py,
   and adding HEALPix pixel coordinates with high density to the mask.
   As these pixels cover less than 1 square degree, these higher density
   regions are likely contaminants missed by the original mask.

   - Add "dummy" primary and secondary radii, and position angles to the
     output from step 2, with values of 0.0 degrees.

   - The mask will have a radius and position angle already, but add a
     secondary radius as radius * ba. This is in degrees.

   Using TOPCAT's Sky Ellipses function with a Scale of 1.0 degrees, do
   an "All Matches", Join Type 1 not 2, where 1 is the output from
   step 2 and 2 is the mask file.

   --> 2,699,096 objects

   Finally, cut out the Galactic plane with abs(b) > 30. Note that this
   was chosen after first trying with 20 and looking at the HEALPix
   distribution. Moved files from abs(b) > 20 analysis to ./absb20/

   --> 1,355,409 objects.

   There is a small population of objects (57) with w1cov < 80. These
   have spuriously high w12 color. Remove these.

   --> 1,355,352 objects.

   Save as catwise_agns_masked_final.fits

   Note that objects cross-matched with DR16Q_v4.fits (3") indicates
   have a maximum pmchi2 = pow(pmra/sigpmra, 2) + pow(pmdec / sigpmdec, 2)
   of 829.48292. Making the cut pmchi2 > 830 on the original 1,355,352
   objects yields 325 sources, or 0.024%. This suggests that this is the
   rate of spurious sources with significant proper motions.

4. Make HEALPix map with mk_hpx.py

   In the exclude_master_final list, add 1 degree to the primary radius
   and make a secondary radius as (radius + 1) * ba. This is to avoid
   edge effects when excluding HEALPix pixels near the edge of masks.

   Do an exclusionary sky ellipse match between the masks and the
   HEALPix map, and then make the additional cut of abs(b) > 31 to deal
   with the edge effect near the Galactic plane. This results in 22329
   HEALPix.

   This results in a quasi-Gaussian distribution of HEALPix pixel
   densities with a peak at 67 AGNs / deg2, or a
   full-sky distribution of 2.8 million AGNs.

   Save this cut HEALPix table as a normal FITS file:

   hpx_final_masked.fits

5. Run hpx_vs_direction to determin the bias correction for ecliptic
   latitude, and make corrected density. This also produces a smoothed
   corrected density for visualization purposes.

   Figuring out  D = (smoothed - x) / x such that min(D) = - max(D), it
   looks like x = 68.55, which suggests that this is the true, intrinsic
   sky density of AGNs above this magnitude (w1 < 16.4). Then, the total
   number of AGNs across the sky would be 2,827,890. Use
   random_coordinates_faster.py to make a random sky with this many
   AGNs. Then run mk_hpx.py to make its HEALPix map. This has a
   dispersion of 9.05 / deg^2, while the sample map has a dispersion of
   9.96. This suggests an intrinsic dispersion of 4.16 / deg^2, or 6.06%.

6. Finally, run lookup_alpha_catwise.py to get the spectral indices.
   This differs from lookup_alpha_allwise.py only in that the w1mpro and
   w2mpro columns are the extinction-corrected w1 and w2 columns. The
   reference files alpha_colors.fits and RSR-W1.txt are simply copied
   into the ./final directory.

7. Running NWAY on Stripe 82 subsample:

   Stripe 82 subsample:

   (ra > 360-42 || ra < 45) && dec >= -1.25 && dec <= 1.25

   has one masked region removed, leaving an area 215 square degrees.

   Make this selection on the CatWISE AGNs, but give a 10" buffer to
   allow for objects that may have scattered out of this region:


   (ra > 360 - 42 - 10/3600/cos(dec * PI / 180)  || ra < 45 + 10/3600/cos(dec * PI / 180)) && dec >= -1.25 - 10/3600 && dec <= 1.25 + 10/3600

   --> 14402 objects.

   Saved as catwise_agns_masked_final_s82.fits
   
   
   # OPTICAL CATALOGS
   Produce sample of bona fide AGNs/quasars in Stripe 82 sub-sample 
   footprint using SDSS DR16Q_v4.fits.
   
   --> 15139 objects with Gaia DR2 coordinates (native J2015.5)
      
   
   It appears that there is some zonal error in the DES1 Stripe 82 
   footprint. The offets are quite good, so a 0.3 arcsec match 
   gives 15072 counterparts (99.6%). Taking 
   
   dra = (RAFdeg - GAIA_RA) * cos(degreesToRadians(GAIA_DEC)) * 3600 * 1000
   ddec = (DEFdeg - GAIA_DEC) * 3600 * 1000
   
   The mean of dra  =  -86.0 +/- 0.4 mas
               ddec = +124.0 +/- 0.3 mas
               
   where the error is the standard error of the mean (N=15072). 
   Note that hypot(86 mas, 124 mas) = 151 mas, the same astrometric 
   precision quoted in Abbott+2018. 
   
   Test: retrieving ALL associations within 0.5 arcsec of the DR16Q 
   sample, 
   
   deccorr = DEFdeg - 124.0/1000/3600
   racorr = RAFdeg + 86.0/1000/3600/cos(degreesToRadians(deccorr))
   
   Note that the ".0" is both significant and required, as entering 
   these values as integers results in the latter terms being set to 0.
   
   Matching back onto DR16Q, there are 15086 matches (compared with 
   15072 as before). The mean offset is dramatically improved, down to 
   50.1 mas, from 157 mas before. The dispersions of dra and ddec, using 
   these corrected coordinates, are 0.046 and 0.034 arcsec, or an overall 
   position error of 0.057 arcsec. The total offset does not show any 
   trend with imag, indicating that 0.057 arcsec can be taken as the 
   overall position error for the (corrected) catalog.
   
   
   Retrieve ALL DES1 counterparts to the 14402 catwise AGNs to within 
   11 arcsec --> 49171. 
   
   Make deccorr, racorr as before. Make Separation column as 
   
   skyDistanceDegrees(ra, dec, racorr, deccorr) * 3600
   
   Note the improvement over the "angDist" column created from the CDS 
   match. Make a cut at Separation < 10 arcsec.
   
   --> 43028 DES matches, 42892 unique objects.
   
   Save this as des1_s82.fits
   
   Using Astropy, make an IPAC file des1_s82.ipac that has the DES 
   designation, and racorr/deccorr as ra/dec. Match this back to the 
   full CatWISE2020 catalog in IRSA using a 10" match, one to one.
   
   Download as des1_s82.tbl
   
   Match on CatWISE source_id back to the catwise_agns_masked_final_s82.fits 
   table excluding any objects in which the best match is NOT in the 
   CatWISE AGN sample.
   
   --> 26721 unique DES sources in which the closest CatWISE2020 association 
   is in the CatWISE AGN sample.
   
   Retrieve the other DES data by matching des1_s82.fits onto this using 
   the DES identifier.
   
   Now, do a Best match on CatWISE ra, dec, and DES racorr, decorr, 
   using a 10" match.
   
   --> 14193 matches, out of 14402 (98.5%).
   
   Save this as des1_s82_best.fits
      
   Taking a best match between des1_s82_best.fits and SDSS DR7 to within 
   1", there are 11962 unique associations. Taking 
   
   drmag = rmag_x - rmag
   
   where rmag_x is the SDSS DR7 mag, the value that must be subtracted 
   to center this distribution at zero is 0.04 mag. So,
   
   rmag_SDSS = rmag_DES1 + 0.04
   
   Yan et al. (2013) use r(AB) - r(Vega) = 0.16
   
   So, r_Vega = rmag_SDSS - 0.16 = rmag_DES1 + 0.04 - 0.16
   
   Then, r - W2 as in Yan et al. goes as
   
   rw2 = rmag_DES1 + 0.04 - 0.16 - w2
   
   Note that w2 here was corrected for Galactic extinction, while r was 
   not. Given the very small extinction coefficient of w2, and the low 
   extinction in Stripe 82, the maximum error introduced here is less 
   than 0.018 mag, and is 0.004 mag on average.
   
   Match the des1_s82_best.fits onto specObj-dr16.fits to within 1".
   
   --> 8594 matches (61%)
   
   The mean w2 of the matches is 14.5099, while the mean w2 of the 
   5599 non-matches is 14.8273, or a difference of 0.3174 mag. The 
   mean r - W2, however, is 5.23915 for the matches and 7.14382 for the 
   non-matches, a difference of 1.9047 mag. 
   
   Save this as specObj-dr16_s82.fits
   
   Now, repeat this for ZWARNING==0
   
   --> 8017 matches
   
   Save as specObj-dr16_s82_zwarning0.fits
   
   Other than suppression of likely spurious z=0 sources, this latter 
   file has a redshift distribution nearly identical to the former.
   


MEMBER export/hpx_vs_direction.py
#!/usr/bin/env python
import numpy as np
from scipy.stats import pearsonr, sem
from scipy.optimize import curve_fit
import astropy.units as u
from astropy.table import Table, vstack
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt

t = Table.read('catwise_agns_masked_final_alpha_hpx.fits')

# Split t on masked and unmasked
msk = t['density'] < 0
masked = t[msk]
t = t[~msk]

binsize = 1

def getstat(xkey, ykey, absx=True, xtyp='lat'):
    if absx == True and xtyp=='lat':
        xs = np.abs(t[xkey].data)
        bins = np.arange(0, 91, binsize)


    elif absx == True and xtyp=='lon':
        xs = t[xkey].data % 180
        bins = np.arange(0, 181, binsize)

    elif absx == False and xtyp=='lat':
        xs = t[xkey].data
        bins = np.arange(-90, 91, binsize)
    elif absx == False and xtyp=='lon':
        xs = t[xkey].data
        bins = np.arange(0, 361, binsize)
    else:
        raise NameError("unrecognized absx or xtyp.")

    binx = bins[0:-1] + binsize / 2
    idx = np.digitize(xs, bins, right=False)

    stat = np.empty((binx.size, 3), dtype=float)
    for i in range(1, binx.size + 1):
        density = t[idx==i][ykey].data
        if density.size < 10:
            stat[i-1, 0] = np.nan
            stat[i-1, 1] = np.nan
        else:
            stat[i-1, 0] = density.mean()
            stat[i-1, 1] = sem(density)

        stat[i-1, 2] = density.size

    msk = np.isfinite(stat[:,1])

    return binx[msk], stat[msk]


def residual(fx, x, y, w):
    r = y - fx
    z = r * w   # z-score
    chi2 = np.sum(z**2)
    dof = x.size - 2
    print("z-score stdev: %.2f" % z.std())
    print("chi2/dof: %.2f/%i = %.2f" % (chi2, dof, chi2/dof))

    return r, z, chi2, dof


def linreg(x, y, w):
    print("Pearson r: %.2f" % pearsonr(x, y)[0])
    p, pcov = np.polyfit(x, y, deg=1, w=w, cov=True)
    perr = np.sqrt(np.diag(pcov))
    print("Equation of fit: y = %.3f(%.3f) * x + %.1f(%.1f)" % (p[0], perr[0],
                                                                p[1], perr[1]))
    fx = np.polyval(p, x)
    r, z, chi2, dof = residual(fx, x, y, w)

    return p, pcov, fx, z, chi2, dof


def pltstat(x, stat):
    plt.errorbar(x, stat[:,0], xerr=binsize/2, yerr=stat[:,1],
                 linestyle='')


# Make linear regression to "correct" density and see if there is an
# additional component due to the Galactic plane.
p = np.polyfit(np.abs(t['elat']), t['density'], deg=1)
print("Equation of raw fit: y = %.3f * x + %.1f" % (p[0], p[1]))

print("Bin size: %.1f deg" % binsize)
x, estat = getstat('elat', 'density', absx=True)
p, pcov, fx, z, chi2, dof = linreg(np.abs(x), estat[:,0], 1 / estat[:,1])

#jointfit(x, estat[:,0], 1 / estat[:,1])

prand = np.random.multivariate_normal(p, pcov, 1000)
for pr in prand:
    plt.plot(x, np.polyval(pr, x), c='k', alpha=0.01, zorder=0)



pltstat(x, estat)
#plt.plot(x, np.polyval(p,x))
plt.xlabel('absolute ecliptic latitude')
plt.ylabel('deg$^{-2}$')
plt.title("y = %.3f * x + %.1f" % (p[0], p[1]))
plt.show()

# Save p and its covariance
np.save('p.npy', p)
np.save('pcov.npy', pcov)

# Sebastian's values:
p[0] = -0.05126576725374681
p[1] = 68.89130135046557

t['denscorr'] = t['density'] - np.polyval(p, np.abs(t['elat'])) + p[1]


# Now look at Galactic latitude

#t = t[(t['l'] > 130) & (t['l']<150)]
x, bstat = getstat('b', 'denscorr', absx=False)

# Make smoothed average for map
print("Calculating smoothed corrected density...")

def omega_to_theta(omega):
    """Convert solid angle omega in steradians to theta in radians for
    a cone section of a sphere."""
    return np.arccos(1 - omega / (2 * np.pi)) * u.rad


theta = omega_to_theta(1)
#theta = 1 * u.rad

# Alternatively, smooth on the scales of a multipole component
#l = 5
#theta = omega_to_theta(2 * np.pi / l)
lent = len(t)
sc = SkyCoord(t['ra'], t['dec'], frame='icrs')
t['smoothed'] = -1 * np.ones(lent)
t['sterr'] = -1 * np.ones(lent)
t['Nsmooth'] = -1 * np.ones(lent)
t['alphasmoothed'] = np.nan * np.ones(lent) # New
t['alphasterr'] = np.nan * np.ones(lent)
t['smoothed_uncorrected'] = -1 * np.ones(lent)
t['sterr_uncorrected'] = -1 * np.ones(lent)
for i in range(lent):
    d2d = sc[i].separation(sc)
    msk = d2d < theta
    sample = t[msk]['denscorr']
    t['smoothed'][i] = sample.mean()
    t['sterr'][i] = sem(sample)
    t['Nsmooth'][i] = sample.size
    sample = t[msk]['alpha']
    t['alphasmoothed'][i] = sample.mean()
    t['alphasterr'][i] = sem(sample)
    sample = t[msk]['density']
    t['smoothed_uncorrected'][i] = sample.mean()
    t['sterr_uncorrected'][i] = sem(sample)
    print("\t%.1f%%" % ((i + 1) / lent * 100), end='\r')

masked['density'] = np.nan
masked['denscorr'] = np.nan
t = vstack((t, masked))
t.sort('hpidx')

t.write('steradian_smoothed.fits', overwrite=True)
pltstat(x, bstat)
#plt.plot(x, y)
plt.xlabel('Galactic latitude (ecliptic bias-corrected)')
plt.ylabel('HEALPix density')
plt.show()
