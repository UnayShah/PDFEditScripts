import os

import PyPDF2

folder = input("Enter directory name: ")

filename1 = input("Enter name of 1st file: ")
filename1 = filename1 if filename1.endswith('.pdf') else filename1+".pdf"
filename2 = input("Enter name of 2nd file: ")
filename2 = filename2 if filename2.endswith('.pdf') else filename2+".pdf"

file1 = open(folder+"/"+filename1, 'rb')
file2 = open(folder+"/"+filename2, 'rb')

pdf_reader = PyPDF2.PdfFileReader(file1)

pdf_writer = PyPDF2.PdfFileWriter()

for pagenum in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(pagenum)
    pdf_writer.addPage(page)

pdf_reader = PyPDF2.PdfFileReader(file2)

for pagenum in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(pagenum)
    pdf_writer.addPage(page)

pdf_out = open(folder+"/"+"_merged.pdf", 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
file1.close()
file2.close()