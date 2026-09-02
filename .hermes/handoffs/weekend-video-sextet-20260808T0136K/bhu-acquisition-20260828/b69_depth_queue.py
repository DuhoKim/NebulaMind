#!/usr/bin/env python3
"""B69 -- the depth-audit queue, computed (rule: DEPTH_QUEUE_RULE_20260902.md). Self-computing; moves no tier.
Mapping entry -> pinned source is EXPLICIT and VERIFIED (each file's first 60 lines must carry the entry's
token, scanned over the full text because OCR scans put the author last or garble it); a failed verification lists the entry UNMAPPED -- never a guess. The 2026-09-02 first version used a
title-keyword matcher and mapped eight entries to other entries' sources; that version was never committed."""
import os, re, json
_HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.abspath(os.path.join(_HERE,".."))
SRC=os.path.join(W,"bhu-reading-20260823","sources"); P6=os.path.join(W,"bhu-theory-phase6-curvature-20260827")
FRAME=list(range(1,29))+[31]+list(range(36,58))
MAP={1:("pathria_1972_universe_black_hole_nature240_298_clean.txt","pathria"),2:("good_1972_chinese_universes_phystoday25_15_clean.txt","chinese"),
3:("stuckey_1994_observable_universe_black_hole_ajp62_788_clean.txt","stuckey"),4:("knutsen_2009_gravcosmol15_273_clean.txt","knutsen"),
5:("khakshournia_2010_note_pathria_arxiv1412.0105_clean.txt","pathria"),6:("smolin_1992_clean.txt","smolin"),8:("0902.1994_clean.txt","pop"),
9:("1007.0587_clean.txt","pop"),10:("1111.4595v2_poplawski_prd85_clean.txt","pop"),11:("1410.3881_clean.txt","pop"),12:("2509.11468v2_poplawski_ijmpa40_clean.txt","pop"),
13:("frolov_markov_mukhanov_1989_plb216_272_clean.txt","216"),14:("frolov_markov_mukhanov_ic8891_clean.txt","frolov"),15:("hep-th_0103019_clean.txt","easson"),
16:("pourhassan_2025_npb1020_clean.txt","pourhassan"),17:("1909.07129_clean.txt","chakrabarty"),19:("dymnikova_2019_universe_clean.txt","dymnikova"),   # full MDPI text (2026-09-01) supersedes the abridged browser capture universe5050111_*

20:("gr-qc_0611022_clean.txt","bronnikov"),21:("2203.13295_clean.txt","roupas"),22:("2606.25023_clean.txt","easson"),23:("2003.11544_clean.txt","causal"),
24:("2104.00521_clean.txt","peek"),25:("sym14091849_clean.txt","black hole universe"),26:("sym14101984_clean.txt","black hole universe"),27:("2204.11608_clean.txt","big bang"),
28:("2411.14673_clean.txt","holographic"),31:("smolin_2004_cns_clean.txt","smolin"),36:("smoller_temple_2000_clean.txt","smoller"),37:("0210105_clean.txt","shock"),
38:("math-ph_0302036_clean.txt","temple"),39:("1105.6127_clean.txt","bounce"),40:("2008.02136_clean.txt","pop"),41:("2007.11556_clean.txt","pop"),
42:("gonzalez-diaz_1991_plb261_357_clean.txt","baby"),43:("2304.12018_clean.txt","baby"),44:("1309.1487_clean.txt","white"),45:("2210.15186_clean.txt","white"),
46:("1111.1017_clean.txt","quantization"),47:("sato_kodama_sasaki_maeda_1982_plb108_103_clean.txt","sato"),48:("farhi_guth_mitctp1400_clean.txt","guth"),
49:("blau_guendelman_guth_1987_clean.txt","guth"),50:("farhi_guth_guven_ctp1690_clean.txt","guth"),51:("0910.1181_clean.txt","pop"),52:("1808.08327_clean.txt","bounce"),
53:("1906.11824_clean.txt","bounce"),54:("2505.23877_clean.txt","bounce"),55:("2007.06664_clean.txt","sitter"),57:("smoller_temple_1997_clean.txt","smoller")}
NO_TEXT={7:"brown-prl (outside sources; audited c5)",18:"Dymnikova 1992 GRG -- no clean text pinned",56:"Gaztanaga 2023 MNRAS Lett -- PDF only, no clean text"}
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))
print("="*98); print("B69 -- depth-audit queue (rule: DEPTH_QUEUE_RULE_20260902.md)"); print("="*98)
files=set(os.listdir(_HERE))|set(os.listdir(P6)) if os.path.isdir(P6) else set(os.listdir(_HERE))
RQ={"RQ_A":{21},"RQ_C":{25,26},"RQ_D":{22,25,26}}
def audited(n):
    if any(re.match(rf"^ENTRY{n}_(DEEP_)?RECONCILIATION_",f) or re.match(rf"^[bc]\d+_entry{n}_",f) or re.match(rf"^ENTRY{n}_STUDY",f) for f in files): return True
    if n==1 and any(f.startswith("PATHRIA_STANDING_RECONCILIATION") for f in files): return True
    if n==23 and any(f.startswith("PROGRAM_C_FLUX_RESULT") for f in files) and any(f.startswith("PROGRAM_A_FREEDOM_MAP") for f in files): return True   # Programs A/B/C (2026-09-02): receipts are PROGRAM_*, not ENTRY23_*
    return any(any(f.startswith(k) and "RECONCILIATION" in f for f in files) and n in v for k,v in RQ.items())
