import json,re
from pathlib import Path
A=Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715");I=A/"scratch/review_base09_ads_identities.json";O=A/"area_review_09_forster_schreiber_wuyts_2020_CURATED_SOURCE_REGISTRY.json"
Q={"P010":"AGN_CENTERED_NOT_USABLE: ADS resolves this row as an AGN-driven outflow paper; excluded from the non-AGN core harvest","P036":"UNCITED_INVALID_NOT_USABLE: supplied Ceverino 2012 tuple resolves to no ADS record and is not a valid review-bibliography identity","P052":"UNCITED_NOT_USABLE: supplied Kennicutt 1998 tuple resolves to the global Schmidt-law paper, but Kennicutt is absent from the review bibliography"}
def n(v):
 if v is None or str(v).strip().lower()=="none":return None
 return str(v).strip()
def eq(a,b):
 a,b=n(a),n(b)
 return (a is None and b is None) or (a is not None and b is not None and re.sub(r"\s+"," ",a).casefold()==re.sub(r"\s+"," ",b).casefold())
rows=json.loads(I.read_text())["sources"];sources=[]
for x in rows:
 k=x['key'];a=x['ads_direct'];quarantine=k in Q
 if not quarantine:assert a['status']=='PASS',(k,a)
 title=n(a['title']) if a['status']=='PASS' else n(x['title_raw']);doi=n(a['doi']) if a['status']=='PASS' else None;ar=n(a['arxiv']) if a['status']=='PASS' else None;bib=n(a['bibcode']) if a['status']=='PASS' else None
 corr=[]
 if a['status']!='PASS':corr.append({'field':'identity','raw':{'title':x['title_raw'],'doi':n(x['doi_raw']),'arxiv':n(x['arxiv_raw']),'ads_bibcode':n(x['ads_raw'])},'canonical':None})
 else:
  for field,raw,can in [('title',x['title_raw'],title),('doi',x['doi_raw'],doi),('arxiv',x['arxiv_raw'],ar),('ads_bibcode',x['ads_raw'],bib)]:
   if not eq(raw,can):corr.append({'field':field,'raw':n(raw),'canonical':can})
 status='QUARANTINED' if quarantine else 'PASS';membership='FAIL_NOT_IN_AR5IV_REVIEW_BIBLIOGRAPHY' if k in {'P036','P052'} else ('PASS_BUT_TOPIC_EXCLUDED' if k=='P010' else 'PASS_AR5IV_AUTHOR_YEAR_JOURNAL_PAGE')
 sources.append({'key':f'REV09-{k}','authors':x['authors_raw'],'year':x['year'],'journal':a.get('publication') or x['journal_raw'],'title':title,'doi':doi,'arxiv':ar,'ads_bibcode':bib,'role':x['role_raw'],'review_locator':x['review_locator_raw'],'boundary':x['boundary_raw'],'source_status':status,'identity_verification':{'status':'PASS_ADS_DIRECT' if status=='PASS' else 'QUARANTINED','ads_url':a['url'],'review_membership':membership},'raw_tuple_corrected':bool(corr),'corrections':corr,'quarantine_reason':Q.get(k)})
usable=[s for s in sources if s['source_status']=='PASS'];q=[s for s in sources if s['source_status']!='PASS']
assert len(sources)==52 and len(usable)==49 and len(q)==3 and all(s['year']<=2020 for s in usable) and all(s['ads_bibcode'] and s['doi'] for s in usable)
r={'status':'PASS_COMPOSITE_IDS_AND_REVIEW_MEMBERSHIP','mission_id':'GALAXY_REVIEW_BASE_DR_20260715','queue_item':9,'review':{'key':'REV09-R00','authors':'Förster Schreiber NM & Wuyts S','year':2020,'title':'Star-Forming Galaxies at Cosmic Noon','journal':'Annual Review of Astronomy and Astrophysics','doi':'10.1146/annurev-astro-032620-021910','arxiv':'2010.10171','ads_bibcode':'2020ARA&A..58..661F','identity_status':'PASS_ADS_CROSSREF_ARXIV'},'review_bibliography_basis':{'source':'https://ar5iv.labs.arxiv.org/html/2010.10171','status':'PASS_COMPLETE_REVIEW_TEXT_AND_REFERENCE_LIST_WEB_ONLY','local_raw_source_extraction_used':False},'counts':{'raw_harvest_rows':52,'total_registry_rows':52,'usable_primary_sources':49,'usable_supporting_reviews':0,'quarantined_sources':3,'corrected_raw_rows':sum(s['raw_tuple_corrected'] for s in sources)},'sources':sources};O.write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n');print(json.dumps(r['counts'],sort_keys=True))
