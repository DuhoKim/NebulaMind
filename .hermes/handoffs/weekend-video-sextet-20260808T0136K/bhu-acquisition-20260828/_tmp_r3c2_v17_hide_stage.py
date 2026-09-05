import io,sys,re
p="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; s=io.open(p,encoding='utf-8').read()
R=[]; W=[]
def R_(pat,new,t): R.append((pat,new,t))
def W_(pat,t): W.append((pat,t))   # wrap the match in SEAT-REDACT
# §1: second question + "first/second" sentence -> master only
W_(r"; and\s+\(ii\) what does that\s+number rest on — derived, standard or measured inputs only, or a chosen, fitted, imported or undeclared one\?\*\* The first is the\s+reproduction verdict; the second is the ledger's `rests_on` field\.","§1 (ii) + first/second")
R_(r"\*\*two questions from one pass: \(i\) does the paper's own number follow\s+from the paper's own recipe applied to the inputs it states","**does the paper's own number follow from the paper's own recipe applied to the inputs it states","§1 one question")
# §2
R_(r"Provenance is recorded under C3 \(`origin`,\s+`derived_from`, `root_origins`\)\.","Provenance is recorded under C3 (`origin`, `derived_from`).","§2 step 4 fields")
W_(r", \*\*and let the script record the claim's `rests_on`\*\* from the ledger","§2 step 5 rests_on")
# §3 heading paragraph + blockquote
W_(r"\*\*One pass, two tallies\.\*\* The reproduction verdict answers \*\"does the paper's arithmetic work from what it states\?\"\*\s+The ledger answers \*\"what did it rest on\?\"\* So:","§3 two tallies")
R_(r"Each record's `origin`\s+> is cited under C3, independently by both seats; `root_origins` and the per-claim summary field \*\*`rests_on`\*\* are\s+> computed from the ledger by the pinned script `r3c2_ledger_tools\.py` \(sha256 `[0-9a-f]{64}`\), with the full\s+> root-origin set printed beside it\. \*\*No seat writes `root_origins` or `rests_on`; the script rejects a ledger that\s+> arrives with either set\.\*\*",
   "Each record's `origin`\n> is cited under C3, independently by both seats. **`origin` is one recorded attribute of a ledger record, beside\n> `status`, `value`, `source_file` and `source_line`; a seat records it and writes no field outside the schema; `validate`\n> fails a ledger that carries one.**\n<!--SEAT-REDACT-->\n> *(Lane side: `root_origins` and the per-claim field `rests_on` are computed from the merged ledger by `r3c2_lane_tools.py`,\n> which no seat is given.)*\n<!--/SEAT-REDACT-->","§3 blockquote seat-visible")
W_(r" The claim's `rests_on` is reported beside it\.","§3 EXACT rests_on")
W_(r"(?<=not \"error\.\"\*\*) `rests_on`\s+is reported beside it\.","§3 FAILED rests_on")
R_(r"claim is attempted and files `REPRO_EXACT` or `REPRO_FAILED` with its `rests_on`\.","claim is attempted and files `REPRO_EXACT` or `REPRO_FAILED`.","§3 INPUT_ABSENT rests_on")
W_(r" \*\*`rests_on` is computed and reported for every included claim that has at least one\s+ledger record, whatever its outcome; a claim with no ledger record carries `rests_on` `NOT_COMPUTED`, and the `rests_on`\s+tally reports a `NOT_COMPUTED` row\.\*\*","§3 rests_on tally membership")
# §4
W_(r", \*\*and the `rests_on` tally beside it — two tallies from one pass\.\*\*","§4 two tallies")
# C3 schema: alphabetical taxonomy + schema-only rule
R_(r"origin: DERIVED\|STANDARD\|MEASURED\|CHOSEN\|FITTED\|IMPORTED\|UNDECLARED,","origin: CHOSEN|DERIVED|FITTED|IMPORTED|MEASURED|STANDARD|UNDECLARED,","C3 taxonomy alphabetical")
R_(r"\*\*The seat-authored\s+ledger MUST omit `root_origins`, `rests_on`, `origin_alt` and `origin_evidence_alt`; `validate` fails a ledger that\s+carries any of them\. The script adds `root_origins` and per-claim `rests_on` on `compute`; the merge step adds\s+`origin_alt` and `origin_evidence_alt`\.",
   "**The seat-authored\n  ledger carries only the schema fields; `validate` fails a ledger that carries any other field.**<!--SEAT-REDACT-->\n  *(Lane side: `r3c2_lane_tools.py merge` adds `origin_alt` and `origin_evidence_alt`; `compute` adds `root_origins` and\n  per-claim `rests_on`.)*<!--/SEAT-REDACT-->","C3 schema-only rule")
