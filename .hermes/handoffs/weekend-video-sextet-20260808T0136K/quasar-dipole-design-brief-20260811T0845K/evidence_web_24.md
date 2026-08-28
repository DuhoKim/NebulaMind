CELL 0
import numpy as np
import healpy as hp
from healpy.newvisufunc import projview
from astropy.table import Table

import matplotlib
from matplotlib import pyplot as plt

CELL 1
matplotlib.rcParams['ytick.labelsize'] = 18
matplotlib.rcParams['xtick.labelsize'] = 18
matplotlib.rcParams['axes.labelsize'] = 22
matplotlib.rcParams['legend.fontsize'] = 18

matplotlib.rc('text', usetex=True)

CELL 2
cmap_map = 'plasma'

CELL 3
## Data access

CELL 4
The files are accessible on Zenodo at https://doi.org/10.5281/zenodo.10403370 (this notebook shows version 1.0.0).
    
The file names are:
- quaia_G\<Glim\>\<tag\>.fits
- random_G\<Glim\>_10x\<tag\>.fits
- selection_function_NSIDE64_G\<Glim\>\<tag\>.fits

where \<Glim\> is either 20.0 or 20.5, and \<tag\> is an empty string for the full catalogs.

More details are available in the Zenodo descriptions linked above, and in the Quaia publication: https://arxiv.org/abs/2306.17749.

We also show here the G<20.5 catalog split into two redshift bins and the associated selection functions, as used in the CMB lensing tomography analysis of Quaia: https://arxiv.org/abs/2306.17748. These are updated versions of the selection functions available at https://zenodo.org/records/8098636. The file names of the selection functions are the same as above, with \<tag\> replaced by 'zsplit2bin0' or 'zsplit2bin1' for the low-$z$ and high-$z$ split samples. The 'zsplit' catalogs loaded in below can be recreated by simply dividing the G<20.5 catalog into two redshift bins at the median redshift.

CELL 5
## Load data from local machine

CELL 6
fn_gcatlo = f'../data/quaia_G20.0.fits'
fn_gcathi = f'../data/quaia_G20.5.fits'

fn_sello = f"../data/maps/selection_function_NSIDE64_G20.0.fits"
fn_selhi = f"../data/maps/selection_function_NSIDE64_G20.5.fits"

fn_randlo = f'../data/randoms/random_G20.0_10x.fits'
fn_randhi = f'../data/randoms/random_G20.5_10x.fits'

CELL 7
fn_gcathi_zbin0 = f'../data/quaia_G20.5_zsplit2bin0.fits'
fn_gcathi_zbin1 = f'../data/quaia_G20.5_zsplit2bin1.fits'

fn_selhi_zbin0 = f"../data/maps/selection_function_NSIDE64_G20.5_zsplit2bin0.fits"
fn_selhi_zbin1 = f"../data/maps/selection_function_NSIDE64_G20.5_zsplit2bin1.fits"

CELL 8
## Parameters

CELL 9
NSIDE = 64
NPIX = hp.nside2npix(NSIDE)

CELL 10
name_catalog = '\emph{{Gaia}}-\emph{{unWISE}} Quasar Catalog'
abbrv_catalog = 'Quaia'

CELL 11
G_hi = 20.5
G_lo = 20.0

CELL 12
# for plotting purposes
fac_stdev = 1.5

CELL 13
## Quasar catalog

CELL 14
tab_gcatlo = Table.read(fn_gcatlo)
N_gcatlo = len(tab_gcatlo)
print(f"Number of data sources: {N_gcatlo}")

CELL 15
print(tab_gcatlo.meta)

CELL 16
print(f"Column names: {tab_gcatlo.columns}")

CELL 17
tab_gcathi = Table.read(fn_gcathi)
N_gcathi = len(tab_gcathi)
print(f"Number of data sources: {N_gcathi}")

CELL 18
### Make map of quasar number counts

CELL 19
pixel_indices_gcatlo = hp.ang2pix(NSIDE, tab_gcatlo['ra'], tab_gcatlo['dec'], lonlat=True)
map_gcatlo = np.bincount(pixel_indices_gcatlo, minlength=NPIX)

CELL 20
title_gcatlo = rf"{name_catalog}, $G<{G_lo}$ (N={len(tab_gcatlo):,})"
projview(map_gcatlo, title=title_gcatlo,
            unit=r"number density per healpixel (deg$^{-2}$)", cmap=cmap_map, coord=['C', 'G'], 
            min=np.median(map_gcatlo)-fac_stdev*np.std(map_gcatlo), max=np.median(map_gcatlo)+fac_stdev*np.std(map_gcatlo), 
            norm='log', graticule=True,
            cbar_ticks=[5, 10, 20]) 

