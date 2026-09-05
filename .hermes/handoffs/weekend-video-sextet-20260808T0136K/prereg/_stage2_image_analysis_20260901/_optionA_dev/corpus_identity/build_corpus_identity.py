#!/usr/bin/env python3
"""Build the ordered, catalogue-only corpus identity and CSV templates."""
import csv, hashlib, json, re, sys, time, urllib.error
from datetime import timedelta
from pathlib import Path
import numpy as np
from astropy.io import fits

HERE=Path(__file__).resolve().parent; ROOT=HERE.parent.parent
sys.path.insert(0, str(HERE.parent/'beacon_v2'))
import beacon_record, nist_pulse
ORDERING_RULE='h = SHA256(ASCII base-10 GZ1_OBJID) as unsigned big-endian integer; order by h mod 2^32 ascending, ties by GZ1_OBJID ascending'

def digest_objids(rows): return hashlib.sha256(('\n'.join(str(r['objid']) for r in rows)).encode('ascii')).hexdigest()
def order_rows(rows, seed_hex=None):
    """§9B.5 ordering when seed_hex is None (h = SHA256(ASCII objid)); BEACON ordering when a seed is given:
    h' = SHA256(seed_hex_lowercase + '||' + ASCII objid), same mod 2^32 and objid tie-break. The seed is the beacon value of §3b."""
    if seed_hex is not None:
        seed_hex = seed_hex.lower()
        return sorted(rows, key=lambda r: (int.from_bytes(hashlib.sha256((seed_hex + '||' + str(r['objid'])).encode('ascii')).digest(), 'big') % (2**32), r['objid']))
    return sorted(rows,key=lambda r:(int.from_bytes(hashlib.sha256(str(r['objid']).encode('ascii')).digest(),'big')%(2**32),r['objid']))
def resolve_brick(ra,dec,bricks):
    hit=np.flatnonzero((bricks['ra1']<=ra)&(ra<bricks['ra2'])&(bricks['dec1']<=dec)&(dec<bricks['dec2']))
    return None if len(hit)!=1 else str(bricks['name'][hit[0]])
def classify(rows,bricks,no_r,start_rank=1,counts=(400,200,2000)):
    selected=[[] for _ in counts]; skipped=[]; stage=0; last=0
    for rank,r in enumerate(rows,start_rank):
        if stage==len(counts): break
        last=rank; brick=resolve_brick(r['ra'],r['dec'],bricks)
        if brick is None or brick in no_r:
            skipped.append({'rank':rank,'objid':r['objid'],'reason':'NO_DR9N_BRICK' if brick is None else 'NO_PUBLISHED_R_COVERAGE','brick':brick})
            continue
        q=dict(r); q.update(rank=rank,brick=brick); selected[stage].append(q)
        if len(selected[stage])==counts[stage]: stage+=1
    if stage!=len(counts): raise RuntimeError('insufficient renderable objects')
    return selected,skipped,last
def load_bricks(path):
    with fits.open(path,memmap=False) as h:
        d=h[1].data
        return {'name':np.asarray(d['brickname']).astype(str),'ra1':np.asarray(d['ra1'],dtype=np.float64),'ra2':np.asarray(d['ra2'],dtype=np.float64),'dec1':np.asarray(d['dec1'],dtype=np.float64),'dec2':np.asarray(d['dec2'],dtype=np.float64)}
def _refuse(token, detail):
    raise SystemExit(f'{token}: {detail}')

def _validate_beacon_record(path, rule_sha256, signature_statement, fetch=None, now=None):
    """ONE verdict, shared with the fetcher: beacon_v2.beacon_record.verdict recomputes every acceptance condition from the record's
    EVIDENCE BYTES (there are no stored results to trust) and, with `fetch`, re-fetches every public input live and requires equality.
    A production build uses the real network; tests inject a mocked network. Returns (record dict, raw bytes, verdict)."""
    raw=Path(path).read_bytes()
    try: B=json.loads(raw)
    except (ValueError, TypeError) as e: _refuse('BEACON-RECORD-INVALID-JSON', str(e))
    if not re.fullmatch(r'[0-9A-Fa-f]{64}',str(rule_sha256 or '')): _refuse('RULE-DIGEST-INVALID','--rule-sha256 must be 64 hex')
    stmt=Path(signature_statement).read_bytes()
    from datetime import datetime as _dt, timezone as _tz
    now=now or _dt.now(_tz.utc)
    if fetch is None:
        import urllib.request
        def fetch(url, timeout=30):
            with urllib.request.urlopen(url, timeout=timeout) as r: return r.read()
    r=beacon_record.verdict(B, now, nist_pulse.pinned_roots(), fetch=fetch, rule_sha256=rule_sha256, statement_bytes=stmt)
    if not str(r['outcome']).startswith('ACCEPT'): _refuse('BEACON-NOT-ACCEPTED', f"verdict {r['outcome']}: {r.get('why','')}")
    return B, raw, r

