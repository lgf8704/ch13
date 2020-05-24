import PyPDF2


with open('meetingminutes.pdf', 'rb') as minutes_file:
    with open('watermark.pdf', 'rb') as watermark_file:
        with open('watermarked_cover.pdf', 'wb') as result_pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(minutes_file)
            watermark_reader = PyPDF2.PdfFileReader(watermark_file)           

            pdf_writer = PyPDF2.PdfFileWriter()            

            for page_num in range(1, pdf_reader.numPages):
                page_obj = pdf_reader.getPage(page_num)
                page_obj.mergePage(watermark_reader.getPage(0))
                pdf_writer.addPage(page_obj)

            pdf_writer.write(result_pdf_file)