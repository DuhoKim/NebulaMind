import csv, io, json, numpy as np
np.random.seed(7)
LANE='/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/overnight-z7-mzr-20260720/'
z7=list(csv.DictReader(io.StringIO(open(LANE+'z7_metallicity.csv').read())))
anc=json.load(open(LANE+'sdss_anchor.json'))
KE08=dict(a=230.7820,b=-75.79752,c=8.526986,d=-0.3162894)
def conv(x): x=np.asarray(x,float); return KE08['a']+KE08['b']*x+KE08['c']*x**2+KE08['d']*x**3
centers=np.array(anc['mass_bin_centers']); t04=np.array(anc['T04']['median_OH'])
m=(centers>=7.9)&(centers<=9.75)
coef=np.polyfit(centers[m],conv(t04)[m],2)
def sdss(logM): return np.polyval(coef,logM)
OLO,OHI=8.0,9.5
def flt(x):
    try:return float(x)
    except:return None
ov=[d for d in z7 if OLO<=float(d['logM'])<=OHI and d['mass_limit']!='<']
def delta(sample):
    M=np.array([float(d['logM']) for d in sample]); OH=np.array([float(d['OH']) for d in sample])
    return sdss(M)-OH
def boot_ci(sample,NB=20000):
    M=np.array([float(d['logM']) for d in sample]); OH=np.array([float(d['OH']) for d in sample])
    n=len(sample); b=np.empty(NB)
    for i in range(NB):
        idx=np.random.randint(0,n,n); b[i]=(sdss(M[idx])-OH[idx]).mean()
    return np.percentile(b,[2.5,97.5])

# TEST 3: bracketing Te-direct vs strong-line
te=[d for d in ov if d['calib']=='direct']
sl=[d for d in ov if d['calib']!='direct']
dte=delta(te); dsl=delta(sl)
cite=boot_ci(te) if len(te)>2 else (np.nan,np.nan)
cisl=boot_ci(sl)
print('TEST3 bracketing:')
print('  Te-direct  N=%d  Delta=%.3f  CI=[%.3f,%.3f]'%(len(te),dte.mean(),cite[0],cite[1]))
print('  strongline N=%d  Delta=%.3f  CI=[%.3f,%.3f]'%(len(sl),dsl.mean(),cisl[0],cisl[1]))
print('  same sign & both CI exclude 0:', (dte.mean()>0 and dsl.mean()>0 and cite[0]>0 and cisl[0]>0))

# TEST 5 detail already have; report N, CI, LOO
dall=delta(ov); ciall=boot_ci(ov)
loo=np.array([np.delete(dall,k).mean() for k in range(len(ov))])
print('\nTEST5 small-N: N=%d Delta=%.3f CI=[%.3f,%.3f] LOO=[%.3f,%.3f]'%(len(ov),dall.mean(),ciall[0],ciall[1],loo.min(),loo.max()))

# TEST 2 mass-control: per-grid stated already; confirm offset>0 across window
print('\nTEST2 mass-control per 0.5dex bin:')
for g in [8.0,8.5,9.0,9.5]:
    sel=[d for d in ov if abs(float(d['logM'])-g)<=0.25]
    if sel:
        dd=delta(sel).mean(); print('  logM~%.1f N=%d Delta=%.3f'%(g,len(sel),dd))

out=dict(
  test3=dict(te_n=len(te),te_delta=round(float(dte.mean()),3),te_ci=[round(float(cite[0]),3),round(float(cite[1]),3)],
             sl_n=len(sl),sl_delta=round(float(dsl.mean()),3),sl_ci=[round(float(cisl[0]),3),round(float(cisl[1]),3)]),
  test5=dict(n=len(ov),delta=round(float(dall.mean()),3),ci=[round(float(ciall[0]),3),round(float(ciall[1]),3)],
             loo=[round(float(loo.min()),3),round(float(loo.max()),3)]),
)
json.dump(out,open(LANE+'_p2_tests.json','w'),indent=1)
