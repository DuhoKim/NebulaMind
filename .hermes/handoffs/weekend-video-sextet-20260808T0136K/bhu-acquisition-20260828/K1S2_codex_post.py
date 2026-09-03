#!/usr/bin/env python3
"""K1S2 post-processing; safe to run while the detached grid is incomplete.

IMF alternatives are importance reweights, not reruns. COMPAS samples the
Kroupa alpha_3=2.3 primary, so for primary Mass@ZAMS(1)=m the system weight is
m**(-(alpha_3-2.3)) for m>=1 Msun and one below. The secondary is conditional
on the sampled primary (the COMPAS mass-ratio draw), not an independent IMF
draw; assigning it another IMF weight would double-count the change of measure.

Star-forming-mass normalization calls the repository implementation
compas_python_utils/cosmic_integration/totalMassEvolvedPerZ.py::
totalMassEvolvedPerZ, including the unsampled Kroupa range. C1 follows the
Madau & Dickinson (2014) functional form exposed in
compas_python_utils/cosmic_integration/FastCosmicIntegration.py::find_sfr.
"""
from __future__ import annotations
import argparse, json, math, re, sys
from pathlib import Path
import h5py
import numpy as np

LANE = Path(__file__).resolve().parent
ROOT = LANE / "_tmp_k1s2_codex"
RUNS = ROOT / "runs"
CI = ROOT / "COMPAS" / "compas_python_utils" / "cosmic_integration"
sys.path.insert(0, str(CI))
import totalMassEvolvedPerZ as MPZ

CAPS=(1.97,2.50,3.50); ALPHAS=(1.6,2.3,3.0)
MASTER=(104729,130363,155921); EXTRA=(181081,196613,216091)
OBS=np.array([1.559,1.174,1.3381,1.2489,1.3330,1.3455,1.341,1.230,
              1.291,1.322,1.4398,1.3886,1.358,1.354,1.27])
NAME=re.compile(r"(?P<kind>bse|sse|c4)_cap(?P<cap>[0-9.]+)_eng(?P<eng>[A-Z]+)_z(?P<z>[0-9.]+)_ce(?P<ce>[a-z]+)_seed(?P<seed>[0-9]+)$")

def h5path(d):
    p=d/'COMPAS_Output'/'COMPAS_Output.h5'
    return p if p.is_file() else None

def ks2(x,y):
    """Two-sided asymptotic two-sample KS; returns D and conservative p."""
    x=np.sort(np.asarray(x)); y=np.sort(np.asarray(y))
    if not len(x) or not len(y): return math.nan, math.nan
    v=np.sort(np.r_[x,y]); d=float(np.max(np.abs(np.searchsorted(x,v,'right')/len(x)-np.searchsorted(y,v,'right')/len(y))))
    ne=len(x)*len(y)/(len(x)+len(y)); lam=(math.sqrt(ne)+.12+.11/math.sqrt(ne))*d
    p=max(0.,min(1.,2*sum((-1)**(k-1)*math.exp(-2*k*k*lam*lam) for k in range(1,101))))
    return d,p

def mass_norm(path, alpha):
    # COMPAS defaults recorded in Run_Details: primary [5,150], secondary >=0.1,
    # binary fraction 1. The same alpha is passed into the repository correction.
    _, total=MPZ.totalMassEvolvedPerZ(str(path),5.,150.,0.1,1.0,a34=alpha)
    return float(np.sum(total))

def sse_mass_norm(m1, alpha):
    # SSE analogue of the repository's IMF-range correction: simulated mass
    # divided by the fraction of universal stellar mass in the sampled range.
    sampled=MPZ.quad(lambda m:m*MPZ.IMF(m,a34=alpha),5.,150.)[0]
    full=MPZ.quad(lambda m:m*MPZ.IMF(m,a34=alpha),.01,200.)[0]
    return float(np.sum(m1)*full/sampled)

