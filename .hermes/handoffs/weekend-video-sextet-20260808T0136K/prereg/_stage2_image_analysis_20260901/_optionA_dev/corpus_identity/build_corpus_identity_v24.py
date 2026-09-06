#!/usr/bin/env python3
"""V24 STAGED CANDIDATE (NOT GATED, NOT ADOPTED): V23 + (codex V23 M2) the build RECONCILES a pending history entry with the remote before any operation (provenance_designs_v4.reconcile_pending). V23 text follows.
Build the ordered, catalogue-only corpus identity and CSV templates. V20 VARIANT (DRAND-ONLY): build_corpus_identity.py + beacon_record_drand (the ONE verdict: BLS-verified, chain-bound, no NIST, no fallback) + approval_witness_v3
(server-side push time, nonce at T_sign) + the COLLECTION LOG LOCK (the first ACCEPT is binding; every attempt retained; codex V17 [MAJOR] source-decision) + the
ADOPTION BINDING (the approved rule digest is read from a committed file, never only from the command line; codex V16/V17 [MAJOR carried])."""
import csv, hashlib, json, re, subprocess, sys, time, urllib.error
from datetime import timedelta
from pathlib import Path
import numpy as np
from astropy.io import fits

HERE=Path(__file__).resolve().parent; ROOT=HERE.parent.parent
sys.path.insert(0, str(HERE.parent/'beacon_v2')); sys.path.insert(0, str(HERE.parent/'drand_only'))
import beacon_record_drand_v24 as beacon_record, verify_drand_v2 as verify_drand, history_v2 as H   # option A V21: drand-only verdict (BLS verified under the pinned key) + the APPROVAL WITNESS below
sys.path.insert(0, str(HERE)); import approval_witness_v4 as approval_witness
WITNESS_REMOTE_REF="origin/feat/paper-workflow-v2"; WITNESS_REMOTE_URL="https://github.com/DuhoKim/NebulaMind.git"; APPROVAL_GLOB="APPROVAL_RECORD_SELRULE_V22*"; WITNESS_FETCH=True; BRANCH_REF="refs/heads/feat/paper-workflow-v2"   # tests override
EVENTS=approval_witness.github_events                       # tests inject a feed; returns (events, provenance)
ADOPTION_FILE=HERE.parent/'ADOPTED_RULE_SHA256.txt'         # committed at approval: exactly one 64-hex line = the approved rule digest
COLLECTION_LOG=HERE.parent/'collection_log.jsonl'           # the AUTHENTICATED history (history_v2): genesis first, hash-chained, first ACCEPT locked atomically
PUBLISH_REMOTE=None; PUBLISH_REF=None                        # v23 producer boundary: when set, every appended entry is committed+pushed+acknowledged before anything else proceeds
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
    """ONE verdict shared with the collector (beacon_record_drand_v21.verdict) + approval_witness_v4 + the AUTHENTICATED HISTORY: the history
    must already hold the collector's GENESIS for THIS approval record (digest), T_pulse, rule and round; every attempt — pre-parse failure,
    verdict, witness refusal (with its PENDING/CLOSED state), adoption refusal, conflict, any other exception — is a chained entry; the
    first ACCEPT is taken atomically under the history lock. Returns (record dict, raw bytes, verdict)."""
    try:
        return _validate_inner(path, rule_sha256, signature_statement, fetch, now)
    except SystemExit: raise
    except BaseException as e:                                                    # V21 (M2): EVERY other path reaches the history, then refuses
        _log_attempt({'stage':'builder-error','error':repr(e)[:160]}); _refuse('BUILDER-ERROR', repr(e)[:120])

def _reconcile():
    """v24 (codex V23 M2): before any operation, a single pending entry is published or the build refuses (PUBLISH-BATCH / PENDING-PUSH)."""
    if not (PUBLISH_REMOTE and PUBLISH_REF): return
    sys.path.insert(0, str(HERE.parent/'track2')); import provenance_designs_v4 as P
    root=subprocess.run(['git','rev-parse','--show-toplevel'],cwd=COLLECTION_LOG.parent,capture_output=True,text=True).stdout.strip()
    P.reconcile_pending(root, Path(COLLECTION_LOG).resolve().relative_to(Path(root).resolve()).as_posix(), PUBLISH_REMOTE, PUBLISH_REF)

