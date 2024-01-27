import os
from pdf2docx import Converter
from pathlib import Path
from tkinter import messagebox as mb
import pytesseract

current_path = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(current_path, "input.pdf")
output = os.path.join(current_path)

def pdf_to_docx_and_extract_text(path, save_path):
    if Path(path).is_file() and (Path(path).suffix == ".pdf" or Path(path).suffix == ".PDF"):
        try:
            docx_file = os.path.splitext(os.path.basename(path))[0] + ".docx"
            cv = Converter(path)
            cv.convert(f"{save_path}/{docx_file}", start=0, end=None)
            cv.close()
            docx_path = f"{save_path}/{docx_file}"
            text = pytesseract.image_to_string(docx_path, lang="ben")
            print("Extracted text:")
            print(text)
        except Exception as ex:
            mb.showerror("ERROR", "File has not been decrypted")
    else:
        mb.showerror("INFO", "File not found!")

pdf_to_docx_and_extract_text(input, output)
