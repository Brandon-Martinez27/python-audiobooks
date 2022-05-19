import PyPDF2 as pdfr
import pyttsx3 as pts


# Split pdf by page then reads text on each page
pdfReader = pdfr.PdfFileReader(open("artifacts/sample.pdf", "rb"))

# Converts text to speech
speaker = pts.init()

# Loop the process for each page, stops the speaker
for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

# Save the audio as an mp3 file
speaker.save_to_file(text, "artifacts/sample.mp3")
speaker.runAndWait()