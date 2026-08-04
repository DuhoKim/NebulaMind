import numpy as np, pandas as pd, json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

LANE='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/overnight-z7-mzr-20260720/'
SRC='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/research-frontiers-20260716/sdss_mzr.csv'

df=pd.read_csv(SRC, comment='#')
n_raw=len(df)
# MPA-JHU cleaning: star-forming (bptclass==1), valid mass & O/H, sane ranges
m = (df.bptclass==1) & df.lgm_tot_p50.between(7,12.5) & df.oh_p50.between(7.0,9.6) & (df.lgm_tot_p50>-99) & (df.oh_p50>-99)
d=df[m].copy()
n_sf=len(d)

# T04 (native MPA-JHU/Tremonti) -> PP04-O3N2 documented bulk offset (brief/memory: T04 ~+0.24 dex high)
OFFSET=-0.24
d['oh_pp04']=d.oh_p50+OFFSET

# Mass bins
edges=np.arange(8.0,11.4,0.15)
cen=0.5*(edges[:-1]+edges[1:])
def binstats(oh):
    med=[]; lo=[]; hi=[]; sc=[]; nn=[]
    for a,b in zip(edges[:-1],edges[1:]):
        s=oh[(d.lgm_tot_p50>=a)&(d.lgm_tot_p50<b)]
        if len(s)>=20:
            med.append(np.median(s)); sc.append(np.std(s)); nn.append(len(s))
            lo.append(np.percentile(s,16)); hi.append(np.percentile(s,84))
        else:
            med.append(np.nan); sc.append(np.nan); nn.append(len(s)); lo.append(np.nan); hi.append(np.nan)
    return np.array(med),np.array(sc),np.array(nn),np.array(lo),np.array(hi)

med_t04,sc_t04,nn,lo_t04,hi_t04=binstats(d.oh_p50)
med_pp,sc_pp,_,lo_pp,hi_pp=binstats(d.oh_pp04)

# Asymptotic MZR fit (Zahid+14 / Moustakas form):
#   12+log(O/H) = Z0 - log10(1 + (M0/M*)^gamma)  with M in linear, using logM
def mzr(logm,Z0,logM0,gamma):
    return Z0 - np.log10(1.0 + 10**(gamma*(logM0-logm)))
from scipy.optimize import curve_fit
def fit(med):
    ok=np.isfinite(med)
    p,_=curve_fit(mzr,cen[ok],med[ok],p0=[9.1,10.0,0.5],maxfev=20000)
    resid=med[ok]-mzr(cen[ok],*p)
    return dict(Z0=float(p[0]),logM0=float(p[1]),gamma=float(p[2]),
                rms=float(np.sqrt(np.mean(resid**2))),
                oh_logM9=float(mzr(9.0,*p)), oh_logM8=float(mzr(8.0,*p)),
                oh_logM10_5=float(mzr(10.5,*p)))
fit_t04=fit(med_t04); fit_pp=fit(med_pp)

# global scatter about fit (T04)
ok=np.isfinite(med_t04)
scatter_global=float(np.nanmedian(sc_t04[ok]))

out=dict(
 source=SRC, calibration_native='Tremonti04 (MPA-JHU oh_p50)',
 n_raw=int(n_raw), n_starforming_clean=int(n_sf),
 selection='bptclass==1 & 7<lgm<12.5 & 7.0<oh<9.6',
 mass_bin_edges=edges.tolist(), mass_bin_centers=cen.tolist(),
 bin_N=nn.tolist(),
 T04={'median_OH':np.where(np.isfinite(med_t04),med_t04,None).tolist(),
      'p16':np.where(np.isfinite(lo_t04),lo_t04,None).tolist(),
      'p84':np.where(np.isfinite(hi_t04),hi_t04,None).tolist(),
      'fit':fit_t04},
 PP04_O3N2_shifted={'applied_offset_dex':OFFSET,
      'offset_reference':'Kewley&Ellison2008 (2008ApJ...681.1183K) family offset; bulk ~0.24 dex per lane memo; refine with KE08 metallicity-dependent polynomial in P2',
      'median_OH':np.where(np.isfinite(med_pp),med_pp,None).tolist(),
      'fit':fit_pp},
 median_bin_scatter_dex=scatter_global,
 note='Constant-offset reconciliation is FIRST-ORDER only; KE08 T04->PP04-O3N2 conversion is metallicity-dependent (cubic). P2 must apply the exact polynomial. SDSS has no line fluxes on disk, so direct O3N2 recompute is NOT possible.'
)
json.dump(out,open(LANE+'sdss_anchor.json','w'),indent=1)

# Figure
plt.figure(figsize=(7,5))
plt.hexbin(d.lgm_tot_p50,d.oh_p50,gridsize=60,cmap='Greys',bins='log',mincnt=1)
plt.plot(cen,med_t04,'o-',color='C3',label='SDSS median (T04, native)')
plt.plot(cen,med_pp,'s--',color='C0',label='SDSS shifted to PP04-O3N2 (-0.24 dex)')
xx=np.linspace(8,11.2,100)
plt.plot(xx,mzr(xx,*[fit_t04['Z0'],fit_t04['logM0'],fit_t04['gamma']]),'-',color='k',lw=1,label='T04 asymptotic fit')
# Overlay published high-z relations (literature, NOT our data)
mm=np.linspace(8.0,9.5,50)
curti24=7.72+0.17*(mm-8.0)   # Curti+24 JADES 3<z<10, PP04-consistent Te scale
plt.plot(mm,curti24,':',color='C2',lw=2,label='Curti+24 3<z<10 (lit)')
plt.scatter([9.0],[7.97],marker='*',s=200,color='C1',zorder=5,label='Nakajima+23 z~4-10 (lit, logM=9)')
plt.xlabel('log M*/Msun'); plt.ylabel('12+log(O/H)')
plt.title('SDSS anchor MZR (T04 vs PP04) + published high-z relations')
plt.legend(fontsize=8); plt.tight_layout()
plt.savefig(LANE+'sdss_anchor.png',dpi=110)
print('N_raw',n_raw,'N_sf_clean',n_sf)
print('T04 fit',fit_t04)
print('PP04 fit',fit_pp)
print('median bin scatter',scatter_global)
