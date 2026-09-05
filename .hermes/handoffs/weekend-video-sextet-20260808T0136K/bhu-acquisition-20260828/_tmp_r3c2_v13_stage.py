import io,sys,re
p="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; s=io.open(p,encoding='utf-8').read(); SCR=sys.argv[1]
E=[]
def E_(o,n,t): E.append((o,n,t))
E_('- **`REPRO_BLOCKED`** — an input whose value the paper does not print, but for which the paper **names a source (a\n  citation)**, where that source is outside this lane and cannot be obtained. Name it. *(Distinct from\n  `REPRO_INPUT_ABSENT`, which is an input the paper neither prints nor traces to any named source.)*','- **`REPRO_BLOCKED`** — an input whose value the claiming paper does not print, and for which the claiming paper\n  **names a source (a citation)** that is **not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`**; whether that\n  source is obtainable elsewhere is irrelevant, because the census may not open or consume it. Name the input and the\n  source. *(Distinct from `REPRO_INPUT_ABSENT`, which is an input the paper neither prints nor traces to any named\n  source; a value cited from a pinned enumerable text is `PRINTED` there under §2.)*',"BLOCKED domain (codex V12 D1)")
E_("`{claim_id, input_id, symbol, status: PRINTED|STANDARD|ABSENT, origin: DERIVED|STANDARD|MEASURED|CHOSEN|FITTED|IMPORTED|UNDECLARED,\n  origin_evidence: {reason_code, source_file, source_line, verbatim}, derived_from: [input_id…], root_origins: […],\n  value, source_file, source_line}`.",
"`{claim_id, input_id, symbol, status: PRINTED|STANDARD|ABSENT, origin: DERIVED|STANDARD|MEASURED|CHOSEN|FITTED|IMPORTED|UNDECLARED,\n  origin_evidence: {reason_code, source_file, source_line, verbatim}, origin_search: {query, files, matches} (required\n  when reason_code is ORIG_SILENT), derived_from: [input_id…], value, source_file, source_line}`. **The seat-authored\n  ledger MUST omit `root_origins`, `rests_on`, `origin_alt` and `origin_evidence_alt`; `validate` fails a ledger that\n  carries any of them. The script adds `root_origins` and per-claim `rests_on` on `compute`; the merge step adds\n  `origin_alt` and `origin_evidence_alt`.**","C3 schema (codex V12 D2/D3)")
E_("where the\n  two seats' `origin` classifications differ the record carries `origin_alt` and the claim's `rests_on` is computed under\n  both and marked `DISPUTED`.**",
"the two seats'\n  independently validated ledgers are merged by `/usr/bin/python3 r3c2_ledger_tools.py merge <ledger_seatA.json>\n  <ledger_seatB.json> <merged.json>` (exit 1 if their `input_id` sets differ); where the two `origin` classifications\n  differ the merged record carries `origin_alt` and `origin_evidence_alt`, `compute` reads the merged ledger, and the\n  claim's `rests_on` is computed under both and marked `DISPUTED`.**","C3 merge command (codex V12 D3)")
miss=[(t,s.count(o)) for o,n,t in E if s.count(o)!=1]
print("dry-run misses:",miss)
if len(sys.argv)>2 and sys.argv[2]=="apply":
    assert not miss
    for o,n,t in E: s=s.replace(o,n); print("  -",t)
    for h in set(re.findall(r"r3c2_ledger_tools\.py` \(sha256 `([0-9a-f]{64})`\)",s))|set(re.findall(r"sha256 `([0-9a-f]{64})`; the seat runs",s)): s=s.replace(h,SCR)
    io.open(p,'w',encoding='utf-8').write(s); print("applied; script pin count:",s.count(SCR))
