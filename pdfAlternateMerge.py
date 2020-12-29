import PyPDF2
import os

folder = input("Enter directory name: ")

filename1 = input("Enter name of 1st file: ")
filename1 = filename1 if filename1.endswith('.pdf') else filename1+".pdf"
filename2 = input("Enter name of 2nd file: ")
filename2 = filename2 if filename2.endswith('.pdf') else filename2+".pdf"

file1 = open(folder+"/"+filename1, 'rb')
file2 = open(folder+"/"+filename2, 'rb')

pdf_reader1 = PyPDF2.PdfFileReader(file1)
pdf_reader2 = PyPDF2.PdfFileReader(file2)

pdf_writer = PyPDF2.PdfFileWriter()

pageswritten = 0

for pagenum in range(min(pdf_reader1.getNumPages(), pdf_reader2.getNumPages())):
    page = pdf_reader1.getPage(pagenum)
    pdf_writer.addPage(page)
    page = pdf_reader2.getPage(pagenum)
    pdf_writer.addPage(page)
    pageswritten = pagenum

pdf_reader1 = pdf_reader1 if (pdf_reader1.getNumPages(
) > pdf_reader2.getNumPages()) else pdf_reader2

for pagenum in range(pdf_reader1.getNumPages() - pageswritten):
    page = pdf_reader1.getPage(pagenum + pageswritten)
    pdf_writer.addPage(page)

pdf_out = open(folder+"/"+"_merged.pdf", 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
file1.close()
file2.close()
