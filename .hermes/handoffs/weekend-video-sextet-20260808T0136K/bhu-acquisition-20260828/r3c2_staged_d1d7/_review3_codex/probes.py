import pathlib, json, subprocess, hashlib, copy, ast, shlex
H=pathlib.Path(__file__).resolve().parents[1]; W=pathlib.Path(__file__).resolve().parent
L=H/'r3c2_ledger_tools_STAGED.py'; B=H/'r3c2_batch_tools_STAGED.py'
def put(p,o):
    p=pathlib.Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(o if isinstance(o,str) else json.dumps(o,sort_keys=True,indent=1)); return p
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
logs=[]; results={}
def run(name,tool,*args):
    cmd=['/usr/bin/python3','-E',str(tool),*map(str,args)]
    r=subprocess.run(cmd,capture_output=True,text=True); out=r.stdout+r.stderr
    logs.append('$ '+shlex.join(cmd)+'\nexit='+str(r.returncode)+'\n'+out)
    short=[s for s in out.splitlines() if s.startswith(('FAIL:','C3_','JOIN=','C6_AUDIT_SAMPLE=','ValueError:','N=','handout:','C1B_'))]
    results[name]={'exit':r.returncode,'output':short,'command':shlex.join(cmd)}
    print(name, r.returncode, ' | '.join(short)); return r
def cand(rows): return dict(declared_candidate_count=len(rows),declared_included_count=sum(bool(c['included']) for c in rows),declared_excluded_count=sum(not c['included'] for c in rows),declared_attempt_count=sum(c.get('attempts',0) for c in rows if c['included']),candidates=rows)
def exc(rows): return dict(declared_exclusion_count=len(rows),exclusions=rows)
def c(f='borrow.txt',i='c',inc=True): return dict(candidate_id=f+'#'+i,source_file=f,source_line=2,numeral='53',included=inc,**(dict(attempts=0,outcome='REPRO_NO_DERIVATION_STATED') if inc else {}))
src=W/'src'; put(src/'borrow.txt','We take q from source, specifically its second line.\nOur result is 53.\n'); put(src/'source.txt','We choose q = 17.\nAgain q = 17.\n')
put(src/'R3C2_CORPUS_MANIFEST.md',''.join('| %d | `%s` | `%s` | %d | 2 |\n'%(i,f,sha(src/f),(src/f).stat().st_size) for i,f in enumerate(['borrow.txt','source.txt'],1)))
cp=put(W/'d1_candidates.json',cand([c()]))
base=dict(claim_id='borrow.txt#c',input_id='borrow.txt#q',symbol='q',status='PRINTED',origin='IMPORTED',origin_evidence=dict(reason_code='ORIG_CITATION',source_file='borrow.txt',source_line=1,verbatim='We take q from source, specifically its second line.'),derived_from=[],value='17',source_file='source.txt',source_line=1)
for name,changes in [('d1_positive',{}),('d1_no_symbol',{'symbol':'zeta'}),('d1_designated_second',{'source_line':2}),('d1_refiled',{'origin':'CHOSEN','origin_evidence':dict(reason_code='ORIG_CHOICE_STATED',source_file='source.txt',source_line=1,verbatim='We choose q = 17.')})]:
    r=copy.deepcopy(base); r.update(changes); p=put(W/(name+'.json'),{'records':[r]}); run(name,L,'validate',p,src,cp)
    if name=='d1_refiled':
        run('d1_refiled_no_candidates',L,'validate',p,src)
        empty=put(W/'empty_candidates.json',cand([])); run('d1_refiled_unbound_claim',L,'validate',p,src,empty)
