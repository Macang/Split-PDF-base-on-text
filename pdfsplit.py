import pdfplumber
from PyPDF2 import PdfFileWriter,PdfFileReader
import re
object = PdfFileReader("*.pdf")
with pdfplumber.open("*.pdf") as pdf:
    start = 0
    pages = []
    final = [] 
    splitnum = []
    first_page = pdf.pages[0]
    target = "your target text"
    NumPages = object.getNumPages()
    end = []
    end.append(object.getNumPages())
    for i in range(0, NumPages):
        PageObj = pdf.pages[i]
        Text = PageObj.extract_text() 
        ResSearch = re.search(target, Text)
        if type(ResSearch) == re.Match:
            splitnum.append(i)
    splitnum.extend(end)
    splitnum.remove(0)
    for point in splitnum:
        list.clear(final)
        output = PdfFileWriter()
        for a in range (start,point):
            pages.append(a)
            final.extend(pages)
            list.clear(pages)
            start=point
            newfile = str(point) + ".pdf"
            output.addPage(object.getPage(a))
            with open(newfile, "wb") as outputStream:
                output.write(outputStream)