def _validate_inner(path, rule_sha256, signature_statement, fetch, now):
    _reconcile()
    try:
        raw=Path(path).read_bytes(); B=json.loads(raw)
        if not re.fullmatch(r'[0-9A-Fa-f]{64}',str(rule_sha256 or '')): raise ValueError('--rule-sha256 must be 64 hex')
        stmt=Path(signature_statement).read_bytes()
    except Exception as e:                                                        # pre-parse failures are logged, then refused
        _log_attempt({'stage':'builder-pre-parse-refusal','record':Path(path).name,'error':repr(e)[:160]}); _refuse('BEACON-RECORD-INVALID', repr(e)[:120])
    from datetime import datetime as _dt, timezone as _tz
    now=now or _dt.now(_tz.utc)
    if fetch is None:
        import urllib.request
        def fetch(url, timeout=30):
            with urllib.request.urlopen(url, timeout=timeout) as r: return r.read()
    import hashlib as _h; d=_h.sha256(raw).hexdigest(); sd=_h.sha256(stmt).hexdigest()
    g=_genesis_or_refuse(sd, B, rule_sha256)
    r=beacon_record.verdict(B, now, fetch=fetch, rule_sha256=rule_sha256, statement_bytes=stmt)
    _log_attempt({'stage':'builder-verdict','record':Path(path).name,'record_sha256':d,'outcome':r['outcome'],'source':r.get('source'),'seed_hex':r.get('seed_hex'),'why':r.get('why')})
    if not str(r['outcome']).startswith('ACCEPT'): _refuse('BEACON-NOT-ACCEPTED', f"verdict {r['outcome']}: {r.get('why','')}")
    t_pulse=beacon_record.parse_utc(B['T_pulse']); t_sign=beacon_record.parse_utc(B['T_sign']); seed_round=verify_drand.round_for(t_pulse)
    try:
        events,prov=EVENTS()
        r['approval_witness']=approval_witness.verify(signature_statement, t_sign, t_pulse, seed_round, rule_sha256, fetch, WITNESS_REMOTE_REF, WITNESS_REMOTE_URL, beacon_record.MIN_T_SIGN, APPROVAL_GLOB, events, BRANCH_REF, do_fetch=WITNESS_FETCH, provenance=prov, now=now)
        _adoption_binding(rule_sha256, r['approval_witness']['commit'])
    except SystemExit as e:
        state=getattr(e,'state',None)
        _log_attempt({'stage':('witness-pending' if state=='PENDING' else 'witness-closed' if state=='CLOSED' else 'builder-witness-or-adoption'),'record_sha256':d,'outcome':r['outcome'],'refusal':str(e),'state':state}); raise
    _collection_lock(Path(path), raw, r)
    r['t_pulse']=B['T_pulse']
    return B, raw, r

def _genesis_or_refuse(statement_sha256, B, rule_sha256):
    """The history must exist and its GENESIS must name THIS approval record, T_pulse, rule and round (the collector wrote it; the builder never initiates)."""
    try: entries=H.validate(COLLECTION_LOG)
    except ValueError as e: _log_side({'stage':'builder-history-refusal','error':str(e)}); _refuse('HISTORY-INVALID', str(e))
    g=entries[0]
    if (g.get('approval_record_sha256'),g.get('t_pulse'),g.get('rule_sha256'),g.get('round'))!=(statement_sha256,B.get('T_pulse'),rule_sha256,B.get('round')):
        _log_attempt({'stage':'builder-witness-or-adoption','refusal':'HISTORY-GENESIS-MISMATCH'}); _refuse('HISTORY-GENESIS-MISMATCH', 'the history was initiated for a different approval record / T_pulse / rule / round')
    return g

