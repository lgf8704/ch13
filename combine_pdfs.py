import PyPDF2
import os


pdf_files = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf') and filename != "encrypted_minutes.pdf":
        print(filename)
        pdf_files.append(filename)

pdf_files.sort(key=str.lower)

for filename in pdf_files:
    print(filename)
    with open(filename, 'rb') as pdf_file:  
        with open("allminutes.pdf", 'ab+') as pdf_output_file:                      
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            pdf_writer = PyPDF2.PdfFileWriter()

            # 遍历pdf文件的页数（从0开始）,通过页数获取pdf某页，写入写的pdf对象
            for page_num in range(1, pdf_reader.numPages):
                # print(page_num)
                page_obj = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page_obj)                    
            pdf_writer.write(pdf_output_file)

print("Successful!")