Q=re.compile(r"\d[\d.,]*\s*(M☉|M_\{?\\?odot|Msun|Mpc|kpc|Gpc|km|GeV|MeV|eV|K\b|σ|sigma|%|Gyr|yr|cm|kg|Hz)|[=<>≃≈≲≳]\s*-?\d")
rows=[]; unmapped=[]; verify_fail=[]
for n in FRAME:
    if n not in MAP: unmapped.append((n,NO_TEXT.get(n,"no mapping"))); continue
    f,tok=MAP[n]; p=os.path.join(SRC,f)
    if not os.path.exists(p): unmapped.append((n,"file missing: "+f)); continue
    lines=open(p,encoding="utf-8",errors="replace").read().split("\n")
    if tok not in " ".join(lines).lower(): verify_fail.append((n,f,tok)); unmapped.append((n,"VERIFY FAILED: "+f)); continue   # full text: OCR scans carry the author at the END (Pathria) or digit-garbled (Frolov: token = volume 216)
    q=sum(1 for l in lines if Q.search(l)); rows.append((n,audited(n),100.0*q/max(1,len(lines)),q,len(lines),f))
queue=sorted([r for r in rows if not r[1]], key=lambda r:(-r[2], r[0]))
aud=sorted(r[0] for r in rows if r[1])+sorted(n for n in NO_TEXT if audited(n))
print(f"  frame {len(FRAME)} | mapped+verified {len(rows)} | unmapped {len(unmapped)}: {unmapped}")
print(f"  audited at depth (receipt on disk): {sorted(set(aud))}")
print(f"  QUEUE ({len(queue)} entries; density = quantitative lines per 100):")
for r in queue: print(f"    entry {r[0]:2d}  {r[2]:5.1f}  ({r[3]}/{r[4]})  {r[5]}")
chk("every frame entry is mapped+verified or listed UNMAPPED with a reason", len(rows)+len(unmapped)==len(FRAME))
chk("no verification failures (a wrong file would poison the ranking)", verify_fail==[], str(verify_fail))
chk("no two entries share a source file", len({r[5] for r in rows})==len(rows))
chk("already deep-audited entries 1, 27, 31, 39, 44, 51, 54 are NOT in the queue", all(r[0] not in (1,27,31,39,44,51,54) for r in queue))
chk("queue is ordered by density desc, then entry asc (empty = depth audit COMPLETE for all mapped entries)", all((-queue[i][2],queue[i][0])<=(-queue[i+1][2],queue[i+1][0]) for i in range(len(queue)-1)))
json.dump({"rule":"DEPTH_QUEUE_RULE_20260902.md","queue":[r[0] for r in queue],"density":{r[0]:round(r[2],2) for r in queue},"unmapped":unmapped,"audited":sorted(set(aud))}, open(os.path.join(_HERE,"depth_queue_state.json"),"w"), indent=1, ensure_ascii=False)
fails=[n for n,p,_ in checks if not p]; print(f"\n{len(checks)-len(fails)}/{len(checks)} checks pass"+(f"  FAILING: {fails}" if fails else ""))
raise SystemExit(1 if fails else 0)
