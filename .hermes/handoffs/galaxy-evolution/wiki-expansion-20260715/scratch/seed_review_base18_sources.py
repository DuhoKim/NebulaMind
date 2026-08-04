import json,re
from pathlib import Path
A=Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715');s=(A/'area_review_18_freeman_bland_hawthorn_2002_DR_RAW_PACKET.md').read_text();rows=[]
for m in re.finditer(r'^REV18-P(\d{3})\t([^\n]+)',s,re.M):
 f=m.group(2).split('\t');
 if len(f)<4:raise SystemExit((m.group(1),f))
 ids=f[1];ads=re.search(r'ADS:\s*([^;]+)',ids);doi=re.search(r'DOI:\s*([^;]+)',ids);ar=re.search(r'arXiv:\s*([^;]+)',ids)
 rows.append({'key':'P'+m.group(1),'raw_citation':f[0],'raw_doi':doi.group(1).strip() if doi else 'none','raw_arxiv':ar.group(1).strip() if ar else 'none','raw_ads':ads.group(1).strip() if ads else 'none','raw_role':f[2],'raw_boundary':f[3]})
(A/'scratch/review_base18_source_candidates.json').write_text(json.dumps({'sources':rows},indent=2,ensure_ascii=False)+'\n');print({'rows':len(rows),'with_ads':sum(x['raw_ads']!='none' for x in rows)})
