#!/usr/bin/env python3
"""Round-2 repairs to the STAGED kit (codex F1, F4, F5, F6, F7 + kimi round 2 when read). Applied only after both reviewers have exited.
Write-at-end; every anchor asserted."""
import io,sys
S="r3c2_staged_d1d7/r3c2_ledger_tools_STAGED.py"; s=io.open(S,encoding="utf-8").read()
# F1: a selection without a seed is not recomputable → fail, never skip
a='    if all(k in S for k in ("seed_hex",)):\n        R=selection_of(sc, S["seed_hex"])'; assert s.count(a)==1
s=s.replace(a,'    if not (isinstance(S.get("seed_hex"),str) and len(S["seed_hex"])==64): fails.append("C6_SELECTION: selection carries no 64-hex seed; nothing to recompute against")  # PROBE:C6_SEED_PRESENT\n    else:\n        R=selection_of(sc, S["seed_hex"])')
# F4: for EVERY PRINTED record, bind the claim to its claiming file; a value line in another file must be an import, whatever reason code was submitted
a='        if r["status"]=="PRINTED" and rc=="ORIG_CITATION":'; assert s.count(a)==1
s=s.replace(a,'''        if r["status"]=="PRINTED" and candidates:
            cf0=claim_file.get(r["claim_id"])
            if cf0 is not None and r["source_file"]!=cf0 and not (r["origin"]=="IMPORTED" and rc=="ORIG_CITATION"):
                fails.append(f"{r['input_id']}: value line is in {r['source_file']} but claim {r['claim_id']} belongs to {cf0}: such a record must be IMPORTED with ORIG_CITATION (submitted {r['origin']}/{rc})")  # PROBE:D1_IMPORT_REFILED
                continue
        if r["status"]=="PRINTED" and rc=="ORIG_CITATION":''')
# F5: the symbol floor fails open when no line carries symbol and numeral
a='                if first is not None and first!=int(r["source_line"]): fails.append('; assert s.count(a)==1
s=s.replace(a,'''                if first is None: fails.append(f"{r['input_id']}: no line of {r['source_file']} carries both {r['symbol']} and {r.get('value')}")  # PROBE:D1_NO_SYMBOL_LINE
                elif first!=int(r["source_line"]): fails.append(''')
# F2: state what the study files
a='"C6_AUDIT_SAMPLE":tok,"scope":'; assert s.count(a)==1
s=s.replace(a,'"C6_AUDIT_SAMPLE":tok,"study_files":("none" if tok=="PASS" else "CENSUS_AUDIT_FAILED"),"scope":')
io.open(S,"w",encoding="utf-8").write(s)
B="r3c2_staged_d1d7/r3c2_batch_tools_STAGED.py"; b=io.open(B,encoding="utf-8").read()
# F7: join verifies the sealed ownership fields against the partition and the ordered predecessor chain
a='        bad=False\n        for f in ART(k):'; assert b.count(a)==1
b=b.replace(a,'''        bad=False; sk=S[str(k)]
        if sk.get("owned_files")!=b["files"] or sk.get("owned_sha256")!=b["sha256"]: fails.append(f"batch {k}: sealed ownership differs from the partition"); bad=True  # PROBE:SEAL_OWNERSHIP
        exp_pred=(hashlib.sha256(json.dumps(S[str(k-1)],sort_keys=True).encode()).hexdigest() if str(k-1) in S else None)
        if k>1 and (str(k-1) not in S or sk.get("predecessor_seal_sha256")!=exp_pred): fails.append(f"batch {k}: predecessor chain broken (seal does not bind batch {k-1}'s seal)"); bad=True  # PROBE:SEAL_CHAIN
        for f in ART(k):''')
a='    for b in P["batches"]:\n        k=b["batch"]; owned=set(b["files"])\n        if str(k) not in S: fails.append(f"batch {k}: not sealed"); continue'; assert b.count(a)==1
b=b.replace(a,'''    extra=sorted(set(S)-{str(b["batch"]) for b in P["batches"]})
    if extra: fails.append(f"seals for batches not in the partition: {extra}")
    for b in P["batches"]:
        k=b["batch"]; owned=set(b["files"])
        if str(k) not in S: fails.append(f"batch {k}: not sealed"); continue''')
# F6: every ledger claim_id names an INCLUDED candidate owned by the batch; every input_id begins with that candidate's file + '#'
a='        for r in ld:\n            if owner_of(r.get("claim_id")) not in owned:'; assert b.count(a)==1
b=b.replace(a,'''        inc_ids={c.get("candidate_id") for c in cd["candidates"] if c.get("included")}
        for r in ld:
            if r.get("claim_id") not in inc_ids: fails.append(f"batch {k}: ledger record {r.get('input_id')} names claim {r.get('claim_id')}, not an included candidate of this batch")  # PROBE:ORPHAN_CLAIM
            elif not str(r.get("input_id","")).startswith(str(r.get("claim_id")).split("#",1)[0]+"#"): fails.append(f"batch {k}: input_id {r.get('input_id')} does not begin with its claim's file followed by #")  # PROBE:INPUT_ID_FORM
            if owner_of(r.get("claim_id")) not in owned:''')
io.open(B,"w",encoding="utf-8").write(b); print("round-2 repairs applied to the staged kit (tests to be extended next)")
