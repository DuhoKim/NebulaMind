import json,re
from pathlib import Path
A=Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715');s=(A/'area_review_17_bland_hawthorn_gerhard_2016_DR_RAW_PACKET.md').read_text();rows=[]
for m in re.finditer(r'^REV17-P(\d{3})\t([^\n]+)',s,re.M):
 f=m.group(2).split('\t');
 if len(f)<9: raise SystemExit((m.group(1),len(f),f))
 rows.append({'key':'P'+m.group(1),'raw_authors_year':f[0],'raw_journal':f[1],'raw_title':f[2],'raw_doi':f[3],'raw_arxiv':f[4],'raw_ads':f[5],'raw_role':f[6],'raw_locator':f[7],'raw_boundary':f[8]})
(A/'scratch/review_base17_source_candidates.json').write_text(json.dumps({'sources':rows},indent=2,ensure_ascii=False)+'\n');print({'rows':len(rows),'with_ads':sum(x['raw_ads']!='none' for x in rows)})
