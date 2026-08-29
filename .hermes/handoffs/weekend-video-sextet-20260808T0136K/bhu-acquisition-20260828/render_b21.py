import fitz
doc = fitz.open("../bhu-reading-20260823/sources/harrison_1995_qjras36_193.pdf")
for i in range(len(doc)):
    page = doc.load_page(i)
    pix = page.get_pixmap(dpi=150)
    pix.save(f"harrison_page_{i+1}.png")
print("Rendered 11 pages")
