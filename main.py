import subprocess
import PyPDF2
from tkinter.filedialog import askopenfilename
from tkinter import Tk

# Initialize Tkinter root window
root = Tk()
root.withdraw()  # Hide the root window

book = askopenfilename(filetypes=[("PDF files", "*.pdf")])
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    if text:
        subprocess.run(["say", text])

