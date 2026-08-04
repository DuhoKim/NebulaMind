import json,re
from pathlib import Path
A=Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715');s=(A/'area_review_16_carilli_walter_2013_DR_RAW_PACKET.md').read_text();sec=s[s.index('Primary-Citation Harvest'):s.index('DO_NOT_USE_UNVERIFIED Quarantine')];starts=list(re.finditer(r'^REV16-P\d{3}\t',sec,re.M));rows=[]
for i,m in enumerate(starts):
 block=sec[m.start():starts[i+1].start() if i+1<len(starts) else len(sec)].replace('\n',' ').strip();c=[re.sub(r'\s+',' ',x).strip() for x in block.split('\t')];assert len(c)>=5,(c[0],len(c));ids=[x.strip() for x in c[2].split(' / ')];assert len(ids)==3,(c[0],ids);rows.append({'key':c[0].split('-')[-1],'raw_citation':c[1],'raw_doi':None if ids[0].casefold()=='none' else ids[0],'raw_arxiv':None if ids[1].casefold()=='none' else ids[1].removeprefix('arXiv:'),'bibcode':ids[2],'raw_role':c[3],'boundary':' '.join(c[4:])})
assert len(rows)==45,len(rows);(A/'scratch/review_base16_source_candidates.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n');print({'rows':len(rows),'with_ads':sum(bool(x['bibcode']) for x in rows)})
