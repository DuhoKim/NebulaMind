exec((__import__('pathlib').Path(__file__).parent/'probes.py').read_text().split('summary=[]')[0])
Q=W/'batch'; orig=json.loads((Q/'seals.json').read_text()); part=Q/'part.json'; mf=Q/'manifest.md'
for label in ['chain_only','id_only','orphan_only']:
 for k,f in enumerate(['p.txt','q.txt'],1):
  rr=json.loads((Q/('ledger_b%d.json'%k)).read_text())['records'][0]; rr['claim_id']=f+('#MISSING' if label=='orphan_only' else '#1'); rr['input_id']=('nonglobal'+str(k)) if label=='id_only' else f+'#i'; wr(Q/('ledger_b%d.json'%k),{'records':[rr]})
 s=copy.deepcopy(orig)
 for k in (1,2):
  for f in s['seals'][str(k)]['artefacts']: s['seals'][str(k)]['artefacts'][f]=hashlib.sha256((Q/f).read_bytes()).hexdigest()
 s['seals']['2']['predecessor_seal_sha256']=hashlib.sha256(json.dumps(s['seals']['1'],sort_keys=True).encode()).hexdigest()
 if label=='chain_only': s['seals']['2']['predecessor_seal_sha256']='0'*64
 sp=wr(Q/(label+'_seals.json'),s); rc,out=run(B,'join',part,Q,sp,mf,str(Q/(label+'_'))); wr(Q/(label+'_output.txt'),out); print(label,rc,out.splitlines()[-1])