# Fresh audit enumerations, including a kind-only disagreement.
for name,omit in [('audit',False),('omission',True)]:
    d=W/name; inc=c(); x=c(i='x',inc=False); x['source_line']=1; x['numeral']='2026'
    ac=put(d/'ac.json',cand([inc,x])); sc=put(d/'sc.json',cand([inc] if omit else [inc,x]))
    ax=put(d/'ax.json',exc([dict(x,kind='DATE')])); sx=put(d/'sx.json',exc([] if omit else [dict(x,kind='REFERENCE_NUMBER')]))
    sl=put(d/'sl.json',{'records':[]}); rd=put(d/'rd.json',{'borrow.txt#c':dict(outcome=inc['outcome'],inputs={})})
    s1=d/'s1.txt'; s2=d/'s2.txt'; sel=d/'sel.json'
    run(name+'_seal',L,'audit','seal-enumeration',ac,ax,s1); run(name+'_select',L,'audit','select',sc,'a'*64,s1,sel)
    run(name+'_handout',L,'audit','handout',sel,sc,d/'handout.json'); run(name+'_seal_red',L,'audit','seal-rederivation',rd,s2)
    def compare(tag,selection):
        out=d/(tag+'.json'); run(tag,L,'audit','compare',s1,ac,ax,sc,sx,sl,selection,s2,rd,out)
        if out.exists():
            ob=json.loads(out.read_text()); print(tag,'rows=',[(r['result'],r['sealed_kind'],r['audit_kind']) for r in ob['completeness_rows']],'study_files=',ob['study_files'])
    compare(name+'_compare',sel)
    if not omit:
        ss=json.loads(sel.read_text()); ss.pop('seed_hex'); ss.update(audited_ids=[],sampled_ids=[],k=0); compare('seedless',put(d/'seedless_selection.json',ss))
        ss=json.loads(sel.read_text()); ss['seed_hex']='A'*64; compare('uppercase_seed',put(d/'uppercase_selection.json',ss))
        ss['seed_hex']='g'*64; compare('nonhex_seed',put(d/'nonhex_selection.json',ss))
        run('select_uppercase',L,'audit','select',sc,'A'*64,s1,d/'rejected_selection.json')
# Two independently authored batches and honest seals; mutate only own seal/artefact files.
part=W/'partition.json'; run('partition',B,'partition',src/'R3C2_CORPUS_MANIFEST.md',2,part)
for mode in ['positive','orphan','input_form','chain','ownership','extra','root_chain','collision']:
    d=W/('batch_'+mode); seals=d/'seals.json'
    for k,f in enumerate(['borrow.txt','source.txt'],1):
        cc=c(f); rr=copy.deepcopy(base); rr.update(claim_id=cc['candidate_id'],input_id=f+'#q')
        if mode=='orphan' and k==1: rr['claim_id']='borrow.txt#missing'
        if mode=='input_form' and k==1: rr['input_id']='local_q'
        rows=[cc,copy.deepcopy(cc)] if mode=='collision' and k==1 else [cc]
        put(d/('candidates_b%d.json'%k),cand(rows)); put(d/('exclusions_b%d.json'%k),exc([])); put(d/('ledger_b%d.json'%k),{'records':[rr]}); put(d/('SEAT_REPORT_b%d.md'%k),'ACCESS_SHA='+'d'*64+'\n')
        run(mode+'_seal_'+str(k),B,'seal',part,k,d,src,seals)
    ss=json.loads(seals.read_text())
    if mode=='chain': ss['seals']['2']['predecessor_seal_sha256']='0'*64
    if mode=='ownership': ss['seals']['2']['owned_files']=['borrow.txt']
    if mode=='extra': ss['seals']['3']=copy.deepcopy(ss['seals']['2'])
    if mode=='root_chain':
        ss['seals']['1']['predecessor_seal_sha256']='f'*64
        ss['seals']['2']['predecessor_seal_sha256']=hashlib.sha256(json.dumps(ss['seals']['1'],sort_keys=True).encode()).hexdigest()
    if mode in ['chain','ownership','extra','root_chain']: seals=put(d/'mutated_seals.json',ss)
    run('join_'+mode,B,'join',part,d,seals,src/'R3C2_CORPUS_MANIFEST.md',str(d/'joined_'))
tree=ast.parse((H/'r3c2_staged_tests.py').read_text()); calls=[n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='probe']
print('OWN_AST_PROBE_CALLS='+str(len(calls))); print('ID_COLLISION_PROBE='+str(any(any(isinstance(a,ast.Constant) and a.value=='PROBE:ID_COLLISION' for a in n.args) for n in calls)))
put(W/'commands_output.txt','\n'.join(logs)); put(W/'results.json',results)
