#!/usr/bin/env python3
"""H7 mechanical audit of the P2 source-ledger packet. Read-only on all inputs."""
import json, re, os
from collections import Counter

PRIOR = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-burn-20260711T010503Z/p2-cycle7-source-ledger"
led = json.load(open(os.path.join(PRIOR, "SOURCE_LEAD_LEDGER.json")))
raw_ledger_text = open(os.path.join(PRIOR, "SOURCE_LEAD_LEDGER.json")).read()
mp = open(os.path.join(PRIOR, "AGN_SFR_STATUS_DEBATE_MAP.md")).read()
cand = open(os.path.join(PRIOR, "PRIOR_WORK_COMPARISON_CANDIDATE.md")).read()
rec = open(os.path.join(PRIOR, "P2_RECEIPT.md")).read()

print("== C1 ledger integrity ==")
leads = led["leads"]
ids = [l["lead_id"] for l in leads]
print("total leads:", len(leads))
dup = [i for i, c in Counter(ids).items() if c > 1]
print("duplicate ids:", dup or "none")
pref = {}
for i in ids:
    pref.setdefault(i[0], []).append(int(i[1:]))
for p, nums in pref.items():
    print(f"prefix {p}: n={len(nums)} contiguous_1..n={nums == list(range(1, len(nums)+1))}")
LEGAL = {"VERIFIED_LOCAL", "NEEDS_NETWORK_VERIFICATION", "REJECTED"}
print("illegal classifications:", [(l["lead_id"], l["classification"]) for l in leads if l["classification"] not in LEGAL] or "none")
expect = {"V": "VERIFIED_LOCAL", "N": "NEEDS_NETWORK_VERIFICATION", "U": "NEEDS_NETWORK_VERIFICATION", "R": "REJECTED"}
print("prefix/classification mismatches:", [(l["lead_id"], l["classification"]) for l in leads if expect[l["lead_id"][0]] != l["classification"]] or "none")
CORE = ["lead_id", "source_ref", "exact_claim", "classification", "network_pass_must_confirm", "notes"]
problems = []
for l in leads:
    lid = l["lead_id"]
    for k in CORE:
        if k not in l:
            problems.append(f"{lid}: missing field {k}")
    for k in l:
        if k not in CORE + ["local_basis", "local_basis_reason"]:
            problems.append(f"{lid}: unexpected field {k}")
    lb_null = l.get("local_basis") is None
    has_reason = "local_basis_reason" in l
    if lb_null != has_reason:
        problems.append(f"{lid}: local_basis null={lb_null} but local_basis_reason present={has_reason}")
    cl, np_ = l["classification"], l.get("network_pass_must_confirm")
    if cl == "VERIFIED_LOCAL" and np_ is not None:
        problems.append(f"{lid}: VERIFIED_LOCAL with non-null network_pass_must_confirm")
    if cl != "VERIFIED_LOCAL" and (np_ is None or not str(np_).strip()):
        problems.append(f"{lid}: {cl} with null/empty network_pass_must_confirm")
    if cl in ("VERIFIED_LOCAL", "REJECTED") and l.get("local_basis") is None:
        problems.append(f"{lid}: {cl} with null local_basis")
    for k in ("source_ref", "exact_claim", "notes"):
        if not str(l.get(k) or "").strip():
            problems.append(f"{lid}: empty {k}")
print("field-structure problems:", problems or "none")
unum = []
for l in leads:
    if l["lead_id"].startswith("U"):
        m = re.search(r"label instance (\d+)/26", l["notes"])
        n = int(l["lead_id"][1:])
        if not m or int(m.group(1)) != n:
            unum.append((l["lead_id"], m.group(1) if m else None))
print("U instance-number mismatches:", unum or "none")

