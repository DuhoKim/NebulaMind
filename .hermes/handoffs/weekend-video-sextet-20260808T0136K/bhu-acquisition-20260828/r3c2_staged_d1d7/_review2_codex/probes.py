import pathlib,json,subprocess,hashlib,copy
W=pathlib.Path(__file__).resolve().parent; T=W.parent/'r3c2_ledger_tools_STAGED.py'; B=W.parent/'r3c2_batch_tools_STAGED.py'
def wr(p,x):
 p=pathlib.Path(p); p.write_text(x if isinstance(x,str) else json.dumps(x,indent=2)); return p
def run(t,*a):
 r=subprocess.run(['/usr/bin/python3','-E',str(t),*map(str,a)],capture_output=True,text=True); return r.returncode,r.stdout+r.stderr
def c(i): return dict(candidate_id='own.txt#'+str(i),source_file='own.txt',source_line=i,numeral=str(40+i),included=True,attempts=0,outcome='REPRO_NO_DERIVATION_STATED')
def cf(p,cs): return wr(p,dict(declared_candidate_count=len(cs),declared_included_count=sum(bool(c['included']) for c in cs),declared_excluded_count=sum(not c['included'] for c in cs),declared_attempt_count=sum(c.get('attempts',0) for c in cs if c['included']),candidates=cs))
summary=[]
def audit(tag,scs,acs,sxs=[],axs=[],hack=False):
 d=W/tag; d.mkdir(exist_ok=True); wr(d/'own.txt','\n'.join('We report our own result: the dimensionless yield is '+str(40+i)+'.' for i in range(1,22))+'\n')
 sc=cf(d/'sealed_c.json',scs); cf(d/'seatA_c.json',scs); cf(d/'seatB_c.json',copy.deepcopy(scs)); ac=cf(d/'aud_c.json',acs)
 sx=wr(d/'sealed_x.json',dict(declared_exclusion_count=len(sxs),exclusions=sxs)); ax=wr(d/'aud_x.json',dict(declared_exclusion_count=len(axs),exclusions=axs)); sl=wr(d/'sealed_l.json',{'records':[]})
 s1=d/'stage1.txt'; sel=d/'selection.json'; s2=d/'stage2.txt'; red=d/'red.json'; log=[]
 for args in [('seal-enumeration',ac,ax,s1),('select',sc,'1'*64,s1,sel),('handout',sel,sc,d/'handout.json')]:
  rc,out=run(T,'audit',*args); log.append(out); assert rc==0,out
 ids=json.loads(sel.read_text())['audited_ids']; wr(red,{i:{'outcome':'REPRO_NO_DERIVATION_STATED','inputs':{}} for i in ids}); log.append(run(T,'audit','seal-rederivation',red,s2)[1])
 if hack:
  s=json.loads(sel.read_text()); s.pop('seed_hex'); s['audited_ids']=[]; s['sampled_ids']=[]; s['k']=0; wr(sel,s)
 rc,out=run(T,'audit','compare',s1,ac,ax,sc,sx,sl,sel,s2,red,d/'C6_AUDIT.json'); log.append(out); wr(d/'commands_output.txt','\n'.join(log))
 j=json.loads((d/'C6_AUDIT.json').read_text()); summary.append([tag,rc,j['completeness_rows'],j['inclusion_disputed_count'],j['C6_AUDIT_SAMPLE']]); return d
base=[c(1),c(2)]
audit('both_omit',[c(1)],base); audit('reverse',base,[c(1)]); audit('missing_seed_skips_selection',base,base,hack=True)
for n in (2,3):
 scs=[c(i) for i in range(1,21)]; acs=copy.deepcopy(scs); axs=[]
 for a in acs[:n]:
  a['included']=False; axs.append(dict(candidate_id=a['candidate_id'],source_file=a['source_file'],source_line=a['source_line'],numeral=a['numeral'],kind='ATTRIBUTED_NOT_DERIVED'))
 audit('dispute_'+str(n)+'_of_20',scs,acs,axs=axs)