def build(check_control=True, out_dir=None, seed_hex=None, exclude_path=None, beacon_record_path=None, test_seed=False, rule_sha256=None, signature_statement=None, fetch=None, now=None):
    beacon_sha=None; verdict=None
    if beacon_record_path is not None:
        if rule_sha256 is None or signature_statement is None: _refuse('BEACON-VALIDATION-ARGS-MISSING','--rule-sha256 and --signature-statement are required with --beacon-record')
        B,braw,verdict=_validate_beacon_record(beacon_record_path, rule_sha256, signature_statement, fetch=fetch, now=now)
        beacon_sha=hashlib.sha256(braw).hexdigest(); seed_hex=verdict['seed_hex']
    elif seed_hex is not None and not test_seed: raise SystemExit('SEED-WITHOUT-BEACON-RECORD: a bare --seed-hex is only allowed with --test-seed (never for production)')
    OUT=Path(out_dir) if out_dir else HERE; OUT.mkdir(parents=True, exist_ok=True)
    start=time.perf_counter(); pool_path=HERE/'guarded_pool.csv'
    with open(pool_path,newline='') as f: rows=[{'objid':int(r['GZ1_OBJID']),'ra':float(r['RA']),'dec':float(r['DEC']),'g':int(r['G'])} for r in csv.DictReader(f)]
    ordered=order_rows(rows)
    # CONTROL (§9B.5): the 2,000 smallest h mod 2^32 of the guarded pool must be EXACTLY the failed set, with the same labels.
    # The selection CSV is written in GZ1_OBJID order (the first step of §9B.5), not in rank order, so the control is set equality
    # plus per-object label equality — Hwao's build brief of 23:0x wrongly asked for row-order equality; codex correctly stopped on it.
    with open(ROOT/'VALIDATION_SELECTION_V29_20260905.csv',newline='') as f: exp_rows={int(r['GZ1_OBJID']):int(float(r['G'])) for r in csv.DictReader(f)}
    act_rows={r['objid']:int(float(r['g'])) for r in ordered[:2000]}
    if check_control and (set(act_rows)!=set(exp_rows) or any(act_rows[o]!=exp_rows[o] for o in act_rows)):
        print('CONTROL FAILURE: ranks 1-2000 as a set differ from VALIDATION_SELECTION_V29 (missing %d, extra %d, label disagreements %d)'%(len(set(exp_rows)-set(act_rows)),len(set(act_rows)-set(exp_rows)),sum(1 for o in act_rows if o in exp_rows and act_rows[o]!=exp_rows[o]))); return False
    print('validation ranks 1-2000 match the failed set as a set with equal labels: 2000')
    bricks=load_bricks(ROOT/'scratch/survey-bricks-dr9-north.fits.gz')
    with open(ROOT/'validation_bricks/_bricks_without_r_coverage.txt') as _f: no_r={x.strip() for x in _f if x.strip()}
    if seed_hex is None:
        population=ordered[2000:]; start=2001; mode='deterministic-ranks-2001-up (DRY RUN ONLY; not the rule)'
    else:
        # BEACON SPLIT (§3b): population = guarded pool MINUS the failed set (ranks 1-2000 of the unseeded order) MINUS the
        # excluded identities (the dry-run outputs of 2026-09-05, archived), re-ordered by the seeded hash; ranks restart at 1.
        failed={r['objid'] for r in ordered[:2000]}
        excluded=set()
        if exclude_path is not None:
            excluded={int(x) for x in Path(exclude_path).read_text().split() if x.strip()}
        population=order_rows([r for r in rows if r['objid'] not in failed and r['objid'] not in excluded], seed_hex); start=1
        mode=('beacon-seeded (SHA256(seed||objid) mod 2^32), failed set and dry-run identities excluded' if beacon_record_path is not None else 'TEST-SEED (not for production): seeded ordering with a caller-supplied seed')
    groups,skipped,last=classify(population,bricks,no_r,start_rank=start)
    names=('tuning','holdout','fresh_validation')
    lists={n:{'objids':[r['objid'] for r in g],'bricks':[r['brick'] for r in g],'count':len(g),'objids_sha256':digest_objids(g)} for n,g in zip(names,groups)}
    raw=pool_path.read_bytes()
    def fsha(p):
        h=hashlib.sha256()
        with open(p,'rb') as fh:
            for c in iter(lambda: fh.read(1<<20), b''): h.update(c)
        return h.hexdigest()
    # SCHEMA CONSUMED BY THE DRIVER (run_configurations.load_identity): top-level ordered lists tuning_objids / holdout_objids /
    # fresh_validation_objids. The nested per-set detail (bricks, digests) is kept under 'detail'. Codex, V6 gate: the previous
    # nested-only schema could not be read by the driver and the driver fixture had masked it with a hand-built identity.
    identity={'schema_version':'CORPUS-IDENTITY-2','pool_sha256':hashlib.sha256(raw).hexdigest(),
      'ordering_rule':ORDERING_RULE,'split_mode':mode,'seed_hex':seed_hex,'excluded_count':(len(excluded) if seed_hex is not None else 0),'exclude_file_sha256':(fsha(exclude_path) if (seed_hex is not None and exclude_path) else None),'population_count':len(population),'beacon_record_sha256':beacon_sha,'beacon_outcome':(verdict['outcome'] if verdict else None),'beacon_source':(verdict.get('source') if verdict else None),'rule_sha256':rule_sha256,'signature_statement_sha256':(hashlib.sha256(Path(signature_statement).read_bytes()).hexdigest() if signature_statement else None),'T_sign':(B['T_sign'] if beacon_record_path is not None else None),'T_pulse':(B['T_pulse'] if beacon_record_path is not None else None),'source':(verdict.get('source') if verdict else None),'validation_control_count':2000,'validation_control_pass':True,
      'tuning_objids':lists['tuning']['objids'],'holdout_objids':lists['holdout']['objids'],'fresh_validation_objids':lists['fresh_validation']['objids'],
      'renderability_inputs':{'survey_bricks_dr9_north_sha256':fsha(ROOT/'scratch/survey-bricks-dr9-north.fits.gz'),'bricks_without_r_coverage_sha256':fsha(ROOT/'validation_bricks/_bricks_without_r_coverage.txt'),
                              'rule':'brick exists in the pinned DR9-north survey-bricks table (half-open RA1<=RA<RA2, DEC1<=DEC<DEC2) AND brick not in the pinned no-r registry; the sealed checksum catalogue is NOT consulted here'},
      'detail':lists,
      'skipped_non_renderable':skipped,'skipped_non_renderable_count':len(skipped),'last_rank_consumed':last,'pool_remaining_unused':len(ordered)-last}
    with open(OUT/'corpus_identity.json','w') as f: json.dump(identity,f,sort_keys=True,separators=(',',':')); f.write('\n')
    def manifest(path,group,validation=False):
        with open(OUT/path,'w',newline='') as f:
            if validation:
                w=csv.writer(f,lineterminator='\n'); w.writerow(['GZ1_OBJID','RA','DEC','G','DR9N_BRICK']); w.writerows((r['objid'],r['ra'],r['dec'],r['g'],r['brick']) for r in group)
            else:
                w=csv.writer(f,lineterminator='\n'); w.writerow(['objid','g','tensor_sha256']); w.writerows((r['objid'],r['g'],'') for r in group)
    manifest('tuning_manifest_template.csv',groups[0]); manifest('holdout_manifest_template.csv',groups[1]); manifest('fresh_validation_selection.csv',groups[2],True)
    receipt={'schema_version':'CORPUS-IDENTITY-RECEIPT-1','validation_control_expected':2000,'validation_control_matched':2000,
      'counts':{n:len(g) for n,g in zip(names,groups)},'skipped_non_renderable_count':len(skipped),'last_rank_consumed':last,
      'pool_remaining_unused':len(ordered)-last,'runtime_seconds':time.perf_counter()-start}
    with open(OUT/'corpus_identity_receipt.json','w') as f: json.dump(receipt,f,sort_keys=True,separators=(',',':')); f.write('\n')
    return True
if __name__=='__main__':
    import argparse; ap=argparse.ArgumentParser(); ap.add_argument('--seed-hex',default=None,help='test seed; requires --test-seed'); ap.add_argument('--exclude',default=None,help='file of objids to exclude (the archived dry-run identities)'); ap.add_argument('--out',default=None); ap.add_argument('--beacon-record',default=None,help='beacon_record.json from fetch_beacon.py (production seed source)'); ap.add_argument('--rule-sha256',default=None); ap.add_argument('--signature-statement',default=None); ap.add_argument('--test-seed',action='store_true',help='allow a bare --seed-hex (tests only; split_mode marks it)'); a=ap.parse_args()
    sys.exit(0 if build(seed_hex=a.seed_hex, exclude_path=a.exclude, out_dir=a.out, beacon_record_path=a.beacon_record, test_seed=a.test_seed, rule_sha256=a.rule_sha256, signature_statement=a.signature_statement) else 1)
