import json,re
from pathlib import Path
A=Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715');s=(A/'area_review_20_renzini_2006_DR_RAW_PACKET.md').read_text();rows=[]
for m in re.finditer(r'^REV20-P(\d{3})\t([^\n]+)',s,re.M):
 f=m.group(2).split('\t');ads=re.search(r'ADS\s+([^;\s]+)',f[1] if len(f)>1 else '')
 rows.append({'key':'P'+m.group(1),'raw_citation':f[0],'raw_ads':ads.group(1).strip() if ads else 'none','raw_role':f[2] if len(f)>2 else '','raw_boundary':f[3] if len(f)>3 else (f[2] if len(f)>2 else '')})
(A/'scratch/review_base20_source_candidates.json').write_text(json.dumps({'sources':rows},indent=2,ensure_ascii=False)+'\n');print({'rows':len(rows),'with_ads':sum(x['raw_ads']!='none' for x in rows)})
