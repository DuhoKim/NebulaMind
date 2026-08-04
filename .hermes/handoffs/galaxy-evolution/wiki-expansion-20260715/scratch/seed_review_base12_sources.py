import json
from pathlib import Path
A=Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715');s=(A/'area_review_12_blanton_moustakas_2009_DR_RAW_PACKET.md').read_text();sec=s[s.index('REV12-P001\t'):s.index('The following highly-cited papers')];rows=[]
for line in sec.splitlines():
 if not line.startswith('REV12-P'):continue
 c=line.split('\t');assert len(c)==11,(c[0],len(c));key=c[0].replace('REV12-','');rows.append({'key':key,'raw_authors':c[1],'raw_year':c[2],'raw_journal':c[3],'raw_title':c[4],'raw_doi':None if c[5]=='none' else c[5],'raw_arxiv':None if c[6]=='none' else c[6].replace('arXiv:',''),'bibcode':c[7],'role':c[8],'review_locator':c[9],'boundary':c[10]})
assert len(rows)==45
(A/'scratch/review_base12_source_candidates.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n');print({'rows':len(rows),'primary':sum(x['role']!='supporting_review' for x in rows),'supporting':sum(x['role']=='supporting_review' for x in rows)})
