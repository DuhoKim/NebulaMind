import re, html, sys

raw = open("b4_springer_access.html", encoding="utf-8", errors="replace").read()
print("LEN", len(raw))
for pat in [r'<title>(.*?)</title>', r'citation_journal_title" content="([^"]+)', r'citation_volume" content="([^"]+)', r'citation_doi" content="([^"]+)', r'citation_author" content="([^"]+)', r'citation_publication_date" content="([^"]+)']:
    m = re.findall(pat, raw, re.S)
    print(pat[:40], "->", [x.strip()[:90] for x in m[:4]])
tex = re.findall(r'<script type="math/tex[^"]*"[^>]*>(.*?)</script>', raw, re.S)
print("math/tex count:", len(tex))
for i, t in enumerate(tex):
    s = html.unescape(t).strip().replace("\n", " ")
    print("EQIDX", i, s[:220])
