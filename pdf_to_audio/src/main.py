import PyPDF2 as pdfr
import pyttsx3 as pts

from convert_pdf import *

pdfReader = splitPdfPages("pdf_to_audio/src/artifacts/sample.pdf")
text, speaker = convertTextToSpeech(pdfReader)
saveFile(text, speaker)
