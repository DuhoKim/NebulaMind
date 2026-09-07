#!/usr/bin/python3
import re, html
base = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/"
raw = open(base+"b4_springer_access.html", encoding="utf-8", errors="replace").read()
m = re.search(r'id="Equ35" class="c-article-equation">(.*?)</div></div>', raw, re.S)
t = re.search(r'<span class="mathjax-tex">(.*?)</span>', m.group(1), re.S).group(1)
pub = html.unescape(t).strip()
pub_inner = pub[2:-2].strip()

rep = open(base+"B7_CURVED_20260907.md", encoding="utf-8").read()
q = re.search(r'> \\\[(.*?)\\\]\s*\r?\n?>?\s*\(35\)', rep, re.S).group(1)
def norm(s):
    s = re.sub(r"^>\s*", "", s, flags=re.M)
    return re.sub(r"\s+", " ", s).strip()
print("publisher:", norm(pub_inner))
print("report   :", norm(q))
print("MATCH:", norm(pub_inner) == norm(q))
