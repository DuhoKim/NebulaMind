#!/usr/bin/env python3
"""Fetch primary arXiv full text discovered after the first Gate-B pass."""
from __future__ import annotations
import hashlib, json, os, re, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlparse
import fitz, requests

PACKET=Path(__file__).resolve().parents[1]
META=PACKET/'sources/metadata'; RAW=PACKET/'sources/raw'; TEXT=PACKET/'sources/text'; LOG=PACKET/'sources/FETCH_LOG.jsonl'
TOKEN=os.getenv('ADS_API_KEY') or os.getenv('ADS_API_TOKEN') or os.getenv('ADS_DEV_KEY')
UA='NebulaMindSourceVerifier/1.0 (read-only research verification; contact: local operator)'
ARXIV=re.compile(r'(?:arXiv:|arXiv\.)?(\d{4}\.\d{4,5})',re.I)
MANUAL={7:'1901.10203',11:'1702.06148',16:'1607.02151',21:'2306.04024'}
last={}; fetches=0

def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def sha(b): return hashlib.sha256(b).hexdigest()
def log(r):
 with LOG.open('a') as f: f.write(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n')
def fetch(url,index,label,purpose,ads=False):
 global fetches
 host=urlparse(url).netloc.lower(); delay=2-(time.monotonic()-last.get(host,0))
 if delay>0: time.sleep(delay)
 h={'User-Agent':UA,'Accept':'application/json,application/pdf,text/html;q=0.8,*/*;q=0.5'}
 if ads:
  if not TOKEN: raise RuntimeError('ADS token missing')
  h['Authorization']='Bearer '+TOKEN
 started=now(); fetches+=1
 try:
  x=requests.get(url,headers=h,timeout=60,allow_redirects=True); last[host]=time.monotonic(); b=x.content
  ct=x.headers.get('content-type','').split(';',1)[0].lower(); ext='.pdf' if 'pdf' in ct or x.url.lower().split('?',1)[0].endswith('.pdf') else '.json' if 'json' in ct else '.html'
  d=sha(b); p=RAW/f'idx{index:02d}_{label}_{d[:12]}{ext}'; p.write_bytes(b)
  r={'utc':started,'method':'GET','host':host,'index':index,'label':label,'purpose':purpose,'requested_url':url,'final_url':x.url,'status':int(x.status_code),'bytes':len(b),'sha256':d,'content_type':ct,'raw_path':p.relative_to(PACKET).as_posix(),'auth':'ADS_CONFIGURED_BOOLEAN_ONLY' if ads else 'NONE','cache_reuse':False}; log(r); return r
 except Exception as e:
  last[host]=time.monotonic(); r={'utc':started,'method':'GET','host':host,'index':index,'label':label,'purpose':purpose,'requested_url':url,'final_url':'','status':0,'bytes':0,'sha256':sha(b''),'content_type':'','raw_path':'','auth':'ADS_CONFIGURED_BOOLEAN_ONLY' if ads else 'NONE','cache_reuse':False,'error':f'{type(e).__name__}: {str(e)[:240]}'}; log(r); return r

def text_pdf(rec,index,label):
 if rec.get('status')!=200 or not rec.get('raw_path'): return {'text_path':'','text_chars':0,'pages':0}
 try:
  b=(PACKET/rec['raw_path']).read_bytes(); doc=fitz.open(stream=b,filetype='pdf'); t='\n\n'.join(str(p.get_text('text')) for p in doc); d=sha(t.encode()); q=TEXT/f'idx{index:02d}_{label}_{d[:12]}.txt'; q.write_text(t); return {'text_path':q.relative_to(PACKET).as_posix(),'text_sha256':d,'text_chars':len(t),'pages':doc.page_count}
 except Exception as e: return {'text_path':'','text_chars':0,'pages':0,'extract_error':f'{type(e).__name__}: {str(e)[:200]}'}

def ids(doc):
 out=[]
 for v in doc.get('identifier',[])+doc.get('doi',[]):
  m=ARXIV.search(str(v))
  if m and m.group(1) not in out: out.append(m.group(1))
 return out

def existing_primary(meta):
 return any(e.get('label') in {'arxiv_pdf','publisher_pdf'} and e.get('text_chars',0)>1000 for e in meta.get('extracts',[]))

def main():
 discovered={}
 for p in sorted(META.glob('index_[0-9][0-9].json')):
  m=json.loads(p.read_text()); idx=int(m['index']); found=[]
  for rec in m.get('records',[]):
   if rec.get('label')!='ads' or rec.get('status')!=200 or not rec.get('raw_path'): continue
   try: obj=json.loads((PACKET/rec['raw_path']).read_text())
   except Exception: continue
   for doc in obj.get('response',{}).get('docs',[]):
    for aid in ids(doc):
     if aid not in found: found.append(aid)
  if idx in MANUAL and MANUAL[idx] not in found: found.insert(0,MANUAL[idx])
  if found: discovered[idx]=found
 results=[]; cache={}
 for idx,aids in sorted(discovered.items()):
  base=json.loads((META/f'index_{idx:02d}.json').read_text())
  if existing_primary(base): continue
  aid=aids[0]
  if aid in cache:
   rec,tm=cache[aid]; rec=dict(rec); rec['cache_reuse']=True
  else:
   rec=fetch(f'https://arxiv.org/pdf/{aid}',idx,'supplemental_arxiv_pdf','primary_full_text_discovered_after_metadata')
   tm=text_pdf(rec,idx,'supplemental_arxiv_pdf'); cache[aid]=(rec,tm)
  out={'schema':'NM_GATE_B_SUPPLEMENTAL_ARXIV_V1','index':idx,'candidate_arxiv_ids':aids,'selected_arxiv_id':aid,'record':rec,'pdf_text':tm}
  (META/f'index_{idx:02d}_supplemental.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n'); results.append(out)
 summary={'schema':'NM_GATE_B_SUPPLEMENTAL_ARXIV_SUMMARY_V1','completed_utc':now(),'fetches_made':fetches,'resolved_indices':len(results),'full_text_indices':sum(x['pdf_text'].get('text_chars',0)>1000 for x in results),'indices':[{'index':x['index'],'arxiv_id':x['selected_arxiv_id'],'text_chars':x['pdf_text'].get('text_chars',0)} for x in results]}
 (PACKET/'sources/SUPPLEMENTAL_ARXIV_SUMMARY.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({'status':'DONE','fetches':fetches,'resolved_indices':len(results),'full_text_indices':summary['full_text_indices']},indent=2))
if __name__=='__main__': main()
