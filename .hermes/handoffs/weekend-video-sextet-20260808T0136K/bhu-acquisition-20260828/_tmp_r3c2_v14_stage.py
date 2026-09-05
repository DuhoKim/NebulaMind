import io,sys,re
p="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; s=io.open(p,encoding='utf-8').read()
def cnt(pat): return len(re.findall(pat,s,re.S))
checks={
 "§2 step 3 status enum": r"3\. \*\*Classify each input\*\* as `PRINTED` \(given in the paper\), `STANDARD`",
 "ABSENT supply rule": r"\*\*A seat may not supply a value for an `ABSENT` input\.\*\*",
 "C3 schema status": r"status: PRINTED\|STANDARD\|ABSENT, origin:",
 "C2 statuses": r"Every input classified `PRINTED` / `STANDARD` / `ABSENT`",
 "NO_CLASS def": r"4\. \*\*`R3C2_NO_CLASS`\*\* — a control fails \*\*in every seat that attempted it\*\* after two attempts\.",
}
for k,v in checks.items(): print(f"  {k}: {cnt(v)}")