CELL 21
pixel_indices_gcathi = hp.ang2pix(NSIDE, tab_gcathi['ra'], tab_gcathi['dec'], lonlat=True)
map_gcathi = np.bincount(pixel_indices_gcathi, minlength=NPIX)

CELL 22
title_gcathi = rf"{name_catalog}, $G<{G_hi}$ (N={len(tab_gcathi):,})"
projview(map_gcathi, title=title_gcathi,
            unit=r"number density per healpixel (deg$^{-2}$)", cmap=cmap_map, coord=['C', 'G'], 
            min=np.median(map_gcathi)-fac_stdev*np.std(map_gcathi), max=np.median(map_gcathi)+fac_stdev*np.std(map_gcathi), 
            norm='log', graticule=True,
            cbar_ticks=[5, 10, 20, 50]) 

CELL 23
## z-split catalogs

CELL 24
tab_gcathi_zbin0 = Table.read(fn_gcathi_zbin0)
N_gcathi_zbin0 = len(tab_gcathi_zbin0)
print(f"Number of data sources: {N_gcathi_zbin0}")

CELL 25
pixel_indices_gcathi_zbin0 = hp.ang2pix(NSIDE, tab_gcathi_zbin0['ra'], tab_gcathi_zbin0['dec'], lonlat=True)
map_gcathi_zbin0 = np.bincount(pixel_indices_gcathi_zbin0, minlength=NPIX)

CELL 26
title_gcathi_zbin0 = rf"{name_catalog}, low-$z$ bin, $G<{G_hi}$ (N={len(tab_gcathi_zbin0):,})"
projview(map_gcathi_zbin0, title=title_gcathi_zbin0,
            unit=r"number density per healpixel (deg$^{-2}$)", cmap=cmap_map, coord=['C', 'G'], 
            min=np.median(map_gcathi_zbin0)-fac_stdev*np.std(map_gcathi_zbin0), 
             max=np.median(map_gcathi_zbin0)+fac_stdev*np.std(map_gcathi_zbin0), 
            norm='log', graticule=True,
            cbar_ticks=[5, 10, 20, 50]) 

CELL 27
tab_gcathi_zbin1 = Table.read(fn_gcathi_zbin1)
N_gcathi_zbin1 = len(tab_gcathi_zbin1)
print(f"Number of data sources: {N_gcathi_zbin1}")

CELL 28
pixel_indices_gcathi_zbin1 = hp.ang2pix(NSIDE, tab_gcathi_zbin1['ra'], tab_gcathi_zbin1['dec'], lonlat=True)
map_gcathi_zbin1 = np.bincount(pixel_indices_gcathi_zbin1, minlength=NPIX)

CELL 29
title_gcathi_zbin1 = rf"{name_catalog}, high-$z$ bin, $G<{G_hi}$ (N={len(tab_gcathi_zbin1):,})"
projview(map_gcathi_zbin1, title=title_gcathi_zbin1,
            unit=r"number density per healpixel (deg$^{-2}$)", cmap=cmap_map, coord=['C', 'G'], 
            min=np.median(map_gcathi_zbin1)-fac_stdev*np.std(map_gcathi_zbin1), 
             max=np.median(map_gcathi_zbin1)+fac_stdev*np.std(map_gcathi_zbin1), 
            norm='log', graticule=True,
            cbar_ticks=[5, 10, 20, 50]) 

CELL 30
## Selection function models

CELL 31
map_sello = hp.read_map(fn_sello)
print(np.min(map_sello), np.max(map_sello))

CELL 32
np.arange(0, max(map_sello), 0.25)

CELL 33
projview(map_sello, title=rf"Selection function model, $G<{G_lo}$",
            unit=r"relative completeness", cmap=cmap_map, coord=['C', 'G'], 
            graticule=True,
            min=0, max=np.max(map_sello),
            cbar_ticks=np.arange(0, max(map_sello), 0.25)
            ) 

CELL 34
map_selhi = hp.read_map(fn_selhi)
print(np.min(map_selhi), np.max(map_selhi))

CELL 35
projview(map_selhi, title=rf"Selection function model, $G<{G_hi}$",
            unit=r"relative completeness", cmap=cmap_map, coord=['C', 'G'], 
            graticule=True,
            min=0, max=np.max(map_selhi),
            cbar_ticks=np.arange(0, max(map_selhi), 0.25)
            ) 

CELL 36
map_selhi_zbin0 = hp.read_map(fn_selhi_zbin0)
print(np.min(map_selhi_zbin0), np.max(map_selhi_zbin0))

