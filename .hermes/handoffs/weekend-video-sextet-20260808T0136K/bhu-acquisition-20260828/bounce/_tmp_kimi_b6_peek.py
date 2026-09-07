import re, html

raw = open("b4_springer_access.html", encoding="utf-8", errors="replace").read()

# locate equation anchors
for anchor in ['Equ27', 'Equ28', 'Equ30', 'Equ34', 'Equ35']:
    idxs = [m.start() for m in re.finditer(anchor, raw)]
    print(anchor, "occurrences:", idxs[:6])

# look at structure around first Equ30 occurrence
i = raw.find('Equ30')
print("---- context around Equ30 ----")
print(raw[i-200:i+3000])
