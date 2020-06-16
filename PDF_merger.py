import os
from PyPDF2 import PdfFileMerger

all_files = os.listdir()
pdfs = []
for each_file in all_files:
    if each_file.endswith(".pdf")>0:
        pdfs.append(each_file)

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()