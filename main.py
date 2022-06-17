from gtts import gTTS
import PyPDF2
from playsound import playsound

text = ''
with open('code_rules.pdf', 'rb') as obj:
    pdfObj = PyPDF2.PdfFileReader(obj)
    # for i in range(pdfObj.numPages):
    pageObj = pdfObj.getPage(1)
    text += pageObj.extractText()

tts = gTTS(text, slow=True)
tts.save('txt.mp3')
playsound('txt.mp3')

