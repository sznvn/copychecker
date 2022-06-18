#########################################
#
#   Модуль для обработки текста         #
#
#########################################
import re

# Форматирование текста для дальнейшей обработки с использованием регулярных выражений
def format(text):
    regex = re.compile('[\s.,`!&\-«»()]|[0-9]')
    words = '`' + re.sub(regex, '`', text)
    place = []
    for i in range(len(words)-1):
        if words[i+1] != '`' and words[i]=='`':
            place.append(i)
    #words = regex.sub(' ', text).lower()#.split(' ')
    #words = list(filter(None, words))
    print(place)
    return words