import json,re
from pathlib import Path
A=Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715');I=A/'scratch/review_base11_ads_identities.json';O=A/'area_review_11_wechsler_tinker_2018_CURATED_SOURCE_REGISTRY.json';rows=json.loads(I.read_text())['sources'];uncited={'P015':'NOT_FOUND_IN_COMPLETE_AR5IV_REVIEW_BIBLIOGRAPHY','P026':'NOT_FOUND_IN_COMPLETE_AR5IV_REVIEW_BIBLIOGRAPHY','P027':'NOT_FOUND_IN_COMPLETE_AR5IV_REVIEW_BIBLIOGRAPHY'};overrides={
'P016':('measurement','observed galaxy environment correlations','SDSS luminosity/color/environment correlations; this physical paper does not establish the minimum luminous-halo mass.'),
'P021':('measurement','SDSS luminosity and color clustering','Clustering measurement interpreted with HOD; this paper does not originate the standard central/satellite occupation equations.'),
'P031':('measurement','group and cluster star-formation demographics','Local group/cluster SFR and red-fraction trends; use REV11-P044 for delayed-then-rapid quenching timescales.'),
}
sources=[];corrected=[]
for x in rows:
 a=x['ads_direct'];assert a['status']=='PASS',x['key'];key=x['key'];role=x['role'];loc=x['review_locator'];bd=x['boundary']
 if key in overrides:role,loc,bd=overrides[key]
 status='QUARANTINED' if key in uncited else 'PASS';membership='FAIL_NOT_IN_REVIEW' if key in uncited else ('PASS_AR5IV_TINKER_2008B_REFERENCE' if key=='P012' else 'PASS_AR5IV_AUTHOR_YEAR_JOURNAL_PAGE')
 z={'key':'REV11-'+key,'authors':'; '.join(a['authors']),'year':int(a['bibcode'][:4]),'journal':a['publication'],'title':a['title'],'doi':a['doi'],'arxiv':a['arxiv'],'ads_bibcode':a['bibcode'],'role':'quarantined_candidate' if status!='PASS' else role,'review_locator':loc,'boundary':bd,'source_status':status,'identity_verification':{'status':'PASS_ADS_DIRECT','ads_url':a['url'],'review_membership':membership}}
 if status!='PASS':z['quarantine_reason']=uncited[key]
 sources.append(z)
 if 'raw_title' in x:
  n=lambda v:re.sub(r'[^a-z0-9]','',(v or '').casefold());diff=[f for f,rv,av in [('title',x.get('raw_title'),a['title']),('doi',x.get('raw_doi'),a['doi']),('arxiv',x.get('raw_arxiv'),a['arxiv']),('bibcode',x.get('bibcode'),a['bibcode'])] if n(rv)!=n(av)]
  if diff:corrected.append({'key':'REV11-'+key,'fields':diff})
qs=[
('P047','Allen et al. 2025 JWST high-z analysis',2025,'2501.11674','POST_2018_UNCITED_NOT_USABLE'),
('P048','Meyer et al. 2025 JWST high-z analysis',2025,'2503.14280','POST_2018_UNCITED_NOT_USABLE'),
('P049','DESI post-2018 cosmology result',2025,'2507.07798','POST_2018_UNCITED_NOT_USABLE'),
('P050','AbacusSummit HOD emulator',2021,None,'POST_2018_UNCITED_NOT_USABLE'),
('P051','Shen et al. 2024 SMBH dark-halo paper',2024,None,'POST_2018_UNCITED_NOT_USABLE'),
('P052','Berner et al. 2024 forward modeling',2024,None,'POST_2018_UNCITED_NOT_USABLE')]
for key,title,year,ar,reason in qs:sources.append({'key':'REV11-'+key,'authors':'unverified browsing candidate','year':year,'journal':None,'title':title,'doi':None,'arxiv':ar,'ads_bibcode':None,'role':'quarantined_candidate','review_locator':'raw browsing spillover','boundary':'not usable','source_status':'QUARANTINED','identity_verification':{'status':'QUARANTINED','review_membership':'FAIL_OUTSIDE_2018_REVIEW_SOURCE_BASE'},'quarantine_reason':reason})
primary=[s for s in sources if s['source_status']=='PASS' and s['role']!='supporting_review'];support=[s for s in sources if s['source_status']=='PASS' and s['role']=='supporting_review'];q=[s for s in sources if s['source_status']!='PASS'];assert(len(primary),len(support),len(q))==(40,3,9);assert all(s['year']<=2018 for s in primary+support)
r={'status':'PASS_WITH_UNCITED_RAW_ROWS_QUARANTINED','mission_id':'GALAXY_REVIEW_BASE_DR_20260715','queue_item':11,'review':{'key':'REV11-R00','authors':'Wechsler RH; Tinker JL','year':2018,'title':'The Connection Between Galaxies and Their Dark Matter Halos','journal':'Annual Review of Astronomy and Astrophysics','doi':'10.1146/annurev-astro-081817-051756','arxiv':'1804.03097','ads_bibcode':'2018ARA&A..56..435W','identity_status':'PASS_ADS_CROSSREF_ARXIV'},'review_bibliography_basis':{'source':'https://ar5iv.labs.arxiv.org/html/1804.03097','status':'PASS_COMPLETE_REVIEW_TEXT_AND_REFERENCE_LIST_WEB_ONLY','ads_verification':'PASS_DIRECT_FULL_PAGES_FOR_46_CANDIDATES','local_raw_source_extraction_used':False},'raw_response_reconciliation':{'raw_source_rows':40,'raw_rows_not_found_in_review':3,'raw_identity_tuples_corrected':len(corrected),'supplemented_review_cited_primary_rows':6,'raw_packet_preserved':True,'corrections':corrected},'counts':{'raw_source_rows':40,'total_registry_rows':52,'usable_primary_sources':40,'usable_supporting_reviews':3,'quarantined_sources':9,'usable_sources_verified_by_ads':43},'sources':sources};O.write_text(json.dumps(r,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'counts':r['counts'],'corrected':len(corrected)},sort_keys=True))
