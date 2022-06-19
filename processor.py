#########################################
#
#   Модуль для обработки текста         #
#
#########################################
import re
import hashlib
from configuration import width
from itertools import permutations

def hashstore(s):
    sum = hashlib.sha1()
    sum.update(str.encode(s))
    return sum.hexdigest()

# def comparator(hash, previous):
#     value = con.get(hash)
#     if value != None:
#         # print(previous, ' ', value.decode() == str(previous), ' ', value.decode())
#         if value.decode() != str(previous):
#             #print(value.decode())
#             a = 1

# Форматирование текста для дальнейшей обработки с использованием регулярных выражений
def format(text):
    regex = re.compile('[\s.,`!&\-«»()]|[0-9]')
    words = '`' + re.sub(regex, '`', text)
    place = []
    for i in range(len(words)-1):
        if words[i+1] != '`' and words[i]=='`':
            place.append(i)
    words = list(filter(None, words.lower().split('`')))
    return words, place

# Это нужно оптимизировать
def shingler(array):
    # print(len(array))
    half = int(width / 2)
    keval = {}
    val = []
    for word in range(half, len(array) - half):
        shingle = []
        unit = ''
        for i in range(-half, half + 1):
            shingle.append(array[word + i])
            unit += array[word + i]
        keval.update({hashstore(unit): shingle})

    return keval