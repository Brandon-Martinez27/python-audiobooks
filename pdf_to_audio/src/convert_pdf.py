import PyPDF2 as pdfr
import pyttsx3 as pts

def splitPdfPages(file):
    """Split pdf by page then reads text on each page."""
    return pdfr.PdfFileReader(open(file, "rb"))
