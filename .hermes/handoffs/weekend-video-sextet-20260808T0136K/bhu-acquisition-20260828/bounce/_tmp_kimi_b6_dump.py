import re, html

raw = open("b4_springer_access.html", encoding="utf-8", errors="replace").read()

# Cut to article body: from first section to references
start = raw.find('id="Sec1-section"')
end = raw.find('id="Sec10-section"')
if end == -1:
    end = raw.find('class="c-article-references"')
body = raw[start:end]
print("body span", start, end, len(body))

# tokenize: paragraphs and equations in order
tokens = re.split(r'(<div id="Equ\d+".*?</div></div>)', body, flags=re.S)

def clean(s):
    s = re.sub(r'<span class="mathjax-tex">\\\((.*?)\\\)</span>', lambda m: ' [ ' + html.unescape(m.group(1)).strip() + ' ] ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

out = []
for t in tokens:
    m = re.match(r'<div id="Equ(\d+)"', t)
    if m:
        num = m.group(1)
        tm = re.search(r'<span class="mathjax-tex">\$\$(.*?)\$\$</span>', t, flags=re.S)
        eq = html.unescape(tm.group(1)).strip() if tm else "(NO TEX FOUND)"
        eq = re.sub(r'\s+', ' ', eq)
        out.append(f"<<<EQ {num}>>> {eq}")
    else:
        c = clean(t)
        if c:
            out.append("PROSE: " + c)
print("\n\n".join(out))
