import PyPDF2


# 打开两个pdf文件，打开一个合并后的文件
with open('meetingminutes.pdf', 'rb') as pdf1_file:
    with open('rotatedPage.pdf', 'wb') as result_pdf_file:            
        pdf1_reader = PyPDF2.PdfFileReader(pdf1_file)
        page = pdf1_reader.getPage(0)
        page.rotateClockwise(90)
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(page)
        
        pdf_writer.write(result_pdf_file)