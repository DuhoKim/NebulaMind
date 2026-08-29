import fitz
doc = fitz.open("../bhu-reading-20260823/sources/rothman_ellis_1993_qjras34_201.pdf")
for i in range(len(doc)):
    page = doc.load_page(i)
    pix = page.get_pixmap(dpi=150)
    pix.save(f"re_page_{i+1}.png")
print(f"Rendered {len(doc)} pages")