CELL 37
projview(map_selhi_zbin0, title=rf"Selection function model, low-$z$ bin, $G<{G_hi}$",
            unit=r"relative completeness", cmap=cmap_map, coord=['C', 'G'], 
            graticule=True,
            min=0, max=np.max(map_selhi_zbin0),
            cbar_ticks=np.arange(0, max(map_selhi_zbin0), 0.25)
            ) 

CELL 38
map_selhi_zbin1 = hp.read_map(fn_selhi_zbin1)
print(np.min(map_selhi_zbin1), np.max(map_selhi_zbin1))

CELL 39
projview(map_selhi_zbin1, title=rf"Selection function model, high-$z$ bin, $G<{G_hi}$",
            unit=r"relative completeness", cmap=cmap_map, coord=['C', 'G'], 
            graticule=True,
            min=0, max=np.max(map_selhi_zbin1),
            cbar_ticks=np.arange(0, max(map_selhi_zbin1), 0.25)
            ) 

CELL 40
## Random catalog

CELL 41
tab_randlo = Table.read(fn_randlo)
N_randlo = len(tab_randlo)
print(f"Number of random sources: {N_randlo}")

CELL 42
print(f"Column names: {tab_randlo.columns}")

CELL 43
tab_randhi = Table.read(fn_randhi)
N_randhi = len(tab_randhi)
print(f"Number of random sources: {N_randhi}")

CELL 44
### Make maps of random number counts

CELL 45
pixel_indices_randlo = hp.ang2pix(NSIDE, tab_randlo['ra'], tab_randlo['dec'], lonlat=True)
map_randlo = np.bincount(pixel_indices_randlo, minlength=NPIX)

CELL 46
projview(map_randlo, title=rf"Random catalog, $G<{G_lo}$ ($N={N_randlo}$)",
            unit=r"number density per healpixel (deg$^{-2}$)", cmap=cmap_map, coord=['C', 'G'], 
            min=np.median(map_randlo)-fac_stdev*np.std(map_randlo), 
            max=np.median(map_randlo)+fac_stdev*np.std(map_randlo), 
            norm='log', graticule=True,
            cbar_ticks=[50, 100, 200, 500]) 

CELL 47
pixel_indices_randhi = hp.ang2pix(NSIDE, tab_randhi['ra'], tab_randhi['dec'], lonlat=True)
map_randhi = np.bincount(pixel_indices_randhi, minlength=NPIX)

CELL 48
projview(map_randhi, title=rf"Random catalog, $G<{G_hi}$ ($N={N_randhi}$)",
            unit=r"number density per healpixel (deg$^{-2}$)", cmap=cmap_map, coord=['C', 'G'], 
            min=np.median(map_randhi)-fac_stdev*np.std(map_randhi), max=np.median(map_randhi)+fac_stdev*np.std(map_randhi), 
            norm='log', graticule=True,
            cbar_ticks=[100, 200, 500]) 

CELL 49
norm_factor = N_gcatlo/N_randlo
i_nonzero = np.abs(map_gcatlo)>1e-8
map_residuals_lo = np.full(len(map_randlo), np.nan)
map_residuals_lo[i_nonzero] = norm_factor*map_randlo[i_nonzero]/map_gcatlo[i_nonzero] - 1

CELL 50
projview(map_residuals_lo, title=rf"Residuals between data and random, $G<{G_lo}$",
            unit=r"$\bar{n}_\mathrm{rand} - \bar{n}_\mathrm{data}$ per healpixel (deg$^{-2}$) [normalized]", 
            cmap='coolwarm_r', coord=['C', 'G'], 
            min=-0.5, max=0.5, graticule=True,
            cbar_ticks=[-0.5, -0.25, 0, 0.25, 0.5]) 

CELL 51
norm_factor = N_gcathi/N_randhi
i_nonzero = np.abs(map_gcathi)>1e-8
map_residuals_hi = np.full(len(map_randhi), np.nan)
map_residuals_hi[i_nonzero] = norm_factor*map_randhi[i_nonzero]/map_gcathi[i_nonzero] - 1

CELL 52
projview(map_residuals_hi, title=rf"Residuals between data and random, $G<{G_hi}$",
            unit=r"$\bar{n}_\mathrm{rand} - \bar{n}_\mathrm{data}$ per healpixel (deg$^{-2}$) [normalized]", 
            cmap='coolwarm_r', coord=['C', 'G'], 
            min=-0.5, max=0.5, graticule=True,
            cbar_ticks=[-0.5, -0.25, 0, 0.25, 0.5]) 