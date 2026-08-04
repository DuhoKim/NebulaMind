import json,re
from pathlib import Path
A=Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715');s=(A/'area_review_14_kewley_nicholls_sutherland_2019_DR_RAW_PACKET.md').read_text();sec=s[s.index('REV14-P001\t'):s.index('DO_NOT_USE_UNVERIFIED Quarantine')];starts=list(re.finditer(r'(?m)^REV14-P\d{3}\t',sec));rows=[]
for i,m in enumerate(starts):
 block=sec[m.start():starts[i+1].start() if i+1<len(starts) else len(sec)];block=re.sub(r' +',' ',block.replace('\n',' ')).strip();c=block.split('\t');assert len(c)>=5,(c[0],len(c));ids=[x.strip() for x in c[2].split(',')];assert len(ids)==3,(c[0],ids);rows.append({'key':c[0].replace('REV14-',''),'raw_citation':c[1],'raw_doi':None if ids[0]=='none' else ids[0],'raw_arxiv':None if ids[1]=='none' else ids[1],'bibcode':None if ids[2]=='none' else ids[2],'raw_role':c[3],'boundary':' '.join(c[4:])})
assert len(rows)==45
(A/'scratch/review_base14_source_candidates.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n');print({'rows':len(rows),'with_ads':sum(bool(x['bibcode']) for x in rows)})
