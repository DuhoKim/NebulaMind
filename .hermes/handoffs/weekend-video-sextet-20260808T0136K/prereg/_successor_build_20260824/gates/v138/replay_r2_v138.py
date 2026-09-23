#!/usr/bin/env python3
"""V138 §6.6 primary replay — Tier A shard through the NEW pinned reader tree, twice, through the recording adapter,
then exact record equality. Subcommands:
  run      --tree TREE_R2_DIR --shard SHARD.json --brick-root ROOT --out DIR --pass N [--workers 4] [--limit K]
           each worker is a FRESH process with the pinned single-thread env; writes records.jsonl (full adapter record:
           38 features, peak_snr, comparators, logit, label, selective_label, status, tensor sha) + rows.jsonl (driver row)
           + PIN_LAUNCH.json / PIN_COMPLETION.json (sha256 of every module in sys.modules with a file, at both endpoints)
  compare  --a PASS1_DIR --b PASS2_DIR --out RECEIPT.json   exact equality per record; fallback criterion evaluated and
           reported but only INVOKED when the primary is FAILED; a missing record refuses.
  control  --a PASS1_DIR --out RECEIPT.json   fail-first control: copies pass A, perturbs ONE feature of ONE record by
           one ULP, compares -> must report FAILED, else the checker is broken and the control REFUSES.
No pixel of an unexposed object is read: the shard's machine half is already exposed (V138 §6.4)."""
import argparse, hashlib, importlib.util, json, math, os, pathlib, shutil, subprocess, sys, datetime, struct
H=pathlib.Path(__file__).resolve().parent
RS=pathlib.Path('/Users/duhokim/work/Trio/HWAO_TIER_A_INPUTS_20260909/run_scoring.py')
ADAPTER=pathlib.Path('/Users/duhokim/work/Trio/RELIABILITY_AND_BIAS_PHASE_20260910/hwao/recording_adapter.py')
ENV={'OMP_NUM_THREADS':'1','VECLIB_MAXIMUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','PYTHONHASHSEED':'0','PYTHONDONTWRITEBYTECODE':'1'}
DZ_BOUND=1e-12
def utc(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
def sha_file(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
def pin_modules():
    out={}
    for name,m in list(sys.modules.items()):
        f=getattr(m,'__file__',None)
        if f and os.path.isfile(f): out[name]={'file':f,'sha256':sha_file(f)}
    return out
def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def cmd_worker(a):
    """One fresh process: score its slice of the shard through the tree, recording everything."""
    tree=pathlib.Path(a.tree).resolve(); out=pathlib.Path(a.out); out.mkdir(parents=True,exist_ok=True)
    rs=load_module(RS,'run_scoring_pinned'); rs.R2=tree            # bind the NEW tree before build()
    RD,loader,chain,inference=rs.build()
    if pathlib.Path(inference.__file__).resolve()!=tree/'inference.py': sys.exit('REFUSED: inference imported from elsewhere')
    ad=load_module(ADAPTER,'recording_adapter')
    rec=ad.Recorder(inference.predict, model_identity={'inference.py':str(tree/'inference.py'),'model.json':str(tree/'model.json'),
                    'spectral_shim':str(tree/'spectral_branch/spectral.py')}, source_roots=(str(tree.parent),'/Users/duhokim/work/Trio'))
    (out/'PIN_LAUNCH.json').write_text(json.dumps({'utc':utc(),'pid':os.getpid(),'env':{k:os.environ.get(k) for k in ENV},'modules':pin_modules(),
        'harness_sha256':{'replay_r2_v138.py':sha_file(__file__),'run_scoring.py':sha_file(RS),'recording_adapter.py':sha_file(ADAPTER)}},indent=1,sort_keys=True))
    root=pathlib.Path(a.brick_root).resolve(); RD.SEARCH[:]=[root]; loader.SEARCH[:]=[root]
    import numpy as np
    pinned=rs.pinned_inventory(None)
    if not pinned: sys.exit('REFUSED: no pinned DR10 inventory')
    targets=json.loads(pathlib.Path(a.shard).read_text()); targets=sorted(targets,key=rs.object_key)
    mine=[t for i,t in enumerate(targets) if i%a.workers==a.index]
    if a.limit: mine=mine[:a.limit]
    current={}
    def predict(x):
        r=rec.record(x, identity=dict(current)); recs.write(json.dumps(r,sort_keys=True)+'\n'); recs.flush()
        if r['inference'] is None: raise ValueError(r.get('reason','REFUSED'))
        return r['inference']
    with (out/'records.jsonl').open('x') as recs, (out/'rows.jsonl').open('x') as rows:
        for t in mine:
            current={'object_key':rs.object_key(t),'brick':t['brick']}
            row=rs.score(t,RD,loader,chain,predict,np,root,pinned); rows.write(json.dumps(row,sort_keys=True)+'\n')
    rec.finalize(); (out/'SESSION.json').write_text(json.dumps(rec.session,indent=1,sort_keys=True,default=str))
    (out/'PIN_COMPLETION.json').write_text(json.dumps({'utc':utc(),'modules':pin_modules()},indent=1,sort_keys=True))
    print(json.dumps({'worker':a.index,'n':len(mine),'out':str(out)}))

def cmd_run(a):
    out=pathlib.Path(a.out)/f'pass-{a.pass_}'
    if out.exists(): sys.exit(f'REFUSED: {out} exists; passes are never overwritten')
    out.mkdir(parents=True)
    env=dict(os.environ); env.update(ENV)
    procs=[]
    for i in range(a.workers):
        cmd=[sys.executable,'-B',__file__,'worker','--tree',a.tree,'--shard',a.shard,'--brick-root',a.brick_root,'--out',str(out/f'worker-{i}'),'--workers',str(a.workers),'--index',str(i)]+(['--limit',str(a.limit)] if a.limit else [])
        log=(out/f'worker-{i}.log').open('w'); procs.append((subprocess.Popen(cmd,env=env,stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL),log))
    rc=[p.wait() for p,_ in procs]; [l.close() for _,l in procs]
    summ={'schema':'hwao-v138-replay-pass-1','pass':a.pass_,'workers':a.workers,'exit_codes':rc,'shard':a.shard,'shard_sha256':sha_file(a.shard),'tree':a.tree,'finished_utc':utc(),
          'records':sum(sum(1 for _ in (out/f'worker-{i}/records.jsonl').open()) for i in range(a.workers) if (out/f'worker-{i}/records.jsonl').exists())}
    (out/'PASS_SUMMARY.json').write_text(json.dumps(summ,indent=1,sort_keys=True)); print(json.dumps(summ))

def _load_pass(d):
    d=pathlib.Path(d); recs={}
    for f in sorted(d.glob('worker-*/records.jsonl')):
        for line in f.open():
            r=json.loads(line); k=r['identity'].get('object_key')
            if k in recs: raise SystemExit(f'REFUSED: duplicate record {k} in {d}')
            recs[k]=r
    if not recs: raise SystemExit(f'REFUSED: no records under {d}')
    return recs
def _key_fields(r):
    inf=r.get('inference') or {}
    feats=inf.get('features'); q=inf.get('quality') or {}
    return {'tensor_sha256':r['input'].get('sha256'),'status':r['status'],
            'features':[struct.pack('<d',float(x)).hex() if isinstance(x,(int,float)) else repr(x) for x in (feats if isinstance(feats,list) else (list(feats.values()) if isinstance(feats,dict) else []))],
            'logit':struct.pack('<d',float(inf['logit'])).hex() if 'logit' in inf and isinstance(inf['logit'],(int,float)) else repr(inf.get('logit')),
            'label':inf.get('label'),'selective_label':inf.get('selective_label'),'peak_snr':struct.pack('<d',float(q['peak_snr'])).hex() if isinstance(q.get('peak_snr'),(int,float)) else repr(q.get('peak_snr'))}
def _load_rows(d):
    """Driver rows (one per target, incl. pre-inference REFUSED/INPUT_MISSING/ERROR). Time-free by construction."""
    d=pathlib.Path(d); rows={}
    for f in sorted(d.glob('worker-*/rows.jsonl')):
        for line in f.open():
            r=json.loads(line); k=r['object_key']
            if k in rows: raise SystemExit(f'REFUSED: duplicate row {k} in {d}')
            rows[k]=r
    return rows
def _row_key(r):
    def bits(x): return struct.pack('<d',float(x)).hex() if isinstance(x,(int,float)) and not isinstance(x,bool) else repr(x)
    rd=r.get('render') or {}
    return {'status':r.get('status'),'stage':r.get('stage'),'reason':r.get('reason'),'error_type':r.get('error_type'),
            'raster_digest':rd.get('raster_digest'),'peak':bits(rd.get('peak')),'flagged':rd.get('flagged_output_count'),'source_fill':bits(rd.get('source_fill')),
            'core_tensor_sha256':r.get('core_tensor_sha256'),'label':r.get('label'),'selective_label':r.get('selective_label'),'logit':bits(r.get('logit')),'confidence':bits(r.get('confidence_score')),
            'input_receipts':json.dumps(r.get('input_receipts'),sort_keys=True)}
def cmd_compare(a, _write=True):
    A=_load_pass(a.a); B=_load_pass(a.b)
    RA=_load_rows(a.a); RB=_load_rows(a.b)
    if not RA or not RB: raise SystemExit('REFUSED: driver rows missing on one side; the 35-class pre-inference refusals cannot be compared')
    if set(RA)!=set(RB): raise SystemExit(f'REFUSED: row sets differ: only-A {len(set(RA)-set(RB))}, only-B {len(set(RB)-set(RA))}')
    rows_unequal=[{'object_key':k,'fields':[f for f in _row_key(RA[k]) if _row_key(RA[k])[f]!=_row_key(RB[k])[f]]} for k in RA if _row_key(RA[k])!=_row_key(RB[k])]
    if set(A)!=set(B): raise SystemExit(f'REFUSED: record sets differ: only-A {len(set(A)-set(B))}, only-B {len(set(B)-set(A))}')
    unequal=[]; dec_unequal=[]; maxdz=0.0
    for k in A:
        fa,fb=_key_fields(A[k]),_key_fields(B[k])
        if fa!=fb: unequal.append({'object_key':k,'fields':[f for f in fa if fa[f]!=fb[f]]})
        da=(fa['label'],fa['selective_label'],fa['status']); db=(fb['label'],fb['selective_label'],fb['status'])
        if da!=db: dec_unequal.append(k)
        ia,ib=(A[k].get('inference') or {}),(B[k].get('inference') or {})
        if isinstance(ia.get('logit'),(int,float)) and isinstance(ib.get('logit'),(int,float)): maxdz=max(maxdz,abs(ia['logit']-ib['logit']))
    primary='PASS' if (not unequal and not rows_unequal) else 'FAILED'
    fallback={'criterion':f'label/selective_label/status equal on 100% AND max|dz| <= {DZ_BOUND}','decision_unequal':len(dec_unequal),'max_abs_dz':maxdz,
              'would_pass':(not dec_unequal) and maxdz<=DZ_BOUND,'invoked':primary=='FAILED'}
    rec={'schema':'hwao-v138-replay-receipt-1','utc':utc(),'pass_a':str(a.a),'pass_b':str(a.b),'records':len(A),
         'primary_criterion':'exact record equality: adapter records (tensor_sha256, all features as binary64 bits, logit bits, label, selective_label, status, peak_snr bits) AND driver rows for every target incl. pre-inference refusals (status, stage, reason, raster digest, peak bits, tensor sha, decision fields, input receipts)',
         'primary':primary,'unequal_records':len(unequal),'unequal_examples':unequal[:20],'rows_compared':len(RA),'rows_unequal':len(rows_unequal),'rows_unequal_examples':rows_unequal[:20],'fallback':fallback,
         'verdict':'PRIMARY-PASS' if primary=='PASS' else ('FALLBACK-PASS (primary FAILED, disclosed)' if fallback['would_pass'] else 'STOP (primary FAILED and fallback FAILED)'),
         'harness_sha256':sha_file(__file__)}
    if _write: pathlib.Path(a.out).write_text(json.dumps(rec,indent=1,sort_keys=True)); print(json.dumps({k:rec[k] for k in ('records','primary','unequal_records','verdict')}))
    return rec
def cmd_control(a):
    """Fail-first: a 1-ULP perturbation of one feature in a copy of pass A must be caught."""
    src=pathlib.Path(a.a); dst=pathlib.Path(a.out).with_suffix('')/'_control_copy'
    if dst.exists(): shutil.rmtree(dst)
    shutil.copytree(src,dst); f=sorted(dst.glob('worker-*/records.jsonl'))[0]; lines=f.read_text().splitlines()
    for i,line in enumerate(lines):
        r=json.loads(line); inf=r.get('inference')
        if inf and isinstance(inf.get('features'),list) and inf['features']:
            x=float(inf['features'][0]); inf['features'][0]=math.nextafter(x,math.inf); lines[i]=json.dumps(r,sort_keys=True); break
    else: raise SystemExit('REFUSED: no record with features to perturb')
    f.write_text('\n'.join(lines)+'\n')
    class NS: pass
    ns=NS(); ns.a=str(src); ns.b=str(dst); ns.out=a.out
    rec=cmd_compare(ns,_write=False); ok=rec['primary']=='FAILED' and rec['unequal_records']==1
    out={'schema':'hwao-v138-replay-control-1','utc':utc(),'perturbation':'1 ULP on features[0] of one record','checker_caught_it':ok,'verdict':'CONTROL-PASS' if ok else 'CONTROL-FAILED: checker is broken; no PASS from it may be trusted'}
    pathlib.Path(a.out).write_text(json.dumps(out,indent=1)); shutil.rmtree(dst); print(json.dumps(out))
    if not ok: sys.exit(2)

if __name__=='__main__':
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    for name in ('run','worker'):
        p=sp.add_parser(name); p.add_argument('--tree',required=True); p.add_argument('--shard',required=True); p.add_argument('--brick-root',required=True); p.add_argument('--out',required=True); p.add_argument('--workers',type=int,default=4); p.add_argument('--limit',type=int,default=0)
        if name=='run': p.add_argument('--pass',dest='pass_',type=int,required=True)
        else: p.add_argument('--index',type=int,required=True)
    p=sp.add_parser('compare'); p.add_argument('--a',required=True); p.add_argument('--b',required=True); p.add_argument('--out',required=True)
    p=sp.add_parser('control'); p.add_argument('--a',required=True); p.add_argument('--out',required=True)
    a=ap.parse_args(); {'run':cmd_run,'worker':cmd_worker,'compare':cmd_compare,'control':cmd_control}[a.cmd](a)
