# pdfReaderTTS.py

from  PyPDF2 import PdfReader
import pyttsx3

# tts 사용하기 위해 선언
tts = pyttsx3.init()

reader = PdfReader("../pdf/novel1.pdf")

total_pages = len(reader.pages)
print("total_pages : ", total_pages)

for page_num in range(total_pages) :

    text = reader.pages[page_num].extract_text()

    print(text)

    tts.setProperty("rate", 300)
    tts.say(text)
    tts.runAndWait()

tts.stop()

