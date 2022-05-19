import PyPDF2 as pdfr
import pyttsx3 as pts

def splitPdfPages(file):
    """Split pdf by page then reads text on each page."""
    return pdfr.PdfFileReader(open(file, "rb"))

def convertTextToSpeech(pdfReader):
    """Converts text to speech, loops the process for each page, 
    & finally stops the speaker
    """
    speaker = pts.init()
 
    for page_num in range(pdfReader.numPages):
        text = pdfReader.getPage(page_num).extractText()
        speaker.say(text)
        speaker.runAndWait()
    speaker.stop()
    return text, speaker

def saveFile(text, speaker):
    speaker.save_to_file(text, "artifacts/sample.mp3")
    speaker.runAndWait()
    return "Audio has been successfully recorded!"