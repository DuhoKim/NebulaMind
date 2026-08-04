import numpy as np, json
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import selection_forward_model as m

RNG = np.random.default_rng(7)
# one big fiducial realisation, re-derived here so we can keep the arrays for plotting
n=250000
logM = m.draw_masses(n, -1.9)
z = RNG.choice(m.Z_SAMPLE, n)
eps = RNG.normal(0,0.35,n)
SFR = 10**(m.z8_main_sequence(logM)+eps)
OH  = m.intrinsic_MZR(logM,'local_like') - 0.20*eps + RNG.normal(0,np.sqrt(0.12**2-(0.2*0.35)**2),n)
LHb = m.LHb_of_SFR(SFR); L5007=LHb*m.R3_ratio(OH); L4363=L5007*m.r4363_5007(m.Te_of_OH(OH))
A = 4*np.pi*m.dL_cm(z)**2
sl=1.5e-19; snr=5.0
def det(L): return (L/A + RNG.normal(0,sl,n)) > snr*sl
dS = det(LHb)&det(L5007); dT = dS & det(L4363)

res = json.load(open("selection_results.json"))
mg = np.linspace(7.6,9.7,50)

fig,(ax,ax2)=plt.subplots(1,2,figsize=(12,5.2))
# --- left: MZR ---
sub=RNG.choice(np.where(logM<9.7)[0], 6000, replace=False)
ax.scatter(logM[sub],OH[sub],s=3,c='0.8',alpha=0.5,label='parent population (intrinsic)',rasterized=True)
ax.plot(mg,m.intrinsic_MZR(mg,'local_like'),'k-',lw=2.2,label='intrinsic MZR (input)')
# binned recovered means
edges=np.arange(8.0,9.51,0.5); ctr=0.5*(edges[:-1]+edges[1:])
def binmean(mask):
    return [OH[(logM>=lo)&(logM<hi)&mask].mean() if ((logM>=lo)&(logM<hi)&mask).sum()>3 else np.nan
            for lo,hi in zip(edges[:-1],edges[1:])]
ax.plot(ctr,binmean(dS),'s-',color='#1f77b4',ms=9,lw=1.6,label='recovered: strong-line detected')
ax.plot(ctr,binmean(dT),'D-',color='#d62728',ms=9,lw=1.6,label='recovered: Te/auroral detected')
ax.plot(ctr,binmean(np.ones(n,bool)),'o:',color='0.4',ms=6,label='parent binned mean')
ax.axvspan(8.0,9.5,color='gold',alpha=0.08)
ax.set_xlim(7.6,9.7); ax.set_ylim(7.2,8.8)
ax.set_xlabel(r'$\log(M_\star/M_\odot)$'); ax.set_ylabel(r'$12+\log({\rm O/H})$')
ax.set_title('Intrinsic vs selection-recovered MZR (z$\\sim$8 mock)')
ax.legend(fontsize=8,loc='lower right'); ax.grid(alpha=0.25)

# --- right: Delta_sel(mass) + brackets ---
pS=res['fiducial_result']['prof_strong']; pT=res['fiducial_result']['prof_te']
bc=res['fiducial_result']['bin_centers']
ax2.plot(bc,pS,'s-',color='#1f77b4',ms=9,label='strong-line $\\Delta_{\\rm sel}$')
ax2.plot(bc,pT,'D-',color='#d62728',ms=9,label='Te/auroral $\\Delta_{\\rm sel}$')
sB=res['Delta_sel_strongline_dex']; tB=res['Delta_sel_Te_dex']
ax2.axhspan(sB['min'],sB['max'],color='#1f77b4',alpha=0.15,label=f"strong-line bracket {sB['min']:.2f}-{sB['max']:.2f}")
ax2.axhspan(tB['min'],tB['max'],color='#d62728',alpha=0.12,label=f"Te bracket {tB['min']:.2f}-{tB['max']:.2f}")
ax2.axhline(0,color='k',lw=0.8)
ax2.set_xlabel(r'$\log(M_\star/M_\odot)$'); ax2.set_ylabel(r'$\Delta_{\rm sel}$ = intrinsic $-$ recovered [dex]')
ax2.set_title('Selection bias $\\Delta_{\\rm sel}$ (auroral subset is the biased one)')
ax2.legend(fontsize=8,loc='upper left'); ax2.grid(alpha=0.25)
ax2.set_ylim(-0.02,0.42)
fig.suptitle('Phase-6 JWST emission-line selection forward model  |  Test 4: PASS (matched); Te-only selection-dominated',
             fontsize=11,y=1.00)
fig.tight_layout()
fig.savefig("fig_selection.png",dpi=130,bbox_inches='tight')
print("fig_selection.png written")
