{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "61bb548c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import healpy as hp\n",
    "from healpy.newvisufunc import projview\n",
    "from astropy.table import Table\n",
    "\n",
    "import matplotlib\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "92b82ad6",
   "metadata": {},
   "outputs": [],
   "source": [
    "matplotlib.rcParams['ytick.labelsize'] = 18\n",
    "matplotlib.rcParams['xtick.labelsize'] = 18\n",
    "matplotlib.rcParams['axes.labelsize'] = 22\n",
    "matplotlib.rcParams['legend.fontsize'] = 18\n",
    "\n",
    "matplotlib.rc('text', usetex=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "61df7955",
   "metadata": {},
   "outputs": [],
   "source": [
    "cmap_map = 'plasma'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7639326d",
   "metadata": {},
   "source": [
    "## Data access"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ff78eb3",
   "metadata": {},
   "source": [
    "The files are accessible on Zenodo at https://doi.org/10.5281/zenodo.10403370 (this notebook shows version 1.0.0).\n",
    "    \n",
    "The file names are:\n",
    "- quaia_G\\<Glim\\>\\<tag\\>.fits\n",
    "- random_G\\<Glim\\>_10x\\<tag\\>.fits\n",
    "- selection_function_NSIDE64_G\\<Glim\\>\\<tag\\>.fits\n",
    "\n",
    "where \\<Glim\\> is either 20.0 or 20.5, and \\<tag\\> is an empty string for the full catalogs.\n",
    "\n",
    "More details are available in the Zenodo descriptions linked above, and in the Quaia publication: https://arxiv.org/abs/2306.17749.\n",
    "\n",
    "We also show here the G<20.5 catalog split into two redshift bins and the associated selection functions, as used in the CMB lensing tomography analysis of Quaia: https://arxiv.org/abs/2306.17748. These are updated versions of the selection functions available at https://zenodo.org/records/8098636. The file names of the selection functions are the same as above, with \\<tag\\> replaced by 'zsplit2bin0' or 'zsplit2bin1' for the low-$z$ and high-$z$ split samples. The 'zsplit' catalogs loaded in below can be recreated by simply dividing the G<20.5 catalog into two redshift bins at the median redshift."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "55dcc75d",
   "metadata": {},
   "source": [
    "## Load data from local machine"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "acdbc2c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "fn_gcatlo = f'../data/quaia_G20.0.fits'\n",
    "fn_gcathi = f'../data/quaia_G20.5.fits'\n",
    "\n",
    "fn_sello = f\"../data/maps/selection_function_NSIDE64_G20.0.fits\"\n",
    "fn_selhi = f\"../data/maps/selection_function_NSIDE64_G20.5.fits\"\n",
    "\n",
    "fn_randlo = f'../data/randoms/random_G20.0_10x.fits'\n",
    "fn_randhi = f'../data/randoms/random_G20.5_10x.fits'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "27a6805e",
   "metadata": {},
   "outputs": [],
   "source": [
    "fn_gcathi_zbin0 = f'../data/quaia_G20.5_zsplit2bin0.fits'\n",
    "fn_gcathi_zbin1 = f'../data/quaia_G20.5_zsplit2bin1.fits'\n",
    "\n",
    "fn_selhi_zbin0 = f\"../data/maps/selection_function_NSIDE64_G20.5_zsplit2bin0.fits\"\n",
    "fn_selhi_zbin1 = f\"../data/maps/selection_function_NSIDE64_G20.5_zsplit2bin1.fits\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76c7ec92",
   "metadata": {},
   "source": [
    "## Parameters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a648ffd7",
   "metadata": {},
   "outputs": [],
   "source": [
    "NSIDE = 64\n",
    "NPIX = hp.nside2npix(NSIDE)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3a093816",
   "metadata": {},
   "outputs": [],
   "source": [
    "name_catalog = '\\emph{{Gaia}}-\\emph{{unWISE}} Quasar Catalog'\n",
    "abbrv_catalog = 'Quaia'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0e4f5a79",
   "metadata": {},
   "outputs": [],
   "source": [
    "G_hi = 20.5\n",
    "G_lo = 20.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5c71d3ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "# for plotting purposes\n",
    "fac_stdev = 1.5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "82e8839d",
   "metadata": {},
   "source": [
    "## Quasar catalog"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2de615dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of data sources: 755850\n"
     ]
    }
   ],
   "source": [
    "tab_gcatlo = Table.read(fn_gcatlo)\n",
    "N_gcatlo = len(tab_gcatlo)\n",
    "print(f\"Number of data sources: {N_gcatlo}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f07ca9e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "OrderedDict([('NAME', '\\\\emph{{Gaia}}--\\\\emph{{unWISE}} Quasar Catalog'), ('ABBRV', 'Quaia')])\n"
     ]
    }
   ],
   "source": [
    "print(tab_gcatlo.meta)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "003dcd02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Column names: <TableColumns names=('source_id','unwise_objid','redshift_quaia','redshift_quaia_err','ra','dec','l','b','phot_g_mean_mag','phot_bp_mean_mag','phot_rp_mean_mag','mag_w1_vg','mag_w2_vg','pm','pmra','pmdec','pmra_error','pmdec_error')>\n"
     ]
    }
   ],
   "source": [
    "print(f\"Column names: {tab_gcatlo.columns}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "17c57a3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of data sources: 1295502\n"
     ]
    }
   ],
   "source": [
    "tab_gcathi = Table.read(fn_gcathi)\n",
    "N_gcathi = len(tab_gcathi)\n",
    "print(f\"Number of data sources: {N_gcathi}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3b7db17",
   "metadata": {},
   "source": [
    "### Make map of quasar number counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "45f64e98",
   "metadata": {},
   "outputs": [],
   "source": [
    "pixel_indices_gcatlo = hp.ang2pix(NSIDE, tab_gcatlo['ra'], tab_gcatlo['dec'], lonlat=True)\n",
    "map_gcatlo = np.bincount(pixel_indices_gcatlo, minlength=NPIX)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "69af4397",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.QuadMesh at 0x153cf65776d0>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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

[... middle omitted — see footer ...]

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",
      "text/plain": [
       "<Figure size 850x535.5 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "projview(map_residuals_hi, title=rf\"Residuals between data and random, $G<{G_hi}$\",\n",
    "            unit=r\"$\\bar{n}_\\mathrm{rand} - \\bar{n}_\\mathrm{data}$ per healpixel (deg$^{-2}$) [normalized]\", \n",
    "            cmap='coolwarm_r', coord=['C', 'G'], \n",
    "            min=-0.5, max=0.5, graticule=True,\n",
    "            cbar_ticks=[-0.5, -0.25, 0, 0.25, 0.5]) "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:gaiaenv]",
   "language": "python",
   "name": "conda-env-gaiaenv-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}


──────── [TRUNCATED] ────────
Showing 37,500 chars (head) + 12,500 chars (tail) of 4,776,252 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/raw.githubusercontent.com-8c9f5c8e18.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/raw.githubusercontent.com-8c9f5c8e18.md" offset=284 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────