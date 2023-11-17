# pdfReader.py

from PyPDF2 import PdfReader

reader = PdfReader("../pdf/novel1.pdf")

total_pages = len(reader.pages)
print("total_pages : ", total_pages)

for page_num in range(total_pages) :

    # 페이지별 추출된 문자를 text 변수에 저장
    text = reader.pages[page_num].extract_text()
    print(text)

