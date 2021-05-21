import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))

watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_file.pdf', 'wb') as op_file:
        output.write(op_file)
        

# import sys

# inputs = sys.argv[1:]

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()

#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
    
#     merger.write('super.pdf')

# pdf_combiner(inputs)

# with open('python_pdfs/dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)
