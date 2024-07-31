import PyPDF2 as pdf
from PyPDF2 import PdfReader

# 1 - Version and Methods of PyPDF2
print(pdf.__version__)
print(dir(pdf))

# 2 - Import PDF file
file = open('../files/sample.pdf', 'rb')
reader = PdfReader(file)
print(reader)
info = reader.metadata

# 3 - Extracting some information
print(info.title)
print(info.author)
print(info.subject)
print(info.creator)
print(info.producer)
print(len(reader.pages))
print(reader.pages[0].extract_text())