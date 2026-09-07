import re, html
raw = open("b4_springer_access.html", encoding="utf-8", errors="replace").read()
print("len:", len(raw))
items = re.findall(r'<li[^>]*c-article-references__item[^>]*>(.*?)</li>', raw, re.S)
print("num refs:", len(items))
def clean(t):
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()
want = {14, 15, 50, 52, 60, 74, 75, 109, 47}
for i, it in enumerate(items, start=1):
    if i in want:
        print(i, "->", clean(it)[:340])
