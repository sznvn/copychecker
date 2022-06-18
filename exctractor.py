#########################################
#
#   Модуль для извлечения текста        #
#
#########################################


import io
from io import StringIO

import docxpy

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


# Извлечение текста из pdf
def pdfExtract(path):
    output_string = StringIO()
    with open(path, 'rb') as file:
        parser = PDFParser(file)
        pdf = PDFDocument(parser)
        mgr = PDFResourceManager()
        device = TextConverter(mgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(mgr, device)
        for page in PDFPage.create_pages(pdf):
            interpreter.process_page(page)

    text = output_string.getvalue()
    return text

# Извлечение текста из docx
def docxExtract(path):
    text = docxpy.process(path)
    return text

# Извлечение текста из txt
def txtExtract(path):
        file = io.open(path, mode="r", encoding="utf-8")
        text = file.read()
        return text

# Функция извлечения текста
def extract(path):
    type = path.split('.')[-1]
    text = ''
    if type == 'pdf':
        text = pdfExtract(path)
    elif type == 'docx':
        text = docxExtract(path)
    elif type == 'txt':
        text = txtExtract(path)
    else:
        print('Необрабатываемый тип или неправильное имя')
    return text
