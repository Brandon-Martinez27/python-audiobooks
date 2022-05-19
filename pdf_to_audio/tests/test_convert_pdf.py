import pdf_to_audio.src.convert_pdf as c
import sys
import os

def test_splitPdfPages():
    c.splitPdfPages("pdf_to_audio/src/artifacts/sample.pdf")