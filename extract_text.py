import PyPDF2
import docx


with open('学员健康档案港澳--李一一.pdf', 'rb') as pdf_file:
    with open("学员健康档案港澳--李一一.docx", 'wb') as docx_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        page_obj = pdf_reader.getPage(0)

        text = page_obj.extractText()
        docx_file.write(text.encode('utf-8'))