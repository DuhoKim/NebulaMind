#!/usr/bin/env python3
"""Rebuild the catalogue-only protected-footprint guarded pool."""
import csv, gzip, hashlib, json, math, sys, time
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
POOLBUILD = ROOT.parent
EXPECTED = (12100, 46, 12054)
R_GUARD_ARCSEC = (33.536 / 2) * math.sqrt(2)

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def load_pool(gz_path, receipt_path):
    with open(receipt_path,encoding='utf-8') as f: receipt=json.load(f)
    dispositions=receipt['terminal_dispositions']
    rows=[]; counts={'clockwise':0,'anticlockwise':0,'contradictory':0,'below_threshold':0}
    with gzip.open(gz_path,'rt',encoding='utf-8',newline='') as f:
        for r in csv.DictReader(f):
            oid=r['OBJID']; ra=float(r['ra_deg']); dec=float(r['dec_deg'])
            pcw=float(r['P_CW']); pacw=float(r['P_ACW'])
            if not (math.isfinite(ra) and math.isfinite(dec) and math.isfinite(pcw) and math.isfinite(pacw)
                    and 0<=ra<360 and -90<=dec<=90 and 0<=pcw<=1 and 0<=pacw<=1):
                raise ValueError('invalid/non-finite GZ1 value for '+oid)
            if pcw>=0.8 and pacw>=0.8: counts['contradictory']+=1; continue
            if pcw>=0.8: g=1; counts['clockwise']+=1
            elif pacw>=0.8: g=-1; counts['anticlockwise']+=1
            else: counts['below_threshold']+=1; continue
            if dispositions.get(oid)=='NO-DR10-WITHIN-1ARCSEC': rows.append((int(oid),ra,dec,g))
    return rows,counts

def load_protected(paths):
    out=[]
    for path, racol, deccol in paths:
        with open(path,encoding='utf-8',newline='') as f:
            out.extend((float(r[racol]),float(r[deccol])) for r in csv.DictReader(f))
    return np.asarray(out,dtype=np.float64)

def guard_mask(candidates, protected):
    """True for candidates within the inclusive great-circle guard radius."""
    pdec=np.deg2rad(protected[:,1]); order=np.argsort(pdec); pdec=pdec[order]
    pra=np.deg2rad(protected[:,0][order]); radius=np.float64(R_GUARD_ARCSEC/3600*math.pi/180)
    result=np.zeros(len(candidates),dtype=bool)
    for i,(_,ra,dec,_) in enumerate(candidates):
        d=np.float64(math.radians(dec)); lo=np.searchsorted(pdec,d-radius,'left'); hi=np.searchsorted(pdec,d+radius,'right')
        if lo==hi: continue
        # Stable great-circle angle: atan2(||u x v||, u dot v), all binary64.
        rr=np.float64(math.radians(ra)); dl=pdec[lo:hi]; dr=pra[lo:hi]-rr
        sd=np.sin(dl); cd=np.cos(dl); s0=np.sin(d); c0=np.cos(d)
        dot=s0*sd+c0*cd*np.cos(dr)
        cross=np.sqrt(np.maximum(np.float64(0),np.float64(1)-dot*dot))
        sep=np.arctan2(cross,dot)
        result[i]=bool(np.any(sep<=radius))
    return result

def build(check_controls=True):
    start=time.perf_counter()
    gz=ROOT/'scratch/gz1_parsed.csv.gz'; cp=ROOT/'completeness_gate/artifacts_full/checkpoint.jsonl'
    cr=ROOT/'completeness_gate/artifacts_full/completeness_receipt_20260903T122712Z.json'
    rows,label_counts=load_pool(gz,cr)
    paths=[(POOLBUILD/'_successor_build_20260824/acquire/positions_selected_cut.csv','ra','dec'),
           (POOLBUILD/'_successor_build_20260824/acquire/positions_selected.csv','ra','dec'),
           (ROOT/'TIER_C_SAMPLE_MANIFEST_V13_20260904.csv','RA','DEC')]
    protected=load_protected(paths); dropped=guard_mask(rows,protected); kept=[r for r,x in zip(rows,dropped) if not x]
    actual=(len(rows),int(dropped.sum()),len(kept))
    print('pool = %d; guard dropped = %d; guarded pool = %d'%actual)
    if check_controls and actual!=EXPECTED:
        print('CONTROL FAILURE: expected %r, actual %r'%(EXPECTED,actual)); return False
    out=HERE/'guarded_pool.csv'
    with open(out,'w',encoding='ascii',newline='') as f:
        w=csv.writer(f,lineterminator='\n'); w.writerow(['GZ1_OBJID','RA','DEC','G']); w.writerows(kept)
    rec={'schema_version':'GUARDED-POOL-1','pool_count':actual[0],'guard_dropped_count':actual[1],
         'guarded_pool_count':actual[2],'controls_expected':dict(zip(('pool','guard_dropped','guarded_pool'),EXPECTED)),
         'controls_pass':actual==EXPECTED,'label_counts':label_counts,'protected_rows_with_duplicates':len(protected),
         'r_guard_expression_arcsec':'(33.536 / 2) * sqrt(2)','r_guard_binary64_hex':float(R_GUARD_ARCSEC).hex(),
         'separation':'binary64 great-circle atan2(norm(cross), dot); inclusive <= boundary',
         'disposition_container_field':'terminal_dispositions','disposition_object_id_field':'mapping key (GZ1 OBJID)',
         'disposition_value_field':'mapping value','required_disposition':'NO-DR10-WITHIN-1ARCSEC',
         'checkpoint_context':str(cp.relative_to(ROOT)),'completeness_receipt':str(cr.relative_to(ROOT)),
         'guarded_pool_sha256':sha256(out),'runtime_seconds':time.perf_counter()-start}
    with open(HERE/'guarded_pool_receipt.json','w',encoding='utf-8') as f: json.dump(rec,f,sort_keys=True,separators=(',',':')); f.write('\n')
    return True

if __name__=='__main__': sys.exit(0 if build() else 1)
