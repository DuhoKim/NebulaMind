import glob, os, re

IMPOSSIBILITY = r"cannot be both|cannot be\b|can not be\b|does not yield|no .{0,30}(?:can|exists?)\b|impossible|obstruct\w*|must give up|prevents?\b"
DOMAIN        = r"[Cc]onsider a .{0,80}(?:spacetime|metric|parent|class|solution)|[Aa]ssume that|under the (?:same )?assumptions?|hypothes[ei]s"
REFUTABLE     = r"escape|evasion|requires? an? (?:additional|extra)|must give up at least one|unless"

def score(T):
    return (len(re.findall(IMPOSSIBILITY, T)), len(re.findall(DOMAIN, T)), len(re.findall(REFUTABLE, T)))

def is_obstruction(T):
    imp, dom, ref = score(T)
    return imp >= 5 and dom >= 2 and ref >= 2

flagged = []
for f in sorted(glob.glob("../bhu-reading-20260823/sources/*_clean.txt")):
    T = " ".join(open(f, errors="ignore").read().split())
    if is_obstruction(T):
        flagged.append(os.path.basename(f))

print("Flagged files:", flagged)
