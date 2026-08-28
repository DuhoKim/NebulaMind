#!/usr/bin/env python
from astropy.table import Table
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
rc('font', family='serif')
rc('text', usetex='true')

t = Table.read('steradian_smoothed.fits')

msk = np.isfinite(t['denscorr'])
t['denscorr'][~msk] = hp.pixelfunc.UNSEEN
t['smoothed'][~msk] = hp.pixelfunc.UNSEEN

fig, (ax1, ax2) = plt.subplots(ncols=2)
fig.set_figheight(4)
fig.set_figwidth(11)

plt.axes(ax1)
hp.visufunc.mollview(t['denscorr'], coord=['C', 'G'], hold=True,
                     unit=r'source deg$^{-2}$',
                     title=None, cmap='Blues', badcolor='white',
                     notext=True, format='%i',
                     margins=(0,0,1,1),
                     min=30, max=90)
hp.graticule()


plt.axes(ax2)
hp.visufunc.mollview(t['smoothed'], coord=['C', 'G'], hold=True,
                     unit=r'source deg$^{-2}$',
                     title=None, cmap='RdBu_r', badcolor='white',
                     notext=True, format='%.1f',
                     margins=(0,0,1,1))

f = plt.gcf().get_children()

unit_text_obj = f[2].get_children()[1]

unit_text_obj.set_fontsize(12)
unit_text_obj.set_verticalalignment('top')

unit_text_obj = f[4].get_children()[1]

unit_text_obj.set_fontsize(12)
unit_text_obj.set_verticalalignment('top')

plt.savefig('moll.pdf', dpi=600, format='pdf', bbox_inches='tight')
plt.close()


# Make distributions of flux densities and spectral indices
rcParams.update({'font.size': 16})
t = Table.read('catwise_agns_masked_final_alpha.fits')
SW1 = t['k'] * t['nu_W1_iso']**t['alpha_W1'] * 1e23 * 1000  # mJy

fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True)
x0, x1 = np.log10(SW1.min()), np.log10(SW1.max())
bins = np.logspace(x0, x1, 100)
ax1.hist(SW1, bins=bins, density=True, histtype='stepfilled')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.tick_params(axis='both', which='both', direction='in', top=True, right=True)
ax1.set_ylim(bottom=1e-6, top=3e1)
ax1.set_ylabel(r'PDF')
ax1.set_xticks([1e-1, 1e0, 1e1, 1e2])
ax1.set_xlabel(r'$S_\mathrm{W1}$ [mJy]')
ax1.grid(linewidth=0.5)

ax2.hist(-t['alpha_W1'], 100, density=True, histtype='stepfilled')
ax2.set_yscale('log')
ax2.tick_params(axis='both', which='both', direction='in', top=True, right=True)
ax2.set_xticks([1,3,5,7])
ax2.set_xlim(left=0, right=8)
ax2.set_xlabel(r'$\alpha_\mathrm{W1}$')
ax2.grid(linewidth=0.5)

plt.savefig('distros.pdf', dpi=600, format='pdf', bbox_inches='tight')


# Finally, get the redshift distribution
t = Table.read('specObj-dr16_s82_zwarning0.fits')
fig, ax1 = plt.subplots(ncols=1, sharey=True)
ax1.hist(t['Z'], bins=200, density=True, histtype='stepfilled')
ax1.set_xticks(np.arange(0, 4, 0.5))
ax1.set_xlim(left=0, right=3.7)
ax1.tick_params(axis='both', which='both', direction='in', top=True, right=True)
ax1.set_ylabel(r'PDF')
ax1.set_xlabel(r'redshift')
ax1.grid(linewidth=0.5)

plt.savefig('redshifts.pdf', dpi=600, format='pdf', bbox_inches='tight')
