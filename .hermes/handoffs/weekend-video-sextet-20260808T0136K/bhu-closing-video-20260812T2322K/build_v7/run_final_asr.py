#!/usr/bin/env python3
"""Run fresh per-card ASR on audio decoded from the final MP4."""
from __future__ import annotations
import difflib
import json
import re
import subprocess
from pathlib import Path

BUILD=Path(__file__).resolve().parent
T=json.loads((BUILD/'audio/timeline.json').read_text())
PY='/Users/duhokim/.hermes/hermes-agent/venv/bin/python'


def norm(s):
    s=s.lower().replace('’',"'").replace('‘',"'").replace('–','-').replace('—','-').replace('clockwise- and counterclockwise-spinning','clockwise and counterclockwise spinning')
    s=re.sub(r'\bb\.?\s*h\.?\s*u\.?\b','bhu',s)
    s=s.replace('sixty-eight point three percent','68.3 percent').replace('ninety-five point four percent','95.4 percent')
    s=s.replace('one point nine seven','1.97').replace('zero point zero four','0.04').replace('two point zero eight','2.08').replace('zero point zero seven','0.07')
    s=s.replace('one point five','1.5').replace('two point zero zero','2.00')
    s=s.replace('programme','program').replace('favour','favor').replace('centre','center')
    s=s.replace('brown-li-ro','brown lee rho').replace('brown-lee-rho','brown lee rho').replace('brown, li, and rowe','brown lee rho').replace('brown, lee, and rho','brown lee rho')
    s=s.replace('brown-bethy','brown bethe').replace('brown-bethe','brown bethe').replace('demerest','demorest')
    s=re.sub(r'\btoo\b','two',s); s=re.sub(r'\b2\b','two',s)
    s=re.sub(r'\b1\.5\b','one point five',s); s=re.sub(r'\b1\.97\b','one point nine seven',s); s=re.sub(r'\b0\.04\b','zero point zero four',s); s=re.sub(r'\b2\.08\b','two point zero eight',s); s=re.sub(r'\b0\.07\b','zero point zero seven',s)
    s=s.replace('±',' plus or minus ').replace('%',' percent ')
    s=re.sub(r"[^a-z0-9.]+",' ',s)
    return ' '.join(s.split())

records=[]
for c in T['cards']:
    cid=c['card_id']; audio=BUILD/f'final_qa/cards/card-{cid}.wav'; out=BUILD/f'final_qa/cards/card-{cid}-asr.json'
    p=subprocess.run([PY,str(BUILD/'transcribe.py'),str(audio),'--out',str(out)],capture_output=True,text=True,timeout=300)
    if p.returncode: raise RuntimeError(f'encoded ASR {cid} failed: {p.stderr[-500:]}')
    tr=json.loads(out.read_text()).get('text',''); ne,nt=norm(c['narration']),norm(tr); ratio=difflib.SequenceMatcher(None,ne,nt).ratio()
    rec={'card_id':cid,'expected':c['narration'],'transcript':tr,'normalized_expected':ne,'normalized_transcript':nt,'similarity':ratio,'status':'PASS' if ratio>=.93 else 'HOLD'}
    records.append(rec); print(cid,f'{ratio:.4f}',tr)
report={'status':'PASS' if all(r['status']=='PASS' for r in records) else 'HOLD','model':'whisper-1','scope':'AAC audio decoded from final MP4 and split at exact card boundaries','threshold':.93,'normalization_scope':'punctuation, numeric forms, UK/US spelling, and proper-name phonetics only','records':records}
(BUILD/'final_qa/encoded_audio_asr.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print('STATUS',report['status'])
raise SystemExit(0 if report['status']=='PASS' else 2)
