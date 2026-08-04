import json
from pathlib import Path
A=Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715');s=(A/'area_review_11_wechsler_tinker_2018_DR_RAW_PACKET.md').read_text();sec=s[s.index('REV11-P001\t'):s.index('7. DO_NOT_USE')];rows=[]
for line in sec.splitlines():
 if not line.startswith('REV11-P'):continue
 c=line.split('\t');assert len(c)==9,(c[0],len(c));key=c[0].replace('REV11-','');role=c[6];rows.append({'key':key,'raw_authors_year_journal':c[1],'raw_title':c[2],'raw_doi':None if c[3]=='none' else c[3],'raw_arxiv':None if c[4]=='none' else c[4],'bibcode':c[5],'role':role,'review_locator':c[7],'boundary':c[8]})
extra=[
{'key':'P041','bibcode':'2017ApJ...834...37L','role':'calibration','review_locator':'SHAM secondary halo proxy','boundary':'Generalized abundance matching using virial velocity and concentration; simulation and sample assumptions apply.'},
{'key':'P042','bibcode':'2016MNRAS.457.4360Z','role':'measurement','review_locator':'joint clustering and weak lensing','boundary':'SDSS DR7 stellar-mass-selected galaxy samples; halo-mass and central/satellite model assumptions apply.'},
{'key':'P043','bibcode':'2015ApJ...799..130R','role':'calibration','review_locator':'color-dependent SHMR','boundary':'Local central galaxies split by color; group-catalog and stellar-mass systematics apply.'}]
rows.extend(extra);assert len(rows)==43
(A/'scratch/review_base11_source_candidates.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'sources':len(rows),'raw_rows':40,'supplemented_review_cited_primary':3}))
