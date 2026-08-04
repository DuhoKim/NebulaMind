#!/usr/bin/env python3
"""
Cycle-4 Goru — resolve the THREE TNG data flags on paper #4, from REAL
TNG100-1 group-catalog chunks (public API; same api-key + col-4=stars
convention as tools/lab_runner_worker.tng_field). STANDALONE: does not
touch the worker daemon/queue or any tracked file.

Groupcat subhalos are ordered by descending FoF-halo mass, so every
massive galaxy (logM*>10.5) lives in the first ~20 of 448 chunks (verified:
chunk0 has 20 such galaxies & maxlogM*=11.31; chunk20 maxlogM*=7.82, zero).
We pull chunks 0..NCH in PARALLEL (disk-cached, resumable), keeping only
Subhalo/{SubhaloFlag,SubhaloMassType,SubhaloMassInRadType}, and verify the
massive-end has converged (a long flat tail of chunks with maxlogM*<<10.5).

z=5 -> snap17 (z=4.996); z=6 -> snap13 (z=6.011). Box 75 Mpc/h, h=0.6774.
"""
import warnings; warnings.filterwarnings("ignore")
import io, time, math, sys, os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np, requests, h5py

REPO=Path("/Users/duhokim/NebulaMind/NebulaMind"); ENV=REPO/"backend"/".env"
CACHE=Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/quartet-papers-20260723T092024Z/_tng_c4")
CACHE.mkdir(parents=True,exist_ok=True)
KEY=[l.split("=",1)[1].strip().strip('"').strip("'") for l in ENV.read_text().splitlines() if l.startswith("NM_TNG_API_KEY")][0]
SIM="TNG100-1"; H=0.6774; L_BOX=75.0/H; V_BOX=L_BOX**3
SNAPS={5:17,6:13}; THRESH=10.5; THRESH_LO=10.3
NCH=30                # chunks/snapshot (converges by ~20; 30 gives a 10-chunk flat tail)
WORKERS=8

def fetch_to_disk(snap,i,tries=8):
    fn=CACHE/f"gc_{snap}_{i}.hdf5"
    if fn.exists() and fn.stat().st_size>2000:
        try:
            with h5py.File(fn,"r") as f: _=f["Subhalo"]["SubhaloFlag"][:1]
            return i,True
        except Exception: pass
    url=f"https://www.tng-project.org/api/{SIM}/files/groupcat-{snap}.{i}.hdf5"
    s=requests.Session(); s.headers.update({"api-key":KEY})
    for _ in range(tries):
        try:
            r=s.get(url,timeout=240,allow_redirects=True)
            if r.status_code!=200: time.sleep(5); continue
            with open(fn,"wb") as o: o.write(r.content)
            with h5py.File(fn,"r") as f: _=f["Subhalo"]["SubhaloFlag"][:1]
            return i,True
        except Exception:
            if fn.exists(): fn.unlink(missing_ok=True)
            time.sleep(5)
    return i,False

def read_chunk(snap,i):
    fn=CACHE/f"gc_{snap}_{i}.hdf5"
    with h5py.File(fn,"r") as f:
        mt=f["Subhalo"]["SubhaloMassType"][:,4]*1e10/H
        mr=f["Subhalo"]["SubhaloMassInRadType"][:,4]*1e10/H
        fl=f["Subhalo"]["SubhaloFlag"][:]
    return mt,mr,fl

def poisson(n): return float('inf') if n==0 else 1.0/math.sqrt(n)

