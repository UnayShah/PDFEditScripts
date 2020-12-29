import PyPDF2
import os

folder = input("Enter directory name: ")
files = []
for (dirpath, dirnames, filenames) in os.walk(folder):
    for filename in filenames:
        if(str(filename).endswith(".pdf")):
            files.append(dirpath+"/"+filename)

for f in files:
    pdf_in = open(f)
    pdf_reader = PyPDF2.PdfFileReader(f)
    pdf_writer = PyPDF2.PdfFileWriter()

    for pagenum in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(pagenum)
        if pagenum % 2:
            page.rotateClockwise(180)
        pdf_writer.addPage(page)

    pdf_out = open(str(pdf_in.name).replace('.pdf', '') + '_rotated.pdf', 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()
