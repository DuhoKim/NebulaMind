#!/usr/bin/env python3
"""Compose PC400/brick_root/<brick>/legacysurvey-<brick>-<plane>.fits.fz as SYMLINKS (no bytes copied, nothing downloaded)
over the roots the DR10 transfer itself resolved from (transfer_common.dr10_cached: acquire/bricks_tier_c, acquire/bricks, flat)
plus the transfer's own per-brick dir. Refuses unless every brick of the recorded 400 draw resolves all three planes; reports
coverage of the whole 1,079 population too (the §6.5 'bricks on disk' statement, checked)."""
import json, os, pathlib, sys, datetime, hashlib
P=pathlib.Path(__file__).resolve().parent; PC=P/'PC400'; OUT=PC/'brick_root'
D=pathlib.Path('/Users/duhokim/work/Trio/HWAO_DR10_TRANSFER_20260909')
AQ=pathlib.Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/acquire')
PLANES=('image-r','maskbits','nexp-r')
def candidates(b,p):
    n=f'legacysurvey-{b}-{p}.fits.fz'
    return [D/'bricks'/b/n, AQ/'bricks_tier_c'/n, AQ/'bricks'/n]
def resolve(b,p):
    for c in candidates(b,p):
        if c.is_file() and c.stat().st_size>0: return c
    return None
man=json.load(open(D/'MANIFEST.json')); allb=sorted({o['primary_brick'] for o in man['objects']})
draw=json.load(open(PC/'DRAW.json')); drawn=sorted({e['brick'] for e in draw['entries']})
pop={b:{p:resolve(b,p) for p in PLANES} for b in allb}
full=[b for b in allb if all(pop[b].values())]; missing={b:[p for p in PLANES if not pop[b][p]] for b in allb if not all(pop[b].values())}
src=collections=__import__('collections').Counter(str(pop[b][p]).split('/')[-2] if 'acquire' in str(pop[b][p]) else 'transfer/bricks' for b in allb for p in PLANES if pop[b][p])
rep={'schema':'hwao-v138-pc-brick-root-1','utc':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'population_bricks':len(allb),'population_bricks_all_three_planes':len(full),
     'population_unresolved':missing,'planes_by_source':dict(src),'drawn_bricks':len(drawn),'drawn_unresolved':{b:missing[b] for b in drawn if b in missing},'method':'symlinks only; no bytes copied; no network'}
if rep['drawn_unresolved']: (PC/'BRICK_ROOT_REFUSED.json').write_text(json.dumps(rep,indent=1)); sys.exit('REFUSED: drawn bricks unresolved: '+json.dumps(rep['drawn_unresolved']))
if OUT.exists(): sys.exit(f'REFUSED: {OUT} exists')
n=0
for b in allb:
    if b not in full: continue
    (OUT/b).mkdir(parents=True)
    for p in PLANES: os.symlink(pop[b][p], OUT/b/f'legacysurvey-{b}-{p}.fits.fz'); n+=1
rep['symlinks_created']=n; rep['dangling']=sum(1 for l in OUT.rglob('*.fz') if not l.resolve().is_file()); rep['root']=str(OUT)
(PC/'BRICK_ROOT.json').write_text(json.dumps(rep,indent=1)); print(json.dumps({k:rep[k] for k in ('population_bricks','population_bricks_all_three_planes','drawn_bricks','symlinks_created','dangling','planes_by_source')}))
if rep['population_unresolved']: print('population bricks NOT fully resolved (not drawn):', len(rep['population_unresolved']))
