#!/usr/bin/env python3
"""Persistent background fetcher for the 6 TNG field files (snap 17 & 13).
Retries the per-field extraction endpoint through server-load 504s.
Writes each field to _tng_c4/ ; prints progress to stdout."""
import warnings; warnings.filterwarnings("ignore")
import os, time, requests
from pathlib import Path
REPO=Path("/Users/duhokim/NebulaMind/NebulaMind"); ENV=REPO/"backend"/".env"
CACHE=Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/quartet-papers-20260723T092024Z/_tng_c4")
CACHE.mkdir(parents=True,exist_ok=True)
KEY=[l.split("=",1)[1].strip().strip('"').strip("'") for l in ENV.read_text().splitlines() if l.startswith("NM_TNG_API_KEY")][0]
S=requests.Session(); S.headers.update({"api-key":KEY})
FIELDS=["SubhaloFlag","SubhaloMassType","SubhaloMassInRadType"]
SNAPS=[17,13]
def ok(fn):
    if not (fn.exists() and fn.stat().st_size>2000): return False
    try:
        import h5py
        with h5py.File(fn,"r") as f: _=f["Subhalo"][list(f["Subhalo"].keys())[0]][:1]
        return True
    except Exception: return False
def grab(snap,field,deadline):
    fn=CACHE/f"TNG100-1_{snap}_{field}.hdf5"
    if ok(fn): print(f"cached {field}@{snap}",flush=True); return True
    url=f"https://www.tng-project.org/api/TNG100-1/files/groupcat-{snap}/?Subhalo={field}"
    while time.time()<deadline:
        try:
            with S.get(url,timeout=420,allow_redirects=True,stream=True) as r:
                if r.status_code==200:
                    with open(fn,"wb") as o:
                        for c in r.iter_content(1<<20): o.write(c)
                    if ok(fn): print(f"OK {field}@{snap} {fn.stat().st_size}B",flush=True); return True
                    print(f"bad-body {field}@{snap}",flush=True)
                else:
                    print(f"{field}@{snap} {r.status_code}",flush=True)
        except Exception as e:
            print(f"{field}@{snap} err {type(e).__name__}",flush=True)
        time.sleep(20)
    return False
deadline=time.time()+3300  # ~55 min budget
done=0
for snap in SNAPS:
    for field in FIELDS:
        if grab(snap,field,deadline): done+=1
print(f"DONE {done}/6",flush=True)