def one_run(meta,path,alpha):
    with h5py.File(path,'r') as f:
        group='SSE_System_Parameters' if meta['kind']=='sse' else 'BSE_System_Parameters'
        if group not in f: return None
        g=f[group]; sse=meta['kind']=='sse'
        m1=np.asarray(g['Mass@ZAMS'] if sse else g['Mass@ZAMS(1)'])
        w=np.where(m1>=1.,m1**(-(alpha-2.3)),1.)
        t1=np.asarray(g['Stellar_Type'] if sse else g['Stellar_Type(1)'])
        t2=np.asarray(g['Stellar_Type(2)']) if not sse else np.zeros_like(t1)
        # Y_BH counts systems (not individual BHs) with either final component=14.
        num=float(np.sum(w*((t1==14)|(t2==14))))
    return num/(sse_mass_norm(m1,alpha) if sse else mass_norm(path,alpha))

def discover():
    out=[]
    if not RUNS.exists(): return out
    for d in RUNS.iterdir():
        m=NAME.match(d.name); p=h5path(d)
        if not m or not p: continue
        q=m.groupdict(); q.update(cap=float(q['cap']),z=float(q['z']),seed=int(q['seed']),path=p)
        out.append(q)
    return out

def aggregate(rows, kinds=('bse',), seeds=MASTER):
    a={}
    for r in rows:
        if r['kind'] not in kinds or r['seed'] not in seeds: continue
        for alpha in ALPHAS:
            try: y=one_run(r,r['path'],alpha)
            except (OSError,KeyError,ValueError) as e:
                print(f"partial/unreadable {r['path']}: {e}",file=sys.stderr); continue
            if y is not None: a.setdefault((r['eng'],r['z'],r['ce'],alpha,r['cap']),[]).append(y)
    return a

def derivatives(a):
    ans=[]
    boxes=sorted(set(k[:-1] for k in a))
    for box in boxes:
        vals=[a.get(box+(c,),[]) for c in CAPS]
        if not all(vals): continue
        means=[float(np.mean(v)) for v in vals]
        # central secant around the registered centre cap, unequal spacing.
        per=[]
        for lo,hi in zip(vals[0],vals[2]): per.append((hi-lo)/(CAPS[2]-CAPS[0]))
        err=float(np.std(per,ddof=1)/math.sqrt(len(per))) if len(per)>1 else math.nan
        curv=2*((means[2]-means[1])/(CAPS[2]-CAPS[1])-(means[1]-means[0])/(CAPS[1]-CAPS[0]))/(CAPS[2]-CAPS[0])
        ans.append(dict(engine=box[0],z=box[1],ce=box[2],alpha=box[3],nseed=min(map(len,vals)),yields=dict(zip(map(str,CAPS),means)),derivative=np.mean(per),mc_standard_error=err,curvature=curv))
    return ans

def c2(rows):
    masses=[]
    for r in rows:
        if not (r['kind']=='bse' and r['cap']==2.5 and r['eng']=='DELAYED' and r['z']==.02 and r['ce']=='default' and r['seed'] in MASTER): continue
        try:
            with h5py.File(r['path'],'r') as f:
                g=f['BSE_Double_Compact_Objects']
                # Near-birth cut: NS components only, explicitly Recycled_NS=False.
                for j in (1,2):
                    typ=np.asarray(g[f'Stellar_Type({j})']); rec=np.asarray(g[f'Recycled_NS({j})']).astype(bool)
                    masses.extend(np.asarray(g[f'Mass({j})'])[(typ==13)&~rec].tolist())
        except (OSError,KeyError): pass
    d,p=ks2(masses,OBS)
    return dict(n_synthetic=len(masses),n_observed=15,D=d,p=p,alpha=.05,pass_control=bool(p>=.05) if np.isfinite(p) else None,cut='DCO NS components with Recycled_NS(j)==False')