print(f"Box L={L_BOX:.2f} Mpc  V={V_BOX:.4e} Mpc^3  (75 Mpc/h, h={H})",flush=True)
R={}
for zlab,snap in SNAPS.items():
    t0=time.time(); okset={}
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs=[ex.submit(fetch_to_disk,snap,i) for i in range(NCH)]
        for fu in as_completed(futs):
            i,ok=fu.result(); okset[i]=ok
            if not ok: print(f"  WARN chunk {snap}.{i} FAILED",flush=True)
    ndl=sum(okset.values())
    print(f"[z{zlab} snap{snap}] downloaded {ndl}/{NCH} chunks in {time.time()-t0:.0f}s",flush=True)
    MT=[];MR=[];FL=[];cmax=[]
    for i in range(NCH):
        if not okset.get(i): continue
        mt,mr,fl=read_chunk(snap,i); MT.append(mt);MR.append(mr);FL.append(fl)
        cmax.append((i, float(np.log10(mt.max()) if mt.max()>0 else -9)))
    mt=np.concatenate(MT);mr=np.concatenate(MR);fl=np.concatenate(FL)
    gal=(fl==1)
    lt=np.log10(np.where(mt>0,mt,np.nan)); lr=np.log10(np.where(mr>0,mr,np.nan))
    N_tot=int((gal&(mt>10**THRESH)).sum()); n_tot=N_tot/V_BOX
    N_rad=int((gal&(mr>10**THRESH)).sum()); n_rad=N_rad/V_BOX
    pop=gal&(mt>10**THRESH_LO)&(mr>0); d=(lt-lr)[pop]; d=d[np.isfinite(d)]
    off=float(np.median(d)); olo,ohi=np.percentile(d,[16,84])
    pop2=gal&(mt>10**THRESH)&(mr>0); d2=(lt-lr)[pop2]; d2=d2[np.isfinite(d2)]
    off2=float(np.median(d2)) if d2.size else float('nan')
    tail=[c for ii,c in cmax if ii>=20]; tailmax=max(tail) if tail else 9.9
    R[zlab]=dict(snap=snap,N_tot=N_tot,n_tot=n_tot,N_rad=N_rad,n_rad=n_rad,off=off,
                 olo=float(olo),ohi=float(ohi),npop=int(d.size),off2=off2,npop2=int(d2.size),
                 subs=int(gal.sum()),ndl=ndl,tailmax=float(tailmax))
    print(f"[z={zlab}] {int(gal.sum()):,} flagged subhalos in {ndl} chunks; convergence: max logM* over chunks>=20 = {tailmax:.2f} (<< {THRESH})",flush=True)
    print(f"   N(>10^{THRESH} TOTAL) ={N_tot:4d} -> n={n_tot:.3e} Mpc^-3  Poisson +/-{poisson(N_tot)*100:.0f}%",flush=True)
    print(f"   N(>10^{THRESH} 2Rhalf)={N_rad:4d} -> n={n_rad:.3e} Mpc^-3  Poisson +/-{poisson(N_rad)*100:.0f}%",flush=True)
    print(f"   aperture offset TOTAL-2Rhalf (logM*>{THRESH_LO}): median {off:+.3f} dex [16-84 {olo:+.3f},{ohi:+.3f}] N={d.size}",flush=True)
    print(f"      restricted >10^{THRESH}: median {off2:+.3f} dex N={d2.size}",flush=True)

print("="*72);print("SUMMARY");print("="*72,flush=True)
z5,z6=R[5],R[6]
print(f"M4 aperture offset (TOTAL SubhaloMassType vs 2Rhalf SubhaloMassInRadType, logM*>{THRESH_LO}, z=5): {z5['off']:+.3f} dex (16-84 {z5['olo']:+.3f}/{z5['ohi']:+.3f}, N={z5['npop']})")
print(f"M5 z=5 raw in-box count @10^{THRESH}: TOTAL N={z5['N_tot']} n={z5['n_tot']:.3e} (+/-{poisson(z5['N_tot'])*100:.0f}%) | 2Rhalf N={z5['N_rad']} n={z5['n_rad']:.3e} (+/-{poisson(z5['N_rad'])*100:.0f}%)")
print(f"M6 z=6 abundance @10^{THRESH}: TOTAL n={z6['n_tot']:.3e} (N={z6['N_tot']}) | 2Rhalf n={z6['n_rad']:.3e} (N={z6['N_rad']})")
print(f"   z=5 ref: TOTAL n={z5['n_tot']:.3e} | 2Rhalf n={z5['n_rad']:.3e}")
print(f"Paper z=5 anchor 1.1e-5 -> match: TOTAL={z5['n_tot']:.2e} 2Rhalf={z5['n_rad']:.2e}")
if z6['n_tot']>0: print(f"z5/z6 ratio TOTAL {z5['n_tot']/z6['n_tot']:.2f}x")
if z6['n_rad']>0: print(f"z5/z6 ratio 2Rhalf {z5['n_rad']/z6['n_rad']:.2f}x")
print(f"convergence tail max logM* (chunks>=20): z5={z5['tailmax']:.2f} z6={z6['tailmax']:.2f}")
