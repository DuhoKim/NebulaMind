import io,sys,re
p="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; s=io.open(p,encoding='utf-8').read()
R=[]
def R_(pat,new,t): R.append((pat,new,t))
R_(r"a packet or seat-isolation failure before dispatch stops dispatch without a census tally\.",
   "a packet or seat-isolation failure before dispatch files this class.","codex V14: neutralise pre-dispatch sentence")
R_(r"\*\*The candidate and exclusion ledgers are JSON files validated by the pinned script:\s+`/usr/bin/python3 r3c2_ledger_tools\.py census <candidates\.json> <exclusions\.json>` — exit 0 only if every candidate\s+carries exactly one disposition and the printed counts equal the recomputed counts; print its command, stdout and\s+exit status\.\*\*",
   "**The candidate file is a JSON object `{declared_candidate_count, declared_included_count, declared_excluded_count,\n  candidates: [...]}` and the exclusion file is `{declared_exclusion_count, exclusions: [...]}`. Before the tally, print\n  those four declared counts verbatim from the files, then run\n  `/usr/bin/python3 r3c2_ledger_tools.py census <candidates.json> <exclusions.json>`: PASS requires exit 0 after the\n  script verifies that every candidate has exactly one disposition, that every exclusion names one excluded candidate,\n  and that each declared count equals the count recomputed from the rows; its stdout prints both the declared and the\n  recomputed counts. Print its command, stdout and exit status.**","codex V14 2.1: C1 declared counts")
miss=[(t,len(re.findall(pat,s))) for pat,new,t in R if len(re.findall(pat,s))!=1]
print("dry-run misses:",miss)
if len(sys.argv)>1 and sys.argv[1]=="apply":
    assert not miss
    for pat,new,t in R: s=re.sub(pat,lambda m:new,s,count=1); print("  -",t)
    io.open(p,'w',encoding='utf-8').write(s); print("applied")
