import json,re
from pathlib import Path
A=Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715');s=(A/'area_review_15_veilleux_cecil_bland_hawthorn_2005_DR_RAW_PACKET.md').read_text();sec=s[s.index('7. Primary Citation Harvest'):s.index('8. DO_NOT_USE_UNVERIFIED')];starts=list(re.finditer(r'^REV15-P\d{3}\t',sec,re.M));rows=[]
for i,m in enumerate(starts):
 block=sec[m.start():starts[i+1].start() if i+1<len(starts) else len(sec)].replace('\n',' ').strip();c=[re.sub(r'\s+',' ',x).strip() for x in block.split('\t')];assert len(c)>=8,(c[0],len(c));ident=c[1];rows.append({'key':c[0].split('-')[-1],'raw_citation':ident,'raw_doi':None if c[2].casefold()=='none' else c[2],'raw_arxiv':None if c[3].casefold()=='none' else c[3],'bibcode':c[4],'raw_role':c[5],'review_locator':c[6],'boundary':' '.join(c[7:])})
assert len(rows)==45,len(rows);(A/'scratch/review_base15_source_candidates.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n');print({'rows':len(rows),'with_ads':sum(bool(x['bibcode']) for x in rows)})
