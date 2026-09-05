import io,sys,re
p="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; s=io.open(p,encoding='utf-8').read(); TW=sys.argv[1]
R=[]
def R_(pat,new,t): R.append((pat,new,t))
R_(r" \*\*Neither contaminates the other\.\*\*"," **The reproduction verdict and the provenance fields are recorded separately.**","codex leak 1 §1")
R_(r"from the paper's own recipe applied to the inputs it states — chosen constants included; and","from the paper's own recipe applied to the inputs it states; and","§1 chosen constants included")
R_(r"i\.e\. every ledger record with status `PRINTED` or `STANDARD`, chosen and fitted values included\.\*\* Provenance is\s+\*\*recorded\*\* \(C3's `origin`, `derived_from`, `root_origins`\), never filtered on\. \*\(A paper can direct you to use its own chosen constant, and following that instruction is reproducing the\s+paper\.\)\*",
   "i.e. every ledger record with status `PRINTED` or `STANDARD`.** Provenance is recorded under C3 (`origin`,\n   `derived_from`, `root_origins`).","codex leak 3 §2 step 4")
R_(r"\*\*One pass, two tallies\.\*\* The reproduction verdict answers \*\"does the paper's\s+arithmetic work from what it states\?\"\* The ledger answers \*\"what did it rest on\?\"\* — a value can be printed in the\s+paper and still have been chosen or fitted, <!--SEAT-REDACT-->as entry 59's `β = 1/929\.25` is, <!--/SEAT-REDACT-->and both facts\s+survive: the arithmetic reproduces AND the ledger says what it rested on\. So:",
   "**One pass, two tallies.** The reproduction verdict answers *\"does the paper's arithmetic work from what it states?\"*\nThe ledger answers *\"what did it rest on?\"* So:","codex leak 4 §3 both-facts")
R_(r"\*\*PROVENANCE IS RECORDED, NOT FILTERED\*\*: each record's `origin`[\s>]+is cited under C3, independently by both seats;","**Arithmetic consumes records according to status `PRINTED` or `STANDARD`.** Each record's `origin`\n> is cited under C3, independently by both seats;","codex leak 2 §3")
R_(r"120-second cap on symbolic operations with `SYMBOLIC_TIMEOUT` as a reportable\s+outcome;", f"every symbolic operation launched through the committed wrapper `r3c2_timeout.py` (sha256\n`{TW}`) as `/usr/bin/python3 r3c2_timeout.py 120.0 -- <command>`, which enforces a 120.0-second wall-clock\ndeadline on the monotonic clock, prints the wrapper command, the child's stdout and stderr and its exit status, and on\nthe deadline prints `SYMBOLIC_TIMEOUT` and exits 124 — the reportable outcome;","codex timeout wrapper §9")
miss=[(t,len(re.findall(pat,s))) for pat,new,t in R if len(re.findall(pat,s))!=1]
print("dry-run misses:",miss)
if len(sys.argv)>2 and sys.argv[2]=="apply":
    assert not miss
    for pat,new,t in R: s=re.sub(pat,lambda m:new,s,count=1); print("  -",t)
    io.open(p,'w',encoding='utf-8').write(s); print("applied")
