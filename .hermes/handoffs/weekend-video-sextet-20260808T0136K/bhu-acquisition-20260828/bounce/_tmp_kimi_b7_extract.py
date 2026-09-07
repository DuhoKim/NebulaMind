#!/usr/bin/python3
"""Extract numbered equation payloads + adjacent prose from publisher HTML."""
import re, html
p = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/b4_springer_access.html"
raw = open(p, encoding="utf-8", errors="replace").read()
want = [1,2,6,10,11,14,15,16,24,25,30,31,32,33,34,35,36,37]
for n in want:
    m = re.search(r'id="Equ%d" class="c-article-equation">(.*?)</div></div>' % n, raw, re.S)
    if not m:
        print(f"Equ{n}: NOT FOUND"); continue
    block = m.group(1)
    t = re.search(r'<span class="mathjax-tex">(.*?)</span>', block, re.S)
    num = re.search(r'equation__number">\s*(.*?)\s*</div>', block, re.S)
    print(f"=== Equ{n} printed-number={num.group(1).strip() if num else '?'}")
    print(html.unescape(t.group(1)).strip() if t else "NO TEX")
    print()
