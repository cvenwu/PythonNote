import PyPDF2
pdfFileObj = open('../../工程实验室2019年硕士研究生复试结果.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
print(pdfReader.getPage(0).extractText())
print(type(pdfReader.getPage(0).extractText()))
print(pdfReader.isEncrypted)    # 查看PDF是否加密

