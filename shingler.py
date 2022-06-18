import io
import redis
import numpy
import pickle
from io import StringIO
from configuration import path, width
import hashlib
import re
from itertools import permutations
import docxpy
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

con = redis.Redis('localhost')

# Извлечение текста из pdf
def pdfExtractor(path):
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
def docxExtractor(path):
    text = docxpy.process(path)
    return text

# Извлечение текста из txt
def txtExtractor(path):
        file = io.open(path, mode="r", encoding="utf-8")
        text = file.read()
        return text

# Функция извлечения текста
def extractor(path):
    type = path.split('.')[-1]
    text = ''
    if type == 'pdf':
        text = pdfExtractor(path)
    elif type == 'docx':
        text = docxExtractor(path)
    elif type == 'txt':
        text = txtExtractor(path)
    else:
        print('Необрабатываемый тип или неправильное имя')
    return text

# Форматирование текста для дальнейшей обработки с использованием регулярных выражений
def formatter(text):
    regex = re.compile('[\s.,!&\-«»()]|[0-9]')
    a = regex.sub(' ', text).lower().split(' ')
    a = list(filter(None, a))
    return a

def comparator(hash, previous):
    value = con.get(hash)
    if value != None:
        # print(previous, ' ', value.decode() == str(previous), ' ', value.decode())
        if value.decode() != str(previous):
            #print(value.decode())
            a = 1


# Разбиение текста на отдельные шинглы
def shingler(array, width):
    print(len(array))
    half = int(width / 2)
    old = []
    keval = {}
    for word in range(half, len(array) - half):
        shingle = []
        for i in range(-half, half + 1):
            shingle.append(array[word + i])

        permutated = list(permutations(shingle))
        for i in range(len(permutated)):
            unit = ''
            for place in permutated[i]:
                unit += place
            #con.set(hashstore(unit), str(shingle))
            keval.update({hashstore(unit): shingle + [word]})

            comparator(hashstore(unit), old)
            old = shingle
    return keval

# хеширование шинглов sha-1 алгоритмом
def hashstore(s):
    sum = hashlib.sha1()
    sum.update(str.encode(s))
    return sum.hexdigest()

# Словарь для хранения
dict = shingler(formatter(extractor(path)), width)
pdict = pickle.dumps(dict)


# con.set("Test", pdict)
#print((con.get("c9e4476626f039ad25addb634de6cf0816a7a596").decode()))

#print(dict)


# Преобразование исходного файла

# Comparator

# comparator('c9e4476626f039ad25addb634de6cf0816a7a596kaka')


