import PyPDF2


with open("meetingminutes.pdf", 'rb') as pdf_file:
    with open("encrypted_minutes.pdf", 'wb') as result_pdf:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        pdf_writer = PyPDF2.PdfFileWriter()

        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

        pdf_writer.encrypt("fight for freedom")
        pdf_writer.write(result_pdf)