def _log_side(entry):
    """A failure that cannot enter the chain (no valid history) is disclosed beside it, never silently dropped."""
    entry={'utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()), **entry}
    with open(str(COLLECTION_LOG)+'.pregenesis.jsonl','a') as f: f.write(json.dumps(entry,sort_keys=True)+'\n')

def _publish(message):
    """v23 producer boundary: publish exactly the one new entry and require the remote's acknowledgment (SystemExit PENDING-PUSH / PUBLISH-BATCH otherwise)."""
    if not (PUBLISH_REMOTE and PUBLISH_REF): return
    sys.path.insert(0, str(HERE.parent/'track2')); import provenance_designs_v4 as P
    root=subprocess.run(['git','rev-parse','--show-toplevel'],cwd=COLLECTION_LOG.parent,capture_output=True,text=True).stdout.strip()
    P.publish_entry(root, Path(COLLECTION_LOG).resolve().relative_to(Path(root).resolve()).as_posix(), PUBLISH_REMOTE, PUBLISH_REF, message)
def _log_attempt(entry):
    """Hash-chained append (history_v2.append: validates the chain under the lock, then appends), then PUBLISHED if configured. If the history is not valid the entry goes beside it."""
    try: H.append(COLLECTION_LOG, entry)
    except (ValueError, SystemExit, OSError) as e: _log_side({**entry,'history_error':repr(e)[:120]}); return
    _publish('history: '+str(entry.get('stage')))

def _adoption_binding(rule_sha256, approval_commit):
    """V19: the approved rule digest is a COMMITTED file at the APPROVAL COMMIT (a blob there, byte-equal to disk), exactly one 64-hex
    line and nothing else (no blank lines); the command-line digest must equal it; absent → refuse (fail closed). codex V18 item 4."""
    import subprocess
    p=ADOPTION_FILE
    if not p.is_file(): _refuse('ADOPTION-MISSING', f'{p.name} absent — no approved rule digest is bound')
    raw=p.read_bytes(); lines=raw.decode('utf-8','replace').split('\n')
    if not (len(lines)==2 and lines[1]=='' and re.fullmatch(r'[0-9a-f]{64}', lines[0])): _refuse('ADOPTION-MALFORMED', f'{p.name} must be exactly one 64-hex line followed by one newline')
    if lines[0]!=rule_sha256: _refuse('ADOPTION-MISMATCH', f'--rule-sha256 {rule_sha256[:12]}… != adopted {lines[0][:12]}…')
    root=subprocess.run(['git','rev-parse','--show-toplevel'],cwd=p.parent,capture_output=True,text=True)
    if root.returncode!=0: _refuse('ADOPTION-NOT-IN-REPO', 'adoption file is not inside a git worktree')
    rel=p.resolve().relative_to(Path(root.stdout.strip()).resolve()).as_posix()
    blob=subprocess.run(['git','cat-file','-p',f'{approval_commit}:{rel}'],cwd=root.stdout.strip(),capture_output=True)
    if blob.returncode!=0 or blob.stdout!=raw: _refuse('ADOPTION-NOT-AT-APPROVAL-COMMIT', f'{rel} is not a byte-equal blob at the witnessed approval commit {approval_commit[:12]}')

def _collection_lock(record_path, raw, verdict):
    """V21 ATOMIC first accept: under the history lock, re-read the chain; if a builder-accept exists it must name this record, outcome and
    seed (idempotent replay) else a builder-conflict entry is appended and the build refused; if none exists, the builder-accept is appended
    before the lock is released — two racing builders cannot both be first. Semantic conflicts (any later accept-bearing entry naming a
    different record or seed) are detected by history.first_accept and refused."""
    import hashlib as _h; d=_h.sha256(raw).hexdigest(); state={}
    def decide(entries):
        acc=[e for e in entries if e.get('stage')=='builder-accept']
        if acc and (acc[0]['record_sha256']!=d or acc[0]['outcome']!=verdict['outcome'] or acc[0].get('seed_hex')!=verdict.get('seed_hex')):
            state['conflict']=acc[0]; return {'stage':'builder-conflict','record':record_path.name,'record_sha256':d,'outcome':verdict['outcome'],'seed_hex':verdict.get('seed_hex'),'first_accept_utc':acc[0]['utc']}
        if acc: state['first']=acc[0]; return None
        return {'stage':'builder-accept','record':record_path.name,'record_sha256':d,'outcome':verdict['outcome'],'source':verdict.get('source'),'seed_hex':verdict.get('seed_hex')}
    e=H.append_locked(COLLECTION_LOG, decide)
    if e is not None: _publish('history: '+e['stage'])
    if 'conflict' in state: _refuse('COLLECTION-LOCKED', f"first ACCEPT already logged at {state['conflict']['utc']} ({state['conflict']['outcome']}, record {state['conflict']['record_sha256'][:12]}…); this build names a different one")
    entries=H.validate(COLLECTION_LOG); fa,conf=H.first_accept(entries)
    if conf: _refuse('COLLECTION-CONFLICT', f'{len(conf)} later accept-bearing entries name a different record or seed')
    verdict['collection_lock']={'log':COLLECTION_LOG.name,'first_accept':fa,'log_sha256':_h.sha256(COLLECTION_LOG.read_bytes()).hexdigest(),'entries':len(entries),'genesis_sha256_of_line':None}

def build(check_control=True, out_dir=None, seed_hex=None, exclude_path=None, beacon_record_path=None, test_seed=False, rule_sha256=None, signature_statement=None, fetch=None, now=None):
    beacon_sha=None; verdict=None
    if beacon_record_path is not None:
        if rule_sha256 is None or signature_statement is None:
            _log_side({'stage':'builder-args-refusal','record':str(beacon_record_path),'refusal':'BEACON-VALIDATION-ARGS-MISSING'})          # V22 (C4): disclosed, then refused
            _refuse('BEACON-VALIDATION-ARGS-MISSING','--rule-sha256 and --signature-statement are required with --beacon-record')
        B,braw,verdict=_validate_beacon_record(beacon_record_path, rule_sha256, signature_statement, fetch=fetch, now=now)
        beacon_sha=hashlib.sha256(braw).hexdigest(); seed_hex=verdict['seed_hex']
    elif seed_hex is not None and not test_seed: raise SystemExit('SEED-WITHOUT-BEACON-RECORD: a bare --seed-hex is only allowed with --test-seed (never for production)')
    try:
        return _build_outputs(check_control, out_dir, seed_hex, exclude_path, beacon_record_path, rule_sha256, signature_statement, beacon_sha, verdict, B if beacon_record_path is not None else None)
    except SystemExit: raise
    except BaseException as e:                                                    # V22 (C4): catalogue / control / classification / output failures are logged, then refused
        if beacon_record_path is not None: _log_attempt({'stage':'builder-error','record_sha256':beacon_sha,'error':repr(e)[:160]})
        _refuse('BUILDER-ERROR', repr(e)[:120])

def _build_outputs(check_control, out_dir, seed_hex, exclude_path, beacon_record_path, rule_sha256, signature_statement, beacon_sha, verdict, B):
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
        if beacon_record_path is not None: _log_attempt({'stage':'builder-control-refusal','record_sha256':beacon_sha,'missing':len(set(exp_rows)-set(act_rows)),'extra':len(set(act_rows)-set(exp_rows))})   # v23 (codex V22 D)
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
      'ordering_rule':ORDERING_RULE,'split_mode':mode,'seed_hex':seed_hex,'excluded_count':(len(excluded) if seed_hex is not None else 0),'exclude_file_sha256':(fsha(exclude_path) if (seed_hex is not None and exclude_path) else None),'population_count':len(population),'beacon_record_sha256':beacon_sha,'approval_witness':(verdict.get('approval_witness') if beacon_record_path is not None else None),'collection_lock':(verdict.get('collection_lock') if beacon_record_path is not None else None),'beacon_t_pulse':(verdict.get('t_pulse') if beacon_record_path is not None else None),'adoption_sha256':(fsha(ADOPTION_FILE) if beacon_record_path is not None else None),'beacon_outcome':(verdict['outcome'] if verdict else None),'beacon_source':(verdict.get('source') if verdict else None),'beacon_round':(verdict.get('round') if verdict else None),'beacon_source':(verdict.get('source') if verdict else None),'rule_sha256':rule_sha256,'signature_statement_sha256':(hashlib.sha256(Path(signature_statement).read_bytes()).hexdigest() if signature_statement else None),'T_sign':(B['T_sign'] if beacon_record_path is not None else None),'T_pulse':(B['T_pulse'] if beacon_record_path is not None else None),'source':(verdict.get('source') if verdict else None),'validation_control_count':2000,'validation_control_pass':True,
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
    import argparse; ap=argparse.ArgumentParser(); ap.add_argument('--seed-hex',default=None,help='test seed; requires --test-seed'); ap.add_argument('--exclude',default=None,help='file of objids to exclude (the archived dry-run identities)'); ap.add_argument('--out',default=None); ap.add_argument('--beacon-record',default=None,help='beacon_record.json from fetch_beacon.py (production seed source)'); ap.add_argument('--rule-sha256',default=None); ap.add_argument('--signature-statement',default=None); ap.add_argument('--test-seed',action='store_true',help='allow a bare --seed-hex (tests only; split_mode marks it)'); ap.add_argument('--publish-remote',default=None); ap.add_argument('--publish-ref',default=None); a=ap.parse_args(); PUBLISH_REMOTE=a.publish_remote; PUBLISH_REF=a.publish_ref
    sys.exit(0 if build(seed_hex=a.seed_hex, exclude_path=a.exclude, out_dir=a.out, beacon_record_path=a.beacon_record, test_seed=a.test_seed, rule_sha256=a.rule_sha256, signature_statement=a.signature_statement) else 1)
