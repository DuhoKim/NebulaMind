import csv, io, json, numpy as np
np.random.seed(20260720)

LANE='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/overnight-z7-mzr-20260720/'

# ---------- KE08 T04 -> PP04_O3N2 cubic (Kewley&Ellison 2008 Table 3; target y=PP04_O3N2, source x=T04) ----------
# valid x-range 8.05-9.2 ; conversion rms rho_r = 0.046 dex
KE08 = dict(a=230.7820, b=-75.79752, c=8.526986, d=-0.3162894, xmin=8.05, xmax=9.2, rms=0.046)
def t04_to_pp04o3n2(x):
    x=np.asarray(x,float)
    return KE08['a'] + KE08['b']*x + KE08['c']*x**2 + KE08['d']*x**3

# ---------- 1. Build z7 metallicity CSV from Nakajima+23 tabled1 ----------
rows=list(csv.DictReader(io.StringIO(open(LANE+'_nakajima_tabled1_raw.csv').read())))
def f(x):
    try: return float(x)
    except: return None
def err(E,e):
    E=f(E); e=f(e)
    vals=[v for v in (E,e) if v is not None]
    return round(np.mean(vals),3) if vals else None

def build(zmin):
    out=[]
    for x in rows:
        z=f(x['zspec']); M=f(x['logMs']); OH=f(x['logOH'])
        if z is None or z<=zmin or M is None or OH is None: continue
        out.append(dict(ref='Nakajima2023', id=x['ID'].strip(), z=z,
            logM=M, logM_err=err(x['E_logMs'],x['e_logMs']),
            OH=OH, OH_err=err(x['E_logOH'],x['e_logOH']),
            calib=x['MFl'].strip() or 'strongline',
            mass_limit=x['l_logMs'].strip()))
    return out

z7=build(7.0); z4=build(4.0)
def write_csv(path,data):
    with open(path,'w',newline='') as fh:
        w=csv.DictWriter(fh, fieldnames=['ref','id','z','logM','logM_err','OH','OH_err','calib','mass_limit'])
        w.writeheader()
        for d in data: w.writerow(d)
write_csv(LANE+'z7_metallicity.csv', z7)
write_csv(LANE+'z4_metallicity_superset.csv', z4)
print('N z>7 =',len(z7),' N z>4 =',len(z4))

# ---------- 2. SDSS matched-scale MZR (T04 -> PP04_O3N2 via KE08 cubic) ----------
anc=json.load(open(LANE+'sdss_anchor.json'))
centers=np.array(anc['mass_bin_centers'])
t04med=np.array(anc['T04']['median_OH'])
binN=np.array(anc['bin_N'])
pp04med = t04_to_pp04o3n2(t04med)   # metallicity-dependent KE08 conversion per bin
sdss_scatter = anc['median_bin_scatter_dex']   # 0.149 dex intrinsic

# Fit SDSS PP04_O3N2 median vs logM over overlap-ish range [7.9, 9.7] with a quadratic
OLO, OHI = 8.0, 9.5
fitmask = (centers>=7.9)&(centers<=9.75)
coef = np.polyfit(centers[fitmask], pp04med[fitmask], 2)
def sdss_pp04(logM): return np.polyval(coef, logM)
def sdss_t04(logM):
    c2=np.polyfit(centers[fitmask], t04med[fitmask],2); return np.polyval(c2,logM)

# grid points
grid=np.array([8.0,8.5,9.0,9.5])
print('SDSS T04  @grid:', np.round(sdss_t04(grid),3))
print('SDSS PP04 @grid:', np.round(sdss_pp04(grid),3))
print('KE08 shift @grid:', np.round(sdss_pp04(grid)-sdss_t04(grid),3))

# ---------- 3. Mass-overlap z>7 sample ----------
def in_overlap(d): return OLO<=d['logM']<=OHI
ov_all=[d for d in z7 if in_overlap(d)]
ov=[d for d in ov_all if d['mass_limit']!='<']      # primary: exclude mass upper-limits
print('z>7 in overlap [%.1f,%.1f]: all=%d, non-limit=%d'%(OLO,OHI,len(ov_all),len(ov)))

# ---------- 4. Per-object matched-scale offset Delta_i = SDSS_PP04(M_i) - OH_highz_i ----------
def offsets(sample):
    M=np.array([d['logM'] for d in sample]); OH=np.array([d['OH'] for d in sample])
    return sdss_pp04(M) - OH
d_ov = offsets(ov)
mean_delta = d_ov.mean()
# also naive (unmatched, T04) and relation-level
d_ov_t04 = sdss_t04(np.array([d['logM'] for d in ov])) - np.array([d['OH'] for d in ov])

# Bootstrap over galaxies (>=1e4) + add per-object OH measurement noise each draw
NB=20000
Mov=np.array([d['logM'] for d in ov]); OHov=np.array([d['OH'] for d in ov])
OHe=np.array([d['OH_err'] or 0.2 for d in ov]); Me=np.array([d['logM_err'] or 0.2 for d in ov])
boot=np.empty(NB)
n=len(ov)
for i in range(NB):
    idx=np.random.randint(0,n,n)
    mm=Mov[idx]+np.random.normal(0,Me[idx])
    oo=OHov[idx]+np.random.normal(0,OHe[idx])
    boot[i]=(sdss_pp04(mm)-oo).mean()
