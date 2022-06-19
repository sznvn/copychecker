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
    words = list(filter(None, words.split('`')))
    return words, place

# Это нужно оптимизировать
def shingler(array):
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

            ###################
            for place in permutated[i]:
                unit += place
            #con.set(hashstore(unit), str(shingle))
            # keval.update({hashstore(unit): shingle + [word]})
            keval.update({hashstore(unit): shingle})
            # comparator(hashstore(unit), old)
            old = shingle
    return keval