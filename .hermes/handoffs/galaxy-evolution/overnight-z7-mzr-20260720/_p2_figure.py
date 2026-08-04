import csv,io,json,numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
LANE='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/overnight-z7-mzr-20260720/'
A=np.load(LANE+'_p2_arrays.npz')
z7=list(csv.DictReader(io.StringIO(open(LANE+'z7_metallicity.csv').read())))
tng=json.load(open('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/research-frontiers-20260716/topic3/tng_results.json'))
centers=A['centers']; t04=A['t04med']; pp04=A['pp04med']; coef=A['coef']
zint=float(A['zint']); zslope=float(A['zslope']); md=float(A['mean_delta'])

fig,ax=plt.subplots(figsize=(8.4,6.4))
mg=np.linspace(7.8,9.7,100)
# SDSS T04 native
sm=(centers>=7.9)&(centers<=9.75)
ax.plot(centers[sm],t04[sm],'-',color='#B0B0B0',lw=2.2,label='SDSS anchor (T04, native)')
# SDSS matched PP04_O3N2 (KE08 cubic)
ax.plot(mg,np.polyval(coef,mg),'-',color='#1f77b4',lw=2.8,label='SDSS anchor -> PP04-O3N2 (KE08 cubic)')
# calibration systematic band (+-0.10 residual)
ax.fill_between(mg,np.polyval(coef,mg)-0.10,np.polyval(coef,mg)+0.10,color='#1f77b4',alpha=0.15,
                label=r'matched-scale residual $\sigma_{cal}=0.10$ dex')
# z>7 points, colour by calib
cmap={'direct':'#d62728','R23':'#ff7f0e','R3':'#e377c2'}
for cal,lab in [('direct','z>7 Te-direct (Nakajima+23)'),('R23','z>7 R23 strong-line'),('R3','z>7 R3 strong-line')]:
    pts=[d for d in z7 if d['calib']==cal and 8.0<=float(d['logM'])<=9.5 and d['mass_limit']!='<']
    if pts:
        M=[float(d['logM']) for d in pts]; OH=[float(d['OH']) for d in pts]
        Me=[float(d['logM_err']) for d in pts]; OHe=[float(d['OH_err']) for d in pts]
        ax.errorbar(M,OH,xerr=Me,yerr=OHe,fmt='o',color=cmap[cal],ms=6,capsize=2,lw=0.8,
                    ecolor=cmap[cal],alpha=0.85,label=lab)
# mass upper-limit objects
lim=[d for d in z7 if d['mass_limit']=='<' and 8.0<=float(d['logM'])<=9.5]
if lim:
    ax.scatter([float(d['logM']) for d in lim],[float(d['OH']) for d in lim],marker='<',
               facecolors='none',edgecolors='#7f7f7f',s=55,label='z>7 mass upper-limit (excl.)')
# z>7 linear fit
ax.plot(mg,zint+zslope*mg,'--',color='#d62728',lw=2.2,label='z>7 MZR fit (this work)')
# Curti+24 published relation
ax.plot(mg,7.72+0.17*(mg-8.0),':',color='#9467bd',lw=2.2,label='Curti+24 relation (3<z<10)')
# TNG z=6 intrinsic trend
g=np.array(tng['z6.0']['mzr_median_grid']); 
ax.plot(g[:,0],g[:,1],'-.',color='#2ca02c',lw=2.0,label='IllustrisTNG z=6 (intrinsic scale, trend only)')
# offset arrow at logM9
x0=9.0; y_sdss=np.polyval(coef,x0); y_hz=zint+zslope*x0
ax.annotate('',xy=(x0,y_hz),xytext=(x0,y_sdss),arrowprops=dict(arrowstyle='<->',color='k',lw=1.6))
ax.text(x0+0.04,(y_sdss+y_hz)/2,r'$\Delta$=%.2f dex'%md,fontsize=11,va='center')

ax.axvspan(8.0,9.5,color='gold',alpha=0.06)
ax.text(8.75,7.15,'mass-overlap window',ha='center',fontsize=9,color='#8a6d00')
ax.set_xlabel(r'$\log_{10}(M_\star/M_\odot)$',fontsize=13)
ax.set_ylabel(r'$12+\log_{10}(\mathrm{O/H})$',fontsize=13)
ax.set_title('z>7 mass–metallicity offset on a matched (PP04-O3N2) scale\nNakajima+23 (N=16 overlap) vs KE08-reconciled SDSS anchor',fontsize=12)
ax.set_xlim(7.8,9.7); ax.set_ylim(7.1,8.9)
ax.legend(fontsize=8.2,loc='lower right',framealpha=0.92,ncol=1)
ax.grid(alpha=0.25)
plt.tight_layout()
plt.savefig(LANE+'fig_z7mzr.png',dpi=140)
print('figure saved')