ci=np.percentile(boot,[2.5,97.5])
# leave-one-out
loo=np.array([np.delete(d_ov,k).mean() for k in range(n)])
# bootstrap excluding most extreme object
kext=np.argmax(np.abs(d_ov-mean_delta))
ov_ex=[d for j,d in enumerate(ov) if j!=kext]
d_ex=offsets(ov_ex); 
bo2=np.empty(NB); m2=np.array([d['logM'] for d in ov_ex]); o2=np.array([d['OH'] for d in ov_ex])
for i in range(NB):
    idx=np.random.randint(0,len(ov_ex),len(ov_ex)); bo2[i]=(sdss_pp04(m2[idx])-o2[idx]).mean()
ci_ex=np.percentile(bo2,[2.5,97.5])

sigma_cal_resid=0.10
print('\n=== OFFSET RESULTS (matched PP04_O3N2 scale) ===')
print('mean Delta (matched) =%.3f dex'%mean_delta)
print('bootstrap 95%% CI = [%.3f, %.3f]'%(ci[0],ci[1]))
print('mean Delta (naive T04, unmatched) =%.3f dex'%d_ov_t04.mean())
print('LOO range = [%.3f, %.3f]'%(loo.min(),loo.max()))
print('excl most-extreme obj (%s): Delta=%.3f CI=[%.3f,%.3f]'%(ov[kext]['id'],d_ex.mean(),ci_ex[0],ci_ex[1]))
print('sigma_cal_resid=%.2f ; |Delta|-sigma = %.3f'%(sigma_cal_resid, abs(mean_delta)-sigma_cal_resid))

# per grid-mass offset (fixed mass): SDSS_PP04(grid) - (z7 local mean OH in +-0.35 dex bin)
print('\nPer-grid fixed-mass offset:')
grid_off={}
for g in grid:
    sel=[d for d in ov if abs(d['logM']-g)<=0.35]
    if sel:
        oh=np.mean([d['OH'] for d in sel]); dd=sdss_pp04(g)-oh
        grid_off[float(g)]=dict(n=len(sel), highz_OH=round(oh,3), sdss_pp04=round(float(sdss_pp04(g)),3), delta=round(float(dd),3))
        print('  logM=%.1f N=%d highzOH=%.2f sdssPP04=%.2f Delta=%.2f'%(g,len(sel),oh,sdss_pp04(g),dd))

# z>7 relation fit (for figure + slope)
Mall=np.array([d['logM'] for d in ov_all]); OHall=np.array([d['OH'] for d in ov_all])
zslope,zint=np.polyfit(Mall,OHall,1)
print('\nz>7 linear MZR fit (overlap): OH = %.3f + %.3f*logM'%(zint,zslope))

# Curti+24 published relation on grid (7.72 + 0.17*log(M/1e8))
def curti(logM): return 7.72+0.17*(logM-8.0)
print('Curti+24 @grid:', np.round(curti(grid),3))

results=dict(
  data_source='VizieR TAP J/ApJS/269/33 (Nakajima+2023) tabled1; Curti+2024 J/A+A/684/A75 NOT in VizieR',
  N_z7_total=len([d for d in z7]), N_z7_with_M_and_OH=len(z7),
  N_z7_overlap_nonlimit=len(ov), overlap_window=[OLO,OHI],
  KE08_conversion=KE08,
  calib_breakdown={k:sum(1 for d in ov if d['calib']==k) for k in set(d['calib'] for d in ov)},
  mean_delta_matched_dex=round(float(mean_delta),3),
  bootstrap95_CI=[round(float(ci[0]),3),round(float(ci[1]),3)],
  mean_delta_naive_T04_dex=round(float(d_ov_t04.mean()),3),
  LOO_range=[round(float(loo.min()),3),round(float(loo.max()),3)],
  excl_extreme=dict(id=ov[kext]['id'],delta=round(float(d_ex.mean()),3),CI=[round(float(ci_ex[0]),3),round(float(ci_ex[1]),3)]),
  sigma_cal_resid=sigma_cal_resid,
  per_grid_offset=grid_off,
  z7_fit=dict(intercept=round(float(zint),3),slope=round(float(zslope),3)),
  sdss_pp04_grid={float(g):round(float(sdss_pp04(g)),3) for g in grid},
  sdss_t04_grid={float(g):round(float(sdss_t04(g)),3) for g in grid},
  curti24_grid={float(g):round(float(curti(g)),3) for g in grid},
)
json.dump(results, open(LANE+'_p2_intermediate.json','w'), indent=1)
# stash arrays for figure
np.savez(LANE+'_p2_arrays.npz', centers=centers, t04med=t04med, pp04med=pp04med,
         binN=binN, coef=coef, Mall=Mall, OHall=OHall,
         zint=zint, zslope=zslope, mean_delta=mean_delta, ci=ci, boot=boot)
print('\nsaved intermediate + arrays')