def c1(rows):
    # Discrete delay-time convolution at z=0.2. Flat 50/50 weight is the declared
    # quadrature over the two registered metallicity nodes; rate units follow
    # rho_SFR [Msun yr^-1 Gpc^-3] times events/Msun.
    H0=67.74; om=.3089; sec_gyr=3.15576e16; mpc_km=3.085677581e19
    H0g=H0/mpc_km*sec_gyr
    zg=np.linspace(0,20,20001); look=np.r_[0,np.cumsum(.5*np.diff(zg)*(1/((1+zg[:-1])*H0g*np.sqrt(om*(1+zg[:-1])**3+1-om))+1/((1+zg[1:])*H0g*np.sqrt(om*(1+zg[1:])**3+1-om))))]
    t0=np.interp(.2,zg,look); rate=0.; n=0
    for r in rows:
        if not (r['kind']=='bse' and r['cap']==2.5 and r['eng']=='DELAYED' and r['ce']=='default' and r['seed'] in MASTER): continue
        try:
            with h5py.File(r['path'],'r') as f:
                g=f['BSE_Double_Compact_Objects']; mask=(np.asarray(g['Stellar_Type(1)'])==14)&(np.asarray(g['Stellar_Type(2)'])==14)&np.asarray(g['Merges_Hubble_Time']).astype(bool)
                delays=(np.asarray(g['Time'])+np.asarray(g['Coalescence_Time']))[mask]/1000.
            norm=mass_norm(r['path'],2.3)
            zform=np.interp(t0+delays,look,zg,left=np.nan,right=np.nan); zform=zform[np.isfinite(zform)]
            sfr=.015*(1+zform)**2.7/(1+((1+zform)/2.9)**5.6)*1e9 # MD14 eq.15
            rate += .5*float(np.sum(sfr))/norm; n+=1
        except (OSError,KeyError,ValueError): pass
    if n: rate/=len(MASTER) # average seeds; .5 already weights each metallicity
    return dict(rate_Gpc3_yr=rate if n else None,target=[17.9,44.0],pass_control=(17.9<=rate<=44) if n else None,n_files=n,sfh='Madau & Dickinson 2014 eq.15')

def classify(ds):
    if not ds:return 'PENDING'
    signs=[]
    for d in ds:
        e=d['mc_standard_error']; x=d['derivative']
        signs.append(-1 if np.isfinite(e) and x+e<0 else 1 if np.isfinite(e) and x-e>0 else 0)
    if all(s<0 for s in signs): return 'K1S2_MONOTONE_DOWN'
    if all(s>0 for s in signs): return 'K1S2_MONOTONE_UP'
    if 1 in signs and -1 in signs:return 'K1S2_SIGN_INVERTS'
    return 'K1S2_UNIDENTIFIED'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--json',action='store_true'); ns=ap.parse_args()
    rows=discover(); maina=aggregate(rows); ds=derivatives(maina)
    ssea=aggregate(rows,('sse',),MASTER); ssed=derivatives(ssea)
    c4a=aggregate(rows,('bse','c4'),MASTER+EXTRA); c4d=[d for d in derivatives(c4a) if d['engine']=='DELAYED' and d['z']==.02 and d['ce']=='default']
    report=dict(files_found=len(rows),done=(RUNS/'DONE').exists(),normalization='COMPAS compas_python_utils/cosmic_integration/totalMassEvolvedPerZ.py::totalMassEvolvedPerZ',imf_secondary_treatment='conditional mass-ratio draw; no independent secondary IMF weight',table=ds,class_if_complete=classify(ds) if (RUNS/'DONE').exists() else 'PENDING',C1=c1(rows),C2=c2(rows),C3=dict(table=ssed,sign=classify(ssed)),C4=dict(table=c4d,sign=classify(c4d),sign_unchanged=(classify(c4d)==classify([d for d in ds if d['engine']=='DELAYED' and d['z']==.02 and d['ce']=='default'])) if c4d else None))
    print(json.dumps(report,indent=2,default=lambda x: None if isinstance(x,float) and not np.isfinite(x) else x))
if __name__=='__main__': main()
