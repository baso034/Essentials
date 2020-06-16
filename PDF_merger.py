import os
from PyPDF2 import PdfFileMerger
import sys

all_files = os.listdir()
pdfs = []
for each_file in all_files:
    if each_file.endswith(".pdf")>0:
        pdfs.append(each_file)
if len(pdfs)==0:
    sys.exit()
    
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()

#Thanks For Using the code