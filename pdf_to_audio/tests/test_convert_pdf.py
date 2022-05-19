import pdf_to_audio.src.convert_pdf as c

def test_splitPdfPages():
    pdfReader = c.splitPdfPages("pdf_to_audio/src/artifacts/sample.pdf")
    return pdfReader

def test_convertTextToSpeech():
    text, speaker = c.convertTextToSpeech(test_splitPdfPages())
    return text, speaker

def test_saveFile():
    c.saveFile(text, speaker)