print("== C2 count recompute ==")
cnt = Counter(l["classification"] for l in leads)
print("recount:", dict(cnt), "| grand total:", len(leads))
print("ledger counts block:", {k: led["counts"][k] for k in ("total_leads", "VERIFIED_LOCAL", "NEEDS_NETWORK_VERIFICATION", "REJECTED", "uncited_not_usable_label_instances")})
ret = led["counts"]["retained_lead_entries"]
noted = [l["lead_id"] for l in leads if "RETAINED LEAD" in (l.get("notes") or "")]
print("retained claimed:", ret, "| notes-flagged:", noted, "| equal-sets:", set(ret) == set(noted))
for l in leads:
    if l["lead_id"] in ret:
        m = re.search(r"RETAINED LEAD (\d) of 5", l["notes"])
        print("  ", l["lead_id"], "k-of-5:", m.group(1) if m else "MISSING", "| cls:", l["classification"])
n_n = sum(1 for i in ids if i.startswith("N")); n_u = sum(1 for i in ids if i.startswith("U"))
print(f"N={n_n} U={n_u} N+U={n_n+n_u} (receipt asserts N01–N13 + U01–U26 = 39)")

print("== C3 map/candidate/receipt cross-references ==")
lset = set(ids)
def refs(txt): return set(re.findall(r"\b([VNUR]\d{2})\b", txt))
mrefs, crefs, rrefs = refs(mp), refs(cand), refs(rec)
print("map refs not in ledger:", sorted(mrefs - lset) or "none")
print("cand refs not in ledger:", sorted(crefs - lset) or "none")
print("receipt refs not in ledger:", sorted(rrefs - lset) or "none")
print("ledger ids never explicitly referenced in map:", sorted(lset - mrefs) or "none")
print("map has 'U01–U26' range ref:", "U01–U26" in mp or "U01-U26" in mp)
print("map has 'Remaining N- and U-entries' catch-all:", "Remaining N- and U-entries" in mp)
q = re.search(r"## 6\..*?(?=\n---|\Z)", mp, re.S).group(0)
qitems = re.findall(r"^(\d+)\.\s+(.+)$", q, re.M)
print("queue items:")
for n, t in qitems: print(f"   {n}. {t[:90]}")
qids = re.findall(r"\b([VNUR]\d{2})\b", q)
print("queue ids in order:", qids, "| dups:", [i for i, c in Counter(qids).items() if c > 1] or "none")

print("== C4 stance-tag consistency (map+cand inline tags vs ledger) ==")
mism = []
for tag, lid in re.findall(r"\[(VERIFIED_LOCAL|NEEDS_NETWORK_VERIFICATION|REJECTED)\s*[—–-]+\s*(?:ledger\s+)?([VNUR]\d{2})", mp + cand):
    actual = next(l["classification"] for l in leads if l["lead_id"] == lid)
    if actual != tag: mism.append((lid, tag, actual))
print("inline tag/classification mismatches:", mism or "none")

print("== C5 candidate numeric fidelity ==")
for n in ["-1.309", "[-1.334,-1.283]", "8,146", "-0.06", "-14.85", "-11.71", "1,123,718", "0.02<z<0.12", "J/ApJS/196/11"]:
    print(f"  {n!r}: cand={n in cand} map={n in mp} ledger={n in raw_ledger_text}")
print("'centrals' in cand:", "centrals" in cand, "| in map:", "centrals" in mp, "| in ledger:", "centrals" in raw_ledger_text)
print("'-0.12' count cand:", cand.count("-0.12"), "map:", mp.count("-0.12"))
print("'6.7' in cand:", "6.7" in cand, "| '6.5' in cand:", "6.5" in cand)

print("== prohibited-verb occurrences (map + cand) for own-voice review ==")
for name, txt in (("map", mp), ("cand", cand)):
    for m in re.finditer(r"establish\w*|confirm\w*|demonstrat\w*|\bproves?\b|\bproven\b|settl\w*", txt, re.I):
        s, e = max(0, m.start() - 70), min(len(txt), m.end() + 70)
        print(f"[{name}] …{txt[s:e]}…".replace("\n", " ⏎ "))