x=c(3); x['included']=False; xe={k:x[k] for k in ('candidate_id','source_file','source_line','numeral')}; xe['kind']='DATE'
audit('audit_excluded_only',base,base+[x],axs=[xe]); audit('sealed_excluded_only',base+[x],base,sxs=[xe]); audit('kind_difference',base+[x],base+[x],sxs=[xe],axs=[dict(xe,kind='REFERENCE_NUMBER')])
D=W/'d1'; D.mkdir(exist_ok=True); wr(D/'borrow.txt','We take a from source.txt.\nWe report our own result y = 82.\n'); cand=cf(D/'c.json',[dict(c(2),candidate_id='borrow.txt#2',source_file='borrow.txt')])
r=dict(claim_id='borrow.txt#2',input_id='borrow.txt#i',symbol='a',status='PRINTED',origin='IMPORTED',origin_evidence=dict(reason_code='ORIG_CITATION',source_file='borrow.txt',source_line=1,verbatim='We take a from source.txt.'),derived_from=[],value='41',source_file='source.txt',source_line=1)
def manifest():
 wr(D/'R3C2_CORPUS_MANIFEST.md','\n'.join('| %d | `%s` | `%s` | %d | 2 |'%(i,f,hashlib.sha256((D/f).read_bytes()).hexdigest(),(D/f).stat().st_size) for i,f in enumerate(['borrow.txt','source.txt'],1)))
def val(tag,rr):
 p=wr(D/(tag+'.json'),{'records':[rr]}); rc,out=run(T,'validate',p,D,cand); wr(D/(tag+'.txt'),out); summary.append([tag,rc,out.strip()])
for verb in ('choose','fit','measure','adopt from X'):
 wr(D/'source.txt','We '+verb+' a = 41.\nAgain a = 41.\n'); manifest(); val(verb.replace(' ','_'),r)
val('second_line',dict(r,source_line=2))
wr(D/'source.txt','We choose b = 41.\n'); manifest(); val('no_symbol',r)
wr(D/'source.txt','We choose a = 41.\n'); manifest(); rr=copy.deepcopy(r); rr['origin']='CHOSEN'; rr['origin_evidence']=dict(reason_code='ORIG_CHOICE_STATED',source_file='source.txt',source_line=1,verbatim='We choose a = 41.'); val('import_refiled_CHOSEN',rr)
# Batch fixtures written here, independent of kit controls.
Q=W/'batch'; Q.mkdir(exist_ok=True); wr(Q/'p.txt','one\n'); wr(Q/'q.txt','two\n'); mf=wr(Q/'manifest.md','\n'.join('| %d | `%s` | `%s` | 4 | 1 |'%(i,f,hashlib.sha256((Q/f).read_bytes()).hexdigest()) for i,f in enumerate(['p.txt','q.txt'],1))); part=Q/'part.json'; run(B,'partition',mf,2,part)
for k,f in enumerate(['p.txt','q.txt'],1):
 cf(Q/('candidates_b%d.json'%k),[dict(c(1),candidate_id=f+'#1',source_file=f)]); wr(Q/('exclusions_b%d.json'%k),dict(declared_exclusion_count=0,exclusions=[])); rr=copy.deepcopy(r); rr.update(claim_id=f+'#MISSING',input_id='nonglobal'+str(k),source_file=f); rr['origin_evidence']['source_file']=f; wr(Q/('ledger_b%d.json'%k),dict(records=[rr])); wr(Q/('SEAT_REPORT_b%d.md'%k),'ACCESS_SHA='+'a'*64); run(B,'seal',part,k,Q,Q,Q/'seals.json')
seals=json.loads((Q/'seals.json').read_text()); seals['seals']['2']['predecessor_seal_sha256']='0'*64; wr(Q/'seals_bad_chain.json',seals)
rc,out=run(B,'join',part,Q,Q/'seals_bad_chain.json',mf,str(Q/'joined_')); wr(Q/'join_output.txt',out); summary.append(['batch_bad_chain_nonglobal_orphan',rc,out])
wr(W/'summary.json',summary)
for x in summary: print(json.dumps(x))
