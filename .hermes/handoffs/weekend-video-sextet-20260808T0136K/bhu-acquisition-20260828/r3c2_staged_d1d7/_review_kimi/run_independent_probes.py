import pathlib, tempfile, json, subprocess, hashlib, copy
H=pathlib.Path(__file__).resolve().parent.parent
W=pathlib.Path(tempfile.mkdtemp(prefix='codex_',dir=H/'_review_kimi'))
TOOL=H/'r3c2_ledger_tools_STAGED.py'; BATCH=H/'r3c2_batch_tools_STAGED.py'; PY='/usr/bin/python3'
LOG=[]; RESULTS=[]
def write(p,obj):
 p=pathlib.Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(obj if isinstance(obj,str) else json.dumps(obj,indent=2,sort_keys=True)); return p
def run(label,tool,*args):
 cmd=[PY,'-E',str(tool),*map(str,args)]
 r=subprocess.run(cmd,text=True,capture_output=True)
 LOG.append({'label':label,'command':cmd,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
 return r

def candidate(cid,line,num,inc=True):
 c=dict(candidate_id=cid,source_file='results.txt',source_line=line,numeral=str(num),included=inc)
 if inc:c.update(attempts=0,outcome='REPRO_NO_DERIVATION_STATED')
 return c

def cfile(p,cs,bad=False):
 return write(p,dict(declared_candidate_count=len(cs)+(1 if bad else 0),declared_included_count=sum(c['included'] for c in cs),declared_excluded_count=sum(not c['included'] for c in cs),declared_attempt_count=sum(c.get('attempts',0) for c in cs),candidates=cs))
def xfile(p,cs):
 xs=[dict(candidate_id=c['candidate_id'],source_file=c['source_file'],source_line=c['source_line'],numeral=c['numeral'],kind='AUTHOR_SPECIFIED_INPUT') for c in cs if not c['included']]
 return write(p,dict(declared_exclusion_count=len(xs),exclusions=xs))
write(W/'results.txt','We report our own calculated result: the dimensionless yield is 41.\nWe report our own calculated result: the dimensionless yield is 73.\nFor our calculation we set the input q = 9.\n')
base=[candidate('s1',1,41)]; extra=candidate('s2',2,73)

def audit(label,scs,acs,bad=False,select_first=False,tamper=False):
 d=W/label; d.mkdir()
 sa=cfile(d/'seatA.json',scs); sb=cfile(d/'seatB.json',copy.deepcopy(scs))
 assert sa.read_bytes()==sb.read_bytes()
 sc=cfile(d/'sealed.json',scs); sx=xfile(d/'sealed_x.json',scs)
 ac=cfile(d/'auditor.json',[dict(c,candidate_id='a_'+c['candidate_id']) for c in acs],bad); ax=xfile(d/'auditor_x.json',[dict(c,candidate_id='a_'+c['candidate_id']) for c in acs])
 sl=write(d/'inputs.json',{'records':[]}); seal=d/'stage1.txt'; sel=d/'selection.json'
 if select_first:run(label+' select before seal',TOOL,'audit','select',sc,'19'*32,sel)
 run(label+' seal',TOOL,'audit','seal-enumeration',ac,ax,seal)
 if not select_first:run(label+' select',TOOL,'audit','select',sc,'19'*32,sel)
 s=json.loads(sel.read_text())
 if tamper:
  s['audited_ids']=[]; s['sampled_ids']=[]; s['k']=0; write(sel,s)
 by={c['candidate_id']:c for c in scs}
 rd=write(d/'rederive.json',{cid:dict(outcome=by[cid]['outcome'],inputs={},**({k:by[cid][k] for k in ['printed_value','reproduced_value']} if 'printed_value' in by[cid] else {})) for cid in s['audited_ids']})
 r=run(label+' compare',TOOL,'audit','compare',seal,ac,ax,sc,sx,sl,sel,rd,d/'C6_AUDIT.json')
 obj=json.loads((d/'C6_AUDIT.json').read_text())
 RESULTS.append(dict(label=label,exit=r.returncode,token='C6_AUDIT_SAMPLE='+obj['C6_AUDIT_SAMPLE'],completeness=obj['completeness']))
 print(label, 'exit='+str(r.returncode),'C6_AUDIT_SAMPLE='+obj['C6_AUDIT_SAMPLE'])
 if label in ['both_seats_omit','reverse_omission']:
  print(json.dumps(obj['completeness'],sort_keys=True))
 if bad:
  cr=run(label+' census',TOOL,'census',ac,ax)
  print(' auditor census:',cr.stdout.splitlines()[-1])
 return d

audit('both_seats_omit',base,base+[extra])
audit('reverse_omission',base+[extra],base)
audit('valid_baseline',base,base)
audit('invalid_auditor_counts',base,base,bad=True)
audit('selection_before_seal',base,base,select_first=True)
audit('tampered_selection',base,base,tamper=True)
audit('sealed_exclusion_omitted',base+[candidate('s3',3,9,False)],base)
audit('auditor_exclusion_omitted',base,base+[candidate('s3',3,9,False)])
big=[candidate('s'+str(i),i,str(i)) for i in range(1,21)]
for flips in [2,3]:
 acs=copy.deepcopy(big)
 for c in acs[:flips]:c['included']=False; c.pop('outcome'); c.pop('attempts')
 audit('disputes_'+str(flips)+'_of_20',big,acs)
audit('zero_denominator_dispute',[candidate('s1',1,41,False)],base)

# D1: borrower does NOT print the imported value; distinct source lines deliberately share it.
S=W/'d1_sources'; S.mkdir()
write(S/'borrower.txt','We take parameter a from source.txt.\nOur own result is z = a + a = 4.\nAn unrelated sentence.\n')
write(S/'source.txt','For this calculation we choose a = 2.\nFor this calculation we fit a = 2.\nFor this calculation we measure a = 2.\nFor this calculation we adopt a = 2 from X.\nThe unrelated parameter b = 2.\nThe unrelated parameter b = 20.\n')
write(S/'third.txt','No citation is made here.\n')
def manifest(directory,names):
 write(directory/'R3C2_CORPUS_MANIFEST.md','# Synthetic manifest\n| # | file | sha256 | bytes | non-blank lines |\n|---|---|---|---|---|\n'+''.join('| %d | `%s` | `%s` | %d | %d |\n'%(i,n,hashlib.sha256((directory/n).read_bytes()).hexdigest(),len((directory/n).read_bytes()),len((directory/n).read_text().splitlines())) for i,n in enumerate(names,1)))
manifest(S,['borrower.txt','source.txt','third.txt'])
r0=dict(claim_id='borrower_claim',input_id='a',symbol='a',status='PRINTED',origin='IMPORTED',origin_evidence=dict(reason_code='ORIG_CITATION',source_file='borrower.txt',source_line=1,verbatim='We take parameter a from source.txt.'),derived_from=[],value='2',source_file='source.txt',source_line=1)
def val(label,r,directory=S):
 p=write(W/'d1'/str(label+'.json'),{'records':[r]}); out=run(label,TOOL,'validate',p,directory)
 RESULTS.append(dict(label=label,exit=out.returncode,stdout=out.stdout)); print(label,out.stdout.strip().replace('\n',' | '))
for ln,name in enumerate(['choose','fit','measure','adopt','wrong_symbol_same_value','substring_20'],1):
 r=copy.deepcopy(r0);r['source_line']=ln;val('review_wording_'+name,r)
r=copy.deepcopy(r0);r['origin_evidence']=dict(reason_code='ORIG_CITATION',source_file='source.txt',source_line=1,verbatim='For this calculation we choose a = 2.');val('tori_wording_choose',r)
r=copy.deepcopy(r);r['origin']='CHOSEN';r['origin_evidence']['reason_code']='ORIG_CHOICE_STATED';val('borrower_misfiled_CHOSEN',r)
r=copy.deepcopy(r0);r['origin_evidence']=dict(reason_code='ORIG_CITATION',source_file='third.txt',source_line=1,verbatim='No citation is made here.');val('evidence_unrelated_third_paper',r)
r=copy.deepcopy(r0);r['origin_evidence']['verbatim']='';val('empty_citation',r)
no_manifest=W/'d1_no_manifest'; no_manifest.mkdir()
for n in ['borrower.txt','source.txt']:write(no_manifest/n,(S/n).read_text())
val('no_manifest',r0,no_manifest)
raw=W/'d1_raw';raw.mkdir()
for n in ['borrower.txt','source.txt']:write(raw/n,(S/n).read_text())
write(raw/'R3C2_CORPUS_MANIFEST.md','# Manifest\nRAW, not enumerable: `source.txt`\n')
val('raw_mentioned_only',r0,raw)
restricted=W/'batch1_sources';restricted.mkdir()
for n in ['borrower.txt','R3C2_CORPUS_MANIFEST.md']:write(restricted/n,(S/n).read_text())
val('batch_only_sources',r0,restricted)

# Batch seal accepts reverse order; partition argument is unused by seal.
D=W/'batches';D.mkdir()
part=write(D/'partition.json',dict(manifest_sha256='00'*32,n_texts=2,n_batches=2,batches=[dict(batch=1,files=['borrower.txt']),dict(batch=2,files=['source.txt'])]))
for k in [1,2]:
 c=candidate('c1',1,41);c['source_file']='borrower.txt' if k==1 else 'source.txt'
 cfile(D/('candidates_b%d.json'%k),[c]);xfile(D/('exclusions_b%d.json'%k),[c])
 rr=copy.deepcopy(r0);rr['claim_id']='c1';rr['input_id']='i1';rr['derived_from']=['b2_i1'] if k==1 else []
 write(D/('ledger_b%d.json'%k),{'records':[rr]});write(D/('SEAT_REPORT_b%d.md'%k),'ACCESS_SHA='+'ab'*32+'\n')
for k in [2,1]:
 r=run('seal batch '+str(k),BATCH,'seal',part,k,D,D/'seals.json');print('seal batch',k,'exit='+str(r.returncode))
r=run('batch join',BATCH,'join',part,D,D/'seals.json',str(D/'joined_'));print('batch join',r.stdout.splitlines()[-1])
j=json.loads((D/'joined_ledger.json').read_text());print('cross-batch derived_from after join:',j['records'][0]['derived_from'])
write(W/'command_log.json',LOG);write(W/'results.json',RESULTS)
write(H/'_review_kimi'/'latest_probe_dir.txt',str(W)+'\n')
print('PROBE_DIR='+str(W))
