import fitz
import pytesseract
from PIL import Image
import sys

doc = fitz.open("../bhu-reading-20260823/sources/rothman_ellis_1993_qjras34_201.pdf")
full_text = ""
for i in range(len(doc)):
    page = doc.load_page(i)
    pix = page.get_pixmap(dpi=300)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    text = pytesseract.image_to_string(img)
    full_text += f"\n--- Page {i+1} ---\n{text}"

with open("ocr_output.txt", "w") as f:
    f.write(full_text)
print("OCR done. Saved to ocr_output.txt")