R_(r"`ORIG_EQUATION`→`DERIVED`, `ORIG_CONSTANT`→`STANDARD`, `ORIG_MEASURED`→`MEASURED` \(a quantity the paper reports as\s+its own measurement, with the measurement described\), `ORIG_CHOICE_STATED`→`CHOSEN`, `ORIG_FIT_STATED`→`FITTED`,\s+`ORIG_CITATION`→`IMPORTED`, `ORIG_SILENT`→`UNDECLARED`",
   "`ORIG_CHOICE_STATED`→`CHOSEN`, `ORIG_EQUATION`→`DERIVED`, `ORIG_FIT_STATED`→`FITTED`, `ORIG_CITATION`→`IMPORTED`,\n  `ORIG_MEASURED`→`MEASURED` (a quantity the paper reports as its own measurement, with the measurement described),\n  `ORIG_CONSTANT`→`STANDARD`, `ORIG_SILENT`→`UNDECLARED` (listed alphabetically by origin; the list carries no order of its own)","C3 code list alphabetical")
R_(r"a sentence\s+that names an external source for the value is a citation whatever else it says\.\*\*","a sentence\n  that names an external source for the value is a citation whatever else it says — the order is a tie-break by the\n  specificity of the evidence, not a ranking of the values.**","C3 tie-break reason")
# C3 provenance machinery -> seat sees derived_from + validate; lane side redacted; seat-visible input-set reconciliation
R_(r"\*\*Provenance is transitive, and the transitivity is computed\.\*\* Every `DERIVED` record lists its `derived_from`\s+ids; \*\*a script computes `root_origins`, the origins at the leaves of that chain, and no seat writes that field\.\*\*\s+A chain's root origins are computed from every step, never from its last step alone\.",
   "**Provenance is transitive.** Every `DERIVED` record lists its `derived_from` ids; `validate` fails a `derived_from` id\n  that names no record, a cycle, and a `DERIVED` record with no `derived_from`.<!--SEAT-REDACT--> *(Lane side: `r3c2_lane_tools.py\n  compute` derives `root_origins`, the origins at the leaves of that chain, from every step; no seat writes that field.)*<!--/SEAT-REDACT-->","C3 transitivity seat-visible")
W_(r" \*\*The script is `r3c2_ledger_tools\.py`,\s+committed beside this document, sha256 `[0-9a-f]{64}`; the seat runs\s+`/usr/bin/python3 r3c2_ledger_tools\.py compute <ledger\.json> <out\.json>` and prints its stdout and exit status\. It\s+computes each claim's `rests_on` from its `root_origins` and prints the root-origin set beside it; it REJECTS \(exit 2\) a\s+ledger that arrives with `root_origins` or `rests_on` already set; it FAILS \(exit 1\) on a `derived_from` id that names\s+no record, on a cycle, and on a `DERIVED` record with no `derived_from`, so an empty root set cannot occur; the two seats'\s+independently validated ledgers are merged by `/usr/bin/python3 r3c2_ledger_tools\.py merge <ledger_seatA\.json>\s+<ledger_seatB\.json> <merged\.json>` \(exit 1 if their `input_id` sets differ — \*\*if `merge` exits 1, the two seats reconcile their input lists against the\s+paper's stated equation once; an input-set difference surviving that reconciliation stops the study under\s+`CENSUS_DENOMINATOR_DISPUTED` \(§4\), the disputed inputs listed with both seats' quotations\*\*\); where the two `origin` classifications\s+differ the merged record carries `origin_alt` and `origin_evidence_alt`, `compute` reads the merged ledger, and the\s+claim's `rests_on` is computed under both and marked `DISPUTED`\.\*\* A `rests_on` value present in the seat-authored input ledger fails this control; after a successful `compute` run,\s+a `rests_on` value absent from the script-produced output ledger fails this control\.","C3 lane machinery (redact)")
R_(r", and recomputing `rests_on` by the pinned script\*\*:","**:","C6 recompute rests_on")
W_(r" \*\*A claim whose root-origin set contains an `ORIGIN_DISPUTED` input carries `rests_on` computed\s+under both classifications, printed as a pair and marked `DISPUTED`; the `rests_on` tally reports a `DISPUTED` row\.\*\*","C6 DISPUTED pair")
miss=[(t,len(re.findall(pat,s))) for pat,new,t in R if len(re.findall(pat,s))!=1]+[(t,len(re.findall(pat,s))) for pat,t in W if len(re.findall(pat,s))!=1]
print("dry-run misses:",miss)
if len(sys.argv)>1 and sys.argv[1]=="apply":
    assert not miss
    for pat,new,t in R: s=re.sub(pat,lambda m:new,s,count=1); print("  -",t)
    for pat,t in W:
        m=re.search(pat,s); s=s[:m.start()]+"<!--SEAT-REDACT-->"+m.group(0)+"<!--/SEAT-REDACT-->"+s[m.end():]; print("  - redacted:",t)
    io.open(p,'w',encoding='utf-8').write(s); print("applied")
