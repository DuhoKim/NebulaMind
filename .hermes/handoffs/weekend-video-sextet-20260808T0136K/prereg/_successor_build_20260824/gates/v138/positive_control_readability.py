#!/usr/bin/env python3
"""V138 §6.5 positive control (Run B) — the SAME reader route as the pilot, with the FULL rubric bytes delivered this
time, on V138-N-PC = 400 known-readable spirals drawn by a drand-anchored seed from the 1,079 DR10-south human-labelled
targets (outside the 49,211). Stages, each a subcommand, each refusing to overwrite:
  draw     --manifest MANIFEST.json --n 400 --drand-round R (or --seed-hex H) --out DIR   -> DRAW.json (pinned list)
  render   --draw DIR --bricks BRICKS_DIR --out DIR                                         -> images/<pid>/<pid>.png (+ mirrored copies for the fixture)
  fixtures --out DIR --rubric FILE [--reader R1]                                            -> FIXTURES.json: decoy-isolation + mirror-invariance, raw responses kept
  present  --out DIR --rubric FILE --reader R1|R2 [--max-hours H]                           -> votes_<reader>.jsonl (one isolated agy call per presentation; no retry)
  evaluate --out DIR --a-min 0.50 --dir-min 0.90 --expert-map "+1:S,-1:Z"                  -> RECEIPT.json PASS/FAIL (Wilson 95% LB); REFUSES without --expert-map
The reader is never given identity, catalogue label, machine output or another reader's answer; the crosswalk pid->object
is read only by draw/render/evaluate, never by present. The expert-label -> S/Z direction map is a REQUIRED pinned input
(the documentary CzSL R/L <-> S/Z relation must be fixed from the source before evaluate; it is not fitted)."""
import argparse, hashlib, json, math, pathlib, random, subprocess, sys, time, datetime, urllib.request, re
import numpy as np
R=pathlib.Path('/Users/duhokim/work/Trio'); AUDIT=R/'TRIO_SPIN_AUDIT_20260910/hwao'
AGY='/Users/duhokim/.local/bin/agy'
def utc(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def sha_b(b): return hashlib.sha256(b).hexdigest()
def sha_f(p): return sha_b(pathlib.Path(p).read_bytes())
def wilson_lb(k,n,z=1.959963984540054):
    if n==0: return 0.0
    p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d; return max(0.0,c-h)

def cmd_draw(a):
    out=pathlib.Path(a.out); out.mkdir(parents=True,exist_ok=True); f=out/'DRAW.json'
    if f.exists(): sys.exit('REFUSED: DRAW.json exists')
    man=json.loads(pathlib.Path(a.manifest).read_text()); objs=man['objects']
    if a.seed_hex: seed_hex=a.seed_hex; src={'form':'caller-supplied hex','note':'not drand-anchored unless the caller says so'}
    else:
        url=f'https://api.drand.sh/8990e7a9aaed2ffed73dbd7092123d6f28993054/public/{a.drand_round}'
        d=json.loads(urllib.request.urlopen(url,timeout=30).read()); seed_hex=d['randomness']; src={'form':'drand mainnet chain 8990e7a9…','round':a.drand_round,'signature':d.get('signature','')[:32]+'…','fetched_utc':utc()}
    rnd=random.Random(int(seed_hex,16)); order=sorted(objs,key=lambda o:str(o['objid'])); rnd.shuffle(order); pick=order[:a.n]
    salt=sha_b((seed_hex+'|pc400').encode())[:16]
    entries=[{'pid':sha_b(f"{salt}|{o['objid']}".encode())[:20],'objid':str(o['objid']),'ra':o['ra'],'dec':o['dec'],'brick':o['primary_brick'],'expert':int(o['expert'])} for o in pick]
    json.dump({'schema':'hwao-v138-pc-draw-1','utc':utc(),'manifest':str(a.manifest),'manifest_sha256':sha_f(a.manifest),'n':a.n,'seed_hex':seed_hex,'seed_source':src,
               'pool':len(objs),'entries':entries,'expert_distribution':{str(k):sum(1 for e in entries if e['expert']==k) for k in (-1,1)}},f.open('x'),indent=1)
    print(json.dumps({'drawn':len(entries),'seed':seed_hex[:16]}))

def cmd_render(a):
    import importlib.util
    out=pathlib.Path(a.out); draw=json.loads((out/'DRAW.json').read_text()); img=out/'images'
    sys.path.insert(0,str(R/'EXPLORATORY_COMPARISON_20260907/code')); sys.path.insert(0,str(R/'SPIN_IMPROVEMENT_20260908')); sys.path.insert(0,str(AUDIT))
    spec=importlib.util.spec_from_file_location('_rd',R/'SPIN_IMPROVEMENT_20260908/render_diagnostic.py'); loader=importlib.util.module_from_spec(spec); spec.loader.exec_module(loader)
    loader.SEARCH[:]=[pathlib.Path(a.bricks).resolve()]
    chain=__import__('study_renderer.render_chain_v3',fromlist=['rv4']); from render_presentation import save as render_save
    made,failed=[],[]
    for e in draw['entries']:
        d=img/e['pid']; d.mkdir(parents=True,exist_ok=True); png=d/f"{e['pid']}.png"; mdir=img/('m'+e['pid']); mdir.mkdir(exist_ok=True); mpng=mdir/f"m{e['pid']}.png"
        if png.is_file() and mpng.is_file(): made.append(e['pid']); continue
        try:
            planes=loader.load(e['brick'])
            raster=chain.rv4.render_cutout([(planes[0],planes[1],planes[2],planes[3])],chain.rv4.RenderTarget(ra=e['ra'],dec=e['dec'],primary_tile_id=e['brick']))
            arr=np.asarray(raster.array,dtype=np.float64); render_save(arr,png); render_save(np.fliplr(arr),mpng); made.append(e['pid'])
        except Exception as exc: failed.append({'pid':e['pid'],'error':f'{type(exc).__name__}: {exc}'[:200]})
    (out/'RENDER_REPORT.json').write_text(json.dumps({'utc':utc(),'rendered':len(made),'failed':failed,'renderer_sha256':sha_f(AUDIT/'render_presentation.py'),'render_chain':'study_renderer.render_chain_v3 (pinned in STUDIO_APPROVAL_INPUTS.sha256)','bricks_dir':str(pathlib.Path(a.bricks).resolve())},indent=1))
    print(json.dumps({'rendered':len(made),'failed':len(failed)}))

def present_one(png, rubric_text, timeout='4m'):
    d=pathlib.Path(png).parent
    prompt=f"Read the image file {pathlib.Path(png).name} in this directory, then follow these instructions exactly.\n\n{rubric_text}"
    cmd=[AGY,'--add-dir',str(d),'--dangerously-skip-permissions','--print-timeout',timeout,f'--print={prompt}']
    t0=time.time(); p=subprocess.run(cmd,capture_output=True,text=True,stdin=subprocess.DEVNULL); return (p.stdout or p.stderr or '').strip(), round(time.time()-t0,2), p.returncode
LETTER=re.compile(r'\b([ABCD])\b'); DIR=re.compile(r'\b(CW|CCW|S|Z)\b')
def parse(txt):
    """Rubric rule 6: single letter, direction iff A, one-sentence reason. Real schema test; refusals do not pass."""
    lines=[l for l in txt.strip().splitlines() if l.strip()]
    head=' '.join(lines[:2])   # rubric rule 6: letter, direction iff A, one sentence; some readers break the line after the letter
    m=LETTER.search(head)
    if not m: return None,'UNPARSEABLE'
    cat=m.group(1)
    if cat!='A': return {'category':cat,'direction':None},'OK'      # direction is defined only for A; a stray S/Z in a reason is not a direction
    dm=DIR.search(head[m.end():]); direction=dm.group(1) if dm else None
    if direction is None: return {'category':cat,'direction':None},'A_WITHOUT_DIRECTION'
    return {'category':cat,'direction':direction},'OK'

def cmd_fixtures(a):
    out=pathlib.Path(a.out); rub=pathlib.Path(a.rubric).read_text(); f=out/'FIXTURES.json'
    if f.exists(): sys.exit('REFUSED: FIXTURES.json exists')
    draw=json.loads((out/'DRAW.json').read_text()); pid=draw['entries'][0]['pid']; png=out/'images'/pid/f'{pid}.png'; mpng=out/'images'/('m'+pid)/f'm{pid}.png'
    res={'schema':'hwao-v138-pc-fixtures-1','utc':utc(),'rubric_sha256':sha_b(rub.encode())}
    # decoy-isolation: a decoy file OUTSIDE the presentation dir; the reader is asked (once, non-scientific) to list what it can see
    decoy=out/'_decoy'/'DECOY_DO_NOT_READ.txt'; decoy.parent.mkdir(exist_ok=True); decoy.write_text('decoy '+utc())
    d=png.parent; cmd=[AGY,'--add-dir',str(d),'--dangerously-skip-permissions','--print-timeout','3m',f'--print=List every file you are able to read in this directory and in its parent directory. Answer with file names only.']
    p=subprocess.run(cmd,capture_output=True,text=True,stdin=subprocess.DEVNULL); ans=(p.stdout or p.stderr or '')
    res['decoy_isolation']={'decoy_path':str(decoy),'reader_saw_decoy':('DECOY_DO_NOT_READ' in ans),'reader_saw_other_presentations':sum(1 for e in draw['entries'][1:] if e['pid'] in ans),'raw_response':ans[:2000],'rc':p.returncode,
                            'verdict':'PASS' if ('DECOY_DO_NOT_READ' not in ans and not any(e['pid'] in ans for e in draw['entries'][1:])) else 'FAIL'}
    # mirror-invariance: same object, mirrored; category must be equal; direction (if A) must flip
    t1,s1,rc1=present_one(png,rub); t2,s2,rc2=present_one(mpng,rub); v1,st1=parse(t1); v2,st2=parse(t2)
    flip={'S':'Z','Z':'S','CW':'CCW','CCW':'CW'}
    inv=(v1 and v2 and st1=='OK' and st2=='OK' and v1['category']==v2['category'] and (v1['category']!='A' or flip.get(v1['direction'])==v2['direction']))
    res['mirror_invariance']={'original':{'raw':t1[:600],'parsed':v1,'status':st1,'s':s1},'mirrored':{'raw':t2[:600],'parsed':v2,'status':st2,'s':s2},'verdict':'PASS' if inv else 'FAIL',
                             'note':'one object only; a PASS is a demonstration of the mechanism on one case, not a rate'}
    res['verdict']='PASS' if res['decoy_isolation']['verdict']=='PASS' and inv else 'FAIL'
    f.write_text(json.dumps(res,indent=1)); print(json.dumps({'decoy':res['decoy_isolation']['verdict'],'mirror':res['mirror_invariance']['verdict']}))
    if res['verdict']!='PASS': sys.exit(3)

def cmd_present(a):
    out=pathlib.Path(a.out); rub=pathlib.Path(a.rubric).read_text(); led=out/f'votes_{a.reader}.jsonl'
    if led.exists(): sys.exit(f'REFUSED: {led} exists; fresh output only, no append, no retry')
    fx=out/'FIXTURES.json'
    if not fx.exists() or json.loads(fx.read_text())['verdict']!='PASS': sys.exit('REFUSED: fixtures not PASSED; no scientific presentation before the decoy-isolation and mirror fixtures pass')
    draw=json.loads((out/'DRAW.json').read_text()); rnd=random.Random(int(draw['seed_hex'],16)+ (1 if a.reader=='R1' else 2)); order=[e['pid'] for e in draw['entries']]; rnd.shuffle(order)
    t0=time.time(); counts={}
    with led.open('x') as f:
        for i,pid in enumerate(order,1):
            if (time.time()-t0)/3600>a.max_hours:
                f.write(json.dumps({'pid':pid,'status':'NOT_PRESENTED','reason':'completion bound reached'})+'\n'); continue
            png=out/'images'/pid/f'{pid}.png'
            if not png.is_file(): f.write(json.dumps({'pid':pid,'status':'NO_RENDER'})+'\n'); continue
            txt,s,rc=present_one(png,rub); v,st=parse(txt)
            f.write(json.dumps({'pid':pid,'ordinal':i,'reader':a.reader,'status':'VOTE' if st=='OK' else st,'parsed':v,'raw':txt[:800],'seconds':s,'rc':rc,'utc':utc(),'rubric_sha256':sha_b(rub.encode())},sort_keys=True)+'\n'); f.flush()
            counts[st]=counts.get(st,0)+1
    (out/f'PRESENT_SUMMARY_{a.reader}.json').write_text(json.dumps({'reader':a.reader,'n':len(order),'status_counts':counts,'elapsed_s':round(time.time()-t0,1),'route':{'agy':AGY,'agy_sha256':sha_f(AGY) if pathlib.Path(AGY).is_file() else None}},indent=1)); print(json.dumps(counts))

def cmd_evaluate(a):
    out=pathlib.Path(a.out)
    if not a.expert_map: sys.exit('REFUSED: --expert-map is REQUIRED and must be fixed from the CzSL documentation before evaluation (e.g. "+1:S,-1:Z"); it is never fitted')
    emap={int(k):v for k,v in (kv.split(':') for kv in a.expert_map.split(','))}
    draw={e['pid']:e for e in json.loads((out/'DRAW.json').read_text())['entries']}
    rec={'schema':'hwao-v138-pc-receipt-1','utc':utc(),'a_min':a.a_min,'dir_min':a.dir_min,'expert_map':emap,'readers':{}}
    passes=[]
    for led in sorted(out.glob('votes_*.jsonl')):
        votes=[json.loads(l) for l in led.open()]; valid=[v for v in votes if v.get('status')=='VOTE']; n=len(valid)
        A=[v for v in valid if v['parsed']['category']=='A']; kA=len(A)
        agree=sum(1 for v in A if v['parsed']['direction']==emap[draw[v['pid']]['expert']] or (v['parsed']['direction'] in ('CW','CCW') and {'CW':'Z','CCW':'S'}[v['parsed']['direction']]==emap[draw[v['pid']]['expert']]))
        lbA=wilson_lb(kA,n); lbD=wilson_lb(agree,kA) if kA else 0.0
        ok=(lbA>=a.a_min) and (lbD>=a.dir_min)
        rec['readers'][led.stem]={'presented':len(votes),'valid_votes':n,'category_A':kA,'A_fraction':kA/n if n else None,'A_wilson_lb':lbA,'direction_agree':agree,'direction_agree_fraction':agree/kA if kA else None,'direction_wilson_lb':lbD,'PASS':ok,
                                 'category_counts':{c:sum(1 for v in valid if v['parsed']['category']==c) for c in 'ABCD'}}
        passes.append(ok)
    rec['verdict']='PASS' if passes and all(passes) else 'FAIL'; rec['consequence']=('the BS-RG subsample may be read' if rec['verdict']=='PASS' else 'f_R ABSENT; no Tier A subsample is read; the flagship proceeds without the term (V138 §6.5)')
    (out/'RECEIPT.json').write_text(json.dumps(rec,indent=1)); print(json.dumps({'verdict':rec['verdict'],**{k:(v['A_wilson_lb'],v['direction_wilson_lb']) for k,v in rec['readers'].items()}}))

if __name__=='__main__':
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest='cmd',required=True)
    p=sp.add_parser('draw'); p.add_argument('--manifest',required=True); p.add_argument('--n',type=int,default=400); p.add_argument('--drand-round',type=int); p.add_argument('--seed-hex'); p.add_argument('--out',required=True)
    p=sp.add_parser('render'); p.add_argument('--bricks',required=True); p.add_argument('--out',required=True)
    p=sp.add_parser('fixtures'); p.add_argument('--rubric',required=True); p.add_argument('--out',required=True)
    p=sp.add_parser('present'); p.add_argument('--rubric',required=True); p.add_argument('--reader',required=True,choices=['R1','R2']); p.add_argument('--max-hours',type=float,default=6.0); p.add_argument('--out',required=True)
    p=sp.add_parser('evaluate'); p.add_argument('--a-min',type=float,default=0.50); p.add_argument('--dir-min',type=float,default=0.90); p.add_argument('--expert-map',default=None); p.add_argument('--out',required=True)
    a=ap.parse_args(); {'draw':cmd_draw,'render':cmd_render,'fixtures':cmd_fixtures,'present':cmd_present,'evaluate':cmd_evaluate}[a.cmd](a)
