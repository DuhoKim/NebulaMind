import io,sys,re
p="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; s=io.open(p,encoding='utf-8').read()
R=[]
def R_(pat,new,t): R.append((pat,new,t))
R_(r"- \*\*C1 — denominator\.\*\* Claims \*\*included\*\*, claims \*\*excluded\*\* \(with the exclusion ledger of §3\), and attempts made,\s+all printed before any tally\.",
   "- **C1 — denominator.** Claims **included**, claims **excluded** (with the exclusion ledger of §3), and the attempts\n  made, all printed before any tally.","C1 lead (keep)")
R_(r"\*\*The candidate file is a JSON object `\{declared_candidate_count, declared_included_count, declared_excluded_count,\s+candidates: \[\.\.\.\]\}`",
   "**The candidate file is a JSON object `{declared_candidate_count, declared_included_count, declared_excluded_count,\n  declared_attempt_count, candidates: [...]}`; every included candidate carries `attempts`, the number of §2 attempts made\n  on it, in {0, 1, 2}, and `declared_attempt_count` is their sum","codex 2.1 attempts schema")
R_(r"script verifies that every candidate has exactly one disposition, that every exclusion names one excluded candidate,\s+and that each declared count equals the count recomputed from the rows;",
   "script verifies that every candidate has exactly one disposition, that every exclusion names one excluded candidate,\n  that every included candidate carries a permitted `attempts` value, and that each of the four declared counts equals\n  the count recomputed from the rows;","codex 2.1 attempts check")
R_(r"\*\*What the blind proves and does not:\*\* it proves the seat was not given the pattern record and did not read it\s+from its working directory\.",
   "**What the blind supports and does not:** the dispatch record proves that the seat was not furnished the pattern\n  record in its working directory. The self-reported path list is secondary evidence and, because it is not complete\n  and filesystem access is not denied, this design does not prove that the seat did not read an absolute path into the\n  lane; `C4_SEAT_ISOLATION=PASS` certifies the contents of the printed list and of the dispatch copy, not actual\n  non-access.","codex 3.1 blind claim")
R_(r"the script\s+`r3c2_ledger_tools\.py`, and the pinned sources of `R3C2_CORPUS_MANIFEST\.md`,",
   "the script\n  `r3c2_ledger_tools.py`, the wrapper `r3c2_timeout.py`, and the pinned sources of `R3C2_CORPUS_MANIFEST.md`,","codex 7.1 wrapper in dispatch copy")
miss=[(t,len(re.findall(pat,s))) for pat,new,t in R if len(re.findall(pat,s))!=1]
print("dry-run misses:",miss)
if len(sys.argv)>1 and sys.argv[1]=="apply":
    assert not miss
    for pat,new,t in R: s=re.sub(pat,lambda m:new,s,count=1); print("  -",t)
    io.open(p,'w',encoding='utf-8').write(s); print("applied")
